package br.com.sankhya.dstech.nomedemanda.botaoacao;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;

/**
 * Botão de ação na tela de NomeTela (AD_NOMETABELA).
 *
 * Descrição do que este botão faz.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA
 *   Classe Java : br.com.sankhya.dstech.nomedemanda.botaoacao.NomeAction
 *   Descrição   : Texto exibido no menu "Ações"
 */
public class Modelo_BotaoAcao implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao ctx) throws Exception {
        // Validar seleção
        if (ctx.getLinhas().length == 0) {
            ctx.setMensagemRetorno("Selecione ao menos um registro!");
            return;
        }
        if (ctx.getLinhas().length > 1) {
            ctx.setMensagemRetorno("Selecione apenas um registro!");
            return;
        }

        // Confirmação prévia (opcional — remover se não necessário)
        boolean confirmado = ctx.confirmarSimNao("Confirmar", "Deseja executar esta operação?", 1);
        if (!confirmado) {
            ctx.setMensagemRetorno("Operação cancelada.");
            return;
        }

        BigDecimal id = BigDecimalUtil.getBigDecimal(ctx.getLinhas()[0].getCampo("ID_CAMPO"));

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();

            // Delegar para helper — sem lógica de negócio aqui
            String resultado = NomeModuloHelper.executarOperacao(id);

            ctx.setMensagemRetorno(resultado);

        } catch (Exception e) {
            throw MGEModelException.prettyMsg("Erro ao executar operação: <br>" + e.getMessage(), e);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
