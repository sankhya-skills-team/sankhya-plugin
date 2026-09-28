> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/WarningException (snapshot 2026-09-28)

# WarningException

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / WarningException

# Class: WarningException

`WarningException`: Exceção lançada quando o "erro" vindo do backend é caracterizado como warning.

## Extends

  * `Error`

## Constructors

### new WarningException()

> **new WarningException**(`title`, `message`, `errorCode`): `WarningException`

#### Parameters

• **title** : `string`

• **message** : `string`

• **errorCode** : `string`= `""`

#### Returns

`WarningException`

#### Overrides

`Error.constructor`

#### Source

src/exceptions/WarningException.ts:18

## Properties

### cause?

> `optional` **cause** : `unknown`

#### Inherited from

`Error.cause`

#### Source

node_modules/typescript/lib/lib.es2022.error.d.ts:26

### errorCode

> **errorCode** : `string`

Código do alerta, indica o alerta disparado pelo backend.

#### Source

src/exceptions/WarningException.ts:16

### message

> **message** : `string`

Descrição do alerta.

#### Overrides

`Error.message`

#### Source

src/exceptions/WarningException.ts:13

### name

> **name** : `string`

Nome da exceção.

#### Overrides

`Error.name`

#### Source

src/exceptions/WarningException.ts:7

### stack?

> `optional` **stack** : `string`

#### Inherited from

`Error.stack`

#### Source

node_modules/typescript/lib/lib.es5.d.ts:1055

### title

> **title** : `string`

Titulo do alerta.

#### Source

src/exceptions/WarningException.ts:10

### prepareStackTrace()?

> `static` `optional` **prepareStackTrace** : (`err`, `stackTraces`) => `any`

Optional override for formatting stack traces

#### See

<https://v8.dev/docs/stack-trace-api#customizing-stack-traces>

#### Parameters

• **err** : `Error`

• **stackTraces** : `CallSite`[]

#### Returns

`any`

#### Inherited from

`Error.prepareStackTrace`

#### Source

node_modules/@types/node/globals.d.ts:27

### stackTraceLimit

> `static` **stackTraceLimit** : `number`

#### Inherited from

`Error.stackTraceLimit`

#### Source

node_modules/@types/node/globals.d.ts:29

## Methods

### captureStackTrace()

> `static` **captureStackTrace**(`targetObject`, `constructorOpt`?): `void`

Create .stack property on a target object

#### Parameters

• **targetObject** : `object`

• **constructorOpt?** : `Function`

#### Returns

`void`

#### Inherited from

`Error.captureStackTrace`

#### Source

node_modules/@types/node/globals.d.ts:20
