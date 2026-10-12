-- Botão de Ação (Rotina no Banco de dados) — com confirmação, parâmetro e UPDATE.
-- Encerra as ordens de serviço selecionadas numa tabela adicional AD_OSCAB
-- (colunas: NUOS, STATUS, OBSENCERRA, DHENCERRA, CODUSUENCERRA).
-- Parâmetro do formulário do botão: MOTIVO (texto).
-- Sem COMMIT: a transação é do Sankhya.
CREATE OR REPLACE PROCEDURE STP_ENCERRA_OS (
  P_CODUSU    NUMBER,
  P_IDSESSAO  VARCHAR2,
  P_QTDLINHAS NUMBER,
  P_MENSAGEM  OUT VARCHAR2
) AS
  V_NUOS    NUMBER;
  V_STATUS  VARCHAR2(1);
  V_MOTIVO  VARCHAR2(4000);
  V_QTD     NUMBER := 0;
BEGIN
  IF P_QTDLINHAS = 0 THEN
    RAISE_APPLICATION_ERROR(-20001, 'Selecione ao menos uma OS.');
  END IF;

  V_MOTIVO := ACT_TXT_PARAM(P_IDSESSAO, 'MOTIVO');
  IF V_MOTIVO IS NULL THEN
    RAISE_APPLICATION_ERROR(-20002, 'Informe o motivo do encerramento.');
  END IF;

  -- Pergunta uma vez, antes de alterar qualquer linha (sequencia 1).
  IF ACT_ESCOLHER_SIMNAO('Encerrar OS',
                         'Encerrar ' || P_QTDLINHAS || ' OS selecionada(s)?',
                         P_IDSESSAO, 1) <> 'S' THEN
    P_MENSAGEM := 'Operação cancelada.';
    RETURN;
  END IF;

  FOR I IN 1..P_QTDLINHAS LOOP
    V_NUOS   := ACT_INT_FIELD(P_IDSESSAO, I, 'NUOS');
    V_STATUS := ACT_TXT_FIELD(P_IDSESSAO, I, 'STATUS');

    IF V_NUOS IS NULL THEN
      RAISE_APPLICATION_ERROR(-20003, 'Campo NUOS não disponível na grade.');
    END IF;
    IF V_STATUS = 'E' THEN
      RAISE_APPLICATION_ERROR(-20004, 'OS ' || V_NUOS || ' já está encerrada.');
    END IF;

    UPDATE AD_OSCAB
       SET STATUS        = 'E',
           OBSENCERRA    = V_MOTIVO,
           DHENCERRA     = SYSDATE,
           CODUSUENCERRA = P_CODUSU
     WHERE NUOS = V_NUOS;

    V_QTD := V_QTD + SQL%ROWCOUNT;
  END LOOP;

  P_MENSAGEM := V_QTD || ' OS encerrada(s).';
END;
/
