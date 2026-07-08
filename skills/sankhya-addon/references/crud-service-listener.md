# CRUD Service Listener (`DatasetCRUDListenerAdapter`)

> Mecanismo **legado** da camada `modelcore` (MGE), anterior ao `@Listener` do Add-on Studio. Continua existente e funcional nas plataformas atuais, mas **não possui anotação** de registro no Studio.

## Visão Geral

O CRUD Service Listener intercepta as operações de CRUD que passam pelo **serviço de dataset de uma tela/instância** (a grade/formulário DWF que o front-end aciona). É a camada usada pelas telas de cadastro clássicas do Sankhya.

Diferente do `@Listener` — que opera na **camada de persistência (JAPE)** e dispara em qualquer origem (tela, API, importação, código Java) — o CRUD Service Listener só dispara quando a operação trafega pelo **dataset daquela instância específica**. Ele recebe o `DynamicVO` como o dataset o enxerga, incluindo **campos transientes/dinâmicos da tela** que nunca chegam à tabela.

Existem duas gerações da mesma família:

| Classe | Interface | Situação |
|---|---|---|
| `CRUDServiceListenerAdapter` | `CRUDServiceListener` | **Legado.** 13 métodos, inclui interceptação de metadados via `org.jdom.Element` (`interceptMetadata`, `interceptEntitiesElement`, `interceptMetadataFields`). O runtime embrulha em `Html5CRUDServiceListenerDelegator` e emite aviso pedindo migração. |
| `DatasetCRUDListenerAdapter` | `DatasetCRUDListener` | **Atual (não-SDK).** 10 métodos, apenas o ciclo CRUD + `loadCustomData`. É o tipo que o runtime usa nativamente (`crudListenerInstance: DatasetCRUDListener`). Preferir este. |

Ambas vivem em `br.com.sankhya.modelcore.util` e chegam ao classpath via `mge-modelcore` (transitivo do plugin `addonstudio`).

---

## Quando usar

Use o CRUD Service Listener **em vez** do `@Listener` quando:

- **A lógica depende de campos transientes do dataset** — colunas dinâmicas/calculadas que existem só na grade da tela e não são persistidas (ex.: matriz `FORNECEDOR_1..N`, `DESCFORNECEDOR_N`). Um `@Listener` recebe o VO persistido e **não enxerga** esses campos.
- **A interceptação deve ser exclusiva daquela tela/instância** — não de toda persistência da entidade, independente da origem.
- **Você está convertendo código legado** que já estende `CRUDServiceListenerAdapter` e não toca os métodos de metadados jdom (migração drop-in, ver abaixo).

Nos demais casos — lógica que vale para a entidade em qualquer origem (auditoria, validação genérica, integração) — prefira `@Listener`.

---

## `DatasetCRUDListener` vs. `@Listener`

| | `DatasetCRUDListener(Adapter)` | `@Listener` + `PersistenceEventAdapter` |
|---|---|---|
| **Camada** | Serviço de dataset (grade/tela DWF) | Persistência (JAPE / `EntityFacade`) |
| **Dispara quando** | CRUD passa pelo dataset **daquela instância** | **Qualquer** persistência da entidade (tela, API, importação, código) |
| **Registro** | **DB-side**: configuração da instância aponta a FQN da classe. Sem anotação, sem entrada no datadictionary | Anotação `@Listener(instanceNames={...})`, auto-descoberta no deploy |
| **Argumento** | `DynamicVO vo` — enxerga **campos transientes do dataset** | `PersistenceEvent event` |
| **Valor anterior (old)** | **Não há** `getOldVO`; buscar manualmente via `FinderWrapper` | `event.getOldVO()` disponível em `update`/`delete` |
| **Pacote** | `br.com.sankhya.modelcore.util` | `br.com.sankhya.jape.event` + `br.com.sankhya.studio.annotations` |

**Resumo:**
- Regra usa `FORNECEDOR_1..N` (campo só da tela)? → CRUD Service Listener.
- Auditoria de `Produto` em qualquer origem? → `@Listener`.

---

## Como funciona

Crie uma classe que estenda `br.com.sankhya.modelcore.util.DatasetCRUDListenerAdapter` e sobrescreva apenas os hooks necessários.

### Métodos da interface `DatasetCRUDListener`

| Método | Quando é chamado |
|---|---|
| `beforeInsert(DynamicVO vo)` | Antes de inserir o registro |
| `afterInsert(DynamicVO vo)` | Após inserir o registro |
| `beforeUpdate(DynamicVO vo)` | Antes de atualizar o registro |
| `afterUpdate(DynamicVO vo)` | Após atualizar o registro |
| `beforeDelete(DynamicVO vo)` | Antes de excluir o registro |
| `afterDelete(DynamicVO vo)` | Após excluir o registro |
| `beforeLoadRecord(DynamicVO vo)` | Antes de carregar um registro para exibição |
| `beforeFind(FinderWrapper finder)` | Antes de executar a busca — permite injetar critérios |
| `afterResult(Collection result)` | Após montar o resultado — permite pós-processar a coleção |
| `loadCustomData(FinderWrapper finder)` | Carrega dados customizados (retorna `Collection`; `null` = sem customização) |

> O `DatasetCRUDListenerAdapter` já fornece implementação vazia de todos. Sobrescreva só o que precisar.

### Registro (DB-side)

Não há anotação. A classe é vinculada à **instância** (entidade DWF) pela configuração da instância no ERP — a instância aponta a **FQN** da classe listener. O serviço de dataset resolve a classe em tempo de execução (`ClasspathUtils.getClassFromContextClassLoader(fqn).newInstance()`) e a executa no CRUD daquela tela.

Consequências práticas:
- A vinculação **não vai no fonte** do add-on nem no `datadictionary` — é configuração da instância no banco.
- A classe precisa estar no classpath do add-on (basta estendê-la e compilar no módulo).

### Valor anterior (old)

`DatasetCRUDListener` **não entrega** o VO anterior. Quando a regra precisa comparar com o estado atual do banco (ex.: bloquear alteração de campo), busque manualmente:

```java
FinderWrapper finder = new FinderWrapper(
    "MinhaInstancia", "this.CHAVE = ?", new Object[] { vo.asBigDecimal("CHAVE") });
finder.setMaxResults(1);
Collection<PersistentLocalEntity> col = dwfFacade.findByDynamicFinder(finder);
DynamicVO voOld = col.isEmpty() ? null : (DynamicVO) col.iterator().next().getValueObject();
```

---

## Exemplo prático

Listener de grade que valida permissão, bloqueia alteração de campos travados comparando com o valor anterior e replica dados em tabela relacionada. Note o uso de campo transiente da tela (`FORNECEDOR_N`), invisível a um `@Listener`.

```java
package br.com.fabricante.addon.crudlisteners;

import java.math.BigDecimal;
import java.util.Collection;

import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.bmp.PersistentLocalEntity;
import br.com.sankhya.jape.dao.JdbcWrapper;
import br.com.sankhya.jape.util.FinderWrapper;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.modelcore.util.DatasetCRUDListenerAdapter;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;

public class ItemCotacaoCRUDListener extends DatasetCRUDListenerAdapter {

    @Override
    public void beforeUpdate(DynamicVO vo) throws Exception {
        EntityFacade dwf = EntityFacadeFactory.getDWFFacade();

        DynamicVO voOld = obterAtual(dwf, vo.asBigDecimal("NUMCOTACAO"), vo.asBigDecimal("CODPROD"));
        if (voOld == null) return;

        // Campo travado após liberação — comparação com estado anterior
        if (!vo.asBigDecimalOrZero("QTDCOTADA").equals(voOld.asBigDecimalOrZero("QTDCOTADA"))) {
            throw new Exception("Registro não atualizado.\r\nA Qtd. Cotada não pode ser alterada.");
        }

        // Campo transiente da grade — só existe no dataset, não na tabela
        BigDecimal precoForn = vo.asBigDecimalOrZero("FORNECEDOR_1");
        if (precoForn.signum() < 0) {
            throw new Exception("Preço do fornecedor não pode ser negativo.");
        }
    }

    @Override
    public void afterInsert(DynamicVO vo) throws Exception {
        JdbcWrapper jdbc = null;
        try {
            EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
            jdbc = dwf.getJdbcWrapper();
            jdbc.openSession();
            // ... replicar em tabela relacionada usando o jdbc da sessão ...
        } finally {
            JdbcWrapper.closeSession(jdbc);
        }
    }

    private DynamicVO obterAtual(EntityFacade dwf, BigDecimal numCotacao, BigDecimal codProd) throws Exception {
        FinderWrapper finder = new FinderWrapper(
            "TzaCotZanPro", "this.NUMCOTACAO = ? AND this.CODPROD = ?",
            new Object[] { numCotacao, codProd });
        finder.setMaxResults(1);
        Collection<PersistentLocalEntity> col = dwf.findByDynamicFinder(finder);
        return col.isEmpty() ? null : (DynamicVO) col.iterator().next().getValueObject();
    }
}
```

> Lançar `Exception` (ou `MGEModelException`) em qualquer método `before*` cancela a operação e exibe a mensagem ao usuário.

---

## Migração de `CRUDServiceListenerAdapter` → `DatasetCRUDListenerAdapter`

Se a classe legada sobrescreve **apenas** métodos do ciclo CRUD (`beforeInsert`, `afterUpdate`, `beforeDelete`, etc.) e **não** toca os métodos jdom de metadados, a migração é **drop-in** — as assinaturas são idênticas:

```java
// antes
import br.com.sankhya.modelcore.util.CRUDServiceListenerAdapter;
public class MeuCRUDListener extends CRUDServiceListenerAdapter { ... }

// depois
import br.com.sankhya.modelcore.util.DatasetCRUDListenerAdapter;
public class MeuCRUDListener extends DatasetCRUDListenerAdapter { ... }
```

Corpo dos métodos, `@Override` e o registro da instância permanecem inalterados.

**Exceção:** se a classe legada sobrescreve `interceptMetadata`, `interceptEntitiesElement` ou `interceptMetadataFields` (`org.jdom.Element`), esses métodos **não existem** em `DatasetCRUDListener`. Nesse caso a lógica de metadados precisa ir para o equivalente BFF (`IDynaformInterceptor.interceptFieldMetadata`) — o que exige o SDK do Add-on Studio.

---

## Boas práticas

- **Prefira `DatasetCRUDListenerAdapter`** a `CRUDServiceListenerAdapter`: evita o `Html5CRUDServiceListenerDelegator` (reflection) e o aviso de migração.
- **Feche a sessão JDBC que você abriu**: ao usar `EntityFacadeFactory.getDWFFacade().getJdbcWrapper()` + `openSession()`, sempre feche em `finally` com `JdbcWrapper.closeSession(jdbc)`.
- **Old via finder**: como não há `getOldVO`, encapsule a busca do valor anterior em um método privado reutilizável.
- **Validações bloqueantes**: lance exceção nos `before*` para cancelar a operação.

## Anti-patterns

- **Usar CRUD Service Listener para lógica de entidade genérica**: se a regra deve valer em qualquer origem (API, importação), o dataset listener **não dispara** — use `@Listener`.
- **Depender de `getOldVO`**: não existe nesta interface; buscar manualmente.
- **Reimplementar metadados jdom no legado**: em vez de manter `interceptMetadata*`, migre a interceptação de metadados para o caminho BFF quando aplicável.
- **Esquecer o registro da instância**: sem a vinculação DB-side, a classe nunca é acionada, mesmo compilada no add-on.
