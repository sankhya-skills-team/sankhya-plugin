> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tree/ (snapshot 2026-09-28)

# Tree

Uma árvore ou **Tree** é um componente usado para exibir dados hierárquicos de forma organizada. É possível expandir e contrair informações, auxiliando a navegação entre os registros.

demo.js

```jsx
import React from 'react';
import { EzTree } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzTree items={items} />
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
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    },
    {
        id: "4654326", label: "Fiscal",
        children: [
            { id: "4654327", label: "NF-e/NFS-e/CT-e" }
        ]
    },
    { id: "4654328", label: "Lotação" },
    { id: "4654329", label: "Observação" },
    { id: "4654330", label: "Juros/Multa", disabled: true}
];
```

#### Carregamento sob demanda

Em algumas situações pode ser necessário fazer a carga dos filhos de um item de forma dinâmica.
Para isso basta atribuir ao atributo "children" do item, uma função. Veja:

## Propriedades

### Item selecionado

> Propriedade utilizada: **value**

Item selecionado: **Selecione um item...**

demo.js

```jsx
import React from 'react';
import { EzTree } from '@sankhyalabs/ezui/react/components';
import { useState } from 'react';

const Demo = () => {
    const [selectedItem, setSelectedItem] = useState();

    const onChangeHandler = (evt) => {
        setSelectedItem(evt.detail);
    };

    return (
        <div className="ez-flex ez-flex--column">
            <label className="ez-margin-horizontal--auto ez-margin-top--medium">
                Item selecionado: <strong>{selectedItem ? selectedItem.label : "Selecione um item..."}</strong>
            </label>
            <EzTree onEzChange={evt => onChangeHandler(evt)} items={items}/>
        </div>
    )
};
export default Demo;

const items = [
    {
        id: "4654321",
        label: "Geral",
        expanded: true
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    },
    {
        id: "4654326", label: "Fiscal",
        children: [
            { id: "4654327", label: "NF-e/NFS-e/CT-e" }
        ]
    }
];
```

### ID selecionado

> Propriedade utilizada: **selectedId**

Também podemos determinar a seleção pelo id

demo.js

```jsx
import React from 'react';
import { EzTree } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzTree selectedId="4654323" items={items}/>
    )
};
export default Demo;

const items = [
    {
        id: "4654321",
        label: "Geral",
        expanded: true
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    },
    {
        id: "4654326", label: "Fiscal",
        children: [
            { id: "4654327", label: "NF-e/NFS-e/CT-e" }
        ]
    }
];
```

### Itens selecionáveis

> Propriedade utilizada: **selectable**

Através do atributo selectable é possível determinar se os itens serão ou não selecionáveis.

Quando o selectable for verdadeiro, os itens da lista se comportam de forma diferente. Com `selectable={true}`, ao clicar no item o mesmo é selecionado e os itens filhos não são abertos automaticamente, apenas serão abertos quando clicado na seta de expansão. Já quando o selectable for falso, tanto o ícone quanto o próprio item, quando clicados, expandem os filhos.

Item selecionado: **Selecione um item...**

### Personalização de ícones

> Propriedade utilizada: **iconResolver**

Através do atributo iconResolver é possível interferir na criação do ícone de expandir/contrair.

demo.js

```jsx
import React from 'react';
import { EzTree } from '@sankhyalabs/ezui/react/components';

const iconResolver = (item, expanded, level) => {
    return expanded ? "minus" : "plus";
}

const Demo = () => {
    return (
        <EzTree items={items} iconResolver={iconResolver}/>
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
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" }
        ]
    }
];
```

#### Icones por item

Além disso, o próprio item consegue determinar qual ícone deve ser usado para representar seu estado (aberto/fechado).

### Personalização de tooltip

> Propriedade utilizada: **tooltipResolver**

Através do atributo tooltipResolver é possível personalizar o tooltip dos itens.

demo.js

```jsx
import React from 'react';
import { EzTree } from '@sankhyalabs/ezui/react/components';

const tooltipResolver = (item, enabled, level) => {
    return enabled ? `Tooltip personalizado: "${item.label}"` : "Item inativo";
}

const Demo = () => {
    return (
        <EzTree items={items} tooltipResolver={tooltipResolver}/>
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
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" }
        ]
    }
];
```

#### Tooltip por item

A exemplo dos ícones, o próprio item consegue determinar seu tooltip.

## Principais métodos

### applyFilter

O método `applyFilter` permite filtrar os itens da árvore utilizando uma string como parâmetro.
É possível realizar buscas simples ou buscas hierárquicas utilizando o caractere ponto (`.`) para separar os níveis da hierarquia.

Exemplos de uso:

  * `applyFilter("Geral")` irá buscar todos os itens que contenham "Geral".
  * `applyFilter("Endereço")` irá buscar todos os itens que contenham "Endereço".
  * `applyFilter("Geral.Endereço")` irá buscar o caminho hierárquico "Geral" > "Endereço".
  * `applyFilter("Geral.Endereço.Entrega.CEP")` irá buscar o caminho completo até "CEP".
  * `applyFilter("Fiscal.NF-e/NFS-e/CT-e.Canceladas.Por erro")` irá buscar o caminho até "Por erro" dentro de "Canceladas".

Dessa forma, é possível refinar a busca por caminhos específicos dentro da árvore, facilitando a localização de itens em estruturas complexas.

demo.js

```jsx
import React from 'react';
import { EzTree, EzFilterInput } from '@sankhyalabs/ezui/react/components';
import { useRef } from 'react';

const Demo = () => {
    const tree = useRef();
    const applyFilter = filter => {
        tree.current.applyFilter(filter);
    };
    return (
        <>
            <EzFilterInput label="Digite um filtro" onEzChange={evt => applyFilter(evt.detail)}/>
            <EzTree ref={tree} items={items} />
        </>
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
                    {id: "4654331", label: "Pendencias", disabled: true},
                    {
                        id: "4654332",
                        label: "Entrega",
                        children: [
                            { id: "4654333", label: "CEP" },
                            { id: "4654334", label: "Complemento" },
                            {
                                id: "4654335",
                                label: "Referências",
                                children: [
                                    { id: "4654336", label: "Ponto de referência 1" },
                                    { id: "4654337", label: "Ponto de referência 2", disabled: true }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                id: "4654338",
                label: "Documentos",
                children: [
                    { id: "4654339", label: "RG" },
                    { id: "4654340", label: "CPF" },
                    {
                        id: "4654341",
                        label: "Comprovantes",
                        children: [
                            { id: "4654342", label: "Residência" },
                            { id: "4654343", label: "Renda" }
                        ]
                    }
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" },
            {
                id: "4654344",
                label: "Telefones",
                children: [
                    { id: "4654345", label: "Celular" },
                    { id: "4654346", label: "Residencial" },
                    { id: "4654347", label: "Comercial", disabled: true }
                ]
            },
            {
                id: "4654348",
                label: "E-mails",
                children: [
                    { id: "4654349", label: "Pessoal" },
                    { id: "4654350", label: "Corporativo" }
                ]
            }
        ]
    },
    {
        id: "4654326", label: "Fiscal",
        children: [
            {
                id: "4654327",
                label: "NF-e/NFS-e/CT-e",
                children: [
                    { id: "4654351", label: "Emitidas" },
                    { id: "4654352", label: "Recebidas" },
                    {
                        id: "4654353",
                        label: "Canceladas",
                        children: [
                            { id: "4654354", label: "Por erro" },
                            { id: "4654355", label: "Por duplicidade" }
                        ]
                    }
                ]
            },
            {
                id: "4654356",
                label: "Tributação",
                children: [
                    { id: "4654357", label: "ICMS" },
                    { id: "4654358", label: "ISS" },
                    { id: "4654359", label: "IPI" }
                ]
            }
        ]
    },
    {
        id: "4654328",
        label: "Lotação",
        children: [
            { id: "4654360", label: "Setor A" },
            { id: "4654361", label: "Setor B" },
            {
                id: "4654362",
                label: "Setor C",
                children: [
                    { id: "4654363", label: "Equipe 1" },
                    { id: "4654364", label: "Equipe 2" }
                ]
            }
        ]
    },
    {
        id: "4654329",
        label: "Observação",
        children: [
            { id: "4654365", label: "Observação Geral" },
            { id: "4654366", label: "Observação Fiscal" }
        ]
    },
    { id: "4654330", label: "Juros/Multa", disabled: true,
        children: [
            { id: "4654367", label: "Juros" },
            { id: "4654368", label: "Multa" }
        ]
    }
];
```

### addChild

### disableItem e enableItem

demo.js

```jsx
import React, { useRef } from 'react';
import { EzTree, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const tree = useRef()

    const disableHandler = () => {
        tree.current.disableItem("4654323");
    };

    const enableHandler = () => {
        tree.current.enableItem("4654323");
    };

    return (
        <div>
            <div className="ez-col ez-flex--justify-center ez-margin-horizontal--auto ez-margin-top--medium">
                <EzButton
                    onClick={() => disableHandler()}
                    label="Desabilitar Contatos"
                />
                <EzButton
                    onClick={() => enableHandler()}
                    label="Habilitar Contatos"
                />
            </div>
            <EzTree
                ref={tree}
                items={items}
            />
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
    },
    {
        id: "4654323",
        label: "Contatos",
        expanded: true,
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    }
];
```

### expandAll e collapseAll

### openItem

demo.js

```jsx
import React, { useRef } from 'react';
import { EzTree, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const tree = useRef()

    const openHandler = () => {
        tree.current.openItem("4654321 >> 4654322");
    };

    return (
        <div className="ez-flex ez-flex--column">
            <EzButton
                className="ez-margin-horizontal--auto ez-margin-top--medium"
                onClick={() => openHandler()}
                label="Abrir itens"
            />
            <EzTree
                ref={tree}
                items={items}
            />
        </div>
    )
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
                children: [
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    }
];
```

### selectItem

### updateItem

O método `updateItem` permite atualizar as propriedades de um ou mais itens existentes na árvore. Pode receber como parâmetro um item individual ou um array de itens, juntamente com opções de configuração.

**Parâmetros:**

  * `item` \- Um objeto `ITreeItem` ou array de objetos `ITreeItem` com as novas informações
  * `config` (opcional) - Objeto de configuração com as seguintes propriedades:
    * `updatedBySelectedId`: Se `true`, utiliza o `selectedId` atual como ID do item a ser atualizado
    * `forceDefaultValues`: Se `true`, aplica valores padrão para propriedades não definidas (disabled: false, expanded: false)

**Funcionalidades:**

  * Atualiza propriedades como título/label, estado disabled/enabled, filhos, etc.
  * Suporte para atualização em lote (múltiplos itens)
  * Atualização baseada no item selecionado atual
  * Aplicação automática de valores padrão quando necessário
  * Emite evento `ezChange` se o item atualizado estiver selecionado

Selecione um item na árvore para usar as ações acima

demo.js

```jsx
import { useRef, useState } from 'react';
import { EzTree, EzButton, EzTextInput } from '@sankhyalabs/ezui/react/components';
import { copyObject, INITIAL_ITEMS } from '../utilsTree';

const Demo = () => {
    const tree = useRef();
    const items = useRef(copyObject(INITIAL_ITEMS));
    const [selectedItem, setSelectedItem] = useState(null);
    const [newLabel, setNewLabel] = useState('');

    const updateItemLabel = () => {
        if (selectedItem && newLabel.trim()) {
            // Cria um novo objeto com as propriedades atualizadas
            const updatedItem = {
                ...selectedItem,
                label: newLabel.trim()
            };
            tree.current.updateItem(updatedItem);
            setNewLabel('');
        }
    };

    const toggleDisableItem = () => {
        if (selectedItem) {
            const updatedItem = {
                ...selectedItem,
                disabled: !selectedItem.disabled
            };
            tree.current.updateItem(updatedItem);
        }
    };

    const addChildToSelected = () => {
        if (selectedItem) {
            const newChild = {
                id: `new-${Date.now()}`,
                label: 'Novo Item Filho'
            };

            const updatedItem = {
                ...selectedItem,
                children: [...(selectedItem.children || []), newChild],
                expanded: true
            };
            tree.current.updateItem(updatedItem);
        }
    };

    const resetToInitial = () => {
        tree.current.updateItem(copyObject(INITIAL_ITEMS), { forceDefaultValues: true });
    }

    return (
        <div className="ez-flex ez-flex--column">
            <div className="ez-flex ez-flex--gap-medium ez-flex--align-items-center ez-margin-bottom--medium ez-flex--wrap">

                <div className="ez-flex ez-flex--gap-small ez-flex--align-items-center">
                    <EzTextInput
                        label="Novo nome do item"
                        placeholder="Digite o novo nome"
                        value={newLabel}
                        onEzChange={(e) => setNewLabel(e.detail)}
                    />
                    <EzButton
                        onClick={updateItemLabel}
                        label="Alterar Nome"
                        className="ez-margin-left--medium"
                        disabled={!selectedItem || !newLabel.trim()}
                        size="small"
                    />
                </div>

                <EzButton
                    onClick={toggleDisableItem}
                    label={selectedItem?.disabled ? 'Habilitar Item' : 'Desabilitar Item'}
                    className="ez-margin-left--medium"
                    disabled={!selectedItem}
                    size="small"
                />

                <EzButton
                    onClick={addChildToSelected}
                    label="Adicionar Filho"
                    className="ez-margin-left--medium"
                    disabled={!selectedItem}
                    size="small"
                />

                <EzButton
                    onClick={resetToInitial}
                    label="Restaurar padrão"
                    className="ez-margin-left--medium"
                    disabled={!selectedItem}
                    size="small"
                />
            </div>

            <div className="ez-text-small ez-margin-bottom--small">
                {selectedItem
                    ? `Item selecionado: ${selectedItem.label}`
                    : 'Selecione um item na árvore para usar as ações acima'}
            </div>

            <EzTree
                ref={tree}
                items={items.current}
                selectable={true}
                onEzChange={(e) => setSelectedItem(e.detail)}
            />
        </div>
    );
};

export default Demo;
```

### removeItem

O método `removeItem` permite remover um item específico da árvore. Pode receber como parâmetro o ID do item que será removido. Caso nenhum ID seja passado, o item atualmente selecionado será removido.

Formas de uso:

  * `removeItem()` \- Remove o item selecionado
  * `removeItem(id)` \- Remove o item com o ID especificado

Ao remover um item que possui filhos, todos os seus descendentes também serão removidos da árvore.

Selecione um item na árvore para removê-lo

## Exemplos de eventos

### ezChange

Selecione um item na árvore

demo.js

```jsx
import React from "react";
import { EzTree } from "@sankhyalabs/ezui/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const showEventHandler = (event) => {
        ApplicationUtils.message("Evento emitido", `Evento: "${event.type}"<br />Item: "${event.detail.label}"`);
    }

    return (
        <div>
            Selecione um item na árvore
            <EzTree items={items} onEzChange={evt => showEventHandler(evt)}/>
        </div>
    );
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
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    }
];
```

### ezOpenItem

Abra um item da árvore

### ezRemoveItem

Selecione um item na árvore para removê-lo

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| enableHierarchicalFilter | enable-hierarchical-filter | Define se a árvore deve permitir a filtragem hierárquica. | boolean | true |
| iconResolver | -- | Define uma função que vai resolver o ícone daquele item. Retorna o nome do ícone da lib de icones do DS. | (item: ITreeItem, expanded: boolean, level: number) => string | defaultIconResolver |
| items | -- | Define os itens apresentados na árvore. | ITreeItem[] | [] |
| selectable | selectable | Define se os itens da árvore são selecionáveis. | boolean | true |
| selectedId | selected-id | Forma alternativa para atribuir o item selecionado por seu ID. | string | undefined |
| tooltipResolver | -- | Define uma função que vai resolver o tooltip ou title daquele item. | (item: ITreeItem, enabled: boolean, level: number) => string | undefined |
| value | -- | Define o item selecionado na árvore. | ITreeItem | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando um item é selecionado na árvore. | CustomEvent<ITreeItem> |
| ezDbClickItem | Emitido ao dar clique duplo em um item da árvore. | CustomEvent<ITreeItem> |
| ezOpenItem | Emitido quando um item é aberto na árvore. | CustomEvent<ITreeItem> |
| ezRemoveItem | Emitido ao remover um item da árvore. | CustomEvent<string> |

### Methods

#### `addChild(item: ITreeItem, parentId?: string) => Promise<void>`

Adiciona um ou mais itens. Opcionalmente pode-se determinar a qual item da árvore será anexado o item. Caso não informado parentId, adiciona no item selecionado. Observação para carga dinâmica (Lazyload): O parentId deve ser um item carregado atualmente na árvore.

##### Returns

Type: `Promise<void>`

#### `applyFilter(pattern: string) => Promise<void>`

Efetua a seleção de um item.

##### Returns

Type: `Promise<void>`

#### `collapseAll() => Promise<void>`

Recolhe todos os itens da árvore.

##### Returns

Type: `Promise<void>`

#### `disableItem(id: string | Array<string>) => Promise<void>`

Desabilita um ou mais itens.

##### Returns

Type: `Promise<void>`

#### `enableItem(id: string | Array<string>) => Promise<void>`

Habilita um ou mais itens.

##### Returns

Type: `Promise<void>`

#### `expandAll() => Promise<void>`

Expande todos os itens da árvore.

##### Returns

Type: `Promise<void>`

#### `getCurrentPath() => Promise<Array<ITreeItem>>`

Obtem um array do caminho de itens da seleção atual.

##### Returns

Type: `Promise<ITreeItem[]>`

Retorna um array do caminho de itens da seleção atual.

#### `getItem(id: string) => Promise<ITreeItem>`

Obtem um item pelo id

##### Returns

Type: `Promise<ITreeItem>`

#### `getParent(id: string) => Promise<ITreeItem>`

Obtem o item pai a partir de um id

##### Returns

Type: `Promise<ITreeItem>`

#### `openItem(id: string) => Promise<void>`

Realiza a abertura de um item, incluindo a hieraquia acima. Observação para carga dinâmica (Lazyload): O item solicitado já deve estar carregado na lista. Nos casos onde o item ainda não esteja carregado o id pode ser uma string no formato "id1>>id2>>id3", tornando possível a carga a partir de um ponto já carregado.

##### Returns

Type: `Promise<void>`

#### `removeItem(id?: string) => Promise<void>`

Remove um item da árvore pelo seu ID. Se o item removido estiver selecionado, a seleção será limpa.

##### Returns

Type: `Promise<void>`

#### `selectItem(id: string) => Promise<void>`

Efetua a seleção de um item.

##### Returns

Type: `Promise<void>`

#### `updateItem(item: ITreeItem | ITreeItem[], config?: Partial<UpdateItemConfig>) => Promise<void>`

Atualiza um item

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-guide-navigator

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-tree--border-radius | Define o arredondamento dos retangulos. |
| --ez-tree--padding-inline-start | Define a largura da identação de cada nível. |
| --ez-tree--margin | Define a margem do componente. |
| --ez-tree--margin-right | Define a margem da direita do componente. |
| --ez-tree--user-select | Define se o texto dos itens pode ser selecionado pelo usuário. |
| --ez-tree--font-family | Define a família da fonte. |
| --ez-tree--font-size | Define o tamanho da fonte. |
| --ez-tree--selected--font-weight | Define o peso da fonte. |
| --ez-tree--font-weight | Define o peso da fonte. |
| --ez-tree--color | Define a cor da fonte e do ícone. |
| --ez-tree--selected--color | Define a cor da fonte e do ícone quando selecionado. |
| --ez-tree--disabled--color | Define a cor da fonte e do ícone quando desabilitado. |
| --ez-tree--font-weight--bold | Usado em fontes com peso maior (bold) |
| --ez-tree__tree-item--height | Define a altura de cada item. |
| --ez-tree__tree-item--padding | Define o espaçamento interno do item. |
| --ez-tree__tree-item--background-color | Define a cor de background. |
| --ez-tree__tree-item--selected--background-color | Define a cor de background quando selecionado. |
| --ez-tree__tree-item--hover--background-color | Define a cor de background com o mouse sobre o item. |
| --ez-tree__tree-item--disabled--background-color | Define a cor de background quando deabilitado. |
| --ez-tree__item-icon-box--height | Define a altura do box do ícone. |
| --ez-tree__item-icon-box--width | Define a largura do box do ícone. |
| --ez-tree__item-icon-box--padding | Define o espaçamento interno do ícone. |
| --ez-tree__badge--icon-color--default | Cor de ícone de badge padrão. |
| --ez-tree__badge--icon-color--error | Cor de ícone de badge de erro. |
| --ez-tree__badge--icon-color--success | Cor de ícone de badge sucesso. |
| --ez-tree__badge--icon-color--warning | Cor de ícone de badge de aviso. |
| --ez-tree__badge--icon-color--disabled | Cor de ícone de badge desabilitado. |
