> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-message-builder/ (snapshot 2026-09-28)

# Message Builder

O componente **SnkMessageBuilder** é o responsável por disponibilizar para a aplicação as mensagens predefinidas, respeitando o padrão do sistema ou as mensagens específicas de cada tela.

Esse componente permite a personalização das mensagens padrão dos componentes, para isso, é necessário criar o arquivo `appmessages.js` na pasta `public\messages\appmessages.js` da aplicação _React_.

## Exemplos

A seguir serão apresentados os exemplos da estrutura do arquivo de mapeamento das mensagens para cada componente.

Observação

Os arquivos de exemplo a seguir foram divididos por componente, mas podem ser configurados em um único arquivo conforme a necessidade, basta respeitar a estrutura de cada componente dentro do _JSON_.

### SnkCrud

Este componente apresenta uma grade (**SnkGrid**), juntamente com uma barra de tarefas (**SnkTaskbar**) e um formulário (**SnkForm**), fazendo a comunicação entre eles para que seja possível realizar operações de _CRUD_ em um servidor com a aplicação Sankhya.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    crudUtils: {
        errorArray: "CrudUtils.find deve receber um array de fields, ou uma lista separada por virgula."
    }
};

export default appMessages;
```

### SnkFilterBar

Este componente apresenta uma barra de filtros com a possíbilidade de gerenciar os filtros exibidos.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkFilterBar: {
        addFilter: "Adicionar filtro",
        pinFilter: "Fixar filtro",
        unpinFilter: "Desfixar filtro",
        removeFilter: "Remover filtro",
        cleanFilter: "Limpar",
        applyFilter: "Aplicar",
        findFilter: "Buscar filtros...",
        findField: "Buscar filtros...",
        modalFindFilter: "Buscar filtro",
        emptyFiltersList: "Não há filtros disponíveis",
        emptyAppliedFiltersList: "Não há filtros aplicados",
        customFilter: "Filtro personalizado",
        defaultFilter: "Filtro padrão",
        failToLoadConfig: "Falha ao buscar configuração de filtros",
        clearAllFilters: "Limpar todos os filtros",
        successfullyCleaned: "Filtro limpo com sucesso!",
        activeFilter: "{{ACTIVE_FILTERS}} filtro aplicado",
        activeFilters: "{{ACTIVE_FILTERS}} filtros aplicados",
        noActiveFilters: "Nenhum filtro aplicado",
        modalDefaultFilterTitle: "Filtro padrão",
        modalInfoTextEditDefault: "Use o layout antigo para editar o seu filtro padrão, em breve traremos uma nova experiência.",
        modalInfoTextCreateDefault: "Use o layout antigo para criar o seu filtro padrão, em breve traremos uma nova experiência.",
        modalPersonalizedFilterTitle: "Filtro personalizado",
        modalPersonalizedFilterSubTitle: "Gerencie seus filtros",
        modalInfoTextCreateEditPersonalized: "Use o layout antigo para criar ou editar filtros, em breve traremos uma nova experiência",
        modalOkButtonLabel: "Aplicar",
        modalCancelButtonLabel: "Limpar"
    }
};

export default appMessages;
```

### SnkForm

Este componente corresponde ao formulário com os campos de uma entidade da aplicação Sankhya junto com um cabeçalho apresentando o título e a barra de tarefas (**SnkTaskbar**) com botões de ações correspondente à entidade.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkForm: {
        title: {
            clone: "Duplicar registro",
            insert: "Cadastrar registro",
            update: "Alterar registro",
            clean: "{{ENTITY_NAME}}"
        },
        goBackTitle: "Voltar"
    }
};

export default appMessages;
```

### SnkTaskbar

Este componente apresenta uma barra de tarefas com botões para executar ações de uma entidade na aplicação Sankhya.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkTaskbar: {
        titleUpdate: "Editar",
        titlePrevious: "Anterior",
        titleNext: "Próximo",
        titleRefresh: "Atualizar",
        titleClone: "Duplicar",
        titleRemove: "Excluir",
        titleMoreOptions: "Mais Opções",
        titleInsert: "Cadastrar",
        titleCancel: "Cancelar",
        titleSave: "Salvar",
        titleGridMode: "Modo Grade",
        titleFormMode: "Modo Formulário",
        titleConfigurator: "Configurações",
        forbidden: "Permissão não liberada"
    }
};

export default appMessages;
```

### SnkFormConfig

Este componente refere-se ao configurador de formulário.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkFormConfig: {
        title: "Configuração do formulário",
        applyConfig: "Aplicar configuração",
        availableFields: {
            title: "Campos disponíveis",
            labelNoFields: "Nenhum campo disponível",
            labelOneField: "1 campo disponível",
            labelAvailableFields: "Campos disponíveis",
            labelSearchField: "Procurar campo"
        },
        form: {
            subTitleInfo: "Inclua estes campos nos grupos ou deixe-os separados no topo do formulário!",
            labelDropField: "Arraste e solte um campo aqui",
            labelNewGroup: "Adicionar novo grupo",
            mainArea: "Área principal",
            tabGeneral: "Geral"
        },
        confirm: {
            title: "Aviso",
            deleteTab: "Você realmente deseja excluir a aba",
            cancel: "As alterações realizadas serão descartadas.<br/><br/><b>Gostaria de continuar?</b>",
            exit: "Ao sair as alterações serão descartadas.<br/><br/><b>Você realmente gostaria de sair?</b>",
            apply: "A <b>{0}</b> irá substituir a sua configuração {1}!<br/><br/><b>Deseja continuar?</b>",
            group: "Não é possível salvar as configurações com um grupo vazio!",
            labelCancel: "Cancelar",
            labelDelete: "Excluir"
        },
        alert: {
            titleGroupExists: "Já existe um grupo com título",
            infoValidTitle: "Por favor, digite um título válido.",
            inTab: "na aba"
        },
        info: {
            successfullyConfigSaved: "As configurações foram salvas com sucesso!"
        }
    },
    snkConfigOptions: {
        label: {
            nameField: "Nome do Campo *",
            typeValueDefault: "Tipo de valor padrão *",
            valueDefault: "Valor Padrão",
            clearDuplicate: "Limpar ao Duplicar",
            requiredField: "Campo Obrigatório",
            protectedField: "Campo Protegido"
        },
        options: {
            valueFixed: "Valor Fixo",
            variable: "Variável"
        }
    },
    snkFieldConfig: {
        titleRemove: "Remover",
        titleConfigurations: "Configurações",
        titleAdd: "Adicionar"
    },
    snkTabConfig: {
        labelRename: "Renomear",
        labelHide: "Ocultar",
        labelShow: "Exibir",
        labelDelete: "Excluir"
    }
};

export default appMessages;
```

### SnkGridConfig

Este componente refere-se ao modal de configurações da grade.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkGridConfig: {
        gridConfiguration: "Configuração da Grade",
        columnVisibilityOrder: "Defina visibilidade e ordem das colunas.",
        sortingSequence: "Sequência da ordenação",
        findColumn: "Localizar coluna",
        cancel: "Cancelar",
        complete: "Concluir",
        tab: {
            columns: "Colunas",
            lineOrdering: "Ordenação das linhas",
        },
        info: {
            successfullyConfigSaved: "As configurações foram salvas com sucesso!"
        },
        confirm: {
            cancel: "Descartar",
            save: "Salvar",
            alert: "Aviso",
            msgCancel: "As alterações realizadas serão descartadas. Gostaria de salvar antes de sair?"
        },
        group: {
            visible: "Visíveis",
            hidden: "Ocultas"
        }
    }
};

export default appMessages;
```

### SnkDataUnit

Este componente atua na aplicação Sankhya como uma camada de abstração entre o _back-end_ e a interface do usuário, proporcionando uma solução eficaz para o gerenciamento de dados.

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkDataUnit: {
        saveInfo: {
            clone: "Duplicação realizada!",
            insert: "Inclusão realizada!",
            update: "Aleração realizada!"
        },
        cancelInfo: {
            clone: "Duplicação descartada!",
            insert: "A inclusão descartada!",
            update: "A edição foi descartada!"
        },
        confirm: {
            cancel: "Cancelar",
            delete: "Excluir"
        },
        removeInfo: "Registro removido com sucesso!",
        cancelConfirmationTitle: "Aviso",
        cancelConfirmation: "As alterações realizadas serão descartadas<br/><br/><b>Você realmente gostaria de cancelar?",
        removeConfirmationTitle: "Aviso",
        removeConfirmation: "Deseja realmente excluir o registro atual?",
        forbidden: "Sem permissão",
        forbiddenUpdate: "Não é possível fazer alterações. Verifique as permissões de acesso.",
        forbiddenInsert: "Não é possível incluir. Verifique as permissões de acesso.",
        forbiddenClone: "Não é possível duplicar. Verifique as permissões de acesso.",
        forbiddenRemove: "Não é possível remover. Verifique as permissões de acesso."
    }
};

export default appMessages;
```

### SnkConfigurator

Este componente refere-se ao modal de controle de visualização das opções de configuração do formulário (**SnkForm**) e da grade (**SnkGrid**).

Exemplo da estrutura do arquivo de mapeamento `appmessages.js` :

```js
const appMessages = {
    snkConfigurator: {
        titleConfigurations: "Configurações",
        subTitleModeConfig: "Modo de visualização",
        labelConfigGrid: "Configurar grade",
        labelConfigForm: "Configurar formulário",
        labelGrid: "Grade",
        labelForm: "Formulário"
    }
};

export default appMessages;
```
