> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-radio-button/ (snapshot 2026-09-28)

# Radio Button

Use os Radio button quando tiver um grupo de opções e apenas uma seleção da lista for permitida.

demo.js

```jsx
import React from 'react';
import { EzRadioButton, EzRadioButtonOption } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzRadioButton label="Escolha um esporte">
            <ez-radio-button-option label="Futebol" value="F" />
            <ez-radio-button-option label="Basquete" value="B" />
            <ez-radio-button-option label="Volei" value="V" />
        </EzRadioButton>
    )
};

export default Demo;
```

## Adicionar as opções por array

demo.js

```jsx
import React from 'react';
import { EzRadioButton } from '@sankhyalabs/ezui/react/components';

const options = [
    { label: "Futebol", value: "F" },
    { label: "Basquete", value: "B" },
    { label: "Volei", value: "V" }
];

const Demo = () => {
    return (
        <EzRadioButton label="Escolha um esporte" options={options}/>
    );
};

export default Demo;
```

## Desabilitado

## Orientação horizontal

demo.js

```jsx
import React from 'react';
import { EzRadioButton, EzRadioButtonOption } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzRadioButton label="Escolha um esporte" direction="horizontal">
            <ez-radio-button-option label="Futebol" value="F" />
            <ez-radio-button-option label="Basquete" value="B" />
            <ez-radio-button-option label="Volei" value="V" />
        </EzRadioButton>
    )
};

export default Demo;
```

## Evento

Sempre que uma opção é selecionada, um evento ezChange é emitido com o valor selecionado.

**Valor selecinonado:**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| direction | direction | Define a direção dos itens. | "horizontal" \| "vertical" | "vertical" |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| options | -- | Define as opções que serão apresentadas | Radio[] | [] |
| value | value | Define o valor do campo. | any | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<any> |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-radio-button--font-family | Define a família da fonte do label. |
| --ez-radio-button--font-size | Define o tamanho do label. |
| --ez-radio-button--font-weight | Define o peso da fonte do label. |
| --ez-radio-button--font-color | Define a cor do texto. |
| --ez-radio-button--padding-vertical | Define o espaço superior e inferior da lista de opções. |
| --ez-radio-button--padding-horizontal | Define o espaço lateral da lista de opções. |
| --ez-radio-button__form-label--font-family | Define a família da fonte do label. |
| --ez-radio-button__form-label--font-weight | Define o peso da fonte do label. |
| --ez-radio-button__form-label--title-primary | Define a cor do texto. |
| --ez-radio-button__form-label--font-size | Define o tamanho do label. |
| --ez-radio-button__form-label--padding-horizontal | Define o espaço lateral da lista de opções. |
| --ez-radio-button__form-radio--border-color | cor da borda do radio sem seleção (sem seleção / sem foco / sem hover / enabled) |
| --ez-radio-button__form-radio--checked--color | cor do radio selecionado (com seleção / sem foco / sem hover / enabled) |
| --ez-radio-button__form-radio--disabled--border-color | cor da borda do radio quando está desativado (sem seleção / sem foco / sem hover / disabled) |
| --ez-radio-button__form-radio--disabled--background-color | cor do background do radio quando está desativado (sem seleção / sem foco / sem hover / disabled) |
| --ez-radio-button__form-radio--disabled--color | cor da label quando o radio está desativado (sem seleção / sem foco / sem hover / disabled) |
| --ez-radio-button__form-radio--disabled--before--background-color | cor do centro do radio quando o radio está desativado (com seleção / sem foco / sem hover / disabled) |
| --ez-radio-button__form-radio--focus--background-color | cor do background quando o radio está ativado e sem seleção (sem seleção / com foco / sem hover / enabled) |
| --ez-radio-button__form-radio--checked--box-shadow-color | cor do box-shadow quando o radio está ativado e sem seleção (sem seleção / com foco / sem hover / enabled) |
| --ez-radio-button__form-radio--checked--focus--background-color | cor do background quando o radio está marcado e com foco (com seleção / com foco / sem hover / enabled) |
| --ez-radio-button__form-radio--checked--focus--box-shadow-color | cor do background quando o radio está marcado e com foco (com seleção / com foco / sem hover / enabled) |
| --ez-radio-button__form-radio--checked--hover--background-color | cor do background quando o radio está marcado, com foco e com hover (com seleção / com foco / com hover / enabled) |
| --ez-radio-button__form-radio--checked--hover--box-shadow-color | cor do box-shadow quando o radio está marcado, com foco e com hover (com seleção / com foco / com hover / enabled) |
| --ez-radio-button__form-radio--hover--box-shadow-color | cor do hover quando o radio está desmarcado (sem seleção / sem foco / com hover / enabled) |
| --ez-radio-button__form-radio--checked--disabled--hover--background-color | cor do fundo quando o radio está marcado e desativado (com seleção / sem foco / com hover / disabled) |
