> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitInMemoryLoader/ (snapshot 2026-09-28)

# DataUnitInMemoryLoader

O **DataUnit** atua como uma camada de abstração entre o _back-end_ e a interface do usuário, proporcionando uma solução eficaz para o gerenciamento de dados.

Porém, devido a necessidade de implementação de _loaders_ , gerenciamento de metadados e paginação, sua utilização pode trazer um nível de complexidade que não faça sentido para determinados contextos.

Pensando nisso, desenvolvemos o **DataUnitInMemoryLoader** que nada mais é, do quê um utilitário que nos entrega de forma bastante simplificada, uma instância de **DataUnit** pronta para uso, com seus _loaders_ já configurados e realizando o gerenciamento dos registros em memória.

Importante

O **DataUnitInMemoryLoader** implementa automaticamente o método `dataLoader` e outros métodos necessários do DataUnit, abstraindo a complexidade de paginação, ordenação e filtragem. Caso deseje sobrescrever esses métodos para implementar comportamentos personalizados (como integração com APIs específicas), consulte a documentação do **DataUnit** para entender como implementar corretamente esses métodos.

____

Nome ____

____

Dt. Nascimento ____

____

Nro. Camisa ____

Cristiano Ronaldo

05/02/1985

7

Leonel Messi

24/06/1987

10

Ronaldo Nazário

18/09/1976

9

Zinédine Zidane

23/06/1972

5

Manuel Neur

27/03/1986

1

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import React, { useEffect, useState } from 'react';
import { DataUnitInMemoryLoader, DateUtils } from '@sankhyalabs/core';
import { EzGrid, EzButton, EzDateInput, EzNumberInput, EzTextInput } from '@sankhyalabs/ezui/react/components';

const PLAYER_METADATA = {
  'name': 'jogadores',
  'label': 'jogadores',
  'fields': [
    {
      'name': 'NAME',
      'label': 'Nome',
      'dataType': 'TEXT',
      'userInterface': 'TEXT',
      'readOnly': true,
      'required': true,
    },
    {
      'name': 'BIRTHDAY',
      'label': 'Dt. Nascimento',
      'dataType': 'DATE',
      'userInterface': 'DATE',
    },
    {
      'name': 'SHIRT_NUMBER',
      'label': 'Nro. Camisa',
      'dataType': 'NUMBER',
      'userInterface': 'INTEGERNUMBER',
    },
  ],
};

const PLAYER_DATA = [
  {
    '__record__id__': '1',
    'NAME': 'Cristiano Ronaldo',
    'BIRTHDAY': '05/02/1985',
    'SHIRT_NUMBER': '7',
  },
  {
    '__record__id__': '2',
    'NAME': 'Leonel Messi',
    'BIRTHDAY': '24/06/1987',
    'SHIRT_NUMBER': '10',
  },
  {
    '__record__id__': '3',
    'NAME': 'Ronaldo Nazário',
    'BIRTHDAY': '18/09/1976',
    'SHIRT_NUMBER': '9',
  },
  {
    '__record__id__': '4',
    'NAME': 'Zinédine Zidane',
    'BIRTHDAY': '23/06/1972',
    'SHIRT_NUMBER': '5',
  },
  {
    '__record__id__': '5',
    'NAME': 'Manuel Neur',
    'BIRTHDAY': '27/03/1986',
    'SHIRT_NUMBER': '1',
  },
];

const Demo = () => {

  const [duPlayers, setDuPlayers] = useState();
  const [name, setName] = useState(null);
  const [birthDay, setBirthDay] = useState(null);
  const [shirtNumber, setShirtNumber] = useState(null);
  const [showErrorName, setShowErrorName] = useState(false);
  const [showErrorDate, setShowErrorDate] = useState(false);

  useEffect(() => {
    const inMemoryLoader = new DataUnitInMemoryLoader(PLAYER_METADATA, PLAYER_DATA);
    setDuPlayers(inMemoryLoader.dataUnit);
  }, []);

  async function handleAddRecord() {
    if (!duPlayers) return;

    if (!name || name.trim() === '') {
      setShowErrorName(true);
      return;
    }

    if (birthDay?.length > 0 && !DateUtils.validateDate(birthDay)) {
      setShowErrorDate(true);
      return;
    }

    await duPlayers.addRecord();
    await duPlayers.setFieldValue('NAME', name);
    await duPlayers.setFieldValue('BIRTHDAY', birthDay);
    await duPlayers.setFieldValue('SHIRT_NUMBER', shirtNumber);
    await duPlayers.saveData();

    setName(null);
    setBirthDay(null);
    setShirtNumber(null);
    setShowErrorName(false);
    setShowErrorDate(false);
  }

  return (
    <div>
      <div className="ez-flex ez-flex--justify-between ez-padding-vertical--small">
        <div className="ez-flex-item--auto">
          <EzTextInput label="Nome" id="recordLoaderName" mode="slim"
                       errorMessage={showErrorName ? 'Campo Obrigatório' : undefined} value={name}
                       onEzChange={(event) => setName(event.target.value)} />
        </div>

        <div className="ez-flex-item--auto ez-padding-horizontal--small">
          <EzDateInput label="Dt. Nascimento" id="recordLoaderPopulation" mode="slim" value={birthDay}
                       errorMessage={showErrorDate ? 'Data Inválida' : undefined}
                       onEzChange={(event) => setBirthDay(event.target.value)} />
        </div>

        <div className="ez-flex-item--auto ez-padding-horizontal--small">
          <EzNumberInput label="Nr. Camisa" id="recordLoaderName" mode="slim" value={shirtNumber}
                         onEzChange={(event) => setShirtNumber(event.target.value)} />
        </div>

        <div className="ez-flex-item--auto">
          <EzButton mode="icon" iconName="plus" size="small" className="ez-button--primary"
                    onClick={handleAddRecord} />
        </div>
      </div>

      {duPlayers &&
        <EzGrid dataUnit={duPlayers} compact={true} autoFocus={false}>
          <EzButton
            slot="leftButtons"
            onClick={() => duPlayers.removeSelectedRecords()}
            iconName="delete"
            size="small"
            mode="icon">
          </EzButton>
        </EzGrid>
      }
    </div>
  );
};

export default Demo;
```

## Configurações

Existem algumas opções de configurações que permitem um certo nível de customização no **DataUnit** criado pelo **DataUnitInMemoryLoader**.

Essas configurações devem ser passadas para o contrutor do **DataUnitInMemoryLoader** , seguindo a interface `DataUnitInMemoryLoaderConfig` disponibilizada pelo `sankhyacore`.

```text
export interface DataUnitInMemoryLoaderConfig {
  autoLoad?: boolean; // Define se os dados devem ser carregados automaticamente.
  pageSize?: number; // Controla a quantidade de registros por página
  recordDateFormat?: RECORD_DATE_FORMAT; // Define o formato padrão dos campos do tipo Data
}

export enum RECORD_DATE_FORMAT {
  DD_MM_YYYY = 'DD/MM/YYYY',
  ISO = 'ISO'
}
```

## Controle de Paginação

Por padrão, o **DataUnitInMemoryLoader** define um total de **150** registros por página. Porém, caso o desenvolvedor deseje personalizar isso, na instanciação do **DataUnitInMemoryLoader** , além dos parâmetros `metadata` e `records`, basta informar também o parâmetro `config` com a propriedade `pageSize` contendo o valo desejado.

> Propriedade utilizada: **pageSize**

### Tamanho da página

No exemplo abaixo, mostramos como criar um **DataUnit** com um tamanho de página de 5 registros.

____

Nome ____

____

Time ____

Cristiano Ronaldo

Real Madrid

Lionel Messi

Barcelona

Neymar Jr

Paris Saint-Germain

Kylian Mbappé

Paris Saint-Germain

Kevin De Bruyne

Manchester City

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### Escondendo controle de paginação

Existem cenários onde desejamos esconder o controle de paginação, para manter um layout mais _clean_ , por exemplo.

Nesses casos, para fazer isso, basta definir a propriedade `pageSize` com o valor **0**. Isso fará com que, além de todos os registros serem carregados em uma única página, o controle de paginação fique oculto.

____

Nome ____

____

Time ____

Cristiano Ronaldo

Real Madrid

Lionel Messi

Barcelona

Neymar Jr

Paris Saint-Germain

Kylian Mbappé

Paris Saint-Germain

Kevin De Bruyne

Manchester City

Robert Lewandowski

Bayern Munich

Mohamed Salah

Liverpool

Virgil van Dijk

Liverpool

Harry Kane

Tottenham

Eden Hazard

Real Madrid

Sergio Ramos

Paris Saint-Germain

Luis Suárez

Atlético Madrid

Paul Pogba

Juventus

Romelu Lukaku

Inter Milan

Gareth Bale

Los Angeles FC

Erling Haaland

Manchester City

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import React, { useEffect, useState } from 'react';
import { DataUnitInMemoryLoader, DateUtils } from '@sankhyalabs/core';
import { EzGrid, EzButton, EzDateInput, EzNumberInput, EzTextInput } from '@sankhyalabs/ezui/react/components';

const PLAYER_METADATA = {
  'name': 'jogadores',
  'label': 'jogadores',
  'fields': [
    {
      'name': 'NAME',
      'label': 'Nome',
      'dataType': 'TEXT',
      'userInterface': 'TEXT',
    },
    {
      'name': 'TEAM',
      'label': 'Time',
      'dataType': 'TEXT',
      'userInterface': 'TEXT',
    },

  ],
};

const PLAYER_DATA = [
  {
    '__record__id__': '1',
    'NAME': 'Cristiano Ronaldo',
    'TEAM': 'Real Madrid',
  },
  {
    '__record__id__': '2',
    'NAME': 'Lionel Messi',
    'TEAM': 'Barcelona',
  },
  {
    '__record__id__': '3',
    'NAME': 'Neymar Jr',
    'TEAM': 'Paris Saint-Germain',
  },
  {
    '__record__id__': '4',
    'NAME': 'Kylian Mbappé',
    'TEAM': 'Paris Saint-Germain',
  },
  {
    '__record__id__': '5',
    'NAME': 'Kevin De Bruyne',
    'TEAM': 'Manchester City',
  },
  {
    '__record__id__': '6',
    'NAME': 'Robert Lewandowski',
    'TEAM': 'Bayern Munich',
  },
  {
    '__record__id__': '7',
    'NAME': 'Mohamed Salah',
    'TEAM': 'Liverpool',
  },
  {
    '__record__id__': '8',
    'NAME': 'Virgil van Dijk',
    'TEAM': 'Liverpool',
  },
  {
    '__record__id__': '9',
    'NAME': 'Harry Kane',
    'TEAM': 'Tottenham',
  },
  {
    '__record__id__': '10',
    'NAME': 'Eden Hazard',
    'TEAM': 'Real Madrid',
  },
  {
    '__record__id__': '11',
    'NAME': 'Sergio Ramos',
    'TEAM': 'Paris Saint-Germain',
  },
  {
    '__record__id__': '12',
    'NAME': 'Luis Suárez',
    'TEAM': 'Atlético Madrid',
  },
  {
    '__record__id__': '13',
    'NAME': 'Paul Pogba',
    'TEAM': 'Juventus',
  },
  {
    '__record__id__': '14',
    'NAME': 'Romelu Lukaku',
    'TEAM': 'Inter Milan',
  },
  {
    '__record__id__': '15',
    'NAME': 'Gareth Bale',
    'TEAM': 'Los Angeles FC',
  },
  {
    '__record__id__': '16',
    'NAME': 'Erling Haaland',
    'TEAM': 'Manchester City',
  },
  {
    '__record__id__': '17',
    'NAME': 'Karim Benzema',
    'TEAM': 'Real Madrid',
  },
  {
    '__record__id__': '18',
    'NAME': 'Luka Modrić',
    'TEAM': 'Real Madrid',
  },
  {
    '__record__id__': '19',
    'NAME': 'Toni Kroos',
    'TEAM': 'Real Madrid',
  },
  {
    '__record__id__': '20',
    'NAME': 'Marcus Rashford',
    'TEAM': 'Manchester United',
  },
];

const Demo = () => {

  const [duPlayers, setDuPlayers] = useState();

  /**
   * Define as configurações do DU que será gerado
   */
  const duInMemoryLoaderConfig = { pageSize: 0 };

  useEffect(() => {
    const inMemoryLoader = new DataUnitInMemoryLoader(
      PLAYER_METADATA,
      PLAYER_DATA,
      duInMemoryLoaderConfig
    );

    setDuPlayers(inMemoryLoader.dataUnit);
  }, []);

  return (
    <div>
      {duPlayers &&
        <EzGrid dataUnit={duPlayers} compact={true} autoFocus={false} canEdit={false} suppressCheckboxColumn={true} />}
    </div>
  );
};

export default Demo;
```

## Carregando de dados

> Propriedade utilizada: **autoLoad**

Por padrão, o **DataUnit** irá carregar os dados assim que for renderizado na tela. Porém, podemos inibir esse comportamento, para que esse carregamento seja feito no momento que for mais adequado.

Para isso, podemos utilizar a propriedade `autoLoad` das configuraçõs definida com o valor `false` e quando for o momento de carregar os dados, chamar a função `loadData` do **DataUnit**.

____

Nome ____

____

Time ____

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

/

Há **registro** selecionado na grade.

## Padrão de campos tipo DATE

> Propriedade utilizada: **recordDateFormat**

A princípio, o **DataUnit** gerado pelo **DataUnitInMemoryLoader** está preparado para receber em seus campos do tipo `DATE` o padrão _DD/MM/YYYY_. Porém, existem casos onde o padrão adotado pelo desenvolvedor é o _ISO_.

Para atender asse cenário de forma simples e rápida, basta na criação da instância do **DataUnitInMemoryLoader** , informar a propriedade `recordDateFormat` com o valor `ISO`, podendo utilizar o _enum_ `RECORD_DATE_FORMAT` fornecido pela `sankhyacore`.

____

Nome ____

____

Dt. Nascimento ____

____

Nro. Camisa ____

Cristiano Ronaldo

05/02/1985

7

Leonel Messi

24/06/1987

10

Ronaldo Nazário

18/09/1976

9

Zinédine Zidane

23/06/1972

5

Manuel Neur

26/03/1986

1

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import React, { useEffect, useState } from 'react';
import { DataUnitInMemoryLoader, RECORD_DATE_FORMAT } from '@sankhyalabs/core';
import { EzGrid } from '@sankhyalabs/ezui/react/components';

const PLAYER_METADATA = {
  'name': 'jogadores',
  'label': 'jogadores',
  'fields': [
    {
      'name': 'NAME',
      'label': 'Nome',
      'dataType': 'TEXT',
      'userInterface': 'TEXT',
      'readOnly': true,
      'required': true,
    },
    {
      'name': 'BIRTHDAY',
      'label': 'Dt. Nascimento',
      'dataType': 'DATE',
      'userInterface': 'DATE',
    },
    {
      'name': 'SHIRT_NUMBER',
      'label': 'Nro. Camisa',
      'dataType': 'NUMBER',
      'userInterface': 'INTEGERNUMBER',
    },
  ],
};

const PLAYER_DATA = [
  {
    '__record__id__': '1',
    'NAME': 'Cristiano Ronaldo',
    'BIRTHDAY': '1985-02-05T05:00:00Z',
    'SHIRT_NUMBER': '7',
  },
  {
    '__record__id__': '2',
    'NAME': 'Leonel Messi',
    'BIRTHDAY': '1987-06-24T12:30:00Z',
    'SHIRT_NUMBER': '10',
  },
  {
    '__record__id__': '3',
    'NAME': 'Ronaldo Nazário',
    'BIRTHDAY': '1976-09-18T18:15:00Z',
    'SHIRT_NUMBER': '9',
  },
  {
    '__record__id__': '4',
    'NAME': 'Zinédine Zidane',
    'BIRTHDAY': '1972-06-23T04:00:00Z',
    'SHIRT_NUMBER': '5',
  },
  {
    '__record__id__': '5',
    'NAME': 'Manuel Neur',
    'BIRTHDAY': '1986-03-27',
    'SHIRT_NUMBER': '1',
  },
];

const Demo = () => {

  const [duPlayers, setDuPlayers] = useState();

  /**
   * Define as configurações do DU que será gerado
   */
  const duInMemoryLoaderConfig = { pageSize: 0, recordDateFormat: RECORD_DATE_FORMAT.ISO };

  useEffect(() => {
    const inMemoryLoader = new DataUnitInMemoryLoader(
      PLAYER_METADATA,
      PLAYER_DATA,
      duInMemoryLoaderConfig,
    );

    setDuPlayers(inMemoryLoader.dataUnit);
  }, []);

  return (
    <div>
      {duPlayers &&
        <EzGrid dataUnit={duPlayers} compact={true} autoFocus={false} canEdit={false} suppressCheckboxColumn={true} />}
    </div>
  );
};

export default Demo;
```
