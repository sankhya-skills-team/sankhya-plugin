package br.com.sankhya.dstech.nomedemanda.service;

import br.com.sankhya.dstech.nomedemanda.exception.NomeModuloException;
import br.com.sankhya.jape.vo.DynamicVO;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * Service de NomeDemanda.
 *
 * Regras de negócio puras: validações, cálculos, transformações.
 * NÃO acessa banco. NÃO chama repository. NÃO chama MGEModelException.
 * Recebe dados já carregados pelo component/ e opera sobre eles.
 * Lança NomeModuloException para erros de negócio.
 */
public class NomeService {

    // -------------------------------------------------------------------------
    // Exemplo 1 — Validação de estado
    // O DynamicVO já foi carregado pelo component/ via repository/ antes desta chamada.
    // -------------------------------------------------------------------------

    /**
     * Valida se o registro pode ser executado no estado atual.
     *
     * @param vo DynamicVO carregado pelo component
     * @throws NomeModuloException se o estado não permitir a operação
     */
    public void validarParaExecucao(DynamicVO vo) throws NomeModuloException {
        String status = vo.asString("STATUS");
        if ("F".equals(status)) {
            throw NomeModuloException.statusInvalido(status, "executar operação");
        }
    }

    // -------------------------------------------------------------------------
    // Exemplo 2 — Cálculo puro (sem acesso a dados)
    // -------------------------------------------------------------------------

    /**
     * Calcula o desconto sobre um valor.
     *
     * @param valor      valor base
     * @param percentual percentual de desconto (ex: 10 para 10%)
     * @return valor do desconto arredondado em 2 casas
     */
    public BigDecimal calcularDesconto(BigDecimal valor, BigDecimal percentual) {
        if (BigDecimalUtil.isNullOrZero(valor) || BigDecimalUtil.isNullOrZero(percentual)) {
            return BigDecimal.ZERO;
        }
        return valor.multiply(percentual).divide(new BigDecimal("100"), 2, RoundingMode.HALF_UP);
    }

    // -------------------------------------------------------------------------
    // Exemplo 3 — Validação com múltiplos VOs
    // O component/ carrega pai e filho antes de chamar este service.
    // -------------------------------------------------------------------------

    /**
     * Valida se o registro filho pode ser vinculado ao pai.
     *
     * @param voFilho VO do registro filho
     * @param voPai   VO do registro pai, já carregado pelo component
     * @throws NomeModuloException se o pai estiver em estado que não permite vínculo
     */
    public void validarVinculo(DynamicVO voFilho, DynamicVO voPai) throws NomeModuloException {
        String statusPai = voPai.asString("STATUS");
        if ("F".equals(statusPai)) {
            throw NomeModuloException.statusInvalido(statusPai,
                    "vincular registro ID " + voFilho.asBigDecimal("ID"));
        }
    }
}
