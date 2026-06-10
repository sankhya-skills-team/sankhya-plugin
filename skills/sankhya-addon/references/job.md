# Jobs Agendados (@Job)

## Visão Geral

A anotação `@Job` simplifica a criação de tarefas agendadas no Sankhya, substituindo a abordagem legada baseada em `mgeschedule.xml` por configuração declarativa em Java.

## Interface `IJob`

Define o contrato obrigatório para toda classe Job:

| Método | Obrigatório | Descrição |
|---|---|---|
| `onSchedule()` | Sim | Executado a cada disparo do agendador |
| `getScheduleConfigHook()` | Não | Executado uma única vez na inicialização para configurações dinâmicas |

## Atributos da Anotação `@Job`

| Atributo | Obrigatório | Descrição | Exemplo |
|---|---|---|---|
| `name` | Sim | Nome do Bean gerado. **Deve terminar com "SP"** | `"SincronizadorSP"` |
| `frequency` | Sim | Expressão CRON ou intervalo em ms. **Deve começar com "&"** | `"&0 0/15 * * * ?"` |
| `transactionType` | Não | Comportamento transacional | `TransactionType.NotSupported` |

## Exemplo Completo

```java
@Job(
    name = "SincronizadorDeEstoqueSP",
    frequency = "&0 0 2 * * ?" // Executa todo dia às 02:00
)
public class SincronizadorDeEstoqueJob implements IJob {

    private static final Logger logger = Logger.getLogger(SincronizadorDeEstoqueJob.class);

    @Override
    @Transactional
    public void onSchedule() {
        try {
            logger.info("Iniciando sincronização de estoque...");
            EstoqueService estoqueService = new EstoqueService();
            estoqueService.sincronizar();
            logger.info("Sincronização de estoque finalizada.");
        } catch (Exception e) {
            logger.error("Erro na sincronização de estoque", e);
        }
    }
}
```

## Sintaxe de Expressões CRON

Formato: `& segundo minuto hora dia_mês mês dia_semana`

| Expressão | Significado |
|---|---|
| `&0 0 2 * * ?` | Diariamente às 02:00 |
| `&0 0/15 * * * ?` | A cada 15 minutos |
| `&0 0 * * * MON` | Segunda-feira à meia-noite |
| `&120000` | A cada 2 minutos (ms) |
| `&86400000` | A cada 1 dia (ms) |

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

- Modificações de dados: use `@Transactional` em `onSchedule()`
- Somente leitura: considere `transactionType = TransactionType.NotSupported`

### 3. Tratamento de erros

Implemente tratamento robusto para evitar que falhas impeçam execuções futuras:

```java
@Override
@Transactional
public void onSchedule() {
    try {
        // lógica do job
    } catch (Exception e) {
        logger.error("Erro no job", e);
    }
}
```

### 4. Frequência configurável

Use `getScheduleConfigHook()` para ler a frequência de parâmetros do sistema em vez de hardcodar:

```java
@Override
public String getScheduleConfigHook() {
    return systemParamService.obterFrequencia();
}
```

## Migração do Modelo Legado

Ao usar `@Job`, os arquivos `mgeschedule.xml` e `mgechedule-cfg.xml` **não são permitidos** — a compilação falhará se existirem. Todos os jobs legados devem ser migrados para o novo formato.

**Modelo antigo (não usar):**
```xml
<!-- mgeschedule.xml -->
<jobs>
    <ejb-job name="MeuJob"/>
</jobs>
```

**Modelo novo:**
```java
@Job(name = "MeuJobSP", frequency = "&0 0 2 * * ?")
public class MeuJob implements IJob {
    @Override
    public void onSchedule() { ... }
}
```

## Fonte

https://developer.sankhya.com.br/docs/jobs-agendados-com-job
