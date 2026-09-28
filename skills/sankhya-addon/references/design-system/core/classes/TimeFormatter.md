> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/TimeFormatter (snapshot 2026-09-28)

# TimeFormatter

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / TimeFormatter

# Class: TimeFormatter

`TimeFormatter`: Utilizado para formatar horas.

## Constructors

### new TimeFormatter()

> **new TimeFormatter**(): `TimeFormatter`

#### Returns

`TimeFormatter`

## Properties

### _maskFormatter

> `static` **_maskFormatter** : `MaskFormatter`

#### Source

src/utils/TimeFormatter.ts:8

## Methods

### prepareValue()

> `static` **prepareValue**(`value`, `showSeconds`): `string`

Converte um texto para o formato de hora.

#### Parameters

• **value** : `string`

Texto não formatado.

• **showSeconds** : `boolean`

Se será validado os segundos.

#### Returns

`string`

  * Texto em formato de hora.

#### Exemples

@"1012" | "10:12" @"10:12" | "10:12:00" @"100112" | "10:01:12"

#### Source

src/utils/TimeFormatter.ts:22

### validateTime()

> `static` **validateTime**(`value`, `showSeconds`): `boolean`

Retorna se o texto está no formato de hora.

#### Parameters

• **value** : `string`

Texto a ser validado.

• **showSeconds** : `boolean`

Se será validado os segundos.

#### Returns

`boolean`

  * Verdadeiro para valores no formato de hora e False para formatos diferentes.

#### Exemples

@"1012" | true @"14e4" | false @"2624" | false

#### Source

src/utils/TimeFormatter.ts:64
