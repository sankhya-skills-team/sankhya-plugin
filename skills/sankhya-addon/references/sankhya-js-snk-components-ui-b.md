# sankhya-js — snk.components UI: Botões, Visuais e Listas

Botões, ícones, loading, seleção, listas e componentes especializados.

> Para layout, tabs e popups: ver `sankhya-js-snk-components-ui.md`

---

## Botões

### button (directive)

**ID:** `snk.components.button.directive:button`

Botão padrão do framework com suporte a temas. Usar como atributo em elementos `<button>`.

```html
<button default>Padrão</button>
<button primary>Primário</button>
<button danger>Perigo</button>
<button success>Sucesso</button>
<button small>Pequeno</button>
<button large>Grande</button>
```

### ButtonThemes

**ID:** `snk.components.button.service:ButtonThemes`

Serviço com os temas disponíveis para botões.

### sk-btn-novo

**ID:** `snk.components.btnnovo.directive:sk-btn-novo`

Botão "Novo" padronizado para inclusão de registros.

### sk-btn-place

**ID:** `snk.components.btnnovo.directive:sk-btn-place`

Espaço reservado para botões no layout — garante espaçamento consistente.

### sk-btn-old-layout

**ID:** `snk.components.btnoldlayout.directive:sk-btn-old-layout`

Botão para retornar ao layout antigo (Flex). Apresentado quando `sk-can-back-to-old-layout="true"` no dynaform.

### sk-btn-other-options

**ID:** `snk.components.btnotheroptions`

Botão "Outras Opções" com menu dropdown de ações adicionais.

---

## Componentes Visuais

### sk-icon

**ID:** `snk.components.icon.directive:sk-icon`

Exibe ícone da fonte de ícones do Sankhya.

```html
<sk-icon font-icon="user"></sk-icon>
<sk-icon font-icon="edit"></sk-icon>
<sk-icon font-icon="trash"></sk-icon>
```

### font (directive)

**ID:** `snk.components.icon.directive:font`

Fonte de ícones base do framework.

### sk-label

**ID:** `snk.components.label.directive:sk-label`

Label estilizado pelo tema.

### sk-title

**ID:** `snk.components.icon.directive:sk-title`

Título de seção com estilo padrão.

### sk-list

**ID:** `snk.components.icon.directive:sk-list`

Lista estilizada.

### sk-load

**ID:** `snk.components.load.directive:sk-load`

Indicador de carregamento inline.

### sk-loading-panel

**ID:** `snk.components.loadingpanel.directive:sk-loading-panel`

Painel de carregamento sobreposto ao conteúdo.

### WaitWindow

**ID:** `snk.components.waitwindow.service:WaitWindow`

Serviço para exibir/ocultar janela de espera global (bloqueia interação).

```js
WaitWindow.open('Processando...');
// ...
WaitWindow.close();
```

### sk-popover

**ID:** `snk.components.popover.directive:sk-popover`

Popover — balloon de informações exibido ao hover ou clique.

### tooltip

**ID:** `snk.components.tooltip.directive:tooltip`

Tooltip simples via atributo.

```html
<button tooltip="Clique para salvar">Salvar</button>
```

### sk-help-tip

**ID:** `snk.components.sk-help-tip.directive:sk-help-tip`

Ícone de interrogação com tooltip explicativo. Útil para documentar campos.

---

## Componentes de Seleção e Listas

### sk-checkbox

**ID:** `snk.components.checkbox.directive:sk-checkbox`

Checkbox individual.

### sk-checkbox-list

**ID:** `snk.components.checkboxlist.directive:sk-checkbox-list`

Lista de checkboxes para seleção múltipla.

### sk-two-lists

**ID:** `snk.components.twolists.directive:sk-two-lists`

Componente de duas listas com botões para transferir itens entre elas.

### sk-draggable-list

**ID:** `snk.components.draggablelist.directive:sk-draggable-list`

Lista com suporte a reordenação por drag-and-drop.

### sk-interval-selector

**ID:** `snk.components.intervalselector.directive:sk-interval-selector`

Seletor de intervalo (ex: faixa de valores).

### sk-select-distinct-input

**ID:** `snk.components.selectdistinctinput.directive:sk-select-distinct-input`

Input com autocomplete baseado em valores distintos de um campo do dataset.

### sk-tags-input

**ID:** `snk.components.tagsinput.directive:sk-tags-input`

Input para entrada de múltiplas tags/palavras-chave.

### sk-dropdown-menu

**ID:** `snk.components.dropdownmenu.directive:sk-dropdown-menu`

Menu dropdown customizável.

### sglclick

**ID:** `snk.components.sglclick.directive:sglclick`

Captura click simples distinguindo de duplo-clique.

---

## Componentes de Dados Especializados

### sk-attach

**ID:** `snk.components.attach.directive:sk-attach`

Componente de anexos de arquivos.

### sk-entity-attach

**ID:** `snk.components.entityattach.directive:sk-entity-attach`

Anexo vinculado a uma entidade específica.

### sk-image-input

**ID:** `snk.components.entityattach.directive:sk-image-input`

Input de imagem com preview.

### sk-entity-card

**ID:** `snk.components.entitycard.directive:sk-entity-card`

Card de apresentação de entidade com links e toolbar.

```html
<sk-entity-card>
    <sk-entity-card-toolbar><!-- botões --></sk-entity-card-toolbar>
    <sk-entity-card-link><!-- links --></sk-entity-card-link>
</sk-entity-card>
```

### sk-rich-text-link / sk-text-area-link

**ID:** `snk.components.entitycard`

Links para campos rich text e textarea.

### sk-entity-detail

**ID:** `snk.components.entitydetail.directive:sk-entity-detail`

Detalhe de entidade com suporte a interceptor `IEntityDetailInterceptor`.

### sk-entity-list

**ID:** `snk.components.entitylist.directive:sk-entity-list`

Lista de registros de entidade com paginação.

### sk-entity-nav

**ID:** `snk.components.entitynav.directive:sk-entity-nav`

Navegação entre registros de entidade.

### sk-entity-start-page

**ID:** `snk.components.navigator.directive:sk-entity-start-page`

Página inicial da entidade exibida antes de listar registros.

---

## Componentes de Edição e Ferramentas

### sk-code-editor

**ID:** `snk.components.codeeditor.directive:sk-code-editor`

Editor de código com syntax highlighting (ACE Editor).

### sk-cron-syntax-selector

**ID:** `snk.components.cronsyntaxselector.directive:sk-cron-syntax-selector`

Seletor visual de expressão CRON.

### sk-color-picker

**ID:** `snk.components.colorpicker.directive:sk-color-picker`

Seletor de cor.

### sk-change-order-bar

**ID:** `snk.components.colorpicker.directive:sk-change-order-bar`

Barra para alterar ordenação de registros.

### sk-records-organizer-bar

**ID:** `snk.components.colorpicker.directive:sk-records-organizer-bar`

Barra organizadora de registros.

### sk-mask-builder

**ID:** `snk.components.sk-mask-builder.directive:sk-mask-builder`

Editor visual de máscara de campo.

---

## Componentes de Drag-and-Drop

### sk-draggable

**ID:** `snk.components.draggable.directive:sk-draggable`

Torna um elemento arrastável.

---

## Componentes de Filtro

### sk-dynamic-filter-panel

**ID:** `snk.components.dynamicfilterpanel.directive:sk-dynamic-filter-panel`

Painel de filtros dinâmicos baseado em metadados.

### sk-personalized-filter

**ID:** `snk.components.personalizedfilter.directive:sk-personalized-filter`

Filtro personalizado criado pelo usuário.

### filter-assistent

**ID:** `snk.components.personalizedfilter.directive:filter-assistent`

Assistente de criação de filtros personalizados.

---

## Organização e Apresentação

### sk-sidenav

**ID:** `snk.components.sidenav.directive:sk-sidenav`

Painel lateral deslizante (drawer).

### sk-sidenav-focus

**ID:** `snk.components.sidenav.directive:sk-sidenav-focus`

Gerenciamento de foco no sidenav.

### skSidenav

**ID:** `snk.components.sidenav.service:skSidenav`

Serviço para controlar o sidenav programaticamente.

### sk-list-order

**ID:** `snk.components.listOrder.directive:sk-list-order`

Ordenação de listas por drag-and-drop.

### sk-time-line-diagram

**ID:** `snk.components.timelinediagram`

Diagrama de linha do tempo com tarefas e ações.

| Componente | ID | Descrição |
|---|---|---|
| `sk-time-line-diagram` | `snk.components.timelinediagram:sk-time-line-diagram` | Directive principal |
| `TimeLineTask` | `snk.components.timelinediagram:TimeLineTask` | Modelo de tarefa |
| `IActionInterceptor` | `snk.components.timelinediagram:IActionInterceptor` | Interface de interceptação |

### sk-divider

**ID:** `snk.components.divider`

Linha divisória visual entre seções.

| Componente | ID | Descrição |
|---|---|---|
| `sk-grid-config` | `snk.components.gridconfig.directive:sk-grid-config` | Configuração de colunas pelo usuário |
| `GridConfigInstance` | `snk.components.gridconfig.service:GridConfigInstance` | Serviço de instância de configuração |
| `sk-grid-printer` | `snk.components.gridprinter.directive:sk-grid-printer` | Impressão de grade |
| `gridstatistics` | `snk.components.gridstatistics.directive:gridstatistics` | Estatísticas e totalizadores de colunas |
| `sk-navigator` | ver `sankhya-js-snk-components-grid-nav.md` | Barra de navegação CRUD |
