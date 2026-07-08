# JAPE — InMemoryDataSet (cache L2 em memória)

`br.com.sankhya.jape.util.InMemoryDataSet` é o cache de segundo nível (L2) proprietário do JAPE, mantido em memória da JVM. Carrega o resultado de um `SELECT` **uma única vez** para a memória e serve as leituras seguintes de lá, sem novo acesso ao banco.

Use quando a **mesma** informação é consultada repetidamente e muda pouco: tabelas de referência/configuração pequenas (CST, classe tributária, restrições de TOP, CFOP, parâmetros — ex.: `TLFCSTIC`, `TLFCLASTRIBIC`, `TGFREP`, `TGFCFO`). Elimina consultas repetitivas para o mesmo dado em caminhos quentes (listener, laço, faturamento).

> Código de referência: `JAPE/src/br/com/sankhya/jape/util/InMemoryDataSet.java`. Exemplos reais em `MGECom-Model/.../utils/ReformaTributariaUtils.java` e `MGECom-Model/.../utils/RestricaoTopUtil.java`.

---

## Como funciona a invalidação

A invalidação é **automática e inteligente**. O dataset declara as tabelas que observa via `addObservingTable` e o JAPE o invalida quando qualquer uma sofre `INSERT`/`UPDATE`/`DELETE` (gancho em `DMLStats`/`EntityDAO`).

| Mecanismo | Comportamento |
|---|---|
| Invalidação por escrita | Qualquer DML em tabela observada invalida o dataset. É **por tabela, não por linha**. |
| Cluster | A invalidação é propagada aos demais nós via `InMemoryDatasetEventProcessor`. |
| TTL | Opcional, via `setLifeSpan(ms)`. `0` = sem expiração (padrão). |
| Invalidação manual | `invalidateById` / `invalidateAll`. |
| Recarga | **Preguiçosa** — ocorre na próxima chamada a `getDataSet` após invalidar, não no momento da invalidação. |

---

## Quando usar

- Dado de **referência/configuração pequeno e limitado**, lido com frequência.
- Leitura "quente" no caminho de uma operação repetida (listener, laço, faturamento) com a **mesma** consulta e os **mesmos** dados.

## Quando NÃO usar (crítico)

| Cenário | Por quê |
|---|---|
| **Tabela grande/ilimitada** | A carga usa `setMaxRows(Integer.MAX_VALUE)`: o `SELECT` inteiro vai para o heap. Nunca cacheie `TGFCAB`/`TGFITE`/`TGFFIN` ou tabela transacional volumosa. |
| **Tabela "quente" (muita escrita)** | Cada escrita na tabela observada invalida o dataset **inteiro** (por tabela, não por linha), causando recarga constante e anulando o ganho. |
| **Consistência transacional estrita / tempo real** | A leitura vem de um snapshot e a recarga é preguiçosa; existe janela de defasagem. |
| **Dado por usuário/sessão/requisição (chave de alta cardinalidade)** | O registro é global e permanente (sem TTL, não sai da memória). Cada `id` distinto cria entrada definitiva; chave com muitos valores = vazamento de memória. |

Para o último caso, **prefira carregar a tabela pequena uma vez e filtrar em memória** (`query().filter()` / `byIndex()`) a parametrizar o `id` por valor. **Não embuta dado de alta cardinalidade no `id`.**

---

## Padrão idiomático

O idioma do codebase (de `ReformaTributariaUtils`, `RestricaoTopUtil`) é um **método estático** que retorna `InMemoryDataSet.getDataSet(id, jdbc, preparer)`:

- **`id` estável e namespaced** — `Classe.class.getName() + ":finalidade"`. Nunca coloque dado de alta cardinalidade no `id`.
- **`addObservingTable` é OBRIGATÓRIO** dentro do preparer. Registre **todas** as tabelas que o `SELECT` lê. Sem isso, o dado fica obsoleto até TTL/invalidação manual/restart.
- **Consulta em memória** — `dataset.query().filter(...)...exec()` retorna um `ResultSet` (proxy sobre a memória; não segura conexão JDBC, mas feche por convenção com `JdbcUtils.closeResultSet`). Para `DynamicVO` em vez de `ResultSet`, use `query().execAsVO(dao)`.
- **`BigDecimal` no filter** — `compareTo`, nunca `equals` (ver `gotchas.md`).

### Exemplo 1 — método preparador

```java
import br.com.sankhya.jape.util.InMemoryDataSet;
import br.com.sankhya.jape.util.InMemoryDataSet.DatasetPreparer;
import br.com.sankhya.jape.sql.NativeSql;
import br.com.sankhya.jape.wrapper.JdbcWrapper;

public final class RepresentanteCache {

    private RepresentanteCache() { }

    private static final String DS_ID =
            RepresentanteCache.class.getName() + ":TGFREP";

    public static InMemoryDataSet getDataSet(JdbcWrapper jdbc) throws Exception {
        return InMemoryDataSet.getDataSet(DS_ID, jdbc, new DatasetPreparer() {
            public void prepare(NativeSql sql, InMemoryDataSet ds) throws Exception {
                sql.appendSql("SELECT * FROM TGFREP");
                ds.addObservingTable("TGFREP"); // OBRIGATORIO para invalidacao
            }
        });
    }
}
```

### Exemplo 2 — consulta em memória com filter e fechamento em finally

```java
import java.math.BigDecimal;
import java.sql.ResultSet;
import com.sankhya.util.JdbcUtils;
import br.com.sankhya.jape.util.InMemoryDataSet;
import br.com.sankhya.jape.util.InMemoryDataSet.Filter;

public static boolean isRepresentanteAtivo(JdbcWrapper jdbc, final BigDecimal codrep)
        throws Exception {

    InMemoryDataSet ds = RepresentanteCache.getDataSet(jdbc);
    ResultSet rs = null;
    try {
        rs = ds.query().filter(new Filter() {
            public boolean accept(ResultSet row) throws Exception {
                // BigDecimal: compareTo, nunca equals
                return codrep.compareTo(row.getBigDecimal("CODREP")) == 0
                        && "S".equals(row.getString("ATIVO"));
            }
        }).exec();
        return rs.next();
    } finally {
        JdbcUtils.closeResultSet(rs);
    }
}
```

---

## Cuidados

- **`addObservingTable` é OBRIGATÓRIO** — sem ele o dado fica obsoleto até TTL/invalidação manual/restart. Registre **todas** as tabelas que o `SELECT` lê.
- **Dentro de classe BEAN (xDoclet/Java 6)** — escreva o `DatasetPreparer` e o `Filter` como **classe anônima com genéricos completos, SEM lambda**; feche o `ResultSet` de `exec()` em `finally`, **NUNCA com try-with-resources**. Os exemplos do repo vivem em classes `*Util` (Java 8) e usam try-with-resources — copiá-los para dentro de um BEAN quebra a geração xDoclet.
- **Não sincronize manualmente** — a concorrência é tratada internamente (`ReentrantReadWriteLock` + `ConcurrentHashMap`).
- **Não use para escrever no banco** — há modo `setUpdateable`/insert, mas é avançado; o uso recomendado é cache de **leitura**.

---

## Ver também

- Armadilhas de `BigDecimal` (`compareTo` vs `equals`), fechamento de `ResultSet` em `finally` e demais regras "NUNCA faça": `gotchas.md`.
- Regra Java 6 (BEAN/xDoclet) vs Java 8 (`*Util`): BEAN gerado por xDoclet compila em Java 6 (sem lambda/diamond/try-with-resources); classes `*Util` comuns compilam em Java 8.
