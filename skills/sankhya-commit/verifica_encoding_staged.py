#!/usr/bin/env python3
"""Verifica o encoding dos arquivos de texto staged antes do commit.

Camadas:
  1. Caractere (qualquer arquivo de texto): U+FFFD e mistura de encodings no mesmo
     arquivo são ERRO; mojibake é AVISO.
  2. Política do projeto: charset declarado no .editorconfig para o caminho do arquivo.
     Sem charset declarado, só os tipos Sankhya têm padrão embutido (Java em Latin-1,
     Kotlin em UTF-8, XML de artefato Sankhya em Latin-1). Divergência é ERRO nos tipos
     Sankhya e AVISO nos demais.
  3. Comparação com o HEAD: arquivo que mudou de encoding (Latin-1 <-> UTF-8) é AVISO.

O conteúdo lido é sempre o do índice (git show :caminho), nunca o do disco.

Uso:  python verifica_encoding_staged.py [--repo CAMINHO]
Saída: lista de achados; código de saída 1 se houver ERRO.
Limitação do .editorconfig: cobre *, **, ?, {a,b} e "última seção que casa vence", só a
propriedade charset (latin1/iso-8859-1/utf-8). Não cobre classes [abc] nem {1..3}.
"""
import os
import re
import subprocess
import sys
from collections import namedtuple

ERRO = 'ERRO'
AVISO = 'AVISO'

LATIN1 = 'latin-1'
UTF8 = 'utf-8'
MISTO = 'misto'
ASCII = 'ascii'

CODIGO_SAIDA_ERRO = 1
LIMITE_ASCII = 127
BYTE_NULO = b'\x00'
BYTES_CARACTERE_SUBSTITUICAO = b'\xef\xbf\xbd'
ARQUIVO_EDITORCONFIG = '.editorconfig'

EXTENSOES_BINARIAS = {
    '.jar', '.zip', '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.exe', '.class', '.xls', '.xlsx',
    '.doc', '.docx', '.pptx', '.woff', '.woff2', '.ttf', '.eot', '.jasper', '.bin', '.dll', '.so', '.gz',
    '.7z', '.rar', '.mp4',
}
PASTAS_XML_SANKHYA = {'datadictionary', 'dbscripts', 'dbquerys', 'dashboards'}
CHARSET_PADRAO_POR_EXTENSAO = {'.java': LATIN1, '.kt': UTF8}
CHARSET_PADRAO_XML_SANKHYA = LATIN1
CHARSETS_LATIN1 = {'latin1', 'iso-8859-1'}
CHARSETS_UTF8 = {'utf-8', 'utf8'}

MOJIBAKE_EM_LATIN1 = re.compile(rb'\xc3[\x80-\xbf]')
MOJIBAKE_EM_UTF8 = re.compile('Ã[\u0080-¿]|Â[ -¿]')

Achado = namedtuple('Achado', 'severidade caminho mensagem')


def executar_git(raiz, *argumentos):
    """Executa o git em bytes (sem passar por pipe de texto). Retorna None se o comando falhar."""
    resultado = subprocess.run(['git', '-C', raiz] + list(argumentos), capture_output=True)
    if resultado.returncode != 0:
        return None
    return resultado.stdout


def listar_arquivos_staged(raiz):
    saida = executar_git(raiz, 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z') or b''
    return [nome.decode('utf-8', 'replace') for nome in saida.split(b'\0') if nome]


def classificar_encoding(conteudo):
    """Retorna 'ascii', 'utf-8', 'latin-1' ou 'misto' (linhas UTF-8 válidas e inválidas no mesmo arquivo)."""
    linhas_utf8 = linhas_latin1 = 0
    for linha in conteudo.split(b'\n'):
        if not any(byte > LIMITE_ASCII for byte in linha):
            continue
        try:
            linha.decode('utf-8')
            linhas_utf8 += 1
        except UnicodeDecodeError:
            linhas_latin1 += 1
    if linhas_utf8 and linhas_latin1:
        return MISTO
    if linhas_utf8:
        return UTF8
    if linhas_latin1:
        return LATIN1
    return ASCII


def glob_para_regex(glob):
    glob = glob.lstrip('/')
    if '/' not in glob:
        glob = '**/' + glob
    regex, i = '', 0
    while i < len(glob):
        if glob.startswith('**/', i):
            regex += '(?:.*/)?'
            i += 3
            continue
        if glob.startswith('**', i):
            regex += '.*'
            i += 2
            continue
        caractere = glob[i]
        if caractere == '*':
            regex += '[^/]*'
        elif caractere == '{':
            fim = glob.index('}', i)
            regex += '(?:' + '|'.join(re.escape(parte) for parte in glob[i + 1:fim].split(',')) + ')'
            i = fim
        elif caractere == '?':
            regex += '[^/]'
        else:
            regex += re.escape(caractere)
        i += 1
    return re.compile('^' + regex + '$')


def ler_secoes_editorconfig(raiz):
    """Lista de (regex_do_glob, charset) na ordem do arquivo; a última seção que casa vence."""
    caminho = os.path.join(raiz, ARQUIVO_EDITORCONFIG)
    if not os.path.isfile(caminho):
        return []
    secoes, glob = [], None
    with open(caminho, encoding='utf-8', errors='replace') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            cabecalho = re.match(r'^\[(.+)\]$', linha)
            if cabecalho:
                glob = cabecalho.group(1)
                continue
            charset = re.match(r'^charset\s*=\s*(\S+)', linha, re.I)
            if charset and glob:
                secoes.append((glob_para_regex(glob), charset.group(1).lower()))
    return secoes


def normalizar_charset(charset):
    if charset in CHARSETS_LATIN1:
        return LATIN1
    if charset in CHARSETS_UTF8:
        return UTF8
    return None


def eh_tipo_sankhya(caminho):
    extensao = os.path.splitext(caminho)[1].lower()
    if extensao in CHARSET_PADRAO_POR_EXTENSAO:
        return True
    pastas = {pasta.lower() for pasta in caminho.split('/')[:-1]}
    return extensao == '.xml' and bool(pastas & PASTAS_XML_SANKHYA)


def charset_padrao(caminho):
    extensao = os.path.splitext(caminho)[1].lower()
    if extensao in CHARSET_PADRAO_POR_EXTENSAO:
        return CHARSET_PADRAO_POR_EXTENSAO[extensao]
    return CHARSET_PADRAO_XML_SANKHYA if eh_tipo_sankhya(caminho) else None


def charset_esperado(caminho, secoes):
    declarado = None
    for regex, charset in secoes:
        if regex.match(caminho):
            declarado = charset
    return normalizar_charset(declarado) if declarado else charset_padrao(caminho)


def verificar_caracteres(caminho, conteudo, classe):
    achados = []
    quantidade = conteudo.count(BYTES_CARACTERE_SUBSTITUICAO)
    if quantidade:
        achados.append(Achado(ERRO, caminho, 'U+FFFD x%d (caractere perdido; não recuperável a partir do arquivo)' % quantidade))
    if classe == MISTO:
        achados.append(Achado(ERRO, caminho, 'encodings misturados no mesmo arquivo (linhas UTF-8 e Latin-1)'))
    if classe == LATIN1 and MOJIBAKE_EM_LATIN1.search(conteudo):
        achados.append(Achado(AVISO, caminho, 'possível mojibake (sequência C3 xx em arquivo Latin-1)'))
    if classe == UTF8 and MOJIBAKE_EM_UTF8.search(conteudo.decode('utf-8')):
        achados.append(Achado(AVISO, caminho, 'possível mojibake (UTF-8 lido como Latin-1 e regravado)'))
    return achados


def verificar_politica(caminho, classe, secoes):
    esperado = charset_esperado(caminho, secoes)
    divergente = (esperado == LATIN1 and classe == UTF8) or (esperado == UTF8 and classe == LATIN1)
    if not divergente:
        return []
    severidade = ERRO if eh_tipo_sankhya(caminho) else AVISO
    return [Achado(severidade, caminho, 'política do projeto espera %s, mas o arquivo está em %s' % (esperado, classe))]


def verificar_mudanca_vs_head(raiz, caminho, classe):
    anterior = executar_git(raiz, 'show', 'HEAD:' + caminho)
    if not anterior:
        return []
    classe_anterior = classificar_encoding(anterior)
    classes_comparaveis = {UTF8, LATIN1}
    if classe_anterior in classes_comparaveis and classe in classes_comparaveis and classe_anterior != classe:
        return [Achado(AVISO, caminho, 'encoding mudou em relação ao HEAD (%s -> %s)' % (classe_anterior, classe))]
    return []


def verificar_arquivo(raiz, caminho, secoes):
    if os.path.splitext(caminho)[1].lower() in EXTENSOES_BINARIAS:
        return []
    conteudo = executar_git(raiz, 'show', ':' + caminho)
    if conteudo is None or BYTE_NULO in conteudo:
        return []
    classe = classificar_encoding(conteudo)
    return (verificar_caracteres(caminho, conteudo, classe)
            + verificar_politica(caminho, classe, secoes)
            + verificar_mudanca_vs_head(raiz, caminho, classe))


def verificar_staged(raiz):
    secoes = ler_secoes_editorconfig(raiz)
    achados = []
    for caminho in listar_arquivos_staged(raiz):
        achados.extend(verificar_arquivo(raiz, caminho, secoes))
    return achados


def obter_raiz(argumentos):
    if '--repo' in argumentos:
        return argumentos[argumentos.index('--repo') + 1]
    return os.getcwd()


def principal(argumentos):
    try:
        achados = verificar_staged(obter_raiz(argumentos))
    except Exception as erro:
        print('AVISO verificação de encoding não executada: %s' % erro)
        return 0
    for severidade in (ERRO, AVISO):
        for achado in achados:
            if achado.severidade == severidade:
                print('%-5s %s: %s' % (achado.severidade, achado.caminho, achado.mensagem))
    if not achados:
        print('Encoding OK.')
    return CODIGO_SAIDA_ERRO if any(achado.severidade == ERRO for achado in achados) else 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(principal(sys.argv[1:]))
