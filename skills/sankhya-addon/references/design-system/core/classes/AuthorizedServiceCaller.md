> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/AuthorizedServiceCaller (snapshot 2026-09-28)

# AuthorizedServiceCaller

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / AuthorizedServiceCaller

# Class: AuthorizedServiceCaller

## Constructors

### new AuthorizedServiceCaller()

> **new AuthorizedServiceCaller**(`serverURL`, `unauthorizedPath`): `AuthorizedServiceCaller`

#### Parameters

• **serverURL** : `string`

• **unauthorizedPath** : `string`

#### Returns

`AuthorizedServiceCaller`

#### Source

src/http/AuthorizedServiceCaller.ts:6

## Properties

### serverURL

> `private` **serverURL** : `string` = `"http://192.168.1.218:8503"`

#### Source

src/http/AuthorizedServiceCaller.ts:3

### unauthorizedPath

> `private` **unauthorizedPath** : `string` = `"/"`

#### Source

src/http/AuthorizedServiceCaller.ts:4

## Methods

### requestService()

> **requestService**(`request`, `callback`?): `Promise`<`void` | `Response`>

#### Parameters

• **request** : `AuthorizedRequest`

• **callback?** : `Function`

#### Returns

`Promise`<`void` | `Response`>

#### Source

src/http/AuthorizedServiceCaller.ts:12
