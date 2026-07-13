# Regra de Negócio e Ação Agendada

## RegraNegocioJava — Tela "Regras de Negócio"

Registrada na tela **Regras de Negócio** do Sankhya. Executa lógica customizada no ciclo de vida
de documentos comerciais, com acesso ao resultado e à possibilidade de interagir com liberações de limite.

### Interface `RegraNegocioJava`

```java
import br.com.sankhya.extensions.regrasnegocio.RegraNegocioJava;
import br.com.sankhya.extensions.regrasnegocio.ContextoRegra;

public class NomeRegra implements RegraNegocioJava {

    @Override
    public void executa(ContextoRegra ctx) throws MGEModelException {
        // implementação
        ctx.setSucesso(true);
        ctx.setMensagem("");
        ctx.setCodUsuLib(0);
    }
}
```

### `ContextoRegra`

| Método | Descrição |
|---|---|
| `ctx.getNunota()` | Número da nota em processamento |
| `ctx.setSucesso(boolean)` | `true` = passou, `false` = falhou/pendente liberação |
| `ctx.setMensagem(String)` | Mensagem exibida ao usuário |
| `ctx.setCodUsuLib(int)` | Código do usuário liberador (0 = não exige liberação) |

---

## Padrão Completo — RegraNegocioJava com Liberação de Limite

```java
package br.com.sankhya.customizacao.nomedemanda.regra;

import br.com.sankhya.customizacao.utils.MessageUtils;
import br.com.sankhya.extensions.regrasnegocio.ContextoRegra;
import br.com.sankhya.extensions.regrasnegocio.RegraNegocioJava;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.comercial.AtributosRegras;
import br.com.sankhya.modelcore.util.DynamicEntityNames;

import java.math.BigDecimal;
import java.util.Collection;

/**
 * Regra de negócio registrada na tela Regras de Negócio do Sankhya.
 *
 * Configuração no Sankhya:
 *   Classe Java : br.com.sankhya.customizacao.nomedemanda.regra.NomeRegra
 *   Evento      : ID do evento cadastrado em Regras de Negócio
 */
public class NomeRegra implements RegraNegocioJava {

    Boolean sucesso;
    String msgError;

    @Override
    public void executa(ContextoRegra ctx) throws MGEModelException {

        sucesso  = false;
        msgError = "";

        processa(ctx);

        ctx.setSucesso(sucesso);
        if (!msgError.isEmpty()) {
            ctx.setMensagem(msgError);
            MessageUtils.showInfo(msgError);
        } else if (sucesso) {
            ctx.setMensagem("");
        } else {
            ctx.setMensagem(msgError);
            MessageUtils.showInfo(msgError);
        }
        ctx.setCodUsuLib(0);
    }

    private void processa(ContextoRegra ctx) throws MGEModelException {
        JapeSession.SessionHandle hnd = null;

        try {
            hnd = JapeSession.open();
            hnd.setFindersMaxRows(-1);

            // Validações de contexto — executar somente na confirmação
            if (isItem() || !ehConfirmacao() || ehDuplicacao() || ehMovFin()) {
                sucesso = true;
                return;
            }

            BigDecimal nuNota = ctx.getNunota();

            DynamicVO notaVO = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);
            if (notaVO == null) throw new MGEModelException("Nota não encontrada: " + nuNota);
            String tipMov = notaVO.asString("TIPMOV");

            if ("V".equals(tipMov)) {
                // lógica específica de venda
                sucesso = true;
            } else {
                sucesso = false;
                msgError = "<br>Tipo de movimento não suportado por esta regra.";
            }

        } catch (MGEModelException e) {
            sucesso  = false;
            msgError = "Ocorreu um erro no processamento: " + e.getMessage();
            throw e;
        } catch (Exception e) {
            sucesso  = false;
            msgError = "Ocorreu um erro inesperado: " + e.getMessage();
            throw new MGEModelException(e.getMessage(), e.getCause());
        } finally {
            JapeSession.close(hnd);
        }
    }

    // Verificadores de contexto (usando AtributosRegras)
    public static boolean isItem() {
        return JapeSession.getPropertyAsBoolean("isItem", Boolean.FALSE);
    }

    public static boolean ehConfirmacao() {
        return JapeSession.getPropertyAsBoolean(AtributosRegras.CONFIRMANDO, Boolean.FALSE);
    }

    public static boolean ehMovFin() {
        return JapeSession.getPropertyAsBoolean(AtributosRegras.CENTRAL_FINANCEIRO, Boolean.FALSE);
    }

    public static boolean ehDuplicacao() {
        return JapeSession.getPropertyAsBoolean(AtributosRegras.NUNOTA_SENDO_DUPLICADA, Boolean.FALSE);
    }

    // Verificar liberação de limite existente
    public int existeLibLimite(BigDecimal nuNota, BigDecimal codEvento) throws MGEModelException {
        try {
            Collection<DynamicVO> libVO = JapeFactory.dao(DynamicEntityNames.LIBERACAO_LIMITE)
                    .find("NUCHAVE = ? AND EVENTO = ? AND TABELA = 'TGFCAB'",
                            new Object[]{nuNota, codEvento});
            return libVO == null ? 0 : libVO.size();
        } catch (Exception e) {
            MGEModelException.throwMe(e);
        }
        return 0;
    }

    // Verificar se a liberação está aprovada
    public boolean estaLiberado(BigDecimal nuNota, BigDecimal codEvento) throws MGEModelException {
        try {
            DynamicVO libVO = JapeFactory.dao(DynamicEntityNames.LIBERACAO_LIMITE)
                    .findOne("NUCHAVE = ? AND EVENTO = ? AND TABELA = 'TGFCAB'" +
                                    " AND VLRLIBERADO = VLRATUAL AND VLRLIBERADO > 0 AND DHLIB IS NOT NULL",
                            new Object[]{nuNota, codEvento});
            return libVO != null;
        } catch (Exception e) {
            MGEModelException.throwMe(e);
        }
        return false;
    }
}
```

---

## Interface `Regra` — Alternativa para Regras via Preferência

Registrada como preferência no sistema (ex: `10@br.com.sankhya.customizacao.nomedemanda.regra`).
Usada quando a regra deve ser configurável por preferência de módulo Java.

```java
package br.com.sankhya.customizacao.nomedemanda.regra;

import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.comercial.AtributosRegras;
import br.com.sankhya.modelcore.comercial.ContextoRegra;
import br.com.sankhya.modelcore.comercial.Regra;
import com.sankhya.util.BigDecimalUtil;
import java.math.BigDecimal;

/**
 * Regra registrada via preferência: NOME_PREFERENCIA = "10@br.com.sankhya.customizacao..."
 *
 * Configuração no Sankhya:
 *   Preferência : NOME_PREFERENCIA
 *   Valor       : {codModulo}@br.com.sankhya.customizacao.nomedemanda.regra.NomeRegraPreferencia
 */
public class NomeRegraPreferencia implements Regra {

    @Override
    public void afterUpdate(ContextoRegra ctx) throws Exception {
        try {
            if (!JapeSession.getPropertyAsBoolean(AtributosRegras.CONFIRMANDO, Boolean.FALSE)) {
                return; // só na confirmação
            }

            String tipMov = ctx.getPrePersistEntityState().getNewVO().asString("TIPMOV");
            BigDecimal nuNota = BigDecimalUtil.getValueOrZero(
                    ctx.getPrePersistEntityState().getNewVO().asBigDecimal("NUNOTA"));

            // lógica aqui
        } catch (Exception ex) {
            throw MGEModelException.prettyMsg("Erro na regra: <br>" + ex.getMessage(), ex);
        }
    }

    @Override public void afterDelete(ContextoRegra ctx) throws Exception {}
    @Override public void afterInsert(ContextoRegra ctx) throws Exception {}
    @Override public void beforeDelete(ContextoRegra ctx) throws Exception {}
    @Override public void beforeInsert(ContextoRegra ctx) throws Exception {}
    @Override public void beforeUpdate(ContextoRegra ctx) throws Exception {}
}
```

---

## AtributosRegras — Constantes de Contexto

```java
import br.com.sankhya.modelcore.comercial.AtributosRegras;

// Contextos disponíveis em JapeSession
AtributosRegras.CONFIRMANDO               // nota sendo confirmada
AtributosRegras.CENTRAL_FINANCEIRO        // contexto de movimentação financeira
AtributosRegras.NUNOTA_SENDO_DUPLICADA    // nota sendo duplicada
```

---

## ScheduledAction — Ação Agendada (Cuckoo)

Tarefa agendada registrada no Sankhya via menu **Ações Agendadas**. Interface `ScheduledAction`
da biblioteca `org.cuckoo.core`.

```java
package br.com.sankhya.customizacao.nomedemanda.job;

import org.cuckoo.core.ScheduledAction;
import org.cuckoo.core.ScheduledActionContext;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.modelcore.MGEModelException;
import org.apache.log4j.Logger;

/**
 * Ação agendada — executada periodicamente pelo Sankhya.
 *
 * Configuração no Sankhya:
 *   Menu        : Gerenciamento → Ações Agendadas
 *   Classe Java : br.com.sankhya.customizacao.nomedemanda.job.NomeAgendada
 *   Frequência  : configurada na própria tela (CRON ou intervalo)
 */
public class NomeAgendada implements ScheduledAction {

    private static final Logger logger = Logger.getLogger(NomeAgendada.class);

    @Override
    public void onTime(ScheduledActionContext arg0) {
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            hnd.setFindersMaxRows(-1);

            logger.info("Iniciando processamento agendado...");

            NomeService nomeService = new NomeService();
			nomeService.processarLote();

            logger.info("Processamento agendado finalizado.");

        } catch (Exception e) {
            logger.error("Erro no processamento agendado", e);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
```

### Diferenças do @Job (Addon Studio)

| Aspecto | ScheduledAction (Módulo Java) | @Job (Addon Studio) |
|---|---|---|
| Interface | `org.cuckoo.core.ScheduledAction` | `br.com.sankhya.studio.annotations.Job` |
| Método | `onTime(ScheduledActionContext)` | `onSchedule()` |
| Configuração | Manual — tela Ações Agendadas | Automática via anotação |
| CRON | Configurado na tela | Atributo `frequency` na anotação |

### Registro no Sankhya

```
Menu: Gerenciamento → Ações Agendadas (ou Agendador de Tarefas)

Campos:
  Descrição   : nome descritivo
  Classe Java : br.com.sankhya.customizacao.nomedemanda.job.NomeAgendada
  Frequência  : CRON ou intervalo em milissegundos
```

---