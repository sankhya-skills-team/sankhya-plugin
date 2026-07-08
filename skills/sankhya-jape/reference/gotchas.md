# JAPE — Armadilhas e regras "NUNCA faça"

Regras não-óbvias do JAPE que geram bugs recorrentes. Cada entrada traz o sintoma, a causa e a correção.

---

## BigDecimal

### Comparação: nunca use `equals`

**Errado**
```java
if (valor.equals(BigDecimal.ZERO)) { ... }     // false para new BigDecimal("0.00")
```

**Certo**
```java
if (valor.compareTo(BigDecimal.ZERO) == 0) { ... }
```

**Causa:** `BigDecimal.equals` considera o `scale`. `new BigDecimal("1")` e `new BigDecimal("1.00")` não são iguais por `equals`, mas são por `compareTo`. Como o banco Oracle pode devolver valores com scale variável, comparações por `equals` falham silenciosamente.

### Concatenação em SQL: nunca use `toString`

**Errado**
```java
sql.append("WHERE VALOR = ").append(valor.toString());  // pode emitir "1E+2"
```

**Certo**
```java
sql.append("WHERE VALOR = ").append(valor.toPlainString());
```

**Causa:** `BigDecimal.toString()` emite notação científica (`1E+2`, `5.5E-3`) para números com `scale < 0` ou magnitudes extremas. O Oracle não aceita esse formato em literal SQL e lança `ORA-01722 invalid number`. O `NativeSql` já trata isso internamente ao usar `setNamedParameter`/`setParameter`, mas qualquer concatenação manual em string SQL precisa de `toPlainString()`.

**Ainda melhor:** não concatene valor nenhum em SQL. Use `setNamedParameter`:
```java
query.appendSql("WHERE VALOR = :VAL");
query.setNamedParameter("VAL", valor);
```

---

## JapeSession

### Close fora de finally — vazamento de conexão

**Errado**
```java
SessionHandle hnd = JapeSession.open();
doWork();                    // se lançar exceção, o close nunca executa
JapeSession.close(hnd);
```

**Certo**
```java
SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    doWork();
} finally {
    JapeSession.close(hnd);  // close(null) é seguro
}
```

### Compartilhar sessão entre threads

**Não faça:**
```java
SessionHandle hnd = JapeSession.open();
new Thread(() -> { doWork(hnd); }).start();    // sessão é ThreadLocal
```

**Correto para paralelizar:**
```java
// Na thread filha, abra nova sessão
new Thread(() -> {
    SessionHandle hnd = JapeSession.open();
    try { doWork(); } finally { JapeSession.close(hnd); }
}).start();
```

Ou, para executar em TX autônoma na thread corrente sem conflitar com a sessão atual, use `JapeSession.execWithAutonomousTX(...)`.

### Chamadas aninhadas de `open()` não criam sessão nova

Não se preocupe em proteger chamadas aninhadas. O framework empilha `SessionHandle` e só a raiz libera recursos. Padrão seguro:

```java
public void metodoA() {
    SessionHandle hnd = JapeSession.open();
    try { metodoB(); } finally { JapeSession.close(hnd); }
}

public void metodoB() {
    SessionHandle hnd = JapeSession.open();   // reaproveita a sessão
    try { /* ... */ } finally { JapeSession.close(hnd); }
}
```

### Sessão expirada ou interrompida

Se o timeout da sessão estourar, `getCurrentSession()` lança `PersistenceError`. Se for interrompida externamente, lança `JapeSessionInterruptedError`. Em ambos os casos, **não tente reusar** — abra nova sessão.

---

## NativeSql

### Parâmetro nomeado ausente

**Sintoma:** `IllegalStateException: Parameter :XXX not set`.

**Causa:** o SQL referencia `:XXX` mas `setNamedParameter("XXX", ...)` não foi chamado.

**Correção:**
- Garanta que todos os `:nome` no SQL tenham um `setNamedParameter` correspondente.
- Para construção dinâmica de queries opcionais: `query.setFillNamedParametersWithNull(true)` antes de `executeQuery()`. Parâmetros não fornecidos vão como `NULL`.

### Batch sem reuseStatements

**Errado**
```java
NativeSql q = new NativeSql(jdbc);
q.appendSql("UPDATE X SET Y = :Y WHERE ID = :ID");
q.setNamedParameter("Y", 1);
q.setNamedParameter("ID", 10);
q.addBatch();                // lança exceção
```

**Certo**
```java
NativeSql q = new NativeSql(jdbc);
q.setReuseStatements(true);   // OBRIGATÓRIO para addBatch/flushBatchTail
q.appendSql("UPDATE X SET Y = :Y WHERE ID = :ID");
for (Item i : items) {
    q.setNamedParameter("Y", i.getY());
    q.setNamedParameter("ID", i.getId());
    q.addBatch();
}
q.flushBatchTail();
```

### Não fechar NativeSql / ResultSet

**Errado**
```java
NativeSql q = new NativeSql(jdbc);
q.appendSql("...");
ResultSet rs = q.executeQuery();
return parse(rs);    // PreparedStatement e ResultSet vazam
```

**Certo — idioma canônico do codebase** (usa `JdbcUtils.closeResultSet` + `NativeSql.releaseResources`):

```java
import com.sankhya.util.JdbcUtils;
import br.com.sankhya.jape.sql.NativeSql;

NativeSql q = null;
ResultSet rs = null;
try {
    q = new NativeSql(jdbc);
    q.appendSql("...");
    rs = q.executeQuery();
    return parse(rs);
} finally {
    JdbcUtils.closeResultSet(rs);       // null-safe, engole SQLException
    NativeSql.releaseResources(q);       // null-safe, fecha o statement e limpa o estado
}
```

Notas:
- `JdbcUtils.closeResultSet(rs)` — fecha o `ResultSet` explicitamente. Útil quando o `ResultSet` foi extraído do `NativeSql` e repassado.
- `NativeSql.releaseResources(q)` — equivalente estático null-safe a `q.close()`. Utilizado em [InMemoryDataSet.java:150-151](../../../../JAPE/src/br/com/sankhya/jape/util/InMemoryDataSet.java) e em Centrais do MGECom.

Se o método consome o `ResultSet` no mesmo escopo, `if (q != null) q.close();` é suficiente. Para fluxos que separam extração e processamento, use o par `JdbcUtils.closeResultSet` + `NativeSql.releaseResources`.

### Comentários SQL e hints Oracle

`/* ... */` comuns são removidos antes do parse de parâmetros nomeados. Mas hints Oracle (`/*+ INDEX(tab idx) */`) são preservados. Se precisar de hints, mantenha o formato `/*+ ... */` com o `+` imediatamente após a barra-asterisco.

### OnlyDate em Oracle

Parâmetros do tipo `OnlyDate` precisam de conversão especial em Oracle. O framework faz isso automaticamente, mas se você usa `setReuseStatements(true)` e o mesmo parâmetro oscila entre `OnlyDate` e outros tipos, pré-registre:
```java
query.addOnlyDateNamedParameter("DATA_REF");
```

---

## Macros SQL

### Macro dentro de macro não funciona

**Errado**
```sql
SELECT onlydate(addMonths(DATA, 1)) FROM TAB   -- MacroTranslator não é recursivo
```

**Certo** — decomponha:
```java
// Opção 1: use SQL nativo do banco
"SELECT TRUNC(ADD_MONTHS(DATA, 1)) FROM TAB"  // só Oracle

// Opção 2: calcule em Java ou use duas queries
```

### Dialetos suportados

Apenas **Oracle** e **SQL Server**. MySQL é parcialmente suportado dentro do dialeto Oracle (detectado via `databaseVendor`). Outros SGBDs (PostgreSQL, DB2) **não são suportados** pelo MacroTranslator e lançam `MacroTranslator.InvalidDialect`.

### Lista de macros seguras

Ver [macros.md](macros.md) para o catálogo completo. Macros mais usadas: `onlydate`, `ignorecase`, `nullValue`, `diffdays`, `maxLines`, `dbDate`, `concatstr`.

---

## Transações

### `beginTransaction` com TX ativa

**Sintoma:** `PersistenceError: já existe transação ativa`.

**Causa:** chamada de `hnd.beginTransaction()` dentro de contexto já em TX (EJB com `REQUIRED`, callback de `execWithTX`).

**Correção:** não inicie TX manual dentro de método EJB com TX container-managed. Use `execWithTX` apenas quando estiver fora de TX (ex.: action de Cuckoo, thread standalone).

### Fake transaction sempre faz rollback

```java
hnd.execWithAutonomousFakeTX(new NewTXBody() {
    public void doWithTx() throws Exception {
        // tudo aqui será desfeito no final, mesmo sem erro
    }
});
```

Útil para simulação, validação que usa lock de banco, ou leitura que precisa isolar efeitos colaterais.

### Listeners desativados em TX autônoma

`transactionListenersActive = false` em TX autônoma. Se seu código depende de o `TransactionListener` disparar, **não rode em TX autônoma**. Use `execWithTX` na TX corrente.

---

## EntityFacade / EntityDAO

### Entidade duplicada

Ao registrar duas entidades com o mesmo nome no mesmo provider, o `EntityDAOLocator` lança `PersistenceError`. Isso indica conflito de metadado XML — ver `DataDictionary/` e revisar se há dois descritores para a mesma entidade.

### VO carregado fora de TX

VOs carregados fora de TX não são sincronizados com updates posteriores. Se você carregar um VO, sair da TX, modificar e tentar salvar, o estado pode estar stale. Mantenha load-modify-save dentro do mesmo `execWithTX`.

### `createEmptyVO` vs `createEntity`

`createEmptyVO` apenas instancia o VO em memória. Para persistir:

```java
DynamicVO vo = (DynamicVO) dwf.createEmptyVO(DynamicEntityNames.MINHA);
vo.setProperty("CAMPO", valor);
dwf.createEntity(DynamicEntityNames.MINHA, (EntityVO) vo);  // só aqui vai pro banco
```

### `createEntity` vs `setEntity` vs `setValueObject`

| Chamada | O que faz | Quando usar |
|---|---|---|
| `dwf.createEntity(entName, vo)` | INSERT — retorna `PersistentLocalEntity` | Registro novo |
| `entity.setValueObject(vo)` | UPDATE — aplica as mudanças do VO ao registro persistido | Registro já existe |
| `state.setEntity(entity)` | Atribuição de campo em `PrePersistEntityState` — não executa IO | Logo após `createEntity`, para que os próximos passos reusem a referência |
| `dwf.removeEntity(entName, pk)` | DELETE por PK | Para apagar |

Padrão usado nas Centrais ([CACHelper.java:1501-1506](../../../../MGECom-Model/src/br/com/sankhya/mgecomercial/model/helper/centrais/CACHelper.java)):

```java
if (state.isNew()) {
    PersistentLocalEntity entity = dwf.createEntity(
        state.getDao().getEntityName(),
        (EntityVO) state.getNewVO());   // INSERT
    state.setEntity(entity);             // guarda a referência
} else {
    state.getEntity().setValueObject(
        (EntityVO) state.getNewVO());   // UPDATE
}
```

`setEntity` aparece logo após `createEntity` no fluxo de INSERT; a proximidade induz à confusão de que ele participa da persistência. A implementação ([PrePersistEntityState.java:142](../../../../JAPE/src/br/com/sankhya/jape/vo/PrePersistEntityState.java)) atribui o campo `this.entity`.

`EntityFacade` não expõe `updateEntity`. Para UPDATE use `PersistentLocalEntity.setValueObject(vo)`; para forçar `ejbStore` síncrono use `setValueObjectWithUpdate(vo)` (disponível em `AbstractBMPEntity`).

---

## Miscelânea

### Encoding do projeto

- Arquivos `.java` em `ISO-8859-1`, não UTF-8
- Literal string com acentos em código Java segue esse encoding
- Mensagens em `PersistenceTierMessages` usam propriedades ISO-8859-1

### Java version

- Código geral: Java 8
- BEAN classes com xDoclet: Java 6 obrigatório
- Não use `var`, lambdas complexas em `switch`, `List.of`, `Optional.ifPresentOrElse`, etc.

### stdout no JAPE (antipattern herdado)

O próprio `NativeSql.logNamedParameters` faz `System.out.println`. Não replique. Use o logger do seu módulo (`SKLog`, `Logger`, etc.).

### EasySQL é legado

Evite `EasySQL` em código novo. Usa `maxRows=100` hardcoded e fecha a conexão no `close()`, diferente do `NativeSql`. Migre para `NativeSql` se encontrar.
