# JAPE — Transações

Padrões de uso de `execWithTX`, `execWithAutonomousTX`, `execWithAutonomousFakeTX` e `execWithNoTX`.

## Modelo mental

1. **TX gerenciada pelo container (EJB REQUIRED)** — default para métodos de `*SPBean`/`*FacadeBean`. Você não abre TX; o container faz.
2. **TX explícita (`execWithTX`)** — quando você precisa de TX e não está em contexto EJB managed (jobs Cuckoo, threads standalone, actions de comando).
3. **TX autônoma (`execWithAutonomousTX`)** — suspende a TX corrente e roda o bloco em TX própria. O commit da TX autônoma não afeta a TX original.
4. **Fake TX (`execWithAutonomousFakeTX`)** — igual à autônoma, mas sempre faz rollback.
5. **Sem TX (`execWithNoTX`)** — suspende a TX corrente e roda sem nenhuma TX.

## `execWithTX` — padrão mais comum

```java
SessionHandle hnd = JapeSession.open();
try {
    hnd.execWithTX(new JapeSession.TXBody() {
        public void doWithTx() throws Exception {
            EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
            // ... operações que devem commitar juntas
        }
    });
} finally {
    JapeSession.close(hnd);
}
```

### Regras
- Se o bloco lança exceção, a TX sofre rollback automático.
- Se você captura a exceção dentro do bloco e não faz rethrow, o framework ainda commita — evite.
- Não chame `execWithTX` se já estiver em TX ativa (ex.: dentro de método EJB REQUIRED). Vai lançar `PersistenceError`.

### Verificando se há TX ativa
```java
if (JapeSession.getCurrentSession().isInTransaction()) {
    // já estamos em TX — apenas execute
} else {
    hnd.execWithTX(new JapeSession.TXBody() { ... });
}
```

## `execWithAutonomousTX` — operação isolada

Quando você está em uma TX e precisa executar algo que **não deve ser afetado pelo rollback** da TX externa (ex.: log de auditoria que deve persistir mesmo se o fluxo principal falhar).

```java
JapeSession.execWithAutonomousTX(new JapeSession.NewTXBody() {
    public void doWithNewTX() throws Exception {
        EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
        DynamicVO logVO = (DynamicVO) dwf.createEmptyVO(DynamicEntityNames.LOG);
        logVO.setProperty("MENSAGEM", "erro em X");
        dwf.createEntity(DynamicEntityNames.LOG, (EntityVO) logVO);
    }
});
```

### Limitações
- `transactionListenersActive = false` — listeners da TX corrente não disparam.
- Executa em thread separada internamente (via `DistributedTransaction.doWithNonDistributedTransaction`). Não guarde `ThreadLocal` dentro do bloco.
- Mais caro que o `execWithTX` normal — use só quando realmente precisar isolar.

## `execWithAutonomousFakeTX` — simulação com rollback garantido

Útil para:
- Validação que precisa **ver** o resultado de um UPDATE sem persistir
- Teste de lógica que depende de lock pessimista sem deixar marca
- Leitura isolada que precisa rodar em TX nova

```java
JapeSession.execWithAutonomousFakeTX(new JapeSession.NewTXBody() {
    public void doWithNewTX() throws Exception {
        // insere, atualiza, lê com isolation... tudo será desfeito
        EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
        dwf.updateEntity(...);  // visível dentro deste bloco
        // ... validação
    }
});
// após este ponto, nenhuma das mudanças foi commitada
```

## `execWithNoTX` — sem TX alguma

Útil para SELECTs longos que não devem manter lock, ou operações que devem rodar fora de contexto transacional:

```java
JapeSession.execWithNoTX(new JapeSession.NoTXBody() {
    public void doWithNoTX() throws Exception {
        // SELECT sem TX - sem lock, sem snapshot isolation
    }
});
```

## Retry automático em deadlock de banco

Se a TX implementa `TXBlockRedoable` e a system property `jape.manual-tx.deadlock.max-retry` é maior que zero, o framework refaz a TX automaticamente em caso de deadlock do banco.

```java
class MinhaTX extends JapeSession.TXBody implements JapeSession.TXBlockRedoable {
    public void doWithTx() throws Exception { /* ... */ }
    // Framework chama novamente em caso de deadlock, até max-retry
}
```

Para deadlocks detectados a nível de aplicação (`DeadLockError` do próprio JAPE) não há retry automático — a sessão de menor prioridade morre e precisa ser reiniciada pelo chamador.

## Stp_skw_before_commit

Se `jape.ds.call.before.commit.proc` está setado, cada commit dispara a procedure `Stp_skw_before_commit()` em cada datasource usado. Falha nessa proc desfaz **toda** a TX. Se sua feature toca integração com essa procedure, teste com a flag ativa — é ponto de falha crítico.

## Listeners de TX

### `TransactionListener` — registrado por sessão
```java
JapeSession.getCurrentSession().addTransactionListener(new TransactionListener() {
    public void beforeCommit() throws Exception { /* ... */ }
    public void afterCommit() { /* ... */ }
    public void afterRollback() { /* ... */ }
});
```

### `ITransactionListener` — registrado globalmente (via `Jape.getSingleton().addTransactionListener`)

Escopo global — dispara em **todas** as TX. Use com moderação.

## Erros comuns

| Sintoma | Causa provável |
|---|---|
| `PersistenceError: já existe TX ativa` | Chamou `execWithTX` em contexto EJB com TX container-managed |
| `PersistenceError: não há sessão ativa` | Chamou `getCurrentSession()` sem `open()` antes |
| `DeadLockError` | Duas sessões esperando recursos mútuos — a de menor prioridade morreu |
| `JapeSessionInterruptedError` | Alguém chamou `interrupt()` externamente (comum em cancelamento de job) |
| Listeners não disparam | Você está em `execWithAutonomousTX` — por design |


## Correção de assinatura (jape 4.35 — verificado em build real, 2026)

`JapeSession.execWithAutonomousTX` é **estático** e recebe `JapeSession.NewTXBody`, cujo método abstrato é **`public Object run() throws Exception`** (NÃO `doWithNewTX()` — assinatura antiga/desatualizada). Forma correta:

```java
JapeSession.execWithAutonomousTX(new JapeSession.NewTXBody() {
    public Object run() throws Exception {
        // ... operação isolada
        return null;
    }
});
```

Erro típico se usar a assinatura antiga: *"<anonymous ...> is not abstract and does not override abstract method run() in NewTXBody"*. Não chame `execWithAutonomousTX` a partir de `SessionHandle` (não existe o método de instância) — é estático em `JapeSession`.


## `@Service` de leitura via JdbcWrapper exige TX ativa (verificado em build real, 2026)

Um `@Service` de **leitura** que acessa o banco por `EntityFacadeFactory.getDWFFacade().getJdbcWrapper().getPreparedStatement(...)` precisa de **contexto transacional ativo**. Se o `@Service` for declarado com `transactionType = EJBTransactionType.NotSupported`, não há TX → o `JdbcWrapper` não tem conexão JDBC ligada e lança **`"JDBC Wrapper: Sessão não inicializada"`**.

Sintoma típico: o método de **gravação** (que roda em TX, ex.: `finalizarPesagem`) funciona, mas o método de **leitura/consulta** falha com esse erro.

Correção: declarar o `@Service` de leitura com `transactionType = EJBTransactionType.Required`. **Não** use `Supports` — ele não cria TX quando a SP é chamada direto pelo broker sem TX envolvente, e o erro persiste. Abrir `JapeSession.open()` no controller **não basta** sozinho: o `JdbcWrapper` depende da transação, não só da sessão.
