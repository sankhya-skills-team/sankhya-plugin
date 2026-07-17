# Micromódulo Sankhya SDK — abordagem moderna baseada em anotações

> **Escopo:** cobre a abordagem **moderna** SDK/Add-on Studio. Para a abordagem
> legada EJB2/XDoclet (`BaseSPBean`, `service-providers.xml`), veja
> `references/micromodule.md`.

## Quando usar

- Criar ou alterar componentes com `@Controller` (ou `@Service`, **deprecated**), `@Repository`, `@Listener`, `@BusinessRule`, `@Callback`, `@ActionButton`, `@Job`
- Configurar injeção de dependências (`@Inject`, `@Component`)
- Transações declarativas (`@Transactional`) e validação (`@Valid`)
- Tratamento de exceções (`@ControllerAdvice`, `@ExceptionHandler`)
- Injeção de valores de env vars / system properties / parâmetros Sankhya (`@Value`)
- Mapeamento de entidades (`@JapeEntity`, `@Column`, `@ManyToOne`, `@OneToMany`)

## SDK vs Legado (referência rápida)

| Aspecto | Legado (`micromodule`) | SDK (`micromodule-sdk`) |
|--------|----------------------|------------------------|
| Endpoints | `BaseSPBean` + XDoclet + `service-providers.xml` | `@Controller` (`@Service` deprecated) |
| DI | manual (`new`, singletons) | `@Inject` via construtor (Guice) |
| Dados | `JapeSession`, `EntityFacade`, `NativeSql` direto | `@Repository` + `JapeRepository` |
| Listeners | interface `EntityListener` | `@Listener` + `PersistenceEventAdapter` |
| Regras de negócio | interface `Regra` manual | `@BusinessRule` + `Regra` + `ContextoRegra` |
| Callbacks | `ICustomCallBack` manual | `@Callback` + `ICustomCallBack` declarativo |
| Botões | `AcaoRotinaJava` manual | `@ActionButton` + `@Form` |
| Jobs | `IJob` + config XML | `@Job` declarativo com frequência CRON |
| Transações | `JapeSession.open/close` manual | `@Transactional` declarativo |
| Validação | if/throw manual | `@Valid` + Bean Validation |
| Exceções | try/catch manual | `@ControllerAdvice` + `@ExceptionHandler` |
| Config | vários arquivos XML | `metadados.xml` + anotações |

## Pilares do SDK

1. **Injeção de dependências (DI)** — container IoC baseado em Google Guice
2. **Camada de dados (Repository)** — acesso a dados declarativo via interfaces anotadas
3. **Transações declarativas** — `@Transactional` com controle fino de propagação
4. **Bean Validation** — validação automática com JSR 303/380

## Anotações principais (referência rápida)

| Anotação | Propósito | Detalhe |
|------------|---------|--------|
| `@Controller` | endpoint HTTP (REST) — substituto oficial de `@Service` | `serviceName` DEVE terminar com `SP`; TX padrão `Supports` |
| `@Service` | **deprecated** — será removido; use `@Controller` | mantida só para manutenção de legado |
| `@Component` | bean gerenciado | lógica de negócio, validadores, helpers |
| `@Inject` | injeção de dependência | usar `com.google.inject.Inject`, **nunca** `javax.inject.Inject` |
| `@Repository` | camada de acesso a dados | estende `JapeRepository<ID, Entity>` |
| `@JapeEntity` | mapeamento entidade→tabela | atributos `entity` + `table` obrigatórios |
| `@Listener` | ganchos de evento de persistência | `instanceNames` = nome da entidade, não da tabela |
| `@BusinessRule` | ganchos do ciclo de vida de documento de venda | para Notas de Saída e Mov. Interna |
| `@Callback` | ganchos de evento de documento | todos os tipos de documento, inclusive compras |
| `@ActionButton` | botão de ação com formulário opcional | `description` + `instanceName` obrigatórios |
| `@Job` | tarefa agendada | `name` termina com `SP`; `frequency` começa com `&` |
| `@Transactional` | controle de transação | usar `TransactionType` (UPPER_SNAKE_CASE) |
| `@Valid` | validação de DTO de entrada | anotações JSR 303/380 nos campos do DTO |
| `@ControllerAdvice` | tratamento centralizado de exceções | handlers retornam POJO, nunca void |
| `@Value` | injeção de valor de fontes externas | eager (direto) ou lazy (`Provider<T>`) |

## Exemplo mínimo de @Controller

```java
@Controller(serviceName = "PedidoControllerSP")
public class PedidoController {

    private final PedidoRepository pedidoRepository;

    @Inject
    public PedidoController(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }

    @Transactional
    public List<PedidoDTO> consultarPorPeriodo(PedidoFiltroDTO filtro) {
        return pedidoRepository.buscarPorPeriodo(filtro.getDataInicial(), filtro.getDataFinal());
    }
}
```

## Exemplo mínimo de @Repository

```java
@Repository
public interface PedidoRepository extends JapeRepository<BigDecimal, Pedido> {

    @Criteria("DTPEDIDO >= :dataInicial AND DTPEDIDO <= :dataFinal")
    List<Pedido> buscarPorPeriodo(
        @Parameter("dataInicial") Timestamp dataInicial,
        @Parameter("dataFinal") Timestamp dataFinal
    );

    @Modifying
    @NativeQuery("UPDATE TGFCAB SET VLRNOTA = :valor WHERE NUNOTA = :nunota")
    int atualizarValor(@Parameter("valor") BigDecimal valor, @Parameter("nunota") BigDecimal nunota);
}
```

## Regras críticas

1. **`@Inject` deve ser `com.google.inject.Inject`** — nunca `javax.inject.Inject`
2. **Injeção via construtor** — nunca por campo ou setter
3. **`serviceName` termina com `SP`** — para `@Controller`, `@Service` (legado) e `@Job`
4. **Métodos de `@Controller`/`@Service` recebem/retornam DTOs** — nunca `ServiceContext`
5. **`@Repository` estende `JapeRepository<ID, Entity>`**
6. **`@Parameter("nome")`** em queries — não `@Param`
7. **`@Modifying` obrigatório** para queries de escrita (`@NativeQuery` INSERT/UPDATE/DELETE)
8. **`@Listener` usa `instanceNames`** = nome da instância/entidade, não da tabela
9. **`@Job frequency` começa com `&`** antes da expressão CRON
10. **`@ExceptionHandler` retorna POJO** — nunca void ou ServiceContext
11. **Use `TransactionType` (UPPER_SNAKE_CASE)** em `@Transactional`; `EJBTransactionType` (PascalCase) na anotação de classe (`@Controller`/`@Service`)

## Erros comuns

| Erro | Causa | Correção |
|-------|-------|-----|
| DI não resolvida | `javax.inject.Inject` usado | trocar por `com.google.inject.Inject` |
| Endpoint não registrado | `serviceName` sem `SP` | adicionar sufixo `SP` |
| `ServiceContext` nos parâmetros | padrão legado | substituir por DTOs |
| Query falha em runtime | `@Modifying` ausente na escrita | adicionar `@Modifying` |
| Binding de parâmetro errado | `@Param` usado | trocar por `@Parameter` |
| Listener não dispara | `instanceNames` = nome da tabela | usar nome da entidade/instância |
| Job não agenda | `frequency` sem `&` | adicionar prefixo `&` à CRON |
| `@ExceptionHandler` engolido | catch-all genérico `Exception.class` | usar tipos específicos de exceção |
| Enum de TX divergente | mistura `TransactionType` / `EJBTransactionType` | `@Transactional` → `TransactionType`, `@Controller`/`@Service` → `EJBTransactionType` |

## Estrutura do projeto

Para o layout completo de diretórios do Add-on Studio e a configuração
`application.yaml`, veja `references/estrutura-do-projeto.md` e `references/add-on-studio.md`.

## Para schema de banco (dbscripts, datadictionary)

Use dbscripts + datadictionary para mudanças de schema; mantenha o SQL portável entre
Oracle/MSSQL com os helpers de macro.
