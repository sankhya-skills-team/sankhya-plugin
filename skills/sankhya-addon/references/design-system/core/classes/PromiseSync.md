> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/PromiseSync (snapshot 2026-09-28)

# PromiseSync

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / PromiseSync

# Class: PromiseSync<T>

O intuito desta classe é organizar a finalização de várias promessas executando determinada ação (callback) com o resultado.

## Type parameters

• **T**

## Constructors

### new PromiseSync()

> **new PromiseSync** <`T`>(`callBack`): `PromiseSync`<`T`>

#### Parameters

• **callBack** : `PromiseSyncCallback`<`T`>

#### Returns

`PromiseSync`<`T`>

#### Source

src/async/PromiseSync.ts:13

## Properties

### _callBack

> **_callBack** : `PromiseSyncCallback`<`T`>

#### Source

src/async/PromiseSync.ts:8

### _promises

> **_promises** : `Promise`<`T`>[]

#### Source

src/async/PromiseSync.ts:7

## Methods

### add()

> **add**(`promise`): `void`

Adiciona na lista de promises pendentes. Isso faz com que criemos uma nova espera.

#### Parameters

• **promise** : `Promise`<`T`>

Entrará na lista aguardada.

#### Returns

`void`

#### Source

src/async/PromiseSync.ts:23
