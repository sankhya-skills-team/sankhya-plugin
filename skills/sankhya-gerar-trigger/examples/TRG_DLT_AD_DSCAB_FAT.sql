-- Bloqueia a exclusão de demonstrativo de serviço já faturado.
-- Tabela adicional AD_DSCAB (ilustrativa): STATUS 'F' = faturado.
-- Confira o domínio de STATUS com describe_table antes de usar.
CREATE OR REPLACE TRIGGER TRG_DLT_AD_DSCAB_FAT
  BEFORE DELETE ON AD_DSCAB
  FOR EACH ROW
  WHEN (OLD.STATUS = 'F')
DECLARE
  ERRMSG    VARCHAR2(4000);
  ERRO      EXCEPTION;
  P_VALIDAR BOOLEAN;
BEGIN
  IF STP_GET_ATUALIZANDO THEN
    RETURN;
  END IF;

  P_VALIDAR := FPODEVALIDAR('AD_DSCAB');

  ERRMSG := 'Demonstrativo ' || :OLD.NUDS || ' já foi faturado e não pode ser excluído.';
  RAISE ERRO;

EXCEPTION
  WHEN ERRO THEN
    IF P_VALIDAR THEN
      RAISE_APPLICATION_ERROR(-20101, ERRMSG);
    END IF;
END;
/
