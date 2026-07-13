package br.com.sankhya.customizacao.nomedemanda.job;

import br.com.sankhya.customizacao.nomedemanda.component.NomeComponent;
import br.com.sankhya.customizacao.utils.Logger;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import org.cuckoo.core.ScheduledAction;
import org.cuckoo.core.ScheduledActionContext;

/**
 * Job agendado — executado periodicamente pelo agendador Cuckoo.
 *
 * Responsabilidade: abrir sessão, delegar para NomeComponent, fechar sessão.
 * Sem regras de negócio — toda a lógica fica no component/.
 *
 * Configuração no Sankhya:
 *   Classe Java : br.com.sankhya.customizacao.nomedemanda.job.NomeJob
 *   Frequência  : definida no menu Ações Agendadas
 */
public class Modelo_Job implements ScheduledAction {

    @Override
    public void onTime(ScheduledActionContext arg0) {
        Logger.info("Iniciando NomeJob.");

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            hnd.setFindersMaxRows(-1);

            NomeComponent component = new NomeComponent();
            component.processarPendentes();

            Logger.info("NomeJob concluido com sucesso.");

        } catch (MGEModelException e) {
            Logger.error("Erro de negocio em NomeJob.", e);
        } catch (Exception e) {
            Logger.error("Erro inesperado em NomeJob.", e);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
