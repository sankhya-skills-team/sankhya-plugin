# NativeSql — Uso Assertivo no Repository

## Prioridade de Acesso a Dados

Antes de usar `NativeSql`, verifique se o JAPE resolve:

| API | Usar quando |
|---|---|
| `JapeFactory` | CRUD por PK, insert, update, delete em uma entidade |
| `DwfUtils.findEntitysAsVO` | Busca com filtro simples em uma entidade |
| `EntityFacade / FinderWrapper` | Filtros compostos, múltiplos critérios em uma entidade |
| **`NativeSql`** | **JOIN entre entidades sem relacionamento JAPE, GROUP BY, subconsultas, funções de agregação, queries que precisam contornar eventos** |

**Regra:** JAPE dispara eventos Sankhya (INSERT/UPDATE/DELETE via JAPE acionam `EventoProgramavelJava`). `NativeSql` / `JdbcWrapper` **não disparam eventos**. Use isso a favor — nunca como atalho para "economizar código".

Para o ciclo de vida completo do `JdbcWrapper` (como abrir, fechar, regra dentro de evento), ver `references/acesso-dados.md`.

---

## Métodos Utilitários — Quando Usar Cada Um

| Método | Retorno | Quando usar |
|---|---|---|
| `getResultSetAsCollection` | `Collection<Map<String, Object>>` | Múltiplas linhas esperadas |
| `getColumnsAsMap` | `Map<String, Object>` (primeira linha) | Exatamente uma linha esperada |
| `getResultSetRowAsMap` | `Map<String, Object>` (linha atual do RS) | Processamento linha por linha com lógica intermediária |

---

## getResultSetAsCollection — Múltiplas Linhas

### Assinaturas principais

```java
// Sem parâmetros
Collection<Map<String, Object>> NativeSql.getResultSetAsCollection(
    String select, String from, String where) throws Exception

// Com um parâmetro
Collection<Map<String, Object>> NativeSql.getResultSetAsCollection(
    String select, String from, String where, Object param) throws Exception

// Com múltiplos parâmetros
Collection<Map<String, Object>> NativeSql.getResultSetAsCollection(
    String select, String from, String where, Object[] params) throws Exception

// Com JdbcWrapper explícito (padrão no repository/)
Collection<Map<String, Object>> NativeSql.getResultSetAsCollection(
    String select, String from, String where, Object[] params, JdbcWrapper jdbc) throws Exception
```

> Retorna `Collection` vazia quando nenhuma linha é encontrada — nunca `null`.

### Exemplo — itens de uma nota com JOIN

```java
public List<ItemNotaDto> buscarItensParaProcessamento(BigDecimal nuNota, JdbcWrapper jdbc)
        throws Exception {
    Collection<Map<String, Object>> linhas = NativeSql.getResultSetAsCollection(
        "i.SEQUENCIA, i.CODPROD, i.QTDNEG, i.VLRUNIT, p.DESCRPROD",
        "TGFITE i JOIN TGFPRO p ON p.CODPROD = i.CODPROD",
        "i.NUNOTA = ? AND i.QTDNEG > 0 ORDER BY i.SEQUENCIA",
        new Object[] { nuNota },
        jdbc
    );

    List<ItemNotaDto> itens = new ArrayList<>();
    for (Map<String, Object> linha : linhas) {
        itens.add(new ItemNotaDto(
            MapUtils.getMapValueAsBigDecimal(linha, "SEQUENCIA"),
            MapUtils.getMapValueAsBigDecimal(linha, "CODPROD"),
            MapUtils.getMapValueAsString(linha, "DESCRPROD"),
            MapUtils.getMapValueAsBigDecimal(linha, "QTDNEG"),
            MapUtils.getMapValueAsBigDecimal(linha, "VLRUNIT")
        ));
    }
    return itens;
}
```

---

## getColumnsAsMap — Uma Linha

### Assinaturas principais

```java
// Com parâmetro único
Map<String, Object> NativeSql.getColumnsAsMap(
    String select, String from, String where, Object param) throws Exception

// Com múltiplos parâmetros
Map<String, Object> NativeSql.getColumnsAsMap(
    String select, String from, String where, Object[] params) throws Exception

// Com JdbcWrapper explícito
Map<String, Object> NativeSql.getColumnsAsMap(
    String select, String from, String where, Object[] params, JdbcWrapper jdbc) throws Exception
```

> Retorna `Collections.emptyMap()` quando nenhuma linha é encontrada — **nunca null**. Verificar com `!mapa.isEmpty()`.

### Exemplo — total agregado por nota

```java
public BigDecimal calcularTotalPendente(BigDecimal nuNota, JdbcWrapper jdbc)
        throws Exception {
    Map<String, Object> resultado = NativeSql.getColumnsAsMap(
        "SUM(VLRTOT) AS TOTAL_PENDENTE",
        "TGFITE",
        "NUNOTA = ? AND STATUS = 'P'",
        new Object[] { nuNota },
        jdbc
    );

    if (resultado.isEmpty()) return BigDecimal.ZERO;
    BigDecimal total = MapUtils.getMapValueAsBigDecimal(resultado, "TOTAL_PENDENTE");
    return total != null ? total : BigDecimal.ZERO;
}
```

### getColumnsAsMap vs. múltiplos getString/getBigDecimal

```java
// RUIM — 3 viagens ao banco para o mesmo registro
BigDecimal codProd = NativeSql.getBigDecimal("CODPROD", "TGFPRO", "CODPROD = ?", id);
String descr       = NativeSql.getString("DESCRPROD", "TGFPRO", "CODPROD = ?", id);
String ativo       = NativeSql.getString("ATIVO", "TGFPRO", "CODPROD = ?", id);

// BOM — 1 viagem ao banco
Map<String, Object> prod = NativeSql.getColumnsAsMap(
    "CODPROD, DESCRPROD, ATIVO", "TGFPRO", "CODPROD = ?", id
);
BigDecimal codProd = MapUtils.getMapValueAsBigDecimal(prod, "CODPROD");
String descr       = MapUtils.getMapValueAsString(prod, "DESCRPROD");
String ativo       = MapUtils.getMapValueAsString(prod, "ATIVO");
```

---

## getResultSetRowAsMap — Linha por Linha com Lógica Intermediária

Use quando precisar tomar decisão por linha durante a iteração (ex: parar ao encontrar condição, acumular seletivamente).

```java
NativeSql query = new NativeSql(jdbc);
query.appendSql(
    "SELECT NUNOTA, CODPARC, VLRNOTA " +
    "FROM TGFCAB " +
    "WHERE TIPMOV = 'V' AND DTNEG >= :REFERENCIA"
);
query.setNamedParameter("REFERENCIA", referencia);

ResultSet rs = null;
try {
    rs = query.executeQuery();
    while (rs.next()) {
        Map<String, Object> linha = NativeSql.getResultSetRowAsMap(rs);
        BigDecimal vlrNota = MapUtils.getMapValueAsBigDecimal(linha, "VLRNOTA");
        if (BigDecimalUtil.isNullOrZero(vlrNota)) continue;
        // processar linha...
    }
} finally {
    JdbcUtils.closeResultSet(rs);
    NativeSql.releaseResources(query);
}
```

---

## MapUtils — Extração Tipada de Maps

**Classe:** `com.sankhya.util.MapUtils`

| Método | Retorno | Tipo SQL mapeado |
|---|---|---|
| `getMapValueAsBigDecimal(map, "CAMPO")` | `BigDecimal` ou `null` | NUMERIC, NUMBER, INTEGER |
| `getMapValueAsString(map, "CAMPO")` | `String` ou `null` | VARCHAR, CHAR |
| `getMapValueAsTimestamp(map, "CAMPO")` | `Timestamp` ou `null` | DATE, TIMESTAMP |

> Todos retornam `null` quando a chave não existe **ou** o valor é `null` no banco — não distingue os dois casos.

```java
Map<String, Object> dados = NativeSql.getColumnsAsMap(
    "NUNOTA, CODPARC, VLRNOTA, DTNEG",
    "TGFCAB", "NUNOTA = ?", nuNota
);

if (!dados.isEmpty()) {
    BigDecimal vlrNota  = MapUtils.getMapValueAsBigDecimal(dados, "VLRNOTA");
    BigDecimal codParc  = MapUtils.getMapValueAsBigDecimal(dados, "CODPARC");
    Timestamp dtNeg     = MapUtils.getMapValueAsTimestamp(dados, "DTNEG");
    // vlrNota pode ser null se o campo for nulo no banco — verificar antes de usar
}
```

---

## SQL Inline com appendSql

Para queries simples que não justificam arquivo `.sql` externo:

```java
NativeSql sql = new NativeSql(jdbc);
sql.appendSql(
    "SELECT COUNT(1) AS QTD " +
    "FROM AD_MINHATAB t " +
    "JOIN TGFCAB c ON c.NUNOTA = t.NUNOTA " +
    "WHERE c.CODEMP      = :CODEMP " +
    "  AND t.STATUS     <> 'C' " +
    "  AND t.DTPROCESSO >= :REFERENCIA"
);
sql.setNamedParameter("CODEMP",     codEmp);
sql.setNamedParameter("REFERENCIA", referencia);

ResultSet rs = null;
try {
    rs = sql.executeQuery();
    if (rs.next()) {
        return rs.getInt("QTD") > 0;
    }
    return false;
} finally {
    JdbcUtils.closeResultSet(rs);
    NativeSql.releaseResources(sql);
}
```

### Parâmetros nomeados vs. `?`

| Estilo | Quando usar |
|---|---|
| `:NOME` com `setNamedParameter` | SQL em arquivo externo ou inline com múltiplos parâmetros — mais legível, ordem não importa |
| `?` com array `Object[]` | `getResultSetAsCollection` / `getColumnsAsMap` estáticos — os métodos utilitários só aceitam `?` |

---

## IN Clause com Chunking — Limite Oracle de 1000 Elementos

Oracle rejeita `IN` com mais de 1000 elementos. Para listas maiores, processar em chunks e agregar resultados:

```java
private static final int ORACLE_IN_LIMIT = 1000;

public Map<BigDecimal, BigDecimal> buscarPercentuais(List<BigDecimal> ids, JdbcWrapper jdbc)
        throws Exception {
    Map<BigDecimal, BigDecimal> resultado = new LinkedHashMap<>();
    if (ids == null || ids.isEmpty()) return resultado;

    int from = 0;
    while (from < ids.size()) {
        int to = Math.min(from + ORACLE_IN_LIMIT, ids.size());
        List<BigDecimal> fatia = ids.subList(from, to);

        String sql = montarSqlComIn(fatia);
        NativeSql exec = new NativeSql(jdbc);
        exec.appendSql(sql);
        for (int i = 0; i < fatia.size(); i++) {
            exec.setNamedParameter("p" + i, fatia.get(i));
        }

        ResultSet rs = null;
        try {
            rs = exec.executeQuery();
            while (rs.next()) {
                BigDecimal codCR = rs.getBigDecimal("CODCENCUS");
                BigDecimal perc  = rs.getBigDecimal("PERCENTUAL");
                if (codCR == null || perc == null) continue;
                BigDecimal atual = resultado.get(codCR);
                resultado.put(codCR, atual == null ? perc : atual.add(perc));
            }
        } finally {
            JdbcUtils.closeResultSet(rs);
            NativeSql.releaseResources(exec);
        }
        from = to;
    }
    return resultado;
}

private String montarSqlComIn(List<BigDecimal> fatia) {
    StringBuilder placeholders = new StringBuilder();
    for (int i = 0; i < fatia.size(); i++) {
        if (i > 0) placeholders.append(", ");
        placeholders.append(":p").append(i);
    }
    return
        "SELECT CODCENCUS, SUM(PERCENTUAL) AS PERCENTUAL " +
        "FROM AD_RATEIO " +
        "WHERE CODREGISTRO IN (" + placeholders + ") " +
        "GROUP BY CODCENCUS";
}
```

---

## Boas Práticas

**Especifique apenas as colunas necessárias** — nunca `SELECT *` em produção.

```java
// RUIM
NativeSql.getColumnsAsMap("*", "TGFCAB", "NUNOTA = ?", nuNota);

// BOM
NativeSql.getColumnsAsMap("NUNOTA, CODPARC, VLRNOTA", "TGFCAB", "NUNOTA = ?", nuNota);
```

**Sempre use parâmetros `?` ou `:NOME`** — nunca concatenação de strings (SQL injection).

```java
// RUIM
NativeSql.getResultSetAsCollection("NUNOTA", "TGFCAB", "CODPARC = " + codParc);

// BOM
NativeSql.getResultSetAsCollection("NUNOTA", "TGFCAB", "CODPARC = ?", codParc);
```

**Verifique resultado vazio antes de acessar.**

```java
Map<String, Object> nota = NativeSql.getColumnsAsMap("VLRNOTA", "TGFCAB", "NUNOTA = ?", nuNota);
if (nota.isEmpty()) throw NomeDemandaException.naoEncontrado("Nota", nuNota);
BigDecimal vlrNota = MapUtils.getMapValueAsBigDecimal(nota, "VLRNOTA");
```

**Use `BigDecimal` para IDs e valores numéricos** — `int` pode causar falha no bind Oracle.

```java
// RUIM
NativeSql.getColumnsAsMap("*", "TGFPRO", "CODPROD = ?", 1000);

// BOM
NativeSql.getColumnsAsMap("CODPROD, DESCRPROD", "TGFPRO", "CODPROD = ?", new BigDecimal(1000));
```

**Para queries complexas com muitos parâmetros** — preferir arquivo `.sql` externo (ver `references/acesso-dados.md`).
