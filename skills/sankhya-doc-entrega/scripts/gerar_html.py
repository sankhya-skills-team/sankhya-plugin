"""Gera o documento de entrega em HTML interativo, na estrutura do modelo DS v.4.

Uso: python gerar_html.py <dados.json>
Contrato do JSON: ver secao "Contrato dados.json" no SKILL.md.
Imprime na saida padrao um JSON com {arquivo, versao, backup, evidencias_faltando}.

Mesmas secoes do DOCX (capa, controle do documento, 01-08, assinaturas e
contracapa), com cores e tipografia do guia Padrao 2026. Campo sem valor
aparece como o placeholder "< ... >" do modelo.
"""

import base64
import json
import mimetypes
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _brand as B
from _comum import (ASSINATURAS_PADRAO, autor_atual, carregar_dados, coletar_evidencias,
                    detalhes_checklist, nome_item_checklist, parse_personas, resolver_versao)

D = carregar_dados(sys.argv)

ARQUIVO_SAIDA = D["arquivo_saida"]
AUTOR = autor_atual(D.get("responsavel_tecnico"))
VERSAO, BACKUP, HISTORICO = resolver_versao(ARQUIVO_SAIDA, D.get("changelog"), AUTOR)
DATA_GERACAO = HISTORICO[0]["data"]

FUNCIONALIDADES     = D.get("funcionalidades", [])
CHECKLIST           = D.get("checklist_deploy", {}) or {}
HOMOLOGACAO         = D.get("homologacao") or {}
TREINAMENTO         = D.get("treinamento") or {}
INCLUIR_HOMOLOGACAO = bool(D.get("incluir_homologacao", True))
INCLUIR_ASSINATURAS = bool(D.get("incluir_assinaturas", True))
INCLUIR_DEPLOY      = bool(CHECKLIST.get("pre_requisitos") or CHECKLIST.get("pos_deploy"))
ASSINATURAS         = parse_personas(D.get("assinaturas")) or ASSINATURAS_PADRAO
EMAIL               = D.get("email_responsavel", "")

_evidencias, EVIDENCIAS_FALTANDO = coletar_evidencias(D)
EVIDENCIAS = {id(teste): itens for _f, teste, itens in _evidencias}

# Textos fixos do modelo DS v.4 -- iguais aos do DOCX.
OBJETIVO_DOCUMENTO = (
    "Este documento tem como objetivo formalizar a entrega das personalizações "
    "solicitadas pelo cliente, bem como fornecer um manual de uso detalhado que facilite "
    "a correta utilização dos recursos personalizados. O objetivo é garantir compreensão, "
    "segurança e rastreabilidade de tudo o que foi entregue.")
GARANTIA = (
    "Este documento tem garantia dos produtos e serviços entregues das demandas "
    "solicitadas com prazo de <strong>30 dias</strong>. Por se tratar de uma "
    "personalização, o Service Desk não atua nos casos de dúvidas ou incidentes. "
    "Alterações solicitadas após esse prazo serão consideradas improcedentes, "
    "necessitando de nova estimativa e resultando em custos adicionais para o parceiro "
    "contratante.")


def h(s):
    """Escapa caracteres HTML basicos."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
                  .replace(">", "&gt;").replace('"', "&quot;"))


def valor_ou_placeholder(valor, placeholder):
    if valor:
        return h(valor)
    return '<span class="ph">%s</span>' % h(placeholder)


def lista(itens):
    itens = itens if isinstance(itens, list) else str(itens or "").split("\n")
    return [str(i).strip() for i in itens if str(i).strip()]


def data_uri(caminho):
    mime = mimetypes.guess_type(caminho)[0] or "image/png"
    with open(caminho, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


# ── Blocos de conteudo ─────────────────────────────────────────────

def tabela_kv(linhas):
    """linhas = [(rotulo, valor, placeholder)]"""
    corpo = "".join('<tr><th>%s</th><td>%s</td></tr>'
                    % (h(r), valor_ou_placeholder(v, ph)) for r, v, ph in linhas)
    return '<table class="kv"><tbody>%s</tbody></table>' % corpo


def tabela_dados(colunas, linhas):
    """Cabecalho navy e linhas alternadas, como o historico do modelo."""
    cab = "".join("<th>%s</th>" % h(c) for c in colunas)
    corpo = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in linha)
                    for linha in linhas)
    return '<table class="dados"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (cab, corpo)


def marcadores(itens, classe="bullets"):
    return '<ul class="%s">%s</ul>' % (classe, "".join("<li>%s</li>" % h(i) for i in itens))


def rotulo(texto):
    return '<div class="rotulo">%s</div>' % h(texto)


def caixa(rotulo_caixa, html_texto, classe="nota"):
    return ('<div class="%s"><span class="nota-rotulo">%s</span>%s</div>'
            % (classe, h(rotulo_caixa), html_texto))


_AVISO_PERFIL = {
    "relatorio": "É necessário configurar os perfis de usuário que terão acesso ao relatório.",
    "tela":      "É necessário configurar os perfis de usuário que terão acesso à tela.",
    "dashboard": "É necessário configurar os perfis de usuário que terão acesso ao dashboard.",
}


def build_func_card(idx, func):
    meta = B.TIPO_META.get(func.get("tipo"), B.TIPO_META["acao"])
    fid = "fc%d" % idx
    passos = "".join("<li>%s</li>" % h(p) for p in lista(func.get("passos")))
    corpo = '<div class="rotulo-inline">Passo a passo:</div><ol class="steps">%s</ol>' % passos
    obs = " ".join(v for v in (str(func.get("obs") or "").strip(),
                                _AVISO_PERFIL.get(func.get("tipo_acesso", ""), "")) if v)
    if obs:
        corpo += caixa("Observação", h(obs))
    if lista(func.get("dicas")):
        corpo += rotulo("Dicas de uso") + marcadores(lista(func["dicas"]))
    if lista(func.get("limitacoes")):
        corpo += rotulo("Limitações") + marcadores(lista(func["limitacoes"]))
    return (
        '<div class="func-card" id="%s">'
        '<button class="func-header" type="button" onclick="toggle(\'%s\')">'
        '<span class="func-icon">%s</span>'
        '<span class="func-info"><span class="rotulo" style="color:%s">%s</span>'
        '<span class="func-name"><strong>Funcionalidade:</strong> %s</span></span>'
        '<span class="func-arrow">›</span></button>'
        '<div class="func-body">%s</div></div>'
    ) % (fid, fid, func.get("icone") or meta["icone"], meta["cor"], h(meta["badge"]),
         h(func.get("titulo", "")), corpo)


STATUS_TESTE = {"pendente":  ("pendente",  "⏳ Pendente"),
                "aprovado":  ("aprovado",  "✅ Aprovado"),
                "reprovado": ("reprovado", "❌ Reprovado")}


def build_galeria(itens, tid):
    """Mesma marcacao que o botao 'Exportar com evidencias' produz no navegador,
    para que reexportar por cima nao perca nem duplique nada."""
    partes = []
    for caminho, legenda in itens:
        nome = os.path.basename(caminho)
        partes.append(
            '<div class="evidence-item">'
            '<img src="%s" title="%s" alt="Evidência: %s">'
            '<button class="remove-img" type="button" onclick="removeImg(this,\'%s\')">✕</button>'
            '<input type="text" class="evidence-caption" value="%s" '
            'placeholder="Descreva o que esta imagem mostra...">'
            '</div>' % (data_uri(caminho), h(nome), h(nome), tid, h(legenda)))
    return '<div class="evidence-gallery">%s</div>' % "".join(partes)


def build_cenarios(funcionalidades):
    saida = ""
    for fi, func in enumerate(funcionalidades, 1):
        testes = func.get("testes") or []
        if not testes:
            continue
        saida += '<div class="hom-group">%s' % rotulo(func.get("titulo", ""))
        for ti, t in enumerate(testes, 1):
            tid = "hom-fc%d-%d" % (fi, ti)
            itens = EVIDENCIAS.get(id(t)) or []
            classe, rotulo_status = STATUS_TESTE.get(
                str(t.get("status", "")).lower(),
                STATUS_TESTE["aprovado"] if itens else STATUS_TESTE["pendente"])
            galeria = build_galeria(itens, tid) if itens else ""
            n = len(itens)
            hint = ("Nenhuma imagem anexada" if n == 0 else
                    "%d %s" % (n, "imagens anexadas" if n > 1 else "imagem anexada"))
            saida += (
                '<div class="test-case" id="%s">'
                '<div class="test-header">'
                '<button class="status-btn %s" type="button" onclick="toggleStatus(this)">%s</button>'
                '<div class="test-desc">'
                '<div class="test-name">%s</div>'
                '<div class="test-expected"><strong>Resultado esperado:</strong> %s</div>'
                '</div></div>'
                '<div class="test-evidence">%s'
                '<div class="evidence-row">'
                '<label class="attach-btn">📎 Adicionar evidência'
                '<input type="file" accept="image/*" multiple onchange="attachImage(this,\'%s\')"></label>'
                '<span class="no-evidence" id="%s-hint">%s</span>'
                '</div></div></div>'
            ) % (tid, classe, rotulo_status, h(t.get("nome", "")), h(t.get("esperado", "")),
                 galeria, tid, tid, hint)
        saida += "</div>"
    return saida


MARCA_RESULTADO = {"aprovado":  "(X) Aprovado &nbsp;&nbsp; ( ) Reprovado — com pendências abaixo",
                   "reprovado": "( ) Aprovado &nbsp;&nbsp; (X) Reprovado — com pendências abaixo"}


def build_homologacao():
    resultado = MARCA_RESULTADO.get(str(HOMOLOGACAO.get("resultado", "")).lower(),
                                    "( ) Aprovado &nbsp;&nbsp; ( ) Reprovado — com pendências abaixo")
    resumo = tabela_kv([
        ("Responsável pelos testes no cliente", HOMOLOGACAO.get("responsavel"), "< Nome e cargo >"),
        ("Data da homologação", HOMOLOGACAO.get("data"), "< DD/MM/AAAA >"),
    ]).replace("</tbody>", "<tr><th>Resultado</th><td>%s</td></tr></tbody>" % resultado)
    pendencias = valor_ou_placeholder(HOMOLOGACAO.get("pendencias"),
                                      "< Descrever eventuais pendências ou melhorias futuras >")
    return (resumo + build_cenarios(FUNCIONALIDADES)
            + rotulo("Pendências / observações") + '<p class="texto">%s</p>' % pendencias)


def build_historico(entradas):
    linhas = [[h("v" + e["versao"]), h(e["data"]), h(e.get("autor", "")),
               "<br>".join(h(a) for a in (e.get("alteracoes") or ["—"]))]
              for e in reversed(entradas)]
    return tabela_dados(["Versão", "Data", "Autor", "Descrição da alteração"], linhas)


def build_deploy(checklist):
    pre = checklist.get("pre_requisitos") or []
    pos = checklist.get("pos_deploy") or []
    contador = [0]

    def item(it):
        contador[0] += 1
        cid = "ck%d" % contador[0]
        detalhes = ["%s: %s" % (r, "<code>%s</code>" % h(v) if mono else h(v)) if r else h(v)
                    for r, v, mono in detalhes_checklist(it)]
        detalhe_html = ('<span class="ck-detail">%s</span>'
                        % " &nbsp;|&nbsp; ".join(detalhes)) if detalhes else ""
        tipo = it.get("tipo", "")
        return ('<div class="ck-item"><label class="ck-label">'
                '<input type="checkbox" class="ck-box" id="%s" onchange="ckSave(\'%s\')">'
                '<span class="ck-badge">%s</span>'
                '<span class="ck-name">%s</span>%s</label></div>'
                % (cid, cid, h(B.LABEL_CHECKLIST.get(tipo, tipo)),
                   h(nome_item_checklist(it)), detalhe_html))

    def grupo(titulo, itens):
        if not itens:
            return ""
        return rotulo(titulo) + '<div class="ck-group">%s</div>' % "".join(item(i) for i in itens)

    return (grupo("Pré-requisitos — antes do deploy", pre)
            + grupo("Pós-deploy — após o JAR no servidor", pos))


def build_anexos():
    blocos = ""
    if EVIDENCIAS:
        blocos += ('<h3 class="h2">Capturas de tela</h3><p class="texto">As capturas de cada '
                   'cenário ficam junto ao teste, em 05 Homologação e Testes.</p>')
    if INCLUIR_DEPLOY:
        blocos += '<h3 class="h2">Checklist de deploy</h3>' + build_deploy(CHECKLIST)
    if blocos:
        return blocos
    return ('<ul class="bullets">%s</ul>' % "".join(
        '<li><span class="ph">%s</span></li>' % h(p) for p in (
            "< Capturas de tela >", "< Diagramas técnicos >",
            "< Planilhas ou documentos de apoio >", "< Links para base de conhecimento >")))


def build_assinaturas():
    local = "%s, &lt; dia &gt; de &lt; mês &gt; de &lt; ano &gt;" % (
        h(D["cidade"]) if D.get("cidade") else "&lt; Cidade &gt;")
    caixas = "".join(
        '<div class="sign-box"><div class="sign-name">Nome:%s</div>'
        '<div class="sign-role">%s</div></div>'
        % (" " + h(p["nome"]) if p.get("nome") else "", h(p.get("funcao", "")))
        for p in ASSINATURAS)
    return '<p class="sign-local">%s</p><div class="sign-grid">%s</div>' % (local, caixas)


# ── Secoes ─────────────────────────────────────────────────────────

SECOES = [("controle", "", "Controle do documento", "")]
SECOES.append(("identificacao", "01", "Identificação", tabela_kv([
    ("Parceiro / Cliente", D.get("parceiro"), "< Nome do parceiro >"),
    ("Número da solicitação", D.get("id_demanda"),
     "< Número do ID na tela SOLICITAÇÃO DE SERVIÇOS - DS >"),
    ("Desenvolvedor", D.get("responsavel_tecnico"), "< Nome do dev que entregou a demanda >"),
    ("Solicitante da demanda (Sankhya)", D.get("solicitante_sankhya"),
     "< GP, Analista de Projeto, Sucesso do Cliente, Gerente de Relacionamento etc. >"),
    ("Solicitante ou responsável pela demanda (Parceiro)", D.get("solicitante_parceiro"),
     "< Responsável no parceiro/cliente que esteve em contato com o desenvolvedor >"),
])))
SECOES.append(("objetivo", "02", "Objetivo", '<p class="texto">%s</p>' % OBJETIVO_DOCUMENTO))
SECOES.append(("descricao", "03", "Descrição das Personalizações Realizadas", tabela_kv([
    ("Descrição da customização", D.get("objetivo"), "< Descrição abreviada >"),
    ("Módulo / Área", D.get("modulo_area"), "< Módulo nativo ou nome geral da rotina customizada >"),
    ("Observações", D.get("observacoes") or "—", ""),
    ("Anexos técnicos", D.get("anexos_tecnicos") or "—", ""),
])))
SECOES.append(("manual", "04", "Manual de Uso das Customizações", (
    '<h3 class="h2">Acesso às novas funcionalidades</h3><ul class="bullets">'
    '<li><strong>Caminho no sistema:</strong> %s</li>'
    '<li><strong>Permissões necessárias:</strong> %s</li></ul>'
    '<h3 class="h2">Como utilizar as customizações</h3>%s'
    '<h3 class="h2">Limitações conhecidas</h3>%s'
) % (valor_ou_placeholder(D.get("caminho_sistema"), "< Ex.: Menu > Financeiro > Relatórios Personalizados >"),
     valor_ou_placeholder(D.get("permissoes"), "< Perfis de usuários com acesso >"),
     "".join(build_func_card(i, f) for i, f in enumerate(FUNCIONALIDADES, 1)),
     marcadores(lista(D.get("limitacoes_gerais")) or ["Nenhuma limitação global identificada."]))))
if INCLUIR_HOMOLOGACAO:
    SECOES.append(("homologacao", "05", "Homologação e Testes", build_homologacao()))
SECOES.append(("treinamento", "06", "Treinamento e Suporte", tabela_kv([
    ("Treinamento realizado em", TREINAMENTO.get("data"), "< DD/MM/AAAA >"),
    ("Público treinado", TREINAMENTO.get("publico"), "< Equipe Financeira, TI etc. >"),
    ("Material complementar", TREINAMENTO.get("material"),
     "< Link ou anexo do material em PDF, vídeo ou apresentação >"),
    ("Contato para suporte", TREINAMENTO.get("contato"), "< E-mail, telefone, horário de atendimento >"),
])))
SECOES.append(("anexos", "07", "Anexos", build_anexos()))
SECOES.append(("garantia", "08", "Prazo de Garantia para Validação das Entregas",
               caixa("Garantia", GARANTIA)))
if INCLUIR_ASSINATURAS:
    SECOES.append(("assinaturas", "", "Assinaturas", build_assinaturas()))

# Sem homologacao a numeracao segue corrida, como o Word faz com a lista do Heading1.
_n = 0
for i, (sid, num, titulo, corpo) in enumerate(SECOES):
    if num:
        _n += 1
        SECOES[i] = (sid, "%02d" % _n, titulo, corpo)

CONTROLE = (
    '<h2 class="abertura"><span class="l1">Controle do</span><span class="l2">documento</span></h2>'
    '%s<div class="rotulo">Histórico de versões</div>%s'
) % (tabela_kv([("Cliente", D.get("parceiro"), "Nome do cliente"),
                ("Projeto", D.get("nome_customizacao"), "Nome do projeto"),
                ("Tipo de documento", "Evidências de Entrega de Customização", ""),
                ("Versão", VERSAO, ""), ("Data", DATA_GERACAO, ""),
                ("Responsável", " — ".join(v for v in (AUTOR, EMAIL) if v), "Nome Sobrenome")]),
     build_historico(HISTORICO))


def secao_html(sid, num, titulo, corpo):
    if sid == "controle":
        return '<section class="section" id="controle">%s</section>' % CONTROLE
    cab = ('<h2 class="h1"><span class="h1-num">%s</span>%s</h2>' % (num, h(titulo)) if num
           else '<h2 class="h1">%s</h2>' % h(titulo))
    return '<section class="section" id="%s">%s%s</section>' % (sid, cab, corpo)


nav_html = "".join(
    '<a class="nav-item%s" href="#%s"><span class="nav-num">%s</span>%s</a>'
    % (" active" if i == 0 else "", sid, num, h(titulo))
    for i, (sid, num, titulo, _c) in enumerate(SECOES))
main_html = "".join(secao_html(*s) for s in SECOES)

CAPA = (
    # O fundo da capa ja traz a logo; so a contracapa recebe a logo por cima.
    '<div class="cover" style="background-image:url(%(fundo)s)">'
    '<div class="cover-titulo"><span class="l1">Evidências de entrega</span>'
    '<span class="l1">de customização</span><span class="l2">%(projeto)s</span></div>'
    '<p class="cover-sub">Formalização da entrega, manual de uso,<br>'
    'homologação e garantia das personalizações.</p>'
    '<div class="cover-meta">'
    '<div><span>Cliente</span>%(cliente)s</div><div><span>Versão</span>%(versao)s</div>'
    '<div><span>Data</span>%(data)s</div><div><span>Responsável</span>%(resp)s</div>'
    '</div></div>'
) % {"fundo": data_uri(B.CAPA_JPG),
     "projeto": h(D.get("nome_customizacao") or "< Nome do projeto >"),
     "cliente": h(D.get("parceiro") or "< Nome do cliente >"), "versao": h(VERSAO),
     "data": DATA_GERACAO, "resp": h(AUTOR or "< Nome Sobrenome >")}

CONTRACAPA = (
    '<div class="backcover" style="background-image:url(%(fundo)s)">'
    '<div class="cover-titulo"><span class="l1">Obrigado.</span>'
    '<span class="l2">Dúvidas? Fale com a gente.</span></div>'
    '<div class="back-contato"><span>Delivery Service Tech</span>%(email)s<br>%(tel)s</div>'
    '<div class="back-logo">%(logo)s</div></div>'
) % {"fundo": data_uri(B.CONTRACAPA_JPG), "logo": B.LOGO_SVG,
     "email": h(EMAIL or "< nome.sobrenome@sankhya.com.br >"),
     "tel": h(D.get("telefone_responsavel") or "< (XX) 99999-9999 >")}


# ── CSS ────────────────────────────────────────────────────────────
# Tamanhos do guia Padrao 2026 convertidos de pt (x 4/3 = px).

def px(pt):
    return "%.1fpx" % (pt * 4 / 3)


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;600&display=swap');
:root{
  --navy900:%(navy900)s;--navy:%(navy700)s;--slate:%(slate)s;--verde:%(verde)s;
  --verde-apoio:%(verde_apoio)s;--cinza:%(cinza)s;--cinza-claro:%(cinza_claro)s;
  --danger:%(danger)s;--linha:#D9D9D9;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:%(font)s;background:#fff;color:var(--navy);font-size:%(pt_texto)s;
  line-height:1.6;-webkit-font-smoothing:antialiased;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.layout{display:flex;min-height:100vh}
strong{font-weight:600}

/* sidebar */
.sidebar{width:260px;flex-shrink:0;background:var(--navy);color:#fff;
  position:sticky;top:0;height:100vh;overflow-y:auto;display:flex;flex-direction:column}
.sidebar-logo{padding:22px 20px 16px;border-bottom:1px solid rgba(255,255,255,.1)}
.logo{height:24px;width:auto;display:block;color:#fff;margin-bottom:14px}
.s-brand{font-size:11px;font-weight:600;letter-spacing:2px;color:var(--verde);
  text-transform:uppercase;margin-bottom:4px}
.s-title{font-size:15px;font-weight:600;color:#fff;line-height:1.38}
.s-meta{font-size:12px;color:rgba(255,255,255,.5);margin-top:6px}
.nav{padding:10px 0;flex:1}
.nav-item{display:flex;align-items:baseline;gap:10px;padding:8px 20px;
  color:rgba(255,255,255,.7);font-size:13px;text-decoration:none;
  border-left:3px solid transparent}
.nav-item:hover{background:rgba(255,255,255,.06);color:#fff}
.nav-item.active{color:#fff;border-left-color:var(--verde);background:rgba(0,214,102,.08)}
.nav-num{width:20px;flex-shrink:0;color:var(--verde);font-weight:300}
.export-btn{margin:16px;background:var(--verde);color:var(--navy);border:none;
  padding:10px 14px;font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;
  width:calc(100%% - 32px)}
.export-btn:hover{filter:brightness(.94)}
.pdf-btn{margin:0 16px 16px;background:transparent;color:#fff;
  border:1px solid rgba(255,255,255,.35);padding:10px 14px;
  font-family:inherit;font-size:14px;font-weight:600;cursor:pointer;width:calc(100%% - 32px)}
.pdf-btn:hover{background:rgba(255,255,255,.08)}

/* main */
.main{flex:1;min-width:0}
.content{padding:48px 56px;max-width:920px}
.section{margin-bottom:52px;scroll-margin-top:24px}
.h1{font-size:%(pt_h1)s;font-weight:600;text-transform:uppercase;letter-spacing:.06em;
  color:var(--navy);margin-bottom:18px;display:flex;gap:18px;align-items:baseline}
.h1-num{color:var(--verde-apoio);font-weight:300;letter-spacing:0}
.h2{font-size:%(pt_h2)s;font-weight:600;color:var(--navy);margin:26px 0 10px}
.abertura{display:flex;flex-direction:column;font-size:%(pt_abertura)s;line-height:1.15;
  text-transform:uppercase;letter-spacing:.04em;margin-bottom:24px}
.abertura .l1{font-weight:300;color:var(--verde-apoio)}
.abertura .l2{font-weight:600;color:var(--navy)}
.rotulo{font-size:%(pt_legenda)s;font-weight:600;text-transform:uppercase;letter-spacing:.25em;
  color:var(--verde-apoio);margin:22px 0 8px}
.rotulo-inline{font-weight:600;margin:4px 0 6px}
.texto{margin-bottom:10px}
.ph{color:var(--cinza);font-style:italic}
code{font-family:ui-monospace,Consolas,monospace;font-size:12px;background:var(--cinza-claro);
  padding:1px 5px}

/* tabelas */
.kv,.dados{width:100%%;border-collapse:collapse;font-size:13px}
.kv th,.kv td{padding:9px 12px;border-bottom:1px solid var(--linha);text-align:left;
  vertical-align:middle}
.kv th{background:var(--cinza-claro);font-weight:600;width:34%%}
.dados th{background:var(--navy);color:#fff;font-weight:600;text-transform:uppercase;
  text-align:left;padding:9px 12px;font-size:12px}
.dados td{padding:9px 12px;border-bottom:1px solid var(--linha);vertical-align:top}
.dados tbody tr:nth-child(even) td{background:var(--cinza-claro)}

/* listas */
.bullets{list-style:none;margin:6px 0 10px}
.bullets li{position:relative;padding:4px 0 4px 26px}
.bullets li::before{content:"";position:absolute;left:6px;top:.85em;width:7px;height:7px;
  background:var(--verde-apoio)}
.steps{list-style:none;counter-reset:passo;margin:0 0 8px}
.steps li{counter-increment:passo;position:relative;padding:4px 0 4px 26px}
.steps li::before{content:counter(passo) ".";position:absolute;left:0;font-weight:600;
  color:var(--verde-apoio)}

/* caixas */
.nota{background:var(--cinza-claro);border-left:6px solid var(--verde);padding:14px 20px;
  margin:12px 0;line-height:1.7}
.nota-rotulo{color:var(--verde-apoio);font-weight:600;text-transform:uppercase;
  letter-spacing:.2em;margin-right:12px}

/* funcionalidades */
.func-card{border:1px solid var(--linha);border-left:4px solid var(--verde);margin-bottom:12px}
.func-header{width:100%%;background:none;border:none;font-family:inherit;text-align:left;
  padding:12px 16px;cursor:pointer;display:flex;align-items:center;gap:12px;color:var(--navy)}
.func-icon{font-size:20px;flex-shrink:0}
.func-info{flex:1;display:flex;flex-direction:column}
.func-info .rotulo{margin:0 0 2px}
.func-name{font-size:%(pt_texto)s}
.func-arrow{font-size:16px;color:var(--cinza);transition:transform .2s;flex-shrink:0}
.func-card.open .func-arrow{transform:rotate(90deg)}
.func-body{display:none;border-top:1px solid var(--linha);padding:14px 18px 16px}
.func-card.open .func-body{display:block}

/* homologacao */
.hom-group{margin-top:8px}
.test-case{border:1px solid var(--linha);margin-bottom:10px}
.test-header{display:flex;align-items:flex-start;gap:12px;padding:12px 16px}
.status-btn{border:1px solid transparent;font-family:inherit;cursor:pointer;font-size:12px;
  font-weight:600;padding:3px 12px;border-radius:9999px;white-space:nowrap;flex-shrink:0}
.status-btn.pendente{background:var(--cinza-claro);color:var(--cinza);border-color:var(--linha)}
.status-btn.aprovado{background:rgba(0,214,102,.14);color:#008F45;border-color:var(--verde)}
.status-btn.reprovado{background:#FEE2E2;color:var(--danger);border-color:#FCA5A5}
.test-desc{flex:1}
.test-name{font-weight:600;margin-bottom:3px}
.test-expected{font-size:13px}
.test-evidence{padding:10px 16px;border-top:1px solid var(--linha)}
.evidence-gallery{display:flex;flex-direction:column;gap:8px;margin-bottom:8px}
.evidence-item{position:relative}
.evidence-item img{width:100%%;max-height:420px;object-fit:contain;
  border:1px solid var(--linha);display:block;background:var(--cinza-claro)}
.evidence-caption{width:100%%;margin-top:6px;font:inherit;font-size:%(pt_legenda)s;
  color:var(--cinza);border:1px solid var(--linha);padding:6px 10px;background:#fff}
.evidence-caption:focus{outline:none;border-color:var(--verde)}
.evidence-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.attach-btn{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;
  color:var(--navy);background:rgba(0,214,102,.08);border:1px dashed var(--verde);
  padding:5px 12px;cursor:pointer}
.attach-btn input[type=file]{display:none}
.remove-img{position:absolute;top:6px;right:6px;background:#fff;border:1px solid #FCA5A5;
  color:var(--danger);padding:2px 7px;font-size:12px;cursor:pointer}
.no-evidence{font-size:12px;color:var(--cinza);font-style:italic}

/* checklist */
.ck-group{border:1px solid var(--linha)}
.ck-item{padding:9px 14px;border-top:1px solid var(--linha)}
.ck-item:first-child{border-top:none}
.ck-item:nth-child(even){background:var(--cinza-claro)}
.ck-item:has(.ck-box:checked){background:rgba(0,214,102,.08)}
.ck-label{display:flex;align-items:center;gap:8px;cursor:pointer;font-size:13px;flex-wrap:wrap}
.ck-box{width:16px;height:16px;accent-color:var(--navy);cursor:pointer;flex-shrink:0}
.ck-badge{background:var(--navy);color:#fff;font-size:11px;font-weight:600;
  padding:1px 8px;white-space:nowrap;flex-shrink:0}
.ck-name{font-weight:600}
.ck-detail{font-size:12px;color:var(--slate);line-height:1.5}

/* assinaturas */
.sign-local{text-align:right;margin:24px 0 8px}
.sign-grid{display:grid;grid-template-columns:1fr 1fr;column-gap:48px}
.sign-box{border-top:2px solid var(--verde);margin-top:64px;padding-top:8px}
.sign-name{font-weight:600;font-size:12px}
.sign-role{font-size:12px;color:var(--cinza)}

/* capa e contracapa -- fundos do modelo DS v.4 */
.cover,.backcover{position:relative;background:var(--navy900) center/cover no-repeat;color:#fff;
  aspect-ratio:210/297;max-height:100vh;width:100%%;overflow:hidden}
.back-logo .logo{height:32px;width:auto;color:#fff}
.cover-titulo{position:absolute;left:11%%;right:11%%;top:39%%;display:flex;flex-direction:column;
  font-size:clamp(18px,3.4vw,%(pt_abertura)s);line-height:1.2;text-transform:uppercase;
  letter-spacing:.06em}
.cover-titulo .l1{font-weight:300;color:var(--verde)}
.cover-titulo .l2{font-weight:600;color:#fff}
.cover-sub{position:absolute;left:11%%;top:50%%;font-size:14px;line-height:2;
  color:rgba(255,255,255,.9)}
.cover-meta{position:absolute;left:11%%;right:11%%;top:77%%;border-top:1px solid var(--verde);
  padding-top:10px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;font-size:12px}
.cover-meta span{display:block;color:var(--verde);font-size:9px;font-weight:600;
  letter-spacing:.3em;text-transform:uppercase;margin-bottom:4px}
.backcover .cover-titulo{top:42%%}
.back-contato{position:absolute;left:11%%;top:52%%;font-size:12px;line-height:1.7}
.back-contato span{display:block;color:var(--verde);font-size:9px;font-weight:600;
  letter-spacing:.3em;text-transform:uppercase}
.back-logo{position:absolute;left:11%%;top:82%%}

@page{size:A4;margin:2cm 2.3cm}
@page capa{margin:0}
@media print{
  .sidebar{display:none}
  .content{padding:0;max-width:100%%}
  /* largura 100%%, e nao 210mm: largura fixa alargava o main e o conteudo
     das paginas com margem estourava a direita */
  .layout{display:block}
  .cover,.backcover{page:capa;width:100%%;height:297mm;max-height:none;aspect-ratio:auto}
  .cover{break-after:page}
  .backcover{break-before:page}
  .func-body{display:block!important}
  .func-arrow,.attach-btn,.no-evidence,.export-btn,.remove-img,.pdf-btn{display:none}
  .test-case,.func-card,.ck-group,.sign-box{break-inside:avoid}
  #assinaturas{break-before:page}
  .evidence-caption{border:none;background:none;padding:2px 0;text-align:center}
  .evidence-caption:placeholder-shown{display:none}
}
@media screen and (max-width:768px){
  .layout{flex-direction:column}
  .sidebar{width:100%%;height:auto;position:static}
  .content{padding:28px 16px}
  .sign-grid,.cover-meta{grid-template-columns:1fr 1fr}
}
""" % {"navy900": B.NAVY_900, "navy700": B.NAVY_700, "slate": B.SLATE, "verde": B.VERDE,
       "verde_apoio": B.VERDE_APOIO, "cinza": B.CINZA, "cinza_claro": B.CINZA_CLARO,
       "danger": B.DANGER, "font": B.FONT_STACK, "pt_texto": px(B.PT_TEXTO),
       "pt_h1": px(B.PT_TITULO_1), "pt_h2": px(B.PT_TITULO_2),
       "pt_abertura": px(B.PT_TITULO_ABERTURA), "pt_legenda": px(B.PT_LEGENDA)}


# ── JavaScript ─────────────────────────────────────────────────────

JS = """
function toggle(id){document.getElementById(id).classList.toggle('open')}

var SC=[{cls:'pendente',label:'\\u23F3 Pendente'},
        {cls:'aprovado',label:'\\u2705 Aprovado'},
        {cls:'reprovado',label:'\\u274C Reprovado'}];
function toggleStatus(btn){
  var cur=SC.findIndex(function(s){return btn.classList.contains(s.cls)});
  var next=SC[(cur+1)%SC.length];
  btn.setAttribute('class','status-btn '+next.cls);btn.textContent=next.label;
}

function attachImage(input,caseId){
  var files=input.files; if(!files||!files.length)return;
  var tc=document.getElementById(caseId);
  var ev=tc.querySelector('.test-evidence');
  var gallery=ev.querySelector('.evidence-gallery');
  if(!gallery){gallery=document.createElement('div');gallery.className='evidence-gallery';
    ev.insertBefore(gallery,ev.querySelector('.evidence-row'));}
  Array.prototype.forEach.call(files,function(file){
    var reader=new FileReader();
    reader.onload=function(e){
      var item=document.createElement('div');item.className='evidence-item';
      var img=document.createElement('img');img.src=e.target.result;img.title=file.name;
      img.setAttribute('alt','Evidencia: '+file.name);
      var rb=document.createElement('button');rb.className='remove-img';
      rb.type='button';rb.textContent='\\u2715';
      rb.setAttribute('onclick','removeImg(this,\\''+caseId+'\\')');
      var cap=document.createElement('input');cap.type='text';cap.className='evidence-caption';
      cap.placeholder='Descreva o que esta imagem mostra...';
      item.appendChild(img);item.appendChild(rb);item.appendChild(cap);gallery.appendChild(item);
      updateHint(caseId);
    };reader.readAsDataURL(file);
  });
  input.value='';
}

function removeImg(btn,caseId){btn.parentNode.remove();updateHint(caseId);}

function updateHint(caseId){
  var tc=document.getElementById(caseId);
  var hint=document.getElementById(caseId+'-hint'); if(!hint)return;
  var gallery=tc.querySelector('.evidence-gallery');
  var n=gallery?gallery.querySelectorAll('.evidence-item').length:0;
  hint.textContent=n===0?'Nenhuma imagem anexada':
    n+(n>1?' imagens anexadas':' imagem anexada');
}

/* Persiste no DOM o que so existe como propriedade, senao o outerHTML
   exportado perde os checkboxes marcados. */
function congelarEstado(){
  document.querySelectorAll('input[type=checkbox]').forEach(function(cb){
    if(cb.checked)cb.setAttribute('checked','checked');
    else cb.removeAttribute('checked');
  });
  document.querySelectorAll('input.evidence-caption').forEach(function(cap){
    cap.setAttribute('value',cap.value);
  });
}

function exportar(){
  congelarEstado();
  var clone=document.documentElement.cloneNode(true);
  clone.querySelectorAll('input[type=file]').forEach(function(i){i.value='';});
  var html='<!DOCTYPE html>\\n'+clone.outerHTML;
  var blob=new Blob([html],{type:'text/html;charset=utf-8'});
  var a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download=DOC_NOME;
  a.click();URL.revokeObjectURL(a.href);
}

/* localStorage e opaco em file:// em alguns navegadores — nunca deixar
   a excecao derrubar o resto do script. */
function ckSave(id){
  var cb=document.getElementById(id); if(!cb)return;
  if(cb.checked)cb.setAttribute('checked','checked');else cb.removeAttribute('checked');
  try{localStorage.setItem(CK_NS+id,cb.checked?'1':'0')}catch(e){}
}
(function(){
  try{
    document.querySelectorAll('.ck-box').forEach(function(cb){
      var v=localStorage.getItem(CK_NS+cb.id);
      if(v!==null)cb.checked=(v==='1');
    });
  }catch(e){}
})();

var secs=document.querySelectorAll('.section');
var navs=document.querySelectorAll('.nav-item');
window.addEventListener('scroll',function(){
  var cur='';
  secs.forEach(function(s){if(window.scrollY>=s.offsetTop-80)cur=s.id});
  navs.forEach(function(n){
    n.classList.toggle('active',n.getAttribute('href')==='#'+cur);
  });
},{passive:true});
"""

NOME = D.get("nome_customizacao", "Entrega")
JS_CONST = ("var DOC_NOME=%s;var CK_NS=%s;\n"
            % (json.dumps("Entrega - %s.html" % NOME),
               json.dumps("ck_%s_" % NOME)))


# ── Montagem ───────────────────────────────────────────────────────

HTML = (
    '<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '<meta name="doc-versao" content="%(versao)s">\n'
    '<title>Evidências de Entrega — %(nome)s v%(versao)s</title>\n'
    '<style>%(css)s</style>\n</head>\n<body>\n'
    '<div class="layout">\n'
    '<nav class="sidebar">\n'
    '<div class="sidebar-logo">%(logo)s'
    '<div class="s-brand">Evidências de entrega</div>'
    '<div class="s-title">%(nome)s</div>'
    '<div class="s-meta">v%(versao)s · %(data)s</div></div>\n'
    '<div class="nav">%(nav)s</div>\n'
    '%(export)s'
    '<button class="pdf-btn" type="button" onclick="window.print()">🖨️ Gerar PDF</button>\n'
    '</nav>\n'
    '<main class="main">%(capa)s<div class="content">%(main)s</div>%(contracapa)s</main>\n'
    '</div>\n<script>%(jsconst)s%(js)s</script>\n</body>\n</html>'
) % {
    "versao": h(VERSAO), "nome": h(NOME), "css": CSS, "logo": B.LOGO_SVG,
    "data": DATA_GERACAO, "nav": nav_html, "main": main_html,
    "capa": CAPA, "contracapa": CONTRACAPA, "js": JS, "jsconst": JS_CONST,
    # seta simples (U+2193): o glifo emoji U+2B07 falta em varias fontes
    "export": ('<button class="export-btn" type="button" onclick="exportar()">'
               '↓ Exportar com evidências</button>\n') if INCLUIR_HOMOLOGACAO else "",
}

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
    f.write(HTML)

print(json.dumps({"arquivo": ARQUIVO_SAIDA, "versao": VERSAO, "backup": BACKUP,
                  "evidencias_faltando": EVIDENCIAS_FALTANDO}))
