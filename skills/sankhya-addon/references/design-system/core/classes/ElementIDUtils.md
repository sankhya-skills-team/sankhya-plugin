> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ElementIDUtils (snapshot 2026-09-28)

# ElementIDUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ElementIDUtils

# Class: ElementIDUtils

`ElementIDUtils`: O ElementIDUtils é um utilitário responsável por criar e adicionar identificadores únicos aos componentes através do atributo data-element-id. A finalidade dele é otimizar a automação dos testes e melhorar a eficiência na manipulação dos componentes do Design System, garantindo seleções precisas e seguras.

## Constructors

### new ElementIDUtils()

> **new ElementIDUtils**(): `ElementIDUtils`

#### Returns

`ElementIDUtils`

## Properties

### DATA_ELEMENT_ID_ATTRIBUTE_NAME

> `static` **DATA_ELEMENT_ID_ATTRIBUTE_NAME** : `string` = `"data-element-id"`

#### Source

src/utils/ElementIDUtils.ts:14

### INTERNAL_INPUT_NAME

> `static` **INTERNAL_INPUT_NAME** : `string` = `"embedded"`

#### Source

src/utils/ElementIDUtils.ts:15

### REGEX_DATAUNIT_NAME

> `static` `private` **REGEX_DATAUNIT_NAME** : `RegExp`

#### Source

src/utils/ElementIDUtils.ts:16

## Methods

### addIDInfo()

> `static` **addIDInfo**(`element`, `suffix`?, `iDInfo`?): `string`

Cria e adiciona a propriedade `data-element-id` em um elemento.

#### Parameters

• **element** : `HTMLElement`

Elemento HTML a ser modificado (HTMLElement).

• **suffix?** : `string`

Sufixo/Texto para ser adicionado.

• **iDInfo?** : `IElementIDInfo`

ID para ser adicionado.

#### Returns

`string`

  * O data-element-id gerado.

#### Source

src/utils/ElementIDUtils.ts:26

### addIDInfoIfNotExists()

> `static` **addIDInfoIfNotExists**(`element`, `suffix`?, `iDInfo`?): `string`

#### Parameters

• **element** : `HTMLElement`

• **suffix?** : `string`

• **iDInfo?** : `IElementIDInfo`

#### Returns

`string`

#### Source

src/utils/ElementIDUtils.ts:39

### addPrefix()

> `static` `private` **addPrefix**(`iDInfo`, `dataElementID`): `string`

Adiciona a propriedade name do DataUnit como prefixo do data-element-id do elemento.

#### Parameters

• **iDInfo** : `undefined` | `IElementIDInfo`

ID para ser adicionado ao `data-element-id`.

• **dataElementID** : `string`

Sufixo/Texto para ser adicionado ao `data-element-id`.

#### Returns

`string`

  * String contendo informação para ser usada no `data-element-id` do elemento.

#### Source

src/utils/ElementIDUtils.ts:147

### addSuffix()

> `static` `private` **addSuffix**(`dataElementID`, `suffix`, `element`): `string`

Adiciona sufixo ao atributo `data-element-id` de um elemento, utilizado para montar a hierarquia dos ids dos componentes em tela.

#### Parameters

• **dataElementID** : `null` | `string`

ID para ser adicionado ao `data-element-id`.

• **suffix** : `undefined` | `string`

Sufixo/Texto para ser adicionado ao `data-element-id`.

• **element** : `HTMLElement`

Elemento HTML a ser modificado (HTMLElement).

#### Returns

`string`

  * `data-element-id` com sufixo.

#### Example

```ts
Um ez-combo-box tem data-element-id = codparc_input_embedded_combo.
Dentro desse ez-combo-box existe um ez-text-input. O data-element-id teria como sufixo o id 'codparc_input_embedded_combo' referente ao seu pai.
```

#### Source

src/utils/ElementIDUtils.ts:130

### formatDescription()

> `static` `private` **formatDescription**(`value`): `string`

Remove caracteres especiais.

#### Parameters

• **value** : `null` | `string`

Texto que terá os caracteres especiais removidos.

#### Returns

`string`

  * Retorna a string sem caracteres especiais e em camelCase.

#### Source

src/utils/ElementIDUtils.ts:162

### getAttributeValid()

> `static` `private` **getAttributeValid**(`element`, `iDInfo`?): `null` | `string`

Obtém ID válido para o elemento.

#### Parameters

• **element** : `HTMLElement`

Elemento HTML a ser modificado (HTMLElement).

• **iDInfo?** : `IElementIDInfo`

ID para ser adicionado.

#### Returns

`null` | `string`

  * ID para ser adicionado ao elemento conforme ordem de prioridade.

#### Source

src/utils/ElementIDUtils.ts:90

### getDataElementID()

> `static` `private` **getDataElementID**(`element`, `suffix`?, `iDInfo`?): `string`

Obtém o `data-element-id` do elemento com adição do sufixo e ID.

#### Parameters

• **element** : `HTMLElement`

Elemento HTML a ser modificado (HTMLElement).

• **suffix?** : `string`

Sufixo/Texto para ser adicionado.

• **iDInfo?** : `IElementIDInfo`

ID para ser adicionado.

#### Returns

`string`

  * Atributo `data-element-id` do elemento modificado com sufixo e/ou ID.

#### Source

src/utils/ElementIDUtils.ts:66

### getDataElementIDAttribute()

> `static` `private` **getDataElementIDAttribute**(`element`): `null` | `string`

#### Parameters

• **element** : `HTMLElement`

#### Returns

`null` | `string`

#### Source

src/utils/ElementIDUtils.ts:168

### getInternalIDInfo()

> `static` **getInternalIDInfo**(`sufix`): `string`

#### Parameters

• **sufix** : `string`

#### Returns

`string`

#### Source

src/utils/ElementIDUtils.ts:54

### parseDataUnitName()

> `static` `private` **parseDataUnitName**(`uri`): `string`

#### Parameters

• **uri** : `string`

#### Returns

`string`

#### Source

src/utils/ElementIDUtils.ts:175
