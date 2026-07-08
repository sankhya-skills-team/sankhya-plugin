# sankhya-js — Catalogo de APIs

Referencia das APIs publicas mais usadas. Caminhos relativos ao repo `sankhya-js` (sibling de `sankhyaw`).

---

## `ServiceProxy` — comunicacao com backend

Service em `snk.core.util`. Declarado em [serviceproxy.service.js:2-5](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L2-L5).

### Chamada direta

| Metodo | Linha | Uso |
|---|---|---|
| `callService(serviceName, content, config)` | [122](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L122) | Chamada direta. Retorna promise |
| `builder()` | [44-53](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L44-L53) | Retorna `FluidBuilder` com `serviceName` (required), `ignoreLoadingBar` (asOption), `params` e alias `.call()` |

### Formato do `serviceName`

`"modulo@Servico.metodo"` ou apenas `"Servico.metodo"` (assume `defModule = "mge"`). Split em `@` em [linha 153-157](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L153-L157).

### URL montada

```
{urlBase}/{modulo}/service.sbr?serviceName={nome}&counter={n}&application={app}&outputType=json&preventTransform={bool}
```

Parametros opcionais agregados na URL ([serviceproxy.service.js:167-191](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L167-L191)): `mgeSession`, `resourceID`, `globalID`, `flowID`, `vss`, e os de `config.aditionalUrlParameters`.

### `config` suportado em `callService`

| Chave | Default | Efeito |
|---|---|---|
| `method` | `'POST'` | POST/PUT/DELETE/GET. Outros lancam `Error` ([linha 134](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L134)) |
| `ignoreLoadingBar` | `false` | Nao exibe barra de loading global |
| `preventTransform` | `false` | Nao aplica transform no response do backend |
| `normalizedJson` | — | Indica que `content` ja foi normalizado por `XmlJson.normalize` ([138-148](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L138-L148)) |
| `headers` | — | Extra headers (apenas POST/PUT) |
| `callback(data)` | — | Substitui `.then` — resolve vira callback direto |
| `exceptionCallback(data)` | — | Substitui `.catch` |
| `errorHandler(data, status, headers, config)` | — | Suprime popup de erro padrao |
| `ignorePopUpErrorMsgs` | `false` | Suprime popups mas mantem reject |
| `aditionalUrlParameters` | — | Objeto `{k:v}` concatenado como query string |

### Headers padroes da requisicao

```
Content-Type: application/json; charset=UTF-8
appkey: <valor configurado via self.appKey(...)>
sktk: <sktk.y(requestContent)>
```

[serviceproxy.service.js:232-236](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L232-L236).

### Client events

| Metodo | Linha | Uso |
|---|---|---|
| `addClientEvent(eventId, handler)` | [79-87](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L79-L87) | Registra handler. Retorna `ClientEventHandler` com `.unregistry()` |
| `addSingleClientEvent(eventId, handler)` | [112](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L112) | Idempotente: so registra se nao houver handler para o id |
| `removeClientEvent(eventId, handler?)` | [89](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L89) | Remove handler especifico ou todos do id |
| `hasClientEvent(eventId)` | [118](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L118) | Boolean |

Eventos sao injetados automaticamente no request body (`clientEventList.clientEvent`) em [linhas 198-210](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L198-L210).

### Listeners de impressao

| Metodo | Linha | Uso |
|---|---|---|
| `addPrintListener(fn)` | [35](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L35) | Disparado quando `data.pendingPrinting == "true"` |
| `addLocalPrintingListener(fn)` | [39](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L39) | Disparado quando `data.localPrintings` presente |

### Serializacao de chamadas

| Metodo | Linha | Uso |
|---|---|---|
| `addSerializedService(serviceName)` | [31](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L31) | Forca execucao sequencial de chamadas subsequentes deste servico |

### Abortar request

`promise.abort()` ([linha 381-384](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L381-L384)) — marca `aborted = true` e resolve o deferred de abort.

---

## `FluidBuilder` — padrao builder dos servicos

Provider em [fluidbuilder.service.js:3](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L3).

### Metadados de variavel

Cada entrada do array de metadados pode ser:
- String: `"nomeVar"` — variavel simples, nao-required, nao-asOption
- Object: `{name, required?, asOption?, value?, transformer?, fnImpl?}`

| Campo | Efeito |
|---|---|
| `required` | `.build()` lanca `Error` se nao preenchida ([linha 63-65](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L63-L65)) |
| `asOption` | Vai para `_options` em vez de `_variables` |
| `value` | Default aplicado no build se nao setada ([linha 58-60](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L58-L60)) |
| `transformer(value, ...)` | Aplica transformacao no setter ([linha 130-133](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L130-L133)) |
| `fnImpl({workingObj, builder, args})` | Substitui o setter default por funcao customizada ([linha 81-97](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L81-L97)) |

### Metodos do builder

| Metodo | Linha | Uso |
|---|---|---|
| `.build()` | [54-69](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L54-L69) | Valida requireds e invoca `buildFn(variables, options, workingObj)` |
| `.buildFn(fn, alias?)` | [42-52](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L42-L52) | Define funcao de build; `alias` expoe como metodo (`.call()`, etc.) |
| `.reset()` | [23-28](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L23-L28) | Limpa variaveis e options |
| `.toFunction()` | [36-40](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L36-L40) | Retorna funcao que chama `reset()` ao ser invocada |
| `.workingObj(obj)` | [30-34](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L30-L34) | Define contexto passado ao `buildFn` |
| `.options(map)` | [71-74](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L71-L74) | Substitui todas as options |
| `.option(k, v)` | [76-79](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L76-L79) | Seta uma option |
| `.fnImpl(nome, fn)` | [81-97](../../../../../sankhya-js/src/core/util/fluidbuilder/fluidbuilder.service.js#L81-L97) | Adiciona metodo customizado apos construcao |

Mensagem de erro exata quando `required` falta: `"Variável X é requerida e não foi preenchida no builder"` (ou `"Opção X..."` se `asOption: true`).

---

## `MetadataProvider` — metadados de entidades

Service em `snk.core.metadataprovider` (depende de `snk.core.util`). [metadataprovider.service.js:8-11](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L8-L11).

| Metodo | Linha | Uso |
|---|---|---|
| `getEntityMetadata(names)` | [77](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L77) | Aceita string, CSV, array. Retorna `promise<{ [name]: entity }>` |
| `getEntityAndRelationsMetadata(names, filterFn?, includeOneToMany?)` | [185](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L185) | Retorna `{entities, relations, oneToManyRelations}` |
| `getSizeOfCache()` | [35-37](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L35-L37) | Tamanho do cache interno |

Endpoint: `GET /mge/metadataProvider.mge/{entityName-locale}.js` ([linha 103](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L103)).

Cache chave: `entityName + '-' + SkI18nService.getLang()` ([linha 43-45](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L43-L45)). `_useInternalCache` e `false` por default ([linha 18](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L18)) — alterar via atribuicao direta.

Exposto globalmente em `top.mdProvider` ([linha 12](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L12)).

---

## `SkComponentRegistry` — compartilhamento de instancias

Factory em `snk.core.services.registry`. [componentregistry.service.js:62-64](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L62-L64).

| Metodo | Linha | Uso |
|---|---|---|
| `get(handle)` | [80-96](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L80-L96) | Retorna `promise`. Se ja registrado resolve imediato; senao empilha ate o `register` |
| `register(instance, handle, scope?, ignoreDuplicity?)` | [107-150](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L107-L150) | Retorna funcao de desregistro. Se `scope` passado, auto-desregistra no `$destroy` |
| `getSync(handle)` | [152](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L152) | Retorna instancia ou `null` sincrono. Nao empilha |

Handle duplicado: `console.warn` + retorna `angular.noop` ([linhas 115-117](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L115-L117)). Passar `ignoreDuplicity: true` permite sobrescrever.

Handle vazio ou undefined no `register`: retorna `angular.noop` ([linha 108-110](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L108-L110)).

---

## `SkI18nService` — internacionalizacao

Service em `snk.i18n`. [i18n.service.js:1-3](../../../../../sankhya-js/src/i18n/i18n.service.js#L1-L3).

| Metodo | Linha | Uso |
|---|---|---|
| `instant(id, values?)` | [17-19](../../../../../sankhya-js/src/i18n/i18n.service.js#L17-L19) | Traducao sincrona via `$translate.instant` |
| `translate(id, values?)` | [21-23](../../../../../sankhya-js/src/i18n/i18n.service.js#L21-L23) | Traducao assincrona (promise) |
| `setLang(lang)` | [25-27](../../../../../sankhya-js/src/i18n/i18n.service.js#L25-L27) | Muda idioma corrente |
| `getLang()` | [29-31](../../../../../sankhya-js/src/i18n/i18n.service.js#L29-L31) | Idioma corrente (ou `'pt_BR'` default) |
| `loadAsyncBundle(locale, url)` | [33-48](../../../../../sankhya-js/src/i18n/i18n.service.js#L33-L48) | GET + `addBundle` para cada chave |
| `addBundle(lang, bundleName, translations)` | [50-73](../../../../../sankhya-js/src/i18n/i18n.service.js#L50-L73) | Registra bundle (alias: `addPart`) |
| `adjustTranslateValues(values)` | [99](../../../../../sankhya-js/src/i18n/i18n.service.js#L99) | Array vira `{p0, p1, ...}` |

Tambem ha o provider `i18n` ([linha 116-122](../../../../../sankhya-js/src/i18n/i18n.service.js#L116-L122)) injetavel como funcao: `i18n('chave', valores)`.

Values array: posicoes viram `p0`, `p1`, `p2`... no mapa ([linha 101-113](../../../../../sankhya-js/src/i18n/i18n.service.js#L101-L113)).

---

## `SkWorkspace` — integracao com a shell do produto

Service em `snk.core.workspace`. Depende da variavel global `workspace` injetada pelo GWT ([workspace.service.js:5](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L5)).

| Metodo | Linha | Uso |
|---|---|---|
| `openAppActivity(resourceId, pkObject)` | [123-125](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L123-L125) | Abre tela pelo resourceId |
| `closeApp(resourceId)` | [131](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L131) | Fecha tela |
| `reloadApp(resourceId, pkObject)` | [135](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L135) | Recarrega tela |
| `requestSignature(stamp, params, executor, callback, resourceId)` | [139](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L139) | Pede assinatura digital |
| `revokeSignature(...)` | [143](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L143) | Revoga assinatura |
| `showDigitalSignDetails(stamp, chaveArquivo)` | [147](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L147) | Detalhes de assinatura |
| `openHelp(url)` | [151](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L151) | Ajuda contextual |
| `downloadFile(serverAddress, chave, extension, params)` | [99-113](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L99-L113) | Fallback: `/mge/visualizadorArquivos.mge?chaveArquivo=X` |
| `trackAnalyticsEvent(category, action, label)` | [155](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L155) | Evento de analytics |
| `isJivaW()` / `isSankhyaW()` | [174-180](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L174-L180) | Deteccao de produto pelo `PROFILEID` |
| `logout()` | [194](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L194) | Delega para `workspace.logout()` |
| `getCurrentHistory(resourceID?)` | [37-69](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L37-L69) | Hash da tela ativa (ciente de multi-abas) |
| `addHistoryChangeHandler(fn, resourceID, useLocalHash?)` | [71-97](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L71-L97) | Listener de mudanca de hash |
| `openSideBarWorkspace(...)` | [34](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L34) | Multi Abas — abre workspace lateral |

PROFILEID: `S4W8LB` = SankhyaW, `J1WE9N` = JivaW ([linha 8-9](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L8-L9)).

---

## `$SkInjectorProvider` — registro dinamico de modulos

Provider em [framework.config.js:44-85](../../../../../sankhya-js/src/core/framework.config.js#L44-L85).

| API | Linha | Uso |
|---|---|---|
| `$SkInjectorProvider.register(module, depNames)` | [54-73](../../../../../sankhya-js/src/core/framework.config.js#L54-L73) | Adiciona `depNames` como dependencias do `module` apos bootstrap. Executa `_invokeQueue` e `_configBlocks` do modulo dependente |
| `$SkInjectorProvider.setProviders({$provide, $controllerProvider, $compileProvider, $filterProvider, $injector})` | [50-52](../../../../../sankhya-js/src/core/framework.config.js#L50-L52) | Configurado uma vez no config do `snk` ([framework.config.js:31-42](../../../../../sankhya-js/src/core/framework.config.js#L31-L42)). Nao precisa chamar em codigo de aplicacao |

Injetar `$SkInjector` fora de um `.config(...)` lanca `Error('Este injector deve ser usado apenas em configuracoes de modulos.')` ([linha 47](../../../../../sankhya-js/src/core/framework.config.js#L47)).

---

## Modulos principais

| Modulo | Dependencias | Local |
|---|---|---|
| `snk` | (agrega tudo) | [framework.config.js:30](../../../../../sankhya-js/src/core/framework.config.js#L30) |
| `snk.commons` | `[]` | [commons.module.js](../../../../../sankhya-js/src/commons/commons.module.js) |
| `snk.core.util` | inclui `snk.components.popup` | (ver seus config blocks) |
| `snk.core.metadataprovider` | `['snk.core.util']` | [metadataprovider.service.js:9](../../../../../sankhya-js/src/core/metadataprovider/metadataprovider.service.js#L9) |
| `snk.core.services.registry` | — | [componentregistry.service.js:63](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L63) |
| `snk.core.workspace` | — | [workspace.service.js:2](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L2) |
| `snk.i18n` | — | [i18n.service.js:2](../../../../../sankhya-js/src/i18n/i18n.service.js#L2) |
| `snk.components.<nome>` | geralmente `[]` | Um por componente. Ex.: [button.module.js](../../../../../sankhya-js/src/components/button/button.module.js) |

Dependencias externas fixadas em `package.json.otherModuleDependencies`: `ngSanitize`, `ngTouch`, `ui.tinymce`, `ui.mask` ([package.json:8-13](../../../../../sankhya-js/package.json#L8-L13)).
