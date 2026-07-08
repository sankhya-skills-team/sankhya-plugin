# JAPE — Cheatsheet de APIs

Referência rápida das classes mais usadas. Para detalhes internos, ver [component-analysis-jape.md](../../../../docs/agents/component-deep-analyzer/component-analysis-jape.md).

---

## JapeSession — `br.com.sankhya.jape.core.JapeSession`

| API | Uso | Notas |
|---|---|---|
| `JapeSession.open()` | Abre/reusa sessão na Thread | Retorna `SessionHandle`. Chamadas aninhadas são seguras |
| `JapeSession.close(SessionHandle)` | Fecha o handle | Aceita `null`; só libera recursos se for o handle raiz |
| `JapeSession.getCurrentSession()` | Sessão corrente | Lança `PersistenceError` se não houver sessão |
| `JapeSession.suspend()` | Suspende sessão/TX para operação isolada | Retorna `SuspendHandle` — chamar `resume()` no finally |
| `JapeSession.execWithTX(TXBody)` | Executa o bloco em nova TX | Não chame se já há TX ativa |
| `JapeSession.execWithAutonomousTX(NewTXBody)` | Executa em TX independente da corrente | Suspende a sessão atual, cria nova |
| `JapeSession.execWithAutonomousFakeTX(NewTXBody)` | TX autônoma que sempre faz rollback | Para simulação/validação |
| `JapeSession.execWithNoTX(NoTXBody)` | Executa sem TX | Útil para SELECTs longos sem lock |

Ver [transactions.md](transactions.md) para exemplos completos.

---

## SessionHandle

Métodos relevantes do objeto retornado por `open()`:

| API | Uso |
|---|---|
| `hnd.execWithTX(TXBody)` | Executa em TX |
| `hnd.beginTransaction()` | Inicia TX manual (raro) |
| `hnd.commit()` / `hnd.rollback()` | Controle manual de TX (raro) |
| `JapeSession.close(hnd)` | Fecha o handle (via classe estática) |

Prefira `execWithTX` ao controle manual — evita esquecer o rollback em exceção.

---

## EntityFacade — `br.com.sankhya.jape.EntityFacade`

Obtenção:
```java
EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
```

| API | Uso |
|---|---|
| `findEntityByPrimaryKey(entName, pk)` | Retorna `PersistentLocalEntity` por PK (ou `null`) |
| `findByDynamicFinder(FinderWrapper)` | Retorna `Collection<PersistentLocalEntity>` |
| `findByDynamicFinderAsVO(FinderWrapper)` | Retorna `Collection<DynamicVO>` (mais leve) |
| `createEmptyVO(entName)` | Cria VO vazio em memória — **não persiste** |
| `createEntity(entName, EntityVO)` | **INSERT** — retorna `PersistentLocalEntity` recém-criada |
| `removeEntity(entName, Object[] pk)` | DELETE por PK. Não existe `deleteEntity` |
| `getDescriptor(entName)` | Metadados da entidade |

> **Não existe** `dwf.updateEntity(...)` em `EntityFacade`. UPDATE é feito no `PersistentLocalEntity` (tabela abaixo), não no facade.

### PersistentLocalEntity — caminhos reais de UPDATE/DELETE

Obtida via `findEntityByPrimaryKey` ou `findByDynamicFinder`.

| API | Uso |
|---|---|
| `getValueObject()` | Retorna o `EntityVO` atual |
| `setValueObject(EntityVO vo)` | **UPDATE** — persiste as mudanças do VO (flush) |
| `setValueObjectWithUpdate(EntityVO vo)` | UPDATE forçando `ejbStore` síncrono (somente em `AbstractBMPEntity`) |
| `remove()` | DELETE via EJB local object (herdado de `EJBLocalObject`) |
| `isValid()` | Se a entidade ainda é válida (não removida) |

### Padrão canônico INSERT vs UPDATE (PrePersistEntityState)

Usado nas Centrais (`CACHelper`, etc.). `setEntity` NÃO persiste — é apenas guardador de referência.

```java
if (state.isNew()) {
    PersistentLocalEntity entity = dwf.createEntity(
        state.getDao().getEntityName(),
        (EntityVO) state.getNewVO());    // INSERT
    state.setEntity(entity);              // apenas guarda a referência
} else {
    state.getEntity().setValueObject(
        (EntityVO) state.getNewVO());    // UPDATE
}
```

Referência real: [CACHelper.java:1501-1506](../../../../MGECom-Model/src/br/com/sankhya/mgecomercial/model/helper/centrais/CACHelper.java).

### FinderWrapper

```java
new FinderWrapper(
    DynamicEntityNames.MINHA_ENTIDADE,                // nome
    "this.ATIVO = 'S' AND this.DATA >= ?",             // cláusula where
    new Object[]{ dataRef }                             // parâmetros posicionais
);
```

- Use o alias `this.` para referenciar campos da entidade
- Placeholder `?` para parâmetros posicionais
- Pode incluir ordenação: `FinderWrapper(name, where, params, orderBy)`

---

## DynamicVO — `br.com.sankhya.jape.vo.DynamicVO`

VO dinâmico usado em toda a camada de negócio.

| API | Tipo de retorno |
|---|---|
| `vo.asBigDecimal("CAMPO")` | `BigDecimal` (null-safe, retorna `null` se o campo for null) |
| `vo.asString("CAMPO")` | `String` |
| `vo.asDate("CAMPO")` | `Timestamp` |
| `vo.asBigDecimalValue("CAMPO")` | `BigDecimal` com default 0 para null |
| `vo.asInt("CAMPO")` | `int` primitivo |
| `vo.setProperty("CAMPO", valor)` | Seta o valor (qualquer tipo) |
| `vo.asVO("CAMPO_RELACIONADO")` | VO de relacionamento |

**Campos sempre em MAIÚSCULAS** (convenção do dicionário de dados Sankhya).

---

## NativeSql — `br.com.sankhya.jape.sql.NativeSql`

```java
NativeSql q = null;
try {
    q = new NativeSql(jdbc);
    q.appendSql("SELECT ... FROM ... WHERE CAMPO = :VAL");
    q.setNamedParameter("VAL", valor);
    ResultSet rs = q.executeQuery();
    while (rs.next()) { /* ... */ }
} finally {
    if (q != null) q.close();
}
```

| API | Uso |
|---|---|
| `new NativeSql(JdbcWrapper)` | Inicializa |
| `appendSql(String)` | Monta o SQL (pode ser chamado várias vezes) |
| `setNamedParameter(String, Object)` | Parâmetro `:nome` |
| `addParameter(Object)` | Parâmetro posicional `?` |
| `executeQuery()` | SELECT — retorna `ResultSet` |
| `executeUpdate()` | DML — retorna `int` (linhas afetadas) |
| `setScrollableResult(boolean)` | ResultSet scrollable |
| `setReuseStatements(boolean)` | Obrigatório para batch |
| `addBatch()` | Adiciona ao batch (requer reuseStatements) |
| `flushBatchTail()` | Executa o batch |
| `setFillNamedParametersWithNull(boolean)` | Parâmetros não fornecidos viram NULL |
| `addOnlyDateNamedParameter(String)` | Pré-registra parâmetro `OnlyDate` (Oracle) |
| `close()` | Libera PreparedStatement/ResultSet |

### Helpers estáticos

```java
BigDecimal valor = (BigDecimal) NativeSql.getBigDecimal(
    jdbc, "VALOR", "TGFCAB",
    "NUNOTA = :NUNOTA",
    new Object[]{ nunota });
```

Formato `(jdbc, coluna, tabela, where, params)`. Retorna valor único — lança se a query devolver mais de uma linha.

---

## ObtainJdbcWrapper

Dentro de EJB:
```java
JdbcWrapper jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
```

Dentro de callback de `execWithTX`:
```java
JdbcWrapper jdbc = JapeSession.getCurrentSession().getJdbcWrapper();
```

Fora desses contextos: raro. Normalmente recebe-se `jdbc` como parâmetro de método.

---

## EntityQuery — `br.com.sankhya.jape.core.EntityQuery` (API fluente)

```java
Collection<DynamicVO> rows = EntityQuery.build(dwf)
    .entity(DynamicEntityNames.TGFCAB)
    .where("this.TIPMOV = ? AND this.STATUSNOTA = ?")
    .parameters(new Object[]{ "V", "L" })
    .orderBy("this.NUNOTA DESC")
    .loadOnFind("this.PARCEIRO")   // eager load de relacionamento
    .list();
```

Vantagens sobre `FinderWrapper`: encadeamento fluente e `loadOnFind` para relacionamentos.

---

## EntitySaver — `br.com.sankhya.jape.core.EntitySaver`

```java
EntitySaver.build(dwf)
    .entity(DynamicEntityNames.MINHA)
    .vo(meuVO)
    .create();   // ou .update()
```

---

## Criteria — `br.com.sankhya.jape.sql.Criteria`

Builder de cláusulas WHERE programáticas. Uso em finders customizados.

```java
Criteria c = new Criteria();
c.addClause("ATIVO = ?", "S");
c.addClause("VALOR > ?", valorMinimo);
String where = c.getSql();
Object[] params = c.getParameters();
```

---

## ProcedureCaller — `br.com.sankhya.jape.util.ProcedureCaller`

```java
ProcedureCaller pc = new ProcedureCaller(jdbc);
pc.setProcedureName("STP_MINHA_PROC");
pc.addParameter(IN_PARAM, Types.NUMERIC, codigo);
pc.addParameter(OUT_PARAM, Types.VARCHAR, null);
pc.execute();
String retorno = (String) pc.getReturnValue("OUT_PARAM");
```

---

## Obter facades conforme o domínio

| Facade | Uso | Método |
|---|---|---|
| DWF | Entidades em geral | `EntityFacadeFactory.getDWFFacade()` |
| MGEFront | Entidades do front MGE | `EntityFacadeFactory.getMGEFrontFacade()` |
| CRUDServiceProvider | CRUD genérico | `EntityFacadeFactory.getCRUDServiceProvider()` |

Para decidir qual facade usar, veja a regra no módulo — a maioria usa DWF.

---

## ValueObjectManager (quando precisar de VO fora de entidade)

```java
DynamicVO vo = ValueObjectManager.getValueObject(
    descriptor, DynamicVO.class);
vo.setProperty("CAMPO", valor);
```

Use apenas para VOs temporários (DTO-like). Para persistência, `createEmptyVO` + `createEntity` é o caminho.


## Fechamento de PreparedStatement (verificado em build, 2026)

Não existe `JdbcWrapper.closeStatement(...)`. Para liberar `PreparedStatement`/`Statement` use **`com.sankhya.util.JdbcUtils.closeStatement(java.sql.Statement)`** (mesma classe de `closeResultSet`/`closeConnection`). No `finally`: `JdbcUtils.closeResultSet(rs); JdbcUtils.closeStatement(ps);`.
