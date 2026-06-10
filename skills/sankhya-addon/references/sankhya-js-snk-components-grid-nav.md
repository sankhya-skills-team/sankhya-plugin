# sankhya-js — snk.components (Grid, Navegação, Filtro)

Componentes de grade de dados, navegação de registros, dynaform e filtro.

---

## sk-datagrid

**ID:** `snk.components.datagrid.directive:sk-datagrid`
**Tipo:** directive (cria novo scope)

Grade de dados do framework HTML5.

**Uso:**
```html
<sk-datagrid
    sk-dataset="{SkDataset}"
    sk-config-name="{string}"
    sk-editable="{boolean}"
    sk-allow-multiple-selection="{boolean}"
    sk-on-dbl-click="{function}"
    sk-on-click="{function}"
    sk-focus-to-after-refresh="{function}"
    sk-on-datagrid-loaded="{function}"
    sk-datagrid-interceptor="{function}"
    sk-hide-cbx-column="{boolean}"
    sk-disable-pagination="{boolean}"
    sk-disable-search="{boolean}"
    sk-disable-tour="{boolean}"
    sk-drag-enabled="{boolean}"
    sk-drop-enabled="{boolean}"
    sk-drag-field-presentation="{string}"
    sk-drag-start="{function}"
    sk-drag-enter="{function}"
    sk-drag-over="{function}"
    sk-drop="{function}"
    sk-drag-end="{function}">
</sk-datagrid>
```

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `sk-dataset` | SkDataset | Dataset com os dados |
| `sk-config-name` | string | Nome da configuração de colunas |
| `sk-editable` | boolean | Habilita edição inline |
| `sk-allow-multiple-selection` | boolean | Permite seleção múltipla |
| `sk-on-dbl-click` | function | Duplo clique em linha |
| `sk-on-click` | function | Clique em linha |
| `sk-on-datagrid-loaded` | function | Callback ao carregar o grid |
| `sk-datagrid-interceptor` | function | Interceptor da grade |
| `sk-hide-cbx-column` | boolean | Oculta coluna de checkbox |
| `sk-disable-pagination` | boolean | Desabilita paginação (cuidado: impacto de performance) |
| `sk-disable-search` | boolean | Desabilita busca |
| `sk-drag-enabled` | boolean | Habilita arrastar linha |
| `sk-drop-enabled` | boolean | Habilita soltar linha |

**Métodos da API (via controller):**

| Método | Retorno | Descrição |
|---|---|---|
| `getColumnByName(fieldName)` | object | Metadados da coluna pelo nome |
| `getColumnDefs()` | array | Coleção de colunas (referência) |
| `getOriginalColumnDefs()` | array | Colunas originais do dataset |
| `getVisibleColumnDefs()` | array | Colunas visíveis no momento |
| `getDataset()` | Dataset | Dataset do datagrid |
| `getGridApi()` | object | API do ui-grid |
| `getRecords()` | array | Registros exibidos |
| `getSelectedRecords()` | array | Registros selecionados |
| `setSelectedRecords(Array)` | - | Define seleção programaticamente |
| `selectedAllRecords()` | - | Seleciona todos os registros |
| `unselectAllSelectedRows()` | - | Deseleciona todos |
| `refresh()` | - | Recalcula dimensões (não recarrega dados) |
| `refreshCells()` | - | Atualiza células após mudança programática |
| `isEditable()` | boolean | Informa se a grade é editável |
| `setCompactMode(isCompact, force)` | - | Altera modo compacto/expandido |
| `updateColumnLabels()` | - | Atualiza labels das colunas |
| `getScopeId()` | string | ID do scope do controller |

**Exemplo básico:**
```html
<sk-datagrid sk-dataset="ctrl.dataset"
    sk-editable="false"
    sk-on-dbl-click="ctrl.abrirDetalhe()"
    sk-on-datagrid-loaded="ctrl.onGridLoaded(datagrid)">
</sk-datagrid>
```

**Colunas customizadas:** usar `sk-datagrid-custom-column` (ver módulo snk.form).

---

## sk-navigator

**ID:** `snk.components.navigator.directive:sk-navigator`
**Tipo:** directive (cria novo scope)

Barra de navegação com botões de CRUD e paginação de registros.

```html
<sk-navigator
    dataset="{object}"
    show-crud="{boolean}"
    sk-add-function="{function}"
    sk-show-navigation="{boolean}"
    sk-show-add-button="{boolean}"
    sk-show-copy-button="{boolean}"
    sk-show-remove-button="{boolean}"
    sk-show-refresh-button="{boolean}"
    sk-show-cancel-button="{boolean}"
    sk-show-save-button="{boolean}"
    sk-edit-unique-record="{boolean}"
    sk-save-handler="{function}"
    sk-show-edit-button="{boolean}"
    sk-always-navigation="{boolean}">
</sk-navigator>
```

| Parâmetro | Tipo | Default | Descrição |
|---|---|---|---|
| `dataset` | object | - | Instância do dataset |
| `show-crud` | boolean | true | Exibe botões CRUD |
| `sk-add-function` | function | - | Função ao incluir registro |
| `sk-show-navigation` | boolean | - | Exibe botões de navegação |
| `sk-show-add-button` | boolean | - | Exibe botão Novo |
| `sk-show-copy-button` | boolean | - | Exibe botão Copiar |
| `sk-show-remove-button` | boolean | - | Exibe botão Remover |
| `sk-show-refresh-button` | boolean | - | Exibe botão Refresh |
| `sk-show-cancel-button` | boolean | - | Exibe botão Cancelar |
| `sk-show-save-button` | boolean | - | Exibe botão Salvar |
| `sk-edit-unique-record` | boolean | - | Modo de edição única |
| `sk-save-handler` | function | - | Handler do botão Salvar |
| `sk-show-edit-button` | boolean | - | Exibe botão de edição múltipla |
| `sk-always-navigation` | boolean | - | Navegação sempre visível; salva ao trocar de linha |

---

## sk-dynaform

**ID:** `snk.components.dynaform.directive:sk-dynaform`
**Tipo:** directive (cria novo scope)

Componente completo de manutenção de entidade — integra dataset, grid, form, navigator e filtro automaticamente.

```html
<sk-dynaform
    sk-entity-name="{string}"
    sk-resource-id="{string}"
    sk-on-dynaform-loaded="{function}"
    sk-on-datagrid-loaded="{function}"
    sk-parent-dynaform="{object}"
    sk-show-filter="{boolean}"
    sk-skip-start-page="{boolean}"
    sk-edit-unique-record="{boolean}"
    sk-dynaform-interceptor="{object}"
    sk-datagrid-interceptor="{object}"
    sk-form-interceptor="{object}"
    sk-filter-panel-interceptor="{object}"
    sk-helper-class-name="{string}"
    sk-save-handler="{function}">
</sk-dynaform>
```

**Parâmetros principais:**

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `sk-entity-name` | string | Nome da entidade |
| `sk-resource-id` | string | ID de recurso (permissões) |
| `sk-on-dynaform-loaded` | function | Callback com o dynaform pronto — ideal para configurar campos |
| `sk-on-datagrid-loaded` | function | Callback quando o grid está pronto |
| `sk-parent-dynaform` | object | Dynaform pai para relação master-detail |
| `sk-show-filter` | boolean | Exibe/oculta botão de filtro |
| `sk-skip-start-page` | boolean | Pula a página inicial |
| `sk-edit-unique-record` | boolean | Modo de edição de registro único |
| `sk-dynaform-interceptor` | object | Implementação de IDynaformInterceptor |
| `sk-datagrid-interceptor` | object | Implementação de IDatagridInterceptor |
| `sk-form-interceptor` | object | Implementação de IFormInterceptor |
| `sk-filter-panel-interceptor` | object | Implementação de IFilterPanelInterceptor |
| `sk-helper-class-name` | string | FQN da classe Helper Java |
| `sk-save-handler` | function | Handler do botão Salvar — retorna array de metadados de blocos |

**Métodos do dynaform (via `sk-on-dynaform-loaded`):**

| Método | Descrição |
|---|---|
| `setFieldProperty(fieldNames, propertyName, propertyValue)` | Altera metadado de campo: `enabled`, `required`, `description`, `visible`, `nullable` |
| `addFieldPropertyEvaluator(fieldName, propName, fn, dependentFields)` | Avaliador reativo de propriedade de campo |
| `getDataset()` | Retorna o dataset do dynaform |
| `getEntityName()` | Nome da entidade |
| `getNavigatorAPI()` | API para controlar botões do navigator |
| `getFieldTabName(fieldName)` | Aba em que o campo está |
| `isFieldVisible(fieldName)` | Verifica visibilidade do campo |
| `newRecord()` | Inicia inclusão |
| `hasAccess(action)` | Verifica permissão do usuário |
| `whenLoaded()` | Promise de quando os metadados estão prontos |
| `addShortcut(label, fn)` | Adiciona atalho de teclado |
| `showFieldTooltip(id, fieldName, i18nKey, duration)` | Exibe tooltip em campo |
| `setTabOrderConfig(config)` | Customiza ordem das abas |
| `addMetadataUpdateListener(listener)` | Listener de atualização de metadados |

**Exemplo de uso:**
```html
<sk-dynaform
    sk-entity-name="Produto"
    sk-resource-id="html5.Produto"
    sk-on-dynaform-loaded="ctrl.onDynaformLoaded(dynaform)"
    sk-show-filter="true">
</sk-dynaform>
```

```js
ctrl.onDynaformLoaded = function(dynaform) {
    dynaform.setFieldProperty('CODPROD', 'enabled', false);
    dynaform.getNavigatorAPI()
        .showAddButton(false)
        .showCopyButton(false);
};
```

---

## sk-filter-panel

**ID:** `snk.components.filterpanel.directive:sk-filter-panel`

Painel de filtros. Carrega filtros configurados no dicionário de dados automaticamente, além de permitir filtros customizados.

```html
<sk-filter-panel
    sk-data-source="{SkDataset}"
    sk-resource-id="{String}"
    sk-entity-name="{String}"
    sk-is-open="{boolean}"
    sk-has-active-filter="{boolean}"
    sk-dynamic-filter="{boolean}"
    sk-disable-personalized-filter="{boolean}"
    sk-filter-panel-interceptor="{IFilterPanelInterceptor}"
    sk-panel-width="{String}"
    sk-hide-btn-apply="{boolean}"
    sk-apply-function="{function}"
    sk-btn-apply-label="{String}"
    sk-field-filter-function="{function}"
    sk-link-filter-function="{function}"
    sk-pf-expanded="{boolean}"
    sk-custom-criteria-loader="{function}">
</sk-filter-panel>
```

**Parâmetros principais:**

| Parâmetro | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-data-source` | SkDataset | - | DataSource (dataset) |
| `sk-resource-id` | String | - | ID para salvar últimos filtros |
| `sk-is-open` | boolean | - | Abre o painel inicialmente |
| `sk-has-active-filter` | boolean | - | Bind para indicar filtro ativo |
| `sk-apply-function` | function | `refresh()` | Função chamada ao aplicar |
| `sk-btn-apply-label` | String | "Aplicar" | Label do botão |
| `sk-pf-expanded` | boolean | true | Filtro personalizado expandido |
| `sk-custom-criteria-loader` | function | undefined | Retorna critério dos filtros adicionais |

**Filtros customizados dentro do painel:**
```html
<sk-filter-panel sk-data-source="ctrl.dataset" sk-resource-id="html5.MinhaEntidade">
    <default-group label="Filtros">
        <sk-text-input sk-value="ctrl.filtroNome" sk-change="ctrl.aplicarFiltro()"></sk-text-input>
    </default-group>
    <custom-group label="Filtros Avançados" no-padding>
        <!-- conteúdo customizado -->
    </custom-group>
</sk-filter-panel>
```

---

## sk-filter-panel-btn

**ID:** `snk.components.filterpanel.directive:sk-filter-panel-btn`

Botão que abre/fecha o `sk-filter-panel`. Muda de cor quando há filtro ativo.

---

## IDatagridInterceptor

**ID:** `snk.components.datagrid.interfaces:IDatagridInterceptor`

Interface para interceptar comportamentos do datagrid.

---

## IFilterPanelInterceptor

**ID:** `snk.components.filterpanel.interfaces:IFilterPanelInterceptor`

Interface para interceptar o painel de filtros.

---

## FilterPanelService

**ID:** `snk.components.filterpanel.service:FilterPanelService`

Serviço para operações programáticas no filtro.
