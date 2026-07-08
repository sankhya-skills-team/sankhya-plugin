# controller/

Endpoint REST/serviço exposto externamente ao módulo via `ServiceProvider` manual.

## Responsabilidade

- Receber chamadas externas (requisições do portal ou de outros módulos)
- Gerenciar sessão com `JapeHelper`
- Delegar toda lógica para `component/`
- Retornar resultado serializado

## Proibido

- Regras de negócio — delegar para `component/`
- Acesso direto ao banco — sempre via `component/`
- Lógica além de receber, delegar e retornar

---

## Skeleton

```java
package br.com.sankhya.dstech.nomedemanda.controller;

import br.com.sankhya.dstech.nomedemanda.component.NomeComponent;
import br.com.sankhya.dstech.nomedemanda.exception.NomeDemandaException;
import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import br.com.sankhya.jape.core.JapeSession;
import com.sankhya.util.BigDecimalUtil;

import java.math.BigDecimal;

/**
 * Controller: [Descrição do endpoint]
 *
 * Configuração no Sankhya:
 *   - Tipo: ServiceProvider (registro manual via Construtor de Telas ou configuração)
 *   - Classe: br.com.sankhya.dstech.nomedemanda.controller.NomeController
 */
public class NomeController {

    public String executarOperacao(BigDecimal id) throws Exception {
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();

            NomeComponent component = new NomeComponent();
            return component.executarViaServico(id, null);

        } catch (NomeDemandaException e) {
            throw MGEModelException.prettyMsg(e.getMessage(), e);
        } catch (Exception e) {
            throw MGEModelException.prettyMsg("Erro inesperado: " + e.getMessage(), e);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
```

---

## Padrões de Recebimento de Parâmetros

### Parâmetros simples (BigDecimal, String)

```java
public String processarPorId(BigDecimal id) throws Exception {
    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();
        NomeComponent component = new NomeComponent();
        return component.executarViaServico(id, null);
    } catch (NomeDemandaException e) {
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        throw MGEModelException.prettyMsg("Erro inesperado: " + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

### Parâmetros via JSON (request body)

Quando o portal envia JSON, o controller deserializa e passa para o component:

```java
public String processarComDados(String jsonPayload) throws Exception {
    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();

        // Extrair dados do JSON (usar SankhyaUtil JsonUtils)
        BigDecimal id = BigDecimalUtil.getBigDecimal(
                JsonUtils.getField(jsonPayload, "id"));
        String parametro = JsonUtils.getField(jsonPayload, "parametro");

        NomeComponent component = new NomeComponent();
        return component.executarViaServico(id, parametro);

    } catch (NomeDemandaException e) {
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        throw MGEModelException.prettyMsg("Erro inesperado: " + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

---

## Registro Manual

O controller é registrado como serviço no arquivo de configuração do módulo (`module-config.xml`)
ou via Construtor de Telas. Consultar `references/estrutura-modulo.md` para detalhes do deploy.

```xml
<!-- Exemplo de registro como ServiceProvider -->
<service class="br.com.sankhya.dstech.nomedemanda.controller.NomeController"
         name="NomeController" />
```

---

## Diferença entre Controller e ActionButton

| Aspecto | `controller/` | `actionbutton/` |
|---|---|---|
| Iniciado por | Chamada programática externa (portal, outro módulo) | Usuário clicando em "Ações" na tela |
| Sessão | Abre `JapeSession` explicitamente | Sessão já existe no contexto do `ContextoAcao` |
| Resposta | Retorno serializado (String, JSON) | `ctx.setMensagemRetorno()` |
| Contexto | Sem `ContextoAcao` | Com `ContextoAcao` (linhas selecionadas, params) |

---

## Boas Práticas

- **`JapeSession.open()` com `finally { JapeSession.close(hnd); }`** — obrigatório
- **Dois catches separados** — `NomeDemandaException` para erros de negócio, `Exception` para inesperados
- **Delegar tudo para `component/`** — controller não contém lógica além de sessão + delegação
- **Retorno sempre String ou tipo primitivo** — evitar objetos complexos não serializáveis
