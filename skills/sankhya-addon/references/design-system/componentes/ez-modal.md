> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal/ (snapshot 2026-09-28)

# Modal

## Título

Embora o conteúdo seja livre, é recomendável usar um EzModalContainer por facilidade de uso e padronização.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzModal, EzModalContainer } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [opened, setOpened] = useState(false);
    const modal = useRef();

    const showModal = align => {
        setOpened(true);
        modal.current.align = align;
        modal.current.opened = opened;
    }

    return (
        <div>
            <EzModal opened={opened} ref={modal} closeEsc={true}>
                <EzModalContainer
                    modalTitle="Título"
                    cancelButtonLabel="cancelar"
                    okButtonLabel="OK"
                    onEzModalAction={()=>setOpened(false)}
                >
                    Embora o conteúdo seja livre, é recomendável usar um EzModalContainer por facilidade de uso e padronização.
                </EzModalContainer>
            </EzModal>
            <div className="ez-row">
                <EzButton className="ez-margin--small" label="Mostrar à esquerda" onClick={()=>showModal("left")}/>
                <EzButton className="ez-margin--small" label="Mostrar à direita" onClick={()=>showModal("right")}/>
            </div>
        </div>
    )
};

export default Demo;
```

## Altura do Modal

A propriedade `heightMode` controla o comportamento de altura do Modal, permitindo definir o modo `regular` ou `full`. O modo `regular` possui altura padrão para conteúdo compacto, enquanto o modo `full` expande o Modal verticalmente, ocupando todo o espaço disponível na tela.

## Título

A propriedade **heightMode** controla o comportamento de altura do Modal, permitindo definir o modo **regular** ou **full**.

## Tamanho ocupado

A prop `modalSize` define o tamanho do componente ez-modal, permitindo especificar o tamanho desejado seguindo o grid-layout. Desse modo, é possível utilizar classes de dimensionamento, como `col-sd-3`, para determinar o tamanho do modal.

Os tamanhos podem ser definidos de 1 a 12 colunas, sendo que 12 corresponde à área total disponível.

**Selecionado: col--sd-3**

1 coluna2 colunas3 colunas4 colunas5 colunas6 colunas7 colunas8 colunas9 colunas10 colunas11 colunas12 colunas

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzModal, EzComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [opened, setOpened] = useState(false);
    const [size, setSize] = useState("col--sd-3");
    const modal = useRef();

    const showModal = () => {
        setOpened(true);
        modal.current.modalSize = size;
        modal.current.opened = opened;
    }

    return (
        <div>
            <EzModal opened={opened} ref={modal} closeEsc={true}>
                <label>
                    Os tamanhos podem ser definidos de 1 a 12 colunas,
                    sendo que 12 corresponde à área total disponível.<br/><br/>
                    <strong>Selecionado: {size}</strong>
                </label>
                <div className="ez-row  ez-flex--align-items-end ez-flex--justify-end">
                    <EzButton className="ez-button--primary" label="OK" onClick={()=>setOpened(false)}/>
                </div>
            </EzModal>
            <div className="ez-row">
                <EzComboBox label="Tamanho:" value={size} onEzChange={evt => setSize(evt.detail?.value)} >
                    <option value="col--sd-1">1 coluna</option>
                    <option value="col--sd-2">2 colunas</option>
                    <option value="col--sd-3">3 colunas</option>
                    <option value="col--sd-4">4 colunas</option>
                    <option value="col--sd-5">5 colunas</option>
                    <option value="col--sd-6">6 colunas</option>
                    <option value="col--sd-7">7 colunas</option>
                    <option value="col--sd-8">8 colunas</option>
                    <option value="col--sd-9">9 colunas</option>
                    <option value="col--sd-10">10 colunas</option>
                    <option value="col--sd-11">11 colunas</option>
                    <option value="col--sd-12">12 colunas</option>
                </EzComboBox>
                <EzButton label="Mostrar modal" onClick={()=>showModal()}/>
            </div>
        </div>
    )
};

export default Demo;
```

## Scrim

A prop `scrim` define o tipo de overlay a ser aplicado no backdrop do modal, podendo alterar entre `medium` ou `light`.

## Título

A propriedade **scrim** controla o overlay do modal, permitindo definir **medium** ou **light**.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzModal, EzModalContainer } from '@sankhyalabs/ezui/react/components';

const scrim = () => {
    const [opened, setOpened] = useState(false);
    const modal = useRef();

    const showModal = (scrim) => {
        modal.current.scrim = scrim;
        modal.current.opened = opened;
        setOpened(true);
    }

    return (
        <div>
            <EzModal opened={opened} modalSize={"col--sd-3"} ref={modal} closeEsc={true}>
                <EzModalContainer
                    modalTitle="Título"
                    cancelButtonLabel="cancelar"
                    okButtonLabel="OK"
                    onEzModalAction={()=>setOpened(false)}
                >
                    A propriedade <b>scrim</b> controla o overlay do modal, permitindo definir <b>medium</b> ou <b>light</b>.
                </EzModalContainer>
            </EzModal>
            <div className="ez-row">
                <EzButton className="ez-margin--small" label="Scrim medium" onClick={()=>showModal("medium")}/>
                <EzButton className="ez-margin--small" label="Scrim light" onClick={()=>showModal("light")}/>
            </div>
        </div>
    )
};

export default scrim;
```

## Fechamento automático

Existem duas opções para fechar o modal automaticamente:

  * closeEsc = true: Habilitando esta opção, a tecla "ESC" faz com que o modal seja fechado.
  * closeOutsideClick = true: Se Habilitada, esta opção fecha o modal ao clicar fora do conteúdo.
Podem ser habilitadas simultaneamente.

Teste com a habilidade de fechar automaticamente. Experimente clicar fora do conteúdo e pressionar a tecla **ESC** do teclado.
**Fechar com ESC: Desabilitado**
**Fechar com clique: Desabilitado**

## Eventos

Sempre que o modal é exibido ou ocultado os eventos ezOpenModal e ezCloseModal são emitidos repectivamente.

Teste com a habilidade de fechar automaticamente. Experimente clicar fora do conteúdo e pressionar a tecla **ESC** do teclado.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzModal } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const [opened, setOpened] = useState(false);
    const modal = useRef();

    const showModal = () => {
        setOpened(true);
        modal.current.closeEsc=true;
        modal.current.closeOutsideClick=true;
        modal.current.opened = opened;
    }

    const showEvent = (eventName) => {
       ApplicationUtils.message("Evento emitido", eventName);
    }

    return (
        <div>
            <EzModal
                ref={modal}
                onEzOpenModal={()=>showEvent("ezOpenModal")}
                onEzCloseModal={()=>showEvent("ezCloseModal")}
                opened={opened}
                closeEsc={true}
                closeOutsideClick={true}
                key="demo.events"
            >
               <label>
                    Teste com a habilidade de fechar automaticamente.
                    Experimente clicar fora do conteúdo e pressionar
                    a tecla <strong>ESC</strong> do teclado.
                </label>
            </EzModal>
            <div className="ez-row">
                <EzButton label="Mostrar modal" onClick={()=>showModal()}/>
            </div>
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| align | align | Define o alinhamento do ez-modal. | "left" \| "right" | undefined |
| closeEsc | close-esc | Define se o ez-modal será fechado ao clicar ESC . | boolean | false |
| closeOutsideClick | close-outside-click | Define se o modal será fechado ao clicar fora do conteúdo. | boolean | false |
| closeOutsideLeave | close-outside-leave | Define se o modal será fechado se o mouse sair para fora do conteúdo. | boolean | false |
| heightMode | height-mode | Ativa o modo Full, permitindo que o Modal expanda-se verticalmente e ocupe todo o espaço disponível. | "full" \| "regular" | "regular" |
| modalSize | modal-size | Define o tamanho do ez-modal. Devem ser definidas seguindo grid-layout. Exemplo: col-sd-3 . | string | undefined |
| opened | opened | Define se o ez-modal está aberto. | boolean | true |
| scrim | scrim | Define o tipo de scrim a ser aplicado no overlay do modal | "light" \| "medium" \| "none" | "medium" |

### Events

| Event | Description | Type |
|---|---|---|
| ezCloseModal | Emitido quando o modal é fechado. | CustomEvent<boolean> |
| ezModalAction | Representa a interação com o usuário. OK - Quando o botão é acionado CANCEL - Quando o botão de cancelar é acionado CLOSE - Quando o botão de fechar é acionado. LOAD - Quando o modal é carregado (eventualmente pode ser usado para dar foco a um elemento específico) | CustomEvent<string> |
| ezOpenModal | Emitido quando o modal é aberto. | CustomEvent<any> |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-modal-z-index | Define a camada em que o componente será exibido. |
| --ez-modal-vertical-padding | Define o espaçamento vertical do conteúdo do modal. |
| --ez-modal-content-padding | Define o padding entre o conteúdo e o modal |
| --ez-modal-content-min-width | Define a largura mínima do conteúdo do modal |
