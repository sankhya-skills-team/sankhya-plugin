> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/LockManager (snapshot 2026-09-28)

# LockManager

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / LockManager

# Class: LockManager

## Constructors

### new LockManager()

> **new LockManager**(): `LockManager`

#### Returns

`LockManager`

## Properties

### ATTRIBUTE_NAME

> `static` **ATTRIBUTE_NAME** : `string` = `"data-locker-manger-context-id"`

Nome do atributo que será utilizado para controlar contexto de locks nos elementos da DOM.

#### Source

src/utils/LockManager.ts:28

### _locks

> `static` `private` **_locks** : `Map`<`string`, `Lock`[]>

#### Source

src/utils/LockManager.ts:23

## Methods

### addLockManagerCtxId()

> `static` **addLockManagerCtxId**(`startElement`): `string`

Cria um contexto de locker, caso nao exista, para todos elementos pais iniciados com ez- ou snk-.

#### Parameters

• **startElement** : `HTMLElement`

Elemento de de onde o lock deve começar.

#### Returns

`string`

  * O id do locker, que pode ser usado para iniciar ou aguardar um lock do contexto.

#### Source

src/utils/LockManager.ts:87

### buildContextID()

> `static` `private` **buildContextID**(): `string`

#### Returns

`string`

#### Source

src/utils/LockManager.ts:30

### buildLockerID()

> `static` `private` **buildLockerID**(`ctxId`, `operation`): `undefined` | `string`

#### Parameters

• **ctxId** : `string` | `HTMLElement`

• **operation** : `LockManagerOperation`

#### Returns

`undefined` | `string`

#### Source

src/utils/LockManager.ts:34

### findExistingCtxId()

> `static` `private` **findExistingCtxId**(`element`): `null` | `string`

#### Parameters

• **element** : `HTMLElement`

#### Returns

`null` | `string`

#### Source

src/utils/LockManager.ts:47

### lock()

> `static` **lock**(`id`, `operation`): () => `void`

Inicia um locker baseado em um contexto e uma operação.

#### Parameters

• **id** : `string` | `HTMLElement`

Pode ser um ID do contexto de locker, ou, o elemento contendo um contexto de locker.

• **operation** : `LockManagerOperation`

Operação do contexto que o lock deve ser feito.

#### Returns

`Function`

  * Uma função que fara a liberação do lock.

##### Returns

`void`

#### Source

src/utils/LockManager.ts:136

### resetLocks()

> `static` **resetLocks**(`id`, `operation`): `Promise`<`void`>

Reseta todos os locks existentes para um determinado contexto e operação de forma assíncrona

#### Parameters

• **id** : `string` | `HTMLElement`

ID do contexto ou elemento HTML contendo contexto

• **operation** : `LockManagerOperation`

Operação específica para resetar os locks

#### Returns

`Promise`<`void`>

Promise que será resolvida quando todos os locks forem resetados

#### Source

src/utils/LockManager.ts:110

### traverseAndAddAttr()

> `static` `private` **traverseAndAddAttr**(`element`, `ctxId`): `void`

#### Parameters

• **element** : `HTMLElement`

• **ctxId** : `string`

#### Returns

`void`

#### Source

src/utils/LockManager.ts:69

### whenHasLock()

> `static` **whenHasLock**(`id`, `operation`, `timeOut`?): `Promise`<`void`>

#### Parameters

• **id** : `string` | `HTMLElement`

• **operation** : `LockManagerOperation`

• **timeOut?** : `number`

#### Returns

`Promise`<`void`>

#### Source

src/utils/LockManager.ts:190

### whenResolve()

> `static` **whenResolve**(`id`, `operation`, `debounce`?, `timeOut`?): `Promise`<`void`>

Aguarda todos os lockers de um contexto e operação serem resolvidos.

#### Parameters

• **id** : `string` | `HTMLElement`

Pode ser um ID do contexto de locker, ou, o elemento contendo um contexto de locker.

• **operation** : `LockManagerOperation`

Operação do contexto que devera aguardar.

• **debounce?** : `number`

• **timeOut?** : `number`

#### Returns

`Promise`<`void`>

  * Promise que será resolvida quando todos lockers forem finalizados.

#### Source

src/utils/LockManager.ts:163
