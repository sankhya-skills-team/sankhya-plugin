> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/box/ (snapshot 2026-09-28)

# Box

A seguir será apresentada a documentação e os exemplos de uso da **Box** , controlando tamanhos e estilos.

## Como funciona

A **Box** é utilizada para separar a página em sessões, mantendo a organização dos dados.

**Box**

demo.js

```jsx
import React from 'react';

const Demo = () => (
    <div className="ez-box ez-margin-bottom--medium">
        <b>Box</b>
    </div>
)

export default Demo;
```

## Container

Para formar o desenho da caixa e permitir a utilização de mais estilos, basta inserir um elemento interno utilizando a classe CSS `ez-box__container`, conforme exemplo a seguir:

**Exemplo padrão de box.**

demo.js

```jsx
import React from 'react';

const Demo = () => (
    <div className="ez-box ez-margin-bottom--medium">
        <div className="ez-box__container">
            <b>Exemplo padrão de box.</b>
        </div>
    </div>
)

export default Demo;
```

## Tamanho

É possível alterar o tamanho da **box** utilizando algumas classes complementares, conforme será apresentado a seguir.

### Pequena

Para utilizar o tamanho do box _small_ , basta inserir a classe CSS `ez-box__container--small`, conforme exemplo a seguir:

Exemplo de box pequena.

### Média

Para utilizar o tamanho do box _medium_ , basta inserir a classe CSS `ez-box__container--medium`, conforme exemplo a seguir:

Exemplo de box no tamanho médio.

demo.js

```jsx
import React from 'react';

const Demo = () => (
    <div className="ez-box ez-margin-bottom--medium">
        <div className="ez-box__container ez-box__container--medium">
            Exemplo de box no tamanho médio.
        </div>
    </div>
)

export default Demo;
```

### Grande

Para utilizar o tamanho do box _large_ , basta inserir a classe CSS `ez-box__container--large`, conforme exemplo a seguir:

Exemplo de box no tamanho grande.

### Muito Grande

Para utilizar o tamanho do box _extra-large_ , basta inserir a classe CSS `ez-box__container--extra-large`, conforme exemplo a seguir:

Exemplo de box no tamanho muito grande.

demo.js

```jsx
import React from 'react';

const Demo = () => (
    <div className="ez-box ez-margin-bottom--medium">
        <div className="ez-box__container ez-box__container--extra-large">
            Exemplo de box no tamanho muito grande.
        </div>
    </div>
)

export default Demo;
```

### Tamanho Automático

Para utilizar o tamanho do box _size-auto_ , basta inserir a classe CSS `ez-box__container--size-auto`, conforme exemplo a seguir:

Exemplo de box no tamanho automático. Nessa classe tanto altura como largura são dinâmicas, se ajustando conforme o conteúdo a ser apresentado.

## Cores

Também é possível estilizar para demonstrar algum retorno visual em cores para o usuário, como sucesso ou aviso.

### Sucesso

Para utilizar o box com a cor _success_ , basta inserir a classe CSS `ez-box--info--success`, conforme exemplo a seguir:

Exemplo de box para mensagem de sucesso.

demo.js

```jsx
import React from 'react';

const Demo = () => (
    <div className="ez-box ez-margin-bottom--medium">
        <div className="ez-box__container ez-box--info--success">
            Exemplo de box para mensagem de sucesso.
        </div>
    </div>
)

export default Demo;
```

### Aviso

Para utilizar o box com a cor _warning_ , basta inserir a classe CSS `ez-box--info--warning`, conforme exemplo a seguir:

Exemplo de box para mensagem de aviso.
