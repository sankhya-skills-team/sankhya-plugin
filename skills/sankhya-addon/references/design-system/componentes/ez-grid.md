> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/ (snapshot 2026-09-28)

# Grid

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils, DataUnitLoaderUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    return (
        <div className="box">
            <EzGrid dataUnit={dataUnit} autoFocus={false}/>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (dataUnit, request) => {
    return DataUnitLoaderUtils.buildLoadDataResponse(source, dataUnit, request);
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataUnit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit(dataUnit, request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

> **Observação** : A grade tem uma altura mínima de 300px

## Navegação via teclado

Esta funcionalide permite aos usuários editar e avançar para células da grade de forma eficiente, além de fornecer uma experiência de navegação simplificada.

Para navegar pela grade, utilize as seguintes teclas:

  * **Seta para cima` ↑ `:** Move para a célula acima.
  * **Seta para baixo` ↓ `:** Move para a célula abaixo.
  * **Seta para a esquerda` ← `:** Move para a célula à esquerda.
  * **Seta para a direita` → `:** Move para a célula à direita.
  * **Tecla` ENTER `:** Além de ser utilizada na edição é possível usar para navegação também, ao pressionar a tecla a navegação move para a célula abaixo, ou quando a propriedade **useEnterLikeTab ** está habilitada, moverá para o lado direito.
  * **Tecla` SHIFT ` \+ ` ENTER `:** Além de ser utilizada na edição é possível usar para navegação também, ao pressionar a tecla a navegação move para a célula acima, ou quando a propriedade **useEnterLikeTab ** está habilitada, moverá para o lado esquerdo.

## Edição de Células

Quando a propriedade **canEdit** está habilitada siga as instruções abaixo:

  1. **Seleção da Célula:**

     * Utilize as teclas de navegação para selecionar a célula desejada.
  2. **Iniciar Edição:**

     * Pressione a tecla ` ENTER ` para iniciar a edição na célula selecionada.
  3. **Cancelar Edição:**

     * A qualquer momento durante a edição, pressione a tecla ` ESC ` para cancelar as alterações e sair do modo de edição.
  4. **Salvar Edição:**

     * Após fazer as alterações desejadas, pressione a tecla ` ENTER ` novamente para salvar as alterações e sair do modo de edição.

## Controle de paginação

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

Importante

Quando a grid é limitada horizontalmente, a informação de **Itens na página** e **Total de itens** será exibida por um tooltip nos **botões de navegação**.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    useEffect(() => {
        dataUnit.loadData();
    }, []);

    return (
        <div className={"dual-grid"}>
            <div className={"box-with-space"}>
                <EzGrid dataUnit={dataUnit} autoFocus={false} />
            </div>
            <div className="box-without-space">
                <EzGrid dataUnit={dataUnit} autoFocus={false} />
            </div>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {offset, limit, sort}) => {
    const currentPage = Math.ceil(offset / limit);
    const total = source.length;
    const firstRecord = offset;
    const lastRecord = Math.min(firstRecord + limit, total);
    const hasMore = lastRecord < total;

    return {
        records:
            sortRecords(source, sort)
            .slice(firstRecord, lastRecord),
        paginationInfo: {
            currentPage,
            firstRecord,
            lastRecord,
            total,
            hasMore
        }
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.pageSize = 3;

dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};

dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Totalizador de colunas

É possível definir colunas que possuam totalizadores, como soma, média, contagem, valor máximo e valor mínimo.

Para isso, nas definições dos **fields** dos metadados do **DataUnit** , deve-se utilizar a propriedade **aggFunc** com o nome da função que será utilizada para calcular o totalizador.

____

Estado ____

____

Capital ____

____

Sigla ____

____

População ____

____

Área (km²) ____

____

IDH ____

____

PIB per Capita (R$) ____

____

Temp. Mín (°C) ____

Acre

Rio Branco

AC

906.876,00

164.123,00

0,66

18.362,00

18,00

Alagoas

Maceió

AL

3.365.351,00

27.848,00

0,63

17.687,00

20,00

Amapá

Macapá

AP

877.613,00

142.815,00

0,71

19.722,00

23,00

Amazonas

Manaus

AM

4.269.995,00

1.559.162,00

0,67

23.647,00

22,00

Bahia

Salvador

BA

14.985.284,00

564.732,00

0,66

17.714,00

18,00

Ceará

Fortaleza

CE

9.240.580,00

148.894,00

0,68

17.772,00

22,00

Distrito Federal

Brasília

DF

3.094.325,00

5.760,00

0,82

85.274,00

15,00

Espírito Santo

Vitória

ES

4.108.508,00

46.095,00

0,74

31.622,00

18,00

Goiás

Goiânia

GO

7.206.589,00

340.111,00

0,74

26.389,00

16,00

Maranhão

São Luís

MA

7.153.262,00

331.937,00

0,64

13.833,00

22,00

Mato Grosso

Cuiabá

MT

3.567.234,00

903.366,00

0,73

41.484,00

18,00

Mato Grosso do Sul

Campo Grande

MS

2.839.188,00

357.145,00

0,73

32.029,00

15,00

Minas Gerais

Belo Horizonte

MG

21.411.923,00

586.522,00

0,73

27.063,00

12,00

Pará

Belém

PA

8.777.124,00

1.247.690,00

0,65

17.180,00

22,00

Paraíba

João Pessoa

PB

4.059.905,00

56.469,00

0,66

16.344,00

20,00

0,00

0,00

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

Dica

As funções de agregação suportadas para totalizadores são:

  * **sum** : Soma dos valores.
  * **avg** : Média dos valores.
  * **count** : Contagem dos valores.
  * **max** : Valor máximo.
  * **min** : Valor mínimo.

Importante

Caso não queira exibir o totalizador de uma coluna específica, basta que nenhum campo tenha a propriedade **aggFunc** definida.

## Seleção múltipla

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    return (
        <div className="box">
            <EzGrid
                dataUnit={dataUnit}
                multipleSelection={true}
                autoFocus={false}
            />
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"}
];
```

## Seleção múltipla com paginação

Importante

A barra de informações que indica a **quantidade de registros selecionados** será visível somente quando a **Seleção múltipla** e a **Paginação** estiverem ativadas.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

## Suprimir filtro de coluna

Dica

Em alguns cenários específicos, desejamos suprimir o filtro de coluna. Para isso, podemos utilizar a propriedade **suppressFilterColumn**.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils, DataUnitLoaderUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
  useEffect(()=>{
    dataUnit.loadData();
  }, []);

  return (
    <div className="box">
      <EzGrid dataUnit={dataUnit} autoFocus={false} suppressFilterColumn={true}/>
    </div>
  );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (dataUnit, request) => {
  return DataUnitLoaderUtils.buildLoadDataResponse(source, dataUnit, request);
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
  name: "exemplo.datagrid",
  label: "Exemplo data grid",
  fields: [
    {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
    {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
    {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
  ]
};
dataUnit.dataLoader = (dataUnit, request) => new Promise(
  resolve => {
    //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
    setTimeout(() => resolve(fetchDataUnit(dataUnit, request)), 0);
  }
);

const source = [
  {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
  {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
  {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
  {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
  {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
  {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
  {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
  {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
  {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
  {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
  {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
  {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
  {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
  {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
  {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
  {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
  {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
  {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
  {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
  {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
  {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
  {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
  {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
  {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
  {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
  {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
  {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Validação de registros

> Propriedade utilizada: **recordsValidator**

Define um validador responsável pela integridade dos registros.

Reprodução

Para testar a demonstração abaixo altere alguma informação do primeiro registro da grade.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

## Edição na grade

> Propriedade utilizada: **canEdit**

Define se a edição está habilitada na grade.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import React, { useEffect, useState } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzButton, EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";

const Demo = () => {
    const [canEdit, setCanEdit] = useState(true);

    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    const buttonLabel = canEdit? 'Desabilitar edição' : 'Habilitar edição';

    return (
        <div className="box">
            <EzGrid dataUnit={dataUnit} canEdit={canEdit} autoFocus={false}>
                <EzButton slot="leftButtons" label={buttonLabel} onClick={() => setCanEdit(!canEdit)} />
            </EzGrid>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Configuração

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

## Parâmetro ENTER como TAB

> Propriedade utilizada: **useEnterLikeTab**

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    return (
        <div className="box">
            <EzGrid dataUnit={dataUnit} useEnterLikeTab={true} autoFocus={false} />
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Coluna de status

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

###

A coluna de status também pode ser resolvida por uma função.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    const status = data =>{
        if(data.SIGLA == "AM"){
            return "#157A00";
        }
    }

    return (
        <div className="box">
            <EzGrid
                statusResolver={status}
                dataUnit={dataUnit}
                autoFocus={false}
            />
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"}
];
```

## Tamanho mínimo

Por padrão a grade possui a altura mínima de **300px** , porém existe alguns casos onde o desenvolvedor pode desejar que a mesma possua uma altura mínima de **0px** para que o componente acompanhe o tamanho do container que o envolve.

Para isso, basta adicionar a classe css `grid_height-0`.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

## Foco automático

Por padrão, a grade possui foco automático, sendo importante para casos onde possui implementações de atalhos de teclado. Porém, existe alguns casos onde o desenvolvedor pode desejar que a mesma não ocorra, para isso, existe a propriedade booleana `autoFocus` onde pode ser definido seu comportamento.

## Inserção de item

> Propriedade utilizada: **enableGridInsert** Por padrão a inserção na grade vem desabilitada, porém quando ativada da ao usuário a possibilidade de inserir novos registros diretamente na grade.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzGrid, EzButton } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    const addRecord = () => {
        dataUnit.addRecord();
    }

    return (
        <div className="box">
            <EzGrid dataUnit={dataUnit} enableGridInsert={true}>
                <EzButton
                    slot="leftButtons"
                    label="Inserir registro"
                    onClick={() => addRecord()}
                />
            </EzGrid>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Inserção continua

> Propriedade utilizada: **enableContinuousInsert**

Essa propriedade somente é utilizada quando a inserção está ativada propriedade `enableGridInsert`. Por padrão caso a inserção de item esteja ativada a inserção continua também vem ativada, fazendo com que após salvar um registro, seja por envento de um botão salvar ou por alterar a linha selecionada, uma vez o salve sendo bem sucedido automaticamente inicia a inserção de um novo registro. Quando desabilitada ao final da inserção de um registro finaliza a edição.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

## Linhas zebradas

> Propriedade utilizada: **enableRowTableStriped**

Por padrão o zebrado na grade vem habilitado, porém sendo possivel desabilita-lo.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzGrid, EzButton } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    return (
        <div className="box">
            <EzGrid dataUnit={dataUnit} enableRowTableStriped={false}>
            </EzGrid>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Modo simplificado

> Propriedade utilizada: **mode**

O modo simples do componente ez-grid é projetado para oferecer uma experiência de usuário simplificada, mantendo as funcionalidades essenciais. Quando a propriedade `mode` é definida como `"simple"`, o grid opera em modo somente leitura, desabilitando a edição de células e removendo elementos de interface como a barra de ações e o cabeçalho. A paginação não é exibida visualmente, e os checkboxes de seleção de linhas são ocultados. Funcionalidades como ordenação, filtro e ajuste de largura das colunas são mantidas.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

Pará

Belém

PA

Paraíba

João Pessoa

PB

Paraná

Curitiba

PR

Pernambuco

Recife

PE

Piauí

Teresina

PI

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect } from "react";
import { DataUnit, StringUtils, DataUnitLoaderUtils } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    return (
        <div className="box">
            <EzGrid dataUnit={dataUnit} autoFocus={false} mode="simple"/>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (dataUnit, request) => {
    return DataUnitLoaderUtils.buildLoadDataResponse(source, dataUnit, request);
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataUnit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit(dataUnit, request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió", "SIGLA": "AL"},
    {__record__id__: "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá", "SIGLA": "AP"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador", "SIGLA": "BA"},
    {__record__id__: "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza", "SIGLA": "CE"},
    {__record__id__: "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília", "SIGLA": "DF"},
    {__record__id__: "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória", "SIGLA": "ES"},
    {__record__id__: "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia", "SIGLA": "GO"},
    {__record__id__: "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís", "SIGLA": "MA"},
    {__record__id__: "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá", "SIGLA": "MT"},
    {__record__id__: "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande", "SIGLA": "MS"},
    {__record__id__: "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte", "SIGLA": "MG"},
    {__record__id__: "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém", "SIGLA": "PA"},
    {__record__id__: "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa", "SIGLA": "PB"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife", "SIGLA": "PE"},
    {__record__id__: "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina", "SIGLA": "PI"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal", "SIGLA": "RN"},
    {__record__id__: "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre", "SIGLA": "RS"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis", "SIGLA": "SC"},
    {__record__id__: "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo", "SIGLA": "SP"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"},
    {__record__id__: "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas", "SIGLA": "TO"}
];
```

## Métodos

### setColumnsDef

Cria a definição sem depender dos metadados do DataUnit.

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### addColumnMenuItem

Permite adicionar itens de menu em cada uma das colunas.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### setColumnsState

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

```jsx
import React, { useEffect, useRef } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzButton, EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    const grid = useRef();
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    const setColumnsState = () => {
        grid.current.setColumnsState(state);
    }

    return (
        <div className="box">
            <EzGrid
                ref={grid}
                dataUnit={dataUnit}
                autoFocus={false}
            >
                <EzButton
                    slot="leftButtons"
                    label="Atribuir estado"
                    onClick={()=>setColumnsState()}
                />
            </EzGrid>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const state = [
    { name: "CAPITAL", width: 300, orderIndex: 1, ascending: true},
    { name: "SIGLA", width: 50},
    { name: "ESTADO", width: 100}
];

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"}
];
```

### getColumnsState

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

**Estado atual das colunas:**
```
Clique em "Listar estado de colunas"...
```

```jsx
import React, { useEffect, useRef, useState } from "react";
import { DataUnit, StringUtils } from "@sankhyalabs/core";
import { EzButton, EzGrid } from "@sankhyalabs/ezui/react/components";
import { DataType } from "@sankhyalabs/core/dist/dataunit/metadata/DataType";
import "./demo.css";

const Demo = () => {
    const grid = useRef();
    const [stateResult, setStateResult] = useState();
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    const getColumnsState = () => {
        grid.current.getColumnsState()
            .then(result => setStateResult(JSON.stringify(result, undefined, " ")));
    }

    return (
        <div className="ez-flex ez-flex--column">
            <div className="box">
                <EzGrid
                    ref={grid}
                    dataUnit={dataUnit}
                    autoFocus={false}
                >
                    <EzButton
                        slot="leftButtons"
                        label="Listar estado de colunas"
                        onClick={()=>getColumnsState()}
                    />
                </EzGrid>
            </div>
            <label className="ez-margin-top--large">
                <b>Estado atual das colunas: </b> <pre>{stateResult ? stateResult : "Clique em \"Listar estado de colunas\"..."}</pre>
            </label>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"}
];
```

### getColumns

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

**Colunas:**
```
Clique em "Listar colunas"...
```

### getSelection

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

**Linha(s) selecionada(s):** Clique em "Obter seleção"...

### setData

```jsx
import React, { useEffect, useRef } from "react";
import { EzGrid, EzButton } from "@sankhyalabs/ezui/react/components";
import "./demo.css";

const Demo = () => {
    const grid = useRef();
    useEffect(() => {
        grid.current.setColumnsDef(
            [
                { name: "ESTADO", label: "Estado" },
                { name: "CAPITAL", label: "Capital" }
            ]
        );
    }, [grid]);

    const applyData = () => {
        grid.current.setData(source);
    }

    return (
        <div>
            <div className="box">
                <EzGrid ref={grid} autoFocus={false}>
                    <EzButton
                        slot="leftButtons"
                        className="ez-padding-left--medium"
                        label="Aplicar dados"
                        onClick={()=>applyData()}
                    />
                </EzGrid>
            </div>
        </div>
    );
};

export default Demo;

const source = [
    {"ID": "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco"},
    {"ID": "01321321502", "ESTADO": "Alagoas", "CAPITAL": "Maceió"},
    {"ID": "01321321503", "ESTADO": "Amapá", "CAPITAL": "Macapá"},
    {"ID": "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus"},
    {"ID": "01321321505", "ESTADO": "Bahia", "CAPITAL": "Salvador"},
    {"ID": "01321321506", "ESTADO": "Ceará", "CAPITAL": "Fortaleza"},
    {"ID": "01321321507", "ESTADO": "Distrito Federal", "CAPITAL": "Brasília"},
    {"ID": "01321321508", "ESTADO": "Espírito Santo", "CAPITAL": "Vitória"},
    {"ID": "01321321509", "ESTADO": "Goiás", "CAPITAL": "Goiânia"},
    {"ID": "01321321510", "ESTADO": "Maranhão", "CAPITAL": "São Luís"},
    {"ID": "01321321511", "ESTADO": "Mato Grosso", "CAPITAL": "Cuiabá"},
    {"ID": "01321321512", "ESTADO": "Mato Grosso do Sul", "CAPITAL": "Campo Grande"},
    {"ID": "01321321513", "ESTADO": "Minas Gerais", "CAPITAL": "Belo Horizonte"},
    {"ID": "01321321514", "ESTADO": "Pará", "CAPITAL": "Belém"},
    {"ID": "01321321515", "ESTADO": "Paraíba", "CAPITAL": "João Pessoa"},
    {"ID": "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba"},
    {"ID": "01321321517", "ESTADO": "Pernambuco", "CAPITAL": "Recife"},
    {"ID": "01321321518", "ESTADO": "Piauí", "CAPITAL": "Teresina"},
    {"ID": "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro"},
    {"ID": "01321321520", "ESTADO": "Rio Grande do Norte", "CAPITAL": "Natal"},
    {"ID": "01321321521", "ESTADO": "Rio Grande do Sul", "CAPITAL": "Porto Alegre"},
    {"ID": "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho"},
    {"ID": "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista"},
    {"ID": "01321321524", "ESTADO": "Santa Catarina", "CAPITAL": "Florianópolis"},
    {"ID": "01321321525", "ESTADO": "São Paulo", "CAPITAL": "São Paulo"},
    {"ID": "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju"},
    {"ID": "01321321527", "ESTADO": "Tocantins", "CAPITAL": "Palmas"}
];
```

### addGridCustomRender

Com o método **addGridCustomRender** é possível alterar o elemento que é mostrado na coluna do Grid, podendo criar um elemento customizado dependendo ou não dos valores anteriores.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### addCustomEditor

Com o método **addCustomEditor** é possível alterar o elemento que é mostrado na coluna daq Grid em modo de edição e no formulário.

Importante

Ao retornar o elemento como string ou utilizando o método `renderToString` provido pelo `react-dom/server`, não será aplicado **nenhum** código JavaScript, portanto, em casos de inputs ou similares é necessário que o elemento seja criado a partir do `document`, utilizando o método `createElement`.

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Alagoas

Maceió

AL

Amapá

Macapá

AP

Amazonas

Manaus

AM

Bahia

Salvador

BA

Ceará

Fortaleza

CE

Distrito Federal

Brasília

DF

Espírito Santo

Vitória

ES

Goiás

Goiânia

GO

Maranhão

São Luís

MA

Mato Grosso

Cuiabá

MT

Mato Grosso do Sul

Campo Grande

MS

Minas Gerais

Belo Horizonte

MG

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import { EzButton, EzGrid } from "@sankhyalabs/ezui/react/components";
import React, { useEffect, useRef } from 'react';
import { renderToString } from "react-dom/server";
import { buildDataUnit } from "./constants";

const dataUnit = buildDataUnit();
const Demo = () => {
    const ezGridRef = useRef(null);

    useEffect(() => {
        dataUnit.loadData();
    }, []);

    const setCustomElement = () => {
        const customEditor = {
            getEditorElement: ({ setValue, value }) => {
                const textInput = document.createElement('input');
                textInput.label = 'Editor customizado';
                textInput.value = value;
                textInput.onkeyup = (event) => {
                    setValue(event.target.value);
                };
                return textInput;
            }
        };
        ezGridRef.current?.addCustomEditor("ESTADO", customEditor);
    }

    const setCustomElementString = () => {
        const customEditor = {
            getEditorElement: () => {
                const elemment = `<div class='ez-text--tertiary'>Elento customizado em modo de edição</div>`;
                return elemment;
            }
        };
        ezGridRef.current?.addCustomEditor("ESTADO", customEditor);
    }

    const setCustomElementReactString = () => {
        const customEditor = {
            getEditorElement: (params) => {
                const Element = <div className="ez-text--tertiary">Edição utilizando reactToString: {params.value}</div>
                const stringElement = renderToString(Element);
                return stringElement;
            }
        };
        ezGridRef.current?.addCustomEditor("ESTADO", customEditor);
    }

    const editElement = () => {
        const customEditor = {
            getEditorElement: (params) => {
                const container = document.createElement('div');
                container.className = 'ez-flex';
                const icon = document.createElement('ez-icon');
                icon.size = "x-small"
                icon.iconName = "search"
                icon.className = "ez-padding-right--small"
                container.appendChild(icon)
                const element = params.currentEditor;
                container.appendChild(element);
                return container;
            }
        };
        ezGridRef.current?.addCustomEditor("ESTADO", customEditor);
    }

    const cleanElement = () => {
        const customEditor = {
            getEditorElement: () => { }
        };
        ezGridRef.current?.addCustomEditor("ESTADO", customEditor);
    }

    return (
        <div className="box">
            <EzGrid
                ref={ezGridRef}
                dataUnit={dataUnit}
                multipleSelection={true}
                autoFocus={false}
            >
                <div className='ez-flex ez-flex--wrap ez-padding--medium' slot="footer">
                    <EzButton size="small" label="Exibir elemento nativo customizado" onClick={setCustomElement} className="ez-margin-top--medium" />
                    <EzButton size="small" label="Exibir elemento em string customizado" onClick={setCustomElementString} className="ez-margin-top--medium" />
                    <EzButton size="small" label="Exibir elemento utilizando o reactToString" onClick={setCustomElementReactString} className="ez-margin-top--medium" />
                    <EzButton size="small" label="Exibir elemento editado" onClick={editElement} className="ez-margin-top--medium" />
                    <EzButton size="small" label="Resetar elemento" onClick={cleanElement} className="ez-margin-top--medium" />
                </div>

            </EzGrid>
        </div>
    );
};

export default Demo;
```

## Eventos

### ezSelectionChange

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

**Linhas selecionadas:**

### ezDoubleClick

Clique duas vezes em uma das linhas da grade:

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

**Linha do clique duplo:**

```jsx
import React, { useState, useEffect } from "react";
import { DataUnit, StringUtils, DataType } from "@sankhyalabs/core";
import { EzGrid } from "@sankhyalabs/ezui/react/components";
import "./demo.css";

const Demo = () => {
    const [doubleClickResult, setDoubleClickResult] = useState();
    useEffect(()=>{
        dataUnit.loadData();
    }, []);

    const doubleClickHandler = (item) => {
        setDoubleClickResult(item.ESTADO);
    };

    return (
        <div className="ez-flex ez-flex--column">
            <label className="ez-margin-bottom--medium">Clique duas vezes em uma das linhas da grade:</label>
            <div className="box">
                <EzGrid
                    dataUnit={dataUnit}
                    onEzDoubleClick={evt=>doubleClickHandler(evt.detail)}
                    autoFocus={false}
                />
            </div>
            <label className="ez-margin-top--large">
                <b>Linha do clique duplo: </b> {doubleClickResult}
            </label>
        </div>
    );
};

export default Demo;

//Monta o resultado da carga de registros.
const fetchDataUnit = (source, {sort}) => {
    return {
        records: sortRecords(source, sort)
    };
};

//Aplica os critérios de ordenação.
const sortRecords = (source, sortingFields) => {
    if(!sortingFields){
        return source;
    }
    return source.sort((record1, record2) => {
        for(let fieldSort of sortingFields){
            const {field, mode} = fieldSort;
            const valueA = mode === "ASC" ? record1[field] : record2[field];
            const valueB = mode === "ASC" ? record2[field] : record1[field];
            const result = StringUtils.compare(valueA, valueB);
            if(result !== 0){
                return result;
            }
        }
    });
};

const dataUnit = new DataUnit();
dataUnit.metadata = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: DataType.TEXT},
        {name: "CAPITAL", label: "Capital", dataType: DataType.TEXT},
        {name: "SIGLA", label: "Sigla", dataType: DataType.TEXT}
    ]
};
dataUnit.dataLoader = (dataunit, request) => new Promise(
    resolve => {
        //Um setTimeout foi utilizado com a finalidade de simular o tempo de carga de um servidor
        setTimeout(() => resolve(fetchDataUnit([...source], request)), 0);
    }
);

const source = [
    {__record__id__: "01321321501", "ESTADO": "Acre", "CAPITAL": "Rio Branco", "SIGLA": "AC"},
    {__record__id__: "01321321504", "ESTADO": "Amazonas", "CAPITAL": "Manaus", "SIGLA": "AM"},
    {__record__id__: "01321321516", "ESTADO": "Paraná", "CAPITAL": "Curitiba", "SIGLA": "PR"},
    {__record__id__: "01321321519", "ESTADO": "Rio de Janeiro", "CAPITAL": "Rio de Janeiro", "SIGLA": "RJ"},
    {__record__id__: "01321321522", "ESTADO": "Rondônia", "CAPITAL": "Porto Velho", "SIGLA": "RO"},
    {__record__id__: "01321321523", "ESTADO": "Roraima", "CAPITAL": "Boa Vista", "SIGLA": "RR"},
    {__record__id__: "01321321526", "ESTADO": "Sergipe", "CAPITAL": "Aracaju", "SIGLA": "SE"}
];
```

### ezColumnStateChange

Modifique a ordem, posição, largura ou fixação das colunas e visualize o resultado do evento:

____

Estado ____

____

Capital ____

____

Sigla ____

Acre

Rio Branco

AC

Amazonas

Manaus

AM

Paraná

Curitiba

PR

Rio de Janeiro

Rio de Janeiro

RJ

Rondônia

Porto Velho

RO

Roraima

Boa Vista

RR

Sergipe

Aracaju

SE

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

**Detalhe do evento:**
```
Altere a configuração de colunas...
```

## Formatador personalizado

É possível adicionar formatadores personalizados (CustomValueFormatter) através do método **addCustomValueFormatter** do componente. Este formatador deve seguir a interface ICustomFormatter e, através do método **format** , retornar um valor formatado a ser apresentado na grade.

O método **removeCustomValueFormatter** remove um formatador personalizado previamente adicionado.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| autoFocus | auto-focus | Define se a grid será focada ao ser carregada. | boolean | true |
| canEdit | can-edit | Define se a edição está habilitada na grid. | boolean | true |
| columnfilterDataSource | -- | Define um IMultiSelectionListDataSource responsável por alimentar o filtro de colunas. | IMultiSelectionListDataSource | undefined |
| compact | compact | Define se a grade deve ser exibida em modo compacto | boolean | false |
| config | -- | Configuração de exibição da grade. | IGridConfig | undefined |
| dataUnit | -- | Unidade de dados. Responsável pelo controle de edição de registros e informações pertinentes aos campos. | DataUnit | undefined |
| enableContinuousInsert | enable-continuous-insert | Ativa/desativa a inserção continua na grade Só funciona quando a prop enableGridInsert está ativa | boolean | true |
| enableGridInsert | enable-grid-insert | Ativa inserção de registros no modo grade. | boolean | false |
| enableLockManagerLoadingComp | enable-lock-manager-loading-comp | Define se o componente deve usar o LockManager para controle de carregamento da aplicação | boolean | false |
| enableLockManagerTaskbarClick | enable-lock-manager-taskbar-click | Ativa inserção de registros no modo grade pela Taskbar. | boolean | true |
| enableRowTableStriped | enable-row-table-striped | Ativa modo de linhas com cores alternadas. | boolean | true |
| hidePagination | hide-pagination | Esconder paginação. | boolean | false |
| mode | mode | Define o modo de uso da grade | "complete" \| "simple" | "complete" |
| multipleSelection | multiple-selection | Habilita a seleção de várias linhas. | boolean | undefined |
| outlineMode | outline-mode | Altera visualmente as sombras e bordas do componente Quando false, aplica o padrão de sombras ao componente (Utilizar quando for o elemento principal do layout) Quando true, aplica o padrão de outline ao componente (Utilizar quando estiver contido em outro elemento como um painel ou pop-up) | boolean | false |
| paginationCounterMode | pagination-counter-mode | Define a forma como a paginação irá se comportar. | "auto" \| "hidden" \| "show" | 'auto' |
| recordsValidator | -- | Define um validador responsável pela integridade dos registros. | IRecordValidator | undefined |
| selectionToastConfig | -- | Configuração da seleção de grade no toast. | ISelectionToastConfig | undefined |
| serverUrl | server-url | Endereço do servidor para obtenção dos dados. | string | undefined |
| statusResolver | -- | Define um IStatusResolver responsável pelo estado da coluna de status. | ((data: object) => string) \| IStatusResolver | undefined |
| suppressCheckboxColumn | suppress-checkbox-column | Informa se a coluna de chechbox deve ser suprimida | boolean | false |
| suppressFilterColumn | suppress-filter-column | Informa se a grade deve suprimir o filtro de coluna. | boolean | false |
| suppressHorizontalScroll | suppress-horizontal-scroll | Define se a grade deve suprimir o scroll horizontal. | boolean | false |
| useEnterLikeTab | use-enter-like-tab | Quando verdadeiro, o ENTER fará a navegação como se fosse a tecla TAB na grade. | boolean | false |
| useSearchColumn | use-search-column | Define se a grade deve exibir um buscador de coluna com uso do Ctrl+F | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| componentReady | Emitido quando o componente estiver completamente carregado. | CustomEvent<void> |
| configChange | Emitido quando acontece a alteração de configuração do grade. | CustomEvent<IGridConfig> |
| ezColumnFilterChanged | Emitido quando acontece a alteração de filtro de colunas. | CustomEvent<Filter[]> |
| ezColumnStateChange | Emitido quando acontece a alteração de estado das colunas do grid: Ordenação, largura, etc. | CustomEvent<EzGridColumStateEvent> |
| ezDoubleClick | Emitido com o duplo clique de uma linha | CustomEvent<any> |
| ezPageChangedChanged | Emitido a página atual é alterada. | CustomEvent<void> |
| ezSelectionChange | Emitido quando acontece a alteração de seleção de linhas. | CustomEvent<ISelection> |

### Methods

#### `addColumnMenuItem(label: string, name: string, action: Function, icon: HTMLElement | string) => Promise<void>`

Adiciona item de menu nas colunas.

##### Returns

Type: `Promise<void>`

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

##### Returns

Type: `Promise<void>`

#### `addCustomValueFormatter(columnName: string, customFormatter: ICustomFormatter) => Promise<void>`

Registra um formatador de valores para uma coluna da grid.

##### Returns

Type: `Promise<void>`

#### `addGridCustomRender(fieldName: string, customRender: ICustomRender, detailContext?: string) => Promise<void>`

Registra um render customizado para colunas da grid.

##### Returns

Type: `Promise<void>`

#### `checkStopEditOutsideClick(event: MouseEvent) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `filterColumns(search: string) => Promise<Array<EzGridColumn>>`

Usa um argumento para filtrar as colunas po label

##### Returns

Type: `Promise<EzGridColumn[]>`

#### `getAppliedColumnFilters() => Promise<Array<Filter>>`

Retorna os filtros aplicados.

##### Returns

Type: `Promise<Filter[]>`

#### `getColumns() => Promise<Array<EzGridColumn>>`

Obtém a lista de definição de colunas.

##### Returns

Type: `Promise<EzGridColumn[]>`

#### `getColumnsState() => Promise<Array<EzGridColumn>>`

Obtém o estado atual das colunas.

##### Returns

Type: `Promise<EzGridColumn[]>`

#### `getCustomValueFormatter(columnName: string) => Promise<ICustomFormatter | undefined>`

Retorna o formatador customizado da coluna caso exista.

##### Returns

Type: `Promise<ICustomFormatter>`

#### `getSelection() => Promise<Array<any>>`

Obtém as linhas selecionadas.

##### Returns

Type: `Promise<any[]>`

#### `handlePageChange() => Promise<void>`

Manipula a mudança de página da grid.

##### Returns

Type: `Promise<void>`

#### `locateColumn(columnName: string) => Promise<void>`

Localiza determinada coluna tornando-a visível.

##### Returns

Type: `Promise<void>`

#### `quickFilter(term: string) => Promise<void>`

Aplica um filtro rápido.

##### Returns

Type: `Promise<void>`

#### `refreshColumnFilterDataSource() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `refreshSelectedRows() => Promise<void>`

Atualiza linhas da grade.

##### Returns

Type: `Promise<void>`

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

Remove o formatador de valores de uma coluna da grid.

##### Returns

Type: `Promise<void>`

#### `setColumnsDef(cols: Array<EzGridColumn>) => Promise<void>`

Aplica a definição de colunas.

##### Returns

Type: `Promise<void>`

#### `setColumnsState(state: Array<EzGridColumnConfig>) => Promise<void>`

Aplica o estado das colunas.

##### Returns

Type: `Promise<void>`

#### `setData(data: Array<any>) => Promise<void>`

Insere os registros no ez-grid.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Atribui o foco para a grade.

##### Returns

Type: `Promise<void>`

#### `stopEdit() => Promise<void>`

Para a edição da grade.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-grid-view

#### Depends on

  * filter-column
  * ez-popover
  * ez-grid-pagination
  * ez-button
  * ez-icon
  * ez-search

### CSS Variables

| Variable | Description |
|---|---|
| --ez-grid__header--background-color | Define a cor de fundo do header do componente. |
| --ez-grid__selection-counter--z-index | Define o z-index do componente selection counter. |
| --ez-grid__container--shadow | Define o sombreamento usado como borda. |
| --ez-grid--min-height | Define altura mínima da grid |
| --ez-grid__container--shadow--outline | Define o outline usado como borda. |
| --ez-grid__header--shadow | Define a sombra do header. |
| --ez-grid__header--shadow--outline | Define o outline usado como borda do header. |
| --ez-grid__header--outline | Define o outline do header. |
| --ez-grid__header--border | Define a borda do header. |
