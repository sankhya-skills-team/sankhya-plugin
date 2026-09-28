> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitInMemoryLoader (snapshot 2026-09-28)

# DataUnitInMemoryLoader

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / DataUnitInMemoryLoader

# Class: DataUnitInMemoryLoader

## Constructors

### new DataUnitInMemoryLoader()

> **new DataUnitInMemoryLoader**(`metadata`?, `records`?, `config`?): `DataUnitInMemoryLoader`

#### Parameters

• **metadata?** : `UnitMetadata`

• **records?** : `Record`[]

• **config?** : `DataUnitInMemoryLoaderConfig`

#### Returns

`DataUnitInMemoryLoader`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:26

## Properties

### _dataUnit

> `private` **_dataUnit** : `DataUnit`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:19

### _initialRecords

> `private` **_initialRecords** : `Record`[] = `[]`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:21

### _metadata

> `private` **_metadata** : `undefined` | `UnitMetadata`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:20

### recordDateFormat

> `private` **recordDateFormat** : `RECORD_DATE_FORMAT`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:22

### DEFAULT_PAGE_SIZE

> `static` `readonly` **DEFAULT_PAGE_SIZE** : `150` = `150`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:24

### IN_MEMORY_DATA_UNIT_NAME

> `static` `readonly` **IN_MEMORY_DATA_UNIT_NAME** : `"InMemoryDataUnit"` = `'InMemoryDataUnit'`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:23

## Accessors

### dataUnit

> `get` **dataUnit**(): `DataUnit`

#### Returns

`DataUnit`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:58

### metadata

> `get` **metadata**(): `UnitMetadata`

> `set` **metadata**(`metadata`): `void`

#### Parameters

• **metadata** : `UnitMetadata`

#### Returns

`UnitMetadata`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:122

### records

> `get` **records**(): `Record`[]

> `set` **records**(`records`): `void`

#### Parameters

• **records** : `Record`[]

#### Returns

`Record`[]

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:62

## Methods

### buildColumns()

> `private` **buildColumns**(): `undefined` | `Map`<`string`, `FieldDescriptor`>

#### Returns

`undefined` | `Map`<`string`, `FieldDescriptor`>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:92

### buildInitialRecords()

> `private` **buildInitialRecords**(`records`, `columns`): `Record`[]

#### Parameters

• **records** : `Record`[]

• **columns** : `undefined` | `Map`<`string`, `FieldDescriptor`>

#### Returns

`Record`[]

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:98

### generateUniqueId()

> `private` **generateUniqueId**(): `string`

#### Returns

`string`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:134

### getRecordsToLoad()

> `private` **getRecordsToLoad**(): `Record`[]

#### Returns

`Record`[]

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:46

### inMemoryLoader()

> `private` **inMemoryLoader**(`dataUnit`, `request`, `recordsIn`): `Promise`<`LoadDataResponse`>

#### Parameters

• **dataUnit** : `DataUnit`

• **request** : `LoadDataRequest`

• **recordsIn** : `Record`[]

#### Returns

`Promise`<`LoadDataResponse`>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:138

### metadaLoader()

> `private` **metadaLoader**(): `Promise`<`UnitMetadata`>

#### Returns

`Promise`<`UnitMetadata`>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:142

### removeLoader()

> **removeLoader**(`_dataUnit`, `recordIds`): `Promise`<`string`[]>

#### Parameters

• **_dataUnit** : `DataUnit`

• **recordIds** : `string`[]

#### Returns

`Promise`<`string`[]>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:173

### saveLoader()

> `private` **saveLoader**(`_dataUnit`, `changes`): `Promise`<`SavedRecord`[]>

#### Parameters

• **_dataUnit** : `DataUnit`

• **changes** : `Change`[]

#### Returns

`Promise`<`SavedRecord`[]>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:146

### getConvertedValue()

> `static` **getConvertedValue**(`descriptor`, `strValue`, `dateFormat`?): `any`

#### Parameters

• **descriptor** : `FieldDescriptor`

• **strValue** : `string`

• **dateFormat?** : `RECORD_DATE_FORMAT`

#### Returns

`any`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:77
