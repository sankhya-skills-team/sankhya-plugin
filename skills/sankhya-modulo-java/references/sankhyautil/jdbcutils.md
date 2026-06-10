# JdbcUtils

**Pacote:** `com.sankhya.util.JdbcUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.JdbcUtils;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Connection;
```

> **Atenção:** nome da classe é `JdbcUtils` (não `JDBCUtils`).

> Em módulos Java Sankhya, prefer `JapeFactory`/`JdbcWrapper` para executar queries.
> Use `JdbcUtils` somente para **fechar recursos JDBC** e para auxiliares de ResultSet.

---

## Fechar recursos (uso principal)

Sempre usar em bloco `finally` ao manipular `ResultSet`/`Statement` diretamente.
Todos os métodos são null-safe — não lançam exceção.

```java
ResultSet rs    = null;
Statement stmt  = null;
try {
    stmt = conn.createStatement();
    rs   = stmt.executeQuery(sql);
    while (rs.next()) {
        // processar...
    }
} finally {
    JdbcUtils.closeResultSet(rs);
    JdbcUtils.closeStatement(stmt);
    // NÃO fechar conn aqui — gerenciada pelo container Sankhya
}
```

---

## Fechar Connection (casos especiais)

Usar somente quando a Connection foi criada manualmente (integração externa).
Connections obtidas via `JapeFactory` ou `JapeSession` **não devem** ser fechadas manualmente.

```java
Connection conn = null;
try {
    conn = JdbcUtils.buildConnectionFromProperties(props); // conexão externa
    // ...
} finally {
    JdbcUtils.closeConnection(conn); // null-safe
}
```

---

## Ler campos tipados do ResultSet

```java
// Lê campo inferindo tipo pelo metadado da coluna
Object valor = JdbcUtils.getTypedFieldFromResultSet("VLRTOTAL", rs);

// Lê campo com tipo explícito
BigDecimal bd = (BigDecimal) JdbcUtils.getTypedFieldFromResultSet("VLRTOTAL", BigDecimal.class, rs);

// Preenche Map com todos os campos da linha atual
Map<String, Object> row = new LinkedHashMap<>();
JdbcUtils.fillMapFromResultSet(row, rs); // throws SQLException
// → {"NUNOTA"=1234, "CODPARC"=5, "VLRTOTAL"=BigDecimal(100.00), ...}
```

---

## CLOB como String

```java
// Ler campo CLOB do ResultSet como String
String clob = JdbcUtils.getClobFieldAsString(rs, "DESCRICAO"); // throws Exception
```

---

## Criar conexão manual (raro em módulos)

```java
import java.util.Properties;

Properties props = new Properties();
props.setProperty("driver", "oracle.jdbc.OracleDriver");
props.setProperty("url", "jdbc:oracle:thin:@host:1521:sid");
props.setProperty("user", "user");
props.setProperty("password", "pass");

Connection conn = JdbcUtils.buildConnectionFromProperties(props); // throws Exception
```

---

## Antipadrões

```java
// ERRADO — import errado
import br.com.sankhya.util.JDBCUtils; // não existe
// CORRETO
import com.sankhya.util.JdbcUtils;

// ERRADO — não fechar ResultSet (vaza connection)
ResultSet rs = stmt.executeQuery(sql);
// processar sem finally...

// CORRETO
} finally {
    JdbcUtils.closeResultSet(rs);
    JdbcUtils.closeStatement(stmt);
}

// ERRADO — fechar Connection da Sankhya manualmente
JdbcUtils.closeConnection(conn); // se conn veio do JapeSession
// CORRETO — não fechar; container gerencia o ciclo de vida
```
