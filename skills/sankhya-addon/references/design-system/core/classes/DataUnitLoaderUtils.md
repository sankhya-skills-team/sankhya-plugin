> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitLoaderUtils (snapshot 2026-09-28)

# DataUnitLoaderUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / DataUnitLoaderUtils

# Class: DataUnitLoaderUtils

## Constructors

### new DataUnitLoaderUtils()

> **new DataUnitLoaderUtils**(): `DataUnitLoaderUtils`

#### Returns

`DataUnitLoaderUtils`

## Methods

### applyFilter()

> `static` **applyFilter**(`records`, `dataUnit`, `filters`): `Record`[]

#### Parameters

• **records** : `Record`[]

• **dataUnit** : `DataUnit`

• **filters** : `Filter`[]

#### Returns

`Record`[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:12

### applySorting()

> `static` **applySorting**(`records`, `dataUnit`, `sorting`): `Record`[]

#### Parameters

• **records** : `Record`[]

• **dataUnit** : `DataUnit`

• **sorting** : `Sort`[]

#### Returns

`Record`[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:41

### buildLoadDataResponse()

> `static` **buildLoadDataResponse**(`recordsIn`, `dataUnit`, `request`): `Promise`<`object`>

#### Parameters

• **recordsIn** : `Record`[]

• **dataUnit** : `DataUnit`

• **request** : `LoadDataRequest`

#### Returns

`Promise`<`object`>

##### paginationInfo

> **paginationInfo** : `undefined` | `PaginationInfo`

##### records

> **records** : `Record`[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:21

### buildPaginationInfo()

> `static` **buildPaginationInfo**(`__namedParameters`): `undefined` | `PaginationInfo`

#### Parameters

• **__namedParameters** : `PaginationInfoBuilderParams`

#### Returns

`undefined` | `PaginationInfo`

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:62

### getPagesByRecords()

> `static` **getPagesByRecords**(`records`, `offset`, `limit`): `Record`[]

#### Parameters

• **records** : `Record`[]

• **offset** : `number`= `0`

• **limit** : `number`= `0`

#### Returns

`Record`[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:52

### hasValidLimitAndOffset()

> `static` `private` **hasValidLimitAndOffset**(`offset`, `limit`): `boolean`

#### Parameters

• **offset** : `number`

• **limit** : `number`

#### Returns

`boolean`

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:58
