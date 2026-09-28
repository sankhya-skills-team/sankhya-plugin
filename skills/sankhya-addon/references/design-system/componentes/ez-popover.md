> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover/ (snapshot 2026-09-28)

# Popover

Qualquer conteúdo HTML é aceito.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzButton, EzPopover } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const popover = useRef();

    const showPopover = ()=>{
        popover.current.show();
    };

    return (
        <div>
            <div className="ez-row">
                <EzButton label="Mostrar popover" onClick={() => showPopover()} />
            </div>
            <EzPopover ref={popover}>
                <div className="ez-padding--large">
                    <label>Qualquer conteúdo HTML é aceito.</label>
                </div>
            </EzPopover>
        </div>
    )
};

export default Demo;
```

## Controle de exibição

O controle de exibição do componente é feito através de dois métodos e um atributo:

  * show() faz com o que seja exibido.
  * hide() oculta o elemento.
  * Além disso, caso o usuário clique em algum lugar fora do conteúdo o faz ocultar automaticamente. Isso pode ser desligado pela flag "autoClose".

Observação

É necessário definir o parâmetro `overlayType` com valor **none**. Uma vez que, tendo o `overlayType` ligado o `autoClose` por regra também será ligado.

Se clicar fora o popover fecha

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzPopover, EzCheck } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const popover = useRef();
    const [autoClose, setAutoClose] = useState(true);

    const showPopover = ()=>{
        popover.current.show();
    };

    const closePoppover = ()=>{
        popover.current.hide();
    };

    const updateAutoClose = value => {
        setAutoClose(value);
        closePoppover();
    }

    return (
        <div>
            <div className="ez-row">
                <EzButton label="Mostrar popover" onClick={() => showPopover()}/>
                <EzButton label="Ocultar popover" onClick={() => closePoppover()}/>
                <EzCheck
                    label="autoClose"
                    value={autoClose}
                    onEzChange={evt=>updateAutoClose(evt.target.value)}
                />
            </div>
            <EzPopover overlayType="none" ref={popover} autoClose={autoClose}>
                <div className="ez-padding--large">
                    <label>{autoClose ? "Se clicar fora o popover fecha" : "Só fecha quando clicar no botão ocultar"}</label>
                </div>
            </EzPopover>
        </div>
    )
};

export default Demo;
```

## Controle de sobreposição

Por padrão, o popover é exibido acima de outros elementos com uma sobreposição/overlay, essa sobreposição é controlada pela propriedade `overlayType`. Caso a propriedade `autoClose` esteja desligada e a propriedade `overlayType` seja diferente de `none`, o componente irá desconsiderar o valor de `autoClose` e sempre fechará o popover ao clicar fora do conteúdo.

Qualquer conteúdo HTML é aceito.

## Demonstrando o valor de opened

Sempre que os métodos "show" e "hide" são chamados, um evento "ezVisibilityChange" é disparado.
Usando esse evento juntamente com a propriedade "opened", é possível reagir à abertura e fechamento do componente:

Popover **Fechado**

Qualquer conteúdo HTML é aceito.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzPopover } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const popover = useRef();
    const [opened, setOpened] = useState(false);

    const showPopover = ()=>{
        popover.current.show();
    };

    const closePoppover = ()=>{
        popover.current.hide();
    };

    const updateOpened = value => {
        setOpened(value);
    }

    return (
        <div>
            <div className="ez-row ez-flex--align-items-center">
                <EzButton label="Mostrar popover" onClick={() => showPopover()} />
                <EzButton label="Ocultar popover" onClick={() => closePoppover()}/>
            </div>
            <label className="ez-flex ez-padding-top--small">Popover&nbsp;<strong>{opened ? "Aberto" : "Fechado"}</strong></label>
            <EzPopover
                overlayType="none"
                ref={popover}
                onEzVisibilityChange={evt => updateOpened(evt.target.opened)}
                autoClose={false}
            >
                <div className="ez-padding--large">
                    <label>Qualquer conteúdo HTML é aceito.</label>
                </div>
            </EzPopover>
        </div>
    )
};

export default Demo;
```

## Usando largura total

Usa toda a largura disponível.

## Abrindo abaixo de um elemento

É possível determinar que o popover se posicione no canto inferior esquerdo de um elemento HTML, por exemplo um botão.
Para isso é necessário usar o método "showUnder" ao invés do "show", sendo necessário informar o elemento de referência.
Também é possível determinar o posicionamento a partir do canto direito ao invés do esquerdo.
Há ainda a opção de informar algum deslocamento horizontal e/ou vertical.

Abrindo da **esquerda para a direita**

Deslocamento vertical: **10 pixels**

Deslocamento horizontal: **0 pixels**

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzCheck, EzButton, EzPopover, EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const popover = useRef();

    const [fromRight, setfromRight] = useState(false);
    const [verticalGap, setVerticalGap] = useState(10);
    const [horizontalGap, setHorizontalGap] = useState(0);

    const show = (target)=>{
        const options = {
            horizontalGap: horizontalGap,
            verticalGap: verticalGap,
            fromRight: fromRight
        };
        popover.current.showUnder(target, options);
    };

    return (
        <div>
            <EzCheck
                label="À Direita"
                value={fromRight}
                onEzChange={evt => setfromRight(evt.detail)}
            />
            <EzNumberInput
                label="Deslocamento vertical (pixels)"
                value={verticalGap}
                onEzChange={evt => setVerticalGap(evt.detail)}
            />
            <EzNumberInput
                label="Deslocamento Horizontal (pixels)"
                value={horizontalGap}
                onEzChange={evt => setHorizontalGap(evt.detail)}
            />
            <div className={"ez-row" + (fromRight ? " ez-flex--justify-end" : "")}>
                <EzButton label="Botão 1" onClick={(event) => show(event.target)}/>
                <EzButton label="Botão 2" onClick={(event) => show(event.target)}/>
                <EzButton label="Botão 3" onClick={(event) => show(event.target)}/>
                <EzButton label="Botão 4" onClick={(event) => show(event.target)}/>
            </div>
            <EzPopover overlayType="none" ref={popover}>
                <div className="ez-padding--large">
                    <div>Abrindo da <b>{fromRight ? "direita para a esquerda" : "esquerda para a direita"}</b></div>
                    <div>Deslocamento vertical: <b>{verticalGap||0} pixels</b></div>
                    <div>Deslocamento horizontal: <b>{horizontalGap||0} pixels</b></div>
                </div>
            </EzPopover>
        </div>
    )
};

export default Demo;
```

## Alterando a posição do popover

Pocisionamente em relação ao pai.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| autoClose | auto-close | Define que será fechado automaticamente quando o usuário clicar fora do conteúdo. | boolean | true |
| boxWidth | box-width | Ajusta o comportamento da largura do popover. | "fit-content" \| "full-width" | "fit-content" |
| innerElement | inner-element | Define as tags que serão consideradas conteúdo. | string \| string[] | undefined |
| opened | opened | Define se o ez-popover está aberto. | boolean | undefined |
| overlayType | overlay-type | Define o tipo de overlay do popover. | "light" \| "medium" \| "none" | "light" |

### Events

| Event | Description | Type |
|---|---|---|
| ezVisibilityChange | Emitido quando acontece a alteração de estado do componente. | CustomEvent<boolean> |

### Methods

#### `hide() => Promise<void>`

Oculta o ez-popover.

##### Returns

Type: `Promise<void>`

#### `show(top?: string, left?: string) => Promise<void>`

Exibe o ez-popover.

##### Returns

Type: `Promise<void>`

#### `showAbove(offsets?: { bottom?: string; left?: string; right?: string; }) => Promise<void>`

Exibe o ez-popover ancorado acima da posição de origem (usa `bottom` em vez de `top`). Aceita opcionalmente `left` ou `right` para alinhamento horizontal.

##### Returns

Type: `Promise<void>`

#### `showUnder(element: HTMLElement, options?: IEzPopoverAnchorOptions) => Promise<void>`

Ancora a exibição do popOver a um elemento HTML.

##### Returns

Type: `Promise<void>`

#### `updatePosition(top?: string, left?: string) => Promise<void>`

Atualiza a posição do popover.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form
  * ez-grid
  * ez-grid-pagination

### CSS Variables

| Variable | Description |
|---|---|
| --ez-popover__box--border-radius | Define o raio da borda do popover. |
| --ez-popover__box--box-shadow | Define a sombra do popover. |
| --ez-popover__box--background-color | Define a cor de fundo do popover. |
| --ez-popover__box--z-index | Define a camada de visibilidade do popover. |
