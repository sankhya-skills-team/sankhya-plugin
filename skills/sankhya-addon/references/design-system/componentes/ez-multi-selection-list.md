> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list/ (snapshot 2026-09-28)

# Multi Selection List

`<EzMultiSelectionList />` é um componente versátil que permite aos usuários selecionar múltiplos itens de uma lista. O componente oferece duas formas principais de renderização: através de uma lista estática de opções (`options`) ou através de um callback dinâmico (`dataSource`) que permite busca no backend.

* * * * demo.js

```jsx
import { EzMultiSelectionList } from '@sankhyalabs/ezui/react/components';

import React from 'react';

const Demo = () => {

    const options = [
        {
            label: 'Valor 1',
            value: '1',
            check: true
        },
        {
            label: 'Valor 2',
            value: '2',
            check: true
        },
        {
            label: 'Valor 3',
            value: '3',
            check: true
        },
        {
            label: 'Valor 4',
            value: '4',
            check: true
        }
    ];

    return (
        <EzMultiSelectionList
            options={options}
            useOptions={true}
        />
    )
};

export default Demo;
```

## Renderização com `options`

A propriedade `options` recebe uma lista do tipo `IMultiSelectionOption` e renderiza essa lista com checkboxes. Cada opção possui:

  * `label`: Texto exibido para o usuário
  * `value`: Valor único para identificação
  * `check`: Estado inicial (selecionado ou não)

Importante

Para que o filtro funcione corretamente com `options`, você deve definir `useOptions={true}`.

* * * * * demo.js

```jsx
import { EzMultiSelectionList } from '@sankhyalabs/ezui/react/components';

const RenderOption = () => {
    const options = [
        {
            label: 'JavaScript',
            value: 'js',
            check: true
        },
        {
            label: 'TypeScript',
            value: 'ts',
            check: false
        },
        {
            label: 'Python',
            value: 'py',
            check: true
        },
        {
            label: 'Java',
            value: 'java',
            check: false
        },
        {
            label: 'C#',
            value: 'csharp',
            check: false
        }
    ];

    return (
        <EzMultiSelectionList
            options={options}
            useOptions={true}
        />
    );
};

export default RenderOption;
```

## Renderização com `dataSource`

A propriedade `dataSource` permite integração dinâmica com backends, oferecendo busca em tempo real e carregamento sob demanda.

O `IMultiSelectionListDataSource` deve implementar:

  * `fetchData(filterTerm, fieldName)`: Callback que retorna uma Promise com os dados filtrados
  * `sortItems(column, items)`: Função para ordenação dos resultados

Importante

Para a utilização de `dataSource`, é necessário definir a propriedade `columnName`.

#### Multi Selection List com DataSource Avançado

Digite para buscar produtos por nome ou categoria...

Selecione os valores a serem filtrados através do campo de busca.

## Eventos

O componente oferece o evento `onChangeFilteredOptions` para capturar alterações na seleção. Este evento é disparado sempre que a seleção é alterada, permitindo que você reaja a essas mudanças.

Observação

Ao selecionar ou desmarcar itens, o objeto passado para a propriedade `options` é atualizado automaticamente.

#### Multi Selection List com Eventos

* * * * **Log de Eventos**

14:36:40: ezChange - Valores selecionados: [{"label":"Produto B","value":"produto-b","check":true},{"label":"Produto D","value":"produto-d","check":true},{"label":"Produto A","value":"produto-a","check":false},{"label":"Produto C","value":"produto-c","check":false}]

```jsx
import { EzMultiSelectionList } from '@sankhyalabs/ezui/react/components';
import { useRef, useState } from 'react';
import './events.css';

const Events = () => {
    const [logs, setLogs] = useState([]);
    const options = useRef([
        {
            label: 'Produto A',
            value: 'produto-a',
            check: false
        },
        {
            label: 'Produto B',
            value: 'produto-b',
            check: true
        },
        {
            label: 'Produto C',
            value: 'produto-c',
            check: false
        },
        {
            label: 'Produto D',
            value: 'produto-d',
            check: true
        }
    ]);

    const addLog = (message) => {
        setLogs(prev => [`${new Date().toLocaleTimeString()}: ${message}`, ...prev.slice(0, 4)]);
    };

    const handleChange = (event) => {
        addLog(`ezChange - Valores selecionados: ${JSON.stringify(event.detail)}`);
    };

    return (
        <div className="eventos-container">
            <h4 className="eventos-title">Multi Selection List com Eventos</h4>
            <EzMultiSelectionList
                options={options.current}
                useOptions={true}
                onChangeFilteredOptions={handleChange}
            />

            <div className="ez-margin-top--large">
                <div className="logs-container">
                    <strong>Log de Eventos</strong>
                    {logs.map((log, index) => (
                        <div key={index} className="log-entry">{log}</div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Events;
```

## Métodos:

O componente `EzMultiSelectionList` oferece um método para a limpeza dos itens adicionados:

  * **`clearFilteredOptions()`** : Limpa a seleção atual

Selecione os valores a serem filtrados através do campo de busca.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| columnName | column-name | Nome da coluna onde serão aplicadas as opções selecionadas. | string | undefined |
| dataSource | -- | Classe que implementa o método fetchData, responsável por realizar a pesquisa dos dados, com base no termo informado pelo usuário. | IMultiSelectionListDataSource | undefined |
| isTextSearch | is-text-search | Informa se a pesquisa é do tipo texto ou numérico. | boolean | false |
| options | -- | Opções de filtros a serem exibidas na listagem. | IMultiSelectionOption[] | undefined |
| orderSelectedFirst | order-selected-first | Define se as opções marcadas devem ser reordenadas para o topo da lista (e ordenadas alfabeticamente/pelo datasource). Quando false , a ordem original das opções é preservada — inclusive ao marcar/desmarcar itens. Padrão: true (mantém o comportamento histórico). | boolean | true |
| useOptions | use-options | Indica se deve ser exibida lista de opções do atributo options (true), ou se deve utilizar o datasource (false) | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| changeFilteredOptions | Evento que informa que a lista de opções selecionadas sofreu alteração. | CustomEvent<IMultiSelectionOption[]> |

### Methods

#### `clearFilteredOptions() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `clearSelection() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-multi-select-input
  * filter-column

#### Depends on

  * ez-check
  * ez-list
  * ez-icon
  * multi-selection-box-message
  * ez-filter-input
  * ez-search
