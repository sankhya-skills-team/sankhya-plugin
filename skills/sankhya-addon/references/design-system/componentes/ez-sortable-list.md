> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sortable-list/ (snapshot 2026-09-28)

# Sortable list

Lista ordenável com suporte a múltipla seleção e personalização.

## ez-sortable-list

O `ez-sortable-list` é um componente de lista ordenável que permite arrastar e soltar itens, selecionar múltiplos itens e personalizar a forma como os itens são renderizados.

## Exemplos

### Lista básica

Este exemplo exibe uma lista ordenável simples com dois itens iniciais.

demo.js

```jsx
import React from "react";
import { EzSortableList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
    {id: 1, label: "Google" },
    {id: 2, label: "Amazon" },
    {id: 3, label: "Apple" },
    {id: 4, label: "Facebook" },
    {id: 5, label: "Oracle" },
];

const Demo = () => {
    return (
      <EzSortableList dataSource={dataSource}/>
    );
};

export default Demo;
```

### Lista com seleção múltipla

Neste exemplo, ativamos a seleção múltipla, permitindo que o usuário selecione vários itens segurando a tecla `Ctrl` (Windows/Linux) ou `Command` (Mac) ao clicar.

demo.js

```jsx
import React from "react";
import { EzSortableList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
    {id: 1, label: "Google" },
    {id: 2, label: "Amazon" },
    {id: 3, label: "Apple" },
    {id: 4, label: "Facebook" },
    {id: 5, label: "Oracle" },
];

const Demo = () => {
    return (
        <EzSortableList
            dataSource={dataSource}
            enableMultipleSelection={true}
        />
    );
};

export default Demo;
```

### Personalizando os itens

Aqui personalizamos os itens adicionando um ícone à esquerda e um botão de ação à direita.

### Manipulando eventos

Este exemplo demonstra como capturar eventos de seleção e reordenação de itens.

demo.js

```jsx
import React, { useState } from "react";
import { EzSortableList } from "@sankhyalabs/ezui/react/components";

const dataSource = [
    {id: 1, label: "Google" },
    {id: 2, label: "Amazon" },
    {id: 3, label: "Apple" },
    {id: 4, label: "Facebook" },
    {id: 5, label: "Oracle" },
];

const Demo = () => {
    const [logs, setLogs] = useState([]);

    const addLog = (message) => {
        setLogs([message]);
    };

    const sanitizeDetail = (detail) => {
        try {
            return JSON.stringify(detail, (key, value) =>
                value instanceof HTMLElement ? `[HTMLElement: ${value.tagName}]` : value
            );
        } catch (error) {
            return "Erro ao processar evento";
        }
    };

    const handleSelection = (event) => {
        addLog(`Itens selecionados: ${sanitizeDetail(event.detail)}`);
    };

    const handleReorder = (event) => {
        addLog(`Nova ordem: ${sanitizeDetail(event.detail)}`);
    };

    const handleDoubleClick = (event) => {
        addLog(`Item que sofreu dois cliques: ${sanitizeDetail(event.detail)}`);
    };

    const handleChoose = (event) => {
        addLog(`Item escolhido: ${sanitizeDetail(event.detail)}`);
    };

    return (
        <><EzSortableList
            dataSource={dataSource}
            enableMultipleSelection={true}
            onEzSelectItens={handleSelection}
            onItemsReordered={handleReorder}
            onEzDoubleClick={handleDoubleClick}
            onEzChoose={handleChoose}
        />
        <div className="ez-box">
            {logs && logs.map((log, index) => (
                <span key={index} className="event-log">{log}</span>
            ))}
        </div>
        </>
    );
};

export default Demo;
```

## Conclusão

O `ez-sortable-list` é um componente poderoso e flexível para listas ordenáveis, com suporte para personalização e eventos úteis para manipulação da lista.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| dataSource | -- | Lista de itens para serem renderizados | ListItem[] | [] |
| emptyMessage | empty-message | Mensagem exibida quando a lista está vazia | string | undefined |
| enableMultipleSelection | enable-multiple-selection | Habilita seleção de múltiplos itens utilizando as teclas 'Ctrl/Command' ou 'Shift' | boolean | false |
| entityLabel | entity-label | Nome da entidade listada. Exemplo: "Campo", "Item", "Empresa". | string | undefined |
| entityLabelPlural | entity-label-plural | Variação plural do nome da entidade listada. Exemplo: "Campos", "Itens", "Empresas". | string | undefined |
| group | group | Grupo ao qual o ez-sortable-list pertence | string | 'default' |
| hideHeader | hide-header | Define se o cabeçalho deve ficar oculto. | boolean | false |
| hideTotalizer | hide-totalizer | Define se o totalizador deve ser escondido. | boolean | false |
| hoverFeedback | hover-feedback | Quando verdadeiro, ativa o feedback visual ao efetuar hover nos itens da lista | boolean | true |
| idSortableList | id-sortable-list | ID do sortable list | string | 'DEFAULT_LIST' |
| itemLeftSlotBuilder | -- | Função builder que possibilita gerar conteúdo dinâmico à esquerda do item da lista. * Observação: No react ele se transforma em VNode e não como HTMLElement. | (item: ListItem, group?: ListGroup) => string \| HTMLElement | undefined |
| itemRightSlotBuilder | -- | Função builder que possibilita alterar como o item da lista vai ser apresentado. Observação: No react ele se transforma em VNode e não como HTMLElement. | (item: ListItem, group?: ListGroup) => string \| HTMLElement | undefined |
| removeItensMoved | remove-itens-moved | Remove itens arrastados de uma lista para outra | boolean | false |
| title | title | Define o título da lista. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChoose | Emitido quando ocorre a escolha de um item da lista | CustomEvent<ListItem \| ListItem[]> |
| ezDoubleClick | Emitido quando ocorre um duplo clique em um item da lista | CustomEvent<ListItem> |
| ezSelectItens | Emitido sempre que um ou vários itens da lista forem selecionados | CustomEvent<ListItem \| ListItem[]> |
| itemsReordered | Evento emitido quando a ordem dos itens muda | CustomEvent<any> |

### Methods

#### `clearSelection() => Promise<void>`

Remove a seleção de todos os itens da lista

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-double-list

#### Depends on

  * ez-filter-input

### CSS Variables

| Variable | Description |
|---|---|
| --ez-sortable-list__selected-item--border-radius | Define o raio da borda de items selecionados. |
| --ez-sortable-list__selected-item--background-color | Define a cor de fundo de items selecionados. |
| --ez-sortable-list__selectable--padding-right | Define o espaçamento lateral direito para items selecionados. |
| --ez-sortable-list__selectable--padding-left | Define o espaçamento lateral esquerdo para items selecionados. |
| --ez-sortable-list__icon--color | Define a cor do ícone de arrasto do item da lista. |
| --ez-sortable-list__scrollbar--color-default | Define a cor da barra de rolagem do componente. |
| --ez-sortable-list--color-background | Define a cor de fundo da barra de rolagem do componente. |
| --ez-sortable-list__scrollbar--color-clicked | Define a cor do active na barra de rolagem do componente. |
| --ez-sortable-list__scrollbar--color-hover | Define a cor do hover na barra de rolagem do componente. |
| --ez-sortable-list--border-radius | Define o raio da borda da barra de rolagem do componente. |
| --ez-sortable-list__scrollbar--width | Define a largura da barra de rolagem do componente. |
