# Design System — API Java (BFF e Sanmodule)

Interfaces Java do lado servidor para integração com o Design System.

---

## Visão Geral — sankhya-bff

A biblioteca `sankhya-bff` fornece interfaces Java para interceptar e personalizar comportamentos de componentes do Design System no servidor.

**Interfaces disponíveis:**
- `IDataUnitInterceptor` — manipulação de metadados
- `IDataUnitCrudListener` — interceptação de CRUD
- `ICustomFilterBarResolver` — resolução de FilterBar
- `IDataExporterInterceptor` — personalização de exportação
- `ITotalsResolver` — resolvers de totalização customizados

---

## IDataUnitInterceptor

Interface que define interceptadores para ações relacionadas a um `DataUnit`, permitindo manipulação de metadados de entidades.

**Casos de uso:**
- Mapear campos de entidades filhas
- Remover dependências de campos FK
- Modificar propriedades de campos (label, valor padrão, obrigatoriedade, visibilidade)

**Anotação:** `@DataUnitInterceptor(entity = "EntityName", resourceId = "resource.id")`

### Métodos

#### `interceptFieldMetadata(DataUnitField duField)`
Intercepta e manipula metadados de um campo específico durante a construção do DataUnit.

```java
@DataUnitInterceptor(entity = "Financeiro",
  resourceId = "br.com.sankhya.fin.cad.movimentacaoFinanceira")
public class CustomFieldMetadataInterceptor implements IDataUnitInterceptor {
    @Override
    public void interceptFieldMetadata(DataUnitField duField) {
        if ("VALOR_TOTAL".equalsIgnoreCase(duField.getName())) {
            duField.setRequired(true);
            duField.setLabel("Valor Total (R$)");
        }
    }
}
```

#### `interceptFieldsMetadata(List<DataUnitField> duFields)`
Intercepta e manipula metadados de uma lista de campos.

#### `isIgnoredField(DataUnitField duField) → boolean`
Determina se um campo deve ser excluído dos fluxos de execução.

#### `isInvisibleChild(String masterName, DataUnitChild child) → boolean`
Determina se um elemento filho deve ser invisível durante manipulação do DataUnit.

#### `getFieldMap() → List<DataUnitFieldMap>`
Retorna mapeamento customizado de campos para o DataUnit.

---

## IDataUnitCrudListener

Interface que define interceptadores para operações CRUD em um `DataUnit`.

**Casos de uso:**
- Validações e regras de negócio antes/após persistência
- Preenchimento automático de campos
- Auditoria de alterações
- Filtros automáticos de busca

**Anotação:** `@DataUnitCrudListener(entity = "EntityName", resourceId = "resource.id")`

### Métodos

| Método | Assinatura | Descrição |
|--------|-----------|-----------|
| `beforeInsert` | `void beforeInsert(DataUnitCrudListenerContext ctx) throws Exception` | Antes de inserir |
| `afterInsert` | `void afterInsert(DataUnitCrudListenerContext ctx) throws Exception` | Após inserir |
| `beforeUpdate` | `void beforeUpdate(DataUnitCrudListenerContext ctx) throws Exception` | Antes de atualizar |
| `afterUpdate` | `void afterUpdate(DataUnitCrudListenerContext ctx) throws Exception` | Após atualizar |
| `beforeDelete` | `void beforeDelete(DataUnitCrudListenerContext ctx) throws Exception` | Antes de deletar |
| `afterDelete` | `void afterDelete(DataUnitCrudListenerContext ctx) throws Exception` | Após deletar |
| `beforeFind` | `void beforeFind(DataUnitCrudListenerContext ctx) throws Exception` | Antes de buscar |
| `afterLoadVOs` | `void afterLoadVOs(Collection result) throws Exception` | Após carregar VOs |
| `loadCustomData` | `Collection loadCustomData(FinderWrapper finder) throws Exception` | Carga customizada |

**Exemplo:**
```java
@DataUnitCrudListener(entity = "MovimentoBancario",
  resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class MovimentoCrudListener implements IDataUnitCrudListener {

    @Override
    public void beforeInsert(DataUnitCrudListenerContext ctx) throws Exception {
        // Validação antes de inserir
    }

    @Override
    public void afterUpdate(DataUnitCrudListenerContext ctx) throws Exception {
        // Registro de auditoria após atualização
    }

    @Override
    public void beforeFind(DataUnitCrudListenerContext ctx) throws Exception {
        // Adiciona filtro automático de WHERE
    }
}
```

---

## ICustomFilterBarResolver

Interface para gerenciar e ajustar configurações do `FilterBar`.

**Casos de uso:**
- Adicionar configurações customizadas para resolução de filtros
- Recuperar configurações de filtros por usuário

**Anotação:** `@CustomFilterBarResolver(resourceId = "resource.id")`

### Método

#### `handle(FilterBarConfig filterBarConfig) throws Exception`
Processa a configuração da FilterBar, permitindo modificações.

```java
@CustomFilterBarResolver(resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class CustomFilterBarResolver implements ICustomFilterBarResolver {
    @Override
    public void handle(FilterBarConfig filterBarConfig) throws Exception {
        if (filterBarConfig == null) {
            System.out.println("Nenhuma configuração informada");
            return;
        }
        System.out.println("Lidando com configurações: " + filterBarConfig);
    }
}
```

---

## IDataExporterInterceptor

Interface para interceptar e customizar o comportamento do exportador de dados.

**Casos de uso:**
- Adicionar colunas obrigatórias às exportações
- Implementar expressões de soma agrupadas

**Anotação:** `@DataExporterInterceptor(entity = "EntityName", resourceId = "resource.id")`

### Métodos

#### `buildSumExpression(String jrFieldName, String expression, Map<String, String> extraParams) → String`
Constrói expressão de agregação personalizada (ex: `SUM`) para exportação.

```java
@DataExporterInterceptor(entity = "MovimentoBancario",
  resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class ConditionalSumExporterInterceptor implements IDataExporterInterceptor {
    @Override
    public String buildSumExpression(String jrFieldName, String expression,
                                     Map<String, String> extraParams) {
        if ("DESCONTO".equalsIgnoreCase(jrFieldName)) {
            return String.format("SUM(%s) * 0.9", jrFieldName);
        }
        return String.format("SUM(%s)", jrFieldName);
    }
}
```

#### `getRequiredColumns() → List<ExporterColumMetadata>`
Retorna colunas obrigatórias na exportação de dados.

```java
@Override
public List<ExporterColumMetadata> getRequiredColumns() {
    return List.of(
        new ExporterColumMetadata("TOTAL", "Valor total da compra"),
        new ExporterColumMetadata("QUANTIDADE", "Quantidade total de itens")
    );
}
```

---

## ITotalsResolver

Interface para implementar resolvers customizados do componente Totalizador.

**Anotação:** `@CustomFilterBarResolver(resourceId = "resource.id")`

### Métodos

#### `canResolve(ResourceURI uri) → boolean`
Determina se a implementação pode processar uma URI específica.

```java
@Override
public boolean canResolve(ResourceURI uri) {
    return "pedidos/total".equals(uri.getPath());
}
```

#### `resolve(List<DataUnitFilter> filter, TotalsResolverSqlContext sqlContext) → List<TotalsResult>`
Calcula valores do totalizador com base nos filtros e contexto SQL.

```java
@Override
public List<TotalsResult> resolve(List<DataUnitFilter> filter,
                                   TotalsResolverSqlContext sqlContext) throws Exception {
    int totalEstoque = 0;
    for (DataUnitFilter filtro : filter) {
        if ("PRODUTO_ID".equals(filtro.getFieldName())) {
            totalEstoque += 100;
        }
    }
    TotalsResult result = new TotalsResult("TOTAL_ESTOQUE", totalEstoque);
    return List.of(result);
}
```

---

## Visão Geral — sanmodule

A biblioteca `sanmodule` fornece interfaces Java para gerenciamento do ciclo de vida de módulos Sankhya.

---

## BootModuleListener

Interface que define listeners para momentos específicos do ciclo de vida de um módulo Sankhya.

**Caso de uso principal:** registro de telas no sistema durante a inicialização do módulo (padrão utilizado em `mgefin-bff` e `mgecom-bff`).

### Métodos

| Método | Parâmetro | Descrição |
|--------|-----------|-----------|
| `beforeStartModule` | `ServletContextEvent` | Antes da inicialização do módulo |
| `afterStartModule` | `ServletContextEvent` | Após inicialização completa |
| `beforeStopModule` | `ServletContextEvent` | Antes da parada do módulo |
| `afterStopModule` | `ServletContextEvent` | Após parada completa |

```java
public class BootModuleListenerImpl implements BootModuleListener {

    @Override
    public void beforeStartModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Inicializando módulo...");
        registryScreens();
    }

    @Override
    public void afterStartModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Módulo inicializado com sucesso.");
    }

    @Override
    public void beforeStopModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Interrompendo execução...");
        removeScreens();
    }

    @Override
    public void afterStopModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Módulo finalizado com sucesso.");
    }

    private void registryScreens() {
        // Lógica de registro de telas
    }

    private void removeScreens() {
        // Lógica de remoção de telas
    }
}
```
