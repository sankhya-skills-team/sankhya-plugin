> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-text-area/ (snapshot 2026-09-28)

# Classic Text Area

O **Classic Text Area** é um componente de entrada de texto multilinha versátil que oferece diversas opções de customização, incluindo ícones, redimensionamento automático e estados visuais.

### Exemplo formulário

#### Dados do Formulário

```
{
  "description": "",
  "comments": "",
  "feedback": ""
}
```

#### Log de Eventos

```jsx
import React, { useState, useRef } from 'react';
import { EzClassicTextArea, EzButton } from '@sankhyalabs/ezui/react/components';
import "./demo.css";

const Demo = () => {
    const [formData, setFormData] = useState({
        description: '',
        comments: '',
        feedback: ''
    });
    const [formErrors, setFormErrors] = useState({});
    const [logs, setLogs] = useState([]);

    const descriptionRef = useRef();

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
            case 'description':
                if (!value || !value.trim()) {
                    error = 'Descrição é obrigatória';
                } else if (value.length < 10) {
                    error = 'Descrição deve ter ao menos 10 caracteres';
                }
                break;
            case 'comments':
                if (value && value.length > 500) {
                    error = 'Comentário não pode exceder 500 caracteres';
                }
                break;
        }

        return error;
    };

    const handleBlur = (field, value) => {
        const error = validateField(field, value);
        setFormErrors(prev => ({ ...prev, [field]: error }));
        addLog(`Campo ${field} perdeu o foco`);
    };

    const handleSubmit = () => {
        const errors = {};
        Object.keys(formData).forEach(field => {
            if (field !== 'feedback') { // feedback não é obrigatório
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
            description: '',
            comments: '',
            feedback: ''
        });
        setFormErrors({});
        setLogs([]);
        addLog('Formulário resetado');
    };

    const focusDescription = () => {
        descriptionRef.current?.setFocus();
        addLog('Foco definido no campo descrição');
    };

    return (
        <div className="ez-classic-input-demo_container">
            <h3>Exemplo formulário</h3>
            <form>
                {/* Descrição com validação e altura automática */}
                <EzClassicTextArea
                    ref={descriptionRef}
                    label="Descrição *"
                    placeholder="Digite uma descrição detalhada..."
                    value={formData.description}
                    state={formErrors.description ? 'error' : formData.description ? 'success' : 'default'}
                    errorText={formErrors.description}
                    onEzChange={(evt) => handleInputChange('description', evt.detail)}
                    onEzBlur={(evt) => handleBlur('description', evt.detail)}
                    helpText={formErrors.description || "Descrição obrigatória (mínimo 10 caracteres)"}
                />

                {/* Comentários com contador de caracteres */}
                <EzClassicTextArea
                    label="Comentários"
                    placeholder="Adicione seus comentários..."
                    value={formData.comments}
                    resize="vertical"
                    state={formErrors.comments ? 'error' : 'default'}
                    errorText={formErrors.comments}
                    onEzChange={(evt) => handleInputChange('comments', evt.detail)}
                    onEzBlur={(evt) => handleBlur('comments', evt.detail)}
                    helpText={formErrors.comments || `${formData.comments.length}/500 caracteres`}
                />

                {/* Feedback com ícone */}
                <EzClassicTextArea
                    label="Feedback"
                    placeholder="Deixe seu feedback..."
                    value={formData.feedback}
                    iconLeftName="message"
                    resize="both"
                    onEzChange={(evt) => handleInputChange('feedback', evt.detail)}
                    helpText="Campo opcional para feedback"
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
                        onClick={focusDescription}
                        label="Focar na Descrição"
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

O Classic Text Area suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

demo.js

```jsx
import React from 'react';
import { EzClassicTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-row">
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicTextArea
                    label="Estado padrão"
                    placeholder="Digite seu texto aqui..."
                    state="default"
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicTextArea
                    label="Estado de sucesso"
                    placeholder="Success"
                    state="success"
                    value="Dados válidos inseridos"
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicTextArea
                    label="Estado de erro"
                    placeholder="Error"
                    state="error"
                    value="Dados inválidos inseridos"
                    helpText="Este campo contém erros"
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicTextArea
                    label="Estado de aviso"
                    placeholder="Warning"
                    state="warning"
                    value="Atenção necessária neste texto"
                    helpText="Verifique este campo"
                />
            </div>
        </div>
    );
};

export default Demo;
```

### Ícones

É possível adicionar ícones à esquerda e/ou direita do textarea, com opção de torná-los clicáveis.

### Redimensionamento

O componente oferece suporte a diferentes modos de redimensionamento (vertical, horizontal, ambos ou nenhum).

```jsx
import React from 'react';
import { EzClassicTextArea } from '@sankhyalabs/ezui/react/components';
import './resize.css';

const Demo = () => {
    return (
        <div className="ez-classic-input-resize_container">
            <EzClassicTextArea
                label="Redimensionamento vertical"
                placeholder="Arraste a alça inferior para redimensionar apenas verticalmente..."
                resize="vertical"
                helpText="Resize: vertical - apenas altura pode ser alterada"
            />
            <EzClassicTextArea
                label="Redimensionamento horizontal"
                placeholder="Arraste a alça lateral para redimensionar apenas horizontalmente..."
                resize="horizontal"
                helpText="Resize: horizontal - apenas largura pode ser alterada"
            />
            <EzClassicTextArea
                label="Redimensionamento livre"
                placeholder="Arraste a alça do canto para redimensionar em ambas as direções..."
                resize="both"
                helpText="Resize: both - altura e largura podem ser alteradas"
            />
            <EzClassicTextArea
                label="Sem redimensionamento"
                placeholder="Este campo tem tamanho fixo e não pode ser redimensionado..."
                resize="none"
                helpText="Resize: none - tamanho fixo"
            />
        </div>
    );
};

export default Demo;
```

### Estados de Interação

Controle sobre estados desabilitado e somente leitura.

## Eventos

### Evento ezChange

Disparado sempre que o valor do textarea é alterado.

**Eventos ezChange:**

_Nenhum evento ainda_

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [value, setValue] = useState('');

    const handleChange = (event) => {
        const newValue = event.detail;
        setValue(newValue);
    };

    return (
        <div>
            <div className="ez-col--sd-6">
                <EzClassicTextArea
                    label="Digite algo para ver os eventos"
                    placeholder="Comece a digitar..."
                    value={value}
                    onEzChange={handleChange}
                    helpText="O evento ezChange é disparado a cada alteração"
                />
            </div>

            <div className="ez-margin-top--large">
                <strong>Eventos ezChange:</strong>
                <div className="ez-box ez-margin-top--small">
                    {!value ? (
                        <em>Nenhum evento ainda</em>
                    ) : (
                        <pre>{value}</pre>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Demo;
```

### Evento ezBlur

Disparado quando o textarea perde o foco.

**Estatísticas do evento ezBlur:**

Quantidade de vezes que perdeu o foco: **0**

### Evento iconClick

Disparado quando um ícone clicável é clicado.

**Histórico de cliques nos ícones:**

_Nenhum clique ainda_

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicTextArea } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [clickHistory, setClickHistory] = useState([]);

    const handleIconClick = (event) => {
        const { position } = event.detail;
        const timestamp = new Date().toLocaleTimeString();
        const newClick = `${timestamp}: Ícone ${position === 'left' ? 'esquerdo' : 'direito'} clicado`;

        setClickHistory(prev => [...prev.slice(-4), newClick]);
    };

    return (
        <div>
            <div className="ez-row">
                <div className="ez-col--sd-6 ez-padding--medium">
                    <EzClassicTextArea
                        label="Campo com ícones clicáveis"
                        placeholder="Clique nos ícones"
                        leftIconName="search"
                        rightIconName="settings"
                        leftIconClickable={true}
                        rightIconClickable={true}
                        onIconClick={handleIconClick}
                        helpText="Ambos os ícones são clicáveis"
                    />
                </div>
                <div className="ez-col--sd-6 ez-padding--medium">
                    <EzClassicTextArea
                        label="Campo com ícone não clicável"
                        placeholder="Ícone apenas decorativo"
                        leftIconName="help"
                        leftIconClickable={false}
                        helpText="Este ícone não é clicável"
                    />
                </div>
            </div>

            <div className="ez-margin-top--large">
                <strong>Histórico de cliques nos ícones:</strong>
                <div className="ez-box ez-margin-top--small">
                    {clickHistory.length === 0 ? (
                        <em>Nenhum clique ainda</em>
                    ) : (
                        clickHistory.map((click, index) => (
                            <div key={index} className="ez-margin-bottom--small">
                                {click}
                            </div>
                        ))
                    )}
                </div>
            </div>
        </div>
    );
};

export default Demo;
```

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

**Opções do setFocus:**

Selecionar texto ao focarPrevenir scroll ao focar

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| enabled | enabled | Define se a textarea está habilitada | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido | string | undefined |
| helpText | help-text | Texto de ajuda exibido abaixo da textarea | string | undefined |
| label | label | Texto do rótulo exibido acima da área de texto | string | '' |
| leftIconClickable | left-icon-clickable | Define se o ícone da esquerda é clicável | boolean | false |
| leftIconName | left-icon-name | Nome do ícone à esquerda | string | undefined |
| leftIconTooltip | left-icon-tooltip | Título do ícone à esquerda (tooltip) | string | undefined |
| maxlength | maxlength | Número máximo de caracteres permitidos | number | undefined |
| name | name | Nome da textarea | string | StringUtils.generateUUID() |
| placeholder | placeholder | Texto de placeholder exibido quando a área de texto está vazia | string | '' |
| readonly | readonly | Se a área de texto é somente leitura | boolean | false |
| resize | resize | Comportamento de redimensionamento da área de texto | "both" \| "horizontal" \| "none" \| "vertical" | 'vertical' |
| rightIconClickable | right-icon-clickable | Define se o ícone da direita é clicável | boolean | false |
| rightIconName | right-icon-name | Nome do ícone à direita | string | undefined |
| rightIconTooltip | right-icon-tooltip | Título do ícone à direita (tooltip) | string | undefined |
| rows | rows | Define o número de linhas da área de texto | number | 5 |
| state | state | Estado visual da textarea: default, error, success ou warning | "default" \| "error" \| "success" \| "warning" | "default" |
| value | value | Valor atual da área de texto | string | '' |

### Events

| Event | Description | Type |
|---|---|---|
| ezBlur | Evento emitido quando a área de texto perde foco | CustomEvent<string> |
| ezChange | Evento emitido quando o valor da área de texto muda | CustomEvent<string> |
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

  * ez-form-view

#### Depends on

  * ez-icon
