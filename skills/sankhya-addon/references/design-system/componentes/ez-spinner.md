> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-spinner/ (snapshot 2026-09-28)

# Spinner

O **Spinner** é um componente de feedback visual que indica o progresso de carregamento ou processamento de uma operação. É utilizado para informar ao usuário que uma ação está sendo executada em segundo plano.

```jsx
import { EzSpinner } from "@sankhyalabs/ezui/react/components";
import "./demo.css";

const Demo = () => {
    return (
        <div className="ez-spinner-demo">
            <EzSpinner />
        </div>
    );
};

export default Demo;
```

## Variações

### Tamanhos

O Spinner suporta diferentes tamanhos que podem ser definidos através da propriedade `size`. Por padrão, o Spinner será renderizado no tamanho small (pequeno). Os tamanhos disponíveis e seus usos recomendados são:

  * `small`: Tamanho Pequeno. Ideal para contextos compactos, como dentro de botões, campos de entrada de texto (inputs) ou em espaços reduzidos onde a discrição é essencial.
  * `medium`: Tamanho Médio. Adequado para a maioria dos casos de uso, como dentro de caixas de conteúdo, listas de dados ou carregamento de seções específicas da interface.
  * `large`: Tamanho Grande. Recomendado para indicar carregamento em áreas amplas, como telas completas (fullscreen), blocos de informação proeminentes ou quando o carregamento é o foco principal da interação.

Small

Medium

Large

```jsx
import { EzSpinner } from "@sankhyalabs/ezui/react/components";
import "./size.css";

const Demo = () => {
  return (
    <div className="ez-spinner-demo__size-comparison">
      <div className="ez-spinner-demo__size-item">
        <EzSpinner size="small" />
        <span className="ez-spinner-demo__size-label">Small</span>
      </div>

      <div className="ez-spinner-demo__size-item">
        <EzSpinner size="medium" />
        <span className="ez-spinner-demo__size-label">Medium</span>
      </div>

      <div className="ez-spinner-demo__size-item">
        <EzSpinner size="large" />
        <span className="ez-spinner-demo__size-label">Large</span>
      </div>
    </div>
  );
};

export default Demo;
```

## Exemplos de uso

### Carregamento de página

Use o spinner para indicar que uma página ou seção está carregando.

Carregando página...

### Com texto descritivo

Combine o spinner com um texto para fornecer contexto sobre o que está sendo carregado.

Salvando dados...

```jsx
import { EzSpinner } from "@sankhyalabs/ezui/react/components";
import "./with-text.css";

const Demo = () => {
    return (
        <div className="ez-spinner-demo__with-text">
            <EzSpinner size="medium" />
            <span className="ez-spinner-demo__text">
                Salvando dados...
            </span>
        </div>
    );
};

export default Demo;
```

### Spinner sobreposto

Use o spinner sobre o conteúdo que está sendo carregado para indicar o estado de carregamento.

### Dados da Tabela

### Em botões

Integre o spinner em botões para indicar ações em processamento.

Clique para ver o spinner no botão

```jsx
import { useState } from "react";
import { EzButton, EzSpinner } from "@sankhyalabs/ezui/react/components";
import "./in-button.css";

const Demo = () => {
    const [isLoading, setIsLoading] = useState(false);

    const handleClick = () => {
        setIsLoading(true);
        // Simula uma operação que demora 3 segundos
        setTimeout(() => {
            setIsLoading(false);
        }, 3000);
    };

    return (
        <div>
            <EzButton
                onClick={handleClick}
                label={isLoading ? 'Processando...' : 'Processar Dados'}
                className="ez-spinner-demo__button"
            >
                {isLoading &&
                    <div slot="rightIcon" className="ez-spinner-demo__button-spinner">
                        <EzSpinner />
                    </div>
                }
            </EzButton>

            <span className="ez-spinner-demo__button-text">
                {isLoading ? 'Aguarde...' : 'Clique para ver o spinner no botão'}
            </span>
        </div>
    );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| size | size | Define o tamanho do spinner | "large" \| "medium" \| "small" | 'small' |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-spinner--color | Define a cor do spinner. |
| --ez-spinner--size-default | Define o tamanho padrão do spinner. |
| --ez-spinner--size-medium | Define o tamanho médio do spinner. |
| --ez-spinner--size-large | Define o tamanho grande do spinner. |
| --ez-spinner--animation-duration | Define a duração da animação do spinner. |
