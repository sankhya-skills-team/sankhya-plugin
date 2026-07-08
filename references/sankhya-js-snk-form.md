# sankhya-js — snk.form

Módulo de formulários. Renderiza campos de entidade de forma responsiva com base nos metadados do dataset.

---

## sk-form

**ID:** `snk.form.directive:sk-form`
**Tipo:** directive (cria novo scope)

Renderiza campos (`sk-form-item`) de acordo com as propriedades recebidas ou com os metadados do dataset. Suporta campos customizados via `sk-form-custom-item`.

**Uso:**
```html
<sk-form
    properties="{object}"
    [sk-columns="{string}"]
    [sk-inline="{boolean}"]
    [sk-only-custom]="{attribute}"
    [sk-form-custom-block]="{tag}">
</sk-form>
```

| Parâmetro | Tipo | Default | Descrição |
|---|---|---|---|
| `properties` | object | - | Objeto com array `fields` (alternativa ao dataset) |
| `sk-columns` | string | 1 | Número de colunas: `1`, `2`, `3`, `6` (max responsivo: 4) |
| `sk-inline` | boolean | false | `true` = 1 coluna (padrão Flex); `false` = responsivo |
| `[sk-only-custom]` | attribute | - | Renderiza apenas os `sk-form-custom-item` declarados no HTML |
| `[sk-form-custom-block]` | tag | - | Conteúdo renderizado no final do formulário |

**Uso com dataset (renderização automática):**
```html
<sk-form sk-dataset="ctrl.myDS"></sk-form>
```

**Uso com dataset + campos customizados:**
```html
<sk-form sk-dataset="ctrl.myDS">
    <!-- Override de campo específico -->
    <sk-form-custom-item sk-field-name="STATUS" sk-description="Situação">
        <sk-combobox sk-dataset="ctrl.myDS" sk-field-name="STATUS" sk-options="ctrl.opcoesStatus"></sk-combobox>
    </sk-form-custom-item>
</sk-form>
```

**Uso com apenas campos customizados (sem automático):**
```html
<sk-form sk-dataset="ctrl.myDS" sk-only-custom>
    <sk-form-custom-item sk-field-name="ATIVO" sk-description="Ativo?">
        <sk-switch sk-dataset="ctrl.myDS" sk-field-name="ATIVO"></sk-switch>
    </sk-form-custom-item>
    <sk-form-custom-item sk-field-name="VALOR" sk-description="Valor">
        <sk-number-input sk-dataset="ctrl.myDS" sk-field-name="VALOR" sk-precision="2"></sk-number-input>
    </sk-form-custom-item>
</sk-form>
```

**Uso com `properties` (sem dataset):**
```html
<sk-form properties="ctrl.formProperties" columns="2" flex></sk-form>
```

Objeto `properties`:
```js
ctrl.formProperties = {
    fields: [
        {
            label: 'Nome',
            fieldName: 'NOME',
            value: ctrl.dados.nome,
            type: 'S',              // tipo do campo
            required: true,
            groupName: 'Dados Gerais',
            fieldProp: { 'sk-align': 'left' }
        }
    ]
};
```

---

## sk-form-custom-item

**ID:** `snk.form.directive:sk-form-custom-item`

Personalização de campo específico dentro do `sk-form`. Pode substituir o componente padrão ou apenas customizar a label.

**Parâmetros:**

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `sk-field-name` | string | Nome do campo a ser customizado |
| `sk-description` | string | Label customizada para o campo |
| `sk-visible` | boolean/expression | Controla visibilidade do item |

**Exemplo com componente customizado:**
```html
<sk-form-custom-item sk-field-name="TEMPERATURA" sk-description="{{ ctrl.getDescricao() }}" sk-visible="!ctrl.escondido">
    <sk-hbox align="start stretch" flex>
        <sk-text-input sk-custom-item-input sk-dataset="ctrl.myDS" sk-field-name="TEMPERATURA"></sk-text-input>
        <button default small ng-click="ctrl.incrementar()">+</button>
    </sk-hbox>
</sk-form-custom-item>
```

**Observação:** ao usar componente customizado dentro de `sk-form-custom-item`, adicionar o atributo `sk-custom-item-input` no componente de input para que o form o reconheça corretamente.

---

## sk-form-block

**ID:** `snk.components.form.directive:sk-form-block`

Bloco dentro de um formulário com agrupamento visual.

---

## sk-datagrid-custom-column

**ID:** `snk.form.directive:sk-datagrid-custom-column`

Personalização de colunas do `sk-datagrid`. Deve ser usado como filho do `sk-datagrid` ou dentro de um `sk-dynaform`.

**Uso:**
```html
<sk-datagrid sk-dataset="ctrl.dataset">
    <sk-datagrid-custom-column field-name="CAMPO">
        <!-- template customizado da célula -->
    </sk-datagrid-custom-column>
</sk-datagrid>
```

---

## IFormInterceptor

**ID:** `snk.components.form.interfaces:IFormInterceptor`

Interface para interceptar o comportamento do formulário.

---

## sk-form com sk-dynaform (blocos customizados)

Ao usar `sk-save-handler` no `sk-dynaform`, é possível definir blocos customizados no formulário:

```js
ctrl.onDynaformLoaded = function(dynaform) {
    dynaform.setSaveHandler(function() {
        return [{
            blockId: 'dadosComplementares',
            description: 'Dados Complementares',
            controller: 'DadosCompController',
            controllerAs: 'ctrl',
            templateUrl: 'html5/Entidade/blocos/dados-comp.tpl.html',
            properties: { entidade: ctrl.entidade }
        }];
    });
};
```

---

## Módulos relacionados

| Módulo | Descrição |
|---|---|
| `snk.formitem` | Item individual de formulário |
| `snk.gridconfig` | Configuração de grade |
| `snk.gridstatistics` | Estatísticas de grade |
