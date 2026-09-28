> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-edit/ (snapshot 2026-09-28)

# Text Edit

Os inputs permitem que os usuários insiram dados de texto de formato livre. O tipo de campo utilizado deve refletir o cumprimento do conteúdo que você espera que o usuário insira. Esse input padrão é para conteúdo curto de uma linha.

demo.js

```jsx
import React from 'react';
import { EzTextEdit } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTextEdit value="Título do Campo"/>
);

export default Demo;
```

## Exemplos de métodos.

demo.js

```jsx
import React, {useRef} from 'react';
import { EzTextEdit, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const applyFocusSelect = () => {
        element.current.applyFocusSelect();
    };

    return (
        <>
            <EzTextEdit ref={element} value="Título do Campo"/>
            <EzButton
                label="Aplicar foco no campo"
                className="ez-margin-top--medium"
                onClick={applyFocusSelect}
            />
        </>
    )
};

export default Demo;
```

## Exemplos de eventos.

### Evento emitido ao salvar uma edição.

### Disparado ao cancelar uma edição.

demo.js

```jsx
import React, {useRef} from 'react';
import { EzTextEdit, EzToast } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezToastElement = useRef(null);

    const  cancelEdition = () => {
        ezToastElement.current.show("Evento cancelEdition disparado");
    }

    return (
        <>
            <EzTextEdit value="Título do Campo" onCancelEdition={cancelEdition}/>
            <EzToast ref={ezToastElement} />
        </>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| styled | -- | Define atributos do estilo. | IStyled | undefined |
| value | value | Define o valor do campo. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| cancelEdition | Emitido ao cancelar uma edição | CustomEvent<any> |
| saveEdition | Emitido ao salvar uma edição | CustomEvent<any> |

### Methods

#### `applyFocusSelect() => Promise<void>`

Aplica foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-collapsible-box

#### Depends on

  * ez-text-input
  * ez-button
