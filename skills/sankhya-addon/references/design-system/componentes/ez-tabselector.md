> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tabselector/ (snapshot 2026-09-28)

# Tabselector

Selecionador de abas.

demo.js

```jsx
import React from 'react';
import { EzTabselector } from '@sankhyalabs/ezui/react/components';

const buildIdTabSelector = () => {
    return [
        "Geral",
        "Opções",
        "Configurações",
        "Cadastro",
        "Títulos",
        "Processos",
        "Artigos",
        "Administração",
        "Blog",
        "Fale Conosco",
        "Sobre",
        "Galeria",
        "Informações"
    ].join(",");
}

const Demo = () => (
    <EzTabselector tabs={buildIdTabSelector()} />
);

export default Demo;
```

## Variações e estados.

### Define o index da aba selecionada.

demo.js

```jsx
import React from 'react';
import { EzTabselector } from '@sankhyalabs/ezui/react/components';

const buildIdTabSelector = () => {
    return [
        "Geral",
        "Opções",
        "Configurações",
        "Cadastro",
        "Títulos",
        "Processos",
        "Artigos",
        "Administração",
        "Blog",
        "Fale Conosco",
        "Sobre",
        "Galeria",
        "Informações"
    ].join(",");
}

const Demo = () => (
    <EzTabselector tabs={buildIdTabSelector()} selectedIndex={2} />
);

export default Demo;
```

### Define a aba selecionada.

### Define as abas do componente.

Abas separadas por vírgula ",".

demo.js

```jsx
import React from 'react';
import { EzTabselector } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzTabselector tabs="Primeira aba, Segunda aba"  />
);

export default Demo;
```

## Exemplos de eventos.

### Ao mudar o estado do componente.

**Valor Alterado:**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| reorderable | reorderable | Define se as abas podem ser reordenadas via drag-and-drop. Desabilitado por padrão. | boolean | false |
| selectedIndex | selected-index | Define o index da aba selecionada. | number | undefined |
| selectedTab | selected-tab | Define a aba selecionada. | string | undefined |
| tabs | tabs | Define o nome das abas do componente. Podendo serem separadas por vírgula "," ou em um Array de configuração. | Tab[] \| string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do componente. | CustomEvent<Tab> |
| ezReorder | Emitido quando as abas são reordenadas via drag-and-drop. Recebe o array de abas na nova ordem. | CustomEvent<Tab[]> |

### Methods

#### `goToTab(tabIndex: number, silent?: boolean) => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --tabselector--backward-icon | Contém o ícone de voltar para a aba anterior. |
| --tabselector--forward-icon | Contém o ícone de avançar para a aba posterior. |
