# SQLUtils

**Pacote:** `com.sankhya.util.SQLUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.SQLUtils;
```

> **Atenção:** todos os métodos de IN/NOT IN recebem o **nome da coluna** como primeiro parâmetro.
> O resultado já inclui `COLUNA IN (valores)` — pronto para concatenar no WHERE.

---

## Cláusulas IN dinâmicas

```java
import java.util.Arrays;
import java.util.List;

List<Long> ids = Arrays.asList(1L, 2L, 3L);

// Gera: "NUNOTA IN (1,2,3)"
String inNums = SQLUtils.buildINClauseByValues("NUNOTA", ids);

// Gera: "CODPARC IN ('CLI001','CLI002')"
String inStr = SQLUtils.buildINClauseByValuesWithQuotes("CODPARC",
                   Arrays.asList("CLI001", "CLI002"));

// NOT IN numérico
String notIn = SQLUtils.buildNOTINClauseByValues("NUNOTA", ids);

// IN a partir de String CSV (ex: "1,2,3")
String inCsv = SQLUtils.buildINClauseByValues("NUNOTA", "1,2,3");

// NOT IN a partir de String CSV
String notInCsv = SQLUtils.buildNOTINClauseByValues("NUNOTA", "1,2,3");
```

### Uso típico no WHERE

```java
String sql = "SELECT NUNOTA, NUMNOTA FROM TGFCAB WHERE "
           + SQLUtils.buildINClauseByValues("NUNOTA", listaNotas);
```

---

## IN com controle de batch (Oracle: limite 1000 por cláusula)

```java
// Gera ORs automáticos quando > maxPorClausula itens
// buildINClauseByValues(coluna, colecao, maxPorClausula, negate)
String inBatch = SQLUtils.buildINClauseByValues("NUNOTA", ids, 500, false);

// negate = true → NOT IN
String notInBatch = SQLUtils.buildINClauseByValues("NUNOTA", ids, 500, true);
```

---

## IN com bind parameters (PreparedStatement)

```java
// Gera: "NUNOTA IN (?,?,?)" com count parâmetros
String inBind = SQLUtils.buildINClause("NUNOTA", ids.size());
```

---

## Executar query dinâmica com bind

```java
import java.sql.Connection;
import java.sql.ResultSet;

StringBuffer sb = new StringBuffer("SELECT NUNOTA FROM TGFCAB WHERE CODPARC = ?");
Object[] params = { codParc };
ResultSet rs = SQLUtils.executeDynamicQuery(conn, sb, params); // throws Exception
```

---

## Montar WHERE incremental

```java
StringBuilder where = new StringBuilder();

// Adiciona " AND " se já tiver conteúdo, retorna o próprio StringBuilder
SQLUtils.appendAnd(where); // StringBuilder version (in-place)
where.append("ATIVO = 'S'");

SQLUtils.appendOr(where);
where.append("CODPARC = 1");

// String version — retorna nova String
String clause = SQLUtils.appendAnd("ATIVO = 'S'"); // " AND ATIVO = 'S'"
```

---

## Utilitários

```java
// escapa aspas simples em valores para SQL
String seguro = SQLUtils.escapeQuotes(valorUsuario);

// remove alias de campo ("T.CAMPO" → "CAMPO")
String campo = SQLUtils.removeAlias("T.NUNOTA"); // "NUNOTA"
```

---

## Antipadrões

```java
// ERRADO: IN manual
String ids_str = ids.stream().map(String::valueOf).collect(Collectors.joining(","));
String in = "NUNOTA IN (" + ids_str + ")";

// CORRETO
String in = SQLUtils.buildINClauseByValues("NUNOTA", ids);

// ERRADO: parâmetro sem coluna (método não existe)
// SQLUtils.buildINClauseByValues(ids) — compile error
// CORRETO: sempre passar nome da coluna primeiro
String in = SQLUtils.buildINClauseByValues("NUNOTA", ids);
```
