# sankhya-js — snk.core

Módulo de infraestrutura do framework: aplicação, layout, utilitários, tema e serviços de apoio.

---

## sk-application

**ID:** `snk.core.application.directive:sk-application`
**Tipo:** directive (cria novo scope)

**Elemento raiz obrigatório** para todas as telas HTML5/xhtml5. Implementa o `DefaultSankhyaApplication` que orquestra funcionalidades padrão do framework.

```html
<!-- Como elemento -->
<sk-application ng-controller="MeuController as ctrl">
    <!-- conteúdo da tela -->
</sk-application>

<!-- Como atributo -->
<div sk-application ng-controller="MeuController as ctrl">
    <!-- conteúdo da tela -->
</div>
```

---

## Directives de Layout (snk.core.directives.layout)

Directives de atributo para estilização inline:

| Diretiva | Descrição | Exemplo |
|---|---|---|
| `sk-bg-color` | Cor de fundo | `sk-bg-color="primary"` |
| `sk-border` | Borda | `sk-border="1px solid red"` |
| `sk-color` | Cor do texto | `sk-color="accent"` |
| `sk-font-size` | Tamanho da fonte | `sk-font-size="14"` |
| `sk-overflow` | Overflow | `sk-overflow="auto"` |
| `sk-padding` | Padding | `sk-padding="10"` |
| `sk-position` | Posicionamento | `sk-position="relative"` |
| `sk-margin` | Margem | `sk-margin="10"` |

**Uso:**
```html
<div sk-padding="20" sk-bg-color="white" sk-border="1px solid #ccc">
    conteúdo
</div>
```

---

## MessageUtils

**ID:** `snk.core.util.service:MessageUtils`
**Tipo:** service

Serviço para mensagens ao usuário. **Usar sempre este serviço** para manter o padrão visual do sistema.

**Métodos:**

| Método | Descrição | Retorna |
|---|---|---|
| `showInfo(title, msg)` | Mensagem informativa | Promise (resolve ao fechar) |
| `showAlert(title, msg)` | Mensagem de alerta | Promise (resolve ao fechar) |
| `showAlertWithConfirm(title, msg)` | Alerta com confirmação obrigatória | Promise |
| `showError(title, msg)` | Mensagem de erro | Promise (resolve ao fechar) |
| `confirm(title, msg, okBtnLabel?, noBtnLabel?, showAsWarning?)` | Confirmação com Sim/Não/Cancelar | httpPromise |
| `simpleConfirm(title, msg, showAsWarning?)` | Confirmação apenas Sim/Não | httpPromise |
| `showAlertOptionNotDisplay(title, msg, showAsWarning?)` | Alerta sem opção de "não mostrar" | httpPromise |
| `showErrorTroubleShooting(...)` | Erro com link para wiki | Promise |
| `showWarningTroubleShooting(...)` | Aviso com link para wiki | Promise |

**Exemplos:**

```js
// Informação simples
MessageUtils.showInfo('Sucesso', 'Registro salvo com sucesso.');

// Confirmação
MessageUtils.confirm('Atenção', 'Deseja excluir este registro?')
    .then(function() {
        // usuário confirmou (Sim)
        ctrl.excluir();
    }, function(reason) {
        if (reason === 'no') {
            // clicou Não
        } else {
            // fechou ou cancelou
        }
    });

// Confirmação simples (Sim/Não apenas)
MessageUtils.simpleConfirm('Confirmar', 'Tem certeza?')
    .then(function() { /* sim */ }, function() { /* não */ });

// Erro
MessageUtils.showError('Erro', 'Falha ao processar. Tente novamente.');
```

---

## DateBuilder

**ID:** `snk.core.util.service:DateBuilder`
**Tipo:** service

Utilitário para construção e manipulação de datas.

---

## HierarchyUtils

**ID:** `snk.core.util.service:HierarchyUtils`
**Tipo:** service

Utilitário para operações em estruturas hierárquicas.

---

## MessageUtils — Parâmetros de TroubleShooting

```js
MessageUtils.showErrorTroubleShooting(
    'Erro de Integração',    // title
    'ERR-001',               // errorCode
    'Falha na API externa',  // msg
    'http://wiki/ERR-001',   // wikiLocale
    'MinhaEmpresa',          // company
    'error'                  // exibe (tipo)
);
```

---

## UserAgentUtils

**ID:** `snk.core.util.service:UserAgentUtils`

Detecta informações do browser e dispositivo.

---

## skMedia

**ID:** `snk.core.util.service:skMedia`

Responsividade — detecta breakpoints de tela.

---

## PositionUtils

**ID:** `snk.core.util.service:PositionUtils`

Utilitário para posicionamento de elementos no DOM.

---

## SwipeUtil

**ID:** `snk.core.util.service:SwipeUtil`

Detecção de gestos de swipe para mobile.

---

## UserDetailBuilder

**ID:** `snk.core.util.service:UserDetailBuilder`

Constrói informações detalhadas do usuário logado.

---

## AvisosUtils

**ID:** `snk.core.util.avisos:AvisosUtils`

Utilitário para exibição de avisos do sistema.

---

## SkConstants

**ID:** `snk.core.util:SkConstants`

Constantes globais do framework.

---

## md-virtual-repeat / md-virtual-repeat-container

**ID:** `snk.core.util.directive:md-virtual-repeat`

Renderização virtual de listas longas (somente renderiza itens visíveis).

```html
<md-virtual-repeat-container>
    <div md-virtual-repeat="item in ctrl.listaGrande">
        {{ item.nome }}
    </div>
</md-virtual-repeat-container>
```

---

## ThemeColors

**ID:** `snk.core.theme.service:ThemeColors`
**Tipo:** service

Acesso às cores do tema atual.

---

## skTourService

**ID:** `snk.core.tour.service:skTourService`
**Tipo:** service

Serviço para tour guiado (onboarding) nas telas.

---

## SkComponentRegistry

**ID:** `snk.core.services.registry.service:SkComponentRegistry`
**Tipo:** service

Registro de componentes do framework. Permite recuperar instâncias de componentes por ID.

---

## snk.db — MetadataProvider

**ID:** `snk.db.metadataprovider.service:MetadataProvider`
**Tipo:** service

Acessa metadados de entidades via API REST do backend.

```js
MetadataProvider.getEntityMetadata(entityId)
    .then(function(metadata) {
        // metadata com definições de campos
    });
```

---

## snk.db — MGEParameters

**ID:** `snk.db.parameters.service:MGEParameters`
**Tipo:** service

Acessa parâmetros do sistema (tabela de parâmetros do Sankhya).
