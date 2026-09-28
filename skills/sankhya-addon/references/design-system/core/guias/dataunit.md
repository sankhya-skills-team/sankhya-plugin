> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/ (snapshot 2026-09-28)

# DataUnit

Criar interfaces de usuário que manipulam dados é um grande desafio que envolve diversas etapas, desde a recuperação dos dados até a apresentação deles de forma amigável para o usuário. A manipulação de dados costuma ser a parte mais desafiadora desse processo, uma vez que envolve uma série de tarefas, como a criação de registros, recuperação de informações, associação de atributos a campos na interface, a persistência dos dados, entre outras.

Embora as tecnologias atuais de desenvolvimento ofereçam recursos para reduzir a complexidade na manipulação de dados no contexto _front-end_ , essa ainda é uma das etapas mais desafiadoras na implementação de interfaces. Com base nesse pressuposto, foi criado o componente **DataUnit** , uma ferramenta intuitiva cujo objetivo é simplificar a manipulação de dados, abstraindo os detalhes técnicos desse processo. Com o **DataUnit** , é possível realizar as operações **CRUD** (_Create_ , _Read_ , _Update_ , _Delete_) nos registros e gerenciar os eventos associados a essas ações. Isso significa que os desenvolvedores podem se concentrar na criação de uma interface amigável para o usuário, sem se preocupar com os detalhes de como os dados são gerenciados.

O **DataUnit** atua como uma camada de abstração entre o _back-end_ e a interface do usuário, proporcionando uma solução eficaz para o gerenciamento de dados. Com essa abordagem, os desenvolvedores não precisam implementar essa funcionalidade de maneira detalhada, pois o **DataUnit** assume essa responsabilidade. Além disso, cabe destacar que o **DataUnit** possui forte desacoplamento com serviços de regra de negócio do _back-end_ , o que significa que não há conexão ou relação estabelecida com as entidades presentes no banco de dados. Isso torna o processo de gerenciamento de dados mais flexível e escalável, permitindo independência entre o _back-end_ e o _front-end_ , pois as alterações no _back-end_ não requerem mudanças no lado _front-end_. Desse modo, possibilitando mudanças futuras de forma ágil, sem comprometer o funcionamento do _back-end_.

> Em resumo, o DataUnit funciona como um intermediário entre os dados e a aplicação, atuando como uma espécie de API que conecta o estado com a View. Em outras palavras, funciona como um repositório de dados que contém metainformação para descrever cada um dos campos, o que o torna uma ferramenta poderosa para o gerenciamento e manipulação de dados de forma eficiente e intuitiva.

## Loaders do DataUnit

No contexto do `DataUnit`, um _Loader_ é um ponteiro de **função que executa serviços externos** ao `DataUnit`. Em termos gerais, são uma abstração usada para manter o `DataUnit` isolado de qualquer caso de uso específico. A ideia é permitir um nível de abstração que gera uma despreocupação com o processo interno de obtenção dos dados.

O `DataUnit` passa as informações para o ponteiro de função e espera que ele retorne uma `Promise`. O objetivo é que o `DataUnit` não precise conhecer a implementação e não saiba como os dados serão obtidos, tornando o componente agnóstico. Sendo assim, basta invocar um _Loader_ desejado e tratar a `Promise` retornada.

Em resumo, o conjunto de métodos responsáveis por carregar e manipular dados do `DataUnit` inclui os seguintes _Loaders_ :

  * metadataLoader, que fornece metadados do `DataUnit`;
  * dataLoader, que gerencia a solicitação de carregamento de dados;
  * saveLoader, que salva as alterações no `DataUnit`;
  * removeLoader, que exclui registros do `DataUnit`;
  * recordLoader, que carrega registros especificados do `DataUnit`.

Nos tópicos a seguir, serão espeficados cada um dos _Loaders_ , usando como exemplo uma simulação de uma carga de dados por um servidor.

### metadataLoader

O método `metadataLoader` é responsável por **definir os metadados** do DataUnit, recuperando as informações com base no parâmetro `DataUnit` passado como argumento e, em seguida, transforma essas informações em um objeto de metadados e o retorna a partir de uma `Promise`.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `metadataLoaderCountries`, implementação do `metadataLoader`.

____

Nome do País ____

____

Num. Habitantes ____

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useState, useEffect } from 'react';
import { EzGrid } from '@sankhyalabs/ezui/react/components';
import { DataUnit, StringUtils } from '@sankhyalabs/core';
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
    }

    //Carrega as informações do dataUnit, usando os loaders implementados
    function loadDataUnit() {
        duCountries.loadMetadata();
    }

    //Implementação do metadataLoader
    function metadataLoaderCountries(dataUnit){
        return new Promise((resolve) => {
            //Simulação do retorno do servidor
            console.log("Metadados carregados: ", COUNTRY_METADATA);
            resolve(COUNTRY_METADATA);
        });
    }

    return (
        <div className="metadata-loader">
            {duCountries &&
                <EzGrid dataUnit={duCountries} autoFocus={false}/>
            }
        </div>
    );
}

export default Demo;
```

### dataLoader

O método `dataLoader` encarrega-se de gerenciar a solicitação de **carregamento de dados** retornando os dados do DataUnit. O método recebe como parâmetro os atributos `dataUnit` e `request`, o primeiro parâmetro é o `DataUnit` ser carregado enquanto o `request` trata-se de um objeto do tipo `LoadDataRequest` que contém informações adicionais sobre como os dados devem ser carregados, como os filtros a serem aplicados, a ordenação, etc. A função retorna uma `Promise` que é resolvida com um objeto contendo os dados carregados.

É importante ressaltar que, é de respondabilidade do desenvolvedor ao implementar o `dataLoader`, que o mesmo lide com as funcionalidades de **paginação** , **ordenação** e **filtragem** , seja no _backend_ , no serviço que retorna os dados solicitados, ou no _frontend_ , na implementação do próprio `dataLoader`.

Informação

É esperado que todo registro possua uma propriedade chamada `__record__id__`, que é utilizada pelo `DataUnit` para indexação dos registros.

Dica

Para implementação das funcionalidades de **paginação** , **ordenação** e **filtragem** no _frontend_ , podemos utilizar a classe **DataUnitLoaderUtils** , que disponibiliza alguns utilitários que abstraem essa complexidade.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `dataLoaderCountries`, implementação do `dataLoader`.

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

### saveLoader

O `saveLoader` tem como atribuição **salvar as alterações** realizadas no `DataUnit`, e retorna uma `Promise` contendo os registros salvos. Para isso, a função recebe o `DataUnit` cujas mudanças serão salvas e um `Array` de objetos que representam as mudanças a serem feitas.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `saveLoaderCountries`, implementação do `saveLoader`.

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
import { EzGrid, EzButton, EzTextInput, EzNumberInput } from '@sankhyalabs/ezui/react/components';
import { DataUnit, StringUtils } from '@sankhyalabs/core';
import "./demo.css";

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
    const [countryName, setCountryName ] = useState();
    const [countryPopulation, setCountryPopulation ] = useState();

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
        duCountries.saveLoader = saveLoaderCountries;
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
    function dataLoaderCountries(dataUnit){
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {
                //Simulação do retorno do servidor
                console.log("Dados carregados: ", {records: COUNTRY_DATA});
                resolve({records: COUNTRY_DATA});
            }, 500);
        });
    }

    //Implementação do saveLoader
    function saveLoaderCountries(dataUnit, changes){
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {
                let dataUnitRecords = [];

                changes.forEach(change => {
                    let {record, updatingFields, operation} = change;

                    //Atribui um id caso um novo registro seja adicionado
                    if(operation === "INSERT") {
                        record["__record__id__"] = generateUniqueId(updatingFields);
                    }

                    //Atualiza o registro com as alterações realizadas
                    dataUnitRecords.push({...record, ...updatingFields});
                });

                //Simulação do retorno do servidor
                console.log("Alterações que serão salvas:", changes);
                resolve(dataUnitRecords);
            }, 500);
        });
    }

    //Gera um ID único para um novo registro
    function generateUniqueId(updatingFields) {
        return StringUtils.hashCode(`${updatingFields["POPULACAO"]+ updatingFields["NOME"]}`) + Math.floor(Math.random() * 200000);
    }

    //Popula os campos com o registro selecionado
    function changeSelection(selection) {
        if(selection?.length > 0) {
            setCountryName(selection[0]["NOME"]);
            setCountryPopulation(selection[0]["POPULACAO"]);
        } else {
            setCountryName(null);
            setCountryPopulation(null);
        }
    }

    //Adiciona um novo país
    function addCountry() {
        duCountries.addRecord();
        duCountries.setFieldValue("NOME", countryName);
        duCountries.setFieldValue("POPULACAO", countryPopulation);
        duCountries.saveData();
    }

    //Atualiza a população do registro selecionado
    function updatePopulation() {
        if(duCountries.getSelectedRecords().length > 0) {
            duCountries.setFieldValue("POPULACAO", countryPopulation);
            duCountries.saveData();
        } else {
            alert("Selecione um registro!");
        }
    }

    return (
        <div>
            <div className="ez-flex ez-flex--justify-between ez-padding-vertical--small">
                <div className="ez-flex-item--auto">
                    <EzTextInput
                        label="Nome do país"
                        id='recordLoaderName'
                        value={countryName}
                        onEzChange={(event) => setCountryName(event.target.value)}>
                    </EzTextInput>
                </div>

                <div className="ez-flex-item--auto ez-padding-horizontal--small">
                    <EzNumberInput
                        label="População"
                        id='recordLoaderPopulation'
                        value={countryPopulation}
                        onEzChange={(event) => setCountryPopulation(event.target.value)}>
                    </EzNumberInput>
                </div>

                <div>
                    <EzButton
                        mode="icon"
                        iconName="plus"
                        onClick={() => addCountry()} >
                    </EzButton>
                </div>
            </div>

            <div className="ez-row ez-padding-vertical--small ez-padding-bottom--medium ez-align--right">
                <div className="ez-col ez-align--right">
                    <div className="ez-col ez-padding-horizontal--small ">
                        <EzButton
                            size="small"
                            label="Atualizar População"
                            onClick={() => updatePopulation()} >
                        </EzButton>
                    </div>
                </div>
            </div>

            <div className="save-loader">
                { duCountries &&
                    <EzGrid
                        dataUnit={duCountries}
                        onEzSelectionChange={(event) => changeSelection(event.detail.selection)}
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
        </div>
    );
}

export default Demo;
```

### removeLoader

O método `removeLoader` é responsável por **excluir registros** do `DataUnit` e retornar uma `Promise` contendo os IDs dos registros que foram alvos da exclusão. O método recebe como parâmetro `dataUnit` e `recordIds`, onde `recordIds` é definido como um array contendo os identificadores dos registros que serão removidos do `DataUnit`.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `removeLoaderCountries`, implementação do `removeLoader`.

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

### recordLoader

O método `recordLoader` é usado para **carregar registros** do `DataUnit`. O método recebe como parâmetro `dataUnit` e `recordIds`, onde `recordIds` trata-se de um `Array` contendo os IDs que são passados automaticamente pela seleção dos registros. O método retorna uma `Promise` que, quando resolvida, fornece as informações dos registros carregados.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `recordLoaderCountries`, que é a implementação do `recordLoader`, para atualizar a população de um país selecionado para um valor aleatório. Para executá-lo, basta clicar no botão "Recarregar Registro Selecionado".

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
import { EzGrid, EzButton, EzTextInput, EzNumberInput } from '@sankhyalabs/ezui/react/components';
import { DataUnit, StringUtils } from '@sankhyalabs/core';
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
    const [countryName, setCountryName ] = useState();
    const [countryPopulation, setCountryPopulation ] = useState();

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
        duCountries.saveLoader = saveLoaderCountries;
        duCountries.removeLoader = removeLoaderCountries;
        duCountries.recordLoader = recordLoaderCountries;
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
    function dataLoaderCountries(dataUnit){
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {
                //Simulação do retorno do servidor
                console.log("Dados carregados: ", {records: COUNTRY_DATA});
                resolve({records: COUNTRY_DATA});
            }, 500);
        });
    }

    //Implementação do saveLoader
    function saveLoaderCountries(dataUnit, changes){
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {
                let dataUnitRecords = [];

                changes.forEach(change => {
                    let {record, updatingFields, operation} = change;

                    //Atribui um id caso um novo registro seja adicionado
                    if(operation === "INSERT") {
                        record["__record__id__"] = generateUniqueId(updatingFields);
                    }

                    //Atualiza o registro com as alterações realizadas
                    dataUnitRecords.push({...record, ...updatingFields});
                });

                //Simulação do retorno do servidor
                console.log("Alterações que serão salvas:", changes);
                resolve(dataUnitRecords);
            }, 500);
        });
    }

    //Gera um ID único para um novo registro
    function generateUniqueId(updatingFields) {
        return StringUtils.hashCode(`${updatingFields["POPULACAO"]+ updatingFields["NOME"]}`) + Math.floor(Math.random() * 200000);
    }

    //Implementação do removeLoader
    function removeLoaderCountries(dataUnit, recordIds){
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {
                //Simulação do retorno do servidor
                console.log("ID's dos registros removidos: ", recordIds);
                resolve(recordIds);
            }, 500);
        });
    }

    //Implementação do recordLoader
    function recordLoaderCountries(dataUnit, recordIds){
        return new Promise((resolve) => {
            //Foi utilizado um timeout para simular o tempo de carga de um servidor
            setTimeout(() => {
                let newPopulation = Math.floor(Math.random() * 200000000);
                dataUnit.setFieldValue("POPULACAO", newPopulation, recordIds);

                let selectedRecords = dataUnit.getSelectedRecords();
                setCountryPopulation(selectedRecords[0]["POPULACAO"]);

                resolve(selectedRecords);
            }, 500);
        });
    }

    //Popula os campos com o registro selecionado
    function changeSelection(selection) {
        if(selection?.length > 0) {
            setCountryName(selection[0]["NOME"]);
            setCountryPopulation(selection[0]["POPULACAO"]);
        } else {
            setCountryName(null);
            setCountryPopulation(null);
        }
    }

    //Adiciona um novo país
    function addCountry() {
        duCountries.addRecord();
        duCountries.setFieldValue("NOME", countryName);
        duCountries.setFieldValue("POPULACAO", countryPopulation);
        duCountries.saveData();
    }

    //Atualiza a população do registro selecionado
    function updatePopulation() {
        if(duCountries.getSelectedRecords().length > 0) {
            duCountries.setFieldValue("POPULACAO", countryPopulation);
            duCountries.saveData();
        } else {
            alert("Selecione um registro!");
        }
    }

    //Recarrega o país selecionado
    function reloadCountry() {
        if(duCountries.getSelectedRecords().length > 0) {
            duCountries.reloadCurrentRecord();
        } else {
            alert("Selecione um registro!");
        }
    }

    return (
        <div>
            <div className="ez-flex ez-flex--justify-between ez-padding-vertical--small">
                <div className="ez-flex-item--auto">
                    <EzTextInput
                        label="Nome do país"
                        id='recordLoaderName'
                        value={countryName}
                        onEzChange={(event) => setCountryName(event.target.value)}>
                    </EzTextInput>
                </div>

                <div className="ez-flex-item--auto ez-padding-horizontal--small">
                    <EzNumberInput
                        label="População"
                        id='recordLoaderPopulation'
                        value={countryPopulation}
                        onEzChange={(event) => setCountryPopulation(event.target.value)}>
                    </EzNumberInput>
                </div>

                <div>
                    <EzButton
                        mode="icon"
                        iconName="plus"
                        onClick={() => addCountry()} >
                    </EzButton>
                </div>
            </div>

            <div className="ez-row ez-padding-vertical--small ez-padding-bottom--medium ez-flex--justify-between">
                <div className="ez-col ez-padding-horizontal--small">
                    <EzButton
                        size="small"
                        label="Recarregar Registro Selecionado"
                        onClick={() => reloadCountry()} >
                    </EzButton>
                </div>

                <div className="ez-col ez-align--right">
                    <div className="ez-col ez-padding-horizontal--small ">
                        <EzButton
                            size="small"
                            label="Atualizar População"
                            onClick={() => updatePopulation()} >
                        </EzButton>
                    </div>
                </div>
            </div>

            <div className="record-loader">
                { duCountries &&
                    <EzGrid
                        dataUnit={duCountries}
                        onEzSelectionChange={(event) => changeSelection(event.detail.selection)}
                        autoFocus={false}>
                            <EzButton
                                slot="leftButtons"
                                onClick={() => duCountries.loadData().then(alert("Dados Carregados"))}
                                iconName="sync"
                                size="small"
                                mode="icon">
                            </EzButton>
                            <EzButton
                                slot="leftButtons"
                                onClick={() => duCountries.removeSelectedRecords()}
                                iconName="delete"
                                size="small"
                                mode="icon">
                            </EzButton>
                    </EzGrid>
                }
            </div>
        </div>
    );
}

export default Demo;
```

## Métodos públicos

O dataUnit expõe uma gama de métodos para permitir manipular seus dados, metadados, seleção de registros, controle de paginação, entre outros.

Seguem alguns exemplos:

### hideField / showField

Os métodos `hideField` e `showField` permitem que os metadados sejam manipulados, informando se um campo deve ser ocultado ou exibido.

____

Nome do País ____

____

Continente do País ____

____

Num. Habitantes ____

Brasil

América

214300000

Portugal

Europa

10330000

Angola

África

34500000

Japão

Ásia

78500000

Estados Unidos

América

298300000

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### setFieldValue

O método `setFieldValue` é utilizado para **inserir ou atualizar o valor de um campo** no registro atual do DataUnit. Este método possui um comportamento especial: **se não houver nenhum registro selecionado ou registro novo criado, ele automaticamente criará um novo registro** antes de atribuir o valor ao campo.

#### Parâmetros

  * **`fieldName`** (string): Identificador do campo que será modificado.
  * **`newValue`** (any): Valor a ser inserido no campo. Pode ser um valor direto ou uma `Promise` que será resolvida posteriormente.
  * **`records`** (Array<string>, opcional): Array com os IDs dos registros que serão afetados pela alteração. Se não fornecido, a alteração será aplicada ao registro atual.
  * **`options`** (DataUnitEventOptions, opcional): Objeto de configurações do evento, incluindo:
    * **`suppressCreateNewRecord`** (boolean): Quando `true`, impede a criação automática de um novo registro caso não haja registro selecionado. Neste caso, o método retornará `false` sem realizar alterações.

#### Retorno

Retorna uma `Promise<boolean>` que será resolvida quando o novo valor for persistido no state:

  * **`true`** : Quando o valor foi alterado com sucesso.
  * **`false`** : Quando o valor não foi alterado (valor igual ao atual, sem registro selecionado com `suppressCreateNewRecord` ativo, etc.).

#### Comportamento de criação de novo registro

Comportamento Importante

Se o método for chamado **sem nenhum registro selecionado** e **sem um registro novo em edição** , o DataUnit **automaticamente criará um novo registro** antes de atribuir o valor ao campo. Este comportamento pode ser suprimido utilizando a opção `suppressCreateNewRecord: true`.

____

Nome do País ____

____

Continente do País ____

____

Num. Habitantes ____

Brasil

América

214300000

Portugal

Europa

10330000

Angola

África

34500000

Japão

Ásia

78500000

Estados Unidos

América

298300000

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import { DataUnit } from '@sankhyalabs/core';
import { EzButton, EzClassicInput, EzGrid } from '@sankhyalabs/ezui/react/components';
import { useRef, useState } from 'react';
import "./demo.css";

const COUNTRY_METADATA = {
    "name": "paises",
    "label": "paises",
    "fields": [
        {
            "name": "NOME",
            "label": "Nome do País",
            "dataType": "TEXT",
            "userInterface": "TEXT",
            "visible": true,
            "readOnly": false,
            "required": true
        },
        {
            "name": "CONTINENTE",
            "label": "Continente do País",
            "dataType": "TEXT",
            "userInterface": "TEXT",
            "visible": true,
            "readOnly": false,
            "required": true
        },
        {
            "name": "POPULACAO",
            "label": "Num. Habitantes",
            "dataType": "NUMBER",
            "userInterface": "INTEGERNUMBER",
            "visible": true,
            "readOnly": false,
            "required": false
        }
    ]
};

const COUNTRY_DATA = [
    {
        "__record__id__": "1",
        "NOME": "Brasil",
        "CONTINENTE": "América",
        "POPULACAO": 214300000
    },
    {
        "__record__id__": "2",
        "NOME": "Portugal",
        "CONTINENTE": "Europa",
        "POPULACAO": 10330000
    },
    {
        "__record__id__": "3",
        "NOME": "Angola",
        "CONTINENTE": "África",
        "POPULACAO": 34500000
    },
    {
        "__record__id__": "4",
        "NOME": "Japão",
        "CONTINENTE": "Ásia",
        "POPULACAO": 78500000
    },
    {
        "__record__id__": "5",
        "NOME": "Estados Unidos",
        "CONTINENTE": "América",
        "POPULACAO": 298300000
    }
];

function buildInitialDataUnit() {
    const du = new DataUnit();
    du.metadata = COUNTRY_METADATA;
    du.records = COUNTRY_DATA;
    return du;
}

const Demo = () => {
    const duCountries = useRef(buildInitialDataUnit());
    const [inputFieldValue, setInputFieldValue] = useState("");
    const [alertMessage, setAlertMessage] = useState("");

    function applyNameChange() {
        if (duCountries.current == undefined) {
            return;
        }

        if(duCountries.current.getSelectedRecord() == null) {
            setAlertMessage("Nenhum país selecionado. Selecione um país na tabela para alterar seu nome.");
            return;
        }

        if(!inputFieldValue) {
            setAlertMessage("Nenhum valor informado. Por favor, insira um novo nome para o país.");
            return;
        }

        duCountries.current.setFieldValue("NOME", inputFieldValue);
    }

    function handleInputChange(event) {
        setInputFieldValue(event.detail);
        setAlertMessage("");
    }

    return (
        <div>
            <div className="ez-row ez-padding-vertical--small ez-padding-bottom--medium">
                <div className="field-value-controls">
                    <div className="field-value-controls__input">
                        <EzClassicInput
                            label="Definir valor do campo Nome do País:"
                            onEzChange={handleInputChange}
                            value={inputFieldValue}
                            state={alertMessage ? "error" : "default"}
                            helpText={alertMessage}
                        />
                    </div>
                    <div className="field-value-controls__button">
                        <EzButton
                            label="Alterar nome do país selecionado"
                            variant="primary"
                            onClick={applyNameChange} >
                        </EzButton>
                    </div>
                </div>
            </div>

            <div className="record-loader">
                {duCountries.current &&
                    <EzGrid
                        dataUnit={duCountries.current}
                        autoFocus={false}
                    />
                }
            </div>
        </div>
    );
}

export default Demo;
```

# API do Componente

**Clique aqui para acessar a API do DataUnit**
