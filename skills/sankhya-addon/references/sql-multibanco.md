# SQL Multibanco — Oracle ↔ SQL Server

Regras para escrever SQL que roda **igual** em Oracle e SQL Server (Sankhya suporta ambos). Aplica a dbscripts, queries de NativeSql/`.sql`, views e qualquer SQL embutido no código.

> Para o formato dos arquivos `dbscripts` (tags `<sql>`, `<oracle>`, `<mssql>`, versionamento `V1.xml`), ver `dbscripts.md`. Este doc cobre **compatibilidade e convenções**, não o formato do arquivo.

---

## Mapeamento de tipos Oracle ↔ SQL Server

| Oracle | SQL Server | Uso |
|---|---|---|
| `NUMBER(n)` | `NUMERIC(n,0)` | inteiros, códigos, PKs |
| `NUMBER(p,s)` | `NUMERIC(p,s)` | valores monetários |
| `VARCHAR2(n)` | `VARCHAR(n)` | strings curtas |
| `CLOB` | `VARCHAR(MAX)` | texto longo |
| `CHAR(1)` | `CHAR(1)` | booleano S/N |
| `DATE` | `DATETIME` | datas |
| `FLOAT` | `FLOAT` | ponto flutuante |

No dicionário de dados Sankhya, o `CHAR(1)` S/N corresponde a `dataType="CHECKBOX"` — **não** existe `dataType="LOGICO"`.

---

## Funções e construções proibidas (não portáveis)

| ❌ Não use (específico de um banco) | ✅ Use no lugar |
|---|---|
| `A \|\| B` (concat Oracle) | `CONCAT(A, B)` — máx. 2 args; aninhe para 3+ |
| `NVL(x, y)` | `COALESCE(x, y)` |
| `DECODE(x, a, b, c)` | `CASE WHEN x = a THEN b ELSE c END` |
| `SYSDATE` | passe a data como parâmetro Java |
| `ROWNUM` (Oracle) / `TOP` (SQL Server) | passe o limite como parâmetro |
| `TO_DATE()`, `TO_CHAR()` | `CAST()` / `CONVERT()` ou parâmetro tipado |
| `FROM DUAL` | omita ou use subquery |

**Regra de bolso:** se a função não é ANSI SQL padrão, provavelmente quebra em um dos dois bancos. Na dúvida, parametrize o valor no Java em vez de calcular no SQL.

---

## Convenções de nomenclatura de objetos

| Objeto | Padrão | Exemplo |
|---|---|---|
| Tabela | PREFIXO_ÚNICO + NOME_MAIÚSCULO | `TTKREGRA`, `TTKNOT` |
| View | `V` + tabela | `VTTKREGRA` |
| Índice | `IDX_` + tabela + campo | `IDX_TTKREGRA_CNAE` |
| PK | `PK_` + tabela | `PK_TTKREGRA` |
| FK | `FK_` + tabela + ref | `FK_TTKNOT_TTKEVT` |
| Campo PK | `NU` ou `COD` + nome | `NUREGRA`, `CODTIPO` |
| Campo status | `ATIVO` CHAR(1) S/N | — |
| Campo data | `DT` + nome | `DTALTER` |
| Campo data/hora | `DH` + nome | `DHCRIACAO` |

Sempre use **prefixo único** (do projeto/cliente) em todas as tabelas, colunas e objetos — evita colisão com tabelas nativas do Sankhya e de outros add-ons. Não use o prefixo genérico `AD_`.

---

## Convenção de nomes para arquivos `.sql`

| Prefixo | Tipo | Exemplo |
|---|---|---|
| `que` | SELECT | `queSeqMaximaICMS.sql` |
| `ins` | INSERT | `insRegistroRegra.sql` |
| `upd` | UPDATE | `updStatusRegra.sql` |
| `del` | DELETE | `delRegraPorCodigo.sql` |

Use parâmetros nomeados (`:PARAM`) — nunca concatene input. Ver SQL injection em [seguranca-sankhya.md](seguranca-sankhya.md).

---

## Idempotência de DML

INSERT de dados de referência deve ser idempotente para sobreviver a reexecução:

- Oracle: `INSERT ... WHERE NOT EXISTS (...)`
- SQL Server: `IF NOT EXISTS (...) INSERT ...`

Teste todo script em **base limpa** e em **base já existente**.
