> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-list/ (snapshot 2026-09-28)

# List

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

demo.js

```jsx
import React from "react";
import { EzList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
    { label: "Jeff Bezos" },
    { label: "Bill Gates" },
    { label: "Warren Buffett" },
    { label: "Bernard Arnault" },
    { label: "Carlos Slim Helu" },
    { label: "Amancio Ortega" },
    { label: "Larry Ellison" },
    { label: "Mark Zuckerberg" },
    { label: "Michael Bloomberg" },
    { label: "Larry Page" }
];

const Demo = () => {
    return (
        <EzList dataSource={dataSource}/>
    );
};

export default Demo;
```

## Lista categorizada

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

## Modo check

* * * **Item(s) Selecionado(s):**["Jeff Bezos","Bill Gates"]

demo.js

```jsx
import React, { useState } from "react";
import { EzList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
  {
    id: 1,
    label: "Jeff Bezos",
    check: true,
  },
  {
    id: 2,
    label: "Bill Gates",
    check: true
  },
  {
    id: 3,
    label: "Warren Buffett",
    check: false
  }
];

const Demo = () => {
  const [selectedItem, setItem] = useState(dataSource.filter(i => i.check).map(i => i.label));

  const onSelect = (item) => {
    if (item.check) {
      // Adicionar o item ao array se ainda não estiver presente
      if (!selectedItem.includes(item.label)) {
        setItem([...selectedItem, item.label]);
      }
    } else {
      // Remover o item do array se estiver presente
      setItem(selectedItem.filter((selected) => selected !== item.label));
    }
  };

  return (
      <div>
        <div className="ez-row ez-padding-bottom--large">
          <EzList dataSource={dataSource} listMode="check" onEzCheckChange={evt=>onSelect(evt.detail)}/>
        </div>
        <label>
          <p>
            <b>Item(s) Selecionado(s): </b>
            {!!selectedItem.length && JSON.stringify(selectedItem)}
          </p>
        </label>
      </div>
  );
};

export default Demo;
```

## Selecionável

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

demo.js

```jsx
import React from "react";
import { EzList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
  {
    group: "Classificados",
    items: [
      { label: "Jeff Bezos"},
      { label: "Bill Gates"},
      { label: "Warren Buffett"},
      { label: "Bernard Arnault"},
      { label: "Carlos Slim Helu"}
    ]
  },
  {
    group: "Não classificados",
    items: [
      { label: "Amancio Ortega"},
      { label: "Larry Ellison"},
      { label: "Mark Zuckerberg"},
      { label: "Michael Bloomberg"},
      { label: "Larry Page"}
    ],
    sort:"DSC"
  }
];

const Demo = () => {
    return (
      <EzList dataSource={dataSource} useGroups={true} ezSelectable={true}/>
    );
};

export default Demo;
```

## Selecionável (múltiplos itens)

> Propriedade utilizada: **enableMultipleSelection** É possível selecionar mais de um item pressionando a tecla `CRLT` (`⌘` no MACOS) ou um intervalo de itens, pressionando a tecla `SHIFT`.

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

CUIDADO

No momento, essa funcionalidade **não** está disponível para lista categorizada.

Caso o desenvolvedor utilize as simultaneamente as propriedades **useGroups** e **enableMultipleSelection** , então a propriedade **enableMultipleSelection** será ignorada.

## Arrastáveis

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

demo.js

```jsx
import React from "react";
import { EzList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
  {
    group: "Classificados",
    items: [
      { label: "Jeff Bezos"},
      { label: "Bill Gates"},
      { label: "Warren Buffett"},
      { label: "Bernard Arnault"},
      { label: "Carlos Slim Helu"}
    ]
  },
  {
    group: "Não classificados",
    items: [
      { label: "Amancio Ortega"},
      { label: "Larry Ellison"},
      { label: "Mark Zuckerberg"},
      { label: "Michael Bloomberg"},
      { label: "Larry Page"}
    ],
    sort:"DSC"
  }
];

const Demo = () => {
    return (
      <EzList dataSource={dataSource} useGroups={true} ezDraggable={true}/>
    );
};

export default Demo;
```

## Interatividade com feedback visual

> Propriedade utilizada: **hoverFeedback**

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

## Personalização dos itens

> Propriedade utilizada: **itemSlotBuilder**

A propriedade _itemSlotBuilder_ é uma função que possibilita alterar como o item da lista será apresentado. Conforme o exemplo a seguir:

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

demo.js

```jsx
import React from "react";
import { renderToString } from "react-dom/server";
import { EzList, EzIcon } from "@sankhyalabs/ezui/react/components";

const dataSource = [
    { label: "Jeff Bezos" },
    { label: "Bill Gates" },
    { label: "Warren Buffett" },
    { label: "Bernard Arnault" },
    { label: "Carlos Slim Helu" },
    { label: "Amancio Ortega" },
    { label: "Larry Ellison" },
    { label: "Mark Zuckerberg" },
    { label: "Michael Bloomberg" },
    { label: "Larry Page" }
];

const Demo = () => {
    const itemSlotBuilder = item => renderToString(
        <EzIcon
            icon-name="alert-circle"
            title={item.label}
        />
    )

    return (
        <EzList
            dataSource={dataSource}
            itemSlotBuilder={itemSlotBuilder}
        />
    )
}

export default Demo;
```

> Propriedade utilizada: **itemLeftSlotBuilder**

A propriedade _itemLeftSlotBuilder_ é uma função que possibilita inserir conteúdo dinâmico à esquerda do item da lista. Conforme o exemplo a seguir:

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

## Métodos

### Posicionar no topo: scrollToTop

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

demo.js

```jsx
import React, { useRef } from "react";
import { EzList, EzButton } from "@sankhyalabs/ezui/react/components";

const dataSource = [
  {
    group: "Classificados",
    items: [
      { label: "Jeff Bezos"},
      { label: "Bill Gates"},
      { label: "Warren Buffett"},
      { label: "Bernard Arnault"},
      { label: "Carlos Slim Helu"}
    ]
  },
  {
    group: "Não classificados",
    items: [
      { label: "Amancio Ortega"},
      { label: "Larry Ellison"},
      { label: "Mark Zuckerberg"},
      { label: "Michael Bloomberg"},
      { label: "Larry Page"}
    ],
    sort:"DSC"
  }
];

const Demo = () => {
  const list = useRef()

  return (
    <div>
      <EzButton
        label="Posicionar no topo"
        onClick={()=>list.current.scrollToTop()}
      />
      <div style={{height: "150px"}}>
          <EzList
            ref={list}
            dataSource={dataSource}
            useGroups={true}
            ezSelectable={true}
          />
      </div>
    </div>
  );
};

export default Demo;
```

### Selecionar item: setSelection

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

### Obter item selecionado: getSelection

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

**Item Selecionado:**

demo.js

```jsx
import React, { useRef, useState } from "react";
import { EzList, EzButton } from "@sankhyalabs/ezui/react/components";

const dataSource = [
  {
    group: "Classificados",
    items: [
      { label: "Jeff Bezos"},
      { label: "Bill Gates"},
      { label: "Warren Buffett"},
      { label: "Bernard Arnault"},
      { label: "Carlos Slim Helu"}
    ]
  },
  {
    group: "Não classificados",
    items: [
      { label: "Amancio Ortega"},
      { label: "Larry Ellison"},
      { label: "Mark Zuckerberg"},
      { label: "Michael Bloomberg"},
      { label: "Larry Page"}
    ],
    sort:"DSC"
  }
];

const Demo = () => {
  const list = useRef();
  const [selection, setSelection] = useState();

  const obtemSelecao = async () => {
    setSelection(await list.current.getSelection());
  };

  return (
      <div>
        <div className="ez-row ez-padding-bottom--large">
          <EzButton label="Obtém item selecionado" onClick={obtemSelecao}/>
        </div>
        <EzList ref={list} dataSource={dataSource} useGroups={true} ezSelectable={true}/>
        <label>
            <b>Item Selecionado: </b> {selection?.label}
        </label>
      </div>
  );
};

export default Demo;
```

### Limpar seleção: removeSelection

Selecione um item

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

### Obter lista: getList

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

**Resultado:**

demo.js

```jsx
import React, { useRef, useState } from "react";
import { EzList, EzButton } from "@sankhyalabs/ezui/react/components";

const dataSource = [
  {
    group: "Classificados",
    items: [
      { label: "Jeff Bezos"},
      { label: "Bill Gates"},
      { label: "Warren Buffett"},
      { label: "Bernard Arnault"},
      { label: "Carlos Slim Helu"}
    ]
  },
  {
    group: "Não classificados",
    items: [
      { label: "Amancio Ortega"},
      { label: "Larry Ellison"},
      { label: "Mark Zuckerberg"},
      { label: "Michael Bloomberg"},
      { label: "Larry Page"}
    ],
    sort:"DSC"
  }
];

const Demo = () => {
  const list = useRef();
  const [listResult, setListResult] = useState();

  const obtemListaResultante = async () => {
    let result = "";
    (await list.current.getList()).forEach(item => {
      if(result.length > 0){
        result += ", "
      }
      result += item.group;
    });
    setListResult("[" + result + "]");
  };

  return (
      <div>
        <div className="ez-row ez-padding-bottom--large">
          <EzButton label="Obtém grupos" onClick={obtemListaResultante}/>
        </div>
        <EzList ref={list} dataSource={dataSource} useGroups={true} ezSelectable={true}/>
        <label>
            <b>Resultado: </b> {listResult}
        </label>
      </div>
  );
};

export default Demo;
```

## Evento ezChange

Arraste os itens para alterar a ordem e veja o resultado do ezChange

* Jeff Bezos

* Bill Gates

* Warren Buffett

**Resultado change:**

## Evento ezSelectItem

Selecione um item:

* Jeff Bezos

* Bill Gates

* Warren Buffett

**Item selecionado:**

demo.js

```jsx
import React, { useState } from "react";
import { EzList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
    { label: "Jeff Bezos" },
    { label: "Bill Gates" },
    { label: "Warren Buffett" }
];

const Demo = () => {
    const [selectedItem, setItem] = useState()

    const onSelect = (item) => {
        setItem(item.label);
    }

    return (
        <div>
            Selecione um item:
            <EzList
                dataSource={dataSource}
                onEzSelectItem={evt=>onSelect(evt.detail)}
                ezSelectable={true}
            />
            <div>
                <label>
                    <b>Item selecionado: </b> {selectedItem}
                </label>
            </div>
        </div>
    );
};

export default Demo;
```

## Evento ezDoubleClick

Clique duplo em um item:

* Jeff Bezos

* Bill Gates

* Warren Buffett

**Item retornado:**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| dataSource | -- | Define a lista inicial do componente. | (ListItem \| ListGroup)[] | [] |
| enableMultipleSelection | enable-multiple-selection | Habilita seleção de múltiplos items. | boolean | false |
| enabled | enabled | Habilita a seleção de checkbox. | boolean | true |
| ezDraggable | ez-draggable | Se true habilita drag and drop para os itens. | boolean | false |
| ezSelectable | ez-selectable | Se true os itens serão selecionáveis. | boolean | false |
| hoverFeedback | hover-feedback | Quando verdadeiro, ativa o feedback visual ao efetuar houver nos itens da lista. | boolean | false |
| itemLeftSlotBuilder | -- | Função builder que possibilita gerar conteúdo dinâmico à esquerda do item da lista. * Observação: No react ele se transforma em VNode e não como HTMLElement. | (item: ListItem, group?: ListGroup) => string \| HTMLElement | undefined |
| itemSlotBuilder | -- | Função builder que possibilita alterar como o item da lista vai ser apresentado. Observação: No react ele se transforma em VNode e não como HTMLElement. | (item: ListItem, group?: ListGroup) => string \| HTMLElement | undefined |
| listMode | list-mode | Define o modo de apresentação da lista. | "check" \| "regular" | 'regular' |
| useGroups | use-groups | Se true os grupos serão exibidos. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de estado da lista. | CustomEvent<(ListItem \| ListGroup)[]> |
| ezCheckChange | Emitido quando acontece a alteração de um item do checkbox. | CustomEvent<ListItem> |
| ezDoubleClick | Emitido quando ocorre um duplo clique em um item da lista. | CustomEvent<ListItem> |
| ezSelectItem | Emitido sempre que um item da lista for selecionado. | CustomEvent<ListItem> |
| ezSelectMultipleItems | Emitido sempre que um ou vários item da lista for selecionado. | CustomEvent<ListItem[]> |

### Methods

#### `clearHistory() => Promise<void>`

Limpa o histórico da lista.

##### Returns

Type: `Promise<void>`

#### `getList() => Promise<Array<ListItem | ListGroup>>`

Obtém a lista de items ou grupos.

##### Returns

Type: `Promise<(ListItem | ListGroup)[]>`

#### `getSelection() => Promise<ListItem>`

Obtém o item selecionado.

##### Returns

Type: `Promise<ListItem>`

#### `removeSelection() => Promise<void>`

Limpa a seleção atual

##### Returns

Type: `Promise<void>`

#### `scrollToTop() => Promise<void>`

Traz o conteúdo da lista para a área visível.

##### Returns

Type: `Promise<void>`

#### `setSelection(selectedItem: ListItem, scrollToOption?: boolean, shitkey?: boolean, ctrlKey?: boolean) => Promise<void>`

Aplica seleção nas linhas da lista.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-alert-list
  * ez-multi-selection-list

#### Depends on

  * ez-check

### CSS Variables

| Variable | Description |
|---|---|
| --ez-list__host--z-index | Define a camada de visibilidae do componente. |
| --ez-list__host--border-radius | Define o raio da borda do componente. |
| --ez-list__host--padding | Define o espaçamento entre a lista e o componente. |
| --ez-list__icon--padding | Define o espaçamento interno do ícone. |
| --ez-list__icon--color | Define a cor do ícone de arrasto do item da lista. |
| --ez-list__item--margin | Define o espaçamento externo do item da lista. |
| --ez-list__item--color | Define a cor do texto do item da lista. |
| --ez-list__item--border-bottom | Define o estilo borda inferior do item da lista. |
| --ez-list__item--border-bottom-color | Define a cor da borda inferior do item da lista. |
| --ez-list__item--font-family | Define o estilo do texto do item da lista. |
| --ez-list__item--font-size | Define o tamanho do texto do item da lista. |
| --ez-list__item--white-space | Define o tipo da quebra de linha do item da lista. |
| --ez-list__selectable--padding-right | Define o espaçamento lateral direito para items selecionados. |
| --ez-list__selectable--padding-left | Define o espaçamento lateral esquerdo para items selecionados. |
| --ez-list__selected-item--border-radius | Define o raio da borda de items selecionados. |
| --ez-list__selected-item--background-color | Define a cor de fundo de items selecionados. |
| --ez-list__group--font-family | Define o estilo do texto do grupo da lista. |
| --ez-list__group--font-size | Define o tamanho do texto do grupo da lista. |
| --ez-list__group--font-weight | Define o peso do texto do grupo da lista. |
| --ez-list__group--padding-bottom | Define o espaçamento inferior do grupo da lista. |
| --ez-list__group-overlay--font-family | Define o estilo do texto da área de transferência de grupos. |
| --ez-list__group-overlay--font-size | Define o tamanho do texto da área de transferência de grupos. |
| --ez-list__over--border--color | Define a cor da borda pontilhada sobre os elementos da lista. |
| --ez-list__last-droppable-space--height | Define a altura do container para arrasto para última posição . |
| --ez-list__draggable-list--padding-bottom | Define o espaçamento do container de itens arrastáveis . |
| --ez-list__draggable-icon--image | Define a imagem do ícone de drag. |
| --ez-list__scrollbar--color-default | Define a cor da barra de rolagem do componente. |
| --ez-list__scrollbar--color-background | Define a cor de fundo da barra de rolagem do componente. |
| --ez-list__scrollbar--color-hover | Define a cor do hover na barra de rolagem do componente. |
| --ez-list__scrollbar--color-clicked | Define a cor do active na barra de rolagem do componente. |
| --ez-list__scrollbar--border-radius | Define o raio da borda da barra de rolagem do componente. |
| --ez-list__scrollbar--width | Define a largura da barra de rolagem do componente. |
