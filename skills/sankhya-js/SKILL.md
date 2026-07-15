---
name: sankhya-js
description: Use ao escrever, modificar ou revisar codigo AngularJS 1.x do framework frontend proprietario sankhya-js do Sankhya OM — telas HTML5, consumo de servicos backend via /mge/service.sbr (ServiceProxy, FluidBuilder), componentes (button, popup, grid, dataset, datagrid, wizard, pesquisa, etc.), metadados de entidades via MetadataProvider, i18n via SkI18nService, registro dinamico de modulos via $SkInjectorProvider, SkComponentRegistry, SkWorkspace, ou telas compartilhadas entre modulos em src/commons. Invocar em arquivos do repositorio sibling ../sankhya-js e no consumo pelos modulos VC (MGE-Base-VC, MGE-Fin-VC, MGE-Checkout-VC) via JSPs.
---

# sankhya-js

Framework frontend proprietario baseado em **AngularJS 1.x** (nao Angular 2+). Publicado como `@sankhya-frontend/sankhya-js` (`package.json:2`), com `moduleName: "snk"` e `distName: "snk"`/`"jiva"` (`package.json:4-6`). Build: **Grunt 0.4.5** + Babel + Less (`package.json:30-40`).

## Regras nao-negociaveis

1. **AngularJS 1.x** (nao Angular moderno). Use `angular.module(...)`, DI por array, `$scope`, `$q`, `$http`. Nao use sintaxe de Angular 2+.
2. **Padrao de servico backend e `/{module}/service.sbr`** (`serviceproxy.service.js:150`). Nunca monte a URL manualmente — use `ServiceProxy.callService` ou `ServiceProxy.builder()`.
3. **Prefixo de modulo no `serviceName`**: formato `"modulo@Servico.metodo"` (ex.: `"mgecom@FichaParceiroSP.getFinanceiros"`). Sem prefixo, `defModule = "mge"` (`serviceproxy.service.js:151-157`).
4. **Registro de modulos sob `snk.*`**: `snk.core.*`, `snk.components.*`, `snk.commons`. Cada componente/service vive em seu proprio `angular.module(...)` com `.module.js` declarando a dependencia.
5. **Metadados de entidade com locale**: `MetadataProvider` cacheia por `entity + '-' + locale` (`metadataprovider.service.js:43-45`). Trocar idioma invalida o cache implicitamente.
6. **Handles de `SkComponentRegistry` sao globais** — duplicidade gera `console.warn` e retorna `angular.noop` por default (`componentregistry.service.js:114-118`).
7. **Sem emojis. Sem UTF-8 BOM.** Encoding ISO-8859-1 no produto (mas JS em si e UTF-8). Textos fixos em PT-BR vao via `SkI18nService`.

## Quando NAO usar esta skill

- Codigo Angular 2+ / Angular moderno (standalone components, signals, RxJS) — `sankhya-js` e **AngularJS 1.x** (`angular.module`, `$scope`, `$q`).
- Microfrontends React do `mgefin-bff-module` (Contas a Receber, Movimentacao Bancaria) — React 18 + Vite, stack independente.
- UI Adobe Flex (MXML/AS3) do `vc-flex` — consome os mesmos servicos backend mas a UI e Flex, nao AngularJS.
- Telas GWT legadas — convivem com HTML5 no mesmo produto mas usam GWT Java, nao `sankhya-js`.

## Estrutura do repositorio

```
src/
  core/          # infra do framework: ServiceProxy, FluidBuilder, MetadataProvider,
                 # SkComponentRegistry, SkWorkspace, $SkInjectorProvider, util/*
  components/    # 110 widgets reutilizaveis (button, popup, grid, datepicker, ...)
  commons/       # telas compartilhadas entre modulos (chamadas por mais de um modulo)
  i18n/          # SkI18nService + bundles
  assets/        # imagens, fonts, svg
  mocks/         # mocks para desenvolvimento isolado
```

`core/` e infraestrutura do framework. `components/` sao componentes de UI — entre eles, o **`sk-dataset`** (`dataset.controller.js`, ~7600 linhas) e a primitiva central de binding de dados (CRUD, listeners, metadados, navegacao). `commons/` contem telas (controller + service + html) que sao invocadas por mais de um modulo — por isso vivem fora dos modulos VC.

## Padrao canonico 1 — Chamar um servico backend

```javascript
angular.module('snk.commons').controller('MinhaCtrl',
  ['ServiceProxy', function(ServiceProxy) {

    ServiceProxy.callService('mgecom@FichaParceiroSP.getFinanceiros', {
      codParc: { $: codParc }
    }).then(function(data) {
      $scope.financeiros = data.responseBody;
    });

  }]);
```

Ou com builder:

```javascript
ServiceProxy.builder()
  .serviceName('mgecom@FichaParceiroSP.getFinanceiros')
  .params({ codParc: { $: codParc } })
  .ignoreLoadingBar(true)
  .call();
```

Builder em `serviceproxy.service.js:44-53`; `callService` em `:122`.

## Padrao canonico 2 — Declarar um componente (directive)

```javascript
// meucomp.module.js
angular.module('snk.components.meucomp', []);

// meucomp.directive.js
angular.module('snk.components.meucomp')
  .directive('skMeucomp', [function() {
    return {
      restrict: 'E',
      scope: { value: '=' },
      templateUrl: 'components/meucomp/meucomp.html',
      controller: ['$scope', function($scope) {
        // ...
      }]
    };
  }]);
```

Um `.module.js` por pasta declarando o modulo vazio (`button.module.js`); demais arquivos (`*.directive.js`, `*.service.js`, `*.controller.js`) usam `angular.module('snk.components.meucomp')` **sem array de dependencias** (`button.directive.js`).

## Padrao canonico 3 — Compartilhar instancia entre controllers

```javascript
// Registrar
var deregister = SkComponentRegistry.register(self, 'minhaInstancia');
$scope.$on('$destroy', deregister);

// Consumir (em outro controller)
SkComponentRegistry.get('minhaInstancia').then(function(instance) {
  instance.fazerAlgo();
});
```

`get()` retorna promise que resolve assim que o `register()` correspondente for chamado (`componentregistry.service.js:80,107`).

## Padrao canonico 4 — Obter metadados de entidade

```javascript
MetadataProvider.getEntityMetadata('Produto').then(function(entities) {
  var produto = entities['Produto'];
  // produto.fields, produto.relations, produto.tableName
});

// Com relacoes 1-1 e 1-N
MetadataProvider.getEntityAndRelationsMetadata(
  'Parceiro', null, /*includeOneToMany*/ true
).then(function(result) {
  // result.entities, result.relations, result.oneToManyRelations
});
```

GET sincrono contra `/mge/metadataProvider.mge/{entity}.js` (`metadataprovider.service.js:103`). Deduplica requests em voo via `pendingEntityRequests`.

## Padrao canonico 5 — Registro dinamico de modulos

AngularJS nao permite adicionar dependencias apos `bootstrap`. O `$SkInjectorProvider` faz isso via reflection do `_invokeQueue`/`_configBlocks`:

```javascript
angular.module('meuApp').config(['$SkInjectorProvider',
  function($SkInjectorProvider) {
    $SkInjectorProvider.register(angular.module('meuApp'),
      ['snk.components.popup', 'snk.components.button']);
  }]);
```

Permite telas carregadas **apos** o bootstrap declararem dependencias novas (`framework.config.js:54-73`).

## Armadilha critica — tela HTML5 custom roda em iframe + colide com Bootstrap

Tela HTML5 (`/$ctx/<Nome>.xhtml5`) abre dentro de um **iframe**; o framework injeta o `.html` da tela via `ng-include` em `#pageWrapper > #page` e carrega **`bootstrap.min.css` + `snk.min.css` ANTES** da CSS da tela. Isso gera dois problemas que NAO aparecem no `node --check` nem na leitura do codigo — so renderizando:

1. **Bootstrap reserva nomes de classe genericos.** Se a CSS da tela usa esses nomes, o Bootstrap (carregado antes, mas com regras `!important` ou propriedades que a tela nao redeclara) sobrescreve silenciosamente:
   - `.show` -> Bootstrap define `.show{display:block !important}`. Mata qualquer `.algo.show{display:flex}` (modal nao centraliza, kanban/colunas empilham). Corrija com `display:flex !important` em seletor de maior especificidade (`.minha-classe.show`), ou nao use `.show`.
   - `.modal` -> Bootstrap define `.modal{position:fixed;top:0;left:0;...}`. Se a tela usa `.modal` como o card e nao redeclara `position`, o card fica preso no canto superior-esquerdo, fora do flex-center do backdrop. Corrija com `position:relative; inset:auto` no `.modal`.
   - Outros reservados: `.modal-backdrop`, `.modal-header/body/footer/title`, `.modal-dialog`, `.active`, `.container`, `.row`, `.col`, `.card`, `.btn`, `.fade`, `.collapse`.
   - **Melhor pratica:** escopar TODA a CSS da tela sob uma classe-raiz propria (ex.: `.minha-tela .modal { ... }`) ou usar prefixo proprio nos nomes. Nunca depender de nome generico cru.

2. **Cadeia de altura.** Nao confie em `height:100vh`/`min-height:100vh` no root da tela: `#pageWrapper`/`#page` crescem ate a altura do conteudo (ex.: 2747px num iframe de 1000px), o `<main>` nao rola e scroll infinito nunca dispara. Trave `#pageWrapper, #page { height:100% !important; min-height:0 !important }` e use `height:100%` (nao `100vh`) no root, com `min-height:0` nos filhos flex que devem rolar.

3. **Verifique renderizando, nao lendo.** Para bug de layout em embedding, dirija a URL viva com browser headless (Playwright/`google-chrome`) e compare **estilos computados** (`getComputedStyle`) — `display`, `position`, `getBoundingClientRect()`. Foi o unico jeito de achar a colisao `.show`/`.modal` (o CSS-fonte parecia correto).

## Onde aprofundar

- [reference/api-cheatsheet.md](reference/api-cheatsheet.md) — APIs de `ServiceProxy`, `FluidBuilder`, `MetadataProvider`, `SkComponentRegistry`, `SkI18nService`, `SkWorkspace`, `$SkInjectorProvider`
- [reference/patterns.md](reference/patterns.md) — 11 padroes canonicos + tabela de decisao
- [reference/anti-patterns.md](reference/anti-patterns.md) — 14 praticas a evitar, util em triagem de bug
- [reference/gotchas.md](reference/gotchas.md) — armadilhas de API
- [reference/build-grunt.md](reference/build-grunt.md) — build e publicacao Grunt, ordem de concatenacao, JSHint, temas LESS
- [reference/bootstrap-release.md](reference/bootstrap-release.md) — bootstrap manual da tela, versionamento release.snk, branch canaria
- [reference/code-quality.md](reference/code-quality.md) — padroes de codigo, performance (digest), seguranca, ngdocs, god screens

### Componentes

- [reference/application.md](reference/application.md) — `sk-application`: container raiz, singleton, ciclo de vida
- [reference/tabs.md](reference/tabs.md) — `sk-tab` + `sk-tab-item`: abas estruturais
- [reference/inputs.md](reference/inputs.md) — `sk-text-input`, `sk-combobox`, `sk-date-time-input`, `sk-switch`, `sk-checkbox`
- [reference/navigator.md](reference/navigator.md) — `sk-navigator`: barra CRUD + navegacao
- [reference/filter-panel.md](reference/filter-panel.md) — `sk-filter-panel` + `sk-filter-panel-btn`
- [reference/sidenav.md](reference/sidenav.md) — `sk-sidenav` e variantes
- [reference/wizard.md](reference/wizard.md) — `sk-wizard` + `sk-step` + botoes
- [reference/form.md](reference/form.md) — `sk-form`, `sk-dynaform`, interceptors
- [reference/dataset.md](reference/dataset.md) — `sk-dataset`: entity/standalone, listeners, CRUD
- [reference/datagrid.md](reference/datagrid.md) — `sk-datagrid`: backends, custom columns
- [reference/messages-popup.md](reference/messages-popup.md) — `MessageUtils` + `SanPopup`
- [reference/pesquisa.md](reference/pesquisa.md) — `sk-pesquisa-input` + `SkPesquisaService`

### Templates

- [templates/component-directive.js](templates/component-directive.js) — esqueleto de directive + uso em HTML
- [templates/service-call-simple.js](templates/service-call-simple.js) — `callService` + `.then` (caso canonico)
- [templates/service-call-builder.js](templates/service-call-builder.js) — builder, options, abort, erro manual
- [templates/dataset-standalone.js](templates/dataset-standalone.js) — `sk-dataset sk-standalone` + handlers + `sk-dsfield-md`
- [templates/wizard-step.js](templates/wizard-step.js) — `sk-wizard` com `$step` API + `sk-context` + validacao
- [templates/popup-custom.js](templates/popup-custom.js) — `SanPopup.open` + `$popupInstance` + evento `popup.closing`
- [templates/filter-panel-interceptor.js](templates/filter-panel-interceptor.js) — `IFilterPanelInterceptor` + `FilterPanelService` + `<default-group>`/`<custom-group>`
