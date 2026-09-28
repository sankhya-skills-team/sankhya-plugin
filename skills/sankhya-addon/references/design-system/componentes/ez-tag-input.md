> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tag-input/ (snapshot 2026-09-28)

# Tag Input

O **Tag Input** é um componente de entrada que permite aos usuários inserir e gerenciar múltiplas opções de forma interativa. Ele é ideal para cenários onde é necessário coletar informações em forma de tags, como categorias, palavras-chave ou outras entradas discretas.

### Perfil Profissional

#### Resumo do Perfil

**Habilidades (3):**

**Interesses (2):**

**Idiomas (2):**

#### Log de Eventos

Nenhum evento registrado ainda...

```jsx
import { useState, useRef } from 'react';
import { EzTagInput, EzButton, EzChip } from '@sankhyalabs/ezui/react/components';
import './demo.css';

const Demo = () => {
    const formData = useRef({
        skills: ['JavaScript', 'React', 'Node.js'],
        interests: ['Design System', 'UX/UI'],
        languages: ['Português', 'Inglês'],
        tools: [],
        keywords: [],
        categories: []
    })
    const [formErrors, setFormErrors] = useState({});
    const [logs, setLogs] = useState([]);

    const skillsRef = useRef();
    const keywordsRef = useRef();

    const addLog = (message) => {
        setLogs(prev => [`${new Date().toLocaleTimeString()}: ${message}`, ...prev.slice(-9)]);
    };

    const handleTagChange = (field, tags) => {
        formData.current = ({ ...formData.current, [field]: [...tags] });

        // Limpar erro se existir
        if (formErrors[field]) {
            setFormErrors(prev => ({ ...prev, [field]: '' }));
        }

        addLog(`Campo ${field} alterado: ${tags.length} tags`);
    };

    const validateField = (field, tags) => {
        let error = '';

        switch (field) {
            case 'skills':
                if (tags.length === 0) error = 'Pelo menos uma habilidade é obrigatória';
                if (tags.length > 10) error = 'Máximo de 10 habilidades permitidas';
                break;
            case 'interests':
                if (tags.length === 0) error = 'Pelo menos um interesse é obrigatório';
                if (tags.length > 5) error = 'Máximo de 5 interesses permitidos';
                break;
            case 'languages':
                if (tags.length === 0) error = 'Pelo menos um idioma é obrigatório';
                break;
            case 'keywords':
                if (tags.length > 20) error = 'Máximo de 20 palavras-chave permitidas';
                break;
        }

        return error;
    };

    const handleTagBlur = (field) => {
        const tags = formData.current[field];
        const error = validateField(field, tags);
        if (error) {
            setFormErrors(prev => ({ ...prev, [field]: error }));
        }
        addLog(`Campo ${field} perdeu o foco`);
    };

    const handleTagFocus = (field) => {
        addLog(`Campo ${field} recebeu o foco`);
    };

    const handleSubmit = () => {
        const errors = {};
        const requiredFields = ['skills', 'interests', 'languages'];

        requiredFields.forEach(field => {
            const error = validateField(field, formData.current[field]);
            if (error) errors[field] = error;
        });

        // Validar outros campos não obrigatórios
        ['keywords', 'tools', 'categories'].forEach(field => {
            const error = validateField(field, formData.current[field]);
            if (error) errors[field] = error;
        });

        setFormErrors(errors);

        if (Object.keys(errors).length === 0) {
            addLog('Formulário enviado com sucesso!');
            alert('Perfil profissional criado com sucesso!');
        } else {
            addLog('Erro na validação do formulário');
        }
    };

    const handleReset = () => {
        formData.current = {
            skills: [],
            interests: [],
            languages: [],
            tools: [],
            keywords: [],
            categories: []
        };
        setFormErrors({});
        setLogs([]);
        addLog('Formulário resetado');
    };

    const focusSkills = () => {
        skillsRef.current?.setFocus();
        addLog('Foco definido no campo habilidades');
    };

    const addPredefinedSkills = () => {
        const newSkills = [...formData.current.skills, 'TypeScript', 'GraphQL', 'Docker'];
        const uniqueSkills = [...new Set(newSkills)];
        formData.current = { ...formData.current, skills: uniqueSkills };
        addLog('Habilidades pré-definidas adicionadas');
    };

    const clearKeywords = () => {
        formData.current = { ...formData.current, keywords: [] };
        addLog('Palavras-chave limpos');
    };

    const getFieldState = (field) => {
        if (formErrors[field]) return 'error';
        if (formData.current[field].length > 0) return 'success';
        return 'default';
    };

    return (
        <div className="ez-tag-input-demo_container">
            <h3>Perfil Profissional</h3>
            <form>
                {/* Habilidades Técnicas */}
                <EzTagInput
                    ref={skillsRef}
                    label="Habilidades Técnicas *"
                    placeholder="Digite suas habilidades técnicas..."
                    tags={formData.current.skills}
                    maxTags={10}
                    state={getFieldState('skills')}
                    onEzChange={(evt) => handleTagChange('skills', evt.detail)}
                    onEzBlur={(evt) => handleTagBlur('skills', evt.detail)}
                    onEzFocus={() => handleTagFocus('skills')}
                    helpText={formErrors.skills || `${formData.current.skills.length}/10 habilidades adicionadas`}
                />

                {/* Áreas de Interesse */}
                <EzTagInput
                    label="Áreas de Interesse *"
                    placeholder="Quais áreas te interessam?"
                    tags={formData.current.interests}
                    maxTags={5}
                    state={getFieldState('interests')}
                    onEzChange={(evt) => handleTagChange('interests', evt.detail)}
                    onEzBlur={(evt) => handleTagBlur('interests', evt.detail)}
                    onEzFocus={() => handleTagFocus('interests')}
                    helpText={formErrors.interests || `${formData.current.interests.length}/5 interesses selecionados`}
                />

                {/* Idiomas */}
                <EzTagInput
                    label="Idiomas *"
                    placeholder="Que idiomas você fala?"
                    tags={formData.current.languages}
                    state={getFieldState('languages')}
                    onEzChange={(evt) => handleTagChange('languages', evt.detail)}
                    onEzBlur={(evt) => handleTagBlur('languages', evt.detail)}
                    onEzFocus={() => handleTagFocus('languages')}
                    helpText={formErrors.languages || "Idiomas que você domina"}
                />

                {/* Ferramentas */}
                <EzTagInput
                    label="Ferramentas e Softwares"
                    placeholder="Ferramentas que você utiliza..."
                    tags={formData.current.tools}
                    state={getFieldState('tools')}
                    onEzChange={(evt) => handleTagChange('tools', evt.detail)}
                    onEzBlur={(evt) => handleTagBlur('tools', evt.detail)}
                    onEzFocus={() => handleTagFocus('tools')}
                    helpText="Ferramentas do seu dia a dia"
                />

                {/* Palavras-chave (campo livre) */}
                <EzTagInput
                    ref={keywordsRef}
                    label="Palavras-chave"
                    placeholder="Palavras-chave para SEO do seu perfil..."
                    tags={formData.current.keywords}
                    maxTags={20}
                    state={getFieldState('keywords')}
                    onEzChange={(evt) => handleTagChange('keywords', evt.detail)}
                    onEzBlur={(evt) => handleTagBlur('keywords', evt.detail)}
                    onEzFocus={() => handleTagFocus('keywords')}
                    helpText={formErrors.keywords || `${formData.current.keywords.length}/20 palavras-chave`}
                />

                {/* Categorias (campo desabilitado para demonstração) */}
                <EzTagInput
                    label="Categorias Especializadas"
                    placeholder="Categorias não disponíveis no momento"
                    tags={formData.current.categories}
                    enabled={false}
                    state="default"
                    helpText="Este campo está temporariamente desabilitado"
                />

                <section className="form-actions">
                    <EzButton
                        type="submit"
                        className="ez-button--primary"
                        label="Criar Perfil"
                        onClick={handleSubmit}
                    />
                    <EzButton
                        type="button"
                        onClick={handleReset}
                        label="Limpar Tudo"
                    />
                    <EzButton
                        type="button"
                        className="ez-button--tertiary"
                        onClick={focusSkills}
                        label="Focar Habilidades"
                    />
                    <EzButton
                        type="button"
                        className="ez-button--tertiary"
                        onClick={addPredefinedSkills}
                        label="Adicionar Habilidades"
                    />
                    <EzButton
                        type="button"
                        className="ez-button--tertiary"
                        onClick={clearKeywords}
                        label="Limpar Palavras-chave"
                    />
                </section>
            </form>

            <h4>Resumo do Perfil</h4>
            <section className="form-summary">
                <div className="summary-grid">
                    <div className="summary-item">
                        <strong>Habilidades ({formData.current.skills.length}):</strong>
                        <div className="tag-preview">
                            {formData.current.skills.map((skill, index) => (
                                <EzChip key={index} label={skill} disableAutoUpdateValue/>
                            ))}
                        </div>
                    </div>

                    <div className="summary-item">
                        <strong>Interesses ({formData.current.interests.length}):</strong>
                        <div className="tag-preview">
                            {formData.current.interests.map((interest, index) => (
                                <EzChip key={index} label={interest} disableAutoUpdateValue/>
                            ))}
                        </div>
                    </div>

                    <div className="summary-item">
                        <strong>Idiomas ({formData.current.languages.length}):</strong>
                        <div className="tag-preview">
                            {formData.current.languages.map((lang, index) => (
                                <EzChip key={index} label={lang} disableAutoUpdateValue/>
                            ))}
                        </div>
                    </div>

                    {formData.current.tools.length > 0 && (
                        <div className="summary-item">
                            <strong>Ferramentas ({formData.current.tools.length}):</strong>
                            <div className="tag-preview">
                                {formData.current.tools.map((tool, index) => (
                                    <span key={index} className="tag">{tool}</span>
                                ))}
                            </div>
                        </div>
                    )}

                    {formData.current.keywords.length > 0 && (
                        <div className="summary-item">
                            <strong>Palavras-chave ({formData.current.keywords.length}):</strong>
                            <div className="tag-preview">
                                {formData.current.keywords.map((keyword, index) => (
                                    <span key={index} className="tag">{keyword}</span>
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            </section>

            <h4>Log de Eventos</h4>

            <div className="logs-container">
                {logs.map((log, index) => (
                    <div key={index} className="log-entry">
                        {log}
                    </div>
                ))}
                {logs.length === 0 && (
                    <div className="log-entry--empty">
                        Nenhum evento registrado ainda...
                    </div>
                )}
            </div>
        </div>
    );
};

export default Demo;
```

## Variações

### Estados Visuais

O Tag Input suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

### Modo Somente Leitura

O componente pode ser configurado para exibir apenas as tags sem permitir edição.

```jsx
import React from 'react';
import { EzTagInput } from '@sankhyalabs/ezui/react/components';
import './readonly.css';

const Demo = () => {
    const readonlyTags = ['Somente Leitura', 'Não Editável', 'Visualização'];

    return (
        <div className="ez-tag-input-readonly-container">
            <EzTagInput
                label="Modo Somente Leitura"
                placeholder="Tags em modo somente leitura"
                tags={readonlyTags}
                readonly={true}
            />

            <EzTagInput
                label="Modo Editável (Comparação)"
                placeholder="Adicione ou remova tags"
                tags={readonlyTags}
                readonly={false}
            />
        </div>
    );
};

export default Demo;
```

### Estados de Interação

Controle sobre estados desabilitados e múltiplos modos de interação.

### Limite de Tags

É possível definir um limite máximo de tags que podem ser adicionadas.

#### Máximo 3 tags

#### Máximo 5 tags

#### Sem limite

```jsx
import React, { useState } from 'react';
import { EzTagInput } from '@sankhyalabs/ezui/react/components';
import './max-tags.css';

const Demo = () => {
    const [tags3, setTags3] = useState(['Tag 1', 'Tag 2']);
    const [tags5, setTags5] = useState(['A', 'B', 'C', 'D']);
    const [tagsUnlimited, setTagsUnlimited] = useState(['Sem limite']);

    return (
        <div className="ez-tag-input-max-tags-container">
            <section>
                <h4 className="demo-subtitle">
                    Máximo 3 tags
                </h4>
                <EzTagInput
                    label="Limite de 3 tags"
                    placeholder="Digite uma tag..."
                    tags={tags3}
                    maxTags={3}
                    onEzChange={({detail}) => setTags3(detail)}
                    helpText={`${tags3.length}/3 tags`}
                />
            </section>

            <section>
                <h4 className="demo-subtitle">
                    Máximo 5 tags
                </h4>
                <EzTagInput
                    label="Limite de 5 tags"
                    placeholder="Digite uma tag..."
                    tags={tags5}
                    maxTags={5}
                    onEzChange={({detail}) => setTags5(detail)}
                    helpText={`${tags5.length}/5 tags`}
                />
            </section>

            <section>
                <h4 className="demo-subtitle">
                    Sem limite
                </h4>
                <EzTagInput
                    label="Sem limite de tags"
                    placeholder="Digite uma tag..."
                    tags={tagsUnlimited}
                    onEzChange={(e) => setTagsUnlimited(e.detail)}
                    helpText={`${tagsUnlimited.length} tags`}
                />
            </section>
        </div>
    );
};

export default Demo;
```

### Validação Customizada

O componente permite validação personalizada antes de adicionar novas tags através da propriedade `validator`.

Esta funcionalidade oferece controle total sobre quais tags são aceitas, permitindo implementar regras de negócio específicas como:

  * **Validação de formato** : Garantir que tags sigam um padrão específico (ex: emails, números, códigos)
  * **Validação de conteúdo** : Bloquear palavras inadequadas ou termos específicos
  * **Validação de tamanho** : Controlar o comprimento mínimo e máximo das tags
  * **Validação contextual** : Usar as tags existentes para validar novas entradas

A função `validator` recebe dois parâmetros:

  * `tag`: A tag que está sendo validada
  * `existingTags`: Array com as tags já existentes no componente

E pode retornar:

  * `true`: Tag válida, será adicionada
  * `false`: Tag inválida, será rejeitada silenciosamente
  * `string`: Tag inválida, será rejeitada e emitirá o evento `onEzValidationError` com a mensagem de erro

Dica

No evento onEzValidationError, você pode exibir uma mensagem de erro personalizada para o usuário. Utilizando o próprio target passado, é possível acessar suas propriedades e métodos.

#### Validação de E-mail

#### Validação Numérica

#### Validação de Tamanho

### Remoção de Tags

O componente oferece múltiplas formas de remover tags, garantindo uma experiência de usuário flexível e acessível:

#### Remoção com Mouse

  * **Clique no ícone X** : Cada tag possui um ícone X que pode ser clicado para remoção

#### Remoção com Teclado

  * **Navegação** : Use `Tab`, `Shift+Tab`, `Seta Esquerda` e `Seta Direita` para navegar entre as tags
  * **Remoção** : Com uma tag selecionada, pressione `Enter`, `Backspace` ou `Delete` para removê-la
  * **Remoção rápida** : Com o input vazio, pressione `Backspace` para remover a última tag

#### Controle de Comportamento

Você pode personalizar o comportamento de remoção através das seguintes propriedades:

  * **`suppressBackspaceToRemove` (false por padrão)**: Define se a tecla `Backspace` deve remover a última tag quando o input está vazio
  * **`suppressTagsKeyboardNavigation` (false por padrão)**: Define se a navegação por teclado pelas tags deve ser suprimida

```jsx
import React, { useState } from 'react';
import { EzTagInput } from '@sankhyalabs/ezui/react/components';
import './removable-tags.css';

const Demo = () => {
    const [tags1, setTags1] = useState(['Removível 1', 'Removível 2', 'Removível 3']);
    const [tags2, setTags2] = useState(['Removível 1', 'Removível 2', 'Removível 3']);
    const [tags3, setTags3] = useState(['Removível 1', 'Removível 2', 'Removível 3']);

    return (
        <div className="ez-tag-input-removable-tags-container">
            <EzTagInput
                label="Tags removíveis"
                placeholder="Digite uma tag..."
                tags={tags1}
                onEzChange={({ detail }) => setTags1(detail)}
                helpText="Tags removíveis por teclado ou clique no X"
            />
            <hr />
            <EzTagInput
                label="Tags sem navegação por teclado"
                placeholder="Digite uma tag..."
                tags={tags2}
                onEzChange={({ detail }) => setTags2(detail)}
                suppressTagsKeyboardNavigation={true}
                helpText="Tags removíveis por clique no X apenas"
            />
            <hr />
            <EzTagInput
                label="Remoção pelo Backspace desativado"
                placeholder="Digite uma tag..."
                tags={tags3}
                onEzChange={({ detail }) => setTags3(detail)}
                suppressBackspaceToRemove={true}
                helpText="Tags removíveis por teclado ou clique no X, mas não removíveis com Backspace"
            />
        </div>
    );
};

export default Demo;
```

## Eventos

### ezChange

Disparado sempre que a lista de tags é alterada.

Nenhum evento capturado ainda...

### ezTagAdded

Disparado quando uma nova tag é adicionada.

Nenhum evento capturado ainda...

```jsx
import React, { useState } from 'react';
import { EzTagInput } from '@sankhyalabs/ezui/react/components';
import './ez-tag-add.css';

const Demo = () => {
    const [tags, setTags] = useState(['Tag inicial']);
    const [events, setEvents] = useState([]);

    const addEvent = (tag) => {
        setEvents(prev => [`Tag adicionada: ${tag}`, ...prev.slice(-4)]);
    }

    return (
        <div className="ez-tag-add-demo-container">
            <EzTagInput
                label="Adicione tags para ver o evento"
                placeholder="Digite uma tag e pressione Enter..."
                tags={tags}
                onEzTagAdded={({ detail }) => addEvent(detail)}
                onEzChange={({ detail }) => setTags(detail)}
            />
            <div className="logs-container">
                {events.length === 0 ? (
                    <div>
                        Nenhum evento capturado ainda...
                    </div>
                ) : (
                    events.map((event, index) => (
                        <div key={index} className="log-entry">
                            {event}
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default Demo;
```

### ezTagRemoved

Disparado quando uma tag é removida.

Nenhum evento capturado ainda...

```jsx
import React, { useState } from 'react';
import { EzTagInput } from '@sankhyalabs/ezui/react/components';
import './ez-tag-remove.css';

const Demo = () => {
    const [tags, setTags] = useState(['Tag 1', 'Tag 2', 'Tag 3']);
    const [events, setEvents] = useState([]);

    const addEvent = (tag) => {
        setEvents(prev => [`Tag removida: ${tag}`, ...prev.slice(-4)]);
    }

    return (
        <div className='ez-tag-remove-demo-container'>
            <EzTagInput
                label="Remova tags para ver o evento"
                placeholder="Adicione mais tags se desejar..."
                tags={tags}
                onEzTagRemoved={({ detail }) => addEvent(detail)}
                onEzChange={({ detail }) => setTags(detail)}
            />

            <div className="logs-container">
                {events.length === 0 ? (
                    <div>
                        Nenhum evento capturado ainda...
                    </div>
                ) : (
                    events.map((event, index) => (
                        <div key={index} className="log-entry">
                            {event}
                        </div>
                    ))
                )}
            </div>

        </div>
    );
};

export default Demo;
```

### ezBlur e ezFocus

Disparado quando o componente perde ou ganha o foco.

Nenhum evento capturado ainda...

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

**Opções do setFocus:**

Selecionar texto ao focarPrevenir scroll ao focarDemonstrar setBlur automaticamente após 3 segundos

**💡 Demonstração:** Quando esta opção estiver marcada, o método `setBlur()`será chamado automaticamente 3 segundos após dar foco. Isso é apenas para exemplificar o uso do método.

demo.js

```jsx
import React, { useState, useRef, useEffect } from 'react';
import { EzTagInput, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const tagInputRef = useRef(null);
    const [tags, setTags] = useState(['Tag 1', 'Tag 2']);
    const [focusOptions, setFocusOptions] = useState({
        selectText: false,
        preventScroll: false
    });
    const [autoBlurEnabled, setAutoBlurEnabled] = useState(true);
    const [blurTimer, setBlurTimer] = useState(null);

    const handleSetFocus = async () => {
        if (tagInputRef.current) {
            await tagInputRef.current.setFocus(focusOptions);

            if (autoBlurEnabled) {
                const timer = setTimeout(() => {
                    handleSetBlur();
                }, 3000);
                setBlurTimer(timer);
            }
        }
    };

    const handleSetBlur = async () => {
        if (tagInputRef.current) {
            await tagInputRef.current.setBlur();
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
            <EzTagInput
                ref={tagInputRef}
                label="Tag Input com controle de foco"
                placeholder="Digite uma tag..."
                tags={tags}
                onEzChange={(e) => setTags(e.detail.tags)}
            />
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

### addTag

Método para adicionar uma tag programaticamente.

### removeTag

Método para remover uma tag específica.

```jsx
import React, { useState, useRef } from 'react';
import { EzTagInput, EzButton, EzClassicComboBox } from '@sankhyalabs/ezui/react/components';
import './remove-tag.css';

const Demo = () => {
    const [tags, setTags] = useState(['Tag 1', 'Tag 2', 'Tag 3', 'Tag 4', 'Tag 5']);
    const [selectedTagToRemove, setSelectedTagToRemove] = useState(null);
    const [message, setMessage] = useState('');
    const tagInputRef = useRef(null);

    const handleRemoveTag = () => {
        if (!selectedTagToRemove) {
            setMessage('Selecione uma tag para remover');
            return;
        }

        if (tagInputRef.current) {
            const success = tagInputRef.current.removeTag(selectedTagToRemove.value);
            if (success) {
                setMessage(`Tag "${selectedTagToRemove.value}" removida com sucesso`);
                setSelectedTagToRemove(null);
            } else {
                setMessage(`Erro ao remover tag "${selectedTagToRemove.value}"`);
            }
        }
    };

    const handleRemoveFirstTag = () => {
        if (tags.length === 0) {
            setMessage('Não há tags para remover');
            return;
        }

        const firstTag = tags[0];
        if (tagInputRef.current) {
            const success = tagInputRef.current.removeTag(firstTag);
            if (success) {
                setMessage(`Primeira tag "${firstTag}" removida`);
            }
        }
    };

    const handleRemoveLastTag = () => {
        if (tags.length === 0) {
            setMessage('Não há tags para remover');
            return;
        }

        const lastTag = tags[tags.length - 1];
        if (tagInputRef.current) {
            const success = tagInputRef.current.removeTag(lastTag);
            if (success) {
                setMessage(`Última tag "${lastTag}" removida`);
            }
        }
    };

    const handleRemoveRandomTag = () => {
        if (tags.length === 0) {
            setMessage('Não há tags para remover');
            return;
        }

        const randomTag = tags[Math.floor(Math.random() * tags.length)];
        if (tagInputRef.current) {
            const success = tagInputRef.current.removeTag(randomTag);
            if (success) {
                setMessage(`Tag aleatória "${randomTag}" removida`);
            }
        }
    };

    const tagOptions = tags.map(tag => ({ value: tag, label: tag }));

    return (
        <div className="ez-tag-remove-demo-container">
            <EzTagInput
                ref={tagInputRef}
                label="Tag Input com remoção programática"
                placeholder="Use os botões para remover tags..."
                tags={tags}
                onEzChange={({ detail }) => setTags(detail)}
                helpText={message}
            />

            <section className="tag-selection-to-remove">
                <EzClassicComboBox
                    label="Selecione uma tag para remover"
                    placeholder="Escolha uma tag..."
                    options={tagOptions}
                    value={selectedTagToRemove}
                    onEzChange={({ detail }) => setSelectedTagToRemove(detail)}
                    enabled={tags.length > 0}
                />

                <EzButton
                    label="Remover Tag Selecionada"
                    onClick={handleRemoveTag}
                    disabled={!selectedTagToRemove}
                    variant="outline"
                />
            </section>

            <section>
                <EzButton
                    label="Remover Primeira Tag"
                    onClick={handleRemoveFirstTag}
                    disabled={tags.length === 0}
                    variant="secondary"
                />

                <EzButton
                    label="Remover Última Tag"
                    onClick={handleRemoveLastTag}
                    disabled={tags.length === 0}
                    variant="secondary"
                />

                <EzButton
                    label="Remover Tag Aleatória"
                    onClick={handleRemoveRandomTag}
                    disabled={tags.length === 0}
                    variant="outline"
                />
            </section>
        </div>
    );
};

export default Demo;
```

### clearTags

Método para limpar todas as tags.

Total de tags: **5**

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| allowDuplicates | allow-duplicates | Define se tags duplicadas são permitidas | boolean | false |
| enabled | enabled | Define se o input está habilitado | boolean | true |
| helpText | help-text | Texto de ajuda exibido abaixo do input | string | undefined |
| label | label | Texto do label exibido acima do input | string | '' |
| maxTagLength | max-tag-length | Tamanho máximo de uma tag | number | undefined |
| maxTags | max-tags | Número máximo de tags permitidas | number | undefined |
| name | name | Nome do input | string | undefined |
| placeholder | placeholder | Placeholder do input | string | '' |
| readonly | readonly | Define se o input é somente leitura | boolean | false |
| state | state | Estado visual do componente | "default" \| "error" \| "success" \| "warning" | "default" |
| suppressBackspaceToRemove | suppress-backspace-to-remove | Define se a tecla Backspace deve remover a última tag quando o input está vazio | boolean | false |
| suppressTagsKeyboardNavigation | suppress-tags-keyboard-navigation | Define se a navegação por teclado pelas tags deve ser suprimida | boolean | false |
| tags | -- | Array de tags iniciais | string[] | [] |
| validator | -- | Função de validação customizada para tags | (tag: string, existingTags: string[]) => string \| boolean | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezBlur | Evento disparado quando o input perde foco | CustomEvent<string[]> |
| ezChange | Evento disparado quando as tags mudam | CustomEvent<string[]> |
| ezFocus | Evento disparado quando o input recebe foco | CustomEvent<string[]> |
| ezTagAdded | Evento disparado quando uma tag é adicionada | CustomEvent<string> |
| ezTagRemoved | Evento disparado quando uma tag é removida | CustomEvent<string> |
| ezType | Emitido quando é digitado no campo de entrada | CustomEvent<string> |
| ezValidationError | Evento disparado quando uma validação falha | CustomEvent<{ tag: string; error?: string; }> |

### Methods

#### `addTag(tag: string) => Promise<boolean>`

Adiciona uma tag programaticamente

##### Returns

Type: `Promise<boolean>`

#### `clearTags() => Promise<void>`

Limpa todas as tags

##### Returns

Type: `Promise<void>`

#### `removeTag(tag: string) => Promise<boolean>`

Remove uma tag programaticamente

##### Returns

Type: `Promise<boolean>`

#### `setBlur() => Promise<void>`

Remove o foco do campo

##### Returns

Type: `Promise<void>`

#### `setFocus(option?: OptionsSetFocus) => Promise<void>`

Aplica o foco no campo

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-chip

### CSS Variables

| Variable | Description |
|---|---|
| --ez-tag-input--background-color | Define a cor de fundo do container do input. |
| --ez-tag-input--border-color-default | Define a cor da borda no estado padrão. |
| --ez-tag-input--border-color-focused | Define a cor da borda no estado focado. |
| --ez-tag-input--border-color-error | Define a cor da borda no estado de erro. |
| --ez-tag-input--border-color-success | Define a cor da borda no estado de sucesso. |
| --ez-tag-input--border-color-warning | Define a cor da borda no estado de aviso. |
| --ez-tag-input--border-radius | Define o raio da borda do container. |
| --ez-tag-input--padding | Define o espaçamento interno do container. |
| --ez-tag-input--gap | Define o espaçamento entre tags e input. |
| --ez-tag-input--label-color | Define a cor do texto do label. |
| --ez-tag-input--label-font-weight | Define o peso da fonte do label. |
| --ez-tag-input--input-color | Define a cor do texto do input. |
| --ez-tag-input--input-font-size | Define o tamanho da fonte do input. |
| --ez-tag-input--placeholder-color | Define a cor do placeholder. |
| --ez-tag-input--background-color-disabled | Define a cor de fundo do input quando está desabilitado. |
| --ez-tag-input--helptext-color | Define a cor do texto de ajuda do input. |
