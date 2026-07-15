---
name: sankhya-jape
description: Use quando for escrever, modificar ou revisar código Java que acessa banco de dados no Sankhya OM (JapeSession, NativeSql, EntityFacade, DynamicVO, JdbcWrapper, EntityDAO, execWithTX, transações autônomas ou fake, macros portáveis Oracle/SQL Server, BigDecimal em SQL). Invocar sempre que houver open/close de sessão JAPE, parâmetros nomeados (:nome), DML manual, chamada de stored procedure via ProcedureCaller, Criteria, EntityQuery ou manipulação de Value Objects dinâmicos.
---

# JAPE — Persistência Sankhya OM

O JAPE é o framework de persistência proprietário do Sankhya OM, classificado como **"NEVER modify"** no CLAUDE.md. Esta skill cobre como *consumir* a API corretamente — não como alterar o framework.

## Quando usar

- Abertura/fechamento de `JapeSession`
- Execução de `NativeSql` (SELECT/DML/batch)
- CRUD de entidades via `EntityFacade` ou `EntityQuery`/`EntitySaver`
- Manipulação de `DynamicVO`
- Transações manuais (`execWithTX`, `execWithAutonomousTX`, `execWithAutonomousFakeTX`, `execWithNoTX`)
- Chamada de stored procedures (`ProcedureCaller`)
- Uso de macros SQL portáveis (Oracle/SQL Server)
- Qualquer manipulação de `BigDecimal` destinado a SQL

## Regras inegociáveis

1. **BigDecimal compareTo, nunca equals** — `a.equals(b)` retorna false para `1` vs `1.00` por diferença de scale. Sempre `a.compareTo(b) == 0`.
2. **BigDecimal toPlainString em SQL** — `toString()` pode emitir notação científica (ex.: `1E+2`), quebrando o parse do Oracle. Sempre `.toPlainString()` ao concatenar em SQL literal.
3. **Toda abertura de recurso JDBC precisa de liberação em finally** — `hnd = JapeSession.open(); try {...} finally { JapeSession.close(hnd); }` para sessão; `JdbcUtils.closeResultSet(rs)` + `NativeSql.releaseResources(q)` para `NativeSql` que expõe `ResultSet`. Close fora de `finally` gera vazamento de conexão JDBC.
4. **Não compartilhe JapeSession entre threads** — a sessão é ThreadLocal. Se precisa rodar em outra thread, use `execWithAutonomousTX` ou abra nova sessão na thread alvo.
5. **Chamadas aninhadas de `open()` são seguras** — o framework empilha handles; a sessão real só fecha quando o handle raiz (`canClose=true`) é fechado.
6. **Parâmetro nomeado não fornecido lança IllegalStateException** — se o SQL contém `:CODPRN` e você não chamou `setNamedParameter("CODPRN", ...)`, a execução quebra. Use `setFillNamedParametersWithNull(true)` para construção dinâmica de queries opcionais.
7. **`addBatch()` exige `setReuseStatements(true)`** — caso contrário lança exceção no flush.
8. **Macros: não aninhe macro dentro de macro** — o `MacroTranslator` não é recursivo. Use SQL nativo ou decomponha.
9. **Não use `System.out` para log** — o próprio JAPE tem esse antipattern no `logNamedParameters`; não replique. Use o logger do módulo.
10. **ISO-8859-1 é o encoding do projeto** — strings literais com acentos em Java seguem ISO-8859-1, não UTF-8.

## Fluxo típico — leitura simples

```java
SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
    Collection<DynamicVO> rows = dwf.findByDynamicFinderAsVO(
        new FinderWrapper(DynamicEntityNames.ACAO_AGENDADA,
                          "this.ATIVO = 'S' AND this.CODMODULO = ?",
                          new Object[]{ codModulo }));
    // processar rows
} catch (Exception e) {
    throw new IllegalStateException(e);
} finally {
    JapeSession.close(hnd);
}
```

## Fluxo típico — NativeSql com parâmetros nomeados

```java
import com.sankhya.util.JdbcUtils;
import br.com.sankhya.jape.sql.NativeSql;

JdbcWrapper jdbc = // injetado ou obtido via ProcedureCaller/EntityFacade
NativeSql query = null;
ResultSet rs = null;
try {
    query = new NativeSql(jdbc);
    query.appendSql("SELECT CONFIG FROM TWFCRD WHERE CODPRN = :CODPRN AND NOMEVIEW = :NOMEVIEW");
    query.setNamedParameter("CODPRN", codprn);       // BigDecimal
    query.setNamedParameter("NOMEVIEW", nomeView);    // String
    rs = query.executeQuery();
    if (rs.next()) {
        // ler rs
    }
} finally {
    JdbcUtils.closeResultSet(rs);
    NativeSql.releaseResources(query);
}
```

## Fluxo típico — DML com transação manual

```java
SessionHandle hnd = JapeSession.open();
try {
    hnd.execWithTX(new JapeSession.TXBody() {
        public void doWithTx() throws Exception {
            EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
            DynamicVO vo = (DynamicVO) dwf.createEmptyVO(DynamicEntityNames.MINHA_ENTIDADE);
            vo.setProperty("CAMPO", valor);
            dwf.createEntity(DynamicEntityNames.MINHA_ENTIDADE, (EntityVO) vo);
        }
    });
} finally {
    JapeSession.close(hnd);
}
```

## Leituras detalhadas (sob demanda)

Quando o contexto exigir profundidade, leia apenas o que for relevante:

- Regras "NUNCA faça" e armadilhas: [reference/gotchas.md](reference/gotchas.md)
- Catálogo completo de APIs (JapeSession, NativeSql, EntityFacade, EntityQuery, EntitySaver, DynamicVO, ProcedureCaller): [reference/api-cheatsheet.md](reference/api-cheatsheet.md)
- Transações (TXBody, autônomas, fake, sem TX, deadlock retry): [reference/transactions.md](reference/transactions.md)
- Catálogo de macros portáveis Oracle vs SQL Server: [reference/macros.md](reference/macros.md)
- Padrões de Criteria e EntityQuery fluente: [reference/queries.md](reference/queries.md)
- Cache L2 de leitura em memória (`InMemoryDataSet`, invalidação por tabela observada): [reference/inmemory-dataset.md](reference/inmemory-dataset.md)
- Listeners de persistência — contrato/API, eventos do ciclo de vida, `getModifingFields`/`getJdbcWrapper`: [reference/listeners.md](reference/listeners.md)

## O que NÃO fazer

- Não modifique arquivos em `JAPE/` — módulo marcado como intocável.
- Não sugira upgrade de versão do JAPE — é proprietário, sem release externo.
- Não troque JAPE por outro ORM (Hibernate, JPA puro, MyBatis) em escopo de task — é mudança arquitetural macro fora de escopo de feature/fix.
- Não use `EasySQL` em código novo — legado com `maxRows=100` hardcoded e fechamento de conexão no `close()`, comportamento inconsistente com `NativeSql`.
- Não use `System.out.println` para debug de SQL — use o `JDBCSpy` ou o logger do módulo.
