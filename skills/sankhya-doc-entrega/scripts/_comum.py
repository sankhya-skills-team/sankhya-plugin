"""Utilitarios compartilhados entre gerar_html.py e gerar_docx.py.

Cuida de: leitura do JSON de entrada, versionamento/backup do documento
anterior e historico de versoes. Sem dependencias externas.
"""

import json
import os
import re
import subprocess
import sys
from datetime import date

HISTORICO = ".historico-entregas.json"


# ── Entrada ────────────────────────────────────────────────────────

def carregar_dados(argv):
    """Le o JSON de entrada informado na linha de comando."""
    if len(argv) < 2:
        sys.exit("uso: python %s <dados.json>" % os.path.basename(argv[0]))
    with open(argv[1], encoding="utf-8") as f:
        return json.load(f)


def garantir(modulo, pacote=None):
    """Importa um modulo, instalando o pacote via pip se necessario.

    Usa sys.executable -m pip para funcionar em Windows, Linux e venv.
    """
    try:
        return __import__(modulo)
    except ImportError:
        pass
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet",
                           pacote or modulo])
    return __import__(modulo)


# ── Versionamento ──────────────────────────────────────────────────

def _caminho_historico(pasta):
    return os.path.join(pasta, HISTORICO)


def _ler_historico(pasta):
    caminho = _caminho_historico(pasta)
    if not os.path.exists(caminho):
        return {}
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, OSError):
        # historico corrompido nao pode impedir a geracao do documento
        return {}


def _gravar_historico(pasta, historico):
    with open(_caminho_historico(pasta), "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def resolver_versao(arquivo_saida, changelog):
    """Determina a versao, faz backup do documento anterior e registra o historico.

    Retorna (versao, backup_ou_None, lista_historico) onde lista_historico ja
    inclui a entrada da versao atual, mais recente primeiro.
    """
    pasta = os.path.dirname(arquivo_saida)
    os.makedirs(pasta, exist_ok=True)
    base, ext = os.path.splitext(os.path.basename(arquivo_saida))
    historico = _ler_historico(pasta)
    chave = base + ext            # a chave separa .html de .docx do mesmo modulo
    entradas = historico.get(chave, [])

    backup = None
    if os.path.exists(arquivo_saida):
        anterior = entradas[0]["versao"] if entradas else _versao_no_arquivo(arquivo_saida)
        major, minor = (int(p) for p in anterior.split("."))
        versao = "%d.%d" % (major, minor + 1)
        backup = os.path.join(pasta, "%s v%s%s" % (base, anterior, ext))
        if os.path.exists(backup):
            os.remove(backup)
        os.rename(arquivo_saida, backup)
    else:
        versao = "1.0"

    entradas.insert(0, {
        "versao": versao,
        "data": date.today().strftime("%d/%m/%Y"),
        "alteracoes": list(changelog) if changelog else
                      (["Primeira versão do documento."] if versao == "1.0" else []),
    })
    historico[chave] = entradas
    _gravar_historico(pasta, historico)
    return versao, backup, entradas


def _versao_no_arquivo(caminho):
    """Fallback quando o sidecar de historico nao existe (docs gerados antes)."""
    if caminho.lower().endswith(".docx"):
        try:
            from docx import Document
            v = Document(caminho).core_properties.version
            if v and re.match(r"^\d+\.\d+$", v):
                return v
        except Exception:
            pass
        return "1.0"
    try:
        with open(caminho, encoding="utf-8") as f:
            cabecalho = f.read(4000)
    except OSError:
        return "1.0"
    m = re.search(r'name="doc-versao"\s+content="(\d+\.\d+)"', cabecalho)
    return m.group(1) if m else "1.0"


# ── Formatacao ─────────────────────────────────────────────────────

def parse_personas(itens):
    """Aceita ['Nome — Funcao', ...] ou [{'nome':..,'funcao':..}, ...]."""
    pessoas = []
    for item in itens or []:
        if isinstance(item, dict):
            pessoas.append({"nome": item.get("nome", ""),
                            "funcao": item.get("funcao", "")})
            continue
        linha = str(item).strip()
        if not linha:
            continue
        for sep in ("—", "–", " - "):
            if sep in linha:
                nome, funcao = linha.split(sep, 1)
                pessoas.append({"nome": nome.strip(), "funcao": funcao.strip()})
                break
        else:
            pessoas.append({"nome": linha, "funcao": ""})
    return pessoas
