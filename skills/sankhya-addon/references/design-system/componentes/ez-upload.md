> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-upload/ (snapshot 2026-09-28)

# Upload

O componente de upload é utilizado para selecionar arquivos, imagens, vídeo e etc do diretório do usuário, de acordo com o que a tela permitir.

demo.js

```jsx
import React from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const Demo = () => (<EzUpload />);

export default Demo;
```

### Habilitado.

demo.js

```jsx
import React from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzUpload
    enabled={true}
  />
);

export default Demo;
```

### Desabilitado.

### Label.

demo.js

```jsx
import React from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzUpload label="Label do campo" />
);

export default Demo;
```

### Subtitle.

### Tamanho limite do arquivo.

demo.js

```jsx
import React from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const urlUpload = "http://localhost";

const Demo = () => (
  <EzUpload
    maxFileSize={1000}
    urlUpload={urlUpload}
  />
);

export default Demo;
```

### Quantidade limite de arquivos.

### Cabeçalhos da requisição.

demo.js

```jsx
import React from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const urlUpload = "http://localhost";

const Demo = () => (
  <EzUpload
    requestHeaders={{"Header-Name": "headerValue"}}
    urlUpload={urlUpload}
  />
);

export default Demo;
```

### URL de upload.

### URL para remover arquivo.

demo.js

```jsx
import React from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const urlDelete = "http://localhost";

const Demo = () => (
  <EzUpload urlDelete={urlDelete} />
);

export default Demo;
```

## Exemplos de métodos.

### Adiciona o foco.

Focado: **Não**

### Remove o foco.

O foco será removido automaticamente após 2 segundos

demo.js

```jsx
import React, { useRef } from 'react';
import { EzUpload} from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);

    const removeFocus = () => {
        setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <>
            <EzUpload
                ref={element}
                label="Título do campo"
                onFocus={removeFocus}
            >
            </EzUpload>

            <label>O foco será removido automaticamente após 2 segundos</label>
        </>
    );
}

export default Demo;
```

### Adiciona arquivos para upload.

## Exemplos de eventos.

### Ao mudar o estado do componente.

**Valor Alterado:**

demo.js

```jsx
import React, { useState } from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const urlUpload = "http://localhost";

const Demo = () => {
    const [value, setValue] = useState(null);

    const onChange = (evt) => {
        setValue(evt.detail);
    };

    return (
        <>
            <EzUpload
                label="Título do campo"
                onEzChange={onChange}
                urlUpload={urlUpload}
            />
            <label>
                <b>Valor Alterado: </b> {value?.toString()}
            </label>
        </>
    );
}

export default Demo;
```

### Ao iniciar a alteração.

Aguardando Alteração: **Não**

### Ao interromper uma alteração.

Alteração Cancelada: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzUpload } from '@sankhyalabs/ezui/react/components';

const urlUpload = "http://localhost";

const Demo = () => {
    const [isCanceled, setIsCanceled] = useState(false);

    const onCancelWaitingChange = (evt) => {
        setIsCanceled(evt && evt.detail === null);
    };

    return (
        <>
            <EzUpload
                urlUpload={urlUpload}
                onInput={onCancelWaitingChange}
                onEzCancelWaitingChange={onCancelWaitingChange}
            />
            <label>
                Alteração Cancelada: <strong>{isCanceled ? "Sim" : "Não"}</strong>
            </label>
        </>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| maxFileSize | max-file-size | Define o tamanho máximo (em bytes) de cada arquivo que pode ser transferido | number | undefined |
| maxFiles | max-files | Define um limite para a quantidade de arquivos | number | undefined |
| requestHeaders | request-headers | Headers para a requisição Http | any | undefined |
| subtitle | subtitle | Define o subtítulo utilizado no campo de upload | string | undefined |
| urlDelete | url-delete | Define a URL de deleção | string | undefined |
| urlUpload | url-upload | Define a URL de upload | string | undefined |
| value | -- | Define o valor do campo. | EzFile[] | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezCancelWaitingChange | Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. | CustomEvent<void> |
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<EzFile[]> |
| ezStartChange | Emitido ao iniciar a alteração (remover ou adicionar um arquivo). | CustomEvent<WaitingChange> |

### Methods

#### `addFiles(files: Array<File>) => Promise<void>`

Adiciona arquivos.

##### Returns

Type: `Promise<void>`

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus() => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form-view

### CSS Variables

| Variable | Description |
|---|---|
| --ez-upload--height | Define a altura do componente. |
| --ez-upload--width | Define a largura do componente. |
| --ez-upload__icon--width | Define a largura do slot que contém o ícone. |
| --ez-upload__container--background-color | Define a cor de fundo do container. |
| --ez-upload__color--primary | Define a cor de fundo do container. |
| --ez-upload--padding--extra-small | Define os espaçamentos extra pequenos no componente. |
| --ez-upload--padding--small | Define os espaçamentos pequenos no componente. |
| --ez-upload--padding--medium | Define os espaçamentos médios no componente. |
| --ez-upload--padding--large | Define os espaçamentos grandes no componente. |
| --ez-upload__border--color | Define a cor das bordas no componente. |
| --ez-upload--text-shadow | Define as sombras dos textos do componente. |
| --ez-upload--text--primary | Define a cor dos textos do componente. |
| --ez-upload--font-size | Define o tamanho dos textos do componente. |
| --ez-upload--font-family | Define a família dos textos do componente. |
| --ez-upload--font-weight | Define o peso dos textos do componente. |
| --ez-upload__btn__cancel-image | Contém o ícone de cancelamento. |
| --ez-upload__file-icon-image | Contém o ícone de arquivo. |
