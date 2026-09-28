> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit (snapshot 2026-09-28)

# DataUnit

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / DataUnit

# Class: DataUnit

`DataUnit`: Atua como uma camada de abstração entre o back-end e a interface do usuário.

## Constructors

### new DataUnit()

> **new DataUnit**(`name`, `parentDataUnit`?): `DataUnit`

#### Parameters

• **name** : `string`= `DataUnit.DEFAULT_DATAUNIT_NAME`

• **parentDataUnit?** : `DataUnit`

#### Returns

`DataUnit`

#### Source

src/dataunit/DataUnit.ts:71

## Properties

### _allowReleaseCallbacks

> `private` **_allowReleaseCallbacks** : `boolean`

#### Source

src/dataunit/DataUnit.ts:58

### _cancelPagination

> `private` **_cancelPagination** : `boolean` = `false`

#### Source

src/dataunit/DataUnit.ts:60

### _childByName

> `private` **_childByName** : `Map`<`string`, `DataUnit`>

#### Source

src/dataunit/DataUnit.ts:53

### _defaultSorting

> `private` **_defaultSorting** : `Sort`[]

#### Source

src/dataunit/DataUnit.ts:57

### _fieldSourceValue

> `private` **_fieldSourceValue** : `Map`<`string`, `string`>

#### Source

src/dataunit/DataUnit.ts:62

### _filterProviders

> `private` **_filterProviders** : `Map`<`string`, `FilterProvider`>

#### Source

src/dataunit/DataUnit.ts:49

### _interceptors

> `private` **_interceptors** : `Map`<`string`, `DUActionInterceptor`>

#### Source

src/dataunit/DataUnit.ts:51

### _isMultipleEdition

> `private` **_isMultipleEdition** : `boolean` = `false`

#### Source

src/dataunit/DataUnit.ts:61

### _loadingLockers

> `private` **_loadingLockers** : `Promise`<`void`>[]

#### Source

src/dataunit/DataUnit.ts:55

### _name

> `private` **_name** : `string`

#### Source

src/dataunit/DataUnit.ts:46

### _observers

> `private` **_observers** : `Map`<`string`, (`action`, `options`?) => `void`>

#### Source

src/dataunit/DataUnit.ts:47

### _pageSize

> `private` **_pageSize** : `number`

#### Source

src/dataunit/DataUnit.ts:52

### _parentDataUnit

> `private` **_parentDataUnit** : `undefined` | `DataUnit`

#### Source

src/dataunit/DataUnit.ts:54

### _savingLockers

> `private` **_savingLockers** : `Promise`<`any`>[] = `[]`

#### Source

src/dataunit/DataUnit.ts:56

### _sortingProvider?

> `private` `optional` **_sortingProvider** : `SortingProvider`

#### Source

src/dataunit/DataUnit.ts:48

### _stateManager

> `private` **_stateManager** : `default`

#### Source

src/dataunit/DataUnit.ts:50

### _uuid

> `private` **_uuid** : `string`

#### Source

src/dataunit/DataUnit.ts:45

### _waitingToReload

> `private` **_waitingToReload** : `boolean` = `false`

#### Source

src/dataunit/DataUnit.ts:59

### allRecordsLoader()?

> `optional` **allRecordsLoader** : (`dataUnit`) => `undefined` | `Record`[]

#### Parameters

• **dataUnit** : `DataUnit`

#### Returns

`undefined` | `Record`[]

#### Source

src/dataunit/DataUnit.ts:69

### dataLoader()?

> `optional` **dataLoader** : (`dataUnit`, `request`) => `Promise`<`LoadDataResponse`>

#### Parameters

• **dataUnit** : `DataUnit`

• **request** : `LoadDataRequest`

#### Returns

`Promise`<`LoadDataResponse`>

#### Source

src/dataunit/DataUnit.ts:65

### metadataLoader()?

> `optional` **metadataLoader** : (`dataUnit`) => `Promise`<`UnitMetadata`>

#### Parameters

• **dataUnit** : `DataUnit`

#### Returns

`Promise`<`UnitMetadata`>

#### Source

src/dataunit/DataUnit.ts:64

### recordLoader()?

> `optional` **recordLoader** : (`dataUnit`, `recordIds`) => `Promise`<`Record`[]>

#### Parameters

• **dataUnit** : `DataUnit`

• **recordIds** : `string`[]

#### Returns

`Promise`<`Record`[]>

#### Source

src/dataunit/DataUnit.ts:68

### removeLoader()?

> `optional` **removeLoader** : (`dataUnit`, `recordIds`) => `Promise`<`string`[]>

#### Parameters

• **dataUnit** : `DataUnit`

• **recordIds** : `string`[]

#### Returns

`Promise`<`string`[]>

#### Source

src/dataunit/DataUnit.ts:67

### saveLoader()?

> `optional` **saveLoader** : (`dataUnit`, `changes`) => `Promise`<`SavedRecord`[]>

#### Parameters

• **dataUnit** : `DataUnit`

• **changes** : `Change`[]

#### Returns

`Promise`<`SavedRecord`[]>

#### Source

src/dataunit/DataUnit.ts:66

### ALL_RECORDS_SELECTION_SOURCE

> `static` **ALL_RECORDS_SELECTION_SOURCE** : `string` = `"ALL_RECORDS_SELECTION_SOURCE"`

#### Source

src/dataunit/DataUnit.ts:42

### CHANGING_PAGE_LOADING_SOURCE

> `static` **CHANGING_PAGE_LOADING_SOURCE** : `string` = `"CHANGING_PAGE_LOADING_SOURCE"`

#### Source

src/dataunit/DataUnit.ts:41

### DEFAULT_DATAUNIT_NAME

> `static` **DEFAULT_DATAUNIT_NAME** : `string` = `"dataunit"`

#### Source

src/dataunit/DataUnit.ts:43

## Accessors

### allowReleaseCallbacks

> `set` **allowReleaseCallbacks**(`allow`): `void`

#### Parameters

• **allow** : `boolean`

#### Source

src/dataunit/DataUnit.ts:2002

### cancelPagination

> `get` **cancelPagination**(): `boolean`

Informa se a paginação deve ser cancelada.

> `set` **cancelPagination**(`cancelPagination`): `void`

Informa se a paginação deve ser cancelada.

#### Parameters

• **cancelPagination** : `boolean`

#### Returns

`boolean`

#### Source

src/dataunit/DataUnit.ts:180

### dataUnitId

> `get` **dataUnitId**(): `string`

#### Returns

`string`

#### Source

src/dataunit/DataUnit.ts:157

### defaultSorting

> `set` **defaultSorting**(`sorting`): `void`

Define a ordenação padrão.

#### Parameters

• **sorting** : `Sort`[]

Ordenação padrão.

#### Source

src/dataunit/DataUnit.ts:833

### isMultipleEdition

> `get` **isMultipleEdition**(): `boolean`

Informa se o DataUnit está no modo de edição de múltiplos registros.

> `set` **isMultipleEdition**(`isMultipleEdition`): `void`

Define se o DataUnit está no modo de edição de múltiplos registros.

#### Parameters

• **isMultipleEdition** : `boolean`

#### Returns

`boolean`

#### Source

src/dataunit/DataUnit.ts:194

### metadata

> `get` **metadata**(): `UnitMetadata`

Obtém os metadados do DataUnit.

> `set` **metadata**(`md`): `void`

Define a propriedade metadata da instância da classe com um novo valor e chama o método dispatchAction para notificar os observers da aplicação sobre a mudança.

#### Parameters

• **md** : `UnitMetadata`

#### Returns

`UnitMetadata`

#### Source

src/dataunit/DataUnit.ts:851

### name

> `get` **name**(): `string`

Obtém o nome de identificação do DataUnit (geralmente em formato de URI - Uniform Resource Identifier).

#### Returns

`string`

  * Nome de identificação do DataUnit.

#### Source

src/dataunit/DataUnit.ts:213

### pageSize

> `get` **pageSize**(): `number`

Obtém a quantidade de registros que está sendo exibido por página.

> `set` **pageSize**(`size`): `void`

Define a quantidade de registros que será exibido por página.

#### Parameters

• **size** : `number`

Quantidade de registros que será exibido por página.

#### Returns

`number`

  * Quantidade de registros exibidos por página.

#### Source

src/dataunit/DataUnit.ts:924

### records

> `get` **records**(): `Record`[]

Obtém todos os registros atuais.

> `set` **records**(`records`): `void`

Define a propriedade records da instância da classe com um novo valor e chama o método dispatchAction para notificar os observers da aplicação sobre a mudança.

#### Parameters

• **records** : `Record`[]

#### Returns

`Record`[]

  * Todos os registros atuais.

#### Source

src/dataunit/DataUnit.ts:901

### sortingProvider

> `set` **sortingProvider**(`provider`): `void`

Define a lógica de ordenação dos registros.

#### Parameters

• **provider** : `SortingProvider`

Objeto usado para definir a propriedade sortingProvider da instância da classe.

#### Source

src/dataunit/DataUnit.ts:822

## Methods

### addField()

> **addField**(`field`): `void`

Adiciona um campo stand-alone ao dataUnit.

#### Parameters

• **field** : `Omit`<`FieldDescriptor`, `"standAlone"`>

Campo a ser adicionado.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1983

### addFilterProvider()

> **addFilterProvider**(`provider`): `void`

Adiciona um FilterProvider.

#### Parameters

• **provider** : `FilterProvider`

FilterProvider que será adicionado.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:779

### addGlobalLoaderProp()

> **addGlobalLoaderProp**(`name`, `value`): `void`

Adiciona uma propriedade transacional que será envida aos loaders (dataLoader, saveLoader, removeLoader e recordLoader) na chamada. Essas propriedades serão limpas ao final da execução de cada método.

#### Parameters

• **name** : `string`

Nome da propriedade

• **value** : `string`

Valor da propriedade

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:144

### addInterceptor()

> **addInterceptor**(`interceptor`): `void`

Adiciona um interceptor correspondente a uma ação do DataUnit para fazer um processamento customizado.

#### Parameters

• **interceptor** : `DUActionInterceptor`

Interceptor a ser adicionado.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:757

### addLoadingLocker()

> **addLoadingLocker**(): `Function`

Adiciona um locker para impedir o carregamento dos registros do dataUnit.

#### Returns

`Function`

Retorna uma função responsável por liberar o lock adicionado.

#### Source

src/dataunit/DataUnit.ts:1992

### addRecord()

> **addRecord**(`executionCtx`?): `Promise`<`boolean`>

Adiciona um novo registro.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da inserção do dado no DataUnit.

#### Returns

`Promise`<`boolean`>

#### Source

src/dataunit/DataUnit.ts:970

### addSourceFieldValue()

> **addSourceFieldValue**(`sourceFieldName`, `targetFieldName`): `void`

Adiciona um mapeamento de origem dos dados de um determinado campo

#### Parameters

• **sourceFieldName** : `string`

• **targetFieldName** : `string`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:2010

### ~~addStandAloneField()~~

> **addStandAloneField**(): `void`

Adiciona um campo stand-alone ao dataUnit.

#### Returns

`void`

#### Deprecated

  * metodo depreciado, utilizar o metodo addField

#### Source

src/dataunit/DataUnit.ts:1974

### areEquivalentValues()

> `private` **areEquivalentValues**(`newValue`, `currentValue`, `typedValue`): `boolean`

#### Parameters

• **newValue** : `any`

• **currentValue** : `any`

• **typedValue** : `any`

#### Returns

`boolean`

#### Source

src/dataunit/DataUnit.ts:1097

### buildChangesToSave()

> **buildChangesToSave**(): `Change`[]

Retorna as alterações a serem salvas no DataUnit atual.

#### Returns

`Change`[]

  * Mudanças realizadas no DataUnit atual

#### Source

src/dataunit/DataUnit.ts:585

### buildChangesToSaveFromChild()

> **buildChangesToSaveFromChild**(`allChanges`, `dataUnit`): `void`

#### Parameters

• **allChanges** : `Change`[]

• **dataUnit** : `DataUnit`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:589

### canRedo()

> **canRedo**(): `boolean`

Retorna se a informação do estado futuro está salva, permitindo refazer a ação.

#### Returns

`boolean`

Verdadeiro se for possível refazer a ação.

#### Source

src/dataunit/DataUnit.ts:1583

### canUndo()

> **canUndo**(): `boolean`

Retorna se a informação do estado anterior está salva, permitindo desfazer a ação.

#### Returns

`boolean`

Verdadeiro se for possível desfazer a ação.

#### Source

src/dataunit/DataUnit.ts:1572

### cancelEdition()

> **cancelEdition**(`executionCtx`?, `fromParent`?, `silent`?): `Promise`<`boolean`>

Cancela edição do registro atual.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução do cancelamento da seleção dos registros.

• **fromParent?** : `boolean`

• **silent?** : `boolean`= `false`

#### Returns

`Promise`<`boolean`>

#### Source

src/dataunit/DataUnit.ts:1424

### cancelWaitingChange()

> **cancelWaitingChange**(`fieldName`): `void`

Cancela o início de uma alteração no campo.

#### Parameters

• **fieldName** : `string`

Identificador do campo.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1171

### childrenIsDirty()

> `private` **childrenIsDirty**(): `boolean`

Retorna se existe algum DataUnit detail com alterações pendentes.

#### Returns

`boolean`

Verdadeiro se existir alterações pendentes em algum DataUnit detail.

#### Source

src/dataunit/DataUnit.ts:1467

### clearDataUnit()

> **clearDataUnit**(): `void`

Limpa todos os registros do DataUnit

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1357

### clearInvalid()

> **clearInvalid**(`recordId`, `fieldName`?): `void`

Limpa campos inválidos.

#### Parameters

• **recordId** : `string`

Indica em qual registro o campo não está mais inválido.

• **fieldName?** : `string`

Nome do campo. Caso omitido, todos os campos serão limpos.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1136

### clearSelection()

> **clearSelection**(`executionCtx`?): `void`

Limpa a seleção.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção dos registros do DataUnit.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1245

### copySelected()

> **copySelected**(`executionCtx`?): `void`

Efetua a cópia do registro selecionado.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da cópia do dado do DataUnit.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:981

### disableField()

> **disableField**(`fieldName`): `void`

Desabilita um campo do DataUnit

#### Parameters

• **fieldName** : `string`

nome do campo para ficar desabilitado.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1864

### dispatchAction()

> `private` **dispatchAction**(`actionType`, `payload`?, `executionCtx`?, `options`?): `Promise`<`boolean`>

Lança ação do DataUnit para que sejam processadas.

#### Parameters

• **actionType** : `Action`

Tipo de ação que será executada.

• **payload?** : `any`

Dados que serão processados na ação.

• **executionCtx?** : `ExecutionContext`

Contexto de execução de lançar a ação que será executada.

• **options?** : `DataUnitEventOptions`

#### Returns

`Promise`<`boolean`>

  * Verdadeiro se ação iniciada.

#### Source

src/dataunit/DataUnit.ts:1633

### doDispatchAction()

> `private` **doDispatchAction**(`action`, `options`): `void`

Processa as ações no DataUnit e notifica os observers.

#### Parameters

• **action** : `DataUnitAction`

Ações em execução no DataUnit.

• **options** : `DataUnitEventOptions`= `{}`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1681

### enableField()

> **enableField**(`fieldName`): `void`

Habilita um campo do DataUnit

#### Parameters

• **fieldName** : `string`

nome do campo para ser habilitado.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1845

### executeLoadData()

> `private` **executeLoadData**(`request`, `executionCtx`?, `checkLastFilter`?, `selectFirstRecord`?): `Promise`<`LoadDataResponse`>

Executa o carregamento dos registros.

#### Parameters

• **request** : `LoadDataRequest`

Dados da requisição para carregamento dos registros.

• **executionCtx?** : `ExecutionContext`

Contexto de execução do carregamento dos registros do DataUnit.

• **checkLastFilter?** : `boolean`

Habilita a verificação da última requisição, evitando carga desnecessária.

• **selectFirstRecord?** : `boolean`

#### Returns

`Promise`<`LoadDataResponse`>

  * Registros do DataUnit.

#### Source

src/dataunit/DataUnit.ts:282

### getAddedRecords()

> **getAddedRecords**(): `Record`[]

Obtém os registros adicionados no DataUnit.

#### Returns

`Record`[]

  * Lista dos registros adicionados.

#### Source

src/dataunit/DataUnit.ts:947

### getAllChangesToSave()

> **getAllChangesToSave**(): `Change`[]

Retorna todas as alterações do DataUnit a serem salvas, incluindo no nível Master e Detail.

#### Returns

`Change`[]

  * Todas as mudanças realizadas no DataUnit, tanto Master quanto Detail;

#### Source

src/dataunit/DataUnit.ts:607

### getAppliedFilters()

> **getAppliedFilters**(): `undefined` | `Filter`[]

Obtém os filtros aplicados.

#### Returns

`undefined` | `Filter`[]

  * Lista de filtros.

#### Source

src/dataunit/DataUnit.ts:1834

### getBeforeSavePromisses()

> `private` **getBeforeSavePromisses**(): (`undefined` | `Promise`<`any`>)[]

#### Returns

(`undefined` | `Promise`<`any`>)[]

#### Source

src/dataunit/DataUnit.ts:500

### getChildDataunit()

> **getChildDataunit**(`name`): `DataUnit`

Cria um dataunit filho.

#### Parameters

• **name** : `string`

Nome do dataunit filho.

#### Returns

`DataUnit`

#### Source

src/dataunit/DataUnit.ts:1701

### getChildInfo()

> **getChildInfo**(`name`): `undefined` | `ChildDescriptor`

Obtém informações da ligação para um DataUnit filho.

#### Parameters

• **name** : `string`

Nome do DataUnit que se deseja.

#### Returns

`undefined` | `ChildDescriptor`

  * As informações sobre a ligação solicitada. Pode retornar undefined.

#### Source

src/dataunit/DataUnit.ts:864

### getField()

> **getField**(`fieldName`): `undefined` | `FieldDescriptor`

Obtém metadados de um campo específico.

#### Parameters

• **fieldName** : `string`

Identificador do campo.

#### Returns

`undefined` | `FieldDescriptor`

  * Metadados do campo informado.

#### Source

src/dataunit/DataUnit.ts:959

### getFieldValue()

> **getFieldValue**(`fieldName`): `any`

Obtém valor do campo desejado.

#### Parameters

• **fieldName** : `string`

Identificador do campo a ser buscado.

#### Returns

`any`

  * Valor do campo.

#### Source

src/dataunit/DataUnit.ts:1044

### getFielterProviderKey()

> `private` **getFielterProviderKey**(`provider`): `string`

Obtém chave única para identificação do FilterProvider.

#### Parameters

• **provider** : `FilterProvider`

Interface FilterProvider na qual será retornada uma chave correspondente.

#### Returns

`string`

  * A chave do provider.

#### Source

src/dataunit/DataUnit.ts:264

### getFilters()

> **getFilters**(): `undefined` | `Filter`[]

Obtém todos os filtros de dados.

#### Returns

`undefined` | `Filter`[]

  * Lista de filtros.

#### Source

src/dataunit/DataUnit.ts:1805

### getFormattedValue()

> **getFormattedValue**(`fieldName`, `value`?): `string`

Formata o valor do campo considerando as informações do descriptor. Diferente do método "valueToString" que retorna o dado em valor textual, getFormattedValue retorna uma informação amigável ao usuário, geralmente usada na interface.

#### Parameters

• **fieldName** : `string`

Nome do campo utilizado do qual se quer obter valor.

• **value?** : `any`

(opcional) - O valor a ser convertido. Caso omitido pega do registro selecionado.

#### Returns

`string`

  * Valor formatado.

#### Source

src/dataunit/DataUnit.ts:735

### getGlobalLoaderProps()

> **getGlobalLoaderProps**(): `Map`<`string`, `string`>

Retorna as propriedades transacionais adicionados anteriores à chamada.

#### Returns

`Map`<`string`, `string`>

  * Todas as propriedades desde o final do último loader.

#### Source

src/dataunit/DataUnit.ts:153

### getInvalidMessage()

> **getInvalidMessage**(`recordId`, `fieldName`): `undefined` | `string`

Obtém a mensagem de campo inválido para determinado registro.

#### Parameters

• **recordId** : `string`

Identificador do registro.

• **fieldName** : `string`

Nome do campo.

#### Returns

`undefined` | `string`

#### Source

src/dataunit/DataUnit.ts:1148

### getLastLoadRequest()

> **getLastLoadRequest**(): `undefined` | `LoadDataRequest`

Obtém as informações da última carga de dados.

#### Returns

`undefined` | `LoadDataRequest`

  * As informações de filtro e paginação.

#### Source

src/dataunit/DataUnit.ts:1823

### getLoadDataRequest()

> `private` **getLoadDataRequest**(`quickFilter`?, `source`?, `keepSelection`?): `LoadDataRequest`

#### Parameters

• **quickFilter?** : `QuickFilter`

• **source?** : `string`

• **keepSelection?** : `boolean`

#### Returns

`LoadDataRequest`

#### Source

src/dataunit/DataUnit.ts:464

### getModifiedRecords()

> **getModifiedRecords**(): `Record`[]

Obtém os registros modificados e ainda não salvos no DataUnit.

#### Returns

`Record`[]

  * Lista dos registros em edição.

#### Source

src/dataunit/DataUnit.ts:935

### getPaginationInfo()

> **getPaginationInfo**(): `void` | `PaginationInfo`

Obtém informações de paginação dos registros.

#### Returns

`void` | `PaginationInfo`

  * Informações da paginação de registros.

#### Source

src/dataunit/DataUnit.ts:800

### getParentDataUnit()

> **getParentDataUnit**(): `undefined` | `DataUnit`

Retorna o DataUnit pai

#### Returns

`undefined` | `DataUnit`

DataUnit pai ou undefined

#### Source

src/dataunit/DataUnit.ts:1347

### getParentRecordId()

> `private` **getParentRecordId**(): `undefined` | `string`

#### Returns

`undefined` | `string`

#### Source

src/dataunit/DataUnit.ts:1017

### getRecordsByDataUnit()

> `private` **getRecordsByDataUnit**(`records`): `Map`<`string`, `Record`[]>

#### Parameters

• **records** : `Record`[]

#### Returns

`Map`<`string`, `Record`[]>

#### Source

src/dataunit/DataUnit.ts:995

### getSelectedRecord()

> **getSelectedRecord**(): `undefined` | `Record`

Retorna apenas um registro selecionado no Dataunit

#### Returns

`undefined` | `Record`

  * Registro selecionado.

#### Source

src/dataunit/DataUnit.ts:1338

### ~~getSelectedRecords()~~

> **getSelectedRecords**(): `undefined` | `Record`[]

Obtém todos os registros selecionados.

#### Returns

`undefined` | `Record`[]

  * Lista de registros selecionados.

#### Deprecated

  * Utilize o método `getSelectionInfo()` para obter os registros selecionados. Devido a seleção virtual baseada em critérios e ordenação (ALL_RECORDS), esse método foi descontinuado e pode retornar erros no caso da seleção virtual.

#### Source

src/dataunit/DataUnit.ts:1931

### ~~getSelection()~~

> **getSelection**(): `string`[]

Obtém ids dos registros selecionados.

#### Returns

`string`[]

  * Lista com id de todos os registros selecionados.

#### Deprecated

  * Utilize o método `getSelectionInfo()` para obter os registros selecionados. Devido a seleção virtual baseada em critérios e ordenação (ALL_RECORDS), esse método foi descontinuado e pode retornar erros no caso da seleção virtual.

#### Source

src/dataunit/DataUnit.ts:1955

### getSelectionInfo()

> **getSelectionInfo**(): `SelectionInfo`

Obtém informações sobre a seleção atual.

#### Returns

`SelectionInfo`

  * Objeto com informações como registros selecionados e seleção por critério.

#### Source

src/dataunit/DataUnit.ts:1309

### getSort()

> **getSort**(): `undefined` | `Sort`[]

Obtém a estrutura de ordenação das colunas dos dados.

#### Returns

`undefined` | `Sort`[]

  * Lista dos ordenáveis por prioridade.

#### Source

src/dataunit/DataUnit.ts:1794

### getSourceFieldValue()

> **getSourceFieldValue**(`sourceFieldName`): `undefined` | `string`

Retornar o campo de origem dos dados caso exista mapeamento

#### Parameters

• **sourceFieldName** : `string`

#### Returns

`undefined` | `string`

#### Source

src/dataunit/DataUnit.ts:2017

### gotoPage()

> **gotoPage**(`page`, `executionCtx`?): `Promise`<`void` | `LoadDataResponse`>

Alterna entre os registros por número de página.

#### Parameters

• **page** : `number`

Número da página desejada.

• **executionCtx?** : `ExecutionContext`

Contexto de execução do carregamento dos registros do DataUnit.

#### Returns

`Promise`<`void` | `LoadDataResponse`>

  * Registros da página desejada.

#### Source

src/dataunit/DataUnit.ts:413

### hasCopiedRecord()

> **hasCopiedRecord**(): `boolean`

Retorna se existe pelo menos um registro novo.

#### Returns

`boolean`

Verdadeiro se algum registro foi adicionado.

#### Source

src/dataunit/DataUnit.ts:1551

### hasDirtyRecords()

> **hasDirtyRecords**(): `boolean`

Retorna se existe algum registro em modo de edição.

#### Returns

`boolean`

Verdadeiro se existir alterações de registros pendentes.

#### Source

src/dataunit/DataUnit.ts:1481

### hasNewRecord()

> **hasNewRecord**(): `boolean`

Retorna se existe pelo menos um registro novo.

#### Returns

`boolean`

Verdadeiro se algum registro foi adicionado.

#### Source

src/dataunit/DataUnit.ts:1539

### hasNext()

> **hasNext**(): `boolean`

Retorna se existir uma pagina seguinte a atual na paginação.

#### Returns

`boolean`

Verdadeiro se existir uma próxima página.

#### Source

src/dataunit/DataUnit.ts:1492

### hasPrevious()

> **hasPrevious**(): `boolean`

Retorna se existe uma página anterior a atual na paginação.

#### Returns

`boolean`

Verdadeiro se existir uma página anterior.

#### Source

src/dataunit/DataUnit.ts:1507

### hasWaitingChanges()

> **hasWaitingChanges**(): `boolean`

Retorna se existe alterações pendentes.

#### Returns

`boolean`

Verdadeiro se existir pendências de modificações.

#### Source

src/dataunit/DataUnit.ts:1179

### hideField()

> **hideField**(`fieldName`, `options`?): `void`

Deixa um campo do DataUnit invisível

#### Parameters

• **fieldName** : `string`

nome do campo para ficar invisível.

• **options?** : `HideFieldOptions`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1883

### intercept()

> `private` **intercept**(`action`, `interceptors`): `Promise`<`DataUnitAction`>

Notifica os interceptors de que uma ação foi executada, para que cada interceptor possa fazer sua respectiva tratativa dos dados.

#### Parameters

• **action** : `DataUnitAction`

Ação que foi executada.

• **interceptors** : `IterableIterator`<`DUActionInterceptor`>

Interceptors que serão notificados.

#### Returns

`Promise`<`DataUnitAction`>

  * Ação executada no DataUnit.

#### Source

src/dataunit/DataUnit.ts:1664

### isDirty()

> **isDirty**(`ignoreChildren`?): `boolean`

Retorna se existe algum tipo de alteração pendente.

#### Parameters

• **ignoreChildren?** : `boolean`

#### Returns

`boolean`

Verdadeiro se existir alterações pendentes.

#### Source

src/dataunit/DataUnit.ts:1443

### isNewRecord()

> **isNewRecord**(`recordId`): `boolean`

Verifica se um registro é proveniente de inclusão.

#### Parameters

• **recordId** : `string`

O id do registro a ser verificado.

#### Returns

`boolean`

Verdadeiro se o id solicitado é de um registro novo.

#### Source

src/dataunit/DataUnit.ts:1523

### isParentDirty()

> **isParentDirty**(): `boolean`

Retorna se existe alterações pendentes no DataUnit pai.

#### Returns

`boolean`

Verdadeiro se existir alterações pendentes e Falso caso não exista alterações ou não exista DataUnit pai.

#### Source

src/dataunit/DataUnit.ts:1456

### isSameRequest()

> `private` **isSameRequest**(`request`): `boolean`

#### Parameters

• **request** : `LoadDataRequest`

#### Returns

`boolean`

#### Source

src/dataunit/DataUnit.ts:335

### isWaitingToReload()

> **isWaitingToReload**(): `boolean`

Retorna se o dataUnit está com recarregamento pendente.

#### Returns

`boolean`

#### Source

src/dataunit/DataUnit.ts:165

### loadData()

> **loadData**(`quickFilter`?, `executionCtx`?, `checkLastFilter`?, `source`?, `selectFirstRecord`?, `keepSelection`?): `Promise`<`LoadDataResponse`>

Carrega os registros do DataUnit.

#### Parameters

• **quickFilter?** : `QuickFilter`

Filtros a serem aplicados.

• **executionCtx?** : `ExecutionContext`

Contexto de execução do carregamento dos registros.

• **checkLastFilter?** : `boolean`

Habilita a verificação da última requisição, evitando carga desnecessária.

• **source?** : `string`

• **selectFirstRecord?** : `boolean`

• **keepSelection?** : `boolean`

#### Returns

`Promise`<`LoadDataResponse`>

  * Registros requisitados.

#### Source

src/dataunit/DataUnit.ts:383

### loadDataWithParams()

> **loadDataWithParams**(`__namedParameters`): `Promise`<`LoadDataResponse`>

#### Parameters

• **__namedParameters** : `LoadDataParams`

#### Returns

`Promise`<`LoadDataResponse`>

#### Source

src/dataunit/DataUnit.ts:368

### loadMetadata()

> **loadMetadata**(`executionCtx`?): `Promise`<`void` | `UnitMetadata`>

Carrega os metadados do DataUnit.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução do carregamento dos metadados do DataUnit.

#### Returns

`Promise`<`void` | `UnitMetadata`>

  * Metadados carregados.

#### Source

src/dataunit/DataUnit.ts:350

### nextPage()

> **nextPage**(`executionCtx`?): `Promise`<`void` | `LoadDataResponse`>

Vai para os registros da página seguinte.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução do carregamento dos registros do DataUnit.

#### Returns

`Promise`<`void` | `LoadDataResponse`>

  * Registros da página seguinte.

#### Source

src/dataunit/DataUnit.ts:447

### nextRecord()

> **nextRecord**(`executionCtx`?): `Promise`<`void`>

Seleciona o próximo registro.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção do registro do DataUnit.

#### Returns

`Promise`<`void`>

#### Source

src/dataunit/DataUnit.ts:1369

### notifySavingData()

> `private` **notifySavingData**(`executionCtx`?): `Promise`<`boolean`>

#### Parameters

• **executionCtx?** : `ExecutionContext`

#### Returns

`Promise`<`boolean`>

#### Source

src/dataunit/DataUnit.ts:485

### onDataUnitParentEvent()

> `private` **onDataUnitParentEvent**(`action`): `void`

Trata as Actions do DataUnit Parent

#### Parameters

• **action** : `DataUnitAction`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:238

### previousPage()

> **previousPage**(`executionCtx`?): `Promise`<`void` | `LoadDataResponse`>

Vai para os registros da página anterior.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução do carregamento dos registros do DataUnit.

#### Returns

`Promise`<`void` | `LoadDataResponse`>

  * Registros da página anterior.

#### Source

src/dataunit/DataUnit.ts:460

### previousRecord()

> **previousRecord**(`executionCtx`?): `Promise`<`void`>

Seleciona o registro anterior.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção do registro do DataUnit.

#### Returns

`Promise`<`void`>

#### Source

src/dataunit/DataUnit.ts:1396

### processLoadingLockers()

> `private` **processLoadingLockers**(): `Promise`<`void`>

#### Returns

`Promise`<`void`>

#### Source

src/dataunit/DataUnit.ts:2021

### redo()

> **redo**(`executionCtx`?): `void`

Refaz a última ação.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução de refazer a última ação.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1606

### release()

> **release**(): `void`

Desfaz vinculos do DataUnit. Chamado quando o DU não é mais necessário.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:106

### releaseCallbacks()

> **releaseCallbacks**(): `void`

Remove callbacks registrados internamente no dataunit, é util para evitar memory leak em cenários onde o dataunit é reaproveitado em cache.

Callbacks que são liberados:

  * Filters Providers
  * Interceptors
  * Observers
  * Sorting Providers

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:126

### reloadCurrentRecord()

> **reloadCurrentRecord**(): `Promise`<`Record`[]>

Recarrega registro selecionado com dados atualizados do servidor.

#### Returns

`Promise`<`Record`[]>

  * Dados atualizados do registro selecionado.

#### Source

src/dataunit/DataUnit.ts:1763

### removeChildDataunit()

> **removeChildDataunit**(`name`): `void`

Remove um dataunit filho.

#### Parameters

• **name** : `string`

Nome do dataunit filho.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1714

### removeFilterProvider()

> **removeFilterProvider**(`provider`): `boolean`

Remove um FilterProvider.

#### Parameters

• **provider** : `FilterProvider`

FilterProvider que será removido.

#### Returns

`boolean`

#### Source

src/dataunit/DataUnit.ts:790

### removeInterceptor()

> **removeInterceptor**(`interceptor`): `void`

Remove um interceptor da lista de interceptors.

#### Parameters

• **interceptor** : `DUActionInterceptor`

Interceptor a ser removido.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:768

### removeRecords()

> **removeRecords**(`recordIds`, `cachedRecords`, `buffered`, `executionCtx`?, `silent`?): `Promise`<`string`[]>

Efetua requisição para remoção dos registros.

#### Parameters

• **recordIds** : `string`[]

Lista de IDs dos registros que serão removidos.

• **cachedRecords** : `Record`[]

Dados dos registros que serão removidos.

• **buffered** : `boolean`= `false`

Se será utilizado buffer na solicitação.

• **executionCtx?** : `ExecutionContext`

Contexto de execução da remoção do registro do DataUnit.

• **silent?** : `boolean`= `false`

Define se haverá mensagem de confirmação da remoção

#### Returns

`Promise`<`string`[]>

  * ID's dos registros removidos.

#### Source

src/dataunit/DataUnit.ts:653

### removeSelectedRecords()

> **removeSelectedRecords**(`buffered`, `silent`): `Promise`<`string`[]>

Remove o registro selecionado.

#### Parameters

• **buffered** : `boolean`= `false`

Se será utilizado buffer na solicitação.

• **silent** : `boolean`= `false`

Define se haverá mensagem de confirmação da remoção

#### Returns

`Promise`<`string`[]>

  * ID's dos registros removidos.

#### Source

src/dataunit/DataUnit.ts:624

### requestSelectFirst()

> `private` **requestSelectFirst**(`executionCtx`?): `void`

#### Parameters

• **executionCtx?** : `ExecutionContext`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:329

### saveData()

> **saveData**(`executionCtx`?): `Promise`<`void`>

Salva o estado do registro do DataUnit.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da persistencia do registro do DataUnit.

#### Returns

`Promise`<`void`>

  * Resposta da solicitação.

#### Source

src/dataunit/DataUnit.ts:515

### savingCanceled()

> **savingCanceled**(`fields`, `recordId`): `void`

Cancela o saving exibindo os campos invalidos.

#### Parameters

• **fields** : `object`[]

• **recordId** : `string`

Indica qual registro está com os campos inválido.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1124

### selectAllRecords()

> **selectAllRecords**(): `Promise`<`undefined` | `SelectionInfo`>

Seleciona todos os registros da página.

#### Returns

`Promise`<`undefined` | `SelectionInfo`>

  * Informações sobre a seleção.

#### Source

src/dataunit/DataUnit.ts:1289

### selectFirst()

> **selectFirst**(`executionCtx`?): `void`

Seleciona o primeiro registro.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção do registro do DataUnit.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1191

### selectLast()

> **selectLast**(`executionCtx`?): `void`

Seleciona o último registro.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção do registro do DataUnit.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1204

### setFieldValue()

> **setFieldValue**(`fieldName`, `newValue`, `records`?, `options`?): `Promise`<`boolean`>

Insere valor no campo desejado.

#### Parameters

• **fieldName** : `string`

Identificador do campo a ser modificado.

• **newValue** : `any`

Valor a ser inserido no campo.

• **records?** : `string`[]

Indica quais registros foram afetados pela alteração no valor do campo.

• **options?** : `DataUnitEventOptions`

Configurações do evento

#### Returns

`Promise`<`boolean`>

  * Promise que será resolvida quando o novo valor for persistido no state.

#### Source

src/dataunit/DataUnit.ts:1059

### setInvalidField()

> **setInvalidField**(`fieldName`, `message`, `recordId`): `void`

Marca campos como inválidos.

#### Parameters

• **fieldName** : `string`

Nome do campo inválido.

• **message** : `string`

Mensagem descrevendo o motivo da invalidade.

• **recordId** : `string`

Indica qual registro está com o campo inválido.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1112

### setRecordsKeepingSelection()

> **setRecordsKeepingSelection**(`records`): `void`

Define a propriedade records da instância da classe com um novo valor e chama o método dispatchAction para notificar os observers da aplicação sobre a mudança, mantendo a seleção definida anteriormente.

#### Parameters

• **records** : `Record`[]

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:879

### setSelection()

> **setSelection**(`selection`, `executionCtx`?): `Promise`<`SelectionInfo`>

Seleciona múltiplos registros por ID ou todos os registros (multipágina) .

#### Parameters

• **selection** : `string`[] | `ALL_RECORDS`

IDs para selecionar ou o modo de seleção completo.

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção dos registros do DataUnit.

#### Returns

`Promise`<`SelectionInfo`>

#### Source

src/dataunit/DataUnit.ts:1231

### setSelectionByIndex()

> **setSelectionByIndex**(`selection`, `executionCtx`?): `void`

Seleciona múltiplos registros por índice.

#### Parameters

• **selection** : `number`[]

Índices desejados para a seleção.

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção do registro do DataUnit.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1218

### setWaitingToReload()

> **setWaitingToReload**(`isWaiting`): `void`

Define se o dataUnit tem um recarregamento pendente.

#### Parameters

• **isWaiting** : `boolean`

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:173

### showField()

> **showField**(`fieldName`): `void`

Deixa um campo do DataUnit visível

#### Parameters

• **fieldName** : `string`

nome do campo para ficar visível.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1907

### startChange()

> **startChange**(`fieldName`, `waitingChange`): `void`

Inicia alteração no campo.

#### Parameters

• **fieldName** : `string`

Identificador do campo a ser modificado.

• **waitingChange** : `WaitingChange`

Informa que uma mudança irá iniciar.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1160

### subscribe()

> **subscribe**(`observer`, `uuid`?): `string`

Adiciona um novo observer no DataUnit. Ela vai ser chamada sempre que uma ação for despachada (dispatchAction()).

#### Parameters

• **observer**

Função que recebe como parâmetro as ações que serão monitoradas.

• **uuid?** : `string`

Identificador do observer. Quando não informado, será gerado um identificador aleatório.

#### Returns

`string`

#### Source

src/dataunit/DataUnit.ts:1726

### toString()

> **toString**(): `string`

Obtém a representação textual do DataUnit, nesse caso, o nome do DataUnit.

#### Returns

`string`

  * Valor contido na propriedade name.

#### Source

src/dataunit/DataUnit.ts:1617

### unSelectAllRecords()

> **unSelectAllRecords**(): `Promise`<`undefined` | `SelectionInfo`>

Desseleciona todos os registros da página.

#### Returns

`Promise`<`undefined` | `SelectionInfo`>

  * Informações sobre a seleção.

#### Source

src/dataunit/DataUnit.ts:1298

### undo()

> **undo**(`executionCtx`?): `void`

Desfaz a última ação.

#### Parameters

• **executionCtx?** : `ExecutionContext`

Contexto de execução de desfazer a última ação.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1595

### unsubscribe()

> **unsubscribe**(`observer`, `uuid`?): `void`

Remove um observer existente.

#### Parameters

• **observer** : `Function`

Observer que se deseja remover.

• **uuid?** : `string`

Identificador do observer. Quando não informado o delete removera com base no equals do observer.

#### Returns

`void`

#### Source

src/dataunit/DataUnit.ts:1744

### updatePageSelection()

> **updatePageSelection**(`selection`?, `executionCtx`?): `Promise`<`undefined` | `SelectionInfo`>

Atualiza a seleção dos registros atuais.

#### Parameters

• **selection?** : `string`[]

IDs dos registros selecionados no snapshot atual

• **executionCtx?** : `ExecutionContext`

Contexto de execução da seleção dos registros do DataUnit.

#### Returns

`Promise`<`undefined` | `SelectionInfo`>

  * Informações sobre a seleção.

#### Source

src/dataunit/DataUnit.ts:1257

### updatePageSelectionAll()

> `private` **updatePageSelectionAll**(`addRecords`): `Promise`<`undefined` | `SelectionInfo`>

#### Parameters

• **addRecords** : `boolean`

#### Returns

`Promise`<`undefined` | `SelectionInfo`>

#### Source

src/dataunit/DataUnit.ts:1269

### updatePagination()

> **updatePagination**(`info`): `Promise`<`boolean`>

Obtém informações de paginação dos registros.

#### Parameters

• **info** : `PaginationInfo`

#### Returns

`Promise`<`boolean`>

  * Informações da paginação de registros.

#### Source

src/dataunit/DataUnit.ts:810

### validateAndTypeValue()

> `private` **validateAndTypeValue**(`fieldName`, `newValue`): `any`

Obtém o valor convertido de acordo com o tipo do campo.

#### Parameters

• **fieldName** : `string`

Identificador do campo.

• **newValue** : `any`

Novo valor que será atribuído ao campo pós validação.

#### Returns

`any`

  * Novo valor convertido em um tipo valido.

#### Source

src/dataunit/DataUnit.ts:227

### valueFromString()

> **valueFromString**(`fieldName`, `value`): `any`

Obtém o valor do campo em seu formato/tipo correto a partir de uma string.

#### Parameters

• **fieldName** : `string`

Nome do campo que terá o tipo identificado para conversão.

• **value** : `string`

Texto que será convertido de acordo com o tipo identificado no campo.

#### Returns

`any`

  * Valor convertido ou ele mesmo.

#### Source

src/dataunit/DataUnit.ts:702

### valueToString()

> **valueToString**(`fieldName`, `value`): `string`

Converte o valor informado para texto de acordo com o tipo do campo informado.

#### Parameters

• **fieldName** : `string`

Nome do campo utilizado para buscar o tipo de dado com o padrão de conversão para string.

• **value** : `any`

Valor a ser convertido.

#### Returns

`string`

  * Valor informado convertido.

#### Source

src/dataunit/DataUnit.ts:717

### waitingForChange()

> **waitingForChange**(`fieldName`): `boolean`

Retorna se a alteração no campo já foi concluída ou se ainda está incompleta.

#### Parameters

• **fieldName** : `string`

Identificador do campo a ser verificado.

#### Returns

`boolean`

  * Verdadeiro se ainda está pendente.

#### Source

src/dataunit/DataUnit.ts:1031
