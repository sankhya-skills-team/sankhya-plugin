# Jobs Agendados (@Job)

## Visão Geral

A anotação `@Job` cria tarefas agendadas no addon por configuração declarativa em Java, no lugar do `mgeschedule.xml` escrito à mão.

> API verificada no Add-on Studio 2.x (`studio-annotations`, `studio-processors`). Os atributos e assinaturas abaixo são os da 2.x — versões anteriores usavam nomes diferentes.

## Classe base `IJob`

`IJob` é uma **classe abstrata**, não uma interface. A classe do job usa `extends`, não `implements`:

```java
public class MeuJob extends IJob { ... }
```

O processor recusa a compilação com a mensagem `deve implementar 'br.com.sankhya.studio.stereotypes.IJob'` quando a classe anotada não estende `IJob`.

| Método | Obrigatório | Descrição |
|---|---|---|
| `onSchedule()` | Sim | Executado a cada disparo do agendador |
| `getScheduleConfig()` | Não | Devolve a frequência em tempo de carga. Retornando valor não nulo, **prevalece sobre `frequency`**. Retornando `null`, vale o `frequency` da anotação |
| `getScheduleConfigHook()` | — | **Obsoleto.** Existe só por retrocompatibilidade e retorna `void`. Use `getScheduleConfig()` |

## Atributos da Anotação `@Job`

| Atributo | Obrigatório | Descrição | Exemplo |
|---|---|---|---|
| `serviceName` | Sim | Nome único do job no módulo. Terminar com `"SP"` é convenção, não exigência | `"SincronizadorSP"` |
| `frequency` | Não | Frequência padrão. Default: `"&60000"` (60s) | `"0 0/15 * * * ?"` |
| `transactionType` | Não | Tipo de transação EJB. Default: `EJBTransactionType.Supports` | `EJBTransactionType.NotSupported` |

**`serviceName` duplicado quebra o deploy** — o Wildfly não aceita dois serviços com o mesmo nome. Duplicidade se manifesta como job com configuração errada, conflito de registro ou job que simplesmente não executa.

## Exemplo Completo

```java
import br.com.sankhya.studio.annotations.Job;
import br.com.sankhya.studio.annotations.enums.EJBTransactionType;
import br.com.sankhya.studio.stereotypes.IJob;

@Job(
    serviceName = "SincronizadorDeEstoqueSP",
    frequency = "0 0 2 * * ?",                      // todo dia as 02:00
    transactionType = EJBTransactionType.Supports
)
public class SincronizadorDeEstoqueJob extends IJob {

    private static final Logger logger = Logger.getLogger(SincronizadorDeEstoqueJob.class);

    @Override
    @Transactional
    public void onSchedule() {
        try {
            new EstoqueService().sincronizar();
        } catch (Exception e) {
            logger.error("Falha na sincronizacao de estoque", e);
            throw new RuntimeException(e);           // sem relancar, a execucao conta como normal
        }
    }
}
```

## Sintaxe da frequência

Dois formatos, e o `&` distingue um do outro:

| Formato | Regra | Exemplo |
|---|---|---|
| Intervalo em milissegundos | **com** prefixo `&` | `"&60000"` = a cada 60s |
| Expressão CRON (6 campos) | **sem** prefixo `&` | `"0 0 2 * * ?"` = todo dia às 02:00 |

CRON de 6 campos: `segundo minuto hora dia_do_mês mês dia_da_semana`.

| Expressão | Significado |
|---|---|
| `"0 0 2 * * ?"` | Diariamente às 02:00 |
| `"0 0/5 * * * ?"` | A cada 5 minutos |
| `"0 0 9-17 * * MON-FRI"` | De hora em hora, das 9 às 17, de segunda a sexta |
| `"&120000"` | A cada 2 minutos (intervalo em ms) |
| `"&86400000"` | A cada 1 dia (intervalo em ms) |

CRON inválido em geral **não gera erro explícito** — apenas impede o agendamento, e o job nunca roda. Confira a expressão ao subir um job novo que "não dispara".

## Boas Práticas

### 1. Delegar lógica para Services

Mantenha `onSchedule()` enxuto:

```java
@Override
public void onSchedule() {
    new FilaService().processarItens();
}
```

### 2. Controle transacional

- Modificações de dados: `@Transactional` em `onSchedule()`
- Somente leitura: considere `transactionType = EJBTransactionType.NotSupported`

### 3. Tratamento de erros

Trate e **relance**. Capturar e apenas logar faz o ciclo ser contabilizado como execução normal, e a falha desaparece do acompanhamento do job:

```java
@Override
@Transactional
public void onSchedule() {
    try {
        // logica do job
    } catch (Exception e) {
        logger.error("Erro no job", e);
        throw new RuntimeException(e);
    }
}
```

Falha de um item isolado que não deve abortar o lote se trata **dentro do laço**, por item.

### 4. Frequência configurável

Use `getScheduleConfig()` para ler a frequência de um parâmetro do sistema em vez de fixá-la:

```java
@Override
public String getScheduleConfig() {
    return systemParamService.obterFrequencia();   // null -> vale o frequency da anotacao
}
```

### 5. Idempotência

O mesmo ciclo pode repetir (reinício do servidor, disparo sobreposto, retry operacional). Escreva `onSchedule()` de forma que rodar duas vezes não duplique efeito.

## Migração do Modelo Legado

Ao usar `@Job`, os arquivos `mgeschedule.xml` e `mgechedule-cfg.xml` **não são permitidos** — a compilação falhará se existirem. Todos os jobs legados devem ser migrados para o novo formato. O processor é quem gera o `mgeschedule.xml` a partir da anotação.

**Modelo antigo (não usar):**
```xml
<!-- mgeschedule.xml -->
<jobs>
    <ejb-job name="MeuJob"/>
</jobs>
```

**Modelo novo:**
```java
@Job(serviceName = "MeuJobSP", frequency = "0 0 2 * * ?")
public class MeuJob extends IJob {
    @Override
    public void onSchedule() { ... }
}
```

## Runtime, concorrência e fila

Como o job executa de fato — o que conta como erro, job que consome fila (claim-first), armadilha de acordar job dentro da transação, concorrência entre instâncias e sessão JAPE: [job-runtime.md](job-runtime.md).

## Fonte

https://developer.sankhya.com.br/docs/jobs-agendados-com-job
