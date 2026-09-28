> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/margin/ (snapshot 2026-09-28)

# Margin

A propriedade _margin_ corresponde à margem de um elemento HTML, ou seja, o espaçamento externo do elemento.

## Como funciona

Para utilizar a propriedade _margin_ do **EzDesign** , basta inserir a classe CSS `ez-margin` incluindo o lado e/ou o tamanho desejado, conforme será apresentado a seguir.

Informação

Nos exemplos a seguir foram utilizadas classes CSS para destacar os espaçamentos externos ao redor do elemento, para demonstrar o exemplo de forma mais aparente.

## Tamanhos

Os tamanhos correspondem ao espaçamento externo aplicado ao redor do elemento (_left_ , _right_ , _top_ e _bottom_).

### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin--extra-small sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin--small sk-demo-highlight">
                    Elemento com Espaçamento Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin--large sk-demo-highlight">
                    Elemento com Espaçamento Grande
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Sem margem

Para remover a margem, basta inserir a classe CSS `ez-margin--none`, conforme exemplo a seguir:

Elemento sem espaçamento

### Centralização automática

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin--auto`, conforme exemplo a seguir:

Elemento Centralizado

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex sk-demo-spacing sk-demo-h-100">
            <div className="ez-margin--auto sk-demo-highlight">
                Elemento Centralizado
            </div>
        </div>
    )
};

export default Demo;
```

## Lados

É possível aplicar espaçamento externo em cada lado do elemento (_left_ , _right_ , _top_ e _bottom_).

### Horizontal

Para configurar a margem horizontal (_left_ e _right_) do elemento, basta inserir a classe `ez-margin-horizontal` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin-horizontal--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

#### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin-horizontal--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-horizontal--small sk-demo-highlight">
                    Elemento com Espaçamento Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin-horizontal--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

#### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin-horizontal--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-horizontal--large sk-demo-highlight">
                    Elemento com Espaçamento Grande
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Centralização horizontal

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin-horizontal--auto`, conforme exemplo a seguir:

Elemento Centralizado na Horizontal

### Vertical

Para configurar a margem vertical (_top_ e _bottom_) do elemento, basta inserir a classe `ez-margin-vertical` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin-vertical--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-vertical--extra-small sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin-vertical--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin-vertical--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-vertical--medium sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin-vertical--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

#### Centralização vertical

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin-vertical--auto`, conforme exemplo a seguir:

Elemento Centralizado na Vertical

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-flex sk-demo-spacing sk-demo-h-100">
                <div className="ez-margin-vertical--auto sk-demo-highlight">
                    Elemento Centralizado na Vertical
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Esquerdo

Para configurar a margem do lado esquerdo (_left_) do elemento, basta inserir a classe `ez-margin-left` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin-left--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

#### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin-left--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-left--small sk-demo-highlight">
                    Elemento com Espaçamento Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin-left--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

#### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin-left--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-left--large sk-demo-highlight">
                    Elemento com Espaçamento Grande
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento automático

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin-left--auto`, conforme exemplo a seguir:

Elemento com Espaçamento Automático na Esquerda

### Direito

Para configurar a margem do lado direito (_right_) do elemento, basta inserir a classe `ez-margin-right` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin-right--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-right--extra-small sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin-right--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin-right--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-right--medium sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin-right--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

#### Espaçamento automático

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin-right--auto`, conforme exemplo a seguir:

Elemento com Espaçamento Automático na Direita

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex sk-demo-spacing">
            <div className="ez-margin-right--auto sk-demo-highlight">
                Elemento com Espaçamento Automático na Direita
            </div>
        </div>
    )
};

export default Demo;
```

### Superior

Para configurar a margem do lado superior (_top_) do elemento, basta inserir a classe `ez-margin-top` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin-top--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

#### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin-top--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-top--small sk-demo-highlight">
                    Elemento com Espaçamento Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin-top--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

#### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin-top--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-top--large sk-demo-highlight">
                    Elemento com Espaçamento Grande
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento automático

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin-top--auto`, conforme exemplo a seguir:

Elemento com Espaçamento Automático Superior

### Inferior

Para configurar a margem do lado inferior (_bottom_) do elemento, basta inserir a classe `ez-margin-bottom` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho da margem _extra-small_ , basta inserir a classe CSS `ez-margin-bottom--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-bottom--extra-small sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho da margem _small_ , basta inserir a classe CSS `ez-margin-bottom--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho da margem _medium_ , basta inserir a classe CSS `ez-margin-bottom--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="sk-demo-spacing">
                <div className="ez-margin-bottom--medium sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho da margem _large_ , basta inserir a classe CSS `ez-margin-bottom--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

#### Espaçamento automático

Para utilizar o tamanho da margem _auto_ , basta inserir a classe CSS `ez-margin-bottom--auto`, conforme exemplo a seguir:

Elemento com Espaçamento Automático Inferior

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-flex sk-demo-spacing sk-demo-h-100">
                <div className="ez-margin-bottom--auto sk-demo-highlight">
                    Elemento com Espaçamento Automático Inferior
                </div>
            </div>
        </div>
    )
};

export default Demo;
```
