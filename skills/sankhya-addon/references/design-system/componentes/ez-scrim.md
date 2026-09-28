> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-scrim/ (snapshot 2026-09-28)

# Scrim

## Utilização

Este componente trata-se de um utilitário CSS que aplica estilos de sobreposição na página.

## Variações

### Modo light

Com a utilização das classes `ez-scrim ez-scrim-light`, este modo aplica opacidade de 10% ao componente de sobreposição.

Clique em qualquer lugar da tela para fechar a sobreposição..

demo.js

```jsx
import React, { useRef } from "react";
import { EzButton, EzPopover } from "@sankhyalabs/ezui/react/components";

const Light = () => {
    const popover = useRef();

    const handlePopover = () => {
        popover.current.show();
    }

    return (
        <section>
            <EzButton label="Abrir componente com sobreposição" onClick={handlePopover} />
                <EzPopover ref={popover}>
                    <div className="ez-padding--large">
                        <label>Clique em qualquer lugar da tela para fechar a sobreposição..</label>
                    </div>
                </EzPopover>
        </section>
    )
};

export default Light;
```

### Modo medium

Com a utilização das classes `ez-scrim ez-scrim-medium`, este modo aplica opacidade de 40% ao componente, além de aplicar filtro **blur** com valor de `4px`.

Clique em qualquer lugar da tela para fechar a sobreposição..

demo.js

```jsx
import React, { useRef } from "react";
import { EzButton, EzPopover } from "@sankhyalabs/ezui/react/components";

const Medium = () => {
    const popover = useRef();

    const handlePopover = () => {
        popover.current.show();
    }

    return (
        <section>
            <EzButton label="Abrir componente com sobreposição" onClick={handlePopover} />
                <EzPopover ref={popover} overlayType="medium">
                    <div className="ez-padding--large">
                        <label>Clique em qualquer lugar da tela para fechar a sobreposição..</label>
                    </div>
                </EzPopover>
        </section>
    )
};

export default Medium;
```
