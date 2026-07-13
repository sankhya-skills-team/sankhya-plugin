# NativeSql — Como Utilizar de Forma Assertiva

**Classe:** `br.com.sankhya.jape.sql.NativeSql`
**Versão do Documento:** 1.0
**Data:** 2026-03-25
**Versão mínima do SankhyaOn:** 4.35b525

---

## Índice

- [Visão Geral](#visão-geral)
- [Métodos getResultSetAsCollection](#métodos-getresultsetascollection)
- [Métodos getResultSetRowAsMap](#métodos-getresultsetrowasmap)
- [Métodos getColumnsAsMap](#métodos-getcolumnsasmap)
- [Boas Práticas](#boas-práticas)
- [Tratamento de Tipos](#tratamento-de-tipos)
- [Comparação com Métodos Alternativos](#comparação-com-métodos-alternativos)
- [Observações Importantes](#observações-importantes)
- [MapUtils](#maputils---métodos-auxiliares-para-manipulação-de-maps)

---

## Visão Geral

Os métodos utilitários da classe `NativeSql` fornecem formas simplificadas de executar consultas SQL e obter os resultados como estruturas de dados Java (`Map` e `Collection`), eliminando a necessidade de manipular diretamente objetos `ResultSet`.

### Principais Benefícios

- **Simplicidade**: Reduz boilerplate code para consultas SQL simples
- **Type-Safe**: Conversão automática de tipos SQL para Java (BigDecimal, Timestamp, String)
- **Gerenciamento de Recursos**: Fechamento automático de conexões e statements
- **Flexibilidade**: Múltiplas sobrecargas para diferentes cenários de uso

---

## Métodos getResultSetAsCollection

### Descrição

Executa uma consulta SQL e retorna os resultados como uma `Collection<Map<String, Object>>`, onde cada `Map` representa uma linha do resultado e as chaves são os nomes das colunas.

### Assinaturas

```java
// 1. Sem parâmetros
public static Collection<Map<String, Object>> getResultSetAsCollection(
    String select, String from, String where) throws Exception

// 2. Com um parâmetro
public static Collection<Map<String, Object>> getResultSetAsCollection(
    String select, String from, String where, Object param) throws Exception

// 3. Com múltiplos parâmetros
public static Collection<Map<String, Object>> getResultSetAsCollection(
    String select, String from, String where, Object[] params) throws Exception

// 4. Com JdbcWrapper customizado
public static Collection<Map<String, Object>> getResultSetAsCollection(
    String select, String from, String where, Object[] params, JdbcWrapper jdbc) throws Exception

// 5. Primeira linha apenas (com JdbcWrapper)
public static Collection<Map<String, Object>> getResultSetAsCollectionFirstOnly(
    String select, String from, String where, Object[] params, JdbcWrapper jdbc) throws Exception

// 6. A partir de ResultSet existente
public static Collection<Map<String, Object>> getResultSetAsCollection(
    ResultSet rset) throws Exception

// 7. A partir de ResultSet - primeira linha apenas
public static Collection<Map<String, Object>> getResultSetAsCollectionFirstOnly(
    ResultSet rset) throws Exception
```

### Parâmetros

- **select**: Colunas a serem retornadas (Ex: "NUNOTA, SEQUENCIA, CODPROD")
- **from**: Nome da tabela (Ex: "TGFITE")
- **where**: Cláusula WHERE, ORDER BY e/ou GROUP BY (Ex: "NUNOTA = ? AND SEQUENCIA = ? ORDER BY DTALTER DESC")
- **param**: Objeto único usado como parâmetro do WHERE
- **params**: Array de objetos usados como parâmetros do WHERE (ordem deve corresponder aos `?` no SQL)
- **jdbc**: Conexão JDBC customizada (se não informado, usa EntityFacade "mge-dwf")
- **rset**: ResultSet já posicionado para conversão

### Retorno

- `Collection<Map<String, Object>>`: Lista de mapas, onde cada mapa representa uma linha
- Se não encontrar linhas, retorna uma Collection vazia (nunca null)
- Cada Map contém: chave = nome da coluna, valor = conteúdo da coluna

### Exemplos de Uso

#### Exemplo 1: Consulta com múltiplos parâmetros

```java
BigDecimal nuNota = new BigDecimal(12345);
String pendente = "S";

Collection<Map<String, Object>> itens = NativeSql.getResultSetAsCollection(
    "SEQUENCIA, CODPROD, QTDNEG, VLRUNIT",
    "TGFITE",
    "NUNOTA = ? AND PENDENTE = ? ORDER BY SEQUENCIA",
    new Object[] { nuNota, pendente }
);

for (Map<String, Object> item : itens) {
    BigDecimal seq = MapUtils.getMapValueAsBigDecimal(item, "SEQUENCIA");
    BigDecimal codProd = MapUtils.getMapValueAsBigDecimal(item, "CODPROD");
    BigDecimal qtd = MapUtils.getMapValueAsBigDecimal(item, "QTDNEG");
    BigDecimal vlr = MapUtils.getMapValueAsBigDecimal(item, "VLRUNIT");
    System.out.println("Item " + seq + ": Prod=" + codProd + ", Qtd=" + qtd + ", Vlr=" + vlr);
}
```

#### Exemplo 2: Converter ResultSet existente

```java
NativeSql query = new NativeSql(jdbc);
query.appendSql("SELECT CODPROD, DESCRPROD FROM TGFPRO WHERE ATIVO = 'S'");

ResultSet rs = null;
try {
    rs = query.executeQuery();
    Collection<Map<String, Object>> produtos = NativeSql.getResultSetAsCollection(rs);
    for (Map<String, Object> produto : produtos) {
        System.out.println("Produto: " + produto.get("CODPROD"));
    }
} finally {
    JdbcUtils.closeResultSet(rs);
    NativeSql.releaseResources(query);
}
```

---

## Métodos getResultSetRowAsMap

### Descrição

Converte a linha atual de um `ResultSet` em um `Map<String, Object>`, onde as chaves são os nomes das colunas e os valores são os conteúdos das colunas.

### Assinatura

```java
public static Map<String, Object> getResultSetRowAsMap(ResultSet rset) throws Exception
```

### Parâmetros

- **rset**: ResultSet posicionado em uma linha válida (após `rset.next()` retornar true)

### Retorno

- `Map<String, Object>`: Map contendo os dados da linha atual
- Chave: Nome da coluna; Valor: Conteúdo da coluna (com conversão automática de tipo)
- Se a coluna for NULL, o valor será null

### Conversão de Tipos

- **Number** (NUMERIC, INTEGER, etc.) → `BigDecimal`
- **Date** (DATE, TIMESTAMP) → `Timestamp` ou `Date`
- **String** (VARCHAR, CHAR) → `String`
- **Outros** → `Object` genérico

### Exemplo: Processar ResultSet linha por linha

```java
NativeSql query = new NativeSql(jdbc);
query.appendSql("SELECT NUNOTA, CODPARC, VLRNOTA FROM TGFCAB WHERE TIPMOV = 'V'");

ResultSet rs = null;
try {
    rs = query.executeQuery();
    while (rs.next()) {
        Map<String, Object> linha = NativeSql.getResultSetRowAsMap(rs);
        BigDecimal nuNota = MapUtils.getMapValueAsBigDecimal(linha, "NUNOTA");
        BigDecimal vlrNota = MapUtils.getMapValueAsBigDecimal(linha, "VLRNOTA");
        if (vlrNota.compareTo(new BigDecimal(1000)) > 0) {
            System.out.println("Nota de alto valor: " + nuNota + " - R$ " + vlrNota);
        }
    }
} finally {
    JdbcUtils.closeResultSet(rs);
    NativeSql.releaseResources(query);
}
```

---

## Métodos getColumnsAsMap

### Descrição

Executa uma consulta SQL e retorna **apenas a primeira linha** como um `Map<String, Object>`. Forma otimizada para consultas que retornarão apenas um registro.

### Assinaturas

```java
// 1. Sem parâmetros
public static Map<String, Object> getColumnsAsMap(
    String select, String from, String where) throws Exception

// 2. Com um parâmetro
public static Map<String, Object> getColumnsAsMap(
    String select, String from, String where, Object param) throws Exception

// 3. Com múltiplos parâmetros
public static Map<String, Object> getColumnsAsMap(
    String select, String from, String where, Object[] params) throws Exception

// 4. Com JdbcWrapper customizado
public static Map<String, Object> getColumnsAsMap(
    String select, String from, String where, Object[] params, JdbcWrapper jdbc) throws Exception
```

### Retorno

- `Map<String, Object>`: Map com os dados da primeira linha encontrada
- Se não encontrar nenhuma linha, retorna `Collections.emptyMap()` (Map vazio, não null)

### Exemplo: Buscar dados de um registro específico

```java
BigDecimal nuNota = new BigDecimal(12345);
BigDecimal sequencia = new BigDecimal(1);

Map<String, Object> item = NativeSql.getColumnsAsMap(
    "CODPROD, QTDNEG, VLRUNIT, VLRTOT",
    "TGFITE",
    "NUNOTA = ? AND SEQUENCIA = ?",
    new Object[] { nuNota, sequencia }
);

if (!item.isEmpty()) {
    BigDecimal codProd = MapUtils.getMapValueAsBigDecimal(item, "CODPROD");
    BigDecimal qtd = MapUtils.getMapValueAsBigDecimal(item, "QTDNEG");
    BigDecimal vlrUnit = MapUtils.getMapValueAsBigDecimal(item, "VLRUNIT");
    BigDecimal vlrTot = MapUtils.getMapValueAsBigDecimal(item, "VLRTOT");
}
```

---

## Boas Práticas

### 1. Sempre use parâmetros prepared (?), principalmente com datas — não faça concatenação

**ERRADO:**
```java
String codParc = "100";
NativeSql.getResultSetAsCollection(
    "NUNOTA, VLRNOTA", "TGFCAB",
    "CODPARC = " + codParc  // RISCO DE SQL INJECTION!
);
```

**CORRETO:**
```java
BigDecimal codParc = new BigDecimal(100);
NativeSql.getResultSetAsCollection(
    "NUNOTA, VLRNOTA", "TGFCAB",
    "CODPARC = ?", codParc
);
```

### 2. Sempre verifique se o resultado está vazio

**ERRADO:**
```java
Map<String, Object> nota = NativeSql.getColumnsAsMap("*", "TGFCAB", "NUNOTA = ?", nuNota);
BigDecimal vlrNota = MapUtils.getMapValueAsBigDecimal(nota, "VLRNOTA"); // NullPointerException!
```

**CORRETO:**
```java
Map<String, Object> nota = NativeSql.getColumnsAsMap("*", "TGFCAB", "NUNOTA = ?", nuNota);
if (!nota.isEmpty()) {
    BigDecimal vlrNota = MapUtils.getMapValueAsBigDecimal(nota, "VLRNOTA");
} else {
    throw new Exception("Nota não encontrada");
}
```

### 3. Use BigDecimal para números

**ERRADO:**
```java
int codProd = 1000;
NativeSql.getColumnsAsMap("*", "TGFPRO", "CODPROD = ?", codProd); // Pode causar problemas
```

**CORRETO:**
```java
BigDecimal codProd = new BigDecimal(1000);
NativeSql.getColumnsAsMap("*", "TGFPRO", "CODPROD = ?", codProd); // Padrão Sankhya
```

### 4. Use try-with-resources quando possível

```java
try (NativeSql query = new NativeSql(jdbc)) {
    // código...
} // Fechamento automático
```

### 5. Especifique apenas as colunas necessárias

**ERRADO:**
```java
NativeSql.getColumnsAsMap("*", "TGFCAB", "NUNOTA = ?", nuNota); // Traz todas as colunas
```

**CORRETO:**
```java
NativeSql.getColumnsAsMap("NUNOTA, CODPARC, VLRNOTA", "TGFCAB", "NUNOTA = ?", nuNota);
```

### 6. Trate valores NULL adequadamente

```java
Map<String, Object> item = NativeSql.getColumnsAsMap("CODPROD, OBSERVACAO", "TGFITE", "NUNOTA = ?", nuNota);
if (!item.isEmpty()) {
    String obs = MapUtils.getMapValueAsString(item, "OBSERVACAO");
    if (obs == null) {
        obs = "Sem observação";
    }
}
```

### 7. Use getColumnsAsMap para uma linha, getResultSetAsCollection para múltiplas

```java
// Uma linha esperada? Use getColumnsAsMap
Map<String, Object> produto = NativeSql.getColumnsAsMap("CODPROD, ATIVO, DESCRPROD, CODVOL", "TGFPRO", "CODPROD = ?", codProd);

// Múltiplas linhas? Use getResultSetAsCollection
Collection<Map<String, Object>> itens = NativeSql.getResultSetAsCollection("*", "TGFITE", "NUNOTA = ?", nuNota);
```

---

## Tratamento de Tipos

### Mapeamento Automático SQL → Java

| Tipo SQL | Tipo Java Retornado | Observações |
|---|---|---|
| NUMERIC, NUMBER, INTEGER | BigDecimal | Sempre use BigDecimal no código |
| VARCHAR, CHAR, CLOB | String | |
| DATE | Date ou Timestamp | Depende do driver JDBC |
| TIMESTAMP | Timestamp | |
| DOUBLE, FLOAT | BigDecimal | Convertido automaticamente |

### Conversão de Tipos nos Exemplos

```java
Map<String, Object> dados = NativeSql.getColumnsAsMap(
    "CODPROD, DESCRPROD, QTDNEG, DTNEG", "TGFITE", "NUNOTA = ?", nuNota
);

BigDecimal codProd = MapUtils.getMapValueAsBigDecimal(dados, "CODPROD");
BigDecimal qtd = MapUtils.getMapValueAsBigDecimal(dados, "QTDNEG");
String descricao = MapUtils.getMapValueAsString(dados, "DESCRPROD");
Timestamp dtNeg = MapUtils.getMapValueAsTimestamp(dados, "DTNEG");

// Verificar tipo em runtime se necessário
Object valor = dados.get("ALGUMA_COLUNA");
if (valor instanceof BigDecimal) {
    BigDecimal numero = (BigDecimal) valor;
} else if (valor instanceof String) {
    String texto = (String) valor;
}
```

---

## Comparação com Métodos Alternativos

### getColumnsAsMap vs getString/getBigDecimal

**getColumnsAsMap (múltiplas colunas — 1 consulta ao banco):**
```java
Map<String, Object> dados = NativeSql.getColumnsAsMap(
    "CODPROD, DESCRPROD, ATIVO", "TGFPRO", "CODPROD = ?", codProd
);
BigDecimal cod = MapUtils.getMapValueAsBigDecimal(dados, "CODPROD");
String descr = MapUtils.getMapValueAsString(dados, "DESCRPROD");
String ativo = MapUtils.getMapValueAsString(dados, "ATIVO");
```

**getString/getBigDecimal (uma coluna por vez — 3 consultas ao banco):**
```java
BigDecimal cod = NativeSql.getBigDecimal("CODPROD", "TGFPRO", "CODPROD = ?", codProd);
String descr = NativeSql.getString("DESCRPROD", "TGFPRO", "CODPROD = ?", codProd);
String ativo = NativeSql.getString("ATIVO", "TGFPRO", "CODPROD = ?", codProd);
```

**Recomendação:** Use `getColumnsAsMap` quando precisar de múltiplas colunas (evita múltiplas consultas ao banco).

---

## Observações Importantes

1. **Parâmetros Nomeados**: Os parâmetros nomeados (`:PARAM`) são automaticamente substituídos por `?`. **Prefira usar sempre `?` diretamente**.
2. **Gerenciamento de Sessão**: Os métodos estáticos gerenciam automaticamente a abertura e fechamento da sessão JDBC quando necessário.
3. **Performance**: Para consultas que retornam muitas linhas, considere usar `NativeSql` com `ResultSet` diretamente e processar linha por linha ao invés de carregar tudo em memória.
4. **Thread-Safety**: Os métodos estáticos NÃO são thread-safe por si só. Cada thread deve ter sua própria instância de `JdbcWrapper`.
5. **Encoding**: Os arquivos Java no projeto podem estar em cp1252 (Windows-1252). Evite caracteres especiais em strings SQL.

---

## MapUtils — Métodos Auxiliares para Manipulação de Maps

**Classe:** `com.sankhya.util.MapUtils`
**Módulo:** SankhyaUtil

Fornece métodos auxiliares para trabalhar com `Map<String, Object>` retornados por consultas SQL, especialmente úteis em conjunto com `NativeSql.getResultSetAsCollection()` e `NativeSql.getColumnsAsMap()`.

### getMapValueAsBigDecimal

```java
public static BigDecimal getMapValueAsBigDecimal(Map<String, Object> map, String key)
```

- **Retorno:** `BigDecimal` ou `null` se a chave não existir ou o valor for null

### getMapValueAsTimestamp

```java
public static Timestamp getMapValueAsTimestamp(Map<String, Object> map, String key)
```

- **Retorno:** `Timestamp` ou `null` se a chave não existir ou o valor for null

### getMapValueAsString

```java
public static String getMapValueAsString(Map<String, Object> map, String key)
```

- **Retorno:** `String` ou `null` se a chave não existir ou o valor for null

### Exemplo de Uso Combinado

```java
BigDecimal nuNota = new BigDecimal(12345);

Map<String, Object> nota = NativeSql.getColumnsAsMap(
    "NUNOTA, CODPARC, VLRNOTA, DTNEG, STATUSNOTA",
    "TGFCAB", "NUNOTA = ?", nuNota
);

// Forma tradicional (cast manual)
BigDecimal vlrNota1 = (BigDecimal) nota.get("VLRNOTA");

// Forma com MapUtils (mais segura)
BigDecimal vlrNota2 = MapUtils.getMapValueAsBigDecimal(nota, "VLRNOTA");
BigDecimal codParc = MapUtils.getMapValueAsBigDecimal(nota, "CODPARC");
String statusnota = MapUtils.getMapValueAsString(nota, "STATUSNOTA");
Timestamp dtNeg = MapUtils.getMapValueAsTimestamp(nota, "DTNEG");

if (vlrNota2 != null && vlrNota2.compareTo(new BigDecimal(1000)) > 0) {
    System.out.println("Nota de alto valor: " + vlrNota2);
}
```

### Limitações

1. **ClassCastException**: Os métodos ainda podem lançar `ClassCastException` se o valor no Map não for do tipo esperado.
2. **Não converte tipos**: Os métodos fazem cast, não conversão. Se você tem uma String "123" e chama `getMapValueAsBigDecimal()`, vai lançar exceção.
3. **Retorna null para chave inexistente**: Não distingue entre "chave não existe" e "chave existe com valor null".

---

## Padrão Real — SQL em Arquivo Externo com loadSql

> Este é o padrão recomendado para queries complexas. Mantém o SQL fora do Java, facilita manutenção e permite syntax highlighting no editor.

### Estrutura de diretórios

```
model/src/main/resources/
└── scriptsSql/
    ├── processaDados.sql
    ├── cabecalho/
    │   ├── buscaCabecalhoPorContrato.sql
    │   └── buscaCabecalhoPorDespesa.sql
    └── impostos/
        └── buscaImpostos.sql
```

### Como carregar e executar

```java
// O JdbcWrapper é obtido de EntityFacadeFactory e passado como parâmetro
EntityFacade ef = EntityFacadeFactory.getDWFFacade();
JdbcWrapper jdbc = ef.getJdbcWrapper();

try (NativeSql ns = new NativeSql(jdbc)) {
    // Carrega o SQL do classpath — o primeiro argumento é qualquer classe do mesmo módulo
    ns.loadSql(MinhaClasse.class, "/scriptsSql/cabecalho/buscaCabecalhoPorContrato.sql");

    // Parâmetros nomeados — correspondem a :NOME no arquivo SQL
    ns.setNamedParameter("REFERENCIA",  referencia);   // Timestamp
    ns.setNamedParameter("TIPREGISTRO", tipRegistro);  // String
    ns.setNamedParameter("NUMCONTRATO", numContrato);  // BigDecimal (aceita null)
    ns.setNamedParameter("CODFUNC",     codFunc);      // BigDecimal (aceita null)

    try (ResultSet rs = ns.executeQuery()) {
        while (rs.next()) {
            BigDecimal numContrato = rs.getBigDecimal("NUMCONTRATO");
            String tipRegistro    = rs.getString("TIPREGISTRO");
            Timestamp referencia  = rs.getTimestamp("REFERENCIA");
            // ...
        }
    }
}
```

### Arquivo SQL com parâmetros nomeados e filtros opcionais

```sql
-- /scriptsSql/cabecalho/buscaCabecalhoPorContrato.sql
SELECT DISTINCT
    CON.NUMCONTRATO,
    REG.CODEMP,
    REG.TIPREGISTRO,
    CON.CODPARC,
    REG.REFERENCIA
  FROM MINHA_TABELA_PRINCIPAL REG
  JOIN MINHA_TABELA_DETALHE DET ON REG.CODFUNC = DET.CODFUNC
  JOIN MINHA_TABELA_VINCULO VIN ON DET.CODDEP  = VIN.CODDEP
  JOIN MINHA_TABELA_CONTRATO CON ON VIN.NUMCONTRATO = CON.NUMCONTRATO
 WHERE REG.REFERENCIA  = :REFERENCIA
   AND REG.TIPREGISTRO = :TIPREGISTRO
   AND (:NUMCONTRATO IS NULL OR CON.NUMCONTRATO = :NUMCONTRATO)
   AND (:CODFUNC     IS NULL OR REG.CODFUNC     = :CODFUNC)
```

> Parâmetros opcionais usam o padrão `(:PARAM IS NULL OR CAMPO = :PARAM)` — quando `null` é passado via `setNamedParameter`, o filtro é ignorado automaticamente.

### DELETE com NativeSql

```java
try (NativeSql del = new NativeSql(jdbc)) {
    del.appendSql("DELETE FROM MINHA_TABELA WHERE CODREGISTRO = :CODREGISTRO");
    del.setNamedParameter("CODREGISTRO", codRegistro);
    del.executeUpdate();
}
```

### Gerenciamento de sessão JDBC

Quando o `JdbcWrapper` é obtido de `EntityFacadeFactory`, a sessão deve ser aberta e fechada manualmente:

```java
EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
JdbcWrapper jdbc = dwf.getJdbcWrapper();
jdbc.openSession();
try {
    // operações com NativeSql usando este jdbc
} finally {
    JdbcWrapper.closeSession(jdbc);
}
```

Quando o `JdbcWrapper` vem de um evento (`event.getJdbcWrapper()`), **não abrir nem fechar** — o ciclo de vida é gerenciado pelo framework.

### Passando JdbcWrapper entre classes

Para compartilhar a mesma conexão entre múltiplas classes dentro de uma operação:

```java
// Na classe orquestradora
public void processar(BigDecimal codRegistro, JdbcWrapper jdbc) throws Exception {
    try (NativeSql ns = new NativeSql(jdbc)) {
        ns.loadSql(getClass(), "/scriptsSql/processaDados.sql");
        ns.setNamedParameter("CODREGISTRO", codRegistro);
        try (ResultSet rs = ns.executeQuery()) {
            while (rs.next()) {
                // processar linha
            }
        }
    }
}
```

> Passar `JdbcWrapper` como parâmetro garante que todas as operações participem da mesma transação e evita abrir múltiplas conexões desnecessárias.

### Observação sobre parâmetros nomeados

A documentação oficial menciona preferir `?` direto, mas na prática dos projetos reais o padrão `:NOME` com `setNamedParameter` é amplamente usado — especialmente com arquivos SQL externos, onde os nomes tornam o SQL mais legível e a ordem dos parâmetros não importa.

---

## SQL Inline com appendSql

Para queries simples ou dinâmicas que não justificam um arquivo externo, use `appendSql`:

```java
try (NativeSql sql = new NativeSql(jdbc)) {
    sql.appendSql(
        "SELECT COUNT(1) AS QTD " +
        "FROM MINHA_TABELA_ITEM ITM " +
        "JOIN MINHA_TABELA_CAB CAB ON ITM.CODREGISTRO = CAB.CODREGISTRO " +
        "WHERE CAB.REFERENCIA  = :REFERENCIA " +
        "  AND CAB.NUMCONTRATO = :NUMCONTRATO " +
        "  AND CAB.STATUS     <> 'C' " +
        "  AND CAB.CODREGISTRO <> :CODREGISTRO " +
        "  AND ITM.CODFUNC     = :CODFUNC"
    );
    sql.setNamedParameter("REFERENCIA",   referencia);
    sql.setNamedParameter("NUMCONTRATO",  numContrato);
    sql.setNamedParameter("CODREGISTRO",  codRegistro);
    sql.setNamedParameter("CODFUNC",      codFunc);

    try (ResultSet rs = sql.executeQuery()) {
        if (rs.next()) {
            return rs.getInt("QTD") > 0;
        }
    }
}
```

---

## SQL Dinâmico com IN Clause e Chunking (Oracle)

O Oracle limita cláusulas `IN` a 1000 elementos. Para listas maiores, processe em chunks e agregue os resultados:

```java
private static final int ORACLE_IN_LIMIT = 1000;

public Map<BigDecimal, BigDecimal> buscarPercentuais(List<BigDecimal> ids) throws Exception {
    Map<BigDecimal, BigDecimal> resultado = new LinkedHashMap<>();
    if (ids == null || ids.isEmpty()) return resultado;

    JdbcWrapper jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
    try {
        jdbc.openSession();

        int from = 0;
        while (from < ids.size()) {
            int to = Math.min(from + ORACLE_IN_LIMIT, ids.size());
            List<BigDecimal> slice = ids.subList(from, to);

            // Monta placeholders dinâmicos: :p0, :p1, :p2, ...
            String finalSql = buildSqlComIn(slice);
            NativeSql exec = new NativeSql(jdbc).appendSql(finalSql);
            for (int i = 0; i < slice.size(); i++) {
                exec.setNamedParameter("p" + i, slice.get(i));
            }

            try (ResultSet rs = exec.executeQuery()) {
                while (rs.next()) {
                    BigDecimal codCR = rs.getBigDecimal("CODCENCUS");
                    BigDecimal perc  = rs.getBigDecimal("PERCENTUAL");
                    if (codCR == null || perc == null) continue;
                    // Agrega resultados de múltiplos chunks
                    BigDecimal atual = resultado.get(codCR);
                    resultado.put(codCR, atual == null ? perc : atual.add(perc));
                }
            }
            from = to;
        }
    } finally {
        JdbcWrapper.closeSession(jdbc);
    }
    return resultado;
}

// Lê o SQL do arquivo e substitui o marcador :IDS pelos placeholders dinâmicos
private String buildSqlComIn(List<BigDecimal> slice) throws Exception {
    String raw = lerRecurso("/scriptsSql/meuQuery.sql");
    StringBuilder ph = new StringBuilder();
    for (int i = 0; i < slice.size(); i++) {
        if (i > 0) ph.append(", ");
        ph.append(":p").append(i);
    }
    return raw.replace(":IDS", ph.toString());
}

// Lê arquivo SQL do classpath como String
private String lerRecurso(String path) throws Exception {
    InputStream in = getClass().getResourceAsStream(path);
    if (in == null) throw new IllegalStateException("SQL nao encontrado: " + path);
    StringBuilder sb = new StringBuilder();
    char[] buf = new char[4096];
    int n;
    try (Reader r = new InputStreamReader(in, StandardCharsets.UTF_8)) {
        while ((n = r.read(buf)) != -1) sb.append(buf, 0, n);
    }
    return sb.toString();
}
```

**Arquivo SQL com marcador substituível:**
```sql
-- /scriptsSql/meuQuery.sql
SELECT CODCENCUS, SUM(PERCENTUAL) AS PERCENTUAL
  FROM MINHA_TABELA_RATEIO
 WHERE CODREGISTRO IN (:IDS)
 GROUP BY CODCENCUS
```

> O marcador `:IDS` no arquivo SQL é substituído em tempo de execução pelos placeholders `:p0, :p1, ...` antes de passar para o `NativeSql`. Isso contorna a limitação do Oracle de 1000 elementos no `IN`.

---

## Referências

### NativeSql
- Classe: `br.com.sankhya.jape.sql.NativeSql`
- Módulo: JAPE (Java Persistence Engine)
- Ver também: `NativeSql.getBigDecimal()`, `NativeSql.getString()`, `NativeSql.getTimestamp()`, `JdbcWrapper`, `EntityFacade`

### MapUtils
- Classe: `com.sankhya.util.MapUtils`
- Módulo: SankhyaUtil
- Métodos: `getMapValueAsBigDecimal()`, `getMapValueAsTimestamp()`, `getMapValueAsString()`

