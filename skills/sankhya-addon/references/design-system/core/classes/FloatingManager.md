> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/FloatingManager (snapshot 2026-09-28)

# FloatingManager

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / FloatingManager

# Class: FloatingManager

`FloatingManager`: Gerenciador de elementos flutuantes na tela.

## Constructors

### new FloatingManager()

> **new FloatingManager**(): `FloatingManager`

#### Returns

`FloatingManager`

## Properties

### DATA_OLD_ZINDEX_ATTRIBUTE_NAME

> `static` **DATA_OLD_ZINDEX_ATTRIBUTE_NAME** : `string` = `"data-old-zindex"`

#### Source

src/ui/FloatingManager.ts:70

### MODAL_DEFAULT_CLASSNAME

> `static` **MODAL_DEFAULT_CLASSNAME** : `string` = `"FloatingManager__modal"`

#### Source

src/ui/FloatingManager.ts:67

### MODAL_ELEMENT_ID

> `static` **MODAL_ELEMENT_ID** : `string` = `"FloatingManager__overlay"`

#### Source

src/ui/FloatingManager.ts:68

### STYLE_ELEMENT_ID

> `static` **STYLE_ELEMENT_ID** : `string` = `"FloatingManager__style"`

#### Source

src/ui/FloatingManager.ts:69

### entries

> `static` `private` **entries** : `FloatingEntry`[]

#### Source

src/ui/FloatingManager.ts:73

### initialized

> `static` `private` **initialized** : `boolean`

#### Source

src/ui/FloatingManager.ts:72

### overlayElements

> `static` `private` **overlayElements** : `HTMLElement`[] = `[]`

#### Source

src/ui/FloatingManager.ts:74

## Methods

### applyStyle()

> `static` `private` **applyStyle**(`element`, `propertyName`, `value`?): `void`

Adiciona uma propriedade CSS em um elemento HTML.

#### Parameters

• **element** : `HTMLElement`

Elemento HTML que será modificado.

• **propertyName** : `string`

Nome da propriedade CSS que será adicionada.

• **value?** : `string`

Valor da propriedade adicionada.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:179

### close()

> `static` **close**(`id`): `void`

Fecha elemento flutuante da tela.

#### Parameters

• **id** : `number`

Índice do elemento desejado.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:374

### closeAll()

> `static` **closeAll**(): `void`

Fecha todos os elemento flutuante da tela.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:383

### createOrUpdatOverlay()

> `static` `private` **createOrUpdatOverlay**(`className`): `HTMLDivElement`

Cria ou atualiza o elemento de sobreposição.

#### Parameters

• **className** : `string`= `FloatingManager.MODAL_DEFAULT_CLASSNAME`

Classe CSS que será adicionada ao modal.

#### Returns

`HTMLDivElement`

  * O elemento atualizado.

#### Source

src/ui/FloatingManager.ts:297

### createStyleElement()

> `static` `private` **createStyleElement**(): `void`

Cria elemento de estilo. Elemento que define o estilo padrão do elemento de sobreposição.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:324

### doClose()

> `static` `private` **doClose**(`id`, `entry`, `target`?, `event`?): `void`

Fecha uma entrada flutuante (FloatingManager).

#### Parameters

• **id** : `number`

Código da entrada que se deseja encerrar.

• **entry** : `FloatingEntry`

FloatingManager.

• **target?** : `HTMLElement`

Elemento HTML referente.

• **event?** : `Event`

Evento específico que será verificado, como clique do mouse.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:116

### float()

> `static` **float**(`content`, `parent`, `options`): `number`

Cria e exibe um novo item no FloatingManager.

#### Parameters

• **content** : `HTMLElement`

Elemento HTML que será criado.

• **parent** : `HTMLElement`

Elemento HTML que será o pai do item a ser criado.

• **options** : `FloatingOptions`= `undefined`

Opções de configuração a serem adicionadas.

#### Returns

`number`

  * ID do novo item criado.

#### Source

src/ui/FloatingManager.ts:228

### getCSSPropertyValue()

> `static` `private` **getCSSPropertyValue**(`element`, `property`): `string`

#### Parameters

• **element** : `HTMLElement`

• **property** : `string`

#### Returns

`string`

#### Source

src/ui/FloatingManager.ts:422

### getFloatIndex()

> `static` `private` **getFloatIndex**(`content`, `parent`): `number`

Obtém o índice do FloatingManager do Elemento HMTL desejado.

#### Parameters

• **content** : `HTMLElement`

Elemento a ser buscado.

• **parent** : `HTMLElement`

Elemento pai do content a ser buscado.

#### Returns

`number`

  * Índice do elemento informado.

#### Source

src/ui/FloatingManager.ts:193

### getHighestZIndex()

> `static` `private` **getHighestZIndex**(): `number`

#### Returns

`number`

#### Source

src/ui/FloatingManager.ts:426

### handleDocumentEvent()

> `static` `private` **handleDocumentEvent**(`event`): `void`

Fecha todas as FloatingManagers abertas.

#### Parameters

• **event** : `Event`

Evento ocorrido, como clique do mouse, por exemplo.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:143

### handleKeyboardEvent()

> `static` `private` **handleKeyboardEvent**(`event`): `void`

Captura eventos de teclado para manipular os elementos flutuantes via eventos da tecla pressionada.

#### Parameters

• **event** : `KeyboardEvent`

Evento de teclado.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:157

### hideOverlay()

> `static` `private` **hideOverlay**(): `void`

Desfaz o desfoque/overlay dos elementos na tela.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:274

### init()

> `static` `private` **init**(): `void`

Inicializa a classe FloatingManager.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:82

### innerClick()

> `static` `private` **innerClick**(`container`, `node`): `boolean`

Retorna se o elemento clicado possui elementos internos.

#### Parameters

• **container** : `HTMLElement`

• **node** : `HTMLElement`

#### Returns

`boolean`

#### Source

src/ui/FloatingManager.ts:94

### isFloating()

> `static` **isFloating**(`id`): `boolean`

Retorna se uma entrada flutuante existe.

#### Parameters

• **id** : `number`

Índice para ser verificado no FloatingManager.

#### Returns

`boolean`

  * Verdadeiro se existir.

#### Source

src/ui/FloatingManager.ts:213

### showOverlay()

> `static` `private` **showOverlay**(`options`): `void`

Aplica o desfoque na página se o elemento possuir essa option ativada.

#### Parameters

• **options** : `FloatingOptions`

Configurações que serão utilizadas no elemento.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:262

### subscribeOverlayControl()

> `static` **subscribeOverlayControl**(`item`): `undefined` | `number`

Controle a sobreposição do elemento

#### Parameters

• **item** : `HTMLElement`

Elemento HTML que será manipulado

#### Returns

`undefined` | `number`

  * O ID do elemento na lista de controle

#### Source

src/ui/FloatingManager.ts:397

### unsubscribeOverlayControl()

> `static` **unsubscribeOverlayControl**(`identifier`): `void`

#### Parameters

• **identifier** : `number` | `HTMLElement`

Elemento HTML ou ID do item que será removido do controle de sobreposição

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:412

### updateFloatPosition()

> `static` **updateFloatPosition**(`content`, `parent`, `options`): `void`

Atualiza posição de um elemento que já está em tela.

#### Parameters

• **content** : `HTMLElement`

Elemento HTML que será atualizado.

• **parent** : `HTMLElement`

Elemento pai do content passado.

• **options** : `FloatingOptions`= `undefined`

Novas opções desejadas.

#### Returns

`void`

#### Source

src/ui/FloatingManager.ts:356
