> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view/ (snapshot 2026-09-28)

# Form View

Esse componente é responsável por criar os campos e distribuí-los responsivamente no espaço disponível. Ele é usado pelo EzForm para diagramar o conteúdo interno

IMPORTANTE

##### EzForm vs. EzFormView

Ao contrário EzForm que cuida de todo o fluxo de dados, o EzFormView somente cria a estrutura dos campos.

demo.js

```jsx
import React from 'react';
import { EzFormView } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzFormView fields={fields} />
    )
};

export default Demo;

const fields = [
    { name: "nomeCliente", label: "Nome", group: "Dados bancários", userInterface: "SHORTTEXT", required: true },
    { name: "dataCadastro", label: "Data de cadastro", group: "Dados bancários", userInterface: "DATE", required: true },
    {
        name: "departamentos",
        label: "Departamentos",
        group: "Dados bancários",
        userInterface: "MULTISELECTOR",
        props: {
            useOptions: true,
            options: [
                { value: "1", label: "Financeiro", check: false },
                { value: "2", label: "Comercial", check: false },
                { value: "3", label: "Logística", check: false }
            ]
        }
    },
    { name: "valorDesconto", label: "Desconto", group: "Valores", userInterface: "DECIMALNUMBER", props: { precision: 2 } },
    { name: "valorMulta", label: "Multa", group: "Valores", userInterface: "DECIMALNUMBER", props: { precision: 2 } },
    { name: "historico", label: "Histórico", userInterface: "LONGTEXT", readOnly: true }
];
```

## Variações e estados

### Atribuindo metadados

> Propriedade utilizada: **fields**

Atribuindo um array com objetos tipo `IFormViewField`, para cada elemento será criado um campo, respeitando o `UserInterface`. Os campos serão envolvidos em uma estrutura responsiva (ajustável de acordo com o espaço disponível), automatizando o trabalho de diagramá-los.

demo.js

```jsx
import React from 'react';
import { EzFormView } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzFormView fields={fields} />
    )
};

export default Demo;

const fields = [
    { name: "nomeCliente", label: "Nome", userInterface: "SHORTTEXT" },
    { name: "dataCadastro", label: "Data de cadastro", userInterface: "DATE" },
    {
        name: "departamentos",
        label: "Departamentos",
        userInterface: "MULTISELECTOR",
        props: {
            useOptions: true,
            options: [
                { value: "1", label: "Financeiro", check: false },
                { value: "2", label: "Comercial", check: false },
                { value: "3", label: "Logística", check: false }
            ]
        }
    },
    { name: "valorDesconto", label: "Desconto", userInterface: "DECIMALNUMBER", props: { precision: 2 } },
    { name: "valorMulta", label: "Multa", userInterface: "DECIMALNUMBER", props: { precision: 2 } },
    { name: "historico", label: "Histórico", userInterface: "LONGTEXT" }
];
```

Observação

Os campos serão apenas adicionados ao DOM, sem qualquer tipo de bind ou tratamento de eventos específicos. Todos os campos terão o atributo `data-field-name` preenchido, sendo possível acessá-los através de queryString.

### Grupos

> Propriedade utilizada: **IFormViewField.group**

Usado para organizar os campos em grupos, além de permitir que o usuário se concentre em um grupo por vez, contraindo os outros.

### Campos sinalizados como requerido

> Propriedade utilizada: **IFormViewField.required**

Campos requeridos são sinalizados visualmente.

demo.js

```jsx
import React from 'react';
import { EzFormView } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzFormView fields={fields} />
    )
};

export default Demo;

const fields = [
    { name: "nomeCliente", label: "Nome", userInterface: "SHORTTEXT", required: true  },
    { name: "dataCadastro", label: "Data de cadastro", userInterface: "DATE", required: true  },
    { name: "valorDesconto", label: "Desconto", userInterface: "DECIMALNUMBER", required: true , props: {precision: 2} },
    { name: "valorMulta", label: "Multa", userInterface: "DECIMALNUMBER", required: true , props: {precision: 2} },
    { name: "historico", label: "Histórico", userInterface: "LONGTEXT", required: true }
];
```

Observação

Não há validação de preenchimento, apenas a sinalização.

### Campos com edição desabilitada

> Propriedade utilizada: **IFormViewField.readOnly**

Em várias situações, pode ser necessário exibir o valor do campo, mas mantendo-o inativo para edição.

### Campos com elementos nas extremidades

Permite a adição de elementos nas extremidades do formulário, incluindo botões, ícones, badges ou qualquer outro elemento desejado.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

demo.js

```jsx
import { EzDialog, EzFormView } from '@sankhyalabs/ezui/react/components';
import React, { useRef } from 'react';

const fields = [
    { name: "nomeCliente", label: "Nome", userInterface: "SHORTTEXT" },
    { name: "dataCadastro", label: "Data de cadastro", userInterface: "DATE" },
    { name: "valorDesconto", label: "Desconto", userInterface: "DECIMALNUMBER", props: { precision: 2 } },
    { name: "valorMulta", label: "Multa", userInterface: "DECIMALNUMBER", props: { precision: 2 } },
    { name: "historico", label: "Histórico", userInterface: "LONGTEXT" }
];

const Demo = () => {
    const dialog = useRef();

    function showDialog(title, message){
        dialog.current.show(title, message, "warn");
    }

    function formItemsReady(items){
        let div = document.createElement("div");
        div.classList.add("ez-flex", "ez-flex--row");

        const addAttr = (el, elName) => {
            el.setAttribute("mode", "icon");
            el.setAttribute("icon-name", "chevron-right");
            el.setAttribute("title", elName);
            el.classList.add("ez-button--tertiary");
            el.addEventListener("click", function(){
                showDialog("Click!", `${elName} foi clicado!`);
            });
        }

        let btn = document.createElement("ez-button");
        addAttr(btn, 'btn1');

        let btn2 = document.createElement("ez-button");
        addAttr(btn2, 'btn2');

        let btn3 = document.createElement("ez-button");
        addAttr(btn3, 'btn3');

        div.appendChild(btn2);
        div.appendChild(btn3);

        items.get("nomeCliente")?.addRightElement(btn);

        items.get("dataCadastro")?.addRightElement(div);
    };

    return (
        <div className="ez-flex">
            <EzDialog ref={dialog} />
            <EzFormView fields={fields} onFormItemsReady={(evt) => formItemsReady(evt.detail.items)} />
        </div>
    )
};
export default Demo;
```

## Alterção dinâmica de props

É possível alterar dinamicamente propriedades de campos através do método **setFieldProp** do componente.

## Editores customizados

Através do método **addCustomEditor** , é possível adicionar editores customizados (**ICustomEditor**) no lugar de campos do formulário. Quando nenhum editor customizado é adicionado à coluna, seu campo padrão é renderizado.

Existem quatro retornos possíveis para o métodoo **getEditorElement** do **ICustomEditor** , sendo eles:

  * **Nulo/indefinido** : renderiza o elemento padrão para aquele campo;
  * **O elemento padrão** : renderiza o elemento padrão para aquele campo;
  * **Uma string** : faz o parse da string e renderiza o elemento passado;
  * **Um elemento HTML** : renderiza o elemento.

Importante

O método **renderToString** não aceita **nenhum** código javascript. Para um botão, por exemplo, um onClick não irá funcionar. O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTMLAllCollection.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| customUiBuilders | -- | Define construtores customizados para tipos de campos específicos | Map<UserInterface, (field: IFormViewField, context?: IFieldBuilderContext) => HTMLElement> | new Map() |
| fields | -- | Define a lista de metadados usada para criar os campos de user interface. | IFormViewField[] | undefined |
| formLayout | form-layout | Define o layout do formulário. | FormLayout.CASCADE \| FormLayout.CLASSIC_CASCADE \| FormLayout.CLASSIC_SIDE_BY_SIDE \| FormLayout.SIDE_BY_SIDE | undefined |
| selectedRecord | -- | Define os registros da linha selecionada. | Record | undefined |
| singleColumn | single-column | Define se o formulario deve possuir apenas 1 coluna. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| ezContentReady | Evento emitido quando o componente foi totalmente carregado na DOM. | CustomEvent<HTMLElement[]> |
| formItemsReady | Responsável por notificar quando ocorrer a renderização de itens do formulário. | CustomEvent<FormItems> |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

##### Returns

Type: `Promise<void>`

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

Altera/adiciona uma propriedade nos metados do campo.

##### Returns

Type: `Promise<void>`

#### `showUp() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form

#### Depends on

  * ez-custom-form-input
  * ez-collapsible-box
  * ez-check
  * ez-classic-combo-box
  * ez-combo-box
  * ez-classic-date-input
  * ez-date-input
  * ez-classic-time-input
  * ez-time-input
  * ez-classic-date-time-input
  * ez-date-time-input
  * ez-upload
  * ez-classic-number-input
  * ez-number-input
  * ez-classic-text-area
  * ez-text-area
  * ez-classic-input
  * ez-text-input
  * ez-classic-search-plus
  * ez-search-plus
  * ez-classic-search
  * ez-search
  * ez-rich-text
  * ez-image-input
  * ez-multi-select-input

### CSS Variables

| Variable | Description |
|---|---|
| --ez-form-view__item--min-width | Define o tamanho mínimo dos itens do formulário. |
| --ez-form-view__long-item--min-width | Define o tamanho mínimo dos itens do formulário. |
| --ez-form-view__item--max-width | Define o tamanho máximo dos itens do formulário. |
| --ez-form-view__long-item--max-width | Define o tamanho máximo dos itens longos do formulário. |
| --ez-form-view__item--gap | Define o colunas entre itens do formulário. |
| --ez-form-view__item--padding | Define o padding do formulário. |
