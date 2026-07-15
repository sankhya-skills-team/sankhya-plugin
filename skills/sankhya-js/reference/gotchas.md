# sankhya-js — Armadilhas

Comportamentos nao-obvios extraidos do codigo. Ler antes de escrever ou revisar codigo que toque essas APIs.

---

## 1. `serviceName` sem `@` cai no modulo `mge`

`serviceproxy.service.js:151-157`:

```javascript
var defModule = "mge";
if (serviceName.indexOf("@") > -1) {
    var s = serviceName.split("@");
    defModule = s[0];
    serviceName = s[1];
}
```

Consequencia: `ServiceProxy.callService('FichaParceiroSP.getFinanceiros', ...)` vai para `/mge/service.sbr?serviceName=FichaParceiroSP.getFinanceiros`. Se o servico estiver em `mgecom`, o request chega no modulo errado e falha. **Sempre prefixe com o modulo correto** (`mgecom@`, `mgefin@`, `mgecheckout@`, etc.).

---

## 2. `MetadataProvider` cacheia com locale no nome

`metadataprovider.service.js:43-45`:

```javascript
function getFullEntityName(entity) {
    return entity + '-' + getLocale();
}
```

Entrada `"Produto"` vira chave de cache `"Produto-pt_BR"`. Trocar idioma invalida as entradas anteriores (ficam orfas no cache ate reload). Alem disso, requests para o backend vao para `/mge/metadataProvider.mge/Produto-pt_BR.js` — o backend precisa responder aquela rota.

Pratico: chamar `SkI18nService.setLang(novoLang)` **nao** limpa o cache do MetadataProvider.

---

## 3. `_useInternalCache` do MetadataProvider e `false` por default

`metadataprovider.service.js:18`:

```javascript
var _useInternalCache = false;
```

Resultado: toda chamada a `getEntityMetadata` dispara request HTTP, mesmo que a entidade tenha sido buscada antes. So ha deduplicacao **em voo** via `pendingEntityRequests`. Para ativar o cache, setar via atribuicao direta (nao ha setter publico).

---

## 4. Handle duplicado no `SkComponentRegistry.register`

`componentregistry.service.js:114-118`:

```javascript
if (instances[handle]) {
    console.warn('[ComponentRegistry] Instancias com handle duplicado: ' + handle);
    exists = true;
    if(!ignoreDuplicity) return angular.noop;
}
```

Segundo `register` com mesmo handle NAO sobrescreve — retorna `angular.noop`. A instancia antiga permanece ate alguem chamar a funcao de desregistro dela. Para sobrescrever intencional, passe `ignoreDuplicity: true`.

Consequencia pratica: se dois controllers com mesmo handle sao instanciados em ordem imprevisivel, o segundo silenciosamente nao se registra — e `get(handle)` continua resolvendo com a primeira instancia, que pode ja estar destruida.

---

## 5. `SkComponentRegistry.get` empilha para sempre se ninguem registrar

`componentregistry.service.js:80-96`:

```javascript
if (instance) {
    deferred.resolve(instance);
} else {
    addToPendingHandles(handle, deferred);
}
```

O deferred fica em `pendings[handle]` sem timeout. Se nenhum `register` ocorrer para aquele handle, a promise nunca resolve nem rejeita — vaza memoria e trava cadeias `.then`. Use `getSync(handle)` quando puder tolerar `null` imediato.

---

## 6. `ServiceProxy.builder()` lanca `Error` se `serviceName` faltar

`fluidbuilder.service.js:63-65`:

```javascript
if (varMD.required && angular.isUndefined(currValue)) {
    throw Error((varMD.asOption ? 'Opção ' : 'Variável ') + key
                + ' é requerida e não foi preenchida no builder');
}
```

`ServiceProxy.builder()` marca `serviceName` como required (`serviceproxy.service.js:46`). Esquecer `.serviceName(...)` derruba com `Error` sincrono — nao volta como rejection de promise.

---

## 7. `config.callback` suprime o `.then`

`serviceproxy.service.js:289-293`:

```javascript
if (angular.isFunction(config.callback)) {
    config.callback(clonedData);
} else {
    deffered.resolve(clonedData);
}
```

Se passar `{ callback: fn }` no config, o `.then` do promise retornado **nunca resolve com dados**. So com reject. Decida entre um modelo ou outro.

Mesmo vale para `exceptionCallback`: se setado, o reject pode nao chegar em `.catch` (`serviceproxy.service.js:408-412`).

---

## 8. Erro de servico exibe popup por default

`serviceproxy.service.js:447-459`:

```javascript
function handleDefaultSystemError(data, config, statusMessage) {
    if(config?.ignorePopUpErrorMsgs){ return; }
    ...
    MessageUtils.showError(MessageUtils.TITLE_ERROR, statusMessage);
}
```

Qualquer erro do backend abre popup `MessageUtils.showError`, mesmo que o codigo cliente trate via `.catch`. Isso gera popups duplicados quando o cliente tambem mostra mensagem propria.

Solucoes: passar `ignorePopUpErrorMsgs: true` ou `errorHandler: fn` no config para suprimir o popup padrao.

---

## 9. `$SkInjectorProvider` so funciona dentro de `.config(...)`

`framework.config.js:47`:

```javascript
this.$get = function(){throw new Error('Este injector deve ser usado apenas em configurações de módulos.')};
```

Injetar `$SkInjector` (sem o `Provider`) em qualquer service/controller lanca erro. Uso correto e sempre `$SkInjectorProvider` dentro de um `.config([...])`.

---

## 10. `addHistoryChangeHandler` tem dois caminhos de codigo divergentes

`workspace.service.js:71-97`:

- Se `workspace.addHistoryChangeHandler` existir (ambiente GWT normal), delega para ele.
- Se nao existir, ha fallback usando `$window.onhashchange` ou `$interval` de 100ms polling.

O fallback polling **nao para** automaticamente — se a tela nao chama algo que limpe a funcao no `$interval`, ela continua a cada 100ms. Comentario no codigo menciona "Aqui nao esta force como o flex devido a Central, que entra em loop ao abrir duas notas" — comportamento conhecido.

---

## 11. Componentes declaram modulo em `.module.js` separado

Convencao da base de codigo: sempre um arquivo `<nome>.module.js` declarando `angular.module('snk.components.<nome>', [])` com lista de dependencias. Demais arquivos (`*.directive.js`, `*.service.js`, etc.) reusam o modulo com `angular.module('snk.components.<nome>')` **sem** o segundo argumento.

Passar `[]` de novo em outro arquivo **sobrescreve** o modulo ja registrado, perdendo as services declaradas antes no ciclo de carga. Armadilha comum quando se copia-e-cola um `.module.js` ao criar componente novo sem notar que outro arquivo ja declarou o modulo.

Ver: `button.module.js` + `button.directive.js:41-42`.

---

## 12. Build usa Grunt 0.4.5 + Babel 7

`package.json:30-40`:

- `grunt`: `0.4.5` (EOL ha anos; 1.x e a versao corrente do Grunt publico)
- `grunt-babel`: `8.0.0` + `@babel/preset-env`: `7.26.7`
- `grunt-contrib-*` em varias versoes antigas (0.4.x, 0.5.x, 0.8.x)
- `grunt-html2js` converte templates HTML em `$templateCache` entries

Consequencia: o pipeline compila com Babel moderno mas roda sobre Grunt antigo. Adicionar task grunt nova pode esbarrar em API quebrada entre versoes. Plugins novos do ecossistema geralmente exigem Grunt 1+.

---

## 13. `pt_BR` e idioma fallback

`i18n.service.js:6`:

```javascript
const DEFAULT_LANG = 'pt_BR';
```

Se `$translate.use()` retornar `undefined`, `SkI18nService.getLang()` devolve `'pt_BR'`. Codigo que faz lookup manual por locale precisa lidar com os dois cenarios (locale setado explicitamente vs. default implicito).

---

## 14. `workspace` global injetado pelo GWT

`workspace.service.js:5`:

```javascript
/**A variavel 'workspace' e 'PROFILEID' são injetadas no contexto pelo GWT;*/
```

`SkWorkspace` e um wrapper sobre `window.workspace` e `window.PROFILEID`. Muitos metodos sao `workspace && workspace.xxx()` — se executar fora do container do produto (ex.: teste unitario sem mock, standalone), a maioria e no-op silencioso.

Para testar: mockar `window.workspace` com os metodos que a tela precisa.
