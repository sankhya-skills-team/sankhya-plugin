> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-pagination/ (snapshot 2026-09-28)

# Pagination

Componente de Paginação reutilizável e flexível, que permite navegação entre páginas de forma acessível e responsiva, com possibilidade de exibir ou ocultar o texto de paginação e personalizar seu conteúdo.

Default

1 até 10 de 100

Numérico

...

```jsx
import React from 'react';
import "./demo.css";
import { EzPagination } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  return (
    <div className="pagination-demo-container">

      <div className={'pagination-demo-example'}>
        <span className={"pagination-demo-header"}>Default</span>
        <EzPagination currentPage={1} pageSize={10} totalItems={100} />
      </div>

      <div className={'pagination-demo-example'}>
        <span className={"pagination-demo-header"}>Numérico</span>
        <EzPagination currentPage={1} pageSize={10} pageLimit={6} totalItems={100} type={'number'} />
      </div>
    </div>
  );
};

export default Demo;
```

Atenção

Para que o componente funcione corretamente, é necessário informar as seguintes propriedades:

  * `totalItems`: quantidade total de itens a serem paginados.
  * `pageSize`: quantidade de itens por página.

## Tipos de exibição

Existem dois tipos de exibição do componente, o tipo padrão e o tipo numérico.

> A propriedade type é do tipo string e aceita os valores `default` e `numeric`.

### Tipo padrão

É o tipo de exibição padrão do componente, no qual são exibidos os botões de navegação para a página anterior e próxima, além do texto de paginação, informando a quantidade total de elementos.

Tipo Default

1 até 10 de 100

demo.js

```jsx
import React from 'react';
import { EzPagination } from '@sankhyalabs/ezui/react/components';

const Default = () => {
  return (
    <div className="pagination-demo-container">
      <div className={'pagination-demo-example'}>
        <span className={"pagination-demo-header"}>Tipo Default</span>
        <EzPagination currentPage={1} pageSize={10} totalItems={100} type={"default"} />
      </div>

    </div>
  );
};

export default Default;
```

### Tipo numérico

É o tipo de paginação convencional, no qual são exibidos os números das páginas, além dos botões de navegação para a página anterior e próxima.

Tipo numérico

## Esconder informações de paginação

É possível ocultar o texto de paginação, que informa a quantidade total de elementos e a página atual, por meio da propriedade `hideInfoLabel`.

Esconder texto de informação

demo.js

```jsx
import React from 'react';
import { EzPagination } from '@sankhyalabs/ezui/react/components';
import '../demo.css';

const Default = () => {
  return (
    <div className="pagination-demo-container">
      <div className={'pagination-demo-example'}>
        <span className={"pagination-demo-header"}>Esconder texto de informação</span>
        <EzPagination currentPage={1} pageSize={10} totalItems={100} hideInfoLabel={true} />
      </div>

    </div>
  );
};

export default Default;
```

## Limite de páginas

É possível definir a quantidade de páginas que devem ser exibidas no componente em tipo numérico, por meio da propriedade `pageLimit`.

Page limit = 8

...

Page limit = 6

...

Page limit = 5

...

Dica

O valor padrão da propriedade `pageLimit` é **10** , ou seja, serão exibidas **no máximo 10** opções de páginas.

## Eventos

### ezPageChange

Emitido ao realizar a troca de página, informando o número da página selecionada.

Tipo numérico

demo.js

```jsx
import React, { useState } from 'react';
import { EzPagination } from '@sankhyalabs/ezui/react/components';
import '../demo.css';

const Default = () => {
  const [page, setPage] = useState(undefined);

  const onChange = (evt) => {
    setPage(evt.detail);
  };

  return (
    <div className="pagination-demo-container">
      <div className={'pagination-demo-example'}>
        <span className={'pagination-demo-header'}>Tipo numérico</span>
        <EzPagination
          pageSize={10}
          totalItems={100}
          type={'number'}
          onEzPageChange={onChange}
        />
      </div>

      {page && (
        <div>
          <strong>Evento ezPageChange disparado!</strong>
          <br />
          Página atual: {page}
        </div>
      )}
    </div>
  );
};

export default Default;
```
