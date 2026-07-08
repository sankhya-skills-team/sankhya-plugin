# sankhya-js — snk.components.input

Módulo de componentes de entrada de dados. Todos os inputs podem operar em dois modos:
- **Com Dataset:** informar `sk-dataset` + `sk-field-name` (ou `sk-field-index`)
- **Standalone:** informar `sk-value` para bind direto

Parâmetros comuns a todos os inputs:

| Parâmetro | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-dataset` | SkDataset | undefined | Dataset vinculado |
| `sk-field-name` | string | undefined | Nome do campo no dataset |
| `sk-field-index` | string | undefined | Índice do campo no dataset |
| `sk-value` | varies | undefined | Bind standalone |
| `sk-change` | function | undefined | Callback ao alterar valor |
| `sk-focus-out` | function | undefined | Callback ao perder foco |
| `sk-enabled` | boolean | true | Habilita/desabilita edição |
| `sk-required` | boolean | false/true | Campo obrigatório |

---

## sk-text-input

**ID:** `snk.components.input.directive:sk-text-input`

Entrada de texto, análogo ao `<input type="text">`.

```html
<sk-text-input
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-required="{boolean}"
    sk-align="{string}"
    sk-password="{string}"
    [sk-restrict]="{string}">
</sk-text-input>
```

| Parâmetro extra | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-align` | string | undefined | Alinhamento do texto |
| `sk-password` | string | false | Exibe como campo de senha |
| `sk-restrict` | string | - | Regex de aceite de caracteres. Ex: `[^0-9]` aceita só números |

**Exemplo standalone:**
```html
<sk-text-input sk-value="ctrl.nome" sk-change="ctrl.onChange()" sk-enabled="ctrl.habilitado"></sk-text-input>
```

---

## sk-number-input

**ID:** `snk.components.input.directive:sk-number-input`

Entrada numérica com suporte a decimais.

```html
<sk-number-input
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-required="{boolean}"
    sk-align="{string}"
    sk-precision="{string}"
    sk-pretty-precision="{string}">
</sk-number-input>
```

| Parâmetro extra | Tipo | Descrição |
|---|---|---|
| `sk-precision` | string | Casas decimais |
| `sk-pretty-precision` | string | Casas decimais significantes |

---

## sk-date-input

**ID:** `snk.components.input.directive:sk-date-input`

Seletor de data com calendário.

```html
<sk-date-input
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-required="{boolean}"
    sk-month-mode="{boolean}"
    sk-align="{string}"
    sk-button-mode="{string}">
</sk-date-input>
```

| Parâmetro extra | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-month-mode` | boolean | false | Seleciona apenas mês/ano |
| `sk-button-mode` | string | undefined | Modo botão (sem input de texto) |

---

## sk-date-time-input

**ID:** `snk.components.input.directive:sk-date-time-input`

Seletor de data e hora.

```html
<sk-date-time-input
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-required="{boolean}"
    sk-align="{string}"
    sk-show-date="{boolean}"
    sk-show-seconds="{boolean}">
</sk-date-time-input>
```

| Parâmetro extra | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-show-date` | boolean | true | Exibe componente de data |
| `sk-show-seconds` | boolean | false | Exibe segundos |

---

## sk-switch

**ID:** `snk.components.input.directive:sk-switch`

Toggle booleano. Valores padrão: `S` / `N`.

```html
<sk-switch
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-true-value="{string}"
    sk-false-value="{string}">
</sk-switch>
```

| Parâmetro extra | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-true-value` | string | `S` | Valor quando ligado |
| `sk-false-value` | string | `N` | Valor quando desligado |

**Exemplo:**
```html
<sk-switch sk-value="ctrl.ativo" sk-true-value="S" sk-false-value="N"></sk-switch>
```

---

## sk-combobox

**ID:** `snk.components.input.directive:sk-combobox`

Select/dropdown com opções fixas ou dinâmicas.

```html
<sk-combobox
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-allow-null="{boolean}"
    sk-required="{boolean}"
    sk-options="{array}"
    sk-opt-key="{string}"
    sk-opt-label="{string}"
    sk-options-from-query="{objeto}">
</sk-combobox>
```

| Parâmetro extra | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-allow-null` | boolean | true | Permite valor nulo |
| `sk-options` | array | undefined | Array de opções `[{data, value}]` |
| `sk-opt-key` | string | `data` | Propriedade da chave nas opções |
| `sk-opt-label` | string | `value` | Propriedade do label nas opções |
| `sk-options-from-query` | object | undefined | Carrega opções via query SQL: `{descriptionField, keyField, query, callback}` |

**Exemplo com opções fixas:**
```html
<sk-combobox sk-value="ctrl.tipo"
    sk-options="ctrl.tipoOptions"
    sk-opt-key="codigo"
    sk-opt-label="descricao">
</sk-combobox>
```

---

## sk-pesquisa-input

**ID:** `snk.components.input.directive:sk-pesquisa-input`

Input de pesquisa (lookup) — abre popup de busca de entidade.

```html
<sk-pesquisa-input
    sk-dataset="{SkDataset}"
    [sk-entity-name]="{string}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-required="{boolean}"
    sk-entity-change="{function}"
    sk-enviroment-criteria="{function}"
    sk-show-finder-error="{function}">
</sk-pesquisa-input>
```

| Parâmetro extra | Tipo | Descrição |
|---|---|---|
| `sk-entity-name` | string | Entidade a ser pesquisada |
| `sk-entity-change` | function | Callback ao selecionar registro na pesquisa |
| `sk-enviroment-criteria` | function | Função para adicionar critério à pesquisa |
| `sk-show-finder-error` | function | Exibe ou não erros quando não encontra (default: true) |

---

## sk-text-area

**ID:** `snk.components.input.directive:sk-text-area`

Área de texto multi-linha, análoga ao `<textarea>`.

```html
<sk-text-area
    sk-dataset="{SkDataset}"
    sk-field-name="{string}"
    sk-value="{string}"
    sk-change="{function}"
    sk-enabled="{boolean}"
    sk-required="{boolean}"
    sk-height="{int}"
    sk-drop-enabled="{boolean}"
    sk-drag-enter="{function}"
    sk-drag-over="{function}"
    sk-drop="{function}">
</sk-text-area>
```

| Parâmetro extra | Tipo | Default | Descrição |
|---|---|---|---|
| `sk-height` | int | 230 | Altura em pixels |
| `sk-drop-enabled` | boolean | - | Habilita drop de itens |

---

## sk-radio-input

**ID:** `snk.components.input.directive:sk-radio-input`

Radio button. Usar múltiplos com o mesmo `sk-value` e diferentes `sk-option`.

```html
<sk-radio-input
    sk-value="{string}"
    sk-option="'M'"
    sk-enabled="{boolean}"
    sk-name="grupo">
    Masculino
</sk-radio-input>
```

---

## Outros inputs disponíveis

| Diretiva | Descrição |
|---|---|
| `sk-time-input` | Entrada de hora |
| `sk-date-period-input` | Período de datas (início/fim) |
| `sk-masked-input` | Input com máscara |
| `sk-phone-input` | Entrada de telefone |
| `sk-cep-input` | Entrada de CEP |
| `sk-cgc-cpf-input` | Entrada de CNPJ/CPF |
| `sk-file-input` | Upload de arquivo |
| `sk-rich-text` | Editor rich text (TinyMCE) |
| `sk-search-input` | Campo de busca genérico |
| `sk-typeahead` | Autocomplete |
| `sk-url-input` | Entrada de URL |
| `sk-multi-combo` | Combobox de múltipla seleção |
| `sk-numeric-stepper` | Incremento/decremento numérico |
| `sk-rate-input` | Entrada de avaliação (estrelas) |
| `sk-company-selector` | Seletor de empresa |
| `sk-controle-estoque-input-input` | Controle de estoque |
| `sk-filter-dataset` | Input de filtro de dataset |
