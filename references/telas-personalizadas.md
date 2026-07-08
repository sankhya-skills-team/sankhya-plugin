# Telas Personalizadas (UI)

## Visão Geral

Telas Personalizadas permitem criar interfaces customizadas quando os Formulários Dinâmicos não são suficientes e você precisa de controle total sobre a apresentação. Usa tecnologia HTML5/xhtml5 com AngularJS (sankhya-js) — ideal para dashboards, relatórios complexos e layouts específicos.

## Arquitetura

Dois componentes principais:

1. **Arquivo da view (`.xhtml5`)** — desenvolvido em `vc/src/main/webapp/html5/`
2. **Declaração no menu** — vincula o arquivo via tag `<ui>` no dicionário de dados

## Estrutura de Diretórios

```
vc/src/main/webapp/
└── html5/
    └── NomeTela/
        ├── NomeTela.html       ← view principal
        ├── NomeTela.js         ← controller AngularJS
        ├── NomeTela.css        ← estilos
        └── launcher/
            ├── NomeTela.body   ← boilerplate Addon Studio
            └── NomeTela.include
```

## Declaração no Menu

**Arquivo:** `datadictionary/menu.xml`

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <menu id="GGB_MENU" description="Meu Addon" icon="/$ctx/assets/icon.png">
        <ui id="GGB_MINHA_TELA"
            url="/$ctx/GGB_MinhaEntidade.xhtml5"
            description="Minha Tela"/>
    </menu>
</metadados>
```

## Atributos da Tag `<ui>`

| Atributo | Descrição | Exemplo |
|---|---|---|
| `id` | Identificador único do item de menu | `GGB_MINHA_TELA` |
| `url` | Caminho para o arquivo `.xhtml5` | `/$ctx/GGB_MinhaEntidade.xhtml5` |
| `description` | Texto exibido no menu | `Minha Tela` |

## Variável `/$ctx/`

A variável `/$ctx/` é **fundamental** — é substituída em tempo de execução pelo caminho raiz do add-on. Sempre utilize no início da URL.

---

## Estrutura Mínima com sk-dynaform

O padrão mais comum é usar `sk-dynaform` com um interceptor (`IDynaformInterceptor`):

**HTML:**
```html
<sk-application sk-app-module="GGB_MinhaTelaApp">
    <div ng-controller="GGB_MinhaTelaController as ctrl">
        <sk-dynaform
            sk-entity-name="GGB_MinhaEntidade"
            sk-dynaform-interceptor="ctrl"
            sk-skip-start-page="true"
            sk-default-mode="master"
            sk-hide-tour="true"
            sk-on-dynaform-loaded="ctrl.onDynaformLoaded(dynaform, dataset)">

            <dynaform-g-g-b_-minha-entidade>
                <sk-navigator></sk-navigator>
            </dynaform-g-g-b_-minha-entidade>

        </sk-dynaform>
    </div>
</sk-application>
```

---

## Regra de Nomenclatura da Tag `<dynaform-*>`

> **Crítico:** esta regra não está na documentação oficial. Errar o nome da tag faz o dynaform não renderizar corretamente.

A tag `<dynaform-*>` é derivada do **nome da entidade** (`sk-entity-name`) seguindo a convenção **kebab-case do AngularJS**: cada letra maiúscula vira um segmento separado por traço, tudo em minúsculo.

**Fórmula:** cada letra maiúscula → `-` + letra minúscula (exceto a primeira)

| Nome da Entidade | Tag HTML |
|---|---|
| `GGB_Config` | `<dynaform-g-g-b_-config>` |
| `GGB_Repositorio` | `<dynaform-g-g-b_-repositorio>` |
| `MeuAddon_Cabecalho` | `<dynaform-meu-addon_-cabecalho>` |
| `MeuAddon_ItemDetalhe` | `<dynaform-meu-addon_-item-detalhe>` |
| `MinhaEntidade` | `<dynaform-minha-entidade>` |
| `PedidoItem` | `<dynaform-pedido-item>` |

**Exemplos reais do projeto ggbridge:**
```html
<!-- Entidade: GGB_Config -->
<dynaform-g-g-b_-config>
    <sk-navigator></sk-navigator>
</dynaform-g-g-b_-config>

<!-- Entidade: GGB_Repositorio -->
<dynaform-g-g-b_-repositorio>
    <sk-navigator></sk-navigator>
</dynaform-g-g-b_-repositorio>
```

**Como derivar o nome manualmente:**
1. Pegue o nome da entidade: `GGB_Config`
2. Para cada letra maiúscula (exceto a primeira), insira um `-` antes e converta para minúscula
3. `G` → `g`, `G` → `-g`, `B` → `-b`, `_` permanece, `C` → `-c`
4. Resultado: `g-g-b_-config`
5. Prefixo obrigatório: `dynaform-g-g-b_-config`

---


**JS:**
```js
angular.module('GGB_MinhaTelaApp', ['snk'])
    .controller('GGB_MinhaTelaController', [
        'MessageUtils', 'ObjectUtils', '$scope', '$timeout',
        function (MessageUtils, ObjectUtils, $scope, $timeout) {
            const self = this;
            let _dynaform;
            let _dataset;

            ObjectUtils.implements(self, IDynaformInterceptor);
            self.init = init;
            self.onDynaformLoaded = onDynaformLoaded;

            function init() {}

            function onDynaformLoaded(dynaform, dataset) {
                if (dataset.getEntityName() === 'GGB_MinhaEntidade') {
                    _dynaform = dynaform;
                    _dataset = dataset;

                    // Configurar botões de navegação
                    var navApi = dynaform.getNavigationAPI
                        ? dynaform.getNavigationAPI()
                        : dynaform.getNavigatorAPI();

                    navApi.showAddButton(true);
                    navApi.showRemoveButton(true);
                    navApi.showCopyButton(false);
                }
            }
        }
    ]);
```

---

## Chamando um @Service do Frontend

Use `ServiceProxy` para chamar serviços Java. O formato do nome é `addonname@ServiceNameSP.metodo`:

```js
angular.module('GGB_MinhaTelaApp', ['snk'])

    .factory('MeuServiceProxy', ['ServiceProxy', function (ServiceProxy) {
        function executar(dto) {
            return ServiceProxy.callService(
                'integradorgitlabgithub@MeuServiceSP.executar',
                { dto: dto }
            );
        }
        return { executar: executar };
    }])

    .controller('GGB_MinhaTelaController', [
        'MessageUtils', 'ObjectUtils', '$scope', 'MeuServiceProxy',
        function (MessageUtils, ObjectUtils, $scope, MeuServiceProxy) {
            // ...
            function executarAcao() {
                MeuServiceProxy.executar({ CODCONFIG: 1 })
                    .then(function (resp) {
                        var msg = resp.responseBody && resp.responseBody.mensagem;
                        MessageUtils.showInfo('Sucesso', msg);
                    })
                    .catch(function (err) {
                        MessageUtils.showError('Erro', err.statusMessage || 'Falha na operação.');
                    });
            }
        }
    ]);
```

> O nome do addon no `callService` é o `rootProject.name` do `settings.gradle` em **minúsculas**.

---

## Manipulação do DOM com $timeout

O dynaform renderiza de forma assíncrona. Toda manipulação de DOM deve ser feita dentro de `$timeout(fn, 300)`:

```js
function onDynaformLoaded(dynaform, dataset) {
    if (dataset.getEntityName() === 'GGB_MinhaEntidade') {
        _dynaform = dynaform;
        _dataset = dataset;

        // ✅ Correto — aguarda o dynaform renderizar
        $timeout(function () {
            ocultarCampo('CAMPOINTERNO');
            adicionarIconeInfo('NOMEPROJETO', 'Texto de ajuda aqui');
        }, 300);
    }
}
```

---

## Validação no Save (setSaveHandler)

Para bloquear a persistência com validação customizada:

```js
_dataset.setSaveHandler(function () {
    var row = _dataset.getCurrentRowAsObject();
    if (!row) return true;

    var manutencaoAtiva = row.MANUTENCAO === 'S';
    if (manutencaoAtiva && (!row.URLGLLEGADO || row.URLGLLEGADO.trim() === '')) {
        MessageUtils.showError('Campo obrigatório',
            'O campo "URL Legado" é obrigatório quando "Manutenção" estiver marcado.');
        return false; // bloqueia o save
    }
    return true; // permite o save
});
```

---

## Campo Required Dinâmico

Para tornar um campo obrigatório/opcional em tempo de execução:

```js
function setarRequired(skFieldName, obrigatorio) {
    var el = document.querySelector('[sk-field-name="' + skFieldName + '"]');
    if (!el) return;

    var s = angular.element(el).scope();
    if (!s || !s.properties) return;

    s.properties.required = obrigatorio;

    var inputScope = angular.element(el.querySelector('input')).scope();
    if (inputScope) inputScope.required = obrigatorio;

    $timeout(function () { s.$digest(); }, 0);
}
```

---

## Visibilidade de Campos Dinâmica

Para mostrar/ocultar campos com base em condições:

```js
function atualizarVisibilidade(fieldName, visivel) {
    var el = document.querySelector('[sk-field-name="' + fieldName + '"]');
    if (!el) return;
    var container = el.closest('sk-field-container')
        || el.closest('.field-container')
        || el.parentElement;
    if (container) {
        container.style.display = visivel ? '' : 'none';
    }
}

// Reagir a mudança de valor com $watch
$scope.$watch(function () {
    if (!_dataset) return null;
    var row = _dataset.getCurrentRowAsObject();
    return row ? row.MANUTENCAO : null;
}, function (newVal) {
    var ativo = newVal === 'S' || newVal === true;
    atualizarVisibilidade('URLGLLEGADO', ativo);
    setarRequired('URLGLLEGADO', ativo);
});
```

---

## Combobox Dinâmico (input + datalist)

Para comboboxes populados via serviço, use `input + datalist` em vez de `<select>` — evita problemas de foco do AngularJS:

```js
function injetarSelectGrupos(grupos) {
    var el = document.querySelector('[sk-field-name="IDGRUPOGL"]');
    if (!el) return;

    // Ocultar o input nativo do dynaform
    var inputNativo = el.querySelector('input');
    if (inputNativo) inputNativo.style.display = 'none';

    // Evitar duplicação
    if (el.querySelector('.meu-wrapper')) return;

    var listId = 'meu-datalist';

    // Criar datalist com as opções
    var datalist = document.createElement('datalist');
    datalist.id = listId;
    grupos.forEach(function (grupo) {
        var opt = document.createElement('option');
        opt.value = grupo.fullPath;
        datalist.appendChild(opt);
    });

    // Criar input de busca
    var inputBusca = document.createElement('input');
    inputBusca.type = 'text';
    inputBusca.className = 'form-control meu-wrapper';
    inputBusca.setAttribute('list', listId);
    inputBusca.placeholder = 'Digite para filtrar...';
    inputBusca.style.cssText = 'flex: 1; height: 30px; font-size: 13px;';

    // Ao selecionar, gravar o ID (não o label) no dataset
    inputBusca.addEventListener('change', function () {
        var grupo = grupos.find(function (g) { return g.fullPath === inputBusca.value; });
        if (grupo && _dataset) {
            _dataset.setFieldValue('IDGRUPOGL', grupo.id);
        } else if (!inputBusca.value && _dataset) {
            _dataset.setFieldValue('IDGRUPOGL', '');
        }
    });

    angular.element(el).css({ display: 'inline-flex', 'align-items': 'center' });
    el.appendChild(datalist);
    el.appendChild(inputBusca);
}
```

---

## Ícone de Ajuda (tooltip)

Para adicionar ícone de informação com tooltip em um campo:

```js
function adicionarIconeInfo(skFieldName, textoAjuda) {
    var el = document.querySelector('[sk-field-name="' + skFieldName + '"]');
    if (!el) return;
    if (el.querySelector('.meu-info-icon')) return; // evitar duplicação

    var $el = angular.element(el);
    $el.css({ display: 'inline-flex', 'align-items': 'center' });

    var icone = AngularUtil.createDirective(
        'i',
        {
            title: textoAjuda,
            class: 'glyphicons glyphicons-circle-question-mark meu-info-icon',
            style: 'margin-left: 6px; cursor: help; font-size: 14px; color: #555;'
        },
        $el.scope()
    );

    el.appendChild(icone[0]);
    $el.scope().$apply();
}
```

> `AngularUtil` deve ser injetado no controller: `'AngularUtil'` na lista de dependências.

---

## Encoding dos Arquivos

Definido pelo `.editorconfig` do projeto:

| Tipo | Encoding |
|---|---|
| `.java`, `.kt`, `.xml` | `latin1` (iso-8859-1) |
| `.js`, `.html` | `utf-8` |

Caracteres acentuados em XMLs devem usar entidades HTML ou ser escritos em latin1. Nos arquivos `.js` e `.html`, UTF-8 é suportado normalmente.

---

## Boas Práticas

- Toda manipulação de DOM após `onDynaformLoaded` deve usar `$timeout(fn, 300)`
- Use `setSaveHandler` para validações que dependem de múltiplos campos
- Use `input + datalist` para comboboxes dinâmicos — evita problemas de foco com `<select>`
- Sempre verifique duplicação antes de injetar elementos no DOM
- Use `_dataset.setFieldValue('CAMPO', valor)` para gravar valores programaticamente

## Antipadrões

- Manipular DOM diretamente em `onDynaformLoaded` sem `$timeout` — o dynaform ainda não renderizou
- Usar `<select>` nativo para comboboxes dinâmicos — causa problemas de foco no AngularJS
- Esquecer `/$ctx/` na URL do menu — resulta em 404
- IDs duplicados em `<ui>` e `<dynamicForm>` — causa conflitos
- Prefixo `AD_` em IDs — reservado pelo Sankhya

## Fonte

https://developer.sankhya.com.br/docs/07_telas
