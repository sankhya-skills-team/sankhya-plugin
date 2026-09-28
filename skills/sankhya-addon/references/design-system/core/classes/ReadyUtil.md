> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ReadyUtil (snapshot 2026-09-28)

# ReadyUtil

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ReadyUtil

# Class: ReadyUtil

`ReadyUtil`: Registra processos que serão invocados após a conclusão de operações.

## Constructors

### new ReadyUtil()

> **new ReadyUtil**(): `ReadyUtil`

#### Returns

`ReadyUtil`

## Properties

### promise

> `private` **promise** : `any`

#### Source

src/utils/ReadyUtil.ts:6

### resolve

> `private` **resolve** : `any`

#### Source

src/utils/ReadyUtil.ts:5

## Methods

### clean()

> `private` **clean**(): `void`

Limpa o estado da instancia ao finalizar a execução do processo registrado.

#### Returns

`void`

#### Source

src/utils/ReadyUtil.ts:11

### end()

> **end**(): `void`

Executa processo atribuído.

#### Returns

`void`

#### Source

src/utils/ReadyUtil.ts:28

### start()

> `private` **start**(): `void`

Inicializa o estado da instancia ao registrar processo.

#### Returns

`void`

#### Source

src/utils/ReadyUtil.ts:19

### whenReady()

> **whenReady**(): `Promise`<`unknown`>

Atribui processo que será executado por operações que o invocarem no método 'end'.

#### Returns

`Promise`<`unknown`>

Promise que deve conter o código do processo.

#### Source

src/utils/ReadyUtil.ts:36
