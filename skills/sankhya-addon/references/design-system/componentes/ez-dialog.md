> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dialog/ (snapshot 2026-09-28)

# Dialog

Dialogs são janelas "pop-up" usadas para apresentar informações que precisam de atenção imediata do usuário.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzDialog, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const dialog = useRef();

    function showDialog(title, message){
        dialog.current.show(title, message, "warn");
    }

    return (
        <div className="ez-row">
            <EzDialog ref={dialog} />
            <EzButton
                label="Exibir Dialog"
                onClick={() => showDialog("Atenção", "Nesse caso precisamos de sua atenção exclusiva. Por isso você está vendo a mensagem sobre o conteúdo.")}
            />
        </div>
    )
};

export default Demo;
```

### Variações

demo.js

```jsx
import React, { useRef } from 'react';
import { EzDialog, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const dialog = useRef();

    function showDefault(message){
        dialog.current.show("", message, "default");
    }

    function showSuccess(title, message){
        dialog.current.show(title, message, "success");
    }

    function showAlert(title, message){
        dialog.current.show(title, message, "warn");
    }

    function showError(title, message){
        dialog.current.show(title, message, "critical");
    }

    return (
        <div className="ez-row">
            <EzDialog ref={dialog} />
            <EzButton
                label="Sucesso"
                onClick={() => showSuccess("Sucesso", "Usamos esse tipo de linguagem para evidenciar que tudo deu certo.")}
            >
                <EzIcon
                    class="ez-padding-right--medium"
                    iconName="check"
                    slot="leftIcon"
                />
            </EzButton>
            <EzButton
                label="Aviso"
                onClick={() => showAlert("Atenção", "Talvez algo não esteja como deveria...")}
            >
                <EzIcon
                    class="ez-padding-right--medium"
                    iconName="warning-outline"
                    slot="leftIcon"
                />
            </EzButton>
            <EzButton
                label="Erro"
                onClick={() => showError("Problema", "A ação solicitada não foi possível por uma falha.")}
            >
                <EzIcon
                    class="ez-padding-right--medium"
                    iconName="alert-circle-inverted"
                    slot="leftIcon"
                />
            </EzButton>
            <EzButton
                label="Mensagem neutra"
                onClick={() => showDefault("Mensagens que necessitam alguma atenção mas são neutras.")}
            />
        </div>
    )
};

export default Demo;
```

### Confirmação

### Ícones personalizados

demo.js

```jsx
import React, { useRef } from 'react';
import { EzDialog, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const dialog = useRef();

    function showDialog(title, message){
        dialog.current.show(title, message, "warn", true, "help-inverted", "Não", "Sim");
    }

    return (
        <div className="ez-row">
            <EzDialog ref={dialog} />
            <EzButton
                label="Ícones personalizados"
                onClick={() => showDialog("Confirmação", "Gostaria de continuar com a execução da rotina?")}
            />
        </div>
    )
};

export default Demo;
```

### Trabalhando com eventos

### Propriedade beforeClose

demo.js

```jsx
import React, { useRef } from 'react';
import { EzDialog, EzButton } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const dialog = useRef();

    const showDialog = (title, message) => {
        dialog.current.show(title, message, "warn", true, undefined, "Não", "Sim", null, beforeCloseAction);
    }

    const showDialogAppUtils = (title, message) => {
        ApplicationUtils.confirm(title, message, undefined, undefined, { beforeClose: beforeCloseAction });
    }

    const beforeCloseAction = () => {
        ApplicationUtils.message("BeforeClose", "Evento beforeClose emitido");
    }

    return (
        <div className="ez-row">
            <EzDialog
                beforeClose={beforeCloseAction}
                ref={dialog}
            />
            <EzButton
                label="Exibir Dialog (Propriedades)"
                onClick={() => showDialog("Utilizando beforeClose", "Com a propriedade beforeClose é possível criar regras para impedir o fechamento do modal")}
            />
            <EzButton
                label="Exibir Dialog (ApplicationUtils)"
                onClick={() => showDialogAppUtils("Utilizando beforeClose", "também é possível utilizar o beforeClose como uma opção da exibição de modais do ApplicationUtils")}
            />
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| beforeClose | -- | Define função a ser executada antes de fechar o modal | Function | undefined |
| confirm | confirm | Define se o ez-dialog será utilizado no modo de confirmação. | boolean | false |
| dialogType | dialog-type | Define aparência do ez-dialog. | DialogType.CRITICAL \| DialogType.DEFAULT \| DialogType.SUCCESS \| DialogType.WARN | undefined |
| ezTitle | ez-title | Texto a ser apresentado como título do campo. | string | undefined |
| message | message | Define a menssagem exibida no ez-dialog. | string | undefined |
| opened | opened | Define se o ez-dialog está aberto. | boolean | false |
| personalizedIconPath | personalized-icon-path | Define o ícone a ser exibido. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezAccept | Emitido ao confirmar o ez-dialog. | CustomEvent<boolean> |
| ezCancel | Emitido ao cancelar o ez-dialog. | CustomEvent<boolean> |

### Methods

#### `show(title: string, message: string, dialogType: DialogType, confirm: boolean, icon: string, labelCancel: string, labelConfirm: string, btnConfirmDanger: boolean, beforeClose: Function) => Promise<boolean>`

Exibe o ez-dialog.

##### Returns

Type: `Promise<boolean>`

### Dependencies

#### Depends on

  * ez-icon
  * ez-button

### CSS Variables

| Variable | Description |
|---|---|
| --dialog__container-padding | Define o espaçamento do container. |
| --dialog__btn__close--background-color | Define a cor de fundo do botão de fechar. |
| --dialog__btn__no--padding-right | Define o espaçamento direito do botão de negação. |
| --dialog__btn__close__image | Contém a imagem do ícone de fechamento. |
| --dialog__btn__min-width | Define a largura mínima dos botões. |
| --dialog__title--font-pattern | Define o estilo da mensagem exibida no título. |
| --dialog__title--padding-left | Define o espaçamento a esquerda do título. |
| --dialog__title__container--padding-bottom | Define o espaçamento abaixo do container do título. |
| --dialog__title--weight--large | Define o peso do título. |
| --dialog__body--font-pattern | Define o estilo do texto da mensagem. |
| --dialog__body--text-shadow | Define a sombra do texto da mensagem. |
| --dialog__body--text-weight--medium | Define o peso do texto da mensagem. |
| --dialog__body--padding-bottom | Define o espaçamento inferior do texto da mensagem. |
| --dialog__body--font-size | Define o tamanho do texto da mensagem. |
| --dialog__body--color | Define a cor do texto da mensagem. |
| --dialog__icon--color | Define a cor dos ícones dos indicadores de modo. |
| --dialog__critical--background-color | Define a cor do indicador do dialog de erro. |
| --dialog__warning--background-color | Define a cor do indicador do dialog de alert. |
| --dialog__success--background-color | Define a cor do indicador do dialog de sucesso. |
| --dialog-z-index | Define a camada que o dialog será exibido. |
| --dialog--warning__image | Contém a imagem do ícone de alerta. |
| --dialog--critical__image | Contém a imagem do ícone crítico. |
