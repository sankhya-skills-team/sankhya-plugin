> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box/ (snapshot 2026-09-28)

# Combo box

Um combobox é um menu suspenso que apresenta uma lista de opções, ele pode ser usado em conjuntos com checkbox, entradas de textos e outros elementos. Campos deste tipo permitem aos usuários escolher um valor a partir de uma lista opções filtrável.

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

demo.js

```jsx
import React from 'react';
import { EzComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div class="ez-col ez-col--sd-4">
            <EzComboBox label="Estado:">
                <option value="AC">Acre</option>
                <option value="AL">Alagoas</option>
                <option value="AP">Amapá</option>
                <option value="AM">Amazonas</option>
                <option value="BA">Bahia</option>
                <option value="CE">Ceará</option>
                <option value="ES">Espírito Santo</option>
                <option value="GO">Goiás</option>
                <option value="MA">Maranhão</option>
                <option value="MT">Mato Grosso</option>
                <option value="MS">Mato Grosso do Sul</option>
                <option value="MG">Minas Gerais</option>
                <option value="PA">Pará</option>
                <option value="PB">Paraíba</option>
                <option value="PR">Paraná</option>
                <option value="PE">Pernambuco</option>
                <option value="PI">Piauí</option>
                <option value="RJ">Rio de Janeiro</option>
                <option value="RN">Rio Grande do Norte</option>
                <option value="RS">Rio Grande do Sul</option>
                <option value="RO">Rondônia</option>
                <option value="RR">Roraima</option>
                <option value="SC">Santa Catarina</option>
                <option value="SP">São Paulo</option>
                <option value="SE">Sergipe</option>
                <option value="TO">Tocantins</option>
                <option value="DF">Distrito Federal</option>
            </EzComboBox>
        </div>
    )
};

export default Demo;
```

### Desabilitar interação

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

demo.js

```jsx
import React from 'react';
import { EzComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div class="ez-col ez-col--sd-4">
            <EzComboBox label="Estado:" value="MG" enabled={false}>
                <option value="AC">Acre</option>
                <option value="AL">Alagoas</option>
                <option value="AP">Amapá</option>
                <option value="AM">Amazonas</option>
                <option value="BA">Bahia</option>
                <option value="CE">Ceará</option>
                <option value="ES">Espírito Santo</option>
                <option value="GO">Goiás</option>
                <option value="MA">Maranhão</option>
                <option value="MT">Mato Grosso</option>
                <option value="MS">Mato Grosso do Sul</option>
                <option value="MG">Minas Gerais</option>
                <option value="PA">Pará</option>
                <option value="PB">Paraíba</option>
                <option value="PR">Paraná</option>
                <option value="PE">Pernambuco</option>
                <option value="PI">Piauí</option>
                <option value="RJ">Rio de Janeiro</option>
                <option value="RN">Rio Grande do Norte</option>
                <option value="RS">Rio Grande do Sul</option>
                <option value="RO">Rondônia</option>
                <option value="RR">Roraima</option>
                <option value="SC">Santa Catarina</option>
                <option value="SP">São Paulo</option>
                <option value="SE">Sergipe</option>
                <option value="TO">Tocantins</option>
                <option value="DF">Distrito Federal</option>
            </EzComboBox>
        </div>
    )
};

export default Demo;
```

### Mostra o valor da opção

#### Mostrar na opção selecionada.

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

#### Mostrar em todas as opções da lista.

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

demo.js

```jsx
import React from 'react';
import { EzComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div class="ez-col ez-col--sd-4">
            <EzComboBox label="Estado:" showOptionValue={true} value="MG">
                <option value="AC">Acre</option>
                <option value="AL">Alagoas</option>
                <option value="AP">Amapá</option>
                <option value="AM">Amazonas</option>
                <option value="BA">Bahia</option>
                <option value="CE">Ceará</option>
                <option value="ES">Espírito Santo</option>
                <option value="GO">Goiás</option>
                <option value="MA">Maranhão</option>
                <option value="MT">Mato Grosso</option>
                <option value="MS">Mato Grosso do Sul</option>
                <option value="MG">Minas Gerais</option>
                <option value="PA">Pará</option>
                <option value="PB">Paraíba</option>
                <option value="PR">Paraná</option>
                <option value="PE">Pernambuco</option>
                <option value="PI">Piauí</option>
                <option value="RJ">Rio de Janeiro</option>
                <option value="RN">Rio Grande do Norte</option>
                <option value="RS">Rio Grande do Sul</option>
                <option value="RO">Rondônia</option>
                <option value="RR">Roraima</option>
                <option value="SC">Santa Catarina</option>
                <option value="SP">São Paulo</option>
                <option value="SE">Sergipe</option>
                <option value="TO">Tocantins</option>
                <option value="DF">Distrito Federal</option>
            </EzComboBox>
        </div>
    )
};

export default Demo;
```

### Modo "slim"

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

### Evento `ezChange`

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

**Valor Selecionado:**

demo.js

```jsx
import React, { useState } from 'react';
import { EzComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const [selection, setSelection] = useState(null);

    const onChange = (evt) => {
        setSelection(evt.detail);
    };

    return (
        <div>
            <div class="ez-col ez-col--sd-4">
                <EzComboBox
                    label="Estado:"
                    onEzChange={onChange}
                >
                    <option value="AC">Acre</option>
                    <option value="AL">Alagoas</option>
                    <option value="AP">Amapá</option>
                    <option value="AM">Amazonas</option>
                    <option value="BA">Bahia</option>
                    <option value="CE">Ceará</option>
                    <option value="ES">Espírito Santo</option>
                    <option value="GO">Goiás</option>
                    <option value="MA">Maranhão</option>
                    <option value="MT">Mato Grosso</option>
                    <option value="MS">Mato Grosso do Sul</option>
                    <option value="MG">Minas Gerais</option>
                    <option value="PA">Pará</option>
                    <option value="PB">Paraíba</option>
                    <option value="PR">Paraná</option>
                    <option value="PE">Pernambuco</option>
                    <option value="PI">Piauí</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="RN">Rio Grande do Norte</option>
                    <option value="RS">Rio Grande do Sul</option>
                    <option value="RO">Rondônia</option>
                    <option value="RR">Roraima</option>
                    <option value="SC">Santa Catarina</option>
                    <option value="SP">São Paulo</option>
                    <option value="SE">Sergipe</option>
                    <option value="TO">Tocantins</option>
                    <option value="DF">Distrito Federal</option>
                </EzComboBox>
            </div>
            <div>
                <label>
                    <b>Valor Selecionado: </b> {selection?.label}
                </label>
            </div>
        </div>
    );
}

export default Demo;
```

### Controle programático de foco: `setFocus()` e `setBlur()`

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

Focado: **Não**

### Posicionamento da lista

Em algumas situações pode ser necessário arbitrar o posicionamento da lista de opções. Isso é possível através da propriedade `listOptionsPosition`. Essa propriedade permite definir o deslocamento horizontal e vertical da lista, além de determinar a referência do deslocamento.

#### Horizontal

Naturalmente o deslocamento horizontal é aplicado da esquerda para a direita, mas isso pode ser invertido passando o atributo `fromRight: true`.

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

demo.js

```jsx
import React, { useState } from 'react';
import { EzComboBox, EzCheck, EzNumberInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const [fromRight, setfromRight] = useState(false);
    const [horizontalPosition, setHorizontalPosition] = useState(10);

    function getListPosition() {
        return {fromRight, horizontalPosition};
    }

    return (
        <div className="ez-col ez-col--sd-4">
            <div className="ez-flex ez-flex--align-items-start">
                <EzNumberInput
                    label="Posicionamento Horizontal (pixels)"
                    value={horizontalPosition}
                    onEzChange={evt => setHorizontalPosition(evt.detail)}
                />
                <EzCheck
                    label="A partir da direita"
                    value={fromRight}
                    onEzChange={evt => setfromRight(evt.detail)}
                />
            </div>
            <div className="ez-row">
                <EzComboBox
                    label="Estado:"
                    listOptionsPosition={getListPosition()}
                >
                    <option value="AC">Acre</option>
                    <option value="AL">Alagoas</option>
                    <option value="AP">Amapá</option>
                    <option value="AM">Amazonas</option>
                    <option value="BA">Bahia</option>
                    <option value="CE">Ceará</option>
                    <option value="ES">Espírito Santo</option>
                    <option value="GO">Goiás</option>
                    <option value="MA">Maranhão</option>
                    <option value="MT">Mato Grosso</option>
                    <option value="MS">Mato Grosso do Sul</option>
                    <option value="MG">Minas Gerais</option>
                    <option value="PA">Pará</option>
                    <option value="PB">Paraíba</option>
                    <option value="PR">Paraná</option>
                    <option value="PE">Pernambuco</option>
                    <option value="PI">Piauí</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="RN">Rio Grande do Norte</option>
                    <option value="RS">Rio Grande do Sul</option>
                    <option value="RO">Rondônia</option>
                    <option value="RR">Roraima</option>
                    <option value="SC">Santa Catarina</option>
                    <option value="SP">São Paulo</option>
                    <option value="SE">Sergipe</option>
                    <option value="TO">Tocantins</option>
                    <option value="DF">Distrito Federal</option>
                </EzComboBox>
            </div>
        </div>
    )
};

export default Demo;
```

#### Vertical

O mesmo acontece com o deslocamento vertical que por padrão posiciona a lista tendo o topo como referência, mas podemos mostrá-la a partir da base - `fromBottom: true`. Caso a base seja a referência, a lista será exibida acima do seletor.

AcreAlagoasAmapáAmazonasBahiaCearáEspírito SantoGoiásMaranhãoMato GrossoMato Grosso do SulMinas GeraisParáParaíbaParanáPernambucoPiauíRio de JaneiroRio Grande do NorteRio Grande do SulRondôniaRoraimaSanta CatarinaSão PauloSergipeTocantinsDistrito Federal

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| alternativePlaceholder | alternative-placeholder | Texto alternativo a ser apresentado como título do campo. | string | undefined |
| autoFocus | auto-focus | Se true o campo de texto receberá o foco ao ser renderizado. | boolean | false |
| canShowError | can-show-error | Se false deixa de exibir a mensagem de erro dentro do campo. | boolean | true |
| enabled | enabled | Se false o usuário não pode interagir com o campo. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| hideErrorOnFocusOut | hide-error-on-focus-out | Quando verdadeiro deixa de exibir a mensagem de erro (se existente) quando focar em um elemento diferente. | boolean | true |
| isTextSearch | is-text-search | Informa se a pesquisa é do tipo texto. | boolean | false |
| label | label | Texto a ser apresentado como título do campo. | string | undefined |
| limitCharsToSearch | limit-chars-to-search | Define o limite de caracteres mínimo para realizar uma pesquisa | number | 3 |
| listOptionsPosition | -- | Define um posicionamento fixo para a lista de opções do CheckBox. | IEzCheckBoxListPosition | undefined |
| mode | mode | Define o tamanho do campo. | "regular" \| "slim" | "regular" |
| optionLoader | -- | Carrega as opções dinamicamente. | (argument: ISearchArgument) => IOption \| IOption[] \| Promise<IOption[]> | undefined |
| options | -- | Array com as opções do ez-combo-box. Os elementos devem obedecer o formato: {value: string, label: string} . | IOption[] | undefined |
| preventAutoFocus | prevent-auto-focus | Se true, impede que o campo de texto receba foco automaticamente ao abrir as opções. | boolean | false |
| showOptionValue | show-option-value | Se true cada opção na lista exibe o value junto com label . | boolean | false |
| showSelectedValue | show-selected-value | Se true a opção selecionada exibe o value junto com label . | boolean | false |
| stopPropagateEnterKeyEvent | stop-propagate-enter-key-event | Se true, ineterrompe a propagação do evento de KeyDown da tecla enter | boolean | true |
| suppressEmptyOption | suppress-empty-option | Se true remove a opção vazia da lista. | boolean | false |
| suppressSearch | suppress-search | Se true desabilita a digitação dentro do componente. | boolean | false |
| textEmptyOption | text-empty-option | Texto a ser apresentado na opção de valor nulo. | string | undefined |
| value | value | Define o valor do campo. | IOption \| string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezChange | Emitido quando acontece a alteração de valor do campo. | CustomEvent<IOption> |
| ezVisibilityChange | Emitido quando acontece a alteração de visibilidade do popover. | CustomEvent<boolean> |

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

  * ez-form-view

#### Depends on

  * ez-text-input
  * ez-icon
  * ez-popover-plus
  * ez-combo-box-list
