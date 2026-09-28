> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/StringUtils (snapshot 2026-09-28)

# StringUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / StringUtils

# Class: StringUtils

`StringUtils`: Utilizado para manipulação de Strings.

## Constructors

### new StringUtils()

> **new StringUtils**(): `StringUtils`

#### Returns

`StringUtils`

## Methods

### compare()

> `static` **compare**(`a`, `b`): `number`

Determina a ordem de strings.

#### Parameters

• **a** : `string`

Primeira string para comparação.

• **b** : `string`

Segunda string para comparação.

#### Returns

`number`

  * Um numeral negativo se o primeiro argumento é menor que o segundo, zero se os dois são iguais e um numeral positivo quando o primeiro é maior que o segundo.

#### Source

src/utils/StringUtils.ts:250

### decodeHtmlEntities()

> `static` **decodeHtmlEntities**(`text`): `string`

Converte todas as entidades HTML de um texto

#### Parameters

• **text** : `string`

String para ser transformada.

#### Returns

`string`

#### Example

```ts
entrada: "&lt;Teste&gt;" // retorno: "<Teste>"
```

#### Source

src/utils/StringUtils.ts:71

### escapeString()

> `static` **escapeString**(`str`): `string`

Escapa caracteres especiais em uma string, usando sequencias de escape Unicode.

#### Parameters

• **str** : `string`

A string que deve sofrer alteração.

#### Returns

`string`

String com valores alterados.

#### Source

src/utils/StringUtils.ts:552

### formatBytes()

> `static` **formatBytes**(`bytes`): `string`

Utilitário para formatar bytes em string legível, convertendo para múltiplos maiores caso necessário.

#### Parameters

• **bytes** : `number`

#### Returns

`string`

string formatada de acordo com a unidade.

#### Source

src/utils/StringUtils.ts:335

### generateUUID()

> `static` **generateUUID**(): `string`

Método utilizado para gerar IDs únicos.

#### Returns

`string`

id único randômico.

#### Source

src/utils/StringUtils.ts:381

### getArgumentNumber()

> `static` **getArgumentNumber**(`argument`): `number`

#### Parameters

• **argument** : `String`

#### Returns

`number`

#### Source

src/utils/StringUtils.ts:489

### getBooleanValue()

> `static` **getBooleanValue**(`value`, `defaultValue`): `boolean`

Converte um texto do tipo string para um booleano.

#### Parameters

• **value** : `string`

Valor a ser convertido.

• **defaultValue** : `boolean`= `false`

Valor padrão.

#### Returns

`boolean`

  * Texto convertido.

#### Example

```ts
Informado: 'true'  | Retorna: true
Informado: 'false' | Retorna: false
```

#### Source

src/utils/StringUtils.ts:180

### getOppositeCase()

> `static` **getOppositeCase**(`original`): `string`

Inverte uma string de minúsculas para maiúsculas e vice-versa

#### Parameters

• **original** : `string`

A string a ser invertida

#### Returns

`string`

A string invertida

#### Source

src/utils/StringUtils.ts:419

### getSpecialCharacters()

> `static` **getSpecialCharacters**(`str`): `string`[]

#### Parameters

• **str** : `string`

#### Returns

`string`[]

#### Source

src/utils/StringUtils.ts:461

### hashCode()

> `static` **hashCode**(`value`): `string`

Calcula um código hash para uma string.

#### Parameters

• **value** : `string`

String que será gerado o hash code.

#### Returns

`string`

  * Um hash calculado com base no valor informado.

#### Example

```ts
Informado: '123456' | Retorna: 1450575459
```

#### Source

src/utils/StringUtils.ts:158

### highlightValue()

> `static` **highlightValue**(`argument`, `matchFields`, `value`, `fieldMD`, `forceMatch`): `string`

#### Parameters

• **argument** : `String`

• **matchFields** : `any`

• **value** : `string`

• **fieldMD** : `any`

• **forceMatch** : `boolean`

#### Returns

`string`

#### Source

src/utils/StringUtils.ts:493

### isCaseable()

> `static` **isCaseable**(`original`): `boolean`

Checa se uma string pode ser convertida para letras maiúsculas ou minúsculas

#### Parameters

• **original** : `string`

A string a ser verificada

#### Returns

`boolean`

Se a string pode ser convertida

#### Source

src/utils/StringUtils.ts:391

### isEmpty()

> `static` **isEmpty**(`value`): `Boolean`

Retorna se a string está vazia. Valores null e undefined são considerados como vazio.

#### Parameters

• **value** : `any`

String para ser validada.

#### Returns

`Boolean`

  * Verdadeiro caso a string não contenha informação.

#### Source

src/utils/StringUtils.ts:18

### isLowerCase()

> `static` **isLowerCase**(`original`): `boolean`

Checa se uma string é minúscula

#### Parameters

• **original** : `string`

A string a ser verificada

#### Returns

`boolean`

Se a string é minúscula

#### Source

src/utils/StringUtils.ts:406

### isString()

> `static` **isString**(`text`): `boolean`

Verifica se argumento informado é do tipo string

#### Parameters

• **text** : `any`

#### Returns

`boolean`

#### Source

src/utils/StringUtils.ts:38

### padEnd()

> `static` **padEnd**(`str`, `len`, `pad`): `string`

Adiciona caracteres à direita caso texto seja menor que o valor do parâmetro len passado.

#### Parameters

• **str** : `string`

Texto para ser ajustado.

• **len** : `number`

Tamanho desejado do texto.

• **pad** : `string`= `" "`

Caractere a ser adicionado a direita caso o texto menor que o tamanho passado.

#### Returns

`string`

  * Texto passado se este for maior que o len. Ou retorna o texto com os caracteres adicionados na direita.

#### Examples

```ts
padStart('SANKHYA', 8,'.') | Retorna: 'SANKHYA...'
```

```ts
padStart('SANKHYA', 5,'A') | Retorna: 'SANKHYA'
```

#### Source

src/utils/StringUtils.ts:234

### padStart()

> `static` **padStart**(`str`, `len`, `pad`): `string`

Adiciona caracteres à esquerda caso texto seja menor que o valor do parâmetro len passado.

#### Parameters

• **str** : `string`

Texto para ser ajustado.

• **len** : `number`

Tamanho desejado do texto.

• **pad** : `string`= `" "`

Caractere a ser adicionado a esquerda caso o texto menor que o tamanho passado.

#### Returns

`string`

  * Texto passado se este for maior que o len. Ou retorna o texto com os caracteres adicionados na esquerda.

#### Examples

```ts
padStart('SANKHYA', 8,'.') | Retorna: '...SANKHYA'
```

```ts
padStart('SANKHYA', 5,'A') | Retorna: 'SANKHYA'
```

#### Source

src/utils/StringUtils.ts:209

### prettyPrecision()

> `static` `private` **prettyPrecision**(`strNumber`): `string`

Método interno. Remove zeros depois da vírgula diminuindo o tamanho da string.

#### Parameters

• **strNumber** : `string`

representação textual do número a ser ajustado.

#### Returns

`string`

simplificação do strNumber, sem os zeros à direita depois do ponto.

#### Source

src/utils/StringUtils.ts:360

### removeSpecialCharacters()

> `static` **removeSpecialCharacters**(`str`): `string`

#### Parameters

• **str** : `string`

#### Returns

`string`

#### Source

src/utils/StringUtils.ts:480

### replaceAccentuatedChars()

> `static` **replaceAccentuatedChars**(`text`, `removeSpecialChars`): `string`

Remove acentuação de vogais e de caracteres especiais que não sejam letras ou numeral.

#### Parameters

• **text** : `string`

String para ser transformada.

• **removeSpecialChars** : `boolean`= `true`

Remove outros caracteres especiais que não sejam letras e números.

#### Returns

`string`

#### Example

```ts
entrada: "á@Êç#Ò", false // retorno: "a@Ec#O"
entrada: "á@Êç#Ò", true // retorno: "aEcO"
```

#### Source

src/utils/StringUtils.ts:124

### replaceAccentuatedCharsHtmlEntities()

> `static` **replaceAccentuatedCharsHtmlEntities**(`source`): `string`

#### Parameters

• **source** : `string`

#### Returns

`string`

#### Source

src/utils/StringUtils.ts:441

### replaceAccentuatedCharsKeepSymbols()

> `static` **replaceAccentuatedCharsKeepSymbols**(`text`): `string`

Remove acentos de vogais, substitui Ç por c e retorna a string em caixa alta mantendo espaços e símbolos.

#### Parameters

• **text** : `string`

Texto para ser transformado.

#### Returns

`string`

  * Texto sem acentuação e caixa alta, mantendo espaços e símbolos.

#### Source

src/utils/StringUtils.ts:143

### replaceAccentuatedCharsLower()

> `static` **replaceAccentuatedCharsLower**(`text`): `string`

Remove acentos de vogais minúsculas.

#### Parameters

• **text** : `string`

String para ser transformada.

#### Returns

`string`

#### Example

```ts
entrada: "áêçò" // retorno: "aeco"
```

#### Source

src/utils/StringUtils.ts:101

### replaceAccentuatedCharsUpper()

> `static` **replaceAccentuatedCharsUpper**(`text`): `string`

Remove acentos de vogais maiúsculas

#### Parameters

• **text** : `string`

String para ser transformada.

#### Returns

`string`

#### Example

```ts
entrada: "ÁÊÇÒ" // retorno: "AECO"
```

#### Source

src/utils/StringUtils.ts:49

### replaceAll()

> `static` **replaceAll**(`str`, `strFrom`, `strTo`): `string`

#### Parameters

• **str** : `string`

• **strFrom** : `string`

• **strTo** : `string`

#### Returns

`string`

#### Source

src/utils/StringUtils.ts:471

### replaceBlankCharacters()

> `static` **replaceBlankCharacters**(`value`): `string`

Utilitário para remover caracteres em branco da string.

#### Parameters

• **value** : `string`

String a ser removido os espaços.

#### Returns

`string`

String sem espaços em branco.

#### Source

src/utils/StringUtils.ts:325

### replaceToSpace()

> `static` **replaceToSpace**(`source`, `replaceList`): `string`

#### Parameters

• **source** : `string`

• **replaceList** : `string`[]= `[]`

#### Returns

`string`

#### Source

src/utils/StringUtils.ts:424

### toCamelCase()

> `static` **toCamelCase**(`value`): `string`

Converte string em camelCase. Combina palavras compostas ou frases, alterando a inicial de cada uma, a partir da primeira, para maiúscula e unidas sem espaços.

#### Parameters

• **value** : `string`

String a ser convertida.

#### Returns

`string`

String convertida em camelCase.

#### Example

```ts
toCamelCase('Exemplo de uso') | Retorna: 'exemploDeUso'
```

#### Source

src/utils/StringUtils.ts:276

### toKebabCase()

> `static` **toKebabCase**(`value`): `string`

Utilitário para converter string em kebab-case.

#### Parameters

• **value** : `string`

String a ser convertida.

#### Returns

`string`

String convertida em KebabCase.

#### Source

src/utils/StringUtils.ts:316

### toPascalCase()

> `static` **toPascalCase**(`value`): `string`

Converte string para PascalCase.

#### Parameters

• **value** : `string`

String a ser convertida.

#### Returns

`string`

String convertida em PascalCase.

#### Source

src/utils/StringUtils.ts:291

### toSnakeCase()

> `static` **toSnakeCase**(`value`): `string`

Utilitário para converter string em snake_case.

#### Parameters

• **value** : `string`

String a ser convertida.

#### Returns

`string`

String convertida em snake_case.

#### Source

src/utils/StringUtils.ts:303
