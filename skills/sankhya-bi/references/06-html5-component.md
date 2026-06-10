# Controles > HTML5 — Componente Customizado

O componente HTML5 permite criar painéis completamente customizados dentro do Sankhya OM,
usando HTML, CSS e JavaScript puro. É a abordagem mais flexível — ideal para kanban boards,
tabelas operacionais, painéis com edição inline, progress bars, timelines, etc.

---

## Dois padrões de implementação

### Padrão 1 — JSP com `<snk:load/>` (Server-side)

Arquivo: `index.jsp`

> **⚠️ IMPORTANTE:** O `executeQuery` injetado pelo `snk:load` é **incompatível com SQL dinâmico** montado no JavaScript. Internamente o GWT tenta substituir parâmetros `:PARAM` no SQL e falha com `b.replace is not a function` quando a query não usa esse padrão de placeholders. **Use sempre `JX.consultar` para executar queries em JSPs**, incluindo o `jx.min.js` junto com `snk:load`.

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" isELIgnored="false"%>
<%@ page import="java.util.*" %>
<%@ taglib uri="http://java.sun.com/jstl/core_rt" prefix="c" %>
<%@ taglib prefix="snk" uri="/WEB-INF/tld/sankhyaUtil.tld" %>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <snk:load/>
    <script src="https://cdn.jsdelivr.net/gh/wansleynery/SankhyaJX@main/jx.min.js"></script>
    <style>...</style>
</head>
<body>
    ...
    <script>
        // Query via JX.consultar — funciona em JSP e HTML5 puro, retorna Promise
        function carregarDados() {
            const query = "SELECT CAMPO1, CAMPO2 FROM AD_TABELA WHERE STATUS = 'A'";
            JX.consultar(query)
              .then(function(rows) {
                  // rows é diretamente o array de objetos
                  rows.forEach(function(r) { console.log(r.CAMPO1); });
              })
              .catch(function(e) {
                  console.error("Erro:", e);
              });
        }
        carregarDados();
    </script>
</body>
</html>
```

**Quando usar JSP:**
- Quando o componente precisa de `${BASE_FOLDER}` para referenciar assets (CSS, fontes, ícones) empacotados no ZIP
- Quando precisar ler argumentos passados de drill-down via `${param.NOME_ARG}`
- Projetos mais estruturados com múltiplos arquivos (JSP + CSS + assets)

**Estrutura do ZIP para JSP:**
```
NNN_html5Component.zip
└── index/
    ├── index.jsp          ← entryPoint
    └── assets/            ← (opcional) CSS, fontes, imagens
```

---

### Padrão 2 — HTML puro com SankhyaJX (Client-side)

Arquivo: `index.html`

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/gh/wansleynery/SankhyaJX@main/jx.min.js"></script>
    <style>...</style>
</head>
<body>
    ...
    <script>
        // Query via JX.consultar (retorna Promise)
        function carregarDados() {
            const query = `
                SELECT CAMPO1, CAMPO2
                FROM AD_TABELA
                WHERE STATUS = 'A'
                ORDER BY CAMPO1
            `;
            JX.consultar(query)
                .then(result => {
                    // result é array de objetos {CAMPO1: valor, CAMPO2: valor}
                    renderizar(result);
                })
                .catch(erro => {
                    console.error("Erro:", erro);
                });
        }
        carregarDados();
    </script>
</body>
</html>
```

**Quando usar HTML puro:**
- Desenvolvimento mais simples e rápido
- Sem necessidade de assets externos
- Quando precisar de atualização/persistência via API REST (update de campos)

**Estrutura do ZIP para HTML:**
```
NNN_html5Component.zip
└── index/
    └── index.html         ← entryPoint
```

---

## Padrão 3 — HTML puro com API direta (para leitura + escrita)

Usado quando o dashboard precisa **escrever de volta** no Sankhya (ex: atualizar status, atribuir operador).

```javascript
const api = (function() {
    function getJnid() {
        // Obtém o token de sessão
        const jnidCookie = document.cookie.split('; ').find(row => row.startsWith('JSESSIONID='));
        if (jnidCookie) return jnidCookie.split('=')[1].split('.')[0];
        return parent?.JNID || window.JNID || null;
    }

    function callService(serviceName, body, retries = 3) {
        return new Promise((resolve, reject) => {
            const jnid = getJnid();
            if (!jnid) return reject("Sessão não encontrada (JNID).");
            const { hostname, port } = window.location;
            const url = `http://${hostname}:${port}/mge/service.sbr?serviceName=${serviceName}&outputType=json&mgeSession=${jnid}`;
            const xhr = new XMLHttpRequest();
            xhr.withCredentials = true;
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhr.onload = function() {
                if (xhr.status >= 200 && xhr.status < 300) {
                    try {
                        const response = JSON.parse(xhr.responseText);
                        if (response.status === "4" && retries > 0) {
                            setTimeout(() => callService(serviceName, body, retries - 1).then(resolve).catch(reject), 500);
                        } else resolve(response);
                    } catch(e) { reject("Erro JSON: " + e.message); }
                } else reject("Erro HTTP: " + xhr.statusText);
            };
            xhr.onerror = () => reject("Erro de rede.");
            xhr.send(JSON.stringify(body));
        });
    }

    return {
        // Carregar registros de uma entidade
        loadRecords: function(entityName, fields, criteria, joinEntities, pagination = {}) {
            const entityArray = [{ path: "", fieldset: { list: fields.join(',') } }];
            if (joinEntities) entityArray.push(...joinEntities);
            return callService("CRUDServiceProvider.loadRecords", {
                serviceName: "CRUDServiceProvider.loadRecords",
                requestBody: { dataSet: {
                    rootEntity: entityName,
                    includePresentationFields: "S",
                    pageSize: pagination.limit || "100000",
                    offsetPage: pagination.offset || "0",
                    criteria: criteria,
                    entity: entityArray
                }}
            });
        },
        // Atualizar campos de um registro
        updateRecord: function(entityName, fields, pks, records) {
            return callService("DatasetSP.save", {
                serviceName: "DatasetSP.save",
                requestBody: {
                    entityName: entityName,
                    standAlone: false,
                    fields: fields,
                    records: pks.map((pk, i) => ({ pk, values: records[i].values }))
                }
            });
        }
    };
})();
```

---

## Estrutura XML do componente (`NNN_component.xml`)

O ZIP do componente HTML5 pode incluir um XML que define parâmetros, níveis e argumentos.
Este XML é importado no **Construtor de Componentes de BI** (botão "Importar"):

```xml
<gadget refresh-time="60000">

  <!-- Parâmetros de filtro (aparecem na barra de filtros do Dashboard) -->
  <prompt-parameters>
    <parameter
      id="P_EMPRESA"
      description="Empresa"
      metadata="multiList:Text"
      listType="sql"
      required="false"
      keep-last="true"
      keep-date="false"
      show-inactives="false"
      order="0">
      <expression type="SQL"><![CDATA[
        SELECT CODEMP AS VALUE, CODEMP || ' - ' || NOMEFANTASIA AS LABEL
        FROM TSIEMP
        ORDER BY 1
      ]]></expression>
    </parameter>

    <parameter id="P_DATA_INI" description="Data Inicial" metadata="date"
               required="false" keep-last="true" keep-date="true" order="1"/>
  </prompt-parameters>

  <!-- Nível principal -->
  <level id="LV1" description="Principal">
    <container orientacao="V" tamanhoRelativo="100">
      <html5component id="html5_001" entryPoint="index.jsp"/>
    </container>
  </level>

  <!-- Nível de drill-down (abre ao clicar no componente do nível anterior) -->
  <level id="LV2" description="Detalhes">
    <args>
      <arg id="A_CODIGO" type="integer" label="Código selecionado"/>
    </args>
    <container orientacao="V" tamanhoRelativo="100">
      <html5component id="html5_002" entryPoint="index.jsp"/>
    </container>
  </level>

</gadget>
```

**Atributos do `<parameter>`:**

| Atributo | Descrição |
|---|---|
| `id` | Identificador — usado no JS para ler o valor (`getUrlParam('P_EMPRESA')`) |
| `description` | Label visível ao usuário |
| `metadata` | Tipo: `text`, `integer`, `decimal`, `date`, `period`, `boolean`, `singleList:Text`, `multiList:Text` |
| `listType` | `sql` (lista via query) ou `text` (valores manuais) |
| `required` | `true` / `false` |
| `keep-last` | Salva o último valor informado |
| `keep-date` | Para datas: usa data atual como padrão |

**Tipos de container:**

| Orientação | Descrição |
|---|---|
| `V` | Componentes empilhados verticalmente (padrão) |
| `H` | Componentes lado a lado horizontalmente |

---

## Como ler parâmetros e argumentos no JavaScript

### Parâmetros (filtros da barra superior)
```javascript
function getUrlParam(name) {
    const params = new URLSearchParams(window.location.search);
    return params.get(name) || '';
}

// Uso:
const empresa = getUrlParam('P_EMPRESA');  // "101" ou "101,401" se multiList
const dataIni = getUrlParam('P_DATA_INI'); // "01/01/2024"
```

### Argumentos (passados via drill-down do nível pai)
```javascript
// No JSP: ${param.A_CODIGO}
// No JS via URL:
const codigo = getUrlParam('A_CODIGO');
```

---

## Formatos de data retornados pelo Sankhya

Datas retornam como string `"DDMMYYYYHHMM"` (12 dígitos):

```javascript
function formatarData(str) {
    if (!str) return '';
    const s = str.replace(/[^0-9]/g, '');
    if (s.length >= 8) {
        const dia = s.substring(0, 2);
        const mes = s.substring(2, 4);
        const ano = s.substring(4, 8);
        const hora = s.length >= 12 ? ` ${s.substring(8, 10)}:${s.substring(10, 12)}` : '';
        return `${dia}/${mes}/${ano}${hora}`;
    }
    return str;
}

// Para input datetime-local:
function formatarParaInput(str) {
    if (!str) return '';
    const s = str.replace(/[^0-9]/g, '');
    if (s.length >= 12) {
        return `${s.substring(4,8)}-${s.substring(2,4)}-${s.substring(0,2)}T${s.substring(8,10)}:${s.substring(10,12)}`;
    }
    return '';
}

// Para enviar ao Sankhya (update):
function formatarParaBanco(valorInput) {
    if (!valorInput) return '';
    const [data, hora] = valorInput.split('T');
    const [ano, mes, dia] = data.split('-');
    return `${dia}/${mes}/${ano} ${hora}:00`;
}
```

---

## Ocultar barra do Sankhya (padrão de todos os HTML5)

Injetar CSS no documento pai para ocultar a barra de título do dashboard e o botão de configuração GWT que aparece sobreposto ao iframe:

```javascript
try {
    const style = parent.document.createElement('style');
    style.textContent = [
        '.VCompactBar, .DashWindow-TopBar-Title { display: none !important; }',
        '.gwt-Button.chartConfigButton { display: none !important; }'
    ].join(' ');
    parent.document.head.appendChild(style);
} catch (e) { /* ignora se cross-origin */ }
```

> **Por que ocultar `.gwt-Button.chartConfigButton`?**
> O Sankhya injeta um botão de configuração GWT com `position: absolute` por cima do iframe do componente HTML5. Ele fica na posição `top: 7px; right: 10px` e sobrepõe controles do próprio dashboard. Como componentes HTML5 não utilizam as configurações nativas de BI, esse botão pode ser ocultado com segurança.

---

## Processo de deploy do componente HTML5

1. Criar o arquivo `index.jsp` ou `index.html`
2. Criar pasta `index/` e colocar o arquivo dentro
3. Compactar em ZIP: `NNN_html5Component.zip` (onde `NNN` = código do componente)
4. No Sankhya: `Configurações > Avançado > Construtor de Componentes de BI`
5. Criar novo gadget → aba **Design** → arrastar **Controles > HTML5** para a área de trabalho
6. Editar o componente HTML5 → informar o nome do arquivo de entrada (`index.jsp` ou `index.html`)
7. Salvar o gadget → fazer upload do ZIP
8. Se houver XML separado: usar botão **Importar XML** para carregar parâmetros e estrutura de níveis

---

## Armadilhas comuns (bugs confirmados em produção)

### ❌ Comparação de datas com TO_CHAR — retorna zero resultados

**Problema:** Usar `TO_CHAR` para formatar a data e depois comparar como string `BETWEEN` falha silenciosamente quando o formato é `DD/MM/YYYY`. A comparação é **lexicográfica**, não cronológica. Exemplo:

```
'27/12/2024' > '27/03/2026'  →  TRUE (porque '12' > '03' caractere a caractere)
```

Resultado: o BETWEEN fica com os extremos invertidos e retorna zero linhas, sem nenhum erro.

```sql
-- ❌ ERRADO — comparação lexicográfica, sempre vazio para formatos DD/MM/YYYY
WHERE TO_CHAR(CAB.DATA, 'DD/MM/YYYY') BETWEEN '27/12/2024' AND '27/03/2026'

-- ✅ CORRETO — comparação cronológica real
WHERE TRUNC(CAB.DATA) BETWEEN TO_DATE('27/12/2024','DD/MM/YYYY') AND TO_DATE('27/03/2026','DD/MM/YYYY')
```

Ao montar o WHERE com datas vindas de `<input type="date">` (formato `YYYY-MM-DD`), converter primeiro para `DD/MM/YYYY` e usar `TO_DATE`:

```javascript
// Converte YYYY-MM-DD (valor do input) → DD/MM/YYYY (para o TO_DATE do Oracle)
function toOracle(val) {
  if (!val) return null;
  var parts = val.split('-');
  return parts[2] + '/' + parts[1] + '/' + parts[0];
}

// Uso no WHERE:
"TRUNC(CAB.DATA) BETWEEN TO_DATE('" + toOracle(dtIni) + "','DD/MM/YYYY')" +
" AND TO_DATE('" + toOracle(dtFin) + "','DD/MM/YYYY')"
```

---

### ❌ `snk:load` trava com `Cannot read properties of undefined`

O `<snk:load/>` tenta acessar o contexto GWT do parent (`nuGdg=N`). Se o componente for carregado fora do contexto normal de dashboard (ex.: aba isolada, teste direto pela URL), a linha falha com:

```
Cannot read properties of undefined (reading '75')
```

**Solução:** Remover `<snk:load/>` do JSP. Para queries, usar `JX.consultar` (ver acima). Manter apenas a diretiva de charset:

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" isELIgnored="false"%>
```

> A diretiva `contentType` é obrigatória mesmo sem outros tags JSP — sem ela, o servidor serve o arquivo com Latin-1, quebrando caracteres especiais (ex: `ã` vira `Ã£`).

---

### ❌ Funções dentro de IIFE não acessíveis por `onclick=""`

```javascript
(function() {
  function aplicarFiltros() { ... }  // ← não acessível externamente
})();
```

```html
<button onclick="aplicarFiltros()">Buscar</button>  <!-- ❌ ReferenceError -->
```

**Solução:** Expor explicitamente no `window`:

```javascript
window.aplicarFiltros = aplicarFiltros;
```

---

## Dicas de UX para dashboards operacionais

- **Altura 100vh com overflow hidden** → tabela com scroll interno, sem scroll de página
- **Sticky thead** → cabeçalho da tabela fixo ao rolar
- **CSS variáveis** (`--primary`, `--border`, etc.) → fácil ajuste de tema
- **Auto-refresh** → `setInterval(loadData, 60000)` para dados em tempo real
- **Loading state** → overlay ou contador no badge durante carregamento
- **Export CSV** → gerar blob sem backend
- **Filtros em memória** → filtrar `dados[]` localmente sem nova query (mais rápido)

---

## Padrão 4 — JSP Unificado (HTML + API JSON no mesmo arquivo)

**Objetivo:** Criar dashboards que acessam recursos do servidor (filesystem, propriedades JVM, etc.) sem dependência de botão de ação (TSIBTA) ou JAR customizado.

**Quando usar:**
- Acessar arquivos do servidor (logs, configurações)
- Ler propriedades de sistema (`System.getProperty`)
- Operações de filesystem não suportadas por SPBeans nativos
- Eliminar dependências de módulos Java customizados

**Estrutura do JSP Unificado:**

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.io.*" %>
<%@ page import="java.util.*" %>
<%!
// ============================================================================
// MÉTODOS AUXILIARES JAVA (executados no servidor)
// ============================================================================
private static final String PROP_LOG_FILE = "org.jboss.boot.log.file";
private static final String FALLBACK_LOG_PATH = "/home/mgeweb/wildfly_producao/standalone/log/server.log";

private static String obterPathLog() {
    String path = System.getProperty(PROP_LOG_FILE);
    if (path == null || path.trim().isEmpty()) {
        return FALLBACK_LOG_PATH;
    }
    return path.trim();
}

private static String escapeJson(String s) {
    if (s == null) return "";
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        switch (c) {
            case '\\': sb.append("\\\\"); break;
            case '"': sb.append("\\\""); break;
            case '\n': sb.append("\\n"); break;
            case '\r': sb.append("\\r"); break;
            case '\t': sb.append("\\t"); break;
            default:
                if (c < 0x20) {
                    sb.append(String.format("\\u%04x", (int) c));
                } else {
                    sb.append(c);
                }
        }
    }
    return sb.toString();
}

private static List<String> lerArquivo(String path) throws IOException {
    List<String> linhas = new ArrayList<String>();
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
        String linha;
        while ((linha = br.readLine()) != null) {
            linhas.add(linha);
        }
    }
    return linhas;
}
%>
<%
// ============================================================================
// ROTEAMENTO: Interface HTML ou API JSON
// ============================================================================
String action = request.getParameter("action");

// Se não há action, serve a interface HTML
if (action == null || action.isEmpty()) {
%>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
    <style>
        /* CSS aqui */
    </style>
</head>
<body>
    <!-- Interface HTML -->
    <script>
        // Função para construir URLs de API
        function buildUrl(action, params) {
            var url = window.location.href.split('#')[0];
            url = url.replace(/[?&]action=[^&]*/g, '');
            url += (url.indexOf('?') >= 0 ? '&' : '?') + 'action=' + encodeURIComponent(action);
            if (params) {
                for (var k in params) {
                    url += '&' + encodeURIComponent(k) + '=' + encodeURIComponent(params[k]);
                }
            }
            return url;
        }

        // Chamada à API
        async function carregarDados() {
            var url = buildUrl('ler', { offset: 0 });
            var resp = await fetch(url, { credentials: 'include' });
            var data = await resp.json();
            // processar data...
        }
    </script>
</body>
</html>
<%
    return; // Importante: encerra execução após servir HTML
}

// ============================================================================
// API JSON (quando há parâmetro action)
// ============================================================================
response.setContentType("application/json");
response.setCharacterEncoding("UTF-8");
response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");

try {
    String pathLog = obterPathLog();

    if ("ler".equals(action)) {
        List<String> linhas = lerArquivo(pathLog);

        StringBuilder json = new StringBuilder();
        json.append("{\n");
        json.append("  \"success\": true,\n");
        json.append("  \"linhas\": [");
        for (int i = 0; i < linhas.size() && i < 100; i++) {
            if (i > 0) json.append(",");
            json.append("\n    \"").append(escapeJson(linhas.get(i))).append("\"");
        }
        json.append("\n  ]\n");
        json.append("}");
        out.print(json.toString());

    } else if ("info".equals(action)) {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        json.append("  \"success\": true,\n");
        json.append("  \"path\": \"").append(escapeJson(pathLog)).append("\",\n");
        json.append("  \"existe\": ").append(new File(pathLog).exists()).append("\n");
        json.append("}");
        out.print(json.toString());

    } else {
        out.print("{\"success\": false, \"error\": \"Ação desconhecida.\"}");
    }

} catch (Exception e) {
    out.print("{\"success\": false, \"error\": \"" + escapeJson(e.getMessage()) + "\"}");
}
%>
```

**APIs disponíveis:**
- `action=null` → Serve interface HTML
- `action=ler` → Retorna JSON com dados
- `action=info` → Retorna metadados

**Vantagens:**
- Zero dependência de TSIBTA (botão de ação)
- Zero JAR customizado
- Autenticação nativa do Sankhya (JSESSIONID)
- Acesso direto a recursos do servidor via Java
- Deploy simplificado (apenas 1 arquivo JSP)

**Estrutura do componente XML:**

```xml
<gadget>
  <level id="02Q" description="Principal">
    <container orientacao="V" tamanhoRelativo="100">
      <html5component id="html5_01W" entryPoint="monitor.jsp">
      </html5component>
    </container>
  </level>
</gadget>
```

**URL de acesso:**
```
/mge/html5component.mge?entryPoint=monitor.jsp&nuGdg=127&gadGetID=html5_01W&userID=0
```

**Deploy:**
1. Criar ZIP com estrutura: `NOME_COMPONENTE/monitor.jsp` + `html5_component.xml`
2. Importar no Construtor de Componentes de BI
3. O entryPoint no XML deve incluir o diretório: `entryPoint="NOME_COMPONENTE/monitor.jsp"`

---

### Boas Práticas para JSP Unificado

**1. Usar `var` em vez de `let/const`**
O Sankhya pode minificar o JavaScript e causar conflitos com nomes de variáveis.

```javascript
// ✅ CORRETO
var resultUrl = buildUrl('ler', { offset: currentOffset });

// ❌ EVITAR
let resultUrl = buildUrl('ler', { offset: currentOffset });
const resultUrl = buildUrl('ler', { offset: currentOffset });
```

**2. Não declarar `PrintWriter out`**
O JSP já define `out` implicitamente. Declarar novamente causa erro de compilação.

```jsp
<%
// ❌ ERRADO — variável duplicada
PrintWriter out = response.getWriter();

// ✅ CORRETO — usar out implicitamente
out.print("{\"success\": true}");
%>
```

**3. Escape de JSON para caracteres especiais**
Sempre escapar `\`, `"`, `\n`, `\r`, `\t` e caracteres de controle.

**4. Timeout para fetch**
Usar `AbortController` para evitar requisições penduradas.

```javascript
async function fetchJson(url, timeout) {
    var controller = new AbortController();
    var signal = controller.signal;
    var timeoutId = setTimeout(function() { controller.abort(); }, timeout || 10000);
    try {
        var resp = await fetch(url, { credentials: 'include', signal: signal });
        clearTimeout(timeoutId);
        return await resp.json();
    } catch (e) {
        clearTimeout(timeoutId);
        throw e;
    }
}
```

**5. Buffer circular para logs**
Para monitores de log em tempo real, usar buffer circular para evitar consumo excessivo de memória.

```javascript
var BUFFER_MAX = 1000;
var LOTE_DESCARTE = 200;

function adicionarLinhasAoBuffer(novas) {
    for (var i = 0; i < novas.length; i++) {
        buffer.push(novas[i]);
    }
    if (buffer.length > BUFFER_MAX) {
        buffer.splice(0, buffer.length - BUFFER_MAX + LOTE_DESCARTE);
    }
}
```

**6. Propriedades JVM úteis**

| Propriedade | Uso |
|---|---|
| `org.jboss.boot.log.file` | Caminho do server.log do WildFly |
| `user.home` | Home do usuário do sistema |
| `user.dir` | Diretório de trabalho atual |
| `java.io.tmpdir` | Diretório temporário |
| Custom (`snk.*`) | Propriedades de configuração do Sankhya |

**Exemplos de uso:**
- `System.getProperty("snk.auth.folder")` → Pasta de autorizações
- `System.getProperty("org.jboss.boot.log.file")` → Caminho do server.log
- `MgmtRuntime.getProperties().getProperty("snk.use.action.auth")` → Flag customizada

---

### Arquitetura: comparativo dos padrões

| Padrão | Backend | Dependências | Use quando |
|---|---|---|---|
| HTML + SankhyaJX | Nenhum | CDN SankhyaJX | Queries simples, leitura apenas |
| JSP + `<snk:load/>` | JSP | Taglib Sankhya | Queries parametrizadas, assets |
| HTML + API direta | Nenhum | JNID da sessão | CRUD completo (ler/escrever) |
| **JSP Unificado** | **JSP** | **Nenhuma** | **Acesso ao servidor (filesystem, propriedades JVM)** |
