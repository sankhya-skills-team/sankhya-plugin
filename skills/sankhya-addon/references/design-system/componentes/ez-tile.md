> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile/ (snapshot 2026-09-28)

# Tile

O **Tile** é um componente versátil que pode ser utilizado para criação de um botão grande, item de menu ou elemento de navegação destacado.

demo.js

```jsx
import { EzTile } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '50%'}}>
            <EzTile
                text="color default"
                isInteractive
                onClick={() => alert("default")}
            />
            <EzTile
                text="color green"
                color="green"
                iconName="acao"
                isInteractive
                onClick={() => alert("green")}
            />
            <EzTile
                text="color gray"
                color="gray"
                iconName="bell"
                isInteractive
                onClick={() => alert("gray")}
            />
            <EzTile
                text="color red"
                color="red"
                iconName="check"
                isInteractive
                onClick={() => alert("red")}
            />
            <EzTile
                text="color yellow"
                color="yellow"
                iconName="clipboard"
                isInteractive
                onClick={() => alert("yellow")}
            />
        </div>
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '50%'}}>
            <EzTile
                text="color default"
                onClick={() => alert("default")}
            />
            <EzTile
                text="color green"
                color="green"
                iconName="acao"
                onClick={() => alert("green")}
            />
            <EzTile
                text="color gray"
                color="gray"
                iconName="bell"
                onClick={() => alert("gray")}
            />
            <EzTile
                text="color red"
                color="red"
                iconName="check"
                onClick={() => alert("red")}
            />
            <EzTile
                text="color yellow"
                color="yellow"
                iconName="clipboard"
                onClick={() => alert("yellow")}
            />
        </div>
    </div>
  );
};

export default Demo;
```

## Variações

### Tamanhos

O Tile suporta diferentes tamanhos, que podem ser definidos por meio da propriedade `size`.

Além disso o Tile suporta altura e largura customizadas por padrão, que podem ser definidas por meio das propriedades `height` e `width`.

demo.js

```jsx
import { EzTile } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
          <EzTile text="Custom height and width" size="small" height={250} width={250} />
        </div>
    </div>
  );

};

export default Demo;
```

### Cores

O Tile possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio da propriedade `color`.

demo.js

```jsx
import { EzTile } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
        <EzTile
            text="Color default"
            isInteractive
            onClick={() => alert("default")}
        />
        <EzTile
            text="Color green"
            color="green"
            isInteractive
            onClick={() => alert("green")}
        />
        <EzTile
            text="Color gray"
            color="gray"
            isInteractive
            onClick={() => alert("gray")}
        />
        <EzTile
            text="Color red"
            color="red"
            isInteractive
            onClick={() => alert("red")}
        />
        <EzTile
            text="Color yellow"
            color="yellow"
            isInteractive
            onClick={() => alert("yellow")}
        />
    </div>
  );
};

export default Demo;
```

### Ícone

O ícone utilizado no Tile pode ser definido pelo propriedade `iconName`, dentre os ícones disponíveis na biblioteca.

Veja a lista completa de ícones.

### Quantidade de linhas

O Tile por padrão apresenta somente 1 linha de texto, podemos mudar a quantidade máxima de linhas com a propriedade `maximumLines`.

demo.js

```jsx
import { EzTile } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
      <EzTile text="Tile padrão com 1 linha de texto" size="medium" />
      <EzTile text="Tile com 3 linhas de texto antes de aplicar o ellipsis" size="medium" maximumLines={3} />
    </div>
  );
};

export default Demo;
```

### Interatividade

A propriedade `isInteractive` adiciona interatividade ao Tile, exibindo um feedback visual quando o mouse passa por cima e permitindo gerenciar o evento de clique.

## Métodos

### setFocus e setBlur

O Tile pode receber ou remover foco de forma imperativa através dos métodos `setFocus` e `setBlur`.

Focado: **Não** O foco será removido automaticamente após 2 segundos

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzTile } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [isFocus, setIsFocus] = useState(false);

    const focusTile = () => {
        element.current.setFocus();
    };

    const handleFocus = () => {
        setIsFocus(true);
        setTimeout(() => {
            element.current.setBlur();
            setIsFocus(false);
        }, 2000);
    };

    return (
        <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
            <EzTile
                ref={element}
                text="Tile default"
                isInteractive
                onClick={() => alert("default")}
                onBlur={() => setIsFocus(false)}
                onFocus={() => handleFocus()}
            />

            <label className="ez-margin--medium">
                Focado: <strong>{isFocus ? "Sim" : "Não"}</strong>
            </label>
            <label className="ez-margin-top--small">O foco será removido automaticamente após 2 segundos</label>

            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-gap--medium">
                <EzButton
                    label="Focar Tile"
                    className="ez-padding--medium"
                    onClick={focusTile}
                />
            </div>
        </div>
    );
}

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| color | color | Define a cor tema do componente. | "default" \| "gray" \| "green" \| "red" \| "yellow" | "default" |
| height | height | Define o tamanho do componente, sobrescrevendo o padrão da propriedade size. | number | undefined |
| iconName | icon-name | Define o ícone a ser usado da biblioteca de ícones: ez-icons | string | "home" |
| isInteractive | is-interactive | Define se o componente será interativo. Caso contrário, será estático.  Se true, permite permite clique. Se false, não permite clique | boolean | false |
| maximumLines | maximum-lines | Define a quantidade máxima de linhas de texto a serem apresentadas. Quando a propriedade não é passada, limita a 1 linha. | number | undefined |
| size | size | Define qual o tamanho do componente. - "default" : 120x80px - "medium" : 120x170px | "medium" \| "small" | "small" |
| text | text | Texto a ser apresentado como título do componente. | string | undefined |
| width | width | Define a largura do componente, sobrescrevendo o padrão da propriedade size. | number | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| tileClick | Emitido quando o elemento principal é clicado | CustomEvent<void> |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do componente.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Aplica o foco no componente.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-tile--width | Define a largura do componente. |
| --ez-tile--height | Define a altura do componente. |
| --ez-tile--padding | Define a margem do componente. |
| --ez-tile--icon--margin-bottom | Define o espaçamento entre o ícone e o title. |
| --ez-tile--border-radius | Define o raio da borda do componente. |
| --ez-tile--background-color | Define a cor de fundo do componente. |
| --ez-tile--color | Define a cor do title. |
| --ez-tile--icon-color | Define a cor do ícone. |
| --ez-tile--hover-background-color | Define a cor de fundo do componente no hover. |
| --ez-tile--hover-color | Define a cor do title no hover. |
| --ez-tile--hover-icon-color | Define a cor do ícone no hover. |
| --ez-tile--focus-visible-border | Define a cor do ícone no hover. |
| --ez-tile--font-family | Define a família da fonte do title. |
| --ez-tile--font-weight | Define o peso da fonte do title. |
| --ez-tile--font-size | Define o tamanho do title. |
| --ez-tile--title-line-height | Define a altura da linha do title. |
| --ez-tile--icon-line-height | Define a altura da linha do ícone. |
