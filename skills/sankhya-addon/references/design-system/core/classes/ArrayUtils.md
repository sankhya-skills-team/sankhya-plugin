> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ArrayUtils (snapshot 2026-09-28)

# ArrayUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ArrayUtils

# Class: ArrayUtils

`ArrayUtils`: Utilitário com a responsabilidade de manipular Arrays.

## Constructors

### new ArrayUtils()

> **new ArrayUtils**(): `ArrayUtils`

#### Returns

`ArrayUtils`

## Methods

### applyStringFilter()

> `static` **applyStringFilter**(`argument`, `originalArray`, `alphabeticalSorting`, `fieldName`): `any`[]

Filtra um array a partir de um critério textual.

#### Parameters

• **argument** : `string`

Texto a ser usado no filtro.

• **originalArray** : `any`[]

Array no formato original.

• **alphabeticalSorting** : `boolean`= `true`

Determina se o resultado deve ser ordenado ou mantido na ordem original. Por padrão ordena.

• **fieldName** : `string`= `"label"`

Caso o objeto deva ser filtrado por um campo diferente de "label", pode-se usar esse parâmetro.

#### Returns

`any`[]

  * Um array filtrado e ordenado conforme necessidade..

#### Source

src/utils/ArrayUtils.ts:18

### find()

> `static` **find**(`arr`, `checkerFn`): `any`

Ordena valores de um array alfabeticamente.

#### Parameters

• **arr** : `any`

Array a ser ordenado.

• **checkerFn** : `any`

#### Returns

`any`

  * Array ordenado alfabeticamente..

#### Source

src/utils/ArrayUtils.ts:69

### indexOf()

> `static` **indexOf**(`arr`, `obj`): `number`

Retorna o objeto se for encontrado no array, ou -1 se não for encontrado.

#### Parameters

• **arr** : `any`

Array onde está o objeto.

• **obj** : `any`

Objeto a ser procurado.

#### Returns

`number`

  * Array ordenado alfabeticamente..

#### Source

src/utils/ArrayUtils.ts:88

### isIn()

> `static` **isIn**(`arr`, `obj`): `boolean`

Remove um objeto do array.

#### Parameters

• **arr** : `any`

• **obj** : `any`

Objeto a ser removido.

#### Returns

`boolean`

  * Array sem o Objeto informado.

#### Source

src/utils/ArrayUtils.ts:131

### normalizeSearchString()

> `static` `private` **normalizeSearchString**(`original`): `string`

Converte texto para caixa alta e substitui caracteres acentuados.

#### Parameters

• **original** : `string`

Texto a ser convertido.

#### Returns

`string`

  * Texto com as letras acentuadas sem os acentos e em caixa alta.

#### Source

src/utils/ArrayUtils.ts:36

### removeAtIndex()

> `static` **removeAtIndex**(`array`, `index`): `any`

Remove um item de array de acordo com o index.

#### Parameters

• **array** : `any`

Array onde está o item.

• **index** : `number`

Index do item a ser removido.

#### Returns

`any`

  * Array sem o item do index informado.

#### Source

src/utils/ArrayUtils.ts:106

### removeReference()

> `static` **removeReference**(`array`, `obj`): `any`

Remove um objeto do array.

#### Parameters

• **array** : `any`

Array onde está o objeto.

• **obj** : `any`

Objeto a ser removido.

#### Returns

`any`

  * Array sem o Objeto informado.

#### Source

src/utils/ArrayUtils.ts:119

### sortAlphabetically()

> `static` **sortAlphabetically**(`originalArray`, `fieldName`): `any`[]

Ordena valores de um array alfabeticamente.

#### Parameters

• **originalArray** : `any`[]

Array a ser ordenado.

• **fieldName** : `string`= `"label"`

#### Returns

`any`[]

  * Array ordenado alfabeticamente..

#### Source

src/utils/ArrayUtils.ts:46
