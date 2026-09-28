> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert-list/ (snapshot 2026-09-28)

# AlertList

O componente AlertList tem a função de exibir uma lista de alertas em formato de popup, garantindo que não interfira na usabilidade do conteúdo abaixo dele.

demo.js

```jsx
import React from 'react';
import { useState, useRef } from 'react';
import { EzAlertList, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [opened, setOpened] = useState(false);
    const alertList = useRef()

    const showAlertList = () => {
        alertList.current.opened = true;
    }

    return (
        <div style={{overflow: "auto", padding: "10px"}}>
            <EzAlertList opened={opened} enableExpand={false} ref={alertList} alerts={[
                {
                    title: "title 1",
                    detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                },
                {
                    title: "title 2",
                    detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                },
                {
                    title: "title 3",
                    detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                },
                {
                    title: "title 4",
                    detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                },
            ]}/>
            <EzButton
                label="Exibir Lista de alertas"
                onClick={() => showAlertList()}
            />
        </div>
    )
};

export default Demo;
```

## Habilitar expansão

demo.js

```jsx
import React from 'react';
import { useState, useRef } from 'react';
import { EzAlertList, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [opened, setOpened] = useState(false);
    const alertList = useRef()

    const showAlertList = () => {
        alertList.current.opened = true;
    }

    return (
        <div style={{overflow: "auto", padding: "10px"}}>
            <EzAlertList opened={false} ref={alertList} enableExpand={true} alerts={[
               {
                title: "title 1",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                title: "title 2",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                title: "title 3",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                title: "title 4",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                title: "title 5",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                title: "title 6",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                title: "title 7",
                detail: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            ]}/>
            <EzButton
                label="Exibir Lista de alertas"
                onClick={() => showAlertList()}
            />
        </div>
    )
};

export default Demo;
```

## Título com callback

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alerts | -- | Lista de alertas que devem ser apresentados no componente. | AlertItem[] | [] |
| enableDragAndDrop | enable-drag-and-drop | Define se o componente pode ser arrastado na tela. | boolean | undefined |
| enableExpand | enable-expand | Define se o componente pode ser expandido. | boolean | true |
| expanded | expanded | Define se o componente está expandido. | boolean | false |
| itemRightSlotBuilder | -- | Define builder para elementos a direita do componente | (item: ListItem, group?: ListGroup) => string \| HTMLElement | undefined |
| opened | opened | Define se o componente está aberto. | boolean | true |

### Dependencies

#### Depends on

  * ez-button
  * ez-list

### CSS Variables

| Variable | Description |
|---|---|
| --ez-alert-list__container--width | Define a largura da lista minimizado |
| --ez-alert-list__container--height | Define a altura da lista minimizado |
| --ez-alert-list__container--width--expanded | Define a largura da lista maximizada |
| --ez-alert-list__container--height--expanded | Define a altura da lista maximizada |
| --ez-alert-list__title--font-family | Define a fonte do título do componente |
| --ez-alert-list__title--font-size | Define o tamanho da fonte do título do popup. |
| --ez-alert-list__title--color | Define a cor da fonte do título do popup. |
| --ez-alert-list__title--font-weight | Define o peso da fonte do título do popup. |
| --ez-list__item--border-bottom | Define a borda inferior do item da lista. |
| --ez-list__item--border-bottom-color | Define a cor da borda inferior do item da lista. |
| --ez-list__item--white-space | Define o tipo da quebra de linha do item da lista. |
