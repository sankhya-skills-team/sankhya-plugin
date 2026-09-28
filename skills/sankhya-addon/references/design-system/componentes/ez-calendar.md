> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-calendar/ (snapshot 2026-09-28)

# Calendar

Documentação do componente EzCalendar.

demo.js

```jsx
import React from 'react';
import { EzCalendar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCalendar></EzCalendar>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Com horas e minutos

Exibe as horas e minutos no calendário.

demo.js

```jsx
import React from 'react';
import { EzCalendar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCalendar time="true"></EzCalendar>
        </div>
    )
};

export default Demo;
```

### Com segundos

Exibe os segundos no calendário.

### Modo floating

No modo floating o calendário só se tornará visível quando o método show() for acionado.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzCalendar, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const onShow = () => {
        element.current.show();
    };

    return (
        <div className="ez-flex ez-flex--column ez-flex--align-items-center">
            <EzCalendar ref={element} floating="true"></EzCalendar>

            <EzButton
                label="Mostrar Calendário"
                onClick={onShow}
            >
            </EzButton>
        </div>
    )
};

export default Demo;
```

### Principais métodos

#### show()

Faz com que o componente seja exibido quando utilizado no modo floating.

É possível determinar ajustes de posicionamento através dos parâmetros:

  * top;
  * left;
  * bottom;
  * right.

Esses parâmetros devem ser informados como strings no formato css.

#### fitVertical()

Usado no modo floating. Método necessário para ajustar o posicionamento do calendar acima ou abaixo do elemento pai conforme a disponibilidade de espaço.

É possível determinar ajustes de posicionamento através dos parâmetros:

  * topOffset;
  * bottomOffset.

Esses parâmetros devem ser informados como number.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzCalendar, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const onShow = () => {
        element.current.fitVertical(47, 5); // topOffset: 47, bottomOffset: 5
    };

    return (
        <div className="ez-flex ez-flex--column ez-flex--align-items-center">
            <EzCalendar ref={element} floating="true"></EzCalendar>

            <EzButton
                label="Mostrar Calendário"
                onClick={onShow}
            >
            </EzButton>
        </div>
    )
};

export default Demo;
```

#### hide()

Faz com que o componente seja ocultado quando utilizado no modo floating.

Observação

No exemplo abaixo, ao clicar no botão **Mostrar Calendário** , o calendário será exibido, após 2 segundos será chamado o médodo **hide()** , e então ele será ocultado automaticamente.

### Exemplos de eventos

#### ezChange()

Quando o usuário escolhe uma data, esse evento é emitido.

Valor: **Mon Sep 28 2026 14:25:28 GMT-0300 (Horário Padrão de Brasília)**

demo.js

```jsx
import React, { useState } from "react";
import { EzCalendar } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  const [newValue, setNewValue] = useState(new Date());

  return (
    <div className="ez-flex ez-flex--column ez-flex--align-items-center">
      <EzCalendar value={newValue} onEzChange={evt => setNewValue(evt.detail)}></EzCalendar>

      <label className="ez-margin-top--large">
        Valor: <strong>{newValue.toString()}</strong>
      </label>
    </div>
  )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| floating | floating | Define se a exibição do ez-calendar será feita pelos métodos show() e hide() . | boolean | false |
| showSeconds | show-seconds | Se true a data considera segundos. Deve ser usado em conjunto com a propriedade time . | boolean | false |
| time | time | Se true a data considera horas e minutos. | boolean | false |
| value | -- | Define o valor do calendário. | Date | new Date() |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do calendário. | CustomEvent<Date> |

### Methods

#### `fitHorizontal(rightOffset: number) => Promise<void>`

Ajusta o posicionamento horizontal do ez-calendar conforme a disponibilidade de espaço.

##### Returns

Type: `Promise<void>`

#### `fitVertical(topOffset: number, bottomOffset: number) => Promise<void>`

Ajusta o posicionamento vertical do ez-calendar conforme a disponibilidade de espaço.

##### Returns

Type: `Promise<void>`

#### `hide() => Promise<void>`

Oculta o ez-calendar.

##### Returns

Type: `Promise<void>`

#### `show(top?: string, left?: string, bottom?: string, right?: string) => Promise<void>`

Exibe o ez-calendar em uma posição determinada. É possível determinar o posicionamento através dos parâmetros, no formato css.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-classic-date-input
  * ez-classic-date-time-input
  * ez-date-input
  * ez-date-time-input

### CSS Variables

| Variable | Description |
|---|---|
| --ez-calendar--font-family | Define a família da fonte do componente. |
| --ez-calendar--color | Define a cor dos textos dentro do componente. |
| --ez-calendar--text-shadow | Define a sombra dos textos dentro do componente. |
| --ez-calendar__body--background-color | Define a cor de fundo do corpo do calendário. |
| --ez-calendar__time--background-color | Define a cor de fundo do corpo da hora do calendário. |
| --ez-calendar__body--padding | Define o espaçamento do corpo do calendário. |
| --ez-calendar__body--border-radius | Define o raio da borda do corpo do calendário. |
| --ez-calendar__body--shadow | Define a sombra do corpo do calendário. |
| --ez-container--z-index | Define a posição do container de calendario nas camadas da página . |
| --ez-calendar__header-line--stroke | Define a espessura da borda inferior do header. |
| --ez-calendar__header-line--color | Define a cor da borda inferior do header. |
| --ez-calendar__nav-btn--fill | Define a cor do ícone de navegação. |
| --ez-calendar__nav-btn--hover--fill | Define a cor do ícone de navegação quando o cursor está sobre ele. |
| --ez-calendar__nav-btn--width | Define a largura do ícone de navegação. |
| --ez-calendar__nav-btn--height | Define a altura do ícone de navegação. |
| --ez-calendar__nav-btn--previous-image | Contém a imagem do ícone de navegação à esquerda. |
| --ez-calendar__nav-btn--next-image | Contém a imagem do ícone de navegação à direita. |
| --ez-calendar__cell--margin | Define o espaçamento vertical entre as células. |
| --ez-calendar__cell--width | Define a largura das células. |
| --ez-calendar__cell--padding | Define o espaçamento horizontal entre as células. |
| --ez-calendar__cell--border-radius | Define o raio da borda das células. |
| --ez-calendar__cell--over--background-color | Define a cor de fundo das células. |
| --ez-calendar__cell--over--color | Define a cor de do texto das células. |
| --ez-calendar__cell--outset--color | Define a cor do texto para células secundárias (fora do mês selecionado). |
| --ez-calendar__cell--selected--background-color | Define a cor de fundo das células selecionadas. |
| --ez-calendar__cell--selected--color | Define a cor do texto da célula selecionada. |
| --ez-calendar__btn-today--color | Define a cor do texto do botão "Hoje". |
| --ez-calendar__btn-today--hover--background-color | Define a cor de fundo do botão "Hoje" quando o cursor está sobre ele. |
| --ez-calendar__btn-today--border-radius | Define o raio da borda do botão "Hoje". |
