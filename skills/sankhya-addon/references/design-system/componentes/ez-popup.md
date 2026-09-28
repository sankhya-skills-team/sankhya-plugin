> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popup/ (snapshot 2026-09-28)

# Popup

São janelas flutuantes usadas com pequenas frases de texto, normalmente como notificação ou aviso, e esperam uma ação do usuário para serem fechadas. O componente oferece flexibilidade para diferentes tipos de interação e personalização, por meio de suas propriedades.

Diferente do Dialog que tem estrutura predeterminada, o conteúdo do Popup é livre aceitando **qualquer estrutura HTML**.

```jsx
import React, { useRef } from 'react';
import { EzPopup, EzButton } from '@sankhyalabs/ezui/react/components';
import './demo.css';

const Demo = () => {
    const popup = useRef();

    const openPopup = () => {
        popup.current.opened = true;
    }

    return (
        <div className='ez-popup-demo-container'>
            <EzPopup
                ezTitle="Popup ou Dialog?"
                size="x-small"
                heightMode="auto"
                ref={popup}
                footerButtons={[
                    {
                        label: "Legal",
                        rightIconName: "thumbs-up",
                    },
                    { label: "Prefiro o Dialog" },
                    { label: "Cancelar" }
                ]}
            >
                <label>
                    Diferente do Dialog que tem estrutura
                    predeterminada, o conteúdo do Popup é livre
                    aceitando <strong>qualquer estrutura HTML</strong>.
                </label>
            </EzPopup>
            <EzButton label="Abrir Popup" onClick={openPopup} />
        </div>
    )
};

export default Demo;
```

## Controle de exibição do cabeçalho

É possível controlar a exibição do cabeçalho através da propriedade `useHeader`. Quando desabilitado, o título e o botão de fechar não são exibidos.

O popup é exibido sem título, mas o header permanece visível, mostrando apenas o ícone de fechar no canto superior direito. Isso permite que o usuário feche o popup mesmo sem um título definido.

demo.js

```jsx
import React, { useRef, useState } from 'react';
import { EzPopup, EzButton } from '@sankhyalabs/ezui/react/components';
import './demo.css';

const Demo = () => {
    const popup = useRef();
    const [useHeader, setUseHeader] = useState(true);

    const openPopup = () => {
        popup.current.opened = true;
    }

    const toggleHeader = (value) => {
        setUseHeader(value);
        openPopup();
    }

    return (
        <div className='ez-popup-demo-container'>
            <EzPopup
                ref={popup}
                useHeader={useHeader}
                size="x-small"
                heightMode="auto"
                footerButtons={[
                    { label: "OK" },
                ]}
            >
                <label>
                    {useHeader ?
                        "O popup é exibido sem título, mas o header permanece visível, mostrando apenas o ícone de fechar no canto superior direito. Isso permite que o usuário feche o popup mesmo sem um título definido."
                        : "O popup é exibido completamente sem header, removendo tanto o título quanto o ícone de fechar. Neste caso, o usuário precisará usar os botões do footer ou outras ações para fechar o popup."
                    }
                </label>
            </EzPopup>
            <EzButton label="Sem título" onClick={() => toggleHeader(true)} />
            <EzButton label="Sem header" onClick={() => toggleHeader(false)} />
        </div>
    )
};

export default Demo;
```

## Botões do rodapé (footerButtons)

A propriedade `footerButtons` permite adicionar até 3 botões no rodapé do popup. Aceita todas as propriedades do componente `ez-button`, incluindo variantes, ícones e eventos personalizados.

### Propriedades padrão por posição

O componente aplica propriedades padrão baseadas na posição do botão, que podem ser sobrescritas:

  * **1º botão (índice 0)** : `variant="primary"`, `size="small"`, `label="Confirmar"`, `onClick` que fecha o popup e emite evento "OK"
  * **2º botão (índice 1)** : `variant="secondary"`, `size="small"`, `label="Cancelar"`, `onClick` que fecha o popup
  * **3º botão (índice 2)** : `variant="tertiary"`, `size="small"`, `label="Fechar"`, `onClick` que fecha o popup

Qualquer propriedade informada no array `footerButtons` sobrescreve as propriedades padrão correspondentes.

Este popup demonstra as **propriedades padrão** dos botões:

  * **1º botão:** variant="primary", label="Confirmar"
  * **2º botão:** variant="secondary", label="Cancelar"
  * **3º botão:** variant="tertiary", label="Fechar"

Todos têm `size="small"` por padrão.

Este popup demonstra como **sobrescrever** as propriedades padrão:

  * Labels personalizados
  * Ícones adicionados
  * Variantes diferentes (incluindo "danger")
  * Tamanhos customizados
  * Eventos onClick personalizados

### Exemplos práticos com múltiplos botões

Esta é uma mensagem informativa que requer apenas uma confirmação do usuário.Você tem certeza que deseja executar esta ação? Esta operação não pode ser desfeita.Você fez alterações no documento. Como deseja proceder?

**Dica:** A propriedade _footerButtons_ aceita até 3 botões e todas as propriedades do componente ez-button.

demo.js

```jsx
import { useRef, useState } from 'react';
import { EzPopup, EzButton } from '@sankhyalabs/ezui/react/components';
import './demo.css';

const Demo = () => {
    const [message, setMessage] = useState('');
    const popupSingleButton = useRef();
    const popupTwoButtons = useRef();
    const popupThreeButtons = useRef();
    const timeoutRef = useRef(null);

    const openSingleButton = () => {
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
        }
        setMessage('');
        popupSingleButton.current.opened = true;
    }

    const openTwoButtons = () => {
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
        }
        setMessage('');
        popupTwoButtons.current.opened = true;
    }

    const openThreeButtons = () => {
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
        }
        setMessage('');
        popupThreeButtons.current.opened = true;
    }

    const handleAction = async (action) => {
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
        }
        setMessage(`Ação executada: ${action}`);
        popupSingleButton.current.opened = false;
        popupTwoButtons.current.opened = false;
        popupThreeButtons.current.opened = false;
        timeoutRef.current = setTimeout(() => setMessage(''), 3000);
    }

    return (
        <div>
            {/* Popup com 1 botão */}
            <EzPopup
                ezTitle="Confirmação"
                size="x-small"
                heightMode="auto"
                ref={popupSingleButton}
                footerButtons={[
                    {
                        label: "Entendi",
                        variant: "primary",
                        onClick: () => handleAction("Confirmado")
                    }
                ]}
            >
                <label>
                    Esta é uma mensagem informativa que requer apenas
                    uma confirmação do usuário.
                </label>
            </EzPopup>

            {/* Popup com 2 botões */}
            <EzPopup
                ezTitle="Confirmar ação"
                size="small"
                heightMode="auto"
                ref={popupTwoButtons}
                footerButtons={[
                    {
                        label: "Confirmar",
                        variant: "primary",
                        onClick: () => handleAction("Confirmado")
                    },
                    {
                        label: "Cancelar",
                        variant: "secondary",
                        onClick: () => handleAction("Cancelado")
                    }
                ]}
            >
                <label>
                    Você tem certeza que deseja executar esta ação?
                    Esta operação não pode ser desfeita.
                </label>
            </EzPopup>

            {/* Popup com 3 botões */}
            <EzPopup
                ezTitle="Múltiplas opções"
                size="medium"
                heightMode="auto"
                ref={popupThreeButtons}
                footerButtons={[
                    {
                        label: "Salvar",
                        variant: "primary",
                        iconName: "save",
                        onClick: () => handleAction("Salvo")
                    },
                    {
                        label: "Salvar e Sair",
                        variant: "secondary",
                        iconName: "save-exit",
                        onClick: () => handleAction("Salvo e fechado")
                    },
                    {
                        label: "Cancelar",
                        variant: "tertiary",
                        iconName: "close",
                        onClick: () => handleAction("Cancelado")
                    }
                ]}
            >
                <label>
                    Você fez alterações no documento. Como deseja proceder?
                    <br /><br />
                    <strong>Dica:</strong> A propriedade <em>footerButtons</em> aceita
                    até 3 botões e todas as propriedades do componente ez-button.
                </label>
            </EzPopup>
            <div className='ez-popup-demo-container'>
                <EzButton label="1 Botão" onClick={openSingleButton} />
                <EzButton label="2 Botões" onClick={openTwoButtons} />
                <EzButton label="3 Botões" onClick={openThreeButtons} />
            </div>
            {message && (
                <div className="ez-row ez-flex--justify-center ez-margin-top--medium">
                    <div className="ez-alert ez-alert--success ez-popup-alert-success">
                        {message}
                    </div>
                </div>
            )}
        </div>
    )
};

export default Demo;
```

## Fechamento automático (autoClose)

Controla se o popup deve fechar automaticamente ao clicar fora dele. Por padrão, esta propriedade está habilitada (`true`), mas pode ser desabilitada quando for necessário forçar o usuário a utilizar os botões para fechar.

Este popup pode ser fechado clicando fora dele ou pressionando ESC. A propriedade **autoClose** está definida como **true** (padrão).Este popup só pode ser fechado através dos botões ou pressionando ESC. A propriedade **autoClose** está definida como **false**.

## Variações de largura

O popup oferece diferentes tamanhos predefinidos através da propriedade `size`: x-small, small, medium, large, x-large e auto.

Dependendo do tamanho do conteúdo pode ser necessário aumentar ou diminuir a largura do Popup.

demo.js

```jsx
import { useRef } from 'react';
import { EzPopup, EzButton } from '@sankhyalabs/ezui/react/components';
import './demo.css';

const Demo = () => {
    const popup = useRef();

    const openPopup = (size) => {
        popup.current.ezTitle = `Tamanho: "${size}"`;
        popup.current.size = size;
        popup.current.opened = true;
    }

    return (
        <div className='ez-popup-demo-container'>
            <EzPopup heightMode="auto" ref={popup}>
                <label>
                    Dependendo do tamanho do conteúdo pode ser necessário
                    aumentar ou diminuir a largura do Popup.
                </label>
            </EzPopup>
            <EzButton label="x-small" onClick={() => openPopup("x-small")} />
            <EzButton label="small" onClick={() => openPopup("small")} />
            <EzButton label="medium" onClick={() => openPopup("medium")} />
            <EzButton label="large" onClick={() => openPopup("large")} />
            <EzButton label="x-large" onClick={() => openPopup("x-large")} />
        </div>
    )
};

export default Demo;
```

## Variações de altura

A propriedade `heightMode` controla como a altura do popup é calculada: `auto` ajusta ao conteúdo ou `full` ocupa toda a altura da tela.

O atributo **heightMode** pode ser definido para se ajustar ao tamanho do conteúdo: **auto** ou para expandir por toda a página: **full**.

## Barra de rolagem vertical

Quando o conteúdo excede a altura disponível, é possível habilitar a barra de rolagem vertical através da propriedade `enabledScroll`.

O atributo **enableScroll** pode ser definido para se ajustar se o conteúdo do componente pode ou não possuir uma barra de rolagem vertical.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac tempus leo. Suspendisse et commodo erat, accumsan efficitur nisl. Aenean tristique magna sit amet tellus porttitor, ut dapibus mauris dictum. Ut eget magna nisl. Etiam in bibendum libero. Phasellus mollis pharetra pretium. Maecenas vulputate laoreet velit et vehicula. Nulla tortor quam, convallis et pharetra et, sollicitudin in sem. Nullam maximus quam tempus magna ultrices feugiat. Nullam eget gravida leo. Vestibulum bibendum fermentum elit ac varius. Phasellus ultricies metus vitae nisi feugiat, ut consectetur neque convallis. In placerat libero sit amet tristique mollis. Ut et metus elit.

Quisque maximus viverra ipsum cursus aliquam. Vivamus enim dolor, auctor in sodales vitae, maximus eu felis. Curabitur placerat ex sem, vitae egestas elit consequat ut. Fusce ultrices ex vitae nibh consequat pulvinar. Sed massa ligula, facilisis cursus magna eget, efficitur sodales tortor. Donec metus nisl, lobortis a cursus ut, convallis id nibh. Fusce sagittis elit sem, eget pharetra purus venenatis eu. Duis id imperdiet lacus, vitae blandit orci. Morbi sit amet tortor enim.

Quisque lacinia imperdiet dui quis auctor. In hac habitasse platea dictumst. Cras ultricies ligula nec faucibus viverra. Vestibulum ac scelerisque odio, a bibendum elit. Nam egestas, tellus id rutrum gravida, leo dui vulputate odio, quis malesuada massa nisl in libero. Mauris dictum scelerisque nisi sit amet tempus. Quisque gravida ut diam vel tempor. Nunc ultrices pharetra consequat. Aenean sit amet ante a neque euismod dictum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse eu massa nunc. Nullam ac consequat neque. Maecenas mauris massa, vehicula at est et, imperdiet scelerisque quam. Cras ut orci sem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas vitae felis sit amet mauris vehicula vestibulum. In elementum, elit lobortis imperdiet porttitor, ipsum turpis laoreet felis, quis hendrerit ex tellus non quam. Nulla facilisi. Morbi facilisis, lacus at consectetur aliquam, turpis velit dictum metus, ut condimentum felis nunc vitae ante. Sed scelerisque lobortis nulla, id pharetra nunc tincidunt eu. Ut sed nunc sed mi finibus pretium. Donec non orci dignissim leo cursus ornare. Proin non nibh ac dui dapibus imperdiet. Fusce tempor sapien at lorem elementum imperdiet. Vestibulum fringilla ultricies lobortis. Donec sit amet egestas ante. Aenean in tempus lorem. Donec bibendum, dolor sit amet posuere convallis, erat metus tempor ligula, in tempor est erat consequat dui. Maecenas venenatis sapien a tincidunt pretium.

Praesent et placerat erat, eu accumsan ex. Integer pellentesque metus turpis, a vestibulum tortor iaculis ac. Vestibulum malesuada, nulla non pulvinar laoreet, ex dolor lacinia neque, ac feugiat turpis felis et tortor. Nullam metus risus, sollicitudin eget egestas nec, imperdiet eget purus. Curabitur consectetur sem quis eros venenatis, non pharetra nisl luctus. Nullam sed fermentum lectus. Mauris ut luctus velit. Ut sagittis lectus sed quam auctor, in aliquam nibh blandit. Sed a malesuada erat.

```jsx
import { useRef } from 'react';
import { EzPopup, EzButton } from '@sankhyalabs/ezui/react/components';
import './overflowY.css'
import './demo.css';

const Demo = () => {
  const popup = useRef();

  const openPopup = (enableScroll) => {
    popup.current.ezTitle = `Permitir barra de rolagem: "${enableScroll}"`;
    popup.current.enabledScroll = enableScroll;
    popup.current.heightMode = 'auto';
    popup.current.opened = true;
  };

  return (
    <div className='ez-popup-demo-container'>
      <EzPopup ref={popup}>
        <label className='ez-popup-scrollable-label'>
          O atributo <strong>enableScroll</strong> pode
          ser definido para se ajustar se o conteúdo do componente
          pode ou não possuir uma barra de rolagem vertical.
        </label>

        <div className='ez-popup-scrollable-text'>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac tempus leo. Suspendisse et commodo erat,
            accumsan efficitur nisl. Aenean tristique magna sit amet tellus porttitor, ut dapibus mauris dictum. Ut eget
            magna nisl. Etiam in bibendum libero. Phasellus mollis pharetra pretium. Maecenas vulputate laoreet velit et
            vehicula. Nulla tortor quam, convallis et pharetra et, sollicitudin in sem. Nullam maximus quam tempus magna
            ultrices feugiat. Nullam eget gravida leo. Vestibulum bibendum fermentum elit ac varius. Phasellus ultricies
            metus vitae nisi feugiat, ut consectetur neque convallis. In placerat libero sit amet tristique mollis. Ut
            et
            metus elit.
          </p>
          <br />
          <p>
            Quisque maximus viverra ipsum cursus aliquam. Vivamus enim dolor, auctor in sodales vitae, maximus eu felis.
            Curabitur placerat ex sem, vitae egestas elit consequat ut. Fusce ultrices ex vitae nibh consequat pulvinar.
            Sed massa ligula, facilisis cursus magna eget, efficitur sodales tortor. Donec metus nisl, lobortis a cursus
            ut, convallis id nibh. Fusce sagittis elit sem, eget pharetra purus venenatis eu. Duis id imperdiet lacus,
            vitae blandit orci. Morbi sit amet tortor enim.
          </p>
          <br />
          <p>
            Quisque lacinia imperdiet dui quis auctor. In hac habitasse platea dictumst. Cras ultricies ligula nec
            faucibus
            viverra. Vestibulum ac scelerisque odio, a bibendum elit. Nam egestas, tellus id rutrum gravida, leo dui
            vulputate odio, quis malesuada massa nisl in libero. Mauris dictum scelerisque nisi sit amet tempus. Quisque
            gravida ut diam vel tempor. Nunc ultrices pharetra consequat. Aenean sit amet ante a neque euismod dictum.
            Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse eu massa nunc. Nullam ac consequat
            neque. Maecenas mauris massa, vehicula at est et, imperdiet scelerisque quam. Cras ut orci sem. Interdum et
            malesuada fames ac ante ipsum primis in faucibus. Maecenas vitae felis sit amet mauris vehicula vestibulum.
            In elementum, elit lobortis imperdiet porttitor, ipsum turpis laoreet felis, quis hendrerit ex tellus non
            quam.
            Nulla facilisi. Morbi facilisis, lacus at consectetur aliquam, turpis velit dictum metus, ut condimentum
            felis
            nunc vitae ante. Sed scelerisque lobortis nulla, id pharetra nunc tincidunt eu. Ut sed nunc sed mi finibus
            pretium. Donec non orci dignissim leo cursus ornare. Proin non nibh ac dui dapibus imperdiet. Fusce tempor
            sapien at lorem elementum imperdiet. Vestibulum fringilla ultricies lobortis. Donec sit amet egestas ante.
            Aenean in tempus lorem. Donec bibendum, dolor sit amet posuere convallis, erat metus tempor ligula, in
            tempor
            est erat consequat dui. Maecenas venenatis sapien a tincidunt pretium.
          </p>
          <br />
          <p>
            Praesent et placerat erat, eu accumsan ex. Integer pellentesque metus turpis, a vestibulum tortor iaculis
            ac.
            Vestibulum malesuada, nulla non pulvinar laoreet, ex dolor lacinia neque, ac feugiat turpis felis et tortor.
            Nullam metus risus, sollicitudin eget egestas nec, imperdiet eget purus. Curabitur consectetur sem quis eros
            venenatis, non pharetra nisl luctus. Nullam sed fermentum lectus. Mauris ut luctus velit. Ut sagittis lectus
            sed
            quam auctor, in aliquam nibh blandit. Sed a malesuada erat.
          </p>
        </div>
      </EzPopup>
      <EzButton label='Permitir rolagem' onClick={() => openPopup(true)} />
      <EzButton label='Não permitir' onClick={() => openPopup(false)} />
    </div>
  );
};

export default Demo;
```

## Eventos do componente

O popup emite eventos quando é fechado, permitindo que a aplicação responda adequadamente às ações do usuário.

Sempre que o popup é fechado, o contexto é notificado através do evento **ezClosePopup**.

## Considerações de usabilidade

  * Use popups para confirmações rápidas ou informações que não interrompam o fluxo principal
  * Prefira `autoClose={false}` quando a ação for crítica e requerer confirmação explícita
  * Limite o uso de três botões no rodapé para manter a interface limpa
  * Utilize variantes apropriadas nos botões: `primary` para ação principal, `secondary` para alternativas e `tertiary` para ações de cancelamento
  * **Aproveite as propriedades padrão** : para casos simples, você pode usar arrays vazios `[{}, {}, {}]` no `footerButtons` para obter botões com configuração padrão
  * **Override seletivo** : sobrescreva apenas as propriedades que precisam ser diferentes dos padrões (ex: apenas o `label` ou `onClick`)
  * O primeiro botão sempre tem `variant="primary"` por padrão, seguindo convenções de UX para ação principal

## Slots

O **Popup** disponibiliza os seguintes slots para personalização:

  * **footer** : Permite adicionar conteúdo personalizado adicional no rodapé do popup. O conteúdo do slot é posicionado à esquerda dos botões configurados pela propriedade `footerButtons`, permitindo adicionar informações extras ou elementos complementares sem substituir os botões existentes.

O slot **footer** permite adicionar conteúdo adicional no rodapé, posicionado à esquerda dos botões do `footerButtons`.

Informação adicional

```jsx
import { useRef } from 'react';
import { EzPopup, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';
import './demo.css';
import './footerSlot.css';

const Demo = () => {
    const popup = useRef();

    const openPopup = () => {
        popup.current.opened = true;
    }

    return (
        <div className='ez-popup-demo-container'>
            <EzPopup
                ezTitle="Rodapé com Conteúdo Adicional"
                size="small"
                heightMode="auto"
                ref={popup}
                footerButtons={[
                    { label: "Confirmar" },
                    { label: "Cancelar" }
                ]}
            >
                <label>
                    O slot <strong>footer</strong> permite adicionar
                    conteúdo adicional no rodapé, posicionado à esquerda
                    dos botões do <code>footerButtons</code>.
                </label>

                <div slot="footer" className="footer-slot-container">
                    <div className="footer-slot-info">
                        <EzIcon iconName="info-circle" size="small"></EzIcon>
                        <span className="footer-slot-info-text">
                            Informação adicional
                        </span>
                    </div>
                </div>
            </EzPopup>
            <EzButton label="Abrir Popup" onClick={openPopup} />
        </div>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| autoClose | auto-close | Define se o popup deve fechar automaticamente ao clicar fora dele. | boolean | true |
| enabledScroll | enabled-scroll | Possibilita scroll vertical no conteúdo interno do componente | boolean | true |
| ezTitle | ez-title | Texto a ser apresentado como título do componente. | string | undefined |
| footerButtons | -- | Botões do rodapé do popup. Aceita todas as propriedades do ez-button. Limitado a até 3 botões. | Partial<EzButtonProps>[] | [] |
| heightMode | height-mode | Define altura do componente. | "auto" \| "full" | "full" |
| opened | opened | Define se o ez-popover está aberto. | boolean | false |
| size | size | Define a largura do ez-popup. | "auto" \| "large" \| "medium" \| "small" \| "x-large" \| "x-small" | "medium" |
| useHeader | use-header | Define se o componente utilizará cabeçalho. | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| ezClosePopup | Evento emitido ao clicar no botão de fechar (onEzClosePopup). | CustomEvent<any> |
| ezPopupAction | Evento emitido ao clicar no botão de fechar (ezPopupAction = OK) | CustomEvent<string> |

### Dependencies

#### Used by

  * ez-image-input
  * ez-link-builder
  * ez-simple-image-uploader

#### Depends on

  * ez-button

### CSS Variables

| Variable | Description |
|---|---|
| --ez-popup-z-index | Define a camada em que o componente será exibido. |
| --ez-popup__container--color | Define a cor do texto do container do popup. |
| --ez-popup__container--padding | Define o espaçamento do container do popup. |
| --ez-popup__title--font-family | Define a família da fonte do título do popup. |
| --ez-popup__title--font-size | Define o tamanho da fonte do título do popup. |
| --ez-popup__title--color | Define a cor da fonte do título do popup. |
| --ez-popup__title--font-weight | Define o peso da fonte do título do popup. |
