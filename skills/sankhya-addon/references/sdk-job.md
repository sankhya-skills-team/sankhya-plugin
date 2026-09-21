# SDK Sankhya — Job Agendado (@Job)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Diferença em relação ao @Job do Add-on Studio

Esta página documenta o `@Job` no uso com o **SDK Sankhya**, que adiciona **injeção de dependências** via `@Inject`. A anotação e a classe base são as mesmas do Add-on Studio (`br.com.sankhya.studio.annotations.Job`, `br.com.sankhya.studio.stereotypes.IJob`) — só muda a forma de obter as dependências. Para os detalhes de contrato, frequência e runtime, ver [job.md](job.md).

---

## Como Criar

1. Anotar a classe com `@Job`
2. Estender `IJob` (classe abstrata, não interface)
3. Injetar dependências via construtor com `@Inject`

```java
@Job(serviceName = "ProcessadorDeFilaSP", frequency = "0 0/5 * * * ?")
public class ProcessadorDeFilaJob extends IJob {

    private final FilaService filaService;

    @Inject
    public ProcessadorDeFilaJob(FilaService filaService) {
        this.filaService = filaService;
    }

    @Override
    public void onSchedule() {
        filaService.processarItens();
    }
}
```

---

## Atributos da Anotação

| Atributo | Obrigatório | Descrição | Exemplo |
|---|---|---|---|
| `serviceName` | Sim | Nome único do job no módulo. Terminar com `"SP"` é convenção, não exigência. Duplicado, o Wildfly recusa o deploy | `"SincronizadorSP"` |
| `frequency` | Não | Frequência padrão. Default: `"&60000"` | `"0 0/15 * * * ?"` |
| `transactionType` | Não | Tipo de transação EJB. Default: `EJBTransactionType.Supports` | `EJBTransactionType.NotSupported` |

`&` só para intervalo em milissegundos (`"&60000"`); expressão CRON de 6 campos vai sem `&` (`"0 0/15 * * * ?"`).

## Classe base `IJob`

| Método | Obrigatório | Descrição |
|---|---|---|
| `onSchedule()` | Sim | Executado a cada disparo |
| `getScheduleConfig()` | Não | Frequência dinâmica em tempo de carga; valor não nulo prevalece sobre `frequency` |
| `getScheduleConfigHook()` | — | **Obsoleto**, retorna `void`. Use `getScheduleConfig()` |

---

## Exemplo Completo

```java
@Job(
    serviceName = "SincronizadorDeEstoqueSP",
    frequency = "0 0 2 * * ?"
)
public class SincronizadorDeEstoqueJob extends IJob {

    private static final Logger logger = Logger.getLogger(SincronizadorDeEstoqueJob.class);

    private final EstoqueService estoqueService;

    @Inject
    public SincronizadorDeEstoqueJob(EstoqueService estoqueService) {
        this.estoqueService = estoqueService;
    }

    @Override
    @Transactional
    public void onSchedule() {
        try {
            estoqueService.sincronizar();
        } catch (Exception e) {
            logger.error("Falha na sincronizacao de estoque", e);
            throw new RuntimeException(e);           // sem relancar, a execucao conta como normal
        }
    }
}
```

---

## Boas Práticas

- Mantenha `onSchedule()` enxuto — delegue para `@Component` ou `@Service`
- Use `@Transactional` para jobs que modificam dados
- Use `transactionType = NotSupported` para jobs somente leitura
- Use `getScheduleConfig()` para ler frequência de parâmetros do sistema
- Trate o erro e **relance**: capturar e apenas logar faz o ciclo ser contabilizado como execução normal
- Escreva `onSchedule()` de forma idempotente — o mesmo ciclo pode repetir

## Migração

Ao usar `@Job` do SDK, os arquivos `mgeschedule.xml` e `mgechedule-cfg.xml` **não são permitidos** — a compilação falhará. O processor gera o `mgeschedule.xml` a partir da anotação.

## Runtime, concorrência e fila

Comportamento de execução, claim-first em fila, armadilha de acordar job dentro da transação e concorrência entre instâncias: [job-runtime.md](job-runtime.md).

---

## Fonte

https://developer.sankhya.com.br/docs/job
