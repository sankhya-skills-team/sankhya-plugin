> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator/ (snapshot 2026-09-28)

# Guide Navigator

Componente responsável por exibir uma navegação baseando em guias.

```jsx
import React from 'react';
import {  EzGuideNavigator } from '@sankhyalabs/ezui/react/components';
import "./demo.css"

const Demo = () => {
    return (
        <div className='ez-row height-120'>
            <EzGuideNavigator items={items} />
        </div>
    )
};

export default Demo;

const items = [
	{
		id: "4654321",
		label: "Geral",
		expanded: true,
		children: [
			{
				id: "4654322",
				label: "Endereço",
				children: [
					{ id: "4654331", label: "Pendencias", disabled: true }
				]
			}
		]
	}
];
```

#### Carregamento sob demanda

Em algumas situações pode ser necessário fazer a carga dos filhos de um item de forma dinâmica. Para isso basta atribuir ao atributo "children" do item, uma função. Veja:

## Propriedades

### Atribuição de dados

> Propriedade utilizada **items**

A exemplo do componente EzTree, os dados desse componente são atribuídos no formato de um array. Cada elemento pode ter uma lista de elementos filhos, formando assim uma estrutura hierárquica.

```jsx
import React from 'react';
import {  EzGuideNavigator } from '@sankhyalabs/ezui/react/components';
import "./demo.css"

const Demo = () => {
    return (
        <div className='ez-row height-120'>
            <EzGuideNavigator items={items} />
        </div>
    )
};

export default Demo;

const items = [
	{
		id: "4654321",
		label: "Geral",
		expanded: true,
		children: [
			{
				id: "4654322",
				label: "Endereço",
				children: [
					{ id: "4654331", label: "Pendencias", disabled: true }
				]
			}
		]
	}
];
```

### Visibilidade do componente

> Propriedade utilizada **open**

Para definir por padrão o componente fechado, basta atribui o valor **false** à propriedade `open`.

demo.js

```jsx
import React from 'react';
import { EzGuideNavigator } from '@sankhyalabs/ezui/react/components';
import "./demo.css"

const Demo = () => {
    return (
        <div className='ez-row height-120'>
            <EzGuideNavigator items={items} open={false} />
        </div>
    )
};

export default Demo;

const items = [
	{
		id: "4654321",
		label: "Geral",
		expanded: true
	}
];
```

### Personalização de tooltip

> Propriedade utilizada: **tooltipResolver**

Através do atributo tooltipResolver é possível personalizar o tooltip dos itens.

#### Tooltip por item

A exemplo dos ícones, o próprio item consegue determinar seu tooltip.

demo.js

```jsx
import React from 'react';
import { EzGuideNavigator } from '@sankhyalabs/ezui/react/components';
import "./demo.css"

const Demo = () => {
    return (
        <div className='ez-row height-120'>
            <EzGuideNavigator items={items} />
        </div>
    )
};
export default Demo;

const items = [
    {
        id: "4654321",
        label: "Geral",
        tooltip: "Aqui podemos colocar um texto explicativo para ser visualizado ao passar o mouse.",
        children: [
            {
                id: "4654322",
                label: "Endereço",
                tooltip: "Um texto personalizado para Endereço.",
                children: [
                    {id: "4654331", label: "Pendencias", disabled: true, tooltip: "Um texto personalizado para Pendencias."}
                ]
            }
        ]
    }
];
```

## Principais métodos

#### **enableItem**

Para habilitar itens, use um único id ou uma lista para habilitar vários de uma vez.

#### **disableItem**

Usado para desabilitar itens. Pode receber um único id ou uma lista.

demo.js

```jsx
import React, { useRef } from "react";
import { EzButton, EzGuideNavigator } from "@sankhyalabs/ezui/react/components";
import "../demo.css"

const Demo = () => {
  const element = useRef(null);

  const handleDisable = (indexs) => {
    const idsFromIndexs = indexs.map((index) => items[index].id);
    element.current.disableItem(idsFromIndexs);
  };

  const handleRestore = () => {
    element.current.items = [...items];
  }

  return (
    <>
      <div className="ez-row height-120">
        <EzGuideNavigator ref={element} items={items} />
      </div>
      <div className="ez-col ez-margin-top--medium ez-flex ez-flex--justify-start ez-flex--align-items-center">
        <EzButton
          className="ez-margin-right--large"
          label="Desabilitar 1º e 2º item"
          onClick={() => handleDisable([0, 1])}
        />
        <EzButton
          label="Restaurar"
          onClick={() => handleRestore()}
        />
      </div>
    </>

  );
};

export default Demo;

const items = [
  {
    id: "4654321",
    label: "Geral",
    children: [
      {
        id: "4654322",
        label: "Endereço",
        children: [{ id: "4654331", label: "Pendencias" }]
      }
    ]
  },
  {
    id: "4654323",
    label: "Contatos",
    children: [
      {
        id: "4654324",
        label: "Perfil",
        children: [
          {
            id: "4654388",
            label: "Contas"
          },
        ]
      },
      { id: "4654325", label: "Endereço" }
    ]
  },
  {
    id: "4654326",
    label: "Fiscal",
    children: [{ id: "4654327", label: "NF-e/NFS-e/CT-e" }]
  },
  { id: "4654328", label: "Lotação" },
  { id: "4654329", label: "Observação" },
  { id: "4654330", label: "Juros/Multa" }
];
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| items | -- | Lista de itens do menu de navegação. | IGuideItem[] | [] |
| open | open | Define se o menu de navegação está aberto. | boolean | true |
| selectedId | selected-id | Define o id do item selecionado. | string | undefined |
| tooltipResolver | -- | Define uma função que vai resolver o tooltip ou title daquele item. | (item: IGuideItem, enabled: boolean, level: number) => string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezSelectionChange | Evento emitido quando o item selecionado no navigator é alterado. | CustomEvent<IGuideItem> |

### Methods

#### `disableItem(id: string | Array<string>) => Promise<void>`

Desabilita um ou mais itens.

##### Returns

Type: `Promise<void>`

#### `enableItem(id: string | Array<string>) => Promise<void>`

Habilita um ou mais itens.

##### Returns

Type: `Promise<void>`

#### `getCurrentPath() => Promise<Array<IGuideItem>>`

Obtem um array do caminho de itens da seleção atual.

##### Returns

Type: `Promise<IGuideItem[]>`

Retorna um array do caminho de itens da seleção atual.

#### `getItem(id: string) => Promise<IGuideItem>`

Obtem um item pelo id

##### Returns

Type: `Promise<IGuideItem>`

#### `getParent(id: string) => Promise<IGuideItem>`

Obtem o item pai a partir de um id

##### Returns

Type: `Promise<IGuideItem>`

#### `openGuideNavidator() => Promise<void>`

Abre o navegador de Guia

##### Returns

Type: `Promise<void>`

#### `selectGuide(id: string) => Promise<void>`

Seleciona o item desejado pelo ID.

##### Returns

Type: `Promise<void>`

#### `updateItem(item: IGuideItem | Array<IGuideItem>) => Promise<void>`

Atualiza um ou mais items

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-sidebar-button
  * ez-filter-input
  * ez-button
  * ez-scroller
  * ez-tree

### CSS Variables

| Variable | Description |
|---|---|
| --ez-guide-navigator--padding-left | Define o espaçamento da esquerda do container |
| --ez-guide-navigator--padding-right | Define o espaçamento da direita do container |
| --ez-guide-navigator--box-shadow | Define a cor de shadow box do container de label |
| --ez-guide-navigator--background-color | Define a cor de fundo do container de label |
| --ez-guide-navigator--border-radius | Define o border radius do container de label |
| --ez-guide-navigator--actions-gap | Define o espaçamento entre as ações |
| --ez-guide-navigator--actions-margin | Define a margem vertical do elemento |
| --ez-guide-navigator--actions-padding-right | Define o espaçamento da direita do elemento |
