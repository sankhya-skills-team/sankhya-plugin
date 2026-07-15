---
name: gerar-doc-entrega-dev
description: >
  Esta skill deve ser utilizada quando o usuário quiser "gerar documento de entrega",
  "criar documento de entrega de desenvolvimento", "documentar módulo do addon",
  "gerar .html de entrega", "gerar .docx de entrega", "documentar o que foi entregue",
  "gerar documentação Sankhya", ou qualquer variação de geração automática de documento
  de entrega para projetos Java Sankhya OM. Gera em dois formatos, à escolha do usuário:
  HTML interativo (colapsáveis, homologação com evidências, checklist de deploy) ou
  DOCX Word (editável, com tabela de identificação e bloco de assinaturas).
---

# Gerador de Documento de Entrega de Desenvolvimento

## Objetivo

Gerar automaticamente o documento de entrega — `Documentacao/Entrega - {NOME_CUSTOMIZACAO}.{html|docx}` — a partir da análise dos fontes Java de um módulo Sankhya OM (Addon Studio ou Módulo Java complementar). O usuário escolhe o formato:

- **HTML interativo** (default): funcionalidades colapsáveis, testes de homologação com marcação de status e evidências por imagem, checklist de deploy, botão "Exportar com evidências". Fluxo completo.
- **DOCX Word**: documento editável no Word com tabela de identificação, manual de uso, homologação em texto e bloco de assinaturas. Fluxo enxuto (sem homologação interativa, deploy-scan nem personas).

A análise dos fontes Java (Etapas de análise) e a leitura do escopo são idênticas nos dois formatos; só a **coleta de inputs extras** e a **geração final** ramificam por formato.

---

## Etapa 0 — Confirmar pasta raiz

```python
import os
print(os.getcwd())
```

Exibir o resultado e perguntar:
> "A pasta raiz do projeto é `{cwd}`? Confirme ou informe o caminho correto."

Usar a resposta como `PASTA_RAIZ`.

---

## Etapa 0.5 — Formato do documento

Perguntar:
> "Em qual formato deseja o documento de entrega? (`html` interativo — default, ou `docx` Word editável)"

Armazenar como `FORMATO` (`"html"` ou `"docx"`; se o usuário não responder, usar `"html"`).

- **`FORMATO = "html"`** → seguir todas as etapas normalmente.
- **`FORMATO = "docx"`** → na Etapa 1 **pular** as perguntas de homologação (8), assinaturas (9, 9a, 9b); **pular** as Etapas 3B (scan de deploy) e 6 (testes de homologação); gerar pela **Etapa 7-DOCX** em vez da Etapa 7.

---

## Etapa 1 — Coleta de inputs

Fazer **todas** as perguntas abaixo **em sequência**, aguardando resposta de cada uma. Só iniciar execução após a última resposta ser coletada.

**Pergunta 1 — Parceiro:**
> "Qual é o nome do cliente / parceiro?"

**Pergunta 2 — ID Demanda:**
> "Informe o ID da demanda (ex: DEM-1234, chamado, ticket). Se não houver, responda 'não'."

Armazenar como `ID_DEMANDA`. Se "não", usar string vazia.

**Pergunta 2b — Pasta da demanda:**
> "Qual é o nome da pasta da demanda no projeto? (Ex: nomedemanda, DEM-1234)"

Armazenar como `PASTA_DEMANDA`.

**Pergunta 3 — Nome da customização:**
> "Qual é o nome da customização entregue? (Ex: Pesagem de Entrada, Controle de Fixação)"

Usar como `NOME_CUSTOMIZACAO` e como base do nome do arquivo de saída.

**Pergunta 4 — Caminho no sistema:**
> "Qual é o caminho de acesso no sistema? (Ex: Menu › Beneficiamento › BEN — Pesagem de Entrada)"

**Pergunta 5 — Pasta dos fontes Java:**
> "Informe o caminho da pasta com os arquivos .java deste módulo. Pode ser relativo à raiz. (Ex: src/br/com/sankhya/dctm/pesagem/)"

Resolver o caminho absoluto: `PASTA_RAIZ + '/' + resposta`. Usar como `PASTA_FONTES`.

**Pergunta 6 — Documento de escopo:**
> "Existe documento de escopo funcional? Informe o caminho (.docx, .pdf ou .md). Se não, responda 'não'."

**Pergunta 7 — Responsável(eis) técnico(s):**
> "Quem desenvolveu este módulo? Se houve passagem de responsabilidade, informe como: 'Dev A → Dev B (a partir da v1.1)'."

> **As perguntas 8 e 9 abaixo são exclusivas do `FORMATO = "html"`.** Se `FORMATO = "docx"`, pular as três e definir `INCLUIR_HOMOLOGACAO = False`, `INCLUIR_ASSINATURAS = True` (o DOCX sempre inclui o bloco de assinaturas padrão), `TEXTO_PERSONAS_SANKHYA = ""` e `TEXTO_PERSONAS_CLIENTE = ""`.

**Pergunta 8 — Bloco de Homologação (só HTML):**
> "Deseja incluir o bloco de homologação (testes de aceitação) no documento? (sim/não)"

Armazenar como `INCLUIR_HOMOLOGACAO` (`True` se "sim", `False` se "não").

**Pergunta 9 — Bloco de Assinaturas:**
> "Deseja incluir o bloco de assinaturas no documento? (sim/não)"

Armazenar como `INCLUIR_ASSINATURAS` (`True` se "sim", `False` se "não").

Se `INCLUIR_ASSINATURAS = True`, fazer as duas perguntas adicionais abaixo:

**Pergunta 9a — Personas Sankhya:**
> "Informe as personas da Sankhya (nome — função), uma por linha:
> Ex:
> Fulano de Tal — Consultor
> Ana Paula Souza — Gerente de Projetos"

Armazenar como `TEXTO_PERSONAS_SANKHYA`.

**Pergunta 9b — Personas Cliente:**
> "Informe as personas do cliente (nome — função), uma por linha:
> Ex:
> Roberto Mendes — Diretor Comercial
> Júlia Lima — Analista de Processos"

Armazenar como `TEXTO_PERSONAS_CLIENTE`.

Se `INCLUIR_ASSINATURAS = False`, definir `TEXTO_PERSONAS_SANKHYA = ""` e `TEXTO_PERSONAS_CLIENTE = ""`.

---

## Etapa 2 — Versionamento

```python
import os, re

NOME_ARQUIVO   = f"Entrega - {NOME_CUSTOMIZACAO}.html"
PASTA_DOC      = os.path.join(PASTA_RAIZ, PASTA_DEMANDA, "Documentacao")
ARQUIVO_SAIDA  = os.path.join(PASTA_DOC, NOME_ARQUIVO)

if os.path.exists(ARQUIVO_SAIDA):
    with open(ARQUIVO_SAIDA, encoding='utf-8') as f:
        conteudo = f.read()
    match = re.search(r'v(\d+)\.(\d+)', conteudo[:600])
    if match:
        major, minor = int(match.group(1)), int(match.group(2))
        versao_anterior = f"{major}.{minor}"
        VERSAO = f"{major}.{minor + 1}"
    else:
        versao_anterior = "1.0"
        VERSAO = "1.1"
    backup = os.path.join(PASTA_DOC,
                          f"Entrega - {NOME_CUSTOMIZACAO} v{versao_anterior}.html")
    os.rename(ARQUIVO_SAIDA, backup)
    print(f"Backup da versão {versao_anterior} salvo em: {backup}")
else:
    VERSAO = "1.0"
    print(f"Primeira geração — versão: {VERSAO}")
```

---

## Etapa 3 — Análise dos fontes Java

Ler **todos os arquivos `.java`** dentro de `PASTA_FONTES` recursivamente usando Glob e Read.

Para cada arquivo, identificar a categoria com base na **interface/classe implementada**, aplicando o mapeamento completo descrito em `references/analise-fontes.md`:

- `AcaoRotinaJava` → tipo `"acao"`
- `EventoProgramavelJava` → tipo `"evento"`
- `ScheduledAction` → tipo `"job"`
- `Regra` / `RegraNegocioJava` → tipo `"regra"`
- Classes com `CustomModuleLoader` → padrão External — **não geram entrada separada**

Para cada classe não-External, construir entrada em `FUNCIONALIDADES` (lista Python):

```python
FUNCIONALIDADES = [
    {
        "titulo":     "",   # nome funcional descritivo (sem SQL, sem nomes de tabela)
        "tipo":       "",   # "acao" | "evento" | "job" | "regra"
        "icone":      "",   # emoji representativo do comportamento
        "passos":     [],   # lista de strings — fluxo em linguagem funcional
        "obs":        "",   # pré-condições, perfis, alçadas (vazio se não houver)
        "limitacoes": "",   # bloqueios MGEModelException, restrições (vazio se não houver)
        "tipo_acesso": "", # "relatorio" | "tela" | "dashboard" | "" — exibe aviso de perfis no HTML
    }
]
```

**Se `INCLUIR_HOMOLOGACAO = True`**, durante a análise de cada classe extrair também os **slots de teste** e adicioná-los à entrada correspondente em `FUNCIONALIDADES`:

```python
{
    # ... campos acima ...
    "slots": {
        "condicao_valida":   "",  # condição/estado específico que permite execução (extraído do fonte)
        "condicao_invalida": "",  # condição/estado que deve ser bloqueado (extraído do fonte)
        "mensagem_bloqueio": "",  # texto exato ou próximo do lançado em MGEModelException / throw
        "resultado_principal":"", # o que ocorre com sucesso (registro criado, campo atualizado, etc.)
        "perfil":            "",  # perfil/permissão requerido identificado no fonte; "—" se não identificado
    }
}
```

Regras de extração dos slots:
- `mensagem_bloqueio`: copiar a string literal do `throw new MGEModelException("...")` ou equivalente. Se houver mais de um bloqueio, usar o principal (primeiro ou mais restritivo).
- `condicao_invalida`: derivar diretamente da condição que dispara o bloqueio no código (ex.: status diferente de "A", campo nulo, etc.).
- `condicao_valida`: inverso lógico de `condicao_invalida` (ex.: status igual a "A", campo preenchido, etc.).
- `resultado_principal`: o que o código efetivamente persiste ou retorna em caso de sucesso.
- Se algum slot não for identificável no fonte, usar `"não identificado"` — **nunca inventar**.

Construir também:
- `OBJETIVO_RASCUNHO` — 2–3 frases sobre o que o módulo entrega ao negócio
- `LIMITACOES_GERAIS` — lista de strings com limitações globais do módulo

**Ordenação de FUNCIONALIDADES:** botões de ação → listeners → jobs → regras.

**Campo `tipo_acesso`:** definir ao identificar a funcionalidade:
- Título contém "relatório", "report" ou há `.jrxml` associado → `"relatorio"`
- Funcionalidade representa tela adicional → `"tela"`
- Funcionalidade representa dashboard → `"dashboard"`
- Demais casos → `""` (vazio)
Se não for possível determinar na Etapa 3, o campo será complementado no drill-down da Etapa 3B.5.

**Regras de linguagem:** consultar `references/analise-fontes.md`.

---

## Etapa 3B — Scan de Artefatos de Deploy

> **Só HTML.** Se `FORMATO = "docx"`, pular toda a Etapa 3B (o DOCX não tem checklist de deploy).

Executar após a Etapa 3. Construir `CHECKLIST_DEPLOY` com dois grupos: `pre_requisitos` e `pos_deploy`.

### 3B.1 — Extrair metadados Javadoc das classes Java

Para cada arquivo `.java` já lido na Etapa 3, extrair o bloco `Configuracao no Sankhya:` do Javadoc. Padrão esperado:

```java
/**
 * Acao "Nome Exibido no Sankhya" da tela ENTIDADE.
 *
 * Configuracao no Sankhya:
 *   Entidade: ENTIDADE
 *   Tipo: AcaoRotinaJava
 *   Classe: br.com.sankhya...
 */
```

Extrair via regex:
- **Nome exibido**: string entre aspas na primeira linha descritiva do Javadoc (ex: `"Calcular PROTEGE/GO"`)
- **Pares chave-valor** do bloco `Configuracao no Sankhya:` (Entidade, Tipo, Classe, etc.)

Se o bloco não existir na classe, os campos ficam vazios — serão complementados no passo 3B.5.

Construir lista `ARTEFATOS_JAVA` (excluir classes `CustomModuleLoader`):

```python
ARTEFATOS_JAVA = [
    {
        "nome_exibicao": "",   # extraído do Javadoc ou vazio
        "entidade":      "",   # campo Entidade do Javadoc
        "tipo_sankhya":  "",   # campo Tipo (AcaoRotinaJava, EventoProgramavelJava, etc.)
        "classe":        "",   # campo Classe (FQN completo)
        "tipo_artefato": "",   # "acao" | "evento" | "job" | "regra"
        "perfis":        "",   # preenchido no drill-down interativo
    }
]
```

### 3B.2 — Scan de arquivos de deploy

Usar Glob para localizar:

- Telas adicionais: `{PASTA_DEMANDA}/Telas Adicionais/**/*.zip`
- Scripts DDL: `{PASTA_DEMANDA}/Objetos de Banco/**/*.sql`
- JARs gerados: `dist/**/*.jar`
- Dashboards: `dist/Dashboards/**/*.zip`

### 3B.3 — Detecção de parâmetros TSIPAR

Usar Grep com padrão `TSIPAR` nos arquivos `.sql` e `.java` em `PASTA_FONTES`. Extrair nomes únicos de parâmetros (valor entre aspas simples ou duplas após referência a TSIPAR, ex: `'PROTEGE_ALIQ'`).

Construir lista `PARAMETROS_DETECTADOS` (pode ser vazia).

### 3B.4 — Montar CHECKLIST_DEPLOY

```python
CHECKLIST_DEPLOY = {
    "pre_requisitos": [
        # Telas adicionais — um item por ZIP encontrado
        # {"tipo": "tela_adicional", "nome": "AD_PROTEGECAB", "arquivo": "Metadados_AD_PROTEGECAB.zip", "observacao": ""}

        # Parâmetros detectados — um item por parâmetro único
        # {"tipo": "parametro", "nome": "PROTEGE_ALIQ", "descricao": "", "tipo_valor": "", "valor_padrao": ""}

        # Scripts DDL — um item por .sql encontrado
        # {"tipo": "script_sql", "nome": "create_ad_xxx.sql", "observacao": ""}
    ],
    "pos_deploy": [
        # Artefatos Java — um item por classe em ARTEFATOS_JAVA
        # {"tipo": "acao", "nome_exibicao": "Calcular PROTEGE/GO", "entidade": "AD_PROTEGECAB",
        #  "tipo_sankhya": "AcaoRotinaJava", "classe": "br.com...", "perfis": ""}

        # JARs — um item por JAR encontrado
        # {"tipo": "jar", "arquivo": "id2009protege-1.0.0.jar", "caminho_servidor": ""}

        # Dashboards — um item por ZIP encontrado
        # {"tipo": "dashboard", "arquivo": "id2009xxx.zip", "observacao": ""}
    ]
}
```

### 3B.5 — Checklist interativo

Apresentar a lista detectada numerada ao usuário:

> "Itens detectados para o **Checklist de Deploy**:
>
> **🔴 Pré-requisitos** (fazer ANTES do deploy):
> 1. [Tela Adicional] `AD_PROTEGECAB.zip`
> 2. [Parâmetro TSIPAR] `PROTEGE_ALIQ`
>
> **🟡 Pós-Deploy** (configurar APÓS o JAR no servidor):
> 3. [Botão de Ação] `Calcular PROTEGE/GO` — Entidade: `AD_PROTEGECAB` | Tipo: `AcaoRotinaJava`
> 4. [JAR] `id2009protege-1.0.0.jar`
>
> Deseja detalhar ou ajustar algum item? (`1,3` / `todos` / `ok`)"

**Para cada item selecionado**, fazer as perguntas correspondentes:

| Tipo | Perguntas |
|---|---|
| `tela_adicional` | "Campos adicionais a documentar além do ZIP? Dependência de outra tela? Qual entrada em FUNCIONALIDADES esta tela representa? (número ou título — Enter para pular)" |
| `parametro` | "Descrição, tipo (texto/número/data), valor padrão?" |
| `script_sql` | "Executar em qual ambiente? (teste / produção / ambos)" |
| `acao` / `evento` / `job` / `regra` | "Nome exibido correto? Entidade correta? Quais perfis têm acesso?" |
| `jar` | "Caminho de destino no servidor? (Enter = padrão Sankhya)" |
| `dashboard` | "Nome exibido do dashboard no Sankhya? Qual entrada em FUNCIONALIDADES este dashboard representa? (número ou título — Enter para pular)" |
| `relatorio` | "Nome exibido no Sankhya? Qual entrada em FUNCIONALIDADES este relatório representa? (número ou título — Enter para pular)" |

Quando o usuário indicar a funcionalidade correspondente para `tela_adicional`, `dashboard` ou `relatorio`, setar `FUNCIONALIDADES[idx]["tipo_acesso"]` com `"tela"`, `"dashboard"` ou `"relatorio"` respectivamente.

Após finalizar, perguntar:

> "Há itens não detectados automaticamente? (parâmetros extras, scripts, telas) Informe ou responda `não`."

Adicionar itens informados ao grupo correspondente em `CHECKLIST_DEPLOY`.

---

## Etapa 4 — Leitura do escopo (se fornecido)

Se documento de escopo foi informado, extrair o texto:

```python
import os

def ler_escopo(caminho):
    ext = os.path.splitext(caminho)[1].lower()
    if ext == '.md':
        with open(caminho, encoding='utf-8') as f:
            return f.read()
    if ext in ('.docx', '.doc'):
        try:
            from docx import Document
            return '\n'.join(p.text for p in Document(caminho).paragraphs if p.text.strip())
        except ImportError:
            import zipfile, re as _re
            with zipfile.ZipFile(caminho) as z:
                xml = z.read('word/document.xml').decode('utf-8')
            return _re.sub(r'\n{3,}', '\n\n', _re.sub(r'<[^>]+>', '', xml)).strip()
    if ext == '.pdf':
        for mod in ['pdfplumber', 'pypdf', 'PyPDF2']:
            try:
                __import__(mod)
                if mod == 'pdfplumber':
                    import pdfplumber
                    with pdfplumber.open(caminho) as pdf:
                        return '\n'.join(p.extract_text() or '' for p in pdf.pages)
                else:
                    r = getattr(__import__(mod), 'PdfReader')(caminho)
                    return '\n'.join(p.extract_text() or '' for p in r.pages)
            except ImportError:
                continue
        os.system('pip install pdfplumber --break-system-packages -q')
        import pdfplumber
        with pdfplumber.open(caminho) as pdf:
            return '\n'.join(p.extract_text() or '' for p in pdf.pages)
    return ''

texto_escopo = ler_escopo(ARQUIVO_ESCOPO)
print(texto_escopo[:3000])
```

Usar o texto para enriquecer `OBJETIVO_RASCUNHO` e os `passos` das funcionalidades.

---

## Etapa 5 — Confirmação do objetivo

Exibir ao usuário:

> "O objetivo abaixo foi gerado a partir da análise dos fontes. Edite se necessário e confirme:
>
> ---
> {OBJETIVO_RASCUNHO}
> ---"

Aguardar confirmação ou texto editado. Usar resposta como `OBJETIVO`.

---

## Etapa 6 — Geração dos testes de homologação

**Executar somente se `INCLUIR_HOMOLOGACAO = True`.**

Para cada funcionalidade em `FUNCIONALIDADES`, preencher `funcionalidade["testes"]` usando **exclusivamente** os templates abaixo com os slots extraídos na Etapa 3. Não alterar a estrutura dos templates — apenas substituir os placeholders `{...}` pelos valores dos slots.

**`acao`** — sempre 3 testes, nesta ordem:

```python
[
    {
        "nome": f"Executar '{func['titulo']}' com {slots['condicao_valida']}",
        "esperado": f"Operação concluída — {slots['resultado_principal']}"
    },
    {
        "nome": f"Tentar executar '{func['titulo']}' em condição inválida: {slots['condicao_invalida']}",
        "esperado": f"Sistema bloqueia com mensagem: \"{slots['mensagem_bloqueio']}\""
    },
    {
        "nome": f"Usuário sem perfil '{slots['perfil']}' tenta executar '{func['titulo']}'",
        "esperado": "Acesso negado ou botão indisponível para o perfil"
    },
]
```

**`evento`** — sempre 2 testes, nesta ordem:

```python
[
    {
        "nome": f"Realizar operação que dispara '{func['titulo']}' com {slots['condicao_valida']}",
        "esperado": f"Evento processa sem erros — {slots['resultado_principal']}"
    },
    {
        "nome": f"Realizar operação bloqueada por '{func['titulo']}': {slots['condicao_invalida']}",
        "esperado": f"Operação impedida — mensagem: \"{slots['mensagem_bloqueio']}\""
    },
]
```

**`job`** — sempre 2 testes, nesta ordem:

```python
[
    {
        "nome": f"Acionar '{func['titulo']}' com registros pendentes ({slots['condicao_valida']})",
        "esperado": f"Processamento correto — {slots['resultado_principal']}"
    },
    {
        "nome": f"Acionar '{func['titulo']}' sem dados novos ou já processados",
        "esperado": "Execução finaliza sem erros, sem duplicidade de processamento"
    },
]
```

**`regra`** — sempre 2 testes, nesta ordem:

```python
[
    {
        "nome": f"Executar ciclo atendendo '{func['titulo']}': {slots['condicao_valida']}",
        "esperado": f"Ciclo permitido sem bloqueio — {slots['resultado_principal']}"
    },
    {
        "nome": f"Executar ciclo violando '{func['titulo']}': {slots['condicao_invalida']}",
        "esperado": f"Ciclo bloqueado — mensagem: \"{slots['mensagem_bloqueio']}\""
    },
]
```

**Regra obrigatória:** substituir `{slots['perfil']}` por `"—"` se o slot tiver valor `"não identificado"`. Nunca alterar a ordem ou quantidade de testes definida por tipo.

---

## Etapa 7 — Geração do arquivo HTML

> **Só quando `FORMATO = "html"`.** Para `FORMATO = "docx"`, pular esta etapa e usar a **Etapa 7-DOCX**.

Executar o script Python abaixo **após preencher todas as variáveis** das etapas anteriores.

```python
import os
from datetime import datetime

# ══════════════════════════════════════════════════════════════════
# VARIÁVEIS — preenchidas nas etapas anteriores
# ══════════════════════════════════════════════════════════════════
# PARCEIRO, ID_DEMANDA, NOME_CUSTOMIZACAO, CAMINHO_SISTEMA,
# VERSAO, RESPONSAVEL_TECNICO, OBJETIVO, LIMITACOES_GERAIS,
# FUNCIONALIDADES, CHECKLIST_DEPLOY, PASTA_RAIZ, ARQUIVO_SAIDA,
# TEXTO_PERSONAS_SANKHYA, TEXTO_PERSONAS_CLIENTE
# (todas já definidas nas etapas anteriores)

def parse_personas(texto):
    """Converte texto multiline 'Nome — Função' em lista de dicts."""
    pessoas = []
    for linha in texto.strip().split('\n'):
        linha = linha.strip()
        if not linha:
            continue
        sep = '—' if '—' in linha else ('-' if '-' in linha else None)
        if sep:
            partes = linha.split(sep, 1)
            pessoas.append({"nome": partes[0].strip(), "funcao": partes[1].strip()})
        else:
            pessoas.append({"nome": linha, "funcao": ""})
    return pessoas

PERSONAS_SANKHYA = parse_personas(TEXTO_PERSONAS_SANKHYA)
PERSONAS_CLIENTE = parse_personas(TEXTO_PERSONAS_CLIENTE)

DATA_GERACAO    = datetime.now().strftime("%d/%m/%Y")
VERSAO_DISPLAY  = "v" + VERSAO
ID_HTML         = ID_DEMANDA if ID_DEMANDA else "—"

TIPO_META = {
    "acao":   {"badge": "Ação Manual",       "classe": "c-acao",   "tb": "tb-acao"},
    "evento": {"badge": "Listener / Evento", "classe": "c-evento", "tb": "tb-evento"},
    "job":    {"badge": "Job Agendado",      "classe": "c-job",    "tb": "tb-job"},
    "regra":  {"badge": "Regra de Negócio",  "classe": "c-regra",  "tb": "tb-regra"},
}

# ── helpers ────────────────────────────────────────────────────────

def h(s):
    """Escapa caracteres HTML básicos."""
    return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"','&quot;')

def build_crumbs(caminho):
    parts = [p.strip() for p in caminho.replace("›","›").split("›")]
    out = ""
    for i, p in enumerate(parts):
        if i > 0:
            out += '<span class="path-sep">›</span>'
        if i == len(parts) - 1:
            out += "<span>" + h(p) + "</span>"
        else:
            out += h(p)
    return out

def build_passos(passos):
    items = "".join(
        "<li><span class=\"step-n\">" + str(i) + ".</span><span>" + h(p) + "</span></li>"
        for i, p in enumerate(passos, 1)
    )
    return "<ul class=\"steps\">" + items + "</ul>"

_AVISO_PERFIL = {
    "relatorio": "É necessário configurar os perfis de usuário que terão acesso ao relatório.",
    "tela":      "É necessário configurar os perfis de usuário que terão acesso à tela.",
    "dashboard": "É necessário configurar os perfis de usuário que terão acesso ao dashboard.",
}

def build_func_card(idx, func):
    meta = TIPO_META.get(func["tipo"], TIPO_META["acao"])
    fid  = "fc" + str(idx)
    obs  = ("<div class=\"obs-box\">" + h(func["obs"]) + "</div>") if func.get("obs") else ""
    lim  = ("<div class=\"lim-box\">" + h(func["limitacoes"]) + "</div>") if func.get("limitacoes") else ""
    aviso_key = func.get("tipo_acesso", "")
    aviso = (
        "<div class=\"obs-box\" style=\"margin-top:8px\">" + _AVISO_PERFIL[aviso_key] + "</div>"
    ) if aviso_key in _AVISO_PERFIL else ""
    return (
        "<div class=\"func-card " + meta["classe"] + "\" id=\"" + fid + "\">"
        "<div class=\"func-header\" onclick=\"toggle('" + fid + "')\">"
        "<div class=\"func-icon\">" + func["icone"] + "</div>"
        "<div class=\"func-info\">"
        "<div class=\"func-name\">" + h(func["titulo"]) + "</div>"
        "<div class=\"func-type\"><span class=\"tbadge " + meta["tb"] + "\">" + meta["badge"] + "</span></div>"
        "</div><div class=\"func-arrow\">›</div></div>"
        "<div class=\"func-body\">"
        + build_passos(func["passos"]) + obs + lim + aviso +
        "</div></div>"
    )

def build_homologacao_html(funcionalidades):
    out = ""
    for fi, func in enumerate(funcionalidades, 1):
        out += (
            "<div style=\"margin-bottom:28px\">"
            "<div style=\"font-size:.82rem;font-weight:700;color:#1a4d2e;margin-bottom:10px;"
            "display:flex;align-items:center;gap:8px\">" + func["icone"] + " " + h(func["titulo"]) + "</div>"
        )
        for ti, t in enumerate(func.get("testes", []), 1):
            tid = "hom-fc" + str(fi) + "-" + str(ti)
            out += (
                "<div class=\"test-case\" id=\"" + tid + "\">"
                "<div class=\"test-header\">"
                "<div class=\"test-status\">"
                "<button class=\"status-btn pendente\" onclick=\"toggleStatus(this)\">⏳ Pendente</button>"
                "</div>"
                "<div class=\"test-desc\">"
                "<div class=\"test-name\">" + h(t["nome"]) + "</div>"
                "<div class=\"test-expected\"><strong>Resultado esperado:</strong> " + h(t["esperado"]) + "</div>"
                "</div></div>"
                "<div class=\"test-evidence\">"
                "<div class=\"evidence-row\">"
                "<label class=\"attach-btn\">📎 Adicionar evidência"
                "<input type=\"file\" accept=\"image/*\" multiple onchange=\"attachImage(this,'" + tid + "')\"></label>"
                "<span class=\"no-evidence\" id=\"" + tid + "-hint\">Nenhuma imagem anexada</span>"
                "</div></div></div>"
            )
        out += "</div>"
    return out

def build_sign_grid(personas_sankhya, personas_cliente):
    def boxes(personas):
        out = ""
        for p in personas:
            nome_html   = "<div class=\"sign-name\">"   + h(p["nome"])   + "</div>" if p["nome"]          else ""
            funcao_html = "<div class=\"sign-role\">"   + h(p["funcao"]) + "</div>" if p.get("funcao")    else ""
            out += "<div class=\"sign-box\"><div class=\"sign-line\"></div>" + nome_html + funcao_html + "</div>\n"
        return out
    return (
        "<div class=\"sign-grid\">"
        "<div class=\"sign-col\"><div class=\"sign-col-title\">Sankhya</div>"
        + boxes(personas_sankhya) +
        "</div>"
        "<div class=\"sign-col\"><div class=\"sign-col-title\">Cliente</div>"
        + boxes(personas_cliente) +
        "</div></div>"
    )

def build_limitacoes(lims):
    if not lims:
        return "<p style='color:#aaa;font-size:.82rem'>Nenhuma limitação global identificada.</p>"
    items = "".join(
        "<li><span class=\"lim-icon\">⚠</span><span>" + h(l) + "</span></li>"
        for l in lims
    )
    return "<ul class=\"lim-list\">" + items + "</ul>"

def build_deploy_checklist(checklist):
    pre = checklist.get("pre_requisitos", [])
    pos = checklist.get("pos_deploy", [])
    if not pre and not pos:
        return "<p style='color:#aaa;font-size:.82rem'>Nenhum artefato de deploy identificado.</p>"

    TIPO_ICON = {
        "tela_adicional": "🖥️", "parametro": "⚙️", "script_sql": "🗄️",
        "acao": "▶️", "evento": "⚡", "job": "⏰", "regra": "📋",
        "jar": "📦", "dashboard": "📊",
    }
    TIPO_LABEL = {
        "tela_adicional": "Tela Adicional", "parametro": "Parâmetro TSIPAR",
        "script_sql": "Script DDL", "acao": "Botão de Ação", "evento": "Evento",
        "job": "Job", "regra": "Regra", "jar": "Deploy JAR", "dashboard": "Dashboard",
    }
    ck_counter = [0]

    def render_item(item):
        ck_counter[0] += 1
        cid = "ck" + str(ck_counter[0])
        tipo = item.get("tipo", "")
        icon = TIPO_ICON.get(tipo, "•")
        label = TIPO_LABEL.get(tipo, tipo)
        nome = item.get("nome_exibicao") or item.get("nome") or item.get("arquivo", "")
        details = []
        if tipo == "tela_adicional":
            if item.get("arquivo"):    details.append("Arquivo: <code>" + h(item["arquivo"]) + "</code>")
            if item.get("observacao"): details.append(h(item["observacao"]))
        elif tipo == "parametro":
            if item.get("descricao"):   details.append(h(item["descricao"]))
            if item.get("tipo_valor"):  details.append("Tipo: " + h(item["tipo_valor"]))
            if item.get("valor_padrao"):details.append("Padrão: <code>" + h(item["valor_padrao"]) + "</code>")
        elif tipo == "script_sql":
            if item.get("observacao"): details.append(h(item["observacao"]))
        elif tipo in ("acao", "evento", "job", "regra"):
            if item.get("entidade"):    details.append("Entidade: <code>" + h(item["entidade"]) + "</code>")
            if item.get("tipo_sankhya"):details.append("Tipo: " + h(item["tipo_sankhya"]))
            if item.get("classe"):      details.append("Classe: <code>" + h(item["classe"]) + "</code>")
            if item.get("perfis"):      details.append("Perfis: " + h(item["perfis"]))
        elif tipo == "jar":
            if item.get("arquivo"):          details.append("Arquivo: <code>" + h(item["arquivo"]) + "</code>")
            if item.get("caminho_servidor"): details.append("Destino: <code>" + h(item["caminho_servidor"]) + "</code>")
        elif tipo == "dashboard":
            if item.get("arquivo"):    details.append("Arquivo: <code>" + h(item["arquivo"]) + "</code>")
            if item.get("observacao"): details.append(h(item["observacao"]))
        detail_html = (" <span class=\"ck-detail\">" + " &nbsp;|&nbsp; ".join(details) + "</span>") if details else ""
        return (
            "<div class=\"ck-item\">"
            "<label class=\"ck-label\">"
            "<input type=\"checkbox\" class=\"ck-box\" id=\"" + cid + "\" onchange=\"ckSave('" + cid + "')\">"
            "<span class=\"ck-icon\">" + icon + "</span>"
            "<span class=\"ck-badge\">" + label + "</span>"
            "<span class=\"ck-name\">" + h(nome) + "</span>"
            + detail_html +
            "</label></div>"
        )

    def render_group(titulo, cor_bg, cor_border, items):
        if not items:
            return ""
        header = (
            "<div class=\"ck-group-header\" style=\"background:" + cor_bg + ";border-left:4px solid " + cor_border + "\">"
            "<span class=\"ck-group-title\">" + titulo + "</span>"
            "</div>"
        )
        body = "".join(render_item(item) for item in items)
        return "<div class=\"ck-group\">" + header + body + "</div>"

    out  = render_group("🔴 Pré-requisitos — fazer ANTES do deploy",              "#fff5f5", "#dc2626", pre)
    out += render_group("🟡 Pós-Deploy — configurar APÓS o JAR no servidor",      "#fffbeb", "#d97706", pos)
    return out

# ── montar seções dinâmicas ────────────────────────────────────────

funcionalidades_html = "".join(build_func_card(i, f) for i, f in enumerate(FUNCIONALIDADES, 1))
homologacao_html     = build_homologacao_html(FUNCIONALIDADES) if INCLUIR_HOMOLOGACAO else ""
limitacoes_html      = build_limitacoes(LIMITACOES_GERAIS)
deploy_html          = build_deploy_checklist(CHECKLIST_DEPLOY)
INCLUIR_DEPLOY       = bool(CHECKLIST_DEPLOY.get("pre_requisitos") or CHECKLIST_DEPLOY.get("pos_deploy"))
crumbs_html          = build_crumbs(CAMINHO_SISTEMA)
sign_html            = build_sign_grid(PERSONAS_SANKHYA, PERSONAS_CLIENTE) if INCLUIR_ASSINATURAS else ""

# ── CSS ────────────────────────────────────────────────────────────

CSS = """
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Segoe UI',Arial,sans-serif;background:#f4f6f8;color:#222;min-height:100vh;display:flex;flex-direction:column}
  .layout{display:flex;min-height:100vh}
  .sidebar{width:220px;flex-shrink:0;background:#1a4d2e;position:sticky;top:0;height:100vh;overflow-y:auto;display:flex;flex-direction:column}
  .sidebar-logo{padding:20px 18px 14px;border-bottom:1px solid rgba(255,255,255,.1)}
  .s-brand{font-size:.62rem;font-weight:700;letter-spacing:2px;color:#6AA84F;text-transform:uppercase;margin-bottom:4px}
  .s-title{font-size:.88rem;font-weight:700;color:#fff;line-height:1.4}
  .s-version{display:inline-block;margin-top:6px;background:rgba(106,168,79,.25);color:#6AA84F;font-size:.65rem;font-weight:700;padding:2px 8px;border-radius:10px;border:1px solid rgba(106,168,79,.4)}
  .s-meta{font-size:.65rem;color:rgba(255,255,255,.4);margin-top:6px}
  .nav{padding:12px 0;flex:1}
  .nav-item{display:flex;align-items:center;gap:10px;padding:9px 18px;color:rgba(255,255,255,.6);font-size:.79rem;transition:background .15s,color .15s;text-decoration:none;border-left:3px solid transparent}
  .nav-item:hover{background:rgba(255,255,255,.07);color:#fff}
  .nav-item.active{background:rgba(106,168,79,.18);color:#6AA84F;border-left-color:#6AA84F}
  .nav-icon{font-size:.95rem;width:18px;text-align:center;flex-shrink:0}
  .nav-divider{height:1px;background:rgba(255,255,255,.07);margin:6px 18px}
  .export-btn{margin:14px 14px 18px;background:#6AA84F;color:#fff;border:none;border-radius:8px;padding:10px 14px;font-size:.76rem;font-weight:700;cursor:pointer;width:calc(100% - 28px);transition:background .15s;display:flex;align-items:center;justify-content:center;gap:6px}
  .export-btn:hover{background:#5a9040}
  .main{flex:1;padding:32px 40px;max-width:880px}
  .section{margin-bottom:40px;scroll-margin-top:24px}
  .section-title{font-size:.95rem;font-weight:700;color:#1a4d2e;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #6AA84F;display:flex;align-items:center;gap:8px}
  .s-num{background:#6AA84F;color:#fff;font-size:.68rem;font-weight:700;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
  .id-table{width:100%;border-collapse:collapse;border-radius:10px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.07)}
  .id-table thead th{background:#1a4d2e;color:#fff;text-align:left;padding:10px 14px;font-size:.76rem;font-weight:700}
  .id-table td{padding:9px 14px;font-size:.82rem;border-bottom:1px solid #eee;background:#fff;vertical-align:top}
  .id-table td:first-child{font-weight:600;color:#666;width:210px;white-space:nowrap}
  .id-table tr:last-child td{border-bottom:none}
  .vpill{background:#e8f5e2;color:#2e7d32;border:1px solid #a5d6a7;font-size:.72rem;font-weight:700;padding:2px 10px;border-radius:10px;display:inline-block}
  .path-crumbs{color:#555;line-height:1.6}
  .path-crumbs span{color:#1a4d2e;font-weight:600}
  .path-sep{color:#bbb;margin:0 4px}
  .obj-box{background:#fff;border-radius:10px;padding:16px 20px;box-shadow:0 2px 10px rgba(0,0,0,.07);font-size:.87rem;line-height:1.85;color:#333}
  .func-card{background:#fff;border-radius:10px;box-shadow:0 2px 10px rgba(0,0,0,.07);margin-bottom:12px;overflow:hidden;border-left:4px solid #ccc;transition:box-shadow .15s}
  .func-card:hover{box-shadow:0 4px 18px rgba(0,0,0,.12)}
  .func-card.c-acao{border-left-color:#1565c0}
  .func-card.c-evento{border-left-color:#2e7d32}
  .func-card.c-job{border-left-color:#e65100}
  .func-card.c-regra{border-left-color:#6a1b9a}
  .func-header{padding:13px 18px;cursor:pointer;display:flex;align-items:center;gap:12px;user-select:none}
  .func-icon{font-size:1.2rem;flex-shrink:0}
  .func-info{flex:1}
  .func-name{font-size:.86rem;font-weight:700;color:#222;line-height:1.3}
  .func-type{font-size:.68rem;margin-top:3px}
  .func-arrow{font-size:.9rem;color:#ccc;transition:transform .2s;flex-shrink:0}
  .func-card.open .func-arrow{transform:rotate(90deg)}
  .func-body{display:none;border-top:1px solid #f2f2f2;padding:14px 18px 18px}
  .func-card.open .func-body{display:block}
  .steps{list-style:none;padding:0}
  .steps li{font-size:.82rem;line-height:1.7;padding:5px 0;display:flex;gap:10px;border-bottom:1px solid #f7f7f7}
  .steps li:last-child{border-bottom:none}
  .step-n{color:#6AA84F;font-weight:700;flex-shrink:0;min-width:20px}
  .obs-box{background:#fffbf0;border-left:3px solid #f59e0b;border-radius:4px;padding:10px 14px;font-size:.79rem;line-height:1.65;color:#78350f;margin-top:10px}
  .lim-box{background:#fef2f2;border-left:3px solid #ef4444;border-radius:4px;padding:10px 14px;font-size:.79rem;line-height:1.65;color:#7f1d1d;margin-top:8px}
  .tbadge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.64rem;font-weight:700}
  .tb-acao{background:#dbeafe;color:#1565c0}
  .tb-evento{background:#dcfce7;color:#2e7d32}
  .tb-job{background:#ffedd5;color:#e65100}
  .tb-regra{background:#f3e8ff;color:#6a1b9a}
  .lim-list{background:#fff;border-radius:10px;padding:16px 20px;box-shadow:0 2px 10px rgba(0,0,0,.07);list-style:none}
  .lim-list li{font-size:.83rem;line-height:1.7;padding:6px 0;display:flex;gap:10px;border-bottom:1px solid #fafafa;color:#555}
  .lim-list li:last-child{border-bottom:none}
  .lim-icon{flex-shrink:0;color:#ef4444}
  .test-case{border:1px solid #eee;border-radius:8px;margin-bottom:12px;overflow:hidden}
  .test-case:last-child{margin-bottom:0}
  .test-header{display:flex;align-items:flex-start;gap:12px;padding:12px 14px;background:#fafafa}
  .test-status{flex-shrink:0;margin-top:1px}
  .status-btn{border:none;background:none;cursor:pointer;font-size:.72rem;font-weight:700;padding:3px 10px;border-radius:12px;white-space:nowrap;transition:all .15s}
  .status-btn.pendente{background:#f3f4f6;color:#9ca3af;border:1px solid #e5e7eb}
  .status-btn.aprovado{background:#dcfce7;color:#16a34a;border:1px solid #86efac}
  .status-btn.reprovado{background:#fee2e2;color:#dc2626;border:1px solid #fca5a5}
  .test-desc{flex:1}
  .test-name{font-size:.82rem;font-weight:700;color:#222;margin-bottom:3px}
  .test-expected{font-size:.76rem;color:#666;line-height:1.5}
  .test-expected strong{color:#444}
  .test-evidence{padding:10px 14px;border-top:1px solid #f0f0f0;background:#fff}
  .evidence-gallery{display:flex;flex-direction:column;gap:8px;margin-bottom:8px}
  .evidence-item{position:relative}
  .evidence-item img{width:100%;max-height:400px;object-fit:contain;border-radius:6px;border:1px solid #eee;display:block;background:#fafafa}
  .evidence-item .remove-img{position:absolute;top:3px;right:3px;background:rgba(255,255,255,.92);border:1px solid #fca5a5;padding:2px 5px;border-radius:4px;font-size:.65rem}
  .evidence-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .attach-btn{display:inline-flex;align-items:center;gap:5px;font-size:.72rem;font-weight:700;color:#1a4d2e;background:#f0f8f0;border:1px dashed #6AA84F;border-radius:6px;padding:5px 12px;cursor:pointer;transition:background .15s}
  .attach-btn:hover{background:#e0f0e0}
  .attach-btn input[type=file]{display:none}
  .remove-img{font-size:.7rem;color:#ef4444;background:none;border:none;cursor:pointer;padding:4px 8px;border-radius:4px}
  .remove-img:hover{background:#fee2e2}
  .no-evidence{font-size:.72rem;color:#bbb;font-style:italic}
  .sign-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}
  .sign-col-title{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:#aaa;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid #eee}
  .sign-box{background:#fff;border-radius:10px;padding:16px 18px 14px;box-shadow:0 2px 10px rgba(0,0,0,.07);text-align:center;margin-bottom:12px}
  .sign-box:last-child{margin-bottom:0}
  .sign-line{border-bottom:1px solid #bbb;margin:32px 12px 10px}
  .sign-name{font-size:.82rem;font-weight:600;color:#333;margin-top:4px}
  .sign-role{font-size:.72rem;color:#888;margin-top:2px}
  .ck-group{margin-bottom:14px}
  .ck-group-header{padding:8px 14px;border-radius:8px 8px 0 0}
  .ck-group-title{font-size:.74rem;font-weight:700;color:#333}
  .ck-item{background:#fff;border:1px solid #eee;border-top:none;padding:9px 14px;transition:background .15s}
  .ck-item:last-child{border-radius:0 0 8px 8px}
  .ck-item:has(.ck-box:checked){background:#f0fdf4;border-color:#86efac}
  .ck-label{display:flex;align-items:center;gap:8px;cursor:pointer;font-size:.82rem;flex-wrap:wrap}
  .ck-box{width:15px;height:15px;accent-color:#1a4d2e;cursor:pointer;flex-shrink:0}
  .ck-icon{font-size:.85rem;flex-shrink:0}
  .ck-badge{background:#f3f4f6;color:#555;font-size:.64rem;font-weight:700;padding:2px 7px;border-radius:8px;white-space:nowrap;flex-shrink:0}
  .ck-name{font-weight:600;color:#222}
  .ck-detail{font-size:.75rem;color:#777;line-height:1.5}
  @media print{
    .sidebar{display:none}
    .main{padding:20px;max-width:100%}
    .func-body{display:block!important}
    .func-arrow,.attach-btn,.remove-img,.no-evidence,.export-btn{display:none}
    .test-case{page-break-inside:avoid}
  }
"""

# ── JavaScript ─────────────────────────────────────────────────────

JS = """
function toggle(id){document.getElementById(id).classList.toggle('open')}

const SC=[{cls:'pendente',label:'⏳ Pendente'},{cls:'aprovado',label:'✅ Aprovado'},{cls:'reprovado',label:'❌ Reprovado'}];
function toggleStatus(btn){
  const cur=SC.findIndex(s=>btn.classList.contains(s.cls));
  const next=SC[(cur+1)%SC.length];
  SC.forEach(s=>btn.classList.remove(s.cls));
  btn.classList.add(next.cls);btn.textContent=next.label;
}

function attachImage(input,caseId){
  const files=input.files; if(!files||!files.length)return;
  const tc=document.getElementById(caseId);
  const ev=tc.querySelector('.test-evidence');
  let gallery=ev.querySelector('.evidence-gallery');
  if(!gallery){gallery=document.createElement('div');gallery.className='evidence-gallery';ev.insertBefore(gallery,ev.querySelector('.evidence-row'));}
  Array.from(files).forEach(function(file){
    const reader=new FileReader();
    reader.onload=function(e){
      const item=document.createElement('div');item.className='evidence-item';
      const img=document.createElement('img');img.src=e.target.result;img.title=file.name;
      const rb=document.createElement('button');rb.className='remove-img';rb.textContent='✕';
      rb.onclick=function(){item.remove();updateHint(caseId);};
      item.appendChild(img);item.appendChild(rb);gallery.appendChild(item);
      updateHint(caseId);
    };reader.readAsDataURL(file);
  });
  input.value='';
}

function updateHint(caseId){
  const tc=document.getElementById(caseId);
  const hint=document.getElementById(caseId+'-hint'); if(!hint)return;
  const gallery=tc.querySelector('.evidence-gallery');
  const count=gallery?gallery.querySelectorAll('.evidence-item').length:0;
  hint.textContent=count===0?'Nenhuma imagem anexada':count+(count>1?' imagens anexadas':' imagem anexada');
}

function exportar(){
  const clone=document.documentElement.cloneNode(true);
  const t=clone.querySelector('title');
  if(t)t.textContent=t.textContent.replace(' [interativo]','');
  const html='<!DOCTYPE html>\\n'+clone.outerHTML;
  const blob=new Blob([html],{type:'text/html;charset=utf-8'});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download='Entrega - " + h(NOME_CUSTOMIZACAO) + ".html';
  a.click();URL.revokeObjectURL(a.href);
}

function ckSave(id){
  const cb=document.getElementById(id);
  if(cb)localStorage.setItem('ck_'+id,cb.checked?'1':'0');
}
(function(){
  document.querySelectorAll('.ck-box').forEach(function(cb){
    if(localStorage.getItem('ck_'+cb.id)==='1')cb.checked=true;
  });
})();

const secs=document.querySelectorAll('.section');
const navs=document.querySelectorAll('.nav-item');
window.addEventListener('scroll',()=>{
  let cur='';
  secs.forEach(s=>{if(window.scrollY>=s.offsetTop-80)cur=s.id;});
  navs.forEach(n=>{n.classList.remove('active');if(n.getAttribute('href')==='#'+cur)n.classList.add('active');});
},{passive:true});
"""

# ── montar HTML final ──────────────────────────────────────────────

HTML = (
    "<!DOCTYPE html>\n"
    "<html lang=\"pt-BR\">\n"
    "<head>\n"
    "<meta charset=\"UTF-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    "<title>Entrega — " + h(NOME_CUSTOMIZACAO) + " " + VERSAO_DISPLAY + " [interativo]</title>\n"
    "<style>" + CSS + "</style>\n"
    "</head>\n<body>\n"
    "<div class=\"layout\">\n"

    # sidebar
    "  <nav class=\"sidebar\">\n"
    "    <div class=\"sidebar-logo\">\n"
    "      <div class=\"s-brand\">Sankhya · Entrega Dev</div>\n"
    "      <div class=\"s-title\">" + h(NOME_CUSTOMIZACAO) + "</div>\n"
    "      <div class=\"s-version\">" + VERSAO_DISPLAY + "</div>\n"
    "      <div class=\"s-meta\">Gerado em " + DATA_GERACAO + "</div>\n"
    "    </div>\n"
    "    <div class=\"nav\">\n"
    "      <a class=\"nav-item active\" href=\"#identificacao\"><span class=\"nav-icon\">🪪</span> Identificação</a>\n"
    "      <a class=\"nav-item\" href=\"#objetivo\"><span class=\"nav-icon\">🎯</span> Objetivo</a>\n"
    "      <div class=\"nav-divider\"></div>\n"
    "      <a class=\"nav-item\" href=\"#funcionalidades\"><span class=\"nav-icon\">⚙️</span> Funcionalidades</a>\n"
    "      <a class=\"nav-item\" href=\"#limitacoes\"><span class=\"nav-icon\">⚠️</span> Limitações</a>\n"
    + (
        "      <div class=\"nav-divider\"></div>\n"
        "      <a class=\"nav-item\" href=\"#deploy\"><span class=\"nav-icon\">🚀</span> Deploy</a>\n"
        if INCLUIR_DEPLOY else ""
    )
    + (
        "      <div class=\"nav-divider\"></div>\n"
        "      <a class=\"nav-item\" href=\"#homologacao\"><span class=\"nav-icon\">🧪</span> Homologação</a>\n"
        if INCLUIR_HOMOLOGACAO else ""
    )
    + (
        "      <div class=\"nav-divider\"></div>\n"
        "      <a class=\"nav-item\" href=\"#assinaturas\"><span class=\"nav-icon\">✍️</span> Assinaturas</a>\n"
        if INCLUIR_ASSINATURAS else ""
    )
    +
    "    </div>\n"
    + (
        "    <button class=\"export-btn\" onclick=\"exportar()\">⬇ Exportar com evidências</button>\n"
        if INCLUIR_HOMOLOGACAO else ""
    )
    +
    "  </nav>\n"

    # main
    "  <main class=\"main\">\n"

    # 1. identificação
    "    <div class=\"section\" id=\"identificacao\">\n"
    "      <div class=\"section-title\"><div class=\"s-num\">1</div> Identificação</div>\n"
    "      <table class=\"id-table\">\n"
    "        <thead><tr><th colspan=\"2\">Dados da Entrega</th></tr></thead>\n"
    "        <tbody>\n"
    "          <tr><td>Parceiro</td><td>" + h(PARCEIRO) + "</td></tr>\n"
    "          <tr><td>ID Demanda</td><td>" + h(ID_HTML) + "</td></tr>\n"
    "          <tr><td>Versão</td><td><span class=\"vpill\">" + VERSAO_DISPLAY + "</span></td></tr>\n"
    "          <tr><td>Data de Geração</td><td>" + DATA_GERACAO + "</td></tr>\n"
    "          <tr><td>Responsável Técnico</td><td>" + h(RESPONSAVEL_TECNICO) + "</td></tr>\n"
    "          <tr><td>Nome da Customização</td><td>" + h(NOME_CUSTOMIZACAO) + "</td></tr>\n"
    "          <tr><td>Caminho no Sistema</td><td><div class=\"path-crumbs\">" + crumbs_html + "</div></td></tr>\n"
    "        </tbody>\n"
    "      </table>\n"
    "    </div>\n"

    # 2. objetivo
    "    <div class=\"section\" id=\"objetivo\">\n"
    "      <div class=\"section-title\"><div class=\"s-num\">2</div> Objetivo</div>\n"
    "      <div class=\"obj-box\">" + h(OBJETIVO) + "</div>\n"
    "    </div>\n"

    # 3. funcionalidades
    "    <div class=\"section\" id=\"funcionalidades\">\n"
    "      <div class=\"section-title\"><div class=\"s-num\">3</div> Funcionalidades</div>\n"
    + funcionalidades_html +
    "    </div>\n"

    # 4. limitações
    "    <div class=\"section\" id=\"limitacoes\">\n"
    "      <div class=\"section-title\"><div class=\"s-num\">4</div> Limitações Conhecidas</div>\n"
    + limitacoes_html +
    "    </div>\n"

    # 5. checklist de deploy (condicional)
    + (
        "    <div class=\"section\" id=\"deploy\">\n"
        "      <div class=\"section-title\"><div class=\"s-num\">5</div> Checklist de Deploy</div>\n"
        + deploy_html +
        "    </div>\n"
        if INCLUIR_DEPLOY else ""
    )

    # 6. homologação (condicional)
    + (
        "    <div class=\"section\" id=\"homologacao\">\n"
        "      <div class=\"section-title\"><div class=\"s-num\">6</div> Homologação</div>\n"
        + homologacao_html +
        "    </div>\n"
        if INCLUIR_HOMOLOGACAO else ""
    )

    # 7. assinaturas (condicional)
    + (
        "    <div class=\"section\" id=\"assinaturas\">\n"
        "      <div class=\"section-title\"><div class=\"s-num\">7</div> Assinaturas</div>\n"
        + sign_html +
        "    </div>\n"
        if INCLUIR_ASSINATURAS else ""
    )

    "  </main>\n"
    "</div>\n"
    "<script>" + JS + "</script>\n"
    "</body>\n</html>"
)

# ── salvar ─────────────────────────────────────────────────────────
os.makedirs(os.path.join(PASTA_RAIZ, PASTA_DEMANDA, "Documentacao"), exist_ok=True)
with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f"✅ Documento gerado: {ARQUIVO_SAIDA}")
```

---

## Etapa 7-DOCX — Geração do arquivo .docx

> **Só quando `FORMATO = "docx"`.** Alternativa à Etapa 7 (HTML). Usa as mesmas variáveis
> das etapas de análise (`NOME_CUSTOMIZACAO`, `OBJETIVO`, `FUNCIONALIDADES`, `LIMITACOES_GERAIS`,
> `CAMINHO_SISTEMA`, `PARCEIRO`, `ID_DEMANDA`, `RESPONSAVEL_TECNICO`, `VERSAO`).

Executar o script Python abaixo. Ele gera um Word com tabela de identificação, manual de uso,
homologação em texto e bloco de assinaturas. `FUNCIONALIDADES` aqui reusa a estrutura da Etapa 3
(`titulo`, `passos` como lista, `obs`, `limitacoes`).

```python
import os
try:
    from docx import Document
except ImportError:
    os.system('pip install python-docx --break-system-packages -q')
    from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ── Caminho de saída (.docx) ───────────────────────────────────────
PASTA_DOC_DOCX = os.path.join(PASTA_RAIZ, PASTA_DEMANDA, "Documentacao")
ARQUIVO_SAIDA_DOCX = os.path.join(PASTA_DOC_DOCX, f"Entrega - {NOME_CUSTOMIZACAO}.docx")

# ── Cores/constantes ───────────────────────────────────────────────
GREEN = (106, 168, 79); WHITE = (255, 255, 255); BLACK = (0, 0, 0); GREEN_HEX = '6AA84F'

def set_cell_shading(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def add_run(para, text, bold=None, size=None, color=None):
    run = para.add_run(text)
    if bold is not None: run.bold = bold
    if size is not None: run.font.size = Pt(size)
    if color is not None: run.font.color.rgb = RGBColor(*color)
    return run

def add_custom_heading(doc, text, level=2):
    p = doc.add_paragraph(); run = p.add_run(text); run.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    p.paragraph_format.space_before = Pt(24 if level == 2 else 12)
    p.paragraph_format.space_after = Pt(6)
    run.font.size = Pt(14 if level == 2 else 12)
    return p

def label_valor(doc, label, valor=""):
    p = doc.add_paragraph(style='Normal'); add_run(p, label, bold=True)
    if valor: add_run(p, valor)
    return p

def print_lines(doc, valor):
    # aceita string (com \n) ou lista de strings
    linhas = valor if isinstance(valor, list) else str(valor).split('\n')
    for linha in linhas:
        c = str(linha).strip()
        if c: doc.add_paragraph(c, style='Normal')

def fill_sign_cell(cell, role, is_last=False):
    p1 = cell.paragraphs[0]; p1.paragraph_format.space_after = Pt(0)
    p1.add_run("_______________________________________")
    p2 = cell.add_paragraph(); p2.paragraph_format.space_after = Pt(0); p2.add_run("Nome:").bold = True
    p3 = cell.add_paragraph(); p3.paragraph_format.space_after = Pt(0) if is_last else Pt(36); p3.add_run(role)

# ── Documento ──────────────────────────────────────────────────────
doc = Document()
for style in doc.styles:
    if hasattr(style, 'font'): style.font.name = 'Roboto'
for section in doc.sections:
    section.top_margin = Cm(1.78); section.bottom_margin = Cm(1.60)
    section.left_margin = Cm(2.14); section.right_margin = Cm(1.43)

p_titulo = doc.add_paragraph(style='Normal')
add_run(p_titulo, "Entrega de Desenvolvimento", bold=True, size=16, color=GREEN)
p_titulo.paragraph_format.space_before = Pt(12)
p_sub = doc.add_paragraph(style='Normal'); add_run(p_sub, NOME_CUSTOMIZACAO)
p_sub.paragraph_format.space_after = Pt(24)

# Identificação
id_table = doc.add_table(rows=6, cols=2); id_table.style = 'Table Grid'
hcell = id_table.rows[0].cells[0].merge(id_table.rows[0].cells[1])
set_cell_shading(hcell, GREEN_HEX)
add_run(hcell.paragraphs[0], "Identificação", bold=True, color=WHITE)
dados_id = [
    ("Parceiro:", PARCEIRO),
    ("ID Demanda:", ID_DEMANDA or "—"),
    ("Responsável Técnico:", RESPONSAVEL_TECNICO),
    ("Versão da Customização:", VERSAO),
    ("Caminho no Sistema:", CAMINHO_SISTEMA),
]
for i, (col0, col1) in enumerate(dados_id):
    row = id_table.rows[i + 1]
    row.cells[0].paragraphs[0].add_run(col0).bold = True
    row.cells[1].paragraphs[0].add_run(str(col1))

# 1. Objetivos
add_custom_heading(doc, "1. Objetivos", level=2)
doc.add_paragraph(OBJETIVO, style='Normal')

# 2. Manual de Uso
add_custom_heading(doc, "2. Manual de Uso das Customizações", level=2)
p_c = doc.add_paragraph(style='Normal'); add_run(p_c, "Caminho no sistema: ", bold=True); add_run(p_c, CAMINHO_SISTEMA)
for i, func in enumerate(FUNCIONALIDADES, 1):
    add_custom_heading(doc, f"Funcionalidade {i}: {func.get('titulo','')}", level=3)
    ph = doc.add_paragraph(); add_run(ph, "Passo a Passo:", bold=True)
    print_lines(doc, func.get("passos", ""))
    if func.get("obs"):
        po = doc.add_paragraph(style='Normal'); add_run(po, "Observações: ", bold=True); add_run(po, str(func["obs"]))
    if func.get("limitacoes"):
        pl = doc.add_paragraph(style='Normal'); add_run(pl, "Limitações: ", bold=True); add_run(pl, str(func["limitacoes"]))

# 3. Limitações Conhecidas
add_custom_heading(doc, "3. Limitações Conhecidas", level=2)
print_lines(doc, LIMITACOES_GERAIS if 'LIMITACOES_GERAIS' in dir() else "")

# 4. Homologação e Testes (preenchimento manual)
add_custom_heading(doc, "4. Homologação e Testes", level=2)
for label in ("Responsável pelos testes no cliente: [Nome e cargo]",
              "Data da homologação: [dd/mm/aaaa]",
              "Resultado: [ ] Aprovado  [ ] Reprovado (com pendências abaixo)"):
    doc.add_paragraph(label, style='Normal')

# 5. Observações finais
add_custom_heading(doc, "Observações", level=2)
doc.add_paragraph(
    "Por se tratar de uma personalização o Service Desk não atua nos casos de dúvidas ou "
    "incidentes; qualquer alteração ou suporte deverá ser negociada como horas adicionais "
    "com a Unidade para o atendimento.", style='Normal')

# 6. Local, data e assinaturas
p_cd = doc.add_paragraph("_______, ____ de _______ de ____", style='Normal')
p_cd.paragraph_format.space_before = Pt(40); p_cd.paragraph_format.space_after = Pt(24)
sign = doc.add_table(rows=2, cols=3); sign.autofit = False
sign.columns[0].width = Inches(2.8); sign.columns[1].width = Inches(0.4); sign.columns[2].width = Inches(2.8)
fill_sign_cell(sign.cell(0, 0), "Líder do Projeto")
fill_sign_cell(sign.cell(0, 2), "Gerente de Projetos – Sankhya")
fill_sign_cell(sign.cell(1, 0), "Consultor", is_last=True)
fill_sign_cell(sign.cell(1, 2), "Solicitante", is_last=True)

os.makedirs(PASTA_DOC_DOCX, exist_ok=True)
doc.save(ARQUIVO_SAIDA_DOCX)
ARQUIVO_SAIDA = ARQUIVO_SAIDA_DOCX
print(f"✅ Documento gerado: {ARQUIVO_SAIDA_DOCX}")
```

---

## Etapa 8 — Retorno ao usuário

Após gerar o arquivo, informar:

1. **Arquivo gerado:** `{PASTA_DEMANDA}/Documentacao/Entrega - {NOME_CUSTOMIZACAO}.{html|docx}` (conforme `FORMATO`)
2. **Versão** (só HTML): `{VERSAO}` — backup da anterior em `{PASTA_DEMANDA}/Documentacao/Entrega - {NOME} v{versao_anterior}.html` (se existia)
3. **Funcionalidades documentadas:** lista numerada com título e tipo de cada uma
4. Se `INCLUIR_HOMOLOGACAO = True`: **Testes gerados** — total por funcionalidade (ex.: `Validação de Pesagem: 3 testes`)

**Se `INCLUIR_HOMOLOGACAO = True`**, exibir obrigatoriamente o bloco de instruções abaixo:

---

> **Como usar o bloco de Homologação:**
>
> 1. Abra o arquivo `{PASTA_DEMANDA}/Documentacao/Entrega - {NOME_CUSTOMIZACAO}.html` no navegador.
> 2. Navegue até a seção **Homologação**.
> 3. Para cada teste: clique no botão de status (⏳ → ✅ → ❌) para marcar o resultado e use **📎 Adicionar evidência** para anexar a imagem de tela.
> 4. Após marcar todos os testes e adicionar as evidências, clique em **⬇ Exportar com evidências** — isso gera um novo arquivo HTML com as imagens embutidas em base64.
> 5. **Substitua** o arquivo original (`{PASTA_DEMANDA}/Documentacao/Entrega - {NOME_CUSTOMIZACAO}.html`) pelo arquivo exportado — assim as evidências ficam salvas permanentemente no documento.
> 6. Para corrigir uma evidência: abra o exportado no navegador, remova/substitua a imagem e exporte novamente.

---

---

## Referências

| Tópico | Arquivo |
|---|---|
| Categorias de artefatos, regras de extração por tipo de classe, linguagem funcional, indicadores de permissão | `references/analise-fontes.md` |
