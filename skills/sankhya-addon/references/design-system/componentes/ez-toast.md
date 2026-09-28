> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-toast/ (snapshot 2026-09-28)

# Toast

Toasts são elementos de notificação não-modais, baseados em tempo de duração, usados para exibir mensagens curtas. Eles, geralmente, aparecem em algum lugar da tela sobrepondo todos os elementos (flutuantes) e desaparecem após alguns segundos.

demo.js

```jsx
import React, {useRef} from 'react';
import { EzToast, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const showToast = () => {
        element.current.show("Toast Demo", 2000, true, true);
    };

    return (
        <>
            <EzToast ref={element} />
            <EzButton label="Exibir Toast" className="ez-margin-top--medium" onClick={showToast} />
        </>
    )
};

export default Demo;
```

## Variações e estados.

### Mensagem exibida.

demo.js

```jsx
import React, {useRef} from 'react';
import { EzToast, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const showToast = () => {
        element.current.show();
    };

    return (
        <>
            <EzToast ref={element} message="Toast demo message" />
            <EzButton
                label="Exibir Toast"
                className="ez-margin-top--medium"
                onClick={showToast}
            />
        </>
    )
};

export default Demo;
```

### Tempo de exibição.

### Adiciona ícone de check.

demo.js

```jsx
import React, {useRef} from 'react';
import { EzToast, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const showToast = () => {
        element.current.show("Toast demo useIcon");
    };

    return (
        <>
            <EzToast ref={element} useIcon={true}>
                <EzIcon slot="icon" iconName="check" />
            </EzToast>
            <EzButton
                label="Exibir Toast"
                className="ez-margin-top--medium"
                onClick={showToast}
            />
        </>
    )
};

export default Demo;
```

### Uso do ícone de fechar.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| canClose | can-close | Se false, o usuário não consegue fechar. | boolean | true |
| fadeTime | fade-time | Define o tempo de exibição em milissegundos. | number | 5000 |
| message | message | Mensagem a ser exibida no componente. | string | undefined |
| useIcon | use-icon | Se true permite a utilização do slot de ícone. | boolean | false |

### Methods

#### `show(message: string, fadeTime: number, useIcon: boolean, canClose?: boolean) => Promise<void>`

Exibe o ez-toast.

##### Returns

Type: `Promise<void>`

### CSS Variables

| Variable | Description |
|---|---|
| --ez-toast__btn__close__image | Contém o ícone de fechamento do toast. |
| --ez-toast__container--z-index | Define a camada em que o container será exibido. |
| --ez-toast__container--background-color | Define a cor de fundo do container. |
| --ez-toast__container--left | Define a posição esquerda do container. |
| --ez-toast__container--bottom | Define a posição inferior do container. |
| --ez-toast__container--width | Define a largura do container. |
| --ez-toast__icon--padding-left | Define o espaçamento à esquerda do ícone. |
