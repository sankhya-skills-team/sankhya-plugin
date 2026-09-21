# JAPE — Gerenciamento de Recursos

Quem fecha o quê, em que ordem, e por quê. Complementa [gotchas.md](gotchas.md) (que traz o idioma de fechamento de `NativeSql`/`ResultSet` e as armadilhas de sessão) e [transactions.md](transactions.md) (ciclo de TX). Aqui o foco é o aninhamento de recursos e a posse deles.

> APIs verificadas em `jape-4.35.jar` e `sanutil-4.35.jar`.

## Ordem de fechamento com recursos aninhados

Fechar na ordem **inversa** da abertura. O recurso de fora precisa continuar válido enquanto o de dentro fecha.

```java
JapeSession.SessionHandle hnd = null;
JdbcWrapper jdbc = null;
NativeSql sql = null;
ResultSet rs = null;
try {
    hnd = JapeSession.open();
    jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
    jdbc.openSession();

    sql = new NativeSql(jdbc);
    sql.loadSql(MinhaClasse.class, "sql/dominio/queExemplo.sql");
    sql.setNamedParameter("CHAVE", chave);
    rs = sql.executeQuery();
    while (rs.next()) {
        // ...
    }
} finally {
    JdbcUtils.closeResultSet(rs);     // 1. ResultSet
    NativeSql.releaseResources(sql);  // 2. NativeSql (libera o statement)
    JdbcWrapper.closeSession(jdbc);   // 3. JdbcWrapper (devolve a conexao ao pool)
    JapeSession.close(hnd);           // 4. SessionHandle
}
```

Todos os quatro são null-safe — não precisa de `if (x != null)`.

Invertendo a ordem (fechar o `JdbcWrapper` antes do `ResultSet`) nada estoura em teste: `JdbcUtils.closeResultSet` captura e **engole** a exceção. O cursor é que pode ficar aberto no banco.

## Quem abre, fecha. Quem recebe, não fecha.

Método que **recebe** `JdbcWrapper` (ou `SessionHandle`) por parâmetro não fecha o recurso: quem abriu ainda vai usá-lo.

```java
// ERRADO - derruba o recurso do caller no meio do fluxo dele
public void processar(JdbcWrapper jdbc) throws Exception {
    try {
        // ...
    } finally {
        JdbcWrapper.closeSession(jdbc);
    }
}

// CERTO - fecha so o que este metodo abriu
public void processar(JdbcWrapper jdbc) throws Exception {
    NativeSql sql = null;
    ResultSet rs = null;
    try {
        sql = new NativeSql(jdbc);
        rs = sql.executeQuery();
        // ...
    } finally {
        JdbcUtils.closeResultSet(rs);
        NativeSql.releaseResources(sql);
        // NAO fecha jdbc - pertence a quem chamou
    }
}
```

Helper estático que recebe o `jdbc` do chamador segue a mesma regra.

## Parâmetro posicional × nomeado em laço

Os dois tipos de parâmetro do `NativeSql` se comportam de forma **diferente** quando o mesmo objeto é reexecutado num laço:

| API | Armazenamento | Em laço |
|---|---|---|
| `setNamedParameter(nome, valor)` | mapa, chaveado pelo nome em maiúsculas | **sobrescreve** — nada a limpar |
| `addParameter(valor)` | lista sequencial | **acumula** — precisa de `cleanParameters()` |

```java
// nomeado: seguro sem cleanParameters - cada volta sobrescreve a chave
for (Item i : items) {
    q.setNamedParameter("NUNOTA", i.getNunota());
    q.executeUpdate();
}

// posicional: sem cleanParameters a lista cresce a cada volta e o bind quebra
for (Item i : items) {
    q.cleanParameters();
    q.addParameter(i.getNunota());
    q.executeUpdate();
}
```

`cleanParameters()` limpa os dois — a lista e o mapa.

## CallableStatement

Para procedure chamada direto pela conexão (quando `ProcedureCaller` não se aplica), o `Statement` é seu para fechar:

```java
CallableStatement cstm = null;
try {
    cstm = jdbc.getConnection().prepareCall("{call STP_MINHA_PROC(?)}");
    cstm.setString(1, flag);
    cstm.execute();
} finally {
    JdbcUtils.closeStatement(cstm);   // null-safe
}
```

Não feche a `Connection` obtida por `jdbc.getConnection()` — ela pertence ao `JdbcWrapper`.

## `TXBlockRedoable` — o bloco roda de novo

Quando o bloco implementa `JapeSession.TXBlockRedoable`, o framework **reexecuta `doWithTx()`** em caso de deadlock de banco (ver [transactions.md](transactions.md)). Consequência para recursos e estado:

- Recurso aberto dentro de `doWithTx()` precisa ser aberto **e fechado** dentro dele, a cada tentativa.
- Objeto mutável que acumula estado (contadores, listas de resultado, contexto de processamento) precisa ser **recriado** no início do bloco. Estado deixado pela primeira tentativa contamina a segunda — a retentativa não é um retry limpo se o objeto veio de fora.

```java
hnd.execWithTX(new JapeSession.TXBlockRedoable() {
    public void doWithTx() throws Exception {
        JdbcWrapper jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
        jdbc.openSession();
        try {
            Processador p = new Processador(parametrosOriginais);   // recriado a cada tentativa
            p.processar();
        } finally {
            JdbcWrapper.closeSession(jdbc);
        }
    }
});
```

## Sintoma → causa

| Sintoma | Causa provável |
|---|---|
| `ORA-00933`/`maximum open cursors exceeded` (`ORA-01000`) | `ResultSet` não fechado dentro de laço |
| Pool de conexões esgota depois de algumas horas no ar | `JdbcWrapper.closeSession` ausente em método que abriu a sessão |
| `PersistenceError` de sessão em job ou listener longo | `JapeSession.close(hnd)` ausente em execução de longa duração |
| Statements vazando devagar | `NativeSql.releaseResources` ausente, ou `setReuseStatements(true)` sem fechar o `NativeSql` no `finally` |
| Falha só na segunda tentativa de uma TX com deadlock | estado mutável não recriado dentro de `doWithTx()` |

## Checklist antes do PR

1. Cada `JapeSession.open()` / `openSession()` / `new NativeSql` / `executeQuery()` / `prepareCall()` tem `finally` correspondente?
2. A ordem do `finally` vai do mais interno (`ResultSet`) para o mais externo (`SessionHandle`)?
3. Algum método fecha `JdbcWrapper` ou `SessionHandle` que recebeu por parâmetro?
4. Laço com `addParameter` chama `cleanParameters()` a cada iteração?
5. Bloco `TXBlockRedoable` recria dentro de `doWithTx()` tudo que é mutável?
