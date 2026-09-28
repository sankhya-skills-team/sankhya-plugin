> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-breadcrumb/ (snapshot 2026-09-28)

# Breadcrumb

O Breadcrumb é um componente responsável por apresentar uma sequência de links hierárquicos, proporcionando ao usuário uma clara orientação em relação à página principal, ao mesmo tempo em que permite uma navegação intuitiva entre as páginas anteriores.

demo.js

```jsx
import React from 'react';
import { EzBreadcrumb } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const items = [
        {
            id: '1',
            label: 'Parceiros',
            iconName: 'home'
        },
        {
            id: '2',
            label: 'Movimentação',
            iconName: 'home'
        },
        {
            id: '3',
            label: 'Plano de Contas',
            iconName: 'home'
        },
        {
            id: '4',
            label: 'Geral',
            iconName: 'home'
        },
        {
            id: '5',
            label: 'Financeiro',
            iconName: 'home'
        },
        {
            id: '6',
            label: 'Vendas',
            iconName: 'home'
        }
    ];

    return (
        <div className="ez-flex">
            <EzBreadcrumb items={items} fillMode="regular" maxItems={4} positionEllipsis={1}></EzBreadcrumb>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Sem ícone

Variação do componente sem a presença de ícones.

demo.js

```jsx
import React from 'react';
import { EzBreadcrumb } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const items = [
    {
      id: '1',
      label: 'Parceiro'
    },
    {
      id: '2',
      label: 'Contatos'
    },
    {
      id: '3',
      label: ' Produtos cotação'
    },
    {
      id: '4',
      label: 'Geral'
    }
  ];

  return (
    <div className="ez-flex">
      <EzBreadcrumb items={items}></EzBreadcrumb>
    </div>
  )
};

export default Demo;
```

### Com ícone

Variação do componente com ícone à esquerda.

## Modos de apresentação `fillMode`

A propriedade `fillMode` permite personalização do modo de apresentação proporcionando flexibilidade ao componente. Sendo assim, é possível escolher entre dois modos: `auto` e `regular`, sendo `auto` o valor padrão.

### Auto

No modo `auto`, o componente se adapta de forma responsiva, ajustando-se dinamicamente ao espaço disponível na tela. Quando o Breadcrumb excede o espaço disponível, é acionado um mecanismo de _ellipsis_ que oculta os itens excedentes, garantindo uma apresentação limpa e organizada.

Importante

Para garantir o correto funcionamento da funcionalidade `auto` do Breadcrumb, é necessário **sempre utilizar o Breadcrumb dentro de um container (HTMLElement) que não contenha outros elementos filhos**.

demo.js

```jsx
import React from 'react';
import { EzBreadcrumb } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const items = [
    {
      id: '1',
      label: 'Parceiros',
      iconName: 'home'
    },
    {
      id: '2',
      label: 'Movimentação',
      iconName: 'home'
    },
    {
      id: '3',
      label: 'Plano de Contas',
      iconName: 'home'
    },
    {
      id: '4',
      label: 'Geral',
      iconName: 'home'
    },
    {
      id: '5',
      label: 'Financeiro',
      iconName: 'home'
    },
    {
      id: '6',
      label: 'Vendas',
      iconName: 'home'
    },
    {
      id: '7',
      label: 'Geral',
      iconName: 'home'
    },
    {
      id: '8',
      label: 'Lançamento',
      iconName: 'home'
    },
    {
      id: '9',
      label: 'Plano de Contas',
      iconName: 'home'
    },
    {
      id: '10',
      label: 'Movimentação',
      iconName: 'home'
    }
  ];

  return (
    <div>
      <EzBreadcrumb items={items} fillMode="auto"></EzBreadcrumb>
    </div>
  )
};

export default Demo;
```

### Regular

Já no modo regular, é concedido controle total sobre as configurações. Por meio desse modo, é possível definir manualmente a quantidade máxima de itens exibidos (`maxItems`) e até mesmo a posição do _ellipsis_ (`positionEllipsis`), permitindo ajustes personalizados de acordo com especificações desejadas.

## Exemplos de eventos

#### onSelectedItem()

Quando o usuário escolhe um link, esse evento é emitido.

Link selecionado: **Nenhum**

demo.js

```jsx
import React, { useState } from "react";
import { EzBreadcrumb } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const items = [
        {
            id: '1',
            label: 'Parceiro',
            iconName: 'home'
        },
        {
            id: '2',
            label: 'Contatos',
            iconName: 'home'
        },
        {
            id: '3',
            label: ' Produtos cotação',
            iconName: 'home'
        },
        {
            id: '4',
            label: 'Geral',
            iconName: 'home'
        }
    ];

    const [itemSelected, setItemSelected] = useState("Nenhum");

    return (
        <div className="ez-flex ez-flex--column">
            <EzBreadcrumb items={items} onSelectedItem={evt => setItemSelected(evt.detail.label)}></EzBreadcrumb>

            <label className="ez-align--center">
                <p>Link selecionado: <strong>{itemSelected.toString()}</strong></p>
            </label>
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| fillMode | fill-mode | Define o modo de uso do Breadcrumb. | "auto" \| "regular" | "auto" |
| items | -- | Lista de itens do breadcrumb. | IBreadcrumbItem[] | [] |
| maxItems | max-items | Define o limite máximo de itens a serem renderizados. | number | 4 |
| positionEllipsis | position-ellipsis | Define a posição do Ellipsis nos itens visíveis do Breadcrumb. | number | 1 |

### Events

| Event | Description | Type |
|---|---|---|
| selectedItem | Emitido quando um item do breadcrumb é selecionado. | CustomEvent<IBreadcrumbItem> |

### Dependencies

#### Depends on

  * ez-icon
  * ez-dropdown

### CSS Variables

| Variable | Description |
|---|---|
| --breadcrumb__item--label--color--title-primary | Define a cor da fonte do link, com exceção do último. |
| --breadcrumb__item--label--color--active | Define a cor da fonte do último link |
| --breadcrumb__item--label--font-weight | Define o peso da fonte. |
