package br.com.sankhya.dstech.nomedemanda.regra;

import br.com.sankhya.dstech.helper.CabecalhoNotaHelper;
import br.com.sankhya.dstech.utils.MessageUtils;
import br.com.sankhya.extensions.regrasnegocio.ContextoRegra;
import br.com.sankhya.extensions.regrasnegocio.RegraNegocioJava;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.comercial.AtributosRegras;
import br.com.sankhya.modelcore.util.DynamicEntityNames;
import br.com.sankhya.jape.wrapper.JapeFactory;

import java.math.BigDecimal;
import java.util.Collection;

/**
 * Regra de negócio executada no ciclo de confirmação/faturamento de nota.
 *
 * Configuração no Sankhya:
 *   Menu: Configurações → Regras de Negócio
 *   Entidade    : CabecalhoNota (ou entidade alvo)
 *   Classe Java : br.com.sankhya.dstech.nomedemanda.regra.NomeRegra
 */
public class Modelo_RegraNegocio implements RegraNegocioJava {

    /** Indica se a execução foi bem-sucedida. */
    Boolean sucesso;

    /** Mensagem de erro ou retorno da execução. */
    String msgError;

    @Override
    public void executa(ContextoRegra ctx) throws MGEModelException {
        sucesso = false;
        msgError = "";

        processa(ctx);

        ctx.setSucesso(sucesso);
        if (!msgError.isEmpty()) {
            ctx.setMensagem(msgError);
            MessageUtils.showInfo(msgError);
        } else if (sucesso) {
            ctx.setMensagem("");
        } else {
            ctx.setMensagem(msgError);
            MessageUtils.showInfo(msgError);
        }
        ctx.setCodUsuLib(0);
    }

    public void processa(ContextoRegra ctx) throws MGEModelException {
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            hnd.setFindersMaxRows(-1);

            // Executar apenas na confirmação do cabeçalho (não item, não duplicação, não mov. financeira)
            if (isItem() || !ehConfirmacao() || ehDuplicacao() || ehMovFin()) {
                sucesso = true;
                return;
            }

            BigDecimal nuNota = ctx.getNunota();

            DynamicVO notaVO = CabecalhoNotaHelper.getVo(nuNota);
            String tipMov = notaVO.asString("TIPMOV");

            if (!"V".equals(tipMov)) {
                sucesso = false;
                msgError = "Esta regra aplica-se apenas a notas de venda.";
                // Use throw para forçar rollback; sem throw, permite liberação de limite:
                // throw new MGEModelException(msgError);
                return;
            }

            // lógica principal aqui
            // NomeService nomeService = new NomeService();
			// nomeService.validar(nuNota, notaVO);

            sucesso = true;

        } catch (MGEModelException e) {
            sucesso = false;
            msgError = "Erro no processamento: " + e.getMessage();
            throw e;
        } catch (Exception e) {
            sucesso = false;
            msgError = "Erro inesperado: " + e.getMessage();
            throw new MGEModelException(e.getMessage(), e.getCause());
        } finally {
            JapeSession.close(hnd);
        }
    }

    // -------------------------------------------------------------------------
    // Verificadores de contexto de sessão
    // -------------------------------------------------------------------------

    /** Retorna true se a regra está sendo executada no contexto de um item (não cabeçalho). */
    public static boolean isItem() {
        return JapeSession.getPropertyAsBoolean("isItem", Boolean.FALSE);
    }

    /** Retorna true se a nota está sendo confirmada. */
    public static boolean ehConfirmacao() {
        return JapeSession.getPropertyAsBoolean(AtributosRegras.CONFIRMANDO, Boolean.FALSE);
    }

    /** Retorna true se o contexto é de movimentação financeira (Central Financeira). */
    public static boolean ehMovFin() {
        return JapeSession.getPropertyAsBoolean(AtributosRegras.CENTRAL_FINANCEIRO, Boolean.FALSE);
    }

    /** Retorna true se a nota está sendo duplicada. */
    public static boolean ehDuplicacao() {
        return JapeSession.getPropertyAsBoolean(AtributosRegras.NUNOTA_SENDO_DUPLICADA, Boolean.FALSE);
    }

    // -------------------------------------------------------------------------
    // Verificação de liberação de limite
    // -------------------------------------------------------------------------

    /** Verifica se existe liberação de limite para a nota e evento informados. */
    public int existeLibLimite(BigDecimal nuNota, BigDecimal codEvento) throws MGEModelException {
        try {
            JapeWrapper libDAO = JapeFactory.dao(DynamicEntityNames.LIBERACAO_LIMITE);
            Collection<DynamicVO> libVO = JapeFactory.dao(DynamicEntityNames.LIBERACAO_LIMITE)
				.find("NUCHAVE = ? AND EVENTO = ? AND TABELA = 'TGFCAB'",
              new Object[]{nuNota, codEvento});
            return libVO == null ? 0 : libVO.size();
        } catch (Exception e) {
            MGEModelException.throwMe(e);
        }
        return 0;
    }

    /** Retorna true se existe liberação válida (VLRLIBERADO = VLRATUAL, VLRLIBERADO > 0, DHLIB não nulo). */
    public boolean estaLiberado(BigDecimal nuNota, BigDecimal codEvento) throws MGEModelException {
        try {
            JapeWrapper libDAO = JapeFactory.dao(DynamicEntityNames.LIBERACAO_LIMITE);
            Collection<DynamicVO> libVOs = libDAO.find(
                "NUCHAVE = ? AND EVENTO = ? AND TABELA = 'TGFCAB'" +
                " AND VLRLIBERADO = VLRATUAL AND VLRLIBERADO > 0 AND DHLIB IS NOT NULL",
                new Object[]{nuNota, codEvento});
            return !libVOs.isEmpty();
        } catch (Exception e) {
            MGEModelException.throwMe(e);
        }
        return false;
    }
}
