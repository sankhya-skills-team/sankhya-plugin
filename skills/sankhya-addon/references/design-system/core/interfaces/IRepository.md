> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/IRepository (snapshot 2026-09-28)

# IRepository

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / IRepository

# Interface: IRepository<T>

## Type parameters

• **T**

## Methods

### clear()

> **clear**(): `Promise`<`void`>

Limpa todo o repositório

#### Returns

`Promise`<`void`>

Promessa de execução

#### Source

src/repository/IRepository.ts:38

### count()

> **count**(): `Promise`<`number`>

Conta os itens do repositório

#### Returns

`Promise`<`number`>

Promessa de quantidade

#### Source

src/repository/IRepository.ts:81

### delete()

> **delete**(`items`): `Promise`<`void`>

Remove itens do repositório

#### Parameters

• **items** : `T`[]

Os itens a serem removidos

#### Returns

`Promise`<`void`>

Promessa de execução

#### Source

src/repository/IRepository.ts:46

### distict()

> **distict**(`itemProcessor`): `Promise`<`Map`<`string`, `any`>>

Itera todos os items colecionando os valores distintos.

#### Parameters

• **itemProcessor**

Uma função que processa um item e gera a chave e valor

#### Returns

`Promise`<`Map`<`string`, `any`>>

Promessa de array com os valores distintos.

#### Source

src/repository/IRepository.ts:23

### getFromCache()

> **getFromCache**(): `undefined` | `T`[]

Retorna todos os registros que estão em cache no momento

#### Returns

`undefined` | `T`[]

Todos registros que estão em cache no momento

#### Source

src/repository/IRepository.ts:88

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

#### Source

src/repository/IRepository.ts:63

### isEmpty()

> **isEmpty**(): `Promise`<`boolean`>

Determina se o repositório está vazio ou ainda não foi criado.

#### Returns

`Promise`<`boolean`>

#### Source

src/repository/IRepository.ts:74

### isOperating()

> **isOperating**(): `boolean`

Determina se o repositório está em condições normais de funcionamento. Caso o banco tenha sido excluido, retorna false.

#### Returns

`boolean`

#### Source

src/repository/IRepository.ts:69

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

#### Source

src/repository/IRepository.ts:14

### push()

> **push**(`items`): `Promise`<`void`>

Adiciona registros no final do repositório

#### Parameters

• **items** : `T`[]

Os items a serem adicionados

#### Returns

`Promise`<`void`>

Promessa de execução

#### Source

src/repository/IRepository.ts:31

### update()

> **update**(`items`): `Promise`<`void`>

Altera itens já persistido no repositório

#### Parameters

• **items** : `T`[]

Os itens a serem alterados

#### Returns

`Promise`<`void`>

Promessa de execução

#### Source

src/repository/IRepository.ts:54
