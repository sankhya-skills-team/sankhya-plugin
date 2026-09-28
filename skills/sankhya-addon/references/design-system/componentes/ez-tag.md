> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tag/ (snapshot 2026-09-28)

# Tag

O Tag é um componente de etiqueta utilizado para identificação rápida de um status ou classificação.

demo.js

```jsx
import React from 'react';
import { EzTag } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    return (
        <div class="ez-flex ez-flex--justify-evenly">
            <EzTag
                label="Sankhya"
            />
            <EzTag
                label="Gestão"
                color="light-red"
            />
            <EzTag
                label="Vendas"
                color="yellow"
            />
        </div>
    )
};

export default Demo;
```

## Variações

### Cores

O Tag possui 12 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio da propriedade `color`.

demo.js

```jsx
import { EzTag } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <>
        <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
            <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ width:"50%", gap: '1rem', padding: '1rem'}}>
                <EzTag
                    label="Default: ocean-green"
                />
                <EzTag
                    label="light-ocean-green"
                    color="light-ocean-green"
                />
                <EzTag
                    label="green"
                    color="green"
                />
                <EzTag
                    label="light-green"
                    color="light-green"
                />
                <EzTag
                    label="yellow"
                    color="yellow"
                />
                <EzTag
                    label="light-yellow"
                    color="light-yellow"
                />
            </div>
            <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ width:"50%", gap: '1rem', padding: '1rem'}}>
                <EzTag
                    label="red"
                    color="red"
                />
                <EzTag
                    label="light-red"
                    color="light-red"
                />
                <EzTag
                    label="gray"
                    color="gray"
                />
                <EzTag
                    label="light-gray"
                    color="light-gray"
                />
                <EzTag
                    label="petroleum"
                    color="petroleum"
                />
                <EzTag
                    label="light-petroleum"
                    color="light-petroleum"
                />
            </div>
        </div>
    </>
  );
};

export default Demo;
```

Além disso qualquer token de cor disponível na paleta de cores do Design System está disponível para ser utilizada através das propriedades `customBackgroundColor` e `customLabelColor`

Veja a paleta de cores...

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| color | color | Define a cor de fundo do componente. | "gray" \| "green" \| "light-gray" \| "light-green" \| "light-ocean-green" \| "light-petroleum" \| "light-red" \| "light-yellow" \| "ocean-green" \| "petroleum" \| "red" \| "yellow" | "ocean-green" |
| customBackgroundColor | custom-background-color | Define uma cor de fundo customizada, dentro da paleta de cores do Design System para o componente. | string | undefined |
| customLabelColor | custom-label-color | Define uma cor de texto customizada, dentro da paleta de cores do Design System para o componente. | string | undefined |
| label | label | Define o conteúdo textual ou numérico do componente. | string | undefined |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-tag--padding-x | Define o padding horizontal do componentes. |
| --ez-tag--padding-y | Define o padding vertical do componente. |
| --ez-tag--min-width | Define a largura minima do componente. |
| --ez-tag--min-height | Define a largura minima do componente. |
| --ez-tag--border-radius | Define o raio da borda do componente. |
| --ez-tag--background-color | Define a cor de fundo. |
| --ez-tag_label--font-weight | Define o peso da fonte do label. |
| --ez-tag_label--font-size | Define o tamanho da fonte do label. |
| --ez-tag_label--color | Define a cor da fonte do label. |
