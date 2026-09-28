> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/NumberUtils (snapshot 2026-09-28)

# NumberUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / NumberUtils

# Class: NumberUtils

`NumberUtils`: Utilizado para manipulação de numerais.

## Constructors

### new NumberUtils()

> **new NumberUtils**(): `NumberUtils`

#### Returns

`NumberUtils`

## Methods

### changeFormat()

> `static` **changeFormat**(`value`): `string`

Troca o formato do numeral(string) de "PT-BR" para "EN-US" e vice-versa.

#### Parameters

• **value** : `string`

Numeral em formato de string a ser convertido.

#### Returns

`string`

  * Numeral em formato de string formatado de "PT-BR" para "EN-US" e vice-versa.

#### Examples

```ts
Informo: "15,55"     | Obtenho: "15.55"
```

```ts
Informo: "27.99"     | Obtenho: "27,99"
```

#### Source

src/utils/NumberUtils.ts:186

### compare()

> `static` **compare**(`a`, `b`): `number`

Determina a ordem de umeros.

#### Parameters

• **a** : `number`

Primeio número para comparação.

• **b** : `number`

Segundo número para comparação.

#### Returns

`number`

  * Um numeral negativo se o primeiro argumento é menor que o segundo, zero se os dois são iguais e um numeral positivo quando o primeiro é maior que o segundo.

#### Source

src/utils/NumberUtils.ts:267

### format()

> `static` **format**(`value`, `precision`, `prettyPrecision`, `defaultValue`): `string`

Formata o numeral com a precisão informada.

#### Parameters

• **value** : `string`

Numeral em formato de string a ser convertido (Importante: formato PT-BR ou já em formato numérico - sem separador de milhares: ######.##).

• **precision** : `number`

Quantidade de casas decimais.

• **prettyPrecision** : `number`= `NaN`

Quantidade de zeros nos decimais.

• **defaultValue** : `string`= `undefined`

Valor padrão caso o value não seja um valor numérico válido.

#### Returns

`string`

  * Numeral em formato de String formatado em PT-BR.

#### Example

```ts
Informado: ('10,9845444', 3, 3) | Retorna: '10,985'
Informado: (undefined, 3, 3) | Retorna: NaN
Informado: (undefined, 3, 3, '0,00') | Retorna: 0,00
```

#### Source

src/utils/NumberUtils.ts:77

### getValueOrDefault()

> `static` **getValueOrDefault**(`value`, `defaultValue`): `number`

Obtém o valor ou o valor padrão, caso o valor seja inválido(NaN/undefined).

#### Parameters

• **value** : `any`

Valor a ser validado.

• **defaultValue** : `number`

Valor padrão a ser retornado caso o value seja inválido.

#### Returns

`number`

  * O próprio numeral passado ou zero.

#### Examples

```ts
Informo: value: 30, defaultValue: 0     | Obtenho: 30
```

```ts
Informo: value: "30", defaultValue: 0   | Obtenho: 30
```

```ts
Informo: value: "30abc", defaultValue: 0   | Obtenho: 0
```

#### Source

src/utils/NumberUtils.ts:208

### getValueOrZero()

> `static` **getValueOrZero**(`value`): `number`

Obtém o valor ou zero, caso o valor seja inválido(NaN/undefined).

#### Parameters

• **value** : `any`

Numeral a ser validado.

#### Returns

`number`

  * O próprio numeral passado. Caso esse seja inválido retorna zero.

#### Source

src/utils/NumberUtils.ts:227

### keepOnlyDecimalSeparator()

> `static` **keepOnlyDecimalSeparator**(`value`, `formatnumber`): `string`

Retira os separadores de milhar de um numeral em formato de string.

#### Parameters

• **value** : `string`

Numeral em formato de string a ser convertido.

• **formatnumber** : `string`= `'pt-BR'`

Formatação de ENTRADA e SAÍDA do utilitário: pt-BR="###.###,##" en-US="###,###.##"; Default: "pt-BR".

#### Returns

`string`

  * Numeral em formato de string formatado apenas com separador decimal.

#### Example

```ts
Informado: '95.12' | Retorna: '9512'
```

#### Source

src/utils/NumberUtils.ts:158

### round()

> `static` **round**(`value`, `decimals`): `number`

Realiza o arredondamento de casas decimais de um numero.

#### Parameters

• **value** : `number`

Numeral a ser arredondado.

• **decimals** : `number`= `2`

Quantidade de casas decimais ussada no arredondamento.

#### Returns

`number`

  * O próprio numeral arredondado com a quantidade de casas decimais do argumento decimals.

#### Example

```ts
Informo: (100.12)       |   100.12
Informo: (100,12)       |   NaN

Informo: ("100.12", 1)  |   100.1
Informo: ("100.12", 2)  |   100.12
Informo: ("100.12", 3)  |   100.12

Informo: ("100.15", 1)  |   100.2
Informo: ("100.15", 2)  |   100.15
Informo: ("100.15", 3)  |   100.15

Informo: ("100.16", 1)  |   100.2
Informo: ("100.16", 2)  |   100.16
Informo: ("100.16", 3)  |   100.16
```

#### Source

src/utils/NumberUtils.ts:255

### safeFormat()

> `static` **safeFormat**(`value`, `precision`, `prettyPrecision`): `string`

Formata o numeral com a precisão informada e o valor default 0,00 caso o value não seja um numero valido.

#### Parameters

• **value** : `string`

Numeral em formato de string a ser convertido (Importante: formato PT-BR ou já em formato numérico - sem separador de milhares: ######.##).

• **precision** : `number`

Quantidade de casas decimais.

• **prettyPrecision** : `number`= `NaN`

Quantidade de zeros nos decimais.

#### Returns

`string`

  * Numeral em formato de String formatado em PT-BR.

#### Example

```ts
Informado: ('10,9845444', 3, 3) | Retorna: '10,985'
Informado: (undefined, 3, 3) | Retorna: 0,00
```

#### Source

src/utils/NumberUtils.ts:143

### stringToNumber()

> `static` **stringToNumber**(`value`): `number`

Converte o dado numérico de string para number.

#### Parameters

• **value** : `string`

Numeral em formato de string a ser convertido (Importante: formato PT-BR ou já em formato numérico: ######.##).

#### Returns

`number`

  * Numeral passado.

#### Example

```ts
@"100,12"     |       100.12
@"100.12"     |       100.12
@"-100,12"    |       -100.12
@"R$100,12"   |       100.12
@"-R$100,12"  |       -100.12
@"string"     |       NaN
```

#### Source

src/utils/NumberUtils.ts:22
