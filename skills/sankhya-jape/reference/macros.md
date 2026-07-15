# JAPE — Macros SQL portáveis

Macros do `MacroTranslator` são funções que abstraem diferenças de sintaxe entre Oracle e SQL Server. Use macros em SQL que precisa rodar em ambos os bancos.

## Regra de ouro

**Não aninhe macro dentro de macro.** O `MacroTranslator` não é recursivo. Decomponha ou use SQL nativo do banco.

**Dialetos suportados**: Oracle e SQL Server. MySQL tem suporte parcial. Outros SGBDs **não funcionam**.

## Catálogo principal

### Datas

| Macro | Oracle | SQL Server | Uso |
|---|---|---|---|
| `dbDate()` | `SYSDATE` | `GETDATE()` | Data/hora atual do banco |
| `onlydate(X)` | `TRUNC(X)` | `DATEADD(DAY, DATEDIFF(DAY, 0, X), 0)` | Remove a hora (meia-noite do dia) |
| `truncDate(X)` | `TRUNC(X)` | `DATEADD(DAY, DATEDIFF(DAY, 0, X), 0)` | Igual a `onlydate` |
| `truncMonth(X)` | `TRUNC(X,'MM')` | `DATEADD(MONTH, DATEDIFF(MONTH, 0, X), 0)` | Primeiro dia do mês |
| `addMonths(X,N)` | `ADD_MONTHS(X,N)` | `DATEADD(MONTH,N,X)` | Soma N meses |
| `diffdays(X,Y)` | `TRUNC((X)-(Y))` | `DATEDIFF(DAY,(Y),(X))` | Diferença em dias (X - Y) |
| `diffhour(X,Y)` | `((X)-(Y))*24` | `DATEDIFF(HOUR,(Y),(X))` | Diferença em horas |
| `yearMonth(X)` | `TO_CHAR(X,'YYYYMM')` | `CONVERT(VARCHAR(6),X,112)` | Ano+mês como string 'YYYYMM' |
| `convertToTimestamp(X)` | `CAST(X AS TIMESTAMP)` | `CAST(X AS DATETIME)` | Conversão para timestamp |
| `convertToMilliseconds(X)` | `(X - DATE '1970-01-01')*86400000` | `DATEDIFF(MS, '1970-01-01', X)` | Epoch millis |

### Strings

| Macro | Oracle | SQL Server | Uso |
|---|---|---|---|
| `ignorecase(X)` | `TRANSLATE(UPPER(X),...)` (remove acentos) | `REPLACE(UPPER(X),...)` | Comparação insensível a caixa e acentos |
| `concatstr(A,B)` | `A \|\| B` | `A + B` | Concatenação de strings |
| `convertToVarchar(X)` | `TO_CHAR(X)` | `CONVERT(VARCHAR,X)` | Conversão para string |

### Números

| Macro | Oracle | SQL Server | Uso |
|---|---|---|---|
| `convertToNumber(X)` | `TO_NUMBER(X)` | `CONVERT(NUMERIC,X)` | Conversão para número |
| `nullValue(X,Y)` | `NVL(X,Y)` | `ISNULL(X,Y)` | Substitui NULL por Y |

### Paginação e agregação

| Macro | Oracle | SQL Server | Uso |
|---|---|---|---|
| `maxLines(N)` | `ROWNUM <= N` | `TOP N` | Limita linhas |
| `agg_string(X)` | `LISTAGG(X)` | `STRING_AGG(X)` | Agregação de strings |

### Contexto de usuário/schema

| Macro | Oracle | SQL Server | Uso |
|---|---|---|---|
| `${user.name}` | schema atual | catalog atual | Prefixo de objeto |

## Exemplos

### Listagem de pedidos dos últimos 30 dias

```sql
SELECT NUNOTA, DTNEG FROM TGFCAB
WHERE DTNEG >= onlydate(dbDate()) - 30
  AND maxLines(100)
```

Tradução Oracle:
```sql
SELECT NUNOTA, DTNEG FROM TGFCAB
WHERE DTNEG >= TRUNC(SYSDATE) - 30
  AND ROWNUM <= 100
```

Tradução SQL Server:
```sql
SELECT TOP 100 NUNOTA, DTNEG FROM TGFCAB
WHERE DTNEG >= DATEADD(DAY, DATEDIFF(DAY, 0, GETDATE()), 0) - 30
```

Note que `maxLines` muda de posição (onde/top) — o MacroTranslator faz esse ajuste.

### Busca case/accent-insensitive

```sql
SELECT * FROM TGFPAR WHERE ignorecase(RAZAOSOCIAL) LIKE ignorecase(:FILTRO)
```

Ambos os lados precisam da macro para funcionar como esperado.

### Diferença entre datas

```sql
SELECT NUNOTA FROM TGFCAB
WHERE diffdays(dbDate(), DTNEG) > 30
```

## Antipadrões

### Macro aninhada

```sql
-- Errado: onlydate contém addMonths
SELECT onlydate(addMonths(DATA_BASE, 3)) FROM TAB
```

Use SQL nativo do banco ou calcule em Java.

### Misturar macro com função nativa sem atenção

```sql
-- OK, mas pouco legível
SELECT CASE WHEN nullValue(VALOR, 0) > 0 THEN 'S' ELSE 'N' END FROM TAB
```

Misturar é permitido. Só não coloque uma macro *dentro* de outra.

### String literal contendo `:`

Parâmetros nomeados usam a regex `:\w+`. Literais string são removidos antes do parse, então isto é seguro:
```sql
SELECT 'tempo: 10s' FROM DUAL
```

Mas se você construir SQL dinamicamente concatenando `:algo` fora de literal, o parser vai interpretar como parâmetro. Sempre use `setNamedParameter` em vez de concatenar.

## Cache de tradução

O MacroTranslator cacheia resultados em dois níveis:
- Por sessão (`__jdbc.wrapper.translated.cache`)
- ThreadLocal global (se `jape.habilita.cache.macro.translator` for true)

Você não precisa se preocupar com isso no dia a dia — apenas saiba que trocar muito o SQL gera cache miss. Para loops de alto volume, reutilize o mesmo `NativeSql` com `setReuseStatements(true)`.

## Catálogo completo

O código de referência está em `MacroTranslator.java` (JAPE, ~800 linhas). Há mais de 40 macros compiladas como regex em bloco estático. Se precisar de uma macro que não está nesta lista, consulte esse arquivo no código Sankhya.
