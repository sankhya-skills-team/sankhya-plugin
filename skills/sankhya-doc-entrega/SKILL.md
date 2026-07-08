---
name: sankhya-doc-entrega
description: >
  Esta skill deve ser utilizada quando o usuário quiser "gerar documento de entrega",
  "criar documento de entrega de desenvolvimento", "documentar módulo do addon",
  "gerar .docx de entrega", "documentar o que foi entregue", "gerar documentação Sankhya",
  ou qualquer variação de geração automática de documento de entrega para projetos Java Sankhya OM.
license: Proprietary
version: 2.1.0
---

# Gerador de Documento de Entrega de Desenvolvimento

## Objetivo

Gerar automaticamente `Documentacao/Entrega - {NOME_MODULO}.docx` a partir da análise dos fontes Java de um módulo Sankhya OM — Addon Studio ou Módulo Java complementar. Todo o conhecimento de estrutura, formatação e geração está embutido nesta skill; nenhum arquivo de contexto externo é necessário.

---

## Etapa 0 — Confirmar pasta raiz

Antes de qualquer coisa, determinar a pasta raiz do projeto executando:

```python
import os
print(os.getcwd())
```

Exibir o resultado ao usuário e perguntar:
> "A pasta raiz do projeto é `{cwd}`? Confirme ou informe o caminho correto."

Usar a resposta confirmada como `PASTA_RAIZ` em todos os caminhos desta skill.

---

## Etapa 1 — Coleta de inputs

Fazer as perguntas abaixo **em sequência**, aguardando resposta de cada uma:

**Pergunta 1 — Nome do módulo:**
> "Qual é o nome do módulo / entrega que será documentado? (Ex: Pesagem de Entrada, Contratos de Armazenagem)"

Usar como `NOME_MODULO` e como nome do arquivo de saída.

**Pergunta 2 — Pasta dos fontes Java:**
> "Informe o caminho da pasta onde estão os arquivos .java deste módulo. Pode ser relativo à raiz do projeto. (Ex: src/br/com/sankhya/dctm/pesagem/)"

Resolver o caminho absoluto: `PASTA_RAIZ + '/' + resposta`. Usar como `PASTA_FONTES`.

**Pergunta 3 — Documento de escopo (opcional):**
> "Existe um documento de escopo funcional para este módulo? Se sim, informe o caminho (.docx, .pdf ou .md). Se não, responda 'não'."

Usar como `ARQUIVO_ESCOPO` (pode ser vazio/None).

**Pergunta 4 — Caminho no sistema:**
> "Qual é o caminho de acesso à tela no sistema? (Ex: Menu > Beneficiamento > BEN - Registro de Amostra)"

Usar como `CAMINHO_SISTEMA`.

**Pergunta 5 — Identificação do cliente:**
> "Informe: Nome do cliente, Número do processo/FAP e Versão (ex: 1.0). Separe por vírgula ou responda em linhas separadas."

Extrair `PARCEIRO`, `NUMERO_FAP`, `VERSAO`.

---

## Etapa 2 — Análise dos fontes Java

Ler **todos os arquivos `.java`** dentro de `PASTA_FONTES` recursivamente usando Glob e Read.

Para cada arquivo, identificar a categoria com base na **interface/classe implementada**, aplicando o mapeamento completo descrito em `references/analise-fontes.md`. Resumo das interfaces reconhecidas:

- `AcaoRotinaJava` — botão de ação manual
- `EventoProgramavelJava` — listener automático (INSERT/UPDATE/DELETE)
- `ScheduledAction` — job agendado
- `Regra` / `RegraNegocioJava` — regra de negócio no ciclo de confirmação
- Classes com `CustomModuleLoader` — padrão External (proxy); **não** geram entrada separada em FUNCIONALIDADES

Para cada classe não-External, construir uma entrada em `FUNCIONALIDADES`:
- `titulo`: nome funcional descritivo
- `passos`: fluxo numerado em linguagem funcional (sem SQL, sem nomes de tabela)
- `obs`: bloqueios, pré-condições, grupos de usuário

**Detalhes de extração e regras de linguagem:** consultar `references/analise-fontes.md`.

---

## Etapa 3 — Leitura do documento de escopo (se fornecido)

Se `ARQUIVO_ESCOPO` foi informado, executar o Python abaixo para extrair o texto:

```python
import os, sys

def ler_escopo(caminho):
    ext = os.path.splitext(caminho)[1].lower()

    if ext == '.md':
        with open(caminho, encoding='utf-8') as f:
            return f.read()

    if ext in ('.docx', '.doc'):
        try:
            from docx import Document
            doc = Document(caminho)
            return '\n'.join(p.text for p in doc.paragraphs if p.text.strip())
        except Exception:
            # fallback: extrai XML sem dependência extra
            import zipfile, re
            with zipfile.ZipFile(caminho) as z:
                xml = z.read('word/document.xml').decode('utf-8')
            text = re.sub(r'<w:br[^/]*/>', '\n', xml)
            text = re.sub(r'<[^>]+>', '', text)
            return re.sub(r'\n{3,}', '\n\n', text).strip()

    if ext == '.pdf':
        # Tenta pdfplumber, depois pypdf, depois pypdf2
        for mod, fn in [
            ('pdfplumber', lambda: __import__('pdfplumber').open(caminho).__enter__()),
            ('pypdf',      lambda: None),
            ('PyPDF2',     lambda: None),
        ]:
            try:
                __import__(mod)
                if mod == 'pdfplumber':
                    import pdfplumber
                    with pdfplumber.open(caminho) as pdf:
                        return '\n'.join(p.extract_text() or '' for p in pdf.pages)
                else:
                    reader_cls = getattr(__import__(mod), 'PdfReader', None)
                    if reader_cls:
                        r = reader_cls(caminho)
                        return '\n'.join(page.extract_text() or '' for page in r.pages)
            except ImportError:
                continue
        # Se nenhum módulo disponível, instala pdfplumber
        os.system('pip install pdfplumber --break-system-packages -q')
        import pdfplumber
        with pdfplumber.open(caminho) as pdf:
            return '\n'.join(p.extract_text() or '' for p in pdf.pages)

    return ''

texto = ler_escopo(ARQUIVO_ESCOPO)
print(texto[:3000])  # imprimir para uso na análise
```

Usar o texto extraído para enriquecer **Objetivo** e **Descrição das Personalizações**.

---

## Etapa 4 — Montagem do conteúdo

Com base nas etapas 2 e 3, montar as variáveis de conteúdo (em português, linguagem funcional):

- `OBJETIVO`: 2–3 frases sobre o que o módulo entrega ao negócio
- `DESCRICAO_CUSTOMIZACAO`: resumo das automatizações implementadas
- `MODULO_AREA`: nome da tela/área no sistema
- `OBSERVACOES`: bullets com cada classe e seu papel funcional
- `PERMISSOES`: baseado em grupos de usuário encontrados nos fontes (procurar `GrupoUsuarioHelper`, `AuthenticationInfo`, alçadas `TSILIM`)
- `FUNCIONALIDADES`: lista ordenada — primeiro botões de ação, depois listeners, depois jobs, depois regras
- `LIMITACOES`: consolidado de todos os bloqueios (`MGEModelException`) + restrições de grupo + operações irreversíveis
- `PENDENCIAS`: itens que o cliente precisa configurar antes de usar

**Regras de linguagem e indicadores de permissão:** consultar `references/analise-fontes.md`.

---

## Etapa 5 — Geração do arquivo .docx

Executar o script Python abaixo **substituindo as variáveis de conteúdo** montadas na Etapa 4. O script é autocontido — nenhum arquivo externo necessário.

```python
import os, io, base64
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH

try:
    from docx import Document
except ImportError:
    os.system('pip install python-docx --break-system-packages -q')
    from docx import Document


# ════════════════════════════════════════════════════════════════════════════
# VARIÁVEIS DE CONTEÚDO — preencher com os dados da Etapa 4
# ════════════════════════════════════════════════════════════════════════════
PARCEIRO             = ""   # nome do cliente
NUMERO_FAP           = ""   # número do processo
RESPONSAVEL_TECNICO  = ""   # deixar em branco se não informado
VERSAO               = "1.0"
CIDADE_DATA          = "_______, ____ de _______ de ____"

NOME_MODULO          = ""   # nome do módulo entregue
ARQUIVO_SAIDA        = f"Documentacao/Entrega - {NOME_MODULO}.docx"

OBJETIVO             = ""
DESCRICAO_CUSTOMIZACAO = ""
MODULO_AREA          = ""
SOLICITANTE          = ""
OBSERVACOES          = ""

CAMINHO_SISTEMA      = ""
PERMISSOES           = (
    "• Todos os usuários com acesso ao módulo podem utilizar as funcionalidades básicas.\n"
    "• [Completar conforme perfis identificados nos fontes]"
)

# Lista de funcionalidades — cada item é um dict:
# { "titulo": str, "passos": str, "obs": str }
# passos e obs suportam '\n' para múltiplas linhas
FUNCIONALIDADES = []

LIMITACOES = ""
PENDENCIAS = "Necessário configurar os acessos do usuário de acordo com a necessidade e andamento das simulações com o cliente."

IMAGENS_ANEXOS = []

# ════════════════════════════════════════════════════════════════════════════
# CORES E CONSTANTES VISUAIS
# ════════════════════════════════════════════════════════════════════════════
GREEN     = (106, 168, 79)
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
GREEN_HEX = '6AA84F'

# ════════════════════════════════════════════════════════════════════════════
# HELPERS DE FORMATAÇÃO
# ════════════════════════════════════════════════════════════════════════════

def set_cell_shading(cell, fill_hex):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def add_run(para, text, bold=None, size=None, color=None):
    run = para.add_run(text)
    if bold  is not None: run.bold = bold
    if size  is not None: run.font.size = Pt(size)
    if color is not None: run.font.color.rgb = RGBColor(*color)
    return run

def add_custom_heading(doc, text, level=2):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    if level == 2:
        p.paragraph_format.space_before = Pt(24)
        p.paragraph_format.space_after  = Pt(6)
        run.font.size = Pt(14)
    elif level == 3:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after  = Pt(6)
        run.font.size = Pt(12)
    return p

def heading_func(doc, numero, nome):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after  = Pt(4)
    add_run(p, f"Funcionalidade {numero}", bold=True, color=BLACK)
    add_run(p, ": ", color=BLACK)
    add_run(p, nome, bold=False, color=BLACK)
    return p

def label_valor(doc, label, valor="", style='Normal'):
    p = doc.add_paragraph(style=style)
    add_run(p, label, bold=True)
    if valor:
        add_run(p, valor)
    return p

def print_multiline(doc, text, style='Normal', indent=0.0):
    for line in text.split('\n'):
        cleaned = line.strip()
        if cleaned:
            p = doc.add_paragraph(cleaned, style=style)
            if indent > 0:
                p.paragraph_format.left_indent = Cm(indent)

def passos_obs(doc, passos, obs, style='Normal'):
    for linha in passos.split('\n'):
        cleaned = linha.strip()
        if cleaned:
            doc.add_paragraph(cleaned, style=style)
    if obs:
        p_obs = doc.add_paragraph(style='Normal')
        add_run(p_obs, "Observações:", bold=True)
        for linha in obs.split('\n'):
            cleaned = linha.strip()
            if cleaned:
                p_o = doc.add_paragraph(cleaned, style='Normal')
                p_o.paragraph_format.left_indent = Cm(0.6)

def add_passo_a_passo_style(doc):
    styles = doc.styles
    try:
        return styles['passo a passo']
    except KeyError:
        style = styles.add_style('passo a passo', 1)
        style.base_style = styles['Normal']
        style.paragraph_format.left_indent  = Cm(1.25)
        style.paragraph_format.space_before = Pt(4)
        style.paragraph_format.space_after  = Pt(4)
        return style

def fill_sign_cell(cell, role, is_last_row=False):
    p1 = cell.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    p1.add_run("_______________________________________")
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    p2.add_run("Nome:").bold = True
    p3 = cell.add_paragraph()
    p3.paragraph_format.space_after = Pt(0) if is_last_row else Pt(36)
    p3.add_run(role)

# ════════════════════════════════════════════════════════════════════════════
# CRIAÇÃO DO DOCUMENTO
# ════════════════════════════════════════════════════════════════════════════

doc = Document()

for style in doc.styles:
    if hasattr(style, 'font'):
        style.font.name = 'Roboto'

add_passo_a_passo_style(doc)

for section in doc.sections:
    section.top_margin    = Cm(1.78)
    section.bottom_margin = Cm(1.60)
    section.left_margin   = Cm(2.14)
    section.right_margin  = Cm(1.43)

# (sem logo no cabecalho)

# ── Título do documento (verde Sankhya) ───────────────────────────────────
p_titulo = doc.add_paragraph(style='Normal')
add_run(p_titulo, "Entrega de Desenvolvimento", bold=True, size=16, color=GREEN)
p_titulo.paragraph_format.space_before = Pt(12)

# ── Subtítulo (nome do módulo) ────────────────────────────────────────────
p_sub = doc.add_paragraph(style='Normal')
add_run(p_sub, NOME_MODULO)
p_sub.paragraph_format.space_after = Pt(24)

# ── Tabela de Identificação ───────────────────────────────────────────────
id_table = doc.add_table(rows=5, cols=2)
id_table.style = 'Table Grid'
header_cell = id_table.rows[0].cells[0].merge(id_table.rows[0].cells[1])
set_cell_shading(header_cell, GREEN_HEX)
add_run(header_cell.paragraphs[0], "Identificação", bold=True, color=WHITE)
dados_id = [
    ("Parceiro:",               PARCEIRO),
    ("Número da FAP:",          NUMERO_FAP),
    ("Responsável Técnico:",    RESPONSAVEL_TECNICO),
    ("Versão da Customização:", VERSAO),
]
for i, (col0, col1) in enumerate(dados_id):
    row = id_table.rows[i + 1]
    row.cells[0].paragraphs[0].add_run(col0).bold = True
    row.cells[1].paragraphs[0].add_run(col1)

# ── Seção 1: Objetivos ────────────────────────────────────────────────────
add_custom_heading(doc, "1. Objetivos", level=2)
doc.add_paragraph(OBJETIVO, style='Normal')

# ── Seção 2: Descrição das Personalizações ───────────────────────────────
add_custom_heading(doc, "2. Descrição das Personalizações Realizadas", level=2)
label_valor(doc, "Descrição clara da customização: ", DESCRICAO_CUSTOMIZACAO)
label_valor(doc, "Módulo/Área: ",   MODULO_AREA)
label_valor(doc, "Solicitante: ",   SOLICITANTE)
label_valor(doc, "Observações: ",   OBSERVACOES)

# ── Seção 3: Manual de Uso ────────────────────────────────────────────────
add_custom_heading(doc, "3. Manual de Uso das Customizações", level=2)

add_custom_heading(doc, "3.1. Acesso às Novas Funcionalidades", level=3)
p_caminho = doc.add_paragraph(style='Normal')
add_run(p_caminho, "Caminho no sistema: ", bold=True)
add_run(p_caminho, CAMINHO_SISTEMA)
p_perm_label = doc.add_paragraph(style='Normal')
add_run(p_perm_label, "Permissões necessárias:", bold=True)
print_multiline(doc, PERMISSOES, indent=0.6)

add_custom_heading(doc, "3.2. Como Utilizar as Customizações", level=3)
for i, func in enumerate(FUNCIONALIDADES, start=1):
    heading_func(doc, i, func.get("titulo", ""))
    p_passo_hdr = doc.add_paragraph()
    p_passo_hdr.paragraph_format.space_after = Pt(2)
    add_run(p_passo_hdr, "Passo a Passo:", bold=True, size=11, color=BLACK)
    passos_obs(doc, func.get("passos", ""), func.get("obs", ""), style='passo a passo')

add_custom_heading(doc, "3.3. Limitações Conhecidas", level=3)
print_multiline(doc, LIMITACOES)

# ── Seção 4: Homologação e Testes ─────────────────────────────────────────
add_custom_heading(doc, "4. Homologação e Testes", level=2)
p_resp = doc.add_paragraph(style='Normal')
add_run(p_resp, "Responsável pelos testes no cliente:", bold=True)
add_run(p_resp, " [Nome e cargo]")
p_data = doc.add_paragraph(style='Normal')
add_run(p_data, "Data da homologação:", bold=True)
add_run(p_data, " [dd/mm/aaaa]")
p_result = doc.add_paragraph(style='Normal')
add_run(p_result, "Resultado:", bold=True)
add_run(p_result, " ✅ Aprovado | ❌ Reprovado (com pendências abaixo)")
p_pend_lbl = doc.add_paragraph("Pendências/Observações (se houver):", style='Normal')
p_pend_lbl.runs[0].bold = True
p_pend_lbl.paragraph_format.space_before = Pt(12)
print_multiline(doc, PENDENCIAS)

# ── Seção 5: Treinamento e Suporte ───────────────────────────────────────
add_custom_heading(doc, "5. Treinamento e Suporte", level=2)
p_trein = doc.add_paragraph(style='Normal')
add_run(p_trein, "Treinamento realizado em:", bold=True)
add_run(p_trein, " [Data]")
p_pub = doc.add_paragraph(style='Normal')
add_run(p_pub, "Público treinado:", bold=True)
add_run(p_pub, " [Equipe responsável]")
p_mat = doc.add_paragraph(style='Normal')
add_run(p_mat, "Material complementar:", bold=True)
doc.add_paragraph("[Link ou anexo do material]", style='Normal').paragraph_format.left_indent = Cm(0.6)
doc.add_paragraph("[Contato para suporte: e-mail, telefone, horário]", style='Normal').paragraph_format.left_indent = Cm(0.6)

# ── Seção 6: Anexos ──────────────────────────────────────────────────────
add_custom_heading(doc, "6. Anexos", level=2)
if IMAGENS_ANEXOS:
    for img_path in IMAGENS_ANEXOS:
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(12)
            p_img.paragraph_format.space_after  = Pt(24)
            p_img.add_run().add_picture(img_path, width=Inches(6.0))
else:
    doc.add_paragraph("[Inserir capturas de tela ou materiais complementares conforme necessário]", style='Normal')

# ── Observações finais ────────────────────────────────────────────────────
add_custom_heading(doc, "Observações", level=2)
doc.add_paragraph(
    "Por se tratar de uma personalização o Service Desk não atua nos casos de dúvidas ou "
    "incidentes, qualquer alteração ou suporte deverão ser negociadas horas adicionais com "
    "a Unidade para o atendimento.",
    style='Normal'
)

# ── Local, data e assinaturas ─────────────────────────────────────────────
p_cidade = doc.add_paragraph(CIDADE_DATA, style='Normal')
p_cidade.paragraph_format.space_before = Pt(40)
p_cidade.paragraph_format.space_after  = Pt(24)

sign_table = doc.add_table(rows=2, cols=3)
sign_table.autofit = False
sign_table.columns[0].width = Inches(2.8)
sign_table.columns[1].width = Inches(0.4)
sign_table.columns[2].width = Inches(2.8)
fill_sign_cell(sign_table.cell(0, 0), "Líder do Projeto")
fill_sign_cell(sign_table.cell(0, 2), "Gerente de Projetos – Sankhya")
fill_sign_cell(sign_table.cell(1, 0), "Consultor", is_last_row=True)
fill_sign_cell(sign_table.cell(1, 2), "Solicitante", is_last_row=True)

# ── Salvar ────────────────────────────────────────────────────────────────
os.makedirs("Documentacao", exist_ok=True)
doc.save(ARQUIVO_SAIDA)
print(f"✅ Documento gerado: {ARQUIVO_SAIDA}")
```

---

## Etapa 6 — Retorno ao usuário

Após gerar o arquivo, informar:

1. **Arquivo gerado:** `Documentacao/Entrega - {NOME_MODULO}.docx`
2. **Funcionalidades documentadas:** lista numerada com os títulos
3. **Campos que requerem preenchimento manual:**
   - Responsável pelos testes no cliente
   - Data da homologação
   - Resultado (Aprovado / Reprovado)
   - Data do treinamento e público treinado
   - Contato de suporte
   - Assinaturas (Líder do Projeto, Gerente de Projetos, Consultor, Solicitante)
4. **Aviso:**
   > "Revise o documento antes de enviar ao cliente. Para ajustes finos de formatação, abra no Word e use as correções necessárias."

---

## Referências

| Tópico | Arquivo |
|---|---|
| Categorias completas de artefatos, regras de extração por tipo de classe, regras de linguagem funcional, indicadores de permissão | `references/analise-fontes.md` |
| Nomes corretos de tabelas, campos, PKs e FKs do banco Sankhya OM (para documentar campos persistidos) | skill: **sankhya-dicionario** |
