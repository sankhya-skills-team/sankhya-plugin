> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-print-selector/ (snapshot 2026-09-28)

# Print Selector

O componente **SnkPrintSelector** é responsável por disponibilizar a seleção de impressora para impressões pendentes no sistema. Em um ambiente em que várias impressoras podem estar disponíveis, o componente oferece uma interface intuitiva para que o usuário escolha a impressora específica na qual deseja que um trabalho de impressão seja realizado.

O componente permite a seleção de uma impressora padrão através da opção _"Usar sempre esta seleção"_. Quando essa opção está marcada, a impressora é memorizada e configurada como padrão.

Observação

Vale ressaltar que a funcionalidade de impressão está restrita exclusivamente a usuários com as devidas permissões.

## Exemplo

Para utilizar o componente pode-se implementar da seguinte forma:

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { StringUtils } from "@sankhyalabs/core";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const CUSTOM_BTN_PRINT = {
    name: "Imprimir",
    hint: "Imprimir",
    iconName: "print"
}

const printJobData = {
    "transactionId": "3A3A7075451056526DFD91E5228C93A4",
    "printServers": [
        {
            "printServerUri": "localhost:9091",
            "printerList": [
                {
                    "port": "9091",
                    "host": "localhost",
                    "printerName": "CutePDF Writer",
                    "printerUri": "localhost:9091/CutePDF Writer",
                    "printServerUri": "localhost:9091",
                    "requiresAuthorization": "false"
                }
            ]
        }
    ],
    "pendingPrinters": [
        {
            "docType": "RELATORIO",
            "originalPrinterName": "?",
            "printJobCount": "1",
            "docTypeDescription": "Relatorio"
        }
    ],
    "printServerActive": true
}

const buildTaskbarManager = () => {
    return {
        getButtons: (taskbarId, dataState, currentButtons) => {
            currentButtons.push(CUSTOM_BTN_PRINT);
            return currentButtons;
        },
        isEnabled: () => true
    }
}

const actionClick = async (buttonID) => {
    if (buttonID.detail === CUSTOM_BTN_PRINT.name) {
        openSnkPrintSelector(printJobData);
        return;
    }
};

const openSnkPrintSelector = async (printJobData) => {
    let printSelector = document.querySelector('snk-print-selector');

    if(!printSelector) {
        printSelector = document.createElement('snk-print-selector');
        printSelector.setAttribute('id', StringUtils.generateUUID());
        window.document.body.appendChild(printSelector);
    }

    const {selectedPrinter, saveSubstitute} = await printSelector.openPrintSelector(printJobData);

    ApplicationUtils.success(
        "Impressão em andamento",
        `Nome da Impressora: <b>${selectedPrinter.printerName}</b> <br> Impressora memorizada como padrão: ${saveSubstitute ? '<b>Sim</b>' : '<b>Não</b>'}`
    );
}

const Demo = () => {
    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">
                <SnkCrud taskbarManager={buildTaskbarManager()} onActionClick={actionClick} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Propriedades

### Abrir PopUp de impressão

> Método: **openPrintSelector**

Esse método foi projetado para ser chamado externamente e tem como objetivo abrir um seletor de impressoras. O método aceita um parâmetro chamado `printJobData`, que contém dados sobre o trabalho de impressão, como as impressoras disponíveis, o servidor de impressão ativo, etc.

O método retorna o tipo **PrintSelectorResponse** :

  * **selectedPrinter:** Informação sobre a impressora selecionada.
  * **saveSubstitute:** Indica se a opção de salvar a impressora selecionada como padrão está habilitada.

### Informações sobre impressões pendentes

> Tipo utilizado: **PendingPrintJobData**

O tipo `PendingPrintJobData` contém informações relacionadas ao trabalho de impressão pendente. Essas informações incluem detalhes sobre o documento a ser impresso, o número de trabalhos de impressão, a ativação do servidor de impressão, a lista de servidores de impressão disponíveis, e assim por diante. Abaixo é possível observar o que cada atributo representa:

  * **transactionId:** identificador da chamada HTTP para o SankhyaOM.
  * **printServers:** Uma lista de servidores de impressão.
  * **pendingPrinters:** Lista de trabalhos de impressão pendentes aguardando processamento.
  * **printServerActive:** Define se utiliza servidor de impressão.

## API do componente

### Methods

#### `openPrintSelector(printJobData: PendingPrintJobData) => Promise<PrintSelectorResponse>`

##### Returns

Type: `Promise<PrintSelectorResponse>`
