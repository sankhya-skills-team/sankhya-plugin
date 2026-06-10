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

## Boas Práticas

- **Sempre validar seleção** no início — `length == 0` antes de qualquer outra coisa
- **`JapeSession.open()` com `finally { JapeSession.close(hnd); }`** — sem exceção
- **`setMensagemRetorno` sempre** — nunca executar silenciosamente
- **HTML básico** no retorno — `<b>valor</b>` e `<br>` são renderizados
- **Delegar para `service/`** — o botão só coordena: valida entrada, abre sessão, chama service, retorna mensagem
- **Dois catches separados** — `NomeModuloException` para erros de negócio esperados, `Exception` para erros inesperados
- **`ctx.confirmarSimNao()`** é exclusivo de `AcaoRotinaJava` — em eventos e regras usar `PopUpBuilder`

## Antipadrões

- Regras de negócio no `doAction()` — validação de status, cálculos, decisões condicionais de negócio
- Acesso a banco direto (`JapeFactory`, SQL) no `doAction()`
- `JapeSession.open()` sem `finally { JapeSession.close(hnd); }`
- `catch (Exception e)` único sem separar exceções de domínio das inesperadas
- Executar sem `setMensagemRetorno` — usuário fica sem feedback
- `ctx.getLinhas()[0]` sem verificar `length` antes
