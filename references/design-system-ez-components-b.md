# Design System — Componentes ez- (Parte B)

Continuação de: `design-system-ez-components.md`. Componentes a partir de `ez-modal`.

Fonte: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/

---

## ez-modal

**Tag:** `<ez-modal>`

Overlay de diálogo com tamanhos configuráveis, modos de altura e opções de fechamento automático.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `align` | `align` | `"left"\|"right"` | `undefined` | Posicionamento |
| `closeEsc` | `close-esc` | `boolean` | `false` | Fecha ao pressionar ESC |
| `closeOutsideClick` | `close-outside-click` | `boolean` | `false` | Fecha ao clicar fora |
| `closeOutsideLeave` | `close-outside-leave` | `boolean` | `false` | Fecha ao sair com o mouse |
| `heightMode` | `height-mode` | `"full"\|"regular"` | `"regular"` | Expansão vertical |
| `modalSize` | `modal-size` | `string` | `undefined` | Tamanho baseado em grid (ex: `col-sd-3`) |
| `opened` | `opened` | `boolean` | `true` | Visibilidade |
| `scrim` | `scrim` | `"light"\|"medium"\|"none"` | `"medium"` | Overlay de fundo |

**Eventos:** `ezOpenModal`, `ezCloseModal: CustomEvent<boolean>`, `ezModalAction: CustomEvent<string>`

---

## ez-modal-container

**Tag:** `<ez-modal-container>`

Container padronizado para modais e popups com cabeçalho, área de conteúdo, rodapé e atalhos de teclado.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `modalTitle` | `modal-title` | `string` | `undefined` | Título |
| `modalSubTitle` | `modal-sub-title` | `string` | `undefined` | Subtítulo |
| `okButtonLabel` | `ok-button-label` | `string` | `undefined` | Texto botão OK |
| `okButtonStatus` | `ok-button-status` | `"DISABLED"\|"ENABLED"\|"HIDDEN"` | `undefined` | Estado botão OK |
| `cancelButtonLabel` | `cancel-button-label` | `string` | `undefined` | Texto botão Cancelar |
| `cancelButtonStatus` | `cancel-button-status` | `"DISABLED"\|"ENABLED"\|"HIDDEN"` | `undefined` | Estado botão Cancelar |
| `showCloseButton` | `show-close-button` | `boolean` | `true` | Exibe botão X |
| `showTitleBar` | `show-title-bar` | `boolean` | `true` | Exibe cabeçalho |

**Eventos:** `ezModalAction` — emite `"OK"` (Enter/botão), `"CANCEL"`, `"CLOSE"` (X/Esc), `"LOAD"` (após montagem)

```html
<ez-modal-container modal-title="Confirmar" ok-button-label="OK" cancel-button-label="Cancelar">
  <p>Conteúdo aqui</p>
</ez-modal-container>
```

---

## ez-multi-selection-list

**Tag:** `<ez-multi-selection-list>`

Seleção múltipla de itens com opções estáticas ou busca dinâmica via backend.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `columnName` | `column-name` | `string` | `undefined` | Nome da coluna para filtro |
| `dataSource` | — | `IMultiSelectionListDataSource` | `undefined` | Fonte de dados dinâmica |
| `isTextSearch` | `is-text-search` | `boolean` | `false` | Tipo de busca (texto vs numérico) |
| `options` | — | `IMultiSelectionOption[]` | `undefined` | Opções estáticas |
| `useOptions` | `use-options` | `boolean` | `false` | Usar lista de opções estáticas |

**Eventos:** `changeFilteredOptions: CustomEvent<IMultiSelectionOption[]>`

**Métodos:** `clearFilteredOptions()`

---

## ez-number-input

**Tag:** `<ez-number-input>`

Input numérico com validação, precisão decimal e modos de exibição.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `allowNegative` | `allow-negative` | `boolean` | `true` | Permite negativos |
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `label` | `label` | `string` | `undefined` | Label |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `precision` | `precision` | `number` | `undefined` | Casas decimais |
| `value` | `value` | `number` | `undefined` | Valor |

**Eventos:** `ezChange: CustomEvent<number>`, `ezInput`, `ezStartChange`, `ezCancelWaitingChange`

**Métodos:** `getValueAsync()`, `isInvalid()`, `setFocus()`, `setBlur()`

---

## ez-pagination

**Tag:** `<ez-pagination>`

Paginação reutilizável e responsiva com dois tipos de exibição.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `totalItems` | `number` | obrigatório | Total de itens |
| `pageSize` | `number` | obrigatório | Itens por página |
| `type` | `string` | `"default"` | Tipo: `"default"` ou `"numeric"` |
| `hideInfoLabel` | `boolean` | `false` | Oculta texto de paginação |
| `pageLimit` | `number` | `10` | Máximo de páginas no modo numérico |

**Eventos:** `ezPageChange`

---

## ez-popover

**Tag:** `<ez-popover>`

Controla visibilidade de conteúdo com gerenciamento de overlay e opções de posicionamento.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoClose` | `auto-close` | `boolean` | `true` | Fecha ao clicar fora |
| `boxWidth` | `box-width` | `"fit-content"\|"full-width"` | `"fit-content"` | Largura |
| `opened` | `opened` | `boolean` | `undefined` | Estado aberto/fechado |
| `overlayType` | `overlay-type` | `"light"\|"medium"\|"none"` | `"light"` | Overlay |

**Eventos:** `ezVisibilityChange: CustomEvent<boolean>`

**Métodos:** `show(top?, left?)`, `hide()`, `showUnder(element, options?)`, `updatePosition(top?, left?)`

---

## ez-popover-plus

**Tag:** `<ez-popover-plus>`

Overlay contextual leve com ancoragem em elemento, controle de posicionamento e opções avançadas.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `anchorElement` | `HTMLElement\|string\|Array` | `undefined` | Elemento âncora |
| `autoClose` | `boolean` | `true` | Fecha ao clicar fora |
| `boxWidth` | `"fit-content"\|"full-width"` | `"fit-content"` | Largura |
| `opened` | `boolean` | `false` | Visibilidade |
| `overlayType` | `"light"\|"medium"\|"none"` | `"light"` | Overlay |
| `useAnchorSize` | `boolean` | `false` | Usa tamanho do âncora |

**Eventos:** `ezVisibilityChange: CustomEvent<boolean>`

**Métodos:** `show(top?, left?)`, `showUnder(element, options?)`, `hide()`, `setAnchorElement(anchor)`, `setOptions(options)`, `updatePosition(top?, left?)`

---

## ez-popup

**Tag:** `<ez-popup>`

Janelas flutuantes para mensagens breves (notificações/avisos) que requerem ação do usuário para fechar.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoClose` | `auto-close` | `boolean` | `true` | Fecha ao clicar fora |
| `ezTitle` | `ez-title` | `string` | `undefined` | Título |
| `footerButtons` | — | `Partial<EzButtonProps>[]` | `[]` | Botões do rodapé (até 3) |
| `heightMode` | `height-mode` | `"auto"\|"full"` | `"full"` | Cálculo de altura |
| `opened` | `opened` | `boolean` | `false` | Estado aberto |
| `size` | `size` | `"auto"\|"x-small"\|"small"\|"medium"\|"large"\|"x-large"` | `"medium"` | Largura |
| `useHeader` | `use-header` | `boolean` | `true` | Exibe cabeçalho |

**Eventos:** `ezClosePopup`, `ezPopupAction: CustomEvent<string>`

---

## ez-progress-bar

**Tag:** `<ez-progress-bar>`

Barra de progresso com label e texto auxiliar para contextualizar carregamento.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `label` | `label` | `string` | `undefined` | Rótulo acima da barra |
| `helpText` | `help-text` | `string` | `undefined` | Mensagem auxiliar |
| `percent` | `percent` | `number` | `undefined` | Percentual de preenchimento |

```html
<ez-progress-bar label="Carregando" help-text="Aguarde..." percent="65"></ez-progress-bar>
```

---

## ez-radio-button

**Tag:** `<ez-radio-button>`

Seleção de uma única opção de um conjunto predefinido.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `direction` | `direction` | `"horizontal"\|"vertical"` | `"vertical"` | Orientação |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `label` | `label` | `string` | `undefined` | Título do campo |
| `options` | — | `Radio[]` | `[]` | Opções disponíveis |
| `value` | `value` | `any` | `undefined` | Valor selecionado |

**Eventos:** `ezChange: CustomEvent<any>`

---

## ez-rich-text

**Tag:** `<ez-rich-text>`

Editor HTML com formatação, listas, imagens, links e modo preview.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `showPreview` | `boolean` | `true` | Modo preview |
| `showUndoRedo` | `boolean` | `true` | Ações desfazer/refazer |
| `showTextFormat` | `boolean` | `true` | Negrito, itálico, sublinhado |
| `showConfigs` | `boolean` | `true` | Listas, imagens, links |
| `enabled` | `boolean` | `true` | Modo edição |
| `value` | `string` | — | Conteúdo HTML |

**Eventos:** `ezChange`

**Métodos:** `setFocus()`, `setBlur()`, `isInvalid()`

**Atalhos:** Ctrl+P (preview), Ctrl+B (negrito), Ctrl+I (itálico), Ctrl+U (sublinhado), Ctrl+K (link)

---

## ez-scrim

**Tag:** Classe CSS (`ez-scrim`, `ez-scrim-light`, `ez-scrim-medium`)

Utilitário CSS para efeito overlay de fundo.

- `ez-scrim-light` — opacidade 10%
- `ez-scrim-medium` — opacidade 40% + blur de 4px

```html
<div class="ez-scrim ez-scrim-medium"></div>
```

---

## ez-scroller

**Tag:** `<ez-scroller>`

Scrollbar para navegação horizontal, vertical ou ambos dentro de um espaço definido.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `activeShadow` | `active-shadow` | `boolean` | `false` | Efeito sombra |
| `direction` | `direction` | `"both"\|"horizontal"\|"vertical"` | `undefined` | Direção do scroll |
| `locked` | `locked` | `boolean` | `false` | Bloqueia scroll |

---

## ez-search

**Tag:** `<ez-search>`

Input de busca por palavra-chave com opções filtráveis, modo slim e validação.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `isTextSearch` | `is-text-search` | `boolean` | `false` | Busca por texto |
| `label` | `label` | `string` | `undefined` | Label |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `options` | — | `IOption[]` | `undefined` | Opções `{value, label}` |
| `suppressEmptyOption` | `suppress-empty-option` | `boolean` | `false` | Remove opção vazia |

**Eventos:** `ezChange: CustomEvent<IOption>`, `ezEmptySearch: CustomEvent<string>`

**Métodos:** `clearValue()`, `setFocus()`, `setBlur()`, `isInvalid()`

---

## ez-search-plus

**Tag:** `<ez-search-plus>`

Busca por código e descrição com carregamento dinâmico de opções via `optionLoader`.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `value` | `string\|IOption` | `undefined` | Valor atual |
| `enabled` | `boolean` | `true` | Habilitado |
| `label` | `string` | `""` | Label |
| `codeLabel` | `string` | `"Cód."` | Label do código |
| `errorMessage` | `string` | `""` | Mensagem de erro |
| `optionLoader` | `OptionLoaderFunction` | `undefined` | Função para carregar opções dinamicamente |
| `mode` | `"regular"\|"slim"` | `"regular"` | Modo de exibição |
| `autoFocus` | `boolean` | `false` | Foco automático |

**Eventos:** `ezChange: CustomEvent<IOption>`, `ezEmptySearch`

**Métodos:** `setFocus()`, `setBlur()`, `isInvalid()`, `getValueAsync()`, `clearValue()`

---

## ez-sidebar-button

**Tag:** `<ez-sidebar-button>`

Botão para expandir menus laterais colapsados.

**Eventos:** `ezClick: CustomEvent<void>`

```html
<ez-sidebar-button></ez-sidebar-button>
```

---

## ez-sidebar-navigator

**Tag:** `<ez-sidebar-navigator>`

Navegação lateral com três modos: flutuante, fixo ou dinâmico.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `type` | `"float"\|"fixed"\|"dynamic"` | `"dynamic"` | Comportamento do menu |
| `mode` | `"float"\|"fixed"` | `"float"` | Estado inicial |
| `size` | `"small"\|"medium"\|"large"` | `"small"` | Largura: 240/280/320px |
| `isResponsive` | `boolean` | `false` | Ajuste automático por tela |
| `titleMenu` | `string` | `""` | Título do menu |
| `showCollapseMenu` | `boolean` | `true` | Botão de colapso |
| `showFixedButton` | `boolean` | `true` | Botão de fixar |

**Eventos:** `ezChangeMode: CustomEvent<ModeMenuEnum>`

**Métodos:** `openSidebar()`, `closeSidebar()`, `changeModeMenu()`

**Slots:** `start`, `content`, `end`, `footer`

---

## ez-skeleton

**Tag:** `<ez-skeleton>`

Placeholder de carregamento que simula o layout do conteúdo enquanto os dados são buscados.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `variant` | `string` | `"text"` | Forma: `text`, `rect`, `circle` |
| `animation` | `string` | `"progress"` | Animação: `progress`, `pulse`, `false` |
| `width` | CSS value | — | Largura |
| `height` | CSS value | — | Altura |
| `count` | `number` | `1` | Quantidade de itens |
| `template` | `HTMLElement\|string` | — | Template HTML customizado |

```html
<ez-skeleton variant="rect" width="200px" height="100px"></ez-skeleton>
```

---

## ez-sortable-list

**Tag:** `<ez-sortable-list>`

Lista ordenável com drag-and-drop, seleção múltipla e personalização de itens.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `dataSource` | — | `ListItem[]` | `[]` | Itens da lista |
| `emptyMessage` | `empty-message` | `string` | `undefined` | Mensagem de lista vazia |
| `enableMultipleSelection` | `enable-multiple-selection` | `boolean` | `false` | Seleção múltipla (Ctrl/Shift) |
| `entityLabel` | `entity-label` | `string` | `undefined` | Nome da entidade |
| `hideHeader` | `hide-header` | `boolean` | `false` | Oculta cabeçalho |
| `hoverFeedback` | `hover-feedback` | `boolean` | `true` | Feedback visual no hover |
| `title` | `title` | `string` | `undefined` | Título da lista |

**Eventos:** `ezChoose`, `ezDoubleClick`, `ezSelectItens`, `itemsReordered`

**Métodos:** `clearSelection()`

---

## ez-spinner

**Tag:** `<ez-spinner>`

Indicador visual de carregamento/processamento em andamento.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `size` | `size` | `"small"\|"medium"\|"large"` | `"small"` | Tamanho (small=contextos compactos, large=tela cheia) |

```html
<ez-spinner size="medium"></ez-spinner>
```

---

## ez-split-button

**Tag:** `<ez-split-button>`

Botão com ação principal e dropdown de ações secundárias.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `label` | `string` | `undefined` | Texto do botão |
| `variant` | `"primary"\|"secondary"\|"tertiary"` | `undefined` | Variante visual |
| `size` | `"small"\|"medium"\|"large"` | `"medium"` | Tamanho |
| `mode` | `"default"\|"icon-left"\|"icon-only"` | `"default"` | Modo de exibição |
| `isDisabled` | `boolean\|"full"` | `false` | Estado desabilitado |
| `items` | `IDropdownItem[]` | `undefined` | Itens do dropdown |

**Eventos:** `buttonClick`, `dropdownItemClick`, `dropdownSubActionClick`

**Métodos:** `setLeftButtonFocus()`, `setRightButtonFocus()`, `setBlur()`, `toggleDropdown()`, `isOpenedDropdown()`

---

## ez-split-panel

**Tags:** `<ez-split-panel>` (container) + `<ez-split-item>` (seção)

Painel redimensionável com múltiplas divisões independentes.

**Propriedades ez-split-panel:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `direction` | `direction` | `"column"\|"row"` | `"column"` | Direção das divisões |
| `anchorToExpand` | `anchor-to-expand` | `boolean` | `false` | Limita tamanho do item expandido |

**Eventos:** `resizeEnd: CustomEvent<IPanelSizeInfo>`

**Métodos:** `rebuildLayout()`

**Propriedades ez-split-item:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `enableExpand` | `enable-expand` | `boolean` | `true` | Habilita expansão |
| `label` | `label` | `string` | `undefined` | Título da seção |
| `size` | `size` | `string` | `undefined` | Tamanho inicial em `fr` ou `%` |

```html
<ez-split-panel direction="row">
  <ez-split-item label="Painel 1" size="1fr">...</ez-split-item>
  <ez-split-item label="Painel 2" size="2fr">...</ez-split-item>
</ez-split-panel>
```

---

## ez-tabselector

**Tag:** `<ez-tabselector>`

Seletor de abas para navegação entre seções distintas.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `selectedIndex` | `selected-index` | `number` | `undefined` | Aba selecionada por índice |
| `selectedTab` | `selected-tab` | `string` | `undefined` | Aba selecionada por nome |
| `tabs` | `tabs` | `Tab[]\|string` | `undefined` | Definição das abas |

**Eventos:** `ezChange: CustomEvent<Tab>`

**Métodos:** `goToTab(tabIndex: number, silent?: boolean)`

---

## ez-tag

**Tag:** `<ez-tag>`

Label para identificação rápida de status ou classificação.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `color` | `color` | `string` | `"ocean-green"` | Cor de fundo (paleta do DS) |
| `customBackgroundColor` | `custom-background-color` | `string` | `undefined` | Cor customizada de fundo |
| `customLabelColor` | `custom-label-color` | `string` | `undefined` | Cor customizada do texto |
| `label` | `label` | `string` | `undefined` | Texto/número |

```html
<ez-tag color="ocean-green" label="Ativo"></ez-tag>
```

---

## ez-tag-input

**Tag:** `<ez-tag-input>`

Input interativo para inserção e gerenciamento de múltiplas tags.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `allowDuplicates` | `allow-duplicates` | `boolean` | `false` | Permite tags duplicadas |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `label` | `label` | `string` | `""` | Label |
| `maxTagLength` | `max-tag-length` | `number` | `undefined` | Máx. de caracteres por tag |
| `maxTags` | `max-tags` | `number` | `undefined` | Máx. de tags |
| `placeholder` | `placeholder` | `string` | `""` | Placeholder |
| `readonly` | `readonly` | `boolean` | `false` | Somente leitura |
| `state` | `state` | `"default"\|"error"\|"success"\|"warning"` | `"default"` | Estado visual |
| `tags` | — | `string[]` | `[]` | Tags iniciais |
| `validator` | — | `Function` | `undefined` | Validação customizada |

**Eventos:** `ezChange`, `ezTagAdded`, `ezTagRemoved`, `ezFocus`, `ezBlur`, `ezType`, `ezValidationError`

**Métodos:** `addTag(tag)`, `removeTag(tag)`, `clearTags()`, `setFocus()`, `setBlur()`

---

## ez-text-area

**Tag:** `<ez-text-area>`

Textarea multilinha para entradas de texto mais longas.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `autoRows` | `auto-rows` | `boolean` | `false` | Linhas ajustadas pela altura máxima |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enableResize` | `enable-resize` | `boolean` | `true` | Habilita redimensionamento |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `label` | `label` | `string` | `undefined` | Label |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `rows` | `rows` | `number` | `4` | Linhas visíveis |
| `value` | `value` | `string` | `undefined` | Valor |

**Eventos:** `ezChange: CustomEvent<string>`

**Métodos:** `setFocus()`, `setBlur()`, `isInvalid()`, `appendTextToSelection(text)`

---

## ez-text-edit

**Tag:** `<ez-text-edit>`

Input de linha única para edição de texto com confirmação ou cancelamento.

**Propriedades:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `styled` | `IStyled` | Atributos de estilo |
| `value` | `string` | Valor do campo |

**Eventos:** `saveEdition`, `cancelEdition`

**Métodos:** `applyFocusSelect()`

---

## ez-text-input

**Tag:** `<ez-text-input>`

Input de texto de linha única fundamental com máscaras, modos e validação.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `label` | `label` | `string` | `undefined` | Label |
| `mask` | `mask` | `string` | `undefined` | Máscara |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `noBorder` | `no-border` | `boolean` | `false` | Remove bordas |
| `password` | `password` | `boolean` | `false` | Modo senha |
| `restrict` | `restrict` | `string` | `undefined` | Restringe caracteres |
| `value` | `value` | `string` | `undefined` | Valor |

**Eventos:** `ezChange: CustomEvent<string>`

**Métodos:** `setFocus()`, `setBlur()`, `isInvalid()`

---

## ez-tile

**Tag:** `<ez-tile>`

Componente versátil para botão grande, item de menu ou elemento de navegação destacado.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `color` | `color` | `"default"\|"gray"\|"green"\|"red"\|"yellow"` | `"default"` | Cor tema |
| `height` | `height` | `number` | `undefined` | Altura customizada |
| `iconName` | `icon-name` | `string` | `"home"` | Ícone |
| `isInteractive` | `is-interactive` | `boolean` | `false` | Habilita clique e hover |
| `size` | `size` | `"small"\|"medium"` | `"small"` | Tamanho: small(120x80px), medium(120x170px) |
| `text` | `text` | `string` | `undefined` | Texto |
| `width` | `width` | `number` | `undefined` | Largura customizada |

**Eventos:** `tileClick: CustomEvent<void>`

**Métodos:** `setFocus()`, `setBlur()`

---

## ez-tile-medium

**Tag:** `<ez-tile-medium>`

Tile para exibição somente leitura ou com botão de ação, com tags de status, título e descrição.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `avatarProps` | `object` | `undefined` | Configura avatar (name, imageSrc, shape) |
| `buttonProps` | `object` | `undefined` | Configura botão de ação |
| `color` | `"default"\|"gray"\|"green"\|"red"\|"yellow"` | `"default"` | Cor tema |
| `descriptionText` | `string` | `undefined` | Texto de descrição |
| `height` | `string` | `undefined` | Altura (padrão 257px) |
| `width` | `string` | `undefined` | Largura (padrão 446px) |
| `iconName` | `string` | `undefined` | Ícone |
| `tags` | `{label: string; color?: string}[]` | `undefined` | Até 3 tags de status |
| `titleText` | `string` | `undefined` | Título principal |

**Métodos:** `setButtonFocus()`, `setButtonBlur()`

---

## ez-time-input

**Tag:** `<ez-time-input>`

Input para seleção de horário com suporte a segundos e validação.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `label` | `label` | `string` | `undefined` | Label |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `showSeconds` | `show-seconds` | `boolean` | `false` | Exibe segundos |
| `value` | `value` | `number` | `undefined` | Valor |

**Eventos:** `ezChange: CustomEvent<number>`, `ezStartChange`, `ezCancelWaitingChange`

**Métodos:** `setFocus()`, `setBlur()`, `isInvalid()`

---

## ez-toast

**Tag:** `<ez-toast>`

Notificação não-modal que exibe brevemente uma mensagem e desaparece automaticamente.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `canClose` | `can-close` | `boolean` | `true` | Permite fechamento manual |
| `fadeTime` | `fade-time` | `number` | `5000` | Duração em milissegundos |
| `message` | `message` | `string` | `undefined` | Texto da mensagem |
| `useIcon` | `use-icon` | `boolean` | `false` | Habilita slot de ícone |

**Métodos:** `show(message, fadeTime, useIcon, canClose?): Promise<void>`

```javascript
const toast = document.querySelector('ez-toast');
toast.show('Operação concluída!', 4000, false);
```

---

## ez-tooltip

**Tag:** `<ez-tooltip>`

Componente flutuante que exibe texto ao passar o mouse sobre um elemento.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `active` | `active` | `boolean` | `true` | Ativa/desativa tooltip |
| `debouncingTime` | `debouncing-time` | `number` | `500` | Delay em ms |
| `maxWidth` | `max-width` | `number` | `200` | Largura máxima em px |
| `message` | `message` | `string` | `undefined` | Texto a exibir |
| `placement` | `placement` | `string` | `"bottom"` | Posição: top/bottom/left/right |
| `strategy` | `strategy` | `"absolute"\|"fixed"` | `"absolute"` | Estratégia de posicionamento |
| `type` | `type` | `string` | `"default"` | Variante: default/success/warning/error |

---

## ez-tree

**Tag:** `<ez-tree>`

Exibição hierárquica de dados com expansão, colapso e navegação em estruturas aninhadas.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `items` | — | `ITreeItem[]` | `[]` | Itens da árvore |
| `value` | — | `ITreeItem` | `undefined` | Item selecionado |
| `selectedId` | `selected-id` | `string` | `undefined` | ID do item selecionado |
| `selectable` | `selectable` | `boolean` | `true` | Permite seleção |
| `enableHierarchicalFilter` | `enable-hierarchical-filter` | `boolean` | `true` | Filtro hierárquico |

**Eventos:** `ezChange`, `ezOpenItem`, `ezDbClickItem`, `ezRemoveItem`

**Métodos:** `applyFilter(pattern)`, `addChild(item, parentId?)`, `selectItem(id)`, `openItem(id)`, `expandAll()`, `collapseAll()`, `enableItem(id)`, `disableItem(id)`, `updateItem(item)`, `removeItem(id?)`, `getCurrentPath()`

---

## ez-underface

**Tag:** `<ez-underface>`

Componente base de fundo para outros conteúdos, com cores e dimensões configuráveis. Dimensões padrão: 693x247px.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `color` | `color` | `"dark-petroleum"\|"default"\|"green"\|"light-gray"\|"light-green"\|"ocean-green"` | `"default"` | Cor de fundo |
| `customColor` | `custom-color` | `string` | `undefined` | Cor customizada (sobrepõe `color`) |
| `height` | `height` | `number` | `undefined` | Altura |
| `width` | `width` | `number` | `undefined` | Largura |

---

## ez-upload

**Tag:** `<ez-upload>`

Seleção e upload de arquivos (imagens, vídeos, documentos) com suporte a limites e endpoints HTTP.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `label` | `label` | `string` | `undefined` | Label |
| `maxFileSize` | `max-file-size` | `number` | `undefined` | Tamanho máximo em bytes |
| `maxFiles` | `max-files` | `number` | `undefined` | Quantidade máxima de arquivos |
| `requestHeaders` | `request-headers` | `any` | `undefined` | Cabeçalhos HTTP |
| `subtitle` | `subtitle` | `string` | `undefined` | Subtítulo do campo |
| `urlDelete` | `url-delete` | `string` | `undefined` | Endpoint de exclusão |
| `urlUpload` | `url-upload` | `string` | `undefined` | Endpoint de upload |
| `value` | — | `EzFile[]` | `undefined` | Valor atual |

**Eventos:** `ezChange: CustomEvent<EzFile[]>`, `ezStartChange`, `ezCancelWaitingChange`

**Métodos:** `setFocus()`, `setBlur()`, `addFiles(files: File[])`

```html
<ez-upload label="Arquivos" url-upload="/api/upload" max-files="5"></ez-upload>
```
