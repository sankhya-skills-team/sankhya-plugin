"""Gera o documento de entrega em .docx sobre o modelo DS v.4.

Uso: python gerar_docx.py <dados.json>
Contrato do JSON: ver secao "Contrato dados.json" no SKILL.md.
Imprime na saida padrao um JSON com {arquivo, versao, backup, evidencias_faltando,
sumario_atualizado}.

Nao desenha o documento: abre assets/modelo-entrega-v4.docx (capa, cabecalho,
rodape, sumario, estilos e fontes do modelo) e preenche os placeholders. Os
blocos repetidos (funcionalidades, cenarios, checklist, evidencias) sao copias
dos proprios elementos do modelo, para herdar a formatacao sem redefini-la aqui.
Campo sem valor no JSON mantem o placeholder "< ... >" do modelo, para
preenchimento manual no Word.
"""

import copy
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _brand as B
from _comum import (ASSINATURAS_PADRAO, autor_atual, carregar_dados, coletar_evidencias,
                    detalhes_checklist, garantir, nome_item_checklist, parse_personas,
                    resolver_versao)

garantir("docx", "python-docx")

from docx import Document
from docx.image.image import Image
from docx.oxml.ns import qn
from docx.shared import Cm

D = carregar_dados(sys.argv)

ARQUIVO_SAIDA = D["arquivo_saida"]
AUTOR = autor_atual(D.get("responsavel_tecnico"))
VERSAO, BACKUP, HISTORICO = resolver_versao(ARQUIVO_SAIDA, D.get("changelog"), AUTOR)
DATA_GERACAO = HISTORICO[0]["data"]

FUNCIONALIDADES = D.get("funcionalidades", [])
CHECKLIST = D.get("checklist_deploy", {}) or {}
PRE = CHECKLIST.get("pre_requisitos") or []
POS = CHECKLIST.get("pos_deploy") or []
HOMOLOGACAO = D.get("homologacao") or {}
TREINAMENTO = D.get("treinamento") or {}

EVIDENCIAS, EVIDENCIAS_FALTANDO = coletar_evidencias(D)

# Faixa util do modelo, em twips (tblW das tabelas de corpo).
LARGURA_TWIPS = 9298
LARGURA_IMAGEM = Cm(16.4)
ALTURA_MAX_IMAGEM = Cm(19)    # print de tela alto nao pode passar da pagina
NUMID_PASSOS = "4"            # lista numerada "1." do exemplo do modelo

_AVISO_PERFIL = {
    "relatorio": "É necessário configurar os perfis de usuário que terão acesso ao relatório.",
    "tela":      "É necessário configurar os perfis de usuário que terão acesso à tela.",
    "dashboard": "É necessário configurar os perfis de usuário que terão acesso ao dashboard.",
}

doc = Document(B.TEMPLATE_DOCX)
CORPO = doc.element.body


# ── Localizacao no modelo ──────────────────────────────────────────

def texto(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def estilo(el):
    st = el.find("./" + qn("w:pPr") + "/" + qn("w:pStyle"))
    return st.get(qn("w:val")) if st is not None else ""


def paragrafo(inicio, nome_estilo=None):
    for el in CORPO.iterchildren(qn("w:p")):
        if texto(el).startswith(inicio) and (nome_estilo is None or estilo(el) == nome_estilo):
            return el
    raise LookupError("modelo sem o paragrafo %r" % inicio)


def tabela(contendo):
    for el in CORPO.iterchildren(qn("w:tbl")):
        if contendo in texto(el):
            return el
    raise LookupError("modelo sem a tabela com %r" % contendo)


def entre(inicio, fim):
    """Elementos do corpo depois de `inicio` e antes de `fim`."""
    saida, el = [], inicio.getnext()
    while el is not None and el is not fim:
        saida.append(el)
        el = el.getnext()
    return saida


def remover(*elementos):
    for el in elementos:
        el.getparent().remove(el)


def inserir_apos(ancora, elementos):
    for el in elementos:
        ancora.addnext(el)
        ancora = el
    return ancora


# ── Texto ──────────────────────────────────────────────────────────

def definir_texto(p, valor, limpar_placeholder=False):
    """Troca o texto do paragrafo mantendo a formatacao do primeiro run.

    `limpar_placeholder` tira o italico cinza que o modelo usa nos "< ... >".
    """
    runs = p.findall(qn("w:r"))
    for r in runs[1:]:
        p.remove(r)
    if runs:
        run = runs[0]
    else:
        run = p.makeelement(qn("w:r"), {})
        p.append(run)
    for t in run.findall(qn("w:t")):
        run.remove(t)
    if limpar_placeholder:
        rpr = run.find(qn("w:rPr"))
        for tag in ("w:i", "w:color"):
            for el in (rpr.findall(qn(tag)) if rpr is not None else []):
                rpr.remove(el)
    t = run.makeelement(qn("w:t"), {})
    t.text = str(valor)
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    run.append(t)
    return p


def definir_ultimo_run(p, valor):
    """Paragrafo 'Rotulo: valor' do modelo: troca so o valor, no ultimo run."""
    runs = p.findall(qn("w:r"))
    for r in runs[2:]:
        p.remove(r)
    alvo = runs[1] if len(runs) > 1 else runs[0]
    for t in alvo.findall(qn("w:t")):
        alvo.remove(t)
    t = alvo.makeelement(qn("w:t"), {})
    t.text = str(valor)
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    alvo.append(t)


def preencher_celula(tc, linhas):
    """Uma linha por paragrafo, copiando o formato do primeiro."""
    linhas = [str(l) for l in (linhas if isinstance(linhas, list) else [linhas])] or [""]
    pars = tc.findall(qn("w:p"))
    for p in pars[1:]:
        tc.remove(p)
    base = pars[0]
    definir_texto(base, linhas[0])
    ancora = base
    for linha in linhas[1:]:
        novo = definir_texto(copy.deepcopy(base), linha)
        ancora.addnext(novo)
        ancora = novo


def preencher_chave_valor(tbl, valores):
    """Tabela rotulo | valor do modelo. Valor vazio mantem o placeholder."""
    for tr in tbl.findall(qn("w:tr")):
        celulas = tr.findall(qn("w:tc"))
        if len(celulas) < 2:
            continue
        valor = valores.get(texto(celulas[0]).strip())
        if valor:
            preencher_celula(celulas[1], valor)


def lista(itens):
    itens = itens if isinstance(itens, list) else str(itens or "").split("\n")
    return [str(i).strip() for i in itens if str(i).strip()]


# ── Prototipos copiados do modelo ──────────────────────────────────
# Capturados antes de qualquer remocao: sao a fonte da formatacao dos blocos
# gerados.

P_H2       = copy.deepcopy(paragrafo("Acesso às novas funcionalidades", "Heading2"))
P_ROTULO   = copy.deepcopy(paragrafo("Exemplo", "SkRotulo"))
P_FUNC     = copy.deepcopy(paragrafo("Funcionalidade:"))
P_PASSO    = copy.deepcopy(paragrafo("Acesse o menu Financeiro"))
P_MARCADOR = copy.deepcopy(paragrafo("Utilize filtros"))
T_CAIXA    = copy.deepcopy(tabela("OBSERVAÇÃO"))
T_DADOS    = copy.deepcopy(tabela("DESCRIÇÃO DA ALTERAÇÃO"))


def rotulo(valor):
    return definir_texto(copy.deepcopy(P_ROTULO), valor)


def subtitulo(valor):
    return definir_texto(copy.deepcopy(P_H2), valor)


def marcadores(itens):
    return [definir_texto(copy.deepcopy(P_MARCADOR), i, limpar_placeholder=True)
            for i in lista(itens)]


def nova_numeracao():
    """Instancia de lista que recomeca em 1: sem ela os passos de uma
    funcionalidade continuariam a contagem da anterior."""
    numbering = doc.part.numbering_part.element
    abstrato = None
    for num in numbering.findall(qn("w:num")):
        if num.get(qn("w:numId")) == NUMID_PASSOS:
            abstrato = num.find(qn("w:abstractNumId")).get(qn("w:val"))
    novo_id = str(max(int(n.get(qn("w:numId"))) for n in numbering.findall(qn("w:num"))) + 1)
    num = numbering.makeelement(qn("w:num"), {qn("w:numId"): novo_id})
    abs_el = num.makeelement(qn("w:abstractNumId"), {qn("w:val"): abstrato})
    override = num.makeelement(qn("w:lvlOverride"), {qn("w:ilvl"): "0"})
    override.append(override.makeelement(qn("w:startOverride"), {qn("w:val"): "1"}))
    num.extend([abs_el, override])
    numbering.append(num)
    return novo_id


def passos_numerados(itens):
    num_id = nova_numeracao()
    saida = []
    for item in lista(itens):
        p = definir_texto(copy.deepcopy(P_PASSO), item)
        p.find(".//" + qn("w:numId")).set(qn("w:val"), num_id)
        saida.append(p)
    return saida


def caixa_observacao(valor):
    """Caixa OBSERVACAO do modelo (borda verde, fundo cinza)."""
    tbl = copy.deepcopy(T_CAIXA)
    p = tbl.find(".//" + qn("w:p"))
    definir_ultimo_run(p, valor)
    return tbl


def tabela_dados(colunas, linhas):
    """Tabela no formato do historico de versoes: cabecalho navy e linhas
    alternando branco e cinza, copiadas das duas linhas de dados do modelo.

    colunas = [(titulo, fracao_da_largura)]; linhas = [[str | [str]]].
    """
    tbl = copy.deepcopy(T_DADOS)
    trs = tbl.findall(qn("w:tr"))
    cabecalho, pares = trs[0], (trs[1], trs[2])
    for tr in trs:
        tbl.remove(tr)
    larguras = [int(LARGURA_TWIPS * f) for _t, f in colunas]

    grid = tbl.find(qn("w:tblGrid"))
    for gc in list(grid):
        grid.remove(gc)
    for w in larguras:
        grid.append(grid.makeelement(qn("w:gridCol"), {qn("w:w"): str(w)}))

    def linha(modelo, valores):
        tr = copy.deepcopy(modelo)
        proto = tr.findall(qn("w:tc"))[0]
        for tc in tr.findall(qn("w:tc")):
            tr.remove(tc)
        for w, valor in zip(larguras, valores):
            tc = copy.deepcopy(proto)
            tc.find(".//" + qn("w:tcW")).set(qn("w:w"), str(w))
            preencher_celula(tc, valor)
            tr.append(tc)
        return tr

    tbl.append(linha(cabecalho, [t.upper() for t, _f in colunas]))
    for i, valores in enumerate(linhas):
        tbl.append(linha(pares[i % 2], valores))
    return tbl


# ── Capa e controle do documento ───────────────────────────────────

definir_texto(paragrafo("< Nome do projeto >", "SkCapaLinha2"),
              D.get("nome_customizacao") or "< Nome do projeto >")

for tc in tabela("< Nome do cliente >").iter(qn("w:tc")):
    rotulo_capa, p_valor = texto(tc.findall(qn("w:p"))[0]), tc.findall(qn("w:p"))[1]
    valor = {"CLIENTE": D.get("parceiro"), "VERSÃO": VERSAO, "DATA": DATA_GERACAO,
             "RESPONSÁVEL": AUTOR}.get(rotulo_capa)
    if valor:
        definir_texto(p_valor, valor)

email = D.get("email_responsavel", "")
preencher_chave_valor(tabela("TIPO DE DOCUMENTO"), {
    "CLIENTE": D.get("parceiro"),
    "PROJETO": D.get("nome_customizacao"),
    "VERSÃO": VERSAO,
    "DATA": DATA_GERACAO,
    "RESPONSÁVEL": " — ".join(v for v in (AUTOR, email) if v),
})

# Historico: mais antiga primeiro, como no modelo.
hist_modelo = tabela("DESCRIÇÃO DA ALTERAÇÃO")
hist_modelo.addprevious(tabela_dados(
    [("Versão", 0.118), ("Data", 0.172), ("Autor", 0.248), ("Descrição da alteração", 0.462)],
    [[e["versao"], e["data"], e.get("autor", ""), e.get("alteracoes") or ["—"]]
     for e in reversed(HISTORICO)]))
remover(hist_modelo)

# ── 01 Identificacao ───────────────────────────────────────────────

preencher_chave_valor(tabela("Número da solicitação"), {
    "Parceiro / Cliente": D.get("parceiro"),
    "Número da solicitação": D.get("id_demanda"),
    "Desenvolvedor": D.get("responsavel_tecnico"),
    "Solicitante da demanda (Sankhya)": D.get("solicitante_sankhya"),
    "Solicitante ou responsável pela demanda (Parceiro)": D.get("solicitante_parceiro"),
})

# ── 03 Descricao das personalizacoes ───────────────────────────────
# Observacoes e anexos tecnicos sao opcionais por natureza: sem valor saem
# como "—", e nao como placeholder pendente.

preencher_chave_valor(tabela("Módulo / Área"), {
    "Descrição da customização": D.get("objetivo"),
    "Módulo / Área": D.get("modulo_area"),
    "Observações": D.get("observacoes") or "—",
    "Anexos técnicos": D.get("anexos_tecnicos") or "—",
})

# ── 04 Manual de uso ───────────────────────────────────────────────

if D.get("caminho_sistema"):
    definir_ultimo_run(paragrafo("Caminho no sistema:"), " " + D["caminho_sistema"])
if D.get("permissoes"):
    definir_ultimo_run(paragrafo("Permissões necessárias:"), " " + D["permissoes"])


def bloco_funcionalidade(func):
    meta = B.TIPO_META.get(func.get("tipo"), B.TIPO_META["acao"])
    p_func = copy.deepcopy(P_FUNC)
    # "Funcionalidade:" | " <titulo>. " | "Passo a passo:" -- troca so o meio.
    p_func.findall(qn("w:r"))[1].find(qn("w:t")).text = " %s. " % func.get("titulo", "")
    blocos = [rotulo(meta["badge"]), p_func] + passos_numerados(func.get("passos"))

    obs = " ".join(v for v in (str(func.get("obs") or "").strip(),
                                _AVISO_PERFIL.get(func.get("tipo_acesso", ""), "")) if v)
    if obs:
        blocos.append(caixa_observacao(obs))
    if lista(func.get("dicas")):
        blocos += [rotulo("Dicas de uso")] + marcadores(func["dicas"])
    if lista(func.get("limitacoes")):
        blocos += [rotulo("Limitações")] + marcadores(func["limitacoes"])
    return blocos


como_usar = paragrafo("Como utilizar as customizações", "Heading2")
limitacoes_h2 = paragrafo("Limitações conhecidas", "Heading2")
remover(*entre(como_usar, limitacoes_h2))
ancora = como_usar
for func in FUNCIONALIDADES:
    ancora = inserir_apos(ancora, bloco_funcionalidade(func))

homologacao_h1 = paragrafo("Homologação e Testes", "Heading1")
remover(*entre(limitacoes_h2, homologacao_h1))
inserir_apos(limitacoes_h2, marcadores(D.get("limitacoes_gerais"))
             or marcadores(["Nenhuma limitação global identificada."]))

# ── 05 Homologacao ─────────────────────────────────────────────────

MARCA_RESULTADO = {"aprovado":  "(X) Aprovado    ( ) Reprovado — com pendências abaixo",
                   "reprovado": "( ) Aprovado    (X) Reprovado — com pendências abaixo"}


def resultado_teste(teste):
    """Marca o status quando a homologacao ja foi executada."""
    status = str(teste.get("status", "")).lower()
    if not status and teste.get("evidencias"):
        status = "aprovado"
    return ["(%s) Aprovado" % ("X" if status == "aprovado" else " "),
            "(%s) Reprovado" % ("X" if status == "reprovado" else " ")]


treinamento_h1 = paragrafo("Treinamento e Suporte", "Heading1")
if not D.get("incluir_homologacao", True):
    remover(homologacao_h1, *entre(homologacao_h1, treinamento_h1))
else:
    tab_hom = tabela("Data da homologação")
    preencher_chave_valor(tab_hom, {
        "Responsável pelos testes no cliente": HOMOLOGACAO.get("responsavel"),
        "Data da homologação": HOMOLOGACAO.get("data"),
        "Resultado": MARCA_RESULTADO.get(str(HOMOLOGACAO.get("resultado", "")).lower()),
    })
    ancora = tab_hom
    for func in FUNCIONALIDADES:
        testes = func.get("testes") or []
        if testes:
            ancora = inserir_apos(ancora, [
                rotulo(func.get("titulo", "")),
                tabela_dados([("Cenário", 0.36), ("Resultado esperado", 0.42),
                              ("Resultado", 0.22)],
                             [[t.get("nome", ""), t.get("esperado", ""), resultado_teste(t)]
                              for t in testes])])
    if HOMOLOGACAO.get("pendencias"):
        definir_texto(paragrafo("< Descrever eventuais pendências"),
                      HOMOLOGACAO["pendencias"], limpar_placeholder=True)

# ── 06 Treinamento e suporte ───────────────────────────────────────

preencher_chave_valor(tabela("Público treinado"), {
    "Treinamento realizado em": TREINAMENTO.get("data"),
    "Público treinado": TREINAMENTO.get("publico"),
    "Material complementar": TREINAMENTO.get("material"),
    "Contato para suporte": TREINAMENTO.get("contato"),
})

# ── 07 Anexos ──────────────────────────────────────────────────────
# Sem evidencias nem checklist, os placeholders do modelo ficam para o
# preenchimento manual.


def imagem(caminho):
    """Paragrafo com a imagem na largura util, limitada em altura."""
    img = Image.from_file(caminho)
    largura = LARGURA_IMAGEM
    if img.px_height * largura / img.px_width > ALTURA_MAX_IMAGEM:
        largura = int(ALTURA_MAX_IMAGEM * img.px_width / img.px_height)
    p = doc.add_paragraph()
    p.add_run().add_picture(caminho, width=largura)
    el = p._p
    el.getparent().remove(el)
    return el


ESTILO_LEGENDA = next(s for s in doc.styles if s.style_id == "SkLegenda")


def legenda(valor):
    p = doc.add_paragraph(valor, style=ESTILO_LEGENDA)._p
    p.getparent().remove(p)
    return p


def tabela_checklist(itens):
    return tabela_dados(
        [("OK", 0.07), ("Tipo", 0.17), ("Item", 0.28), ("Detalhes", 0.48)],
        [["( )", B.LABEL_CHECKLIST.get(i.get("tipo", ""), i.get("tipo", "")),
          nome_item_checklist(i),
          ["%s: %s" % (r, v) if r else v for r, v, _m in detalhes_checklist(i)] or [""]]
         for i in itens])


anexos_h1 = paragrafo("Anexos", "Heading1")
garantia_h1 = paragrafo("Prazo de Garantia", "Heading1")
if EVIDENCIAS or PRE or POS:
    remover(*entre(anexos_h1, garantia_h1))
    blocos = []
    if EVIDENCIAS:
        blocos.append(subtitulo("Capturas de tela"))
        n = 0
        for _func, _teste, itens in EVIDENCIAS:
            for caminho, texto_legenda in itens:
                n += 1
                blocos += [imagem(caminho),
                           legenda("Evidência %02d — %s" % (n, texto_legenda))]
    if PRE or POS:
        blocos.append(subtitulo("Checklist de deploy"))
        if PRE:
            blocos += [rotulo("Pré-requisitos — antes do deploy"), tabela_checklist(PRE)]
        if POS:
            blocos += [rotulo("Pós-deploy — após o JAR no servidor"), tabela_checklist(POS)]
    inserir_apos(anexos_h1, blocos)

# ── Assinaturas ────────────────────────────────────────────────────

p_local = paragrafo("< Cidade >")
tab_assin = tabela("Nome:")
if not D.get("incluir_assinaturas", True):
    remover(p_local, tab_assin)
else:
    # Data e assinaturas abrem pagina propria, como no modelo: no fluxo
    # normal a grade quebrava e deixava a ultima assinatura sozinha.
    ppr = p_local.find(qn("w:pPr"))
    ppr.insert(0, ppr.makeelement(qn("w:pageBreakBefore"), {}))
    if D.get("cidade"):
        definir_texto(p_local, texto(p_local).replace("< Cidade >", D["cidade"]))
    pessoas = parse_personas(D.get("assinaturas")) or ASSINATURAS_PADRAO
    trs = tab_assin.findall(qn("w:tr"))
    proto_tr = trs[0]
    proto_assin, proto_vao = proto_tr.findall(qn("w:tc"))[:2]
    proto_vazia = trs[-1].findall(qn("w:tc"))[-1]

    def celula(pessoa):
        tc = copy.deepcopy(proto_assin)
        p_nome, p_papel = tc.findall(qn("w:p"))[:2]
        definir_texto(p_nome, "Nome: %s" % pessoa["nome"] if pessoa["nome"] else "Nome:")
        definir_texto(p_papel, pessoa["funcao"] or "")
        return tc

    for tr in trs:
        tab_assin.remove(tr)
    for i in range(0, len(pessoas), 2):
        tr = copy.deepcopy(proto_tr)
        for tc in tr.findall(qn("w:tc")):
            tr.remove(tc)
        par = pessoas[i:i + 2]
        tr.extend([celula(par[0]), copy.deepcopy(proto_vao),
                   celula(par[1]) if len(par) > 1 else copy.deepcopy(proto_vazia)])
        tab_assin.append(tr)

# ── Contracapa ─────────────────────────────────────────────────────

if email:
    definir_texto(paragrafo("< nome.sobrenome@sankhya.com.br >"), email)
if D.get("telefone_responsavel"):
    definir_texto(paragrafo("< (XX) 99999-9999 >"), D["telefone_responsavel"])

# ── Sumario ────────────────────────────────────────────────────────
# O modelo vem com w:updateFields, que faz o Word perguntar "Deseja atualizar
# os campos?" a cada abertura. O documento sai sem a flag e, havendo Word na
# maquina, o proprio Word atualiza o sumario em segundo plano. Sem Word, a flag
# volta: o aviso e melhor que um sumario com as paginas do modelo.

ATUALIZAR_SUMARIO_PS = r"""
$w = New-Object -ComObject Word.Application
$w.Visible = $false; $w.DisplayAlerts = 0
try {
  $d = $w.Documents.Open($env:DOC_ENTREGA_ARQUIVO, $false, $false)
  $d.TablesOfContents | ForEach-Object { $_.Update() }
  $d.Save(); $d.Close()
} finally { $w.Quit() }
"""
TIMEOUT_WORD_S = 120


def definir_atualizar_campos(ligado):
    settings = doc.settings.element
    for el in settings.findall(qn("w:updateFields")):
        settings.remove(el)
    if ligado:
        settings.append(settings.makeelement(qn("w:updateFields"), {qn("w:val"): "true"}))


def atualizar_sumario_no_word(caminho):
    """True se o Word atualizou o sumario. So existe no Windows com Office."""
    if sys.platform != "win32" or os.environ.get("DOC_ENTREGA_SEM_WORD"):
        return False
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command",
                            ATUALIZAR_SUMARIO_PS], capture_output=True, timeout=TIMEOUT_WORD_S,
                           env=dict(os.environ, DOC_ENTREGA_ARQUIVO=os.path.abspath(caminho)))
        return r.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


doc.core_properties.version = VERSAO
doc.core_properties.title = "Evidências de Entrega — %s" % D.get("nome_customizacao", "")
definir_atualizar_campos(False)
doc.save(ARQUIVO_SAIDA)
SUMARIO_ATUALIZADO = atualizar_sumario_no_word(ARQUIVO_SAIDA)
if not SUMARIO_ATUALIZADO:
    definir_atualizar_campos(True)
    doc.save(ARQUIVO_SAIDA)

print(json.dumps({"arquivo": ARQUIVO_SAIDA, "versao": VERSAO, "backup": BACKUP,
                  "evidencias_faltando": EVIDENCIAS_FALTANDO,
                  "sumario_atualizado": SUMARIO_ATUALIZADO}))
