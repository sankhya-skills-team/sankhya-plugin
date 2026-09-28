> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/RequestMetadata (snapshot 2026-09-28)

# RequestMetadata

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / RequestMetadata

# Class: RequestMetadata

Representa as propriedades necessárias para se executar uma requisição.

## Constructors

### new RequestMetadata()

> **new RequestMetadata**(`url`, `method`, `headers`?): `RequestMetadata`

#### Parameters

• **url** : `string`

A URL que deve ser chamada.

• **method** : `Method`

O Método da requisição (GET, PUT, POST ou DELETE).

• **headers?** : `Header`[]

#### Returns

`RequestMetadata`

#### Source

src/http/RequestMetadata.ts:22

## Properties

### headers

> **headers** : `Header`[]

Headers para serem enviados na requisição

#### Source

src/http/RequestMetadata.ts:16

### method

> **method** : `Method`

O verbo HTTP

#### Source

src/http/RequestMetadata.ts:10

### timeout

> **timeout** : `number` = `30000`

Tempo limite de espera pela resposta

#### Source

src/http/RequestMetadata.ts:13

### url

> **url** : `string`

A URL a ser chamada

#### Source

src/http/RequestMetadata.ts:7
