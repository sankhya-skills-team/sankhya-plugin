> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/MaskFormatter (snapshot 2026-09-28)

# MaskFormatter

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / MaskFormatter

# Class: MaskFormatter

`MaskFormatter` é usado para formatar strings. Seu comportamento é controlado pelo formato do atributo `mask` que especifica quais caracteres são válidos e onde devem estar posicionados, intercalando-os com eventuais caracteres literais expressados no padrão informado. Sua implementação é inspirada pela implementação em Java do [MaskFormatter](https://docs.oracle.com/javase/7/docs/api/javax/swing/text/MaskFormatter.html).

Para o padrão da máscara podem ser usados os seguintes caracteres especiais:

| Caractere | Comportamento |
|---|---|
| # | Qualquer número |
| ' | "Escapa" o caractere que vem na sequência. Útil quando desejamos converter um caractere especial em literal. |
| U | Qualquer letra. Transforma letras minúsculas em maiúsculas. |
| L | Qualquer letra. Transforma letras maiúsculas em minúsculas. |
| A | Qualquer letra ou número. |
| Z | Qualquer letra ou número. Transforma letras minúsculas em maiúsculas. |
| ? | Qualquer letra. Preserva maiúsculas e minúsculas. |
| * | Qualquer caractere. |

Os demais caracteres presentes no padrão serão tratados como literais, isto é, serão apenas inseridos naquela posição.

Quando o valor a ser formatado é menor que a máscara, um 'placeHolder' será inserido em cada posição ausente, completando a formatação. Por padrão será usado um espaço em branco como 'placeHolder', mas esse valor pode ser alterado.

Por exemplo: ''' const formatter: MaskFormatter = new MaskFormatter("###-####"); formatter.placeholder = '_'; console.log(formatter.format("123")); ''' resultaria na string '123-_ ___'.

##Veja mais alguns exemplos:

| Padrão | Máscara | Entrada | Saída |
|---|---|---|---|
| Telefone | (##) ####-#### | 3432192515 | (34) 3219-2515 |
| CPF | ###.###.###-## | 12345678901 | 123.456.789-01 |
| CNPJ | ZZ.ZZZ.ZZZ/ZZZZ-## | 1a3B5c7D9e1F31 | 1A.3B5.C7D9/E1F3-31 |
| CEP | ##.###-### | 12345678 | 12.345-678 |
| PLACA (veículo) | UUU-#### | abc1234 | ABC-1234 |
| Cor RGB | '#AAAAAA | 00000F0 | #0000F0 |

## Constructors

### new MaskFormatter()

> **new MaskFormatter**(`mask`): `MaskFormatter`

#### Parameters

• **mask** : `string`

#### Returns

`MaskFormatter`

#### Source

src/utils/MaskFormatter.ts:95

## Properties

### _mask

> `private` **_mask** : `string` = `''`

#### Source

src/utils/MaskFormatter.ts:69

### _maskChars

> `private` **_maskChars** : `__class`[]

#### Source

src/utils/MaskFormatter.ts:70

### placeholder

> **placeholder** : `string` = `' '`

Determina qual caractere será usado dos caracteres não presentes no valor, ou seja, aqueles que o usuário ainda não informou. Por padrão usamos um espaço.

#### Source

src/utils/MaskFormatter.ts:76

### ALPHA_NUMERIC_KEY

> `static` `private` **ALPHA_NUMERIC_KEY** : `string` = `"A"`

#### Source

src/utils/MaskFormatter.ts:54

### ALPHA_NUMERIC_UPPERCASE_KEY

> `static` `private` **ALPHA_NUMERIC_UPPERCASE_KEY** : `string` = `"Z"`

#### Source

src/utils/MaskFormatter.ts:55

### ANYTHING_KEY

> `static` `private` **ANYTHING_KEY** : `string` = `"*"`

#### Source

src/utils/MaskFormatter.ts:57

### AlphaNumericCharacter

> `static` `private` **AlphaNumericCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:475

### AlphaNumericUpperCaseCharacter

> `static` `private` **AlphaNumericUpperCaseCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:489

### CHARACTER_KEY

> `static` `private` **CHARACTER_KEY** : `string` = `"?"`

#### Source

src/utils/MaskFormatter.ts:56

### CharCharacter

> `static` `private` **CharCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:507

### DEFAULT_MASKS

> `static` **DEFAULT_MASKS** : `any`

#### Source

src/utils/MaskFormatter.ts:59

### DIGIT_KEY

> `static` `private` **DIGIT_KEY** : `string` = `"#"`

#### Source

src/utils/MaskFormatter.ts:50

### DigitMaskCharacter

> `static` `private` **DigitMaskCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:400

### LITERAL_KEY

> `static` `private` **LITERAL_KEY** : `string` = `"'"`

#### Source

src/utils/MaskFormatter.ts:51

### LOWERCASE_KEY

> `static` `private` **LOWERCASE_KEY** : `string` = `"L"`

#### Source

src/utils/MaskFormatter.ts:53

### LiteralCharacter

> `static` `private` **LiteralCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:381

### LowerCaseCharacter

> `static` `private` **LowerCaseCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:452

### UPPERCASE_KEY

> `static` `private` **UPPERCASE_KEY** : `string` = `"U"`

#### Source

src/utils/MaskFormatter.ts:52

### UpperCaseCharacter

> `static` `private` **UpperCaseCharacter** : _typeof_ `__class`

#### Source

src/utils/MaskFormatter.ts:429

## Accessors

### mask

> `get` **mask**(): `string`

Getter para mask.

> `set` **mask**(`mask`): `void`

Setter para mask. Trata-se do padrão que se espera ao formatar o texto.

#### Parameters

• **mask** : `string`

#### Returns

`string`

A última máscara informada.

#### Source

src/utils/MaskFormatter.ts:91

## Methods

### applyMask()

> **applyMask**(`value`): `string`

Aplica a máscara quando o input é alterado

#### Parameters

• **value** : `string`

Valor a ser aplicado com a máscara.

#### Returns

`string`

O valor processado de acordo com o padrão.

#### Source

src/utils/MaskFormatter.ts:106

### format()

> **format**(`value`, `trimBefore`): `string`

Formata a string passada baseada na máscara definda pelo atributo mask.

#### Parameters

• **value** : `string`

Valor a ser formatado.

• **trimBefore** : `boolean`= `false`

Executa um trim para remover espaços em branco.

#### Returns

`string`

O valor processado de acordo com o padrão.

#### Source

src/utils/MaskFormatter.ts:194

### removeMask()

> **removeMask**(`value`): `string`

Remove a máscara formatando a string retornando sem máscara

#### Parameters

• **value** : `string`

Valor a ser formatado com máscara.

#### Returns

`string`

O valor processado de acordo com o padrão.

#### Source

src/utils/MaskFormatter.ts:174

### updateInternalMask()

> `private` **updateInternalMask**(): `void`

Prepara a formatação internamente de acordo com o padrão.

#### Returns

`void`

#### Source

src/utils/MaskFormatter.ts:214
