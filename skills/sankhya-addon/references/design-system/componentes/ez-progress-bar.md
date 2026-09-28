> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-progress-bar/ (snapshot 2026-09-28)

# ProgressBar

Documentação do componente EzProgressBar.

Barra de progresso30%

Texto auxiliar para contextualização

```jsx
import React, { useRef, useEffect, useState } from 'react';
import { EzProgressBar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const element = useRef(null);

  const [progressValue, setProgressValue] = useState(10);

  useEffect(() => {
    const timer = setTimeout(() => {
      setProgressValue((prev) =>
        prev >= 90 ? 10 : prev + Math.floor(Math.random() * 15) + 5,
      );
    }, 800);
    return () => clearTimeout(timer);
  }, [progressValue]);

  return (
    <div className="ez-flex">
      <EzProgressBar ref={element} percent={progressValue} label={'Barra de progresso'} helpText={"Texto auxiliar para contextualização"} />
    </div>
  );
};

export default Demo;
```

## Label

O `label` é uma propriedade **opcional** que pode ser usada para exibir um texto descritivo acima da barra de progresso. Ao defini-lo, ele será exibido como um título para a barra de progresso, proporcionando contexto adicional sobre o que a barra representa.

Ao ocultá-lo, a barra de progresso ainda funcionará normalmente, mas não terá um título descritivo e não exibirá o valor da percentagem atual.

Com label

Título70%

Texto auxiliar

Sem label

Texto auxiliar

demo.js

```jsx
import '../demo.css';
import React, { useRef } from 'react';
import { EzProgressBar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const element = useRef(null);

  return (
    <div className="progress-bar-demo__container">

      <div className={'progress-bar-demo__example'}>
        <span className={'progress-bar-demo__label'}>Com label</span>
        <EzProgressBar ref={element} percent={70} label={'Título'} helpText={"Texto auxiliar"} />
      </div>

      <hr className={'progress-bar-demo__divider'} />

      <div className={'progress-bar-demo__example'}>
        <span className={'progress-bar-demo__label'}>Sem label</span>
        <EzProgressBar ref={element} percent={70} helpText={"Texto auxiliar"} />
      </div>
    </div>
  );
};

export default Demo;
```

## HelpText

O `helpText` é uma propriedade **opcional** que pode ser usada para fornecer informações adicionais sobre a barra de progresso.

Ao definir o `helpText`, ele será exibido abaixo da barra de progresso, oferecendo contexto ou instruções adicionais sobre o que a barra representa.

Com helpText

Barra de progresso70%

Texto auxiliar para contextualização

Sem helpText

Barra de progresso70%

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| helpText | help-text | Mensagem auxiliar para contextualizar barra de carregamento. | string | undefined |
| label | label | Rótulo da barra de progresso. | string | undefined |
| percent | percent | Porcentagem de preenchimento da barra. | number | undefined |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-progress-bar-container-height | Define a altura do container da barra de progresso. |
| --ez-progress-bar-radius | Define o arredondamento da barra de progresso e de seu container. |
| --ez-progress-bar-container-background | Define a cor de fundo do container da barra de progresso. |
| --ez-progress-bar-container-border | Define a cor de fundo do container da barra de progresso. |
| --ez-progress-bar-height | Define a altura da barra de progresso interna. |
| --ez-progress-bar-background | Define a altura da barra de progresso. |
| --ez-progress-bar-font-size | Define o tamanho da fonte do header. |
| --ez-progress-bar-header-color | Define a cor do texto do label. |
| --ez-progress-bar-gap | Define o espaçamento entre o header e a progressbar. |
| --ez-progress-bar-help-text-color | Define a cor do texto do help text. |
| --ez-progress-bar-help-text-font-size | Define a cor do texto do help text. |
