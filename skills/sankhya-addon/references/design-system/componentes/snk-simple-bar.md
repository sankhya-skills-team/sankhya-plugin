> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-bar/ (snapshot 2026-09-28)

# Simple Bar

O **SnkSimpleBar** é um componente de cabeçalho (header) visual padronizado, utilizado para exibir o título da tela, navegação por breadcrumb, botão de voltar e um slot para conteúdo dinâmico alinhado à direita. Ele foi projetado para proporcionar uma identidade visual consistente e facilitar a navegação em telas do ecossistema Sankhya, sem incluir botões de ação ou lógica de CRUD.

```jsx
import React, {useRef} from 'react';
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    const application = useRef(null);

    const breadcrumbItens = [
        {id: 1, label: 'Tela principal'}, {id: 2, label: 'Tela intermediária'}, {id: 3, label: 'Tela atual'}
    ];

    const handleExit = () => application.current.message('Mensagem', 'Botão voltar acionado.');

    const handleClickBreadcrumbItem = (item) => application.current.message('Mensagem', JSON.stringify(item));

    return (
        <SnkApplication ref={application}>
            <SnkSimpleBar
                label="Título do header"
                breadcrumbItens={breadcrumbItens}
                onExit={handleExit}
                onClickBreadcrumbItem={handleClickBreadcrumbItem}
            />
        </SnkApplication>
    );
}

export default Demo;
```

## Quando utilizar

Utilize o `SnkSimpleBar` quando precisar de um cabeçalho simples e padronizado para suas telas, especialmente em páginas de consulta, dashboards, relatórios ou qualquer contexto onde não haja necessidade de uma barra de ações (como salvar, excluir, editar). Ele é ideal para:

  * Exibir o título da tela de forma destacada.
  * Apresentar breadcrumbs para navegação hierárquica.
  * Disponibilizar um botão de voltar.
  * Inserir conteúdos customizados à direita do header (ex: botões de filtro, informações contextuais).

## Quando não utilizar

Evite utilizar o `SnkSimpleBar` em telas que exigem ações de CRUD (incluir, editar, excluir, salvar, etc.) ou que necessitam de uma barra de tarefas com múltiplos botões de ação. Para esses casos, prefira o uso do componente `SnkTaskbar`, que foi desenvolvido especificamente para gerenciar ações e fluxos de trabalho em entidades de dados.

## Diferença entre Simple Bar e SnkTaskbar

| Característica | SnkSimpleBar | SnkTaskbar |
|---|---|---|
| Propósito | Cabeçalho visual, navegação e título | Barra de ações (CRUD), gerenciamento de tarefas |
| Botões de ação | Não possui | Possui (Salvar, Editar, Excluir, etc.) |
| Breadcrumb | Sim | Não |
| Slot para conteúdo | Sim (à direita) | Sim (elementos customizados) |
| Uso recomendado | Telas informativas, dashboards, consultas | Telas de cadastro, edição, manipulação de dados |
| Integração com DataUnit | Não | Sim |

Em resumo, utilize o **SnkSimpleBar** para headers simples e o **SnkTaskbar** para telas que exigem ações e manipulação de dados.

## Slots

Por meio do slot usado no exemplo a seguir é possível controlar o conteúdo à direita do componente.

  * Customizar conteúdo à direita do header.

```jsx
import React, {useRef} from 'react';
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    const application = useRef(null);

    const breadcrumbItens = [
        {id: 1, label: 'Tela principal'}, {id: 2, label: 'Tela intermediária'}, {id: 3, label: 'Tela atual'}
    ];

    const handleExit = () => application.current.message('Mensagem', 'Botão voltar acionado.');

    const handleClickBreadcrumbItem = (item) => application.current.message('Mensagem', JSON.stringify(item));

    return (
        <SnkApplication ref={application}>
            <SnkSimpleBar
                label="Título do header"
                breadcrumbItens={breadcrumbItens}
                onExit={handleExit}
                onClickBreadcrumbItem={handleClickBreadcrumbItem}
            >
                <div slot='rightSlot'>
                    <h2 className='ez-title'>Conteúdo alinhado à direita no header.</h2>
                </div>
            </SnkSimpleBar>
        </SnkApplication>
    );
}

export default Demo;
```

## Sticky

Por meio da classe `ez-content--sticky`, é possível definir um posicionamento fixo do componente, mesmo quando houver rolagem na tela.

```jsx
import React, {useRef} from 'react';
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    return (
        <SnkApplication>
            <SnkSimpleBar
                label="Título do header"
                class="ez-content-sticky"
            />
        </SnkApplication>
    );
}

export default Demo;
```

Observação

Importante lembrar que o posicionamento `sticky` aplicado em um elemento HTML é referente ao elemento pai na DOM. Ou seja, a classe sticky deve ser aplicada no elemento filho do container onde há rolagem. Caso contrário, não ocorrerá o comportamento esperado, como pode ser visto no exemplo abaixo:

```jsx
import React, {useRef} from 'react';
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    return (
        <SnkApplication>
            {/* Container sem propriedade sticky*/}
            <div>
                <SnkSimpleBar
                    label="Título do header"
                    className="ez-content-sticky"
                />
            </div>
        </SnkApplication>
    );
}

export default Demo;
```

## Propriedades

### Label

> Propriedade: `label`

Exibe um título simples no header.

```jsx
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const ExampleLabel = () => (
  <SnkApplication>
    <SnkSimpleBar label="Título do header" />
  </SnkApplication>
);

export default ExampleLabel;
```

### breadcrumbItens

> Propriedade: `breadcrumbItens`

Exibe um breadcrumb de navegação.

```jsx
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const breadcrumbItens = [
  { id: 1, label: 'Início' },
  { id: 2, label: 'Relatórios' },
  { id: 3, label: 'Vendas' }
];

const ExampleBreadcrumb = () => (
  <SnkApplication>
    <SnkSimpleBar label="Relatórios de Vendas" breadcrumbItens={breadcrumbItens} />
  </SnkApplication>
);

export default ExampleBreadcrumb;
```

## Eventos

### Exit

> Evento: `exit`

Exemplo de uso do evento de sair (botão voltar).

```jsx
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const ExampleExitEvent = () => {

  const handleExit = () => {
    alert('Botão voltar acionado.');
  };

  return (
    <SnkApplication>
      <SnkSimpleBar label="Com evento de sair" onExit={handleExit} />
    </SnkApplication>
  );
};

export default ExampleExitEvent;
```

### ClickBreadcrumbItem

> Evento: `clickBreadcrumbItem`

Exemplo de uso do evento ao clicar em um item do breadcrumb.

```jsx
import { SnkApplication, SnkSimpleBar } from "@sankhyalabs/sankhyablocks/react/components";

const breadcrumbItens = [
  { id: 1, label: 'Início' },
  { id: 2, label: 'Relatórios' },
  { id: 3, label: 'Vendas' }
];

const ExampleClickBreadcrumbEvent = () => {
  const handleClickBreadcrumbItem = (item) => {
    alert('Breadcrumb acionado!');
  };

  return (
    <SnkApplication>
      <SnkSimpleBar
        label="Com evento de breadcrumb"
        breadcrumbItens={breadcrumbItens}
        onClickBreadcrumbItem={handleClickBreadcrumbItem}
      />
    </SnkApplication>
  );
};

export default ExampleClickBreadcrumbEvent;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| breadcrumbItens | -- | Define os itens que serão apresentados no breadcrumb. | IBreadcrumbItem[] | undefined |
| label | label | Define o título do header. | string | undefined |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| clickBreadcrumbItem | Emitido quando algum item do breadcrumb é clicado. | CustomEvent<IBreadcrumbItem> |
| exit | Emitido quando o botão "voltar" é acionado. | CustomEvent<void> |

### Dependencies

#### Used by

  * snk-attach
  * snk-personalized-filter
