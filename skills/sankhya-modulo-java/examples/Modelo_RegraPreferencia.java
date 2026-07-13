package br.com.sankhya.customizacao.nomedemanda.regra;

import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.comercial.AtributosRegras;
import br.com.sankhya.modelcore.comercial.ContextoRegra;
import br.com.sankhya.modelcore.comercial.Regra;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;

/**
 * Regra de negócio registrada via preferência do sistema (interface Regra).
 *
 * Diferente de RegraNegocioJava, esta interface é registrada via preferência:
 *   Preferência: MODREGCENTRAL
 *   Valor      : {codTipOper}@br.com.sankhya.customizacao.nomedemanda.regradenegocio.NomeRegraPreferencia
 *
 * Exemplo de valor: 10@br.com.sankhya.customizacao.nomedemanda.regradenegocio.NomeRegraPreferencia
 */
public class Modelo_RegraPreferencia implements Regra {

    @Override
    public void afterUpdate(ContextoRegra arg0) throws Exception {
        try {
            // Executar apenas na confirmação
            if (!JapeSession.getPropertyAsBoolean(AtributosRegras.CONFIRMANDO, Boolean.FALSE)) {
                return;
            }

            String tipMov = arg0.getPrePersistEntityState().getNewVO().asString("TIPMOV");
            BigDecimal nuNota = BigDecimalUtil.getValueOrZero(
                arg0.getPrePersistEntityState().getNewVO().asBigDecimal("NUNOTA"));

            // lógica principal aqui
			// NomeService nomeService = new NomeService();
            // nomeService.processar(nuNota, tipMov);

        } catch (Exception ex) {
            throw MGEModelException.prettyMsg("Erro na regra de negócio: <br>" + ex.getMessage(), ex);
        }
    }

    @Override public void beforeInsert(ContextoRegra arg0) throws Exception {}
    @Override public void afterInsert(ContextoRegra arg0) throws Exception {}
    @Override public void beforeUpdate(ContextoRegra arg0) throws Exception {}
    @Override public void beforeDelete(ContextoRegra arg0) throws Exception {}
    @Override public void afterDelete(ContextoRegra arg0) throws Exception {}
}
