> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitLoaderUtils/ (snapshot 2026-09-28)

# DataUnitLoaderUtils

Ao implementar o _dataLoader_ do **DataUnit** , o desenvolvedor tem a responsabilidade de lidar com a **paginação** , **ordenação** e **filtragem** de dados.

Pensando nisso, disponibilizamos um utilitário que pode ajudar nessas abstrações, o **DataUnitLoaderUtils**.

Esse utilitário possibilita implementar toda a lógica de paginação, ordenação, filtragem e contrução do retorno exigito pelo _dataLoader_ `Promise<LoadDataResponse>`. Como também, disponibiliza métodos que lidam com cada funcionalidade de forma isolada, permitindo mais flexibilidade ao desenvolvedor.

## buildLoadDataResponse

`buildLoadDataResponse(recordsIn: Array<Record>, dataUnit: DataUnit, request: LoadDataRequest): Promise<LoadDataResponse>`

Esse método abstrai toda a lógica de **paginação** , **ordenação** e **filtragem** e retorna os dados já na estrutura esperada.

____

Nome do País ____

____

Num. Habitantes ____

Brasil

214300000

Portugal

10330000

Angola

34500000

Macau

686607

Cabo Verde

587000

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useState, useEffect } from 'react';
import { EzGrid, EzButton } from '@sankhyalabs/ezui/react/components';
import { DataUnit, DataUnitLoaderUtils } from '@sankhyalabs/core';
import "./demo.css"

const COUNTRY_METADATA = {
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
        }
    ]
};

const COUNTRY_DATA = [
    {
        "__record__id__": "1",
        "NOME": "Brasil",
        "POPULACAO": 214300000
    },
    {
        "__record__id__": "2",
        "NOME": "Portugal",
        "POPULACAO": 10330000
    },
    {
        "__record__id__": "3",
        "NOME": "Angola",
        "POPULACAO": 34500000
    },
    {
        "__record__id__": "4",
        "NOME": "Macau",
        "POPULACAO": 686607
    },
    {
        "__record__id__": "5",
        "NOME": "Cabo Verde",
        "POPULACAO": 587000
    }
];

const Demo = () => {
    const [duCountries, setDuCountries ] = useState();

    useEffect(() => {
        setDuCountries(new DataUnit());
    }, []);

    useEffect(() => {
        if(duCountries == undefined) return;

        initDataUnit();
        loadDataUnit();
    }, [duCountries]);

    //Sobrescreve os loaders do dataUnit
    function initDataUnit(){
        duCountries.metadataLoader = metadataLoaderCountries;
        duCountries.dataLoader = dataLoaderCountries;
    }

    //Carrega as informações do dataUnit, usando os loaders implementados
    function loadDataUnit() {
        duCountries.loadMetadata().then(() => {
            duCountries.loadData();
        });
    }

    //Implementação do metadataLoader
    function metadataLoaderCountries(dataUnit){
        return new Promise((resolve) => {
            //Simulação do retorno do servidor
            console.log("Metadados carregados: ", COUNTRY_METADATA);
            resolve(COUNTRY_METADATA);
        });
    }

    //Implementação do dataLoader
    function dataLoaderCountries(dataUnit, request) {
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {

                /**
                * O utilitário DataUnitLoaderUtils.buildLoadDataResponse sabe lidar com funcionalidades de
                * filtragem, ordenação e paginação.
                */
                const responseData = DataUnitLoaderUtils.buildLoadDataResponse(COUNTRY_DATA, dataUnit, request);

                //Simulação do retorno do servidor
                console.log("Dados carregados: ", responseData);
                resolve(responseData);
            }, 500);
        });
    }

    return (
        <div className="data-loader">
            { duCountries &&
                <EzGrid
                    dataUnit={duCountries}
                    autoFocus={false}>
                        <EzButton
                            slot="leftButtons"
                            onClick={() => duCountries.loadData().then(alert("Dados Carregados"))}
                            iconName="sync"
                            size="small"
                            mode="icon">
                        </EzButton>
                </EzGrid>
                }
        </div>
    );
}

export default Demo;
```

## applyFilter

`applyFilter(records: Array<Record>, dataUnit: DataUnit, filters: Array<Filter>): Array<Record> `

Responsável por lidar com os filtros aplicados, geralmente os filtros de coluna. Retorna o array de registros resultante.

## applySorting

`applySorting(records: Array<Record>, dataUnit: DataUnit, sorting: Array<Sort>): Array<Record>`

Lida com a ordenação aplicada nos registros. Retorna o array de registros com os dados ordenados.

## getPagesByRecords

`getPagesByRecords(records: Record[], offset = 0, limit = 0): Array<Record>`

Retorna os registros de uma paginação específica, a partir de um _offset_ até um _limit_ especificados.

## buildPaginationInfo

`buildPaginationInfo({recordsLength = 0, offset = 0, recordsPerPage = 0}: PaginationInfoBuilderParams): PaginationInfo | undefined`

Retorna as informações de uma determinada paginação.

Dica

A interface do método dataUnitLoader recebe como parâmetro um argumento do tipo **LoadDataRequest** , que por sua vez contém as informações de _filtro_ , _ordenação_ entre outras, que devem ser aplicadas na listagem dos registros.
