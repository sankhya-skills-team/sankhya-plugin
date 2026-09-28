> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search/ (snapshot 2026-09-28)

# Search

O Search input permite ao usuário buscar um conteúdo por meio de uma palavra chave. A pesquisa oferece aos usuários uma maneira de explorar um conteúdo ou informação utilizando palavras chaves, podendo ser utilizada como o principal meio de descoberta de conteúdo ou como um filtro para ajudar o usuário a encontrar o conteúdo desejado.

demo.js

```jsx
import React from 'react';
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzSearch />
);

export default Demo;
```

## Variações e estados.

### Habilitado.

demo.js

```jsx
import React from 'react';
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzSearch
        label="Campo habilitado"
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
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <EzSearch
    label="Label do campo"
  />
);

export default Demo;
```

### Com estado de erro.

### Com lista de registros.

demo.js

```jsx
import React from 'react';
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const buildOptions = () => {
    return [
        { value: "AC", label: "Acre" },
        { value: "AL", label: "Alagoas" },
        { value: "AP", label: "Amapá" },
        { value: "AM", label: "Amazonas" },
        { value: "BA", label: "Bahia" },
        { value: "CE", label: "Ceará" },
        { value: "ES", label: "Espírito Santo" },
        { value: "GO", label: "Goiás" },
        { value: "MA", label: "Maranhão" },
        { value: "MT", label: "Mato Grosso" },
        { value: "MS", label: "Mato Grosso do Sul" },
        { value: "MG", label: "Minas Gerais" },
        { value: "PA", label: "Pará" },
        { value: "PB", label: "Paraíba" },
        { value: "PR", label: "Paraná" },
        { value: "PE", label: "Pernambuco" },
        { value: "PI", label: "Piauí" },
        { value: "RJ", label: "Rio de Janeiro" },
        { value: "RN", label: "Rio Grande do Norte" },
        { value: "RS", label: "Rio Grande do Sul" },
        { value: "RO", label: "Rondônia" },
        { value: "RR", label: "Roraima" },
        { value: "SC", label: "Santa Catarina" },
        { value: "SP", label: "São Paulo" },
        { value: "SE", label: "Sergipe" },
        { value: "TO", label: "Tocantins" },
        { value: "DF", label: "Distrito Federal" }
    ];
}

const Demo = () => (
    <EzSearch
        label="Título do campo"
        showOptionValue={true}
        optionLoader={buildOptions}
    />
);

export default Demo;
```

### Ocultar o value da seleção.

### Ocultar o value das opções.

demo.js

```jsx
import React from 'react';
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const buildOptions = () => {
    return [
        { value: "AC", label: "Acre" },
        { value: "AL", label: "Alagoas" },
        { value: "AP", label: "Amapá" },
        { value: "AM", label: "Amazonas" },
        { value: "BA", label: "Bahia" },
        { value: "CE", label: "Ceará" },
        { value: "ES", label: "Espírito Santo" },
        { value: "GO", label: "Goiás" },
        { value: "MA", label: "Maranhão" },
        { value: "MT", label: "Mato Grosso" },
        { value: "MS", label: "Mato Grosso do Sul" },
        { value: "MG", label: "Minas Gerais" },
        { value: "PA", label: "Pará" },
        { value: "PB", label: "Paraíba" },
        { value: "PR", label: "Paraná" },
        { value: "PE", label: "Pernambuco" },
        { value: "PI", label: "Piauí" },
        { value: "RJ", label: "Rio de Janeiro" },
        { value: "RN", label: "Rio Grande do Norte" },
        { value: "RS", label: "Rio Grande do Sul" },
        { value: "RO", label: "Rondônia" },
        { value: "RR", label: "Roraima" },
        { value: "SC", label: "Santa Catarina" },
        { value: "SP", label: "São Paulo" },
        { value: "SE", label: "Sergipe" },
        { value: "TO", label: "Tocantins" },
        { value: "DF", label: "Distrito Federal" }
    ];
}

const Demo = () => (
    <EzSearch
        label="Título do campo"
        optionLoader={buildOptions}
        showOptionValue={false}
    />
);

export default Demo;
```

### Remove a opção vazia.

### Modo regular.

demo.js

```jsx
import React from 'react';
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <EzSearch
        label="Campo no modo regular"
        mode="regular"
    />
);

export default Demo;
```

### Modo slim.

### Ocultar mensagem de erro no desfoque do componente.

demo.js

```jsx
import React, { useState } from 'react';
import { EzSearch, EzButton } from '@sankhyalabs/ezui/react/components';

const buildOptions = () => {

    return [
        { value: 'AC', label: 'Acre' },
        { value: 'AL', label: 'Alagoas' },
        { value: 'AP', label: 'Amapá' },
        { value: 'AM', label: 'Amazonas' },
        { value: 'BA', label: 'Bahia' },
        { value: 'CE', label: 'Ceará' },
        { value: 'ES', label: 'Espírito Santo' },
        { value: 'GO', label: 'Goiás' },
        { value: 'MA', label: 'Maranhão' },
        { value: 'MT', label: 'Mato Grosso' },
        { value: 'MS', label: 'Mato Grosso do Sul' },
        { value: 'MG', label: 'Minas Gerais' },
        { value: 'PA', label: 'Pará' },
        { value: 'PB', label: 'Paraíba' },
        { value: 'PR', label: 'Paraná' },
        { value: 'PE', label: 'Pernambuco' },
        { value: 'PI', label: 'Piauí' },
        { value: 'RJ', label: 'Rio de Janeiro' },
        { value: 'RN', label: 'Rio Grande do Norte' },
        { value: 'RS', label: 'Rio Grande do Sul' },
        { value: 'RO', label: 'Rondônia' },
        { value: 'RR', label: 'Roraima' },
        { value: 'SC', label: 'Santa Catarina' },
        { value: 'SP', label: 'São Paulo' },
        { value: 'SE', label: 'Sergipe' },
        { value: 'TO', label: 'Tocantins' },
        { value: 'DF', label: 'Distrito Federal' },
    ];

};

const Demo = () => {
    const [value, setValue] = useState(undefined);
    const [preserveError, setPreserveError] = useState(true);

    function onChange(evt) {
        setValue(evt?.detail);
    }

    const buttonLabel = preserveError ? 'Ocultar  mensagem no focus out' : 'Preservar mensagem no focus out';

    return (
        <div className='ez-flex ez-flex--column'>
            <EzSearch
                label="Título do campo"
                value={value}
                optionLoader={buildOptions}
                onEzChange={onChange}
                showOptionValue={false}
                errorMessage={!value ? 'Mensagem de erro' : undefined}
                hideErrorOnFocusOut={!preserveError}
            />
            <EzButton label={buttonLabel} onClick={() => setPreserveError((value) => !value)} />
        </div>

    );

};

export default Demo;
```

### Limpar pesquisa sempre visível.

## Exemplos de métodos.

### Aplica o foco no campo.

Focado: **Não**

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzSearch, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const element = useRef(null);
    const [isFocus, setIsFocus] = useState(false);

    const onFocus = () => {
        element.current.setFocus();
        setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <>
            <EzSearch
                ref={element}
                label="Título do campo"
                onBlur={() => setIsFocus(false)}
                onFocus={() => setIsFocus(true)}
            >
            </EzSearch>
            <label>
                Focado: <strong>{isFocus ? "Sim" : "Não"}</strong>
            </label>

            <EzButton
                label="Focar Campo"
                className="ez-margin-top--medium"
                onClick={onFocus}
            />
        </>
    );
}

export default Demo;
```

### Remove o foco do campo.

O foco será removido automaticamente após 2 segundos

### Retorna se o conteúdo é inválido.

Inválido: **Não**

demo.js

```jsx
import React, { useState } from 'react';
import { EzSearch } from '@sankhyalabs/ezui/react/components';

const buildOptions = () => {
    return [
        { value: "AC", label: "Acre" },
        { value: "AL", label: "Alagoas" },
        { value: "AP", label: "Amapá" },
        { value: "AM", label: "Amazonas" },
        { value: "BA", label: "Bahia" },
        { value: "CE", label: "Ceará" },
        { value: "ES", label: "Espírito Santo" },
        { value: "GO", label: "Goiás" },
        { value: "MA", label: "Maranhão" },
        { value: "MT", label: "Mato Grosso" },
        { value: "MS", label: "Mato Grosso do Sul" },
        { value: "MG", label: "Minas Gerais" },
        { value: "PA", label: "Pará" },
        { value: "PB", label: "Paraíba" },
        { value: "PR", label: "Paraná" },
        { value: "PE", label: "Pernambuco" },
        { value: "PI", label: "Piauí" },
        { value: "RJ", label: "Rio de Janeiro" },
        { value: "RN", label: "Rio Grande do Norte" },
        { value: "RS", label: "Rio Grande do Sul" },
        { value: "RO", label: "Rondônia" },
        { value: "RR", label: "Roraima" },
        { value: "SC", label: "Santa Catarina" },
        { value: "SP", label: "São Paulo" },
        { value: "SE", label: "Sergipe" },
        { value: "TO", label: "Tocantins" },
        { value: "DF", label: "Distrito Federal" }
    ];
}

const Demo = () => {
    const [isInvalid, setIsInvalid] = useState(false);

    const validate = element => {
        if(element.value.value == "1"){
            element.errorMessage = "inválido";
        }
        element.isInvalid().then(value => {
            setIsInvalid(value);
        });
    };

    return (
        <>
            <EzSearch onBlur={evt => validate(evt.target)} optionLoader={buildOptions} />

            <label>
                Inválido: <strong>{isInvalid ? "Sim" : "Não"}</strong>
            </label>
        </>
    );
}

export default Demo;
```

## Exemplos de eventos.

### Ao mudar o estado do componente.

**Valor Alterado:**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alternativePlaceholder | alternative-placeholder | Texto alternativo a ser apresentado como título do campo. | string | undefined |
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| contextProperties | context-properties | Propriedades de contexto da aplicação. | any | undefined |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| ensureClearButtonVisible | ensure-clear-button-visible | Garante que o botão de limpar pesquisa está sempre visível | boolean | false |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| hideDescriptionInput | hide-description-input | Se true o campo de descrição não será exibido. | boolean | false |
| hideErrorOnFocusOut | hide-error-on-focus-out | Quando verdadeiro deixa de exibir a mensagem de erro (se existente) quando focar em um elemento diferente. | boolean | true |
| ignoreLimitCharsToSearch | ignore-limit-chars-to-search | Define se deve ignorar o limite de caracteres mínimo para realizar uma pesquisa | boolean | false |
| isTextSearch | is-text-search | Informa se a pesquisa é do tipo texto. | boolean | false |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| listOptionsPosition | -- | Define um posicionamento fixo para a lista de opções do CheckBox. | IEzCheckBoxListPosition | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| optionLoader | -- | Carrega as opções dinamicamente. | (argument: ISearchArgument, ctxProperties?: any) => IOption \| IOption[] \| Promise<IOption[]> | undefined |
| options | -- | Array com as opções do ez-combo-box. Os elementos devem obedecer o formato: {value: string, label: string} . | IOption[] | undefined |
| showMore | show-more | Informa se deve exibir a opção de mostrar mais resultados. | boolean | undefined |
| showOptionValue | show-option-value | Se false cada opção na lista deve exibir somente o label . | boolean | true |
| showSelectedValue | show-selected-value | Se false a opção selecionada deve exibir somente o label . | boolean | true |
| stopPropagateEnterKeyEvent | stop-propagate-enter-key-event | Se true, ineterrompe a propagação do evento de KeyDown da tecla enter | boolean | false |
| suppressEmptyOption | suppress-empty-option | Se true remove a opção vazia da lista. | boolean | false |
| suppressInputPersist | suppress-input-persist | Informa se o valor da opção selecionada deve persistir no input de texto. | boolean | false |
| suppressPreLoad | suppress-pre-load | Se true, desabilita pré-load das opções ao carregar componente | boolean | true |
| suppressSearch | suppress-search | Se true desabilita a digitação dentro do componente. | boolean | false |
| value | value | Define o valor do campo. | IOption \| string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<IOption> |
| ezEmptySearch | Emitido quando a pesquisa retorna um resultado vazio. | CustomEvent<string> |

### Methods

#### `clearValue() => Promise<void>`

Limpa o valor do campo de pesquisa

##### Returns

Type: `Promise<void>`

#### `getValueAsync() => Promise<unknown>`

##### Returns

Type: `Promise<unknown>`

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

### Dependencies

#### Used by

  * ez-form
  * ez-form-view
  * ez-grid
  * ez-multi-selection-list

#### Depends on

  * ez-button
  * ez-text-input
  * ez-icon
  * ez-popover-plus
  * search-list

### CSS Variables

| Variable | Description |
|---|---|
| --ez-search--height | Define altura do input. |
| --ez-search--width | Define largura do input. |
| --ez-search--min-width | Define largura mínima do input. |
| --ez-search__icon--width | Define largura do slot do ícone do input. |
| --ez-search--border-radius | Define o raio da borda do input. |
| --ez-search--border-radius-small | Define o raio da borda do input quando pequeno. |
| --ez-search--font-size | Define o tamanho da fonte dentro do input. |
| --ez-search--font-family | Define a família da fonte dentro do input. |
| --ez-search--font-weight--large | Define o peso da fonte dentro do input quando pesada. |
| --ez-search--font-weight--medium | Define o peso da fonte dentro do input quando média. |
| --ez-search--background-color--xlight | Define a cor de fundo da lista de opções. |
| --ez-search--background-medium | Define a cor de fundo dos itens da lista de opções. |
| --ez-search--line-height | Define a altura da linha do texto dentro do input. |
| --ez-search__input--background-color | Define a cor de fundo do input. |
| --ez-search__input--border | Define o estilo da borda do input. |
| --ez-search__input--border-color | Define a cor da borda do input. |
| --ez-search__input--focus--border-color | Define a cor da borda do input quando focado. |
| --ez-search__input--disabled--background-color | Define a cor de fundo do input quando desabilitado. |
| --ez-search__input--disabled--color | Define a cor do texto dentro do input quando desabilitado. |
| --ez-search__input--error--border-color | Define a cor da borda do input quando com erro. |
| --ez-search__btn--color | Define a cor do botão de pesquisa do componente. |
| --ez-search__btn-disabled--color | Define a cor do botão de pesquisa do componente quando desabilitado. |
| --ez-search__btn-hover--color | Define a cor do botão de pesquisa do componente quando o mouse está sobre ele. |
| --ez-search__label--color | Define a cor do label. |
| --ez-search--space--medium | Define um espaçamento mediano entre elementos do componente. |
| --ez-search--space--small | Define um espaçamento pequeno entre elementos do componente. |
