> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-taskbar/ (snapshot 2026-09-28)

# Taskbar

O componente **SnkTaskbar** é uma barra de ferramentas que agrupa as principais ações relacionadas a uma entidade ou a um contexto específico da aplicação Sankhya. Ele oferece uma interface consistente para operações como salvar, excluir, navegar entre registros e executar ações personalizadas.

## Quando utilizar

O `snk-taskbar` é um componente fundamental para a construção de telas no ecossistema Sankhya. Ele funciona como uma barra de botões padrão, projetada para agilizar e padronizar o desenvolvimento de interfaces. Utilize o `snk-taskbar` sempre que precisar de uma barra de ações para manipulação de dados, como incluir, alterar, excluir, e outras operações comuns. Ele é a base para componentes mais complexos como `snk-crud`, `snk-grid` e `snk-simple-crud`, que o utilizam para fornecer uma experiência de usuário consistente e familiar.

## Quando não utilizar

Não utilize o `snk-taskbar` para telas ou aplicações que não fazem parte do ecossistema Sankhya, pois ele foi projetado para integrar-se com os padrões e serviços da plataforma. Evite também o seu uso para ações que não se encaixam no padrão de uma barra de ferramentas de CRUD, como navegação principal da aplicação ou ações muito específicas de um determinado contexto que não se beneficiam da padronização oferecida pelo componente.

## Propriedades

Importante

O componente **SnkTaskbar** apenas será exibido ao informar a propriedade **buttons**.

### Lista de botões

> Propriedade utilizada: **buttons**

É a lista padrão utilizada para exibir os botões na barra de tarefas (**SnkTaskbar**), esta lista é uma _string_ separada por vírgula, contendo todos os botões que serão exibidos, conforme o exemplo a seguir:

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}>
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Personalização de botões

> Propriedade utilizada: **customButtons**

Esta propriedade corresponde a um _Map_ com a definição de botões personalizados. A chave deste mapa deve ser passada na lista da propriedade **buttons** , na posição em que o botão irá aparecer, conforme o exemplo a seguir:

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo dos novos botões personalizados
    const customButtons = new Map();

    // Exemplo de carregamento dos novos botões personalizados.
    const loadCustomButtons = () => {
        const newButtons = [{
            "name": "NEW_BUTTON_1",
            "hint": "Novo Botão 1",
            "text": "Novo botão de exemplo 1",
            'iconName': "balance"
        }, {
            "name": "NEW_BUTTON_2",
            "hint": "Novo Botão 2",
            'iconName': "clipboard"
        }];

        newButtons.forEach(newButton => {
            customButtons.set(newButton.name, newButton);
        });
    };

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "NEW_BUTTON_1",
        "NEW_BUTTON_2",
        "DIVIDER",
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    useEffect(() => {
        loadCustomButtons();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    customButtons={customButtons}>
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Elementos personalizados e slots

> Propriedades utilizadas: **customContainerId** , **customSlotId**

É possível adicionar elementos HTML customizados na barra de tarefas (**SnkTaskbar**) de duas maneiras: através de um contêiner externo ou utilizando o slot padrão.

  1. **Contêiner Externo** : Utilize as propriedades `customContainerId` e `customSlotId` para especificar o `id` de um contêiner e de um slot que estão fora do `SnkApplication`. Os elementos dentro deste slot serão movidos para a taskbar.
  2. **Slot Padrão** : Adicione um `div` com `slot="TASKBAR_CUSTOM_ELEMENTS"` diretamente dentro do `SnkTaskbar`.

Em ambos os casos, os `id`s dos elementos customizados devem ser incluídos na propriedade `buttons` para que sejam renderizados na posição correta.

informação

Para mais informações de como utilizar elementos customizados na taskbar leia o artigo [Como utilizar elementos personalizados na Taskbar](/blog/elementos-personalizados-na-taskbar).

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Adicione os IDs dos elementos customizados na propriedade `buttons`.
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CUSTOM_BUTTON_1", // Elemento customizado via customContainerId/customSlotId
        "CUSTOM_INPUT_1",  // Elemento customizado via customContainerId/customSlotId
        "DIVIDER",
        "CUSTOM_BUTTON_2", // Elemento customizado via slot padrão
        "INSERT"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <>
            {/*
              Este container está fora do SnkApplication, mas a taskbar o encontrará
              usando as propriedades customContainerId e customSlotId.
              Os elementos serão movidos para a taskbar, por isso o container pode ser ocultado.
            */}
            <div id="meu-container-customizado" style={{ display: 'none' }}>
                <div id="meu-slot-customizado">
                    <ez-button id="CUSTOM_BUTTON_1" label="Botão Externo" size="small" />
                    <ez-text-input id="CUSTOM_INPUT_1" label="Input Externo" class="ez-padding-left--medium" />
                </div>
            </div>

            <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
                <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                    <SnkTaskbar
                        buttons={buttons.join(",")}
                        customContainerId="meu-container-customizado"
                        customSlotId="meu-slot-customizado"
                    >
                        {/*
                          Este slot é o padrão (TASKBAR_CUSTOM_ELEMENTS) e será usado para
                          renderizar o CUSTOM_BUTTON_2.
                        */}
                        <div slot="TASKBAR_CUSTOM_ELEMENTS" id="TASKBAR_CUSTOM_ELEMENTS">
                            <ez-button id="CUSTOM_BUTTON_2" label="Botão Interno" size="small" />
                        </div>
                    </SnkTaskbar>
                </SnkDataUnit>
            </SnkApplication>
        </>
    );
};

export default Demo;
```

### Lista de ações

> Propriedade utilizada: **actionsList**

Com esta propriedade é possível incluir na barra de tarefas (**SnkTaskbar**) um botão de **Mais opções** com uma lista de ações.

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de uma lista de ações.
    const actionsList = [{
        label: "Opção 1",
        value: "OPPEN_APP: br.com.sankhya.mge.nome_da_tela_1",
        iconName: "settings-inverted"
    }, {
        label: "Opção 2",
        value: "OPPEN_APP: br.com.sankhya.mge.nome_da_tela_2",
        iconName: "business-center"
    }];

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "ATTACH",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS",
        "ACTION_BUTTONS",
        "DIVIDER",
        "GRID",
        "CONFIGURATOR"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    actionsList={actionsList}>
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

#### Item Builder

Ao montar a lista de ações, é possível informar nos itens a propriedade **itemBuilder** , que é uma função responsável por definir a forma como o elemento será renderizado na listagem.

Essa função recebe dois argumentos, sendo o primeiro o **actionsList** (referência para o prório elemento da lista de ações) e o segundo é o **action** (o próprio item a ser renderizado). Além disso, ela deve retornar um **elemento HTML** ou uma **string**.

```jsx
import { useState } from "react";
import { renderToString } from "react-dom/server";

import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const ContasReceber = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Exemplo de uma lista de ações.
    const actionsList = [{
        label: "string",
        value: "itemBuilder.string",
        itemBuilder: (_actionButton, item) => item.label
    },
    {
        label: "Elemento HTML",
        value: "itemBuilder.html",
        disableCloseOnSelect: true,
        eagerInitialize: true,
        itemBuilder: (_actionButton, item) => (
            renderToString(
                <ez-text-input label={item.label}/>
            )
        )
    },{
        label: "Opção Padrão",
        value: "opcaoPadrao",
        iconName: "business-center"
    }];

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "ATTACH",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS",
        "ACTIONS_BUTTON",
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR"
    ];

    const handleDataUnitReady = (evt) => {
        const dataUnit = evt.detail;
        dataUnit.loadData();
        setDataUnitInstance(dataUnit);
    };

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkTaskbar
                        dataUnit={dataUnitInstance}
                        buttons={buttons.join(",")}
                        actionsList={actionsList}>
                    </SnkTaskbar>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default ContasReceber;
```

Informação

  * **eagerInitialize:** Por padrão, a função **itemBuilder** é executada quando o usuário clica para exibir a lista de opções, porém em alguns casos, é necessário que essa função seja executada assim que a lista de **mais opções** é carregada na tela, para uma configuração correta do componente. Caso o desenvolvedor se depare com esse cenário, basta informar a propriedade **eagerInitialize** na definição da action.

  * **disableCloseOnSelect:** Por padrão, a lista de opções do botão **mais opções** é fechada assim que o usuário clica na opção desejada. Caso o desenvolvedor deseje prevenir esse comportameto, basta informar a propriedade **disableCloseOnSelect** na definição da action.

### Definir botão principal

> Propriedade utilizada: **primaryButton**

Esta propriedade é responsável por determinar qual botão deverá receber a aparência de botão primário.

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    primaryButton="CONFIGURATOR">
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Lista de botões desabilitados

> Propriedade utilizada: **disabledButtons**

Com esta propriedade é possível passar uma lista de _Array_ contendo todos os botões a serem desabilitados, conforme o exemplo a seguir:

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões desabilitados na barra de tarefas (SnkTaskbar).
    const disabledButtons = [
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    disabledButtons={disabledButtons}>
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Unidade de dados

> Propriedade utilizada: **dataUnit**

Com esta propriedade é possível passar a instância do **DataUnit** que a barra de tarefas (**SnkTaskbar**) controlará os registros.

```jsx
import { useEffect, useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);
    const [dataUnitMain, setDataUnitMain] = useState();
    const [item, setItem] = useState();

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const setItemValue = (data) => {
        const dataValue = data?.selectedRecords[0]?.NUBCO;
        const itemValue = dataValue != undefined ? dataValue : "Navegue entre os registros usando os botões de navegação...";
        setItem(itemValue);
    };

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
        setDataUnitMain(dataUnit);
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario" onDataStateChange={evt => setItemValue(evt.detail)}>
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    dataUnit={dataUnitMain}>
                </SnkTaskbar>

                <label className="ez-label ez-margin-top--large">
                    Item selecionado no DataUnit: <strong>{item}</strong>
                </label>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Apresentação da barra de tarefas

> Propriedade utilizada: **presentationMode**

O **presentationMode** altera o modo de apresentação dos botões da barra de tarefas (**SnkTaskbar**).

Informação

A definição do modo de apresentação pode ser realizada por meio dos valores:

  * **primary** \- É o modo **padrão** utilizado para apresentar os botões na barra de tarefas (**SnkTaskbar**);
  * **secondary** \- É o modo **secundário** que altera o formato e ordenação dos botões na barra de tarefas (**SnkTaskbar**).

É necessário informar esse valor como uma _string_ , conforme será apresentado no exemplo a seguir.

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "INSERT",
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    primaryButton="INSERT"
                    presentationMode="secondary">
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Alinhar botões à direita

> Propriedade utilizada: **alignRigth**

A propriedade `alignRigth` permite alinhar os botões da barra de tarefas (**SnkTaskbar**) à direita. Por padrão, os botões são alinhados à esquerda.

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);

    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "ATTACH",
        "CLONE",
        "REMOVE",
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    alignRigth={true}>
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Lidando com itens transbordados

> Propriedade utilizada: **overflowStrategy**

Teoricamente, a taskbar permite que haja uma quantidade infinita de itens para serem exibidos. Em alguns casos, não é possível exibir todos os itens, devido à resolução da tela ou em cenários onde há um painel de tamanho redimensionável pelo usuário **(Split Panel)**.

Nesses casos, para garantir que não haja quebra de layout, a propriedade **overflowStrategy** define como será o comportamento da taskbar.

Por padrão, os itens que não forem possíveis de serem exibidos deverão ficar ocultos e suas funcionalidades deverão aparecer na lista de **Mais opções** , conforme o exemplo abaixo:

_Quando há espaço para todos os itens._

_Exibindo apenas os itens para os quais há espaço._

_Exibindo ações de itens ocultos no botão de Mais opções._

Observação:

Alguns itens sempre permanecem visíveis na taskbar

  * **Opções padrão** : - _Mais opções_ , _Botão de Ações_ e _Data Exporter (SnkDataExporter)_
  * **slots** : - Itens personalizados vindos de _slot_.

#### Desabilitando overflow:

Em alguns casos, o desenvolvedor pode desejar impedir o comportamento de overflow e garantir que os itens não sejam ocultados.

Para garantir esse comportamento, basta informar a propriedade `overflowStrategy = none`.

## Exemplos de eventos

### actionClick()

Este evento é acionado sempre que houver clique em um botão ou ação da barra de tarefas (**SnkTaskbar**).

```jsx
import { useEffect, useRef } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "CLONE",
        "REMOVE",
        "MORE_OPTIONS", // Depende da propriedade "actionsList".
        "DIVIDER",
        "GRID_MODE",
        "CONFIGURATOR",
        "INSERT"
    ];

    const actionClick = (action) => {
        ApplicationUtils.message("Título da Mensagem", `Ação clicada: <strong>${action}</strong>`);
    };

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar
                    buttons={buttons.join(",")}
                    onActionClick={evt => actionClick(evt.detail)}>
                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### taskbarSaveLocker() e taskbarSaveUnlocker()

Esses eventos são utilizados para controlar o estado de salvamento de dados iniciado pela barra de tarefas.

  * **taskbarSaveLocker** : Emitido quando uma ação de salvar é iniciada. É útil para bloquear outras interações na tela que possam concorrer com a operação de salvamento, como desabilitar botões.
  * **taskbarSaveUnlocker** : Emitido quando a ação de salvar é concluída (com sucesso ou erro), sinalizando que a tela pode ser desbloqueada.

No exemplo abaixo, um botão "Ação Customizada" é desabilitado enquanto a operação de salvar está em andamento. O `SnkTaskbar` é renderizado somente após o `SnkDataUnit` estar pronto, através do evento `onDataUnitReady`. Ao clicar em "Salvar", o evento `taskbarSaveLocker` é disparado, o que atualiza o estado para desabilitar o botão customizado. Após a conclusão da simulação de salvamento, o evento `taskbarSaveUnlocker` é acionado, reabilitando o botão.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkTaskbar } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

// Clique sobre o botão salvar para ver o comportamento de bloqueio e desbloqueio da barra de tarefas.
// Veja também que o botão de salvar não irá executar a ação enquanto os dados estiverem sendo salvos.
const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [isSaving, setIsSaving] = useState(false);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "DIVIDER",
        "SAVE",
    ];

    const handleDataUnitReady = (evt) => {
        const dataUnit = evt.detail;
        // Mock da função saveData para simular uma requisição com delay.
        dataUnit.saveData = () => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    ApplicationUtils.message("Sucesso", "Dados salvos com sucesso!");
                    resolve(true);
                }, 5000); // Delay de 5 segundos
            });
        };
        dataUnit.loadData();
        setDataUnitInstance(dataUnit);
    };

    const handleSaveLocker = () => {
        setIsSaving(true);
        ApplicationUtils.info("Salvando dados...");
    };

    const handleSaveUnlocker = () => {
        setIsSaving(false);
    };

    const handleCustomAction = () => {
        ApplicationUtils.info("Ação Customizada foi executada.");
    };

    return (
        <SnkApplication configName="MovimentoBancario" className="ez-padding--large">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkTaskbar
                        dataUnit={dataUnitInstance}
                        buttons={buttons.join(",")}
                        onTaskbarSaveLocker={handleSaveLocker}
                        onTaskbarSaveUnlocker={handleSaveUnlocker}
                    />
                )}
                <div class="ez-margin-top--large">
                    <ez-button
                        label="Ação Customizada"
                        onClick={handleCustomAction}
                        enabled={!isSaving}
                    />
                    {isSaving && <p class="ez-margin-top--medium"><b>Status:</b> Salvando... Botão customizado desabilitado.</p>}
                    {!isSaving && <p class="ez-margin-top--medium"><b>Status:</b> Ocioso. Botão customizado habilitado.</p>}
                </div>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| actionsList | -- |  | Action[] | undefined |
| actionsSettingsList | -- |  | Action[] | undefined |
| alignRigth | align-rigth |  | boolean | false |
| buttons | buttons |  | string | undefined |
| configName | config-name |  | string | undefined |
| customButtons | -- |  | Map<string, CustomButton> | undefined |
| customContainerId | custom-container-id |  | string | undefined |
| customSlotId | custom-slot-id |  | string | "TASKBAR_CUSTOM_ELEMENTS" |
| dataUnit | -- |  | DataUnit | undefined |
| disabledButtons | -- |  | string[] | undefined |
| messagesBuilder | -- |  | SnkMessageBuilder | undefined |
| overflowStrategy | overflow-strategy |  | "hiddenItems" \| "none" | 'hiddenItems' |
| presentationMode | presentation-mode |  | PresentationMode.PRIMARY \| PresentationMode.SECONDARY \| PresentationMode.SINGLE_TASKBAR | PresentationMode.PRIMARY |
| primaryButton | primary-button |  | string | undefined |
| resourceID | resource-i-d |  | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| actionClick |  | CustomEvent<string> |
| taskbarSaveLocker |  | CustomEvent<void> |
| taskbarSaveUnlocker |  | CustomEvent<void> |

### Dependencies

#### Used by

  * snk-detail-view
  * snk-grid
  * snk-guides-viewer
  * snk-simple-crud

#### Depends on

  * snk-data-exporter
  * snk-actions-button
  * taskbar-split-button
  * taskbar-actions-button
