<system_instruction>
Sempre responda em PORTUGUESE (PT-BR).
</system_instruction>

# Sankhya Micromodule — Legacy EJB2 Approach

> **Scope:** This skill covers the **legacy** EJB2/XDoclet approach. For the modern SDK approach (@Service, @Repository, @Listener annotations), use `micromodule-sdk`.

## When to use

- Creating or modifying SPBeans, EntityListeners, ServiceWrappers, Jobs
- Writing `service-providers.xml`, `mgeschedule-cfg.xml`, `BootModuleListener`
- Configuring `build.gradle`, `settings.gradle` for micromodule projects
- Understanding `BaseSPBean`, `ServiceContext`, `DynamicVO` usage

## What is a micromodule

Autonomous component deployed as EAR into the customer's WildFly environment. Extends SankhyaOm via shared classpath without altering the monolith. Must have **single responsibility** and be as lean as possible.

## Project structure

```
{name}-model/
  ejbsrc/br/.../
    model/facades/    # *SP.java, *SPHome.java, *SPSession.java (XDoclet generated)
    job/              # Job interfaces (generated)
  src/main/java/br/.../
    entity/           # Rich model (no mandatory suffix)
    repository/       # DB access layer (suffix Repository)
    service/          # Domain orchestrator (suffix Service)
    controller/       # EJB thin entry points (suffix SPBean)
    job/              # *JobSPBean.java
  src/main/resources/
    META-INF/
      ejb-jar.xml
      mgeschedule-cfg.xml
    br/.../
      sql/            # Named .sql files (prefix: que*, ins*, upd*, del*)
      dd/             # Internal entity config
      parameters/     # parameter.xml
{name}-vc/
  src/main/java/br/.../
    servlet/          # BootModuleListener
    graphql/          # GraphQL resolvers (optional)
  webapp/WEB-INF/
    web.xml
    resources/
      service-providers.xml   ← CRITICAL
datadictionary/       # One .xml per table/view
dbscripts/
  oracle.sql
  mssqlserver.sql
build.gradle
settings.gradle
```

## Key components

| Component | Description | Reference |
|-----------|-------------|-----------|
| `*SPBean.java` | EJB2 service endpoint | [reference/ejb2-components.md](reference/ejb2-components.md#service-bean-ejb2) |
| `BootModuleListener` | Registers all components at startup | [reference/ejb2-components.md](reference/ejb2-components.md#bootmodulelistener) |
| `EntityListener` | Persistence hooks (before/afterInsert, etc.) | [reference/ejb2-components.md](reference/ejb2-components.md#entitylistener) |
| `ServiceWrapper` | Pre/post processing around existing services | [reference/ejb2-components.md](reference/ejb2-components.md#servicewrapper) |
| `service-providers.xml` | Exposes SPBeans as HTTP endpoints | [reference/ejb2-components.md](reference/ejb2-components.md#service-providersxml) |
| `ServiceContext` read/write | Request/response API | [reference/request-response.md](reference/request-response.md) |

## Naming conventions

| Artifact | Pattern | Example |
|----------|---------|---------|
| Service bean | `*SPBean.java` | `FiscalSPBean.java` |
| Remote interface (generated) | `*SP.java` | `FiscalSP.java` |
| Home interface (generated) | `*SPHome.java` | `FiscalSPHome.java` |
| Session wrapper (generated) | `*SPSession.java` | `FiscalSPSession.java` |
| Job bean | `*JobSPBean.java` | `ConsultCnpjJobSPBean.java` |
| SQL file | `que*.sql`, `ins*.sql` | `queSeqMaximaICMS.sql` |
| DB table | Unique prefix in UPPERCASE | `TTKREGRA`, `TTKNOT` |
| JNDI | `{module}/model/ejb/session/{Name}SP` | `turnkey/model/ejb/session/FiscalSP` |

## JapeSession pattern (mandatory in all SPBeans)

```java
JapeSession.SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    // business logic
} finally {
    JapeSession.close(hnd);   // ALWAYS close in finally
}
```

## Error handling in micromodules

```java
import br.com.sankhya.internal.sdk.exceptions.TransactionRollbackException;

try {
    hnd = JapeSession.open();
    // logic
} catch (MGEModelException e) {
    throw e;   // business error: propagate clean (container commits — ok if no writes)
} catch (Exception e) {
    throw new TransactionRollbackException(e);  // unexpected: RuntimeException → ROLLBACK
} finally {
    JapeSession.close(hnd);
}
```

> **Do NOT use `throwExceptionRollingBack(e)`** in micromodules — `SessionContext` is not injected by TinyEJB.
> **Do NOT use `MGEModelException.throwMe(e)`** for unexpected errors — TinyEJB does COMMIT instead of rollback.

## Non-negotiable rules

1. **Always extend `BaseSPBean`** in micromodules — provides `throwExceptionRollingBack()` and `setupContext()`
2. **`JapeSession` always closed in `finally`** — no exceptions
3. **`next()` always called in ServiceWrapper** unless fully replacing the service
4. **Business logic in Helper/Service classes**, not in SPBean
5. **For persistence details** → use `sankhya-jape` skill
6. **For DB schema (dbscripts, datadictionary)** → use dbscripts + datadictionary (SQL portable Oracle/MSSQL via macros)
7. **For null-safe utilities** → use the SDK null-safe helpers (`StringUtils`, `BigDecimalUtil`, etc.)

## Implementation checklist

- [ ] `service-providers.xml` created with `domain`, `class`, `type`, `jndi`, `authentication`
- [ ] JNDI in `service-providers.xml` matches `jndi-name` in xdoclet annotation
- [ ] `JapeSession` always closed in `finally` with `JapeSession.close(hnd)`
- [ ] `JdbcWrapper` always closed in `finally` with `JdbcWrapper.closeSession(jdbc)`
- [ ] `next()` called in ServiceWrapper
- [ ] Components registered in `BootModuleListener` via `MicroModuleUtils`
- [ ] `moduleLib` vs `implementation` reviewed in `build.gradle`
- [ ] Each Java class has a corresponding `*Test` class
- [ ] Exceptions: `TransactionRollbackException` for rollback; `MGEModelException` for business errors

## Critical warnings

> **Listeners** block user transactions — performance is essential.
> **Updates** pause listener transactions for up to 2 minutes.
> **`publishModule`** distributes to ALL customers — publish with extreme caution.
> **JNDI mismatch** in `service-providers.xml` causes silent lookup error.
