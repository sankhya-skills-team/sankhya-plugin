> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-time-input/ (snapshot 2026-09-28)

# Time Input

demo.js

```jsx
import React from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTimeInput />
);

export default Demo;
```

## Variações e estados

### Deixa o campo disponível.

### Deixa o campo indisponível.

demo.js

```jsx
import React from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTimeInput label="Campo desabilitado" enabled={false} />
);

export default Demo;
```

### Label.

demo.js

```jsx
import React from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTimeInput label="Label do campo" />
);

export default Demo;
```

### Com estado de erro.

### Modo regular.

demo.js

```jsx
import React from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzTimeInput label="Campo no modo regular" mode="regular" />
);

export default Demo;
```

### Modo slim.

### Exibe ou não os segundos no calendário.

demo.js

```jsx
import React from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTimeInput label="Exibe os segundos" showSeconds={true} />
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
import { EzTimeInput} from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const removeFocus = () => {
        setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <>
            <EzTimeInput
                ref={element}
                label="Título do campo"
                onFocus={removeFocus}
            >
            </EzTimeInput>

            <label>O foco será removido automaticamente após 2 segundos</label>
        </>
    );
}

export default Demo;
```

### Informa se o campo está inválido.

Inválido: **Não**

## Exemplos de eventos.

### Ao mudar o estado do componente.

**Valor Alterado:**

demo.js

```jsx
import React, { useState } from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [value, setValue] = useState(null);

    const onChange = (evt) => setValue(evt.detail);

    return (
        <>
            <EzTimeInput label="Título do campo" onEzChange={onChange} />
            <label>
                <b>Valor Alterado: </b> {value?.toString()}
            </label>
        </>
    );
}

export default Demo;
```

### Ao iniciar a alteração.

Aguardando Alteração: **Não**

### Ao interromper alteração.

Alteração Cancelada: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzTimeInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isCanceled, setIsCanceled] = useState(false);

    const onCancelWaitingChange = (evt) => {
        setIsCanceled(evt && evt.detail === null);
    };

    return (
        <>
            <EzTimeInput onEzCancelWaitingChange={onCancelWaitingChange} />

            <label>
                Alteração Cancelada: <strong>{isCanceled ? "Sim" : "Não"}</strong>
            </label>
        </>
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
| value | value | Define o valor do campo. | number | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezCancelWaitingChange | Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. | CustomEvent<void> |
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<number> |
| ezStartChange | Emitido ao iniciar a alteração (digitação incompleta). | CustomEvent<WaitingChange> |

### Methods

#### `isInvalid() => Promise<boolean>`

Retorna se o conteúdo é inválido.

##### Returns

Type: `Promise<boolean>`

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus({ selectText }: TFocusOptions) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form-view

#### Depends on

  * ez-text-input
  * ez-icon
