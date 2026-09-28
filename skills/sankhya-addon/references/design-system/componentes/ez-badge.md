> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-badge/ (snapshot 2026-09-28)

# Badge

Um elemento em formato de etiqueta que permite reconhecimento rápido de um status temporário.

### Texto

#### Solid

Contém preenchimento semântico e texto neutro.

Por default, o badge é apresentado com a classe **ez-badge--primary-solid** , com isso não precisamos inserir a classe na tag ez-badge.

demo.js

```jsx
import React from 'react';
import { EzBadge } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-row">
            <EzBadge label="primary" size="medium" />
            <EzBadge label="secondary" size="medium" className="ez-badge--secondary-solid" />
            <EzBadge label="success" size="medium" className="ez-badge--success-solid" />
            <EzBadge label="warning" size="medium" className="ez-badge--warning-solid" />
            <EzBadge label="error" size="medium" className="ez-badge--error-solid" />
            <EzBadge label="disabled" size="medium" className="ez-badge--disabled-solid"/>
        </div>
    )
};

export default Demo;
```

#### Subtle

Contém preenchimento semântico na cor clara e texto semântico na cor escura.

demo.js

```jsx
import React from 'react';
import { EzBadge } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-row">
            <EzBadge label="primary" size="medium" className="ez-badge--primary-subtle" />
            <EzBadge label="secondary" size="medium" className="ez-badge--secondary-subtle" />
            <EzBadge label="success" size="medium" className="ez-badge--success-subtle" />
            <EzBadge label="warning" size="medium" className="ez-badge--warning-subtle" />
            <EzBadge label="error" size="medium" className="ez-badge--error-subtle" />
            <EzBadge label="disabled" size="medium" className="ez-badge--disabled-subtle" />
        </div>
    )
};

export default Demo;
```

#### Tamanhos

No formato de texto podemos utilizar o ez-badge com 3 tamanhos: **medium (24px)** , **small-medium (20px)** e **small (16px)**.

### Badge: Ícone

#### Solid

Contém preenchimento semântico e texto neutro.

Por default, o badge é apresentado com a classe **ez-badge--primary-solid** , com isso não precisamos inserir a classe na tag ez-badge.

demo.js

```jsx
import React from 'react';
import { EzBadge } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
            <EzBadge iconLeft="alert-circle" size="medium" />
            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--secondary-solid" />
            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--success-solid" />
            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--warning-solid" />
            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--error-solid" />
            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--disabled-solid" />
            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--transparent-solid" />
        </div>
    )
};

export default Demo;
```

#### Subtle

Contém preenchimento semântico na cor clara e texto semântico na cor escura.

#### Tamanhos

No formato de ícone podemos utilizar o ez-badge com 4 tamanhos: **extra-large (32px)** , **large (24px)** , **medium (20px)** e **small-medium (16px)**.

demo.js

```jsx
import React from 'react';
import { EzBadge } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
            <EzBadge iconRight="alert-circle" size="large" />
            <EzBadge iconRight="alert-circle" size="medium" />
            <EzBadge iconRight="alert-circle" size="small-medium" />
            <EzBadge iconRight="alert-circle" size="small" />
        </div>
    )
};

export default Demo;
```

### Badge: Ícone + Texto

#### Solid

Contém preenchimento semântico e texto neutro.

Por default, o badge é apresentado com a classe **ez-badge--primary-solid** , com isso não precisamos inserir a classe na tag ez-badge.

#### Subtle

Contém preenchimento semântico na cor clara e texto semântico na cor escura.

demo.js

```jsx
import React from 'react';
import { EzBadge, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-row">
            <EzBadge iconLeft="alert-circle" iconRight="alert-circle" label="Primary" size="small-medium" className="ez-badge--primary-subtle ez-margin-bottom--medium" />
            <EzBadge iconLeft="alert-circle" iconRight="alert-circle" label="Secondary" size="small-medium" className="ez-badge--secondary-subtle ez-margin-bottom--medium" />
            <EzBadge iconLeft="alert-circle" iconRight="alert-circle" label="Success" size="small-medium" className="ez-badge--success-subtle ez-margin-bottom--medium" />
            <EzBadge iconLeft="alert-circle" iconRight="alert-circle" label="Warning" size="small-medium" className="ez-badge--warning-subtle ez-margin-bottom--medium"/>
            <EzBadge iconLeft="alert-circle" iconRight="alert-circle" label="Error" size="small-medium" className="ez-badge--error-subtle ez-margin-bottom--medium"/>
            <EzBadge iconLeft="alert-circle" iconRight="alert-circle" label="Disabled" size="small-medium" className="ez-badge--disabled-subtle ez-margin-bottom--medium"/>
        </div>
    )
};

export default Demo;
```

#### Tamanhos

> Propriedade utilizada: **size**

No formato de ícone + texto podemos utilizar o ez-badge com 3 tamanhos: **medium (24px)** , **small-medium (20px)** e **small (16px)**.

#### Ícone na direita do texto

demo.js

```jsx
import React from 'react';
import { EzBadge, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzBadge iconRight="alert-circle" label="Icon Right" size="medium" />
        </div>
    )
};

export default Demo;
```

#### #### Ícone na esquerda do texto

### Badge: Fill

#### Solid

Contém preenchimento semântico e texto neutro.

Por default, o badge é apresentado com a classe **ez-badge--primary-solid** , com isso não precisamos inserir a classe na tag ez-badge.

demo.js

```jsx
import React from 'react';
import { EzBadge, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-row">
            <EzBadge className="ez-margin-bottom--medium">
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary " />
            </EzBadge>
            <EzBadge className="ez-badge--secondary-solid ez-margin-bottom--medium" >
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
            <EzBadge className="ez-badge--success-solid ez-margin-bottom--medium" >
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
            <EzBadge className="ez-badge--warning-solid ez-margin-bottom--medium" >
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
            <EzBadge className="ez-badge--error-solid ez-margin-bottom--medium" >
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
            <EzBadge className="ez-badge--disabled-solid ez-margin-bottom--medium" >
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
        </div>
    )
};

export default Demo;
```

#### Subtle

Contém preenchimento semântico na cor clara e texto semântico na cor escura.

#### Tamanhos

No formato de texto podemos utilizar o ez-badge com 2 tamanhos: **small (12px)** e **extra-small (8px)**. Por default, o fill é apresentado com o size small.

demo.js

```jsx
import React from 'react';
import { EzBadge, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
            <EzBadge size="small" className="ez-badge--warning-solid">
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
            <EzBadge size="extra-small" className="ez-badge--warning-solid">
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
        </div>
    )
};

export default Demo;
```

#### Fill e ícone

#### Fill, ícone e texto

demo.js

```jsx
import React from 'react';
import { EzBadge, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzBadge iconLeft="alert-circle" label="10" position={{ vertical: "bottom", horizontal: "right" }} className="ez-badge--error-solid">
                <EzButton label="OK" slot="child-badge" size="small" className="ez-button--primary" />
            </EzBadge>
        </div>
    )
};

export default Demo;
```

#### Direções horizontal e vertical

> Propriedade utilizada: **position**

Com essa propriedade podemos utilizar o fill nas direções horizontal e na vertical, por default as posições são **horizontal: "right"** , **vertical: "top"**.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alignItems | align-items | Define a posição do ícone em relação ao elemento. | "center" \| "flex-end" \| "flex-start" | "center" |
| iconLeft | icon-left | Define o ícone a ser usado no lado esquerdo do badge: ez-icons | string | undefined |
| iconRight | icon-right | Define o ícone a ser usado no lado direito do badge: ez-icons | string | undefined |
| label | label | Define o conteúdo textual ou numérico do componente. | string | undefined |
| position | -- | Define a posição do ícone em relação ao elemento filho. | IPosition | { horizontal: "right", vertical: "top" } |
| size | size | Define o tamanho de acordo com o tipo utilizado pelo componente. | "extra-large" \| "extra-small" \| "large" \| "medium" \| "small" \| "small-medium" | "small" |

### Dependencies

#### Used by

  * ez-tile-medium

#### Depends on

  * ez-icon
