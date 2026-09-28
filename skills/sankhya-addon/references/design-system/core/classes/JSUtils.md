> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/JSUtils (snapshot 2026-09-28)

# JSUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / JSUtils

# Class: JSUtils

Classe com utiliários comuns para funções genéricas em JavaScript.

## Constructors

### new JSUtils()

> **new JSUtils**(): `JSUtils`

#### Returns

`JSUtils`

## Methods

### debounce()

> `static` **debounce**(`callback`, `timeout`): `any`

Método responsável em criar um timer para processar uma determinada função.

#### Parameters

• **callback** : `any`

Função de callback para processar após o timer.

• **timeout** : `number`= `300`

Valor dos milissegundos desejados para processar a função (o padrão é 300).

#### Returns

`any`

  * Retorna um método com controle de timer para processar a função de callback.

#### Source

src/utils/JSUtils.ts:21

### debounceLeading()

> `static` **debounceLeading**(`callback`, `timeout`, `context`?): `VoidFunction`

Método responsável por executar uma função e ignorar as outras posteriores até o tempo especificado.

#### Parameters

• **callback** : `Function`

Função a ser invocada

• **timeout** : `number`= `300`

Quantidade de tempo para aguardar antes de invocar novamente

• **context?** : `any`

O contexto atual

#### Returns

`VoidFunction`

A função com o debounce

#### Source

src/utils/JSUtils.ts:37

### generateUUID()

> `static` **generateUUID**(): `string`

Método responsável em gerar um UUID.

#### Returns

`string`

  * Retorna um UUID.

#### Source

src/utils/JSUtils.ts:95

### isBase64()

> `static` **isBase64**(`str`): `boolean`

Método que verifica se uma string está encodada com base64.

#### Parameters

• **str** : `string`

String que será verificada.

#### Returns

`boolean`

  * Retorna um valor booleando informando se a string está encodada com base64.

#### Source

src/utils/JSUtils.ts:80

### isEllipsisActive()

> `static` **isEllipsisActive**(`element`): `boolean`

Método responsável em validar se um elemento HTML está com o ellipsis ativo.

#### Parameters

• **element** : `any`

Elemento HTML que será verificado.

#### Returns

`boolean`

  * Retorna um valor booleando informando se o elemento está com o ellipsis ativo.

#### Source

src/utils/JSUtils.ts:60

### isHiddenElement()

> `static` **isHiddenElement**(`element`): `boolean`

#### Parameters

• **element** : `HTMLElement`

#### Returns

`boolean`

#### Source

src/utils/JSUtils.ts:8

### replaceHtmlEntities()

> `static` **replaceHtmlEntities**(`source`): `string`

Substitui caracteres para suas entidades HTML.

#### Parameters

• **source** : `string`

String a ter os caracteres substituidos.

#### Returns

`string`

  * Retorna um UUID.

#### Source

src/utils/JSUtils.ts:105
