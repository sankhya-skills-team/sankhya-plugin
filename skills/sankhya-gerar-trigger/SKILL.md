---
name: gerar-trigger
description: >
  Gera trigger Oracle no padrão das triggers nativas do Sankhya OM:
  nome TRG_<INC|UPD|DLT>_<TABELA>_<SUFIXO>, guarda STP_GET_ATUALIZANDO,
  validação com FPODEVALIDAR, erro de negócio por RAISE_APPLICATION_ERROR
  (-20101), dados por :NEW/:OLD, sem COMMIT e sem SELECT na própria tabela.
  Usar quando o usuário pedir "trigger", "gatilho", "bloquear exclusão",
  "validar ao confirmar", "BEFORE INSERT/UPDATE/DELETE", "TRG_",
  "ORA-04091", "mutating table" ou "/gerar-trigger" em tabela TGF*, TSI*,
  TCS* ou AD_*. Não usar para botão de ação (ver gerar-btnacao-banco) nem
  para evento Java (EventoProgramavelJava / @Listener — ver
  sankhya-modulo-java e sankhya-addon).
---

# Trigger Oracle no padrão Sankhya

Gera triggers que convivem com as triggers nativas do Sankhya OM. O padrão
abaixo foi extraído do próprio banco (conferido em 2026-10-12): 515 triggers
nativas usam o guarda `STP_GET_ATUALIZANDO`, os nomes seguem
`TRG_INC_/TRG_UPD_/TRG_DLT_<TABELA>` e o erro de negócio sai com
`RAISE_APPLICATION_ERROR(-20101, ERRMSG)`.

## Fluxo

1. **Confirme o schema antes de escrever.** Use o MCP `sankhya-schema`
   (`describe_table`) na tabela alvo e nas tabelas consultadas: nomes reais,
   tipos e as opções dos campos codificados. Nunca deduza o domínio pelo nome
   do campo (em `TGFCAB`, `STATUSNOTA` é `A=Atendimento`, `L=Liberada`,
   `P=Pendente`; em `TGFFIN`, `RECDESP` é `1=Receita`, `-1=Despesa`).
2. **Veja as triggers que já existem na tabela** (`USER_TRIGGERS`): a sua vai
   rodar junto com as nativas, na ordem que o Oracle escolher. Não duplique
   regra que o Sankhya já faz.
3. **Pergunte o que falta** (uma rodada só): tabela, evento (INSERT, UPDATE,
   DELETE), condição, mensagem ao usuário, se a regra vale também na
   sincronização de dados.
4. **Gere a trigger** pelo template. Regra extensa vai para uma package.
5. **Entregue o teste** (seção "Teste") para o usuário rodar no banco de dev.

## Regras obrigatórias

- **Nome:** `TRG_<INC|UPD|DLT>_<TABELA>_<SUFIXO>`, o mesmo padrão das
  nativas. O sufixo descreve a regra e evita colisão com trigger do Sankhya
  (ex.: `TRG_DLT_AD_DSCAB_FAT`, `TRG_UPD_TGFCAB_LIMCRED`).
- **BEFORE para validar** (bloquear, ajustar `:NEW`); **AFTER para derivar**
  (gravar em outra tabela).
- **`FOR EACH ROW`** e cláusula `WHEN` sempre que der: a trigger nem executa
  quando a condição não vale.
- **Guarda de sincronização:** `IF STP_GET_ATUALIZANDO THEN RETURN; END IF;`
  no início. Durante a sincronização de dados o Sankhya não valida.
- **Dados da linha só por `:NEW` / `:OLD`.** Nunca `SELECT` na própria tabela
  (ORA-04091, mutating table). Se a regra precisa olhar outras linhas da
  mesma tabela, use compound trigger ou mova para um evento/botão.
- **Erro de negócio:** monte `ERRMSG` e lance
  `RAISE_APPLICATION_ERROR(-20101, ERRMSG)`, protegido por
  `FPODEVALIDAR('<TABELA>')` como nas nativas. Mensagem em português, clara
  para o usuário final.
- **Sem `COMMIT` / `ROLLBACK`.** A transação é de quem disparou (ORA-04092).
- **Nunca `WHEN OTHERS THEN NULL`.**
- **Valores de domínio** (status, tipo de movimento) vêm do `describe_table`,
  nunca chutados.

## Template

```sql
CREATE OR REPLACE TRIGGER TRG_{INC|UPD|DLT}_{TABELA}_{SUFIXO}
  BEFORE {INSERT|UPDATE|DELETE} ON {TABELA}
  FOR EACH ROW
  WHEN ({condição sobre NEW/OLD})
DECLARE
  ERRMSG    VARCHAR2(4000);
  ERRO      EXCEPTION;
  P_VALIDAR BOOLEAN;
BEGIN
  IF STP_GET_ATUALIZANDO THEN   -- sincronização de dados: não valida
    RETURN;
  END IF;

  P_VALIDAR := FPODEVALIDAR('{TABELA}');

  IF {regra violada} THEN
    ERRMSG := '{mensagem clara para o usuário}';
    RAISE ERRO;
  END IF;

EXCEPTION
  WHEN ERRO THEN
    IF P_VALIDAR THEN
      RAISE_APPLICATION_ERROR(-20101, ERRMSG);
    END IF;
END;
/
```

Exemplos completos em `examples/`:
- `TRG_DLT_AD_DSCAB_FAT.sql` — bloqueia exclusão de registro faturado numa
  tabela adicional (`:OLD`, `WHEN`, guarda e erro -20101).
- `TRG_UPD_TGFCAB_LIMCRED.sql` — valida o limite de crédito do parceiro ao
  liberar a nota (`STATUSNOTA` vai para `L`), consultando `TGFPAR` e `TGFFIN`
  — outras tabelas, nunca a própria.

## Teste

Trigger se testa provocando o evento dentro de um bloco e desfazendo no fim
(`examples/teste_trigger.sql`): o bloco espera o ORA-20101 quando a regra é
violada e sucesso quando não é, e faz `ROLLBACK` nos dois casos.

Antes de rodar, compile e confira:

```sql
SELECT STATUS FROM USER_OBJECTS WHERE OBJECT_NAME = 'TRG_DLT_AD_DSCAB_FAT';
SELECT LINE, TEXT FROM USER_ERRORS WHERE NAME = 'TRG_DLT_AD_DSCAB_FAT';
```

`STATUS = 'INVALID'` ou linha em `USER_ERRORS` = erro de compilação.

## Não faça

- `COMMIT` ou `ROLLBACK` dentro da trigger (ORA-04092).
- `SELECT` ou `UPDATE` na própria tabela da trigger (ORA-04091).
- `WHEN OTHERS THEN NULL`: engole o erro e a regra deixa de existir sem aviso.
- Nome fora do padrão (`TRIGGER1`, `TG_X`): quem abre `USER_TRIGGERS` não
  entende o que dispara.
- Esquecer o guarda `STP_GET_ATUALIZANDO`: a sincronização passa a falhar.
- Regra de negócio longa dentro da trigger: delegue a uma package.
- `DBMS_OUTPUT` como mensagem ao usuário: só `RAISE_APPLICATION_ERROR` chega
  à tela.

## SQL Server

Não conferido. A sintaxe T-SQL (`inserted`/`deleted`, `THROW`) e o
equivalente do guarda de sincronização não foram verificados. Antes de gerar
para SQL Server, peça ao usuário o `sp_helptext` de uma trigger nativa do
banco dele e siga aquele padrão.
