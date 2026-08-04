"""Lint de linguagem do dados.json — barra marcas de texto gerado por IA.

Uso: python revisar_texto.py <dados.json>
Sai com codigo 1 quando encontra ocorrencia; 0 quando esta limpo.

Cobre so o que regex pega com seguranca. O resto (regra de tres, elegant
variation, prosa sem sujeito) esta em references/linguagem.md e depende de
leitura humana. Ver tambem: python revisar_texto.py --autoteste
"""

import json
import os
import re
import sys

# ── Campos de prosa ────────────────────────────────────────────────
# Allowlist explicita: campos de identificacao (caminho_sistema, classe,
# arquivo, entidade) usam travessao e simbolos de propriedade e ficam de fora.
CAMPOS_FUNCIONALIDADE = ("titulo", "obs", "limitacoes")
CAMPOS_TESTE = ("nome", "esperado")
CAMPOS_CHECKLIST = ("descricao", "observacao")


def coletar(dados):
    """Devolve [(caminho, texto)] de todos os campos de prosa."""
    itens = []

    def add(caminho, valor):
        if isinstance(valor, str) and valor.strip():
            itens.append((caminho, valor))

    add("objetivo", dados.get("objetivo"))
    for i, lim in enumerate(dados.get("limitacoes_gerais") or []):
        add("limitacoes_gerais[%d]" % i, lim)

    for i, func in enumerate(dados.get("funcionalidades") or []):
        base = "funcionalidades[%d]" % i
        for campo in CAMPOS_FUNCIONALIDADE:
            add("%s.%s" % (base, campo), func.get(campo))
        for j, passo in enumerate(func.get("passos") or []):
            add("%s.passos[%d]" % (base, j), passo)
        for j, teste in enumerate(func.get("testes") or []):
            for campo in CAMPOS_TESTE:
                add("%s.testes[%d].%s" % (base, j, campo), teste.get(campo))

    checklist = dados.get("checklist_deploy") or {}
    for grupo in ("pre_requisitos", "pos_deploy"):
        for i, item in enumerate(checklist.get(grupo) or []):
            for campo in CAMPOS_CHECKLIST:
                add("checklist_deploy.%s[%d].%s" % (grupo, i, campo), item.get(campo))

    return itens


# ── Regras ─────────────────────────────────────────────────────────

GERUNDIOS = (
    "garantindo|permitindo|possibilitando|assegurando|mantendo|evidenciando|"
    "refletindo|contribuindo|proporcionando|otimizando|facilitando|abrangendo|"
    "destacando|reforçando|ampliando|melhorando|viabilizando|consolidando|"
    "demonstrando|ressaltando|agregando|potencializando"
)

INFLADO = (
    "robusto|robusta|robustos|robustas|eficiente|eficientes|otimizado|otimizada|"
    "poderoso|poderosa|inovador|inovadora|abrangente|abrangentes|vasto|vasta|"
    "crucial|cruciais|primordial|imprescindível|inviável de ignorar|"
    "de forma transparente|de maneira eficaz|de forma eficaz|solução completa|"
    "papel fundamental|ponto crucial|vale ressaltar|vale destacar|cabe destacar|"
    "é importante destacar|é importante ressaltar|de ponta"
)

COPULA = "serve como|servem como|atua como|atuam como|configura-se como|apresenta-se como|constitui-se"

# Cada regra: (nome, regex, dica)
REGRAS = [
    ("travessao", re.compile(r"[—–]|(?<= )--(?= )"),
     "Troque por ponto, vírgula, dois-pontos ou parênteses."),
    ("gerundio", re.compile(r",\s*(?:%s)\b[^.!?;]*(?:[.!?]|$)" % GERUNDIOS, re.IGNORECASE),
     "Oração de gerúndio no fim da frase. Corte ou vire frase própria com sujeito."),
    ("inflado", re.compile(r"\b(?:%s)\b" % INFLADO, re.IGNORECASE),
     "Vocabulário de propaganda. Descreva o que o código faz."),
    ("copula", re.compile(r"\b(?:%s)\b" % COPULA, re.IGNORECASE),
     "Fuga do verbo 'ser'. Use 'é' direto."),
    ("negativa", re.compile(r"não (?:apenas|só|somente)\b[^.!?]{0,80}?\bmas\b", re.IGNORECASE),
     "Paralelismo negativo. Afirme direto o que a funcionalidade faz."),
    ("negrito", re.compile(r"\*\*[^*]+\*\*"),
     "O renderizador já define a hierarquia visual. Tire o markdown."),
]

# Mensagens de sistema citadas sao verbatim do fonte e nao entram no lint.
CITACAO = re.compile(r'"[^"]*"|“[^”]*”')


def analisar(caminho, texto):
    limpo = CITACAO.sub(lambda m: " " * len(m.group(0)), texto)
    achados = []
    for nome, regex, dica in REGRAS:
        for m in regex.finditer(limpo):
            achados.append((caminho, nome, dica, trecho(texto, m.start(), m.end())))
    return achados


def trecho(texto, ini, fim, margem=28):
    a = max(0, ini - margem)
    b = min(len(texto), fim + margem)
    return ("..." if a else "") + texto[a:b].replace("\n", " ") + ("..." if b < len(texto) else "")


# ── Saida ──────────────────────────────────────────────────────────

def relatar(achados):
    if not achados:
        print("Linguagem OK - nenhuma marca de texto gerado por IA.")
        print("Confira ainda a mao: regra de tres, sinonimos alternados, passo sem sujeito.")
        return 0

    atual = None
    dicas = {}
    for caminho, nome, dica, excerto in achados:
        if caminho != atual:
            print("\n%s" % caminho)
            atual = caminho
        print("  %-10s %s" % (nome, excerto))
        dicas[nome] = dica

    print("\n%d ocorrencia(s). Corrija antes de gerar." % len(achados))
    print("\nComo corrigir:")
    for nome, dica in sorted(dicas.items()):
        print("  %-10s %s" % (nome, dica))
    print("\nDetalhes e exemplos: references/linguagem.md")
    return 1


# ── Autoteste ──────────────────────────────────────────────────────

def autoteste():
    sujo = {
        "objetivo": "A rotina — central no processo — grava o registro, garantindo a integridade.",
        "caminho_sistema": "Menu › Compras — Cotação",   # fora do lint, tem travessao legitimo
        "limitacoes_gerais": ["O módulo serve como base robusta para o fluxo."],
        "funcionalidades": [{
            "titulo": "Cancelar",
            "obs": "Não apenas valida o status, mas também **bloqueia** a ação.",
            "passos": ["O sistema grava o registro."],
            "testes": [{"nome": "Executar com status válido",
                        "esperado": 'Sistema bloqueia com: "Situação — inválida!"'}],
        }],
        "checklist_deploy": {"pre_requisitos": [
            {"tipo": "parametro", "nome": "X", "descricao": "Parâmetro eficiente.",
             "classe": "br.com.a — b"},
        ]},
    }
    achados = [a for c, t in coletar(sujo) for a in analisar(c, t)]
    tipos = sorted({nome for _c, nome, _d, _e in achados})
    assert tipos == ["copula", "gerundio", "inflado", "negativa", "negrito", "travessao"], tipos

    caminhos = {c for c, _n, _d, _e in achados}
    assert "caminho_sistema" not in caminhos, "campo de identificacao nao deve ser lintado"
    assert not any("testes[0].esperado" in c for c in caminhos), \
        "travessao dentro de mensagem citada nao deve acusar"
    assert "funcionalidades[0].passos[0]" not in caminhos, "passo limpo acusou"

    limpo = {
        "objetivo": "O módulo grava o registro da cotação. O status passa a Pendente.",
        "funcionalidades": [{"titulo": "Cancelar Cotação", "obs": "Exige a permissão de cancelamento.",
                             "passos": ["O usuário seleciona a cotação."], "testes": []}],
    }
    assert not [a for c, t in coletar(limpo) for a in analisar(c, t)], "falso positivo em texto limpo"
    print("autoteste OK - 6 regras acusam, campos de identificacao e citacoes preservados.")
    return 0


# ── Main ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if "--autoteste" in sys.argv:
        sys.exit(autoteste())
    if len(sys.argv) < 2:
        sys.exit("uso: python %s <dados.json> | --autoteste" % os.path.basename(sys.argv[0]))
    with open(sys.argv[1], encoding="utf-8") as f:
        dados = json.load(f)
    todos = [a for caminho, texto in coletar(dados) for a in analisar(caminho, texto)]
    sys.exit(relatar(todos))
