# Design System — Componentes ez-

Componentes genéricos do Sankhya Design System (prefixo `ez-`). Fonte: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/

---

## ez-actions-button

**Tag:** `<ez-actions-button>`

Botão que exibe uma lista de ações em menu popover, suportando diversos tamanhos, estados e opções de customização.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `actions` | — | `IAction[]` | `undefined` | Lista de ações `{value: string, label: string}` |
| `arrowActive` | `arrow-active` | `boolean` | `false` | Exibe seta de ordenação |
| `checkOption` | `check-option` | `boolean` | `false` | Exibe ícone de check para item selecionado |
| `displayIcon` | `display-icon` | `string` | `undefined` | Ícone do componente |
| `enabled` | `enabled` | `boolean` | `true` | Habilita interação |
| `isTransparent` | `is-transparent` | `boolean` | `false` | Fundo transparente |
| `showLabel` | `show-label` | `boolean` | `false` | Exibe label do item selecionado |
| `size` | `size` | `"small"\|"medium"\|"large"` | `"medium"` | Tamanho do botão |
| `value` | `value` | `string` | `undefined` | Valor do componente |

**Eventos:** `ezAction` (ação selecionada), `ezPopoverOpen` (lista exibida), `ezDisconnectedActionButtons` (desconexão do DOM)

**Métodos:** `hideActions()`, `showActions()`, `isOpened(): Promise<boolean>`

```html
<ez-actions-button size="medium" display-icon="ellipsis"></ez-actions-button>
<script>
  const btn = document.querySelector('ez-actions-button');
  btn.actions = [{ value: 'edit', label: 'Editar' }];
  btn.addEventListener('ezAction', (e) => console.log(e.detail));
</script>
```

---

## ez-alert

**Tag:** `<ez-alert>`

Componente de feedback para exibir mensagens contextuais de alerta, erro ou sucesso.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `alertType` | `alert-type` | `"critical"\|"success"\|"warn"` | `"success"` | Tipo visual do alerta |

```html
<ez-alert alert-type="warn">Mensagem de aviso</ez-alert>
```

---

## ez-alert-list

**Tag:** `<ez-alert-list>`

Lista de alertas em formato popup, sem bloquear a usabilidade do conteúdo subjacente.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `alerts` | — | `AlertItem[]` | `[]` | Lista de alertas |
| `enableDragAndDrop` | `enable-drag-and-drop` | `boolean` | `undefined` | Habilita arrastar o componente |
| `enableExpand` | `enable-expand` | `boolean` | `true` | Habilita expansão |
| `expanded` | `expanded` | `boolean` | `false` | Estado expandido |
| `opened` | `opened` | `boolean` | `true` | Estado aberto |

---

## ez-avatar

**Tag:** `<ez-avatar>`

Representa visualmente um usuário exibindo imagem, inicial do nome ou ícone (prioridade: imagem > inicial > ícone padrão).

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `iconName` | `icon-name` | `string` | `undefined` | Ícone do avatar |
| `imageSrc` | `image-src` | `string` | `undefined` | URL da imagem |
| `isInteractive` | `is-interactive` | `boolean` | `false` | Estado interativo com hover |
| `name` | `name` | `string` | `undefined` | Nome do usuário (exibe inicial) |
| `shape` | `shape` | `"circle"\|"square"` | `"circle"` | Formato |
| `size` | `size` | `string` | `"100"` | Tamanho em pixels (60–320) |

```html
<ez-avatar image-src="user.jpg" size="100"></ez-avatar>
<ez-avatar name="João Silva" size="80"></ez-avatar>
```

---

## ez-badge

**Tag:** `<ez-badge>`

Elemento tipo label para reconhecimento rápido de um status temporário.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `alignItems` | `align-items` | `"center"\|"flex-end"\|"flex-start"` | `"center"` | Posição do ícone |
| `iconLeft` | `icon-left` | `string` | `undefined` | Ícone à esquerda |
| `iconRight` | `icon-right` | `string` | `undefined` | Ícone à direita |
| `label` | `label` | `string` | `undefined` | Texto/número do badge |
| `size` | `size` | `"extra-large"\|"large"\|"medium"\|"small-medium"\|"small"\|"extra-small"` | `"small"` | Tamanho |

---

## ez-breadcrumb

**Tag:** `<ez-breadcrumb>`

Apresenta sequência de links hierárquicos para navegação e localização do usuário.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `fillMode` | `fill-mode` | `"auto"\|"regular"` | `"auto"` | Modo de apresentação |
| `items` | — | `IBreadcrumbItem[]` | `[]` | Itens do breadcrumb |
| `maxItems` | `max-items` | `number` | `4` | Máximo de itens |
| `positionEllipsis` | `position-ellipsis` | `number` | `1` | Posição da elipse |

**Eventos:** `selectedItem: CustomEvent<IBreadcrumbItem>`

---

## ez-button

**Tag:** `<ez-button>`

Botão para inicializar ações e interações do usuário.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `iconName` | `icon-name` | `string` | `undefined` | Ícone da biblioteca |
| `isDisabled` | `is-disabled` | `""\|"full"\|boolean` | `false` | Desabilitado (true=acessível, full=nativo) |
| `label` | `label` | `string` | `undefined` | Texto do botão |
| `leftIconName` | `left-icon-name` | `string` | `undefined` | Ícone à esquerda |
| `rightIconName` | `right-icon-name` | `string` | `undefined` | Ícone à direita |
| `mode` | `mode` | `"icon"\|"label-icon"\|"link"\|"regular"` | `"regular"` | Modo de exibição |
| `size` | `size` | `"large"\|"medium"\|"small"\|"x-small"` | `"medium"` | Tamanho |
| `type` | `type` | `string` | `"button"` | Tipo HTML |
| `variant` | `variant` | `"primary"\|"secondary"\|"tertiary"` | `undefined` | Variante visual |

**Métodos:** `setFocus()`, `setBlur()`

```html
<ez-button variant="primary" label="Salvar"></ez-button>
<ez-button mode="icon" icon-name="check"></ez-button>
```

---

## ez-calendar

**Tag:** `<ez-calendar>`

Componente de calendário para seleção de data, com suporte opcional a horário.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `floating` | `floating` | `boolean` | `false` | Controle por show()/hide() |
| `showSeconds` | `show-seconds` | `boolean` | `false` | Exibe segundos |
| `time` | `time` | `boolean` | `false` | Habilita horas e minutos |
| `value` | — | `Date` | `new Date()` | Data selecionada |

**Eventos:** `ezChange: CustomEvent<Date>`

**Métodos:** `show(top?, left?, bottom?, right?)`, `hide()`, `fitVertical(topOffset, bottomOffset)`, `fitHorizontal(rightOffset)`

---

## ez-card-item

**Tag:** `<ez-card-item>`

Exibe itens em formato de card com título, chave e detalhes.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `compacted` | `compacted` | `boolean` | `false` | Modo compacto |
| `enableKey` | `enable-key` | `boolean` | `true` | Visibilidade da chave |
| `item` | — | `CardItem` | `undefined` | Objeto `{title, key, details}` |

**Eventos:** `ezClick: CustomEvent<CardItem>`

---

## ez-chart

**Tag:** `<ez-chart>`

Renderiza gráficos com base em séries de dados fornecidas.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `width` | `number` | — | Largura em pixels |
| `height` | `number` | — | Altura em pixels |
| `chartTitle` | `string` | — | Título principal |
| `chartSubTitle` | `string` | — | Subtítulo |
| `legendEnabled` | `boolean` | `true` | Visibilidade da legenda |
| `type` | `string` | `"line"` | Tipo: `column`, `bar`, `line`, `pie`, `donut` |
| `series` | `ChartSerie\|ChartSerie[]` | — | Séries de dados |
| `xAxis` | `ChartAxis\|ChartAxis[]` | — | Configuração eixo X |
| `yAxis` | `ChartAxis\|ChartAxis[]` | — | Configuração eixo Y |

**Eventos:** `onEzSerieClick`

---

## ez-check

**Tag:** `<ez-check>`

Checkbox para seleção de uma ou mais opções, com modo regular e switch (toggle).

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `compact` | `compact` | `boolean` | `false` | Modo compacto |
| `enabled` | `enabled` | `boolean` | `true` | Habilita interação |
| `indeterminate` | `indeterminate` | `boolean` | `undefined` | Estado indeterminado |
| `label` | `label` | `string` | `undefined` | Título do campo |
| `mode` | `mode` | `"regular"\|"switch"` | `"regular"` | Modo de visualização |
| `value` | `value` | `boolean` | `undefined` | Valor do campo |

**Eventos:** `ezChange: CustomEvent<any>`

**Métodos:** `getMode()`, `setFocus()`

---

## ez-chip

**Tag:** `<ez-chip>`

Chip versátil que funciona como label selecionável ou botão de ação.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `label` | `label` | `string` | `undefined` | Texto |
| `value` | `value` | `boolean` | `false` | Estado selecionado |
| `type` | `type` | `"primary"\|"secondary"\|"error"\|"error-light"\|"success"\|"success-light"\|"warning"\|"warning-light"` | `"primary"` | Variante |
| `size` | `size` | `"default"\|"medium"\|"large"` | `"default"` | Altura: 32/42/50px |
| `mode` | `mode` | `"label"\|"action"` | `undefined` | Modo de comportamento |
| `enabled` | `enabled` | `boolean` | `true` | Habilita interação |
| `iconNameLeft` | `icon-name-left` | `string` | `undefined` | Ícone esquerdo |
| `iconNameRight` | `icon-name-right` | `string` | `undefined` | Ícone direito |
| `removePosition` | `remove-position` | `"left"\|"right"` | `undefined` | Botão de remoção |

**Eventos:** `valueChange`, `removeChip`, `actionClick`, `iconClick`

**Métodos:** `setFocus()`, `setBlur()`

---

## ez-classic-combo-box

**Tag:** `<ez-classic-combo-box>`

Seleção de opções com dropdown, busca, estados visuais e slots customizáveis.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `label` | `label` | `string` | `undefined` | Label |
| `options` | — | `IOption[]` | `undefined` | Array `{value, label}` |
| `placeholder` | `placeholder` | `string` | `undefined` | Placeholder |
| `readonly` | `readonly` | `boolean` | `false` | Somente leitura |
| `state` | `state` | `"default"\|"error"\|"success"\|"warning"` | `"default"` | Estado visual |
| `suppressSearch` | `suppress-search` | `boolean` | `false` | Desabilita digitação |
| `value` | — | `IOption` | `null` | Valor selecionado |

**Eventos:** `ezBlur`, `ezChange: CustomEvent<IOption>`, `ezType`, `ezVisibilityChange`, `iconClick`

**Métodos:** `setFocus()`, `setBlur()`, `showPopover()`, `hidePopover()`, `setValue(option)`

---

## ez-classic-input

**Tag:** `<ez-classic-input>`

Input de texto versátil com ícones, máscaras e estados visuais.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `enabled` | `boolean` | `true` | Habilitado |
| `label` | `string` | `undefined` | Label |
| `leftIconName` | `string` | `undefined` | Ícone esquerdo |
| `mask` | `string` | `undefined` | Máscara de formatação |
| `placeholder` | `string` | `undefined` | Placeholder |
| `readonly` | `boolean` | `false` | Somente leitura |
| `rightIconName` | `string` | `undefined` | Ícone direito |
| `state` | `"default"\|"error"\|"success"\|"warning"` | `"default"` | Estado visual |
| `type` | `string` | `"text"` | Tipo do input |
| `value` | `string` | `undefined` | Valor |

**Eventos:** `ezChange`, `ezBlur`, `ezFocus`, `iconClick`

**Métodos:** `setFocus()`, `setBlur()`

---

## ez-classic-text-area

**Tag:** `<ez-classic-text-area>`

Textarea multilinha com ícones, redimensionamento automático e estados visuais.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `enabled` | `boolean` | `true` | Habilitado |
| `label` | `string` | `""` | Label |
| `maxlength` | `number` | `undefined` | Limite de caracteres |
| `placeholder` | `string` | `""` | Placeholder |
| `readonly` | `boolean` | `false` | Somente leitura |
| `resize` | `string` | `"vertical"` | Redimensionamento: vertical/horizontal/both/none |
| `rows` | `number` | `5` | Linhas |
| `state` | `string` | `"default"` | Estado visual |
| `value` | `string` | `""` | Valor |

**Eventos:** `ezChange`, `ezBlur`, `iconClick`

**Métodos:** `setFocus()`, `setBlur()`

---

## ez-collapsible-box

**Tag:** `<ez-collapsible-box>`

Container colapsável com cabeçalho customizável, opções de edição e remoção.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `boxBordered` | `box-bordered` | `boolean` | `false` | Exibe borda |
| `editable` | `editable` | `boolean` | `false` | Ícone de edição |
| `headerAlign` | `header-align` | `"center"\|"left"\|"right"\|"stretch"` | `"left"` | Alinhamento do header |
| `headerSize` | `header-size` | `"x-small"\|"small"\|"medium"\|"large"\|"x-large"` | `"small"` | Tamanho do header |
| `iconPlacement` | `icon-placement` | `"left"\|"right"` | `"left"` | Posição do ícone |
| `label` | `label` | `string` | `undefined` | Título |
| `removable` | `removable` | `boolean` | `false` | Ícone de remoção |
| `subtitle` | `subtitle` | `string` | `undefined` | Subtítulo |
| `value` | `value` | `boolean` | `false` | Estado expandido/colapsado |

**Eventos:** `ezChange`, `ezEditLabelMode`, `ezRemove`, `ezSaveEditLabel`

**Métodos:** `showHide()`, `applyFocusTextEdit()`, `cancelEdition()`

---

## ez-combo-box

**Tag:** `<ez-combo-box>`

Menu suspenso com lista filtrável de opções para seleção de valores.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `value` | `IOption\|string` | `undefined` | Valor do campo |
| `label` | `string` | `undefined` | Título |
| `options` | `IOption[]` | `undefined` | Array `{value, label}` |
| `enabled` | `boolean` | `true` | Habilitado |
| `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho do campo |
| `isTextSearch` | `boolean` | `false` | Busca por texto |
| `suppressSearch` | `boolean` | `false` | Desabilita digitação |
| `errorMessage` | `string` | `undefined` | Mensagem de erro |

**Eventos:** `ezChange: CustomEvent<IOption>`, `ezVisibilityChange`

**Métodos:** `setFocus()`, `setBlur()`, `clearValue()`, `getValueAsync()`, `isInvalid()`

---

## ez-date-input

**Tag:** `<ez-date-input>`

Popup de seleção de data com suporte a intervalos.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `label` | `label` | `string` | `undefined` | Label |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `value` | — | `Date` | `undefined` | Valor |

**Eventos:** `ezChange: CustomEvent<Date>`, `ezInput`, `ezStartChange`, `ezCancelWaitingChange`

**Métodos:** `getValueAsync()`, `isInvalid()`, `setFocus()`, `setBlur()`

---

## ez-date-time-input

**Tag:** `<ez-date-time-input>`

Input de data e hora com suporte a validação e exibição de segundos.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `autoFocus` | `boolean` | `false` | Foco automático |
| `canShowError` | `boolean` | `true` | Exibe erro |
| `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `string` | `undefined` | Mensagem de erro |
| `label` | `string` | `undefined` | Label |
| `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `showSeconds` | `boolean` | `false` | Exibe segundos |
| `value` | `Date` | `undefined` | Valor |

**Eventos:** `ezChange: CustomEvent<Date>`, `ezStartChange`, `ezCancelWaitingChange`

**Métodos:** `setFocus()`, `setBlur()`, `isInvalid()`, `getValueAsync()`

---

## ez-dialog

**Tag:** `<ez-dialog>`

Janela pop-up para apresentar informações que requerem atenção imediata do usuário.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `confirm` | `confirm` | `boolean` | `false` | Modo confirmação |
| `dialogType` | `dialog-type` | `"critical"\|"default"\|"success"\|"warn"` | `undefined` | Tipo visual |
| `ezTitle` | `ez-title` | `string` | `undefined` | Título |
| `message` | `message` | `string` | `undefined` | Mensagem |
| `opened` | `opened` | `boolean` | `false` | Visibilidade |

**Eventos:** `ezAccept: CustomEvent<boolean>`, `ezCancel: CustomEvent<boolean>`

**Métodos:** `show(title, message, dialogType, confirm, icon, labelCancel, labelConfirm, btnConfirmDanger, beforeClose): Promise<boolean>`

---

## ez-double-list

**Tag:** `<ez-double-list>`

Transferência de itens entre duas listas (esquerda/direita) em ambas direções.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `leftList` | `ListItem[]` | `[]` | Lista de origem |
| `leftListLabel` | `string` | `"disponíveis"` | Label da lista esquerda |
| `leftTitle` | `string` | `undefined` | Título da lista esquerda |
| `rightList` | `ListItem[]` | `[]` | Lista de destino |
| `rightListLabel` | `string` | `"selecionados"` | Label da lista direita |
| `rightTitle` | `string` | `undefined` | Título da lista direita |
| `entityLabel` | `string` | `"item"` | Nome da entidade |
| `useOnlyRightList` | `boolean` | `false` | Exibe apenas lista direita |

**Eventos:** `ezLeftListChanged: CustomEvent<ListItem[]>`, `ezRightListChanged: CustomEvent<ListItem[]>`

**Métodos:** `resetSelectedLists()`

---

## ez-dropdown

**Tag:** `<ez-dropdown>`

Menu dropdown com gerenciamento de visibilidade, submenus e personalização de itens.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `items` | `IDropdownItem[]` | `[]` | Itens do dropdown |
| `value` | `IDropdownItem` | `undefined` | Último item clicado |
| `itemBuilder` | `Function` | `undefined` | Renderização customizada de itens |

**Eventos:** `ezClick: CustomEvent<IDropdownItem>`, `ezSubActionClick`, `ezHover`, `ezOutsideClick`

---

## ez-empty-card

**Tag:** `<ez-empty-card>`

Container base para outros conteúdos, com dimensões e cores configuráveis.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `color` | `color` | `"default"\|"gray"\|"green"\|"petroleum"\|"red"\|"yellow"` | `"default"` | Cor tema |
| `width` | `width` | `number` | `undefined` | Largura (padrão 335px) |
| `height` | `height` | `number` | `undefined` | Altura (padrão 155px) |

---

## ez-file-item

**Tag:** `<ez-file-item>`

Representa um arquivo com progresso de upload, opções de download/remoção e metadados.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `canRemove` | `can-remove` | `boolean` | `true` | Permite remoção |
| `fileName` | `file-name` | `string` | `undefined` | Nome do arquivo |
| `fileSize` | `file-size` | `number` | `undefined` | Tamanho em bytes |
| `iconName` | `icon-name` | `string` | `undefined` | Ícone representativo |
| `progress` | `progress` | `number` | `100` | Progresso de upload (%) |

**Eventos:** `ezClick: CustomEvent<string>`, `ezRemove: CustomEvent<string>`

---

## ez-filter-input

**Tag:** `<ez-filter-input>`

Input de texto para filtragem com suporte a busca síncrona e assíncrona.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `asyncSearch` | `async-search` | `boolean` | `false` | Busca assíncrona |
| `autoFocus` | `auto-focus` | `boolean` | `false` | Foco automático |
| `canShowError` | `can-show-error` | `boolean` | `true` | Exibe erro |
| `enabled` | `enabled` | `boolean` | `true` | Habilitado |
| `errorMessage` | `error-message` | `string` | `undefined` | Mensagem de erro |
| `label` | `label` | `string` | `undefined` | Label |
| `mode` | `mode` | `"regular"\|"slim"` | `"regular"` | Tamanho |
| `restrict` | `restrict` | `string` | `undefined` | Restringe caracteres digitados |
| `value` | `value` | `string` | `undefined` | Valor inicial |

**Eventos:** `ezChange`, `ezFocusIn`, `ezSearching`

**Métodos:** `setFocus()`, `setBlur()`, `setValue(newValue)`, `isInvalid()`, `endSearch()`

---

## ez-form

**Tag:** `<ez-form>`

Formulário para gerenciamento de entrada de dados com configuração dinâmica de campos, validação e editores customizados.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `config` | `IFormConfig` | `undefined` | Configuração do formulário |
| `dataUnit` | `DataUnit` | `undefined` | DataUnit para edição de registros |
| `fieldToFocus` | `string` | `undefined` | Campo a receber foco |
| `onlyStaticFields` | `boolean` | `false` | Renderiza apenas campos estáticos |
| `useSearchField` | `boolean` | `true` | Busca por Ctrl+F |

**Eventos:** `ezFormRequestClearFieldToFocus`, `ezFormSetFields`, `ezReady`, `formItemsReady`

**Métodos:** `validate()`, `setFieldProp(fieldName, propName, value)`, `addCustomEditor(fieldName, customEditor)`

---

## ez-form-view

**Tag:** `<ez-form-view>`

Layout responsivo de campos de formulário. Usado internamente pelo ez-form para distribuição visual dos campos.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `fields` | `IFormViewField[]` | `undefined` | Metadados dos campos |
| `selectedRecord` | `Record` | `undefined` | Registro selecionado |
| `singleColumn` | `boolean` | `false` | Força coluna única |

**Eventos:** `ezContentReady`, `formItemsReady`

**Métodos:** `addCustomEditor(fieldName, customEditor)`, `setFieldProp(fieldName, propName, value)`, `showUp()`

---

## ez-grid

**Tag:** `<ez-grid>`

Tabela de dados com edição, paginação, filtros, ordenação e seleção múltipla. Altura mínima: 300px.

**Propriedades principais:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `autoFocus` | `auto-focus` | `boolean` | `true` | Foco ao carregar |
| `canEdit` | `can-edit` | `boolean` | `true` | Edição de células |
| `enableGridInsert` | `enable-grid-insert` | `boolean` | `false` | Inserção no grid |
| `multipleSelection` | `multiple-selection` | `boolean` | `undefined` | Seleção múltipla |
| `suppressFilterColumn` | `suppress-filter-column` | `boolean` | `false` | Oculta filtros de coluna |
| `mode` | `mode` | `"complete"\|"simple"` | `"complete"` | Modo (simple = somente leitura) |
| `useEnterLikeTab` | `use-enter-like-tab` | `boolean` | `false` | Enter age como Tab |

**Eventos:** `ezSelectionChange`, `ezDoubleClick`, `ezColumnStateChange`, `componentReady`, `ezPageChangedChanged`

**Métodos:** `setData(data)`, `getSelection()`, `setColumnsDef(cols)`, `addGridCustomRender(fieldName, render)`, `addCustomEditor(fieldName, editor)`, `setFocus()`, `stopEdit()`

---

## ez-grid-view

**Tag:** `<ez-grid-view>`

Visualização de dados em grid simplificada (somente leitura). Basta informar metadados de colunas e array de registros.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `columnsConfig` | — | `ColumnConfig[]` | `undefined` | Configuração das colunas |
| `metadata` | — | `UnitMetadata` | `undefined` | Estrutura do grid |
| `multipleSelection` | `multiple-selection` | `boolean` | `false` | Seleção múltipla |
| `pageSize` | `page-size` | `number` | `150` | Registros por página |
| `records` | — | `Record[]` | `undefined` | Dados a exibir |
| `suppressFilterColumn` | `suppress-filter-column` | `boolean` | `false` | Oculta filtros |

**Eventos:** `ezSelectionChange`, `ezDoubleClick`, `ezColumnStateChange`

**Métodos:** `refresh()`, `getDataUnit()`, `getSelection()`, `addCustomValueFormatter(col, fn)`, `addGridCustomRender(field, render)`, `quickFilter(term)`, `setFocus()`

---

## ez-guide-navigator

**Tag:** `<ez-guide-navigator>`

Navegação lateral baseada em guias com estrutura hierárquica e carregamento dinâmico de filhos.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `items` | — | `IGuideItem[]` | `[]` | Itens de navegação |
| `open` | `open` | `boolean` | `true` | Menu aberto |
| `selectedId` | `selected-id` | `string` | `undefined` | ID do item selecionado |

**Eventos:** `ezSelectionChange: CustomEvent<IGuideItem>`

**Métodos:** `enableItem(id)`, `disableItem(id)`, `selectGuide(id)`, `getCurrentPath()`, `getItem(id)`, `getParent(id)`, `updateItem(item)`, `openGuideNavidator()`

---

## ez-icon

**Tag:** `<ez-icon>`

Ícones simples e modernos da biblioteca Sankhya Design System.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `fontSize` | `font-size` | `number\|string` | `undefined` | Tamanho via font-size |
| `href` | `href` | `string` | `undefined` | Endereço de imagem externa |
| `iconName` | `icon-name` | `string` | `undefined` | Nome do ícone da biblioteca |
| `size` | `size` | `"x-small"\|"small"\|"medium"\|"large"\|"x-large"` | `"medium"` | Tamanho (14/16/20/24/32px) |

```html
<ez-icon icon-name="home" size="medium"></ez-icon>
```

---

## ez-list

**Tag:** `<ez-list>`

Lista versátil com categorias, check, seleção única/múltipla, drag-and-drop e renderização customizável.

**Propriedades:**

| Propriedade | Atributo | Tipo | Padrão | Descrição |
|-------------|----------|------|--------|-----------|
| `dataSource` | — | `(ListItem\|ListGroup)[]` | `[]` | Dados da lista |
| `enableMultipleSelection` | `enable-multiple-selection` | `boolean` | `false` | Seleção múltipla |
| `ezDraggable` | `ez-draggable` | `boolean` | `false` | Drag-and-drop |
| `ezSelectable` | `ez-selectable` | `boolean` | `false` | Itens selecionáveis |
| `listMode` | `list-mode` | `"check"\|"regular"` | `"regular"` | Modo de apresentação |
| `useGroups` | `use-groups` | `boolean` | `false` | Agrupa itens |

**Eventos:** `ezChange`, `ezCheckChange`, `ezDoubleClick`, `ezSelectItem`, `ezSelectMultipleItems`

**Métodos:** `getList()`, `getSelection()`, `removeSelection()`, `scrollToTop()`, `setSelection(item)`

---

## ez-list-item

**Tag:** `<ez-list-item>`

Item de lista com título, descrição e ícone opcional à direita.

**Propriedades:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `title` | `string` | Título principal |
| `textTitle` | `string` | Texto descritivo complementar |
| `iconName` | `string` | Ícone à direita |

```html
<ez-list-item title="Item" textTitle="Descrição" iconName="arrow-right"></ez-list-item>
```
