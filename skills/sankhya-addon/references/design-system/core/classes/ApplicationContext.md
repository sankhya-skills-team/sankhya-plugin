> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ApplicationContext (snapshot 2026-09-28)

# ApplicationContext

**@sankhyalabs/core** • **Docs**

@sankhyalabs/core / ApplicationContext

# Class: ApplicationContext

`ApplicationContext`: Utilizado para manipulação do contexto.

  * Evitar uso da classe sem alinhamento com a arquitetura devido ao uso de variáveis globais.

## Constructors

### new ApplicationContext()

> **new ApplicationContext**(): `ApplicationContext`

#### Returns

`ApplicationContext`

## Methods

### getContextValue()

> `static` **getContextValue**(`key`): `any`

Obtém informação específica do contexto.

#### Parameters

• **key** : `string`

Chave do contexto desejada.

#### Returns

`any`

  * Informação do contexto desejado.

#### Source

src/utils/ApplicationContext.ts:13

### getCtx()

> `static` `private` **getCtx**(): `any`

Obtém o contexto global da aplicação sankhyacore.

  * Esse contexto pode ser entendido como um ponto de coesão para atores que não se conhecem poderem trocar informação. Assim, o código x busca por um possível valor no contexto. Se essa informação estiver lá, ele reage de certa forma. O código Y, sabe dessa necessidade mas não consegue passar essa informação diretamente, então atribui o valor ao contexto.

#### Returns

`any`

  * Objeto com as propriedades da variável global _**snkcore___ctx**_.

#### Source

src/utils/ApplicationContext.ts:32

### setContextValue()

> `static` **setContextValue**(`key`, `value`): `any`

Aplica informação no contexto.

#### Parameters

• **key** : `string`

Identificador do contexto.

• **value** : `any`

Informação a ser inserida no contexto.

#### Returns

`any`

#### Source

src/utils/ApplicationContext.ts:23
