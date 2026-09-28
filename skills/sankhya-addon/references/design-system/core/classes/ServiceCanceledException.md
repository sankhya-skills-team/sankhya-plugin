> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ServiceCanceledException (snapshot 2026-09-28)

# ServiceCanceledException

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ServiceCanceledException

# Class: ServiceCanceledException

`ServiceCanceledException`: Exceção lançada quando ocorre o cancelamento de um serviço.

## Extends

  * `Error`

## Constructors

### new ServiceCanceledException()

> **new ServiceCanceledException**(`title`, `message`, `errorCode`): `ServiceCanceledException`

#### Parameters

• **title** : `string`

• **message** : `string`

• **errorCode** : `string`= `""`

#### Returns

`ServiceCanceledException`

#### Overrides

`Error.constructor`

#### Source

src/exceptions/ServiceCanceledException.ts:18

## Properties

### cause?

> `optional` **cause** : `unknown`

#### Inherited from

`Error.cause`

#### Source

node_modules/typescript/lib/lib.es2022.error.d.ts:26

### errorCode

> **errorCode** : `string`

Código do erro, indica o erro disparado pelo backend.

#### Source

src/exceptions/ServiceCanceledException.ts:16

### message

> **message** : `string`

Descrição do erro.

#### Overrides

`Error.message`

#### Source

src/exceptions/ServiceCanceledException.ts:13

### name

> **name** : `string`

Nome da exceção.

#### Overrides

`Error.name`

#### Source

src/exceptions/ServiceCanceledException.ts:7

### stack?

> `optional` **stack** : `string`

#### Inherited from

`Error.stack`

#### Source

node_modules/typescript/lib/lib.es5.d.ts:1055

### title

> **title** : `string`

Titulo do erro.

#### Source

src/exceptions/ServiceCanceledException.ts:10

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
