> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-select-input/ (snapshot 2026-09-28)

# Multi Select Input

O **Multi Select Input** é um campo de formulário de múltipla seleção com o mesmo layout visual do Text Input (label flutuante, estados de foco/erro/desabilitado e modos regular/slim). Ao ser acionado por clique ou teclado, abre um Popover Plus ancorado ao campo, contendo um Multi Selection List. O gatilho exibe a contagem de itens marcados ("N selecionado(s)") e um chevron que alterna entre fechado e aberto.

### Exemplo formulário

#### Seleção atual

```
{
  "departamentos": [
    {
      "value": "2",
      "label": "Comercial",
      "check": true
    },
    {
      "value": "3",
      "label": "Logística",
      "check": true
    }
  ],
  "produtos": []
}
```

#### Log de Eventos

```jsx
import React, { useRef, useState } from 'react';
import { EzMultiSelectInput, EzButton } from '@sankhyalabs/ezui/react/components';
import './demo.css';

// Catálogo estático de departamentos (com estado inicial de marcação).
const DEPARTAMENTOS = [
    { value: '1', label: 'Financeiro', check: false },
    { value: '2', label: 'Comercial', check: true },
    { value: '3', label: 'Logística', check: true },
    { value: '4', label: 'Recursos Humanos', check: false },
    { value: '5', label: 'Tecnologia', check: false },
];

// Base de produtos simulando um carregamento de backend.
const PRODUTOS = [
    { label: 'Notebook', value: 'notebook' },
    { label: 'Monitor', value: 'monitor' },
    { label: 'Teclado', value: 'teclado' },
    { label: 'Mouse', value: 'mouse' },
    { label: 'Headset', value: 'headset' },
    { label: 'Webcam', value: 'webcam' },
];

const Demo = () => {
    const departamentosRef = useRef();

    // Cada campo recebe sua própria cópia das opções, evitando que a
    // marcação de um campo afete os demais (o componente atualiza o objeto).
    const departamentosOptions = useRef(DEPARTAMENTOS.map((o) => ({ ...o })));
    const setoresOptions = useRef(DEPARTAMENTOS.map((o) => ({ ...o })));

    const [departamentos, setDepartamentos] = useState(
        DEPARTAMENTOS.filter((o) => o.check)
    );
    const [produtos, setProdutos] = useState([]);
    const [logs, setLogs] = useState([]);

    const addLog = (message) => {
        setLogs((prev) => [
            `${new Date().toLocaleTimeString()}: ${message}`,
            ...prev.slice(0, 4),
        ]);
    };

    const produtosDataSource = {
        fetchData: (filterTerm) =>
            new Promise((resolve) => {
                setTimeout(() => {
                    const base = filterTerm
                        ? PRODUTOS.filter((p) =>
                              p.label.toLowerCase().includes(filterTerm.toLowerCase())
                          )
                        : PRODUTOS;
                    resolve(base.map((p) => ({ ...p, check: false })));
                }, 200);
            }),
        sortItems: (column, items) =>
            items.sort((a, b) => a.label.localeCompare(b.label)),
    };

    const handleDepartamentos = (evt) => {
        const selecionados = evt.detail.filter((o) => o.check);
        setDepartamentos(selecionados);
        addLog(`Departamentos: ${selecionados.length} selecionado(s)`);
    };

    const handleProdutos = (evt) => {
        const selecionados = evt.detail.filter((o) => o.check);
        setProdutos(selecionados);
        addLog(`Produtos: ${selecionados.length} selecionado(s)`);
    };

    const handleSubmit = async () => {
        const selecionados = await departamentosRef.current?.getSelectedOptions();
        addLog(`Formulário enviado com ${selecionados?.length ?? 0} departamento(s)`);
    };

    const handleReset = async () => {
        await departamentosRef.current?.clearSelection();
        setDepartamentos([]);
        setProdutos([]);
        addLog('Formulário limpo');
    };

    return (
        <div className="ez-multi-select-input-demo_container">
            <h3>Exemplo formulário</h3>
            <form>
                {/* Lista estática */}
                <EzMultiSelectInput
                    ref={departamentosRef}
                    label="Departamentos"
                    useOptions
                    options={departamentosOptions.current}
                    onEzChange={handleDepartamentos}
                />

                {/* Carregamento dinâmico via dataSource */}
                <EzMultiSelectInput
                    label="Produtos"
                    columnName="CODPROD"
                    isTextSearch
                    useOptions={false}
                    dataSource={produtosDataSource}
                    onEzChange={handleProdutos}
                />

                <section>
                    <EzButton
                        type="button"
                        className="ez-button--primary"
                        label="Enviar"
                        onClick={handleSubmit}
                    />
                    <EzButton type="button" label="Limpar" onClick={handleReset} />
                </section>
            </form>

            <h4>Seleção atual</h4>
            <pre>{JSON.stringify({ departamentos, produtos }, null, 2)}</pre>

            <h4>Log de Eventos</h4>
            <div>
                {logs.map((log) => (
                    <div key={log}>{log}</div>
                ))}
            </div>
        </div>
    );
};

export default Demo;
```

## Variações

### Lista estática (`options`)

A propriedade `options` recebe um catálogo do tipo `IMultiSelectionOption[]` (com `label`, `value` e `check`) que é renderizado com checkboxes. O gatilho contabiliza os itens com `check: true`.

Importante

Para utilizar a lista estática, defina `useOptions={true}`.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzMultiSelectInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    // O catálogo é mantido em um ref para que a referência seja estável
    // entre renderizações (o componente atualiza o estado de "check" do objeto).
    const options = useRef([
        { value: '1', label: 'Financeiro', check: false },
        { value: '2', label: 'Comercial', check: true },
        { value: '3', label: 'Logística', check: true },
        { value: '4', label: 'Recursos Humanos', check: false },
        { value: '5', label: 'Tecnologia', check: false },
    ]);

    return (
        <div className="ez-col--sd-6">
            <EzMultiSelectInput
                label="Departamentos"
                useOptions
                options={options.current}
            />
        </div>
    );
};

export default Demo;
```

### Carregamento dinâmico (`dataSource`)

Quando os itens vêm do backend, utilize a propriedade `dataSource` (um `IMultiSelectionListDataSource`) em conjunto com `columnName`. O `dataSource` oferece busca em tempo real através do `fetchData` e ordenação através do `sortItems`. A propriedade `isTextSearch` informa se a pesquisa é do tipo texto (`true`) ou numérica (`false`).

Importante

Para a utilização de `dataSource`, defina `useOptions={false}` e informe a propriedade `columnName`.

### Modos regular e slim

A propriedade `mode` controla a altura do campo: `regular` (42px) ou `slim` (32px).

demo.js

```jsx
import React, { useRef } from 'react';
import { EzMultiSelectInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const regularOptions = useRef([
        { value: '1', label: 'Financeiro', check: false },
        { value: '2', label: 'Comercial', check: true },
        { value: '3', label: 'Logística', check: false },
    ]);
    const slimOptions = useRef([
        { value: '1', label: 'Financeiro', check: false },
        { value: '2', label: 'Comercial', check: true },
        { value: '3', label: 'Logística', check: false },
    ]);

    return (
        <div className="ez-row">
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzMultiSelectInput
                    label="Modo regular (42px)"
                    mode="regular"
                    useOptions
                    options={regularOptions.current}
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzMultiSelectInput
                    label="Modo slim (32px)"
                    mode="slim"
                    useOptions
                    options={slimOptions.current}
                />
            </div>
        </div>
    );
};

export default Demo;
```

### Estados de interação

O campo acompanha os estados visuais do Text Input: inválido (`errorMessage`/`hasInvalid`), desabilitado (`enabled={false}`) e sem bordas (`noBorder`).

## Eventos

### Evento ezChange

Disparado a cada mudança real do conjunto de itens marcados. O payload é o array completo de opções (`IMultiSelectionOption[]`) com o estado de `check` atual.

Observação

As propriedades `options` e `dataSource` não refletem como atributo HTML (arrays e objetos não serializam bem). Atribua-as sempre via propriedade/JSX.

**Log de Eventos**

```jsx
import React, { useRef, useState } from 'react';
import { EzMultiSelectInput } from '@sankhyalabs/ezui/react/components';
import './ez-change.css';

const Demo = () => {
    const [logs, setLogs] = useState([]);
    const options = useRef([
        { value: '1', label: 'Financeiro', check: false },
        { value: '2', label: 'Comercial', check: true },
        { value: '3', label: 'Logística', check: false },
        { value: '4', label: 'Recursos Humanos', check: false },
    ]);

    const addLog = (message) => {
        setLogs((prev) => [
            `${new Date().toLocaleTimeString()}: ${message}`,
            ...prev.slice(0, 4),
        ]);
    };

    const handleChange = (event) => {
        const selecionados = event.detail.filter((o) => o.check);
        const rotulos = selecionados.map((o) => o.label).join(', ') || '—';
        addLog(`ezChange · ${selecionados.length} selecionado(s): ${rotulos}`);
    };

    return (
        <div className="eventos-container">
            <div className="ez-col--sd-6">
                <EzMultiSelectInput
                    label="Departamentos"
                    useOptions
                    options={options.current}
                    onEzChange={handleChange}
                />
            </div>

            <div className="ez-margin-top--large">
                <div className="logs-container">
                    <strong>Log de Eventos</strong>
                    {logs.map((log) => (
                        <div key={log} className="log-entry">
                            {log}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Demo;
```

## Métodos

### getSelectedOptions e clearSelection

  * **`getSelectedOptions()`** : retorna apenas as opções com `check: true`.
  * **`clearSelection()`** : limpa todas as seleções (delega ao Multi Selection List) e zera a contagem.

**getSelectedOptions():**
```
[
  {
    "value": "2",
    "label": "Comercial",
    "check": true
  },
  {
    "value": "3",
    "label": "Logística",
    "check": true
  }
]
```

## Integração com formulários

O componente integra-se ao Form View quando o metadata informa `userInterface: "MULTISELECTOR"`. As opções e o modo de carregamento são informados em `props` (`options` \+ `useOptions`, ou `dataSource` \+ `columnName`), e o `DataBinder` injeta a seleção armazenada em `value` no carregamento do registro, gravando-a de volta a cada `ezChange`.

```json
{
  "name": "DEPARTAMENTOS",
  "userInterface": "MULTISELECTOR",
  "label": "Departamentos",
  "readOnly": false,
  "properties": {
    "options": [
      { "value": "1", "label": "Financeiro", "check": false },
      { "value": "2", "label": "Comercial",  "check": false }
    ],
    "useOptions": true,
    "isTextSearch": false
  }
}
```

Observação

`props.options` também aceita o formato JSON `{"chave":"rótulo"}` (igual ao `OPTIONSELECTOR`), convertido para `IMultiSelectionOption[]` com `check: false`. O `columnName` assume o `name` do campo quando omitido, e `useOptions` é inferido (lista estática quando não há `dataSource`).

## API do componente

### Overview

Campo de formulário de múltipla seleção. Possui o mesmo layout visual do `ez-text-input` (label flutuante, estados de foco/erro/desabilitado) e, ao ser acionado, abre um `ez-popover-plus` ancorado ao campo contendo um `ez-multi-selection-list`. O campo exibe o texto "N selecionado(s)" com a contagem de itens marcados.

Suporta tanto lista estática (`options`) quanto carregamento dinâmico via `dataSource`/`columnName`. O valor selecionado é exposto pela prop `value` e pelo evento `ezChange` (ambos no formato `IMultiSelectionOption[]`), o que permite a vinculação automática a formulários através do `DataBinder` quando o metadata informa `userInterface: "MULTISELECTOR"`.

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| columnName | column-name | Nome da coluna para o datasource. | string | undefined |
| dataSource | -- | Datasource dinâmico passado para o ez-multi-selection-list. | IMultiSelectionListDataSource | undefined |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| hasInvalid | has-invalid | Define se o campo está em estado inválido (bordas vermelhas). | boolean | false |
| isTextSearch | is-text-search | Informa se a pesquisa é do tipo texto ou numérico. | boolean | false |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | 'regular' |
| noBorder | no-border | Se true o campo não terá bordas. | boolean | false |
| options | -- | Opções estáticas passadas para o ez-multi-selection-list. | IMultiSelectionOption[] | undefined |
| orderSelectedFirst | order-selected-first | Define se as opções marcadas devem ser reordenadas para o topo da lista. Quando false (padrão), a ordem original das opções é preservada — os itens não "pulam" para o topo ao serem selecionados. Defina true para manter os selecionados no topo (ordenados). | boolean | false |
| useOptions | use-options | Alterna entre lista estática (true) e datasource (false). | boolean | false |
| value | -- | Valor do campo: as opções com o estado de check atual (mesmo formato do payload de ezChange ). Usado para a vinculação com formulários (read-back do DataBinder). Não reflete como atributo pois arrays não serializam bem em HTML. | IMultiSelectionOption[] | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando a seleção de itens na lista é alterada. O payload é o array completo das opções com seu estado de check. | CustomEvent<IMultiSelectionOption[]> |

### Methods

#### `clearSelection() => Promise<void>`

Limpa todas as seleções. Delega ao ez-multi-selection-list.

##### Returns

Type: `Promise<void>`

#### `getSelectedOptions() => Promise<IMultiSelectionOption[]>`

Retorna as opções com o estado de check atual.

##### Returns

Type: `Promise<IMultiSelectionOption[]>`

### Dependencies

#### Used by

  * ez-form-view

#### Depends on

  * ez-icon
  * ez-tooltip
  * ez-popover-core
  * ez-multi-selection-list

### CSS Variables

| Variable | Description |
|---|---|
| --ez-multi-select-input--height | Define a altura do componente. |
| --ez-multi-select-input--height--slim | Define a altura do componente em modo "slim". |
| --ez-multi-select-input--width | Define a largura do componente. |
| --ez-multi-select-input__min-width | Define a largura mínima do componente. |
| --ez-multi-select-input__max-width | Define a largura máxima do componente. |
| --ez-multi-select-input__icon--width | Define a largura reservada para o ícone à direita. |
| --ez-multi-select-input--font-size | Define o tamanho da fonte do componente. |
| --ez-multi-select-input--font-family | Define a família da fonte do componente. |
| --ez-multi-select-input--font-weight | Define o peso da fonte do componente. |
| --ez-multi-select-input--color | Define a cor da fonte do componente. |
| --ez-multi-select-input--border-radius | Define o raio da borda do componente. |
| --ez-multi-select-input__input--border | Define o estilo da borda. |
| --ez-multi-select-input__input--border-color | Define a cor da borda. |
| --ez-multi-select-input__input--focus--border-color | Define a cor da borda quando focado. |
| --ez-multi-select-input__input--error--border-color | Define a cor da borda quando com erro. |
| --ez-multi-select-input__input--background-color | Define a cor de fundo do campo. |
| --ez-multi-select-input__input--disabled--background-color | Define a cor de fundo quando desabilitado. |
| --ez-multi-select-input__input--disabled--color | Define a cor do texto quando desabilitado. |
| --ez-multi-select-input__label--floating--top | Define o posicionamento do label flutuante. |
| --ez-multi-select-input__label--padding-top | Define o espaçamento superior do label. |
| --ez-multi-select-input__label--padding-left | Define o espaçamento esquerdo do label. |
| --ez-multi-select-input__placeholder--color | Define a cor do placeholder. |
| --ez-multi-select-input__tooltip_icon--error--color | Define a cor do ícone de erro. |
| --ez-multi-select-input__tooltip-icon---width | Define a largura do ícone de erro. |
| --ez-multi-select-input__tooltip-icon---horizontal-margin | Define a margem horizontal do ícone de erro. |
| --ez-multi-select-input__tooltip-icon---vertical-margin | Define a margem vertical do ícone de erro. |
