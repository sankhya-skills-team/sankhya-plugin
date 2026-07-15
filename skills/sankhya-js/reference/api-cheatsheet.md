# sankhya-js — Catalogo de APIs

Referencia das APIs publicas mais usadas. Caminhos relativos ao repo `sankhya-js` (sibling de `sankhyaw`).

---

## `ServiceProxy` — comunicacao com backend

Service em `snk.core.util`. Declarado em `serviceproxy.service.js:2-5`.

### Chamada direta

| Metodo | Linha | Uso |
|---|---|---|
| `callService(serviceName, content, config)` | `122` | Chamada direta. Retorna promise |
| `builder()` | `44-53` | Retorna `FluidBuilder` com `serviceName` (required), `ignoreLoadingBar` (asOption), `params` e alias `.call()` |

### Formato do `serviceName`

`"modulo@Servico.metodo"` ou apenas `"Servico.metodo"` (assume `defModule = "mge"`). Split em `@` em `linha 153-157`.

### URL montada

```
{urlBase}/{modulo}/service.sbr?serviceName={nome}&counter={n}&application={app}&outputType=json&preventTransform={bool}
```

Parametros opcionais agregados na URL (`serviceproxy.service.js:167-191`): `mgeSession`, `resourceID`, `globalID`, `flowID`, `vss`, e os de `config.aditionalUrlParameters`.

### `config` suportado em `callService`

| Chave | Default | Efeito |
|---|---|---|
| `method` | `'POST'` | POST/PUT/DELETE/GET. Outros lancam `Error` (`linha 134`) |
| `ignoreLoadingBar` | `false` | Nao exibe barra de loading global |
| `preventTransform` | `false` | Nao aplica transform no response do backend |
| `normalizedJson` | — | Indica que `content` ja foi normalizado por `XmlJson.normalize` (`138-148`) |
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

`serviceproxy.service.js:232-236`.

### Client events

| Metodo | Linha | Uso |
|---|---|---|
| `addClientEvent(eventId, handler)` | `79-87` | Registra handler. Retorna `ClientEventHandler` com `.unregistry()` |
| `addSingleClientEvent(eventId, handler)` | `112` | Idempotente: so registra se nao houver handler para o id |
| `removeClientEvent(eventId, handler?)` | `89` | Remove handler especifico ou todos do id |
| `hasClientEvent(eventId)` | `118` | Boolean |

Eventos sao injetados automaticamente no request body (`clientEventList.clientEvent`) em `linhas 198-210`.

### Listeners de impressao

| Metodo | Linha | Uso |
|---|---|---|
| `addPrintListener(fn)` | `35` | Disparado quando `data.pendingPrinting == "true"` |
| `addLocalPrintingListener(fn)` | `39` | Disparado quando `data.localPrintings` presente |

### Serializacao de chamadas

| Metodo | Linha | Uso |
|---|---|---|
| `addSerializedService(serviceName)` | `31` | Forca execucao sequencial de chamadas subsequentes deste servico |

### Abortar request

`promise.abort()` (`linha 381-384`) — marca `aborted = true` e resolve o deferred de abort.

---

## `FluidBuilder` — padrao builder dos servicos

Provider em `fluidbuilder.service.js:3`.

### Metadados de variavel

Cada entrada do array de metadados pode ser:
- String: `"nomeVar"` — variavel simples, nao-required, nao-asOption
- Object: `{name, required?, asOption?, value?, transformer?, fnImpl?}`

| Campo | Efeito |
|---|---|
| `required` | `.build()` lanca `Error` se nao preenchida (`linha 63-65`) |
| `asOption` | Vai para `_options` em vez de `_variables` |
| `value` | Default aplicado no build se nao setada (`linha 58-60`) |
| `transformer(value, ...)` | Aplica transformacao no setter (`linha 130-133`) |
| `fnImpl({workingObj, builder, args})` | Substitui o setter default por funcao customizada (`linha 81-97`) |

### Metodos do builder

| Metodo | Linha | Uso |
|---|---|---|
| `.build()` | `54-69` | Valida requireds e invoca `buildFn(variables, options, workingObj)` |
| `.buildFn(fn, alias?)` | `42-52` | Define funcao de build; `alias` expoe como metodo (`.call()`, etc.) |
| `.reset()` | `23-28` | Limpa variaveis e options |
| `.toFunction()` | `36-40` | Retorna funcao que chama `reset()` ao ser invocada |
| `.workingObj(obj)` | `30-34` | Define contexto passado ao `buildFn` |
| `.options(map)` | `71-74` | Substitui todas as options |
| `.option(k, v)` | `76-79` | Seta uma option |
| `.fnImpl(nome, fn)` | `81-97` | Adiciona metodo customizado apos construcao |

Mensagem de erro exata quando `required` falta: `"Variável X é requerida e não foi preenchida no builder"` (ou `"Opção X..."` se `asOption: true`).

---

## `MetadataProvider` — metadados de entidades

Service em `snk.core.metadataprovider` (depende de `snk.core.util`). `metadataprovider.service.js:8-11`.

| Metodo | Linha | Uso |
|---|---|---|
| `getEntityMetadata(names)` | `77` | Aceita string, CSV, array. Retorna `promise<{ [name]: entity }>` |
| `getEntityAndRelationsMetadata(names, filterFn?, includeOneToMany?)` | `185` | Retorna `{entities, relations, oneToManyRelations}` |
| `getSizeOfCache()` | `35-37` | Tamanho do cache interno |

Endpoint: `GET /mge/metadataProvider.mge/{entityName-locale}.js` (`linha 103`).

Cache chave: `entityName + '-' + SkI18nService.getLang()` (`linha 43-45`). `_useInternalCache` e `false` por default (`linha 18`) — alterar via atribuicao direta.

Exposto globalmente em `top.mdProvider` (`linha 12`).

---

## `SkComponentRegistry` — compartilhamento de instancias

Factory em `snk.core.services.registry`. `componentregistry.service.js:62-64`.

| Metodo | Linha | Uso |
|---|---|---|
| `get(handle)` | `80-96` | Retorna `promise`. Se ja registrado resolve imediato; senao empilha ate o `register` |
| `register(instance, handle, scope?, ignoreDuplicity?)` | `107-150` | Retorna funcao de desregistro. Se `scope` passado, auto-desregistra no `$destroy` |
| `getSync(handle)` | `152` | Retorna instancia ou `null` sincrono. Nao empilha |

Handle duplicado: `console.warn` + retorna `angular.noop` (`linhas 115-117`). Passar `ignoreDuplicity: true` permite sobrescrever.

Handle vazio ou undefined no `register`: retorna `angular.noop` (`linha 108-110`).

---

## `SkI18nService` — internacionalizacao

Service em `snk.i18n`. `i18n.service.js:1-3`.

| Metodo | Linha | Uso |
|---|---|---|
| `instant(id, values?)` | `17-19` | Traducao sincrona via `$translate.instant` |
| `translate(id, values?)` | `21-23` | Traducao assincrona (promise) |
| `setLang(lang)` | `25-27` | Muda idioma corrente |
| `getLang()` | `29-31` | Idioma corrente (ou `'pt_BR'` default) |
| `loadAsyncBundle(locale, url)` | `33-48` | GET + `addBundle` para cada chave |
| `addBundle(lang, bundleName, translations)` | `50-73` | Registra bundle (alias: `addPart`) |
| `adjustTranslateValues(values)` | `99` | Array vira `{p0, p1, ...}` |

Tambem ha o provider `i18n` (`linha 116-122`) injetavel como funcao: `i18n('chave', valores)`.

Values array: posicoes viram `p0`, `p1`, `p2`... no mapa (`linha 101-113`).

---

## `SkWorkspace` — integracao com a shell do produto

Service em `snk.core.workspace`. Depende da variavel global `workspace` injetada pelo GWT (`workspace.service.js:5`).

| Metodo | Linha | Uso |
|---|---|---|
| `openAppActivity(resourceId, pkObject)` | `123-125` | Abre tela pelo resourceId |
| `closeApp(resourceId)` | `131` | Fecha tela |
| `reloadApp(resourceId, pkObject)` | `135` | Recarrega tela |
| `requestSignature(stamp, params, executor, callback, resourceId)` | `139` | Pede assinatura digital |
| `revokeSignature(...)` | `143` | Revoga assinatura |
| `showDigitalSignDetails(stamp, chaveArquivo)` | `147` | Detalhes de assinatura |
| `openHelp(url)` | `151` | Ajuda contextual |
| `downloadFile(serverAddress, chave, extension, params)` | `99-113` | Fallback: `/mge/visualizadorArquivos.mge?chaveArquivo=X` |
| `trackAnalyticsEvent(category, action, label)` | `155` | Evento de analytics |
| `isJivaW()` / `isSankhyaW()` | `174-180` | Deteccao de produto pelo `PROFILEID` |
| `logout()` | `194` | Delega para `workspace.logout()` |
| `getCurrentHistory(resourceID?)` | `37-69` | Hash da tela ativa (ciente de multi-abas) |
| `addHistoryChangeHandler(fn, resourceID, useLocalHash?)` | `71-97` | Listener de mudanca de hash |
| `openSideBarWorkspace(...)` | `34` | Multi Abas — abre workspace lateral |

PROFILEID: `S4W8LB` = SankhyaW, `J1WE9N` = JivaW (`linha 8-9`).

---

## `$SkInjectorProvider` — registro dinamico de modulos

Provider em `framework.config.js:44-85`.

| API | Linha | Uso |
|---|---|---|
| `$SkInjectorProvider.register(module, depNames)` | `54-73` | Adiciona `depNames` como dependencias do `module` apos bootstrap. Executa `_invokeQueue` e `_configBlocks` do modulo dependente |
| `$SkInjectorProvider.setProviders({$provide, $controllerProvider, $compileProvider, $filterProvider, $injector})` | `50-52` | Configurado uma vez no config do `snk` (`framework.config.js:31-42`). Nao precisa chamar em codigo de aplicacao |

Injetar `$SkInjector` fora de um `.config(...)` lanca `Error('Este injector deve ser usado apenas em configuracoes de modulos.')` (`linha 47`).

---

## Modulos principais

| Modulo | Dependencias | Local |
|---|---|---|
| `snk` | (agrega tudo) | `framework.config.js:30` |
| `snk.commons` | `[]` | `commons.module.js` |
| `snk.core.util` | inclui `snk.components.popup` | (ver seus config blocks) |
| `snk.core.metadataprovider` | `['snk.core.util']` | `metadataprovider.service.js:9` |
| `snk.core.services.registry` | — | `componentregistry.service.js:63` |
| `snk.core.workspace` | — | `workspace.service.js:2` |
| `snk.i18n` | — | `i18n.service.js:2` |
| `snk.components.<nome>` | geralmente `[]` | Um por componente. Ex.: `button.module.js` |

Dependencias externas fixadas em `package.json.otherModuleDependencies`: `ngSanitize`, `ngTouch`, `ui.tinymce`, `ui.mask` (`package.json:8-13`).
