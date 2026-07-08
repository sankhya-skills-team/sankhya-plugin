# Popups Personalizados via PopUpBuilder

## Visão Geral

O `PopUpBuilder` permite criar popups personalizados em Módulos Java Sankhya, injetando HTML e JavaScript que rodam no contexto Angular do Sankhya OM.

**Quando usar — dois cenários principais:**

**1. Botão de ação com seleção de registros (`AcaoRotinaJava`)**
Os parâmetros nativos (`ctx.getParam()`) suportam apenas inputs simples: texto, data, decimal.
Quando o usuário precisa escolher de uma lista, marcar campos ou executar um fluxo multi-etapa, PopUpBuilder é a única alternativa.

**2. Eventos e Regras de Negócio com confirmação/pergunta (`EventoProgramavelJava`, `RegraNegocioJava`)**
`ctx.confirmarSimNao()` existe apenas em `AcaoRotinaJava`. PopUpBuilder via `MessageUtils.showInfo()` é a forma de apresentar perguntas ou coletar dados nesses fluxos.

**Quando NÃO usar:**
- Confirmação simples em botão de ação → usar `ctx.confirmarSimNao()`
- Mensagem de erro → usar `MGEModelException`
- Mensagem informativa pós-operação → usar `MessageUtils.showInfo()` direto

---

## ⚠️ Regras Críticas — Ler Antes de Qualquer Implementação

### 1. Comentários `//` são PROIBIDOS no JS do popup

O PopUpBuilder injeta o JS inline (como bloco único). Comentários `//` quebram todo o código que vem depois:

```javascript
/* ✅ CORRETO — sempre usar bloco */
/* Esta é minha função */
function minhaFuncao() { ... }

// ❌ ERRADO — vai quebrar tudo após o //
// Esta é minha função
function minhaFuncao() { ... }
```

Ao criar ou editar um `.js` de popup, **remover todos os `//`** antes de salvar.
Substituir por `/* */` se o comentário for necessário.

### 2. Acentuação em HTML — usar entidades HTML

O PopUpBuilder lê os bytes do arquivo HTML estático. Se o sistema operacional ou o JVM interpretar o encoding diferente, caracteres acentuados aparecem como lixo (`avan\xedar`).

**Regra:** nunca escrever ã, ç, ê, á etc. diretamente no HTML. Sempre usar entidades:

| Char | Entidade | | Char | Entidade |
|---|---|---|---|---|
| ã | `&atilde;` | | â | `&acirc;` |
| ç | `&ccedil;` | | á | `&aacute;` |
| ê | `&ecirc;` | | é | `&eacute;` |
| ó | `&oacute;` | | õ | `&otilde;` |
| ú | `&uacute;` | | ô | `&ocirc;` |

No JS, strings usadas no DOM podem usar acentos normalmente — só o HTML estático é afetado.

### 3. build.gradle — incluir todos os tipos de arquivo

O JAR task deve incluir **todos** os recursos do módulo, não apenas `.sql`:

```groovy
// ✅ CORRETO
from('Java/resources') {
    include "${moduleName}/**"
}

// ❌ ERRADO — HTML e JS não entram no JAR
from('Java/resources') {
    include "${moduleName}/*.sql"
}
```

---

## Estrutura de Arquivos

```
Java/
├── src/br/com/sankhya/dstech/
│   ├── utils/
│   │   └── PopUpBuilder.java              ← OBRIGATÓRIO — copiar de examples/PopUpBuilder.java
│   └── {modulo}/
│       └── actionbutton/
│           └── MeuBotaoAcao.java
└── resources/
    └── {modulo}/
        └── popup/
            ├── PopUpNome.html             ← sem acentos: usar entidades HTML
            └── PopUpNome.js               ← sem comentários //
```

> **ATENÇÃO:** O path de resources é `Java/resources/{modulo}/popup/` — **não** `br/com/sankhya/dstech/{modulo}/`.
> O build.gradle usa `from('Java/resources') { include "${moduleName}/**" }`.
> O JAR resultante contém o arquivo em `/{modulo}/popup/PopUpNome.html`.
>
> **PopUpBuilder NÃO é nativo do Sankhya SDK.** É uma classe customizada em `br.com.sankhya.dstech.utils.PopUpBuilder`.
> A implementação completa está em `examples/PopUpBuilder.java`.

---

## PopUpBuilder API

```java
import br.com.sankhya.dstech.utils.PopUpBuilder;
import br.com.sankhya.dstech.utils.MessageUtils;

private static final String POPUP_HTML = "/{modulo}/popup/PopUpNome.html";
private static final String POPUP_JS   = "/{modulo}/popup/PopUpNome.js";

String popup = new PopUpBuilder.Builder()
    .setTitle("T&iacute;tulo do Popup")
    .setHtmlFile(MeuBotaoAcao.class.getResourceAsStream(POPUP_HTML))
    .setJsFile(MeuBotaoAcao.class.getResourceAsStream(POPUP_JS))
    .setWidth(750)
    .setHeight(500)
    .addVariable("entidadesJson", entidadesJson)  // String → var entidadesJson = '[{...}]';
    .addVariable("codRegistro",   codRegistro)    // BigDecimal → var codRegistro = 123;
    .addVariable("ativo",         true)           // Boolean → var ativo = true;
    .build();

MessageUtils.showInfo(popup);
```

### Métodos do Builder

| Método | Tipo | Descrição |
|---|---|---|
| `setTitle(String)` | String | Título no header do popup |
| `setHtmlFile(InputStream)` | InputStream | Arquivo HTML |
| `setJsFile(InputStream)` | InputStream | Arquivo JS |
| `setCssFile(InputStream)` | InputStream | CSS customizado (opcional) |
| `setWidth(int)` | int | Largura em pixels (padrão: 800) |
| `setHeight(int)` | int | Altura em pixels (padrão: 400) |
| `addVariable(String, Object)` | Object | Variável Java → JS |
| `build()` | String | Retorna HTML completo para exibir |

---

## Componentes Angular Disponíveis no Popup

O popup roda no contexto Angular do Sankhya OM. Os seguintes componentes e serviços estão disponíveis:

### Layout

```html
<sk-vbox gap="8">            <!-- container vertical -->
<sk-hbox gap="8" style="align-items: center;">   <!-- container horizontal -->
```

### sk-icon — Três Modos de Uso

O `sk-icon` suporta três fontes. Escolher conforme o contexto:

#### Modo 1: SVG nativo do Sankhya (`svg-src`)

Usa arquivos já presentes no servidor em `/mge/assets/svg/`. Cor controlada via CSS fill.

```html
<sk-icon svg-src="/mge/assets/svg/cancel.svg"  style="max-height: 14px; margin-right: 2px;"></sk-icon>
<sk-icon svg-src="/mge/assets/svg/search.svg"  style="max-height: 16px;"></sk-icon>
<sk-icon svg-src="/mge/assets/svg/pdf.svg"     style="max-height: 18px;"></sk-icon>
<sk-icon svg-src="/mge/assets/svg/forward.svg" style="max-height: 14px;"></sk-icon>
```

Catálogo completo disponível em `/mge/assets/svg/`:

| Categoria | Arquivos disponíveis |
|---|---|
| Navegação | `back.svg` `forward.svg` `next.svg` `rewind.svg` `up.svg` `down.svg` `up-all.svg` `down-all.svg` |
| Ações | `cancel.svg` `exchange.svg` `switch.svg` `upload-arrow.svg` `check-edit.svg` `check-finish.svg` |
| Pesquisa | `search.svg` `search-engine.svg` `search-standard.svg` `screen-search.svg` `zoom-target.svg` |
| Documentos | `pdf.svg` `xls.svg` `html5.svg` `html5Down.svg` `html5Up.svg` |
| Interface | `checkbox.svg` `calendar-date.svg` `calendar-time.svg` `clock-line.svg` `loading.svg` `location.svg` |
| Janela | `maximize.svg` `minimize.svg` `expand_all.svg` `collapse_all.svg` `screen-plus.svg` `screen-minus.svg` |
| Pastas | `folder-opened.svg` `folder-closed.svg` `folder-hierarchy.svg` `list-folder.svg` |
| Gráficos | `barras.svg` `pizza.svg` `donut.svg` `linha.svg` `area.svg` `radar.svg` `dispersao.svg` `velocimetro.svg` `tabela.svg` `tabeladinamica.svg` `TreeMap.svg` `poll.svg` `geografico.svg` `geomapa.svg` |
| Alertas | `alertabloqueio.svg` `yellow-warning.svg` `question-line.svg` |
| Misc | `favorite.svg` `flash.svg` `puzzle.svg` `box.svg` `cube.svg` `link.svg` `chain.svg` `email.svg` `enviosms.svg` `balanca.svg` `transport.svg` |

#### Modo 2: Glyphicons (`font-icon`)

Usa a fonte Glyphicons embutida no Sankhya OM. Dois formatos aceitos:

```html
<!-- Formato curto — nome sem prefixo glyphicon- -->
<sk-icon font-icon="search"       style="font-size: 16px;"></sk-icon>
<sk-icon font-icon="ok"           style="font-size: 14px;"></sk-icon>
<sk-icon font-icon="remove"       style="font-size: 14px;"></sk-icon>
<sk-icon font-icon="dog"          style="font-size: 18px;"></sk-icon>
<sk-icon font-icon="download-alt" style="font-size: 14px;"></sk-icon>

<!-- Formato explícito — alias + classe completa (mais preciso) -->
<sk-icon font-icon="right-arrow glyphicon-right-arrow" style="font-size: 14px; display: inline; top: 1px;"></sk-icon>
<sk-icon font-icon="left-arrow  glyphicon-left-arrow"  style="font-size: 14px;"></sk-icon>
```

Glyphicons úteis em popups:

| `font-icon` | Uso | | `font-icon` | Uso |
|---|---|---|---|---|
| `search` | lupa | | `remove` | X / fechar |
| `ok` | check | | `ok-circle` | check circulado |
| `download-alt` | baixar | | `upload` | enviar |
| `arrow-left` | ← | | `arrow-right` | → |
| `chevron-left` | < | | `chevron-right` | > |
| `plus` | + | | `minus` | - |
| `edit` | lápis | | `trash` | lixeira |
| `warning-sign` | ⚠ | | `info-sign` | ℹ |
| `list` | lista | | `th-list` | grade |
| `floppy-disk` | salvar | | `folder-open` | pasta |
| `refresh` | atualizar | | `filter` | funil |
| `zoom-in` | ampliar | | `zoom-out` | reduzir |

#### Quando usar cada modo

| Situação | Modo |
|---|---|
| Ícone semântico do catálogo Sankhya (PDF, gráfico, balança, etc.) | `svg-src="/mge/assets/svg/nome.svg"` |
| Ícone funcional genérico (fechar, buscar, setas, ok) | `font-icon="nome-glyphicon"` |
| Tamanho/cor precisos via CSS | SVG (mais previsível) |
| Ícone inline em texto ou botão pequeno | Glyphicons (`font-icon`) |

### Botões

```html
<!-- Botão padrão -->
<button class="btn">Ação</button>

<!-- Botão primário (azul Sankhya) -->
<button class="btn" brand>Confirmar</button>

<!-- Botão de perigo (vermelho) -->
<button class="btn" danger>Cancelar</button>

<!-- Botão pequeno -->
<button class="btn btn-xs btn-default">Pequeno</button>
```

### Labels de tipo

```html
<span class="label label-info">Texto</span>
<span class="label label-primary">Inteiro</span>
<span class="label label-success">Data</span>
<span class="label label-warning">Lista</span>
<span class="label label-danger">Binário</span>
<span class="label label-default">Outros</span>

<!-- badge numérico -->
<span class="badge">42</span>
```

### Diretivas Angular

```html
ng-show="pagina === 1"
ng-if="condicao"
ng-repeat="item in lista"
ng-click="minhaFuncao(item)"
ng-dblclick="outraFuncao()"
ng-model="scope.filtro"
ng-disabled="!itemSelecionado"
ng-class="{'sk-row-selected': item.selecionado}"
```

### Serviços JS injetados automaticamente

```javascript
MessageUtils.showAlert(MessageUtils.TITLE_WARNING, "msg");
MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION, "msg");
scope.$dismiss();   /* fecha o popup */
ServiceProxy.callService('modulo@Servico.acao', {params: {}}, {}).then(fn);
```

---

## CSS de Grid com Cabeçalho Fixo

Para tabelas com scroll vertical e cabeçalho sticky — padrão testado e aprovado em produção:

```css
/* Wrapper com scroll vertical — header fica fixo */
.sk-scroll-wrap {
    overflow-y: auto;
    max-height: 345px;          /* ajustar conforme o popup */
    border: 1px solid #ccc;
    border-radius: 3px;
}

/* OBRIGATÓRIO: separate evita bug do sticky com border-collapse:collapse */
.sk-grid {
    width: 100%;
    margin: 0;
    table-layout: fixed;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 12px;
}

/* Sticky header */
.sk-grid thead th {
    position: sticky;
    top: 0;
    z-index: 10;
    background: #f0f0f0;
    padding: 7px 10px;
    text-align: left;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    border-bottom: 2px solid #bbb;
    border-right: 1px solid #ddd;
    /* box-shadow simula borda inferior ao rolar */
    box-shadow: 0 2px 2px -1px rgba(0,0,0,0.10);
}

.sk-grid tbody td {
    padding: 5px 10px;
    border-bottom: 1px solid #eee;
    border-right: 1px solid #eee;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.sk-row { cursor: pointer; }
.sk-row:hover td { background: #f5f9ff; }
.sk-row-selected td { background: #cce5ff !important; }

.sk-row-empty td {
    text-align: center;
    color: #999;
    padding: 20px;
    cursor: default;
}
```

> **Por que `border-collapse: separate`?**
> `position: sticky` em `thead th` não funciona corretamente com `border-collapse: collapse` — as bordas do cabeçalho desaparecem ao rolar. Com `separate + border-spacing: 0`, o sticky funciona e `box-shadow` simula a borda inferior.

---

## Colunas Redimensionáveis

Adicionar um div `.col-resizer` dentro de cada `<th>` e inicializar via JS:

### HTML

```html
<th style="width: 200px;">
    Nome
    <div class="col-resizer"></div>
</th>
```

```css
.col-resizer {
    position: absolute;
    right: 0; top: 0;
    height: 100%;
    width: 6px;
    cursor: col-resize;
    user-select: none;
    z-index: 1;
}
.col-resizer:hover, .col-resizer.resizing {
    background: rgba(33,150,243,0.4);
}
/* Necessário no th pai: */
thead th { position: relative; }
```

### JS

```javascript
function initResizableTable(tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    table.querySelectorAll('thead th .col-resizer').forEach(function(resizer) {
        var th = resizer.parentElement;
        var startX, startW;
        resizer.addEventListener('mousedown', function(e) {
            startX = e.pageX;
            startW = th.offsetWidth;
            resizer.classList.add('resizing');
            function onMove(ev) {
                th.style.width = Math.max(40, startW + ev.pageX - startX) + 'px';
            }
            function onUp() {
                resizer.classList.remove('resizing');
                document.removeEventListener('mousemove', onMove);
                document.removeEventListener('mouseup', onUp);
            }
            document.addEventListener('mousemove', onMove);
            document.addEventListener('mouseup', onUp);
            e.preventDefault();
            e.stopPropagation();
        });
    });
}

/* Inicializar na abertura do popup */
setTimeout(function() { initResizableTable('minha-tabela'); }, 150);

/* Re-inicializar ao navegar entre páginas do wizard */
scope.$watch('pagina', function(newVal) {
    if (newVal === 2) {
        setTimeout(function() { initResizableTable('tabela-pagina2'); }, 100);
    }
});
```

---

## Download de ZIP Client-Side (sem biblioteca externa)

Para gerar um `.zip` contendo um arquivo (ex: `metadata.xml`) diretamente no browser,
sem JSZip nem backend — puro JS com CRC-32 + formato STORED:

```javascript
function gerarZip(nomeArquivoInterno, conteudo, nomeZip) {
    try {
        var zipBytes = criarZip(nomeArquivoInterno, conteudo);
        var blob = new Blob([zipBytes], { type: 'application/zip' });
        var url  = URL.createObjectURL(blob);
        var link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', nomeZip);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        setTimeout(function() { URL.revokeObjectURL(url); }, 2000);
    } catch (e) {
        MessageUtils.showAlert(MessageUtils.TITLE_ERROR, 'Erro ao gerar ZIP: ' + (e.message || e));
    }
}

function criarZip(nomeArquivoInterno, conteudo) {
    var enc      = new TextEncoder();
    var fileData = enc.encode(conteudo);
    var fileName = enc.encode(nomeArquivoInterno);
    var crc     = crc32(fileData);
    var fSize   = fileData.length;
    var fnLen   = fileName.length;
    var now     = new Date();
    var dosDate = ((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate();
    var dosTime = (now.getHours() << 11) | (now.getMinutes() << 5) | Math.floor(now.getSeconds() / 2);
    function u16(n) { return [(n) & 0xFF, (n >>> 8) & 0xFF]; }
    function u32(n) { return [(n) & 0xFF, (n >>> 8) & 0xFF, (n >>> 16) & 0xFF, (n >>> 24) & 0xFF]; }
    var localHdr = [].concat(
        [0x50,0x4B,0x03,0x04], u16(20), u16(0), u16(0),
        u16(dosTime), u16(dosDate), u32(crc), u32(fSize), u32(fSize), u16(fnLen), u16(0));
    var centralHdr = [].concat(
        [0x50,0x4B,0x01,0x02], u16(20), u16(20), u16(0), u16(0),
        u16(dosTime), u16(dosDate), u32(crc), u32(fSize), u32(fSize),
        u16(fnLen), u16(0), u16(0), u16(0), u16(0), u32(0), u32(0));
    var centralDirOffset = localHdr.length + fnLen + fSize;
    var centralDirSize   = centralHdr.length + fnLen;
    var endRec = [].concat(
        [0x50,0x4B,0x05,0x06], u16(0), u16(0), u16(1), u16(1),
        u32(centralDirSize), u32(centralDirOffset), u16(0));
    var fnArr   = Array.from(fileName);
    var dataArr = Array.from(fileData);
    return new Uint8Array(localHdr.concat(fnArr, dataArr, centralHdr, fnArr, endRec));
}

var CRC32_TABLE = (function() {
    var t = new Uint32Array(256);
    for (var n = 0; n < 256; n++) {
        var c = n;
        for (var k = 0; k < 8; k++) { c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1); }
        t[n] = c;
    }
    return t;
}());

function crc32(data) {
    var crc = 0xFFFFFFFF;
    for (var i = 0; i < data.length; i++) {
        crc = (crc >>> 8) ^ CRC32_TABLE[(crc ^ data[i]) & 0xFF];
    }
    return (crc ^ 0xFFFFFFFF) >>> 0;
}
```

**Uso típico para Construtor de Telas:**

```javascript
function gerarArquivo() {
    var xml  = construirMetadataXml(entidade, camposSelecionados);
    var nome = 'Metadados_' + entidade.nometab + '.zip';
    gerarZip('metadata.xml', xml, nome);
    scope.$dismiss();
    MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION,
        nome + ' gerado! Importe em: <b>Gerenciamento &gt; Construtor de Telas &gt; Importar Metadados</b>');
}
```

---

## Download Simples (arquivo único sem ZIP)

Para XML, CSV, JSON ou TXT sem necessidade de compactação:

```javascript
function baixarArquivo(conteudo, nomeArquivo, tipoMime) {
    try {
        var blob = new Blob([conteudo], { type: tipoMime + ';charset=utf-8;' });
        var url  = URL.createObjectURL(blob);
        var link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', nomeArquivo);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        setTimeout(function() { URL.revokeObjectURL(url); }, 1500);
    } catch (e) {
        MessageUtils.showAlert(MessageUtils.TITLE_ERROR, 'Erro ao gerar arquivo: ' + e.message);
    }
}
```

---

## Popup Wizard — Seleção + Configuração (2 Páginas)

Template completo disponível em `assets/popup/PopUpWizard2Paginas.html` e `assets/popup/PopUpWizard2Paginas.js`.

### Padrão geral

- Página 1: lista com filtro + seleção de item (click/duplo clique)
- Página 2: detalhes do item + seleção/configuração (checkboxes, opções)
- Navegação: Próximo / Voltar / Cancelar / Confirmar
- Estado mantido no scope Angular — sem chamadas ao servidor entre páginas

### Java — pré-carregar dados e abrir popup

```java
private static final String POPUP_HTML = "/{modulo}/popup/PopUpWizard2Paginas.html";
private static final String POPUP_JS   = "/{modulo}/popup/PopUpWizard2Paginas.js";

String itensJson = MinhaHelper.buscarItensJson();  /* "[{\"id\":1,...}]" */

String popup = new PopUpBuilder.Builder()
    .setTitle("Selecionar e Configurar")
    .setHtmlFile(MinhaClasse.class.getResourceAsStream(POPUP_HTML))
    .setJsFile(MinhaClasse.class.getResourceAsStream(POPUP_JS))
    .setWidth(750).setHeight(500)
    .addVariable("itensJson", itensJson)
    .build();

MessageUtils.showInfo(popup);
```

### JS — estrutura básica

```javascript
/* Variável injetada pelo Java */
var itens = JSON.parse(itensJson);

scope.pagina          = 1;
scope.itens           = itens;
scope.itemSelecionado = null;
scope.filtro          = '';

scope.itensFiltrados   = itensFiltrados;
scope.selecionarItem   = selecionarItem;
scope.irParaPagina2    = irParaPagina2;
scope.voltar           = voltar;
scope.confirmar        = confirmar;

setTimeout(function() { initResizableTable('tbl-p1'); }, 150);

scope.$watch('pagina', function(val) {
    if (val === 2) setTimeout(function() { initResizableTable('tbl-p2'); }, 100);
});

function itensFiltrados() {
    var f = (scope.filtro || '').toUpperCase().trim();
    if (!f) return scope.itens;
    return scope.itens.filter(function(i) {
        return i.nome.toUpperCase().indexOf(f) !== -1;
    });
}

function selecionarItem(item) { scope.itemSelecionado = item; }

function irParaPagina2() {
    if (!scope.itemSelecionado) {
        MessageUtils.showAlert(MessageUtils.TITLE_WARNING, 'Selecione um item antes de continuar!');
        return;
    }
    scope.pagina = 2;
}

function voltar() { scope.pagina = 1; }

function confirmar() {
    /* executar ação final, ex: gerarZip(...) ou ServiceProxy.callService(...) */
    scope.$dismiss();
}
```

### HTML — estrutura básica

```html
<div ng-show="pagina === 1">
    <sk-vbox gap="8">
        <sk-hbox gap="8" style="align-items: center;">
            <sk-icon font-icon="search" style="color: #888;"></sk-icon>
            <input type="text" ng-model="filtro" placeholder="Filtrar..."
                   class="form-control" style="flex: 1; height: 30px; font-size: 12px;"/>
        </sk-hbox>
        <div class="sk-scroll-wrap">
            <table id="tbl-p1" class="sk-grid">
                <thead>
                    <tr>
                        <th style="width: 200px;">Nome <div class="col-resizer"></div></th>
                        <th>Descri&ccedil;&atilde;o <div class="col-resizer"></div></th>
                    </tr>
                </thead>
                <tbody>
                    <tr ng-repeat="item in itensFiltrados()"
                        ng-click="selecionarItem(item)"
                        ng-dblclick="irParaPagina2()"
                        ng-class="{'sk-row-selected': itemSelecionado && itemSelecionado.id === item.id}"
                        class="sk-row">
                        <td>{{item.nome}}</td>
                        <td>{{item.descr}}</td>
                    </tr>
                    <tr ng-if="itensFiltrados().length === 0" class="sk-row-empty">
                        <td colspan="2">Nenhum item encontrado.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <sk-hbox gap="8" style="justify-content: flex-end; margin-top: 4px;">
            <button class="btn" ng-click="$dismiss()" danger style="min-width: 100px;">
                <sk-hbox gap="4" style="align-items: center; justify-content: center;">
                    <sk-icon font-icon="remove" style="font-size: 14px;"></sk-icon>
                    <span>Cancelar</span>
                </sk-hbox>
            </button>
            <button class="btn" ng-click="irParaPagina2()"
                    ng-disabled="!itemSelecionado" brand style="min-width: 130px;">
                <sk-hbox gap="4" style="align-items: center; justify-content: center;">
                    <span>Pr&oacute;ximo</span>
                    <sk-icon font-icon="chevron-right" style="font-size: 14px;"></sk-icon>
                </sk-hbox>
            </button>
        </sk-hbox>
    </sk-vbox>
</div>

<div ng-show="pagina === 2">
    <sk-vbox gap="8">
        <!-- cabe&ccedil;alho com item selecionado -->
        <div style="background: #e8f4fd; padding: 8px 12px; border-radius: 3px; border-left: 4px solid #2196F3;">
            <strong>{{itemSelecionado.nome}}</strong>
        </div>
        <!-- conte&uacute;do da p&aacute;gina 2 -->
        <sk-hbox gap="8" style="justify-content: space-between; margin-top: 4px;">
            <button class="btn" ng-click="voltar()">
                <sk-hbox gap="4" style="align-items: center; justify-content: center;">
                    <sk-icon font-icon="chevron-left" style="font-size: 14px;"></sk-icon>
                    <span>Voltar</span>
                </sk-hbox>
            </button>
            <sk-hbox gap="8">
                <button class="btn" ng-click="$dismiss()" danger style="min-width: 100px;">
                    <sk-hbox gap="4" style="align-items: center; justify-content: center;">
                        <sk-icon font-icon="remove" style="font-size: 14px;"></sk-icon>
                        <span>Cancelar</span>
                    </sk-hbox>
                </button>
                <button class="btn" ng-click="confirmar()" brand style="min-width: 130px;">
                    <sk-hbox gap="4" style="align-items: center; justify-content: center;">
                        <sk-icon svg-src="/mge/assets/svg/check-finish.svg" style="max-height: 13px; margin-right: 2px;"></sk-icon>
                        <span>Confirmar</span>
                    </sk-hbox>
                </button>
            </sk-hbox>
        </sk-hbox>
    </sk-vbox>
</div>
```

> **Wizard completo de produção** (com sticky header, colunas redimensionáveis, ZIP generation e labels de tipo):
> ver `assets/popup/PopUpWizard2Paginas.html` e `assets/popup/PopUpWizard2Paginas.js`

---

## Tipos de Popup

| Tipo | Largura | Altura | Template |
|---|---|---|---|
| Confirmação simples | 400px | 200px | `assets/popup/PopUpConfirmacao.html/.js` |
| Seleção em Grid | 700-900px | 400-500px | `assets/popup/PopUpSelecao.html/.js` |
| Formulário | 500-600px | 350-450px | `assets/popup/PopUpFormulario.html/.js` |
| **Wizard 2 Páginas** | **750px** | **500px** | **`assets/popup/PopUpWizard2Paginas.html/.js`** |

---

## Integração com Artefatos

### Botão de Ação

```java
public class MeuBotaoAcao implements AcaoRotinaJava {
    private static final String POPUP_HTML = "/{modulo}/popup/PopUpNome.html";
    private static final String POPUP_JS   = "/{modulo}/popup/PopUpNome.js";

    @Override
    public void doAction(ContextoAcao ctx) throws Exception {
        NomeService nomeService = new NomeService();
		String dadosJson = nomeService.buscarDadosJson();
        String popup = new PopUpBuilder.Builder()
            .setTitle("T&iacute;tulo")
            .setHtmlFile(MeuBotaoAcao.class.getResourceAsStream(POPUP_HTML))
            .setJsFile(MeuBotaoAcao.class.getResourceAsStream(POPUP_JS))
            .setWidth(750).setHeight(500)
            .addVariable("dadosJson", dadosJson)
            .build();
        MessageUtils.showInfo(popup);
        /* processamento continua no JS via callback/download */
    }
}
```

### Evento ou Regra de Negócio

```java
/* beforeUpdate de EventoProgramavelJava */
public void beforeUpdate(PersistenceEvent event) throws Exception {
    DynamicVO vo = (DynamicVO) event.getVo();
    String popup = new PopUpBuilder.Builder()
        .setTitle("Confirma&ccedil;&atilde;o")
        .setHtmlFile(MeuEvento.class.getResourceAsStream("/{modulo}/popup/PopUpConfirmar.html"))
        .setJsFile(MeuEvento.class.getResourceAsStream("/{modulo}/popup/PopUpConfirmar.js"))
        .setWidth(400).setHeight(200)
        .addVariable("mensagem", "Deseja prosseguir?")
        .build();
    MessageUtils.showInfo(popup);
    /* fluxo continua no JS via ServiceProxy */
}
```

---

## Checklist

- [ ] `PopUpBuilder.java` existe em `br.com.sankhya.dstech.utils` (copiar de `examples/PopUpBuilder.java`)
- [ ] HTML e JS em `Java/resources/{modulo}/popup/`
- [ ] `build.gradle`: `include "${moduleName}/**"` (não `*.sql`)
- [ ] `getResourceAsStream` usa path `"/{modulo}/popup/PopUpNome.html"` (classpath a partir da raiz do JAR)
- [ ] Nenhum comentário `//` no arquivo JS — apenas `/* */`
- [ ] Nenhum caractere acentuado direto no HTML — usar entidades (`&atilde;`, `&ccedil;` etc.)
- [ ] CSS usa `border-collapse: separate; border-spacing: 0` para sticky funcionar
- [ ] `.col-resizer` em cada `<th>` que deve ser redimensionável
- [ ] `initResizableTable(id)` chamado com `setTimeout(..., 150)` após abertura
- [ ] `scope.$watch('pagina', ...)` reinicializa colunas ao navegar no wizard
- [ ] `scope.$dismiss()` para fechar popup após confirmar/cancelar
- [ ] `MessageUtils` para feedback ao usuário
- [ ] Wizard: `ng-show="pagina === N"` (não `ng-if` — não destruir o DOM entre páginas)
- [ ] Variáveis passadas via `addVariable()` documentadas nos comentários do JS
