package br.com.sankhya.dstech.nomedemanda.eventos.external;

import br.com.sankhya.extensions.eventoprogramavel.EventoProgramavelJava;
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.event.PersistenceEvent;
import br.com.sankhya.jape.event.TransactionContext;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.custommodule.CustomModuleLoader;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import br.com.sankhya.modelcore.util.MGECoreParameter;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;

/**
 * Classe registrada no evento — delega para outro JAR via CustomModuleLoader.
 *
 * Artifício para que a autorização de customização seja realizada uma única vez
 * no módulo externo (proxy), enquanto o código real fica em outro módulo.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA
 *   Tipo        : Before Insert, Before Update
 *   Classe Java : br.com.sankhya.dstech.nomedemanda.eventos.external.NomeEventoExternal
 *
 * Preferência do Sistema:
 *   Nome  : AD_MODEVENTOFINAL
 *   Valor : {ID do módulo Java com a classe de destino}
 */
public class Modelo_EventoExternal implements EventoProgramavelJava {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        chamarEventoExterno(event);
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        chamarEventoExterno(event);
    }

    @Override public void beforeDelete(PersistenceEvent event) throws Exception {}
    @Override public void afterInsert(PersistenceEvent event) throws Exception {}
    @Override public void afterUpdate(PersistenceEvent event) throws Exception {}
    @Override public void afterDelete(PersistenceEvent event) throws Exception {}
    @Override public void beforeCommit(TransactionContext tranCtx) throws Exception {}

    private void chamarEventoExterno(PersistenceEvent pe) throws Exception {
        String nomePreferencia = "AD_MODEVENTOFINAL";
        int codModuloJava = MGECoreParameter.getParameterAsInt(nomePreferencia);
        String classeAlvo = "br.com.sankhya.dstech.nomedemanda.eventos.NomeEvento";

        EntityFacade ef = EntityFacadeFactory.getDWFFacade();
        BigDecimal moduleID = BigDecimalUtil.getValueOrZero(BigDecimal.valueOf(codModuloJava));

        if (moduleID.compareTo(BigDecimal.ZERO) == 0) {
            throw new MGEModelException(
                "O parâmetro \"" + nomePreferencia + "\" não está configurado com o módulo Java.");
        }

        // Carrega a classe do outro JAR e chama via reflection (evento usa executar())
        Object obj = CustomModuleLoader.getClass(ef, moduleID, classeAlvo).newInstance();
        obj.getClass().getMethod("executar", PersistenceEvent.class).invoke(obj, pe);
    }
}
