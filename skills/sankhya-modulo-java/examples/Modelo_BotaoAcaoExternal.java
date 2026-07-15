package br.com.sankhya.customizacao.nomedemanda.botaoacao.external;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.custommodule.CustomModuleLoader;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import br.com.sankhya.modelcore.util.MGECoreParameter;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;

/**
 * Classe registrada no botão de ação — delega para outro JAR via CustomModuleLoader.
 *
 * Artifício para que a autorização de customização seja realizada uma única vez
 * no módulo externo (proxy), enquanto o código real fica em outro módulo.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA
 *   Classe Java : br.com.sankhya.customizacao.nomedemanda.botaoacao.external.NomeActionExternal
 *
 * Preferência do Sistema:
 *   Nome  : AD_MODACAOFINAL
 *   Valor : {ID do módulo Java com a classe de destino}
 */
public class Modelo_BotaoAcaoExternal implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao contexto) throws Exception {
        String nomePreferencia = "AD_MODACAOFINAL";
        int codModuloJava = MGECoreParameter.getParameterAsInt(nomePreferencia);
        String classeAlvo = "br.com.sankhya.customizacao.nomedemanda.botaoacao.NomeAction";

        EntityFacade ef = EntityFacadeFactory.getDWFFacade();
        BigDecimal moduleID = BigDecimalUtil.getValueOrZero(BigDecimal.valueOf(codModuloJava));

        if (moduleID.compareTo(BigDecimal.ZERO) == 0) {
            throw new MGEModelException(
                "O parâmetro \"" + nomePreferencia + "\" não está configurado com o módulo Java.");
        }

        // Cast direto — botão de ação usa doAction(), não precisa de reflection
        AcaoRotinaJava acao = (AcaoRotinaJava)
                CustomModuleLoader.getClass(ef, moduleID, classeAlvo).newInstance();
        acao.doAction(contexto);
    }
}
