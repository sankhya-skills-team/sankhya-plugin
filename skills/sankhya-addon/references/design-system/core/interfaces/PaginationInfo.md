> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PaginationInfo (snapshot 2026-09-28)

# PaginationInfo

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / PaginationInfo

# Interface: PaginationInfo

Informações da paginação retornada na requisição de carregamento de registros

## Properties

### askRowsLimit?

> `optional` **askRowsLimit** : `number`

Informa se deve exibir diálogo para cancelar carregamento de registros

#### Source

src/dataunit/loading/PaginationInfo.ts:30

### count?

> `optional` **count** : `number`

Quantidade de registros carregados até o momento

#### Source

src/dataunit/loading/PaginationInfo.ts:17

### currentPage

> **currentPage** : `number`

Página atual

#### Source

src/dataunit/loading/PaginationInfo.ts:5

### firstRecord

> **firstRecord** : `number`

Indice do primeiro registro na página

#### Source

src/dataunit/loading/PaginationInfo.ts:8

### hasMore

> **hasMore** : `boolean`

Se ainda existem mais registros

#### Source

src/dataunit/loading/PaginationInfo.ts:20

### lastRecord

> **lastRecord** : `number`

Indice do último registro na página

#### Source

src/dataunit/loading/PaginationInfo.ts:11

### loadingInProgress?

> `optional` **loadingInProgress** : `boolean`

Informa se o carregamento de dados em background está sendo executado Caso o dataunit não tenha carga paralela o valor será indefinido

#### Source

src/dataunit/loading/PaginationInfo.ts:25

### total?

> `optional` **total** : `number`

Quantidade total de registros

#### Source

src/dataunit/loading/PaginationInfo.ts:14
