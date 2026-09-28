> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/padding/ (snapshot 2026-09-28)

# Padding

A propriedade _padding_ corresponde ao preenchimento de um elemento HTML, ou seja, o espaçamento interno do elemento.

## Como funciona

Para utilizar a propriedade _padding_ do **EzDesign** , basta inserir a classe CSS `ez-padding` incluindo o lado e/ou o tamanho desejado, conforme será apresentado a seguir.

Informação

Nos exemplos a seguir foram utilizadas classes CSS para destacar os espaçamentos internos ao redor do elemento, para demonstrar o exemplo de forma mais aparente.

## Tamanhos

Os tamanhos correspondem ao espaçamento interno aplicado ao redor do elemento (_left_ , _right_ , _top_ e _bottom_).

### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding--small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding--large sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Grande
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Sem espaçamento

Para remover o espaçamento, basta inserir a classe CSS `ez-padding--none`, conforme exemplo a seguir:

Elemento sem espaçamento

## Lados

É possível aplicar espaçamento interno em cada lado do elemento (_left_ , _right_ , _top_ e _bottom_).

### Horizontal

Para configurar o preenchimento horizontal (_left_ e _right_) do elemento, basta inserir a classe `ez-padding-horizontal` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding-horizontal--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-horizontal--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding-horizontal--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding-horizontal--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-horizontal--medium sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding-horizontal--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

### Vertical

Para configurar o preenchimento vertical (_top_ e _bottom_) do elemento, basta inserir a classe `ez-padding-vertical` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding-vertical--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-vertical--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding-vertical--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding-vertical--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-vertical--medium sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding-vertical--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

### Esquerdo

Para configurar o preenchimento do lado esquerdo (_left_) do elemento, basta inserir a classe `ez-padding-left` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding-left--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-left--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding-left--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding-left--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-left--medium sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding-left--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

### Direito

Para configurar o preenchimento do lado direito (_right_) do elemento, basta inserir a classe `ez-padding-right` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding-right--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-right--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding-right--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding-right--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-right--medium sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding-right--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

### Superior

Para configurar o preenchimento do lado superior (_top_) do elemento, basta inserir a classe `ez-padding-top` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding-top--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-top--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding-top--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding-top--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-top--medium sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding-top--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande

### Inferior

Para configurar o preenchimento do lado inferior (_bottom_) do elemento, basta inserir a classe `ez-padding-bottom` incluindo o tamanho desejado de espaçamento, conforme será apresentado a seguir.

#### Espaçamento muito pequeno

Para utilizar o tamanho do preenchimento _extra-small_ , basta inserir a classe CSS `ez-padding-bottom--extra-small`, conforme exemplo a seguir:

Elemento com Espaçamento Muito Pequeno

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-bottom--extra-small sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Muito Pequeno
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento pequeno

Para utilizar o tamanho do preenchimento _small_ , basta inserir a classe CSS `ez-padding-bottom--small`, conforme exemplo a seguir:

Elemento com Espaçamento Pequeno

#### Espaçamento médio

Para utilizar o tamanho do preenchimento _medium_ , basta inserir a classe CSS `ez-padding-bottom--medium`, conforme exemplo a seguir:

Elemento com Espaçamento Médio

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding-bottom--medium sk-demo-spacing">
                <div className="sk-demo-highlight">
                    Elemento com Espaçamento Médio
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

#### Espaçamento grande

Para utilizar o tamanho do preenchimento _large_ , basta inserir a classe CSS `ez-padding-bottom--large`, conforme exemplo a seguir:

Elemento com Espaçamento Grande
