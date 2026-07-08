# Botão de Ação — AcaoRotinaJava (Registro Manual)

## Visão Geral

Em módulos Java (fora do Addon Studio), botões de ação são implementados com a interface
`AcaoRotinaJava` e registrados **manualmente** no Sankhya via menu de configuração.
Não existem anotações — todo o registro é feito pela UI do ERP.

Responsabilidade da camada `actionbutton/`:
- Validações de UI/interação: seleção vazia, seleção múltipla, campo obrigatório de formulário
- Confirmação de intenção do usuário (`confirmarSimNao`)
- Abertura de `JapeSession`
- Delegação para `service/`
- Conversão de `NomeModuloException` para `MGEModelException`

**Proibido em `actionbutton/`:** regras de negócio, acesso a banco, lógica reutilizável.

---

## Interface `AcaoRotinaJava`

```java
import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;

public class NomeAction implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao ctx) throws Exception {
        // implementação
    }
}
```

## Objeto `ContextoAcao`

| Método | Descrição |
|---|---|
| `ctx.getLinhas()` | Array de registros selecionados na tela |
| `ctx.getLinhas()[i].getCampo("CAMPO")` | Valor de um campo do registro selecionado |
| `ctx.setMensagemRetorno(String msg)` | Exibe mensagem ao usuário (suporta HTML básico: `<b>`, `<br>`) |
| `ctx.confirmarSimNao(titulo, msg, padrao)` | Diálogo de confirmação — retorna `true` se confirmado. `1` = Sim padrão, `2` = Não padrão |
| `ctx.setArquivoRetorno(File f, String nome)` | Retorna arquivo para download |
| `ctx.getParam("campo")` | Valor de campo de formulário exibido antes da ação |

---

## Padrão Base — Estrutura do `doAction`

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    // 1. Validar seleção (sempre primeiro)
    if (ctx.getLinhas().length == 0) {
        ctx.setMensagemRetorno("Selecione ao menos um registro!");
        return;
    }
    if (ctx.getLinhas().length > 1) {
        ctx.setMensagemRetorno("Selecione apenas um registro!");
        return;
    }

    // 2. Confirmação prévia (remover se não necessário)
    boolean confirmado = ctx.confirmarSimNao("Confirmar", "Deseja executar esta operação?", 1);
    if (!confirmado) {
        ctx.setMensagemRetorno("Operação cancelada.");
        return;
    }

    // 3. Extrair chave do registro selecionado
    BigDecimal id = BigDecimalUtil.getBigDecimal(ctx.getLinhas()[0].getCampo("ID_CAMPO"));

    // 4. Delegar para service
    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();

        NomeService nomeService = new NomeService();
        String resultado = nomeService.executarOperacao(id);

        ctx.setMensagemRetorno(resultado);

    } catch (NomeModuloException e) {
        // Exceção de domínio — mensagem já está pronta para o usuário
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        // Erro inesperado
        throw MGEModelException.prettyMsg("Erro inesperado ao executar operação: <br>" + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

---

## Padrão — Botão com Múltiplos Registros

Quando a ação opera sobre todos os registros selecionados:

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    Registro[] linhas = ctx.getLinhas();

    if (linhas == null || linhas.length == 0) {
        ctx.setMensagemRetorno("Selecione ao menos um registro!");
        return;
    }

    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();

        NomeService nomeService = new NomeService();
        int processados = nomeService.processarLote(linhas);

        ctx.setMensagemRetorno(processados + " registro(s) processado(s) com sucesso.");

    } catch (NomeModuloException e) {
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        throw MGEModelException.prettyMsg("Erro inesperado: <br>" + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

---

## Padrão — Botão com Formulário de Parâmetros

Quando o usuário precisa informar um valor antes da ação (via `ctx.getParam()`).
Inputs simples (texto, data, decimal) — para seleção em grid, usar PopUpBuilder.

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    if (ctx.getLinhas().length == 0) {
        ctx.setMensagemRetorno("Selecione ao menos um registro!");
        return;
    }

    // Captura parâmetro informado no formulário
    String motivoCancelamento = String.valueOf(ctx.getParam("MOTIVO"));
    if (motivoCancelamento == null || motivoCancelamento.isBlank()) {
        ctx.setMensagemRetorno("Informe o motivo do cancelamento!");
        return;
    }

    BigDecimal id = BigDecimalUtil.getBigDecimal(ctx.getLinhas()[0].getCampo("ID_CAMPO"));

    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();

        NomeService nomeService = new NomeService();
        nomeService.cancelar(id, motivoCancelamento);

        ctx.setMensagemRetorno("Registro <b>" + id + "</b> cancelado com sucesso.");

    } catch (NomeModuloException e) {
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        throw MGEModelException.prettyMsg("Erro inesperado: <br>" + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

---

## Padrão Completo — Classe com imports, Javadoc e busca de registro

Esqueleto de arquivo completo (package, imports, Javadoc com a configuração no Sankhya) e
uma variação de tratamento de erro com **catch externo + `MGEModelException.throwMe(e)`**
(alternativa ao par de catches `NomeModuloException`/`Exception` mostrado no Padrão Base —
use `throwMe` quando não há exceção de domínio própria e você quer propagar o erro com o stack trace intacto).

```java
package br.com.empresa.dctm.modulo.botaoacao;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.util.DynamicEntityNames;
import com.sankhya.util.BigDecimalUtil;
import java.math.BigDecimal;

/**
 * Botão de ação na tela de NomeTela (AD_NOMETABELA).
 *
 * Descrição detalhada do que o botão faz.
 *
 * Configuração no Sankhya:
 *   Entidade : AD_NOMETABELA (ou CabecalhoNota, etc.)
 *   Classe   : br.com.empresa.dctm.modulo.botaoacao.ProcessarAction
 */
public class ProcessarAction implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao ctx) throws Exception {
        try {
            // 1. Validar seleção
            if (ctx.getLinhas().length == 0) {
                ctx.setMensagemRetorno("Selecione um registro!");
                return;
            }
            if (ctx.getLinhas().length > 1) {
                ctx.setMensagemRetorno("Selecione apenas um registro!");
                return;
            }

            // 2. Extrair chave do registro selecionado
            BigDecimal id = BigDecimalUtil.getBigDecimal(
                    ctx.getLinhas()[0].getCampo("IDCAMPO"));

            // 3. Buscar registro para validações adicionais
            DynamicVO vo = JapeFactory.dao("AD_NOMETABELA").findByPK(id);
            if (vo == null) {
                throw new MGEModelException("Registro não encontrado para o ID: " + id);
            }

            // 4. Validação de negócio
            String status = vo.asString("STATUS");
            if ("F".equals(status)) {
                ctx.setMensagemRetorno("Este registro já está finalizado.");
                return;
            }

            // 5. Executar operação com JapeSession (quando cria/altera outra entidade)
            BigDecimal resultado;
            JapeSession.SessionHandle hnd = null;
            try {
                hnd = JapeSession.open();

                resultado = ModuloHelper.executarOperacao(id, vo);

            } catch (Exception e) {
                throw MGEModelException.prettyMsg(
                        "Erro ao processar: <br>" + e.getMessage(), e);
            } finally {
                JapeSession.close(hnd);
            }

            // 6. Feedback ao usuário
            ctx.setMensagemRetorno(
                    "Operação concluída! Resultado: <b>" + resultado + "</b>");

        } catch (Exception e) {
            e.printStackTrace();
            MGEModelException.throwMe(e);
        }
    }
}
```

---

## Padrão — Botão com Confirmação (operação irreversível)

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    try {
        if (ctx.getLinhas().length == 0) {
            ctx.setMensagemRetorno("Selecione um registro!");
            return;
        }

        BigDecimal id = BigDecimalUtil.getBigDecimal(
                ctx.getLinhas()[0].getCampo("IDCAMPO"));

        // Confirmação antes de operação irreversível
        boolean confirmado = ctx.confirmarSimNao(
                "Confirmar Exclusão",
                "Deseja realmente excluir o registro <b>" + id + "</b>?",
                2); // 1=Sim padrão, 2=Não padrão

        if (!confirmado) {
            ctx.setMensagemRetorno("Operação cancelada.");
            return;
        }

        ModuloHelper.excluir(id);

        ctx.setMensagemRetorno("Registro <b>" + id + "</b> excluído com sucesso.");

    } catch (Exception e) {
        e.printStackTrace();
        MGEModelException.throwMe(e);
    }
}
```

---

## Padrão — Botão sem JapeSession (operação na mesma sessão)

Quando o botão apenas lê e atualiza entidades sem criar nova sessão (mais simples):

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    try {
        if (ctx.getLinhas().length == 0) {
            ctx.setMensagemRetorno("Selecione um registro!");
            return;
        }

        BigDecimal nuNota = BigDecimalUtil.getBigDecimal(
                ctx.getLinhas()[0].getCampo("NUNOTA"));

        DynamicVO cabVO = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA)
                .findByPK(nuNota);

        if (cabVO == null) {
            throw new MGEModelException("Nota não encontrada: " + nuNota);
        }

        // Verificar campo opcional
        if (cabVO.containsProperty("CAMPO_OPCIONAL")) {
            BigDecimal valorOpcional = cabVO.asBigDecimal("CAMPO_OPCIONAL");
            // processar...
        }

        // Atualizar campo
        JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA)
                .prepareToUpdateByPK(nuNota)
                .set("CAMPO_STATUS", "F")
                .update();

        ctx.setMensagemRetorno("Nota <b>" + nuNota + "</b> atualizada com sucesso.");

    } catch (Exception e) {
        e.printStackTrace();
        MGEModelException.throwMe(e);
    }
}
```

---

## Padrão — Botão que cria registro em outra entidade

Cria um registro em uma entidade e vincula ao registro atual.

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    try {
        if (ctx.getLinhas().length != 1) {
            ctx.setMensagemRetorno("Selecione exatamente um registro!");
            return;
        }

        BigDecimal nuNota = BigDecimalUtil.getBigDecimal(
                ctx.getLinhas()[0].getCampo("NUNOTA"));

        DynamicVO cabVO = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA)
                .findByPK(nuNota);

        if (cabVO == null) {
            throw new MGEModelException("Pedido Nº " + nuNota + " não encontrado.");
        }

        // Verificar se já existe vínculo
        BigDecimal vinculoExistente = BigDecimalUtil.getBigDecimal(
                cabVO.getProperty("CAMPO_VINCULO"));
        if (!BigDecimalUtil.isNullOrZero(vinculoExistente)) {
            ctx.setMensagemRetorno(
                    "Este pedido já possui o vínculo <b>" + vinculoExistente + "</b>.");
            return;
        }

        BigDecimal codEmp = BigDecimalUtil.getBigDecimal(cabVO.getProperty("CODEMP"));

        JapeSession.SessionHandle hnd = null;
        BigDecimal idGerado;
        try {
            hnd = JapeSession.open();

            // Criar o registro na outra entidade
            DynamicVO novoVO = JapeFactory.dao("AD_OUTRAENTIDADE").create()
                    .set("CODEMP", codEmp)
                    .set("NUNOTA_ORIGEM", nuNota)
                    .save();

            idGerado = BigDecimalUtil.getBigDecimal(novoVO.getProperty("IDREGISTRO"));

            // Vincular ao registro original
            JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA)
                    .prepareToUpdateByPK(nuNota)
                    .set("CAMPO_VINCULO", idGerado)
                    .update();

        } catch (Exception e) {
            throw MGEModelException.prettyMsg(
                    "Erro ao criar registro: <br>" + e.getMessage(), e);
        } finally {
            JapeSession.close(hnd);
        }

        ctx.setMensagemRetorno(
                "Registro <b>" + idGerado + "</b> criado e vinculado ao pedido <b>" + nuNota + "</b>!");

    } catch (Exception e) {
        e.printStackTrace();
        MGEModelException.throwMe(e);
    }
}
```

---

## Registro Manual no Sankhya

### Via Menu do Sankhya

```
Menu: Gerenciamento → Botões de Ação
  ou: Configurações → Botões de Ação (dependendo da versão)

Campos:
  Descrição   : texto exibido no menu "Ações" (ex: "Criar Ordem de Carga")
  Entidade    : instância JAPE alvo (ex: CabecalhoNota, AD_NOMETABELA)
  Classe Java : pacote completo (ex: br.com.empresa.dctm.modulo.botaoacao.ProcessarAction)
  Recurso ID  : resourceId da tela para restringir — opcional
                (ex: br.com.sankhya.core.mov.centraldenotas para Central de Notas)
```

---

## Boas Práticas

- **Sempre validar seleção** no início — `length == 0` antes de qualquer outra coisa
- **`JapeSession.open()` com `finally { JapeSession.close(hnd); }`** — sem exceção
- **`setMensagemRetorno` sempre** — nunca executar silenciosamente
- **HTML básico** no retorno — `<b>valor</b>` e `<br>` são renderizados
- **Delegar para `service/`** — o botão só coordena: valida entrada, abre sessão, chama service, retorna mensagem
- **Dois catches separados** — `NomeModuloException` para erros de negócio esperados, `Exception` para erros inesperados
- **`MGEModelException.throwMe(e)`** no catch externo — alternativa quando não há exceção de domínio própria; propaga com o stack trace correto
- **`e.printStackTrace()` antes de `throwMe`** — facilita diagnóstico nos logs do servidor
- **`ctx.confirmarSimNao()`** é exclusivo de `AcaoRotinaJava` — em eventos e regras usar `PopUpBuilder`

## Antipadrões

- Regras de negócio no `doAction()` — validação de status, cálculos, decisões condicionais de negócio
- Acesso a banco direto (`JapeFactory`, SQL) no `doAction()`
- `JapeSession.open()` sem `finally { JapeSession.close(hnd); }`
- `catch (Exception e)` único sem separar exceções de domínio das inesperadas
- Capturar `Exception` e retornar mensagem sem relançar — esconde erros de configuração
- Executar sem `setMensagemRetorno` — usuário fica sem feedback
- `ctx.getLinhas()[0]` sem verificar `length` antes
