> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-check/ (snapshot 2026-09-28)

# Check

Os CheckBox são usados para permitir ao usuário selecionar uma ou mais opções de uma lista de opções. Utilize os checkbox quando o usuário possui múltipla escolha em uma grade, por exemplo.

Através da propriedade `mode`, existem dois modos de visualização: **regular** e **switch**.

  * Se esta propriedade for omitida, o componente assume o formato "regular".
  * No modo **regular** a visualização é a tradicional de uma caixinha marcada/desmarcada.
  * No modo **switch** o campo tem uma interface em formato de um pino liga/desliga.

demo.js

```jsx
import React from 'react';
import { EzCheck } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex">
            <EzCheck label="Exemplo 1"></EzCheck>
            <EzCheck label="Exemplo 2" value="true"></EzCheck>
        </div>
    );
};

export default Demo;
```

## Variações e estados

### Habilitado

Utilizado nos momentos em que o usuário pode interagir com o checkbox. É permitido marcar e desmarcar ele.

demo.js

```jsx
import React from 'react';
import { EzCheck } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzCheck
            label="Exemplo de checkbox habilitado por padrão"
            enabled="true">
        </EzCheck>
    );
}

export default Demo;
```

### Desabilitado

Utilizado quando seu conteúdo não pode ser modificado. Podendo ser por questões como permissão ou regra da própria tela. Por exemplo:

### Marcado

O checkbox estará nesse estado quando estiver marcado e seu valor será considerado para as operações que serão feitas no sistema.

demo.js

```jsx
import React from "react";
import { EzCheck } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <EzCheck
      label="Exemplo de checkbox marcado"
      value="true">
    </EzCheck>
  );
};

export default Demo;
```

### Desmarcado

O checkbox estará nesse estado quando estiver desmarcado e seu valor será considerado para as operações que serão feitas no sistema.

### Indeterminado

Deixa o campo em um estado indeterminado, nem marcado nem desmarcado. (não disponível em modo "switch")

demo.js

```jsx
import React from "react";
import { EzCheck } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <EzCheck
      label="Exemplo de checkbox indeterminado"
      indeterminate="true">
    </EzCheck>
  );
};

export default Demo;
```

### Versão alternativa (Switch)

#### Marcado

#### Desmarcado

demo.js

```jsx
import React from "react";
import { EzCheck } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  return (
    <EzCheck
      label="Exemplo de checkbox do tipo switch desmarcado"
      value="false"
      mode="switch">
    </EzCheck>
  );
};

export default Demo;
```

#### Compacto

### Principais métodos

#### getMode()

Utilizado para obter o modo atual do checkbox (regular ou switch).

Mode: ****

demo.js

```jsx
import React, { useRef, useState } from "react";
import { EzCheck, EzButton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  const element = useRef(null);
  const [mode, setMode] = useState(null);

  const onClick = () => {
    element.current.getMode().then(setMode);
  };

  return (
    <div className="ez-flex ez-flex--column ez-flex--align-items-center">
      <EzCheck
        ref={element}
        label="Exemplo de checkbox regular">
      </EzCheck>

      <label>
        Mode: <strong>{mode}</strong>
      </label>

      <EzButton
        label="Chamar Método"
        className="ez-margin-vertical--medium"
        onClick={onClick}>
      </EzButton>

      <EzButton
        label="Limpar"
        onClick={() => setMode(null)}>
      </EzButton>
    </div>
  );
};

export default Demo;
```

#### setFocus()

Utilizado para setar o foco no checkbox.

Focado: **Não**

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do check (onEzChange).

Valor: **false**

demo.js

```jsx
import React, { useState } from "react";
import { EzCheck } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
  const [value, setValue] = useState(false);

  return (
    <div className="ez-flex ez-flex--column ez-flex--align-items-center">
      <EzCheck
        label="Exemplo de checkbox regular"
        onEzChange={evt => setValue(evt.detail)}>
      </EzCheck>

      <label>
        Valor: <strong>{value.toString()}</strong>
      </label>
    </div>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alternativePlaceholder | alternative-placeholder | Texto alternativo a ser apresentado como título do campo. | string | undefined |
| compact | compact | Define o modo compacto com espaçamento menor entre label e o input | boolean | false |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| indeterminate | indeterminate | Se true ativa o estado indeterminado, nem marcado nem desmarcado (não disponível em modo switch ). | boolean | undefined |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mode | mode | Define o modo de visualização do ez-check. | CheckMode.REGULAR \| CheckMode.SWITCH | CheckMode.REGULAR |
| value | value | Define o valor do campo. | boolean | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<any> |

### Methods

#### `getMode() => Promise<CheckMode>`

Obtém o modo escolhido.

##### Returns

Type: `Promise<CheckMode>`

#### `setFocus() => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form-view
  * ez-link-builder
  * ez-list
  * ez-multi-selection-list

### CSS Variables

| Variable | Description |
|---|---|
| --ez-check--box--width | Define a largura do box do checkbox. |
| --ez-check--box--height | Define a altura do box do checkbox. |
| --ez-check--width | Define a largura do input do checkbox. |
| --ez-check--height | Define a altura do input do checkbox |
| --ez-check--border-radius | Define o raio da borda do input do checkbox. |
| --ez-check--checked--background-color | Define a cor de fundo do input do checkbox quando marcado. |
| --ez-check--focus--background-color | Define a cor de fundo do input do checkbox quando focado. |
| --ez-check--hover--background-color | Define a cor de fundo do input do checkbox quando o cursor está sobre ele. |
| --ez-check--checked--disabled--background-color | Define a cor de fundo do input do checkbox quando marcado e desabilitado. |
| --ez-check--border | Define o estilo da borda do input do checkbox. |
| --ez-check--disabled--border | Define o estilo da borda do input do checkbox quando desabilitado. |
| --ez-check--checked--border | Define o estilo da borda do input do checkbox quando marcado. |
| --ez-check--checked--hover--background-color | Define a cor de fundo do input do checkbox quando ativo e com o cursor sobre ele. |
| --ez-check--checked--focus--background-color | Define a cor de fundo do input do checkbox quando ativo e focado. |
| --ez-check--check--image | Contém o ícone do input marcado. |
| --ez-check--indeterminate--image | Ícone usado para o estado "indeterminado" do componente. |
| --ez-check--check--background-color | Define a cor de fundo do slot do ícone quando marcado. |
| --ez-check--check--disabled--background-color | Define a cor de fundo do slot do ícone quando marcado e desabilitado. |
| --ez-switch--slider--width | Define a largura do slider do checkbox. |
| --ez-switch--slider--height | Define a altura do slider do checkbox. |
| --ez-switch--pin--width | Define a largura do pino do slider do checkbox. |
| --ez-switch--pin--height | Define a altura do pino do slider do checkbox. |
| --ez-switch--focus--width | Define a largura do slider quando focado. |
| --ez-switch--focus--height | Define a altura do slider quando focado. |
| --ez-switch--background-color | Define a cor de fundo do checkbox no modo switch. |
| --ez-switch--disabled--background-color | Define a cor de fundo do checkbox desabilitado no modo switch. |
| --ez-switch--disabled--checked--background-color | Define a cor de fundo do checkbox marcado no modo switch. |
| --ez-switch--checked--background-color | Define a cor de fundo do checkbox marcado no modo switch. |
| --ez-switch--pin--background-color | Define a cor de fundo do pino do slider. |
| --ez-switch--pin--disabled--background-color | Define a cor de fundo do pino do slider quando desabilitado. |
| --ez-switch--pin--checked--background-color | Define a cor de fundo do pino do slider quando marcado. |
| --ez-switch--pin--checked--disabled--background-color | Define a cor de fundo do pino do slider quando marcado e desabilitado1. |
| --ez-switch--pin--focus--background-color | Define a cor de fundo do pino do slider quando focado. |
| --ez-switch--pin--checked--focus--background-color | Define a cor de fundo do pino do slider quando marcado e focado. |
| --ez-switch--pin--border-color | Define a cor da borda do pino do slider. |
| --ez-switch--pin--disabled--border-color | Define a cor da borda do pino do slider quando desabilitado. |
| --ez-check--label--font-size | Define o tamanho da fonte do label. |
| --ez-check--label--font-family | Define a família da fonte do label. |
| --ez-check--label--color | Define a cor da fonte do label. |
| --ez-check--label--disabled--color | Define a cor da fonte do label quando desabilitado. |
