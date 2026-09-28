> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter-input/ (snapshot 2026-09-28)

# FilterInput

Documentação do componente EzFilterInput.

demo.js

```jsx
import React from 'react';
import { EzFilterInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzFilterInput label="Informe texto para filtrar..."></EzFilterInput>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Inverted

Em backgrounds escuros os inputs devem mudar de aparência para o modo `inverted` melhorando o contraste.

demo.js

```jsx
import React from 'react';
import { EzFilterInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzFilterInput
                label="Informe texto para filtrar..."
                className="ez-input--inverted">
            </EzFilterInput>
        </div>
    )
};

export default Demo;
```

### Habilitado

Campo disponível para uso.

### Desabilitado

Campo indisponível para uso.

demo.js

```jsx
import React from 'react';
import { EzFilterInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzFilterInput
                label="Informe texto para filtrar..."
                enabled="false">
            </EzFilterInput>
        </div>
    )
};

export default Demo;
```

### Com estado de erro

Quando há um problema de validação, serve como orientação ao usuário.

### Com restrict

Restringe o que o usuário pode digitar. Cada caractere digitado será testado e deve estar contido nessa string ou será descartado.

demo.js

```jsx
import React from 'react';
import { EzFilterInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzFilterInput
                label="Informe apenas vogais..."
                restrict="aeiou">
            </EzFilterInput>
        </div>
    )
};

export default Demo;
```

### Modo slim

Modo reduzido do tamanho do campo.

### Modo regular (default)

Modo padrão do tamanho do campo.

demo.js

```jsx
import React from 'react';
import { EzFilterInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-col--sd-4">
            <EzFilterInput
                label="Informe texto para filtrar..."
                mode="regular">
            </EzFilterInput>
        </div>
    )
};

export default Demo;
```

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática temos os métodos `setFocus()` e `setBlur()`.

O exemplo abaixo demonstra isso através do botão **Focar Campo**. Clicando nesse botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

Focado: **Não**

#### isInvalid()

Retorna informando se o campo está inválido (true | false).

Inválido: **Não**

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzFilterInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [isInvalid, setIsInvalid] = useState(false);
    const [errorMessage, setErrorMessage] = useState(null);

    const onBlur = async () => {
        // Em alguns navegadores é necessário esperar setar a mensagem
        // antes de validar se o campo está válido.
        await setErrorMessage(null);

        element.current.value = element.current.value?.trim() || "";

        if (element.current.value.length > 0 && element.current.value.length < 3) {
            // Em alguns navegadores é necessário esperar setar a mensagem
            // antes de validar se o campo está válido.
            await setErrorMessage("Informe 3 caracteres ou mais.");
        }

        element.current.isInvalid().then(setIsInvalid);
    };

    return (
        <div>
            <div className="ez-col--sd-4">
                <EzFilterInput
                    ref={element}
                    label="Informe texto para filtrar..."
                    onBlur={onBlur}
                    errorMessage={errorMessage}>
                </EzFilterInput>
            </div>

            <div className="ez-flex ez-flex--column ez-flex--align-items-center">
                <label>
                    Inválido: <strong>{isInvalid ? "Sim" : "Não"}</strong>
                </label>
            </div>
        </div>
    )
};

export default Demo;
```

#### setValue()

Método responsável por setar um novo valor ao campo.

Importante

O método **endSearch** funcionará apenas quando a propriedade asyncSearch estiver ativada.

#### endSearch()

Método responsável por resetar o valor do campo para o ultimo valor inputado.

Importante

O método **endSearch** funcionará apenas quando a propriedade asyncSearch estiver ativada.

Valor Guardado: ****

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzFilterInput, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezFilterInputRef = useRef(null);
    const [searchingValue, setSearchingValue] = useState("");
    const [savedValue, setSavedValue] = useState("");

    const handleSaveFilter = async () => {
        await ezFilterInputRef.current.setValue(searchingValue);
        setSavedValue(searchingValue);
    };

    const handleSearching = evt => {
        setSearchingValue(evt.detail);
    }

    const handleEndSearch = () => {
        if (ezFilterInputRef.current) {
            ezFilterInputRef.current.endSearch();
        }
    };

    return (
        <div>
            <div className="ez-col--sd-4 ez-margin-bottom--medium">
                <EzFilterInput
                    ref={ezFilterInputRef}
                    asyncSearch={true}
                    label="Informe texto para filtrar..."
                    onEzSearching={handleSearching}>
                </EzFilterInput>

                <div className="ez-flex">
                    <EzButton
                        className="ez-margin-right--medium"
                        label="Guardar Filtro"
                        onClick={handleSaveFilter}>
                    </EzButton>

                    <EzButton
                        label="Encerrar Busca"
                        onClick={handleEndSearch}>
                    </EzButton>
                </div>
            </div>

            <div>
                <label>Valor Guardado: <strong>{savedValue}</strong></label>
            </div>
        </div>
    )
};

export default Demo;
```

### Exemplos de eventos

#### ezChange()

Evento disparado quando o estado do componente é alterado (onEzChange).

Valor: ****

#### ezSearching()

O evento ezSearching é acionado exclusivamente no modo assíncrono, quando uma pesquisa está sendo realizada.

Importante

O método **endSearch** funcionará apenas quando a propriedade asyncSearch estiver ativada. É importante ressaltar que, quando a propriedade **asyncSearch** estiver ativada, o value não será mais atualizado.

Retorno do evento EzSearching: ****

demo.js

```jsx
import React, { useState } from 'react';
import { EzFilterInput, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [isCheck, setIsCheck] = useState(false);
    const [value, setValue] = useState("");

    const handleSearching = evt => {
        setValue(evt.detail);
    }

    const handleClick = () => {
        setIsCheck(!isCheck);
    };

    return (
        <div>
            <div className="ez-col--sd-4 ez-margin-bottom--medium">
                <EzFilterInput
                    label="Informe o texto para filtrar..."
                    asyncSearch={isCheck}
                    onEzSearching={handleSearching}
                >
                </EzFilterInput>

                <EzButton
                    label={isCheck ? 'Desativar asyncSearch' : 'Ativar asyncSearch'}
                    onClick={handleClick}>
                </EzButton>
            </div>

            <div>
                <label>
                    Retorno do evento EzSearching: <strong>{isCheck ? value : ""}</strong>
                </label>
            </div>
        </div>
    )
};

export default Demo;
```

#### ezFocusin()

Evento disparado quando acontece o foco no componente (ezFocusin).

Focado: **Não**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| asyncSearch | async-search | Define se o campo irá funcionar de forma assíncrona. | boolean | false |
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| restrict | restrict | Restringe o que o usuário pode digitar. | string | undefined |
| value | value | Define o valor do campo. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<string> |
| ezFocusIn | Emitido quando acontece o foco no campo. | CustomEvent<void> |
| ezSearching | Emitido quando está sendo realizada uma pesquisa no modo asyncSearch. | CustomEvent<string> |

### Methods

#### `endSearch() => Promise<void>`

Método responsável por resetar o valor do campo para o ultimo valor inputado.

##### Returns

Type: `Promise<void>`

#### `isInvalid() => Promise<boolean>`

Retorna se o conteúdo é inválido.

##### Returns

Type: `Promise<boolean>`

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus(options?: TFocusOptions) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

#### `setValue(newValue: string) => Promise<void>`

Método responsável por setar um novo valor ao campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-guide-navigator
  * ez-multi-selection-list
  * ez-sortable-list

#### Depends on

  * ez-text-input
  * ez-icon
