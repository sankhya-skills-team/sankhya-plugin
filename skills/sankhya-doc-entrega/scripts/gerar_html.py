"""Gera o documento de entrega em HTML interativo.

Uso: python gerar_html.py <dados.json>
Contrato do JSON: ver secao "Contrato dados.json" no SKILL.md.
Imprime na saida padrao um JSON com {arquivo, versao, backup}.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _brand as B
from _comum import carregar_dados, parse_personas, resolver_versao

D = carregar_dados(sys.argv)

ARQUIVO_SAIDA = D["arquivo_saida"]
VERSAO, BACKUP, HISTORICO = resolver_versao(ARQUIVO_SAIDA, D.get("changelog"))
DATA_GERACAO = HISTORICO[0]["data"]

FUNCIONALIDADES     = D.get("funcionalidades", [])
CHECKLIST           = D.get("checklist_deploy", {}) or {}
INCLUIR_HOMOLOGACAO = bool(D.get("incluir_homologacao"))
INCLUIR_ASSINATURAS = bool(D.get("incluir_assinaturas"))
INCLUIR_DEPLOY      = bool(CHECKLIST.get("pre_requisitos") or CHECKLIST.get("pos_deploy"))
PERSONAS_SANKHYA    = parse_personas(D.get("personas_sankhya"))
PERSONAS_CLIENTE    = parse_personas(D.get("personas_cliente"))


def h(s):
    """Escapa caracteres HTML basicos."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
                  .replace(">", "&gt;").replace('"', "&quot;"))


# ── Blocos de conteudo ─────────────────────────────────────────────

def build_crumbs(caminho):
    partes = [p.strip() for p in str(caminho).split("›") if p.strip()]
    if not partes:
        return "<span class=\"crumb\">—</span>"
    saida = []
    for i, p in enumerate(partes):
        classe = "crumb crumb-last" if i == len(partes) - 1 else "crumb"
        saida.append('<span class="%s">%s</span>' % (classe, h(p)))
    return '<span class="path-sep">›</span>'.join(saida)


def build_passos(passos):
    itens = "".join(
        '<li><span class="step-n">%d</span><span>%s</span></li>' % (i, h(p))
        for i, p in enumerate(passos or [], 1)
    )
    return '<ol class="steps">%s</ol>' % itens


_AVISO_PERFIL = {
    "relatorio": "É necessário configurar os perfis de usuário que terão acesso ao relatório.",
    "tela":      "É necessário configurar os perfis de usuário que terão acesso à tela.",
    "dashboard": "É necessário configurar os perfis de usuário que terão acesso ao dashboard.",
}


def build_func_card(idx, func):
    meta = B.TIPO_META.get(func.get("tipo"), B.TIPO_META["acao"])
    fid = "fc%d" % idx
    blocos = build_passos(func.get("passos"))
    if func.get("obs"):
        blocos += '<div class="obs-box">%s</div>' % h(func["obs"])
    if func.get("limitacoes"):
        blocos += '<div class="lim-box">%s</div>' % h(func["limitacoes"])
    aviso = _AVISO_PERFIL.get(func.get("tipo_acesso", ""))
    if aviso:
        blocos += '<div class="obs-box">%s</div>' % aviso
    return (
        '<div class="func-card" id="%s" style="border-left-color:%s">'
        '<button class="func-header" type="button" onclick="toggle(\'%s\')">'
        '<span class="func-icon">%s</span>'
        '<span class="func-info">'
        '<span class="func-name">%s</span>'
        '<span class="tbadge" style="color:%s;border-color:%s">%s</span>'
        '</span><span class="func-arrow">›</span></button>'
        '<div class="func-body">%s</div></div>'
    ) % (fid, meta["cor"], fid, func.get("icone") or meta["icone"],
         h(func.get("titulo", "")), meta["cor"], meta["cor"], meta["badge"], blocos)


def build_homologacao(funcionalidades):
    saida = ""
    for fi, func in enumerate(funcionalidades, 1):
        testes = func.get("testes") or []
        if not testes:
            continue
        saida += ('<div class="hom-group"><div class="hom-title">%s %s</div>'
                  % (func.get("icone", ""), h(func.get("titulo", ""))))
        for ti, t in enumerate(testes, 1):
            tid = "hom-fc%d-%d" % (fi, ti)
            saida += (
                '<div class="test-case" id="%s">'
                '<div class="test-header">'
                '<button class="status-btn pendente" type="button" onclick="toggleStatus(this)">⏳ Pendente</button>'
                '<div class="test-desc">'
                '<div class="test-name">%s</div>'
                '<div class="test-expected"><strong>Resultado esperado:</strong> %s</div>'
                '</div></div>'
                '<div class="test-evidence">'
                '<div class="evidence-row">'
                '<label class="attach-btn">📎 Adicionar evidência'
                '<input type="file" accept="image/*" multiple onchange="attachImage(this,\'%s\')"></label>'
                '<span class="no-evidence" id="%s-hint">Nenhuma imagem anexada</span>'
                '</div></div></div>'
            ) % (tid, h(t.get("nome", "")), h(t.get("esperado", "")), tid, tid)
        saida += "</div>"
    return saida or '<p class="vazio">Nenhum teste de homologação gerado.</p>'


def build_limitacoes(lims):
    if not lims:
        return '<p class="vazio">Nenhuma limitação global identificada.</p>'
    itens = "".join('<li><span class="lim-icon">⚠</span><span>%s</span></li>' % h(l)
                    for l in lims)
    return '<ul class="lim-list">%s</ul>' % itens


def build_historico(entradas):
    linhas = ""
    for e in entradas:
        alts = e.get("alteracoes") or ["—"]
        itens = "".join("<li>%s</li>" % h(a) for a in alts)
        linhas += ('<tr><td class="hist-v">v%s</td><td class="hist-d">%s</td>'
                   '<td><ul class="hist-list">%s</ul></td></tr>'
                   % (h(e["versao"]), h(e["data"]), itens))
    return ('<table class="hist-table">'
            '<thead><tr><th>Versão</th><th>Data</th><th>Alterações</th></tr></thead>'
            '<tbody>%s</tbody></table>' % linhas)


def build_sign_grid(sankhya, cliente):
    def caixas(personas):
        if not personas:
            return '<div class="sign-box"><div class="sign-line"></div></div>'
        saida = ""
        for p in personas:
            nome = '<div class="sign-name">%s</div>' % h(p["nome"]) if p.get("nome") else ""
            fn = '<div class="sign-role">%s</div>' % h(p["funcao"]) if p.get("funcao") else ""
            saida += '<div class="sign-box"><div class="sign-line"></div>%s%s</div>' % (nome, fn)
        return saida
    return ('<div class="sign-grid">'
            '<div><div class="sign-col-title">Sankhya</div>%s</div>'
            '<div><div class="sign-col-title">Cliente</div>%s</div></div>'
            % (caixas(sankhya), caixas(cliente)))


TIPO_ICON = {"tela_adicional": "🖥️", "parametro": "⚙️", "script_sql": "🗄️",
             "acao": "▶️", "evento": "⚡", "job": "⏰", "regra": "📋",
             "jar": "📦", "dashboard": "📊", "relatorio": "📄"}
TIPO_LABEL = {"tela_adicional": "Tela Adicional", "parametro": "Parâmetro TSIPAR",
              "script_sql": "Script DDL", "acao": "Botão de Ação", "evento": "Evento",
              "job": "Job", "regra": "Regra", "jar": "Deploy JAR",
              "dashboard": "Dashboard", "relatorio": "Relatório"}

CAMPOS_DETALHE = [
    ("arquivo", "Arquivo", True), ("entidade", "Entidade", True),
    ("tipo_sankhya", "Tipo", False), ("classe", "Classe", True),
    ("perfis", "Perfis", False), ("descricao", None, False),
    ("tipo_valor", "Tipo", False), ("valor_padrao", "Padrão", True),
    ("caminho_servidor", "Destino", True), ("observacao", None, False),
]


def build_deploy(checklist):
    pre = checklist.get("pre_requisitos") or []
    pos = checklist.get("pos_deploy") or []
    if not pre and not pos:
        return '<p class="vazio">Nenhum artefato de deploy identificado.</p>'
    contador = [0]

    def item(it):
        contador[0] += 1
        cid = "ck%d" % contador[0]
        tipo = it.get("tipo", "")
        nome = it.get("nome_exibicao") or it.get("nome") or it.get("arquivo", "")
        detalhes = []
        for chave, rotulo, mono in CAMPOS_DETALHE:
            valor = it.get(chave)
            # Sem nome proprio, o arquivo virou o titulo: nao repetir no detalhe.
            if not valor or valor == nome:
                continue
            texto = "<code>%s</code>" % h(valor) if mono else h(valor)
            detalhes.append("%s: %s" % (rotulo, texto) if rotulo else texto)
        detalhe_html = ('<span class="ck-detail">%s</span>'
                        % " &nbsp;|&nbsp; ".join(detalhes)) if detalhes else ""
        return ('<div class="ck-item"><label class="ck-label">'
                '<input type="checkbox" class="ck-box" id="%s" onchange="ckSave(\'%s\')">'
                '<span class="ck-icon">%s</span>'
                '<span class="ck-badge">%s</span>'
                '<span class="ck-name">%s</span>%s</label></div>'
                % (cid, cid, TIPO_ICON.get(tipo, "•"),
                   TIPO_LABEL.get(tipo, tipo), h(nome), detalhe_html))

    def grupo(titulo, cor, itens):
        if not itens:
            return ""
        return ('<div class="ck-group">'
                '<div class="ck-group-header" style="border-left-color:%s">%s</div>%s</div>'
                % (cor, titulo, "".join(item(i) for i in itens)))

    return (grupo("Pré-requisitos — fazer ANTES do deploy", B.DANGER, pre)
            + grupo("Pós-deploy — configurar APÓS o JAR no servidor", B.WARNING, pos))


# ── Secoes ─────────────────────────────────────────────────────────

SECOES = [("identificacao", "🪪", "Identificação"),
          ("objetivo", "🎯", "Objetivo"),
          ("funcionalidades", "⚙️", "Funcionalidades"),
          ("limitacoes", "⚠️", "Limitações")]
if INCLUIR_DEPLOY:
    SECOES.append(("deploy", "🚀", "Checklist de Deploy"))
if INCLUIR_HOMOLOGACAO:
    SECOES.append(("homologacao", "🧪", "Homologação"))
if INCLUIR_ASSINATURAS:
    SECOES.append(("assinaturas", "✍️", "Assinaturas"))

CONTEUDO = {
    "identificacao": (
        '<table class="id-table"><tbody>'
        '<tr><td>Parceiro</td><td>%s</td></tr>'
        '<tr><td>ID Demanda</td><td>%s</td></tr>'
        '<tr><td>Versão</td><td><span class="vpill">v%s</span></td></tr>'
        '<tr><td>Data de Geração</td><td>%s</td></tr>'
        '<tr><td>Responsável Técnico</td><td>%s</td></tr>'
        '<tr><td>Nome da Customização</td><td>%s</td></tr>'
        '<tr><td>Caminho no Sistema</td><td><div class="path-crumbs">%s</div></td></tr>'
        '</tbody></table>'
        '<div class="sub-title">Histórico de versões</div>%s'
    ) % (h(D.get("parceiro", "")), h(D.get("id_demanda") or "—"), h(VERSAO),
         DATA_GERACAO, h(D.get("responsavel_tecnico", "")),
         h(D.get("nome_customizacao", "")), build_crumbs(D.get("caminho_sistema", "")),
         build_historico(HISTORICO)),
    "objetivo":       '<div class="obj-box">%s</div>' % h(D.get("objetivo", "")),
    "funcionalidades": "".join(build_func_card(i, f)
                               for i, f in enumerate(FUNCIONALIDADES, 1)),
    "limitacoes":     build_limitacoes(D.get("limitacoes_gerais")),
    "deploy":         build_deploy(CHECKLIST),
    "homologacao":    build_homologacao(FUNCIONALIDADES) if INCLUIR_HOMOLOGACAO else "",
    "assinaturas":    build_sign_grid(PERSONAS_SANKHYA, PERSONAS_CLIENTE),
}

nav_html = "".join(
    '<a class="nav-item%s" href="#%s"><span class="nav-icon">%s</span>%s</a>'
    % (" active" if i == 0 else "", sid, icone, titulo)
    for i, (sid, icone, titulo) in enumerate(SECOES)
)
main_html = "".join(
    '<section class="section" id="%s">'
    '<h2 class="section-title"><span class="s-num">%d</span>%s</h2>%s</section>'
    % (sid, i, titulo, CONTEUDO[sid])
    for i, (sid, _icone, titulo) in enumerate(SECOES, 1)
)


# ── CSS ────────────────────────────────────────────────────────────

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700&display=swap');
:root{
  --primary:%(primary)s;--secondary:%(secondary)s;--tertiary:%(tertiary)s;
  --surface:%(surface)s;--on-surface:%(on_surface)s;--danger:%(danger)s;--warning:%(warning)s;
  --r-md:3px;--r-lg:4px;--r-xl:5px;--r-full:9999px;
  --sh-sm:%(sh_sm)s;--sh-md:%(sh_md)s;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:%(font)s;background:var(--surface);color:var(--on-surface);
  font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased}
.layout{display:flex;min-height:100vh}

/* sidebar */
.sidebar{width:248px;flex-shrink:0;background:var(--tertiary);color:#fff;
  position:sticky;top:0;height:100vh;overflow-y:auto;display:flex;flex-direction:column}
.sidebar-logo{padding:20px 20px 16px;border-bottom:1px solid rgba(255,255,255,.1)}
.logo{height:24px;width:auto;display:block;color:#fff;margin-bottom:14px}
.s-brand{font-size:12px;font-weight:600;letter-spacing:1.4px;color:var(--primary);
  text-transform:uppercase;margin-bottom:4px}
.s-title{font-size:16px;font-weight:600;color:#fff;line-height:1.38}
.s-version{display:inline-block;margin-top:8px;background:rgba(74,222,128,.16);
  color:var(--primary);font-size:12px;font-weight:700;padding:2px 10px;
  border-radius:var(--r-full);border:1px solid rgba(74,222,128,.4)}
.s-meta{font-size:12px;color:rgba(255,255,255,.45);margin-top:6px}
.nav{padding:12px 0;flex:1}
.nav-item{display:flex;align-items:center;gap:10px;padding:9px 20px;
  color:rgba(255,255,255,.65);font-size:14px;text-decoration:none;
  border-left:3px solid transparent;transition:background .15s,color .15s}
.nav-item:hover{background:rgba(255,255,255,.06);color:#fff}
.nav-item.active{background:rgba(74,222,128,.12);color:var(--primary);border-left-color:var(--primary)}
.nav-icon{width:18px;text-align:center;flex-shrink:0}
.export-btn{margin:16px;background:var(--primary);color:var(--tertiary);border:none;
  border-radius:var(--r-lg);padding:10px 14px;font-family:inherit;font-size:14px;
  font-weight:600;cursor:pointer;width:calc(100%% - 32px)}
.export-btn:hover{filter:brightness(.94)}

/* main */
.main{flex:1;padding:40px;max-width:920px}
.section{margin-bottom:48px;scroll-margin-top:24px}
.section-title{font-size:20px;font-weight:600;color:var(--tertiary);margin-bottom:16px;
  padding-bottom:8px;border-bottom:2px solid var(--primary);display:flex;align-items:center;gap:10px}
.s-num{background:var(--primary);color:var(--tertiary);font-size:12px;font-weight:700;
  width:24px;height:24px;border-radius:var(--r-full);display:flex;
  align-items:center;justify-content:center;flex-shrink:0}
.sub-title{font-size:14px;font-weight:600;color:var(--tertiary);margin:28px 0 10px}
.vazio{color:#9CA3AF;font-size:14px}
.card,.id-table,.obj-box,.lim-list,.hist-table,.sign-box{
  background:#fff;border-radius:var(--r-xl);box-shadow:var(--sh-md)}

/* identificacao */
.id-table,.hist-table{width:100%%;border-collapse:collapse;overflow:hidden}
.id-table td,.hist-table td,.hist-table th{padding:10px 16px;font-size:14px;
  border-bottom:1px solid #EEF2F0;vertical-align:top;background:#fff}
.id-table td:first-child{font-weight:600;color:var(--tertiary);width:220px;white-space:nowrap}
.id-table tr:last-child td,.hist-table tr:last-child td{border-bottom:none}
.hist-table th{background:var(--tertiary);color:#fff;text-align:left;font-size:12px;
  font-weight:600;text-transform:uppercase;letter-spacing:.6px}
.hist-v{font-weight:700;color:var(--tertiary);white-space:nowrap;width:80px}
.hist-d{white-space:nowrap;width:110px}
.hist-list{list-style:none;padding:0}
.hist-list li{padding:1px 0}
.hist-list li::before{content:"—";color:var(--primary);margin-right:6px}
.vpill{background:rgba(74,222,128,.16);color:#15803D;border:1px solid var(--primary);
  font-size:12px;font-weight:700;padding:2px 10px;border-radius:var(--r-full)}
.path-crumbs{line-height:1.6}
.crumb{color:var(--on-surface)}
.crumb-last{color:var(--tertiary);font-weight:600}
.path-sep{color:#C7CDD4;margin:0 6px}
.obj-box{padding:18px 20px;font-size:16px;line-height:1.7;color:var(--on-surface)}

/* funcionalidades */
.func-card{background:#fff;border-radius:var(--r-xl);box-shadow:var(--sh-md);
  margin-bottom:12px;overflow:hidden;border-left:4px solid var(--secondary)}
.func-header{width:100%%;background:none;border:none;font-family:inherit;text-align:left;
  padding:14px 18px;cursor:pointer;display:flex;align-items:center;gap:12px}
.func-icon{font-size:20px;flex-shrink:0}
.func-info{flex:1;display:flex;flex-direction:column;gap:5px;align-items:flex-start}
.func-name{font-size:16px;font-weight:600;color:var(--tertiary);line-height:1.38}
.tbadge{display:inline-block;padding:1px 10px;border-radius:var(--r-full);
  font-size:12px;font-weight:600;border:1px solid currentColor;background:#fff}
.func-arrow{font-size:16px;color:#C7CDD4;transition:transform .2s;flex-shrink:0}
.func-card.open .func-arrow{transform:rotate(90deg)}
.func-body{display:none;border-top:1px solid #EEF2F0;padding:16px 18px 18px}
.func-card.open .func-body{display:block}
.steps{list-style:none;padding:0;counter-reset:none}
.steps li{font-size:14px;line-height:1.6;padding:6px 0;display:flex;gap:12px;
  border-bottom:1px solid #F5F7F6}
.steps li:last-child{border-bottom:none}
.step-n{color:var(--tertiary);background:rgba(74,222,128,.22);font-weight:700;font-size:12px;
  flex-shrink:0;width:20px;height:20px;border-radius:var(--r-full);
  display:flex;align-items:center;justify-content:center;margin-top:1px}
.obs-box{background:#FFFBEB;border-left:3px solid var(--warning);border-radius:var(--r-md);
  padding:10px 14px;font-size:14px;line-height:1.5;color:#78350F;margin-top:12px}
.lim-box{background:#FEF2F2;border-left:3px solid var(--danger);border-radius:var(--r-md);
  padding:10px 14px;font-size:14px;line-height:1.5;color:#7F1D1D;margin-top:12px}

/* limitacoes */
.lim-list{padding:16px 20px;list-style:none}
.lim-list li{font-size:14px;line-height:1.6;padding:6px 0;display:flex;gap:12px;
  border-bottom:1px solid #F5F7F6}
.lim-list li:last-child{border-bottom:none}
.lim-icon{flex-shrink:0;color:var(--danger)}

/* deploy */
.ck-group{margin-bottom:16px}
.ck-group-header{padding:9px 16px;border-left:4px solid var(--danger);background:#fff;
  border-radius:var(--r-xl) var(--r-xl) 0 0;font-size:14px;font-weight:600;
  color:var(--tertiary);box-shadow:var(--sh-sm)}
.ck-item{background:#fff;border-top:1px solid #EEF2F0;padding:10px 16px}
.ck-item:last-child{border-radius:0 0 var(--r-xl) var(--r-xl)}
.ck-item:has(.ck-box:checked){background:#F0FDF4}
.ck-label{display:flex;align-items:center;gap:8px;cursor:pointer;font-size:14px;flex-wrap:wrap}
.ck-box{width:16px;height:16px;accent-color:var(--tertiary);cursor:pointer;flex-shrink:0}
.ck-badge{background:#F3F4F6;color:var(--on-surface);font-size:12px;font-weight:600;
  padding:1px 8px;border-radius:var(--r-full);white-space:nowrap;flex-shrink:0}
.ck-name{font-weight:600;color:var(--tertiary)}
.ck-detail{font-size:12px;color:#6B7280;line-height:1.5}
code{font-family:ui-monospace,Consolas,monospace;font-size:12px;background:#F3F4F6;
  padding:1px 5px;border-radius:var(--r-md)}

/* homologacao */
.hom-group{margin-bottom:28px}
.hom-title{font-size:14px;font-weight:600;color:var(--tertiary);margin-bottom:10px;
  display:flex;align-items:center;gap:8px}
.test-case{background:#fff;border-radius:var(--r-xl);box-shadow:var(--sh-sm);
  margin-bottom:12px;overflow:hidden}
.test-header{display:flex;align-items:flex-start;gap:12px;padding:12px 16px}
.status-btn{border:1px solid transparent;font-family:inherit;cursor:pointer;font-size:12px;
  font-weight:600;padding:3px 12px;border-radius:var(--r-full);white-space:nowrap;flex-shrink:0}
.status-btn.pendente{background:#F3F4F6;color:#9CA3AF;border-color:#E5E7EB}
.status-btn.aprovado{background:rgba(74,222,128,.18);color:#15803D;border-color:var(--primary)}
.status-btn.reprovado{background:#FEE2E2;color:var(--danger);border-color:#FCA5A5}
.test-desc{flex:1}
.test-name{font-size:14px;font-weight:600;color:var(--tertiary);margin-bottom:3px}
.test-expected{font-size:14px;color:var(--on-surface);line-height:1.43}
.test-evidence{padding:10px 16px;border-top:1px solid #EEF2F0}
.evidence-gallery{display:flex;flex-direction:column;gap:8px;margin-bottom:8px}
.evidence-item{position:relative}
.evidence-item img{width:100%%;max-height:420px;object-fit:contain;border-radius:var(--r-lg);
  border:1px solid #EEF2F0;display:block;background:var(--surface)}
.evidence-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.attach-btn{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;
  color:var(--tertiary);background:rgba(74,222,128,.1);border:1px dashed var(--primary);
  border-radius:var(--r-lg);padding:5px 12px;cursor:pointer}
.attach-btn input[type=file]{display:none}
.remove-img{position:absolute;top:6px;right:6px;background:#fff;border:1px solid #FCA5A5;
  color:var(--danger);padding:2px 7px;border-radius:var(--r-lg);font-size:12px;cursor:pointer}
.no-evidence{font-size:12px;color:#9CA3AF;font-style:italic}

/* assinaturas */
.sign-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}
.sign-col-title{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:1.2px;
  color:#9CA3AF;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid #E5E7EB}
.sign-box{padding:16px 18px 14px;text-align:center;margin-bottom:12px}
.sign-line{border-bottom:1px solid #C7CDD4;margin:36px 12px 10px}
.sign-name{font-size:14px;font-weight:600;color:var(--tertiary)}
.sign-role{font-size:12px;color:#6B7280;margin-top:2px}

@media print{
  body{background:#fff}
  .sidebar{display:none}
  .main{padding:0;max-width:100%%}
  .func-body{display:block!important}
  .func-arrow,.attach-btn,.no-evidence,.export-btn,.remove-img{display:none}
  .test-case,.func-card,.ck-group{page-break-inside:avoid}
}
@media (max-width:768px){
  .layout{flex-direction:column}
  .sidebar{width:100%%;height:auto;position:static}
  .main{padding:24px 20px}
  .sign-grid{grid-template-columns:1fr}
}
""" % {"primary": B.PRIMARY, "secondary": B.SECONDARY, "tertiary": B.TERTIARY,
       "surface": B.SURFACE, "on_surface": B.ON_SURFACE, "danger": B.DANGER,
       "warning": B.WARNING, "font": B.FONT_STACK,
       "sh_sm": B.SHADOW_SM, "sh_md": B.SHADOW_MD}


# ── JavaScript ─────────────────────────────────────────────────────

JS = """
function toggle(id){document.getElementById(id).classList.toggle('open')}

var SC=[{cls:'pendente',label:'\\u23F3 Pendente'},
        {cls:'aprovado',label:'\\u2705 Aprovado'},
        {cls:'reprovado',label:'\\u274C Reprovado'}];
function toggleStatus(btn){
  var cur=SC.findIndex(function(s){return btn.classList.contains(s.cls)});
  var next=SC[(cur+1)%SC.length];
  SC.forEach(function(s){btn.classList.remove(s.cls)});
  btn.classList.add(next.cls);btn.textContent=next.label;
  btn.setAttribute('class','status-btn '+next.cls);
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
      item.appendChild(img);item.appendChild(rb);gallery.appendChild(item);
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
    '<title>Entrega — %(nome)s v%(versao)s</title>\n'
    '<style>%(css)s</style>\n</head>\n<body>\n'
    '<div class="layout">\n'
    '<nav class="sidebar">\n'
    '<div class="sidebar-logo">%(logo)s'
    '<div class="s-brand">Entrega de Desenvolvimento</div>'
    '<div class="s-title">%(nome)s</div>'
    '<div class="s-version">v%(versao)s</div>'
    '<div class="s-meta">Gerado em %(data)s</div></div>\n'
    '<div class="nav">%(nav)s</div>\n'
    '%(export)s'
    '</nav>\n'
    '<main class="main">%(main)s</main>\n'
    '</div>\n<script>%(jsconst)s%(js)s</script>\n</body>\n</html>'
) % {
    "versao": h(VERSAO), "nome": h(NOME), "css": CSS, "logo": B.LOGO_SVG,
    "data": DATA_GERACAO, "nav": nav_html, "main": main_html,
    "js": JS, "jsconst": JS_CONST,
    # seta simples (U+2193): o glifo emoji U+2B07 falta em varias fontes
    "export": ('<button class="export-btn" type="button" onclick="exportar()">'
               '↓ Exportar com evidências</button>\n') if INCLUIR_HOMOLOGACAO else "",
}

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
    f.write(HTML)

print(json.dumps({"arquivo": ARQUIVO_SAIDA, "versao": VERSAO, "backup": BACKUP}))
