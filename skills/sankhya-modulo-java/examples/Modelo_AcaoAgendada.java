package br.com.sankhya.dstech.nomedemanda.acoesagendadas;

import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import org.apache.log4j.Logger;
import org.cuckoo.core.ScheduledAction;
import org.cuckoo.core.ScheduledActionContext;

/**
 * Ação agendada — executada periodicamente pelo agendador Cuckoo.
 *
 * Configuração no Sankhya:
 *   Classe Java : br.com.sankhya.dstech.nomedemanda.acoesagendadas.NomeAgendada
 *   Frequência  : definida no menu Ações Agendadas
 */
public class Modelo_AcaoAgendada implements ScheduledAction {

    private static final Logger logger = Logger.getLogger(Modelo_AcaoAgendada.class);

    @Override
    public void onTime(ScheduledActionContext arg0) {
        logger.info("Iniciando processamento agendado: NomeAgendada");

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            hnd.setFindersMaxRows(-1);

            // Delegar lógica para helper
            // NomeModuloHelper.processarLote();

            logger.info("Processamento agendado concluído com sucesso.");

        } catch (MGEModelException e) {
            logger.error("Erro de negócio no processamento agendado: " + e.getMessage(), e);
        } catch (Exception e) {
            logger.error("Erro inesperado no processamento agendado: " + e.getMessage(), e);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
