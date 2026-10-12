---
name: gerar-btnacao-banco
description: >
  Gera a procedure PL/SQL de um Botão de Ação do Sankhya OM do tipo
  "Rotina no Banco de dados" (stored procedure), no padrão oficial:
  assinatura P_CODUSU / P_IDSESSAO / P_QTDLINHAS / P_MENSAGEM, leitura das
  linhas selecionadas com ACT_*_FIELD, parâmetros do formulário com
  ACT_*_PARAM, confirmação com ACT_ESCOLHER_SIMNAO e retorno ao usuário por
  P_MENSAGEM. Usar quando o usuário pedir "botão de ação", "botão de ação
  procedure", "rotina de banco", "ação na grade", "procedure para a tela",
  "STP_", "ACT_INT_FIELD", "P_IDSESSAO" ou "/gerar-btnacao-banco".
  Não usar para botão de ação Java (AcaoRotinaJava / @ActionButton — ver
  sankhya-modulo-java e sankhya-addon) nem para triggers.
---

# Botão de Ação por procedure (Rotina no Banco de dados)

Gera a procedure que o Sankhya OM executa quando o usuário clica num Botão de
Ação configurado como **Rotina no Banco de dados**. O Sankhya grava as linhas
selecionadas e os parâmetros do formulário na tabela `EXECPARAMS`, chama a
procedure e exibe `P_MENSAGEM` ao usuário no fim.

Fonte do padrão: developer.sankhya.com.br/docs/rotina-banco-de-dados.
Conferido no banco Oracle do Sankhya em 2026-10-12: as 10 funções `ACT_*`
existem no schema `SKCONTAINER` e as `STP_*` da própria Sankhya usam
exatamente esta assinatura.

## Fluxo

1. **Confirme o schema antes de escrever.** Use o MCP `sankhya-schema`
   (`describe_table`) na tabela da tela: nome real das colunas, tipos e as
   opções dos campos codificados (`STATUSNOTA`, `TIPMOV`…). Nunca deduza o
   domínio pelo nome do campo: em `TGFCAB`, `STATUSNOTA` é `A=Atendimento`,
   `L=Liberada`, `P=Pendente`.
2. **Pergunte o que falta** (uma rodada só): nome da procedure (`STP_<ACAO>`),
   tela/tabela, campos da grade que a regra usa, parâmetros do formulário do
   botão (nome e tipo), regra de negócio, mensagem final, se precisa de
   confirmação Sim/Não.
3. **Gere a procedure** pelo template abaixo. Regra extensa vai para uma
   package; a procedure do botão só percorre as linhas e delega.
4. **Entregue o passo de cadastro:** no Sankhya OM, cadastrar o Botão de Ação
   na tela alvo com tipo *Rotina no Banco de dados*, informando o nome da
   procedure e os parâmetros do formulário com os mesmos nomes usados em
   `ACT_*_PARAM`.
5. **Entregue o teste sem a tela** (seção "Teste" abaixo), para o usuário
   validar no banco de dev antes de cadastrar o botão.

## Regras obrigatórias

- Assinatura fixa, nesta ordem:
  `P_CODUSU NUMBER, P_IDSESSAO VARCHAR2, P_QTDLINHAS NUMBER, P_MENSAGEM OUT VARCHAR2`.
- Linhas da grade: `FOR I IN 1..P_QTDLINHAS LOOP` e
  `ACT_INT_FIELD(P_IDSESSAO, I, 'CAMPO')` (ou `TXT`/`DEC`/`DTA`).
  Campo inexistente na grade retorna `NULL` sem erro: valide o nome.
- Parâmetros do formulário: `ACT_TXT_PARAM(P_IDSESSAO, 'NOME')` (ou
  `INT`/`DEC`/`DTA`).
- Retorno ao usuário **só** por `P_MENSAGEM`. `DBMS_OUTPUT` não aparece na
  tela.
- Erro de negócio: `RAISE_APPLICATION_ERROR(-20001, 'mensagem clara')`, faixa
  `-20000` a `-20999`. Nunca `WHEN OTHERS THEN NULL`.
- **Sem `COMMIT` / `ROLLBACK`**: a transação é do Sankhya. Só é diferente se
  o botão estiver configurado com transação manual — e aí o usuário tem que
  dizer isso explicitamente.
- Nome: `STP_<ACAO>` (padrão das procedures da própria Sankhya). Objetos de
  cliente seguem o prefixo da empresa quando existir (`AD_STP_…`).
- Confirmação no meio da ação: `ACT_ESCOLHER_SIMNAO(titulo, texto, P_IDSESSAO,
  sequencia)` retorna `'S'` ou `'N'`; `ACT_CONFIRMAR(...)` só OK/Cancelar.
  Perguntas com a mesma `sequencia` se sobrepõem: numere.
- `CODEMP`, `CODUSU` e similares vêm dos parâmetros ou das linhas, nunca
  fixos no código.

## Funções disponíveis (schema SKCONTAINER)

| Função | Assinatura | Retorna |
|---|---|---|
| `ACT_INT_FIELD` | `(P_CHAVE, P_LINHA, P_NOME)` | `NUMBER` inteiro da linha |
| `ACT_DEC_FIELD` | `(P_CHAVE, P_LINHA, P_NOME)` | `NUMBER` decimal da linha |
| `ACT_TXT_FIELD` | `(P_CHAVE, P_LINHA, P_NOME)` | `VARCHAR2` da linha |
| `ACT_DTA_FIELD` | `(P_CHAVE, P_LINHA, P_NOME)` | `DATE` da linha |
| `ACT_INT_PARAM` / `ACT_DEC_PARAM` / `ACT_TXT_PARAM` / `ACT_DTA_PARAM` | `(P_CHAVE, P_NOME)` | valor do parâmetro do formulário |
| `ACT_ESCOLHER_SIMNAO` | `(P_TITULO, P_TEXTO, P_CHAVE, P_SEQUENCIA)` | `'S'` ou `'N'` |
| `ACT_CONFIRMAR` | `(P_TITULO, P_TEXTO, P_CHAVE, P_SEQUENCIA)` | sem retorno; Cancelar aborta |

`P_CHAVE` é sempre `P_IDSESSAO`. Por baixo, todas leem `EXECPARAMS`
(`IDSESSAO`, `SEQUENCIA`, `NOME`, `NUMINT`, `NUMDEC`, `TEXTO`, `DTA`):
linha `i` da grade tem `SEQUENCIA = i`; parâmetros têm `SEQUENCIA = 0`.

## Template

```sql
CREATE OR REPLACE PROCEDURE STP_{ACAO} (
  P_CODUSU    NUMBER,          -- usuário logado
  P_IDSESSAO  VARCHAR2,        -- identifica a execução (chave do EXECPARAMS)
  P_QTDLINHAS NUMBER,          -- linhas selecionadas na grade
  P_MENSAGEM  OUT VARCHAR2     -- exibida ao usuário no fim
) AS
  V_NUNOTA   NUMBER;
  V_QTD      NUMBER := 0;
BEGIN
  IF P_QTDLINHAS = 0 THEN
    RAISE_APPLICATION_ERROR(-20001, 'Selecione ao menos uma linha.');
  END IF;

  FOR I IN 1..P_QTDLINHAS LOOP
    V_NUNOTA := ACT_INT_FIELD(P_IDSESSAO, I, 'NUNOTA');
    IF V_NUNOTA IS NULL THEN
      RAISE_APPLICATION_ERROR(-20002, 'Campo NUNOTA não disponível na grade.');
    END IF;

    PKG_{ACAO}.PROCESSAR(V_NUNOTA, P_CODUSU);   -- regra de negócio fica na package
    V_QTD := V_QTD + 1;
  END LOOP;

  P_MENSAGEM := V_QTD || ' registro(s) processado(s).';
END;
/
```

Exemplos completos em `examples/`:
- `STP_TOTALIZA_NOTAS.sql` — só leitura, soma `VLRNOTA` das notas
  selecionadas e devolve em `P_MENSAGEM`.
- `STP_ENCERRA_OS.sql` — confirmação com `ACT_ESCOLHER_SIMNAO`, parâmetro do
  formulário e `UPDATE` em tabela `AD_`.

## Teste sem a tela

O Sankhya preenche `EXECPARAMS` ao clicar no botão. Para testar no banco de
dev sem cadastrar o botão, simule esse preenchimento num bloco anônimo e
desfaça no fim (`examples/teste_execparams.sql`):

```sql
DECLARE
  V_SESSAO VARCHAR2(50) := 'TESTE-' || TO_CHAR(SYSDATE, 'HH24MISS');
  V_MSG    VARCHAR2(4000);
BEGIN
  -- duas linhas "selecionadas" (SEQUENCIA 1 e 2) com o campo NUNOTA
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, NUMINT) VALUES (V_SESSAO, 1, 'NUNOTA', 1001);
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, NUMINT) VALUES (V_SESSAO, 2, 'NUNOTA', 1002);
  -- parâmetro do formulário (SEQUENCIA 0)
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, TEXTO)  VALUES (V_SESSAO, 0, 'MOTIVO', 'teste');

  STP_{ACAO}(P_CODUSU => 0, P_IDSESSAO => V_SESSAO, P_QTDLINHAS => 2, P_MENSAGEM => V_MSG);
  DBMS_OUTPUT.PUT_LINE('P_MENSAGEM: ' || V_MSG);

  ROLLBACK;   -- desfaz o teste e as linhas do EXECPARAMS
END;
/
```

Troque `NUMINT` por `NUMDEC`, `TEXTO` ou `DTA` conforme o tipo do campo.
`ACT_ESCOLHER_SIMNAO` lê `TEXTO` em `NOME = '__ESCOLHA_SIMNAO__'` com a
`SEQUENCIA` da pergunta; para simular "Sim", insira essa linha com `'S'`.

## Não faça

- `COMMIT` ou `ROLLBACK` dentro da procedure (metade das linhas gravadas,
  metade não, e o usuário vê "sucesso").
- `WHEN OTHERS THEN NULL` ou `WHEN OTHERS THEN` sem re-lançar: engole o erro.
- `DBMS_OUTPUT` como mensagem ao usuário: use `P_MENSAGEM`.
- Ler campo da grade sem validar `NULL`: nome errado passa calado.
- `SELECT *` em cursor, `CODEMP`/`CODUSU` fixos, `SYSDATE` sem considerar
  o fuso do servidor quando a regra depende de data.
- Lógica de negócio longa dentro da procedure do botão: delegue a uma
  package.

## SQL Server

A documentação diz que o recurso existe também no SQL Server, mas a
assinatura T-SQL não está documentada e **não foi conferida**. Antes de
gerar para SQL Server, peça ao usuário o `sp_helptext` de uma procedure de
botão já existente no banco dele e siga aquela assinatura.
