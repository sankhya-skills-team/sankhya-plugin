# MacroTranslator — Macros Sankhya

Macros que abstraem diferenças de sintaxe entre **Oracle** e **MSSQL**. Use em queries SQL nativas (`@NativeQuery`, `@Criteria`, filtros, etc.).

---

## Texto e String

| Macro | Sintaxe | Oracle | MSSQL |
|---|---|---|---|
| `ignorecase` | `ignorecase(<expr>)` | `TRANSLATE(UPPER(...))` | `REPLACE(UPPER(...))` |
| `normalizeText` | `normalizeText(<expr>)` | `CONVERT(UPPER(...), 'US7ASCII')` | `REPLACE(UPPER(...))` |
| `trim` | `trim(<expr>)` | `TRIM(...)` | `LTRIM(RTRIM(...))` |
| `length` | `length(<expr>)` | `LENGTH(...)` | `DATALENGTH(...)` |
| `concatstr` | `concatstr(<s1>, <s2>)` | `s1 \|\| s2` | `s1 + s2` |
| `upperText` | `upperText(<expr>)` | `UPPER(...)` | `UPPER(RTRIM(CONVERT(VARCHAR,...)))` |
| `subString` | `subString(<col>, <ini>, <fim>)` | `SUBSTR(...)` | `SUBSTRING(...)` |
| `stringIndex` | `stringIndex(<src>, <trg>)` | `INSTR(src, trg)` | `CHARINDEX(trg, src)` |
| `leftPad` | `leftPad(<col>, <char>, <tam>)` | `LPAD(...)` | `RIGHT(REPLICATE(...)+col, tam)` |
| `quebraLinha` | `quebraLinha()` | `CHR(13)\|\|CHR(10)` | `CHAR(13)+CHAR(10)` |

---

## Data e Hora

| Macro | Sintaxe | Oracle | MSSQL |
|---|---|---|---|
| `dbDate` | `dbDate()` | `SYSDATE` | `GETDATE()` |
| `onlydate` | `onlydate(<data>)` | `TRUNC(<data>)` | `DATEADD(DAY, DATEDIFF(DAY,0,<data>),0)` |
| `truncDate` | `truncDate(<data>)` | `TRUNC(<data>)` | `CONVERT(date, <data>)` |
| `truncWeek` | `truncWeek(<data>)` | `TRUNC(<data>, 'IW')` | `DATEADD(...)` |
| `truncMonth` | `truncMonth(<data>)` | `TRUNC(<data>, 'MM')` | `DATEADD(...)` |
| `truncQarter` | `truncQarter(<data>)` | `TRUNC(<data>, 'Q')` | `DATEADD(QQ,...)` |
| `truncYear` | `truncYear(<data>)` | `TRUNC(<data>, 'YY')` | `DATEADD(YY,...)` |
| `yearMonth` | `yearMonth(<campo>)` | `TO_NUMBER(TO_CHAR(...,'YYYYMM'))` | `(YEAR(...)*100)+MONTH(...)` |
| `diffdays` | `diffdays(<d1>, <d2>)` | `TRUNC(d1 - d2)` | `DATEDIFF(DAY, d2, d1)` |
| `diffhour` | `diffhour(<d1>, <d2>)` | `(d1 - d2) * 24` | `DATEDIFF(HOUR, d2, d1)` |
| `addMonths` | `addMonths(<data>, <qtd>)` | `ADD_MONTHS(...)` | `DATEADD(MONTH, qtd, data)` |
| `endOfCurrentMonth` | `endOfCurrentMonth()` | `LAST_DAY(SYSDATE)` | `EOMONTH(GETDATE())` |
| `getDay` | `getDay(<data>)` | `TO_CHAR(<data>, 'DD')` | `DAY(<data>)` |
| `getMonth` | `getMonth(<data>)` | `TO_CHAR(<data>, 'MM')` | `MONTH(<data>)` |
| `getYear` | `getYear(<data>)` | `TO_CHAR(<data>, 'YYYY')` | `YEAR(<data>)` |
| `monYear` | `monYear(<data>)` | `TO_CHAR(<data>, 'MM/YYYY')` | `FORMAT(<data>, 'MM/yyyy')` |
| `convertPtBrDate` | `convertPtBrDate(<data>)` | `TO_CHAR(<data>, 'DD/MM/YYYY')` | `CONVERT(VARCHAR, <data>, 103)` |
| `convertToTimestamp` | `convertToTimestamp(<expr>)` | `TO_TIMESTAMP(...)` | `CONVERT(DATETIME, ...)` |
| `convertToMilliseconds` | `convertToMilliseconds(<expr>)` | `EXTRACT(MILLISECOND FROM ...)` | `DATEPART(MILLISECOND, ...)` |

---

## Numérico e Conversão

| Macro | Sintaxe | Oracle | MSSQL |
|---|---|---|---|
| `nullValue` | `nullValue(<expr>, <default>)` | `NVL(...)` | `ISNULL(...)` |
| `convertToNumber` | `convertToNumber(<expr>)` | `TO_NUMBER(...)` | `CONVERT(NUMERIC, ...)` |
| `convertToFloat` | `convertToFloat(<expr>)` | `<expr>` (sem conversão) | `CONVERT(FLOAT, ...)` |
| `convertToVarchar` | `convertToVarchar(<expr>)` | `TO_CHAR(...)` | `CONVERT(VARCHAR, ...)` |
| `maxLines` | `maxLines(<qtd>)` | `AND ROWNUM <= qtd` | `TOP qtd` |

---

## Schema e Banco

| Macro | Sintaxe | Descrição |
|---|---|---|
| `${user.name}` | `${user.name}TABELA` | Prefixo do usuário/schema |
| `sqldatabase` | `sqldatabase.TABELA` | Nome do banco/schema antes da tabela |

---

## Exemplos

```sql
-- Comparação sem case/acento
SELECT * FROM TGFPAR WHERE ignorecase(NOMEPARC) LIKE ignorecase('%silva%')

-- Data atual
SELECT dbDate() AS HOJE

-- Diferença em dias
SELECT diffdays(DTFIM, DTINICIO) AS DIAS FROM TGFCAB

-- Nulo com padrão
SELECT nullValue(VLRDESC, 0) AS DESCONTO FROM TGFITE

-- Limitar linhas
SELECT maxLines(10) * FROM TGFCAB ORDER BY DTNEG DESC
```

---

## Fonte

https://developer.sankhya.com.br/docs/macrotranslator-documenta%C3%A7%C3%A3o-de-macros-sankhya
