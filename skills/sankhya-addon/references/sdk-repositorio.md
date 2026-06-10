# SDK Sankhya — Camada de Repositório (@Repository)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Visão Geral

O padrão Repository abstrai o acesso a dados. Você define uma interface que estende `JapeRepository<ID, T>` e o SDK gera a implementação automaticamente.

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {
    // métodos customizados aqui
}
```

- `T`: classe da entidade (ex: `Veiculo`)
- `ID`: tipo da chave primária (ex: `Long`)

---

## Métodos CRUD Padrão (herdados)

| Método | Descrição |
|---|---|
| `save(T entity)` | Salva ou atualiza a entidade |
| `findByPK(ID id)` | Busca por chave primária — retorna `Optional<T>` |
| `findAll()` | Retorna todas as instâncias |
| `findAll(Pageable pageable)` | Retorna página com ordenação — retorna `Page<T>` |
| `delete(T entity)` | Remove a entidade |

---

## Consultas Customizadas

### `@Criteria` — consultas declarativas

```java
@Criteria("ativo = :ativo AND marca = :nomeMarca")
List<Veiculo> findAtivosPorMarca(
    @Parameter("ativo") boolean ativo,
    @Parameter("nomeMarca") String nomeMarca
);

@Criteria(clause = "ATIVO = :ativo")
Page<Veiculo> findByAtivoPaginado(Boolean ativo, Pageable pageable);
```

### `@NativeQuery` — SQL nativo

Ideal para JOINs complexos, agregações, relatórios e otimizações de performance.

```java
// Retornando DTO (interface anotada com @NativeQuery.Result)
@NativeQuery.Result
public interface ResumoProdutoDTO {
    Long getCodigo();
    String getDescricao();
    BigDecimal getPreco();
}

@NativeQuery("SELECT CODPROD AS Codigo, DESCRPROD AS Descricao, VLRVENDA AS Preco FROM TGFPRO WHERE ATIVO = 'S'")
List<ResumoProdutoDTO> listarProdutosAtivos();
```

> Os nomes dos getters no DTO devem coincidir **exatamente** com os aliases das colunas na query.

```java
// Retornando tipo simples (apenas 1 coluna)
@NativeQuery("SELECT COUNT(1) FROM TGFPRO")
Long contarTotalDeProdutos();

@NativeQuery("SELECT DESCRPROD FROM TGFPRO WHERE CODPROD = :codigo")
String buscarDescricao(@Parameter("codigo") Long codigo);
```

### `@NativeQuery` com `JdbcWrapper` (dentro de Listeners)

```java
@NativeQuery("SELECT COUNT(1) FROM TGFCAB WHERE STATUS = 'P'")
Long contarPendentes(JdbcWrapper jdbc);

// Uso no listener:
JdbcWrapper jdbc = event.getJdbcWrapper();
Long pendentes = repository.contarPendentes(jdbc);
```

### `@Modifying` + `@NativeQuery` — operações de escrita em massa

```java
@Modifying
@NativeQuery("UPDATE TGFPRO SET VLRVENDA = VLRVENDA * :fator WHERE CODGRUPOPROD = :grupo")
int reajustarPrecoPorGrupo(@Parameter("fator") BigDecimal fator, @Parameter("grupo") Long grupo);

@Modifying
@NativeQuery("DELETE FROM AD_LOGS WHERE DTEXPIRACAO < :data")
int excluirLogsExpirados(@Parameter("data") LocalDate data);
```

Retorno: `int` (registros afetados) ou `void`. Sempre use dentro de `@Transactional`.

---

## Queries em Arquivos Externos

Para queries longas ou reutilizadas em múltiplos repositórios:

```java
@NativeQuery(value = "queries/listar-veiculos-ativos.sql", fromFile = true)
List<VeiculoView> listarAtivos(@Parameter("ativo") String ativo);
```

**Arquivo `.sql`** — compatível com Oracle e MSSQL:
```sql
-- resources/queries/listar-veiculos-ativos.sql
SELECT v.CODVEI, v.PLACA FROM TGFVEI v WHERE v.ATIVO = :ativo
```

**Arquivo `.xml`** — queries específicas por banco:
```xml
<sql>
    <both>SELECT ... FROM ... WHERE ...</both>
</sql>
<!-- ou separado por banco: -->
<sql>
    <oracle>SELECT NVL(SUM(QTD), 0) FROM ...</oracle>
    <mssql>SELECT ISNULL(SUM(QTD), 0) FROM ...</mssql>
</sql>
```

O SDK seleciona automaticamente a query correta em runtime. Queries são cacheadas após a primeira leitura.

---

## Paginação

```java
PageRequest pageRequest = PageRequest.of(0, 10,
    Sort.by("NOME", Direction.DESC),
    Sort.by("PLACA", Direction.DESC)
);
Page<Veiculo> pagina = repository.findByAtivoPaginado(true, pageRequest);
```

---

## Boas Práticas

- Prefira interfaces (DTOs) para queries com múltiplas colunas
- Evite `SELECT *` — mapeie apenas os campos necessários
- Use `@Transactional` em todos os métodos `@Modifying`
- Não use palavras reservadas do banco como nome de colunas
- Organize queries externas por contexto: `queries/vendas/`, `queries/estoque/`

---

## Fonte

https://developer.sankhya.com.br/docs/repositorio-dados
