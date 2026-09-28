> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DateUtils (snapshot 2026-09-28)

# DateUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / DateUtils

# Class: DateUtils

`DateUtils`: Utilizado para formatação, padronização e cálculos de datas.

## Constructors

### new DateUtils()

> **new DateUtils**(): `DateUtils`

#### Returns

`DateUtils`

## Methods

### adjustDLST()

> `static` `private` **adjustDLST**(`date`): `Date`

Realiza correção do horário de verão.

#### Parameters

• **date** : `Date`

Data a ser ajustada.

#### Returns

`Date`

  * Data informada ajustada para horário de verão.

#### Source

src/utils/DateUtils.ts:139

### clearTime()

> `static` **clearTime**(`date`, `adjustDayLightSavingTime`): `Date`

Zerar o horário de uma data.

#### Parameters

• **date** : `Date`

Data a ser manipulada.

• **adjustDayLightSavingTime** : `boolean`= `true`

Ajusta horário de verão na data recebida.

#### Returns

`Date`

  * Data sem as informações de horário.

#### Example

```ts
Informo: 2023-03-09 12:42:40      | Obtenho: 2023-03-09 00:00:00
```

#### Source

src/utils/DateUtils.ts:15

### formatDate()

> `static` **formatDate**(`date`, `options`?): `string`

Converte data para uma string no formato pt-BR.

#### Parameters

• **date** : `Date`

Data a ser convertida.

• **options?** : `DateTimeFormatOptions`

Opções de formatação da data.

#### Returns

`string`

  * Uma string com a data no formato pt-BR DD/MM/YYYY.

#### Source

src/utils/DateUtils.ts:27

### formatDateTime()

> `static` **formatDateTime**(`date`, `showSeconds`): `string`

Converte a data e hora para uma string no formato pt-BR.

#### Parameters

• **date** : `Date`

Data a ser convertida.

• **showSeconds** : `boolean`= `false`

define se devemos considerar os segundos.

#### Returns

`string`

  * Uma string com as horas no formato DD/MM/YYYY HH:MM ou DD/MM/YYYY HH:MM:SS.

#### Source

src/utils/DateUtils.ts:56

### formatRfc3339()

> `static` **formatRfc3339**(`date`): `string`

Converte a data para o formato RFC3339.

#### Parameters

• **date** : `Date`

Data a ser convertida

#### Returns

`string`

  * Data informada no formato RFC3339.

  *

#### Example

```ts
Informo: 2023-03-09 12:42:40     | Obtenho: 2023-03-09T12:42:47-03:00
```

#### Source

src/utils/DateUtils.ts:189

### formatTime()

> `static` **formatTime**(`date`, `showSeconds`): `string`

Converte as horas de uma data para uma string pt-BR.

#### Parameters

• **date** : `Date`

Data a ser convertida.

• **showSeconds** : `boolean`= `false`

define se devemos considerar os segundos.

#### Returns

`string`

  * Uma string com as horas no formato HH:MM ou HH:MM:SS.

#### Source

src/utils/DateUtils.ts:41

### getToday()

> `static` **getToday**(`withTime`): `Date`

Obtém a data atual.

#### Parameters

• **withTime** : `boolean`= `false`

Caso true retorna a data com informações de horário.

#### Returns

`Date`

  * Data atual sem informação de horário.

#### Source

src/utils/DateUtils.ts:110

### pad()

> `static` `private` **pad**(`n`): `string` | `number`

Adiciona uma casa decimal a esquerda de uma unidade.

#### Parameters

• **n** : `number`

Número a ser ajustado

#### Returns

`string` | `number`

  * O número informado, com uma casa decimal a esquerda.

#### Examples

```ts
Informo: 15     | Obtenho: 15
```

```ts
Informo:  2     | Obtenho: "02"
```

#### Source

src/utils/DateUtils.ts:158

### strToDate()

> `static` **strToDate**(`strValue`, `adjustDayLightSavingTime`, `monthYearMode`): `undefined` | `Date`

Converte String para Date.

#### Parameters

• **strValue** : `string`

Texto a ser convertido para data.

• **adjustDayLightSavingTime** : `boolean`= `true`

Se verdadeiro, ativa regra de horário de verão.

• **monthYearMode** : `boolean`= `false`

Quando ativado, retorna o primeiro dia do mês apenas para construir a data.

#### Returns

`undefined` | `Date`

  * Data sem as informações de horário.

#### Source

src/utils/DateUtils.ts:68

### timezoneOffset()

> `static` `private` **timezoneOffset**(`offset`): `string`

Retorna timezone da data.

#### Parameters

• **offset** : `number`

Valor do timezone desejado.

#### Returns

`string`

Timezone da data.

#### Source

src/utils/DateUtils.ts:168

### validateDate()

> `static` **validateDate**(`value`, `hasTime`): `undefined` | `Date`

Retorna se a data é válida.

#### Parameters

• **value** : `Date`

Data a ser validada.

• **hasTime** : `boolean`= `false`

Determina se a data retornada deve conter informação de horário ou não. Por padrão não retorna a hora.

#### Returns

`undefined` | `Date`

  * Caso válida, retorna a própria data.

#### Source

src/utils/DateUtils.ts:127
