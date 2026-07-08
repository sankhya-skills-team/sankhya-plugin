# sankhya-js — snk.components UI: Layout, Tabs e Popups

Componentes de interface: layout, tabs, wizard e popups.

> Para botões, ícones, listas e outros componentes visuais: ver `sankhya-js-snk-components-ui-b.md`

---

## Layout / Containers

### hbox / sk-hbox

**ID:** `snk.components.box.directive:hbox`

Agrupamento horizontal de elementos.

```html
<sk-hbox gap="{int}" sk-onload="{function}" button-container="{boolean}">
    <!-- conteúdo -->
</sk-hbox>
```

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `gap` | int | Espaço horizontal entre filhos (px) |
| `sk-onload` | function | Executada no postLink. Recebe `$event` com `target` |
| `button-container` | boolean | Aplica cor de barra de botões e gap padrão |

### vbox / sk-vbox

**ID:** `snk.components.box.directive:vbox`

Agrupamento vertical de elementos (análogo ao `hbox` na vertical).

### sk-divided-box / sk-hdividedbox / sk-vdividedbox

**ID:** `snk.components.dividedbox`

Container dividido com separador redimensionável entre dois painéis.

```html
<sk-hdividedbox>  <!-- horizontal -->
<sk-vdividedbox>  <!-- vertical -->
```

### sk-double-face-panel

**ID:** `snk.components.doublefacepanel.directive:sk-double-face-panel`

Painel com duas faces alternáveis (frente/verso).

```html
<sk-double-face-panel>
    <sk-face>Frente</sk-face>
    <sk-face>Verso</sk-face>
</sk-double-face-panel>
```

### sk-group-container

**ID:** `snk.components.groupcontainer.directive:sk-group-container`

Container com título de agrupamento.

### sk-resizable

**ID:** `snk.components.resizable.directive:sk-resizable`

Torna um container redimensionável pelo usuário.

---

## Tabs e Navegação

### sk-tab

**ID:** `snk.components.tab.directive:sk-tab`
**Tipo:** directive

Componente de abas com `sk-tabnavigator` + `sk-viewstack` integrados.

```html
<sk-tab
    [sk-selected-index="{number}"]
    [sk-on-select="{function}"]
    [sk-creation-policy="{string}"]>
    <sk-tab-item label="Aba 1">
        <!-- conteúdo -->
    </sk-tab-item>
    <sk-tab-item label="Aba 2">
        <!-- conteúdo -->
    </sk-tab-item>
</sk-tab>
```

| Parâmetro | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-selected-index` | number | 0 | Índice da aba ativa |
| `sk-on-select` | function | - | Callback ao selecionar aba |
| `sk-creation-policy` | string | `auto` | `auto` = renderiza sob demanda; `all` = renderiza tudo |

**Exemplo com controladores por aba:**
```html
<sk-tab sk-selected-index="ctrl.abaAtual" sk-on-select="ctrl.onAbaChange">
    <sk-tab-item label="Dados Gerais">
        <sk-form sk-dataset="ctrl.dataset"></sk-form>
    </sk-tab-item>
    <sk-tab-item label="Itens">
        <div ng-controller="ItensController as ctrlItens">
            <sk-datagrid sk-dataset="ctrlItens.dataset"></sk-datagrid>
        </div>
    </sk-tab-item>
</sk-tab>
```

### sk-tabnavigator

**ID:** `snk.components.tabnavigator.directive:sk-tabnavigator`

Navegador de abas stand-alone.

```html
<sk-tabnavigator>
    <sk-tabnavigator-item label="Aba 1"></sk-tabnavigator-item>
</sk-tabnavigator>
```

### sk-tree

**ID:** `snk.components.tabnavigator.directive:sk-tree`

Navegação em árvore.

### sk-viewstack

**ID:** `snk.components.viewstack.directive:sk-viewstack`

Container de múltiplos painéis onde apenas um é visível por vez.

### sk-wizard

**ID:** `snk.components.wizard.directive:sk-wizard`

Passo a passo (stepper) — exibe um container por vez em sequência.

```html
<sk-wizard
    [sk-selected-index="{number}"]
    [sk-on-select="{function}"]
    [sk-creation-policy="{string}"]>
    <!-- sk-tab-item como passos -->
</sk-wizard>
```

---

## Popups

### SanPopup

**ID:** `snk.components.popup.service:SanPopup`
**Tipo:** service

Serviço padrão para abrir popups. **Todos os popups do sistema devem usar este serviço.**

**Método `open(userPopupOptions)`:**

```js
var popupInstance = SanPopup.open({
    title: 'Meu Popup',                          // obrigatório
    templateUrl: 'caminho/template.tpl.html',
    controller: 'MeuController',
    controllerAs: 'ctrl',
    size: 'md',                                  // 'sm', 'md', 'lg', 'alert'
    type: 'default',                             // 'default', 'danger', 'success', 'info', 'primary', 'warning', 'brand', 'gray'
    grayBG: true,                                // fundo cinza para forms
    backdrop: 'static',                          // 'static' = não fecha ao clicar fora
    keyboard: true,                              // ESC fecha
    showBtnOk: true,
    showBtnCancel: true,
    showBtnNo: false,
    okBtnLabel: 'Confirmar',
    cancelBtnLabel: 'Cancelar',
    noBtnLabel: 'Não',
    leftBottomBar: [],                           // botões à esquerda do footer
    rightBottomBar: [],                          // botões à direita do footer
    resolve: {
        parameters: function() { return minhaData; }
    }
});

popupInstance.result
    .then(function(result) { /* ok / success */ })
    .catch(function(reason) { /* cancelado / dismiss */ });
```

**Objeto retornado por `open()`:**

| Propriedade/Método | Descrição |
|---|---|
| `result` | Promise: resolve no success, rejeita no dismiss |
| `success(result)` | Fecha com sucesso |
| `dismiss(reason)` | Fecha por cancelamento |
| `opened` | Promise resolvida quando o popup abrir |
| `rendered` | Promise resolvida quando o popup renderizar |
| `setTitle(newTitle)` | Altera título em runtime |

**No controller do popup:**
```js
// Injetar $popupInstance para controlar o popup
function MeuController($popupInstance, parameters) {
    var ctrl = this;
    ctrl.salvar = function() {
        $popupInstance.success(ctrl.dados);
    };
    ctrl.fechar = function() {
        $popupInstance.dismiss('cancelado');
    };
    // Sobrescrever título
    ctrl.$popupTitle = 'Novo Título';
    // Desabilitar botão Ok
    ctrl.$enableBtnOk = false;
}
```

**No template:** `$success(result)` e `$dismiss(reason)` disponíveis no scope.

**Exemplo completo:**
```js
SanPopup.open({
    title: 'Selecionar Produto',
    templateUrl: 'html5/MinhaApp/popups/selecionarproduto.tpl.html',
    controller: 'SelecionarProdutoController',
    controllerAs: 'ctrl',
    size: 'lg',
    grayBG: true,
    backdrop: 'static',
    resolve: {
        filtro: function() { return ctrl.filtroAtual; }
    }
}).result.then(function(produto) {
    ctrl.produtoSelecionado = produto;
});
```

### sk-popup

**ID:** `snk.components.popup.directive:sk-popup`

Diretiva de popup para uso declarativo.

### PopUpParameter

**ID:** `snk.components.popupparameter.service:PopUpParameter`

Serviço para passar parâmetros entre controladores de popup.

### IPopUpInterceptor

**ID:** `snk.components.popup.interfaces:IPopUpInterceptor`

Interface para interceptar o comportamento de popups.

---

## Accordion

### sk-accordion

**ID:** `snk.components.accordion.directive:sk-accordion`

Container accordion expansível/recolhível.

### sk-accordion-group

**ID:** `snk.components.accordion.directive:sk-accordion-group`

Grupo dentro do accordion.

### sk-ag-grid

**ID:** `snk.components.accordion.directive:sk-ag-grid`

Accordion com ag-grid integrado.
