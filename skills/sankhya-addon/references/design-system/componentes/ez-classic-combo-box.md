> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-combo-box/ (snapshot 2026-09-28)

# Classic Combo Box

O **Classic Combo Box** é um componente de seleção que permite aos usuários escolher uma ou mais opções de uma lista suspensa. Oferece funcionalidades como busca, ícones personalizáveis, diferentes estados visuais e slots customizáveis para renderização personalizada das opções.

### Perfil do Desenvolvedor

#### Dados do Perfil

```
{
  "country": null,
  "state": null,
  "city": null,
  "technology": null,
  "experience": null,
  "framework": null
}
```

#### Log de Eventos

```jsx
import React, { useState, useRef } from 'react';
import { EzClassicComboBox, EzButton } from '@sankhyalabs/ezui/react/components';
import "./demo.css";

const Demo = () => {
    const [formData, setFormData] = useState({
        country: null,
        state: null,
        city: null,
        technology: null,
        experience: null,
        framework: null
    });
    const [formErrors, setFormErrors] = useState({});
    const [logs, setLogs] = useState([]);

    const countryComboRef = useRef();
    const technologyComboRef = useRef();

    // Dados das opções
    const countries = [
        { value: 'br', label: 'Brasil' },
        { value: 'us', label: 'Estados Unidos' },
        { value: 'ca', label: 'Canadá' },
        { value: 'mx', label: 'México' },
        { value: 'ar', label: 'Argentina' }
    ];

    const states = {
        br: [
            { value: 'sp', label: 'São Paulo' },
            { value: 'rj', label: 'Rio de Janeiro' },
            { value: 'mg', label: 'Minas Gerais' },
            { value: 'rs', label: 'Rio Grande do Sul' }
        ],
        us: [
            { value: 'ca', label: 'California' },
            { value: 'ny', label: 'New York' },
            { value: 'tx', label: 'Texas' },
            { value: 'fl', label: 'Florida' }
        ]
    };

    const cities = {
        sp: [
            { value: 'sao-paulo', label: 'São Paulo' },
            { value: 'campinas', label: 'Campinas' },
            { value: 'santos', label: 'Santos' }
        ],
        rj: [
            { value: 'rio-janeiro', label: 'Rio de Janeiro' },
            { value: 'niteroi', label: 'Niterói' },
            { value: 'petropolis', label: 'Petrópolis' }
        ]
    };

    const technologies = [
        { value: 'javascript', label: 'JavaScript' },
        { value: 'python', label: 'Python' },
        { value: 'java', label: 'Java' },
        { value: 'csharp', label: 'C#' },
        { value: 'php', label: 'PHP' },
        { value: 'ruby', label: 'Ruby' },
        { value: 'go', label: 'Go' },
        { value: 'rust', label: 'Rust' }
    ];

    const experienceLevels = [
        { value: 'junior', label: 'Junior (0-2 anos)' },
        { value: 'pleno', label: 'Pleno (2-5 anos)' },
        { value: 'senior', label: 'Senior (5+ anos)' },
        { value: 'lead', label: 'Tech Lead' },
        { value: 'architect', label: 'Arquiteto' }
    ];

    const frameworks = {
        javascript: [
            { value: 'react', label: 'React' },
            { value: 'vue', label: 'Vue.js' },
            { value: 'angular', label: 'Angular' },
            { value: 'svelte', label: 'Svelte' }
        ],
        python: [
            { value: 'django', label: 'Django' },
            { value: 'flask', label: 'Flask' },
            { value: 'fastapi', label: 'FastAPI' }
        ],
        java: [
            { value: 'spring', label: 'Spring' },
            { value: 'quarkus', label: 'Quarkus' },
            { value: 'micronaut', label: 'Micronaut' }
        ]
    };

    const addLog = (message) => {
        setLogs(prev => [`${new Date().toLocaleTimeString()}: ${message}`, ...prev.slice(-4)]);
    };

    const handleComboChange = (field, value) => {
        setFormData(prev => {
            const newData = { ...prev, [field]: value };

            // Reset campos dependentes
            if (field === 'country') {
                newData.state = null;
                newData.city = null;
            } else if (field === 'state') {
                newData.city = null;
            } else if (field === 'technology') {
                newData.framework = null;
            }

            return newData;
        });

        // Limpar erro se existir
        if (formErrors[field]) {
            setFormErrors(prev => ({ ...prev, [field]: '' }));
        }

        addLog(`Campo ${field} alterado: ${JSON.stringify(value, null, 2)}`);
    };

    const validateField = (field, value) => {
        let error = '';

        switch (field) {
            case 'country':
                if (!value) error = 'País é obrigatório';
                break;
            case 'state':
                if (formData.country && !value) error = 'Estado é obrigatório';
                break;
            case 'technology':
                if (!value) error = 'Tecnologia é obrigatória';
                break;
            case 'experience':
                if (!value) error = 'Nível de experiência é obrigatório';
                break;
        }

        return error;
    };

    const handleComboBlur = (field, value) => {
        const error = validateField(field, value);
        if (error) {
            setFormErrors(prev => ({ ...prev, [field]: error }));
        }
        addLog(`Campo ${field} perdeu o foco`);
    };

    const handleIconClick = (field) => {
       if (field === 'technology') {
            addLog('Ícone de ajuda da tecnologia clicado');
            alert('Selecione a tecnologia principal que você utiliza no desenvolvimento.');
        }
    };

    const handleSubmit = () => {
        const errors = {};
        const requiredFields = ['country', 'technology', 'experience'];

        if (formData.country) {
            requiredFields.push('state');
        }

        requiredFields.forEach(field => {
            const error = validateField(field, formData[field]);
            if (error) errors[field] = error;
        });

        setFormErrors(errors);

        if (Object.keys(errors).length === 0) {
            addLog('Formulário enviado com sucesso!');
            alert('Perfil de desenvolvedor criado com sucesso!');
        } else {
            addLog('Erro na validação do formulário');
        }
    };

    const handleReset = () => {
        setFormData({
            country: null,
            state: null,
            city: null,
            technology: null,
            experience: null,
            framework: null
        });
        setFormErrors({});
        setLogs([]);
        addLog('Formulário resetado');
    };

    const focusCountry = () => {
        countryComboRef.current?.setFocus();
        addLog('Foco definido no campo país');
    };

    const openTechnology = () => {
        technologyComboRef.current?.showPopover();
        addLog('Combo de tecnologia aberto programaticamente');
    };

    return (
        <div className="ez-classic-combo-box-demo_container">
            <h3>Perfil do Desenvolvedor</h3>
            <form>
                {/* País com ícone para abrir/fechar */}
                <EzClassicComboBox
                    ref={countryComboRef}
                    label="País *"
                    placeholder="Selecione seu país"
                    options={countries}
                    value={formData.country}
                    iconName="globe"
                    state={formErrors.country ? 'error' : formData.country ? 'success' : 'default'}
                    onEzChange={(evt) => handleComboChange('country', evt.detail)}
                    onEzBlur={(evt) => handleComboBlur('country', evt.detail)}
                    onIconClick={() => handleIconClick('country')}
                    helpText={formErrors.country || "Selecione o país onde você reside"}
                />

                {/* Estado (habilitado apenas se país estiver selecionado) */}
                <EzClassicComboBox
                    label="Estado"
                    placeholder="Selecione seu estado"
                    options={formData.country ? states[formData.country.value] || [] : []}
                    value={formData.state}
                    enabled={!!formData.country}
                    iconName="map-pin"
                    state={formErrors.state ? 'error' : formData.state ? 'success' : 'default'}
                    onEzChange={(evt) => handleComboChange('state', evt.detail)}
                    onEzBlur={(evt) => handleComboBlur('state', evt.detail)}
                    helpText={formErrors.state || (formData.country ? "Selecione seu estado" : "Primeiro selecione um país")}
                />

                {/* Cidade (habilitado apenas se estado estiver selecionado) */}
                <EzClassicComboBox
                    label="Cidade"
                    placeholder="Selecione sua cidade"
                    options={formData.state ? cities[formData.state.value] || [] : []}
                    value={formData.city}
                    enabled={!!formData.state}
                    iconName="building"
                    state={formData.city ? 'success' : 'default'}
                    onEzChange={(evt) => handleComboChange('city', evt.detail)}
                    helpText={formData.state ? "Selecione sua cidade" : "Primeiro selecione um estado"}
                />

                {/* Tecnologia com busca e ícone de ajuda */}
                <EzClassicComboBox
                    ref={technologyComboRef}
                    label="Tecnologia Principal *"
                    placeholder="Digite ou selecione uma tecnologia"
                    options={technologies}
                    value={formData.technology}
                    iconName="help-inverted"
                    iconClickable={true}
                    state={formErrors.technology ? 'error' : formData.technology ? 'success' : 'default'}
                    onEzChange={(evt) => handleComboChange('technology', evt.detail)}
                    onEzBlur={(evt) => handleComboBlur('technology', evt.detail)}
                    onIconClick={() => handleIconClick('technology')}
                    helpText={formErrors.technology || "Tecnologia que você mais utiliza"}
                />

                {/* Nível de experiência */}
                <EzClassicComboBox
                    label="Nível de Experiência *"
                    placeholder="Selecione seu nível"
                    options={experienceLevels}
                    value={formData.experience}
                    iconName="trending-up"
                    state={formErrors.experience ? 'error' : formData.experience ? 'success' : 'default'}
                    onEzChange={(evt) => handleComboChange('experience', evt.detail)}
                    onEzBlur={(evt) => handleComboBlur('experience', evt.detail)}
                    helpText={formErrors.experience || "Seu nível atual de experiência"}
                />

                {/* Framework (habilitado se tecnologia estiver selecionada) */}
                <EzClassicComboBox
                    label="Framework Favorito"
                    placeholder="Selecione um framework"
                    options={formData.technology ? frameworks[formData.technology.value] || [] : []}
                    value={formData.framework}
                    enabled={!!formData.technology && !!frameworks[formData.technology.value]}
                    iconName="layers"
                    state={formData.framework ? 'success' : 'default'}
                    onEzChange={(evt) => handleComboChange('framework', evt.detail)}
                    helpText={
                        formData.technology
                            ? frameworks[formData.technology.value]
                                ? "Framework que você prefere usar"
                                : "Nenhum framework disponível para esta tecnologia"
                            : "Primeiro selecione uma tecnologia"
                    }
                />

                <section>
                    <EzButton
                        type="submit"
                        className="ez-button--primary"
                        label="Criar Perfil"
                        onClick={handleSubmit}
                    />
                    <EzButton
                        type="button"
                        onClick={handleReset}
                        label="Limpar"
                    />
                    <EzButton
                        type="button"
                        className="ez-button--tertiary"
                        onClick={focusCountry}
                        label="Focar no País"
                    />
                    <EzButton
                        type="button"
                        className="ez-button--tertiary"
                        onClick={openTechnology}
                        label="Abrir Tecnologias"
                    />
                </section>
            </form>

            <h4>Dados do Perfil</h4>
            <pre>
                {JSON.stringify(formData, null, 2)}
            </pre>

            <h4>Log de Eventos</h4>
            <div className="logs-container">
                {logs.map((log, index) => (
                    <div key={index} className="log-entry">
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

O Classic Combo Box suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

demo.js

```jsx
import React from 'react';
import { EzClassicComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const options = [
        { value: 'option1', label: 'Opção 1' },
        { value: 'option2', label: 'Opção 2' },
        { value: 'option3', label: 'Opção 3' }
    ];

    return (
        <div className="ez-row">
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Estado padrão"
                    placeholder="Selecione uma opção"
                    options={options}
                    state="default"
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Estado de sucesso"
                    placeholder="Sucesso"
                    options={options}
                    state="success"
                    value={{ value: 'option1', label: 'Opção 1' }}
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Estado de erro"
                    placeholder="Erro"
                    options={options}
                    state="error"
                    value={{ value: 'option2', label: 'Opção 2' }}
                    helpText="Seleção inválida"
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Estado de aviso"
                    placeholder="Aviso"
                    options={options}
                    state="warning"
                    value={{ value: 'option3', label: 'Opção 3' }}
                    helpText="Verifique esta seleção"
                />
            </div>
        </div>
    );
};

export default Demo;
```

### Ícones

É possível adicionar ícones ao combo box para melhorar a experiência visual e funcional.

### Funcionalidade de Busca

O componente oferece suporte à funcionalidade de busca para filtrar opções dinamicamente.

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [selectedValue, setSelectedValue] = useState();

    const countries = [
        { value: 'af', label: 'Afeganistão' },
        { value: 'za', label: 'África do Sul' },
        { value: 'al', label: 'Albânia' },
        { value: 'de', label: 'Alemanha' },
        { value: 'ad', label: 'Andorra' },
        { value: 'ao', label: 'Angola' },
        { value: 'ar', label: 'Argentina' },
        { value: 'am', label: 'Armênia' },
        { value: 'au', label: 'Austrália' },
        { value: 'at', label: 'Áustria' },
        { value: 'br', label: 'Brasil' },
        { value: 'ca', label: 'Canadá' },
        { value: 'cl', label: 'Chile' },
        { value: 'cn', label: 'China' },
        { value: 'co', label: 'Colômbia' },
        { value: 'us', label: 'Estados Unidos' },
        { value: 'fr', label: 'França' },
        { value: 'jp', label: 'Japão' },
        { value: 'mx', label: 'México' },
        { value: 'pt', label: 'Portugal' }
    ];

    return (
        <div className="ez-row">
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Combo box pesquisável"
                    placeholder="Digite para buscar um país"
                    options={countries}
                    suppressSearch={false}
                    iconName="search"
                    value={selectedValue}
                    onEzChange={(evt) => setSelectedValue(evt.detail)}
                    helpText="Digite para filtrar as opções"
                />
            </div>
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Combo box não pesquisável"
                    placeholder="Selecione um país"
                    options={countries.slice(0, 5)}
                    suppressSearch={true}
                    iconName="globe"
                />
            </div>
        </div>
    );
};

export default Demo;
```

### Estados de Interação

Controle sobre estados desabilitado e somente leitura.

### Slots Customizados

O Classic Combo Box permite personalizar completamente a renderização das opções através de slots. Isso possibilita criar listas ricas com informações adicionais, imagens, ícones coloridos e layouts complexos.

Os slots customizados permitem:

  * **Informações do usuário** : Avatar, status online, função e contato
  * **Detalhes do produto** : Imagem, preço, categoria, avaliação e disponibilidade
  * **Status coloridos** : Ícones, descrições e cores específicas para cada estado
  * **Layouts complexos** : Múltiplas linhas de informação e elementos visuais

Atenção

Quando utilizar slots customizados, as funcionalidades de busca e navegação por teclado não estarão disponíveis. Para manter a usabilidade, é recomendado implementar uma lógica de busca personalizada se necessário, para isto explore o evento `ezType` para capturar as mudanças no input. Para navegação por teclado, poderá ser utilizado o utilitário `KeyboardManager` para gerenciar os eventos de teclado.

👩‍💻

Ana Silva

ana.silva@empresa.com

Desenvolvedora

Online

👨‍🎨

Carlos Santos

carlos.santos@empresa.com

Designer

Ausente

👩‍💼

Maria Costa

maria.costa@empresa.com

Gerente

Offline

👨‍💻

João Oliveira

joao.oliveira@empresa.com

Analista

Online

💻

Notebook Dell Inspiron

Informática

R$ 2.899,00

⭐⭐⭐⭐ 4.5✅ Em estoque

🖱️

Mouse Logitech MX

Periféricos

R$ 289,00

⭐⭐⭐⭐ 4.8❌ Fora de estoque

⌨️

Teclado Mecânico RGB

Periféricos

R$ 459,00

⭐⭐⭐⭐ 4.3✅ Em estoque

🖥️

Monitor 4K Samsung

Monitores

R$ 1.799,00

⭐⭐⭐⭐ 4.7✅ Em estoque

✅

Ativo

Item está ativo e funcionando normalmente

⏸️

Inativo

Item foi desativado temporariamente

⏳

Pendente

Aguardando aprovação ou processamento

❌

Erro

Item apresenta problemas que precisam ser resolvidos

#### Seleções Atuais:

**Usuário:** Nenhum usuário selecionado

**Produto:** Nenhum produto selecionado

**Status:** Nenhum status selecionado

## Eventos

### Evento ezChange

Disparado sempre que uma opção é selecionada ou desselecionada.

**Valor selecionado:** Nenhum

#### Log de eventos:

Nenhum evento ainda...

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [selectedValue, setSelectedValue] = useState();
    const [eventLog, setEventLog] = useState([]);

    const options = [
        { value: 'react', label: 'React' },
        { value: 'vue', label: 'Vue.js' },
        { value: 'angular', label: 'Angular' },
        { value: 'svelte', label: 'Svelte' }
    ];

    const handleChange = (event) => {
        const newValue = event.detail;
        setSelectedValue(newValue);

        const timestamp = new Date().toLocaleTimeString();
        setEventLog(prev => [
            `${timestamp} - ezChange: "${JSON.stringify(newValue, null, 2)}"`,
            ...prev.slice(0, 4)
        ]);
    };

    return (
        <div className="ez-flex ez-flex--column">
            <div className="ez-col--sd-6 ez-padding--medium">
                <EzClassicComboBox
                    label="Framework JavaScript"
                    placeholder="Selecione um framework"
                    options={options}
                    value={selectedValue}
                    onEzChange={handleChange}
                    iconName="code"
                />

                <div className='ez-margin-top--medium'>
                    <strong>Valor selecionado:</strong> {JSON.stringify(selectedValue, null, 2) || 'Nenhum'}
                </div>
            </div>

            <div className="ez-padding--medium">
                <h4>Log de eventos:</h4>
                <div className='logs-container'>
                    {eventLog.length === 0 ? (
                        <div>Nenhum evento ainda...</div>
                    ) : (
                        eventLog.map((log, index) => (
                            <div key={index}>{log}</div>
                        ))
                    )}
                </div>
            </div>
        </div>
    );
};

export default Demo;
```

### Evento ezBlur

Disparado quando o combo box perde o foco.

**Estatísticas do evento ezBlur:**

Quantidade de vezes que perdeu o foco: **0**

demo.js

```jsx
import React, { useState } from 'react';
import { EzClassicComboBox } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [blurCount, setBlurCount] = useState(0);
    const [lastBlurTime, setLastBlurTime] = useState('');

    const options = [
        { value: 'option1', label: 'Primeira opção' },
        { value: 'option2', label: 'Segunda opção' },
        { value: 'option3', label: 'Terceira opção' }
    ];

    const handleBlur = () => {
        setBlurCount(prev => prev + 1);
        setLastBlurTime(new Date().toLocaleTimeString());
    };

    return (
        <div>
            <div className="ez-row">
                <div className="ez-col--sd-6 ez-padding--medium">
                    <EzClassicComboBox
                        label="Clique aqui e depois fora para disparar ezBlur"
                        placeholder="Abra o combo e clique fora"
                        options={options}
                        onEzBlur={handleBlur}
                        helpText="O evento ezBlur é disparado quando o combo perde o foco"
                    />
                </div>
                <div className="ez-col--sd-6 ez-padding--medium">
                    <EzClassicComboBox
                        label="Outro combo para testar"
                        placeholder="Clique aqui para tirar o foco do primeiro"
                        options={options}
                        helpText="Este combo não dispara ezBlur"
                    />
                </div>
            </div>

            <div className="ez-margin-top--large">
                <div className="ez-flex ez-flex--column ez-align-items--center">
                    <strong>Estatísticas do evento ezBlur:</strong>
                    <section className='logs-container ez-margin-top--small'>
                        <div>
                            Quantidade de vezes que perdeu o foco: <strong>{blurCount}</strong>
                        </div>
                        {lastBlurTime && (
                            <div>
                                Último blur em: <strong>{lastBlurTime}</strong>
                            </div>
                        )}
                    </section>
                </div>
            </div>
        </div>
    );
};

export default Demo;
```

### Evento iconClick

Disparado quando um ícone clicável é clicado.

**Valor selecionado:** Nenhum

#### Log de eventos iconClick:

Nenhum evento ainda...

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

**Opções do setFocus:**

Selecionar texto ao focarPrevenir scroll ao focarDemonstrar setBlur automaticamente após 3 segundos

**💡 Demonstração:** Quando esta opção estiver marcada, o método `setBlur()`será chamado automaticamente 3 segundos após dar foco. Isso é apenas para exemplificar o uso do método.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzClassicComboBox, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const comboRef = useRef(null);
    const [focusOptions, setFocusOptions] = useState({
        selectText: false,
        preventScroll: false
    });
    const [autoBlurEnabled, setAutoBlurEnabled] = useState(true);
    const [blurTimer, setBlurTimer] = useState(null);

    const options = [
        { value: 'react', label: 'React' },
        { value: 'vue', label: 'Vue.js' },
        { value: 'angular', label: 'Angular' },
        { value: 'svelte', label: 'Svelte' },
        { value: 'ember', label: 'Ember.js' }
    ];

    const handleSetFocus = async () => {
        if (comboRef.current) {
            await comboRef.current.setFocus(focusOptions);

            if (autoBlurEnabled) {
                const timer = setTimeout(() => {
                    handleSetBlur();
                }, 3000);
                setBlurTimer(timer);
            }
        }
    };

    const handleSetBlur = async () => {
        if (comboRef.current) {
            await comboRef.current.setBlur();
        }

        if (blurTimer) {
            clearTimeout(blurTimer);
            setBlurTimer(null);
        }
    };

    useEffect(() => {
        return () => {
            if (blurTimer) {
                clearTimeout(blurTimer);
            }
        };
    }, [blurTimer]);

    return (
        <div>
            <div className="ez-col--sd-6">
                <EzClassicComboBox
                    ref={comboRef}
                    label="Combo para testar métodos"
                    placeholder="Use os botões para controlar o foco"
                    options={options}
                    helpText="Use os botões abaixo para controlar o foco"
                />
            </div>

            <div className="ez-margin-top--medium">
                <div className="ez-flex ez-flex--wrap ez-flex--align-center">
                    <EzButton
                        label="Dar Foco"
                        onClick={handleSetFocus}
                        className="ez-margin-right--medium ez-margin-bottom--small"
                    />
                    <EzButton
                        label="Remover Foco"
                        onClick={handleSetBlur}
                        variant="secondary"
                        className="ez-margin-bottom--small"
                    />
                </div>
            </div>

            <div className="ez-margin-top--medium">
                <strong>Opções do setFocus:</strong>
                <div className="ez-flex ez-flex--column ez-margin-top--small">
                    <label className="ez-margin-bottom--small">
                        <input
                            type="checkbox"
                            checked={focusOptions.selectText}
                            onChange={(e) => setFocusOptions(prev => ({
                                ...prev,
                                selectText: e.target.checked
                            }))}
                        />
                        <span className="ez-margin-left--small">Selecionar texto ao focar</span>
                    </label>
                    <label className="ez-margin-bottom--small">
                        <input
                            type="checkbox"
                            checked={focusOptions.preventScroll}
                            onChange={(e) => setFocusOptions(prev => ({
                                ...prev,
                                preventScroll: e.target.checked
                            }))}
                        />
                        <span className="ez-margin-left--small">Prevenir scroll ao focar</span>
                    </label>
                    <label>
                        <input
                            type="checkbox"
                            checked={autoBlurEnabled}
                            onChange={(e) => setAutoBlurEnabled(e.target.checked)}
                        />
                        <span className="ez-margin-left--small">
                            Demonstrar setBlur automaticamente após 3 segundos
                        </span>
                    </label>
                </div>

                {autoBlurEnabled && (
                    <div className="ez-margin-top--small ez-padding--small" style={{ backgroundColor: '#f0f9ff', border: '1px solid #0ea5e9', borderRadius: '4px' }}>
                        <small>
                            <strong>💡 Demonstração:</strong> Quando esta opção estiver marcada, o método <code>setBlur()</code>
                            será chamado automaticamente 3 segundos após dar foco. Isso é apenas para exemplificar o uso do método.
                        </small>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Demo;
```

### open e close

Métodos para abrir e fechar programaticamente a lista de opções.

Dica

Os métodos `showPopover()` e `hidePopover()` permitem controlar programaticamente a visibilidade da lista de opções do combo box. Isso é útil para criar interações personalizadas ou automações específicas.

**Status:** Fechado

**Valor selecionado:** Nenhum

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| enabled | enabled | Define se o combo box está habilitado. | boolean | true |
| errorMessage | error-message | Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. | string | undefined |
| helpText | help-text | Texto de ajuda exibido abaixo do combo box. | string | undefined |
| iconClickable | icon-clickable | Define se o ícone é clicável | boolean | false |
| iconName | icon-name | Nome do ícone. | string | undefined |
| label | label | Texto do label exibido acima do combo box. | string | undefined |
| name | name | Nome do combo box. | string | undefined |
| options | -- | Array com as opções do ez-classic-combo-box. Os elementos devem obedecer o formato: {value: string, label: string} . | IOption[] | undefined |
| placeholder | placeholder | Placeholder do combo box | string | undefined |
| readonly | readonly | Define se o combo box é somente leitura. | boolean | false |
| required | required | Define se o input é obrigatório (visualmente) | boolean | false |
| size | size | Tamanho do input | "default" \| "small" \| "xsmall" | "default" |
| state | state | Estado visual do combo box: default, error, success ou warning. | "default" \| "error" \| "success" \| "warning" | "default" |
| suppressEmptyOption | suppress-empty-option | Se true remove a opção vazia da lista. | boolean | false |
| suppressSearch | suppress-search | Se true desabilita a digitação dentro do componente. | boolean | false |
| textEmptyOption | text-empty-option | Texto a ser apresentado na opção de valor nulo. | string | undefined |
| titleIcon | title-icon | Título do ícone (tooltip). | string | undefined |
| value | value | Valor do combo box. | IOption \| string | null |

### Events

| Event | Description | Type |
|---|---|---|
| ezBlur | Evento disparado quando o combo box perde o foco. | CustomEvent<IOption> |
| ezChange | Evento disparado quando o valor do combo box muda. | CustomEvent<IOption> |
| ezType | Emitido quando é digitado no campo de entrada. | CustomEvent<string> |
| ezVisibilityChange | Emitido quando acontece a alteração de estado do popover. | CustomEvent<boolean> |
| iconClick | Evento disparado quando o ícone é clicado. | CustomEvent<void> |

### Methods

#### `hidePopover() => Promise<void>`

Oculta o popover.

##### Returns

Type: `Promise<void>`

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

#### `setFocus(option?: OptionsSetFocus) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

#### `setValue(option: IOption | string) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `showPopover() => Promise<void>`

Exibe o popover abaixo do input.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * ez-form-view

#### Depends on

  * ez-classic-input
  * ez-popover-core

### CSS Variables

| Variable | Description |
|---|---|
| --ez-classic-combo-box-highlighted-bg-color | Define a cor da seleção do item. |
| --ez-classic-combo-box-max-height | Define a altura máxima do container da lista de opções. |
| --ez-classic-combo-box-list-bg-color | Define a cor de fundo da lista de opções. |
| --ez-classic-combo-box-item-hover-bg-color | Define a cor de fundo do item em hover. |
| --ez-classic-combo-box-selected-bg-color | Define a cor de fundo do item selecionado. |
| --ez-classic-combo-box-selected-text-color | Define a cor do texto do item selecionado. |
| --ez-classic-combo-box-selected-font-weight | Define o peso da fonte do item selecionado. |
| --ez-classic-combo-box-item-padding | Define o padding interno dos itens da lista. |
| --ez-classic-combo-box-item-border-radius | Define o border-radius dos itens da lista. |
| --ez-classic-combo-box-list-margin | Define a margem da lista de opções. |
| --ez-classic-combo-box-transition-duration | Define a duração da transição dos itens. |
| --ez-classic-combo-box-scrollbar-color | Define a cor da scrollbar. |
| --ez-classic-combo-box-no-results-margin | Define a margem do texto "sem resultados". |
| --ez-classic-combo-box-item-text-color | Define a cor do texto dos itens. |
| --ez-classic-combo-box-item-min-height | Define a altura mínima dos itens da lista. |
| --ez-classic-combo-box-width | Define a largura do componente. |
