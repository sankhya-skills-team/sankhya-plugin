# sankhya-js — snk.components.dataset

Módulo de controle de registros no cliente. O `sk-dataset` é o componente base de todos os outros componentes do sankhya-js; fornece carregamento, edição e persistência de registros de uma entidade.

---

## sk-dataset

**ID:** `snk.components.dataset.directive:sk-dataset`
**Tipo:** directive (cria novo scope)

Controla registros de uma entidade no lado do cliente. Componente central do framework — todos os inputs e grids se baseiam nele.

**Uso:**
```html
<sk-dataset
    entity-name="{string}"
    parent-dataset="{Dataset}"
    metadata-provider="{function}"
    metadata-interceptor="{function}"
    before-refresh-action="{function}"
    before-post-action="{function}"
    order-by="{string}"
    sk-save-handler="{function}"
    sk-remove-handler="{function}"
    sk-refresh-handler="{function}"
    sk-dataset-created="{function}"
    crud-listener="{string}"
    sk-restrict-key-handlers="{string}"
    sk-presentation-field="{string}"
    sk-load-description-fields-stand-alone="{boolean}"
    [sk-ignore-listener-methods]="{string}">
</sk-dataset>
```

**Parâmetros principais:**

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `entity-name` | string | Nome da entidade base (quando não standalone) |
| `parent-dataset` | Dataset | Dataset master para relação master-detail |
| `metadata-provider` | function | Carrega metadados de forma personalizada |
| `metadata-interceptor` | function | Intercepta e modifica os metadados carregados |
| `before-refresh-action` | function | Executada antes do refresh |
| `before-post-action` | function | Executada antes do save |
| `order-by` | string | Campo de ordenação padrão |
| `sk-save-handler` | function | Handler customizado de salvamento |
| `sk-remove-handler` | function | Handler customizado de exclusão |
| `sk-refresh-handler` | function | Handler de refresh (modo standalone) |
| `sk-dataset-created` | function | Callback quando o dataset é criado — recebe `dataset` como parâmetro |
| `crud-listener` | string | Nome do listener de CRUD |
| `sk-presentation-field` | string | Campo usado como descrição nos lookups |
| `sk-load-description-fields-stand-alone` | boolean | Carrega campos de descrição no modo standalone |
| `sk-standalone` | attribute | Marca o dataset como standalone (sem entidade real) |

**Exemplo com standalone:**
```html
<sk-dataset
    sk-refresh-handler="ctrl.refreshHandler(request)"
    sk-dataset-created="ctrl.onDatasetCreated(dataset)"
    sk-standalone>
    <sk-dsfield-md name="CODPROD" description="Código" is-pk="true"></sk-dsfield-md>
    <sk-dsfield-md name="DESCRPROD" description="Descrição"></sk-dsfield-md>
    <sk-dsfield-md name="ATIVO" description="Ativo" presentation-type="S"></sk-dsfield-md>
</sk-dataset>
```

---

## sk-dsfield-md

**ID:** `snk.components.dataset.directive:sk-dsfield-md`
**Tipo:** directive

Configura campos no `sk-dataset` para uso no modo standalone. Deve ser filho direto de `sk-dataset`.

**Uso:**
```html
<sk-dsfield-md
    name="{string}"
    description="{string}"
    user-type="{string}"
    presentation-type="{string}"
    is-pk="{boolean}"
    read-only="{boolean}"
    required
    visible="{boolean}">
</sk-dsfield-md>
```

**Parâmetros:**

| Parâmetro | Tipo | Valores / Descrição |
|---|---|---|
| `name` | string | Nome do campo |
| `description` | string | Label do campo |
| `user-type` | string | Tipo: `S` (string), `I` (inteiro), `F` (float), `T` (texto longo), `D` (data), `H` (hora) |
| `presentation-type` | string | `S` = switch, `P` = padrão (default: `P`) |
| `is-pk` | boolean | Define se é chave primária |
| `read-only` | boolean | Somente leitura |
| `required` | attribute | Campo obrigatório |
| `visible` | boolean | Visibilidade inicial |

---

## sk-field

**ID:** `snk.components.dataset.directive:sk-field`
**Tipo:** directive

Permite solicitar campos adicionais ao dataset a partir do dicionário de dados.

---

## sk-dsfield-md (com options — para campos tipo combo)

Para campos com opções fixas, usar `sk-options` e `sk-option` como filhos:

```html
<sk-dsfield-md name="STATUS" description="Status">
    <sk-options>
        <sk-option data="A" label="Ativo"></sk-option>
        <sk-option data="I" label="Inativo"></sk-option>
    </sk-options>
</sk-dsfield-md>
```

---

## DatasetOnlineFilter

**ID:** `snk.components.dataset.service:DatasetOnlineFilter`
**Tipo:** service

Filtra registros em memória no dataset sem nova requisição ao servidor.

**Instanciação:**
```js
var dsFilter = new DatasetOnlineFilter(dataset);
```

**Métodos:**

| Método | Descrição |
|---|---|
| `andFilter(queryObj)` | Filtro AND — todos os campos devem coincidir |
| `orFilter(queryObj)` | Filtro OR — qualquer campo pode coincidir |
| `inFilter(fieldName, filterArray, notIn?)` | Filtro IN / NOT IN por array de valores |
| `setFilterFn(filterFunction)` | Define função de filtro customizada |
| `clearFilter(preventFilterRecords?)` | Remove filtros. Parâmetro previne reload |
| `refresh()` | Reaaplica o filtro atual |
| `buildRegexForTerm(textTerm)` | Retorna RegExp para o termo informado |

**Exemplos:**
```js
var dsFilter = new DatasetOnlineFilter(dataset);

// AND
dsFilter.andFilter({ CAMPO1: 'valor1', CAMPO2: 'valor2' });

// IN
dsFilter.inFilter('CODPROD', [1, 2, 3, 4, 5]);

// OR
dsFilter.orFilter({ NOME: 'João', APELIDO: 'João' });
```

---

## FieldBinder

**ID:** `snk.components.dataset.interface:FieldBinder`
**Tipo:** interface

Interface para criar componentes customizados que se ligam a um campo do dataset.

---

## interface RecordValidator

**ID:** `components.dataset.validators.interface:RecordValidator`

Interface para validação de registros no dataset antes do save.
