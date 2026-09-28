> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input/ (snapshot 2026-09-28)

# Text Input

Os inputs permitem que os usuários insiram dados de texto de formato livre. O tipo de campo utilizado deve refletir o cumprimento do conteúdo que você espera que o usuário insira. Esse input padrão é para conteúdo curto de uma linha.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextInput label="Text Input" />
);

export default Demo;
```

## Variações e estados.

### Deixa o campo disponível.

### Deixa o campo indisponível.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextInput
        label="Campo desabilitado"
        enabled={false}
    />
);

export default Demo;
```

### Label.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextInput label="Label do campo" />
)

export default Demo;
```

### Com estado de erro.

### Modo regular.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextInput
        label="Campo no modo regular"
        mode="regular"
    />
);

export default Demo;
```

### Modo slim.

### Modo Password.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTextInput
    label="Campo password"
    password={true}
  />
);

export default Demo;
```

### Aplica uma máscara no campo.

### Exibe mensagem de erro.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTextInput
    label="Campo com mensagem de erro"
    errorMessage="Mensagem de erro"
    canShowError={false} />
);

export default Demo;
```

### Restringe o que o usuário pode digitar.

### Define se o campo contará com bordas.

demo.js

```jsx
import React from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTextInput
    label="Campo sem borda"
    noBorder={true}
  />
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
import { EzTextInput} from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const removeFocus = () => {
        setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <>
            <EzTextInput
                ref={element}
                label="Título do campo"
                onFocus={removeFocus}
            >
            </EzTextInput>

            <label>O foco será removido automaticamente após 2 segundos</label>
        </>
    );
}

export default Demo;
```

### Informand se o campo está inválido.

Inválido: **Não**

## Exemplos de eventos.

### Ao mudar o estado do componente.

**Valor Alterado:**

demo.js

```jsx
import React, { useState } from 'react';
import { EzTextInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [value, setValue] = useState(null);

    const onChange = (evt) => {
        setValue(evt.detail);
    };

    return (
        <>
            <EzTextInput label="Título do campo" onEzChange={onChange} />
            <label>
                <b>Valor Alterado: </b> {value?.toString()}
            </label>
        </>
    );
}

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alternativePlaceholder | alternative-placeholder | Texto alternativo a ser apresentado como título do campo. | string | undefined |
| autoFocus | auto-focus | Se true o campo receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| cleanValueMask | clean-value-mask | Para remover a máscara quando fizer um apply no formulário. | boolean | false |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| hasInvalid | has-invalid | Define se o campo está em estado inválido (bordas vermelhas). | boolean | false |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mask | mask | Aplica uma máscara no conteúdo conforme o padrão estabelecido | string | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| noBorder | no-border | Se true o campo não terá bordas. | boolean | false |
| password | password | Se true o campo não terá bordas. | boolean | false |
| restrict | restrict | Restringe o que o usuário pode digitar. | string | undefined |
| value | value | Define o valor do campo. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<string> |

### Methods

#### `isInvalid() => Promise<boolean>`

Retorna se o conteúdo é inválido.

##### Returns

Type: `Promise<boolean>`

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus(options?: TFocusOptions) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-combo-box
  * ez-date-input
  * ez-date-time-input
  * ez-filter-input
  * ez-form-view
  * ez-link-builder
  * ez-number-input
  * ez-search
  * ez-search-plus
  * ez-simple-image-uploader
  * ez-text-edit
  * ez-time-input

#### Depends on

  * ez-tooltip
  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-text-input--height | Define a altura do componente. |
| --ez-text-input--width | Define a largura do componente. |
| --ez-text-input__icon--width | Define a largura do slot que contém o ícone. |
| --ez-text-input--height--slim | Define a altura do componente em modo "slim". |
| --ez-text-input__min-width | Define a largura maxima do componente. |
| --ez-text-input__max-width | Define a largura minima do componente. |
| --ez-text-input--border-radius | Define o raio da borda do input do componente. |
| --ez-text-input--border-top-left-radius | Define o raio da borda no top esquerdo do componente. |
| --ez-text-input--border-bottom-left-radius | Define o raio da borda inferior esquerda do componente. |
| --ez-text-input--border-top-right-radius | Define o raio da borda no top direito do componente. |
| --ez-text-input--border-bottom-right-radius | Define o raio da borda inferior direita do componente. |
| --ez-text-input--font-size | Define o tamanho da fonte do input e label do componente. |
| --ez-text-input--font-family | Define a família da fonte do input, label e caixa de mensagem do componente. |
| --ez-text-input--font-weight | Define o peso da fonte do label do componente. |
| --ez-text-input--color | Define a cor da fonte do input e label do componente. |
| --ez-text-input__margin-bottom | Define a margem abaixo do componente. |
| --ez-text-input__input--background-color | Define a cor de fundo do input. |
| --ez-text-input__input--border | Define o estilo da borda do input. |
| --ez-text-input__input--border-color | Define a cor da borda do input. |
| --ez-text-input__input--focus--border-color | Define a cor da borda do input quando focado. |
| --ez-text-input__input--disabled--background-color | Define a cor de fundo do input quando desabilitado. |
| --ez-text-input__input--disabled--color | Define a cor do texto do input. |
| --ez-text-input__input--error--border-color | Define a cor da borda do input quando com erro. |
| --ez-text-input__input--noborder-color | Define a cor do input quando não possuir borda |
| --ez-text-input__input--padding | Define o padding do input |
| --ez-text-input__placeholder--color | Define a cor do placeholder do input. |
| --ez-text-input__tooltip_icon--error--color | Define a cor da fonte da mensagem quando erro. |
| --ez-text-input__label--floating--top | Define o posicionamento do label. |
| --ez-text-input__label--padding-top | Define o posicionamento do label. |
| --ez-text-input__label--padding-left | Define o espaçamento esquerdo do label. |
| --ez-text-input__label--padding-right | Define o espaçamento direito do label. |
| --ez-text-input__input--focus--icon-color | Define a cor do ícone do slot. |
| --ez-text-input__input--disabled--focus--icon-color | Define a cor do ícone do slot quando disabled. |
| --ez-text-input__tooltip-icon--spacing | Define o espaçamento lateral do icone de erro. |
| --ez-text-input__tooltip-icon---width | Define a largura do icone de erro. |
| --ez-text-input__tooltip-icon---horizontal-margin | Define a margem horizontal do icone de erro. |
| --ez-text-input__tooltip-icon---vertical-margin | Define a margem vertical do icone de erro. |
