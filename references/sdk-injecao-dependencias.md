# SDK Sankhya — Injeção de Dependências (DI)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Visão Geral

A DI é um dos pilares do SDK. Em vez de instanciar objetos com `new`, você declara dependências no construtor e o SDK as injeta automaticamente. Baseado em **Guice**.

> **Importante:** Use `com.google.inject.Inject` — NÃO `javax.inject.Inject`.

---

## Estereótipos

| Anotação | Propósito | Ciclo de Vida |
|---|---|---|
| `@Service` | Ponto de entrada externo (endpoint) | Prototype |
| `@Controller` | Alias semântico para `@Service` | Prototype |
| `@Job` | Tarefa agendada | Prototype |
| `@Repository` | Interface de acesso a dados | Prototype |
| `@Component` | Qualquer classe gerenciada (negócio, helpers, validadores) | Singleton |

---

## Como Usar

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoController {

    private final PedidoService pedidoService;

    @Inject  // com.google.inject.Inject
    public PedidoController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }

    @Transactional
    public Long criarPedido(@Valid PedidoDTO pedido) {
        return pedidoService.criar(pedido);
    }
}

@Component
public class PedidoService {

    private final PedidoRepository repository;
    private final ValidadorPedido validador;

    @Inject
    public PedidoService(PedidoRepository repository, ValidadorPedido validador) {
        this.repository = repository;
        this.validador = validador;
    }

    @Transactional
    public Long criar(PedidoDTO dto) {
        validador.validar(dto);
        return repository.save(dto.toEntity()).getId();
    }
}
```

**Regras:**
- Apenas **um construtor** anotado com `@Inject` por classe
- Todos os parâmetros devem ser tipos gerenciados pelo SDK
- Ciclos de dependência (A→B→A) causam falha na inicialização (fail-fast)

---

## Múltiplas Implementações

### Com `bindWith` (recomendado — type-safe)

```java
// 1. Crie uma anotação qualificadora
@Qualifier
@Retention(RetentionPolicy.RUNTIME)
public @interface Primary {}

// 2. Anote a implementação
@Component(bindWith = Primary.class)
public class EmailNotificationService implements NotificationService { ... }

@Component
public class SmsNotificationService implements NotificationService { ... }

// 3. Injete
@Inject
public OrderProcessor(@Primary NotificationService email, NotificationService sms) { ... }
```

### Com `name` (strings — menos seguro)

```java
@Component(name = "creditCard")
public class CreditCardGateway implements PaymentGateway { ... }

@Inject
public CheckoutService(@Named("creditCard") PaymentGateway gateway) { ... }
```

| | `bindWith` | `name` |
|---|---|---|
| Segurança de tipo | Compile-time | Runtime |
| Refatoração | Segura (IDE) | Manual |
| Recomendado | Sim | Casos simples |

### Injetando todas as implementações

```java
@Inject
public EventDispatcher(Set<EventHandler> handlers) {
    this.handlers = handlers; // todas as implementações registradas
}
```

---

## Boas Práticas

- Sempre use injeção via **construtor** — dependências explícitas e campos `final`
- Programe para **interfaces**, não implementações
- Evite ciclos de dependência — indicam problema de design
- Classes com muitas dependências violam o SRP — considere dividir

## Antipadrões

- `@Service` com lógica de negócio complexa — delegue para `@Component`
- Estado mutável em singletons — use `AtomicInteger` ou estruturas thread-safe
- Dependências circulares — reorganize ou introduza uma abstração

---

## Fonte

https://developer.sankhya.com.br/docs/injecao-de-dependencias
