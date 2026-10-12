-- Valida o limite de crédito do parceiro quando a nota é liberada.
-- Domínios conferidos no banco em 2026-10-12:
--   TGFCAB.STATUSNOTA: A=Atendimento, L=Liberada, P=Pendente
--   TGFCAB.TIPMOV: V=Venda, P=Pedido de venda (entre outros)
--   TGFFIN.RECDESP: 1=Receita, -1=Despesa
-- Consulta TGFPAR e TGFFIN — nunca a própria TGFCAB (ORA-04091).
CREATE OR REPLACE TRIGGER TRG_UPD_TGFCAB_LIMCRED
  BEFORE UPDATE OF STATUSNOTA ON TGFCAB
  FOR EACH ROW
  WHEN (NEW.STATUSNOTA = 'L' AND OLD.STATUSNOTA <> 'L' AND NEW.TIPMOV IN ('V', 'P'))
DECLARE
  ERRMSG     VARCHAR2(4000);
  ERRO       EXCEPTION;
  P_VALIDAR  BOOLEAN;
  V_LIMITE   NUMBER;
  V_ABERTO   NUMBER;
BEGIN
  IF STP_GET_ATUALIZANDO THEN
    RETURN;
  END IF;

  P_VALIDAR := FPODEVALIDAR('TGFCAB');

  SELECT NVL(LIMCRED, 0) INTO V_LIMITE
    FROM TGFPAR
   WHERE CODPARC = :NEW.CODPARC;

  IF V_LIMITE = 0 THEN   -- parceiro sem limite cadastrado: regra não se aplica
    RETURN;
  END IF;

  SELECT NVL(SUM(VLRDESDOB), 0) INTO V_ABERTO
    FROM TGFFIN
   WHERE CODPARC = :NEW.CODPARC
     AND RECDESP = 1
     AND DHBAIXA IS NULL;

  IF V_ABERTO + NVL(:NEW.VLRNOTA, 0) > V_LIMITE THEN
    ERRMSG := 'Limite de crédito do parceiro ' || :NEW.CODPARC || ' excedido. '
           || 'Limite: ' || TO_CHAR(V_LIMITE, 'FM999G999G990D00')
           || ' · Em aberto + esta nota: ' || TO_CHAR(V_ABERTO + NVL(:NEW.VLRNOTA, 0), 'FM999G999G990D00');
    RAISE ERRO;
  END IF;

EXCEPTION
  WHEN ERRO THEN
    IF P_VALIDAR THEN
      RAISE_APPLICATION_ERROR(-20101, ERRMSG);
    END IF;
END;
/
