> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-time-input/ (snapshot 2026-09-28)

# DateTimeInput

Documentação do componente EzDateTimeInput.

demo.js

```jsx
import React from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateTimeInput label="Título do campo"></EzDateTimeInput>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Inverted

Em backgrounds escuros os inputs devem mudar de aparência para o modo `inverted` melhorando o contraste.

demo.js

```jsx
import React from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateTimeInput
                label="Título do campo"
                className="ez-input--inverted">
            </EzDateTimeInput>
        </div>
    )
};

export default Demo;
```

### Inserir valor inicial

Exemplo de data inicial inserida no componente.

### Habilitado

Campo disponível para uso.

demo.js

```jsx
import React from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateTimeInput
                label="Título do campo"
                enabled="true">
            </EzDateTimeInput>
        </div>
    )
};

export default Demo;
```

### Desabilitado

Campo indisponível para uso.

### Com estado de erro

Quando há um problema de validação, serve como orientação ao usuário.

demo.js

```jsx
import React from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateTimeInput
                label="Título do campo"
                errorMessage="Mensagem de erro.">
            </EzDateTimeInput>
        </div>
    )
};

export default Demo;
```

### Com segundos

Exibe os segundos no input.

### Modo slim

Modo reduzido do tamanho do campo.

demo.js

```jsx
import React from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateTimeInput
                label="Título do campo"
                mode="slim">
            </EzDateTimeInput>
        </div>
    )
};

export default Demo;
```

### Modo regular (default)

Modo padrão do tamanho do campo.

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática temos os métodos `setFocus()` e `setBlur()`.

O exemplo abaixo demonstra isso através do botão **Focar Campo**. Clicando nesse botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

Focado: **Não**

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzDateTimeInput, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [isFocus, setIsFocus] = useState(false);

    const onFocus = () => {
        element.current.setFocus();

        // O timeout abaixo serve para demonstrar a remoção do foco
        // apos o tempo de 2 segundos.
        setTimeout(()=>{
            element.current.setBlur();
        }, 2000);
    };

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzDateTimeInput
                    ref={element}
                    label="Título do campo"
                    onBlur={() => setIsFocus(false)}
                    onFocus={() => setIsFocus(true)}>
                </EzDateTimeInput>
            </div>

            <div className="ez-flex ez-flex--column ez-flex--align-items-center">
                <label className="ez-margin-bottom--medium">
                    Focado: <strong>{isFocus ? "Sim" : "Não"}</strong>
                </label>

                <EzButton
                    label="Focar Campo"
                    onClick={onFocus}>
                </EzButton>
            </div>
        </div>
    )
};

export default Demo;
```

#### isInvalid()

Retorna informando se o campo está inválido (true | false).

Inválido: **Não**

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do componente (onEzChange).

Valor: ****

demo.js

```jsx
import React, { useState } from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [value, setValue] = useState(null);

    const onChange = evt => setValue(evt.detail);

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzDateTimeInput
                    label="Título do campo"
                    onEzChange={onChange}>
                </EzDateTimeInput>
            </div>

            <label>
                Valor: <strong>{value?.toString()}</strong>
            </label>
        </div>
    )
};

export default Demo;
```

#### ezStartChange()

Evento emitido ao iniciar a alteração.

Aguardando Alteração: **Não**

#### ezCancelWaitingChange()

Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é disparado.

Alteração Cancelada: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzDateTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isCanceled, setIsCanceled] = useState(false);

    const onCancelWaitingChange = evt => setIsCanceled(evt && evt.detail === null);

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzDateTimeInput
                    label="Título do campo"
                    onInput={onCancelWaitingChange}
                    onEzCancelWaitingChange={onCancelWaitingChange}>
                </EzDateTimeInput>
            </div>

            <label>
                Alteração Cancelada: <strong>{isCanceled ? "Sim" : "Não"}</strong>
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
| alternativePlaceholder | alternative-placeholder | Texto alternativo ser apresentado como título do campo. | string | undefined |
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| showSeconds | show-seconds | Se true considera segundos. | boolean | false |
| value | -- | Define o valor do campo. | Date | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezCancelWaitingChange | Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. | CustomEvent<void> |
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<Date> |
| ezStartChange | Emitido ao iniciar a alteração (digitação incompleta). | CustomEvent<WaitingChange> |

### Methods

#### `getValueAsync() => Promise<Date>`

##### Returns

Type: `Promise<Date>`

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

  * ez-form-view

#### Depends on

  * ez-text-input
  * ez-popover-plus
  * ez-calendar

### CSS Variables

| Variable | Description |
|---|---|
| --ez-date-input__input--background-color | Define a cor de fundo do input. |
| --ez-date-input__input--border-color | Define a cor da borda do input. |
| --ez-date-input__calendar-image | Contém a imagem do calendário. |
