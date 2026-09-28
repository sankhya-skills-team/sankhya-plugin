> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitStorage (snapshot 2026-09-28)

# DataUnitStorage

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / DataUnitStorage

# Class: DataUnitStorage

Classe responsável por armazenar instâncias de DataUnit.

## Constructors

### new DataUnitStorage()

> **new DataUnitStorage**(): `DataUnitStorage`

#### Returns

`DataUnitStorage`

## Properties

### dataUnitMap

> `static` `private` **dataUnitMap** : `WeakMap`<`object`, `DataUnit`>

#### Type declaration

##### key

> **key** : `string`

#### Source

src/dataunit/DataUnitStorage.ts:7

### keyMap

> `static` `private` **keyMap** : `Map`<`string`, `object`>

#### Source

src/dataunit/DataUnitStorage.ts:8

## Methods

### get()

> `static` **get**(`dataUnitName`): `undefined` | `DataUnit`

Retorna uma instância de DataUnit armazenada no DataUnitStorage.

#### Parameters

• **dataUnitName** : `string`

O nome do DataUnit.

#### Returns

`undefined` | `DataUnit`

  * A instância do DataUnit ou undefined caso não seja encontrada.

#### Source

src/dataunit/DataUnitStorage.ts:15

### put()

> `static` **put**(`dataUnit`): `void`

Armazena uma instância de DataUnit no DataUnitStorage.

#### Parameters

• **dataUnit** : `DataUnit`

A instância de DataUnit a ser armazenada.

#### Returns

`void`

#### Source

src/dataunit/DataUnitStorage.ts:24

### remove()

> `static` **remove**(`dataUnit`): `void`

Remove uma instância de DataUnit do DataUnitStorage.

#### Parameters

• **dataUnit** : `string` | `DataUnit`

A instância de DataUnit ou o nome do DataUnit a ser removido.

#### Returns

`void`

#### Source

src/dataunit/DataUnitStorage.ts:34
