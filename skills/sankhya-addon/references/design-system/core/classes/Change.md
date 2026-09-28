> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/Change (snapshot 2026-09-28)

# Change

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / Change

# Class: Change

`Change`: Dados que representam uma alteração.

## Constructors

### new Change()

> **new Change**(`dataUnit`, `record`, `updates`, `operation`, `sourceId`?): `Change`

#### Parameters

• **dataUnit** : `string`

• **record** : `Record`

• **updates** : `any`

• **operation** : `ChangeOperation`

• **sourceId?** : `string`

#### Returns

`Change`

#### Source

src/dataunit/Changes.ts:15

## Properties

### _operation

> `private` **_operation** : `ChangeOperation`

#### Source

src/dataunit/Changes.ts:13

### dataUnit

> **dataUnit** : `string`

#### Source

src/dataunit/Changes.ts:8

### record

> **record** : `Record`

#### Source

src/dataunit/Changes.ts:9

### sourceId

> **sourceId** : `undefined` | `string`

#### Source

src/dataunit/Changes.ts:10

### updatingFields

> **updatingFields** : `any`

#### Source

src/dataunit/Changes.ts:11

## Accessors

### operation

> `get` **operation**(): `string`

Obtém o tipo de operação que está sendo realizada.

#### Returns

`string`

  * Ação que está sendo executada.

#### Source

src/dataunit/Changes.ts:30

## Methods

### isCopy()

> **isCopy**(): `boolean`

Retorna se o DataUnit está em uma operação de cópia.

#### Returns

`boolean`

  * Verdadeiro se a operação for de cópia.

#### Source

src/dataunit/Changes.ts:52

### isDelete()

> **isDelete**(): `boolean`

Retorna se o DataUnit está em uma operação de deleção.

#### Returns

`boolean`

  * Verdadeiro se a operação for de deleção.

#### Source

src/dataunit/Changes.ts:63

### isInsert()

> **isInsert**(): `boolean`

Retorna se o DataUnit está em uma operação de inserção.

#### Returns

`boolean`

  * Verdadeiro se a operação for de inserção.

#### Source

src/dataunit/Changes.ts:41

### isUpdate()

> **isUpdate**(): `boolean`

Retorna se o DataUnit está em uma operação de atualização.

#### Returns

`boolean`

  * Verdadeiro se a operação for de atualização.

#### Source

src/dataunit/Changes.ts:74
