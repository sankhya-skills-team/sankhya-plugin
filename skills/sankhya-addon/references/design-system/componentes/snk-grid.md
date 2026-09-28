> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-grid/ (snapshot 2026-09-28)

# Grid

O componente **SnkGrid** é uma solução robusta voltada para a exibição e manipulação de dados tabulares, totalmente integrado ao ecossistema do ERP Sankhya Om. Ele une a flexibilidade de uma grade de dados moderna com funcionalidades essenciais do sistema, como barra de tarefas (**SnkTaskbar**), filtros, paginação e gerenciamento de configurações. Desenvolvido para ser o principal elemento de visualização em telas de consulta e cadastro, o SnkGrid disponibiliza recursos como ordenação, redimensionamento de colunas, seleção múltipla, edição em linha e exportação de dados.

## Quando usar

  * Para exibir dados de entidades do Sankhya Om em formato tabular.
  * Quando for necessário oferecer ações contextuais aos dados (incluir, alterar, excluir, etc.) por meio da (**SnkTaskbar**) .
  * Em telas que demandam funcionalidades avançadas de grade, como filtros, ordenação, paginação e salvamento de configurações de colunas.
  * Para criar interfaces de consulta e manutenção de registros (CRUD) de forma rápida e padronizada.

## Quando não usar

  * Para exibir listas simples de dados que não requerem interações complexas, como ordenação, filtros ou paginação. Nesses casos, um componente de lista simples ou uma tabela HTML padrão pode ser mais adequado e performático.
  * Em aplicações que não possuem vínculo com o ERP Sankhya Om. Para esses cenários, recomenda-se o uso do componente **EzGrid** , que não depende de regras de negócio específicas do Sankhya.
  * Quando a interface exige um layout de dados que não se encaixa em uma estrutura tabular. Considere utilizar cards ou outros componentes de layout.

## SnkGrid x EzGrid

A principal diferença é que o componente **SnkGrid** possui regras e funcionalidades vinculadas a entidades e regras de negócio específicas do **[ERP Sankhya Om](https://skw.sankhya.com.br)**. Já o componente **EzGrid** não possui esse vínculo, sendo um componente mais genérico e independente.

## Atenção ao uso com SnkDataUnit

Importante

Ao utilizar o **SnkGrid** (assim como **SnkForm** ou **SnkCrud**) como filho direto de um **SnkDataUnit** , é fundamental garantir que o **SnkDataUnit** esteja completamente inicializado e seus metadados carregados **antes** de renderizar o SnkGrid. Caso contrário, o SnkGrid pode não funcionar corretamente ou apresentar erros, pois depende do contexto e dos dados fornecidos pelo SnkDataUnit pai.

A abordagem recomendada é utilizar o evento `onDataUnitReady` do SnkDataUnit em conjunto com um estado (por exemplo, via `useState`) para controlar a renderização dos componentes filhos. Assim, o SnkGrid só será renderizado após o DataUnit estar pronto.

**Exemplo de padrão recomendado:**

```jsx
const [dataUnit, setDataUnit] = useState(null);

const handleDataUnitReady = (duInstance) => {
    setDataUnit(duInstance);
};

<SnkDataUnit
    entityName="SuaEntidade"
    onDataUnitReady={handleDataUnitReady}
>
    {dataUnit && <SnkGrid />}
</SnkDataUnit>
```

Dessa forma, o `<SnkGrid />` só será montado no DOM quando o DataUnit estiver pronto, evitando problemas de inicialização.

Para mais detalhes, consulte a seção correspondente na documentação do SnkDataUnit.

## Propriedades

### Configurações da grade

> Propriedade utilizada: **configName**

Esta propriedade define um identificador único para a grade, que é usado para salvar e carregar suas configurações, como a ordem e a visibilidade das colunas.

Para utilizá-la, basta fornecer uma _string_ com o nome desejado:

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                className="ez-size-height--full"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario">
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Lista de ações

> Propriedade utilizada: **actionsList**

Esta propriedade permite adicionar um botão de **Mais opções** à barra de tarefas (**SnkTaskbar**) com uma lista de ações customizadas.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

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

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        actionsList={actionsList}>
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Gerenciador da barra de tarefas

> Propriedade utilizada: **taskbarManager**

Esta propriedade permite gerenciar a barra de tarefas (**SnkTaskbar**). Com ele, é possível adicionar, remover ou alterar o estado dos botões, personalizando as ações disponíveis para o usuário.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

/**
 * Seleciona uma linha para simular o uso do taskbarManager.
 */
const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Exemplo do gerenciamento da barra de tarefas.
    const taskbarManager = {
        getButtons: (taskbarId, dataState, currentButtons) => {
            // Lista com os novos botões desejados
            const newButtons = [{
                name: "NEW_BUTTON_1",
                hint: "Novo Botão 1",
                iconName: "credit_card"
            }, {
                name: "NEW_BUTTON_2",
                hint: "Novo Botão 2",
                iconName: "clipboard"
            }];

            // Remover um botão que não será utilizado
            const index = currentButtons.findIndex(button => button === "CONFIGURATOR");
            if (index >= 0) {
                currentButtons.splice(index, 1);
            }

            switch (taskbarId) {
                case "snkGridHeaderTaskbar.selected":
                    // Inserir os novos botões na 3ª posição com um novo divisor ao lado
                    currentButtons.splice(3, 0, "DIVIDER", ...newButtons);
                    return currentButtons;

                default:
                    return currentButtons;
            }
        }
    };

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        taskbarManager={taskbarManager}>
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Parâmetro ENTER como TAB

> Propriedade utilizada: **useEnterLikeTab**

Quando habilitada, a tecla `ENTER` passa a ter o mesmo comportamento da tecla `TAB`, facilitando a navegação entre as células da grade.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && <SnkGrid configName="MovimentoBancario" useEnterLikeTab={true} />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Validação de campos na edição

> Propriedade utilizada: **recordsValidator**

Esta propriedade define um validador para garantir a integridade dos registros. Ao salvar uma alteração, a função `validateRecord` é executada para validar os dados.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const validator = {
    validateRecord: (record) => {
        const isValid = record.__record__id__ !== '01321321501';

        return {
            isValid,
            invalidFields: ['01321321501'],
            errorTitle: 'Campo com validação incorreta',
            errorMessage: 'Verifique os campos para prosseguir',
            infoMessage: ''
        }
    }
}

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication >
            <SnkDataUnit
                entityName="MovimentoBancario"
                enableGridInsert={true}
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance &&
                    <SnkGrid
                        recordsValidator={validator}
                        configName="MovimentoBancario"/>}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Resolvedor de status

> Propriedade utilizada: **statusResolver**

Esta propriedade permite configurar as cores de badges coluna de status com base nos valores das células.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Exemplo de uma definição para o Status na grade,
    // baseando no valor do campo "Conciliado?".
    const statusResolver = {
        "CONCILIADO": {
            "false" : "#BD0025", // red = Não
            "true" : "#157A00" // green = Sim
        }
    };

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        statusResolver={statusResolver}>
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

###

O resolvedor de status também pode ser uma função.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Exemplo de uma definição para o Status na grade,
    // baseando no valor do campo "Conciliado?".
    const statusResolver = dataRow => {
        if(dataRow.CONCILIADO){
            return "#157A00"; // green = Sim
        }

        return "#BD0025"; // red = Não
    }

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        statusResolver={statusResolver}>
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Seleção múltipla

> Propriedade utilizada: **multipleSelection**

Habilita a seleção de múltiplas linhas na grade.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
                className="ez-size-height--full">
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        multipleSelection="true">
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Seleção múltipla com paginação

> Propriedade utilizada: **multipleSelection**

Esta propriedade determina se a grade poderá ter mais de uma linha selecionada.

Importante

A barra de informações que indica a **quantidade de registros selecionados** só é exibida quando a seleção múltipla e a paginação estão ativadas.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication>
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
                className="ez-size-height--full">
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        multipleSelection="true">
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Apresentação da barra de tarefas

> Propriedade utilizada: **presentationMode**

Altera o modo de apresentação dos botões na barra de tarefas (**SnkTaskbar**).

Informação

A definição do modo de apresentação pode ser realizada por meio dos valores:

  * **primary** [em processo de descontinuação] - É o modo **padrão** para apresentar os botões na barra de tarefas (**SnkTaskbar**);
  * **secondary** \- É o modo **secundário** , que altera o formato e a ordenação dos botões na barra de tarefas (**SnkTaskbar**).
  * **singleTaskbar** [priorizar o uso] - É o modo de **cabeçalho único** , que move os botões de "adicionar" e "configuração de grade" para o cabeçalho da barra de tarefas (**SnkTaskbar**).

É necessário informar esse valor como uma _string_ , conforme será apresentado no exemplo a seguir.

Modo: **secondary**

Modo: **singleTaskbar**

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance1, setDataUnitInstance1] = useState(null);
    const [dataUnitInstance2, setDataUnitInstance2] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReadySecondary = (event) => {
        const du = event.detail;
        setDataUnitInstance1(du);
        du.loadData();
    };

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReadySingle = (event) => {
        const du = event.detail;
        setDataUnitInstance2(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReadySecondary}
                dataUnitName="duSecondary"
                key="duSecondary">
                {dataUnitInstance1 && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        presentationMode="secondary">
                    </SnkGrid>
                )}
            </SnkDataUnit>

            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReadySingle}
                dataUnitName="duSingle"
                key="duSingle">
                {dataUnitInstance2 && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        presentationMode="singleTaskbar">
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Carregamento automático de registros

> Propriedade utilizada: **autoLoad**

Controla se os dados da grade devem ser carregados automaticamente na inicialização.

Se a propriedade for definida, seu valor prevalecerá sobre a configuração global (`global.carregar.registros.iniciar.tela`).

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && <SnkGrid autoLoad={true} />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Foco automático

> Propriedade utilizada: **autoFocus**

Por padrão, a grade recebe o foco automaticamente, o que é útil para implementações com atalhos de teclado. No entanto, em alguns cenários, pode ser desejável desabilitar esse comportamento. Para isso, utilize a propriedade booleana `autoFocus`.

```jsx
import { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication >
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && <SnkGrid autoFocus={true} configName='MovimentoBancario' />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Modo compacto

> Propriedade utilizada: **compact**

A propriedade `compact` remove os preenchimentos laterais da grade, permitindo que o conteúdo ocupe toda a largura disponível. Isso é útil para maximizar o espaço e proporcionar uma visualização de dados mais densa.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && <SnkGrid configName="MovimentoBancario" compact={true}  />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Ocultar checkbox

> Propriedade utilizada: **suppressCheckboxColumn**

A propriedade `suppressCheckboxColumn` oculta a coluna de checkboxes de seleção. Utilize-a quando a seleção de múltiplas linhas não for necessária, resultando em uma interface mais limpa.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && <SnkGrid configName="MovimentoBancario" suppressCheckboxColumn={true} />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Tamanho mínimo da grade

Por padrão, a grade possui uma altura mínima de `300px`. Em alguns casos, pode ser necessário que a altura mínima seja `0px` para que o componente se ajuste ao contêiner pai.

Para isso, basta adicionar a classe css `grid_height-0`.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    // Evento disparado quando o DataUnit está pronto.
    // É necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <div style={{ height: "500px" }}>
                        <SnkGrid
                            className={"grid_height-0"}
                            configName="MovimentoBancario">
                        </SnkGrid>
                    </div>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Principais métodos

### showConfig() e hideConfig()

Estes métodos controlam a exibição do modal de configuração da grade.

Observação

No exemplo abaixo, ao clicar no botão **Configurações** , o método `showConfig()` é acionado para exibir o modal de **Configuração da grade**. Após 2 segundos, o método `hideConfig()` é chamado para ocultá-lo automaticamente.

```jsx
import { useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const snkGrid = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const actionClick = (action) => {
        if (action === "CONFIGURATOR") {
            // Método de abertura da configuração da grade.
            snkGrid.current.showConfig();

            // O timeout abaixo serve para demonstrar a chamada
            // do médodo hideConfig() apos o tempo de 2 segundos.
            setTimeout(() => {
                snkGrid.current.hideConfig()
                    .then(() => {
                        ApplicationUtils.message(
                            "Título da Mensagem",
                            "A configuração da grade foi fechada!"
                        );
                    });
            }, 2000);
        }
    };

    // Evento disparado quando o DataUnit está pronto.
    // É necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid ref={snkGrid}
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        onActionClick={evt => actionClick(evt.detail)}>
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### setConfig()

Este método é responsável por atribuir uma nova configuração à grade.

Observação

No exemplo abaixo, ao clicar no botão **Alterar Configuração** , o método `setConfig()` é acionado, e a coluna **Conciliado?** é ocultada.

```jsx
import { useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from "@sankhyalabs/ezui/react/components";

// JSON de exemplo de uma nova configuração para a grade,
const newConfig = {
    "columns": [
        {
            "name": "NUMDOC",
            "width": 200,
            "orderIndex": 0
        },
        {
            "name": "HISTORICO",
            "width": 400,
            "orderIndex": 0
        },
        {
            "name": "DTLANC",
            "width": 300,
            "orderIndex": 0
        }
    ]
};

const Demo = () => {
    const snkGrid = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const setConfig = () => {
        snkGrid.current.setConfig(newConfig);
    };

    // Evento disparado quando a instância do DataUnit estiver pronta,
    // é necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <>
                        <SnkGrid ref={snkGrid}
                            className="ez-flex-item--auto"
                            configName="MovimentoBancario">
                        </SnkGrid>

                        <EzButton
                            className="ez-margin-horizontal--auto ez-margin-bottom--large"
                            label="Alterar Configuração"
                            onClick={setConfig}>
                        </EzButton>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Row Metadata

Quando um `RowMetadataProvider` é definido no (**SnkDataUnit**) associado ao `snk-grid`, a grade utilizará esse provedor para renderizar os dados.

No exemplo abaixo, cada produto tem uma configuração diferente de casas decimais (`rm_precision`) para as colunas de Quantidade e Vlr. Unitário. O provedor define dinamicamente a precisão dessas colunas com base no produto.

Importante

O fluxo completo de `RowMetadata` está detalhado na documentação do (**SnkDataUnit**).

### Formatador personalizado

É possível adicionar formatadores de valor personalizados (`ICustomFormatter`) usando o método `addCustomValueFormatter`. Este formatador deve implementar a interface `ICustomFormatter` e, por meio do método `format`, retornar o valor formatado a ser exibido na grade.

O método `removeCustomValueFormatter` remove um formatador personalizado adicionado anteriormente.

#### addGridCustomRender()

O método `addGridCustomRender` permite substituir o conteúdo de uma célula por um elemento HTML customizado, que pode ser criado dinamicamente com base nos dados da linha.

Importante

Ao retornar o elemento como uma string ou usando o método `renderToString` do `react-dom/server`, nenhum código JavaScript será aplicado. Para elementos interativos, como botões, é necessário criar o elemento via `document.createElement`.

**Parâmetros**

O método `getRenderElement` recebe os seguintes parâmetros:

  * **value** \- Retorna o valor da célula.
  * **currentRender** \- Retorna o elemento padrão.
  * **name** \- Retorna o nome do campo.
  * **getValue** \- Método que retorna o valor da célula.
  * **detailContext** \- Retorna o contexto do master/detail.
  * **renderMetadata** \- Retorna o metadata da célula.

```jsx
import { EzButton } from "@sankhyalabs/ezui/react/components";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";
import React, { useRef, useState, useEffect } from 'react';
import { renderToString } from "react-dom/server";

// Configuração customizada para a exibição da coluna HISTORICO
const newConfig = {
    "columns": [
        {
            "name": "HISTORICO",
            "width": 400,
            "orderIndex": 0
        }
    ]
};

const Demo = () => {
    const application = useRef(null);
    const snkGrid = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const setCustomElement = () => {
        const customRender = {
            getRenderElement: () => {
                const element = document.createElement('div');
                element.textContent = 'Esse é um elemento totalmente customizado!';
                return element;
            }
        };
        snkGrid.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const setCustomElementString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const elemment = `<div class='ez-text--tertiary'>Valor do campo: ${params.value}</div>`;
                return elemment;
            }
        };
        snkGrid.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const setCustomElementReactString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const Element = <div className="ez-text--tertiary">Valor do campo: {params.value}</div>
                const stringElement = renderToString(Element);
                return stringElement;
            }
        };
        snkGrid.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const editElement = () => {
        const customRender = {
            getRenderElement: (params) => {
                const element = params.currentRender;
                element.textContent = `Valor do campo: ${params.value}`;
                element.className = "ez-text--tertiary";
                return element;
            }
        };
        snkGrid.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const cleanElement = () => {
        const customRender = {
            getRenderElement: () => {}
        };
        snkGrid.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const handleDataUnitReady =  (event) => {
        const du = event.detail;
        setDataUnitInstance(du);

        du.loadMetadata().then(() => {
            // Seta a configuração customizada para a exibição da coluna HISTORICO
            snkGrid.current.setConfig(newConfig);
        });

        du.loadData();
    };

    useEffect(() => {
        if (snkGrid.current) {
            snkGrid.current.setConfig(newConfig);
        }
    }, [snkGrid.current]);

    return (
        <SnkApplication ref={application} configName="MovimentoBancario">
            <EzButton label="Exibir elemento nativo customizado" onClick={setCustomElement} className="ez-margin-top--medium" />
            <EzButton label="Exibir elemento em string customizado" onClick={setCustomElementString} className="ez-margin-top--medium" />
            <EzButton label="Exibir elemento utilizando o reactToString" onClick={setCustomElementReactString} className="ez-margin-top--medium" />
            <EzButton label="Exibir elemento editado" onClick={editElement} className="ez-margin-top--medium" />
            <EzButton label="Resetar elemento" onClick={cleanElement} className="ez-margin-top--medium" />
            <SnkDataUnit
                className="ez-size-height--full"
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkGrid
                        ref={snkGrid}
                        className="ez-size-height--full"
                        configName="MovimentoBancario"
                    />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

#### addCustomEditor()

Este método permite adicionar editores customizados (`ICustomEditor`) para os campos da grade, substituindo os editores padrão. Se nenhum editor customizado for fornecido, o editor padrão do campo será usado.

O método `getEditorElement` do `ICustomEditor` pode retornar quatro tipos de valores:

  * **Nulo/indefinido** : renderiza o elemento padrão para aquele campo;
  * **O elemento padrão** : renderiza o elemento padrão para aquele campo;
  * **Uma string** : faz o parse da string e renderiza o elemento passado;
  * **Um elemento HTML** : renderiza o elemento.

Nos parâmetros da função `getEditorElement`, o atributo `source` permite diferenciar se o editor está sendo usado na grade ou em um formulário.

Importante

O método `renderToString` não executa código JavaScript. Para um botão, por exemplo, um onClick não irá funcionar. O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTML.

```jsx
import { DataUnit } from '@sankhyalabs/core';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { SnkApplication, SnkGrid } from '@sankhyalabs/sankhyablocks/react/components';
import { useCallback, useEffect, useRef, useState } from 'react';
import { renderToString } from 'react-dom/server';

const dataLoader = () => {
    return new Promise((resolve) => {
        resolve({records: [
            {
                "__record__id__": "1",
                "NOME": "Brasil",
                "POPULACAO": 214300000,
                "IDIOMA": "Português",
                "CONTINENTE": "América do Sul",
                "PIB": 1920000000
              },
              {
                "__record__id__": "2",
                "NOME": "Estados Unidos",
                "POPULACAO": 332915073,
                "IDIOMA": "Inglês",
                "CONTINENTE": "América do Norte",
                "PIB": 25440000000
              }
        ]});
    });
}

const metadataLoader = () => {
    return new Promise((resolve) => {
        resolve({
            "name": "paises",
            "label": "paises",
            "fields": [
                {
                    "name": "NOME",
                    "label": "Nome do País",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": true
                },
                {
                    "name": "POPULACAO",
                    "label": "Num. Habitantes",
                    "dataType": "NUMBER",
                    "userInterface": "INTEGERNUMBER",
                    "readOnly": false,
                    "required": false
                },
                {
                    "name": "IDIOMAOFC",
                    "label": "Idioma oficial",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": false
                },
                {
                    "name": "CONTINENTE",
                    "label": "Continente",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": false
                },
                {
                    "name": "PIB",
                    "label": "PIB",
                    "dataType": "NUMBER",
                    "userInterface": "INTEGERNUMBER",
                    "readOnly": false,
                    "required": false
                }
            ]
        });
    });
}

const Demo = () => {
    const snkGridRef = useRef(null);
    const [dataUnit, setDataUnit] = useState();

    const initDataUnit = () => {
        dataUnit.dataLoader = dataLoader;
        dataUnit.metadataLoader = metadataLoader;
    }

    const loadDataUnit = () => {
        dataUnit.loadMetadata().then((metadata) => {
            const fields = metadata.fields.map(field => ({...field, readOnly: false}));
            dataUnit.metadata = {...metadata, fields};
            dataUnit.loadData();
            dataUnit.selectFirst();
        });
    }

    const addCustomEditor = useCallback(async () => {
        const customEditorPopulacao = {
            getEditorElement: () => {
                return null;
            }
        }

        const customEditorIdioma = {
            getEditorElement: (params) => {
                if(params.source !== "FORM") {
                    return;
                }

                return params.currentEditor;
            }
        }

        const customEditorContinente = {
            getEditorElement: (params) => {
                if(params.source !== "FORM") {
                    return;
                }

                return renderToString(<EzButton label='Teste'/>);
            }
        }

        const customEditorPib = {
            getEditorElement: ({source, setValue, value}) => {
                if(source === "FORM") {
                    const textInput = document.createElement('ez-number-input');
                    textInput.label = 'Editor customizado';
                    textInput.value = value;
                    textInput.onkeyup = (event) => {
                        setValue(event.target.value);
                    };
                    return textInput;
                }
                const textInput = document.createElement('input');
                textInput.value = value;
                textInput.type = 'number';
                textInput.onkeyup = (event) => {
                    setValue(event.target.value);
                };
                return textInput;
            }
        }

        await snkGridRef.current.addCustomEditor('POPULACAO', customEditorPopulacao);
        await snkGridRef.current.addCustomEditor('IDIOMAOFC', customEditorIdioma);
        await snkGridRef.current.addCustomEditor('CONTINENTE', customEditorContinente);
        await snkGridRef.current.addCustomEditor('PIB', customEditorPib);
    }, [snkGridRef]);

    useEffect(() => {
        setDataUnit(new DataUnit("dataUnitTeste"));
    }, []);

    useEffect(() => {
        if(!dataUnit) {
            return;
        }

        initDataUnit();
        loadDataUnit();

    }, [dataUnit]);

    useEffect(() => {
        if(!snkGridRef?.current) {
            return;
        }

        addCustomEditor();
    }, [snkGridRef, dataUnit]);

    return (
        <SnkApplication configName="Countries">
            <SnkGrid className='ez-margin--large' ref={snkGridRef} dataUnit={dataUnit} />
        </SnkApplication>
    )
};

export default Demo;
```

Importante

Ao usar um `input` em um elemento customizado, utilize o listener `onkeyup` para capturar o novo valor a cada tecla pressionada. Isso garante que o ciclo de vida da grade não interfira na atualização do valor.

## Exemplos de eventos

### actionClick()

Este evento é disparado sempre que um botão ou uma ação na barra de tarefas (**SnkTaskbar**) é clicado.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";
/**
 * Clque sobre o botão de configurador do taskbar para ver o evento disparado.
 */
const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const actionClick = (action) => {
        ApplicationUtils.message("Título da Mensagem", `Ação clicada: <strong>${action}</strong>`);
    };

    // Evento disparado quando o DataUnit está pronto.
    // É necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        onActionClick={evt => actionClick(evt.detail)}>
                    </SnkGrid>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### gridDoubleClick()

Este evento é disparado quando o usuário realiza um duplo clique em uma linha da grade.

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkGrid } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

/**
 * Dê um duplo clique sobre uma linha da grid para ver o evento disparado.
 */
const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const gridDoubleClick = () => {
        ApplicationUtils.message("Título da Mensagem", "Duplo clique acionado!");
    };

    // Evento disparado quando o DataUnit está pronto.
    // É necessário para carregar os dados da grid.
    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkGrid
                        className="ez-flex-item--auto"
                        configName="MovimentoBancario"
                        onGridDoubleClick={gridDoubleClick}>
                    </SnkGrid>
                )}
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
| actionsList | -- | Lista de ações que devem ser usadas no botão "Mais opções" do snk-taskbar . | Action[] | undefined |
| autoFocus | auto-focus | Define se a grade receberá o foco automaticamente ao ser carregada. | boolean | true |
| autoLoad | auto-load | Define se os dados serão carregados automaticamente na inicialização do componente. | boolean | undefined |
| canEdit | can-edit | Define se a edição de dados na grade está habilitada. | boolean | true |
| columnFilterDataSource | -- | Define o data source para o filtro de colunas. | IMultiSelectionListDataSource | new SnkMultiSelectionListDataSource() |
| compact | compact | Define se a grade deve ser exibida em modo compacto. | boolean | undefined |
| configName | config-name | Nome usado para salvar e recuperar a configuração da grade. | string | undefined |
| disablePersonalizedFilter | disable-personalized-filter | Desabilita a apresentação da opção de filtros personalizados na barra de filtros (chip de filtros) e no modal lateral de filtros (contêiner de filtros personalizados). | boolean | undefined |
| enableGridInsert | enable-grid-insert | Habilita a inserção de registros diretamente na grade. | boolean | false |
| enableLockManagerLoadingComp | enable-lock-manager-loading-comp | Define se o componente deve usar o LockManager para controle de carregamento da aplicação. | boolean | false |
| enableLockManagerTaskbarClick | enable-lock-manager-taskbar-click | Ativa o gerenciamento de locks na grade pela Taskbar. | boolean | false |
| filterBarLegacyConfigName | filter-bar-legacy-config-name | Chave da configuração legada da barra de filtros. | string | undefined |
| filterBarTitle | filter-bar-title | Título que será apresentado na barra de filtros. | string | undefined |
| filterCustomConfig | -- |  | SnkFilterItemConfig[] | undefined |
| filterCustomConfigInterceptor | -- |  | (config: SnkFilterItemConfig[]) => SnkFilterItemConfig[] | undefined |
| gridHeaderCustomSlotId | grid-header-custom-slot-id | Define o nome do slot para elementos customizados na Taskbar do cabeçalho da grade. | string | 'GRID_HEADER_CUSTOM_ELEMENTS' |
| gridLegacyConfigName | grid-legacy-config-name | Chave da configuração legada da grade. | string | undefined |
| isDetail | is-detail | Determina se a grade está vinculada a um detalhe de outra tela. | boolean | undefined |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| multipleEditionEnabled | multiple-edition-enabled | Habilita a edição de múltiplos registros simultaneamente. | boolean | true |
| multipleSelection | multiple-selection | Determina se a seleção de múltiplas linhas é permitida. | boolean | undefined |
| outlineMode | outline-mode | Altera a aparência das bordas e sombras do componente. Se false , aplica o padrão de sombras (ideal para o elemento principal do layout). Se true , aplica um contorno (ideal para quando o componente está dentro de outro, como um painel ou pop-up). | boolean | false |
| paginationCounterMode | pagination-counter-mode | Define o modo de exibição do contador de paginação. | "auto" \| "hidden" \| "show" | 'auto' |
| presentationMode | presentation-mode | Altera o modo de apresentação dos botões do snk-taskbar . | PresentationMode.PRIMARY \| PresentationMode.SECONDARY \| PresentationMode.SINGLE_TASKBAR | PresentationMode.PRIMARY |
| recordsValidator | -- | Validador responsável por verificar a integridade dos dados de um registro. | IRecordValidator | undefined |
| resourceID | resource-i-d | Identificador de recursos, como configurações e permissões de acesso. | string | undefined |
| selectionToastConfig | -- | Configuração do toast de seleção da grade. | ISelectionToastConfig | undefined |
| statusResolver | -- | Define a configuração de cores para a coluna de status. | ((data: object) => string) \| IStatusResolver | undefined |
| strategyExporter | strategy-exporter | Define o modo de exportação dos dados. | "ClientSideExporterStrategy" \| "ServerSideExporterStrategy" | ExporterStrategy.SERVER_SIDE |
| suppressCheckboxColumn | suppress-checkbox-column | Informa se a coluna de checkbox deve ser suprimida. | boolean | undefined |
| suppressFilterColumn | suppress-filter-column | Informa se a grade deve suprimir o filtro de coluna. | boolean | false |
| suppressHorizontalScroll | suppress-horizontal-scroll | Define se a grade deve suprimir a barra de rolagem horizontal. | boolean | false |
| taskbarCustomContainerId | taskbar-custom-container-id | Define o identificador do contêiner de elementos customizados da Taskbar . | string | undefined |
| taskbarManager | -- | Gerenciador das barras de tarefas. Permite determinar botões específicos ou gerenciar o estado dos botões. | TaskbarManager | undefined |
| topTaskbarCustomSlotId | top-taskbar-custom-slot-id | Define o nome do slot para elementos customizados na Taskbar principal do componente. | string | 'GRID_TASKBAR_CUSTOM_ELEMENTS' |
| useEnterLikeTab | use-enter-like-tab | Quando true , a tecla ENTER navega entre as células como a tecla TAB. | boolean | false |
| useSearchColumn | use-search-column | Define se a grade deve exibir um buscador de colunas ao pressionar Ctrl+F . | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| actionClick | Emitido ao clicar em um botão de ação ou item de menu. | CustomEvent<string> |
| componentReady | Emitido quando o componente estiver completamente carregado. | CustomEvent<void> |
| gridDoubleClick | Emitido ao realizar um duplo clique em uma linha da grade. | CustomEvent<any> |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para um campo da grade ou formulário.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando o editor é registrado.

#### `addCustomValueFormatter(columnName: string, customFormatter: ICustomFormatter) => Promise<void>`

Registra um formatador de valor customizado para uma coluna da grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando o formatador é registrado.

#### `addGridCustomRender(fieldName: string, customRender: ICustomRender, detailContext?: string) => Promise<void>`

Registra um renderizador customizado para uma coluna da grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando o renderizador é registrado.

#### `getFilterBar() => Promise<HTMLSnkFilterBarElement>`

Retorna o elemento da barra de filtros da grade.

##### Returns

Type: `Promise<HTMLSnkFilterBarElement>`

O elemento da barra de filtros.

#### `hideConfig() => Promise<void>`

Fecha a janela de configurações da grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando a janela de configuração é fechada.

#### `refreshColumnFilterDataSource() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `reloadConfig() => Promise<void>`

Recarrega a configuração da grade.

##### Returns

Type: `Promise<void>`

#### `reloadFilterBar() => Promise<void>`

Recarrega a barra de filtros da grade, buscando o estado do servidor.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando a barra de filtros é recarregada.

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

Remove um formatador de valor customizado de uma coluna da grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando o formatador é removido.

#### `setConfig(config: IGridConfig) => Promise<void>`

Define a configuração da grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando a configuração é aplicada.

#### `setFocus() => Promise<void>`

Atribui o foco para a grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando o foco é atribuído.

#### `showConfig() => Promise<void>`

Exibe a janela de configurações da grade.

##### Returns

Type: `Promise<void>`

Uma promessa que é resolvida quando a janela de configuração é exibida.

### Dependencies

#### Used by

  * snk-crud
  * snk-detail-view

#### Depends on

  * snk-filter-bar
  * snk-taskbar
  * snk-grid-config
  * snk-data-exporter
  * snk-actions-button
  * taskbar-split-button
  * taskbar-actions-button
