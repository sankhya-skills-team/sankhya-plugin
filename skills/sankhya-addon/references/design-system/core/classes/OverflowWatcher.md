> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/OverflowWatcher (snapshot 2026-09-28)

# OverflowWatcher

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / OverflowWatcher

# Class: OverflowWatcher

## Constructors

### new OverflowWatcher()

> **new OverflowWatcher**(`__namedParameters`): `OverflowWatcher`

Cria uma instancia do OverflowWatcher

#### Parameters

• **__namedParameters** : `OverFlowWatcherParams`

#### Returns

`OverflowWatcher`

#### Source

src/utils/OverflowWatcher/index.ts:35

## Properties

### DATA_ELEMENT_ID

> `readonly` **DATA_ELEMENT_ID** : `"data-element-id"` = `'data-element-id'`

#### Source

src/utils/OverflowWatcher/index.ts:23

### _deltaSize

> `private` **_deltaSize** : `number`

#### Source

src/utils/OverflowWatcher/index.ts:20

### _hiddenItemsProps

> `private` **_hiddenItemsProps** : `Map`<`Element`, `SizeProps`>

#### Source

src/utils/OverflowWatcher/index.ts:18

### _lastContainerInstance

> `private` **_lastContainerInstance** : `undefined` | `HTMLElement` = `undefined`

#### Source

src/utils/OverflowWatcher/index.ts:15

### _lastContainerSize

> `private` **_lastContainerSize** : `undefined` | `number` = `undefined`

#### Source

src/utils/OverflowWatcher/index.ts:14

### _notOverFlow

> `private` **_notOverFlow** : `string`[] = `[]`

#### Source

src/utils/OverflowWatcher/index.ts:21

### _notOverFlowPros

> `private` **_notOverFlowPros** : `Map`<`string`, `SizeProps`>

#### Source

src/utils/OverflowWatcher/index.ts:19

### _onResize

> `private` **_onResize** : `OnOverflowCallBack`

#### Source

src/utils/OverflowWatcher/index.ts:12

### _propSize

> `private` **_propSize** : `string`

#### Source

src/utils/OverflowWatcher/index.ts:17

### _resizeObserver

> `private` **_resizeObserver** : `ResizeObserver`

#### Source

src/utils/OverflowWatcher/index.ts:13

### _scrollDirection

> `private` **_scrollDirection** : `OverflowDirection` = `OverflowDirection.HORIZONTAL`

#### Source

src/utils/OverflowWatcher/index.ts:16

## Methods

### addNotOverFlowElement()

> **addNotOverFlowElement**(`elementId`): `void`

#### Parameters

• **elementId** : `string`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:52

### calcChildrenSize()

> `private` **calcChildrenSize**(`children`): `number`

#### Parameters

• **children** : `Element`[]

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:221

### calcContainerSize()

> `private` **calcContainerSize**(`container`): `number`

#### Parameters

• **container** : `Element`

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:257

### calcElementSize()

> `private` **calcElementSize**(`el`): `number`

#### Parameters

• **el** : `Element`

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:272

### calculateVariation()

> `private` **calculateVariation**(`elementIdsToCalculate`): `number`

#### Parameters

• **elementIdsToCalculate** : `string`[]

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:193

### canNotOverFlowNotIncludedIds()

> `private` **canNotOverFlowNotIncludedIds**(`elements`): `string`[]

#### Parameters

• **elements** : `Element`[]

#### Returns

`string`[]

#### Source

src/utils/OverflowWatcher/index.ts:203

### canNotRegisterNotOverFlow()

> `private` **canNotRegisterNotOverFlow**(`id`): `boolean`

#### Parameters

• **id** : `string`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:111

### canOverFlowElement()

> `private` **canOverFlowElement**(`element`): `boolean`

#### Parameters

• **element** : `Element`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:173

### clearOverFlow()

> `private` **clearOverFlow**(): `void`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:141

### destroy()

> **destroy**(): `void`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:58

### exceedsAvaliableSize()

> `private` **exceedsAvaliableSize**(`sumElementsSize`, `elements`, `avaliableSize`): `boolean`

#### Parameters

• **sumElementsSize** : `number`

• **elements** : `Element`[]

• **avaliableSize** : `number`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:182

### forceUpdate()

> **forceUpdate**(): `void`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:62

### getDataElementId()

> `private` **getDataElementId**(`element`): `string`

#### Parameters

• **element** : `Element`

#### Returns

`string`

#### Source

src/utils/OverflowWatcher/index.ts:178

### getElementSizeProps()

> `private` **getElementSizeProps**(`element`): `SizeProps`

#### Parameters

• **element** : `Element`

#### Returns

`SizeProps`

#### Source

src/utils/OverflowWatcher/index.ts:213

### getProcessableElements()

> `private` **getProcessableElements**(`container`): `Element`[]

#### Parameters

• **container** : `HTMLElement`

#### Returns

`Element`[]

#### Source

src/utils/OverflowWatcher/index.ts:88

### groupElementsByContainer()

> `private` **groupElementsByContainer**(`elements`): `Map`<`null` | `Element`, `Element`[]>

#### Parameters

• **elements** : `Element`[]

#### Returns

`Map`<`null` | `Element`, `Element`[]>

#### Source

src/utils/OverflowWatcher/index.ts:243

### handleResize()

> `private` **handleResize**(`entries`): `void`

#### Parameters

• **entries** : `ResizeObserverEntry`[]

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:68

### hasChangedSize()

> `private` **hasChangedSize**(`elementSize`): `boolean`

#### Parameters

• **elementSize** : `number`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:115

### isElementOverFlowing()

> `private` **isElementOverFlowing**(`elementsThatFit`, `element`): `boolean`

#### Parameters

• **elementsThatFit** : `Element`[]

• **element** : `Element`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:169

### isOverFlowed()

> `private` **isOverFlowed**(`el`): `boolean`

#### Parameters

• **el** : `Element`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:286

### proccessElements()

> `private` **proccessElements**(`elementSize`, `children`): `void`

#### Parameters

• **elementSize** : `number`

• **children** : `Element`[]

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:127

### proccessElementsOverFlow()

> `private` **proccessElementsOverFlow**(`allElements`, `avaliableSize`): `void`

#### Parameters

• **allElements** : `Element`[]

• **avaliableSize** : `number`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:146

### registerElementSize()

> `private` **registerElementSize**(`element`): `void`

#### Parameters

• **element** : `Element`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:208

### registerNotOverflowProps()

> `private` **registerNotOverflowProps**(`children`): `void`

#### Parameters

• **children** : `Element`[]

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:103

### updateOverFlowedItems()

> `private` **updateOverFlowedItems**(`container`, `containerSize`): `void`

#### Parameters

• **container** : `HTMLElement`

• **containerSize** : `number`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:80
