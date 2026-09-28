> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-filter-field-search/ (snapshot 2026-09-28)

# Filter Field Search

O **SnkFilterFieldSearch** apresenta modal do tipo popover com um campo de busca e uma lista de opções. O componente é utilizado para selecionar um campo em uma determinada hieararquia.

```jsx
import React, { useEffect } from 'react';
import { SnkFilterFieldSearch } from "@sankhyalabs/sankhyablocks/react/components";

const dataSourceFetcher = async () => {
    const response = Promise.resolve({
        data: {
            links: [],
            fields: []
        }
    });

    return await response.data;
}

const Demo = () => {
    const entity = {
        uri: 'dd://Financeiro/br.com.sankhya.fin.cad.receber',
        description: 'Financeiro',
        type: 'LINK',
    }

    const popOver = React.useRef(null);

    useEffect(() => {
        if (popOver.current) popOver.current.setDataSource(entity, dataSourceFetcher);
    }, [popOver]);

    const handleSelectItem = (item) => {
        if (item.detail.type === "LINK") {
            entity = item.detail;
            return popOver.current.setDataSource(item.detail, dataSourceFetcher);
        }
    }
    return (
        <div className="ez-flex">
           <SnkFilterFieldSearch ref={popOver} onEzSelectFilterItem={handleSelectItem} />
        </div>
    )
};

export default Demo;
```

## Propriedades

### Definir o **searchable**

Define se o componente será ou não pesquisável.

> Propriedade utilizada: **searchable**

```jsx
import React  from 'react';
import { SnkFilterFieldSearch } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    return (
        <div className="ez-flex">
           <SnkFilterFieldSearch searchable={false} />
        </div>
    )
};

export default Demo;
```

## Principais métodos

#### setDataSource(currentLink, dataSourceFetcher)

```jsx
import React, { useEffect } from 'react';
import { SnkFilterFieldSearch } from "@sankhyalabs/sankhyablocks/react/components";

const dataSourceFetcher = async () => {
    const response = Promise.resolve({
        data: {
            links: [],
            fields: []
        }
    });

    return await response.data;
}

const Demo = () => {
    const popOver = React.useRef(null);

    useEffect(() => {
        if (popOver.current) popOver.current.setDataSource({}, dataSourceFetcher);
    }, [popOver]);

    return (
        <div className="ez-flex">
           <SnkFilterFieldSearch ref={popOver} />
        </div>
    )
};

export default Demo;
```

## Exemplos de eventos

Ao selecionar um item da lista

```jsx
import React, { useEffect } from 'react';
import { SnkFilterFieldSearch } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const popOver = React.useRef(null);

    useEffect(() => {
        if (popOver.current) popOver.current.setDataSource({}, () => {});
    }, [popOver]);

    const handleSelectItem = (item) => {
        console.log(item.detail)
    }

    return (
        <div className="ez-flex">
           <SnkFilterFieldSearch ref={popOver} onEzSelectFilterItem={handleSelectItem} />
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| fieldsDataSource | -- | Define a fonte de dados que o componente vai utilizar para carregamento dos campos. | FilterFieldsDataSource | undefined |
| searchable | searchable | Define se o componente irá possuir um campo de pesquisa. | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| ezSelectFilterItem | Emitido sempre que um item da lista for selecionado | CustomEvent<IFilterField \| IFilterLink> |

### Methods

#### `applyFilter(filterText: string) => Promise<void>`

Filtra a fonte de dados do componente.

##### Returns

Type: `Promise<void>`

#### `show(element?: HTMLElement, options?: IEzPopoverAnchorOptions) => Promise<void>`

/** Realiza a abertura do componente abaixo do elemento HTML informado e faz a primeira carga de dados.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * snk-expression-item
  * snk-personalized-filter
