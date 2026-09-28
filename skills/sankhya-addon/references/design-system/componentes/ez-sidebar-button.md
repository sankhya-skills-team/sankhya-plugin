> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-button/ (snapshot 2026-09-28)

# Sidebar Button

O componente se trata de uma ação para expandir menu laterais que estejam recolhidos/ocultos.

```jsx
import './demo.css';

import React from 'react';
import { EzSidebarButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="sidebarButton__container">
            <EzSidebarButton />
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### ezClick()

Evento disparado ao clicar no componente.

## Evento emitido

Evento: "ezClick"

demo.js

```jsx
import './demo.css';

import React, { useRef, useState } from 'react';
import { EzSidebarButton, EzModal, EzModalContainer } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
    const [opened, setOpened] = useState(false);
    const modal = useRef();
    const size = "col--sd-3";

    const showModal = align => {
        setOpened(true);
        modal.current.modalSize = size;
        modal.current.opened = opened;
        modal.current.align = align;
    }

    return (
        <div>
            <EzModal
                opened={opened}
                ref={modal}
                closeEsc={true}
                value={size}>
                <EzModalContainer
                    modalTitle="Evento emitido"
                    cancelButtonLabel="cancelar"
                    okButtonLabel="OK"
                    onEzModalAction={() => setOpened(false)}
                >
                    Evento: "ezClick"
                </EzModalContainer>
            </EzModal>
            <div className="ez-row sidebarButton__container">
                <EzSidebarButton label="Mostrar à esquerda" onClick={() => showModal("left")} />
            </div>
        </div>
    );
};

export default Demo;
```

## API do componente

### Events

| Event | Description | Type |
|---|---|---|
| ezClick | Emitido sempre que o ez-sidebar-button é clicado. | CustomEvent<void> |

### Dependencies

#### Used by

  * ez-guide-navigator
  * ez-sidebar-navigator

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-sidebar-button--width | Define a largura do span do botão. |
| --ez-sidebar-button--hover--width | Define a largura do span do botão quando passar o mouse em cima. |
| --ez-sidebar-button--height | Define a altura do span do botão. |
| --ez-sidebar-navigator-button--z-index | Define a camada em que o componente será exibido. |
| --ez-sidebar-button--background-color--xlight | Define a cor de fundo do botão. |
| --ez-sidebar-button--background-color--primary | Define a cor de fundo do span do botão. |
| --ez-sidebar-button--space--small | Define um espaçamento pequeno entre elementos do componente. |
| --ez-sidebar-button--space--medium | Define um espaçamento mediano entre elementos do componente. |
| --ez-sidebar-button--box-shadow | Define a sombra default do botão. |
| --ez-sidebar-button--hover--box-shadow | Define a sombra do botão quando passar o mouse em cima. |
| --ez-sidebar-button--border--radius-small | Define a borda arrendondada no valor de 6px. |
| --ez-sidebar-button--border--radius-medium | Define a borda arrendondada no valor de 12px. |
