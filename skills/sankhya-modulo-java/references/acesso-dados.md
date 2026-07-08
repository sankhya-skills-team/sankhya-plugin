# Acesso a Dados — JapeFactory, DwfUtils, EntityFacade, JdbcWrapper

## Hierarquia das APIs de Dados

```
JapeFactory          ← API primária — CRUD simples por entidade/PK
DwfUtils             ← Busca coleção com filtro (query JAPE)
EntityFacade         ← Operações de alto nível, FinderWrapper
JdbcWrapper          ← SQL direto — usar apenas quando as APIs acima não forem suficientes
```

---

## JapeFactory — API Principal

### Busca por PK

```java
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.jape.wrapper.JapeWrapper;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.modelcore.util.DynamicEntityNames;

// PK simples
DynamicVO vo = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);

// PK composta (passar na ordem dos campos PK)
DynamicVO item = JapeFactory.dao(DynamicEntityNames.ITEM_NOTA).findByPK(nuNota, sequencia);

// Entidade customizada
DynamicVO registro = JapeFactory.dao("AD_NOMETABELA").findByPK(id);
```

### Busca por filtro (primeiro resultado)

```java
// findOne — retorna o primeiro registro que satisfaz o filtro
DynamicVO vo = JapeFactory.dao("AD_NOMETABELA")
        .findOne("this.CAMPO = ?", new Object[]{valor});

// Com múltiplos critérios
DynamicVO vo = JapeFactory.dao("AD_NOMETABELA")
        .findOne("this.CAMPO1 = ? AND this.CAMPO2 = ?", new Object[]{val1, val2});
```

### Criar registro

```java
DynamicVO novo = JapeFactory.dao("AD_NOMETABELA").create()
        .set("CAMPO1", valor1)
        .set("CAMPO2", valor2)
        .set("CAMPO3", valor3)
        .save();

// Acessar o ID gerado após o save
BigDecimal idGerado = BigDecimalUtil.getBigDecimal(novo.getProperty("IDCAMPO"));
```

### Atualizar por PK

```java
// PK simples
JapeFactory.dao("AD_NOMETABELA")
        .prepareToUpdateByPK(id)
        .set("CAMPO_STATUS", "F")
        .set("CAMPO_DATA", new java.sql.Timestamp(System.currentTimeMillis()))
        .update();

// PK composta
JapeFactory.dao(DynamicEntityNames.ITEM_NOTA)
        .prepareToUpdateByPK(nuNota, sequencia)
        .set("VLRUNIT", novoValor)
        .update();
```

### Excluir

```java
// Excluir por critério
JapeFactory.dao("AD_NOMETABELA")
        .deleteByCriteria("this.CAMPO = ?", new Object[]{valor});

// Excluir por PK (via prepareToDelete se disponível)
JapeFactory.dao("AD_NOMETABELA")
        .prepareToUpdateByPK(id)
        .delete(); // verificar disponibilidade na versão do módulo
```

### Buscar com transação explícita (JdbcWrapper da sessão)

```java
import br.com.sankhya.jape.dao.JdbcWrapper;  // import correto

// Dentro de evento — usar o JdbcWrapper do evento para mesma transação
JdbcWrapper jdbc = pEvent.getJdbcWrapper();
JapeWrapper dao = JapeFactory.dao("AD_NOMETABELA", jdbc);

DynamicVO vo = dao.findByPK(id);
```

---

## DwfUtils — Busca de Coleção

```java
import br.com.sankhya.dstech.utils.DwfUtils;
import java.util.Collection;

// Busca simples
Collection<DynamicVO> itens = DwfUtils.findEntitysAsVO(
        DynamicEntityNames.ITEM_NOTA,
        "this.NUNOTA = ?",
        new Object[]{nuNota});

// Busca em entidade customizada
Collection<DynamicVO> registros = DwfUtils.findEntitysAsVO(
        "AD_NOMETABELA",
        "this.STATUS = ?",
        new Object[]{"P"});

// Sempre verificar null/vazio antes de iterar
if (registros == null || registros.isEmpty()) return;

for (DynamicVO registro : registros) {
    BigDecimal campo = registro.asBigDecimal("CAMPO");
    // processar...
}
```

### Acumular valor de coleção

```java
Collection<DynamicVO> itens = DwfUtils.findEntitysAsVO(
        DynamicEntityNames.ITEM_NOTA,
        "this.NUNOTA = ?",
        new Object[]{nuNota});

BigDecimal total = BigDecimal.ZERO;
if (itens != null) {
    for (DynamicVO item : itens) {
        BigDecimal peso = item.asBigDecimal("PESOBRUTO");
        if (BigDecimalUtil.isNullOrZero(peso)) {
            peso = item.asBigDecimal("PESOLIQ"); // fallback
        }
        if (peso != null && peso.compareTo(BigDecimal.ZERO) > 0) {
            total = total.add(peso);
        }
    }
}
```

---

## EntityFacade / FinderWrapper

Útil para queries mais complexas com múltiplos critérios e paginação.

```java
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.util.FinderWrapper;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;

EntityFacade dwfFacade = EntityFacadeFactory.getDWFFacade();

// FinderWrapper com critério simples
FinderWrapper wrapper = new FinderWrapper(
        DynamicEntityNames.CABECALHO_NOTA,
        "NUMCONTRATO = ?",
        numContrato);

@SuppressWarnings("unchecked")
Collection<DynamicVO> entidades = (Collection<DynamicVO>)
        dwfFacade.findByDynamicFinderAsVO(wrapper);

boolean existe = !entidades.isEmpty();
```

---

## DynamicVO — Leitura e Escrita

```java
// Leitura tipada (sempre preferir sobre getProperty com cast)
BigDecimal codParc    = vo.asBigDecimal("CODPARC");
String status         = vo.asString("STATUS");
Timestamp dtAlteracao = vo.asTimestamp("DTALTER");
Boolean ativo         = vo.asBoolean("ATIVO"); // campos S/N mapeados como Boolean

// Leitura com cast (quando asBigDecimal não estiver disponível)
BigDecimal valor = BigDecimalUtil.getBigDecimal(vo.getProperty("CAMPO"));

// Escrita (em eventos before*, modifica o valor antes de persistir)
vo.setProperty("CAMPO", novoValor);

// Verificar existência antes de acessar campo opcional
if (vo.containsProperty("CAMPO_OPCIONAL")) {
    BigDecimal val = vo.asBigDecimal("CAMPO_OPCIONAL");
}
```

---

## BigDecimalUtil — Utilitários

```java
import com.sankhya.util.BigDecimalUtil;

// Converter Object → BigDecimal (seguro para null)
BigDecimal valor = BigDecimalUtil.getBigDecimal(vo.getProperty("CAMPO"));

// Verificar se é nulo ou zero
if (BigDecimalUtil.isNullOrZero(valor)) return;

// Arredondar
BigDecimal arredondado = BigDecimalUtil.getRounded(valor, 2);
```

---

## JdbcWrapper + NativeSql — SQL Nativo

Usar **apenas** quando JapeFactory/DwfUtils não atenderem (ex: GROUP BY, subconsultas, metadados do catálogo).

> **ATENÇÃO:** `JdbcWrapper` **não executa queries diretamente**.
> Quem executa é o `NativeSql`. O `JdbcWrapper` gerencia a sessão/conexão.
>
> Import correto: `import br.com.sankhya.jape.dao.JdbcWrapper;`
> (NÃO usar `br.com.sankhya.jape.util.JdbcWrapper`)

### Imports necessários

```java
import br.com.sankhya.jape.dao.JdbcWrapper;
import br.com.sankhya.jape.sql.NativeSql;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import br.com.sankhya.modelcore.MGEModelException;
import com.sankhya.util.JdbcUtils;
import java.sql.ResultSet;
```

### Padrão completo com arquivo .sql

Preferir arquivos `.sql` para queries complexas. Para queries simples, pode-se
passar a SQL diretamente (ver seção abaixo).

```java
JdbcWrapper jdbc = null;
NativeSql   sql  = null;
ResultSet   rset = null;

try {
    jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
    jdbc.openSession();

    // Carrega SQL de arquivo no classpath (relativo à classe ou absoluto)
    sql = new NativeSql(jdbc, MinhaClasse.class, "/pacote/sql/minhaBusca.sql");

    // Parâmetros nomeados (SQL usa :NOMEPARAM)
    sql.setNamedParameter("NUNOTA",    nuNota);
    sql.setNamedParameter("STATUS",    "F");
    sql.setNamedParameter("REFERENCIA", referencia);

    rset = sql.executeQuery();

    while (rset.next()) {
        BigDecimal valor = BigDecimalUtil.getValueOrZero(rset.getBigDecimal("VALOR"));
        // processar...
    }

} catch (Exception e) {
    MGEModelException.throwMe(e);
} finally {
    NativeSql.releaseResources(sql);    // libera NativeSql
    JdbcUtils.closeResultSet(rset);     // fecha ResultSet
    JdbcWrapper.closeSession(jdbc);     // fecha sessão (método estático)
}
```

### Arquivo .sql com parâmetros nomeados

```sql
-- /src/resources/pacote/sql/minhaBusca.sql
SELECT
    c.CAMPO1,
    c.CAMPO2,
    i.VLRTOTAL
FROM TGFCAB c
JOIN TGFITE i ON i.NUNOTA = c.NUNOTA
WHERE c.NUNOTA     = :NUNOTA
  AND c.STATUSNOTA = :STATUS
  AND c.DTNEG      >= :REFERENCIA
ORDER BY c.DTNEG
```

### Quando usar arquivo .sql vs. SQL inline

- **Arquivo .sql:** queries complexas com múltiplos JOINs, subconsultas, GROUP BY
- **SQL inline (simples):** uma tabela, poucos campos, sem subconsulta — passar diretamente ao construtor de NativeSql

### Ciclo de vida — regras

| Ação | Como |
|---|---|
| Abrir sessão | `jdbc.openSession()` — obrigatório antes de usar NativeSql |
| Fechar sessão | `JdbcWrapper.closeSession(jdbc)` — estático, no `finally` |
| Liberar NativeSql | `NativeSql.releaseResources(sql)` — no `finally` |
| Fechar ResultSet | `JdbcUtils.closeResultSet(rset)` — no `finally` |
| Dentro de evento | usar `pEvent.getJdbcWrapper()` — não chamar `openSession()`, sessão já está aberta |

### Query Cross-Database (SQL Server / Oracle) com Fallback via NativeSql

Para queries em catálogos do sistema (metadados, colunas), usar dois arquivos `.sql`
e tentar SQL Server primeiro:

```java
JdbcWrapper jdbc = null;
NativeSql   sql  = null;
ResultSet   rset = null;

try {
    jdbc = EntityFacadeFactory.getDWFFacade().getJdbcWrapper();
    jdbc.openSession();

    // Tenta SQL Server / H2 (INFORMATION_SCHEMA)
    try {
        sql = new NativeSql(jdbc, MinhaClasse.class, "/pacote/sql/buscarSqlServer.sql");
        rset = sql.executeQuery();
    } catch (Exception e1) {
        // Fallback Oracle (USER_TAB_COLUMNS — schema atual)
        // Para outro schema: editar SQL para ALL_TAB_COLUMNS WHERE OWNER = 'SANKHYA'
        NativeSql.releaseResources(sql);
        sql = new NativeSql(jdbc, MinhaClasse.class, "/pacote/sql/buscarOracle.sql");
        rset = sql.executeQuery();
    }

    while (rset.next()) {
        // processar...
    }

} catch (Exception e) {
    MGEModelException.throwMe(e);
} finally {
    NativeSql.releaseResources(sql);
    JdbcUtils.closeResultSet(rset);
    JdbcWrapper.closeSession(jdbc);
}
```

> **ESCAPE '!'** nos arquivos .sql — trata o `_` como literal no LIKE:
> `COLUMN_NAME LIKE 'AD!_%' ESCAPE '!'` casa com colunas que começam com `AD_`.

---

## JapeSession — Quando e Como Usar

`JapeSession` é necessário quando código executado fora de um contexto de transação existente
(ex: botão de ação que precisa criar registros) precisa abrir uma nova sessão.

```java
import br.com.sankhya.jape.core.JapeSession;

JapeSession.SessionHandle hnd = null;
try {
    hnd = JapeSession.open();

    // operações JapeFactory aqui...
    DynamicVO novo = JapeFactory.dao("AD_NOMETABELA").create()
            .set("CAMPO", valor)
            .save();

} catch (Exception e) {
    throw MGEModelException.prettyMsg("Erro: " + e.getMessage(), e);
} finally {
    JapeSession.close(hnd);  // obrigatório no finally
}
```

### Regras do JapeSession

- **NUNCA usar dentro de eventos** — a sessão já está aberta pela plataforma
- **Sempre usar `finally`** — garante fechamento mesmo em caso de exceção
- **`JapeSession.close(null)`** é seguro — não lança exceção se `hnd` for null

---

## Patterns Comuns de Consulta

### Verificar existência de registro

```java
public static boolean existeRegistro(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao("AD_NOMETABELA").findByPK(id);
    return vo != null;
}
```

### Buscar campo de outra entidade

```java
public static BigDecimal buscarCodEmp(BigDecimal nuNota) throws Exception {
    DynamicVO cabVO = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);
    if (cabVO == null) {
        throw new MGEModelException("Nota não encontrada: " + nuNota);
    }
    return cabVO.asBigDecimal("CODEMP");
}
```

### Verificar FK já preenchida

```java
BigDecimal vinculo = BigDecimalUtil.getBigDecimal(vo.getProperty("CAMPO_VINCULO"));
if (!BigDecimalUtil.isNullOrZero(vinculo)) {
    ctx.setMensagemRetorno("Este registro já possui vínculo: " + vinculo);
    return;
}
```
