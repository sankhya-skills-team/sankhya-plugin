> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon/ (snapshot 2026-09-28)

# Icon

Os ícones são projetados para serem simples, modernos, amigáveis e, às vezes, peculiares. Cada ícone é reduzido à sua forma mínima, expressando características essenciais.

Veja a lista completa de ícones.

## Exemplos

demo.js

```jsx
import React from 'react';
import { EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <EzIcon iconName="chevron-left" className="ez-padding-right--small" />
            <EzIcon iconName="chevron-right" className="ez-padding-right--small" />
            <EzIcon iconName="sync" className="ez-padding-right--small" />
            <EzIcon iconName="edit" className="ez-padding-right--small" />
            <EzIcon iconName="copy" className="ez-padding-right--small" />
            <EzIcon iconName="delete" className="ez-padding-right--small" />
            <EzIcon iconName="plus" className="ez-padding-right--small" />
            <EzIcon iconName="save" className="ez-padding-right--small" />
            <EzIcon iconName="table" className="ez-padding-right--small" />
            <EzIcon iconName="list" className="ez-padding-right--small" />
            <EzIcon iconName="settings-inverted" />
        </div>
    )
};

export default Demo;
```

## Tamanhos

### 14px (Extra small)

demo.js

```jsx
import React from 'react';
import { EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <EzIcon size="x-small" iconName="chevron-left" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="chevron-right" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="sync" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="edit" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="copy" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="delete" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="plus" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="save" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="table" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="list" className="ez-padding-right--small" />
            <EzIcon size="x-small" iconName="settings-inverted" />
        </div>
    );
}

export default Demo;
```

### 16px (Small)

### 20px (Medium)

Nesse caso, como o tamanho "medium" é o padrão, basta omitir o atributo "size"

demo.js

```jsx
import React from 'react';
import { EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <EzIcon iconName="chevron-left" className="ez-padding-right--small" />
            <EzIcon iconName="chevron-right" className="ez-padding-right--small" />
            <EzIcon iconName="sync" className="ez-padding-right--small" />
            <EzIcon iconName="edit" className="ez-padding-right--small" />
            <EzIcon iconName="copy" className="ez-padding-right--small" />
            <EzIcon iconName="delete" className="ez-padding-right--small" />
            <EzIcon iconName="plus" className="ez-padding-right--small" />
            <EzIcon iconName="save" className="ez-padding-right--small" />
            <EzIcon iconName="table" className="ez-padding-right--small" />
            <EzIcon iconName="list" className="ez-padding-right--small" />
            <EzIcon iconName="settings-inverted" />
        </div>
    );
}

export default Demo;
```

### 24px (Large)

### 32px (Extra large)

demo.js

```jsx
import React from 'react';
import { EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <EzIcon size="x-large" iconName="chevron-left" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="chevron-right" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="sync" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="edit" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="copy" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="delete" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="plus" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="save" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="table" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="list" className="ez-padding-right--small" />
            <EzIcon size="x-large" iconName="settings-inverted" />
        </div>
    );
}

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| fontSize | font-size | Define o tamanho da fonte. | number \| string | undefined |
| href | href | Define o endereço da imagem quando não contempladas na biblioteca de ícones. | string | undefined |
| iconName | icon-name | Define o ícone a ser usado da biblioteca de ícones: ez-icons | string | undefined |
| size | size | Define o tamanho do ícone. | "large" \| "medium" \| "small" \| "x-large" \| "x-small" | "medium" |

### Dependencies

#### Used by

  * ez-actions-button
  * ez-alert
  * ez-avatar
  * ez-badge
  * ez-breadcrumb
  * ez-button
  * ez-chip
  * ez-classic-input
  * ez-classic-text-area
  * ez-collapsible-box
  * ez-combo-box
  * ez-dialog
  * ez-dropdown
  * ez-file-item
  * ez-filter-input
  * ez-grid
  * ez-grid-pagination
  * ez-image-input
  * ez-list-item
  * ez-modal-container
  * ez-multi-select-input
  * ez-multi-selection-list
  * ez-rich-toolbar-item
  * ez-scroller
  * ez-search
  * ez-search-plus
  * ez-sidebar-button
  * ez-simple-image-uploader
  * ez-split-button
  * ez-tabselector
  * ez-text-area
  * ez-text-input
  * ez-tile
  * ez-tile-medium
  * ez-time-input
  * ez-tree

### CSS Variables

| Variable | Description |
|---|---|
| --ez-icon--color | Define a cor do ícone. |
