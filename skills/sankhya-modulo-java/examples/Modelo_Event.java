package br.com.sankhya.dstech.nomedemanda.event;

import br.com.sankhya.extensions.eventoprogramavel.EventoProgramavelJava;
import br.com.sankhya.jape.event.PersistenceEvent;
import br.com.sankhya.jape.event.TransactionContext;
import br.com.sankhya.jape.vo.DynamicVO;

/**
 * Evento registrado na entidade AD_NOMETABELA.
 *
 * Descrição do que este evento faz.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA
 *   Tipo        : Before Insert, Before Update
 *   Classe Java : br.com.sankhya.dstech.nomedemanda.event.NomeEvento
 *   Módulo      : dstech-nomemodulo
 */
public class Modelo_Evento implements EventoProgramavelJava {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        processar(event);
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        processar(event);
    }

    @Override public void beforeDelete(PersistenceEvent event) throws Exception {}
    @Override public void afterInsert(PersistenceEvent event) throws Exception {}
    @Override public void afterUpdate(PersistenceEvent event) throws Exception {}
    @Override public void afterDelete(PersistenceEvent event) throws Exception {}
    @Override public void beforeCommit(TransactionContext tranCtx) throws Exception {}

    private void processar(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();

        // Operação simples na própria entidade — direto no evento, sem component
        // vo.setProperty("CAMPO", valor);

        // Verificar campo opcional antes de acessar
        if (vo.containsProperty("CAMPO_OPCIONAL")) {
            BigDecimal valor = vo.asBigDecimal("CAMPO_OPCIONAL");
            // usar valor...
        }

        // Operação que envolve outra entidade ou lógica de negócio — via component
        // NomeComponent component = new NomeComponent();
        // component.processarEvento(vo.asBigDecimal("ID_CAMPO"), vo);
    }
}
