> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/labels/ (snapshot 2026-09-28)

# Labels

A tag `<label>` é um elemento HTML que representa uma legenda para melhorar a acessibilidade de um item de interface do usuário. Este elemento também é conhecido como controle ou rótulo e pode ser associado a outro elemento de controle através de um atributo.

## Como funciona

Para utilizar o estilo padrão dos labels do **EzDesign** , basta inserir a classe CSS `ez-label`, conforme exemplo a seguir:

Meu Label

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-margin-bottom--medium">
            <label className="ez-label">
                Meu Label
            </label>
        </div>
    )
};

export default Demo;
```

## Variações

### title

Para utilizar o estilo padrão do label de título, basta inserir as classes CSS `ez-label` e `ez-label--title`, conforme exemplo a seguir:

Meu Label

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-margin-bottom--medium">
            <label className="ez-label ez-label--title">
                Meu Label
            </label>
        </div>
    )
};

export default Demo;
```

### description

Para utilizar o estilo padrão do label de descrição, basta inserir as classes CSS `ez-label` e `ez-label--description`, conforme exemplo a seguir:

Meu Label

### optional

Para utilizar o estilo padrão do label opcional, basta inserir as classes CSS `ez-label` e `ez-label--optional`, conforme exemplo a seguir:

Meu Label

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-margin-bottom--medium">
            <label className="ez-label ez-label--optional">
                Meu Label
            </label>
        </div>
    )
};

export default Demo;
```

### textarea

Para utilizar o estilo padrão do label de textarea, basta inserir as classes CSS `ez-label` e `ez-label--textarea`, conforme exemplo a seguir:

Meu Label

### tooltip

As tooltips são utilizadas para mostrar descrições mais detalhadas de um componente ao posicionar o cursor do mouse sobre ele.

Tooltip(bottom)Tooltip(top)Tooltip(right)Tooltip(left)

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-margin-bottom--medium">
            <label class="ez-margin-horizontal--medium" data-tooltip="Tooltip bottom" data-flow="bottom">
                Tooltip(bottom)
            </label>
            <label class="ez-margin-horizontal--medium" data-tooltip="Tooltip top" data-flow="top">
                Tooltip(top)
            </label>
            <label class="ez-margin-horizontal--medium" data-tooltip="Tooltip right" data-flow="right">
                Tooltip(right)
            </label>
            <label class="ez-margin-horizontal--medium" data-tooltip="Tooltip left" data-flow="left">
                Tooltip(left)
            </label>
        </div>
    )
};

export default Demo;
```
