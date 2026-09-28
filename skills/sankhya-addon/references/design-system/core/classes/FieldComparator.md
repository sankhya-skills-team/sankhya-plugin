> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/FieldComparator (snapshot 2026-09-28)

# FieldComparator

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / FieldComparator

# Class: FieldComparator

## Constructors

### new FieldComparator()

> **new FieldComparator**(): `FieldComparator`

#### Returns

`FieldComparator`

## Methods

### compare()

> `static` **compare**(`field`, `recordA`, `recordB`, `asc`, `onlyLabel`): `number`

#### Parameters

• **field** : `FieldDescriptor`

• **recordA** : `Record`

• **recordB** : `Record`

• **asc** : `boolean`= `true`

• **onlyLabel** : `boolean`= `false`

#### Returns

`number`

#### Source

src/dataunit/sorting/FieldComparator.ts:7

### compareUndefined()

> `static` **compareUndefined**(`isUndefinedA`, `isUndefinedB`): `undefined` | `number`

#### Parameters

• **isUndefinedA** : `boolean`

• **isUndefinedB** : `boolean`

#### Returns

`undefined` | `number`

#### Source

src/dataunit/sorting/FieldComparator.ts:19

### compareValues()

> `static` **compareValues**(`descriptor`, `valueA`, `valueB`, `onlyLabel`): `number`

#### Parameters

• **descriptor** : `FieldDescriptor`

• **valueA** : `any`

• **valueB** : `any`

• **onlyLabel** : `boolean`= `false`

#### Returns

`number`

#### Source

src/dataunit/sorting/FieldComparator.ts:14
