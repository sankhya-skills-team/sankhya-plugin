-- Testa uma procedure de Botão de Ação no banco de dev SEM cadastrar o botão.
-- Simula o que o Sankhya grava em EXECPARAMS ao clicar e desfaz tudo no fim.
-- Rode com SERVEROUTPUT ligado (SET SERVEROUTPUT ON no sqlplus).
--
-- Colunas de EXECPARAMS (conferidas no banco em 2026-10-12):
--   IDSESSAO VARCHAR2(50) · SEQUENCIA NUMBER(5) · NOME VARCHAR2(50) · TIPO VARCHAR2(1)
--   NUMINT NUMBER(10) · NUMDEC FLOAT · TEXTO VARCHAR2(4000) · DTA DATE
-- Linha i da grade = SEQUENCIA i; parâmetro do formulário = SEQUENCIA 0.
DECLARE
  V_SESSAO VARCHAR2(50) := 'TESTE-' || TO_CHAR(SYSDATE, 'HH24MISS');
  V_MSG    VARCHAR2(4000);
BEGIN
  -- Linhas "selecionadas": campos lidos por ACT_*_FIELD(P_IDSESSAO, i, 'CAMPO')
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, NUMINT) VALUES (V_SESSAO, 1, 'NUOS', 10);
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, TEXTO)  VALUES (V_SESSAO, 1, 'STATUS', 'A');
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, NUMINT) VALUES (V_SESSAO, 2, 'NUOS', 11);
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, TEXTO)  VALUES (V_SESSAO, 2, 'STATUS', 'A');

  -- Parâmetro do formulário: lido por ACT_TXT_PARAM(P_IDSESSAO, 'MOTIVO')
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, TEXTO)  VALUES (V_SESSAO, 0, 'MOTIVO', 'teste automatizado');

  -- Resposta "Sim" para a confirmação de sequencia 1 (ACT_ESCOLHER_SIMNAO)
  INSERT INTO EXECPARAMS (IDSESSAO, SEQUENCIA, NOME, TEXTO)  VALUES (V_SESSAO, 1, '__ESCOLHA_SIMNAO__', 'S');

  STP_ENCERRA_OS(P_CODUSU    => 0,
                 P_IDSESSAO  => V_SESSAO,
                 P_QTDLINHAS => 2,
                 P_MENSAGEM  => V_MSG);

  DBMS_OUTPUT.PUT_LINE('P_MENSAGEM: ' || V_MSG);

  ROLLBACK;   -- desfaz o UPDATE e as linhas de teste do EXECPARAMS
EXCEPTION
  WHEN OTHERS THEN
    ROLLBACK;
    DBMS_OUTPUT.PUT_LINE('ERRO: ' || SQLERRM);
    RAISE;
END;
/
