> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/KeyboardManager (snapshot 2026-09-28)

# KeyboardManager

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / KeyboardManager

# Class: KeyboardManager

`KeyboardManager` é reponsável por gerenciar eventos de teclado.

## Constructors

### new KeyboardManager()

> **new KeyboardManager**(`options`?): `KeyboardManager`

Construtor para a classe Keyboard.

#### Parameters

• **options?** : `Partial`<`IKeyboardOptions`>

opções para o gerenciamento de eventos de teclado.

#### Returns

`KeyboardManager`

#### Source

src/utils/KeyboardManager/index.ts:20

## Properties

### _mappedElements

> `private` **_mappedElements** : `IKeyboardMappedKeysElements` = `{}`

#### Source

src/utils/KeyboardManager/index.ts:13

### _options

> `private` **_options** : `IKeyboardOptions`

#### Source

src/utils/KeyboardManager/index.ts:11

### _shadowRoots

> `private` **_shadowRoots** : `ShadowRoot`[] = `[]`

#### Source

src/utils/KeyboardManager/index.ts:12

## Accessors

### mappedKeys

> `get` **mappedKeys**(): `IGetMappedKeys`[]

Obtém as chaves mapeadas.

#### Returns

`IGetMappedKeys`[]

chaves mapeadas com descrições

#### Source

src/utils/KeyboardManager/index.ts:154

## Methods

### addEventListenerToNestedShadowRoots()

> `private` **addEventListenerToNestedShadowRoots**(`event`, `callback`): `void`

#### Parameters

• **event** : `"keydown"` | `"keyup"`

• **callback** : `VoidFunction`

#### Returns

`void`

#### Source

src/utils/KeyboardManager/index.ts:56

### bind()

> **bind**(`keyMap`, `callback`, `options`?): `KeyboardManager`

Associa um evento de teclado com uma função

#### Parameters

• **keyMap** : `string`

Chave de mapeamento de teclado.

• **callback** : `VoidFunction`

Função a ser executada quando o evento de teclado for disparado.

• **options?** : `Partial`<`IKeyboardOptions`>

Configurações dos eventos de teclado.

#### Returns

`KeyboardManager`

O objeto `KeyboardManager`

#### Source

src/utils/KeyboardManager/index.ts:76

### checkModifiersIsApplied()

> `private` **checkModifiersIsApplied**(`event`, `modifiedList`): `boolean`

Verifica se todas as teclas modificadoras foram aplicadas ao evento

#### Parameters

• **event** : `KeyboardEvent`

O evento de teclado

• **modifiedList** : `string`[]

As teclas modificadoras

#### Returns

`boolean`

Retorna se todas as teclas modificadoras foram aplicadas

#### Source

src/utils/KeyboardManager/index.ts:223

### findAllNestedShadowRoots()

> `private` **findAllNestedShadowRoots**(`element`, `results`): `ShadowRoot`[]

#### Parameters

• **element** : `Element` | `Document` | `HTMLElement` | `ChildNode`

• **results** : `ShadowRoot`[]= `[]`

#### Returns

`ShadowRoot`[]

#### Source

src/utils/KeyboardManager/index.ts:35

### handleListenerEvent()

> `private` **handleListenerEvent**(`keyMap`, `callback`, `propagate`, `event`): `void`

Executa uma função quando um evento de teclado for disparado

#### Parameters

• **keyMap** : `string`

Chave de mapeamento de teclado

• **callback** : `VoidFunction`

Função a ser executada

• **propagate** : `boolean`

Se o evento de teclado deve ser propagado

• **event** : `KeyboardEvent`

O evento de teclado

#### Returns

`void`

#### Source

src/utils/KeyboardManager/index.ts:170

### keyAppliedWithModifiers()

> `private` **keyAppliedWithModifiers**(`keyMap`, `pressedKeyCode`): `IKeyAppliedResponse`

Verifica se um evento de teclado foi disparado

#### Parameters

• **keyMap** : `string`

Chave de mapeamento de teclado

• **pressedKeyCode** : `number`

Código do evento de teclado pressionado

#### Returns

`IKeyAppliedResponse`

Retorna se o evento de teclado foi disparado e as teclas modificadoras aplicadas ao evento

#### Source

src/utils/KeyboardManager/index.ts:186

### removeEventListenerToNestedShadowRoots()

> `private` **removeEventListenerToNestedShadowRoots**(`event`, `callback`): `void`

#### Parameters

• **event** : `"keydown"` | `"keyup"`

• **callback** : `VoidFunction`

#### Returns

`void`

#### Source

src/utils/KeyboardManager/index.ts:62

### unbind()

> **unbind**(`keyMap`): `KeyboardManager`

Remove um evento de teclado

#### Parameters

• **keyMap** : `string`

Chave de mapeamento de teclado.

#### Returns

`KeyboardManager`

  * O objeto `KeyboardManager`

#### Source

src/utils/KeyboardManager/index.ts:126

### unbindAllShortcutKeys()

> **unbindAllShortcutKeys**(`listShortcutKeys`?): `void`

Remove todos os eventos de teclado ou de uma lista informada

#### Parameters

• **listShortcutKeys?** : `string`[]

#### Returns

`void`

#### Source

src/utils/KeyboardManager/index.ts:115

### verifyAndStopPropagation()

> `private` **verifyAndStopPropagation**(`event`, `propagate`): `void`

Verifica e impede que o evento de teclado seja propagado

#### Parameters

• **event** : `KeyboardEvent`

O evento de teclado

• **propagate** : `boolean`

Se o evento de teclado deve ser propagado

#### Returns

`void`

#### Source

src/utils/KeyboardManager/index.ts:259
