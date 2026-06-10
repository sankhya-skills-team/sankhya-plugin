# SDK Sankhya — Job Agendado (@Job)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Diferença em relação ao @Job do Add-on Studio

Esta página documenta o `@Job` do **SDK Sankhya** (versão 2.0+), que adiciona suporte a **injeção de dependências** via `@Inject`. O comportamento base é o mesmo do `@Job` do Add-on Studio clássico.

---

## Como Criar

1. Anotar a classe com `@Job`
2. Implementar `IJob`
3. Injetar dependências via construtor com `@Inject`

```java
@Job(name = "ProcessadorDeFilaSP", frequency = "&0 0/5 * * * ?")
public class ProcessadorDeFilaJob implements IJob {

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
| `name` | Sim | Nome do Bean. Deve terminar com `"SP"` | `"SincronizadorSP"` |
| `frequency` | Sim | Expressão CRON ou ms. Deve começar com `&` | `"&0 0/15 * * * ?"` |
| `transactionType` | Não | Comportamento transacional padrão | `TransactionType.NotSupported` |

## Interface `IJob`

| Método | Obrigatório | Descrição |
|---|---|---|
| `onSchedule()` | Sim | Executado a cada disparo |
| `getScheduleConfigHook()` | Não | Executado uma vez na inicialização — para frequência dinâmica |

---

## Exemplo Completo

```java
@Job(
    name = "SincronizadorDeEstoqueSP",
    frequency = "&0 0 2 * * ?"
)
public class SincronizadorDeEstoqueJob implements IJob {

    private final EstoqueService estoqueService;

    @Inject
    public SincronizadorDeEstoqueJob(EstoqueService estoqueService) {
        this.estoqueService = estoqueService;
    }

    @Override
    @Transactional
    public void onSchedule() {
        estoqueService.sincronizar();
    }
}
```

---

## Boas Práticas

- Mantenha `onSchedule()` enxuto — delegue para `@Component` ou `@Service`
- Use `@Transactional` para jobs que modificam dados
- Use `transactionType = NotSupported` para jobs somente leitura
- Use `getScheduleConfigHook()` para ler frequência de parâmetros do sistema
- Inclua tratamento de erros robusto para não bloquear execuções futuras

## Migração

Ao usar `@Job` do SDK, os arquivos `mgeschedule.xml` e `mgechedule-cfg.xml` **não são permitidos** — a compilação falhará.

---

## Fonte

https://developer.sankhya.com.br/docs/job
