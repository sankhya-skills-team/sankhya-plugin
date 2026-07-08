# Design System — Utilitários TypeScript

Classes, enums e interfaces TypeScript disponíveis no pacote de utilitários do Design System.

---

## Instalação

```bash
npm install @sankhyalabs/core
```

```javascript
import { StringUtils } from '@sankhyalabs/core';
```

---

## DataUnit (componente)

Abstração que simplifica manipulação de dados em UIs, gerenciando operações CRUD e eventos associados.

**Loaders (funções obrigatórias para configuração):**

| Loader | Parâmetros | Descrição |
|--------|-----------|-----------|
| `metadataLoader` | `(dataUnit) => Promise<UnitMetadata>` | Define metadados dos campos |
| `dataLoader` | `(dataUnit, LoadDataRequest) => Promise<LoadDataResponse>` | Carrega registros com filtros/ordenação |
| `saveLoader` | `(dataUnit, changes[]) => Promise<SavedRecord[]>` | Persiste alterações |
| `removeLoader` | `(dataUnit, recordIds[]) => Promise<string[]>` | Remove registros |
| `recordLoader` | `(dataUnit, recordIds[]) => Promise<Record[]>` | Carrega registros específicos |

> Todos os registros devem incluir a propriedade `__record__id__` para indexação.

**Métodos principais:**

| Método | Descrição |
|--------|-----------|
| `hideField(name)` / `showField(name)` | Controla visibilidade de campos |
| `setFieldValue(fieldName, newValue, records?, options?)` | Insere/atualiza valor no registro atual |
| `getFieldValue(fieldName)` | Recupera valor do campo |
| `loadData(quickFilter?, ctx?)` | Carrega registros |
| `saveData(ctx?)` | Persiste alterações |
| `addRecord(ctx?)` | Adiciona novo registro |
| `removeRecords(recordIds, cached, buffered?)` | Remove registros |

> `setFieldValue` sem registros selecionados cria automaticamente um novo registro (use `suppressCreateNewRecord: true` para evitar).

---

## DataUnitInMemoryLoader

Utilitário que entrega instância de `DataUnit` pronta para uso, com loaders configurados e dados em memória.

```typescript
new DataUnitInMemoryLoader(metadata?, records?, config?)
```

**Configuração:**
```typescript
interface DataUnitInMemoryLoaderConfig {
  autoLoad?: boolean;           // Carrega automaticamente (padrão: true)
  pageSize?: number;            // Registros por página (padrão: 150; 0 = todos)
  recordDateFormat?: RECORD_DATE_FORMAT;  // DD_MM_YYYY | ISO
}
```

**Constantes estáticas:**
- `DEFAULT_PAGE_SIZE = 150`
- `IN_MEMORY_DATA_UNIT_NAME = "InMemoryDataUnit"`

**Acessores:** `dataUnit` (get), `metadata` (get/set), `records` (get/set)

**Método público:** `removeLoader(_dataUnit, recordIds) => Promise<string[]>`

**Método estático:** `getConvertedValue(descriptor, strValue, dateFormat?)` — converte string para tipo adequado baseado no FieldDescriptor.

---

## DataUnitLoaderUtils

Utilitário para abstrair lógica de paginação, ordenação e filtragem em data loaders.

```typescript
import { DataUnitLoaderUtils } from '@sankhyalabs/core';
```

**Todos os métodos são estáticos:**

| Método | Assinatura resumida | Descrição |
|--------|-------------------|-----------|
| `buildLoadDataResponse` | `(records, dataUnit, request) => Promise<LoadDataResponse>` | Abstrai toda a lógica de paginação/ordenação/filtragem |
| `applyFilter` | `(records, dataUnit, filters) => Record[]` | Aplica filtros de coluna |
| `applySorting` | `(records, dataUnit, sorting) => Record[]` | Aplica ordenação |
| `getPagesByRecords` | `(records, offset, limit) => Record[]` | Retorna subset paginado |
| `buildPaginationInfo` | `({recordsLength, offset, recordsPerPage}) => PaginationInfo` | Constrói metadados de paginação |

---

## ApplicationContext

Classe utilitária para manipular contexto global da aplicação.

> Usar somente com alinhamento arquitetural — depende de variáveis globais.

**Todos os métodos são estáticos:**

| Método | Parâmetros | Retorno | Descrição |
|--------|-----------|---------|-----------|
| `getContextValue(key)` | `string` | `any` | Recupera valor do contexto |
| `setContextValue(key, value)` | `string, any` | `any` | Armazena informação no contexto |

Funciona como hub de comunicação entre componentes desacoplados via `snkcore___ctx` global.

---

## DataUnit (classe API)

Classe TypeScript de `@sankhyalabs/core` que gerencia ciclo de vida dos dados.

**Propriedades principais:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `name` | string | Identificador (formato URI) |
| `dataUnitId` | string | ID único da instância |
| `records` | Record[] | Registros carregados |
| `metadata` | UnitMetadata | Descritores de campos |
| `pageSize` | number | Registros por página |
| `isMultipleEdition` | boolean | Modo de edição múltipla |

**Loaders opcionais:** `dataLoader`, `saveLoader`, `removeLoader`, `recordLoader`, `metadataLoader`, `allRecordsLoader`

**Métodos de seleção:** `setSelection()`, `selectFirst()`, `selectLast()`, `selectAllRecords()`, `unSelectAllRecords()`, `getSelectionInfo()`

**Métodos de paginação:** `gotoPage(page)`, `nextPage()`, `previousPage()`, `getPaginationInfo()`

**Métodos de estado:** `isDirty()`, `canUndo()`, `canRedo()`, `undo()`, `redo()`

**Observadores:** `subscribe(observer)`, `addInterceptor(interceptor)`, `unsubscribe(observer)`, `removeInterceptor(interceptor)`

**Filtragem:** `addFilterProvider(provider)`, `getAppliedFilters()`, `getSort()`

**Ciclo de vida:** `release()`, `clearDataUnit()`, `releaseCallbacks()`

**DataUnits filhos:** `getChildDataunit(name)`, `removeChildDataunit(name)`, `getChildInfo(name)`

---

## DataUnitAction

Classe que implementa `StateAction` para gerenciar ações no sistema de estado do DataUnit.

```typescript
new DataUnitAction(type: Action, payload?: any)
```

**Acessores:** `type` (retorna `Action`), `payload` (retorna `any`)

---

## ServiceUtils

Facilita gerenciamento de cache em chamadas de serviço.

```typescript
static useCacheWithService<T>(
  identifier: string,
  fetchFunction: () => Promise<T>,
  storageType?: 'sessionStorage' | 'localStorage'
): Promise<T>
```

- Se não especificado, usa `IN_MEMORY_CACHE`
- A `fetchFunction` é chamada apenas quando o cache está ausente ou expirado

```typescript
const actions = await ServiceUtils.useCacheWithService(
  `${entityName} - ${resourceID}`,
  async () => await fetchActionsFromAPI()
);
```

---

## HttpProvider

Abstração do `XMLHttpRequest` para requisições ao backend.

**Todos os métodos são estáticos:**

```typescript
static get(url: string, headers?: Header[]): Promise<Object>
static post(url: string, payload: Object, headers?: Header[]): Promise<any>
```

---

## DateUtils

Utilitário para formatação, padronização e cálculos de datas (pt-BR).

| Método | Retorno | Descrição |
|--------|---------|-----------|
| `formatDate(date, options?)` | `string` | `DD/MM/YYYY` |
| `formatDateTime(date, showSeconds?)` | `string` | `DD/MM/YYYY HH:MM[:SS]` |
| `formatTime(date, showSeconds?)` | `string` | `HH:MM[:SS]` |
| `formatRfc3339(date)` | `string` | `2023-03-09T12:42:47-03:00` |
| `strToDate(str, adjustDLS?, monthYearMode?)` | `Date \| undefined` | String para Date |
| `clearTime(date, adjustDLS?)` | `Date` | Remove horas, minutos, segundos |
| `getToday(withTime?)` | `Date` | Data atual |
| `validateDate(value, hasTime?)` | `Date \| undefined` | Valida e retorna date se válido |

---

## StringUtils

Utilitário para manipulação de strings.

**Validação:** `isEmpty(value)`, `isString(text)`

**Conversão de case:** `toCamelCase(value)`, `toPascalCase(value)`, `toSnakeCase(value)`, `toKebabCase(value)`, `getOppositeCase(original)`

**Acentuação:** `replaceAccentuatedChars(text, removeSpecialChars)`, `replaceAccentuatedCharsUpper(text)`, `replaceAccentuatedCharsLower(text)`

**Padding:** `padStart(str, len, pad)`, `padEnd(str, len, pad)`
- Exemplo: `padStart('SANKHYA', 10, '.')` → `'...SANKHYA'`

**Utilitários:** `generateUUID()`, `hashCode(value)`, `compare(a, b)`, `formatBytes(bytes)`, `getBooleanValue(value, defaultValue)`, `replaceAll(str, from, to)`, `decodeHtmlEntities(text)`, `escapeString(str)`

---

## NumberUtils

Utilitário para manipulação numérica (foco em pt-BR).

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `changeFormat(value)` | Converte entre pt-BR e en-US | `"15,55"` → `"15.55"` |
| `stringToNumber(value)` | String para number | `"100,12"` → `100.12` |
| `format(value, precision, prettyPrecision?, defaultValue?)` | Formata com precisão | `format('10,9845', 3, 3)` → `'10,985'` |
| `safeFormat(value, precision, prettyPrecision?)` | Igual a `format` mas com fallback `"0,00"` | — |
| `keepOnlyDecimalSeparator(value, format?)` | Remove separadores de milhar | `'95.12'` → `'9512'` |
| `round(value, decimals?)` | Arredonda | `round(100.15, 1)` → `100.2` |
| `compare(a, b)` | Ordenação numérica | negativo / zero / positivo |
| `getValueOrZero(value)` | Retorna 0 se NaN/undefined | — |
| `getValueOrDefault(value, defaultValue)` | Retorna default se inválido | `getValueOrDefault("abc", 0)` → `0` |

---

## ArrayUtils

Utilitário para manipulação de arrays.

| Método | Descrição |
|--------|-----------|
| `applyStringFilter(argument, array, alphabeticalSorting?, fieldName?)` | Filtra por texto |
| `sortAlphabetically(array, fieldName?)` | Ordena alfabeticamente (padrão: campo `label`) |
| `removeReference(array, obj)` | Remove objeto do array |
| `removeAtIndex(array, index)` | Remove por índice |
| `indexOf(arr, obj)` | Posição do objeto (ou -1) |
| `isIn(arr, obj)` | Verifica se objeto existe |
| `find(arr, checkerFn)` | Encontra elemento por função |

---

## ObjectUtils

Utilitário para manipulação de objetos.

| Método | Descrição |
|--------|-----------|
| `copy<T>(data)` | Cria cópia do objeto |
| `equals(obj1, obj2)` | Compara igualdade |
| `hasEquivalentProps(obj1, obj2, propToCompare?)` | Compara via propriedade específica |
| `getProp(obj, keyPath)` | Acessa propriedade por path |
| `isEmpty(obj)` / `isNotEmpty(obj)` | Verifica se objeto está vazio |
| `isEmptySafetyCheck(obj)` | Versão segura (retorna true para null/undefined) |
| `objectToString(data)` | Objeto → JSON string |
| `stringToObject(data)` | JSON string → Objeto |
| `removeEmptyValues(obj)` | Remove atributos null/undefined |
| `sortByProperty(data, property)` | Ordena por propriedade |

---

## Enum: Action

Ações de estado para operações do DataUnit. Todas as strings.

| Categoria | Valores |
|-----------|---------|
| Metadados | `LOADING_METADATA`, `METADATA_LOADED` |
| Carregamento | `LOADING_DATA`, `DATA_LOADED`, `PAGINATION_UPDATED` |
| Salvamento | `SAVING_DATA`, `DATA_SAVED`, `SAVING_CANCELED`, `SAVING_ERROR` |
| Mudanças | `CHANGING_DATA`, `DATA_CHANGED`, `DATA_RESOLVED`, `CHANGE_UNDONE`, `CHANGE_REDONE` |
| Registros | `RECORDS_REMOVED`, `RECORDS_ADDED`, `RECORDS_COPIED`, `SELECTION_CHANGED` |
| Navegação | `NEXT_SELECTED`, `PREVIOUS_SELECTED` |
| Avançado | `STATE_CHANGED`, `LOADING_RECORD`, `RECORD_LOADED`, `CHILD_CHANGED`, `EDITION_CANCELED`, `MULTIPLE_EDITION_CHANGED` |

---

## Enum: DataType

Tipos de dados suportados para campos do DataUnit.

| Membro | Valor |
|--------|-------|
| `TEXT` | `"TEXT"` |
| `NUMBER` | `"NUMBER"` |
| `DATE` | `"DATE"` |
| `BOOLEAN` | `"BOOLEAN"` |
| `OBJECT` | `"OBJECT"` |

---

## Enum: SelectionMode

Modos de seleção de registros no DataUnit.

| Valor | Descrição |
|-------|-----------|
| `ALL_RECORDS` | Todos os registros disponíveis |
| `SOME_RECORDS` | Registros específicos/parciais |

---

## Interface: FieldDescriptor

Define a estrutura de metadados para campos do DataUnit.

**Obrigatórios:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `name` | string | Identificador do campo |
| `label` | string | Nome legível do campo |
| `dataType` | DataType | Tipo de dado |

**Opcionais:**

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `userInterface` | UserInterface | Componente UI para renderização |
| `defaultValue` | any | Valor inicial |
| `visible` | boolean | Controla visibilidade |
| `readOnly` | boolean | Impede modificação |
| `required` | boolean | Campo obrigatório |
| `standAlone` | boolean | Comportamento independente |
| `dependencies` | FieldDependency[] | Dependências entre campos |
| `group` | string | Agrupamento lógico |
| `order` | number | Prioridade de exibição |
| `properties` | any | Configurações adicionais |

---

## Interface: Filter

Define critérios de filtragem.

| Propriedade | Tipo | Obrigatório | Descrição |
|-------------|------|-------------|-----------|
| `name` | string | Sim | Identificador do filtro |
| `expression` | string | Sim | Lógica/condição do filtro |
| `params` | FilterParam[] | Não | Parâmetros da expressão |

---

## Interface: LoadDataRequest

Atributos enviados em uma requisição de carregamento de dados.

| Propriedade | Tipo | Obrigatório | Descrição |
|-------------|------|-------------|-----------|
| `source` | string | Não | Origem da ação de refresh |
| `offset` | number | Não | Índice inicial dos registros |
| `limit` | number | Não | Quantidade de registros a retornar |
| `quickFilter` | QuickFilter | Não | Filtro rápido |
| `filters` | Filter[] | Não | Array de filtros |
| `sort` | Sort[] | Não | Especificações de ordenação |
| `parentRecordId` | string | Não | Registro pai (para DataUnits filhos) |
| `keepSelection` | boolean | Não | Mantém seleção durante paginação |

---

## Interface: LoadDataResponse

Estrutura de resposta para requisições de carregamento.

| Propriedade | Tipo | Obrigatório | Descrição |
|-------------|------|-------------|-----------|
| `records` | Record[] | Sim | Array de registros retornados |
| `paginationInfo` | PaginationInfo | Não | Metadados de paginação |

---

## Interface: Record

Interface base para registros de dados no sistema.

```typescript
interface Record {
  [key: string]: any;           // propriedades dinâmicas
  __record__id__: string;       // identificador único (obrigatório)
  __record__label__?: string;   // label de exibição
  __parent__record__id__?: string;  // vincula ao registro pai
  __owner__dataunit__name__?: string; // nome do DataUnit proprietário
}
```

> Estendida por `SavedRecord`. O campo `__record__id__` é obrigatório para indexação no DataUnit.
