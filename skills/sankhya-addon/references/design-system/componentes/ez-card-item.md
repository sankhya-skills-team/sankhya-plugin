> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-card-item/ (snapshot 2026-09-28)

# CardItem

Documentação do componente EzCardItem.

demo.js

```jsx
import React, { useEffect, useRef } from 'react';
import { EzCardItem } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    useEffect(() => {
        populateCardItem();
    });

    function populateCardItem() {
        element.current.item = {
          title: "Atacadista Distribuidor",
          key: "008",
          details:
            {
                "Região": "<span style='color: #3c75e4'>Triangulo mineiro</span>",
                "Endereço": "<u>Floriano Peixoto</u>",
                "Email": "<i>atacadista.distribuidor@sankhya.com.br</i>",
                "Cidade": "Uberlândia",
                "Banco": "Arcor",
                "Ativo": "Sim"
            }
        };
    }

    return (
        <div className="ez-flex">
            <EzCardItem ref={element}></EzCardItem>
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### ezClick()

Evento disparado ao clicar no componente.

demo.js

```jsx
import React, { useEffect, useRef } from 'react';
import { EzCardItem } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const element = useRef(null);

    useEffect(() => {
        populateCardItem();
    });

    function populateCardItem() {
        element.current.item = {
          title: "Atacadista Distribuidor",
          key: "008",
          details:
            {
                "Região": "Triangulo mineiro",
                "Endereço": "Floriano Peixoto",
                "Email": "atacadista.distribuidor@sankhya.com.br",
                "Cidade": "Uberlândia",
                "Banco": "Arcor",
                "Ativo": "Sim"
            }
        };
    }

    function onClick(evt) {
        const { key, title } = evt?.detail;
        const message = `Clicou no CardItem "${key}" com o título "${title}".`;
        ApplicationUtils.message("Título da Mensagem", message);
    }

    return (
        <div className="ez-flex">
            <EzCardItem ref={element} onEzClick={onClick}></EzCardItem>
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| compacted | compacted | Determina se o componente será apresentado no modo compacto. | boolean | false |
| enableKey | enable-key | Determina se a chave do item deve ser exibida. | boolean | true |
| item | -- | Determina o conteúdo do card. Deve conter um objeto no formato: {title: string, key: string, details: any} . | CardItem | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezClick | Emitido sempre que o ez-card é clicado. | CustomEvent<CardItem> |

### Dependencies

#### Used by

  * classic-search-list
  * ez-classic-search-result-list
  * ez-search-result-list
  * search-list

### CSS Variables

| Variable | Description |
|---|---|
| --ez-card-item--font-size | Define o tamanho da fonte do componente. |
| --ez-card-item--font-size-compacted | Define o tamanho da fonte do componente no modo compacto. |
| --ez-card-item--font-family | Define a família da fonte do componente. |
| --ez-card-item--font-weight | Define o peso da fonte do componente. |
| --ez-card-item--font-weight-large | Define o peso da fonte do title do componente. |
| --ez-card-item--color | Define a cor da fonte do componente. |
| --ez-card-item__key--color | Define a cor da fonte da key do componente. |
| --ez-card-item__detail-label--color | Define a cor da fonte do label do detalhe do componente. |
| --ez-card-item__detail-value--color | Define a cor da fonte do valor do detalhe do componente. |
| --ez-card-item__detail--padding-bottom | Define o espaçamento inferior dos detalhes do componente. |
| --ez-card-item__title--padding-bottom | Define o espaçamento inferior do title do componente. |
| --ez-card-item__highlight--color | Define a cor do highlight / marcação nos textos do componente. |
| --ez-card-item--detail-label--font-weight | Define o peso da fonte do componente. |
