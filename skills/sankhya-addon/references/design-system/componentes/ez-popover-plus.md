> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/ (snapshot 2026-09-28)

# Popover Plus

O Popover é um componente utilizado para exibir informações contextuais em uma sobreposição leve e discreta em relação ao conteúdo principal. Ele pode conter texto, botões ou outros elementos interativos e geralmente é ativado por ações do usuário, como clique ou foco.

Atenção

Caso o conteúdo do componente tenha arquivos de estilização próprios, é necessário que o conteúdo seja separado em um componente individual antes de ser utilizado.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam consectetur ante lectus, sed ullamcorper libero venenatis quis. Morbi ac viverra risus, sit amet efficitur ligula. Sed cursus est diam, faucibus venenatis ligula maximus eu. Etiam feugiat quam ac velit gravida rutrum.

demo.js

```jsx
import React, { useCallback, useEffect, useRef } from 'react';
import { EzButton, EzPopoverPlus } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const button = useRef();
    const popover = useRef();

    function showPopover() {
        popover.current.showUnder(button.current);
    }

    return (
        <>
            <div className="ez-row">
                <EzButton ref={button} label="Mostrar popover" onClick={() => showPopover()} />
            </div>
           <EzPopoverPlus ref={popover} useAnchorSize={true} minWidth={300}>
                <div className="ez-padding--medium">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam consectetur ante
                    lectus, sed ullamcorper libero venenatis quis. Morbi ac viverra risus, sit amet
                    efficitur ligula. Sed cursus est diam, faucibus venenatis ligula maximus eu. Etiam
                    feugiat quam ac velit gravida rutrum.
                </div>
           </EzPopoverPlus>
        </>
    )
};

export default Demo;
```

## Controle de exibição

O componente possui três métodos principais:

  * `show()`: Exibe o popover.
  * `showUnder(elemento)`: Exibe o popover abaixo do elemento especificado.
  * `hide()`: Oculta o popover.

E uma propriedade de controle:

  * `opened`: Controla o estado de visibilidade do componente.

Além disso, caso o usuário clique em algum lugar fora do conteúdo o faz ocultar automaticamente. Isso pode ser desligado pela flag "autoClose".

Observação

É necessário definir o parâmetro `overlayType` com valor **none**. Uma vez que, tendo o `overlayType` ligado o `autoClose` por regra também será ligado.

Se clicar fora o popover fecha

Só fecha quando clicar no botão ocultar

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzPopoverPlus, EzCheck } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const popoverAutoClose = useRef();
    const buttonAutoClose = useRef();

    const button = useRef();
    const popover = useRef();

    function showPopoverAutoClose() {
        popoverAutoClose.current.showUnder(buttonAutoClose.current);
    };

    function showPopover() {
        popover.current.showUnder(button.current);
    };

    function closePoppover() {
        popover.current.hide();
    };

    return (
        <div>
            <div className="ez-row ez-flex ez-flex--justify-between">
                <EzButton
                    ref={buttonAutoClose}
                    className="ez-padding--small"
                    label="Mostrar popover com autoClose"
                    onClick={() => showPopoverAutoClose()}
                />
                <div className='ez-flex'>
                    <EzButton
                        ref={button}
                        className="ez-padding--small"
                        label="Mostrar popover sem autoClose"
                        onClick={() => showPopover()}
                    />
                    <EzButton
                        className="ez-padding--small"
                        label="Ocultar popover"
                        onClick={() => closePoppover()}
                    />
                </div>
            </div>
            <EzPopoverPlus overlayType="none" ref={popoverAutoClose} autoClose={true}>
                <div className="ez-padding--medium">
                    <label>Se clicar fora o popover fecha</label>
                </div>
            </EzPopoverPlus>
            <EzPopoverPlus overlayType="none" ref={popover} autoClose={false}>
                <div className="ez-padding--medium">
                    <label>Só fecha quando clicar no botão ocultar</label>
                </div>
            </EzPopoverPlus>
        </div>
    )
};

export default Demo;
```

## Ancoragem de elementos

Para um bom funcionamento do componente, é necessário termos definido um elemento de ancoragem. Para isso, temos algumas estratégias.

### Método showUnder

Este método simplifica o processo de abertura ao permitir a passagem do elemento de ancoragem no momento da exibição do Popover. Isso elimina a necessidade de configurar previamente o componente. Como o elemento de ancoragem só é utilizado no momento da abertura, essa abordagem resolve problemas relacionados à falta de referência durante a renderização inicial e é a **estratégia recomendada**.

Exemplo

### Propriedade anchorElement

Esta propriedade permite especificar o elemento que serve como ponto de referência para o posicionamento do Popover. Ela pode ser configurada com uma referência ao elemento (HTMLElement), com seu identificador único (string) ou com um array contendo múltiplos elementos ou IDs. Quando um array é usado, o Popover será posicionado em relação ao primeiro elemento válido encontrado na lista. Isso é útil para cenários onde múltiplos pontos de ancoragem são possíveis.

### Método setAnchorElement

Este método permite configurar o elemento de referência para o posicionamento do Popover. Sendo necessário ser feito antes do momento de abertura do componente, se tornando uma estratégia para casos onde o elemento de ancoragem são renderizados de forma condicional por exemplo.

## Controle de sobreposição

Por padrão, o popover é exibido acima de outros elementos com uma sobreposição/overlay, essa sobreposição é controlada pela propriedade `overlayType`. Caso a propriedade `autoClose` esteja desligada e a propriedade `overlayType` seja diferente de `none`, o componente irá desconsiderar o valor de `autoClose` e sempre fechará o popover ao clicar fora do conteúdo.

Qualquer conteúdo HTML é aceito.

Qualquer conteúdo HTML é aceito.

## Demonstrando o valor de opened

Sempre que os métodos "show" e "hide" são chamados, um evento "ezVisibilityChange" é disparado.
Usando esse evento juntamente com a propriedade "opened", é possível reagir à abertura e fechamento do componente:

Popover **Fechado**

Qualquer conteúdo HTML é aceito.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzPopoverPlus } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const popover = useRef();
    const labelStatus = useRef();
    const [opened, setOpened] = useState(false);

    function showPopover() {
        popover.current.showUnder(labelStatus.current);
    };

    function closePoppover() {
        popover.current.hide();
    };

    function updateOpened(value) {
        setOpened(value);
    }

    return (
        <div>
            <div className="ez-row ez-flex--align-items-center">
                <EzButton
                    label="Mostrar popover"
                    onClick={() => showPopover()}
                />
                <EzButton
                    label="Ocultar popover"
                    onClick={() => closePoppover()}
                />
            </div>
            <label
                ref={labelStatus}
                className="ez-flex ez-padding-top--small"
            >
                Popover&nbsp;<strong>{opened ? "Aberto" : "Fechado"}</strong>
            </label>
            <EzPopoverPlus
                ref={popover}
                overlayType="none"
                autoClose={false}
                onEzVisibilityChange={({detail}) => {
                    updateOpened(detail);
                }}
            >
                <div className="ez-padding--large">
                    <label>Qualquer conteúdo HTML é aceito.</label>
                </div>
            </EzPopoverPlus>
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
import { EzCheck, EzButton, EzPopoverPlus, EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const popover = useRef();

    const [fromRight, setfromRight] = useState(false);
    const [verticalGap, setVerticalGap] = useState(10);
    const [horizontalGap, setHorizontalGap] = useState(0);

    function show(target) {
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
            <EzPopoverPlus overlayType="none" ref={popover}>
                <div className="ez-padding--large">
                    <div>Abrindo da <b>{fromRight ? "direita para a esquerda" : "esquerda para a direita"}</b></div>
                    <div>Deslocamento vertical: <b>{verticalGap||0} pixels</b></div>
                    <div>Deslocamento horizontal: <b>{horizontalGap||0} pixels</b></div>
                </div>
            </EzPopoverPlus>
        </div>
    )
};

export default Demo;
```

## Alterando a posição do popover

Pocisionamente em relação ao pai.

## Métodos

### show()

  * Exibe o Popover.
  * **Parâmetros:**
    * `x` (número | string | undefined): Valor de deslocamento horizontal.
    * `y` (número | string | undefined): Valor de deslocamento vertical.
  * Exemplo de uso:

```javascript
popover.show();
popover.show(10, 10);
popover.show("10px", "10px");
```

### showUnder()

  * Exibe o Popover abaixo de um elemento de ancoragem.
  * **Parâmetros:**
    * `element` (HTMLElement | string): Elemento de referência para o posicionamento no popover, podendo ser o elemento diretamente ou um id.
    * `options` (IEzPopoverAnchorOptions): Objeto de configurações:
      * `horizontalGap` (number | undefined): Valor de deslocamento horizontal.
      * `verticalGap` (number | undefined): Valor de deslocamento vertical.
      * `fromRight` (boolean | undefined): Caso verdadeiro, o componente será mostrado da direito para esquerda.
  * Exemplo de uso:

```javascript
popover.showUnder(button);
popover.showUnder(button, { horizontalGap: 10, verticalGap: 10 });
popover.showUnder(button, { fromRight: true });
```

### hide()

  * Fecha o Popover.
  * Exemplo de uso:

```javascript
popover.hide();
```

### setOptions()

  * Altera as configurações de deslocamento e ponto de partida.
  * **Parâmetros:**
    * `options` (IEzPopoverAnchorOptions): Objeto de configurações:
      * `horizontalGap` (number | undefined): Valor de deslocamento horizontal.
      * `verticalGap` (number | undefined): Valor de deslocamento vertical.
      * `fromRight` (boolean | undefined): Caso verdadeiro, o componente será mostrado da direito para esquerda.
  * Exemplo de uso:

```javascript
popover.setOptions({ verticalGap: 5 });
popover.setOptions({ horizontalGap: 10, verticalGap: 10 });
popover.setOptions({ fromRight: true });
```

### setAnchorElement()

  * Altera o elemento de ancoragem.
  * **Parâmetros:**
    * `element` (HTMLElement | string): Elemento de referência para o posicionamento no popover, podendo ser o elemento diretamente ou um id.
  * Exemplo de uso:

```javascript
popover.setAnchorElement(button);
popover.setAnchorElement("text_input_id");
```

### updatePosition()

  * Altera o deslocamento do componente.
  * **Parâmetros:**
    * `x` (número | string | undefined): Valor de deslocamento horizontal.
    * `y` (número | string | undefined): Valor de deslocamento vertical.
  * Exemplo de uso:

```javascript
popover.updatePosition(5, 5);
popover.updatePosition("10px", "10px");
```

## Propriedades

### autoClose

  * Define se será fechado automaticamente quando o usuário clicar fora do conteúdo.
  * Tipo: _boolean_.
  * Valor padrão: _true_.

### boxWidth

  * Ajusta o comportamento da largura do popover.
  * Tipo: _string_.
  * Valores possíveis: _fit-content_ (ajusta ao conteúdo) ou _full-width_ (largura máxima).
  * Valor padrão: _fit-content_.

### opened

  * Define se o popover está visível ou oculto.
  * Tipo: _boolean_.
  * Valores possíveis: _true_ (visível) ou _false_ (oculto).
  * Valor padrão: _false_.

### overlayType

  * Define o tipo de overlay do popover.
  * Tipo: _string_.
  * Valores possíveis: _medium_ , _light_ ou _none_ (desabilitado).
  * Valor padrão: _light_.

### anchorElement

  * Define o elemento de ancoragem. O elemento de ancoragem pode ser passado por uma lista de elementos ou ids, neste caso, será priorizado os elementos de indices menores.
  * Tipo: _Array <HTMLElement | string> | HTMLElement | string_.
  * Valor padrão: _undefined_.

### options

  * Define as opções do elemento.
  * Tipo (objeto com as seguintes propriedades):
    * horizontalGap: _number_ (deslocamento horizontal).
    * verticalGap: _number_ (deslocamento vertical).
    * fromRight: _boolean_ (Caso verdadeiro, o componente será mostrado da direito para esquerda).
  * Valor padrão: **`{ horizontalGap: 0, verticalGap: 0, fromRight: false }`**.

### useAnchorSize

  * Define se o elemento manterá o mesmo tamanho do componente de ancora.
  * Tipo: _boolean_.
  * Valor padrão: _false_.

### minWidth

  * Define a largura mínima do elemento (apenas será considerada caso a propriedade useAnchorSize seja verdadeira).
  * Tipo: _number_.
  * Valor padrão: _150_.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| anchorElement | anchor-element | Define o elemento de ancoragem. | (string \| HTMLElement)[] \| HTMLElement \| string | undefined |
| autoClose | auto-close | Define que será fechado automaticamente quando o usuário clicar fora do conteúdo. | boolean | true |
| boxWidth | box-width | Ajusta o comportamento da largura do popover. | "fit-content" \| "full-width" | "fit-content" |
| fitInViewport | fit-in-viewport | Define se o popover deve se ajustar ao espaço visível disponível para não ser cortado pelas bordas da tela (ou por containers com rolagem). Quando verdadeiro, o conteúdo passa a rolar internamente em vez de ficar com parte oculta. Padrão: true. | boolean | true |
| minWidth | min-width | Define a largura mínima do elemento (apenas será considerada caso a propriedade useAnchorSize seja verdadeira). | number | 150 |
| opened | opened | Define se o ez-popover está aberto. | boolean | false |
| options | -- | Define as opções do elemento. | IEzPopoverAnchorOptions | { horizontalGap: 0, verticalGap: 0, fromRight: false } |
| overlayType | overlay-type | Define o tipo de overlay do popover. | "light" \| "medium" \| "none" | "light" |
| useAnchorSize | use-anchor-size | Define se o elemento manterá o mesmo tamanho do componente de ancora. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| ezVisibilityChange | Emitido quando acontece a alteração de estado do componente. | CustomEvent<boolean> |

### Methods

#### `hide() => Promise<void>`

Oculta o ez-popover.

##### Returns

Type: `Promise<void>`

#### `setAnchorElement(anchor: HTMLElement | string) => Promise<void>`

Altera o elemento de ancoragem.

##### Returns

Type: `Promise<void>`

#### `setOptions(options: IEzPopoverAnchorOptions) => Promise<void>`

Altera as opções.

##### Returns

Type: `Promise<void>`

#### `show(top?: string | number, left?: string | number) => Promise<void>`

Exibe o ez-popover.

##### Returns

Type: `Promise<void>`

#### `showUnder(element: HTMLElement | string, options?: IEzPopoverAnchorOptions) => Promise<void>`

Ancora a exibição do popOver a um elemento HTML.

##### Returns

Type: `Promise<void>`

#### `updatePosition(top?: string, left?: string) => Promise<void>`

Atualiza a posição do popover.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-classic-date-input
  * ez-classic-date-time-input
  * ez-classic-search
  * ez-classic-search-plus
  * ez-combo-box
  * ez-date-input
  * ez-date-time-input
  * ez-search
  * ez-search-plus
  * filter-column

#### Depends on

  * ez-popover-core
