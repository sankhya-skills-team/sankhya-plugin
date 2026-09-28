"""Organiza o snapshot site/*.md em references/design-system/ (um arquivo por componente/página).

Uso: python organizar.py <pasta_site> <pasta_destino> <data_snapshot>
"""
import glob
import os
import re
import sys

LINK_INTERNO = re.compile(r'\[([^\]]*)\]\((/docs/[^)]*|/img/[^)]*)\)')
IMAGEM_VAZIA = re.compile(r'^\s*\[\]\([^)]*\)\s*$')
BLOCO_GRAPH = re.compile(r'#### Graph\s*\n+```[^\n]*\n.*?```\n?', re.S)
LINHAS_EM_BRANCO = re.compile(r'\n{3,}')

# prefixo no site -> pasta no destino
MAPA_SECOES = [
    ('components/components-doc/', 'componentes/'),
    ('components/sankhya-erp-componentes/', 'componentes/'),
    ('components/layout-doc/acorde/', 'layout/acorde-'),
    ('components/layout-doc/', 'layout/'),
    ('components/getting-started/', 'setup/'),
    ('onboarding/onboarding/', 'setup/onboarding-'),
    ('utilities/components/', 'core/guias/'),
    ('utilities/api/', 'core/'),
    ('api-java/sankhya-bff/', 'api-java/'),
    ('api-java/', 'api-java/'),
]

# índices do site que viram o índice gerado da skill
IGNORADOS = {'components/components-doc', 'components/sankhya-erp-componentes', 'utilities/api'}


def destino_relativo(rel):
    for prefixo, pasta in MAPA_SECOES:
        if rel.startswith(prefixo):
            return pasta + rel[len(prefixo):] + '.md'
    if rel == 'components/layout-doc/acorde':
        return 'layout/acorde.md'
    raise ValueError(f'Seção não mapeada: {rel}')


def limpar(conteudo, data_snapshot):
    url, corpo = conteudo.split('\n', 1)
    url = url.removeprefix('<!-- ').removesuffix(' -->').strip()
    corpo = BLOCO_GRAPH.sub('', corpo)
    linhas = [l.rstrip() for l in corpo.split('\n')
              if l.strip() not in ('* * *', 'Nesta página') and not IMAGEM_VAZIA.match(l)]
    corpo = LINK_INTERNO.sub(r'\1', '\n'.join(linhas))
    corpo = LINHAS_EM_BRANCO.sub('\n\n', corpo).strip()
    return f'> Fonte oficial: {url} (snapshot {data_snapshot})\n\n{corpo}\n'


TAMANHO_MAX_DESCRICAO = 140

TITULOS_SECOES = [
    ('componentes/ez-', 'Componentes ez- (UI genérica, `@sankhyalabs/ezui`)'),
    ('componentes/snk-', 'Componentes snk- (EIP, `@sankhyalabs/sankhyablocks`)'),
    ('layout/', 'Layout e tokens Acorde'),
    ('setup/', 'Setup e onboarding'),
    ('core/guias/', 'Core — guias (`@sankhyalabs/core`)'),
    ('core/classes/', 'Core — classes'),
    ('core/interfaces/', 'Core — interfaces'),
    ('core/enumerations/', 'Core — enums'),
    ('core/', 'Core — funções, tipos, variáveis e namespaces'),
    ('api-java/', 'API Java (sankhya-bff / sanmodule)'),
]


def titulo_e_descricao(conteudo):
    linhas = conteudo.split('\n')
    titulo = next((l[2:].strip() for l in linhas if l.startswith('# ')), '')
    inicio = next((i for i, l in enumerate(linhas) if l.startswith('# ')), 0)
    descricao = next((l.strip() for l in linhas[inicio + 1:]
                      if len(l.strip()) >= 40 and '.ts:' not in l
                      and not l.startswith(('#', '```', '|', '>', '@', '*', '`'))), '')
    if len(descricao) > TAMANHO_MAX_DESCRICAO:
        descricao = descricao[:TAMANHO_MAX_DESCRICAO].rsplit(' ', 1)[0] + '…'
    return titulo, descricao.replace('|', '/')


def secao_do_arquivo(rel):
    return next(titulo for prefixo, titulo in TITULOS_SECOES if rel.startswith(prefixo))


def gerar_indice(pasta_destino, data_snapshot):
    grupos = {titulo: [] for _, titulo in TITULOS_SECOES}
    for caminho in sorted(glob.glob(os.path.join(pasta_destino, '**', '*.md'), recursive=True)):
        rel = os.path.relpath(caminho, pasta_destino).replace(os.sep, '/')
        if rel == 'INDICE.md':
            continue
        with open(caminho, encoding='utf-8') as f:
            titulo, descricao = titulo_e_descricao(f.read())
        grupos[secao_do_arquivo(rel)].append(f'| `{rel}` | {titulo} | {descricao} |')
    partes = [f'# Índice gerado — Design System (snapshot {data_snapshot})\n',
              'Gerado por `scripts/atualizar-design-system/`. Não editar à mão.\n']
    for titulo, linhas in grupos.items():
        partes += [f'\n## {titulo}\n', '| Arquivo | Título | Resumo |', '|---|---|---|', *linhas]
    with open(os.path.join(pasta_destino, 'INDICE.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(partes) + '\n')


def main(pasta_site, pasta_destino, data_snapshot):
    total = 0
    for origem in glob.glob(os.path.join(pasta_site, '**', '*.md'), recursive=True):
        rel = os.path.relpath(origem, pasta_site)[:-3].replace(os.sep, '/')
        if rel in IGNORADOS:
            continue
        saida = os.path.join(pasta_destino, destino_relativo(rel))
        os.makedirs(os.path.dirname(saida), exist_ok=True)
        with open(origem, encoding='utf-8') as f:
            conteudo = limpar(f.read(), data_snapshot)
        with open(saida, 'w', encoding='utf-8', newline='\n') as f:
            f.write(conteudo)
        total += 1
    gerar_indice(pasta_destino, data_snapshot)
    print(f'{total} arquivos gerados em {pasta_destino}')


if __name__ == '__main__':
    main(*sys.argv[1:4])
