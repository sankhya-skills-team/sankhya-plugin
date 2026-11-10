# sankhya-gerar-trigger

Skill para Claude Code que gera **trigger Oracle no padrão das triggers nativas** do Sankhya OM.

## O que esta skill faz

- Nomeia a trigger como `TRG_<INC|UPD|DLT>_<TABELA>_<SUFIXO>`
- Inclui a guarda `STP_GET_ATUALIZANDO` e a validação com `FPODEVALIDAR`
- Sinaliza erro de negócio com `RAISE_APPLICATION_ERROR (-20101)`
- Usa `:NEW`/`:OLD`, sem `COMMIT` e sem `SELECT` na própria tabela (evita `ORA-04091`, mutating table)
- Traz um roteiro de teste da trigger

## Quando acionar

> trigger · gatilho · bloquear exclusão · validar ao confirmar · BEFORE INSERT/UPDATE/DELETE · `TRG_` · `ORA-04091` · mutating table

Vale para tabelas `TGF*`, `TSI*`, `TCS*` e `AD_*`. Invocação direta: `/sankhya:gerar-trigger`

Não usar para botão de ação nem para evento em Java (`EventoProgramavelJava`, `@Listener`).

## Estrutura da skill

```
sankhya-gerar-trigger/
├── SKILL.md                         Instruções da skill (carregadas pelo Claude Code)
├── README.md                        Este arquivo
└── examples/
    ├── TRG_DLT_AD_DSCAB_FAT.sql     Exemplo de trigger de exclusão
    ├── TRG_UPD_TGFCAB_LIMCRED.sql   Exemplo de trigger de atualização na TGFCAB
    └── teste_trigger.sql            Roteiro de teste
```

## Skills relacionadas

- `sankhya-gerar-btnacao-banco`: procedure de botão de ação
- `sankhya-modulo-java` e `sankhya-addon`: evento em Java
