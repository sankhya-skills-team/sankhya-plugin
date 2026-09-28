> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert/ (snapshot 2026-09-28)

# Alert

O componente Alert tem o papel de apresentar mensagens de feedback contextuais no padrão de alerta, erro ou sucesso.

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

demo.js

```jsx
import React from 'react';
import { EzAlert } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <div className="ez-padding--medium ez-margin--small">
                <EzAlert alertType="warn">Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.</EzAlert>
            </div>
            <div className="ez-padding--medium ez-margin--small">
                <EzAlert alertType="critical">Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.</EzAlert>
            </div>
            <div className="ez-padding--medium ez-margin--small">
                <EzAlert alertType="success">Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.</EzAlert>
            </div>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Alerta

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

demo.js

```jsx
import React from 'react';
import { EzAlert } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  return (
    <div className="ez-flex">
      <EzAlert alertType="warn">Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.</EzAlert>
    </div>
  )
};

export default Demo;
```

### Erro

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

### Sucesso

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

demo.js

```jsx
import React from 'react';
import { EzAlert } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  return (
    <div className="ez-flex">
      <EzAlert alertType="success">Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.</EzAlert>
    </div>
  )
};

export default Demo;
```

### Tamanho

A largura do componente é definida livremente de acordo com o espaço disponível na tela ou o tamanho fixo do componente pai. Já a altura é determinada pelo conteúdo interno.

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.

### Quebra de linha

O componente conta com a funcionalidade de quebra automática de palavras (hyphenation) para evitar espaços excessivos em branco e melhorar a legibilidade do texto.

Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.Os alert badges são utilizados para informar um sucesso, alerto ou erro em cards, popups, modais e telas.Os alert badges são utilizados para informar um sucesso, alerto ou erro em cards, popups, modais e telas.

demo.js

```jsx

import React from 'react';
import { EzAlert } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  return (
    <div class="ez-row">
      <div class="ez-col ez-col--sd-6 ez-padding--medium">
        <EzAlert alertType="warn">Os alert badges são utilizados para informar um sucesso, alerta ou erro em cards, popups, modais e telas.Os alert badges são utilizados para informar um sucesso, alerto ou erro em cards, popups, modais e telas.Os alert badges são utilizados para informar um sucesso, alerto ou erro em cards, popups, modais e telas.</EzAlert>
      </div>
    </div>
  )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alertType | alert-type | Define a cor e o ícone a serem exibidos no componente. | "critical" \| "success" \| "warn" | 'success' |

### Dependencies

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-alert-alert-container--padding-up-down | Define o raio do padding interno para cima e para baixo. |
| --ez-alert-alert-container--padding-right-left | Define o raio do padding interno para a esquerda e para a direita. |
| --ez-alert-alert-container--gap | Define o espaçamento entre os elementos internos |
| --ez-alert-alert-container--border-radius | Define o raio da borda do corpo do Alert. |
| --ez-alert-alert-container--font-color-warn | Define a cor da fonte no estilo Warn. |
| --ez-alert-alert-container--icon-warn | Define a cor do ícone no estilo Warn. |
| --ez-alert-alert-container--background-color-warn | Define a cor do background no estilo Warn. |
| --ez-alert-alert-container--font-color-critical | Define a cor da fonte no estilo Critical. |
| --ez-alert-alert-container--icon-critical | Define a cor do ícone no estilo Critical. |
| --ez-alert-alert-container--background-color-critical | Define a cor do background no estilo Critical. |
| --ez-alert-alert-container--font-color-success | Define a cor da fonte no estilo Success. |
| --ez-alert-alert-container--icon-success | Define a cor do ícone no estilo Success. |
| --ez-alert-alert-container--background-color-success | Define a cor do background no estilo Success. |
