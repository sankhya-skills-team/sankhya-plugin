package br.com.sankhya.customizacao.nomedemanda.helper;

// Helpers transversais (usados por vários módulos) ficam em br.com.sankhya.customizacao.helper
// Helpers específicos de um módulo ficam em br.com.sankhya.customizacao.nomedemanda.helper

import br.com.sankhya.customizacao.helper.CabecalhoNotaHelper;
import br.com.sankhya.customizacao.helper.ItemNotaHelper;
import br.com.sankhya.customizacao.helper.ParceiroHelper;
import br.com.sankhya.customizacao.utils.DwfUtils;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
import br.com.sankhya.modelcore.util.DynamicEntityNames;
import br.com.sankhya.customizacao.utils.Logger;

import java.math.BigDecimal;
import java.util.Collection;
import java.util.List;

/**
 * Helper estático de domínio — centraliza lógica de negócio, consultas e persistência.
 *
 * Regras:
 *   - Construtor privado — nunca instanciar
 *   - Todos os métodos são estáticos
 *   - Nunca abrir JapeSession aqui se chamado de dentro de evento (a sessão já está aberta)
 *   - Lançar MGEModelException para erros de negócio
 */
public class Modelo_Helper {

    private Modelo_Helper() {
        throw new UnsupportedOperationException("Não é permitido instanciar esta classe");
    }

    // -------------------------------------------------------------------------
    // Exemplos de consulta com helpers de customização
    // -------------------------------------------------------------------------

    public static void exemploCabecalhoNota(BigDecimal nuNota) throws Exception {
        // Buscar VO do cabeçalho da nota (lança se não encontrado)
        DynamicVO cabVO = CabecalhoNotaHelper.getVo(nuNota);
        BigDecimal codParc = cabVO.asBigDecimal("CODPARC");
        String tipMov = cabVO.asString("TIPMOV");

        // Buscar VO do parceiro
        DynamicVO parcVO = ParceiroHelper.getVO(codParc);
        String nomeParceiro = parcVO.asString("NOMEPARC");

        Logger.info("Nota " + nuNota + " | Parceiro: " + nomeParceiro + " | TipMov: " + tipMov);
    }

    public static void exemploItensNota(BigDecimal nuNota) throws Exception {
        // Buscar todos os itens da nota
        Collection<DynamicVO> itens = ItemNotaHelper.getVos(nuNota);
        for (DynamicVO item : itens) {
            BigDecimal codProd = item.asBigDecimal("CODPROD");
            BigDecimal qtd = item.asBigDecimal("QTDNEG");
            // processar item...
        }
    }

    // -------------------------------------------------------------------------
    // Exemplo de consulta com DwfUtils
    // -------------------------------------------------------------------------

    public static DynamicVO buscarPorCampo(String campo, Object valor) throws Exception {
        // findEntityAsVO — retorna primeiro resultado ou null (nunca lança para vazio)
        return DwfUtils.findEntityAsVO("AD_MINHAENTIDADE", campo + " = ?", new Object[]{valor});
    }

    public static List<DynamicVO> listarPorStatus(String status) throws Exception {
        // findEntitiesAsVO — retorna List (nunca null, pode ser vazio)
        return DwfUtils.findEntitiesAsVO("AD_MINHAENTIDADE", "STATUS = ?", new Object[]{status});
    }

    // -------------------------------------------------------------------------
    // Exemplo de criação e atualização com JapeFactory
    // -------------------------------------------------------------------------

    public static BigDecimal criarRegistro(BigDecimal campo1, String campo2) throws Exception {
        try {
            DynamicVO novo = JapeFactory.dao("AD_MINHAENTIDADE").create()
                    .set("CAMPO1", campo1)
                    .set("CAMPO2", campo2)
                    .set("STATUS", "P")
                    .save();

            return novo.asBigDecimal("ID_CAMPO");

        } catch (Exception e) {
            MGEModelException.throwMe(e);
        }
        return null;
    }

    public static void atualizarStatus(BigDecimal id, String novoStatus) throws Exception {
        try {
            JapeFactory.dao("AD_MINHAENTIDADE")
                    .prepareToUpdateByPK(id)
                    .set("STATUS", novoStatus)
                    .update();
        } catch (Exception e) {
            MGEModelException.throwMe(e);
        }
    }

    // -------------------------------------------------------------------------
    // Exemplo com usuário logado
    // -------------------------------------------------------------------------

    public static BigDecimal getUsuarioLogado() {
        return AuthenticationInfo.getCurrent().getUserID();
    }

    // -------------------------------------------------------------------------
    // Exemplo com DwfUtils.execWithTx — operação transacional fora de evento
    // -------------------------------------------------------------------------

    public static void processarLote(List<BigDecimal> ids) throws Exception {
        DwfUtils.execWithTx(() -> {
            for (BigDecimal id : ids) {
                JapeFactory.dao("AD_MINHAENTIDADE")
                        .prepareToUpdateByPK(id)
                        .set("PROCESSADO", "S")
                        .update();
            }
            return true;
        });
    }
}
