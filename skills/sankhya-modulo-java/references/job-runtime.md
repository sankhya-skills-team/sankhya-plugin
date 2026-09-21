# Runtime de Job Agendado — Cuckoo

Como o job realmente executa depois que o agendador dispara: onde o trabalho deve morar, o que conta como erro, e as armadilhas de concorrência e de transação.

Vale tanto para addon (`@Job` + `IJob`) quanto para módulo Java (`ScheduledAction`), porque os dois caminhos desembocam no mesmo agendador: o **Cuckoo** (`org.cuckoo.core`), que é um Quartz por baixo.

> Verificado em `cuckoo-master.jar`: `ScheduledAction.onTime(ScheduledActionContext)`, `ScheduledActionContext` (`log`, `info`, `getInfo`, `getCurrent`) e `SchedulerRuntime$JobDelegation` anotada com `@org.quartz.DisallowConcurrentExecution`.

## Os dois caminhos de registro

| Origem | Como o job é registrado | O que você escreve |
|---|---|---|
| Addon (Add-on Studio) | O processor do `@Job` gera `mgeschedule.xml` com `<ejb-job name="..."/>`; o adaptador do Cuckoo o converte em job do scheduler | classe `extends IJob` com `onSchedule()` |
| Módulo Java | Ação agendada cadastrada na tela (`TSIAAG`), com a classe no campo da ação | classe `implements ScheduledAction` com `onTime(ctx)` |

Registro diferente, **mesmo scheduler**. Tudo desta referência vale para os dois.

## Onde vai cada tipo de trabalho

| Necessidade | Onde vai |
|---|---|
| Serviço síncrono chamado pela tela | Service / SPBean |
| Trabalho pesado, assíncrono ou periódico | Job agendado |
| Reação a gravação (`BEFORE_INSERT`, `AFTER_UPDATE`, ...) | Listener de persistência — curto, sem trabalho pesado |
| Processamento longo disparado por uma gravação | Enfileire na gravação e deixe o job drenar a fila |

Listener não é lugar de processamento longo: ele roda por linha, dentro da transação de escrita.

## Exceção engolida vira execução "bem-sucedida"

O erro mais comum em job. O runtime monta a estatística da execução a partir do que escapa do teu método. Se você captura e apenas loga, **a execução é contabilizada como normal** e a falha some do acompanhamento do job.

```java
// ERRADO — job "sempre verde", ninguem descobre a falha
try {
    processarLote();
} catch (Exception e) {
    LOGGER.error("Falhou", e);
}

// CERTO — loga e relanca, para a execucao constar como erro
try {
    processarLote();
} catch (Exception e) {
    LOGGER.error("Falha no processamento do lote", e);
    throw new RuntimeException(e);
}
```

Se a falha realmente não deve interromper o job (item ruim no meio de um lote que precisa continuar), trate **dentro do laço**, por item, e deixe o `onSchedule`/`onTime` propagar qualquer falha do ciclo.

## `ctx.log(...)` não é log de aplicação

Em `ScheduledAction`, o `ScheduledActionContext` oferece dois métodos que parecem equivalentes e não são:

| Método | O que faz |
|---|---|
| `ctx.log(msg)` | `System.out.println("[job: <descrição>]" + msg)` — não passa pelo logger, não respeita nível |
| `ctx.info(msg)` | acumula texto que aparece na **estatística da execução** do job |

Use o logger da aplicação para log, e reserve `ctx.info(...)` para o resumo do ciclo (`"processados=" + n`).

`ScheduledActionContext.getCurrent()` é `ThreadLocal`: só funciona dentro da thread do job. Código assíncrono disparado por ele não enxerga o contexto.

## Job que consome fila: claim-first

Um job que lê a fila, processa e só então marca o status **não é seguro**:

```sql
-- FRAGIL: outra execucao le as mesmas linhas 'P' e aplica o efeito em dobro
SELECT ... FROM AD_FILA WHERE STATUS = 'P';
-- ... processa, aplica efeito colateral ...
UPDATE AD_FILA SET STATUS = 'C' WHERE NUFILA = :NUFILA AND STATUS = 'P';
```

O `UPDATE` no fim apenas **detecta** a colisão (0 linhas atualizadas) — não previne o efeito que já foi commitado.

Marque a posse **antes** de processar e processe só o que este ciclo marcou:

```sql
-- 1) claim: portavel Oracle 11g / SQL Server 2008 (sem SKIP LOCKED / READPAST)
UPDATE AD_FILA SET STATUS = 'X', DHCLAIM = :AGORA
 WHERE STATUS = 'P' AND <recorte do lote>;

-- 2) processar SOMENTE as linhas que este ciclo marcou como 'X'
SELECT ... FROM AD_FILA WHERE STATUS = 'X' AND DHCLAIM = :AGORA;
```

Confira o rowcount do claim: zero significa que outro ciclo levou o lote, e o correto é sair, não reprocessar.

## Não acorde o job de dentro da transação que gravou a fila

Ao enfileirar e mandar o job rodar no mesmo fluxo, o disparo acontece em **transação própria**, em milissegundos. Sob `READ COMMITTED`, ele não enxerga as linhas ainda não commitadas: lê a fila vazia, não processa nada e encerra. Quando o commit sai, o ciclo disparado já terminou, e o trabalho só acontece no próximo disparo agendado.

Ou seja: o "acordar" não tem efeito útil e a latência continua sendo a do intervalo.

Se precisa mesmo antecipar, dispare **depois do commit**, nunca antes. A sessão JAPE registra uma `javax.transaction.Synchronization` na transação, e o ponto pós-commit é o `afterCompletion` com status `STATUS_COMMITTED`. Cuidado com o gancho errado: `beforeCommit` roda **antes** do commit e cai exatamente na mesma corrida. Ver skill `sankhya-jape`, `reference/transactions.md`.

## Concorrência

- `@DisallowConcurrentExecution` (Quartz) garante que **o mesmo job não se sobrepõe a si mesmo dentro de uma JVM**. Ciclo que demora mais que o intervalo é serializado, não paralelizado.
- Essa garantia **não atravessa JVMs**. Se o ambiente tiver mais de uma instância apontando para o mesmo banco sem coordenação de cluster, cada instância roda o próprio agendador e o mesmo job dispara em paralelo. É risco de implantação, não de código — e o claim-first acima é o que protege o job independente da topologia.
- Não use `synchronized` para impedir execução dupla: ele só serializa threads da mesma JVM, exatamente o caso que já está coberto.

## Não crie `Thread` nem `ExecutorService` dentro de EJB

A thread nova não herda contexto transacional nem usuário autenticado, e escapa do gerenciamento do container. Trabalho assíncrono vira job agendado.

## Sessão JAPE em job

Job de longa duração ou em laço é onde vazamento de sessão aparece mais rápido: toda `JapeSession` aberta fecha no `finally`. Pool esgotado derruba leitura e escrita de toda a plataforma, não só o job.
