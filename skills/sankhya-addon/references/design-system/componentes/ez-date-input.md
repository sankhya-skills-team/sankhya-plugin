> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input/ (snapshot 2026-09-28)

# DateInput

Popup de seleção de data, date time e intervalos de data.

Documentação do componente EzDateInput.

demo.js

```jsx
import React from 'react';
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateInput label="Título do campo"></EzDateInput>
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
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateInput
                label="Título do campo"
                className="ez-input--inverted">
            </EzDateInput>
        </div>
    )
};

export default Demo;
```

### Valor inicial

Exemplo de data inicial inserida no componente.

### Habilitado

Campo disponível para uso.

demo.js

```jsx
import React from 'react';
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateInput
                label="Título do campo"
                enabled="true">
            </EzDateInput>
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
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateInput
                label="Título do campo"
                errorMessage="Mensagem de erro.">
            </EzDateInput>
        </div>
    )
};

export default Demo;
```

### Modo slim

Modo reduzido do tamanho do campo.

### Modo regular (default)

Modo padrão do tamanho do campo.

demo.js

```jsx
import React from 'react';
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzDateInput
                label="Título do campo"
                mode="regular">
            </EzDateInput>
        </div>
    )
};

export default Demo;
```

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática temos os métodos `setFocus()` e `setBlur()`.

O exemplo abaixo demonstra isso através do botão **Focar Campo**. Clicando nesse botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

Focado: **Não**

#### isInvalid()

Retorna informando se o campo está inválido (true | false).

Inválido: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isInvalid, setIsInvalid] = useState(false);

    const onBlur = element => element.isInvalid().then(setIsInvalid);

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzDateInput
                    label="Título do campo"
                    onBlur={evt => onBlur(evt.target)}>
                </EzDateInput>
            </div>

            <div className="ez-flex ez-flex--column ez-flex--align-items-center">
                <label>
                    Inválido: <strong>{isInvalid ? "Sim" : "Não"}</strong>
                </label>
            </div>
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do componente (onEzChange).

Valor: ****

#### ezStartChange()

Evento emitido ao iniciar a alteração.

Aguardando Alteração: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzDateInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isWaiting, setIsWaiting] = useState(false);

    const onStartChange = (evt) => {
        setIsWaiting(evt && Object.keys(evt.detail).includes("waitmessage"));
    };

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzDateInput
                    label="Título do campo"
                    onBlur={onStartChange}
                    onEzStartChange={onStartChange}>
                </EzDateInput>
            </div>

            <label>
                Aguardando Alteração: <strong>{isWaiting ? "Sim" : "Não"}</strong>
            </label>
        </div>
    )
};

export default Demo;
```

#### ezCancelWaitingChange()

Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é disparado.

Alteração Cancelada: **Não**

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
| value | -- | Define o valor do campo. | Date | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezCancelWaitingChange | Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. | CustomEvent<void> |
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<Date> |
| ezInput | Emitido quando o usuário digita uma data válida no campo. | CustomEvent<Date> |
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
