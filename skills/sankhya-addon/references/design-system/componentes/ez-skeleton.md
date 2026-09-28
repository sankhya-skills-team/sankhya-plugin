> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-skeleton/ (snapshot 2026-09-28)

# Skeleton

O **Skeleton** é um componente de carregamento que simula o layout do conteúdo enquanto os dados estão sendo carregados. Ele fornece feedback visual aos usuários durante os estados de carregamento.

```html
<ez-skeleton></ez-skeleton>
```

```html
<EzSkeleton></EzSkeleton>
```

## Variantes

O componente suporta as seguintes `variant`:

  * `text (Default)`: Forma de linha de texto.

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="skeleton__container">
      <EzSkeleton variant={"text"} />
    </div>
  );
};

export default Demo;
```

  * `rect`: Forma retangular.

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="skeleton__container">
      <EzSkeleton variant={"rect"} />
    </div>
  );
};

export default Demo;
```

  * `circle`: Forma circular.

## Animações

Define o tipo de `animation` do componente.

  * `progress (Default)`: Animação de progresso de carregamento

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="skeleton__container">
      <EzSkeleton animation={"progress"} />
    </div>
  );
};

export default Demo;
```

  * `pulse`: Animação pulsante

  * `false`: Sem animação

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="skeleton__container">
      <EzSkeleton animation={"false"} />
    </div>
  );
};

export default Demo;
```

## Dimensões

É possível definir o `width` e o `height` do componente. Os valores aceitos são os mesmos aceitos pelo CSS.

## Margem

O componente oferece controle individual das margens:

  * `marginTop`: Margem superior

  * `marginRight`: Margem direita

  * `marginBottom`: Margem inferior

  * `marginLeft`: Margem esquerda

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="sk-demo-spacing">
      <EzSkeleton
        marginTop="20px"
        marginRight="20px"
        marginBottom="15px"
        marginLeft="20px"
      />
    </div>
  );
};

export default Demo;
```

## Contador

Repete o número de itens skeleton a serem renderizados na tela com as mesmas propriedades informadas. Por padrão o `count` do componente é sempre **1**.

## Estilização via Style Props

O componente EzSkeleton permite customização através de propriedades CSS personalizadas (custom properties) passadas via prop `style`. As seguintes propriedades são suportadas:

  * `--skeleton-width`: Define a largura do skeleton
  * `--skeleton-height`: Define a altura do skeleton
  * `--skeleton-border-radius`: Define o raio da borda
  * `--skeleton-background`: Define a cor de fundo base
  * `--skeleton-background-image`: Define a cor da animação
  * `--skeleton-margin-top`: Define a margem superior
  * `--skeleton-margin-right`: Define a margem direita
  * `--skeleton-margin-bottom`: Define a margem inferior
  * `--skeleton-margin-left`: Define a margem esquerda

### Exemplo de uso:

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="skeleton__container ez-flex ez-flex--column">
      <EzSkeleton
        style={{
          "--skeleton-width": "500px",
          "--skeleton-height": "80px",
          "--skeleton-border-radius": "80px",
          "--skeleton-background": "#ccc",
          "--skeleton-background-image": "#fff",
          "--skeleton-margin-top": "32px",
          "--skeleton-margin-right": "32px",
          "--skeleton-margin-bottom": "32px",
          "--skeleton-margin-left": "32px",
        }}
      />
    </div>
  );
};

export default Demo;
```

## Templates Dinâmicos

Define o template a ser usado para a estrutura do skeleton. O componente permite criar estruturas personalizadas de carregamento que se adaptam ao seu layout.

  * Tipo: `HTMLElement | string`

### Comportamento dos Templates:

  * Elementos com `class="skeleton"`: O componente renderiza o skeleton aplicando todas as propriedades disponíveis (variant, animation, width, height, etc)
  * Quando elementos pai e filho possuem `class="skeleton"`: O skeleton é renderizado apenas no elemento pai, evitando duplicidade
  * Elementos `sem` a `class="skeleton"`: São renderizados normalmente, permitindo customização através de classes e styles próprios

### Características dos Templates:

  * Podem ser compostos por múltiplos elementos skeleton
  * Herdam as propriedades de animação definidas
  * Suportam diferentes variantes (circle, rect, text) em um mesmo template
  * Permitem configuração individual de dimensões para cada elemento
  * Mantêm a consistência de animação entre todos os elementos

### Boas Práticas:

  * Use templates para replicar a estrutura exata do conteúdo final
  * Combine diferentes variantes para criar layouts complexos
  * Mantenha as dimensões proporcionais ao conteúdo real
  * Utilize o atributo count para repetir estruturas similares
  * Aplique margens adequadas para manter o espaçamento visual
  * Evite usar class="skeleton" em elementos aninhados quando o pai já possui a classe

### Exemplos de Uso de Templates

### Conteúdo do template com elemento H3 sem classe Skeleton & style para cor do texto

demo.js

```jsx
import React from "react";

import { EzSkeleton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <div className="skeleton__container ez-flex ez-flex--column">
      <EzSkeleton
        template="
            <div class='skeleton' variant='text' width='calc(100% - 20px)' height='48px' marginTop='10px' marginRight='10px' marginBottom='10px' marginLeft='10px' count={1}>teste</div>
            <div class='skeleton' variant='rect' width='calc(100% - 20px)' height='48px' marginTop='10px' marginRight='10px' marginBottom='10px' marginLeft='10px' count={1}>teste</div>
            <h3 style='color: red;margin-left: 10px;'>Conteúdo do template com elemento H3 sem classe Skeleton & style para cor do texto</h3>
            <div class='skeleton' variant='circle' width='50px' height='50px' marginTop='10px' marginRight='10px' marginBottom='10px' marginLeft='10px' count={5}>MINHA DIV</div>
            <span class='skeleton'>span 123</span>
        "
      />
    </div>
  );
};

export default Demo;
```

## Acessibilidade

O componente Skeleton implementa os seguintes atributos ARIA para garantir uma melhor experiência para usuários de tecnologias assistivas:

  * `role="progressbar"`: Indica que o elemento representa uma barra de progresso
  * `data-busy="true"`: Comunica que o conteúdo está em estado de carregamento
  * `data-valuemin="0"`: Define o valor mínimo do progresso
  * `data-valuemax="100"`: Define o valor máximo do progresso
  * `data-valuetext="Loading..."`: Fornece um texto descritivo do estado atual
  * `tabindex="0"`: Permite que o elemento receba foco via teclado

Estes atributos são aplicados automaticamente em todos os elementos skeleton, garantindo que o componente seja acessível e forneça feedback adequado sobre seu estado de carregamento.
