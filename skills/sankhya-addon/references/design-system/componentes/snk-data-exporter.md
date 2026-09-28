> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-data-exporter/ (snapshot 2026-09-28)

# Data Exporter

O componente **SnkDataExporter** é encarregado de exportar dados para um formato de arquivo específico, permitindo que o usuário faça o download do arquivo ou o envie por e-mail.

Importante

É necessário utilizar este componente dentro de um **SnkApplication** devido às suas dependências na aplicação, como exemplificado abaixo:

```jsx
import React from 'react';
import { SnkApplication, SnkDataExporter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication className="ez-padding--large">
        <SnkDataExporter></SnkDataExporter>
    </SnkApplication>
);

export default Demo;
```

## Exemplo

Utilizando esse componente, é possível exportar uma quantidade definida de dados. Como exemplo, pode-se mencionar o seu uso em conjunto com o componente **SnkGrid** , possibilitando a exportação de um ou mais itens selecionados na grade, de toda a página ou de todos os registros exibidos na grade.

## Propriedades

### Fornecedor de informações para exportação

> Propriedade utilizada: **provider**

Esse componente é encarregado de coletar informações para exportação de dados. Para usá-lo, é necessário empregar um conjunto de métodos específicos que coletam cada tipo de informação necessário para a exportação. A seguir, será apresentada a descrição de cada método utilizado:

  * **getFilters()** : Refere-se à lista que contém os filtros de dados utilizados para a exportação;

  * **getColumnsMetadata()** : Refere-se à lista que contém os dados das colunas usados para a exportação;

  * **getOrders()** : Refere-se à lista que determina a ordem das colunas utilizada para a exportação;

  * **getResourceURI()** : Refere-se ao nome da unidade de dados (**DataUnit**) utilizado para solicitar a exportação;

  * **getOffset()** : Refere-se ao índice inicial dos itens que serão exportados;

  * **getLimit()** : Refere-se ao valor máximo que a quantidade de itens exportados pode atingir;

  * **getSelectedIDs()** : Refere-se à lista de IDs dos registros selecionados;

  * **getRecordID()** : Refere-se ao ID em Base64 utilizado para buscar a lista de relatórios personalizados.

#### Exemplo

Com o intuito de ilustrar a utilização de cada método, será exposto a seguir um exemplo:

```jsx
import React from 'react';
import { SnkApplication, SnkDataExporter } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    return (
        <SnkApplication className="ez-padding--large">
            <SnkDataExporter provider={provider}></SnkDataExporter>
        </SnkApplication>
    )
};

export default Demo;

/**
 * Exemplo de JSON com os métodos de captura dos parâmetros do provider.
 */
const provider = {
    getFilters: () => {
        return filters;
    },
    getColumnsMetadata: () => {
        return columns;
    },
    getOrders: () => {
        return orders;
    },
    getResourceURI: () => {
        // Exemplo do nome da unidade de dados (DataUnit) utilizado para solicitar a exportação.
        return "dd://Financeiro/br.com.sankhya.fin.cad.receber";
    },
    getOffset: () => {
        // Exemplo do índice inicial dos itens que serão exportados.
        return 0;
    },
    getLimit: () => {
        // Exemplo do valor máximo que a quantidade de itens exportados pode atingir.
        return 150;
    },
    getSelectedIDs: () => {
        return selectedIDs;
    },
    getRecordID: () => {
        // Exemplo do ID em Base64 utilizado para buscar a lista de relatórios personalizados.
        // Corresponde ao JSON: {"__DATA_UNIT_NAME__":{"value":"dd://Financeiro/br.com.sankhya.fin.cad.receber"},"NUFIN":{"value":"461"}}
        return "eyJfX0RBVEFfVU5JVF9OQU1FX18iOnsidmFsdWUiOiJkZDovL0ZpbmFuY2Vpcm8vYnIuY29tLnNhbmtoeWEuZmluLmNhZC5yZWNlYmVyIn0sIk5VRklOIjp7InZhbHVlIjoiNDYxIn19";
    }
};

/**
 * Exemplo da lista que contém os filtros de dados utilizados para a exportação.
 */
const filters = [
    {
        expression: "this.NUFIN = :NUFIN AND NOT (this.PROVISAO = 'S' AND this.DHBAIXA IS NOT NULL AND this.ORIGEM = 'E')",
        name: "NUFIN",
        params: [
            {
                name: "NUFIN",
                dataType: "NUMBER",
                value: "7076"
            }
        ]
    }
];

/**
 * Exemplo da lista que contém os dados das colunas usados para a exportação.
 */
const columns = [
    {
        id: "NUMNOTA",
        label: "Nr. Nota",
        width: 100,
        dataType: "NUMBER",
        userInterface: "INTEGERNUMBER"
    },
    {
        id: "CODEMP",
        label: "Empresa",
        width: 100,
        dataType: "OBJECT",
        userInterface: "SEARCH"
    }
];

/**
 * Exemplo da lista que determina a ordem das colunas utilizada para a exportação.
 */
const orders = [
    {
        field: "NUMNOTA",
        dataType: "NUMBER",
        mode: "ASC"
    }
];

/**
 * Exemplo da lista de IDs dos registros selecionados.
 */
const selectedIDs = [
    {
        name: "NUFIN",
        type: "NUMBER",
        value: "7439"
    },
    {
        name: "NUFIN",
        type: "NUMBER",
        value: "7441"
    },
    {
        name: "NUFIN",
        type: "NUMBER",
        value: "8272"
    }
];
```

## ServerSideExporter e ClientSideExporter

O **DataExporter** decide qual estratégia usar baseando-se na implementação no provider (IExporterProvider). Caso o provider implemente o método **getRecords** , a estratégia utilizada é **ClientSideExporter**. E, caso o provider não implemente **getRecords** , a estratégia é **ServerSideExporter**.

#### ServerSideExporter

Estratégia responsável por fazer a exportação da grade buscando os dados no back-end para realizar a geração do relatório. Esta é a estratégia utilizada por padrão no (**SnkCrud**) .

#### ClientSideExporter

Estratégia responsável por fazer a exportação da grade utilizando os dados que já estão no front-end para realizar a geração do relatório.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| provider | -- | Provedor das informações para exportação dos dados. | IExporterProvider | null |

### Dependencies

#### Used by

  * snk-crud
  * snk-detail-view
  * snk-grid
  * snk-guides-viewer
  * snk-simple-crud
  * snk-taskbar

#### Depends on

  * snk-exporter-email-sender
