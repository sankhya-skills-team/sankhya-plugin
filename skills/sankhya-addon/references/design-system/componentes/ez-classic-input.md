> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-input/ (snapshot 2026-09-28)

# Classic Input

O **Classic Input** é um componente de entrada de texto versátil que oferece diversas opções de customização, incluindo ícones, máscaras e estados visuais.

### Exemplo formulário

#### Dados do Formulário

```
{
  "name": "",
  "email": "",
  "phone": "",
  "password": "",
  "search": ""
}
```

#### Log de Eventos

demo.js

```jsx
import React, { useState, useRef } from 'react';
import { EzClassicInput, EzButton } from '@sankhyalabs/ezui/react/components';
import "./styles.css";

const Demo = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        password: '',
        search: ''
    });
    const [formErrors, setFormErrors] = useState({});
    const [showPassword, setShowPassword] = useState(false);
    const [logs, setLogs] = useState([]);

    const nameInputRef = useRef();
    const searchInputRef = useRef();

    const addLog = (message) => {
        setLogs(prev => [...prev.slice(-4), `${new Date().toLocaleTimeString()}: ${message}`]);
    };

    const handleInputChange = (field, value) => {
        setFormData(prev => ({ ...prev, [field]: value }));

        if (formErrors[field]) {
            setFormErrors(prev => ({ ...prev, [field]: '' }));
        }

        addLog(`Campo ${field} alterado: ${value}`);
    };

    const validateField = (field, value) => {
        let error = '';

        switch (field) {
            case 'name':
                if (!value || !value.trim()) {
                    error = 'Nome é obrigatório';
                } else if (value.length < 2) {
                    error = 'Nome deve ter ao menos 2 caracteres';
                }
                break;
            case 'email':
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!value || !value.trim()) {
                    error = 'Email é obrigatório';
                } else if (!emailRegex.test(value)) {
                    error = 'Email inválido';
                }
                break;
            case 'phone':
                if (value && value.replace(/\D/g, '').length < 10) {
                    error = 'Telefone deve ter ao menos 10 dígitos';
                }
                break;
            case 'password':
                if (!value) {
                    error = 'Senha é obrigatória';
                } else if (value.length < 6) {
                    error = 'Senha deve ter ao menos 6 caracteres';
                }
                break;
        }

        return error;
    };

    const handleBlur = (field, value) => {
        const error = validateField(field, value);
        if (error) {
            setFormErrors(prev => ({ ...prev, [field]: error }));
        }
        addLog(`Campo ${field} perdeu o foco`);
    };

    const handleSubmit = () => {
        const errors = {};
        Object.keys(formData).forEach(field => {
            if (field !== 'search') { // search não é obrigatório
                const error = validateField(field, formData[field]);
                if (error) errors[field] = error;
            }
        });

        setFormErrors(errors);

        if (Object.keys(errors).length === 0) {
            addLog('Formulário enviado com sucesso!');
            alert('Formulário enviado com sucesso!');
        } else {
            addLog('Erro na validação do formulário');
        }
    };

    const handleReset = () => {
        setFormData({
            name: '',
            email: '',
            phone: '',
            password: '',
            search: ''
        });
        setFormErrors({});
        setLogs([]);
        addLog('Formulário resetado');
    };

    const clearSearch = () => {
        setFormData(prev => ({ ...prev, search: '' }));
        searchInputRef.current?.setFocus();
        addLog('Campo de busca limpo');
    };

    const focusName = () => {
        nameInputRef.current?.setFocus();
        addLog('Foco definido no campo nome');
    };

    return (
        <div className="ez-classic-input-demo_container">
            <h3>Exemplo formulário</h3>
            <form>
                {/* Campo de busca com ícone e ação */}
                <EzClassicInput
                    ref={searchInputRef}
                    label="Buscar"
                    placeholder="Digite para buscar..."
                    value={formData.search}
                    leftIconName="search"
                    rightIconName={formData.search ? "close" : null}
                    rightIconClickable={!!formData.search}
                    onEzChange={(evt) => handleInputChange('search', evt.detail)}
                    onIconClick={(evt) => {
                        if (evt.detail.icon === 'right') {
                            clearSearch();
                        }
                    }}
                    helpText="Campo de busca com ícone funcional"
                />

                {/* Nome com validação */}
                <EzClassicInput
                    ref={nameInputRef}
                    label="Nome completo *"
                    placeholder="Digite seu nome completo"
                    value={formData.name}
                    state={formErrors.name ? 'error' : formData.name ? 'success' : 'default'}
                    errorText={formErrors.name}
                    onEzChange={(evt) => handleInputChange('name', evt.detail)}
                    onEzBlur={(evt) => handleBlur('name', evt.detail)}
                    helpText={formErrors.name || "Nome completo obrigatório"}
                />

                {/* Email com validação */}
                <EzClassicInput
                    label="Email *"
                    type="email"
                    placeholder="seu@email.com"
                    value={formData.email}
                    leftIconName="email"
                    state={formErrors.email ? 'error' : formData.email ? 'success' : 'default'}
                    errorText={formErrors.email}
                    onEzChange={(evt) => handleInputChange('email', evt.detail)}
                    onEzBlur={(evt) => handleBlur('email', evt.detail)}
                    helpText={formErrors.email || "Email válido obrigatório"}
                />

                {/* Telefone com máscara */}
                <EzClassicInput
                    label="Telefone"
                    placeholder="(00) 00000-0000"
                    value={formData.phone}
                    mask="(##) #####-####"
                    leftIconName="phone"
                    state={formErrors.phone ? 'error' : 'default'}
                    errorText={formErrors.phone}
                    onEzChange={(evt) => handleInputChange('phone', evt.detail)}
                    onEzBlur={(evt) => handleBlur('phone', evt.detail)}
                    helpText={formErrors.phone || "Telefone com máscara automática"}
                />

                {/* Senha com toggle de visibilidade */}
                <EzClassicInput
                    label="Senha *"
                    type={showPassword ? "text" : "password"}
                    placeholder="Digite sua senha"
                    value={formData.password}
                    rightIconName={showPassword ? "eye-off" : "eye"}
                    rightIconClickable={true}
                    state={formErrors.password ? 'error' : formData.password ? 'success' : 'default'}
                    errorText={formErrors.password}
                    onEzChange={(evt) => handleInputChange('password', evt.detail)}
                    onEzBlur={(evt) => handleBlur('password', evt.detail)}
                    onIconClick={(evt) => {
                        if (evt.detail.icon === 'right') {
                            setShowPassword(!showPassword);
                            addLog(`Visibilidade da senha ${showPassword ? 'ocultada' : 'exibida'}`);
                        }
                    }}
                    helpText={formErrors.password || "Mínimo 6 caracteres"}
                />

                <section>
                    <EzButton
                        type="submit"
                        className="ez-button--primary"
                        label="Enviar Formulário"
                        onClick={() => handleSubmit()}
                    />
                    <EzButton
                        type="button"
                        onClick={handleReset}
                        label="Limpar"
                    />
                    <EzButton
                        type="button"
                        className="ez-button--tertiary"
                        onClick={focusName}
                        label="Focar no Nome"
                    />
                </section>
            </form>

            <h4>Dados do Formulário</h4>
            <pre>
                {JSON.stringify(formData, null, 2)}
            </pre>

            <h4>Log de Eventos</h4>
            <div>
                {logs.map((log, index) => (
                    <div key={index}>
                        {log}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Demo;
```

## Variações

### Estados Visuais

O Classic Input suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

### Ícones

É possível adicionar ícones à esquerda e/ou direita do input, com opção de torná-los clicáveis.

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [showPassword, setShowPassword] = useState(false);
    const [searchValue, setSearchValue] = useState('');

    const handleIconClick = (event) => {
        if (event.detail.icon === 'right') {
            setShowPassword(!showPassword);
        }
    };

    return (
        <div className="ez-row">
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="Campo com ícone à esquerda"
                    placeholder="Digite para buscar"
                    leftIconName="search"
                    leftIconTooltip="Buscar"
                    value={searchValue}
                    onEzChange={(evt) => setSearchValue(evt.detail)}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="Senha com ícone clicável"
                    placeholder="Digite sua senha"
                    type={showPassword ? "text" : "password"}
                    rightIconName={showPassword ? "eye-off" : "eye"}
                    rightIconClickable={true}
                    rightIconTooltip={showPassword ? "Ocultar senha" : "Mostrar senha"}
                    onIconClick={handleIconClick}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="E-mail com ambos os ícones"
                    placeholder="email@exemplo.com"
                    type="email"
                    leftIconName="email"
                    rightIconName="check-circle"
                    leftIconTooltip="E-mail"
                    rightIconTooltip="Válido"
                    state="success"
                />
            </div>
        </div>
    );
};

export default Demo;
```

### Máscaras

O componente oferece suporte a máscaras para formatação automática dos dados inseridos.

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [cpf, setCpf] = useState('');
    const [phone, setPhone] = useState('');
    const [cep, setCep] = useState('');

    return (
        <div className="ez-row">
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="CPF"
                    mask="###.###.###-##"
                    value={cpf}
                    onEzChange={(evt) => setCpf(evt.detail)}
                    helpText={`Valor sem máscara: ${cpf}`}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="Telefone"
                    mask="(##) #####-####"
                    value={phone}
                    onEzChange={(evt) => setPhone(evt.detail)}
                    helpText={`Valor sem máscara: ${phone}`}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="CEP"
                    mask="#####-###"
                    value={cep}
                    onEzChange={(evt) => setCep(evt.detail)}
                    helpText={`Valor sem máscara: ${cep}`}
                />
            </div>
        </div>
    );
};

export default Demo;
```

### Tipos de Input

Suporte a diferentes tipos de input HTML para validação e comportamento específicos. A propriedade `type` aceita todos os tipos nativos do elemento HTML `<input>` (text, email, password, number, tel, url, search, etc.).

### Estados de Interação

Controle sobre estados desabilitado e somente leitura.

demo.js

```jsx
import React from 'react';
import { EzClassicInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="Campo habilitado"
                    placeholder="Digite aqui"
                    enabled={true}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="Campo desabilitado"
                    placeholder="Campo desabilitado"
                    value="Não é possível editar"
                    enabled={false}
                />
            </div>
            <div className="ez-col--sd-4 ez-padding--medium">
                <EzClassicInput
                    label="Campo somente leitura"
                    value="Somente leitura"
                    readonly={true}
                    helpText="Este campo é apenas para visualização"
                />
            </div>
        </div>
    );
};

export default Demo;
```

## Eventos

### Evento ezChange

Disparado sempre que o valor do input é alterado.

**Eventos ezChange:**

_Nenhum evento ainda_

### Evento ezBlur

Disparado quando o input perde o foco.

**Estatísticas do evento ezBlur:**

Quantidade de vezes que perdeu o foco: **0**

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicInput } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [blurCount, setBlurCount] = useState(0);
    const [lastBlurTime, setLastBlurTime] = useState('');

    const handleBlur = () => {
        setBlurCount(prev => prev + 1);
        setLastBlurTime(new Date().toLocaleTimeString());
    };

    return (
        <div>
            <div className="ez-row">
                <div className="ez-col--sd-6 ez-padding--medium">
                    <EzClassicInput
                        label="Clique aqui e depois fora para disparar ezBlur"
                        placeholder="Foque e depois clique fora"
                        onEzBlur={handleBlur}
                        helpText="O evento ezBlur é disparado quando o campo perde o foco"
                    />
                </div>
                <div className="ez-col--sd-6 ez-padding--medium">
                    <EzClassicInput
                        label="Outro campo para testar"
                        placeholder="Clique aqui para tirar o foco do primeiro"
                        helpText="Este campo não dispara ezBlur"
                    />
                </div>
            </div>

            <div className="ez-margin-top--large">
                <div className="ez-flex ez-flex--column ez-align-items--center">
                    <strong>Estatísticas do evento ezBlur:</strong>
                    <div className="ez-margin-top--small">
                        Quantidade de vezes que perdeu o foco: <strong>{blurCount}</strong>
                    </div>
                    {lastBlurTime && (
                        <div>
                            Último blur em: <strong>{lastBlurTime}</strong>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Demo;
```

### Evento iconClick

Disparado quando um ícone clicável é clicado.

**Histórico de cliques nos ícones:**

_Nenhum clique ainda_

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

**Opções do setFocus:**

Selecionar texto ao focarPrevenir scroll ao focar

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| emitMaskedValue | emit-masked-value | Define se o valor emitido pelo evento ezChange deve conter a máscara aplicada (padrão: false) | boolean | false |
| enabled | enabled | Define se o input está habilitado | boolean | true |
| errorMessage | error-message | Texto de erro exibido abaixo do input | string | undefined |
| helpText | help-text | Texto de ajuda exibido abaixo do input | string | undefined |
| label | label | Texto do label exibido acima do input | string | undefined |
| leftIconClickable | left-icon-clickable | Define se o ícone da esquerda é clicável | boolean | false |
| leftIconName | left-icon-name | Nome do ícone à esquerda | string | undefined |
| leftIconTooltip | left-icon-tooltip | Título do ícone à esquerda (tooltip) | string | undefined |
| mask | mask | Aplica uma máscara no conteúdo conforme o padrão estabelecido.  Para mais informações acesse: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/maskformatter/ | string | undefined |
| maxlength | maxlength | Tamanho máximo do valor | number | undefined |
| minlength | minlength | Tamanho mínimo do valor | number | undefined |
| name | name | Nome do input | string | undefined |
| placeholder | placeholder | Placeholder do input | string | undefined |
| readonly | readonly | Define se o input é somente leitura | boolean | false |
| required | required | Define se o input é obrigatório (visualmente) | boolean | false |
| rightIconClickable | right-icon-clickable | Define se o ícone da direita é clicável | boolean | false |
| rightIconName | right-icon-name | Nome do ícone à direita | string | undefined |
| rightIconTooltip | right-icon-tooltip | Título do ícone à direita (tooltip) | string | undefined |
| size | size | Tamanho do input | "default" \| "small" \| "xsmall" | "default" |
| state | state | Estado visual do input: default, error, success ou warning | "default" \| "error" \| "success" \| "warning" | "default" |
| type | type | Tipo do input (ex: text, password, email, etc) | string | 'text' |
| value | value | Valor do input | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezBlur | Evento disparado quando o input perde o foco. | CustomEvent<string> |
| ezChange | Evento disparado quando o valor do input muda. | CustomEvent<string> |
| ezFocus | Evento disparado quando o input ganha o foco. | CustomEvent<string> |
| iconClick | Evento disparado quando um ícone é clicado. Payload: { icon: "left" \| "right" } | CustomEvent<{ icon: "left" \| "right"; }> |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus(option?: OptionsSetFocus) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-classic-combo-box
  * ez-classic-date-input
  * ez-classic-date-time-input
  * ez-classic-number-input
  * ez-classic-search
  * ez-classic-search-plus
  * ez-classic-time-input
  * ez-form-view

#### Depends on

  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-classic-input--label-color | Define a cor do texto do input. |
| --ez-classic-input--border-color-default | Define a cor da borda do input quando está no estado padrão. |
| --ez-classic-input--border-color-focus | Define a cor da borda do input quando está no estado de foco. |
| --ez-classic-input--border-color-success | Define a cor da borda do input quando está no estado de sucesso. |
| --ez-classic-input--border-color-error | Define a cor da borda do input quando está no estado de erro. |
| --ez-classic-input--border-color-warning | Define a cor da borda do input quando está no estado de aviso. |
| --ez-classic-input--background-color | Define a cor de fundo do input. |
| --ez-classic-input--background-color-disabled | Define a cor de fundo do input quando está desabilitado. |
| --ez-classic-input--text-color | Define a cor do texto do input. |
| --ez-classic-input--placeholder-color | Define a cor do texto do placeholder do input. |
| --ez-classic-input--icon-color | Define a cor do ícone do input. |
| --ez-classic-input--helptext-color | Define a cor do texto de ajuda do input. |
| --ez-classic-input--height | Define a altura do input. |
| --ez-classic-input--height-small | Define a altura do input. |
| --ez-classic-input--height-xsmall | Define a altura do input. |
| --ez-classic-input--gap | Define o gap entre elementos internos do input. |
| --ez-classic-input--padding-inline | Define o padding horizontal do input. |
