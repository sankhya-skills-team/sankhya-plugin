# sankhya-js — Padroes de uso

Padroes observados no codigo real do `sankhya-js`. Use como receita ao escrever novas telas, componentes ou integracoes.

---

## Padrao 1 — Servico backend simples

Uso: tela precisa chamar um servico do backend e tratar a resposta.

```javascript
angular.module('snk.commons')
  .controller('MinhaCtrl', ['$scope', 'ServiceProxy',
    function($scope, ServiceProxy) {

      ServiceProxy.callService('mgecom@FichaParceiroSP.getFinanceiros', {
        codParc: { $: $scope.codParc }
      }).then(function(data) {
        $scope.dados = data.responseBody;
      }).catch(function(err) {
        // Popup de erro ja e exibido por default, a nao ser que
        // config.errorHandler / config.ignorePopUpErrorMsgs sejam setados
      });
    }
  ]);
```

Evidencia real no commons: `FichaParceiroContainer.service.js`.

**Observacoes:**
- `serviceName` com prefixo de modulo (`mgecom@`, `mgefin@`, `mge@`). Sem prefixo vai para `mge`.
- Campos primitivos no `params` usam notacao `{ $: valor }` (herdada do transform XML/JSON do backend).
- Resposta e desserializada; usualmente em `data.responseBody`.

---

## Padrao 2 — Builder fluente

Uso: chamada com mais de uma option ou reuso do builder.

```javascript
var chamador = ServiceProxy.builder()
  .serviceName('mgecom@CentralItemNota.getItens')
  .ignoreLoadingBar(true);

chamador.params({ nunota: { $: 12345 } }).call()
  .then(handleItens);
```

`ignoreLoadingBar` e `asOption` — vai para `options`, nao para `variables`. `.call()` e o alias registrado em `.buildFn(..., 'call')` (`serviceproxy.service.js:52`).

---

## Padrao 3 — Componente (directive) com template

Uso: widget reutilizavel. Sempre tres arquivos: `.module.js`, `.directive.js`, `.html` (opcional), `.less` (opcional).

```javascript
// meucomp.module.js
angular.module('snk.components.meucomp', []);

// meucomp.directive.js
angular.module('snk.components.meucomp')
  .directive('skMeucomp', ['MinhaDep', function(MinhaDep) {
    return {
      restrict: 'E',
      scope: {
        value: '=',
        onChange: '&'
      },
      templateUrl: 'components/meucomp/meucomp.html',
      controller: ['$scope', function($scope) {
        $scope.click = function() {
          $scope.onChange({ value: $scope.value });
        };
      }]
    };
  }]);
```

**Checklist:**
- [ ] `.module.js` declara com `[]` (array vazio de dependencias)
- [ ] Demais arquivos usam `angular.module('snk.components.<nome>')` SEM array
- [ ] Prefixo `sk-` no HTML (`<sk-meucomp>`), `skMeucomp` em JS
- [ ] HTML template servido via `grunt-html2js` a partir do template cache

Evidencia simples: `button.module.js` + `button.directive.js`.

---

## Padrao 4 — Componente composto (modulo + directive + service)

Uso: componente com logica/estado proprio. Multiplos arquivos no mesmo modulo.

Estrutura: `src/components/popup/`
```
popup.module.js             # angular.module('snk.components.popup', [])
popup.service.js            # logica de empilhamento
popupstack.service.js       # estado global
popupwindow.directive.js    # renderizacao
popuptransclude.directive.js
popupanimation.directive.js
popupbackdrop.directive.js
```

Todos chamam `angular.module('snk.components.popup')` sem array de dependencias (reusam o modulo declarado em `popup.module.js`).

---

## Padrao 5 — Compartilhar instancia entre controllers

Uso: duas telas/controllers precisam conversar sem ter relacao de parente no DOM.

```javascript
// ControllerPai
angular.module('snk.commons').controller('Pai',
  ['$scope', 'SkComponentRegistry', function($scope, SkComponentRegistry) {
    var self = this;
    self.refreshLista = refreshLista;

    var deregister = SkComponentRegistry.register(self, 'meuContexto');
    $scope.$on('$destroy', deregister);
  }]);

// ControllerFilho (em outra tela/pop-up)
angular.module('snk.commons').controller('Filho',
  ['SkComponentRegistry', function(SkComponentRegistry) {
    SkComponentRegistry.get('meuContexto').then(function(pai) {
      pai.refreshLista();
    });
  }]);
```

**Observacoes:**
- `get()` **empilha** o deferred ate que o `register()` correspondente ocorra. Util para ordem de inicializacao nao-deterministica.
- Handle e global — conflito gera `console.warn` e `register` retorna `angular.noop` (nao sobrescreve por padrao).
- Passar `$scope` como terceiro argumento auto-desregistra no `$destroy`.

Evidencia: `componentregistry.service.js:107-150`.

---

## Padrao 6 — Metadados de entidade com relacoes

Uso: tela dinamica que precisa saber campos, tipos e relacoes de uma entidade.

```javascript
MetadataProvider.getEntityAndRelationsMetadata(
  ['Parceiro', 'Produto'],
  function filtraRelacao(entity, field) {
    return field.name !== 'PRODUTOHIST'; // ignora FKs especificas
  },
  /*includeOneToMany*/ true
).then(function(result) {
  var parceiro = result.entities['Parceiro'];
  var relacoes = result.relations;         // 1-1 (fk)
  var filhos = result.oneToManyRelations;  // 1-N
});
```

**Observacoes:**
- `filterFn` recebe `(entity, field)` e decide se a FK dele deve ser incluida nas relacoes 1-1.
- 1-N so vem com `includeOneToMany: true`.
- Chaves no `entities` sao o nome da entidade **sem** sufixo de locale (o sufixo so existe internamente no cache).

Evidencia: `metadataprovider.service.js:185-235`.

---

## Padrao 7 — Client events

Uso: servico do backend envia eventos que o frontend precisa reagir (ex.: confirmar ação, abrir wizard).

```javascript
// Registrar
var handler = function(event, recaller) {
  if (event.data.confirm) {
    recaller.recall(); // re-executa a mesma chamada apos confirmacao
  }
};

var registration = ServiceProxy.addClientEvent('CONFIRMACAO_SAIDA', handler);

// Desregistrar quando a tela morre
$scope.$on('$destroy', function() {
  registration.unregistry();
});
```

O backend retorna `data.clientEvents = [{ id: 'CONFIRMACAO_SAIDA', ...payload }]` e o frontend invoca todos os handlers registrados (`serviceproxy.service.js:309-322`).

---

## Padrao 8 — i18n em controller e template

```javascript
// Controller
angular.module('snk.commons').controller('Minha',
  ['$scope', 'SkI18nService', function($scope, SkI18nService) {
    $scope.mensagem = SkI18nService.instant('MinhaTela.mensagem');
    $scope.msgComParam = SkI18nService.instant('MinhaTela.comValor', ['10']);
    // Se for array, posicoes viram p0, p1, ... no bundle
    // Bundle: { "comValor": "Total: {{p0}}" }
  }]);
```

```html
<!-- Template com filter -->
<span>{{ 'MinhaTela.mensagem' | translate }}</span>
```

Tambem ha o provider `i18n` injetavel como funcao: `i18n('chave', [10])`.

Evidencia: `i18n.service.js:17,101-113,116-122`.

---

## Padrao 9 — Download de arquivo

```javascript
// chave vem do backend (ex.: chaveArquivo gerado por upload ou geracao de PDF)
SkWorkspace.downloadFile(null, chaveArquivo, 'pdf', { foo: 'bar' });
```

Se o workspace do GWT estiver disponivel, usa `workspace.downloadFile`. Caso contrario, abre nova aba com URL `/mge/visualizadorArquivos.mge?chaveArquivo=X&foo=bar` (`workspace.service.js:99-113`).

---

## Padrao 10 — Registrar modulo dinamicamente em tela dependente

Uso: tela em `commons` ou em modulo externo precisa de um componente `snk.components.*` que nao estava no modulo raiz no bootstrap.

```javascript
angular.module('minhaTelaApp', [])
  .config(['$SkInjectorProvider', function($SkInjectorProvider) {
    $SkInjectorProvider.register(
      angular.module('minhaTelaApp'),
      ['snk.components.popup', 'snk.components.datepicker']
    );
  }]);
```

Evidencia: `framework.config.js:54-73`.

---

## Padrao 11 — Tela compartilhada em `src/commons/`

Uso: a tela e invocada por mais de um modulo (ex.: "Central de Notas" aberta a partir do Comercial e do Financeiro). Por isso nao vive dentro do codigo de um modulo especifico, e sim em `src/commons/<pasta>/`.

Estrutura tipica:
```
src/commons/fichaparceiro/
  fichaparceiro.module.js            # angular.module('snk.commons.fichaparceiro', [])
  fichaparceiro.controller.js
  fichaparceiro.service.js
  fichaparceiro.html
  FichaParceiroContainer/
    FichaParceiroContainer.directive.js
    FichaParceiroContainer.service.js
```

O modulo `snk.commons` agrega as commons (`commons.module.js`). Cada subpasta declara seu proprio sub-modulo e o registra onde for preciso.

Servicos em commons usam `angular.module('snk.commons')` diretamente, como em `FichaParceiroContainer.service.js:1-3`.

---

## Tabela de decisao

| Precisa... | Use |
|---|---|
| Chamar servico backend | `ServiceProxy.callService` ou `ServiceProxy.builder().call()` |
| Reagir a evento do backend | `ServiceProxy.addClientEvent(id, handler)` |
| Encadear chamadas sequenciais no mesmo servico | `ServiceProxy.addSerializedService(name)` |
| Abortar request em voo | guardar a promise e chamar `.abort()` |
| Obter estrutura de entidade | `MetadataProvider.getEntityMetadata` |
| Obter entidade + FKs | `MetadataProvider.getEntityAndRelationsMetadata` |
| Compartilhar instancia entre controllers | `SkComponentRegistry.register`/`.get` |
| Criar widget UI | directive em `snk.components.<nome>` com `.module.js` + `.directive.js` |
| Traduzir texto estatico | `SkI18nService.instant` ou filter `| translate` |
| Abrir/fechar tela do produto | `SkWorkspace.openAppActivity`/`closeApp` |
| Download de arquivo pelo viewer interno | `SkWorkspace.downloadFile` |
| Adicionar dependencia apos bootstrap | `$SkInjectorProvider.register` em `.config()` |
| Tela chamada por mais de um modulo | colocar em `src/commons/<nome>/` |
