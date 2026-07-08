<system_instruction>
Sempre responda em PORTUGUESE (PT-BR).
</system_instruction>

# Sankhya Micromodule SDK — Modern Annotation-Based Approach

> **Scope:** This skill covers the **modern** SDK/Add-on Studio approach. For the legacy EJB2/XDoclet approach (BaseSPBean, service-providers.xml), use `micromodule` skill.

## When to use

- Creating or modifying components with @Service, @Controller, @Repository, @Listener, @BusinessRule, @Callback, @ActionButton, @Job
- Configuring dependency injection (@Inject, @Component)
- Declarative transactions (@Transactional) and validation (@Valid)
- Exception handling (@ControllerAdvice, @ExceptionHandler)
- Value injection from env vars / system properties / Sankhya params (@Value)
- Entity mapping (@JapeEntity, @Column, @ManyToOne, @OneToMany)

## SDK vs Legacy (quick reference)

| Aspect | Legacy (`micromodule`) | SDK (`micromodule-sdk`) |
|--------|----------------------|------------------------|
| Endpoints | `BaseSPBean` + XDoclet + `service-providers.xml` | `@Service` / `@Controller` |
| DI | Manual (`new`, singletons) | `@Inject` via constructor (Guice) |
| Data | `JapeSession`, `EntityFacade`, `NativeSql` direct | `@Repository` + `JapeRepository` |
| Listeners | `EntityListener` interface | `@Listener` + `PersistenceEventAdapter` |
| Business rules | `Regra` interface manual | `@BusinessRule` + `Regra` + `ContextoRegra` |
| Callbacks | `ICustomCallBack` manual | `@Callback` + `ICustomCallBack` declarative |
| Buttons | `AcaoRotinaJava` manual | `@ActionButton` + `@Form` |
| Jobs | `IJob` + XML config | `@Job` declarative with CRON frequency |
| Transactions | `JapeSession.open/close` manual | `@Transactional` declarative |
| Validation | if/throw manual | `@Valid` + Bean Validation annotations |
| Exceptions | try/catch manual | `@ControllerAdvice` + `@ExceptionHandler` |
| Config | Multiple XML files | `metadados.xml` + annotations |

## SDK pillars

1. **Dependency Injection (DI)** — IoC container based on Google Guice
2. **Data Layer (Repository)** — declarative data access via annotated interfaces
3. **Declarative Transactions** — `@Transactional` with fine propagation control
4. **Bean Validation** — automatic validation with JSR 303/380

## Key annotations (quick reference)

| Annotation | Purpose | Detail |
|------------|---------|--------|
| `@Service` | HTTP endpoint (REST) | `serviceName` MUST end with `SP` |
| `@Controller` | Alias for `@Service`, default `Supports` TX | Use for orchestration layer |
| `@Component` | Managed bean | Business logic, validators, helpers |
| `@Inject` | Dependency injection | Use `com.google.inject.Inject`, **never** `javax.inject.Inject` |
| `@Repository` | Data access layer | Extends `JapeRepository<ID, Entity>` |
| `@JapeEntity` | Entity-to-table mapping | `entity` + `table` attributes required |
| `@Listener` | Persistence event hooks | `instanceNames` = entity name, not table name |
| `@BusinessRule` | Sale document lifecycle hooks | For Notas de Saida and Mov. Interna |
| `@Callback` | Document event hooks | All document types including purchases |
| `@ActionButton` | Action button with optional form | `description` + `instanceName` required |
| `@Job` | Scheduled task | `name` ends with `SP`; `frequency` starts with `&` |
| `@Transactional` | Transaction control | Use `TransactionType` (UPPER_SNAKE_CASE) |
| `@Valid` | Input DTO validation | JSR 303/380 annotations on DTO fields |
| `@ControllerAdvice` | Centralized exception handling | Handlers return POJO, never void |
| `@Value` | Value injection from external sources | Eager (direct) or lazy (`Provider<T>`) |

Full code examples for all annotations: [reference/annotations.md](reference/annotations.md)

## Minimal @Service example

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoController {

    private final PedidoRepository pedidoRepository;

    @Inject
    public PedidoController(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }

    @Transactional
    public List<PedidoDTO> consultarPorPeriodo(PedidoFiltroDTO filtro) {
        return pedidoRepository.buscarPorPeriodo(filtro.getDataInicial(), filtro.getDataFinal());
    }
}
```

## Minimal @Repository example

```java
@Repository
public interface PedidoRepository extends JapeRepository<BigDecimal, Pedido> {

    @Criteria("DTPEDIDO >= :dataInicial AND DTPEDIDO <= :dataFinal")
    List<Pedido> buscarPorPeriodo(
        @Parameter("dataInicial") Timestamp dataInicial,
        @Parameter("dataFinal") Timestamp dataFinal
    );

    @Modifying
    @NativeQuery("UPDATE TGFCAB SET VLRNOTA = :valor WHERE NUNOTA = :nunota")
    int atualizarValor(@Parameter("valor") BigDecimal valor, @Parameter("nunota") BigDecimal nunota);
}
```

## Critical rules

1. **`@Inject` must be `com.google.inject.Inject`** — never `javax.inject.Inject`
2. **Injection via constructor** — never by field or setter
3. **`serviceName` ends with `SP`** — for @Service, @Controller and @Job
4. **@Service methods receive/return DTOs** — never `ServiceContext`
5. **`@Repository` extends `JapeRepository<ID, Entity>`**
6. **`@Parameter("name")`** in queries — not `@Param`
7. **`@Modifying` required** for write queries (@NativeQuery INSERT/UPDATE/DELETE)
8. **`@Listener` uses `instanceNames`** = instance/entity name, not table name
9. **`@Job frequency` starts with `&`** before CRON expression
10. **`@ExceptionHandler` returns POJO** — never void or ServiceContext
11. **Use `TransactionType` (UPPER_SNAKE_CASE)** in `@Transactional`; `EJBTransactionType` (PascalCase) in `@Service`

## Common errors

| Error | Cause | Fix |
|-------|-------|-----|
| DI not resolved | `javax.inject.Inject` used | Change to `com.google.inject.Inject` |
| Endpoint not registered | `serviceName` missing `SP` | Add `SP` suffix |
| `ServiceContext` in method params | Legacy pattern | Replace with DTOs |
| Query fails at runtime | `@Modifying` missing on write | Add `@Modifying` |
| Wrong parameter binding | `@Param` used | Replace with `@Parameter` |
| Listener not firing | `instanceNames` = table name | Use entity/instance name |
| Job not scheduling | `frequency` missing `&` | Add `&` prefix to CRON |
| `@ExceptionHandler` swallowed | Generic `Exception.class` catch-all | Use specific exception types |
| TX enum mismatch | Mixed `TransactionType` / `EJBTransactionType` | `@Transactional` → `TransactionType`, `@Service` → `EJBTransactionType` |

## Project structure

See [reference/project-structure.md](reference/project-structure.md) for full Add-on Studio directory layout and `application.yaml` configuration.

## For DB schema (dbscripts, datadictionary)

Use dbscripts + datadictionary for schema changes; keep SQL portable across Oracle/MSSQL with the macro helpers.
