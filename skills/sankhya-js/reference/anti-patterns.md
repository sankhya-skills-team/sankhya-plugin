# sankhya-js — Praticas nao recomendadas

Anti-padroes observados no codigo real que causam bugs recorrentes. Cada item lista o padrao ruim, **por que** gera problema e qual e a alternativa correta.

Use como checklist de triagem de bugs em telas AngularJS e code-review.

---

## 1. `setTimeout`/`$timeout(fn, ms)` para "esperar" retorno de servico

### Padrao ruim

```javascript
ServiceProxy.callService('mge@Algo.fazer', payload);
$timeout(function() {
    // supostamente o servico ja terminou...
    self.atualizarTela();
}, 500);
```

Variante observada em [AgendadorRelatoriosPopUp.js:71-78](../../../../../sankhya-js/src/commons/visualizadorRelatoriosBase/popup/AgendadorRelatoriosPopUp/AgendadorRelatoriosPopUp.js#L71-L78): `setTimeout` envolvendo `$popupInstance.dismiss` dentro de um `.catch` para "mover o throw para fora da cadeia de promise".

### Por que quebra

- `callService` retorna promise. Em rede lenta ou servico pesado, 500ms pode nao ser suficiente e o codigo do `$timeout` executa com dado velho.
- Em rede rapida, o handler executa antes do tempo e fica preso atras do timer.
- Nunca se sabe se o servico falhou ou foi cancelado quando o callback do timer roda.
- O callback do timer NAO entra no ciclo de digest sempre (se usar `setTimeout` cru), pulando atualizacoes de binding.

### Forma correta

Sempre **encadear no `.then`** da promise:

```javascript
ServiceProxy.callService('mge@Algo.fazer', payload)
    .then(function(data) {
        self.atualizarTela(data.responseBody);
    })
    .catch(function(err) {
        // trate ou deixe o popup padrao agir
    });
```

Para sequenciar, encadeie com outro `.then`. Para paralelizar, use `$q.all([p1, p2])`.

---

## 2. Polling de `dataset.isLoaded()` em vez de `addRefreshedListener`

### Padrao ruim

```javascript
var t = setInterval(function() {
    if (self.ds.isLoaded()) {
        clearInterval(t);
        self.prosseguir();
    }
}, 100);
```

Variante pior com `$timeout` recursivo fazendo a mesma coisa.

### Por que quebra

- `isLoaded()` fica `true` **para sempre** apos o primeiro load ([dataset.controller.js:1119](../../../../../sankhya-js/src/components/dataset/dataset.controller.js#L1119)). Em refreshes subsequentes continua `true`, entao polling nao deteta "terminou este refresh".
- Gera carga desnecessaria no ciclo de digest a cada 100ms.
- Risco de memory leak se a tela fechar antes do load terminar e o interval nao for limpo.

### Forma correta

```javascript
var removeListener = self.ds.addRefreshedListener(function(reason) {
    self.prosseguir();
});
$scope.$on('$destroy', removeListener);
```

Ou, para o primeiro load especificamente:

```javascript
self.ds.initAndRefresh().then(function() {
    self.prosseguir();
});
```

---

## 3. Chamar `getCurrentRow()` imediatamente apos `refresh()`

### Padrao ruim

```javascript
self.ds.refresh();
var row = self.ds.getCurrentRow();   // ainda e o row anterior
```

### Por que quebra

`refresh()` retorna promise — a leitura sincrona logo abaixo pega o registro anterior. Funciona "por sorte" em cache quente, quebra quando o servico e chamado de verdade.

### Forma correta

```javascript
self.ds.refresh().then(function() {
    var row = self.ds.getCurrentRow();
});
```

Ou use `addRefreshedListener` se precisar reagir a todos os refreshes.

---

## 4. Esquecer de desregistrar listeners do dataset/ServiceProxy

### Padrao ruim

```javascript
self.ds.addDataSavedListener(function(isNew, records) {
    ...
});
// sem guardar o retorno nem limpar no $destroy
```

### Por que quebra

Todos os `add*Listener` do dataset retornam **funcao de desregistro** (ver todos os `add*Listener` em [dataset.controller.js:5904-6188](../../../../../sankhya-js/src/components/dataset/dataset.controller.js#L5904-L6188)). Se a tela e reaberta sem recarregar o bundle, o listener antigo continua. Na segunda sessao, cada save dispara o listener 2x. Terceira, 3x. E assim por diante.

Vale o mesmo para `ServiceProxy.addClientEvent` — retorna `ClientEventHandler` com `.unregistry()` ([serviceproxy.service.js:86](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L86)).

### Forma correta

```javascript
var off = self.ds.addDataSavedListener(fn);
$scope.$on('$destroy', off);
```

Ou passar `$scope` onde a API suportar (ex.: `SkComponentRegistry.register(inst, handle, $scope)`).

---

## 5. Mutacao direta de `record[i] = valor`

### Padrao ruim

```javascript
var row = self.ds.getCurrentRow();
row[indexCampoX] = 'novo valor';
```

### Por que quebra

- Nao notifica observers/listeners do dataset.
- Field binders e validadores ligados ao campo nao recalculam.
- Triggers do `addFieldValueEvaluator` nao disparam.
- Row fica "modificada" mas `isRecordDirty()` pode retornar errado.

### Forma correta

```javascript
self.ds.setFieldValue('CAMPOX', 'novo valor');
```

`setFieldValue` passa pelos interceptadores, atualiza binders e dispara `dataModified`.

---

## 6. Construir URL de servico na mao em vez de usar `ServiceProxy`

### Padrao ruim

```javascript
$http.post('/mgecom/service.sbr?serviceName=X.y', payload);
```

### Por que quebra

Nao aplica: headers `appkey`/`sktk`, counter incremental, `mgeSession`, `resourceID`, `globalID`, `flowID`, popup de erro padrao, client events, print listeners, monitoramento de rede, modulo em update, serializacao de chamadas, suporte a abort. Tudo isso esta em [serviceproxy.service.js:150-394](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L150-L394).

### Forma correta

```javascript
ServiceProxy.callService('mgecom@X.y', payload);
```

Sempre. Mesmo para GET (passar `{ method: 'GET' }` no config).

---

## 7. Servicos sem prefixo de modulo

### Padrao ruim

```javascript
// Servico esta no mgecom, mas foi chamado sem prefixo
ServiceProxy.callService('FichaParceiroSP.getFinanceiros', payload);
```

### Por que quebra

Sem `@`, cai em `defModule = "mge"` ([serviceproxy.service.js:151](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L151)). Request vai para `/mge/service.sbr?...` e o backend retorna erro de "servico nao encontrado".

Em triagem: se o bug reporta erro "servico X.y nao encontrado" e o servico existe, verifique o prefixo de modulo no frontend.

### Forma correta

```javascript
ServiceProxy.callService('mgecom@FichaParceiroSP.getFinanceiros', payload);
```

---

## 8. `callService` com `callback` E `.then` ao mesmo tempo

### Padrao ruim

```javascript
ServiceProxy.callService('mge@X.y', payload, {
    callback: function(data) { /* handler A */ }
}).then(function(data) { /* handler B */ });
```

### Por que quebra

Se `config.callback` esta setado, o `.then` nunca recebe o dado ([serviceproxy.service.js:289-293](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L289-L293)). Handler B so dispara em caso de erro (e mesmo assim so se `exceptionCallback` nao estiver setado).

### Forma correta

Use **um modelo ou outro** — de preferencia `.then` (promise-based). `callback`/`exceptionCallback` existe por compatibilidade com codigo mais antigo.

---

## 9. Duplicar handle no `SkComponentRegistry` sem `ignoreDuplicity`

### Padrao ruim

```javascript
// Em dois controllers diferentes, sem coordenar
SkComponentRegistry.register(self, 'meuHandle');
```

### Por que quebra

O segundo `register` com mesmo handle gera `console.warn` e retorna `angular.noop` ([componentregistry.service.js:114-118](../../../../../sankhya-js/src/core/services/registry/componentregistry.service.js#L114-L118)). A instancia antiga continua ativa — se ja foi destruida, `get(handle)` resolve com zumbi.

Em triagem: bugs de "esta chamando o metodo errado" / "mostra dado de tela anterior" em telas que usam `SkComponentRegistry` frequentemente tem raiz aqui.

### Forma correta

- Usar handles unicos por escopo de tela (ex.: incluir resourceId ou uuid).
- Quando a sobrescrita e desejada, passar `ignoreDuplicity: true`.
- Sempre passar `$scope` no terceiro argumento para auto-desregistro.

---

## 10. Tratar erro de servico via try/catch sincrono

### Padrao ruim

```javascript
try {
    ServiceProxy.callService('mge@X.y', payload);
} catch (e) {
    // nunca entra aqui — servico e assincrono
}
```

### Por que quebra

`callService` retorna promise imediatamente. O erro vai via rejection, nao exception. O `try/catch` so pegaria erro na **construcao** da chamada (ex.: metodo HTTP invalido — [serviceproxy.service.js:134](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L134)).

### Forma correta

```javascript
ServiceProxy.callService('mge@X.y', payload)
    .catch(function(err) { ... });
```

---

## 11. Popup duplicado em caso de erro

### Padrao ruim

```javascript
ServiceProxy.callService('mge@X.y', payload)
    .catch(function(err) {
        MessageUtils.showError('Erro', 'Falhou: ' + err.statusMessage);
    });
```

### Por que quebra

O ServiceProxy **ja exibe popup de erro** por default em `handleDefaultSystemError` ([serviceproxy.service.js:447-459](../../../../../sankhya-js/src/core/util/http/serviceproxy.service.js#L447-L459)). O codigo acima abre o popup do framework **e** o popup manual — usuario ve dois modais sobrepostos.

### Forma correta

Escolha um:

```javascript
// Opcao A: so popup manual, suprime o padrao
ServiceProxy.callService('mge@X.y', payload, {
    ignorePopUpErrorMsgs: true
}).catch(handler);

// Opcao B: errorHandler customizado substitui o padrao
ServiceProxy.callService('mge@X.y', payload, {
    errorHandler: function(data, status) {
        MessageUtils.showError(...);
    }
});
```

---

## 12. Injetar `$SkInjector` em service/controller

### Padrao ruim

```javascript
angular.module('snk.commons').service('MinhaSvc',
  ['$SkInjector', function($SkInjector) { ... }]);
```

### Por que quebra

O `$get` do provider lanca `Error('Este injector deve ser usado apenas em configurações de módulos.')` ([framework.config.js:47](../../../../../sankhya-js/src/core/framework.config.js#L47)).

### Forma correta

Usar `$SkInjectorProvider` apenas em `.config([...])`, **nunca** em services/controllers.

---

## 13. Alterar `$scope.parentDataset` apos bootstrap

Dataset usa `AngularUtil.addSingleWatch($scope, 'parentDataset', setParentDataSet)` — `addSingleWatch` dispara uma unica vez. Trocar o parent depois nao re-configura a hierarquia.

### Forma correta

Use `dataset.setParentDataSet(outro)` explicitamente.

---

## 14. Acessar `workspace` global diretamente

### Padrao ruim

```javascript
window.workspace.openAppActivity(id, pk);
```

### Por que quebra

Em ambiente standalone (teste, iframe sem shell, SSR-like), `workspace` e `undefined`. O codigo quebra com TypeError.

### Forma correta

Usar `SkWorkspace` — todos os metodos fazem `workspace && workspace.xxx()` ([workspace.service.js:124,131,...](../../../../../sankhya-js/src/core/workspace/workspace.service.js#L124)).

```javascript
SkWorkspace.openAppActivity(id, pk);
```

---

## 15. Coluna fisica (fora do dicionario) no fieldset do `loadRecords`

### Padrao ruim

```javascript
CRUDServiceProvider.loadRecords('ItemNota', {
    fieldset: { fields: ['NUNOTA', 'CODPROD', 'PESO'] } // PESO existe em TGFITE, mas nao e campo de dicionario da instancia
});
```

### Por que quebra

`CRUDServiceProvider.loadRecords` (e os metadados de entidade via `MetadataProvider`) so enxergam campos do DICIONARIO da instancia — NAO colunas fisicas da tabela. Incluir no fieldset uma coluna que existe na tabela mas nao e campo de dicionario da instancia (ex.: `TGFITE.PESO` na entidade `ItemNota`) falha com `CORE_E04064 'Descritor do campo invalido'`. O `describe_table` mostra a coluna fisica e induz ao erro.

### Forma correta

Antes de usar um campo no `loadRecords`, confirme que e campo de dicionario da instancia (nao basta o `describe_table`, que mostra a coluna fisica). Para campos fora do DD, ou agregacoes/joins (SUM/MAX/GROUP BY, header+item), use um Service backend nativo (`*SP`), nao `loadRecords`.

---

## Checklist rapido para triagem

Em bugs de tela AngularJS/sankhya-js, investigue primeiro:

- [ ] Servico sendo chamado com prefixo de modulo correto?
- [ ] Ha `$timeout`/`setTimeout` aguardando algo assincrono?
- [ ] Listeners de dataset/ServiceProxy estao sendo desregistrados?
- [ ] `refresh()` seguido de leitura sincrona sem `.then()`?
- [ ] `setFieldValue` vs mutacao direta de record[i]?
- [ ] Popup duplicado de erro?
- [ ] Handle duplicado no `SkComponentRegistry`?
- [ ] `callback` + `.then` no mesmo `callService`?

Esses oito itens cobrem a maioria das classes de bugs recorrentes em telas antigas.
