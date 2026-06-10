# sankhya-js — Índice de Referências

Biblioteca AngularJS/Material Design usada para construção de telas personalizadas **HTML5/xhtml5** no portal Sankhya (abordagem legada, anterior ao Design System). Componentes com prefixo `sk-`, organizados em módulos `snk.*`.

> **Atenção:** esta abordagem é distinta do **Design System** (`ez-` / `snk-` web components). Para saber qual usar, verificar `SKILL.md` seção "Abordagens para Telas Personalizadas".

**URL Base da documentação:** `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/` (rede interna Sankhya — inacessível externamente)

---

## Como usar esta documentação

Para detalhes de um componente específico, leia o arquivo do módulo correspondente na tabela abaixo. Cada arquivo é autocontido com parâmetros, tipos, exemplos e métodos.

---

## Índice por módulo

| Módulo | Arquivo | O que contém |
|---|---|---|
| **snk.components.dataset** | `references/sankhya-js-snk-components-dataset.md` | `sk-dataset`, `sk-dsfield-md`, `DatasetOnlineFilter`, `FieldBinder`, `RecordValidator` |
| **snk.components.input** | `references/sankhya-js-snk-components-inputs.md` | `sk-text-input`, `sk-number-input`, `sk-date-input`, `sk-date-time-input`, `sk-switch`, `sk-combobox`, `sk-pesquisa-input`, `sk-text-area`, `sk-radio-input` e outros 15+ inputs |
| **snk.components (grid/nav)** | `references/sankhya-js-snk-components-grid-nav.md` | `sk-datagrid`, `sk-navigator`, `sk-dynaform`, `sk-filter-panel`, interceptors |
| **snk.components UI (layout/tabs/popups)** | `references/sankhya-js-snk-components-ui.md` | layout (hbox/vbox), tabs, sk-wizard, SanPopup, accordion |
| **snk.components UI (botões/visuais/listas)** | `references/sankhya-js-snk-components-ui-b.md` | botões, ícones, WaitWindow, checkboxes, listas, drag-and-drop, sidenav, code-editor, sk-attach |
| **snk.form** | `references/sankhya-js-snk-form.md` | `sk-form`, `sk-form-custom-item`, `sk-datagrid-custom-column`, `sk-form-block` |
| **snk.core** | `references/sankhya-js-snk-core.md` | `sk-application`, `MessageUtils`, directives de layout, `DateBuilder`, `ThemeColors`, `MetadataProvider`, `MGEParameters` |
| **snk.commons / sk-simple-form / util.common** | `references/sankhya-js-snk-commons.md` | liberações, ação programada, BPMN, `sk-simple-form`, `sk-i18n`, `DataSource`, `Criteria` |

---

## Estrutura mínima de uma tela HTML5

```html
<!-- arquivo: minha-tela.xhtml5 -->
<sk-application ng-controller="MeuController as ctrl" layout="column" flex>

    <!-- Dataset da entidade -->
    <sk-dataset
        entity-name="MinhaEntidade"
        sk-dataset-created="ctrl.onDatasetCreated(dataset)">
    </sk-dataset>

    <!-- Navegação CRUD -->
    <sk-navigator dataset="ctrl.dataset" show-crud="true"></sk-navigator>

    <!-- Grade de registros -->
    <sk-datagrid sk-dataset="ctrl.dataset"></sk-datagrid>

    <!-- Formulário de edição -->
    <sk-form sk-dataset="ctrl.dataset"></sk-form>

</sk-application>
```

**Ou usando dynaform (tudo integrado):**
```html
<sk-application sk-app-module="GGB_MinhaTelaApp">
    <div ng-controller="GGB_MinhaTelaController as ctrl">
        <sk-dynaform
            sk-entity-name="GGB_MinhaEntidade"
            sk-dynaform-interceptor="ctrl"
            sk-skip-start-page="true"
            sk-default-mode="master"
            sk-hide-tour="true">
        </sk-dynaform>
    </div>
</sk-application>
```

---

## Dependência AngularJS

```js
angular.module('minhaTela', ['snk'])
    .controller('MeuController', ['MessageUtils', 'SanPopup',
        function(MessageUtils, SanPopup) {
            // ...
        }
    ]);
```

---

## IDynaformInterceptor — Padrão Real

O `IDynaformInterceptor` é o contrato para interceptar o ciclo de vida do dynaform. Implementação completa:

```js
angular.module('GGB_MinhaTelaApp', ['snk'])
    .controller('GGB_MinhaTelaController', [
        'MessageUtils', 'ObjectUtils', '$scope', '$timeout', 'AngularUtil',
        function (MessageUtils, ObjectUtils, $scope, $timeout, AngularUtil) {
            const self = this;
            let _dynaform;
            let _dataset;

            // Declarar implementação da interface
            ObjectUtils.implements(self, IDynaformInterceptor);
            self.init = init;
            self.onDynaformLoaded = onDynaformLoaded;

            function init() {}

            function onDynaformLoaded(dynaform, dataset) {
                // Filtrar pela entidade correta (pode haver múltiplos dynaforms)
                if (dataset.getEntityName() === 'GGB_MinhaEntidade') {
                    _dynaform = dynaform;
                    _dataset = dataset;

                    // API de navegação — compatível com versões antigas e novas
                    var navApi = dynaform.getNavigationAPI
                        ? dynaform.getNavigationAPI()
                        : dynaform.getNavigatorAPI();

                    navApi.showAddButton(true);
                    navApi.showRemoveButton(true);
                    navApi.showCopyButton(false);

                    // Manipulação de DOM sempre com $timeout(fn, 300)
                    $timeout(function () {
                        // DOM já renderizado aqui
                    }, 300);
                }
            }
        }
    ]);
```

---

## ServiceProxy — Chamando @Service do Frontend

```js
.factory('MeuServiceProxy', ['ServiceProxy', function (ServiceProxy) {
    function executar(dto) {
        return ServiceProxy.callService(
            'nomeaddon@MeuServiceSP.metodo',  // addonname em minúsculas
            { dto: dto }
        );
    }
    return { executar: executar };
}])
```

Tratamento da resposta:

```js
MeuServiceProxy.executar({ CODCONFIG: 1 })
    .then(function (resp) {
        // resp.responseBody contém o objeto retornado pelo @Service
        var msg = resp.responseBody && resp.responseBody.mensagem;
        MessageUtils.showInfo('Sucesso', msg);
    })
    .catch(function (err) {
        // err.statusMessage contém a mensagem do MGEModelException
        MessageUtils.showError('Erro', err.statusMessage || 'Falha na operação.');
    });
```

> O nome do addon no `callService` é o `rootProject.name` do `settings.gradle` em **minúsculas**.

---

## Principais serviços injetáveis

| Serviço | Módulo | Uso |
|---|---|---|
| `MessageUtils` | snk.core.util | Mensagens ao usuário (info, erro, confirm) |
| `ObjectUtils` | snk.core.util | `implements`, `getProperty` |
| `ServiceProxy` | snk.core | Chamadas a `@Service` Java |
| `AngularUtil` | snk.core | `createDirective` para injetar diretivas no DOM |
| `SkApplicationInstance` | snk.core | Abrir outras telas do Sankhya (`openApp`) |
| `PopUpParameter` | snk.commons | Popup de parâmetros com campos tipados |
| `SanPopup` | snk.components.popup | Abrir popups customizados |
| `DatasetOnlineFilter` | snk.components.dataset | Filtro em memória do dataset |
| `MetadataProvider` | snk.db.metadataprovider | Metadados de entidade via API |
| `MGEParameters` | snk.db.parameters | Parâmetros do sistema |
| `ThemeColors` | snk.core.theme | Cores do tema atual |
| `WaitWindow` | snk.components.waitwindow | Janela de espera |
| `FilterPanelService` | snk.components.filterpanel | Operações de filtro |
| `PopupLiberacoes` | snk.commons.liberacoes | Popup de liberações |
| `StringUtils` | snk.core.util | Utilitários de string |
| `GridConfig` | snk.components.datagrid | Configuração de grid |
| `i18n` | snk.core | Internacionalização |

---

## Padrões Reais de Uso

### MessageUtils — Variantes de confirmação

```js
// Confirmação simples (Sim / Não)
MessageUtils.simpleConfirm('Título', 'Mensagem', true)
    .then(function () { /* usuário confirmou */ });

// Confirmação com 3 botões (Sim / Não / Cancelar)
MessageUtils.confirm('Título', 'Mensagem', 'Sim', 'Não', false, false, {
    cancelLabel: 'Cancelar',
    showBtnCancel: true
})
.then(function () {
    // clicou "Sim"
})
.catch(function (reason) {
    if (reason === 'no') {
        // clicou "Não"
    }
    // se cancelou, reason é outro valor
});
```

---

### ObjectUtils.getProperty — Leitura segura da resposta

Evita erros quando campos aninhados são nulos:

```js
ServiceProxy.callService('addon@MeuServiceSP.executar', { dto: dto })
    .then(function (resp) {
        var msg    = ObjectUtils.getProperty(resp, 'responseBody.mensagem');
        var falhas = ObjectUtils.getProperty(resp, 'responseBody.falhas');

        if (falhas) {
            MessageUtils.showError('Atenção', msg + '\n\nFalhas:\n' + falhas);
        } else {
            MessageUtils.showInfo('Sucesso', msg);
        }
    })
    .catch(function (err) {
        MessageUtils.showError('Erro', err.statusMessage || 'Falha na operação.');
    });
```

---

### Dataset — Operações essenciais

```js
// Linha atual
var row = _dataset.getCurrentRowAsObject();

// Registros selecionados (múltipla seleção no grid)
var sel = _dataset.getSelectedRecordsAsObjects();
var rows = (sel == null) ? [] : (Array.isArray(sel) ? sel : [sel]);

// Gravar valor programaticamente
_dataset.setFieldValue('CAMPO', valor);

// Ordenação programática
_dataset.setOrderByExpression('this.CODREGISTRO');

// Quantidade de registros
var total = _dataset.size();

// Atualizar dataset com filtro após operação
_dataset.refresh(Criteria('this.CODREGISTRO IN (' + idList.join(',') + ')'));

// Atualizar sem filtro
_dataset.refresh();
```

---

### Operações em lote (seleção múltipla)

Padrão para ações que operam sobre registros selecionados, com fallback para a linha atual:

```js
function getRowsParaAcao() {
    var sel = _dataset.getSelectedRecordsAsObjects();
    var selected = (sel == null) ? [] : (Array.isArray(sel) ? sel : [sel]);
    if (selected.length > 0) return selected;
    var row = _dataset.getCurrentRowAsObject();
    return row ? [row] : [];
}

function btnExecutarEmLote() {
    var rows = getRowsParaAcao();
    if (!rows.length) return;

    var codigos = rows.map(function (r) { return r.CODREGISTRO; });

    MeuServiceProxy.executar({ CODREGISTRO: codigos })
        .then(function (resp) {
            var msg = ObjectUtils.getProperty(resp, 'responseBody.mensagem');
            MessageUtils.showInfo('Sucesso', msg);
            _dataset.refresh(Criteria('this.CODREGISTRO IN (' + codigos.join(',') + ')'));
        })
        .catch(function (err) {
            MessageUtils.showError('Erro', err.statusMessage);
        });
}
```

---

### PopUpParameter — Popup de parâmetros

Para coletar dados do usuário antes de executar uma ação:

```js
function abrirPopupFiltro() {
    // Construir parâmetros
    var pDATA     = PopUpParameter.buildDateParameter('DATA', 'Data de Referência', true);
    var pTIPO     = PopUpParameter.buildComboboxParameter('TIPO', 'Tipo', true, {
        'A': 'Add-on',
        'C': 'Customização'
    });
    var pCODPARC  = PopUpParameter.buildSearchInputParameter('CODPARC', 'Parceiro', false, 'Parceiro', 'CODPARC');
    var swAtivo   = PopUpParameter.buildSwitchParameter('ATIVO', 'Somente Ativos', false);

    // Valor inicial do switch
    if (swAtivo.value == null) swAtivo.value = 'S';

    var params = [pDATA, pTIPO, pCODPARC, swAtivo];
    var popup  = PopUpParameter.openPopUp(params, { size: 'lg' });

    popup.result
        .then(function (result) {
            // result contém os valores preenchidos pelo usuário
            MeuServiceProxy.executar(result)
                .then(function (resp) {
                    var msg = ObjectUtils.getProperty(resp, 'responseBody.mensagem');
                    MessageUtils.showInfo('Sucesso', msg);
                    _dataset.refresh();
                });
        })
        .catch(function () {
            // usuário cancelou o popup
        });
}
```

Builders disponíveis:
- `PopUpParameter.buildDateParameter(campo, label, obrigatorio)`
- `PopUpParameter.buildComboboxParameter(campo, label, obrigatorio, mapaOpcoes)`
- `PopUpParameter.buildSearchInputParameter(campo, label, obrigatorio, entidade, campoRetorno)`
- `PopUpParameter.buildSwitchParameter(campo, label, valorInicial)`

---

### SkApplicationInstance.openApp — Abrir outra tela

```js
// Abrir Central de Notas filtrando por NUNOTA
SkApplicationInstance.openApp(
    'br.com.sankhya.com.mov.CentralNotas',
    { NUNOTA: row.NUNOTA },
    true  // abre em nova aba
);
```

---

### Múltiplos dynaforms na mesma tela (mestre-detalhe)

Quando uma tela tem múltiplos `sk-dynaform`, o `onDynaformLoaded` é chamado uma vez para cada entidade. Use `getEntityName()` para identificar cada um:

```js
function onDynaformLoaded(dynaform, dataset) {
    if (dataset.getEntityName() === 'EntidadePrincipal') {
        _dynaformPrincipal = dynaform;
        _dsPrincipal = dataset;
        // configurar navegação, watches, etc.
    }

    if (dataset.getEntityName() === 'EntidadeDetalhe') {
        _dynaformDetalhe = dynaform;
        _dsDetalhe = dataset;

        // Desabilitar botões de CRUD no detalhe
        var navApi = dynaform.getNavigationAPI
            ? dynaform.getNavigationAPI()
            : dynaform.getNavigatorAPI();
        navApi.showAddButton(false);
        navApi.showRemoveButton(false);
        navApi.showCopyButton(false);
    }
}
```

**HTML com múltiplos dynaforms:**
```html
<sk-dynaform sk-entity-name="EntidadePrincipal"
             sk-dynaform-interceptor="ctrl"
             sk-on-dynaform-loaded="ctrl.onDynaformLoaded(dynaform, dataset)">
    <dynaform-entidade-principal>
        <sk-navigator></sk-navigator>
        <sk-right-top-bar>
            <button primary ng-click="ctrl.btnExecutar()">Executar</button>
        </sk-right-top-bar>
    </dynaform-entidade-principal>

    <dynaform-entidade-detalhe>
        <sk-right-top-bar>
            <button default ng-click="ctrl.btnCarregarDetalhe()">Carregar</button>
        </sk-right-top-bar>
    </dynaform-entidade-detalhe>
</sk-dynaform>
```

---

### Botões na barra superior (`sk-right-top-bar`)

Para adicionar botões contextuais na barra superior do dynaform, use `<sk-right-top-bar>` dentro do `<dynaform-nome-entidade>`:

```html
<dynaform-minha-entidade>
    <sk-navigator></sk-navigator>
    <sk-right-top-bar>
        <button primary ng-click="ctrl.btnPrincipal()">Ação Principal</button>
        <button ng-show="ctrl.exibeAcaoSecundaria()" brand ng-click="ctrl.btnSecundaria()">Secundária</button>
        <button ng-show="ctrl.exibeAcaoCancelar()" danger ng-click="ctrl.btnCancelar()">Cancelar</button>
    </sk-right-top-bar>
</dynaform-minha-entidade>
```

Variantes de estilo de botão: `primary`, `brand`, `info`, `warning`, `danger`, `default`.

Visibilidade condicional com `ng-show`:
```js
self.exibeAcaoSecundaria = function () {
    if (!_dataset) return false;
    var row = _dataset.getCurrentRowAsObject();
    if (!row) return false;
    return row.STATUS === 'P'; // exibe apenas quando status for 'P'
};
```

---

### $scope.$watch com arrow function

```js
// Watch simples em um campo
$scope.$watch(function () {
    if (!_dataset) return null;
    var row = _dataset.getCurrentRowAsObject();
    return row ? row.STATUS : null;
}, function (newVal, oldVal) {
    atualizarVisibilidade(newVal);
});

// Watch em múltiplos campos simultaneamente
$scope.$watch(
    function () { return [swA.value, swB.value, swC.value].join('|'); },
    function () {
        aplicarLogica();
        try { $scope.$applyAsync(); } catch(e) {}
    }
);

// Cancelar watch quando não for mais necessário
var unwatch = $scope.$watch(...);
// depois:
if (typeof unwatch === 'function') unwatch();
```

---

### AngularUtil.createDirective com ng-click e data-*

Para injetar elementos com comportamento Angular e dados customizados:

```js
var icone = AngularUtil.createDirective(
    'i',
    {
        title: 'Ir para central de notas',
        class: 'glyphicon glyphicon-circle-arrow-right',
        style: 'margin-left: 4px; cursor: pointer;',
        'data-campo': skFieldName,       // atributo data-* acessível via getAttribute
        'ng-click': 'irCentralNotas($event)'  // função no scope do elemento
    },
    fieldScope
);

el.appendChild(icone[0]);
fieldScope.$apply();
```

> A função referenciada em `ng-click` deve existir no `fieldScope` antes de chamar `createDirective`.

---

## API Reference (URLs internas)

**Base:** `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/docs/index.html`

Para acessar uma página específica, concatenar o hash:

| Módulo | Hash |
|---|---|
| API Index | `#/api` |
| snk | `#/api/snk` |
| snk.components.dataset | `#/api/snk.components.dataset` |
| sk-dataset | `#/api/snk.components.dataset.directive:sk-dataset` |
| sk-dsfield-md | `#/api/snk.components.dataset.directive:sk-dsfield-md` |
| sk-datagrid | `#/api/snk.components.datagrid.directive:sk-datagrid` |
| sk-dynaform | `#/api/snk.components.dynaform.directive:sk-dynaform` |
| sk-form | `#/api/snk.form.directive:sk-form` |
| sk-navigator | `#/api/snk.components.navigator.directive:sk-navigator` |
| sk-filter-panel | `#/api/snk.components.filterpanel.directive:sk-filter-panel` |
| MessageUtils | `#/api/snk.core.util.service:MessageUtils` |
| SanPopup | `#/api/snk.components.popup.service:SanPopup` |
| DatasetOnlineFilter | `#/api/snk.components.dataset.service:DatasetOnlineFilter` |
| sk-text-input | `#/api/snk.components.input.directive:sk-text-input` |
| sk-combobox | `#/api/snk.components.input.directive:sk-combobox` |
| sk-switch | `#/api/snk.components.input.directive:sk-switch` |
| sk-date-input | `#/api/snk.components.input.directive:sk-date-input` |
| sk-number-input | `#/api/snk.components.input.directive:sk-number-input` |
| sk-pesquisa-input | `#/api/snk.components.input.directive:sk-pesquisa-input` |
| sk-application | `#/api/snk.core.application.directive:sk-application` |

**Documentação principal:**

| Página | URL |
|---|---|
| Home | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!/` |
| Conceitos | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!conceitos` |
| Principais Componentes | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!componentes` |
| Temas/Less | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!temasless` |
| JSON/XML | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!jsonxml` |
| Build | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!build` |
| De/Para Flex→Html5 | `http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!depara` |
