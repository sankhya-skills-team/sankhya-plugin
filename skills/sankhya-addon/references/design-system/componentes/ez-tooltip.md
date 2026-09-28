> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip/ (snapshot 2026-09-28)

# Tooltip

Tooltip é um componente flutuante que exibe uma mensagem de texto quando o usuário passa o mouse sobre um elemento.

O tooltip é um componente inerte, ou seja, ele não possui eventos de foco, seleção ou clique.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzTooltip, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  return (
    <div className="snk-container" style={{
      display: 'flex',
      'flex-direction': 'column',
      height: '80px',
      width: '100%',
      alignItems: 'center',
      justifyContent: 'center',
    }}>
      <div >
        <EzTooltip message="Mensagem que deve ser apresentada!">
          <EzIcon iconName="configuration" />
        </EzTooltip>
      </div>
    </div>
  );
};

export default Demo;
```

## Tipos de Tooltip

> Propriedade utilizada: `type`

Atualmente o tooltip pode assumir um dos seguintes tipos: `default`, `success`, `warning` e `error`.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzTooltip, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div className="snk-container" style={{
      height: '80px',
      width: '100%',
      alignItems: 'center',
      justifyContent: 'center',
      display: 'flex',
    }}>
      <div style={{
        display: 'flex',
        width: '200px',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}>
        <div>
          <EzTooltip message="Tipo default">
            <EzIcon iconName="configuration" />
          </EzTooltip>
        </div>

        <div>
          <EzTooltip message="Tooltipo do tipo success" type={'success'}>
            <EzIcon iconName="check" />
          </EzTooltip>
        </div>

        <div>
          <EzTooltip message="Tooltipo do tipo warning" type={'warning'}>
            <EzIcon iconName="alert-circle-inverted" />
          </EzTooltip>
        </div>

        <div>
          <EzTooltip message="Tooltipo do tipo error" type={'error'}>
            <EzIcon iconName="close" />
          </EzTooltip>
        </div>
      </div>
    </div>
  );
};

export default Demo;
```

## Posicionamento

> Propriedade utilizada: `placement`

O tooltip pode assumir diferentes posicionamentos, conforme necessidade.

bottom

top

left

right

## Espaçamento entre o elemento âncora

> Propriedade utilizada: `gapOptions`

É possível definir o espaçamento entre o tooltip e seu elemento âncora de forma simples.

verticalGap

horizontalGap

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzTooltip, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const styleSpan = {
    padding: '8px',
    border: '1px solid #ccc',
    borderRadius: '8px',
  };

  return (
    <div className="snk-container" style={{
      height: '80px',
      width: '100%',
      alignItems: 'center',
      justifyContent: 'center',
      display: 'flex',
    }}>
      <div style={{
        display: 'flex',
        width: '280px',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}>
        <div>

          <EzTooltip message="Gap vertical entre tooltip e componente"
                     gapOptions={{ horizontalGap: 0, verticalGap: 15 }}>
            <span style={styleSpan}>verticalGap</span>
          </EzTooltip>
        </div>

        <div>
          <EzTooltip message="Gap vertical entre tooltip e componente" placement="left"
                     gapOptions={{ horizontalGap: 15, verticalGap: 0 }}>
            <span style={styleSpan}>horizontalGap</span>
          </EzTooltip>

        </div>

      </div>
    </div>
  );
};

export default Demo;
```

## Debounce

> Propriedade utilizada: `debouncingTime`

Podemos definir um delay para o tempo de exibição do tooltip.

2 segundos

50 milissegundos

## Largura máxima

> Propriedades utilizadas: `maxWidth` e `useAnchorSize`

Podemos ajustar a largura máxima do tooltip conforme necessidade, ou mesmo definir que o tooltip terá a largura do elemento âncora.

Padrão (200px)

50px

500px

Tamanho da âncora

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzTooltip, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const styleSpan = {
    padding: '8px',
    border: '1px solid #ccc',
    borderRadius: '8px',
  };

  return (
    <div className="snk-container" style={{
      height: '80px',
      width: '100%',
      alignItems: 'center',
      justifyContent: 'center',
      display: 'flex',
    }}>
      <div style={{
        display: 'flex',
        width: '600px',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}>
        <div>
          <EzTooltip message="Largura máxima tem o padrão de 200px ">
            <span style={styleSpan}> Padrão (200px)</span>
          </EzTooltip>
        </div>

        <div>
          <EzTooltip message="Podemos definir um tamanho menor. Por exemplo 50PX" maxWidth={50}>
            <span style={styleSpan}> 50px</span>
          </EzTooltip>
        </div>

        <div>
          <EzTooltip
            message="Podemos definir também um maior, conforme a necessidade. Neste exemplo usamos um tamanho máximo de 500px"
            maxWidth={500}>
            <span style={styleSpan}> 500px</span>
          </EzTooltip>
        </div>

        <div>
          <EzTooltip
            message="Se necessário, podemos definir a largura do tooltip como igual à largua do elemento âncora"
            useAnchorSize={true}>
            <span style={styleSpan}> Tamanho da âncora</span>
          </EzTooltip>
        </div>

      </div>
    </div>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| active | active | Define se o tooltip está ativo. | boolean | true |
| anchoringElement | -- | Elemento HTML que será utilizado como ancoragem do tooltip. | HTMLElement | undefined |
| debouncingTime | debouncing-time | Tempo de espera para exibir o tooltip após o evento de mouseenter. | number | 500 |
| gapOptions | -- | Define o espaçamento entre o tooltip e o elemento de ancoragem. | { horizontalGap: number; verticalGap: number; } | { horizontalGap: 0, verticalGap: 0 } |
| maxWidth | max-width | Define a largura máxima do elemento. | number | 200 |
| message | message | Mensagem que será apresentada no tooltip. | string | undefined |
| placement | placement | Define a posição do tooltip em relação ao elemento de ancoragem. | "bottom" \| "bottom-end" \| "bottom-start" \| "left" \| "left-end" \| "left-start" \| "right" \| "right-end" \| "right-start" \| "top" \| "top-end" \| "top-start" | 'bottom' |
| strategy | strategy | Define a estratégia de posicionamento do tooltip. Use 'fixed' quando o elemento estiver dentro de containers com position: relative. | "absolute" \| "fixed" | 'absolute' |
| type | type | Define o tipo de tooltip a ser exibido. | "default" \| "error" \| "success" \| "warning" | 'default' |
| useAnchorSize | use-anchor-size | Define se o elemento manterá o mesmo tamanho do componente de ancora. | boolean | false |

### Dependencies

#### Used by

  * ez-chip
  * ez-grid-pagination
  * ez-multi-select-input
  * ez-record-navigation
  * ez-simple-image-uploader
  * ez-split-button
  * ez-text-area
  * ez-text-input

### CSS Variables

| Variable | Description |
|---|---|
| --ez-tooltip--triangle-size | Define o tamanho do triângulo da seta do tooltip. |
| --ez-tooltip--z-index | Define o z-index do tooltip. |
| --ez-tooltip--padding | Define o padding interno do tooltip. |
| --ez-tooltip--border-radius | Define o border-radius do tooltip. |
| --ez-tooltip--font-family | Define a família da fonte do tooltip. |
| --ez-tooltip--font-size | Define o tamanho da fonte do tooltip. |
| --ez-tooltip--font-weight | Define o peso da fonte do tooltip. |
