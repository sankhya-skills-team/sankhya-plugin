> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-area/ (snapshot 2026-09-28)

# Text Area

Utilizado para entradas mais longas de várias linhas.

demo.js

```jsx
import React from 'react';
import { EzTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextArea label="Label do campo" />
);

export default Demo;
```

## Variações e estados.

### Deixa o campo disponível.

demo.js

```jsx
import React from 'react';
import { EzTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextArea
        label="Campo habilitado"
        enabled={true}
    />
);

export default Demo;
```

### Deixa o campo indisponível.

### Exibe mensagem de erro.

demo.js

```jsx
import React from 'react';
import { EzTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTextArea
    label="Campo com mensagem de erro"
    errorMessage="Mensagem de erro"
  />
);

export default Demo;
```

### Define número de linhas.

### Permite exibir a mensagem de erro.

demo.js

```jsx
import React from 'react';
import { EzTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTextArea
    label="Campo com mensagem de erro"
    errorMessage="Mensagem de erro"
    canShowError={false}
  />
);

export default Demo;
```

### Modo regular.

### Modo slim.

demo.js

```jsx
import React from 'react';
import { EzTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTextArea label="Campo no modo slim" mode="slim" />
);

export default Demo;
```

## Exemplos de métodos.

### Faz o foco no componente de input.

Focado: **Não**

### Remove o foco no componente de input.

O foco será removido automaticamente após 2 segundos

demo.js

```jsx
import React, { useRef } from 'react';
import { EzTextArea} from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const removeFocus = () => {
        setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <>
            <EzTextArea
                ref={element}
                label="Título do campo"
                onFocus={removeFocus}
            >
            </EzTextArea>

            <label>O foco será removido automaticamente após 2 segundos</label>
        </>
    );
}

export default Demo;
```

### Informa se o campo está inválido.

Inválido: **Não**

### Adiciona ou substitui texto selecionado por um valor informado.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzTextArea, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const textToAppend = "NOVO TEXTO"

    function handleClickButton(){
      element.current.appendTextToSelection(textToAppend)
    }

    return (
        <>
            <EzTextArea ref={element} label="Título do campo"/>

            <EzButton label="Adicionar / Substituir texto"
                className="ez-margin-top--medium"
                onClick={handleClickButton}
            />
        </>
    );
}

export default Demo;
```

## Exemplos de eventos.

### Ao mudar o estado do componente.

**Valor Alterado:**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alternativePlaceholder | alternative-placeholder | Texto alternativo a ser apresentado como título do campo. | string | undefined |
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| autoRows | auto-rows | Ativa a opção de fazer as linhas do componente serem baseados na altura máxima. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| enableResize | enable-resize | Ativa a opção de fazer resize do input. | boolean | true |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | 'regular' |
| rows | rows | Define o número de linhas. | number | 4 |
| value | value | Define o valor do campo. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<string> |

### Methods

#### `appendTextToSelection(text: string) => Promise<void>`

Adiciona o argumento text no value do text area, seguindo as regras:

  * Se o cursor do mouse está posicionado em algum local do texto, o argumento será adicionado nesse local.
  * Se existir uma seleção no texto, o trecho selecionado deve ser substituído pelo argumento.
  * Se não existir seleção nem posicionamento do cursor do mouse, o argumento será adicionado no final do texto.

##### Returns

Type: `Promise<void>`

#### `isInvalid() => Promise<boolean>`

Retorna se o conteúdo é inválido.

##### Returns

Type: `Promise<boolean>`

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form-view
  * ez-rich-text

#### Depends on

  * ez-tooltip
  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --text-area--width | Define a largura do componente. |
| --text-area--border-radius | Define o raio da borda do input do componente. |
| --text-area--font-size | Define o tamanho da fonte do input e label do componente. |
| --text-area--font-family | Define a família da fonte do input, label e caixa de mensagem do componente. |
| --text-area--font-weight | Define o peso da fonte do label do componente. |
| --text-area--color | Define a cor da fonte do input e label do componente. |
| --text-area__input--background-color | Define a cor de fundo do input. |
| --text-area__input--border | Define o estilo da borda do input. |
| --text-area__input--border-color | Define a cor da borda do input. |
| --text-area__input--focus--border-color | Define a cor da borda do input quando focado. |
| --text-area__input--disabled--background-color | Define a cor de fundo do input quando desabilitado. |
| --text-area__input--disabled--color | Define a cor do texto do input. |
| --text-area__input--disabled--border--color | Define a borda do texto do input quando desabilitado. |
| --text-area__input--error--border-color | Define a cor da borda do input quando com erro. |
| --text-area__message_box--font-size | Define o tamanho da fonte da mensagem abaixo do input. |
| --text-area__message_box--info--color | Define a cor da fonte da mensagem quando info. |
| --text-area__message_box--error--color | Define a cor da fonte da mensagem quando erro. |
| --text-area__label--floating--top | Define o posicionamento do label. |
| --text-area__label--padding-top | Define o espaçamento superior do label. |
| --text-area__label--padding-left | Define o espaçamento esquerdo do label. |
| --text-area__label--padding-right | Define o espaçamento direito do label. |
| --text-area__scrollbar--color-default | Define a cor da barra de rolagem do componente. |
| --text-area__scrollbar--color-background | Define a cor de fundo da barra de rolagem do componente. |
| --text-area__scrollbar--color-hover | Define a cor do hover na barra de rolagem do componente. |
| --text-area__scrollbar--color-clicked | Define a cor do active na barra de rolagem do componente. |
| --text-area__scrollbar--border-radius | Define o raio da borda da barra de rolagem do componente. |
| --text-area__scrollbar--width | Define a largura da barra de rolagem do componente. |
| --ez-text-area__tooltip-icon--spacing | Define o espaçamento lateral do icone de erro. |
| --ez-text-area__tooltip-icon---width | Define a largura do icone de erro. |
| --ez-text-area__tooltip-icon---horizontal-margin | Define a margem horizontal do icone de erro. |
| --ez-text-area__tooltip-icon---vertical-margin | Define a margem vertical do icone de erro. |
| --ez-text-area__tooltip_icon--error--color | Define a cor da fonte da mensagem quando erro. |
