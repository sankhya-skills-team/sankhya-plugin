> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/grid-system/ (snapshot 2026-09-28)

# Grid System

O sistema de grids do CSS3 visa permitir que o conteúdo dos elementos possam ser divididos em um conteúdo de grade. Com o Grid System usa-se uma série de _containers_ , linhas e colunas para fazer o layout e alinhar o conteúdo. É construído com flexbox e é totalmente responsivo.

## Como funciona

O sistema de grid possui elementos que dividi-se em linhas e colunas, as linhas organizam os elementos internos que podem ser colunas ou outro elemento desejado.

### Linhas

No sistema de grid é possível utilizar elementos de linha para organizar seus elementos internos, basta utilizar a classe CSS `ez-row`, conforme o exemplo a seguir:

Conteúdo da Linha

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="sk-demo-container ez-padding--large">
            <div className="ez-row">
                <span className="ez-size-width--full ez-text--center">
                    Conteúdo da Linha
                </span>
            </div>
        </div>
    )
};

export default Demo;
```

### Colunas

Para utilizar elementos de colunas, basta utilizar a classe CSS `ez-col`. Cada linha do grid possui 12 colunas, então para posicionar os elementos em seu interior são utilizadas classes com prefixos pré-definidos que irão ocupar a quantidade desejada de colunas para uma determinada linha, segue um exemplo de como ocupar uma linha com três elementos internos:

1 de 3

1 de 3

1 de 3

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="sk-demo-container ez-padding--large">
            <div className="ez-row">
                <div className="ez-col ez-col--sd-4">
                    <span className="ez-margin--auto">
                        1 de 3
                    </span>
                </div>
                <div className="ez-col ez-col--sd-4">
                    <span className="ez-margin--auto">
                        1 de 3
                    </span>
                </div>
                <div className="ez-col ez-col--sd-4">
                    <span className="ez-margin--auto">
                        1 de 3
                    </span>
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Linhas e Colunas

Para entender melhor o uso de quantidade desejada de colunas, segue um exemplo com várias linhas, e com quantidades específicas de colunas para cada linha:

1 de 1

1 de 3

1 de 3

1 de 3

1 de 3

1 de 3

1 de 3

1 de 3

1 de 3

1 de 3

1 de 4

1 de 4

1 de 4

1 de 4

1 de 2

1 de 2

## Prefixos de resoluções

Para que funcione corretamente o uso do grid para determinadas resoluções, o correto é usar a combinação de classes com prefixos que determinam até qual resolução aquela quantidade de colunas irá obedecer para aquele determinado elemento. Ou seja, com estes prefixos, o elemento irá ocupar a quantidade desejada de colunas a partir de uma resolução mínima, e abaixo desta resolução, o elemento irá ocupar toda a largura da tela.

A seguir seguem alguns exemplos para cada prefixo:

### Small Devices

Prefixo para adaptar em resolução de dispositivos pequenos.

#### sd (min-width: 320px)

Para que a coluna respeite a resolução mínima de até **320px** de largura, utiliza-se o prefixo `--sd-`.

1 de 4

1 de 4

1 de 4

1 de 4

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="sk-demo-container ez-padding--large">
            <div className="ez-row">
                <div className="ez-col ez-col--sd-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--sd-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--sd-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--sd-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Phones

Prefixo para adaptar em resolução de smartphones.

#### pn (min-width: 480px)

Para que a coluna respeite a resolução mínima de até **480px** de largura, utiliza-se o prefixo `--pn-`.

1 de 4

1 de 4

1 de 4

1 de 4

### Tablets

Prefixo para adaptar em resolução de tablets.

#### tb (min-width: 768px)

Para que a coluna respeite a resolução mínima de até **768px** de largura, utiliza-se o prefixo `--tb-`.

1 de 4

1 de 4

1 de 4

1 de 4

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="sk-demo-container ez-padding--large">
            <div className="ez-row">
                <div className="ez-col ez-col--tb-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--tb-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--tb-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--tb-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Medium Devices

Prefixo para adaptar em resolução de dispositivos médios.

#### md (min-width: 992px)

Para que a coluna respeite a resolução mínima de até **992px** de largura, utiliza-se o prefixo `--md-`.

1 de 4

1 de 4

1 de 4

1 de 4

### Large Devices

Prefixo para adaptar em resolução de dispositivos grandes.

#### ld (min-width: 1200px)

Para que a coluna respeite a resolução mínima de até **1200px** de largura, utiliza-se o prefixo `--ld-`.

1 de 4

1 de 4

1 de 4

1 de 4

demo.js

```jsx
import React from 'react';

const Demo = () => {
    return (
        <div className="sk-demo-container ez-padding--large">
            <div className="ez-row">
                <div className="ez-col ez-col--ld-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--ld-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--ld-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
                <div className="ez-col ez-col--ld-3">
                    <span className="ez-margin--auto">
                        1 de 4
                    </span>
                </div>
            </div>
        </div>
    )
};

export default Demo;
```

### Combinação de prefixos

Para projetos que sejam totalmente responsivos, é possível utilizar a combinação dos prefixos apresentados anteriormente, e evitar a quebra de layout em determinada resolução. A seguir, será apresentado um exemplo de como utilizar essa combinação, na qual serão utilizados todos os prefixos, e cada elemento interno da linha seguirá as seguintes regras:

| Prefixo | Resolução Mínima | Qtd. Colunas Ocupadas |
|---|---|---|
| ld | >= 1200px | 1 |
| md | >= 992px | 2 |
| tb | >= 768px | 3 |
| pn | >= 480px | 4 |
| sd | >= 320px | 6 |
| -- | < 320px | 12 |

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12

1 de 12
