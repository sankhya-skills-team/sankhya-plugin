# MessageUtils e SanPopup — dialogos e popups

Dois servicos complementares para dialogos modais:

- **`MessageUtils`** — dialogos de alerta/erro/info/confirmacao prontos.
- **`SanPopup`** — servico de baixo nivel para popups custom com template/controller proprios. `MessageUtils` e construido em cima de `SanPopup`.

Fontes:
- [core/util/message/messageutil.service.js](../../../../sankhya-js/src/core/util/message/messageutil.service.js) (969 linhas)
- [components/popup/popup.service.js](../../../../sankhya-js/src/components/popup/popup.service.js) (386 linhas)

---

## MessageUtils — constantes

Titulos i18n pre-definidos ([messageutil.service.js:15-19](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L15-L19)):

```javascript
MessageUtils.TITLE_ERROR          // i18n('Geral.msgTitleErro')
MessageUtils.TITLE_INTERNALERROR  // i18n('Geral.msgTitleErroInterno')
MessageUtils.TITLE_WARNING        // i18n('Geral.msgTitleAviso')
MessageUtils.TITLE_CONFIRMATION   // i18n('Geral.msgTitleConfirmacao')
MessageUtils.TITLE_INFORMATION    // i18n('Geral.msgTitleInformacao')
```

Use estes em vez de literais para manter consistencia visual/i18n.

---

## MessageUtils — API

Todos retornam **promise** que resolve quando o usuario fecha. Assinatura curta (so `msg`) usa o titulo default da categoria.

### Mensagens simples (so botao OK)

| Metodo | Tipo visual | Uso |
|--------|-------------|-----|
| `showInfo(title?, msg, emitMessage?)` | `type: 'primary'` | Info |
| `showAlert(title?, msg, emitMessage?)` | `type: 'warning'` | Aviso |
| `showError(title?, msg, emitMessage?)` | `type: 'danger'` | Erro |

Todas resolvem a promise quando usuario fecha ([:124-128, :168-172, :212-216](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L124-L128)).

```javascript
MessageUtils.showInfo('Registro salvo com sucesso.');

MessageUtils.showError(
    MessageUtils.TITLE_ERROR,
    'Codigo do parceiro invalido.'
);
```

### Confirmacao (Sim / Nao / Cancelar)

**`simpleConfirm(title?, msg, showAsWarning?, emitMessage?, options?)`** — so Sim e Nao ([:290-319](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L290-L319)).

```javascript
MessageUtils.simpleConfirm('Deseja realmente excluir?')
    .then(function() {
        // usuario clicou Sim
    }, function(reason) {
        // usuario clicou Nao ou fechou
        // reason === 'no' indica clique em Nao
    });
```

**`confirm(title?, msg, okBtnLabel?, noBtnLabel?, showAsWarning?, emitMessage?, options?)`** — Sim, Nao **e** Cancelar ([:484-510](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L484-L510)).

```javascript
MessageUtils.confirm('Deseja fechar sem salvar?')
    .then(function() {
        // Sim
    }, function(reason) {
        if (reason === 'no') {
            // clicou Nao
        } else {
            // Cancelar, ESC, backdrop, X
        }
    });
```

Convencao dos `reason` strings documentada no proprio codigo ([:465-478](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L465-L478)).

### Builders fluentes

Quando a chamada tem varios parametros, use o builder — retorna promise ao chamar `.show()` ([:42-90](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L42-L90)).

```javascript
MessageUtils.simpleConfirmBuilder()
    .title(MessageUtils.TITLE_CONFIRMATION)
    .msg('Deseja prosseguir?')
    .okLabel('Prosseguir')
    .noLabel('Cancelar')
    .okTheme('warning')
    .show();

MessageUtils.confirmBuilder()
    .msg('Deseja fechar?')
    .showBtnCancel(true)
    .cancelLabel('Voltar')
    .show();

MessageUtils.errorBuilder()
    .msg('Falha na operacao.')
    .show();
```

`msg` e titulo passam por `i18n` automaticamente (os campos tem `transformer: i18n`).

### Mensagens com "ver mais"

Para erros com detalhes longos (stack traces, payloads), usar variantes "show more" ([:593-644](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L593-L644)):

```javascript
MessageUtils.showErrorShowMore({
    msg: 'Falha ao salvar nota.',
    moreMsg: '<pre>' + err.stackTrace + '</pre>'
});

MessageUtils.showAlertShowMore({ msg, moreMsg, title?, icone? });
MessageUtils.showInfoShowMore({ msg, moreMsg, title?, icone? });
```

`moreMsg` aceita HTML ([template em :531-545](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L531-L545)). Se vazio, exibe `EntityCard.semInformacoes`.

### Troubleshooting

Para erros sistemicos com codigo de rastreio:

```javascript
MessageUtils.showErrorTroubleShooting(title?, errorCode, msg, emitMessage?);
MessageUtils.showWarningTroubleShooting(title?, errorCode, msg, emitMessage?);
MessageUtils.showWarningTroubleShootingWithStacktrace(...);
```

O botao "Troubleshooting" so aparece se o `errorCode` for diferente de `ServiceProxyConstants.TROUBLE_SHOOT.DEFAULT_CODE` ([:680](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L680)).

### Variantes especializadas

| Metodo | Funcao |
|--------|--------|
| `showAlertWithConfirm(title?, msg, emitMessage?, addOptions?)` | Alerta **obrigatorio** — sem ESC, sem X, so botao "Sim" ([:238-273](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L238-L273)) |
| `showAlertOptionNotDisplay(title?, msg)` | Alerta com checkbox "Nao exibir novamente" ([:406-432](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L406-L432)) |
| `simpleConfirmOptionApplyForAll(title?, msg, showAsWarning?, emitMessage?, options?)` | Confirm com checkbox "Aplicar para todos" ([:337-373](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L337-L373)) |
| `confirmSerialized(...)` | Confirmacao serializada (fila) |

---

## SanPopup — popup generico

Servico de baixo nivel. Use quando precisa de formulario, wizard, grade ou qualquer conteudo custom.

### Assinatura

```javascript
var popupInstance = SanPopup.open(options);
```

Retorna objeto com:

| Propriedade | Tipo | Uso |
|-------------|------|-----|
| `result` | promise | Resolve em `$success(result)`, rejeita em `$dismiss(reason)` |
| `opened` | promise | Resolve quando popup montou (template + resolve prontos) |
| `rendered` | promise | Resolve quando DOM renderizou |
| `success(result)` | fn | Fecha com sucesso programaticamente |
| `dismiss(reason)` | fn | Fecha com rejeicao programaticamente |
| `setTitle(title)` | fn | Atualiza titulo em runtime |
| `notify(result)` | fn | `notify` na promise (progresso) |
| `center()` | fn | Re-centraliza janela |

Evidencia: [popup.service.js:151-369](../../../../sankhya-js/src/components/popup/popup.service.js#L151-L369).

### Opcoes principais

Defaults em [:39-60](../../../../sankhya-js/src/components/popup/popup.service.js#L39-L60), lista completa documentada em [:78-123](../../../../sankhya-js/src/components/popup/popup.service.js#L78-L123).

| Opcao | Default | Uso |
|-------|---------|-----|
| `title` | — (obrigatorio; throw se ausente, [:213-215](../../../../sankhya-js/src/components/popup/popup.service.js#L213-L215)) | Titulo no cabecalho |
| `template` / `templateUrl` | — (um obrigatorio, [:217-219](../../../../sankhya-js/src/components/popup/popup.service.js#L217-L219)) | Conteudo |
| `controller` | — | Controller do popup; recebe `$popupInstance` injetado |
| `controllerAs` | — | Syntatic sugar para controller-as |
| `resolve` | `{}` | Mesmo padrao das rotas Angular |
| `size` | — | `'sm'`, `'md'`, `'lg'`, `'xl'`, `'alert'` |
| `type` | `'default'` | `'default'`, `'danger'`, `'success'`, `'info'`, `'primary'`, `'warning'`, `'brand'`, `'gray'` |
| `backdrop` | `'static'` | `true`, `false` ou `'static'` (clique no backdrop nao fecha) |
| `keyboard` | `true` | Habilita fechamento via ESC |
| `animation` | `false` | Animacao de abertura |
| `showBtnOk` | `true` | Botao OK |
| `showBtnCancel` | `true` | Botao Cancelar |
| `showBtnNo` | `false` | Botao Nao |
| `showIconClose` | `true` | Icone X no canto |
| `enableBtnOk` | `true` | Habilita OK |
| `enableBtnNo` | `true` | Habilita Nao |
| `okBtnLabel` / `cancelBtnLabel` / `noBtnLabel` | `Geral.lblOK` / `Geral.lblCancelar` / `Geral.lblNo` | Labels |
| `okBtnClass` / `cancelBtnClass` / `noBtnClass` | — | Classes CSS |
| `windowClass` | — | Classe adicional na janela |
| `backdropClass` | — | Classe adicional no backdrop |
| `leftBottomBar` / `rightBottomBar` | `[]` | Botoes adicionais no rodape |
| `largeBottomButtons` | `false` | Botoes maiores |
| `compileFooter` | `false` | Compilar rodape customizado |
| `grayBG` | `false` | Fundo cinza (para popups com formulario) |
| `bodyPadding` | `true` | Padding interno |
| `scrollContainer` | `true` | Conteudo com scroll |
| `hideHeader` | `false` | Esconde cabecalho |
| `ignoreLoading` | `false` | Nao bloqueia abertura se `sk-loading-bar` ativo |
| `useCache` | `true` | Usa cache do popup stack |
| `controllerCache` | `false` | Nao recria controller em reabertura |
| `iconTitle` | — | Icone no titulo (detecta `.svg` vs font-icon automaticamente) |
| `id` | — | Identificador para cache reutilizavel |

### Exemplo canonico

```javascript
var popupInstance = SanPopup.open({
    title: 'Cadastro de Observacao',
    templateUrl: 'commons/observacao/observacao.tpl.html',
    controller: 'ObservacaoPopupController',
    controllerAs: 'ctrl',
    size: 'md',
    windowClass: 'observacao-popup',
    resolve: {
        parametros: function () { return { codParc: codParc }; }
    }
});

popupInstance.result.then(function(resultado) {
    // $success foi chamado
}, function(reason) {
    // $dismiss foi chamado
});
```

### `$success` / `$dismiss` no scope

SanPopup injeta no `$scope` do popup duas funcoes ([popup.service.js:9-16](../../../../sankhya-js/src/components/popup/popup.service.js#L9-L16) e [:286-287](../../../../sankhya-js/src/components/popup/popup.service.js#L286-L287)):

```html
<button ng-click="$success(ctrl.resultado)">Salvar</button>
<button ng-click="$dismiss('cancel')">Cancelar</button>
```

Elas disparam o fechamento e resolvem/rejeitam a promise `popupInstance.result`. Se o popup tem controller, `$popupInstance` e injetado automaticamente:

```javascript
angular.module('x').controller('ObservacaoPopupController',
    ['$scope', '$popupInstance', 'parametros',
    function($scope, $popupInstance, parametros) {
        var ctrl = this;

        ctrl.salvar = function() {
            $popupInstance.success(ctrl.dados);
        };
    }]);
```

### Evento `popup.closing` (cancelar fechamento)

Antes de fechar, o popup emite `popup.closing` no seu scope. Se o listener chamar `preventDefault()`, o popup permanece aberto ([popup.service.js:18-22](../../../../sankhya-js/src/components/popup/popup.service.js#L18-L22)).

```javascript
$scope.$on('popup.closing', function(event, resultOrReason, isSuccess) {
    if (isSuccess && !ctrl.formularioValido()) {
        event.preventDefault();
    }
});
```

### Sobrescrita no `$scope` do popup

Os seguintes bindings no `$scope` do popup modificam comportamento do chrome ([popup.service.js:28-33](../../../../sankhya-js/src/components/popup/popup.service.js#L28-L33)):

```javascript
$scope.$success        // sobrescreve o fechamento com sucesso
$scope.$dismiss        // sobrescreve o fechamento com dismiss
$scope.$popupTitle     // novo titulo
$scope.$enableBtnOk    // habilita/desabilita OK
$scope.$enableBtnNo    // habilita/desabilita Nao
```

Util para formularios que dependem de validacao ao vivo.

---

## Gotchas

### 1. Popup duplicado quando o ServiceProxy ja mostrou erro

O ServiceProxy exibe popup automaticamente em falha ([anti-patterns.md secao 11](anti-patterns.md)). Nao chame `MessageUtils.showError(...)` no `.catch` a menos que passe `{ ignorePopUpErrorMsgs: true }` no `callService`. Senao, dois modais sobrepostos.

### 2. `reason === 'no'` para detectar Nao

`simpleConfirm`/`confirm` rejeitam com string `'no'` quando usuario clica Nao, e com outras strings (ou `undefined`) quando fecha por outras vias. Testar explicitamente.

### 3. `backdrop: 'static'` impede fechamento por clique no backdrop

Todos os dialogos `MessageUtils` usam `backdrop: 'static'` (ou equivalente) — ESC ou botao X sao as unicas saidas em algumas variantes (`showAlertWithConfirm` desativa ate isso: `keyboard: false, showIconClose: false`, [:253-256](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L253-L256)).

### 4. `SanPopup.open` sem `title` lanca erro

```javascript
// Throw: 'É obrigatorio informar um título.'
SanPopup.open({ templateUrl: '...' });
```

Evidencia: [:213-215](../../../../sankhya-js/src/components/popup/popup.service.js#L213-L215).

### 5. `SanPopup.open` sem `template`/`templateUrl` lanca erro

```javascript
// Throw: 'One of template or templateUrl options is required.'
SanPopup.open({ title: 'X' });
```

Evidencia: [:217-219](../../../../sankhya-js/src/components/popup/popup.service.js#L217-L219).

### 6. `controllerCache` guarda o controller entre reaberturas

Com `controllerCache: true`, o controller nao e recriado — estado persiste. Util para popups reabertos com frequencia, mas cuidado: eventos registrados no `$scope` podem disparar duplicado. Usar `$$popupInstance.$$currentPopupInstance` para o popup atual ([:162-168](../../../../sankhya-js/src/components/popup/popup.service.js#L162-L168)).

### 7. `openedPopup` e global, unico

`SanPopup.openedPopup = { opened: bool, dismiss: fn }` guarda **a ultima** popup aberta ([:66-68](../../../../sankhya-js/src/components/popup/popup.service.js#L66-L68)). Com stack de popups, `openedPopup` aponta so pro topo. Para multiplos modais, usar `SanPopupStack` diretamente.

### 8. Botao troubleshooting so aparece se `errorCode` nao e default

Em `showErrorTroubleShooting`, o botao so aparece se `errorCode !== ServiceProxyConstants.TROUBLE_SHOOT.DEFAULT_CODE` ([:680](../../../../sankhya-js/src/core/util/message/messageutil.service.js#L680)). Passar codigo valido ou usar `showError` simples.

### 9. Alert vs Info vs Error — usar a semantica correta

Os tres tem o mesmo layout. A diferenca e o `type` (cor, icone):
- `showInfo` → `type: 'primary'` (azul, info)
- `showAlert` → `type: 'warning'` (laranja/amarelo)
- `showError` → `type: 'danger'` (vermelho)

Nao usar `showError` para mensagens informativas — rompe padrao visual.

### 10. `MessageUtils` e `SanPopup` operam no `$rootScope`

Ambos criam escopos a partir de `$rootScope.$new()` ([popup.service.js:234-236](../../../../sankhya-js/src/components/popup/popup.service.js#L234-L236)). Nao dependem do `$scope` do chamador — sobrevivem a `$destroy` do controller que abriu. Corolario: se o controller que abriu e destruido, o popup continua aberto (se backdrop static e sem interacao do usuario).

---

## Padroes de uso

### Confirmacao antes de acao destrutiva

```javascript
function excluir() {
    MessageUtils.simpleConfirm(
        MessageUtils.TITLE_CONFIRMATION,
        'Deseja realmente excluir este registro?',
        true  // showAsWarning
    ).then(function() {
        self.ds.deleteRecord();
    });
}
```

### Mensagem apos salvar com sucesso

```javascript
ServiceProxy.callService('mge@X.salvar', payload)
    .then(function(data) {
        return MessageUtils.showInfo('Salvo com sucesso.');
    })
    .then(function() {
        $popupInstance.success();
    });
```

### Popup custom com controller

```javascript
SanPopup.open({
    title: SkI18nService.instant('Financeiro.lblAjuste'),
    templateUrl: 'commons/ajuste/ajuste.tpl.html',
    controller: 'AjusteController',
    controllerAs: 'ctrl',
    size: 'md',
    backdrop: 'static',
    resolve: {
        dados: function() { return ctrl.linhaSelecionada; }
    }
}).result.then(function(resultado) {
    self.ds.setFieldValue('VLRAJUSTE', resultado.valor);
});
```

### Validar antes de fechar

```javascript
// No controller do popup
$scope.$on('popup.closing', function(event, result, isSuccess) {
    if (isSuccess) {
        if (!ctrl.formValido()) {
            event.preventDefault();
            MessageUtils.showAlert('Preencha os campos obrigatorios.');
        }
    }
});
```

---

## Checklist de triagem para bugs de dialogo

- [ ] Popup duplicado? Verificar se ServiceProxy ja mostrou popup de erro (`ignorePopUpErrorMsgs`).
- [ ] Promise de confirm nao rejeita em Nao? Verificar `reason === 'no'` vs outros.
- [ ] Popup "congelado" sem fechar? `backdrop: 'static'` + `keyboard: false` + `showIconClose: false` pode ter sido setado.
- [ ] Popup abre vazio? `template`/`templateUrl` ausente gera throw — verificar console.
- [ ] Popup reabre com estado "sujo"? `controllerCache: true` preserva controller.
- [ ] Popup nao fecha ao clicar OK? Verificar `popup.closing` com `preventDefault()`.
- [ ] Multiplos popups sobrepostos? `SanPopup.openedPopup` so referencia o topo — usar `SanPopupStack`.
- [ ] Alert com cor errada? Conferir se usou `showError` em mensagem informativa.
