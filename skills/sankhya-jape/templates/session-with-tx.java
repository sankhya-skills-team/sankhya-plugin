// Template: operacao com JapeSession + TX manual
// Use quando: fora de contexto EJB container-managed (Cuckoo job, action, thread standalone)

import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.core.JapeSession.SessionHandle;
import br.com.sankhya.jape.core.JapeSession.TXBody;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.vo.EntityVO;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import br.com.sankhya.modelcore.util.DynamicEntityNames;

public class OperacaoExemplo {

    public void executar(final Object[] parametros) throws Exception {
        SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            hnd.execWithTX(new TXBody() {
                public void doWithTx() throws Exception {
                    EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
                    DynamicVO vo = (DynamicVO) dwf.createEmptyVO(DynamicEntityNames.MINHA_ENTIDADE);
                    // vo.setProperty(...);
                    dwf.createEntity(DynamicEntityNames.MINHA_ENTIDADE, (EntityVO) vo);
                }
            });
        } finally {
            JapeSession.close(hnd);
        }
    }
}
