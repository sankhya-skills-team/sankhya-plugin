# Design System — Componentes snk- (ERP Sankhya)

Componentes específicos do ERP Sankhya (prefixo `snk-`). Estes componentes integram diretamente com as entidades e funcionalidades do Sankhya W.

---

## snk-application

Container e provedor de contexto para aplicações Sankhya-blocks.

**Responsabilidades principais:**
- Registra-se no `ApplicationContext` como `"__SNK__APPLICATION__"`
- Gerencia `SnkMessageBuilder` para i18n (arquivo `/messages/appmessages.msg.js`)
- Coordena ciclo de vida via `connectedCallback` e `componentDidLoad`
- Gerencia layout via `setLayoutFormConfig`

**Métodos públicos:**

| Método | Descrição |
|--------|-----------|
| `whenApplicationReady()` | Promise resolvida quando o app estiver inicializado |
| `showPopUp(content, size, useHeader, callback)` | Exibe HTML em popup |
| `createDataunit(entityName, dataUnitName)` | Cria/cacheia instâncias DataUnit |
| `getDataUnit(entityName, dataUnitName)` | Recupera DataUnit do cache |
| `callServiceBroker(serviceName, payload)` | Executa chamadas ao backend |
| `get[Boolean/String/Int/Float/Date]Param(name)` | Recupera parâmetros do sistema |
| `hasAccess(access, resourceID)` | Verifica permissões do usuário |
| `importScript(relativePath)` | Carrega JavaScript da pasta `/public` |
| `addClientEvent(eventID, handler)` | Registra event listeners |

**Propriedades de configuração:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `configName` | string | Chave de configuração |
| `enableLockManagerLoadingApp` | boolean | Gerenciamento inteligente de loading |
| `formLegacyConfigName` | string | Chave de configuração legada de formulário |
| `gridLegacyConfigName` | string | Chave de configuração legada de grid |
| `messagesBuilder` | SnkMessageBuilder | Utilitário de mensagens |

**Eventos:** `applicationLoading`, `applicationLoaded`

**Padrões de loadByPK:** Personalizado via função, via atributo `data-load-by-pk`, ou implícito (filtra primeiro `snk-data-unit`).

---

## snk-attach

Componente para anexar arquivos, visualização e download de anexos.

| Propriedade | Tipo | Obrigatório | Descrição |
|-------------|------|-------------|-----------|
| `registerKey` | string | Sim | Identifica o registro pai |
| `entityName` | string | Sim | Entidade associada |
| `dataUnit` | DataUnit | Não | Instância para carregar dados |
| `fetcherType` | string | Não | `"AnexoSistema"` \| `"Another"` \| `"Attach"` |
| `messagesBuilder` | SnkMessageBuilder | Não | Padronização de mensagens |

**Evento:** `back` — disparado ao clicar em voltar/finalizar.

```jsx
<SnkAttach registerKey="999" entityName="Financeiro" onBack={handleBack} />
```

---

## snk-crud

Componente completo para operações CRUD (Create, Read, Update, Delete) de entidades. Integra `SnkGrid`, `SnkFilterBar` e `SnkForm`.

**Hierarquia obrigatória:**
```
SnkApplication → SnkDataUnit → SnkCrud
```

**Inicialização correta (evitar problemas):**
```javascript
const [dataUnit, setDataUnit] = useState(null);
<SnkDataUnit entityName="Entity" onDataUnitReady={(du) => setDataUnit(du)}>
  {dataUnit && <SnkCrud />}
</SnkDataUnit>
```

**Propriedades principais:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `autoLoad` | boolean | — | Carrega dados na inicialização |
| `multipleSelection` | boolean | true | Seleção múltipla de linhas |
| `enableGridInsert` | boolean | false | Inserção direta no grid |
| `statusResolver` | object/function | — | Badge colorido por status |
| `taskbarManager` | object | — | Personaliza botões da taskbar |
| `formLegacyConfigName` | string | — | `FormCfg:{TABLE_KEY}` |
| `gridLegacyConfigName` | string | — | `GrdCfgHtml5:{resourceId}` |
| `filterBarLegacyConfigName` | string | — | `{resourceId}` |

**Métodos:** `goToView(mode)`, `addGridCustomRender(field, render)`, `addCustomEditor(field, editor)`, `setFieldProp(field, prop, value)`, `getFilterBar()`, `openConfigurator()`

**Eventos:** `actionClick`, `formItemsReady`, `viewModeChanged`, `configuratorSave`

**Slots:** `SnkGridFooter`, `SnkFormTaskBar`, `SnkConfigContainerSlot`

---

## snk-data-exporter

Exporta dados para formatos de arquivo ou envio por e-mail.

**Estratégias:**
- `ServerSideExporter` (padrão): busca dados no backend
- `ClientSideExporter`: usa dados já carregados no frontend (quando `provider` implementa `getRecords()`)

**Interface `provider`:**

| Método | Descrição |
|--------|-----------|
| `getFilters()` | Filtros ativos |
| `getColumnsMetadata()` | Metadados das colunas |
| `getOrders()` | Ordenação |
| `getResourceURI()` | Nome do DataUnit |
| `getOffset()` / `getLimit()` | Paginação da exportação |
| `getSelectedIDs()` | IDs selecionados |
| `getRecordID()` | ID Base64 para relatórios customizados |

---

## snk-data-unit

Web Component (StencilJS) que faz bridge entre backend e UI para entidades do ERP Sankhya.

**Quando usar:** gestão de entidades do ERP, CRUD customizado, integração com `snk-grid/snk-form/snk-crud`, lógica de negócios centralizada.

**Hierarquia:** deve estar dentro de `SnkApplication`.

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `entityName` | string | — | Nome da entidade ERP |
| `dataUnitName` | string | — | Identificador/cache do DataUnit |
| `pageSize` | number | 150 | Registros por página |
| `beforeSave` | function | — | Validação pré-save; retorna false cancela |
| `afterSave` | function | — | Executa pós-save |
| `useCancelConfirm` | boolean | true | Confirmação ao cancelar |

**Eventos:**

| Evento | Payload | Descrição |
|--------|---------|-----------|
| `dataUnitReady` | DataUnit | Inicializado com metadados |
| `dataStateChange` | DataState | Mudança de estado dos dados |
| `insertionMode` | void | Modo inserção/cópia |
| `cancelEdition` | void | Edição cancelada |

> Evite modificar estado do DataUnit dentro de `dataStateChange` (loop infinito).

**Métodos:** `getDataUnit()`, `getRowMetadata(record)`, `getSelectedRecordsIDsInfo()`

---

## snk-entity-list

Renderiza lista de múltiplos checkboxes com campo de pesquisa para adicionar itens.

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `config` | SnkFilterItemConfig | Dados de configuração |
| `value` | IOption | Valor atual |
| `maxHeightList` | string | Altura máxima da lista com scroll |
| `rightListSlotBuilder` | function | Apresentação customizada de item |
| `errorMessage` | string | Mensagem de erro |

**Evento:** `valueChanged`
**Método:** `reloadList()` — recarrega a lista.

---

## snk-filter-bar

Barra de filtros interativa com chips horizontais, pop-ups de edição rápida e modal completo.

**Propriedades principais:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `dataUnit` | DataUnit | — | Carrega metadados dos filtros |
| `filterConfig` | SnkFilterItemConfig[] | — | Configuração customizada |
| `mode` | `"regular"` \| `"button"` \| `"hidden"` | `"regular"` | Modo de exibição |
| `autoLoad` | boolean | — | Carrega dados automaticamente |
| `resourceID` | string | — | Identificador do recurso |
| `disablePersonalizedFilter` | boolean | — | Desativa filtros personalizados |

**Métodos:** `reload()`, `getFilterItem(id)`, `updateFilterItem(item)`, `addFilterItem(item)`, `removeFilterItem(id)`, `showFilterModal()`, `getFilters()`

**Evento:** `configUpdated` — emitido ao alterar configuração.

```jsx
<SnkApplication configName="MovimentoBancario">
  <SnkDataUnit entityName="MovimentoBancario">
    <SnkFilterBar />
  </SnkDataUnit>
</SnkApplication>
```

---

## snk-filter-field-search

Popover com campo de busca e lista de campos para seleção de filtros.

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `fieldsDataSource` | FilterFieldsDataSource | Fonte de dados dos campos |
| `searchable` | boolean | Inclui campo de busca (padrão: true) |

**Métodos:** `setDataSource(link, fetcher)`, `applyFilter(text)`, `show(element, options)`

**Evento:** `ezSelectFilterItem` — disparado ao selecionar item.

---

## snk-form

Formulário que carrega automaticamente campos de entidades Sankhya, respeitando o Dicionário de Dados e o Configurador de Formulário.

> Requer `SnkDataUnit` inicializado. Use `onDataUnitReady` com state management.

**Propriedades:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `configName` | string | Chave de configuração do formulário |
| `formLegacyConfigName` | string | Chave legada de configuração |
| `recordsValidator` | IRecordValidator | Validação de registros |
| `messagesBuilder` | SnkMessageBuilder | Mensagens padronizadas |
| `resourceID` | string | Identificador do recurso |

**Métodos:** `showConfig()`, `hideConfig()`, `setFieldProp(field, prop, value)`, `addCustomEditor(field, editor)`, `validate()`

**Evento:** `formItemsReady` — permite adicionar elementos ao lado dos campos.

```javascript
function addIconsInForm(items) {
  const btn = document.createElement("ez-button");
  btn.setAttribute("mode", "icon");
  items.get("FIELDNAME")?.addRightElement(btn);
}
<SnkForm onFormItemsReady={(evt) => addIconsInForm(evt.detail.items)} />
```

---

## snk-grid

Grid tabular robusto para exibição e manipulação de dados no ERP Sankhya.

> Requer `SnkDataUnit` inicializado. Use `onDataUnitReady`.

**Propriedades principais:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `configName` | string | Chave de configuração |
| `multipleSelection` | boolean | Seleção múltipla |
| `compact` | boolean | Remove padding lateral |
| `statusResolver` | function/object | Cores de badge por status |
| `presentationMode` | enum | `primary` / `secondary` / `singleTaskbar` |
| `autoLoad` | boolean | Carrega dados automaticamente |

**Métodos:** `addGridCustomRender(field, render)`, `addCustomEditor(field, editor)`, `setConfig(config)`, `getFilterBar()`, `reloadFilterBar()`, `setFocus()`

**Eventos:** `actionClick`, `gridDoubleClick`, `componentReady`

**Altura mínima:** adicionar classe `grid_height-0` para adaptar ao container pai.

---

## snk-layout-form-config

Gerencia configurações de layout dos formulários de uma tela. Usa `resourceID` como chave.

> Apenas uma instância por tela. Padrão singleton.

| Modo | Comportamento |
|------|--------------|
| `CASCADE` | Campos empilhados verticalmente |
| `SIDE_BY_SIDE` | Campos lado a lado horizontalmente |

**Método:** `save()` — persiste a configuração escolhida.

---

## snk-message-builder

Fornece mensagens pré-definidas aos componentes. Configuração via `public/messages/appmessages.js`.

**Mensagens configuráveis por componente:**
- `SnkCrud`, `SnkFilterBar`, `SnkForm`, `SnkTaskbar`, `SnkFormConfig`, `SnkGridConfig`, `SnkDataUnit`, `SnkConfigurator`

```javascript
const appMessages = {
  SnkTaskbar: { titleSave: "Salvar", titleInsert: "Novo" },
  SnkForm: { "title.insert": "Criar registro" }
};
export default appMessages;
```

---

## snk-personalized-filter

Criação e gestão de filtros personalizados no Sankhya EIP.

> Não utilize diretamente — prefira `SnkFilterBar`.

**Modos:** Assistente (guiado) e Avançado (expressão livre).

**Propriedades:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `entityUri` | string | URI da entidade para campos disponíveis |
| `filterId` | string | Identificador do filtro a carregar |
| `configName` | string | Chave de configuração |
| `resourceID` | string | Identificador do recurso |
| `isDefaultFilter` | boolean | Define como filtro padrão do sistema |

**Método:** `createPersonalizedFilter()` — cria novo filtro personalizado.

**Eventos:** `ezCancel`, `ezSave` (retorna filterId), `ezAfterSave`

---

## snk-pesquisa

Painel de busca avançada para localizar e selecionar registros de entidades Sankhya. Suporta modos lista, grid e árvore hierárquica.

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `searchLoader` | function | Carrega itens (retorna Promise) |
| `selectItem` | function | Callback ao selecionar item |
| `entityName` | string | Entidade alvo |
| `isHierarchyEntity` | boolean | Ativa modo árvore hierárquica |
| `treeLoader` | function | Loader customizado para hierarquia |
| `allowsNonAnalytic` | boolean | Permite selecionar nós não-analíticos |
| `argument` | string | Texto de busca passado ao searchLoader |

---

## snk-print-selector

Interface de seleção de impressora para filas de impressão pendentes.

**Método principal:**
```javascript
const { selectedPrinter, saveSubstitute } = await printSelector.openPrintSelector(printJobData);
```

**`PendingPrintJobData`:** `transactionId`, `printServers`, `pendingPrinters`, `printServerActive`

**Uso:** criar dinamicamente via `document.createElement('snk-print-selector')` e adicionar ao `document.body`.

---

## snk-simple-bar

Header padronizado com título, breadcrumb, botão voltar e slot direito. Sem ações CRUD.

**Use em:** telas informativas, dashboards, relatórios.
**Não use em:** telas com CRUD (use `snk-taskbar`).

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `label` | string | Título do cabeçalho |
| `breadcrumbItens` | IBreadcrumbItem[] | Itens de navegação |
| `messagesBuilder` | SnkMessageBuilder | Mensagens |

**Slot:** `rightSlot` — conteúdo alinhado à direita.
**Sticky:** adicionar classe `ez-content-sticky`.
**Eventos:** `exit` (botão voltar), `clickBreadcrumbItem`

```jsx
<SnkSimpleBar label="Título" breadcrumbItens={items} onExit={handleExit}>
  <div slot="rightSlot">Conteúdo customizado</div>
</SnkSimpleBar>
```

---

## snk-simple-crud

CRUD independente que encapsula EzGrid + EzForm + SnkTaskbar + SnkDataUnit.

**Modos:** `SERVER` (backend) e `IN_MEMORY` (dados temporários locais).

**Propriedades:**

| Propriedade | Tipo | Padrão | Descrição |
|-------------|------|--------|-----------|
| `dataUnit` | DataUnit | — | Instância de gerenciamento de dados |
| `entityName` | string | — | Entidade backend |
| `mode` | SIMPLE_CRUD_MODE | SERVER | Modo de operação |
| `pageSize` | number | 150 | Registros por página |
| `multipleSelection` | boolean | — | Seleção múltipla |
| `configName` | string | — | Chave de persistência de configuração |

**Métodos de dados:** `setMetadata(metadata)`, `setRecords(records)`, `getRecords()`
**Métodos de navegação:** `goToView(mode)`, `openConfigurator()`, `closeConfigurator()`
**Métodos de customização:** `addGridCustomRender()`, `addCustomEditor()`, `setFieldProp()`

**Eventos:** `dataUnitReady`, `dataStateChange`, `actionClick`, `formItemsReady`

---

## snk-simple-form-config

Configura formulário simplificado, tipicamente usado dentro de `SnkSimpleCrud`.

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `configName` | string | Chave de configuração do formulário |
| `dataUnit` | DataUnit | Instância correspondente ao formulário |

**Método:** `show()` — exibe o componente na tela.

---

## snk-taskbar

Barra de ações com botões padronizados para operações CRUD e ações customizadas.

**Botões padrão:** `PREVIOUS`, `NEXT`, `INSERT`, `SAVE`, `REMOVE`, `CLONE`, `ATTACH`, `MORE_OPTIONS`, `GRID_MODE`, `CONFIGURATOR`, `DIVIDER`

**Propriedades:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `buttons` | string | Lista de botões separados por vírgula |
| `customButtons` | Map | Configurações de botões customizados |
| `actionsList` | Action[] | Itens do menu "Mais Opções" |
| `dataUnit` | DataUnit | Controla navegação de registros |
| `presentationMode` | PresentationMode | `primary` \| `secondary` |
| `disabledButtons` | string[] | Botões desabilitados |

**Eventos:** `actionClick`, `taskbarSaveLocker`, `taskbarSaveUnlocker`

**Slot:** `TASKBAR_CUSTOM_ELEMENTS` — para conteúdo HTML customizado.
