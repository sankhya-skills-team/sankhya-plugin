> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-collapsible-box/ (snapshot 2026-09-28)

# CollapsibleBox

Documentação do componente EzCollapsibleBox.

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Tamanho x-small

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" headerSize="x-small">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Tamanho small (default)

Conteúdo

### Tamanho medium

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" headerSize="medium">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Tamanho large

Conteúdo

### Slot para posiconamento de itens a direita

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox, EzBadge } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" headerSize="x-large">
                <div slot="rightSlot">
                    <EzBadge label="2" size="medium"/>
                </div>
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Tamanho x-large

Conteúdo

### Ícone a esquerda (default)

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" iconPlacement="left">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Ícone a direita

Conteúdo

### Conteúdo do cabeçalho alinhado a esquerda (default)

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" headerAlign="left">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Título do conteúdo

Conteúdo

### Conteúdo do cabeçalho alinhado a direita

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" headerAlign="right">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Conteúdo do cabeçalho alinhado ao centro

Conteúdo

### Conteúdo do cabeçalho ocupando todo espaço disponível

Conteúdo

demo.js

```jsx
import React from 'react';
import { EzCollapsibleBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCollapsibleBox label="Título do Grupo" headerAlign="stretch">
                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>
            </EzCollapsibleBox>
        </div>
    )
};

export default Demo;
```

### Componente com borda

Conteúdo

### Principais métodos

#### showHide()

Esconde ou revela o conteúdo do componente.

Conteúdo

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzCollapsibleBox, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [value, setValue] = useState(false);

    function onClick() {
        element.current.showHide();
    }

    return (
        <div className="ez-flex ez-flex--column ez-flex--align-items-center">
            <EzCollapsibleBox
                ref={element}
                label="Título do Grupo"
                value={value}
                onEzChange={evt => setValue(evt.detail)}>

                <div class="ez-box">
                    <div class="ez-box__container">Conteúdo</div>
                </div>

            </EzCollapsibleBox>

            <EzButton
                label={`${value ? "Apresentar" : "Ocultar"} Grupo`}
                className="ez-margin-top--medium"
                onClick={onClick}
            >
            </EzButton>
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do componente (onEzChange).

Conteúdo

Fechado: **Não**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| boxBordered | box-bordered | Define seu o componente deve ter borda | boolean | false |
| conditionalSave | -- | Define uma condição para salvar ou não uma alteração. | Function | undefined |
| editable | editable | Se true mostra o ícone para edição do componente. | boolean | false |
| headerAlign | header-align | Define a posição do conteúdo do cabeçalho do componente. | "center" \| "left" \| "right" \| "stretch" | "left" |
| headerSize | header-size | Define o tamanho do texto e do ícone. | "large" \| "medium" \| "small" \| "x-large" \| "x-small" | "small" |
| iconPlacement | icon-placement | Define o posicionamento do ícone. | "left" \| "right" | "left" |
| label | label | Texto a ser apresentado como título do componente. | string | undefined |
| removable | removable | Se true mostra o ícone para remoção do componente. | boolean | false |
| subtitle | subtitle | Texto a ser apresentado como subtítulo do componente. | string | undefined |
| value | value | Define o valor do componente. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do componente. | CustomEvent<boolean> |
| ezEditLabelMode | Emitido quando o modo de edição da label for aberto e fechado (onEzEditLabelMode). | CustomEvent<boolean> |
| ezRemove | Emitido ao remover o componente (onEzRemove). | CustomEvent<EzCollapsibleBox> |
| ezSaveEditLabel | Emitido ao concluir edição da label (onEzSaveEditLabel). | CustomEvent<CustomEvent<any>> |

### Methods

#### `applyFocusTextEdit() => Promise<void>`

Aplica o foco no campo de edição de título.

##### Returns

Type: `Promise<void>`

#### `cancelEdition() => Promise<void>`

Cancela a edição de título.

##### Returns

Type: `Promise<void>`

#### `showHide() => Promise<void>`

Oculta/mostra o conteúdo do ez-collapsible-box.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form-view

#### Depends on

  * ez-icon
  * ez-text-edit

### CSS Variables

| Variable | Description |
|---|---|
| --ez-collapsible-box--font-size | Define o tamanho da fonte do header. |
| --ez-collapsible-box--font-family | Define a família da fonte do header. |
| --ez-collapsible-box--font-weight | Define o peso da fonte do header. |
| --ez-collapsible-box--color | Define a cor da fonte do header. |
| --ez-collapsible-box--subtitle--font-size | Define o tamanho da fonte do header. |
| --ez-collapsible-box--subtitle--font-family | Define a família da fonte do header. |
| --ez-collapsible-box--subtitle--font-weight | Define o peso da fonte do header. |
| --ez-collapsible-box--subtitle--color | Define a cor da fonte do header. |
| --ez-collapsible-box--subtitle--margin-bottom | Define a cor da fonte do header. |
| --ez-collapsible-box--focus--color | Define a cor do texto e do ícone quando o componente está focado. |
| --ez-collapsible-box__icon--color | Define a cor do chevron. |
| --ez-collapsible-box__header--padding-top | Define o espaçamento superior ao header. |
| --ez-collapsible-box__header--padding-bottom | Define o espaçamento inferior ao header. |
| --ez-collapsible-box__header--padding-right | Define o espaçamento à direita do header. |
| --ez-collapsible-box__header--padding-left | Define o espaçamento à esquerda do header. |
