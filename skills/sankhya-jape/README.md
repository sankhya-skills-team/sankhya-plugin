# sankhya-jape

Skill para Claude Code especializada em **acesso a banco de dados em Java no Sankhya OM** pelo framework JAPE.

## O que esta skill faz

- Orienta a abertura e o fechamento de sessão (`JapeSession`) e o uso de `execWithTX`
- Escreve consultas com `NativeSql` e parâmetros nomeados (`:nome`), sem concatenação
- Cobre `EntityFacade`, `DynamicVO`, `JdbcWrapper`, `EntityDAO`, `Criteria` e `EntityQuery`
- Trata transação manual, transação autônoma e DML
- Usa macros portáveis entre Oracle e SQL Server e `BigDecimal` em SQL
- Lista as armadilhas conhecidas e o que não fazer

## Quando acionar

Ao escrever, alterar ou revisar código Java que acessa o banco no Sankhya OM: abertura de sessão JAPE, `NativeSql`, DML manual, chamada de stored procedure por `ProcedureCaller`, `Criteria`, `EntityQuery` ou Value Objects dinâmicos.

## Estrutura da skill

```
sankhya-jape/
├── SKILL.md                     Instruções da skill (carregadas pelo Claude Code)
├── README.md                    Este arquivo
├── reference/
│   ├── api-cheatsheet.md        Resumo da API
│   ├── gotchas.md               Armadilhas conhecidas
│   ├── inmemory-dataset.md      Dataset em memória
│   ├── listeners.md             Listeners de persistência
│   ├── macros.md                Macros portáveis Oracle/SQL Server
│   ├── queries.md               Consultas
│   ├── resource-management.md   Abertura e liberação de recursos
│   └── transactions.md          Transações
└── templates/
    ├── nativesql-query.java     Modelo de consulta com NativeSql
    └── session-with-tx.java     Modelo de sessão com transação
```

## Skills relacionadas

- `sankhya-addon` e `sankhya-modulo-java`: o artefato em que o acesso a dados roda
- `sankhya-dicionario`: tabelas, campos e `entityName`
