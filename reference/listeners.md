# JAPE — Listeners de Persistência (contrato/API)

Como um listener de persistência funciona como código JAPE: contrato da interface, eventos do ciclo de vida e API do evento. Governança, regra de performance e registro via DataDictionary são assuntos de plataforma, fora do escopo desta reference.

## Contrato

O contrato é a interface `br.com.sankhya.jape.event.PersistenceEventListener`. Na prática, **não implemente a interface direto** — estenda o adapter `PersistenceEventAdapter` e sobrescreva apenas os eventos de que você precisa. O adapter já fornece implementação vazia para todos os métodos.

```java
public class MeuListener extends PersistenceEventAdapter {
    // sobrescreva só o que importa
}
```

## Modelo de invocação

O JAPE invoca o listener **dentro da mesma transação** da operação de persistência, **uma vez por registro (por linha) afetado**. Não é assíncrono e não é em lote:

- Um UPDATE que atinge 500 linhas dispara o evento 500 vezes, em sequência, na mesma TX.
- O código do listener roda na thread e na conexão da operação que o disparou.
- Daí a "regra de ouro" de performance: como o listener roda 1x por linha dentro da TX, evite I/O e SQL pesado por registro.

## Eventos do ciclo de vida

Todos os métodos declaram `throws Exception`. Recebem o evento de persistência correspondente.

| Evento | Quando dispara | Uso típico |
|---|---|---|
| `beforeInsert` | antes de inserir | default de campos, validação prévia |
| `afterInsert` | após inserir | propagação para registros relacionados |
| `beforeUpdate` | antes de atualizar | validação; checar campos alterados |
| `afterUpdate` | após atualizar | recálculo/integração dependente |
| `beforeDelete` | antes de excluir | regras de bloqueio de exclusão |
| `afterDelete` | após excluir | limpeza/auditoria em cascata |
| `afterLoadValueObject` / `afterRetrieveValueObject` | após carregar/recuperar o VO | enriquecimento de leitura (cuidado: dispara em consulta) |
| `beforeCommit` | antes do commit da transação | quando a entidade também implementa `TransactionListener` (ver `transactions.md`) |

Atenção a `afterLoadValueObject` / `afterRetrieveValueObject`: disparam em **leitura**, não só em escrita. Lógica pesada aqui penaliza toda consulta da entidade.

## API do evento

Use no `beforeUpdate`/`afterUpdate` para não recalcular tudo a cada update:

- `event.getModifingFields()` — quais campos mudaram. Filtre a regra por isto; só reaja se o campo relevante está no conjunto.
- `event.getOldVO()` — estado anterior do registro. Evita reconsultar o banco para comparar antes/depois.
- `event.getJdbcWrapper()` — **reuse** a conexão/transação corrente. **Não** abra conexão nova nem novo `JapeSession` dentro do listener (regras de sessão em `transactions.md` e na SKILL.md desta skill).

## Registro via código (caminho programático)

O caminho programático de registro é:

```java
EntityListenerDelegator.registryListener(entityName, listener);
```

Os outros caminhos de registro (DataDictionary `<event-listener>`, `extension-listeners.xml`, `GlobalEntityListenerImpl`, eventos programáveis TSIEVT, sincronização mobile) são da plataforma e não são cobertos aqui.

## Exceção no listener faz rollback

Lançar exceção dentro de qualquer evento do listener faz **rollback de toda a transação** — consistente com as regras transacionais (ver `transactions.md`). Isto é contrato.

O *uso* desse contrato (travar uma exclusão indevida lançando exceção, vs. isolar uma integração best-effort para não derrubar a TX principal) é decisão de governança, definida em cada módulo.

## Exemplo — beforeUpdate filtrando por campo alterado

```java
public class PedidoListener extends PersistenceEventAdapter {

    public void beforeUpdate(PersistenceEvent event) throws Exception {
        Set modifing = event.getModifingFields();
        if (!modifing.contains("CODPARC")) {
            return; // parceiro não mudou; nada a fazer
        }

        DynamicVO novoVO = (DynamicVO) event.getVo();
        DynamicVO antigoVO = (DynamicVO) event.getOldVO();

        BigDecimal parcAntigo = antigoVO.asBigDecimalOrZero("CODPARC");
        BigDecimal parcNovo = novoVO.asBigDecimalOrZero("CODPARC");
        if (parcAntigo.compareTo(parcNovo) == 0) {
            return; // valor igual; sem efeito
        }

        // reusa a conexão/TX corrente — não abre sessão nova
        JdbcWrapper jdbc = event.getJdbcWrapper();
        NativeSql query = null;
        try {
            query = new NativeSql(jdbc);
            query.appendSql("UPDATE TGFCAB SET STATUS = 'P' WHERE NUNOTA = :NUNOTA");
            query.setNamedParameter("NUNOTA", novoVO.asBigDecimal("NUNOTA"));
            query.executeUpdate();
        } finally {
            NativeSql.releaseResources(query);
        }
    }
}
```

Se a classe do listener for um **BEAN xDoclet**, vale a regra Java 6 — sem lambda, sem diamond, tipos genéricos explícitos.

## Onde fica o resto

Esta reference cobre só o contrato/API JAPE. O que **não** está aqui pertence à plataforma e é tratado fora desta skill:

- Governança: quando travar (lançar exceção) vs. isolar integração best-effort.
- Performance: a "regra de ouro" (listener roda 1x por linha, dentro da TX — cuidado com I/O e SQL pesado por registro).
- Registro via DataDictionary (`<event-listener>`), `extension-listeners.xml`, `GlobalEntityListenerImpl`, eventos programáveis TSIEVT e sincronização mobile.
