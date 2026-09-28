> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-panel/ (snapshot 2026-09-28)

# Split Panel

## Painel

O componente `SplitPanel` é um painel com múltiplas divisões internas, onde cada divisão pode ser redimensionada individualmente pelo usuário. O objetivo desse painel é receber outros componentes e permitir um layout mais dinâmico.

```
{}
```

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

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

demo.js

```jsx
import { EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React from "react";
import EzGridDemo from "./grid/demo-grid";

import EzFormDemo from "../ez-form/demo";
import EzListDemo from "../ez-list/demo";

const Demo = () => {
  return (
    <div
      style={{
        height: "400px",
      }}
    >
      <EzSplitPanel direction="column" anchorToExpand>
        <EzSplitItem enable-expand="false" size="2fr">
          <EzSplitPanel direction="row">
            <EzSplitItem>
              <EzFormDemo />
            </EzSplitItem>
            <EzSplitItem>
              <EzGridDemo />
            </EzSplitItem>
          </EzSplitPanel>
        </EzSplitItem>
        <EzSplitItem>
          <EzListDemo />
        </EzSplitItem>
      </EzSplitPanel>
    </div>
  );
};

export default Demo;
```

### Direção de itens

A propriedade `direction` define qual será o sentido que o painel será divido.

#### Column

Classificados

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

Não classificados

* Michael Bloomberg

* Mark Zuckerberg

* Larry Page

* Larry Ellison

* Amancio Ortega

Mover para Não classificados

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

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

#### Row

```
{}
```

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

demo.js

```jsx
import { EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React from "react";
import EzFormDemo from "../ez-form/demo";

import EzListDemo from "../ez-list/demo";

const Demo = () => {
  return (
    <div
      style={{
        height: "500px",
      }}
    >
      <EzSplitPanel direction="row" anchorToExpand>
        <EzSplitItem>
          <EzFormDemo />
        </EzSplitItem>
        <EzSplitItem>
          <EzListDemo />
        </EzSplitItem>
      </EzSplitPanel>
    </div>
  );
};

export default Demo;
```

### Definir âncora para expandir item

Por padrão, cada divisão pode ser expandida. A propriedade `anchorToExpand` no `EzSplitPanel` irá definir que esse elemento é o limite para o item filho expandir, caso não seja passada nenhuma âncora, o item será expandido para a primeira posição relativa que encontrar

#### Sem âncora

```
{}
```

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

#### Com âncora

```
{}
```

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

demo.js

```jsx
import { EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React from "react";
import EzGridDemo from "./grid/demo-grid";

import EzFormDemo from "../ez-form/demo";

const Demo = () => {
  return (
    <div
      style={{
        display: "flex",
        position: "relative",
        flexDirection: "column",
        gap: "1rem",
      }}
    >
      <h4>Sem âncora</h4>
      <div
        style={{
          height: "300px",
        }}
      >
        <EzSplitPanel>
          <EzSplitItem>
            <EzFormDemo />
          </EzSplitItem>
          <EzSplitItem>
            <EzGridDemo />
          </EzSplitItem>
        </EzSplitPanel>
      </div>
      <h4>Com âncora</h4>
      <div
        style={{
          height: "300px",
        }}
      >
        <EzSplitPanel anchorToExpand>
          <EzSplitItem>
            <EzFormDemo />
          </EzSplitItem>
          <EzSplitItem>
            <EzGridDemo />
          </EzSplitItem>
        </EzSplitPanel>
      </div>
    </div>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| anchorToExpand | anchor-to-expand | Responsável por definir o painel que limita o tamanho do item expandido. | boolean | false |
| direction | direction |  | "column" \| "row" | 'column' |
| structural | structural | Define se o painel está sendo utilizado como estrutura para apresentação de outro item | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| resizeEnd |  | CustomEvent<IPanelSizeInfo> |

### Methods

#### `rebuildLayout() => Promise<void>`

##### Returns

Type: `Promise<void>`

## Item

Cada `EzSplitItem` representa uma divisão do painel e pode ter seu tamanho ajustado pelo usuário através de um controle visual intuitivo.

```
{}
```

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

### Título

Os items podem receber títulos através da propriedade `label`.

### Painel com EzList

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

### Painel com EzGrid

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

Rio de Janeiro

Rio de Janeiro

RJ

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import { EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React from "react";
import EzListDemo from "../../ez-list/demo";
import EzGridDemo from "../grid/demo-grid";

const Demo = () => {
  return (
    <div
      style={{
        height: "400px",
      }}
    >
      <EzSplitPanel direction="column" anchorToExpand>
        <EzSplitItem label="Painel com EzList">
          <EzListDemo />
        </EzSplitItem>
        <EzSplitItem label="Painel com EzGrid">
          <EzGridDemo />
        </EzSplitItem>
      </EzSplitPanel>
    </div>
  );
};

export default Demo;
```

### Slot à esquerda do título

Podemos adicionar um conteudo dinâmico à esquerda do título, passando o slot `leftButtons`.

observação

À medida que largura da tela for diminuindo e e o titulo for muito grande, é adicionado "..." ao título.

### Painel com conteudo dinamico à esquerda

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

### Painel com EzGrid

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

Rio de Janeiro

Rio de Janeiro

RJ

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### Slot à direita do título

Podemos adicionar um conteudo dinâmico à esquerda do título, passando o slot `rightButtons`.

observação

À medida que largura da tela for diminuindo e e o titulo for muito grande, é adicionado "..." ao título.

### Painel com conteudo dinamico à direita

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

### Painel com EzGrid

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

Rio de Janeiro

Rio de Janeiro

RJ

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

demo.js

```jsx
import { EzBadge, EzButton, EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React from "react";
import EzListDemo from "../../ez-list/demo";
import EzGridDemo from "../grid/demo-grid";

const Demo = () => {
  return (
    <div
      style={{
        height: "400px",
      }}
    >
      <EzSplitPanel direction="column" anchorToExpand>
        <EzSplitItem label="Painel com conteudo dinamico à direita">
          <EzListDemo />
          <div slot="rightButtons">
            <div className="ez-flex ez-flex--align-items-center ez-margin-right--small">
              <EzBadge label="Conteúdo aleatório" size="medium" className="ez-badge--primary-subtle" />
            </div>
          </div>
        </EzSplitItem>
        <EzSplitItem label="Painel com EzGrid">
          <EzGridDemo />
          <div slot="rightButtons">
            <div className="ez-flex ez-flex--align-items-center ez-margin-right--small">
              <EzBadge label="Conteúdo aleatório" size="medium" className="ez-badge--error-subtle" />
              <EzButton mode="icon" iconName="arrow-forward" size="small" className="ez-margin-left--small" />
            </div>
          </div>
        </EzSplitItem>
      </EzSplitPanel>
    </div>
  );
};

export default Demo;
```

### Habilitar expansão

A propriedade `enableExpand` define se o componente pode ser expandido

### Não expande

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

Rio de Janeiro

Rio de Janeiro

RJ

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### Expande

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

Rio de Janeiro

Rio de Janeiro

RJ

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

### Tamanho inicial

A propriedade `size` define o espaço que o item irá ocupar no painel. Ela pode ser definida através das medidas `fr` e `%`

#### Usando `fr`

```
{}
```

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

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

demo.js

```jsx
import { EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React from "react";
import EzGridDemo from "./../grid/demo-grid";

import EzFormDemo from "../../ez-form/demo";
import EzListDemo from "../../ez-list/demo";

const Demo = () => {
  return (
    <div
      style={{
        height: "400px",
      }}
    >
      <EzSplitPanel direction="column" anchorToExpand>
        <EzSplitItem enable-expand="false" size="3fr">
          <EzSplitPanel direction="row">
            <EzSplitItem size="3fr">
              <EzFormDemo />
            </EzSplitItem>
            <EzSplitItem size="2fr">
              <EzGridDemo />
            </EzSplitItem>
          </EzSplitPanel>
        </EzSplitItem>
        <EzSplitItem>
          <EzListDemo />
        </EzSplitItem>
      </EzSplitPanel>
    </div>
  );
};

export default Demo;
```

#### Usando `%`

```
{}
```

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

ez-grid.remainingTotalLabel ez-grid.remainingTotalLabel

Página {{currentPage}} ez-grid.remainingTotalLabel

Filtro da coluna

Selecione os valores a serem filtrados através do campo de busca.

Há **registro** selecionado na grade.

* Jeff Bezos

* Bill Gates

* Warren Buffett

* Bernard Arnault

* Carlos Slim Helu

* Amancio Ortega

* Larry Ellison

* Mark Zuckerberg

* Michael Bloomberg

* Larry Page

### Exemplos de eventos.

#### Evento emitido ao redimensionar o painel.

#### ID: panel_item_one - Width: 100px - Height: 50px

#### ID: panel_item_two - Width: 100px - Height: 50px

demo.js

```jsx
import { EzSplitItem, EzSplitPanel } from "@sankhyalabs/ezui/react/components";
import React, { useState } from "react";

const PANEL_ITEM_ONE = "panel_item_one";
const PANEL_ITEM_TWO = "panel_item_two";

const Demo = () => {

  const [panelSizeInfo, setPanelSizeInfo] = useState({items: [
    {
      id: PANEL_ITEM_ONE,
      width: 100,
      height: 50
    },
    {
      id: PANEL_ITEM_TWO,
      width: 100,
      height: 50
    }
  ]});

  const handleResizeEnd = (event) => {
    setPanelSizeInfo(event.detail);
  };

  const buildInfo = (panelItemId) => {
    const item = panelSizeInfo.items.find(item => item.id === panelItemId);
    return `ID: ${item.id} - Width: ${item.width}px - Height: ${item.height}px`;
  };

  return (
    <div
      style={{
        height: "400px",
      }}
    >
      <EzSplitPanel id="rootPanel" direction="row" anchorToExpand onResizeEnd={handleResizeEnd}>
        <EzSplitItem id={PANEL_ITEM_ONE} enable-expand="false" >
          <h4>{buildInfo(PANEL_ITEM_ONE)}</h4>
        </EzSplitItem>
        <EzSplitItem id={PANEL_ITEM_TWO} enable-expand="false">
          <h4>{buildInfo(PANEL_ITEM_TWO)}</h4>
        </EzSplitItem>
      </EzSplitPanel>
    </div>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| enableExpand | enable-expand | Define se o item pode ser expandido | boolean | true |
| label | label | Define um título para o painel. | string | undefined |
| size | size | Define o tamanho inicial do painel. | string | undefined |
| structural | structural | Define se o painel está sendo utilizado como estrutura para apresentação de outro item | boolean | false |

### Dependencies

#### Depends on

  * ez-button
