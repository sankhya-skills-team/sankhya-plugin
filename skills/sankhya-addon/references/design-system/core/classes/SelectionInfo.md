> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/SelectionInfo (snapshot 2026-09-28)

# SelectionInfo

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / SelectionInfo

# Class: SelectionInfo

## Constructors

### new SelectionInfo()

> **new SelectionInfo**(`records`, `mode`, `total`?, `filters`?, `sort`?): `SelectionInfo`

#### Parameters

• **records** : `Record`[]

• **mode** : `SelectionMode`= `SelectionMode.SOME_RECORDS`

• **total?** : `number`

• **filters?** : `Filter`[]

• **sort?** : `Sort`[]

#### Returns

`SelectionInfo`

#### Source

src/dataunit/SelectionInfo.ts:13

## Properties

### _records

> `private` **_records** : `Record`[]

#### Source

src/dataunit/SelectionInfo.ts:10

### _total?

> `private` `optional` **_total** : `number`

#### Source

src/dataunit/SelectionInfo.ts:11

### filters?

> `optional` **filters** : `Filter`[]

#### Source

src/dataunit/SelectionInfo.ts:7

### getAllRecords()?

> `optional` **getAllRecords** : () => `Record`[]

#### Returns

`Record`[]

#### Source

src/dataunit/SelectionInfo.ts:9

### mode

> **mode** : `SelectionMode`

#### Source

src/dataunit/SelectionInfo.ts:6

### sort?

> `optional` **sort** : `Sort`[]

#### Source

src/dataunit/SelectionInfo.ts:8

## Accessors

### length

> `get` **length**(): `number`

#### Returns

`number`

#### Source

src/dataunit/SelectionInfo.ts:41

### recordIds

> `get` **recordIds**(): `undefined` | `string`[]

#### Returns

`undefined` | `string`[]

#### Source

src/dataunit/SelectionInfo.ts:31

### records

> `get` **records**(): `Record`[]

#### Returns

`Record`[]

#### Source

src/dataunit/SelectionInfo.ts:21

## Methods

### isAllRecords()

> **isAllRecords**(): `boolean`

#### Returns

`boolean`

#### Source

src/dataunit/SelectionInfo.ts:48

### isEmpty()

> **isEmpty**(): `boolean`

#### Returns

`boolean`

#### Source

src/dataunit/SelectionInfo.ts:52
