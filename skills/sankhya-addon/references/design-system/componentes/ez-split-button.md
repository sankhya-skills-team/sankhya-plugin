> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-button/ (snapshot 2026-09-28)

# Split Button

O componente Split Button tem o papel de permitir que o usuário execute uma ação principal ao clicar no botão principal, enquanto também oferece acesso a opções secundárias ou um menu suspenso quando a seta para baixo é clicada. Isso é útil para agrupar funcionalidades relacionadas em um espaço limitado e oferecer uma experiência de usuário mais eficiente.

Primário

Secundário

Terciário

```jsx
import React from 'react';
import { EzSplitButton} from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";
import './demo.css';

const btnClick = (tipo) => (
  ApplicationUtils.message("Título da Mensagem", `Clicou no botão ${tipo}.`)
)

const itemClick = (tipo) => (
  ApplicationUtils.message("Título da Mensagem", `Clicou no item ${tipo}.`)
)

const subAction = (tipo) => (
  ApplicationUtils.message("Título da Mensagem", `Clico na subAction ${tipo}.`)
)

const dropdownItems = [
  {
      id: "1",
      label: "Emitir NFe",
      type: "item",
      subAction: {
          id: "sub1",
          label: "Agendar",
          type: 'primary'
      }
  },
  {
      id: "2",
      label: "Cancelar NFe",
      type: "item",
      subAction: {
          id: "sub2",
          label: "Termos da legislação",
          type: 'critical'
      }
  },
  {
      id: "3",
      label: "Exportar NFe",
      type: "item",
      children: [
          {
              id: "4",
              label: "Danfe PDF",
              type: "item",
              children: [
                  {
                      id: "6",
                      label: "Modo retrato",
                      type: "item"
                  },
                  {
                      id: "7",
                      label: "Modo paisagem",
                      type: "item"
                  }
              ],
              subAction: {
                  id: "sub3",
                  label: "Selecionar impressora",
                  type: 'primary'
              }
          },
          {
              id: "5",
              label: "XML",
              type: "item"
          }
      ]
  }
];

const Demo = () => {
    return (
      <div className="ez-flex ez-flex--row">
        <div className="display-column">
          <span className="ez-text ez-text--secondary ez-margin--small">Primário</span>
          <EzSplitButton
              label={"Primário"}
              variant="primary"
              mode="icon-left"
              size="large"
              leftIconName={"bell"}
              items={dropdownItems}
              onButtonClick={() => btnClick("primário icon-left")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              label="Primário"
              variant="primary"
              size="large"
              items={dropdownItems}
              onButtonClick={() => btnClick("primário text only")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              variant="primary"
              mode="icon-only"
              size="large"
              leftIconName={"bell"}
              leftTitle="Primário Icon Only"
              items={dropdownItems}
              onButtonClick={() => btnClick("primário icon-only")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              label="Primário Disabled"
              variant="primary"
              size="large"
              leftIconName={"arrow_back"}
              rightIconName={"arrow-forward"}
              items={dropdownItems}
              onButtonClick={() => btnClick("primário disabled")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
              isDisabled
          />
        </div>
        <div className="display-column">
          <span className="ez-text ez-text--secondary ez-margin--small">Secundário</span>
          <EzSplitButton
              label={"Secundário"}
              variant="secondary"
              mode="icon-left"
              size="large"
              leftIconName={"bell"}
              items={dropdownItems}
              onButtonClick={() => btnClick("secundário icon-left")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              label="Secundário"
              variant="secondary"
              size="large"
              items={dropdownItems}
              onButtonClick={() => btnClick("secundário text only")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              variant="secondary"
              mode="icon-only"
              size="large"
              leftIconName={"check"}
              leftTitle="Secundário Icon Only"
              items={dropdownItems}
              onButtonClick={() => btnClick("secundário icon-only")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              label="Secundário Disabled"
              variant="secondary"
              mode="icon-left"
              size="large"
              leftIconName={"lock-alt"}
              items={dropdownItems}
              onButtonClick={() => btnClick("secundário disabled")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
              isDisabled
          />
        </div>
        <div className="display-column">
          <span className="ez-text ez-text--secondary ez-margin--small">Terciário</span>
          <EzSplitButton
              label={"Terciário"}
              variant="tertiary"
              mode="icon-left"
              size="large"
              leftIconName={"bell"}
              items={dropdownItems}
              onButtonClick={() => btnClick("terciário icon-left")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              label="Terciário"
              variant="tertiary"
              size="large"
              items={dropdownItems}
              onButtonClick={() => btnClick("terciário text only")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              variant="tertiary"
              mode="icon-only"
              size="large"
              leftIconName={"clipboard"}
              leftTitle="Terciário Icon Only"
              items={dropdownItems}
              onButtonClick={() => btnClick("terciário icon-only")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
          />
          <EzSplitButton
              label={"Terciário Disabled"}
              variant="tertiary"
              mode="icon-left"
              size="large"
              leftIconName={"bell"}
              items={dropdownItems}
              onButtonClick={() => btnClick("terciário disabled")}
              onDropdownItemClick={(item) => itemClick(item.detail.label)}
              onDropdownSubActionClick={(action) => subAction(action.detail.label)}
              isDisabled
          />
        </div>
    </div>
    )
};

export default Demo;
```

## Variações e estados

Utilize o atributo class ou a prop variant para alterar o estado do botão

Os estados dos botões podem ser alterados através da utilização das classes `ez-split-button--primary`, `ez-split-button--secondary` e `ez-split-button--tertiary` ou através da prop `variant` com os valores `primary`, `secondary` e `tertiary`. O estado secundário é o padrão, portanto não precisa ser adicionado.

### Primário

É o botão de maior destaque da tela. Ele orienta a ação principal onde está inserido. Por isso, deve ser usado apenas 1 por bloco.

**Usando a prop variant e classe CSS:**

### Secundário

É o botão mais comum e com mais opções de uso.

**Usando a prop variant e classe CSS:**

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function Secondary() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="ez-flex ez-flex--row ez-flex--justify-around">
      <EzSplitButton
        label="Botão Secundário"
        variant="secondary"
        items={dropdownItems}
      />

      <EzSplitButton
        label="Botão Secundário (CSS)"
        className="ez-split-button--secondary"
        items={dropdownItems}
      />
    </div>
  );
}
```

### Terciário

Normalmente acompanha um botão primário e expressa uma ação mais incomum na jornada.

**Usando a prop variant e classe CSS:**

### Habilitado

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';
import '../demo.css'

export default function Enabled() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="demo-container">
      <EzSplitButton
        label="Botão Habilitado"
        enabled={true}
        items={dropdownItems}
      />
    </div>
  );
}
```

### Desabilitado

Existem 2 formas de desabilitar um split button utilizando a prop `isDisabled`.

Quando passamos o valor `isDisabled={"full"}`, temos o disable nativo do HTML, onde o botão fica inacessível, ou seja, não entra na navegação via teclado.

Quando passamos o valor `isDisabled={true}` (recomendado), temos um disable acessível, onde o usuário ainda pode acessar o botão via teclado, mesmo que a interação com ele esteja bloqueada.

#### Disabled Acessível (recomendado)

#### Disabled Completo

### Label

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function Label() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="ez-flex ez-flex--row ez-flex--justify-around">
      <EzSplitButton
        label="Minha Label Personalizada"
        items={dropdownItems}
      />
    </div>
  );
}
```

### Tooltips

No hover, os botões esquerdo e direito apresentam, respectivamente, os valores da própria label e 'Mais opções' como padrão.

### Tooltip personalizado do botão esquerdo

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function LeftTitle() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="ez-flex ez-flex--row ez-flex--justify-around">
      <EzSplitButton
        label="Ação Principal"
        leftTitle="Tooltip personalizado do botão esquerdo"
        items={dropdownItems}
      />
    </div>
  );
}
```

### Tooltip personalizado do botão direito

### Suprimir animação

A animação de ripple do componente pode ser suprimida pela prop `suppressAnimation`.

#### Com animação (padrão)

#### Sem animação

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function SuppressAnimation() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div>
      <div style={{ display: 'flex', gap: '16px', flexDirection: 'column' }}>
        <div className="demo-container">
          <h4>Com animação (padrão)</h4>
          <EzSplitButton
            label="Com Ripple"
            items={dropdownItems}
          />
        </div>
        <div className="demo-container">
          <h4>Sem animação</h4>
          <EzSplitButton
            label="Sem Ripple"
            suppressAnimation={true}
            items={dropdownItems}
          />
        </div>
      </div>
    </div>
  );
}
```

### Modos

#### Ícone (icon-only)

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function IconOnly() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="ez-flex ez-flex--row ez-flex--justify-around">
      <EzSplitButton
        leftIconName="star"
        mode="icon-only"
        items={dropdownItems}
      />
    </div>
  );
}
```

#### Somente texto (default)

#### Ícone e texto (icon-left)

### Tamanhos

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function Size() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="demo-container">
      <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
        <EzSplitButton
          label="Small"
          size="small"
          items={dropdownItems}
        />
        <EzSplitButton
          label="Medium"
          size="medium"
          items={dropdownItems}
        />
        <EzSplitButton
          label="Large"
          size="large"
          items={dropdownItems}
        />
      </div>
    </div>
  );
}
```

### Ícones personalizados

#### Ícone esquerdo personalizado

#### Ícone direito personalizado

demo.js

```jsx
import React from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function RightIconName() {
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  return (
    <div className="ez-flex ez-flex--row ez-flex--justify-around">
      <EzSplitButton
        label="Ícone Direito"
        rightIconName="settings"
        items={dropdownItems}
      />
    </div>
  );
}
```

### Imagens personalizadas

#### Imagem personalizada

## Eventos

### Clique no botão principal

Botão clicado 0 vez(es)

demo.js

```jsx
import React, { useState } from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function ButtonClick() {
  const [clickCount, setClickCount] = useState(0);
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  const handleButtonClick = () => {
    setClickCount(prev => prev + 1);
  };

  return (
    <div className="demo-container">
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <EzSplitButton
          label="Clique no botão principal"
          items={dropdownItems}
          onButtonClick={handleButtonClick}
        />
        <p>Botão clicado {clickCount} vez(es)</p>
      </div>
    </div>
  );
}
```

### Clique em item do dropdown

### Clique em subação do dropdown

demo.js

```jsx
import React, { useState } from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function DropdownSubActionClick() {
  const [subAction, setSubAction] = useState(null);
  const dropdownItems = [
    {
        label: 'Item com subações',
        value: 'item1',
        subAction: { id: 'sub1', label: 'Editar', value: 'edit' },
    },
    {
        label: 'Item simples',
        value: 'item2',
        subAction: { id: 'sub2', label: 'Excluir', value: 'delete', type: 'critical' },
     }
  ];

  const handleSubActionClick = (event) => {
    setSubAction(event.detail);
  };

  return (
    <div className="demo-container">
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <EzSplitButton
          label="Com subações"
          items={dropdownItems}
          onDropdownSubActionClick={handleSubActionClick}
        />
        {subAction && (
          <p>Subação executada: {subAction.label} (valor: {subAction.value})</p>
        )}
      </div>
    </div>
  );
}
```

## Exemplos de métodos

### Adicionar foco no botão esquerdo

### Adicionar foco no botão direito

demo.js

```jsx
import React, { useRef } from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function SetRightFocus() {
  const buttonRef = useRef(null);
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' }
  ];

  const handleFocusRight = () => {
    if (buttonRef.current) {
      buttonRef.current.setRightButtonFocus();
    }
  };

  return (
    <div className="demo-container">
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <EzSplitButton
          ref={buttonRef}
          label="Split Button"
          items={dropdownItems}
        />
        <button onClick={handleFocusRight}>
          Focar no botão direito
        </button>
      </div>
    </div>
  );
}
```

### Remover foco

### Alternar dropdown

demo.js

```jsx
import React, { useRef } from 'react';
import { EzSplitButton } from '@sankhyalabs/ezui/react/components';

export default function ToggleDropdown() {
  const buttonRef = useRef(null);
  const dropdownItems = [
    { label: 'Opção 1', value: 'option1' },
    { label: 'Opção 2', value: 'option2' },
    { label: 'Opção 3', value: 'option3' }
  ];

  const handleToggle = () => {
    if (buttonRef.current) {
      buttonRef.current.toggleDropdown();
    }
  };

  return (
    <div className="demo-container">
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <EzSplitButton
          ref={buttonRef}
          label="Split Button"
          items={dropdownItems}
        />
        <button onClick={handleToggle}>
          Alternar dropdown
        </button>
      </div>
    </div>
  );
}
```

### Verificar se o dropdown está aberto

Dropdown está fechado

## API do componente

### Overview

Split Button Component

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| enabled | enabled | ⚠️ [DEPRECATED] Use isDisabled prop instead.Se false o usuário não pode interagir com o botão. | boolean | true |
| iconName | icon-name | ⚠️ [DEPRECATED] Use leftIconName prop instead.Define o ícone a ser usado da biblioteca de ícones: ez-icons | string | undefined |
| image | image | Define o caminho usado nos modos icon-only e icon-left para imagens não contempladas na biblioteca de ícones. | string | undefined |
| isDisabled | is-disabled | Se verdadeiro o clique no botão fica desabilitado mas a navegação continua funcional. Se full, o usuário não pode interagir com o botão. | "" \| "full" \| boolean | false |
| itemBuilder | -- | Função builder que possibilita alterar como o item da lista vai ser apresentado. Observação: No react ele se transforma em VNode e não como HTMLElement. | (item: IDropdownItem, level: number) => string \| HTMLElement | undefined |
| items | -- | Define o conteúdo do dropdown. | IDropdownItem[] | undefined |
| label | label | Texto a ser apresentado como label do botão. | string | undefined |
| leftIconName | left-icon-name | Define o ícone esquerdo a ser usado da biblioteca de ícones: ez-icons | string | undefined |
| leftTitle | left-title | Texto a ser apresentado como title do botão principal | string | undefined |
| mode | mode | Define o modo de uso do botão. | "default" \| "icon-left" \| "icon-only" | 'default' |
| rightIconName | right-icon-name | Define o ícone direito a ser usado da biblioteca de ícones: ez-icons | string | undefined |
| rightTitle | right-title | Texto a ser apresentado como title do botão dropdown | string | undefined |
| show | show | Se true, o dropdown do botão é exibido. | boolean | false |
| size | size | Define o tamanho do ez-split-button. | "large" \| "medium" \| "small" | 'medium' |
| suppressAnimation | suppress-animation | Se verdadeiro, desabilita a animação de ripple. | boolean | false |
| variant | variant | Define a variante do ez-split-button. | "primary" \| "secondary" \| "tertiary" | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| buttonClick | Emitido quando o botão principal é clicado | CustomEvent<void> |
| dropdownItemClick | Emitido quando um item do dropdown é clicado | CustomEvent<IDropdownItem> |
| dropdownSubActionClick | Emitido quando uma subAction de um item do dropdown é clicada | CustomEvent<IDropdownSubAction> |

### Methods

#### `isOpenedDropdown() => Promise<boolean>`

Informa se a lista de ações está aberta.

##### Returns

Type: `Promise<boolean>`

#### `setBlur() => Promise<void>`

Remove o foco de ambos os botões.

##### Returns

Type: `Promise<void>`

#### `setLeftButtonFocus() => Promise<void>`

Aplica o foco no botão principal.

##### Returns

Type: `Promise<void>`

#### `setRightButtonFocus() => Promise<void>`

Aplica o foco no botão do dropdown.

##### Returns

Type: `Promise<void>`

#### `toggleDropdown() => Promise<void>`

Abre ou Fecha o dropdown do Split Button.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-tooltip
  * ez-icon
  * ez-dropdown

### CSS Variables

| Variable | Description |
|---|---|
| --ez-split-button--min-width | Define a largura mínima do componente. |
| --ez-split-button--width | Define a largura do componente. |
| --ez-split-button--height | Define a altura do componente, quando size medium. |
| --ez-split-button__medium-icon--width | Define a largura do slot que contém o ícone. |
| --ez-split-button__large-icon--width | Define a largura do slot que contém o ícone. |
| --ez-split-button__label--padding-top | Define o espaçamento superior ao label. |
| --ez-split-button__label--padding-bottom | Define o espaçamento inferior ao label. |
| --ez-split-button__right-button--padding-left | Define o espaçamento esquerdo ao ícone. |
| --ez-split-button__right-button--padding-right | Define o espaçamento direito ao ícone. |
| --ez-split-button--color | Define a cor do label. |
| --ez-split-button__left-icon--color | Define a cor do ícone esquerdo. |
| --ez-split-button__right-icon--color | Define a cor do ícone direito. |
| --ez-split-button--background-color | Define a cor de fundo do botão. |
| --ez-split-button--border | Define o estilo da borda do botão. |
| --ez-split-button--font-size | Define o tamanho do label. |
| --ez-split-button--line-height | Define a altura da linha do label. |
| --ez-split-button--font-family | Define a família da fonte do label. |
| --ez-split-button--font-weight | Define o peso da fonte do label. |
| --ez-split-button--border-radius | Define o raio da borda do botão. |
| --ez-split-button--hover-color | Define a cor do texto e do ícone quando o cursor está sobre o botão. |
| --ez-split-button--hover--background-color | Define a cor de fundo quando o cursor está sobre o botão. |
| --ez-split-button--disabled-color | Define a cor do texto quando o botão está desabilitado. |
| --ez-split-button--disabled--background-color | Define a cor de fundo quando o botão está desabilitado. |
| --ez-split-button--focus--border | Define o estido da borda quando o botão está selecionado. |
| --ez-split-button--focus--box-shadow | Define a sombra do botão quando selecionado. |
