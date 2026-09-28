> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-file-item/ (snapshot 2026-09-28)

# File item

Componente que representa um arquivo. É possível representar o progresso de upload, expressar a necessidade de download ou remoção. Também fornece informações como tamanho, tipo e nome do arquivo.

demo.js

```jsx
import React from "react";
import { EzFileItem } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
    return (
        <EzFileItem fileName="Arquivo de teste.txt"/>
    );
};

export default Demo;
```

## Características

### Tamanho do arquivo

demo.js

```jsx
import React from "react";
import { EzFileItem } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
    return (
        <EzFileItem fileName="Arquivo de teste.txt" fileSize={654651}/>
    );
};

export default Demo;
```

### Progresso

### Sem remoção

demo.js

```jsx
import React from "react";
import { EzFileItem } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
    return (
        <EzFileItem fileName="Arquivo de teste.txt" canRemove={false}/>
    );
};

export default Demo;
```

### Ícones por extensão

### Ícone personalizado

demo.js

```jsx
import React from "react";
import { EzFileItem } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
    return (
        <EzFileItem fileName="Arquivo de teste.txt" iconName="extrato"/>
    );
};

export default Demo;
```

### Exemplos de eventos

Clique no componente ou no botão de remover.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| canRemove | can-remove | Define se o usuário pode remover o arquivo que está sendo apresentado. | boolean | true |
| fileName | file-name | Define o nome do arquivo, com extensão. | string | undefined |
| fileSize | file-size | Tamanho do arquivo (em bytes). | number | undefined |
| iconName | icon-name | Define qual ícone que representa o arquivo. | string | undefined |
| progress | progress | Percentual de carregamento do arquivo para o servidor. | number | 100 |

### Events

| Event | Description | Type |
|---|---|---|
| ezClick | Emitido ao clicar no ez-file-input (exceto no botão de remover). | CustomEvent<string> |
| ezRemove | Emitido ao clicar no botão de remover. | CustomEvent<string> |

### Dependencies

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-file-item--height | Define a altura do componente. |
| --ez-file-item--padding | Define espaçamento interno do componente. |
| --ez-file-item--border-radius | Define o arredondamento dos retangulos. |
| --ez-file-item--border-color | Define a cor da borda. |
| --ez-file-item--border-style | Define largura e estilo da borda. |
| --ez-file-item--font-family | Define a família da fonte. |
| --ez-file-item--font-size | Define o tamanho da fonte. |
| --ez-file-item--font-weight | Define o peso da fonte. |
| --ez-file-item--color | Define a cor da fonte. |
| --ez-file-item__file-size--font-weight | Define o peso da fonte do tamanho do arquivo. |
| --ez-file-item__file-size--color | Define o peso da fonte do tamanho do arquivo. |
| --ez-file-item--icon-color | Define a cor do ícone. |
