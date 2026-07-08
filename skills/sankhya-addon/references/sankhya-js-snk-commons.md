# sankhya-js — snk.commons e outros módulos

Módulo de componentes comuns (liberações, ação programada, BPM), módulos auxiliares e interfaces utilitárias.

---

## snk.commons

### sk-acao-programada

**ID:** `snk.commons.acaoprogramada.directive:sk-acao-programada`
**Tipo:** directive

Componente para configuração e execução de ações programadas/agendadas.

---

## snk.commons.liberacoes

### sk-liberacoes

**ID:** `snk.commons.liberacoes.component:sk-liberacoes`
**Tipo:** component

Componente de liberação de limites — grade + formulário integrados.

```html
<sk-liberacoes
    sk-data="{object}"
    sk-close-function="{function}"
    sk-ajustaperc-lib-lim="{boolean=false}"
    sk-precision-to-mask="{number=2}">
</sk-liberacoes>
```

| Parâmetro | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-data` | object | - | Objeto com as liberações |
| `sk-close-function` | function | - | Função de fechamento do popup |
| `sk-ajustaperc-lib-lim` | boolean | false | Ajusta precisão do valor percentual |
| `sk-precision-to-mask` | number | 2 | Casas decimais do valor |

### sk-painel-liberacoes

**ID:** `snk.commons.liberacoes.component:sk-painel-liberacoes`
**Tipo:** component

Painel de liberações.

### PopupLiberacoes

**ID:** `snk.commons.liberacoes.service:PopupLiberacoes`
**Tipo:** service

Serviço para abrir o popup de liberações programaticamente.

---

## snk.commons.workFlow.modelerBpmn

### sk-modeler-bpmn

**ID:** `snk.commons.workFlow.modelerBpmn.directive:sk-modeler-bpmn`
**Tipo:** directive

Modelador de processos BPMN integrado ao workflow do Sankhya.

---

## sk-simple-form

Módulo de formulário simplificado — alternativa ao `snk.form` com estrutura mais direta.

### sk-simple-form

**ID:** `sk-simple-form.directive:sk-simple-form`

Formulário simples com grupos e itens declarativos.

```html
<sk-simple-form>
    <sk-simple-group label="Dados Básicos">
        <sk-simple-item label="Nome">
            <sk-text-input sk-value="ctrl.nome"></sk-text-input>
        </sk-simple-item>
    </sk-simple-group>
</sk-simple-form>
```

### sk-simple-group

**ID:** `sk-simple-form.directive:sk-simple-group`

Agrupador de itens dentro do `sk-simple-form`.

### sk-simple-item

**ID:** `sk-simple-form.directive:sk-simple-item`

Item/campo dentro de um `sk-simple-group`.

---

## snk.i18n

### sk-i18n

**ID:** `snk.i18n.directive:sk-i18n`

Diretiva de internacionalização — traduz chaves de i18n para o idioma atual.

```html
<span sk-i18n="Modulo.tela.labelCampo"></span>
```

---

## util.common — Interfaces e Critérios

### DataSource (interface)

**ID:** `util.common.interface:DataSource`

Interface base para datasources (implementada pelo `sk-dataset`).

| Método | Descrição |
|---|---|
| `refresh()` | Recarrega os dados |
| `addCriteriaProvider(criteriaProvider)` | Adiciona provedor de critério |
| `removeCriteriaProvider(criteriaProvider)` | Remove provedor de critério |
| `saveCriteria(id, criteria, criteriaParsed)` | Salva critério |

### CriteriaProvider (interface)

**ID:** `util.common.interface:CriteriaProvider`

Interface para provedores de critério de filtragem.

### Criteria (object)

**ID:** `util.common.object:Criteria`

Objeto de critério de filtragem de dados.

### IDataSetObserver (interface)

**ID:** `util.common.interface:IDataSetObserver`

Observer para eventos do dataset.

### IDynaformConfigObserver (interface)

**ID:** `util.common.interface:IDynaformConfigObserver`

Observer para eventos de configuração do dynaform.

### IPopUpStackObserver (interface)

**ID:** `util.common.interface:IPopUpStackObserver`

Observer para a pilha de popups abertos.

### TXProperties (interface)

**ID:** `util.common.interface:TXProperties`

Propriedades de transação.

---

## snk (raiz)

O módulo `snk` é o ponto de entrada do framework. Para usar o sankhya-js numa tela, declarar como dependência do módulo AngularJS:

```js
angular.module('minhaTela', ['snk'])
    .controller('MeuController', function(MessageUtils, SanPopup) {
        // ...
    });
```

---

## Outros módulos de alto nível

| Módulo | Descrição |
|---|---|
| `snk.formitem` | Form item individual (campo do formulário) |
| `snk.gridconfig` | Configuração de colunas de grid pelo usuário |
| `snk.gridstatistics` | Estatísticas e totalizadores do grid |
| `snk.metadataprovider` | Provedor de metadados de entidade |
