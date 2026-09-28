> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/LoadDataRequest (snapshot 2026-09-28)

# LoadDataRequest

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / LoadDataRequest

# Interface: LoadDataRequest

Atributos enviados na requisição de carregamento dos registros

## Properties

### filters?

> `optional` **filters** : `Filter`[]

Filtros

#### Source

src/dataunit/loading/LoadDataRequest.ts:19

### keepSelection?

> `optional` **keepSelection** : `boolean`

Na navegação de páginas devemos manter a seleção

#### Source

src/dataunit/loading/LoadDataRequest.ts:28

### limit?

> `optional` **limit** : `number`

Quantidade de registros que será retornado

#### Source

src/dataunit/loading/LoadDataRequest.ts:13

### offset?

> `optional` **offset** : `number`

Indice inicial dos registros que será retornado

#### Source

src/dataunit/loading/LoadDataRequest.ts:10

### parentRecordId?

> `optional` **parentRecordId** : `string`

Info parent

#### Source

src/dataunit/loading/LoadDataRequest.ts:25

### quickFilter?

> `optional` **quickFilter** : `QuickFilter`

Filtro rápido

#### Source

src/dataunit/loading/LoadDataRequest.ts:16

### sort?

> `optional` **sort** : `Sort`[]

Ordenação dos resultados

#### Source

src/dataunit/loading/LoadDataRequest.ts:22

### source?

> `optional` **source** : `string`

De onde partiu o refresh. Por padrão a fonte não é identificada

#### Source

src/dataunit/loading/LoadDataRequest.ts:7
