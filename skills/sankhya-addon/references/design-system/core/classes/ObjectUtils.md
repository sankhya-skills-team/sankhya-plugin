> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ObjectUtils (snapshot 2026-09-28)

# ObjectUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ObjectUtils

# Class: ObjectUtils

`ObjectUtils`: Utilizado para manipulação de objetos.

## Constructors

### new ObjectUtils()

> **new ObjectUtils**(): `ObjectUtils`

#### Returns

`ObjectUtils`

## Methods

### copy()

> `static` **copy** <`T`>(`data`): `T`

Faz a cópia do objeto.

#### Type parameters

• **T**

#### Parameters

• **data** : `Object` | `Object`[]

Objeto a ser copiado.

#### Returns

`T`

  * A cópia do objeto válido.

#### Source

src/utils/ObjectUtils.ts:13

### equals()

> `static` **equals**(`obj1`, `obj2`): `any`

Compara se um objeto é igual a outro objeto.

#### Parameters

• **obj1** : `any`

Objeto a ser comparado.

• **obj2** : `any`

Objeto a ser comparado.

#### Returns

`any`

  * Se o objeto 1 é igual ao objeto 2.

#### Source

src/utils/ObjectUtils.ts:84

### getComparableProp()

> `static` `private` **getComparableProp**(`value`, `propToCompare`): `boolean`

#### Parameters

• **value** : `any`

• **propToCompare** : `string`= `"value"`

#### Returns

`boolean`

#### Source

src/utils/ObjectUtils.ts:106

### getProp()

> `static` **getProp**(`obj`, `keyPath`): `undefined` | `Record`<`string`, `any`>

Busca a propriedade de um objeto baseado em seu caminho.

#### Parameters

• **obj** : `Record`<`string`, `any`>

Objeto a ser verificado.

• **keyPath** : `string`

Caminho da propriedade a ser buscada.

#### Returns

`undefined` | `Record`<`string`, `any`>

  * O valor da propriedade caso ela exista.

#### Source

src/utils/ObjectUtils.ts:161

### hasEquivalentProps()

> `static` **hasEquivalentProps**(`obj1`, `obj2`, `propToCompare`): `boolean`

Compara se o valor de dois items são equivalentes. Comparando tanto o valor do item em si, quanto sua propriedade "value"

#### Parameters

• **obj1** : `any`

Objeto a ser comparado.

• **obj2** : `any`

Objeto a ser comparado.

• **propToCompare** : `string`= `"value"`

propriedade que deve ser comparada.

#### Returns

`boolean`

  * Se o objeto 1 é equivalente ao objeto 2.

  *

#### Examples

```ts
hasEquivalentProps('123', {value: '123', label: teste}, 'value') | Retorna: true
```

```ts
hasEquivalentProps('xpto', {value: '123', label: teste}, 'propName') | Retorna: false
```

#### Source

src/utils/ObjectUtils.ts:102

### isEmpty()

> `static` **isEmpty**(`obj`): `boolean`

Verifica se o objeto está vazio (sem atributos).

#### Parameters

• **obj** : `object`

Objeto a ser verificado.

#### Returns

`boolean`

  * True caso o objeto esteja vazio.

#### Source

src/utils/ObjectUtils.ts:119

### isEmptySafetyCheck()

> `static` **isEmptySafetyCheck**(`obj`): `boolean`

Verifica se o objeto está vazio (sem atributos) e retorna true caso seja undefined ou null.

#### Parameters

• **obj** : `object`

Objeto a ser verificado.

#### Returns

`boolean`

  * True caso o objeto esteja vazio.

#### Source

src/utils/ObjectUtils.ts:129

### isNotEmpty()

> `static` **isNotEmpty**(`obj`): `boolean`

Verifica se o objeto NÃO está vazio (sem atributos).

#### Parameters

• **obj** : `object`

Objeto a ser verificado.

#### Returns

`boolean`

  * True caso o objeto NÃO esteja vazio

#### Source

src/utils/ObjectUtils.ts:140

### isNotEmptySafetyCheck()

> `static` **isNotEmptySafetyCheck**(`obj`): `boolean`

Verifica se o objeto NÃO está vazio (sem atributos) e retorna false caso objeto seja null ou undefined.

#### Parameters

• **obj** : `object`

Objeto a ser verificado.

#### Returns

`boolean`

  * True caso o objeto NÃO esteja vazio

#### Source

src/utils/ObjectUtils.ts:150

### objectToString()

> `static` **objectToString**(`data`): `string`

Converte um objeto em string/JSON.

#### Parameters

• **data** : `Object` | `Object`[]

Objeto a ser convertido.

#### Returns

`string`

  * Uma string JSON.

#### Example

@Informado: `{nome : "Sankhya", cidade: "Uberlandia"}` | Obtenho: `"{"nome" : "Sankhya", "cidade":"Uberlandia"}"`

#### Source

src/utils/ObjectUtils.ts:26

### removeEmptyValues()

> `static` **removeEmptyValues**(`obj`): `object`

Remove atributos nulos e indefinidos de um objeto.

#### Parameters

• **obj** : `object`

#### Returns

`object`

  * O objeto com as propriedades válidas.

#### Source

src/utils/ObjectUtils.ts:68

### sortByProperty()

> `static` **sortByProperty**(`data`, `property`): `any`

Faz a ordenação de um objeto por uma propriedade.

#### Parameters

• **data** : `any`

Objeto a ser ordenado.

• **property** : `string`

Nome da propriedade a ser ordenada.

#### Returns

`any`

  * O objeto ordenado pela propriedade.

#### Source

src/utils/ObjectUtils.ts:50

### stringToObject()

> `static` **stringToObject**(`data`): `Object` | `Object`[]

Converte uma string/JSON em objeto.

#### Parameters

• **data** : `string`

String a ser convertida.

#### Returns

`Object` | `Object`[]

  * Um objeto válido.

#### Example

Informado: `"{"nome" : "Sankhya", "cidade":"Uberlandia"}"` | Obtenho: `{nome : "Sankhya", cidade: "Uberlandia"}`

#### Source

src/utils/ObjectUtils.ts:39
