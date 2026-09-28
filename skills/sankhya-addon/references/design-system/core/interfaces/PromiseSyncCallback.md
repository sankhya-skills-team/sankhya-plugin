> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PromiseSyncCallback (snapshot 2026-09-28)

# PromiseSyncCallback

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / PromiseSyncCallback

# Interface: PromiseSyncCallback<T>

Representa o callback de um sincronizador `PromiseSync<T>`.

## Type parameters

• **T**

## Methods

### resolve()

> **resolve**(`result`): `void`

Será chamado sempre que todas as promessas adicionadas finalizarem.

#### Parameters

• **result** : `PromiseSettledResult`<`Awaited`<`T`>>[]

A lista com o resultado de todas as promises aguardadas.

#### Returns

`void`

#### Source

src/async/PromiseSync.ts:48
