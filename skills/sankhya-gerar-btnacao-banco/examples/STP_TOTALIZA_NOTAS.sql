-- Botão de Ação (Rotina no Banco de dados) — só leitura.
-- Soma o VLRNOTA das notas selecionadas na grade e mostra o total ao usuário.
-- Tela: Central de Vendas / Notas (TGFCAB). Campo lido da grade: NUNOTA.
CREATE OR REPLACE PROCEDURE STP_TOTALIZA_NOTAS (
  P_CODUSU    NUMBER,
  P_IDSESSAO  VARCHAR2,
  P_QTDLINHAS NUMBER,
  P_MENSAGEM  OUT VARCHAR2
) AS
  V_NUNOTA NUMBER;
  V_VLR    NUMBER;
  V_TOTAL  NUMBER := 0;
BEGIN
  IF P_QTDLINHAS = 0 THEN
    RAISE_APPLICATION_ERROR(-20001, 'Selecione ao menos uma nota.');
  END IF;

  FOR I IN 1..P_QTDLINHAS LOOP
    V_NUNOTA := ACT_INT_FIELD(P_IDSESSAO, I, 'NUNOTA');
    IF V_NUNOTA IS NULL THEN
      RAISE_APPLICATION_ERROR(-20002, 'Campo NUNOTA não disponível na grade.');
    END IF;

    SELECT NVL(VLRNOTA, 0) INTO V_VLR
      FROM TGFCAB
     WHERE NUNOTA = V_NUNOTA;

    V_TOTAL := V_TOTAL + V_VLR;
  END LOOP;

  P_MENSAGEM := P_QTDLINHAS || ' nota(s) selecionada(s). Total: R$ '
             || TO_CHAR(V_TOTAL, 'FM999G999G990D00');
END;
/
