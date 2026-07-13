package br.com.sankhya.customizacao.nomedemanda.actionbutton;

import br.com.sankhya.customizacao.nomedemanda.component.NomeComponent;
import br.com.sankhya.customizacao.nomedemanda.exception.NomeModuloException;
import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;

/**
 * Botão de ação na tela de NomeTela (AD_NOMETABELA).
 *
 * Responsabilidade: validar interação do usuário (seleção, confirmação),
 * abrir sessão e delegar para NomeComponent. Sem regras de negócio.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA
 *   Classe Java : br.com.sankhya.customizacao.nomedemanda.actionbutton.NomeAction
 *   Descrição   : Texto exibido no menu "Ações"
 */
public class Modelo_ActionButton implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao ctx) throws Exception {
        // 1. Validar seleção
        if (ctx.getLinhas().length == 0) {
            ctx.setMensagemRetorno("Selecione ao menos um registro!");
            return;
        }
        if (ctx.getLinhas().length > 1) {
            ctx.setMensagemRetorno("Selecione apenas um registro!");
            return;
        }

        // 2. Confirmação prévia (remover se não necessário)
        boolean confirmado = ctx.confirmarSimNao("Confirmar", "Deseja executar esta operação?", 1);
        if (!confirmado) {
            ctx.setMensagemRetorno("Operação cancelada.");
            return;
        }

        // 3. Extrair chave do registro selecionado
        BigDecimal id = BigDecimalUtil.getBigDecimal(ctx.getLinhas()[0].getCampo("ID_CAMPO"));

        // 4. Delegar para component — sem lógica de negócio aqui
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();

            NomeComponent component = new NomeComponent();
            String resultado = component.executarOperacao(id);

            ctx.setMensagemRetorno(resultado);

        } catch (NomeModuloException e) {
            throw MGEModelException.prettyMsg(e.getMessage(), e);
        } catch (Exception e) {
            throw MGEModelException.prettyMsg("Erro inesperado ao executar operação: <br>" + e.getMessage(), e);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
