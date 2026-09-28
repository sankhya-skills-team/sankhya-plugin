> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/title/ (snapshot 2026-09-28)

# Title

A seguir será apresentada a documentação e os exemplos dos utilitários de **títulos** comuns para controlar alinhamento, cor e tamanho.

## Como funciona

Para utilizar o estilo padrão dos títulos do **EzDesign** , basta inserir a classe CSS `ez-title`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 class="ez-title">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

## Tamanho

É possível alterar o tamanho do título utilizando algumas classes complementares, conforme será apresentado a seguir.

### Muito Pequeno

Para utilizar o tamanho _extra-small_ , basta inserir a classe CSS `ez-title--extra-small`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 className="ez-title ez-title--extra-small">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

### Pequeno

Para utilizar o tamanho _small_ , basta inserir a classe CSS `ez-title--small`, conforme exemplo a seguir:

### Meu Título

### Médio

Para utilizar o tamanho _medium_ , basta inserir a classe CSS `ez-title--medium`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 className="ez-title ez-title--medium">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

### Grande

Para utilizar o tamanho _large_ , basta inserir a classe CSS `ez-title--large`, conforme exemplo a seguir:

### Meu Título

### Muito Grande

Para utilizar o tamanho _extra-large_ , basta inserir a classe CSS `ez-title--extra-large`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 className="ez-title ez-title--extra-large">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

## Alinhamento

É possível alterar o alinhamento do título utilizando algumas classes complementares, conforme será apresentado a seguir.

### Centralizado

Para centralizar o título, basta inserir as classes CSS `ez-title--center ez-size-width--full`, conforme exemplo a seguir:

### Meu Título

### Alinhado à esquerda

Para alinhar o título à esquerda, basta inserir a classe CSS `ez-title--left ez-size-width--full`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 className="ez-title ez-title--left ez-size-width--full">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

### Alinhado à direita

Para alinhar o título à direita, basta inserir a classe CSS `ez-title--right ez-size-width--full`, conforme exemplo a seguir:

### Meu Título

## Cor

É possível alterar a cor do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Cor Primária

Corresponde a cor principal dos títulos. Para aplicar a cor padrão primária de título, basta inserir a classe CSS `ez-title--primary`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 className="ez-title ez-title--primary">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

### Cor Secundária

Para aplicar a cor padrão secundária dos títulos, basta inserir a classe CSS `ez-title--secondary`, conforme exemplo a seguir:

### Meu Título

### Cor Terciária

Para aplicar a cor padrão terciária dos títulos, basta inserir a classe CSS `ez-title--tertiary`, conforme exemplo a seguir:

### Meu Título

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <h3 className="ez-title ez-title--tertiary">
                Meu Título
            </h3>
        </div>
    )
};

export default Demo;
```

### Inversão de Cor

Em casos de _backgrounds_ mais escuros, para melhorar o contraste do título, basta inverter a cor do título inserindo a classe CSS `ez-title--inverted`, conforme exemplo a seguir:

### Meu Título
