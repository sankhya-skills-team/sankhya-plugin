> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/OnboardingUtils (snapshot 2026-09-28)

# OnboardingUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / OnboardingUtils

# Class: OnboardingUtils

## Constructors

### new OnboardingUtils()

> `private` **new OnboardingUtils**(): `OnboardingUtils`

#### Returns

`OnboardingUtils`

#### Source

src/utils/OnboardingUtils.ts:5

## Properties

### USER_GUIDE_TAG_ID

> `static` `private` `readonly` **USER_GUIDE_TAG_ID** : `"userGuideSnippet"` = `"userGuideSnippet"`

#### Source

src/utils/OnboardingUtils.ts:2

### instance

> `static` `private` **instance** : `OnboardingUtils`

#### Source

src/utils/OnboardingUtils.ts:3

## Methods

### init()

> **init**(`apiKey`, `ctx`): `Promise`<`void`>

#### Parameters

• **apiKey** : `string`

• **ctx** : `EnvironmentContext`

#### Returns

`Promise`<`void`>

#### Source

src/utils/OnboardingUtils.ts:14

### injectScript()

> `private` **injectScript**(`apiKey`): `void`

#### Parameters

• **apiKey** : `string`

#### Returns

`void`

#### Source

src/utils/OnboardingUtils.ts:23

### register()

> `private` **register**(`ctx`): `void`

#### Parameters

• **ctx** : `EnvironmentContext`

#### Returns

`void`

#### Source

src/utils/OnboardingUtils.ts:34

### getInstance()

> `static` **getInstance**(): `OnboardingUtils`

#### Returns

`OnboardingUtils`

#### Source

src/utils/OnboardingUtils.ts:7
