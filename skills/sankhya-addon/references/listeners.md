# Listeners (`@Listener`)

> Disponível a partir da versão 2.0 do Add-on Studio.

## Visão Geral

A anotação `@Listener` é um hook de baixo nível que permite "escutar" e reagir a eventos de persistência (CRUD: Create, Read, Update, Delete) de **qualquer entidade (JAPE)** do sistema. É a ferramenta ideal para criar lógicas transversais — auditoria, validações genéricas, integrações — acionadas quando dados são inseridos, atualizados ou excluídos no banco de dados.

Diferente de `@BusinessRule` e `@Callback`, que reagem a eventos de negócio de alto nível (como "confirmar nota"), o `@Listener` opera diretamente na camada de persistência.

---

## Quando usar

Use para executar lógicas que devem ser aplicadas de forma genérica a uma ou mais entidades durante operações de CRUD.

Casos de uso comuns:
- **Auditoria**: gravar logs detalhados sobre quem alterou, inseriu ou excluiu um registro em qualquer tabela.
- **Validações genéricas**: aplicar uma regra de validação a todas as entidades que possuem um determinado campo (ex: validar CNPJ em `Parceiro`, `Empresa`, etc.).
- **Sincronização de dados**: manter campos denormalizados atualizados. Ex: ao alterar a descrição de um produto, replicar para tabelas relacionadas.
- **Disparar integrações assíncronas**: enfileirar mensagem (JMS) ou iniciar tarefa assíncrona (`CompletableFuture`) para notificar sistemas externos sem impactar a transação principal.

---

## `@Listener` vs. `@BusinessRule` vs. `@Callback`

| Ferramenta | Foco Principal | Quando Usar |
|---|---|---|
| `@Listener` | **Eventos de Persistência de Baixo Nível** (CRUD) | Para lógicas genéricas de CRUD (validação, auditoria, modificação) que se aplicam a **qualquer entidade** (JAPE) do sistema, não apenas documentos comerciais. |
| `@BusinessRule` | **Ciclo de Vida da Confirmação/Faturamento** | Para lógicas complexas na confirmação/faturamento de **notas de saída** que precisam interagir com o **barramento de regras** (ex: solicitar liberação de limites). |
| `@Callback` | **Eventos de Negócio de Alto Nível** (Comercial) | Para reagir a ações como "Confirmar Nota" ou "Faturar" em **todos os tipos de nota** (incluindo entrada). Mais simples que `@BusinessRule` e mais específico que `@Listener`. |

**Resumo:**
- Lógica no `beforeInsert` de `Produto`, `Parceiro` e `Nota`? → `@Listener`
- Solicitar liberação de limite ao confirmar uma venda? → `@BusinessRule`
- Enviar e-mail após confirmação de nota de compra? → `@Callback`

---

## Como funciona

Crie uma classe que estenda `br.com.sankhya.jape.event.PersistenceEventAdapter` e anote-a com `@Listener`.

### Atributos da anotação `@Listener`

| Atributo | Tipo | Descrição |
|---|---|---|
| `instanceNames` | `String[]` | Nomes das entidades (instâncias JAPE) que este listener irá monitorar. |

### Classe `PersistenceEventAdapter`

Métodos disponíveis para sobrescrever:

| Método | Quando é chamado |
|---|---|
| `beforeInsert(PersistenceEvent event)` | Antes de inserir o registro |
| `afterInsert(PersistenceEvent event)` | Após inserir o registro |
| `beforeUpdate(PersistenceEvent event)` | Antes de atualizar o registro |
| `afterUpdate(PersistenceEvent event)` | Após atualizar o registro |
| `beforeDelete(PersistenceEvent event)` | Antes de excluir o registro |
| `afterDelete(PersistenceEvent event)` | Após excluir o registro |

### O objeto `PersistenceEvent`

| Acesso | Descrição |
|---|---|
| `event.getVo()` | `DynamicVO` com os dados da entidade que está sofrendo a ação |
| `event.getOldVO()` | `DynamicVO` com os dados originais antes da alteração (disponível em `before/afterUpdate` e `before/afterDelete`) |
| `event.getJdbcWrapper()` | Wrapper JDBC para executar operações de banco **dentro da transação corrente** |

---

## Exemplo prático: Auditoria genérica

Listener que grava um log em `AD_AUDITORIA` sempre que uma nota (`CabecalhoNota`) ou um financeiro (`Financeiro`) é inserido.

```java
package br.com.fabricante.addon.listeners;

import br.com.sankhya.jape.event.PersistenceEvent;
import br.com.sankhya.jape.event.PersistenceEventAdapter;
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.jape.wrapper.JapeWrapper;
import br.com.sankhya.jape.wrapper.fluid.FluidCreateVO;
import br.com.sankhya.studio.annotations.Listener;
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
import br.com.sankhya.jape.util.JdbcWrapper;

@Listener(instanceNames = {"CabecalhoNota", "Financeiro"})
public class AuditoriaListener extends PersistenceEventAdapter {

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {
        // ✅ Sempre obter o JdbcWrapper do evento para garantir
        // que a operação ocorra na mesma transação.
        JdbcWrapper jdbc = event.getJdbcWrapper();

        JapeWrapper auditoriaDAO = JapeFactory.dao("AD_AUDITORIA", jdbc);
        FluidCreateVO log = auditoriaDAO.create();

        log.set("TABELA",    event.getVo().getEntityName());
        log.set("USUARIO",   AuthenticationInfo.getCurrent().getUserID());
        log.set("EVENTO",    "INSERT");
        log.set("DESCRICAO", "Novo registro inserido com a chave: " + event.getVo().getPrimaryKey());

        log.save();

        // ❗ Não fechar o jdbc! O framework gerencia o ciclo de vida.
    }
}
```

---

## Boas práticas

- **Use o `JdbcWrapper` do evento**: sempre obtenha a conexão via `event.getJdbcWrapper()`. Isso garante que sua operação execute dentro da transação correta.
- **Use assincronismo para integrações**: nunca faça chamadas síncronas a APIs externas dentro de um listener. Isso bloqueia a transação principal e degrada a performance do CRUD. Use `CompletableFuture` ou JMS:
  ```java
  CompletableFuture.runAsync(() -> {
      // Lógica de integração (ex: chamar uma API REST)
      // Roda em thread separada, fora da transação.
  });
  ```
- **Mantenha a lógica enxuta**: listeners devem ser rápidos. Delegue regras complexas para `@Service`.
- **Validações bloqueantes**: para impedir uma operação (em eventos `before...`), lance uma exceção. Ex: `throw new Exception("O campo X é obrigatório.")`.

## Anti-patterns

- **Usar para eventos de negócio**: não use `@Listener` para reagir a "confirmação de nota". O listener dispara em qualquer `UPDATE`, não apenas na confirmação, causando execuções indesejadas. Use `@BusinessRule` ou `@Callback`.
- **Obter `JdbcWrapper` da `EntityFacadeFactory`**: chamar `EntityFacadeFactory.getDWFFacade().getJdbcWrapper()` pode retornar uma conexão fora da transação atual, causando inconsistência de dados e locks.
- **Fechar a conexão**: nunca chame `jdbc.close()` no `JdbcWrapper` obtido do evento. O framework gerencia o ciclo de vida da conexão.
- **Lógica específica de documentos comerciais**: se a lógica se aplica apenas ao ciclo de vida de pedidos/notas, `@BusinessRule` ou `@Callback` são mais semânticos e apropriados.

---

## Exemplos Reais

### beforeDelete — Bloquear exclusão com condição

```java
@Listener(instanceNames = {"MinhaEntidade"})
public class BloqueiaExclusaoListener extends PersistenceEventAdapter {

    @Override
    public void beforeDelete(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        if (vo.asBigDecimal("NUNOTA") != null) {
            throw new MGEModelException(
                "Não é possível excluir este registro pois ele possui uma nota fiscal vinculada (NF: "
                + vo.asBigDecimal("NUNOTA") + ")."
            );
        }
    }
}
```

> Lançar `MGEModelException` em qualquer evento `before*` cancela a operação e exibe a mensagem ao usuário.

### beforeInsert + beforeUpdate — Preencher campo automaticamente

```java
@Listener(instanceNames = {"MinhaEntidadeDetalhe"})
public class PreencheDetalheListener extends PersistenceEventAdapter {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        preencherFuncao(vo);
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        preencherFuncao(vo);
    }

    private void preencherFuncao(DynamicVO vo) throws Exception {
        BigDecimal codEmp  = vo.asBigDecimal("CODEMP");
        BigDecimal codFunc = vo.asBigDecimal("CODFUNC");
        if (codEmp == null || codFunc == null) return;

        // Busca entidade nativa usando DynamicEntityNames
        JapeWrapper funcionarioDAO = JapeFactory.dao(DynamicEntityNames.FUNCIONARIO);
        DynamicVO funcionarioVO = funcionarioDAO.findByPK(codEmp, codFunc);
        if (funcionarioVO == null) return;

        // Modifica o VO antes de persistir — sem abrir nova transação
        vo.setProperty("CODFUNCAO", funcionarioVO.asBigDecimal("CODFUNCAO"));
    }
}
```

> `vo.setProperty(campo, valor)` modifica o VO que será persistido. Não é necessário chamar `save()` — o framework persiste o VO modificado automaticamente.

### beforeInsert com NativeSql — Recalcular campos antes de persistir

Listener que executa uma query SQL para buscar dados complementares e recalcula campos do VO antes de salvar. Abre sua própria sessão JDBC — **não usa o `event.getJdbcWrapper()`** porque precisa de uma query independente:

```java
@Listener(instanceNames = {"MinhaEntidadeItem"})
public class RecalculaCamposListener extends PersistenceEventAdapter {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        recalcular(vo);
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        recalcular((DynamicVO) event.getVo());
    }

    private void recalcular(DynamicVO vo) throws Exception {
        BigDecimal codRegistro = vo.asBigDecimal("CODREGISTRO");
        BigDecimal codEvento   = vo.asBigDecimal("CODEVENTO");

        // Abre sessão própria para a query de lookup
        EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
        JdbcWrapper jdbc = dwf.getJdbcWrapper();
        jdbc.openSession();

        BigDecimal percTaxa;
        BigDecimal percTributo;

        try (NativeSql ns = new NativeSql(jdbc)) {
            ns.loadSql(getClass(), "/scriptsSql/buscaParametrosCalculo.sql");
            ns.setNamedParameter("CODREGISTRO", codRegistro);
            ns.setNamedParameter("CODEVENTO",   codEvento);

            try (ResultSet rs = ns.executeQuery()) {
                if (!rs.next()) return;
                percTaxa    = rs.getBigDecimal("PERCTAXA");
                percTributo = rs.getBigDecimal("PERCTRIBUTO");
            }
        } finally {
            JdbcWrapper.closeSession(jdbc);
        }

        // Modifica o VO — será persistido com os valores recalculados
        BigDecimal vlrBase = BigDecimalUtil.getValueOrZero(vo.asBigDecimal("VLRBASE"));
        BigDecimal vlrTaxa = vlrBase.multiply(percTaxa).divide(new BigDecimal("100"), 2, RoundingMode.HALF_UP);

        vo.setProperty("PERCTAXA",    percTaxa);
        vo.setProperty("PERCTRIBUTO", percTributo);
        vo.setProperty("VLRTAXA",     vlrTaxa);
    }
}
```

> Quando o listener precisa de uma query de lookup independente (não relacionada à transação do evento), abrir e fechar a própria sessão JDBC é correto. Para operações que devem participar da mesma transação do evento, use `event.getJdbcWrapper()`.

### beforeInsert com validação de regra de negócio

```java
@Listener(instanceNames = {"MinhaEntidadeConfiguracao"})
public class ValidaRegraListener extends PersistenceEventAdapter {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        validar(vo);
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        validar((DynamicVO) event.getVo());
    }

    private void validar(DynamicVO vo) throws Exception {
        DynamicVO contratoVo = JapeFactory.dao(DynamicEntityNames.CONTRATO)
            .findByPK(vo.asBigDecimal("NUMCONTRATO"));

        String tipoFatura = contratoVo.asString("TIPOFATURA");
        BigDecimal codEvento = vo.asBigDecimal("CODEVENTO");

        if ("F".equals(tipoFatura) && !isEventoPermitido(codEvento)) {
            throw new IllegalArgumentException(
                "Para contratos do tipo Fixo, apenas os eventos 1, 9 e 200 são permitidos."
            );
        }
    }

    private boolean isEventoPermitido(BigDecimal codEvento) {
        return codEvento.compareTo(BigDecimal.ONE) == 0
            || codEvento.compareTo(new BigDecimal("9"))   == 0
            || codEvento.compareTo(new BigDecimal("200")) == 0;
    }
}
```

> `IllegalArgumentException` também cancela a operação e exibe a mensagem ao usuário — use quando a mensagem é de validação de entrada. Use `MGEModelException` para erros de negócio mais complexos.

### afterInsert — Sincronizar dados em outra entidade

```java
@Listener(instanceNames = {"MinhaEntidadePrincipal"})
public class SincronizaEntidadeListener extends PersistenceEventAdapter {

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();

        // Obter usuário logado dentro do listener
        BigDecimal codUsu = ((AuthenticationInfo) ServiceContext.getCurrent()
            .getAutentication()).getUserID();

        JapeFactory.dao("MinhaEntidadeRelacionada").create()
            .set("CODITEM",    vo.asBigDecimal("CODITEM"))
            .set("TIPITEM",    vo.asBigDecimal("TIPITEM").toPlainString())
            .set("CODUSU",     codUsu)
            .set("DHCADASTRO", Timestamp.valueOf(LocalDateTime.now()))
            .save();
    }

    @Override
    public void afterDelete(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        // Limpar registro relacionado após exclusão
        JapeFactory.dao("MinhaEntidadeRelacionada")
            .prepareToUpdateByPK(vo.asBigDecimal("CODITEM"))
            .update();
    }
}
```

> Use eventos `after*` para sincronizar dados em outras entidades — a operação principal já foi confirmada. Use `before*` para validações e modificações no próprio VO.

### Obter usuário logado dentro de um Listener

Dentro de um `@Listener` não há `ServiceContext ctx` disponível como parâmetro. Use:

```java
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
import br.com.sankhya.ws.ServiceContext;

BigDecimal codUsu = ((AuthenticationInfo) ServiceContext.getCurrent()
    .getAutentication()).getUserID();
```

### Verificar permissão do usuário no beforeInsert

```java
@Listener(instanceNames = {"Departamento"})
public class ValidaPermissaoDepartamentoListener extends PersistenceEventAdapter {

    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();

        // Só valida se for departamento analítico
        if (!"S".equals(vo.asString("ANALITICO"))) return;

        // Busca permissão do usuário logado
        BigDecimal codUsu = ((AuthenticationInfo) ServiceContext.getCurrent()
            .getAutentication()).getUserID();

        DynamicVO usuarioVO = JapeFactory.dao(DynamicEntityNames.USUARIO)
            .findByPK(codUsu);

        if (!"S".equals(usuarioVO.asString("PERMISSAO_ESPECIAL"))) {
            throw new MGEModelException(
                "Usuário sem permissão para esta operação. " +
                "Verifique as permissões na tela de Usuário e tente novamente."
            );
        }
    }
}
```

---

## Fonte

https://developer.sankhya.com.br/docs/07_listeners