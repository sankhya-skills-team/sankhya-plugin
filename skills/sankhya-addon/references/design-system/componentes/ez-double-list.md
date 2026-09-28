> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-double-list/ (snapshot 2026-09-28)

# Double List

O componente **ez-double-list** permite criar um mecanismo de transferências de items de uma lista **A** para uma lista **B** e vice versa, de forma simples e rápida.

demo.js

```jsx
import React from "react";
import { EzDoubleList } from "@sankhyalabs/ezui/react/components";

const leftDataSource = [
    {id: "ID_GOOGLE", label: "Google" },
    {id: "ID_AMAZON", label: "Amazon" },
    {id: "ID_APPLE", label: "Apple" },
    {id: "ID_FACEBOOK", label: "Facebook" },
    {id: "ID_ORACLE", label: "Oracle" },
];

const rightDataSource = [
    { id: "ID_MAGALU",label: "Magalu" },
    { id: "ID_AMERICANAS",label: "Americanas" },
    { id: "ID_IFOOD",label: "Ifood" },
    { id: "ID_ITAU",label: "Itaú" },
    { id: "ID_MERCADO_LIVRE",label: "Mercado Livre" },
];

const Demo = () => {
    return (
      <EzDoubleList leftList={leftDataSource} leftLabel={"Estrangeiras"}
                    rightList={rightDataSource} rightLabel={"Nacionais"}
      />
    );
};

export default Demo;
```

## Propriedades

### slotsListBuilder

Com essa propriedade é possivel personalizar as listas( da esquerda ou da direita) adicionando elementos a esquerda ou a direita de cada item.

demo.js

```jsx
import React from "react";
import { EzDoubleList, EzBadge } from "@sankhyalabs/ezui/react/components";
import { renderToString } from "react-dom/server";

const leftDataSource = [
    {id: "ID_GOOGLE", label: "Google" },
    {id: "ID_AMAZON", label: "Amazon" },
    {id: "ID_APPLE", label: "Apple" },
    {id: "ID_FACEBOOK", label: "Facebook" },
    {id: "ID_ORACLE", label: "Oracle" },
];

const rightDataSource = [
    { id: "ID_MAGALU",label: "Magalu" },
    { id: "ID_AMERICANAS",label: "Americanas" },
    { id: "ID_IFOOD",label: "Ifood" },
    { id: "ID_ITAU",label: "Itaú" },
    { id: "ID_MERCADO_LIVRE",label: "Mercado Livre" },
];

const Demo = () => {

    const buildIdSlot = item => renderToString(
        <EzBadge label={item.id} size="medium"/>
    );

    const buildLabelSlot = item => renderToString(
        <EzBadge size="medium" label={item.label}/>
    )

    const getListSlots = () => {
        return {
            LEFT_LIST:{
                itemLeftSlotBuilder: (item) => buildIdSlot(item),
                itemRightSlotBuilder: (item) => buildLabelSlot(item)
            },
            RIGHT_LIST:{
                itemLeftSlotBuilder: (item) => buildIdSlot(item),
                itemRightSlotBuilder: (item) => buildLabelSlot(item)
            }
        }
    }

    return (
      <EzDoubleList leftList={leftDataSource} leftLabel={"Estrangeiras"}
                    rightList={rightDataSource} rightLabel={"Nacionais"}
                    slotsListBuilder={getListSlots()}
      />
    );
};

export default Demo;
```

### useOnlyRightList

Propriedade importante caso precise utilizar apenas uma lista e ter os recursos de navegação e totalizadores do ez-double-list.

## Eventos

### ezLeftListChanged

Emitido ao realizar uma alteração na **lista esquerda** do componente.

**Lista da esquerda: [Google, Amazon, Apple, Facebook, Oracle]**

demo.js

```jsx
import React, { useState } from 'react';
import { EzDoubleList } from '@sankhyalabs/ezui/react/components';

const dataSource = [
  {id: "ID_GOOGLE", label: "Google" },
  {id: "ID_AMAZON", label: "Amazon" },
  {id: "ID_APPLE", label: "Apple" },
  {id: "ID_FACEBOOK", label: "Facebook" },
  {id: "ID_ORACLE", label: "Oracle" },
];

const Demo = () => {

  const [leftItems, setLeftItems] = useState([...dataSource]);
  const [rightItems, setRightItems] = useState([]);

  const onChange = (items) => {
    const itemsIdList = items.map(i => i.id);
    setLeftItems([...items]);
    setRightItems([...dataSource.filter(i => !itemsIdList.includes(i.id))]);
    alert('Lista da ESQUERDA alterada');
  };

  function buildText() {
    return `[${leftItems.map(item => item.label).join(', ')}]`;
  }

  return (
    <div>
      <EzDoubleList leftList={leftItems} leftLabel={'Estrangeiras'}
                    rightList={rightItems} rightLabel={'Nacionais'}
                    onEzLeftListChanged={evt => onChange(evt.detail)}
      />

      <div>
        <br />
        <label>
          <b>Lista da esquerda: {buildText()}</b>
        </label>
      </div>
    </div>
  );
};

export default Demo;
```

### ezRightListChanged

Emitido ao realizar uma alteração na **lista direita** do componente.

**Lista da direita: [Google, Amazon, Apple, Facebook, Oracle]**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| emptyMessage | -- | Objeto que define as mensagens a serem exibidas quando a lista está vazia Exemplo: { LEFT_LIST?: "Lista lado esquerdo vazia.", RIGHT_LIST?: "Lista lado direito vazia."; } | EmptyMessage | undefined |
| entityLabel | entity-label | Nome da entidade listada. Exemplo: "Campo", "Item", "Empresa". | string | 'item' |
| entityLabelPlural | entity-label-plural | Variação plural do nome da entidade listada. Exemplo: "Campos", "Itens", "Empresas". | string | 'itens' |
| leftList | -- | Define a lista origem. | ListItem[] | [] |
| leftListLabel | left-list-label | Rótulo da lista esquerda. | string | 'disponíveis' |
| leftTitle | left-title | Define o título da lista origem. | string | undefined |
| rightList | -- | Define a lista destino. | ListItem[] | [] |
| rightListLabel | right-list-label | Rótulo da lista direita. | string | 'selecionados' |
| rightTitle | right-title | Define o título da lista destino. | string | undefined |
| slotsListBuilder | -- | Objeto que define os métodos de construção dos elementos visuais para os itens de cada lista.  Este objeto permite configurar dinamicamente os elementos HTML que serão exibidos ao lado esquerdo e direito dos itens em ambas as listas ( LEFT_LIST e RIGHT_LIST ). | DoubleListSlots | undefined |
| useOnlyRightList | use-only-right-list | Define se irá exibir apenas a lista da direita. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| ezLeftListChanged | Emitido ao realizar uma alteração na lista esquerda do componente. | CustomEvent<ListItem[]> |
| ezRightListChanged | Emitido ao realizar uma alteração na lista direita do componente. | CustomEvent<ListItem[]> |

### Methods

#### `resetSelectedLists() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-sortable-list
  * ez-button
