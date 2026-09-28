> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus/ (snapshot 2026-09-28)

# Search Plus

O Search input permite ao usuário buscar um conteúdo por meio de uma palavra chave. A pesquisa oferece aos usuários uma maneira de explorar um conteúdo ou informação utilizando palavras chaves, podendo ser utilizada como o principal meio de descoberta de conteúdo ou como um filtro para ajudar o usuário a encontrar o conteúdo desejado.

demo.js

```jsx
import React from 'react';
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    <div className="ez-row">
        <div className="ez-col ez-col--sd-4 ez-padding-horizontal--medium">
            <EzSearchPlus optionLoader={() => {}} />
        </div>
        <div className="ez-col ez-col--sd-4 ez-padding-horizontal--medium">
            <EzSearchPlus optionLoader={() => {}} />
        </div>
        <div className="ez-col ez-col--sd-4 ez-padding-horizontal--medium">
            <EzSearchPlus optionLoader={() => {}} />
        </div>
    </div>
);

export default Demo;
```

## Propriedades

### value

A propriedade `value` define o valor atual do campo de busca. Pode ser uma string simples ou um objeto que contém value e label. Quando é passado apenas o código, a label será buscada a partir do `optionLoader`.

  * Tipo: `string | IOption`.
  * Valor inicial: `undefined`.

demo.js

```jsx
import React from 'react';
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => (
    <div className="ez-row">
        <div className="ez-col ez-col--sd-4 ez-padding-horizontal--medium">
            <EzSearchPlus
                optionLoader={optionLoaderUF}
                value={{ value: "MG", label: "Minas Gerais" }}
            />
        </div>
        <div className="ez-col ez-col--sd-4 ez-padding-horizontal--medium">
            <EzSearchPlus
                optionLoader={optionLoaderUF}
                value="SP"
            />
        </div>
        <div className="ez-col ez-col--sd-4 ez-padding-horizontal--medium">
            <EzSearchPlus
                optionLoader={optionLoaderUF}
                value={'{"value": "BA", "label": "Bahia"}'}
            />
        </div>
    </div>
);

export default Demo;
```

### enabled

A propriedade `enabled` controla se o campo de busca está habilitado ou não. Quando habilitado, o usuário pode interagir com o campo de busca. Caso contrário, o campo estará desabilitado e não permitirá interações.

  * Tipo: `boolean`.
  * Valor inicial: `true`.

### disableCodeInput

A propriedade `disableCodeInput` desabilita a entrada de código no campo de busca. Quando habilitado, o usuário não poderá digitar ou selecionar um código.

  * Tipo: `boolean`.
  * Valor inicial: `false`.

demo.js

```jsx
import React, { useState } from 'react';
import { EzButton, EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => {
    const [disableCodeInput, setDisableCodeInput] = useState(true);

    function toggleEnable() {
        setDisableCodeInput((prev) => !prev);
    }

    return (
        <div className='ez-flex ez-flex--column ez-flex--justify-start'>
            <EzButton
                label={!disableCodeInput ? "Desabilitar" : "Habilitar"}
                onClick={() => toggleEnable()}
                className="ez-margin-vertical--medium"
            />
            <div className='ez-row'>
                <EzSearchPlus
                    label={!disableCodeInput ? "Código habilitado" : "Código desabilitado"}
                    disableCodeInput={disableCodeInput}
                    className="ez-col ez-col--sd-4"
                    optionLoader={optionLoaderUF}
                />
            </div>
        </div>
    );
};

export default Demo;
```

### disableDescriptionInput

A propriedade `disableDescriptionInput` desabilita a entrada de descrição no campo de busca. Quando habilitado, o usuário não poderá digitar ou selecionar uma descrição.

  * Tipo: `boolean`.
  * Valor inicial: `false`.

### label

A propriedade `label` define o rótulo exibido acima do campo de busca. Este rótulo ajuda a identificar o propósito do campo para o usuário.

  * Tipo: `string`.
  * Valor inicial: `""` (string vazia).

demo.js

```jsx
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import React from 'react';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => (
  <div className='ez-row'>
    <EzSearchPlus
      label="Estado"
      optionLoader={optionLoaderUF}
      className="ez-col ez-col--sd-4"
    />
  </div>
);

export default Demo;
```

### codeLabel

A propriedade `codeLabel` define o rótulo exibido no código no campo de busca. Este rótulo ajuda a identificar o código exibido para o usuário.

  * Tipo: `string`.
  * Valor inicial: `"Cód."`.

### errorMessage

A propriedade `errorMessage` define a mensagem de erro exibida no ícone a direita do campo de busca. Esta mensagem é exibida quando o campo de busca está em um estado de erro.

  * Tipo: `string`.
  * Valor inicial: `""` (string vazia).

demo.js

```jsx
import React, { useState } from 'react';
import { EzButton, EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => {
  const [errorMessage, setErrorMessage] = useState("Mensagem de erro");

  function toggleErrorMessage() {
    setErrorMessage((prev) => !prev ? "Mensagem de erro" : "");
  }

  return (
    <div className='ez-flex ez-flex--column ez-flex--justify-start'>
      <EzButton
        label={!errorMessage ? "Adicionar erro" : "Remover error"}
        onClick={() => toggleErrorMessage()}
        className="ez-margin-vertical--medium"
      />
      <div className='ez-row'>
        <EzSearchPlus
          label="Campo com mensagem de erro"
          errorMessage={errorMessage}
          optionLoader={optionLoaderUF}
          className="ez-col ez-col--sd-4"
        />
      </div>
    </div>
  )
};

export default Demo;
```

### canShowError

A propriedade `canShowError` controla se a mensagem de erro deve ser exibida. Quando habilitado, a mensagem de erro será exibida no ícone a direita do componente.

  * Tipo: `boolean`.
  * Valor inicial: `true`.

### optionLoader

A propriedade `optionLoader` define a função responsável por carregar as opções disponíveis no campo de busca. Esta função pode ser utilizada para carregar opções dinamicamente com base em uma entrada do usuário.

  * Tipo: `OptionLoaderFunction`.
  * Valor inicial: `undefined`.

#### Tipos relacionados:

  * `ISearchArgument`: Interface que define os argumentos passados para a função `optionLoader`.

```typescript
export interface ISearchArgument {
  mode: SearchMode;
  argument: string;
}
```

    * `mode`: Define o modo de busca (por exemplo, busca por código ou por descrição).
    * `argument`: O argumento de busca fornecido pelo usuário.
  * `OptionLoaderFunction`: Tipo da função `optionLoader`.

```typescript
export type OptionLoaderFunction = (
  argument: ISearchArgument,
  ctxProperties?: any
) =>
  Promise<Array<IOption | ISearchOption> | IOption | ISearchOption> |
  Array<ISearchOption | IOption> |
  IOption |
  ISearchOption;
```

    * A função recebe um argumento do tipo `ISearchArgument` e um objeto opcional `ctxProperties`.
    * Retorna uma promessa que resolve para um array de opções (`IOption` ou `ISearchOption`), uma única opção (`IOption` ou `ISearchOption`), ou diretamente um array de opções ou uma única opção.

Atenção

Quando é feita uma busca pelo campo código, o componente irá selecionar o primeiro item retornado pela função `optionLoader`.

demo.js

```jsx
import React from 'react';
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { delay } from '../utils/optionLoader';

async function buildOptions({ argument, mode }) {
    //Para fins demonstrativos de tempo de carregamento.
    await delay();

    const options = [
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

    if (mode === "LOAD_DESCRIPTION") {
        return options.find((option) => option.value === argument);
    }

    if(!argument) {
        return options;
    }

    return options.filter((option) => option.label.toUpperCase().includes(argument.toUpperCase()));
}

const Demo = () => (
    <div className='ez-row'>
        <EzSearchPlus
            label="Título do campo"
            optionLoader={buildOptions}
            className="ez-col ez-col--sd-4"
        />
    </div>
);

export default Demo;
```

### showOptionValue

A propriedade `showOptionValue` controla se o valor das opções deve ser exibido junto com a label no campo de busca. Quando desabilitado, apenas será exibido a label nas opções.

  * Tipo: `boolean`.
  * Valor inicial: `true`.

### mode

A propriedade `mode` define o modo de exibição do campo de busca. Pode ser utilizada para alternar entre diferentes estilos de exibição, como regular ou slim.

  * Tipo: `string`.
  * Valores possíveis: `"regular" | "slim"`.
  * Valor inicial: `"regular"`.

demo.js

```jsx
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import React from 'react';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => (
    <div className="ez-row">
        <EzSearchPlus
            label="Campo no modo regular"
            mode="regular"
            optionLoader={optionLoaderUF}
            className="ez-col ez-col--sd-4 ez-padding-horizontal--medium"
        />
        <EzSearchPlus
            label="Campo no modo slim"
            mode="slim"
            optionLoader={optionLoaderUF}
            className="ez-col ez-col--sd-4 ez-padding-horizontal--medium ez-margin-vertical--auto"
        />
    </div>
);

export default Demo;
```

### ensureClearButtonVisible

A propriedade `ensureClearButtonVisible` garante que o botão de limpar pesquisa esteja visível. Quando habilitado, o botão de limpar pesquisa será exibido mesmo quando o campo de busca estiver vazio.

  * Tipo: `boolean`.
  * Valor inicial: `false`.

### hideDescriptionInput

A propriedade `hideDescriptionInput` oculta a entrada de descrição no campo de busca. Quando habilitado, a entrada de descrição não será exibida.

  * Tipo: `boolean`.
  * Valor inicial: `false`.

demo.js

```jsx
import React, { useState } from 'react';
import { EzButton, EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => {
    const [hideDescriptionInput, setHideDescriptionInput] = useState(true);

    function toggleEnable() {
        setHideDescriptionInput((prev) => !prev);
    }

    return (
        <div className='ez-flex ez-flex--column ez-flex--justify-start'>
            <EzButton
                label={!hideDescriptionInput ? "Desabilitar descrição" : "Habilitar descrição"}
                onClick={() => toggleEnable()}
                className="ez-margin-vertical--medium"
            />
            <div className='ez-row'>
                <EzSearchPlus
                    label="Campo habilitado"
                    hideDescriptionInput={hideDescriptionInput}
                    optionLoader={optionLoaderUF}
                    className="ez-col ez-col--sd-4"
                />
            </div>
        </div>
    );
};

export default Demo;
```

### stopPropagateEnterKeyEvent

A propriedade `stopPropagateEnterKeyEvent` controla se o evento de pressionar a tecla Enter deve ser propagado. Quando habilitado, o evento de pressionar a tecla Enter não será propagado para outros elementos.

  * Tipo: `boolean`.
  * Valor inicial: `false`.

### autoFocus

A propriedade `autoFocus` define se o campo de busca deve receber foco automaticamente ao ser renderizado. Quando habilitado, o campo de busca receberá foco automaticamente.

  * Tipo: `boolean`.
  * Valor inicial: `false`.

### contextProperties

A propriedade `contextProperties` permite passar propriedades de contexto adicionais para a função `optionLoader`. Estas propriedades podem ser utilizadas para personalizar o comportamento da função `optionLoader`.

  * Tipo: `any`.
  * Valor inicial: `undefined`.

## Métodos

### setFocus

O método `setFocus` aplica o foco no campo de busca.

  * Parâmetros: Nenhum.
  * Retorno: `void`.

Focado: **Não**

### setBlur

O método `setBlur` remove o foco do campo de busca.

  * Parâmetros: Nenhum.
  * Retorno: `void`.

O foco será removido automaticamente após 2 segundos

demo.js

```jsx
import React, { useRef } from 'react';
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => {
    const element = useRef(null);
    const timeout = useRef(null);

    const removeFocus = () => {
        clearInterval(timeout.current);
        timeout.current = setTimeout(() => {
            element.current.setBlur();
        }, 2000);
    };

    return (
        <>
            <div className='ez-row'>
                <EzSearchPlus
                    ref={element}
                    label="Título do campo"
                    onFocus={removeFocus}
                    className="ez-col ez-col--sd-4"
                    optionLoader={optionLoaderUF}
                />

            </div>
            <label>O foco será removido automaticamente após 2 segundos</label>
        </>
    );
}

export default Demo;
```

### isInvalid

O método `isInvalid` retorna se o conteúdo do campo de busca é inválido.

  * Parâmetros: Nenhum.
  * Retorno: `boolean`.

Inválido: **Sim**

### getValueAsync

O método `getValueAsync` retorna uma _promise_ do valor atual do campo de busca, aguardando o carregamente dos dados, caso esteja em progresso.

  * Parâmetros: Nenhum.
  * Retorno: `Promise<IOption>`.

Value: ""

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzSearchPlus, EzButton } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => {
    const element = useRef(null);
    const [value, setValue] = useState("");

    async function getValue() {
        const currentValue = await element.current.getValueAsync();
        setValue(currentValue);
    };

    return (
        <div className='ez-flex ez-flex--column ez-flex--justify-start'>
            <div className='ez-row'>
                <EzSearchPlus
                    ref={element}
                    label="Título do campo"
                    className="ez-col ez-col--sd-4"
                    optionLoader={optionLoaderUF}
                />
            </div>
            <label>
                Value: {JSON.stringify(value)}
            </label>
            <EzButton
                label="Buscar valor"
                className="ez-margin-top--medium"
                onClick={getValue}
            />
        </div>
    );
}

export default Demo;
```

### clearValue

O método `clearValue` limpa o valor atual do campo de busca.

  * Parâmetros: Nenhum.
  * Retorno: `void`.

## Eventos

### ezChange

O evento `ezChange` é disparado quando o estado do componente é alterado.

  * Parâmetros: `CustomEvent`.
  * Retorno: `void`.

**Valor Alterado:**

demo.js

```jsx
import React, { useState } from 'react';
import { EzSearchPlus } from '@sankhyalabs/ezui/react/components';
import { optionLoaderUF } from '../utils/optionLoader';

const Demo = () => {
    const [value, setValue] = useState(null);

    const onChange = (evt) => {
        setValue(evt.detail);
    };

    return (
        <div className='ez-flex ez-flex--column ez-flex--justify-start'>
            <div className='ez-row'>
                <EzSearchPlus
                    label="Título do campo"
                    onEzChange={onChange}
                    optionLoader={optionLoaderUF}
                    className="ez-col ez-col--sd-4"
                />
            </div>
            <label>
                <b>Valor Alterado: </b> {value?.label}
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
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| codLabel | cod-label | Texto a ser apresentado no input de código. | string | undefined |
| contextProperties | context-properties | Propriedades de contexto da aplicação. | any | undefined |
| disableCodeInput | disable-code-input | Se true o campo de código ficara desabilitado. | boolean | false |
| disableDescriptionInput | disable-description-input | Se true o campo de de apresentação ficara desabilitado. | boolean | false |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| ensureClearButtonVisible | ensure-clear-button-visible | Garante que o botão de limpar pesquisa está sempre visível | boolean | false |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| hideDescriptionInput | hide-description-input | Se true o campo de de apresentação não será exibido. | boolean | false |
| hideErrorOnFocusOut | hide-error-on-focus-out | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | true |
| ignoreLimitCharsToSearch | ignore-limit-chars-to-search | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | false |
| isTextSearch | is-text-search | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | false |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| listOptionsPosition | -- | Propriedade depreciada na nova versão do componente de pesquisa. | IEzCheckBoxListPosition | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| optionLoader | -- | Carrega as opções dinamicamente. | (argument: ISearchArgument, ctxProperties?: any) => ISearchOption \| IOption \| (ISearchOption \| IOption)[] \| Promise<ISearchOption \| IOption \| (ISearchOption \| IOption)[]> | undefined |
| showOptionValue | show-option-value | Se false cada opção na lista deve exibir somente o label . | boolean | true |
| showSelectedValue | show-selected-value | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | true |
| stopPropagateEnterKeyEvent | stop-propagate-enter-key-event | Se true, interrompe a propagação do evento de KeyDown da tecla enter | boolean | false |
| suppressEmptyOption | suppress-empty-option | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | false |
| suppressPreLoad | suppress-pre-load | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | true |
| suppressSearch | suppress-search | Propriedade depreciada na nova versão do componente de pesquisa. | boolean | false |
| value | value | Define o valor do campo. | IOption \| string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<IOption> |
| ezEmptySearch | Emitido quando a pesquisa retorna um resultado inválido. | CustomEvent<string> |

### Methods

#### `clearValue() => Promise<void>`

Limpa o valor do campo de pesquisa

##### Returns

Type: `Promise<void>`

#### `getValueAsync() => Promise<IOption>`

Obtém o valor do componente só após a compo de apresentação ter sido resolvido pelo option loader quando necessário

##### Returns

Type: `Promise<IOption>`

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

  * ez-form-view

#### Depends on

  * ez-icon
  * ez-text-input
  * ez-popover-plus
  * ez-search-result-list

### CSS Variables

| Variable | Description |
|---|---|
| --ez-search--height | Define altura do input. |
| --ez-search--width | Define largura do input. |
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
| --ez-search__list-title--primary | Define a cor do texto da lista de opções. |
| --ez-search__list-text--primary | Define a cor do texto do value da lista de opções. |
| --ez-search__list-height | Define a altura do box da lista de opções. |
| --ez-search__list-min-width | Define a largura mínima da lista de opções. |
| --ez-search--space--medium | Define um espaçamento mediano entre elementos do componente. |
| --ez-search--space--small | Define um espaçamento pequeno entre elementos do componente. |
| --ez-search__scrollbar--color-default | Define a cor da barra de rolagem do componente. |
| --ez-search__scrollbar--color-background | Define a cor de fundo da barra de rolagem do componente. |
| --ez-search__scrollbar--color-hover | Define a cor do hover na barra de rolagem do componente. |
| --ez-search__scrollbar--color-clicked | Define a cor do active na barra de rolagem do componente. |
| --ez-search__scrollbar--border-radius | Define o raio da borda da barra de rolagem do componente. |
| --ez-search__scrollbar--width | Define a largura da barra de rolagem do componente. |
