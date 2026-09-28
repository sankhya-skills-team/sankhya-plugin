> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-actions-button/ (snapshot 2026-09-28)

# Actions Button

AbacaxiPêraLaranja

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzActionsButton>
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Habilitado

Utilizado nos momentos em que o usuário pode interagir com os botões. Se a propriedade `enabled` não for passada, será habilitado como comportamento padrão.

AbacaxiPêraLaranja

### Desabilitado

Utilizado nos momentos em que o usuário não pode interagir com os botões.

AbacaxiPêraLaranja

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzActionsButton enabled="false">
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

### Tamanhos

#### Small

AbacaxiPêraLaranja

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzActionsButton size="small">
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

#### Medium

AbacaxiPêraLaranja

#### Large

AbacaxiPêraLaranja

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzActionsButton size="large">
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

#### Todos os tamanhos

Colocando todos os tamanhos lado a lado para comparação.

AbacaxiPêraLaranjaAbacaxiPêraLaranjaAbacaxiPêraLaranja

### Com label

Define se o label do item selecionado será apresentado no display do componente.

AbacaxiPêraLaranja

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzActionsButton showLabel="true">
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

### Com ícone

Quando for utilizar ícone, deve-se passar a informação de qual ícone será utilizado.

AbacaxiPêraLaranja

### Com checkOption

Define se na opção selecionada apresentará um ícone de check.

AbacaxiPêraLaranja

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzActionsButton checkOption="true">
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

### Altura máxima

Definindo a altura máxima que a lista de actions pode atingir.

### Com lista de ações (actions)

Define um array com a lista de ações. Os elementos devem obedecer o formato: `{value: string, label: string}`

demo.js

```jsx
import React from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const actions = [
        {value: "1", label: "Opção 1"},
        {value: "2", label: "Opção 2"},
        {value: "3", label: "Opção 3"}
    ];

    return (
        <div className="ez-flex">
            <EzActionsButton actions={actions}></EzActionsButton>
        </div>
    )
};

export default Demo;
```

### Desabilitar item de menu (actions)

Para desabilitar um item específico, basta definir o valor `false` para o atributo `enabled`.

### Principais métodos

#### hideActions()

Oculta a lista de ações.

Observação

No exemplo abaixo, ao clicar no botão disponível, a lista de ações será exibida, após 2 segundos será chamado o médodo **hideActions()** , e então a lista será ocultada automaticamente.

AbacaxiPêraLaranja

demo.js

```jsx
import React, { useRef } from 'react';
import { EzActionsButton, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = new useRef(null);

    function onHide() {
        // O timeout abaixo serve para demonstrar a chamada
        // do médodo hideActions() apos o tempo de 2 segundos.
        setTimeout(() => {
            element.current.hideActions();
        }, 2000);
    }

    return (
        <div className="ez-flex" onClick={onHide}>
            <EzActionsButton ref={element}>
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>
        </div>
    )
};

export default Demo;
```

#### isOpened()

Verifica se a lista de ações está oculta.

AbacaxiPêraLaranja

### Exemplos de eventos

#### ezAction()

Evento disparado ao acionar uma ação.

AbacaxiPêraLaranjaOpção Selecionada: **Selecione uma opção...**

demo.js

```jsx
import React, { useState } from 'react';
import { EzActionsButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [action, setAction] = useState(undefined);

    const onAction = (evt) => {
        setAction(evt.detail);
    };

    return (
        <div className="ez-flex ez-flex--column">
            <EzActionsButton onEzAction={onAction}>
                <action value="A">Abacaxi</action>
                <action value="P">Pêra</action>
                <action value="L">Laranja</action>
            </EzActionsButton>

            <label className="ez-margin-horizontal--auto ez-margin-top--medium">
                Opção Selecionada: <strong>{action ? JSON.stringify(action) : "Selecione uma opção..."}</strong>
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
| actions | -- | Define a lista de ações. Os elementos devem obedecer o formato: {value: string, label: string} . | IAction[] | undefined |
| arrowActive | arrow-active | Se true a seta de ordenação será apresentada. | boolean | false |
| checkOption | check-option | Se true o check será apresentado para os itens. | boolean | false |
| displayIcon | display-icon | Define o ícone do componente. | string | undefined |
| enabled | enabled | Se false o usuário não pode interagir com o componente. | boolean | true |
| isTransparent | is-transparent | Se true o background será transparent. | boolean | false |
| showLabel | show-label | Se true o label será apresentado. | boolean | false |
| size | size | Determina o tamanho do ez-action-button. | "large" \| "medium" \| "small" | "medium" |
| value | value | Define o valor do componente. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezAction | Emitido ao acionar uma ação. | CustomEvent<IAction> |
| ezDisconnectedActionButtons | Emitido quando componente é desconectado da DOM | CustomEvent<void> |
| ezPopoverOpen | Emitido ao mostrar a lista de ações | CustomEvent<HTMLElement> |

### Methods

#### `hideActions() => Promise<void>`

Oculta a lista de ações.

##### Returns

Type: `Promise<void>`

#### `isOpened() => Promise<boolean>`

Verifica se a lista de ações está aberta.

##### Returns

Type: `Promise<boolean>`

#### `showActions() => Promise<void>`

Apresenta a lista de ações.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-button
  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-actions-button__actions-list--border-radius | Define o raio da borda do popover. |
| --ez-actions-button__actions-list--box-shadow | Define a sombra do popover. |
| --ez-actions-button__actions-list--background-color | Define a cor de fundo do popover. |
| --ez-actions-button__actions-list--padding | Define o espaçamento interno do popover |
| --ez-actions-button__actions-list--top-margin | Define a distancia entre o botão e o popover |
| --ez-actions-button__actions-list--z-index | Define a elevação do popover. |
| --ez-actions-button__actions-max-height | Define a altura máxima do popover. |
| --ez-actions-button__btn-action--min-width | Define a largura mínima do popover |
| --ez-actions-button__btn-action--background-color | Define a cor de fundo do popover |
