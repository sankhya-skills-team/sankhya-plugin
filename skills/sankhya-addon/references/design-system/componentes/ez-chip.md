> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chip/ (snapshot 2026-09-28)

# Chip

Documentação do componente EzChip.

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';
import "./demo.css";

const Demo = () => {
    return (
        <div className="container-ez-chip">
            <EzChip label="Chip padrão" />
            <EzChip label="Chip secundário" type="secondary" />
            <EzChip label="Texto longo (maxWidth=100px)" maxWidth="100px" />
            <EzChip label="Com ícone à esquerda" iconNameLeft="acao" />
            <EzChip label="Secundário + ícone à direita" iconNameRight="alert-circle" type="secondary" />
            <EzChip label="Ícone à esquerda e à direita" iconNameLeft="acao" iconNameRight="alert-circle" />
            <EzChip label="Ícone dos dois lados (habilitado)" iconNameLeft="acao" iconNameRight="alert-circle" />
            <EzChip label="Ícone dos dois lados (desabilitado)" iconNameLeft="acao" iconNameRight="alert-circle" enabled={false} />
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Tipo

A propriedade `type` define o estilo de cor do componente.
Valores possíveis:

  * `primary` (padrão)
  * `secondary`

demo.js

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';
import "../demo.css";

const Demo = () => {
    return (
        <div className="container-ez-chip">
            <EzChip
                label="Chip primário"
                type="primary"
            />
            <EzChip
                label="Chip secundário"
                type="secondary"
            />
        </div>
    )
};

export default Demo;
```

### Largura máxima

A propriedade `maxWidth` define o tamanho máximo do componente.
Quando o texto não couber, será exibido um tooltip ao passar o mouse.

### Tamanho

A propriedade `size` define a altura do chip.
Valores possíveis:

  * `default` (32px de altura)
  * `medium` (42px de altura)
  * `large` (50px de altura)

demo.js

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';
import "../demo.css";

const Demo = () => {
    return (
        <div className="container-ez-chip">
            <EzChip
                label="Chip com tamanho default definido"
                size="default"
            />
            <EzChip
                label="Chip com tamanho medium definido"
                size="medium"
            />
            <EzChip
                label="Chip com tamanho large definido"
                size="large"
            />
        </div>
    )
};

export default Demo;
```

### Icones

A propriedade `iconNameLeft` e `iconNameRight` adiciona ícones aos lados do chip, sem necessidade de slots.

### Tooltip

A propriedade `showNativeTooltip` ativa o tooltip que é exibido ao colocar o ponteiro do mouse sobre o componente. Este comportamento acontece de forma automática caso tenha definido largura máxima e espaço interno não seja suficiente para apresentar o texto completamente.

demo.js

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';
import "../demo.css";

const Demo = () => {
    return (
        <div className="container-ez-chip">
            <EzChip
                label="Chip com tooltip ativado"
                showNativeTooltip={true}
            />
            <EzChip
                label="Chip com largura máximo definido de 200px"
                maxWidth="200px"
            />
        </div>
    )
};

export default Demo;
```

### Habilitado

Componente disponível para seleção.

### Desabilitado

Componente indisponível para seleção.

demo.js

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzChip
                label="Chip desabilitado"
                enabled="false">
            </EzChip>
        </div>
    )
};

export default Demo;
```

### Chip em modo ação

Componente com a propriedade "mode" alterada.

É possível determinar a propriedade "mode" com as seguintes opções:

  * label: É a opção padrão do componente, possui o comportamento de seleção ativa;
  * action: O chip terá o comportamento de um botão, não tendo mais o comportamento de seleção ativa.

Essa propriedade deve ser informada no formato string, exemplo:

```html
<EzChip ... mode="action" ... />
```

### Chip com opção de remover

#### Com o ícone a esquerda

demo.js

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzChip
                label="Chip para remoção"
                removePosition="left">
            </EzChip>
        </div>
    )
};

export default Demo;
```

#### Com o ícone a direita

### Com ícone de ação

Componente com ícone customizado e com ação de clique.

#### Com o ícone a esquerda

demo.js

```jsx
import React from 'react';
import { EzChip, EzIcon } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    function onClick() {
        ApplicationUtils.message("Título da Mensagem", "Clicou no ícone.");
    }

    return (
        <div className="ez-flex">
            <EzChip label="Chip com ícone de ação">
                <EzIcon
                    iconName="chevron-left"
                    slot="leftIcon"
                    className="ez-margin-right--small"
                    onClick={onClick}>
                </EzIcon>
            </EzChip>
        </div>
    )
};

export default Demo;
```

#### Com o ícone a direita

#### Com ícone a esquerda e a direita

demo.js

```jsx
import React from 'react';
import { EzChip, EzIcon } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    function onClick(position) {
        ApplicationUtils.message("Título da Mensagem", `Clicou no ícone ${position}.`);
    }

    return (
        <div className="ez-flex">
            <EzChip label="Chip com ícone de ação">
                <EzIcon
                    iconName="chevron-left"
                    slot="leftIcon"
                    className="ez-margin-right--small"
                    onClick={() => onClick("esquerdo")}>
                </EzIcon>
                <EzIcon
                    iconName="chevron-right"
                    slot="rightIcon"
                    className="ez-margin-left--small"
                    onClick={() => onClick("direito")}>
                </EzIcon>
            </EzChip>
        </div>
    )
};

export default Demo;
```

### Com ícone de informação

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática temos os métodos `setFocus()` e `setBlur()`.

O exemplo abaixo demonstra isso através do botão **Focar Chip**. Clicando nesse botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

Focado: **Não**

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzChip, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [isFocus, setIsFocus] = useState(false);

    function onFocus() {
        element.current.setFocus();

        // O timeout abaixo serve para demonstrar a remoção do foco
        // apos o tempo de 2 segundos.
        setTimeout(()=>{
            element.current.setBlur();
        }, 2000);
    }

    return (
        <div className="ez-flex ez-flex--column ez-flex--align-items-center">
            <EzChip
                ref={element}
                label="Chip comum"
                onBlur={() => setIsFocus(false)}
                onFocus={() => setIsFocus(true)}>
            </EzChip>

            <label className="ez-margin-vertical--medium">
                Focado: <strong>{isFocus ? "Sim" : "Não"}</strong>
            </label>

            <EzButton
                label="Focar Chip"
                onClick={onFocus}>
            </EzButton>
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### valueChange()

Evento disparado quando o estado do componente mudar (onValueChange).

Valor: **false**

#### removeChip()

Evento disparado ao clicar no botão de remoção (onRemoveChip).

demo.js

```jsx
import React, { useRef } from 'react';
import { EzChip, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    function onRemove() {
        element.current.style.display = "none";
    }

    function onReset() {
        element.current.style.display = "";
    }

    return (
        <div className="ez-flex ez-flex--column ez-flex--align-items-center">
            <EzChip
                className="ez-margin-bottom--medium"
                ref={element}
                label="Chip removível"
                removePosition="right"
                onRemoveChip={onRemove}>
            </EzChip>

            <EzButton
                label="Mostrar Chip"
                onClick={onReset}>
            </EzButton>
        </div>
    )
};

export default Demo;
```

#### actionClick()

Evento disparado ao clicar no chip usando o modo "action" (onActionClick).

#### iconClick()

O evento `onIconClick` é disparado ao clicar em um ícone adicionado pelas propriedades `iconNameLeft` ou `iconNameRight`.
O evento recebe um objeto com a chave `icon`, que pode ser `'left'` ou `'right'`.

demo.js

```jsx
import React from 'react';
import { EzChip } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    function onClick(event) {
        if(event.detail.icon === "left") {
            ApplicationUtils.message("Uhul!", "Clicou no icone esquerdo!");
        } else {
             ApplicationUtils.message("Uhul!", "Clicou no icone direito!");
        }
    }

    return (
        <div className="ez-flex">
            <EzChip
                label="Chip com icones clicaveis"
                iconNameRight="alert-circle"
                iconNameLeft="acao"

                onIconClick={onClick}>
            </EzChip>
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| disableAutoUpdateValue | disable-auto-update-value | Desabilita a alteração da propriedade value ao clicar. | boolean | false |
| enabled | enabled | Se false o usuário não pode interagir com o ez-chip. | boolean | true |
| iconNameLeft | icon-name-left | Define o icone esquerdo. | string | undefined |
| iconNameRight | icon-name-right | Define o icone direito. | string | undefined |
| label | label | Texto a ser apresentado como título do ez-chip. | string | undefined |
| maxWidth | max-width | Define o tamanho máximo do chip. | string | undefined |
| mode | mode | Define o modo de uso do ez-chip. | "action" \| "label" | undefined |
| removePosition | remove-position | Determina o posicionamento do botão de remover (não disponível no modo action ).  Se não informado, não exibe o botão. | "left" \| "right" | undefined |
| removeWithKeyboard | remove-with-keyboard | Define se o chip deve ser removido ao pressionar a tecla Enter quando focado. | boolean | false |
| showNativeTooltip | show-native-tooltip | Exibe condicionalmente o tooltip nativo do navegador ao sobrepor o cursor acima do elemento. | boolean | false |
| size | size | Define o tamanho do chip. | "default" \| "large" \| "medium" | 'default' |
| tabIndex | tab-index | Define o tabindex do chip. Por padrão é 0, permitindo que o chip seja focável. | number | 0 |
| type | type | Define o tipo de estilização do chip. | "error" \| "error-light" \| "primary" \| "secondary" \| "success" \| "success-light" \| "warning" \| "warning-light" | 'primary' |
| value | value | Define o valor do ez-chip. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| actionClick | Emitido no modo "action" quando o usuário clica no ez-chip. | CustomEvent<void> |
| iconClick | Emitido quando o icone é acionado. | CustomEvent<{ icon: "left" \| "right"; }> |
| removeChip | Emitido quando o botão de remoção é acionado. | CustomEvent<void> |
| valueChange | Emitido quando acontece a alteração de valor do ez-chip. | CustomEvent<boolean> |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do ez-chip.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Aplica o foco no ez-chip.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-tag-input

#### Depends on

  * ez-tooltip
  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-label-chip--height | Define a altura do chip. |
| --ez-label-chip__label--font-size | Define o tamanho do label. |
| --ez-label-chip__label--font-family | Define a família da fonte do label. |
| --ez-label-chip__label--font-weight | Define o peso da fonte do label. |
| --ez-label-chip__horizontal-padding | Define o espaçamento do label. |
| --ez-label-chip__label--text--primary | Define a cor do texto. |
| --ez-label-chip__label--icon--primary | Define a cor do ícone. |
| --ez-label-chip__label__container--border-radius | Define o raio da borda do container do chip. |
| --ez-label-chip__label__container--border | Define o estilo da borda do container. |
| --ez-label-chip__label__container--border-color-strokes | Define a cor da borda do container. |
| --ez-label-chip__label__container-color--disabled | Define a cor da borda e do fundo quando o chip está desativado. |
| --ez-label-chip__label__container--background-color | Define a cor de fundo do container. |
| --ez-label-chip__label__container--border-color-active | Define a cor da borda do container quando ativo. |
| --ez-label-chip__label__container--default--background-color--active | Define a cor do fundo do container quando está ativo. |
| --ez-label-chip__label__container--default--color--active | Define a cor do texto quando está ativo. |
| --ez-label-chip__label__container--text--disabled | Define a cor do texto e do ícone quando o chip está desabilitado. |
| --ez-label-chip__label__container--default--border-color--active | Define a cor da borda quando o componente está ativo. |
| --ez-label-chip__label__container--secondary--border-color--active | Define a cor da borda quando o componente está ativo e na variação secundária. |
| --ez-label-chip__label__container--margin | Define a margem do chip. |
