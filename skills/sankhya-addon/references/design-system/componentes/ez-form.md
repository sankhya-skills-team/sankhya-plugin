> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form/ (snapshot 2026-09-28)

# Form

Documentação do componente EzForm.

```
{}
```

```jsx
import React, { useEffect, useState } from 'react';
import { Action, DataUnit } from '@sankhyalabs/core';
import { EzForm } from '@sankhyalabs/ezui/react/components';
import './demo.css';

/**
 * Exemplo de JSON com o metadata do formulário.
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        {
            "name": "_dadosBancarios_nomeCliente",
            "label": "Nome do cliente",
            "dataType": "TEXT",
            "userInterface": "SHORTTEXT",
            "readOnly": false,
            "required": true
        },
        {
            "name": "_dadosBancarios_dataCadastro",
            "label": "Data do cadastro",
            "dataType": "DATE",
            "userInterface": "DATE",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorDesconto",
            "label": "Desconto",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorMulta",
            "label": "Multas",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "departamentos",
            "label": "Departamentos",
            "dataType": "OBJECT",
            "userInterface": "MULTISELECTOR",
            "properties": {
                // mesma fonte de opções do OPTIONSELECTOR: JSON {chave:rótulo} ou array
                "options": "{\"1\":\"Financeiro\",\"2\":\"Comercial\",\"3\":\"Logística\"}",
                // opcionais (todos via properties):
                "isTextSearch": false,
                "orderSelectedFirst": false
            },
            "readOnly": false,
            "required": false
        },
        {
            "name": "_dadosBancarios_historico",
            "label": "Observações",
            "dataType": "TEXT",
            "userInterface": "LONGTEXT",
            "readOnly": true,
            "required": false
        }
    ]
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState();
    const [logsRecord, setLogsRecord] = useState({});

    useEffect(() => {
        setDataUnit(new DataUnit());
    }, []);

    function dataUnitObserver(action) {
        if(action.type === Action.DATA_CHANGED) {
            setLogsRecord(dataUnit.getSelectedRecord());
        }
    }

    useEffect(() => {
        if (dataUnit == undefined) return;
        dataUnit.metadataLoader = metadataLoader;
        dataUnit.loadMetadata();
        dataUnit.subscribe(dataUnitObserver);

        return () => {
            dataUnit.unsubscribe(dataUnitObserver);
        }
    }, [dataUnit]);

    async function metadataLoader() {
        return new Promise((resolve) => {
            resolve(metadata)
        });
    }

    return (
        <div className="ez-form-demo_container">
            { dataUnit && <EzForm dataUnit={dataUnit}></EzForm> }
            <pre>{JSON.stringify(logsRecord, null, 2)}</pre>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Com config

Com configuração do formulário.

Observação

Os atributos `readOnly` e `required` dos campos vindos no metadata do dataUnit, com valor `true`, terão prioridade sobre os mesmos atributos inseridos na config. Por exemplo, se o campo `Nome do cliente` vier com `required: true` no metadata do dataUnit, este mesmo atributo do campo na config, não será considerado.

### Conteúdo estático

É possível criar conteúdo específico sem o uso de quaisquer tipos de metainformações. Neste contexto, o formulário fará o vínculo entre os campos (EzTextInput, EzDateInput, etc...) e o DataUnit, além de validar os registros. Para isso, é preciso fornecer o atributo **data-field-name** para cada campo.

demo.js

```jsx
import React from 'react';
import { DataUnit } from '@sankhyalabs/core';
import { EzDateInput, EzForm, EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzForm dataUnit={dataUnit}>
            <EzTextInput data-field-name="nomeCliente" label="Nome:"/>
            <EzDateInput data-field-name="dataCadastro" label="Cadastrado em:"/>
        </EzForm>
    )
};

export default Demo;

/**
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const dataUnit = new DataUnit();
dataUnit.metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        { "name": "nomeCliente", "label": "Nome do cliente", "dataType": "TEXT", "userInterface": "SHORTTEXT" },
        { "name": "dataCadastro", "label": "Data de cadastro", "dataType": "DATE", "userInterface": "DATE" },
        { "name": "valorDesconto", "label": "Desconto", "dataType": "NUMBER", "userInterface": "DECIMALNUMBER" },
        { "name": "valorMulta", "label": "Multas", "dataType": "NUMBER", "userInterface": "DECIMALNUMBER" },
        { "name": "historico", "label": "Observações", "dataType": "TEXT", "userInterface": "LONGTEXT"}
    ]
};
dataUnit.addRecord();
```

### Com abas e grupos

Às vezes é necessário organizar os campos em abas e grupos, assim a interface fica mais objetiva e específica, permitindo que o usuário se concentre em um ponto por vez.

demo.js

```jsx
import React from 'react';
import { DataUnit } from '@sankhyalabs/core';
import { EzForm } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzForm dataUnit={dataUnit} config={config} />
    )
};

export default Demo;

/**
 * Todos os campo que não possuem aba específica, serão
 * alocados na aba "Principal". Assim, veja que distribuimos
 * os campos de maneira conveniente em duas abas, e na aba
 * principal, temos dois grupos. Dessa forma o usuário é capaz
 * de ocultar as informações que não são importantes.
 */
const config = {
    "fields": [
        { "name": "historico", "tab": "Histórico" },
        { "name": "nomeCliente", "group": "Dados bancários" },
        { "name": "dataCadastro", "group": "Dados bancários" },
        { "name": "valorDesconto", "group": "Valores" },
        { "name": "valorMulta", "group": "Valores" }
    ]
};

/**
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const dataUnit = new DataUnit();
dataUnit.metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        { "name": "nomeCliente", "label": "Nome do cliente", "dataType": "TEXT", "userInterface": "SHORTTEXT" },
        { "name": "dataCadastro", "label": "Data de cadastro", "dataType": "DATE", "userInterface": "DATE" },
        { "name": "valorDesconto", "label": "Desconto", "dataType": "NUMBER", "userInterface": "DECIMALNUMBER" },
        { "name": "valorMulta", "label": "Multas", "dataType": "NUMBER", "userInterface": "DECIMALNUMBER" },
        { "name": "historico", "label": "Observações", "dataType": "TEXT", "userInterface": "LONGTEXT"}
    ]
};
dataUnit.addRecord();
```

### Validate

Exemplo de como validar o formulário.

### Com recordsValidator

Define um validador responsável pela integridade dos registros.

Observação

No exemplo a seguir, está sendo validado o valor do campo Desconto, que não pode ser valor zero (R$ 0,00).

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { Action, DataUnit } from '@sankhyalabs/core';
import { EzForm, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';

/**
 * Exemplo de JSON com o metadata do formulário.
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        {
            "name": "_dadosBancarios_nomeCliente",
            "label": "Nome do cliente",
            "dataType": "TEXT",
            "userInterface": "SHORTTEXT",
            "readOnly": false,
            "required": true
        },
        {
            "name": "_dadosBancarios_dataCadastro",
            "label": "Data do cadastro",
            "dataType": "DATE",
            "userInterface": "DATE",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorDesconto",
            "label": "Desconto",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorMulta",
            "label": "Multas",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_dadosBancarios_historico",
            "label": "Observações",
            "dataType": "TEXT",
            "userInterface": "LONGTEXT",
            "readOnly": true,
            "required": false
        }
    ]
};

const Demo = () => {
    const element = useRef(null);
    const [dataUnit, setDataUnit] = useState();

    /**
     * Exemplo do uso da propriedade recordsValidator para validar com uma condição específica,
     * neste caso está validando o valor do campo Desconto, que não pode ser valor zero (R$ 0,00).
     */
    const recordsValidator = {
        validateRecord: (record) => {
            const discountAmount = record["_valores_valorDesconto"];

            if (discountAmount != undefined && Number(discountAmount) === 0) {
                return {
                    isValid: false,
                    errorTitle: "Título de Atenção",
                    errorMessage: "Valor do desconto deve ser maior que zero."
                }
            }
        }
    }

    useEffect(() => {
        setDataUnit(new DataUnit());
    }, []);

    useEffect(() => {
        if (dataUnit == undefined) return;
        dataUnit.metadataLoader = metadataLoader;
        dataUnit.loadMetadata();
    }, [dataUnit]);

    async function metadataLoader() {
        return new Promise((resolve) => {
            resolve(metadata)
        });
    }

    function onValidate() {
        element.current.validate();
    }

    function onDataUnitEvent(action) {
        if (action?.type === Action.RECORDS_ADDED) {
            onValidate();
        }
    }

    function onSubmit() {
        if (dataUnit == undefined) return;
        if (dataUnit.records.length === 0) {
            dataUnit.subscribe(onDataUnitEvent);
            dataUnit.addRecord();
        } else {
            onValidate();
        }
    }

    return (
        <div className="ez-flex ez-flex--column">
            <EzButton
                label="Validar Formulário"
                className="ez-margin-bottom--medium ez-margin-left--auto"
                onClick={onSubmit}
            >
                <EzIcon
                    iconName="check-circle-inverted"
                    slot="leftIcon"
                    className="ez-margin-right--small">
                </EzIcon>
            </EzButton>

            {
                dataUnit &&
                <EzForm
                    ref={element}
                    dataUnit={dataUnit}
                    recordsValidator={recordsValidator}>
                </EzForm>
            }
        </div>
    )
};

export default Demo;
```

### Com elementos nas extremidades

Permite a adição de elementos nas extremidades do formulário, incluindo botões, ícones, badges ou qualquer outro elemento desejado.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

### Submit

Exemplo de como utilizar o submit.

demo.js

```jsx
import React, { useEffect, useState } from 'react';
import { Action, DataUnit } from '@sankhyalabs/core';
import { EzForm, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

/**
 * Exemplo de JSON com o metadata do formulário.
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        {
            "name": "_dadosBancarios_nomeCliente",
            "label": "Nome do cliente",
            "dataType": "TEXT",
            "userInterface": "SHORTTEXT",
            "readOnly": false,
            "required": true
        },
        {
            "name": "_dadosBancarios_dataCadastro",
            "label": "Data do cadastro",
            "dataType": "DATE",
            "userInterface": "DATE",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorDesconto",
            "label": "Desconto",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorMulta",
            "label": "Multas",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_dadosBancarios_historico",
            "label": "Observações",
            "dataType": "TEXT",
            "userInterface": "LONGTEXT",
            "readOnly": true,
            "required": false
        }
    ]
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState();
    const [enabled, setEnabled] = useState(false);

    useEffect(() => {
        setDataUnit(new DataUnit());
    }, []);

    useEffect(() => {
        if (dataUnit == undefined) return;
        dataUnit.subscribe(onDataUnitEvent);
        dataUnit.metadataLoader = metadataLoader;
        dataUnit.saveLoader = saveLoader;
        dataUnit.loadMetadata();
    }, [dataUnit]);

    async function metadataLoader() {
        return new Promise((resolve) => {
            resolve(metadata)
        });
    }

    async function saveLoader() {
        return new Promise((resolve) => {
            resolve(dataUnit.records)
        });
    }

    function onDataUnitEvent(action) {
        const type = action?.type;
        if (type === Action.CHANGING_DATA || type === Action.DATA_CHANGED) {
            setEnabled(true);
        } else if (type === Action.DATA_SAVED) {
            setEnabled(false);
            ApplicationUtils.success("Título de Sucesso", "Salvo com sucesso!");
        }
    }

    function onSubmit() {
        if (dataUnit == undefined) return;
        dataUnit.saveData();
    }

    return (
        <div className="ez-flex ez-flex--column">
            <EzButton
                label="Salvar"
                className="ez-margin-bottom--medium ez-margin-left--auto"
                onClick={onSubmit}
                enabled={enabled}
            >
                <EzIcon iconName="save" slot="leftIcon" className="ez-margin-right--small"></EzIcon>
            </EzButton>

            { dataUnit && <EzForm dataUnit={dataUnit}></EzForm> }
        </div>
    )
};

export default Demo;
```

### Cancel

Exemplo de como cancelar edição no formulário.

### Principais componentes

A seguir temos a arquitetura do ez-form, apresentando seus principais componentes e como eles interagem ente si.

#### Processo de updateValue

Arquitetura apresentando o processo de updateValue dos campos do formulário.

#### DataBinder

Realiza o processo de construção dos campos de acordo com o DataUnit, cria os eventos de controle de ações (`DATA_SAVED`, `DATA_CHANGED`, `RECORDS_ADDED`, etc.) e atualiza os campos do formulário de acordo com esses eventos.

#### form.slice

Reducer utilizado para controlar os estados de uso do formulário, como no carregamento do metadata (`METADATA_LOADED`), na alteração realizada nas abas de navegação (`CHANGE_TAB`) e para capturar o metadata do estado atual do formulário (`selectFormMetadata`).

#### FormSheet

Este componente é utilizado para realizar a renderização total do formulário de acordo com as configurações tratadas pelo `form.slice`, este componente consiste na construção de um componente funcional do tipo `FormSheetProps` e possui os seguintes atributos:

| Atributo | Tipo |
|---|---|
| source | FormSheetMetadata |
| store | Store |
| dataElementId | string |

#### FormMetadata

Realiza o carregamento e tratamento do metadata de cada campo do formulário, ele controla uma lista de campos do tipo `FormSheetMetadata` que consiste nos seguintes atributos:

| Atributo | Tipo |
|---|---|
| name | string |
| label | string |
| items | Array<FieldMetadata \| FieldSetMetadata> |
| requiredFields | Array<string> |
| cleanOnCopyFields | Array<string> |
| defaultValues | any |

| Atributo | Tipo |
|---|---|
| label | string |
| items | Array<FieldMetadata> |

| Atributo | Tipo |
|---|---|
| descriptor | FieldDescriptor |
| config | IFieldConfig |

#### FormItem

É utilizado para realizar a renderização de cada campo do formulário de acordo com o metadata carregado, este componente consiste na construção de um componente funcional do tipo `FormItemProps` e possui os seguintes atributos:

| Atributo | Tipo |
|---|---|
| source | FieldMetadata \| FieldSetMetadata |
| store | Store |

#### FieldBuilder

Realiza a renderização do campo de acordo com o seu tipo específico. Podem ser carregados nos seguintes formatos de `UserInterface`:

| Tipo | Descrição |
|---|---|
| LONGTEXT | Campo com caixa de texto maior |
| CHECKBOX | Campo de marcação |
| SWITCH | Campo de marcação |
| OPTIONSELECTOR | Campo com lista de seleção |
| SEARCH | Campo de busca |
| FILE | Campo de anexo |
| DATE | Campo de data |
| TIME | Campo de tempo |
| DATETIME | Campo de data e hora |
| DECIMALNUMBER | Campo com casas decimais |
| INTEGERNUMBER | Campo com número inteiro |

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

O método **renderToString** não aceita **nenhum** código javascript. Para um botão, por exemplo, um onClick não irá funcionar. O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTML.

demo.js

```jsx
import React, { useCallback, useEffect, useRef, useState } from 'react';
import { Action, DataUnit } from '@sankhyalabs/core';
import { EzForm, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';
import { renderToString } from 'react-dom/server';

/**
 * Exemplo de JSON com o metadata do formulário.
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        {
            "name": "_dadosBancarios_nomeCliente",
            "label": "Nome do cliente",
            "dataType": "TEXT",
            "userInterface": "SHORTTEXT",
            "readOnly": false,
            "required": true
        },
        {
            "name": "_dadosBancarios_dataCadastro",
            "label": "Data do cadastro",
            "dataType": "DATE",
            "userInterface": "DATE",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorDesconto",
            "label": "Desconto",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorMulta",
            "label": "Multas",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_dadosBancarios_historico",
            "label": "Observações",
            "dataType": "TEXT",
            "userInterface": "TEXT",
            "readOnly": true,
            "required": false
        }
    ]
};

const Demo = () => {
    const ezFormRef = useRef(null);
    const [dataUnit, setDataUnit] = useState();

    const addCustomEditor = useCallback(async () => {
        const customEditorDataCadastro = {
            getEditorElement: () => {
                return null;
            }
        }

        const customEditorValorDesconto = {
            getEditorElement: (params) => {
                return params.currentEditor;
            }
        }

        const customEditorValorMulta = {
            getEditorElement: () => {
                return renderToString(<EzButton label='Teste'/>);
            }
        }

        const customEditorHistorico = {
            getEditorElement: () => {
                const launchButton = document.createElement('ez-button');
                launchButton.mode = 'icon';
                launchButton.iconName = 'warning-outline';
                launchButton.onclick = () => {console.log('CLICK DO BOTÃO')};

                return launchButton;
            }
        }

        await ezFormRef.current.addCustomEditor('_dadosBancarios_dataCadastro', customEditorDataCadastro);
        await ezFormRef.current.addCustomEditor('_valores_valorDesconto', customEditorValorDesconto);
        await ezFormRef.current.addCustomEditor('_valores_valorMulta', customEditorValorMulta);
        await ezFormRef.current.addCustomEditor('_dadosBancarios_historico', customEditorHistorico);
    }, [ezFormRef]);

    useEffect(() => {
        setDataUnit(new DataUnit());
    }, []);

    useEffect(() => {
        if (!dataUnit) {
            return;
        }

        dataUnit.metadataLoader = metadataLoader;
        dataUnit.loadMetadata();
    }, [dataUnit]);

    useEffect(() => {
        if(!ezFormRef?.current) {
            return;
        }

        addCustomEditor();
    }, [ezFormRef, dataUnit]);

    async function metadataLoader() {
        return new Promise((resolve) => {
            resolve(metadata);
        });
    }

    return (
        <div className="ez-flex ez-flex--column">
            { dataUnit && <EzForm ref={ezFormRef} dataUnit={dataUnit}></EzForm> }
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| config | -- | Configuração do formulário. | IFormConfig | undefined |
| customUiBuilders | -- | Define construtores customizados para tipos de campos específicos | Map<UserInterface, (field: IFormViewField, context?: IFieldBuilderContext) => HTMLElement> | new Map() |
| dataUnit | -- | Unidade de dados. Responsável pelo controle de edição de registros e  informações pertinentes aos campos. | DataUnit | undefined |
| elementFocusSearchField | -- | Define uma ancoragem | HTMLElement | undefined |
| fieldToFocus | field-to-focus | Determina o campo que deve ficar em evidência. | string | undefined |
| onlyStaticFields | only-static-fields | Define se os campos que serão apresentados são todos estáticos. Quando verdadeira, ocorrerá no DataBinder o bind dos campos com o DataUnit. | boolean | false |
| recordsValidator | -- | Define um validador responsável pela integridade dos registros. | IRecordValidator | undefined |
| useSearchField | use-search-field | Define se o formulario deve exibir um buscador de coluna com uso do Ctrl+F | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| ezFormRequestClearFieldToFocus | Emitido quando o campo recebe foco | CustomEvent<void> |
| ezFormSetFields | Emitido quando o campo recebe foco | CustomEvent<IFieldConfig[]> |
| ezReady | Evento disparado quando o formulário está disponível na DOM. | CustomEvent<void> |
| formItemsReady | Responsável por notificar quando ocorrer a renderização de itens do formulário. | CustomEvent<FormItems> |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

##### Returns

Type: `Promise<void>`

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

Altera/adiciona uma propriedade nos metadados do campo.

##### Returns

Type: `Promise<void>`

#### `validate() => Promise<void>`

Realiza validação no conteúdo de todos os campos.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-tabselector
  * ez-popover
  * ez-form-view
  * ez-search
