> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal-container/ (snapshot 2026-09-28)

# Modal Container

## Visão Geral

O componente `ez-modal-container` fornece uma estrutura padronizada para exibir conteúdo em modais e popups. Ele inclui cabeçalho com título e subtítulo, área de conteúdo personalizável e rodapé com botões de ação (OK e Cancelar), além de suporte completo a navegação por teclado.

É especialmente útil quando você precisa de uma interface consistente para diálogos de confirmação, formulários modais ou qualquer conteúdo que exija interação do usuário em uma camada sobreposta.

## Exemplo Básico

## Conteúdo de modal

Elementos mais comuns de um modal.

Inclui: Título, Subtítulo, espaço para conteúdo HTML, botões fechar, cancelar e OK.

## Conteúdo de Popup

Bastante parecido com o modal

Geralmente popups tem texto como conteúdo, mas também é possível usar qualquer conteúdo HTML.

demo.js

```jsx
import React, { useRef } from 'react';
import { EzButton, EzModal, EzPopup, EzModalContainer } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const modal = useRef();
    const poppup = useRef();

    const showModal = () => {
        modal.current.opened = true;
    }

    const showPopup = () => {
        poppup.current.opened = true
    }

    return (
        <div>
            <EzModal
                closeEsc={true}
                closeOutsideClick={true}
                opened={false}
                ref={modal}
            >
                <EzModalContainer
                    modalTitle="Conteúdo de modal"
                    modalSubTitle="Elementos mais comuns de um modal."
                    okButtonLabel="OK"
                    cancelButtonLabel="Cancelar"
                    onEzModalAction={()=>modal.current.opened = false}
                >
                    Inclui: Título, Subtítulo, espaço para conteúdo HTML, botões fechar, cancelar e OK.
                </EzModalContainer>
            </EzModal>
            <EzPopup
                ref={poppup}
                size="x-small"
                //Como o modal container já tem Header, precisamos omitir o header do Popup
                heightMode="auto"
                useHeader={false}
            >
                <EzModalContainer
                    modalTitle="Conteúdo de Popup"
                    modalSubTitle="Bastante parecido com o modal"
                    okButtonLabel="OK"
                    cancelButtonLabel="Cancelar"
                    onEzModalAction={()=>poppup.current.opened = false}
                >
                    Geralmente popups tem texto como conteúdo, mas também é possível usar qualquer conteúdo HTML.
                </EzModalContainer>
            </EzPopup>
            <div className="ez-row">
                <EzButton label="Abrir PopUp" onClick={()=>showPopup()}></EzButton>
                <EzButton label="Abrir Modal" onClick={()=>showModal()}></EzButton>
            </div>
        </div>
    )
};

export default Demo;
```

## Variações e estados

### Sem barra de títulos

Útil quando você precisa de um container simples sem cabeçalho. Utilize a propriedade `showTitleBar={false}` para ocultar o cabeçalho completo.

Quando estamos em um contexto que já tem o Header, podemo omitir a barra de títulos.

### Personalização dos botões

O modal container oferece controle total sobre os botões de ação através das propriedades de label e status.

#### Texto dos botões

Use `okButtonLabel` e `cancelButtonLabel` para definir textos personalizados nos botões.

## Label

O label dos botões é definido pelos atributos **cancelButtonLabel** e **okButtonLabel**.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzModalContainer } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzModalContainer
            modalTitle="Label"
            cancelButtonLabel="Personalizado"
            okButtonLabel="OK"
        >
            O label dos botões é definido pelos atributos <strong>cancelButtonLabel</strong> e <strong>okButtonLabel</strong>.
        </EzModalContainer>
    )
};

export default Demo;
```

#### Botão desabilitado

Use `okButtonStatus="DISABLED"` ou `cancelButtonStatus="DISABLED"` para desabilitar os botões.

## Status DESABILITADO

Também é possível escolher um dos 3 Status pra cada botão **HIDDEN** , **ENABLED** e **DISABLED**.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzModalContainer } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <EzModalContainer
            modalTitle="Status DESABILITADO"
            cancelButtonLabel="Cancel"
            okButtonLabel="OK"
            cancelButtonStatus="DISABLED"
        >
            Também é possível escolher um dos 3 Status pra cada botão <strong>HIDDEN</strong>, <strong>ENABLED</strong> e <strong>DISABLED</strong>.
        </EzModalContainer>
    )
};

export default Demo;
```

#### Botão oculto

Use `okButtonStatus="HIDDEN"` ou `cancelButtonStatus="HIDDEN"` para ocultar os botões.

Dica

Para ocultar um botão, você também pode omitir o `label` correspondente. Ambas as abordagens funcionam.

## Ocultar botão

Com o status **HIDDEN** o botão não é exibido.

### Botão de fechar

Por padrão, o botão de fechar (X) é exibido no canto superior direito. Use `showCloseButton={false}` para ocultá-lo.

## Modal sem botão fechar

Use showCloseButton={false} para ocultar o botão X

Este modal não possui o botão de fechar (X) no canto superior direito.

**💡 Nota:** Mesmo sem o botão X, o usuário ainda pode fechar o modal pressionando a tecla Esc, clicando fora do modal (se closeOutsideClick estiver habilitado) ou usando os botões OK/Cancelar.

```jsx
import { useRef, useState } from 'react';
import { EzButton, EzModal, EzModalContainer } from '@sankhyalabs/ezui/react/components';
import './no-close-button.css';

const Demo = () => {
    const modal = useRef();
    const [opened, setOpened] = useState(false);

    const showModal = () => {
        setOpened(true);
    };

    return (
        <div>
            <EzModal
                closeEsc={true}
                closeOutsideClick={true}
                opened={opened}
                ref={modal}
            >
                <EzModalContainer
                    modalTitle="Modal sem botão fechar"
                    modalSubTitle="Use showCloseButton={false} para ocultar o botão X"
                    showCloseButton={false}
                    okButtonLabel="OK"
                    cancelButtonLabel="Cancelar"
                    onEzModalAction={() => setOpened(false)}
                >
                    <div className="modal-container-no-close-button">
                        <p>
                            Este modal não possui o botão de fechar (X) no canto superior direito.
                        </p>
                        <p className="modal-container-no-close-button__note">
                            <strong>💡 Nota:</strong> Mesmo sem o botão X, o usuário ainda pode fechar o modal
                            pressionando a tecla Esc, clicando fora do modal (se closeOutsideClick estiver habilitado)
                            ou usando os botões OK/Cancelar.
                        </p>
                    </div>
                </EzModalContainer>
            </EzModal>

            <div className="ez-row">
                <EzButton label="Abrir Modal" onClick={showModal}></EzButton>
            </div>
        </div>
    );
};

export default Demo;
```

## Exemplos de uso

### Validação de formulário

Exemplo de como desabilitar o botão OK dinamicamente até que todos os campos obrigatórios sejam preenchidos corretamente.

## Cadastro de Usuário

Preencha todos os campos obrigatórios

Preencha todos os campos corretamente para habilitar o botão Salvar.

### Gerenciamento de eventos

Demonstração de como capturar e tratar as ações do modal. O evento `ezModalAction` pode emitir 4 valores diferentes:

  * **"OK"** \- Quando o usuário clica no botão OK ou pressiona Enter
  * **"CANCEL"** \- Quando o usuário clica no botão Cancelar
  * **"CLOSE"** \- Quando o usuário clica no botão fechar (X) ou pressiona Esc
  * **"LOAD"** \- Disparado após o componente ser montado no DOM

## Modal actions

Clique nos botões e veja as ações emitidas

Evento emitido: **LOAD**

### Modal informativo

Modal simples com apenas um botão de confirmação, ideal para exibir mensagens informativas ou alertas.

## Informação

Esta é uma mensagem importante

🎉 Sua operação foi concluída com sucesso!

**Dica:** Modais informativos geralmente possuem apenas um botão de confirmação, ocultando o botão de cancelamento com `cancelButtonStatus="HIDDEN"`.

```jsx
import { useRef, useState } from 'react';
import { EzButton, EzModal, EzModalContainer } from '@sankhyalabs/ezui/react/components';
import './info-modal.css';

const Demo = () => {
    const modal = useRef();
    const [opened, setOpened] = useState(false);

    const showModal = () => {
        setOpened(true);
    };

    return (
        <div>
            <EzModal
                closeEsc={true}
                closeOutsideClick={true}
                opened={opened}
                ref={modal}
            >
                <EzModalContainer
                    modalTitle="Informação"
                    modalSubTitle="Esta é uma mensagem importante"
                    okButtonLabel="Entendi"
                    cancelButtonStatus="HIDDEN"
                    onEzModalAction={() => setOpened(false)}
                >
                    <div className="modal-container-info-modal">
                        <p>
                            🎉 Sua operação foi concluída com sucesso!
                        </p>
                        <p className="modal-container-info-modal__tip">
                            <strong>Dica:</strong> Modais informativos geralmente possuem apenas um botão de confirmação,
                            ocultando o botão de cancelamento com <code>cancelButtonStatus="HIDDEN"</code>.
                        </p>
                    </div>
                </EzModalContainer>
            </EzModal>

            <div className="ez-row">
                <EzButton label="Mostrar Informação" onClick={showModal}></EzButton>
            </div>
        </div>
    );
};

export default Demo;
```

### Ações customizadas

Exemplo de como criar sua própria interface de ações dentro do modal, ocultando os botões padrão através de `okButtonStatus="HIDDEN"` e `cancelButtonStatus="HIDDEN"`.

## Escolha uma Opção

Selecione a ação desejada

Este modal demonstra como ocultar os botões padrão e criar suas próprias ações personalizadas.

Nenhuma opção selecionada ainda.

**💡 Dica:** Use `okButtonStatus="HIDDEN"` e `cancelButtonStatus="HIDDEN"`para ocultar os botões padrão e criar sua própria interface de ações dentro do conteúdo do modal.

```jsx
import { useRef, useState } from 'react';
import { EzButton, EzModal, EzModalContainer } from '@sankhyalabs/ezui/react/components';
import './custom-actions.css';

const Demo = () => {
    const modal = useRef();
    const [opened, setOpened] = useState(false);
    const [selectedOption, setSelectedOption] = useState('');

    const handleOptionClick = (option) => {
        setSelectedOption(option);
        setTimeout(() => {
            alert(`Você selecionou: ${option}`);
            setOpened(false);
            setSelectedOption('');
        }, 300);
    };

    const showModal = () => {
        setOpened(true);
    };

    return (
        <div>
            <EzModal
                closeEsc={true}
                closeOutsideClick={true}
                opened={opened}
                ref={modal}
            >
                <EzModalContainer
                    modalTitle="Escolha uma Opção"
                    modalSubTitle="Selecione a ação desejada"
                    okButtonStatus="HIDDEN"
                    cancelButtonStatus="HIDDEN"
                    showCloseButton={true}
                    onEzModalAction={() => setOpened(false)}
                >
                    <div className="modal-container-custom-actions">
                        <p className="modal-container-custom-actions__description">
                            Este modal demonstra como ocultar os botões padrão e criar suas próprias ações personalizadas.
                        </p>
                        <span className="modal-container-custom-actions__selected-option">
                            {selectedOption ? `Opção selecionada: ${selectedOption}` : 'Nenhuma opção selecionada ainda.'}
                        </span>

                        <div className="modal-container-custom-actions__buttons">
                            <EzButton
                                label="🎨 Opção de Design"
                                onClick={() => handleOptionClick('Design')}
                                class="ez-button--full-width"
                            />
                            <EzButton
                                label="⚙️ Opção de Configuração"
                                onClick={() => handleOptionClick('Configuração')}
                                class="ez-button--full-width"
                            />
                            <EzButton
                                label="📊 Opção de Relatório"
                                onClick={() => handleOptionClick('Relatório')}
                                class="ez-button--full-width"
                            />
                            <EzButton
                                label="❌ Cancelar"
                                onClick={() => setOpened(false)}
                                class="ez-button--full-width modal-container-custom-actions__cancel-button"
                            />
                        </div>
                    </div>
                </EzModalContainer>
            </EzModal>

            <div className="ez-row">
                <EzButton label="Abrir Menu Customizado" onClick={showModal}></EzButton>
            </div>

            <div className="modal-container-custom-actions__tip">
                <strong>💡 Dica:</strong> Use <code>okButtonStatus="HIDDEN"</code> e <code>cancelButtonStatus="HIDDEN"</code>
                para ocultar os botões padrão e criar sua própria interface de ações dentro do conteúdo do modal.
            </div>
        </div>
    );
};

export default Demo;
```

## Atalhos de teclado

O componente possui suporte nativo para navegação por teclado:

  * **Enter** \- Dispara o evento com ação `"OK"`
  * **Esc** \- Dispara o evento com ação `"CLOSE"`

Importante

Os atalhos de teclado funcionam apenas quando o componente possui foco. O componente só será focado automaticamente caso a propriedade `autoFocus` seja verdadeira. Se você precisar restaurar o foco após interações específicas (como abrir um popup ou executar uma ação), será necessário implementar essa lógica manualmente.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| autoFocus | auto-focus | Se true o modal container receberá o foco ao ser renderizado. | boolean | false |
| cancelButtonLabel | cancel-button-label | Define o texto do botão de cancelamento. | string | undefined |
| cancelButtonStatus | cancel-button-status | Define o estado do botão de cancelamento. | "DISABLED" \| "ENABLED" \| "HIDDEN" | undefined |
| modalSubTitle | modal-sub-title | Texto do subtítulo, geralmente usado para orientação do usuário. | string | undefined |
| modalTitle | modal-title | Texto a ser apresentado como título do modal. | string | undefined |
| okButtonLabel | ok-button-label | Determina o texto do botão de confirmação. | string | undefined |
| okButtonStatus | ok-button-status | Define o estado do botão de confirmação. | "DISABLED" \| "ENABLED" \| "HIDDEN" | undefined |
| showCloseButton | show-close-button | Define a visibilidade do botão de fechar. | boolean | true |
| showTitleBar | show-title-bar | Define se o cabeçalho será mostrado. | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| ezModalAction | Representa a interação com o usuário. OK - Quando o botão é acionado CANCEL - Quando o botão de cancelar é acionado CLOSE - Quando o botão de fechar é acionado. LOAD - Quando o modal é carregado (eventualmente pode ser usado para dar foco a um elemento específico) | CustomEvent<string> |

### Dependencies

#### Used by

  * ez-link-builder
  * ez-simple-image-uploader

#### Depends on

  * ez-icon
  * ez-button
