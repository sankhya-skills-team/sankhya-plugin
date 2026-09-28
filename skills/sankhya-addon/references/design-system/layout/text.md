> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/text/ (snapshot 2026-09-28)

# Text

A seguir será apresentado a documentação e os exemplos dos utilitários de texto comuns para controlar tamanho, largura, alinhamento, cor, peso, tipografia e quebra automática.

## Como funciona

Para utilizar o estilo padrão de texto do **EzDesign** , basta inserir a classe CSS `ez-text`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

## Tamanho

É possivel alterar o tamanho do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Muito Pequeno

Para utilizar o tamanho _xsmall_ , basta inserir a classe CSS `ez-text--xsmall`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
       <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--xsmall">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

### Pequeno

Para utilizar o tamanho _small_ , basta inserir a classe CSS `ez-text--small`, conforme exemplo a seguir:

Meu Texto

### Médio

Para utilizar o tamanho _medium_ , basta inserir a classe CSS `ez-text--medium`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
       <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--medium">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

### Grande

Para utilizar o tamanho _large_ , basta inserir a classe CSS `ez-text--large`, conforme exemplo a seguir:

Meu Texto

### Muito Grande

Para utilizar o tamanho _xlarge_ , basta inserir a classe CSS `ez-text--xlarge`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
       <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--xlarge">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

## Largura

Para fazer com que o texto ocupe toda a largura do elemento em que ele se encontra, basta utilizar a classe CSS `ez-text--full`, conforme exemplo a seguir:

Meu Texto

## Alinhamento

É possivel alterar o alinhamento do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Alinhado à esquerda

Para alinhar o texto à esquerda, basta inserir a classe CSS `ez-text--left`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--full ez-text--left">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

### Alinhado à direita

Para alinhar o texto à direita, basta inserir a classe CSS `ez-text--right`, conforme exemplo a seguir:

Meu Texto

### Centralizado

Para centralizar o texto, basta inserir a classe CSS `ez-text--center`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--full ez-text--center">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

## Cor

É possivel alterar a cor do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Cor primária

Para aplicar a cor padrão primária de texto, basta inserir a classe CSS `ez-text--primary`, conforme exemplo a seguir:

Meu Texto

### Cor secundária

Para aplicar a cor padrão secundária de texto, basta inserir a classe CSS `ez-text--secondary`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--secondary">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

### Cor terciária

Para aplicar a cor padrão terciária de texto, basta inserir a classe CSS `ez-text--tertiary`, conforme exemplo a seguir:

Meu Texto

### Inverção de cor

Em casos de _backgrounds_ mais escuros, para melhorar o contraste do texto, basta inverter a cor do texto inserindo a classe CSS `ez-text--inverted`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--inverted sk-demo-contrast">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

### Mensagem de erro

Para aplicar o estilo padrão de mensagem de erro ao texto, basta inserir a classe CSS `ez-text--error`, conforme exemplo a seguir:

Meu Texto

## Peso

É possivel alterar o peso do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Negrito

Para enfatizar o texto com **negrito** , basta inserir a classe CSS `ez-text--bold`, conforme exemplo a seguir:

Meu Texto

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--bold">
                Meu Texto
            </span>
        </div>
    )
};

export default Demo;
```

## Tipografia

É possivel alterar a tipografia do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Maiúsculo ou Caixa alta

Para alterar a tipografia do texto para **MAIÚSCULO** , basta inserir a classe CSS `ez-text--uppercase`, conforme exemplo a seguir:

Meu Texto

## Quebra automática

É possivel controlar a quebra automática do texto utilizando algumas classes complementares, conforme será apresentado a seguir.

### Reticências

Para que o texto não quebre automaticamente e limite o seu tamanho apresentando reticências no final para indicar que o mesmo foi limitado, basta inserir a classe CSS `ez-text--ellipsis`, conforme exemplo a seguir:

Meu Texto Limitado

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="ez-flex ez-margin-bottom--medium">
            <span className="ez-text ez-text--ellipsis ez-col--sd-1" title="Meu Texto Limitado">
                Meu Texto Limitado
            </span>
        </div>
    )
};

export default Demo;
```

### Preservar quebras de linhas

Para manter as quebras de linhas explicitas no conteúdo como a tag `<br>` ou `'\n'` você pode usar a classe `ez-text--break-line` que aplicará o estilo CSS `white-space: pre-line;` ao elemento.

Este é um exemplo de texto com quebras de linha preservadas. Esta linha possui uma quebra de linha usando no código-fonte. E aqui está uma linha com quebra de linha usando no código-fonte.
