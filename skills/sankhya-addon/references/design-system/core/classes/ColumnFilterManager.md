> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ColumnFilterManager (snapshot 2026-09-28)

# ColumnFilterManager

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ColumnFilterManager

# Class: ColumnFilterManager

## Constructors

### new ColumnFilterManager()

> **new ColumnFilterManager**(): `ColumnFilterManager`

#### Returns

`ColumnFilterManager`

## Methods

### compileDistinct()

> `static` **compileDistinct**(`fieldName`, `dataUnit`): `IMultiSelectionOption`[]

#### Parameters

• **fieldName** : `string`

• **dataUnit** : `DataUnit`

#### Returns

`IMultiSelectionOption`[]

#### Source

src/utils/ColumnFilterManager.ts:60

### compileDistinctFromArray()

> `static` **compileDistinctFromArray**(`fieldName`, `dataUnit`, `records`): `IMultiSelectionOption`[]

#### Parameters

• **fieldName** : `string`

• **dataUnit** : `DataUnit`

• **records** : `Record`[]

#### Returns

`IMultiSelectionOption`[]

#### Source

src/utils/ColumnFilterManager.ts:66

### doCompileDistinct()

> `static` `private` **doCompileDistinct**(`request`, `fieldName`, `dataUnit`, `list`): `IMultiSelectionOption`[]

#### Parameters

• **request** : `undefined` | `LoadDataRequest`

• **fieldName** : `string`

• **dataUnit** : `DataUnit`

• **list** : `Record`[]

#### Returns

`IMultiSelectionOption`[]

#### Source

src/utils/ColumnFilterManager.ts:71

### getColumnFilters()

> `static` **getColumnFilters**(`filters`, `fieldName`): `Map`<`string`, `IColumnFilter`>

#### Parameters

• **filters** : `Filter`[]

• **fieldName** : `string`

#### Returns

`Map`<`string`, `IColumnFilter`>

#### Source

src/utils/ColumnFilterManager.ts:11

### getFilterFunction()

> `static` **getFilterFunction**(`dataUnit`, `filters`?): `undefined` | (`record`) => `boolean`

#### Parameters

• **dataUnit** : `DataUnit`

• **filters?** : `IColumnFilter`[]

#### Returns

`undefined` | (`record`) => `boolean`

#### Source

src/utils/ColumnFilterManager.ts:30

### recordMatchesFilter()

> `static` `private` **recordMatchesFilter**(`dataUnit`, `record`, `columnFilter`): `boolean`

#### Parameters

• **dataUnit** : `DataUnit`

• **record** : `Record`

• **columnFilter** : `IColumnFilter`

#### Returns

`boolean`

#### Source

src/utils/ColumnFilterManager.ts:43
