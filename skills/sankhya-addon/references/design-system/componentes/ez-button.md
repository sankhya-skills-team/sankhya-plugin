> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button/ (snapshot 2026-09-28)

# Button

Botões são usados para inicializar uma ação. Os rótulos dos botões expressam qual ação ocorrerá quando o usuário interagir com eles. Use botões para comunicar as ações que os usuários podem realizar e para permitir que os usuários interajam com a página.

Primário

Secundário

Terciário

```jsx
import { EzButton } from '@sankhyalabs/ezui/react/components';
import "./demo.css"

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--row">
            <div className="display-column">
                <span className="ez-text ez-text--secondary ez-margin--small">Primário</span>
                <EzButton
                    label="Primário"
                    variant="primary"
                    size="large"
                    leftIconName={"arrow_back"}
                />
                <EzButton
                    variant="primary"
                    mode="icon"
                    size="large"
                    iconName={"bell"}
                    onClick={() => alert("Botão primário clicado!")}
                    suppressAnimation
                />
                <EzButton
                    label={"Primário"}
                    variant="primary"
                    mode="label-icon"
                    size="large"
                    iconName={"bell"}
                    onClick={() => alert("Botão primário clicado!")}
                />
                <EzButton
                    label="Disabled"
                    variant="primary"
                    size="large"
                    leftIconName={"arrow_back"}
                    rightIconName={"arrow-forward"}
                    onClick={() => alert("Botão primário clicado!")}
                    isDisabled
                />
            </div>
            <div className="display-column">
                <span className="ez-text ez-text--secondary ez-margin--small">Secundário</span>
                <EzButton
                    label="Secundário"
                    size="large"
                    rightIconName={"arrow-forward"}
                />
                <EzButton
                    variant="secondary"
                    mode="icon"
                    size="large"
                    iconName={"check"}
                    onClick={() => alert("Botão secundário clicado!")}
                />
                <EzButton
                    label={"Secundário"}
                    variant="secondary"
                    mode="label-icon"
                    size="large"
                    iconName={"bell"}
                    onClick={() => alert("Botão secundário clicado!")}
                />
                <EzButton
                    variant="secondary"
                    mode="icon"
                    size="large"
                    iconName={"lock-alt"}
                    onClick={() => alert("Botão secundário clicado!")}
                    isDisabled
                />
            </div>
            <div className="display-column">
                <span className="ez-text ez-text--secondary ez-margin--small">Terciário</span>
                <EzButton
                    label="Terciário"
                    variant="tertiary"
                    size="large"
                    leftIconName={"arrow_back"}
                    rightIconName={"arrow-forward"}
                />
                <EzButton
                    variant="tertiary"
                    mode="icon"
                    size="large"
                    iconName={"clipboard"}
                    onClick={() => alert("Botão terciário clicado!")}
                />
                <EzButton
                    label={"Terciário"}
                    variant="tertiary"
                    mode="label-icon"
                    size="large"
                    iconName={"bell"}
                    onClick={() => alert("Botão terciário clicado!")}
                />
                <EzButton
                    label={"Terciário"}
                    variant="tertiary"
                    mode="label-icon"
                    size="large"
                    iconName={"bell"}
                    onClick={() => alert("Botão terciário clicado!")}
                    isDisabled
                />
            </div>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Variantes

Utilize o atributo class ou a prop variant para mudar o estado do botão

O estado dos botões podem ser alterados através da utilização das classes `ez-button--primary` e `ez-button--tertiary`. O estado secundário é o default, logo não precisa ser adicionado.

A prop variant também pode ser utilizada com a mesma finalidade, recebendo os valores `primary`, `secondary` ou `tertiary`

Utiliza classe

Utiliza prop

```jsx
import React from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const btnClick = (tipo) => (
        ApplicationUtils.message("Título da Mensagem", `Clicou no ${tipo}.`)
    )

    return (
        <>
            <span className="ez-text ez-text--primary ez-margin--small">Utiliza classe</span>
            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
                <EzButton
                    label="Botão Primário"
                    onClick={() => btnClick("Primário")}
                    className="ez-button--primary"
                />

                <EzButton label="Botão Secundário" onClick={() => btnClick("Secundário")} />

                <EzButton
                    label="Botão Terciário"
                    onClick={() => btnClick("Terciário")}
                    className="ez-button--tertiary"
                />
            </div>

            <span className="ez-text ez-text--primary ez-margin--small">Utiliza prop</span>
            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-padding-top--medium">
                <EzButton
                    label="Botão Primário"
                    onClick={() => btnClick("Primário")}
                    variant="primary"
                />

                <EzButton label="Botão Secundário" onClick={() => btnClick("Secundário")} />

                <EzButton
                    label="Botão Terciário"
                    onClick={() => btnClick("Terciário")}
                    variant="tertiary"
                />
            </div>
        </>

    )
};

export default Demo;
```

### Primário.

É o botão de maior destaque da tela. Ele orienta a ação principal onde está inserido. Por isso, deve ser usado apenas 1 por bloco.

### Secundário.

É o botão mais comum e com mais opções de uso.

demo.js

```jsx
import React from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <div className='ez-flex ez-flex--justify-center'>
        <EzButton
            label="Botão Secundário"
            onClick={() => alert("Botão clicado!")}
        />
    </div>
);

export default Demo;
```

### Terciário.

Normalmente acompanhado de um botão primário e expressa uma ação mais incomum na jornada.

### Habilitado.

Prop descontinuada

A prop `enabled` está sendo descontinuada, recomendamos a utilização da prop `isDisabled` com suporte a melhorias de acessibilidade.

demo.js

```jsx
import React from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <div className='ez-flex ez-flex-row ez-flex--justify-around '>
        <EzButton
            label="Botão Habilitado"
        />
        <EzButton
            label="Enabled"
            enabled
        />
        <EzButton
            label="isDisabled"
            isDisabled={false}
        />
    </div>
);

export default Demo;
```

### Desabilitado.

Existem 2 formas de se desabilitar um botão utilizando a prop `isDisabled`.

Quando passamos o valor `isDisabled={"full"}` temos o disable nativo do HTML, onde o botão fica inacessível, ou seja, não entra na navegação via teclado.

Quando passamos o valor `isDisabled={true}`(recomendado) temos um disable acessível, onde o usuário ainda pode acessar o botão via teclado, mesmo que a interação com o mesmo esteja bloqueada.

Utilize a navegação com `Tab` para notar a diferença entre os botões

### Suprimir animação.

A animação de ripple do componente pode ser suprimida pela prop `suppressAnimation`

Com animação

Sem animação

```jsx
import { EzButton } from '@sankhyalabs/ezui/react/components';
import "./suppressAnimation.css"

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--row">
            <div className="display-column">
                <span className="ez-text ez-text--secondary ez-margin--small">Com animação</span>
                <EzButton
                    label="Animado"
                    variant="primary"
                    size="large"
                />
                <EzButton
                    variant="secondary"
                    mode="icon"
                    size="large"
                    iconName={"check"}
                />
                <EzButton
                    label={"Secundário"}
                    variant="tertiary"
                    mode="label-icon"
                    size="large"
                    iconName={"bell"}
                />
                <EzButton
                    variant="secondary"
                    mode="icon"
                    size="large"
                    isDisabled
                    iconName={"lock-alt"}
                />
            </div>
            <div className="display-column">
                <span className="ez-text ez-text--secondary ez-margin--small">Sem animação</span>
                <EzButton
                    variant="primary"
                    label="Não animado"
                    size="large"
                    suppressAnimation
                />
                <EzButton
                    variant="secondary"
                    mode="icon"
                    size="large"
                    iconName={"check"}
                    suppressAnimation
                />
                <EzButton
                    label={"Secundário"}
                    variant="tertiary"
                    mode="label-icon"
                    size="large"
                    iconName={"bell"}
                    suppressAnimation
                />
                <EzButton
                    variant="secondary"
                    mode="icon"
                    size="large"
                    isDisabled
                    iconName={"lock-alt"}
                    suppressAnimation
                />
            </div>

        </div>
    )
};

export default Demo;
```

### Label.

### Modos.

#### Link.

demo.js

```jsx
import React from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <div className='ez-flex ez-flex-row ez-flex--justify-around '>
        <EzButton
          label="Link"
          mode="link"
        />
    </div>
);

export default Demo;
```

#### Ícone.

#### Ícone e texto.

SlotProp

demo.js

```jsx
import React from 'react';
import { EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
      <>
            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
                  <span className="ez-text ez-text--primary ez-margin--small">Slot</span>
                  <span className="ez-text ez-text--primary ez-margin--small">Prop</span>
            </div>
            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
                  <EzButton label='Button'>
                        <EzIcon slot="leftIcon" iconName="check-circle-inverted" />
                  </EzButton>

                  <EzButton label='Button' rightIconName="check-circle-inverted" />
            </div>
      </>
);

export default Demo;
```

#### Ícone na esquerda, direita e texto.

### Tamanhos.

demo.js

```jsx
import React from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
    <EzButton label="Botão pequeno" size="small" />

    <EzButton label="Botão médio" size="medium" />

    <EzButton label="Botão grande" size="large" />
  </div>
);

export default Demo;
```

## Exemplos de métodos.

### Adicionar foco.

Focado: **Não**

### Remover foco.

O foco será removido automaticamente após 2 segundos após o foco inicial.

Focado: **Não**

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [isFocus, setIsFocus] = useState(false);

    const onFocus = () => {
        element.current.setFocus();
    };

    const handleOnFocus = () => {
        setIsFocus(true)
        setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
            <label className="ez-margin--medium">
                O foco será removido automaticamente após 2 segundos após o foco inicial.
            </label>
            <div className="ez-flex ez-flex--column">
                <EzButton
                    ref={element}
                    label="Botão comum"
                    onBlur={() => setIsFocus(false)}
                    onFocus={() => handleOnFocus()}
                    />

                <label className="ez-margin--medium">
                    Focado: <strong>{isFocus ? "Sim" : "Não"}</strong>
                </label>
                <div>
                    <EzButton
                        label="Focar Botão"
                        mode="link"
                        onClick={onFocus}
                        />

                </div>
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
| enabled | enabled | ⚠️ [DEPRECATED] Use isDisabled prop instead.Se false o usuário não pode interagir com o botão. | boolean | true |
| iconName | icon-name | Define o ícone a ser usado da biblioteca de ícones: ez-icons | string | undefined |
| image | image | Define o caminho usado nos modos icon e label-icon para imagens não contempladas na biblioteca de ícones. | string | undefined |
| isDisabled | is-disabled | Se verdadeiro o clique no botão fica desabilitado mas a navegação continua funcional. Se full, o usuário não pode interagir com o botão. | "" \| "full" \| boolean | false |
| label | label | Texto a ser apresentado como título do botão. | string | undefined |
| leftIconName | left-icon-name | Define o ícone esquerdo do ez-button. Tem prioridade sobre o slot leftIcon . | string | undefined |
| mode | mode | Define o modo de uso do botão. | "icon" \| "label-icon" \| "link" \| "regular" | "regular" |
| rightIconName | right-icon-name | Define o ícone direto do ez-button. Tem prioridade sobre o slot rightIcon . | string | undefined |
| size | size | Define o tamanho do ez-button. | "large" \| "medium" \| "small" \| "x-small" | "medium" |
| suppressAnimation | suppress-animation | Se verdadeiro, desabilita a animação de ripple. | boolean | false |
| type | type | Define o tipo do botão. Pode ser button , submit ou reset . | string | "button" |
| variant | variant | Define a variante do ez-button. | "primary" \| "secondary" \| "tertiary" | undefined |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do botão.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Aplica o foco no botão.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-actions-button
  * ez-alert-list
  * ez-classic-search
  * ez-dialog
  * ez-double-list
  * ez-grid
  * ez-grid-pagination
  * ez-guide-navigator
  * ez-image-input
  * ez-modal-container
  * ez-pagination
  * ez-popup
  * ez-record-navigation
  * ez-scroller
  * ez-search
  * ez-sidebar-navigator
  * ez-split-item
  * ez-text-edit
  * ez-tile-medium
  * filter-column

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-button--min-width | Define a largura mínima do componente. |
| --ez-button--width | Define a largura do componente. |
| --ez-button--height | Define a altura do componente. |
| --ez-button--padding-top | Define o espaçamento superior ao label. |
| --ez-button--padding-bottom | Define o espaçamento inferior ao label. |
| --ez-button--padding-right | Define o espaçamento à direita do label. |
| --ez-button--padding-left | Define o espaçamento à esquerda do label. |
| --ez-button--icon--gap | Define o gap entre o texto e ícone, quando existir. |
| --ez-button--color | Define a cor do label. |
| --ez-button--label-icon--color | Define a cor do label do botao tipo label-icon. |
| --ez-button--label-icon--hover-color | Define a cor do label do botao tipo label-icon, quando o mouse sobre o botão. |
| --ez-button--label-icon--disabled-color | Define a cor do label do botao tipo label-icon, quando desabilitado. |
| --ez-button--left-icon--color | Define a cor do icone esquerdo. |
| --ez-button--right-icon--color | Define a cor do icone direito, quando o mouse está sobre o botão. |
| --ez-button--left-icon--hover-color | Define a cor do icone esquerdo. |
| --ez-button--right-icon--hover-color | Define a cor do icone direito, quando o mouse está sobre o botão. |
| --ez-button--left-icon--disabled-color | Define a cor do icone esquerdo, quando desabilitado. |
| --ez-button--right-icon--disabled-color | Define a cor do icone direito, quando desabilitado. |
| --ez-button--font-size | Define o tamanho do label. |
| --ez-button--font-family | Define a família da fonte do label. |
| --ez-button--font-weight | Define o peso da fonte do label. |
| --ez-button--background-color | Define a cor de fundo do botão. |
| --ez-button--border-radius | Define o raio da borda do botão. |
| --ez-button--border | Define o estilo da borda do botão. |
| --ez-button--hover--border | Define o estilo da borda do botão quando em hover. |
| --ez-button--justify-content | Define o alinhamento horizontal do conteúdo do botão. |
| --ez-button--hover-color | Define a cor do texto e do ícone quando o cursor está sobre o botão. |
| --ez-button--hover--background-color | Define a cor de fundo quando o cursor está sobre o botão. |
| --ez-button--disabled-color | Define a cor do texto quando o botão está desabilitado. |
| --ez-button--disabled--background-color | Define a cor de fundo quando o botão está desabilitado. |
| --ez-button--disabled--border | Define a cor da borda quando o botão está desabilitado. |
| --ez-button--disabled-icon-color | Define a cor do icone quando o botão está desabilitado. |
| --ez-button--link-color | Define a cor do texto do botão no modo link. |
| --ez-button--link--hover-color | Define a cor do texto do botão no hover do modo link. |
| --ez-button--link-disabled-color | Define a cor do texto do botão no hover do modo link, quando desabilitado. |
| --ez-button--link--small--font-size | Define o tamanho small na fonte do texto do botão no modo link. |
| --ez-button--link--medium--font-size | Define o tamanho medium na fonte do texto do botão no modo link. |
| --ez-button--link--large--font-size | Define o tamanho large na fonte do texto do botão no modo link. |
