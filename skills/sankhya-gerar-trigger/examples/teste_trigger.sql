-- Testa uma trigger no banco de dev provocando o evento e desfazendo tudo.
-- Rode com SERVEROUTPUT ligado (SET SERVEROUTPUT ON no sqlplus).
-- Ajuste a tabela, a chave e o valor que viola a regra.
DECLARE
  V_ESPERADO EXCEPTION;
  PRAGMA EXCEPTION_INIT(V_ESPERADO, -20101);
BEGIN
  SAVEPOINT TESTE_TRIGGER;

  -- 1) Caso que VIOLA a regra: deve cair no ORA-20101
  BEGIN
    DELETE FROM AD_DSCAB WHERE NUDS = 1 AND STATUS = 'F';
    DBMS_OUTPUT.PUT_LINE('FALHOU: a exclusão de registro faturado passou.');
  EXCEPTION
    WHEN V_ESPERADO THEN
      DBMS_OUTPUT.PUT_LINE('OK: bloqueado -> ' || SQLERRM);
  END;

  -- 2) Caso que NÃO viola: deve passar sem erro
  BEGIN
    DELETE FROM AD_DSCAB WHERE NUDS = 2 AND STATUS <> 'F';
    DBMS_OUTPUT.PUT_LINE('OK: registro não faturado excluído (' || SQL%ROWCOUNT || ' linha).');
  EXCEPTION
    WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('FALHOU: ' || SQLERRM);
  END;

  ROLLBACK TO TESTE_TRIGGER;   -- desfaz os dois casos
END;
/
