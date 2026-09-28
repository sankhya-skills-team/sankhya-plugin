> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-personalized-filter/ (snapshot 2026-09-28)

# Personalized Filter

O componente **snk-personalized-filter** é responsável pela criação, edição e gerenciamento de filtros personalizados no Sankhya EIP. Ele oferece recursos avançados para que os usuários possam definir critérios de filtragem customizados, facilitando a localização e visualização de registros relevantes conforme suas necessidades.

Com suporte aos modos **Assistente** e **Avançado** , o componente permite tanto a criação guiada de filtros quanto a edição livre de expressões, proporcionando flexibilidade para diferentes perfis de usuários.

## Quando usar

  * Quando for necessário permitir que usuários criem, editem ou gerenciem filtros personalizados para refinar a busca e a visualização de dados em telas do Sankhya EIP.
  * Quando a aplicação precisar oferecer flexibilidade para salvar diferentes conjuntos de critérios de filtragem, reutilizáveis em consultas futuras.
  * Em cenários em que a experiência do usuário pode ser aprimorada com filtros avançados, agrupamento de condições e expressões customizadas.

## Quando não usar

  * Não utilize o `snk-personalized-filter` diretamente em aplicações. Sempre prefira o uso do componente `SnkFilterBar`, que já incorpora toda a lógica e integração necessárias.
  * Não utilize para filtros simples ou estáticos, em que não há necessidade de personalização ou salvamento de critérios pelo usuário.
  * Evite o uso em contextos em que a complexidade de filtros personalizados não agrega valor à experiência do usuário final.

## Modo Assistente

No modo **Assistente** , é possível criar expressões em grupos de maneira ágil e orientada, permitindo a adição de expressões vizinhas ou o cadastro de grupos de expressões. Na parte inferior, o painel _"Expressão a ser aplicada"_ exibe, em tempo real, o resultado da configuração.

## Modo Avançado

No modo **Avançado** , o usuário pode escrever livremente a expressão desejada. Para facilitar, há um botão _"Adicionar campo"_ que permite buscar e inserir o nome do campo na posição desejada dentro da expressão.

# Exemplo de uso

Para utilizar o componente, pode-se implementá-lo da seguinte forma:

```jsx
import { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    const handleCancelFilter = () => {
        ApplicationUtils.message("Cancel", "Evento de cancelamento executado.");
    }

    const handleSaveFilter = (filterId) => {
        ApplicationUtils.message("Save", `Salvo com sucesso. Expressão: ${filterId.detail}`);
    }

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                onEzCancel={handleCancelFilter}
                onEzSave={handleSaveFilter}
            />
        </SnkApplication>
    )
};

export default Demo;
```

## Métodos

### createPersonalizedFilter

Método responsável por criar um novo filtro personalizado.

```jsx
import { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
            />
        </SnkApplication>
    )
};

export default Demo;
```

## Propriedades

### entityUri

> Propriedade: `entityUri`

Define a entidade utilizada para buscar os campos disponíveis para filtro.

```jsx
import React, { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
            />
        </SnkApplication>
    )
};

export default Demo;
```

### filterId

> Propriedade: `filterId`

Define o identificador do filtro a ser carregado.

```jsx
import { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                filterId='br.com.sankhya.fin.cad.movimentacaoBancaria.filter-01'
            />
        </SnkApplication>
    )
};

export default Demo;
```

### configName

> Propriedade: `configName`

Define o nome da configuração, útil para distinguir múltiplas instâncias do componente.

```jsx
import React, { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
            />
        </SnkApplication>
    )
};

export default Demo;
```

### resourceID

> Propriedade: `resourceID`

Define o identificador do recurso utilizado para salvar e recuperar filtros.

```jsx
import { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                resourceID="br.com.sankhya.fin.cad.movimentacaoBancaria"
            />
        </SnkApplication>
    )
};

export default Demo;
```

### isDefaultFilter

> Propriedade: `isDefaultFilter`

Indica se o filtro é o filtro padrão do sistema.

```jsx
import React, { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    const handleSaveFilter = (filterId) => {
        ApplicationUtils.message("Save", `Salvo com sucesso. Expressão: ${filterId.detail}`);
    }

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                isDefaultFilter={true}
                onEzSave={handleSaveFilter}
            />
        </SnkApplication>
    )
};

export default Demo;
```

## Eventos

### onEzCancel

> Evento: `onEzCancel`

Emitido ao realizar uma ação de cancelamento, seja por meio do botão 'Cancelar' ou do botão 'Retornar'.

```jsx
import { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    const handleCancelFilter = () => {
        ApplicationUtils.message("Cancel", "Evento de cancelamento executado.");
    }

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                onEzCancel={handleCancelFilter}
            />
        </SnkApplication>
    )
};

export default Demo;
```

### onEzSave

> Evento: `onEzSave`

Emitido ao cadastrar ou editar um filtro.

```jsx
import { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    const handleSaveFilter = (filterId) => {
        ApplicationUtils.message("Save", `Salvo com sucesso. Expressão: ${filterId.detail}`);
    }

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                onEzSave={handleSaveFilter}
            />
        </SnkApplication>
    )
};

export default Demo;
```

### onEzAfterSave

> Evento: `onEzAfterSave`

Evento emitido após salvar as alterações do filtro personalizado. Pode ser utilizado para exibir mensagens de sucesso ou executar outras ações.

```jsx
import React, { useRef, useEffect } from 'react';
import { SnkApplication, SnkPersonalizedFilter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const elPersonalizedFilter = useRef(null);

    const entityUri = 'dd://MovimentoBancario/br.com.sankhya.fin.cad.movimentacaoFinanceira?uuid=9d0c2f82-ae2b-4d20-b28f-552c68296efe';
    const configName = 'MovimentoBancario';

    const handleAfterSave = () => {
      alert("Filtro salvo com sucesso!");
    };

    useEffect(() => {
        elPersonalizedFilter.current.createPersonalizedFilter();
    }, []);

    return (
        <SnkApplication configName={configName}>
            <SnkPersonalizedFilter
                ref={elPersonalizedFilter}
                entityUri={entityUri}
                configName={configName}
                onEzAfterSave={handleAfterSave}
            />
        </SnkApplication>
    )
};

export default Demo;
```

> Todos os exemplos acima podem ser utilizados como referência para integração do componente em aplicações React utilizando o Sankhya Design System.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| configName | config-name | Nome da configuração, utilizado para distinguir múltiplas instâncias do componente. | string | undefined |
| entityUri | entity-uri | URI da entidade utilizada para buscar os campos disponíveis para filtro. | string | undefined |
| filterId | filter-id | Identificador do filtro a ser carregado. | string | undefined |
| isDefaultFilter | is-default-filter | Indica se o filtro é o filtro padrão do sistema. | boolean | false |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| resourceID | resource-i-d | Identificador do recurso utilizado para salvar e recuperar filtros. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezAfterSave | Evento emitido após salvar as alterações do filtro personalizado. | CustomEvent<void> |
| ezCancel | Evento emitido ao cancelar a personalização do filtro. | CustomEvent<void> |
| ezSave | Evento emitido ao salvar as alterações do filtro personalizado. | CustomEvent<string> |

### Methods

#### `createPersonalizedFilter() => Promise<void>`

Cria um novo filtro personalizado caso não exista nenhum.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * snk-filter-bar

#### Depends on

  * snk-filter-field-search
  * snk-filter-assistent-mode
  * snk-filter-advanced-mode
  * snk-simple-bar
