# JAPE — Padrões de Query

Formas de consultar entidades. Escolha conforme a forma do resultado e a complexidade do filtro.

## Matriz de decisão

| Cenário | API recomendada |
|---|---|
| Buscar 1 registro por PK | `EntityFacade.findEntityByPrimaryKey` |
| Lista com filtro simples | `FinderWrapper` via `findByDynamicFinderAsVO` |
| Lista com relacionamentos eager-load | `EntityQuery` fluente com `loadOnFind` |
| Filtro dinâmico construído programaticamente | `Criteria` + `FinderWrapper` |
| SQL complexo (JOIN, GROUP BY, subquery) | `NativeSql` |
| Valor único (count, sum, max) | `NativeSql.getBigDecimal`/`getString` estático |
| Stored procedure | `ProcedureCaller` |

## 1. Busca por PK

```java
EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
PersistentLocalEntity e = dwf.findEntityByPrimaryKey(
    DynamicEntityNames.TGFCAB,
    new Object[]{ nunota }  // array mesmo se a PK for simples
);
if (e == null) {
    throw new IllegalStateException("Nota não encontrada: " + nunota);
}
DynamicVO vo = (DynamicVO) e.getValueObject();
BigDecimal valor = vo.asBigDecimal("VLRNOTA");
```

PKs compostas: passe o array na ordem declarada no dicionário.

## 2. FinderWrapper — filtro simples

```java
FinderWrapper finder = new FinderWrapper(
    DynamicEntityNames.TGFCAB,
    "this.TIPMOV = ? AND this.STATUSNOTA = ? AND this.DTNEG >= ?",
    new Object[]{ "V", "L", dataInicio }
);
Collection<DynamicVO> rows = dwf.findByDynamicFinderAsVO(finder);
for (DynamicVO vo : rows) {
    // ...
}
```

- `this.` referencia campos da entidade
- `?` para parâmetros posicionais
- Terceiro argumento opcional: `orderBy` como string (ex.: `"this.NUNOTA DESC"`)
- Use `findByDynamicFinder` (sem `AsVO`) se precisa do `PersistentLocalEntity` (p.ex. para update direto)

## 3. EntityQuery fluente

```java
Collection<DynamicVO> rows = EntityQuery.build(dwf)
    .entity(DynamicEntityNames.TGFCAB)
    .where("this.TIPMOV = ? AND this.NUNOTA IN (SELECT NUNOTA FROM TGFITE WHERE CODPROD = ?)")
    .parameters(new Object[]{ "V", codProd })
    .orderBy("this.DTNEG DESC")
    .loadOnFind("this.PARCEIRO")      // carrega junto o VO de parceiro
    .loadOnFind("this.TOPVENDA")      // e o de TOP
    .list();
```

`loadOnFind` evita N+1 em navegações de relacionamento.

## 4. Criteria — construção dinâmica

```java
Criteria c = new Criteria();
c.addClause("this.ATIVO = ?", "S");
if (codEmp != null) {
    c.addClause("this.CODEMP = ?", codEmp);
}
if (dataInicio != null) {
    c.addClause("this.DTNEG >= ?", dataInicio);
}

FinderWrapper finder = new FinderWrapper(
    DynamicEntityNames.TGFCAB,
    c.getSql(),
    c.getParameters()
);
Collection<DynamicVO> rows = dwf.findByDynamicFinderAsVO(finder);
```

Vantagem: condições adicionadas conforme parâmetros não-nulos, sem ifs encadeados concatenando string SQL.

## 5. NativeSql — SQL complexo

Use quando:
- JOIN entre múltiplas tabelas
- GROUP BY, agregações
- Subqueries correlacionadas
- SQL específico de banco (CTEs, window functions)
- Performance crítica (SQL ajustado manualmente)

```java
NativeSql q = null;
try {
    q = new NativeSql(jdbc);
    q.appendSql("SELECT CAB.NUNOTA, CAB.VLRNOTA, COUNT(ITE.NUNOTA) AS QTD_ITENS ");
    q.appendSql("FROM TGFCAB CAB ");
    q.appendSql("JOIN TGFITE ITE ON ITE.NUNOTA = CAB.NUNOTA ");
    q.appendSql("WHERE CAB.TIPMOV = :TIPMOV ");
    q.appendSql("  AND CAB.DTNEG >= :DT_INI ");
    q.appendSql("GROUP BY CAB.NUNOTA, CAB.VLRNOTA ");
    q.appendSql("ORDER BY CAB.NUNOTA DESC");

    q.setNamedParameter("TIPMOV", "V");
    q.setNamedParameter("DT_INI", dataInicio);

    ResultSet rs = q.executeQuery();
    while (rs.next()) {
        BigDecimal nunota = rs.getBigDecimal("NUNOTA");
        BigDecimal vlr = rs.getBigDecimal("VLRNOTA");
        int qtd = rs.getInt("QTD_ITENS");
        // ...
    }
} finally {
    if (q != null) q.close();
}
```

## 6. Helpers estáticos para valor único

```java
BigDecimal total = (BigDecimal) NativeSql.getBigDecimal(
    jdbc, "SUM(VLRNOTA)", "TGFCAB",
    "TIPMOV = :TIP AND DTNEG >= :DT",
    new Object[]{ "V", dataInicio });
```

Formato: `(jdbc, expressão-select, tabela, where, params)`.

## 7. Scroll/Paginação

Para ResultSets grandes que precisam de navegação scrollable:

```java
q.setScrollableResult(true);
ResultSet rs = q.executeQuery();
rs.absolute(100);   // pula para a linha 100
```

ScrollableResult consome mais memória — use apenas quando necessário.

## 8. Batch para DMLs em volume

```java
NativeSql q = null;
try {
    q = new NativeSql(jdbc);
    q.setReuseStatements(true);  // OBRIGATÓRIO
    q.appendSql("UPDATE TGFITE SET CODTIPVENDA = :TIPVENDA WHERE NUNOTA = :NUNOTA");
    for (Item i : items) {
        q.setNamedParameter("TIPVENDA", i.getTipVenda());
        q.setNamedParameter("NUNOTA", i.getNunota());
        q.addBatch();
    }
    q.flushBatchTail();
} finally {
    if (q != null) q.close();
}
```

## 9. Criar e atualizar VOs

### Criar

```java
DynamicVO novo = (DynamicVO) dwf.createEmptyVO(DynamicEntityNames.MINHA);
novo.setProperty("CAMPO1", valor1);
novo.setProperty("CAMPO2", valor2);
dwf.createEntity(DynamicEntityNames.MINHA, (EntityVO) novo);
BigDecimal pkGerada = novo.asBigDecimal("ID");  // disponível após o create
```

### Atualizar

UPDATE é feito via `PersistentLocalEntity.setValueObject(vo)`. Não existe `dwf.updateEntity(...)` em `EntityFacade`.

```java
PersistentLocalEntity e = dwf.findEntityByPrimaryKey(
    DynamicEntityNames.MINHA, new Object[]{ id });
if (e == null) throw new IllegalStateException("Não encontrada");

DynamicVO vo = (DynamicVO) e.getValueObject();
vo.setProperty("CAMPO1", novoValor);
e.setValueObject((EntityVO) vo);   // flush
```

### Padrão INSERT vs UPDATE via PrePersistEntityState (Centrais)

Usado em `CACHelper`, triggers e helpers de centrais. `state.setEntity` apenas guarda a referência ao `PersistentLocalEntity` — não dispara IO. INSERT é feito por `createEntity`; UPDATE por `setValueObject`.

```java
if (state.isNew()) {
    PersistentLocalEntity entity = dwf.createEntity(
        state.getDao().getEntityName(),
        (EntityVO) state.getNewVO());   // INSERT
    state.setEntity(entity);             // guarda referência para as próximas chamadas
} else {
    state.getEntity().setValueObject(
        (EntityVO) state.getNewVO());   // UPDATE
}
```

Referência real: [CACHelper.java:1501-1506](../../../../MGECom-Model/src/br/com/sankhya/mgecomercial/model/helper/centrais/CACHelper.java).

Alternativa fluente com `EntitySaver`:
```java
EntitySaver.build(dwf)
    .entity(DynamicEntityNames.MINHA)
    .vo(vo)
    .update();   // ou .create()
```

## 10. Delete

```java
dwf.removeEntity(DynamicEntityNames.MINHA, new Object[]{ id });
```

**Não existe** `deleteEntity` em `EntityFacade` — o nome correto é `removeEntity`.

Ou, com a referência já carregada:
```java
PersistentLocalEntity e = dwf.findEntityByPrimaryKey(
    DynamicEntityNames.MINHA, new Object[]{ id });
if (e != null) e.remove();   // herdado de EJBLocalObject
```

## Dicas transversais

1. **Sempre dentro de `JapeSession.open()`** — qualquer chamada acima requer sessão ativa.
2. **DML exige TX** — `createEntity`, `setValueObject`, `removeEntity`, `executeUpdate` quebram se não houver TX ativa. Use `execWithTX` se estiver fora de contexto EJB.
3. **SELECTs funcionam sem TX** — use `execWithNoTX` para SELECTs longos que não devem manter locks.
4. **Prefira `findByDynamicFinderAsVO` a `findByDynamicFinder`** — mais leve, retorna direto os VOs sem trafegar PersistentLocalEntity.
