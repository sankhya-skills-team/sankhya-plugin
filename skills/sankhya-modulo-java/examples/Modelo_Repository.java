package br.com.sankhya.customizacao.nomedemanda.repository;

import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.jape.wrapper.JapeWrapper;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * Repository de NomeDemanda.
 *
 * Responsável exclusivamente por acesso a dados da entidade AD_NOMETABELA.
 * Sem regras de negócio. Sem lançamento de NomeModuloException.
 *
 * Regra JAPE vs NativeSql:
 *   - Usar JAPE (JapeFactory) quando quiser que outros eventos Sankhya sejam disparados.
 *   - Usar NativeSql/JdbcWrapper quando explicitamente NÃO quiser disparar outros eventos.
 *   Nunca usar NativeSql para "economizar código".
 */
public class NomeRepository {

    private static final String ENTIDADE = "AD_NOMETABELA";

    // -------------------------------------------------------------------------
    // Leitura
    // -------------------------------------------------------------------------

    /**
     * Busca registro por chave primária.
     * Retorna null se não encontrado — quem decide o que fazer é o service.
     */
    public DynamicVO buscarPorId(BigDecimal id) throws Exception {
        return JapeFactory.dao(ENTIDADE).findByPK(id);
    }

    /**
     * Lista registros por status.
     * Retorna lista vazia se não houver resultados — nunca null.
     */
    public List<DynamicVO> listarPorStatus(String status) throws Exception {
        Collection<DynamicVO> resultado = JapeFactory.dao(ENTIDADE)
                .find("this.STATUS = ?", new Object[]{status});

        if (resultado == null) return new ArrayList<>();
        return new ArrayList<>(resultado);
    }

    // -------------------------------------------------------------------------
    // Escrita via JAPE — dispara eventos Sankhya
    // -------------------------------------------------------------------------

    /**
     * Atualiza o status do registro via JAPE.
     * Dispara beforeUpdate/afterUpdate da entidade.
     * Usar quando a atualização deve acionar outros eventos registrados.
     */
    public void atualizarStatus(BigDecimal id, String novoStatus) throws Exception {
        JapeFactory.dao(ENTIDADE)
                .prepareToUpdateByPK(id)
                .set("STATUS", novoStatus)
                .update();
    }

    /**
     * Insere novo registro via JAPE.
     * Retorna o DynamicVO com a chave gerada.
     */
    public DynamicVO inserir(BigDecimal codEmp, String descricao) throws Exception {
        return JapeFactory.dao(ENTIDADE).create()
                .set("CODEMP", codEmp)
                .set("DESCRICAO", descricao)
                .set("STATUS", "A")
                .save();
    }

    // -------------------------------------------------------------------------
    // Escrita via NativeSql — NÃO dispara eventos Sankhya
    // Usar apenas quando o objetivo explícito é não disparar outros eventos.
    // -------------------------------------------------------------------------

    /**
     * Atualiza status diretamente via SQL — sem disparar eventos.
     * Usar quando a atualização é interna/técnica e não deve acionar outros listeners.
     *
     * Requer JdbcWrapper da sessão ou do PersistenceEvent.
     * Em actionbutton: obter via JapeSession.
     * Em event: obter via pEvent.getJdbcWrapper().
     */
    public void atualizarStatusSemEvento(BigDecimal id, String novoStatus,
                                          JapeSession.SessionHandle hnd) throws Exception {
        hnd.getJdbcWrapper().executeUpdate(
                "UPDATE AD_NOMETABELA SET STATUS = ? WHERE ID = ?",
                new Object[]{novoStatus, id});
    }
}
