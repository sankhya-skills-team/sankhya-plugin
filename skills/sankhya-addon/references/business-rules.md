# Regras de Negócio (`@BusinessRule`)

> Disponível a partir da versão 2.0 do Add-on Studio.

## Visão Geral

A anotação `@BusinessRule` é o hook ideal para implementar lógicas de negócio durante os eventos de **confirmação e faturamento** de **documentos comerciais** (Pedidos, Notas de Venda, etc.).

Embora também possa interceptar eventos de CRUD, a abordagem moderna prefere `@Listener` para essas operações, reservando `@BusinessRule` para as etapas mais complexas e específicas do ciclo de vida comercial.

---

## Quando usar

Use para executar validações, modificações ou iniciar processos que devem ocorrer especificamente no momento em que um documento é **confirmado** ou **faturado**.

Casos de uso comuns:
- **Validações de confirmação**: verificar estoque ou limite de crédito no momento da confirmação.
- **Solicitação de liberação de limites**: iniciar processo de aprovação quando um pedido excede um valor/condição.
- **Integrações pós-confirmação**: disparar operações assíncronas (JMS, `CompletableFuture`) para sistemas externos sem bloquear a thread principal.
- **Cálculos complexos de faturamento**: aplicar lógicas de impostos ou comissões que dependem do estado final da nota.

---

## `@BusinessRule` vs. `@Callback`

Ambos reagem a eventos do ciclo de vida comercial, mas com escopos diferentes. A escolha é por **aplicabilidade**, não complexidade.

| Hook | Escopo de Atuação | Quando Usar |
|---|---|---|
| `@BusinessRule` | **Notas de Saída e Mov. Interna** (Vendas, Remessas, etc.) | Para lógicas que precisam interagir com o **barramento de regras** (`ContextoRegra`), como solicitar liberações de limite, ou para validações complexas na confirmação/faturamento. |
| `@Callback` | **Todos os Documentos Comerciais**, incluindo **Notas de Entrada** (Compras) | Para reagir a eventos de negócio de forma direta, especialmente onde `@BusinessRule` não atua (notas de compra) ou quando a interação com o barramento não é necessária. |

**Resumo rápido:**
- Precisa solicitar **liberação de limites** em nota de venda? → `@BusinessRule`
- Precisa validar uma **nota de compra** na confirmação? → `@Callback`
- Lógica simples de auditoria na confirmação de qualquer nota? → `@Callback` é mais direto

---

## Como funciona

Crie uma classe que implemente `br.com.sankhya.modelcore.comercial.Regra` e anote-a com `@BusinessRule`.

### Interface `Regra`

Implementa métodos correspondentes aos eventos do ciclo de vida do documento (`beforeInsert`, `afterUpdate`, etc.). O foco principal está nos eventos de **confirmação e faturamento**.

### `ContextoRegra`

O objeto `ctx` é o **principal diferencial** da `@BusinessRule`:

| Acesso | Descrição |
|---|---|
| `ctx.getPrePersistEntityState().getNewVO()` | `DynamicVO` da nota com as **modificações atuais** |
| `ctx.getPrePersistEntityState().getOldVO()` | `DynamicVO` da nota com os **dados originais** (disponível em `beforeUpdate` e `beforeDelete`) |
| `ctx.getBarramentoRegra().addMensagem("msg")` | Exibe aviso não bloqueante para o usuário |
| `ctx.getBarramentoRegra().addLiberacaoSolicitada(...)` | Inicia evento de liberação de limites |

---

## Exemplos práticos

### 1. Solicitando liberação de limite na confirmação

Caso de uso ideal para `@BusinessRule`. Requer que um evento de liberação (ex: ID 2000) esteja previamente cadastrado no sistema.

```java
@BusinessRule(description = "Solicita liberação para vendas com desconto alto")
public class LiberacaoDescontoRegra implements Regra {

    @Override
    public void beforeUpdate(ContextoRegra ctx) throws Exception {
        DynamicVO notaVO = (DynamicVO) ctx.getPrePersistEntityState().getNewVO();

        // A confirmação internamente dispara um 'update' na nota
        Boolean isConfirmando = (Boolean) JapeSession.getProperty("CabecalhoNota.confirmando.nota");
        if (!Boolean.TRUE.equals(isConfirmando)) return;

        BigDecimal percentualDesconto = notaVO.asBigDecimal("PERCDESC");

        if (percentualDesconto != null && percentualDesconto.compareTo(new BigDecimal("10")) > 0) {
            int idEventoLiberacao = 2000; // deve ser cadastrado no sistema

            LiberacaoSolicitada liberacao = new LiberacaoSolicitada(
                    notaVO.asBigDecimal("NUNOTA"),
                    "TGFCAB",       // tabela da nota
                    idEventoLiberacao,
                    BigDecimal.ONE  // ID do usuário solicitante
            );
            liberacao.setPendente(true);

            ctx.getBarramentoRegra().addLiberacaoSolicitada(liberacao);
            ctx.getBarramentoRegra().addMensagem("Solicitação de liberação enviada para desconto acima de 10%.");
        }
    }

    // ... outros métodos da interface ...
}
```

### 2. Modificando um campo na confirmação

Para modificações durante CRUD simples, prefira `@Listener`. Use `@BusinessRule` quando a modificação precisa ocorrer **especificamente no momento da confirmação**.

```java
@BusinessRule(description = "Adiciona observação de conferência na confirmação")
public class AdicionaObservacaoConfirmacaoRegra implements Regra {

    @Override
    public void beforeUpdate(ContextoRegra ctx) throws Exception {
        DynamicVO notaVO    = (DynamicVO) ctx.getPrePersistEntityState().getNewVO();
        DynamicVO oldNotaVO = (DynamicVO) ctx.getPrePersistEntityState().getOldVO();

        // Detecta transição N → S no campo CONFIRMADA
        boolean isConfirmando = "S".equals(notaVO.asString("CONFIRMADA"))
                && (oldNotaVO == null || !"S".equals(oldNotaVO.asString("CONFIRMADA")));

        if (isConfirmando) {
            String obsAtual = notaVO.asString("OBSERVACAO");
            String novaObs  = "Nota conferida e confirmada pelo sistema.";
            notaVO.setProperty("OBSERVACAO", obsAtual == null ? novaObs : obsAtual + "\n" + novaObs);
        }
    }

    // ... outros métodos da interface ...
}
```

---

## Boas práticas

- **Execução rápida**: a regra roda dentro da mesma transação da confirmação. Qualquer lentidão impacta diretamente o usuário. Deve executar em milissegundos.
- **Assincronismo para integrações**: nunca faça chamadas síncronas a APIs externas. Use `CompletableFuture`, `ExecutorService` ou JMS para isolar a integração da transação principal.
- **Foco na confirmação**: use `@BusinessRule` para o que ela faz de melhor — lógica no momento da confirmação/faturamento.
- **Lógica em Services**: mantenha a classe enxuta. Delegue lógica complexa para `@Service`.
- **Feedback ao usuário**: use `ctx.getBarramentoRegra().addMensagem()` para informar ações automáticas executadas.
- **Validações bloqueantes**: para impedir uma operação, lance uma exceção. Ex: `throw new Exception("Limite de crédito excedido.")`.

## Anti-patterns

- **Usar para CRUD simples**: validações ou modificações de campo que podem ser feitas com `@Listener` não devem usar `@BusinessRule`. Isso acopla a lógica desnecessariamente ao módulo comercial.
- **Chamadas síncronas externas**: chamadas de rede dentro de uma regra de negócio degradam a performance e podem causar timeouts.
- **Manipular a UI**: regras de negócio são back-end. Não tente manipular componentes de interface a partir delas.
- **Ignorar o evento correto**: não use `afterInsert` para validações que deveriam estar em `beforeInsert`. Após o registro ser salvo, pode ser tarde demais.

---

## Fonte

https://developer.sankhya.com.br/docs/06_business_rules