# sankhya-js — Build e publicacao (Grunt)

O sankhya-js **nao usa npm scripts** (`npm test`, `npm run`) nem bundler moderno (webpack/vite/rollup) e nao tem Docker. Todo o build e publicacao passa pelo **Grunt** declarado em `Gruntfile.js`. Build com **Grunt 0.4.5 + Babel 7** (ver `gotchas.md`).

---

## 1. Tarefas essenciais

Setup (uma vez por maquina):

```bash
npm install                 # dependencias do projeto
npm install -g grunt-cli    # CLI do grunt no PATH
```

Tarefas do dia a dia:

| Comando | O que faz |
| --- | --- |
| `grunt` | Padrao: build + publish |
| `grunt build` | Build completo COM minificacao (uglify) |
| `grunt build:false` | Build SEM minificacao (rapido, usar no desenvolvimento) — equivale a `grunt jenkins` |
| `grunt jenkins` | Mesmo efeito de `grunt build:false` |
| `grunt watch` | Observa os LESS e recompila o CSS |
| `grunt publish` | Copia `dist/` para o servidor local definido no `.env` (`PUBLISH_TO_SERVER`) |
| `grunt doc` | Gera a documentacao AngularJS (ngdocs) |

Ciclo de dev agil:

```bash
grunt build:false   # build rapido, sem uglify
grunt publish       # copia dist/ para o destino local
```

Sobrescreva o destino local em `.env-dev` (arquivo **nao commitado**):

```bash
PUBLISH_TO_SERVER=...
PUBLISH_TO_MODULE_CTX=...
```

---

## 2. Ordem de concatenacao (CRITICA)

O `Gruntfile.js` concatena os fontes nesta ordem. **Alterar a ordem quebra a resolucao de dependencias do AngularJS** (um arquivo que usa `angular.module('x')` sem array precisa carregar depois do `.module.js` que declarou `angular.module('x', [])`).

1. `*.model.js`
2. `*.dependencies.js`
3. `*.module.js` (`core` -> `components` -> `i18n` -> `commons`)
4. `*.decorator.js`
5. demais `.js` (services, controllers, directives, providers, filters)
6. cache de templates (`html2js` -> `snk.tpls`)

---

## 3. Convencao de arquivos por componente

Cada componente vive em sua pasta sob `src/components`, `src/core` ou `src/commons`. Sufixos por papel:

| Arquivo | Papel |
| --- | --- |
| `{nome}.module.js` | Declara o modulo com array de deps |
| `{nome}.directive.js` | Directive |
| `{nome}.service.js` / `{nome}.factory.js` | Service / factory |
| `{nome}.controller.js` | Controller |
| `{nome}.provider.js` | Provider |
| `{nome}.filter.js` | Filter |
| `{nome}.decorator.js` | Decorator |
| `{nome}.model.js` | Model |
| `{nome}.dependencies.js` | Dependencias |
| `{nome}.tpl.html` | Template (vai para `$templateCache` via `grunt-html2js`) |

**APENAS** o `.module.js` declara `angular.module(nome, [])` com array; os demais arquivos reusam o modulo sem array:

```javascript
// {nome}.module.js  -> declara
angular.module('snk.components.meucomp', []);

// {nome}.directive.js -> reusa, SEM array
angular.module('snk.components.meucomp').directive('skMeucomp', [/* ... */]);
```

Redeclarar o modulo com `[]` em outro arquivo sobrescreve o que ja foi registrado. A armadilha esta detalhada em `anti-patterns.md` e `gotchas.md` — nao repetir aqui.

---

## 4. Lint (quality gate)

O **JSHint** roda como `beforeconcat` sobre `core/**`, `components/**` e `commons/**`. As regras estao **embutidas no `Gruntfile.js`** — **nao ha `.jshintrc`**:

| Regra | Valor | Efeito |
| --- | --- | --- |
| `curly` | `true` | Exige chaves em blocos |
| `eqeqeq` | `true` | Use `===` / `!==` |
| `freeze` | `true` | Proibe extender prototypes nativos |
| `bitwise` | `false` | Operadores bit-a-bit liberados |
| `strict` | `false` | Nao exige `"use strict"` |
| `globals` | `{ angular: false }` | `angular` reconhecido como global read-only |

Codigo que reprova no lint **nao deve ser commitado**. Nao desabilite uma regra globalmente so para "passar" no gate.

---

## 5. Estilo (LESS, dois temas)

O build gera dois temas a partir do mesmo LESS:

| Tema | Variaveis | Saida |
| --- | --- | --- |
| `snk` (padrao) | `src/assets/css/variables/variables.less` | `dist/assets/css/snk.css` |
| `jiva` | `variables-jiva.less` (sobrescreve o `snk`) | `dist/assets/css/snk-jiva.css` |

Nao hardcode cores nem medidas no CSS/LESS — use as **variaveis LESS do tema**, senao o tema `jiva` nao consegue sobrescrever.

---

## 6. Babel e templates

- O **Babel** transpila para compatibilidade (inclui `async-to-generator`), mas o codigo-fonte e **AngularJS 1.x** — nao dependa de runtime de browser moderno.
- Build com **Grunt 0.4.5 + Babel 7** (ver `gotchas.md`).
- Templates HTML viram entradas de `$templateCache` via `grunt-html2js`. Referencie por:

```javascript
templateUrl: 'components/<nome>/<nome>.html'
```

---

## Onde aprofundar

- `gotchas.md` — armadilhas de API e do toolchain (Grunt 0.4.5 + Babel 7)
- `anti-patterns.md` — praticas a evitar, incluindo redeclaracao de modulo
- ver skill `sankhya-js` (SKILL.md) — visao geral do framework e padroes canonicos
