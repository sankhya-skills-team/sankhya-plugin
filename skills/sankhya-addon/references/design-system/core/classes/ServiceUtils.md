> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ServiceUtils (snapshot 2026-09-28)

# ServiceUtils

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ServiceUtils

# Class: ServiceUtils

## Constructors

### new ServiceUtils()

> **new ServiceUtils**(): `ServiceUtils`

#### Returns

`ServiceUtils`

## Methods

### useCacheWithService()

> `static` **useCacheWithService** <`T`>(`identifier`, `fetchFunction`, `storageType`): `Promise`<`T`>

Auxilia no uso do CacheManager, gerando automaticamente uma chave de cache com base no identificador.

#### Type parameters

• **T**

Tipo do dado a ser retornado.

#### Parameters

• **identifier** : `string`

Identificadores únicos usados para compor a chave de cache.

• **fetchFunction**

Função que retorna uma `Promise` com o valor a ser armazenado no cache caso ele não exista ou tenha expirado.

• **storageType** : `StorageType`= `StorageType.IN_MEMORY_CACHE`

Tipo de armazenamento: `'sessionStorage'` ou `'localStorage'`. O padrão é `'sessionStorage'`.

#### Returns

`Promise`<`T`>

Uma `Promise` com o valor armazenado ou obtido via `fetchFunction`.

#### Example

```typescript
const actions = await useCacheWithService(
 `${this.entityName} - ${this.resourceID}`,
  async () => {
    return await fetchActionsFromAPI();
  }
);
console.log(actions);
```

#### Source

src/utils/ServiceUtils.ts:28
