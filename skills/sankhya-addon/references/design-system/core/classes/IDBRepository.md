> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/IDBRepository (snapshot 2026-09-28)

# IDBRepository

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / IDBRepository

# Class: IDBRepository<T>

Abstração para simplificar o uso do indexed DB

Além de facilitar os comandos de incluir, remover alterar e obter objetos, esse repositório preserva a ordem de inserção na lista, além de permitir filtros e ordenações compostas (impossíveis com uso de índices).

## Type parameters

• **T**

## Implements

  * `IRepository`<`T`>

## Constructors

### new IDBRepository()

> **new IDBRepository** <`T`>(`dbName`, `dbVersion`, `storeName`, `indexKeyPath`, `indexes`?): `IDBRepository`<`T`>

Construtor padrão

#### Parameters

• **dbName** : `string`

Nome do DB

• **dbVersion** : `number`

Versão do DB

• **storeName** : `string`

Nome da store

• **indexKeyPath** : `string`

Um atributo que identifique os objetos guardados

• **indexes?** : `IRepositoryIndex`[]

#### Returns

`IDBRepository`<`T`>

#### Source

src/repository/indexeddb/IDBRepository.ts:35

## Properties

### _addedStoreName

> `private` **_addedStoreName** : `string`

#### Source

src/repository/indexeddb/IDBRepository.ts:21

### _db?

> `private` `optional` **_db** : `IDBPDatabase`<`unknown`>

#### Source

src/repository/indexeddb/IDBRepository.ts:24

### _dbName

> `private` **_dbName** : `string`

#### Source

src/repository/indexeddb/IDBRepository.ts:18

### _dbVersion

> `private` **_dbVersion** : `number`

#### Source

src/repository/indexeddb/IDBRepository.ts:19

### _indexKeyPath

> `private` **_indexKeyPath** : `string`

#### Source

src/repository/indexeddb/IDBRepository.ts:22

### _indexes?

> `private` `optional` **_indexes** : `IRepositoryIndex`[]

#### Source

src/repository/indexeddb/IDBRepository.ts:23

### _operating

> `private` **_operating** : `boolean` = `true`

#### Source

src/repository/indexeddb/IDBRepository.ts:25

### _storeName

> `private` **_storeName** : `string`

#### Source

src/repository/indexeddb/IDBRepository.ts:20

## Methods

### clear()

> **clear**(): `Promise`<`void`>

Limpa todo o repositório

#### Returns

`Promise`<`void`>

Promessa de execução

#### Implementation of

`IRepository`.`clear`

#### Source

src/repository/indexeddb/IDBRepository.ts:123

### count()

> **count**(): `Promise`<`number`>

Conta os itens do repositório

#### Returns

`Promise`<`number`>

Promessa de quantidade

#### Implementation of

`IRepository`.`count`

#### Source

src/repository/indexeddb/IDBRepository.ts:236

### createStore()

> `private` **createStore**(`db`, `name`, `indexPrefix`): `void`

#### Parameters

• **db** : `IDBPDatabase`<`unknown`>

• **name** : `string`

• **indexPrefix** : `string`= `""`

#### Returns

`void`

#### Source

src/repository/indexeddb/IDBRepository.ts:271

### delete()

> **delete**(`items`): `Promise`<`void`>

Remove itens do repositório

#### Parameters

• **items** : `T`[]

Os itens a serem removidos

#### Returns

`Promise`<`void`>

Promessa de execução

#### Implementation of

`IRepository`.`delete`

#### Source

src/repository/indexeddb/IDBRepository.ts:138

### distict()

> **distict**(`itemProcessor`): `Promise`<`Map`<`string`, `any`>>

Itera todos os items colecionando os valores distintos.

#### Parameters

• **itemProcessor**

Uma função que processa um item e gera a chave e valor

#### Returns

`Promise`<`Map`<`string`, `any`>>

Promessa de array com os valores distintos.

#### Implementation of

`IRepository`.`distict`

#### Source

src/repository/indexeddb/IDBRepository.ts:78

### getAddedItems()

> `private` **getAddedItems**(`db`): `Promise`<`IAddedItem`<`T`>[]>

#### Parameters

• **db** : `IDBPDatabase`<`unknown`>

#### Returns

`Promise`<`IAddedItem`<`T`>[]>

#### Source

src/repository/indexeddb/IDBRepository.ts:319

### getFromCache()

> **getFromCache**(): `undefined` | `T`[]

Retorna todos os registros que estão em cache no momento

#### Returns

`undefined` | `T`[]

Todos registros que estão em cache no momento

#### Implementation of

`IRepository`.`getFromCache`

#### Source

src/repository/indexeddb/IDBRepository.ts:324

### getItemPosition()

> `private` **getItemPosition**(`db`, `itemTest`): `Promise`<`number`>

#### Parameters

• **db** : `IDBPDatabase`<`unknown`>

• **itemTest**

#### Returns

`Promise`<`number`>

#### Source

src/repository/indexeddb/IDBRepository.ts:284

### getItemPositionByAdded()

> `private` **getItemPositionByAdded**(`db`, `itemTest`): `Promise`<`number`>

#### Parameters

• **db** : `IDBPDatabase`<`unknown`>

• **itemTest**

#### Returns

`Promise`<`number`>

#### Source

src/repository/indexeddb/IDBRepository.ts:307

### insert()

> **insert**(`itemReference`, `items`): `Promise`<`void`>

Insere itens em uma posição de referência

#### Parameters

• **itemReference** : `T`

O item posterior aos inseridos

• **items** : `T`[]

Os itens a serem inseridos

#### Returns

`Promise`<`void`>

Promessa de execução

#### Implementation of

`IRepository`.`insert`

#### Source

src/repository/indexeddb/IDBRepository.ts:194

### isEmpty()

> **isEmpty**(): `Promise`<`boolean`>

Determina se o repositório está vazio ou ainda não foi criado.

#### Returns

`Promise`<`boolean`>

#### Implementation of

`IRepository`.`isEmpty`

#### Source

src/repository/indexeddb/IDBRepository.ts:218

### isOperating()

> **isOperating**(): `boolean`

Determina se o repositório está em condições normais de funcionamento. Caso o banco tenha sido excluido, retorna false.

#### Returns

`boolean`

#### Implementation of

`IRepository`.`isOperating`

#### Source

src/repository/indexeddb/IDBRepository.ts:214

### load()

> **load**(`filterFunction`?, `sortingFunction`?, `offset`?, `limit`?): `Promise`<`ILoadResult`<`T`>>

Recupera registros do repositório

#### Parameters

• **filterFunction?**

Teste para determinar se um registro está no universo desejado

• **sortingFunction?**

Critério comparação para ordenação

• **offset?** : `number`

Determina que o resultado descarta os registros iniciais

• **limit?** : `number`

Descarta o resultado a partir de uma quantidade de registros

#### Returns

`Promise`<`ILoadResult`<`T`>>

Promessa de um array que satisfaça aos critérios informados

#### Implementation of

`IRepository`.`load`

#### Source

src/repository/indexeddb/IDBRepository.ts:44

### openDB()

> `private` **openDB**(): `Promise`<`IDBPDatabase`<`unknown`>>

#### Returns

`Promise`<`IDBPDatabase`<`unknown`>>

#### Source

src/repository/indexeddb/IDBRepository.ts:250

### push()

> **push**(`items`): `Promise`<`void`>

Adiciona registros no final do repositório

#### Parameters

• **items** : `T`[]

Os items a serem adicionados

#### Returns

`Promise`<`void`>

Promessa de execução

#### Implementation of

`IRepository`.`push`

#### Source

src/repository/indexeddb/IDBRepository.ts:103

### update()

> **update**(`items`): `Promise`<`void`>

Altera itens já persistido no repositório

#### Parameters

• **items** : `T`[]

Os itens a serem alterados

#### Returns

`Promise`<`void`>

Promessa de execução

#### Implementation of

`IRepository`.`update`

#### Source

src/repository/indexeddb/IDBRepository.ts:165
