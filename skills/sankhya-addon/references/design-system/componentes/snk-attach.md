> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-attach/ (snapshot 2026-09-28)

# Attach

O **SnkAttach** é um componente que comtepla a funcionalidade de anexar arquivos, possibilitando a visualização e download dos mesmos. Este componente é utilizado em conjunto com o **SnkSimpleCrud** e **SnkSimpleBar**.

## Exemplo

Para utilizar o componente pode-se implementar da seguinte forma:

```jsx
import React from 'react';
import { SnkApplication, SnkAttach } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const viewStackRef = React.useRef(null);

    const handleAttachmentView = () => {
        viewStackRef.current.show(2)
    }

    return (
        <SnkApplication>
            <ez-view-stack ref={(ref) => viewStackRef = ref}>
                <stack-item>
                    <ez-button label="Abrir anexos" onClick={handleAttachmentView}></ez-button>
                </stack-item>
                <stack-item>
                    <SnkAttach registerKey="999" entityName="Financeiro" />
                </stack-item>
            </ez-view-stack>
        </SnkApplication>
    )
};

export default Demo;
```

## Propriedades

### Identificação do registro

> Propriedade utilizada: **registerKey**

Esta propriedade é necessária para identificar o servidor a qual registro o anexo pertence.

### Nome da entidade

> Propriedade utilizada: **entityName**

Esta propriedade é necessária para identificar o servidor a qual entidade o anexo pertence.

## Exemplo de eventos

> Método utilizado: **onBack**

Evento disparado ao clicar no botão de voltar presente no breadcrumb e botão de voltar do **SnkSimpleBar** , como também ao botão **Finalizar** do mesmo quando não houver alterações não salvas.

```jsx
import React from 'react';
import { SnkApplication, SnkAttach } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const viewStackRef = React.useRef(null);

    const handleAttachmentView = () => {
        viewStackRef.current.show(2)
    }

    const handleBack = () => {
        viewStackRef.current.show(1)
    }

    return (
        <SnkApplication>
            <ez-view-stack ref={(ref) => viewStackRef = ref}>
                <stack-item>
                    <ez-button label="Abrir anexos" onClick={handleAttachmentView}></ez-button>
                </stack-item>
                <stack-item>
                    <SnkAttach onBack={handleBack} />
                </stack-item>
            </ez-view-stack>
        </SnkApplication>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| dataUnit | -- | DataUnit responsável por carregar os dados. | DataUnit | undefined |
| dataUnitBuilder | -- | DataUnitBuilder responsável por implementar dados a serem utilizados no DataUnit. | FetcherFacade | undefined |
| entityName | entity-name | Nome da entidade à ser utilizada para relacionar o anexo ao DataUnit pai. | string | undefined |
| fetcher | -- | Fetcher responsável por carregar os dados do DataUnit. | AttachFetcherFacadeInterface | undefined |
| fetcherType | fetcher-type | FetcherType define o tipo de fetcher responsável por carregar os dados do DataUnit. | "AnexoSistema" \| "Another" \| "Attach" | undefined |
| gridLegacyConfigName | grid-legacy-config-name | Chave da configuração legado da grid. | string | undefined |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| registerKey (required) | register-key | Identificação do registro pai. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| back | Evento disparado quando o usuário clica no botão voltar. | CustomEvent<void> |

### Dependencies

#### Used by

  * snk-crud
  * snk-detail-view

#### Depends on

  * snk-simple-bar
  * snk-simple-crud
