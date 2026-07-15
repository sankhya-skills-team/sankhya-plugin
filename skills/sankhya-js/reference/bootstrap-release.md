# sankhya-js — Bootstrap de tela HTML5 e versionamento do snk.js

Como uma tela HTML5 nasce: template raiz, controllers Angular, bootstrap manual do app e bundle `snk.js` versionado pela compilacao. Cobre o lancador server-side, o `release.snk`, o registro dinamico de modulo apos o bootstrap e o pareamento de branch entre `sankhya-js` e `sankhyaw`.

## Anatomia de uma tela HTML5

As telas HTML5 vivem em `MGE-<Dominio>-VC/build/html5/<NomeDaTela>/`. Cada tela tem:

| Arquivo | Papel |
|---|---|
| `<NomeDaTela>.html` | Template raiz (carregado por `ng-include` da shell; contem o `sk-application` da tela) |
| `<NomeDaTela>.js` | Um ou mais controllers/services Angular da tela |

O bundle `snk.js` (framework `sankhya-js` compilado) e carregado pela shell antes do `.js` da tela. O container raiz e o directive `sk-application` (ver `application.md`).

## Bootstrap MANUAL

A shell carrega a tela de forma assincrona. AngularJS **nao** permite `ng-app` declarativo apos carga assincrona — por isso o bootstrap do app e manual.

O lancador server-side (`DWF/src/br/com/sankhya/dwf/controller/servlet/XHtml5LauncherTemplate.html`) injeta o `snk.js` versionado e da o bootstrap manual do app Angular da tela:

```html
<!-- snk.js entra versionado pela compilacao -->
<script src="/mge/scripts/snk.js?v=5.9.15"></script>

<!-- depois, o .js da propria tela -->
<script src="html5/<MODULE_ID>/<MODULE_ID>.js?v=5.9.15"></script>
```

O `ngAppName` segue o padrao `"<MODULE_ID>App"` (ex.: `CentralNotasStackApp`). No bloco `.run` a tela configura o `SkI18nService` (idioma e bundles) e libera a troca de app no `SkWorkspace`:

```javascript
var ngAppName = "CentralNotasStackApp";

angular.module(ngAppName)
  .run(['SkI18nService', 'SkWorkspace',
    function(SkI18nService, SkWorkspace) {
      SkWorkspace.unlockSwitchApp();

      SkI18nService.setLang(locale);

      angular.forEach(i18nAll, function(translations, bundleName) {
        SkI18nService.addBundle(locale, bundleName, translations);
      });

      angular.forEach(i18nFramework, function(translations, bundleName) {
        SkI18nService.addBundle(locale, bundleName, translations);
      });
    }]);

// Bootstrap manual: necessario porque a tela foi carregada apos a pagina.
angular.bootstrap(document, [ngAppName]);
```

`locale`, `i18nAll` e `i18nFramework` sao variaveis globais pre-renderizadas pelo lancador no `<head>` da pagina.

## Versionamento do snk.js (release.snk)

A versao do framework que cada compilacao usa vem de `build/html5/release.snk` no modulo VC:

```text
SNK_GA_VERSION=5.9.15
SNK_RC_VERSION=5.9.15
SNK_MS_VERSION=5.9.15
SNK_DEV_VERSION=5.9.15
```

O **canal** (GA / RC / MS / DEV) e decidido pela branch/versao do `sankhyaw` e seleciona a chave `SNK_*_VERSION` correspondente, que entra no `?v=` do `<script src="/mge/scripts/snk.js?v=...">` da tela compilada.

| Canal | Chave | Origem |
|---|---|---|
| GA | `SNK_GA_VERSION` | branch de release geral (GA) |
| RC | `SNK_RC_VERSION` | branch release candidate |
| MS | `SNK_MS_VERSION` | milestone |
| DEV | `SNK_DEV_VERSION` | branch de desenvolvimento |

Manter as quatro chaves alinhadas evita que uma compilacao DEV puxe um `snk.js` diferente do que sera publicado em GA.

## Registro dinamico de modulo apos o bootstrap

AngularJS nao aceita novas dependencias depois do `bootstrap`. Telas carregadas tardiamente (apos a pagina) nao podem declarar o que precisam no array do `angular.module(nome, [...])` no momento do load — o injetor ja foi criado.

A saida e declarar as dependencias via `$SkInjectorProvider` **dentro de um `.config([...])`** (nunca em service ou controller, que rodam apos a fase de config):

```javascript
angular.module('minhaTelaApp').config(['$SkInjectorProvider',
  function($SkInjectorProvider) {
    $SkInjectorProvider.register(angular.module('minhaTelaApp'),
      ['snk.components.popup', 'snk.components.datepicker']);
  }]);
```

O `$SkInjectorProvider` reinjeta as dependencias via reflection do `_invokeQueue`/`_configBlocks`. O detalhe do mecanismo esta na SKILL.md (Padrao canonico 5) e em `gotchas.md` — referenciar de la, nao reescrever aqui.

## Branch canaria (pareamento sankhya-js <-> sankhyaw)

O canal do `release.snk` acompanha a branch. Ao abrir uma tarefa que toca a tela e o framework juntos, a branch do `sankhya-js` segue a branch do `sankhyaw`:

| branch sankhyaw | branch sankhya-js |
|---|---|
| `123456-4.35-DEV` | `feat-dev-123456` (ou `bugfix-dev-123456`) |
| `123456-4.35-RC` | `hotfix-rc-123456` |
| `123456-4.35` (GA) | `hotfix-ga-123456` |

O numero `123456` e o identificador do chamado/tarefa, comum aos dois repositorios. O prefixo (`feat`/`bugfix`/`hotfix`) e o canal (`dev`/`rc`/`ga`) traduzem o estagio da branch do `sankhyaw` para a convencao do `sankhya-js`, e e esse canal que seleciona a chave `SNK_*_VERSION`.

Para o gitflow e o formato de commit (cz-sankhya) genericos, nao duplicar aqui:

- ver skill `gitflow` — fluxo de branches e merge
- ver skill `conventional-commit` — formato de mensagem (cz-sankhya)
- ver skill `semantic-version` — derivacao da versao a partir dos commits

## Onde aprofundar

- `application.md` — `sk-application`: container raiz, singleton, ciclo de vida da tela
- `build-grunt.md` — build e publicacao do `snk.js` (Grunt), ordem de concatenacao
- `gotchas.md` — armadilhas de API, incluindo `$SkInjectorProvider`
- ver skill `sankhya-js` (SKILL.md) — visao geral do framework e Padrao canonico 5 (registro dinamico)
