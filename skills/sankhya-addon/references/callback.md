# Callback

## Visão Geral

A anotação `@Callback` é um hook para interceptar eventos de alto nível no ciclo de vida de **documentos comerciais**, como confirmação de nota ou faturamento.

Disponível a partir da versão **2.0 do Add-on Studio**.

Diferente do `@Listener` (opera em nível de persistência/CRUD) e da `@BusinessRule` (focada no ciclo de vida comercial de saída), o `@Callback` reage a ações de negócio específicas de forma direta.

---

## Quando Usar

| Hook | Escopo | Quando Usar |
|---|---|---|
| `@Callback` | Todos os documentos comerciais, incluindo Notas de Entrada (Compras) | Reagir a eventos de negócio de forma direta; único hook que atua em notas de compra |
| `@BusinessRule` | Notas de Saída e Mov. Interna (Vendas, Remessas) | Lógicas que precisam interagir com `ContextoRegra`, como liberação de limites |
| `@Listener` | Qualquer entidade (CRUD genérico) | Lógica aplicada a múltiplas entidades, não apenas documentos comerciais |

**Regra prática:**
- Validar **nota de compra** na confirmação → `@Callback`
- Solicitar **liberação de limites** em nota de venda → `@BusinessRule`
- Auditoria simples na confirmação de qualquer nota → `@Callback`

---

## Como Implementar

A classe deve implementar `br.com.sankhya.modelcore.custommodule.ICustomCallBack` e ser anotada com `@Callback`.

### Atributos da Anotação

| Atributo | Descrição | Exemplo |
|---|---|---|
| `when` | Executa **antes** (`BEFORE`) ou **depois** (`AFTER`) do evento | `CallbackWhen.BEFORE` |
| `event` | Evento de negócio a interceptar | `CallbackEvent.CONFIRMATION` |
| `description` | Descrição do que o callback faz | `"Valida dados na confirmação"` |

### Método da Interface

```java
Object call(String id, Map<String, Object> data) throws Exception
```

- `id`: ID do evento disparado (ex: `central.cabecalho.before`)
- `data`: Mapa com dados contextuais — conteúdo varia por evento

---

## Eventos Disponíveis (`CallbackEvent`)

### `INSERTION`

Disparado na inserção ou alteração de um documento (não por CRUD do JAPE, mas pela lógica de negócio dos portais).

| `when` | Parâmetros em `data` |
|---|---|
| `BEFORE` | `cabState` (`PrePersistEntityState`) — estado antes da persistência, acessa `newVO` |
| `AFTER` | `cabState` (`PrePersistEntityState`), `oldCabVO` (`DynamicVO`), `bRegras` (`BarramentoRegra`) |

### `CONFIRMATION` / `PROCESS_CONFIRMATION`

- `CONFIRMATION`: confirmação de notas pelos **Portais**
- `PROCESS_CONFIRMATION`: confirmação de notas pelas **telas Centrais**

| `when` | Parâmetros em `data` |
|---|---|
| `BEFORE` | `nunota` (`BigDecimal`), `bRegras` (`BarramentoRegra`) |
| `AFTER` | `nunota` (`BigDecimal`), `bRegras` (`BarramentoRegra`), `error` (`Exception`) — preenchido se houve erro |

### `PROCESS_BILLING`

Disparado no início do faturamento. **Não possui evento `AFTER`.**

| `when` | Parâmetros em `data` |
|---|---|
| `BEFORE` | `notasSelecao` (`Collection<BigDecimal>`), `itensEditados` (`Map<String,BigDecimal>`) — chave: `nunota-sequencia`, valor: qtd a faturar |

---

## Exemplo

```java
package br.com.fabricante.addon.callbacks;

import br.com.sankhya.modelcore.custommodule.ICustomCallBack;
import br.com.sankhya.studio.annotations.hooks.Callback;
import br.com.sankhya.studio.annotations.hooks.CallbackEvent;
import br.com.sankhya.studio.annotations.hooks.CallbackWhen;
import java.math.BigDecimal;
import java.util.Map;

@Callback(
    when = CallbackWhen.BEFORE,
    event = CallbackEvent.CONFIRMATION,
    description = "Valida dados antes da confirmação da nota"
)
public class ValidaConfirmacaoCallback implements ICustomCallBack {

    @Override
    public Object call(String id, Map<String, Object> data) throws Exception {
        BigDecimal nunota = (BigDecimal) data.get("nunota");

        if (nunota == null) {
            throw new Exception("NUNOTA não encontrado no contexto da confirmação.");
        }

        // Delegar lógica complexa para um @Service
        // servicoDeValidacao.validar(nunota);

        return null;
    }
}
```

---

## Boas Práticas

- **Verifique as chaves do mapa `data`** antes de usá-las — o conteúdo varia por evento e `when`
- **Mantenha a lógica simples e rápida** — para lógicas complexas ou com I/O, delegue para um `@Service`
- **Use para notas de entrada** — é o único hook que cobre o ciclo de vida de notas de compra

## Antipadrões

- **Lógica de liberação de limites**: pertence exclusivamente à `@BusinessRule` via `BarramentoRegra`
- **CRUD genérico**: se a lógica se aplica a várias entidades, use `@Listener`
- **Operações lentas na thread principal**: chamadas de API síncronas ou I/O de disco impactam a performance do sistema

---

## Fonte

https://developer.sankhya.com.br/docs/08_callback
