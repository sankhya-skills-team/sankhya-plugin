> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-number-input/ (snapshot 2026-09-28)

# Number input

demo.js

```jsx
import React from 'react';
import { EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzNumberInput label="Valor numérico:" value={12.5} precision="2" />
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Inverted

Em backgrounds escuros os inputs devem mudar de aparência para o modo "inverted" melhorando o contraste.

### Desabilitado

Campo indisponível para uso.

demo.js

```jsx
import React from 'react';
import { EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzNumberInput label="Desabilitado:" value={12} enabled="false" />
        </div>
    )
};

export default Demo;
```

### Com estado de erro

Quando há um problema de validação, serve como orientação ao usuário.

demo.js

```jsx
import React from 'react';
import { EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzNumberInput label="Com mensagem de erro:" errorMessage="Atribuída pelo atributo errorMessage." />
        </div>
    )
};

export default Demo;
```

### Modo slim

Modo reduzido do tamanho do campo.

### Precision e Pretty Precision

Existem duas propriedades para influenciar a precisão dos campos numéricos.
"precision" determina o arredondamento do valor.
"prettyPrecision" influencia a apresentação do campo, dando preferência ao menor número de casas decimais.

demo.js

```jsx
import React from 'react';
import { EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <div className="ez-col--sd-4">
                <EzNumberInput
                    label="Com pretty precision:"
                    value={12.5}
                    precision="10"
                    prettyPrecision={1}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding-left--large">
                <EzNumberInput
                    label="Sem pretty precision:"
                    value={12.5}
                    precision="10"
                />
            </div>
        </div>
    )
};

export default Demo;
```

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática temos os métodos "setFocus()" e "setBlur()".

O exemplo abaixo demonstra isso através do botão **Focar campo**. Clicando nesse botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

Focado: **Não**

#### isInvalid()

Retorna informando se o campo está inválido (true | false).

Valor válido

demo.js

```jsx
import React, { useState } from 'react';
import { EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isInvalid, setIsInvalid] = useState(false);

    const onBlur = element => {
        element.isInvalid().then(value => {
            setIsInvalid(value);
        });
    };

    return (
        <div className="ez-row">
            <div className="ez-col ez-col--sd-4">
                <EzNumberInput label="Valor numérico:" precision="2" onBlur={evt => onBlur(evt.target)} />
            </div>
            <div className="ez-row">
                <label>{isInvalid ? "Valor inválido" : "Valor válido"}</label>
            </div>
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### ezChange

Evento disparado ao mudar o estado do componente (onEzChange).

Valor: ****

#### ezStartChange

Evento emitido ao iniciar a alteração.

Aguardando Alteração: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isWaiting, setIsWaiting] = useState(false);

    const onStartChange = (evt) => {
        setIsWaiting(evt && Object.keys(evt.detail).includes("waitmessage"));
    };

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzNumberInput
                    label="Título do campo"
                    onBlur={onStartChange}
                    onEzStartChange={onStartChange}
                />
            </div>

            <label>
                Aguardando Alteração: <strong>{isWaiting ? "Sim" : "Não"}</strong>
            </label>
        </div>
    )
};

export default Demo;
```

#### ezCancelWaitingChange

Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é disparado.

Alteração Cancelada: **Não**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| allowNegative | allow-negative | Se false, o input não aceitará números negativos. | boolean | true |
| alternativePlaceholder | alternative-placeholder | Texto alternativo a ser apresentado como título do campo. | string | undefined |
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| enabled | enabled | Se false, o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| precision | precision | Define quantas casas decimais serão exibidas. Caso haja mais casas haverá arredondamento. | number | undefined |
| prettyPrecision | pretty-precision | Define qual é o mínimo de casas depois da vírgula. Exemplo: 1,1 será exibido como 1,1000 quando prettyPrecision = 4 . | number | undefined |
| value | value | Define o valor do campo. | number | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezCancelWaitingChange | Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. | CustomEvent<void> |
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<number> |
| ezInput | Emitido quando o usuário digita no campo. | CustomEvent<number> |
| ezStartChange | Emitido ao iniciar a alteração (digitação incompleta). | CustomEvent<WaitingChange> |

### Methods

#### `getValueAsync() => Promise<number>`

##### Returns

Type: `Promise<number>`

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

### CSS Variables

| Variable | Description |
|---|---|
| --ez-number-input__min-width | Define a largura maxima do componente. |
| --ez-number-input__max-width | Define a largura minima do componente. |
