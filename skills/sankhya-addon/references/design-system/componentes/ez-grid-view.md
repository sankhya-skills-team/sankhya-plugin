> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid-view/ (snapshot 2026-09-28)

# Grid View

O **EzGridView** é um componente que permite a **visualização** de dados em modo de grade de forma simples e dinâmica.

Diferente do **EzGrid** , ele oferece uma abordagem de implementação mais direta e prática, eliminando a necessidade do desenvolvedor configurar `dataLoaders`, lidar com **filtros** , **paginação** , entre outras configurações que apesar de poderosas, aumentam consideravelmente a complexidade de sua implementação.

Para usar o **EzGridView** , basta informar os **metadados das colunas** e o array com os registros, que o componente cuidará do resto.

Importante

É importante ressaltar que o **EzGridView** é um meio apenas de **visualização** dos dados em modo de grade. Ou seja, ele não possui funcionalidades de edição ou inserção de registros, como no **EzGrid**.

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

```jsx
import React, { useEffect } from 'react';
import { EzGridView } from '@sankhyalabs/ezui/react/components';
import "./demo.css";

const Demo = () => {
  useEffect(() => {
  }, []);

  return (
    <div className="box">
      <EzGridView
        metadata={PLAYER_METADATA}
        records={PLAYER_DATA}/>
    </div>
  );
};

export default Demo;

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
```

## Propriedades

O **EzGridView** possui algumas propriedades que permitem personalizar seu comportamento e aparência.

### Tamanho das colunas

É possível configurar as colunas do **EzGridView** através da propriedade `columnsConfig`. Com isso, é possível definir a largura inicial, alinhamento e outras características de cada coluna.

informação

A Propriedade `columnsConfig` deve ser um array de objetos da interface `ColumnConfig`.

```text
interface ColumnConfig {
  /**
   * ID da coluna. Em cada linha do array de dados, esse ID deve coincidir com
   * o nome do atributo que a coluna representa.
   */
  name: string,

  /**
   * Largura padrão da coluna em pixels absolutos.
   */
  width: number,
}
```

____

Nome ____

____

Dt. Nascimento ____

____

Nro. Camisa ____

Cristiano Ronaldo

7

05/02/1985

Leonel Messi

10

24/06/1987

Ronaldo Nazário

9

18/09/1976

Zinédine Zidane

5

23/06/1972

Manuel Neur

1

27/03/1986

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### Suprimir coluna de checkbox

Por padrão, o **EzGridView** exibe uma coluna de checkbox para seleção de linhas. Para que a mesma não seja exibida, basta definir a propriedade `suppressCheckboxColumn` como `true`.

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
import React, { useEffect } from 'react';
import { EzGridView } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  useEffect(() => {
  }, []);

  return (
    <div className="box">
      <EzGridView metadata={PLAYER_METADATA}
                  records={PLAYER_DATA}
                  suppressCheckboxColumn={true}
      />
    </div>
  );
};

export default Demo;

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
```

### Definir tamanho da página

A propriedade `pageSize` permite definir o número de registros exibidos por página.

> Por padrão, o valor do `pageSize` é `150`.

____

Nome ____

____

Dt. Nascimento ____

____

Nro. Camisa ____

Cristiano Ronaldo

05/02/1985

7

Lionel Messi

24/06/1987

10

Ronaldo Nazário

18/09/1976

9

Zinédine Zidane

23/06/1972

5

Manuel Neuer

27/03/1986

1

Neymar Jr.

05/02/1992

10

Kylian Mbappé

20/12/1998

7

Robert Lewandowski

21/08/1988

9

Luka Modrić

09/09/1985

10

Erling Haaland

21/07/2000

9

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### Seleção de múltiplos registros

Para habilitar a seleção de múltiplos registros, basta definir a propriedade `multipleSelection` como `true`.

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
import React, { useEffect } from 'react';
import { EzGridView } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  useEffect(() => {
  }, []);

  return (
    <div className="box">
      <EzGridView metadata={PLAYER_METADATA}
                  records={PLAYER_DATA}
                  multipleSelection={true}
      />
    </div>
  );
};

export default Demo;

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
```

### Modo de exibição do contador da paginação

A propriedade `paginationCounterMode` permite definir o modo de exibição do contador da paginação.

Informação

Opções disponíveis: `show`, `hidden` e `auto`.

Valor padrão: `auto`.

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
import { EzGridView, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const [mode, setMode] = useState('show');

  useEffect(() => {
  }, []);

  return (
    <div className="flex flex-col gap-2">
      <div className="flew-row gap-8">
        <EzButton label={`show`}
                  onClick={() => setMode('show')} variant={'primary'} />

        <EzButton label={`hidden`}
                  onClick={() => setMode('hidden')}/>
      </div>

      <br />

      <EzGridView metadata={PLAYER_METADATA}
                  records={PLAYER_DATA}
                  paginationCounterMode={mode}
      />
    </div>
  );
};

export default Demo;

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
```

### Suprimindo filtro de colunas

Para suprimir o filtro de colunas, basta definir a propriedade `suppressFilterColumn` como `true`. Dessa forma, ao clicar no menu de contexto de uma coluna, a opção de filtro não será exibida.

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

### Modo outilne

Altera visualmente as sombras e bordas do componente. Quando `false`, aplica o padrão de sombras ao componente (Utilizar quando for o elemento principal do layout). Quando `true`, aplica o padrão de outline ao componente (Utilizar quando estiver contido em outro elemento como um painel ou pop-up).

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
import { EzGridView, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const [outline, setOutline] = useState(true);

  useEffect(() => {
  }, []);

  return (
    <div className="flex flex-col gap-2">
      <EzButton label={`${outline ? 'Desabilitar' : 'Habilitar'} outline`}
                onClick={() => setOutline(!outline)} variant={"primary"}/>

      <br/>

      <EzGridView metadata={PLAYER_METADATA}
                  records={PLAYER_DATA}
                  outlineMode={outline}
      />
    </div>
  );
};

export default Demo;

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
```

### Linhas listradas

A propriedade `enableRowTableStriped` permite definir se as linhas do grid serão exibidas com um estilo listrado.

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

### Formato das datas

É possível definir o formato das datas exibidas no grid através da propriedade `recordDateFormat`.

Dica

A Propriedade `recordDateFormat` aceita as opções `DD_MM_YYYY` e `ISO` ou o _enum_ `RECORD_DATE_FORMAT` da biblioteca `@sankhyalabs/core`.

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
import React from 'react';
import { EzGridView } from '@sankhyalabs/ezui/react/components';
import { RECORD_DATE_FORMAT } from '@sankhyalabs/core';

const Demo = () => {

  return (
    <div className="flex flex-col gap-2">

      <EzGridView metadata={PLAYER_METADATA}
                  records={PLAYER_DATA}
                  recordDateFormat={RECORD_DATE_FORMAT.ISO}
      />
    </div>
  );
};

export default Demo;

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
```

## Métodos

Uma série de métodos são disponibilizados pelo **EzGridView** para manipulação e interação com o componente.

### Obter **DataUnit**

O método `getDataUnit` retorna o `DataUnit` associado ao componente, que contém os dados exibidos no grid.

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

**DataUnitName:**

### Recarregar os registros

Em alguns casos é necessário recarregar os registros exibidos na grade para que seja visível alterações realizadas, como por exemplo a adição de um formatador personalizado.

Para isso, o método `refresh` deve ser utilizado.

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
import React, { useEffect, useRef, useState } from 'react';
import { EzGridView, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const grid = useRef();

  async function refreshGrid() {
    await grid.current.refresh();
  }

  return (
    <div className="flex flex-col gap-2">
      <EzButton label={'Recarregar grade'}
                onClick={async () => await refreshGrid()} variant={'primary'} />

      <br />

      <EzGridView
        ref={grid}
        metadata={PLAYER_METADATA}
        records={PLAYER_DATA}
      />

      <br />

    </div>
  );
};

export default Demo;

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
```

### Obter registros selecionados

O método `getSelectedRecords` retorna um array com os registros selecionados na grade.

**Items selecionados:**[]

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

### Adicionar um formatador de coluna customizado

O método `addCustomValueFormatter` permite adicionar um formatador customizado para uma coluna específica. Para isso, é necessário informar o nome da coluna e a função formatadora que será aplicada aos valores dessa coluna.

Dica

A função formatadora deverá implementar a interface `ICustomFormatter`, que define o método `format` e o método `refreshSelectedRows`.:

```text
interface ICustomFormatter {
    format: (currentValue: any, column: EzGridColumn, recordId: string) => any;
    refreshSelectedRows: () => void;
}
```

Essa interface está disponível em `@sankhyalabs/ezui/dist/types/components/ez-grid/interfaces`

Atenção

O método `addCustomValueFormatter` por si só não recarrega os registros da grade, sendo necessário chamar o método `refresh` para que as alterações possam ser visualizadas.

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
import React, { useEffect, useRef, useState } from 'react';
import { EzGridView, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const grid = useRef();

  async function addCustomFormatter() {
    const customFormatter= {
      format: (currentValue, _column) => {
        return currentValue ? currentValue.toUpperCase() : '';
      },
      refreshSelectedRows: () => {
        console.log("refreshSelectedRows");
      }
    }

    await grid.current.addCustomValueFormatter('NAME', customFormatter);
    await grid.current.refresh();
  }

  return (
    <div className="flex flex-col gap-2">
      <EzButton label={'Adicionar formatador'}
                onClick={async () => await addCustomFormatter()} variant={'primary'} />

      <br />

      <EzGridView
        ref={grid}
        metadata={PLAYER_METADATA}
        records={PLAYER_DATA}
      />

      <br />

    </div>
  );
};

export default Demo;

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
```

### Remover um formatador de coluna customizado

O método `removeCustomValueFormatter` permite remover um formatador customizado previamente adicionado a uma coluna.

Atenção

Assim como o `addCustomValueFormatter`, o método `removeCustomValueFormatter` não recarrega os registros da grade automaticamente. Sendo asism, é necessário chamar o método `refresh` para que as alterações sejam visíveis.

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

### Adicionando um renderizador customizado

Com o método `addGridCustomRender` é possível alterar o elemento que é mostrado na coluna da grade, podendo criar um elemento customizado dependendo ou não dos valores anteriores.

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
import { EzButton, EzGridView } from '@sankhyalabs/ezui/react/components';
import React, { useRef } from 'react';
import { renderToString } from 'react-dom/server';

const Demo = () => {
    const ezGridRef = useRef(null);

    const setCustomElement = () => {
        const customRender = {
            getRenderElement: () => {
                const element = document.createElement('div');
                element.textContent = 'Esse é um elemento totalmente customizado!';
                return element;
            }
        };
        ezGridRef.current?.addGridCustomRender("ESTADO", customRender);
    }

    const setCustomElementString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const elemment = `<div class='ez-text--tertiary'>Utilizando string HTML: ${params.value}</div>`;
                return elemment;
            }
        };
        ezGridRef.current?.addGridCustomRender("ESTADO", customRender);
    }

    const setCustomElementReactString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const Element = <div className="ez-text--tertiary">Utilizando reactToString: {params.value}</div>
                return renderToString(Element);
            }
        };
        ezGridRef.current?.addGridCustomRender("ESTADO", customRender);
    }

    const editElement = () => {
        const customRender = {
            getRenderElement: (params) => {
                const element = params.currentRender;
                element.textContent = `Elemento editado: ${params.value}`;
                element.className = "ez-text--tertiary";
                return element;
            }
        };
        ezGridRef.current?.addGridCustomRender("ESTADO", customRender);
    }

    const cleanElement = () => {
        const customRender = {
            getRenderElement: () => { }
        };
        ezGridRef.current?.addGridCustomRender("ESTADO", customRender);
    }

    return (
        <div>
            <EzGridView
                ref={ezGridRef}
                metadata={METADATA}
                records={RECORDS}
                multipleSelection={true}
            >
                <div className='ez-flex ez-flex--wrap ez-padding--medium' slot="footer">
                    <EzButton  size="small" label="Exibir elemento nativo customizado" onClick={setCustomElement} className="ez-margin-top--medium" />
                    <EzButton  size="small" label="Exibir elemento em string customizado" onClick={setCustomElementString} className="ez-margin-top--medium" />
                    <EzButton  size="small" label="Exibir elemento utilizando o reactToString" onClick={setCustomElementReactString} className="ez-margin-top--medium" />
                    <EzButton  size="small" label="Exibir elemento editado" onClick={editElement} className="ez-margin-top--medium" />
                    <EzButton  size="small" label="Resetar elemento" onClick={cleanElement} className="ez-margin-top--medium" />
                </div>

            </EzGridView>
        </div>
    );
};

export default Demo;

const METADATA = {
    name: "exemplo.datagrid",
    label: "Exemplo data grid",
    fields: [
        {name: "ESTADO", label: "Estado", dataType: "TEXT"},
        {name: "CAPITAL", label: "Capital", dataType: "TEXT"},
        {name: "SIGLA", label: "Sigla", dataType: "TEXT"}
    ]
};

const RECORDS = [
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

### Adicionando item no menu de coluna

Utilize o método `addColumnMenuItem` para adicionar itens de menu em cada uma das colunas.

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

### Localizar coluna

O método `locateColumn` permite localizar uma coluna, tornando-a visível, mesmo que haja scroll na grade.

____

Nome ____

____

Nro. Camisa ____

Cristiano Ronaldo

7

Leonel Messi

10

Ronaldo Nazário

9

Zinédine Zidane

5

Manuel Neur

1

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

## Eventos

Seguem abaixo alguns exemplos de eventos que permitem interagir com o componente.

Dica

O **EzGridView** utiliza o **EzGrid** , portanto, todos os eventos disponíveis no **EzGrid** também estão disponíveis no **EzGridView**.

### Evento de seleção

O evento `ezSelectionChange` é disparado sempre que a seleção de registros na grade é alterada.

**Items selecionados:**[]

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
import React, { useEffect, useRef, useState } from 'react';
import { EzGridView, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const grid = useRef();
  const [selectedItems, setSelectedItems] = useState([]);

  function handleSelectionChange(event) {
    const {selection} = event.detail;
    setSelectedItems([...selection.map(i => i.NAME)]);
  }

  return (
    <div className="flex flex-col gap-2">
      <span className={'flew-row'}>
        <strong>Items selecionados:</strong>
        {JSON.stringify(selectedItems)}
      </span>

      <br />

      <EzGridView
        ref={grid}
        metadata={PLAYER_METADATA}
        records={PLAYER_DATA}
        multipleSelection
        onEzSelectionChange={handleSelectionChange}
      />
    </div>
  );
};

export default Demo;

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
```

### Evento de duplo clique em uma linha

O evento `ezDoubleClick` é disparado quando uma linha da grade é clicada duas vezes.

**Duplo clique no elemento:** ""

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

### Evento de mudança de estado das colunas

O evento `ezColumnStateChange` é disparado quando o estado de uma coluna é alterado, como por exemplo, quando uma coluna é ordenada ou filtrada.

**Alteração:** ""

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
import React, { useEffect, useRef, useState } from 'react';
import { EzGridView, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const grid = useRef();
  const [change, setChange] = useState("");

  function handleColumnStateChange(event) {
    setChange(event.detail.type);
  }

  return (
    <div className="flex flex-col gap-2">
      <span className={'flew-row'}>
        <strong>Alteração:</strong>
        {JSON.stringify(change)}
      </span>

      <br />

      <EzGridView
        ref={grid}
        metadata={PLAYER_METADATA}
        records={PLAYER_DATA}
        multipleSelection
        onEzColumnStateChange={handleColumnStateChange}
      />
    </div>
  );
};

export default Demo;

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
```

## Slots para elementos personalizados

O **EzGridView** permite a utilização de slots para adicionar elementos personalizados ao componente.

### Slot de rodapé

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

Slot com elemento personalizado no rodapé

demo.js

```jsx
import React, { useEffect } from 'react';
import { EzGridView } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  useEffect(() => {
  }, []);

  return (
    <div className="box">
      <EzGridView
        metadata={PLAYER_METADATA}
        records={PLAYER_DATA}>
        <div slot={"footer"} className={"slot-footer"}>
          <span>Slot com elemento personalizado no rodapé</span>
        </div>
      </EzGridView>
    </div>
  );
};

export default Demo;

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
```

### Slot de cabeçalho

Utilize o slot `leftButtons` para adicionar elementos personalizados ao cabeçalho do grade.

Dica

Pode ser utilizado para adicionar uma barra de ferramentas contendo botões de ação, como exportação de dados, filtros avançados, entre outros.

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

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| autoFocus | auto-focus | Define se a grid será focada ao ser carregada. | boolean | true |
| columnsConfig | -- | Configuração de exibição da grade. | ColumnConfig[] | undefined |
| compact | compact | Define se a grade deve ser exibida em modo compacto | boolean | false |
| enableRowTableStriped | enable-row-table-striped | Ativa modo de linhas com cores alternadas. | boolean | true |
| metadata | -- | Metadados que definem a estrutura da grade. | UnitMetadata | undefined |
| multipleSelection | multiple-selection | Habilita a seleção de várias linhas. | boolean | false |
| outlineMode | outline-mode | Altera visualmente as sombras e bordas do componente Quando false, aplica o padrão de sombras ao componente (Utilizar quando for o elemento principal do layout) Quando true, aplica o padrão de outline ao componente (Utilizar quando estiver contido em outro elemento como um painel ou pop-up) | boolean | false |
| pageSize | page-size | Quantidade de registros por página. | number | 150 |
| paginationCounterMode | pagination-counter-mode | Define a forma como a paginação irá se comportar. | "auto" \| "hidden" \| "show" | 'auto' |
| recordDateFormat | record-date-format | Formato dos campos data dos registros. | RECORD_DATE_FORMAT.DD_MM_YYYY \| RECORD_DATE_FORMAT.ISO | RECORD_DATE_FORMAT.DD_MM_YYYY |
| records | -- | Registros a serem exibidos na grade. | Record[] | undefined |
| suppressCheckboxColumn | suppress-checkbox-column | Informa se a coluna de chechbox deve ser suprimida | boolean | false |
| suppressFilterColumn | suppress-filter-column | Informa se a grade deve suprimir o filtro de coluna. | boolean | false |
| suppressHorizontalScroll | suppress-horizontal-scroll | Define se a grade deve suprimir o scroll horizontal. | boolean | false |
| useSearchColumn | use-search-column | Define se a grade deve exibir um buscador de coluna com uso do Ctrl+F | boolean | true |

### Methods

#### `addColumnMenuItem(label: string, name: string, action: Function, icon: HTMLElement | string) => Promise<void>`

Adiciona item de menu nas colunas.

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

#### `filterColumns(search: string) => Promise<Array<EzGridColumn>>`

Usa um argumento para filtrar as colunas por label

##### Returns

Type: `Promise<EzGridColumn[]>`

#### `getDataUnit() => Promise<DataUnit>`

Obtém o DataUnit da grade.

##### Returns

Type: `Promise<DataUnit>`

#### `getSelection() => Promise<Array<any>>`

Obtém as linhas selecionadas.

##### Returns

Type: `Promise<any[]>`

#### `locateColumn(columnName: string) => Promise<void>`

Localiza determinada coluna tornando-a visível.

##### Returns

Type: `Promise<void>`

#### `quickFilter(term: string) => Promise<void>`

Aplica um filtro rápido.

##### Returns

Type: `Promise<void>`

#### `refresh() => Promise<void>`

Recarrega os registros da grade.

##### Returns

Type: `Promise<void>`

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

Remove o formatador de valores de uma coluna da grid.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Atribui o foco para a grade.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-grid
