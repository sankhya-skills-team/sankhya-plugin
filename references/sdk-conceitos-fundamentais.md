# SDK Sankhya — Conceitos Fundamentais

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Por que Mudar? Legado vs. SDK

| Aspecto | Abordagem Antiga | SDK Sankhya |
|---|---|---|
| Segurança de Tipos | "Strings mágicas" | Tipos seguros em compilação |
| Validação | Manual e verbosa | Automática com `@Valid` |
| Injeção de Dependência | Manual (`JapeFactory`, `new`) | Automática (`@Inject`) |
| Controle de Transação | Manual e complexo | Declarativo (`@Transactional`) |
| Testabilidade | Difícil de isolar | Nativamente testável com mocks |
| Manutenibilidade | Código acoplado e verboso | Código limpo e desacoplado |

---

## Os 4 Pilares

### 1. Mapeamento Objeto-Relacional (ORM) com POJOs

Substitui o `DynamicVO` por classes Java anotadas, similar ao JPA.

```java
@JapeEntity(entity = "Veiculo", table = "TGFVEI")
public class Veiculo {
    @Id
    @Column(name = "CODVEICULO")
    private Long codVeiculo;

    @Column(name = "PLACA")
    private String placa;
}
```

### 2. Injeção de Dependências (DI)

Baseado em **Guice**. Declare dependências no construtor com `@Inject` — o SDK injeta automaticamente.

```java
@Inject
public VeiculoService(VeiculoRepository repository) {
    this.repository = repository;
}
```

Estereótipos:
- `@Service` — ponto de entrada externo (controller)
- `@Component` — lógica de negócio, utilitários, helpers
- `@Repository` — acesso a dados
- `@Inject` — solicita injeção via construtor

### 3. Padrão Repository

Interface que estende `JapeRepository`. O SDK gera a implementação.

```java
@Repository
public interface VeiculoRepository extends JapeRepository {
    @Criteria("marca = :marca AND ativo = 'S'")
    List findAllAtivosPorMarca(@Parameter("marca") String marca);
}
```

### 4. Controle Transacional Declarativo

`@Transactional` garante atomicidade. Em caso de exceção, rollback automático.

```java
@Transactional
public void criarPedidoCompleto(PedidoDTO dados) {
    repository.save(dados.toPedido());
    dados.getItens().forEach(item -> repository.saveItem(item));
    // Se qualquer operação falhar, TUDO é desfeito
}
```

---

## Integração dos Conceitos

```
Request → @Service (@Valid DTO) → @Component (negócio) → @Repository → @JapeEntity → BD
```

```java
// 1. Entidade
@JapeEntity(entity = "Veiculo", table = "TGFVEI")
public class Veiculo { @Id @Column(name="CODVEICULO") private Long id; }

// 2. DTO com validação
@Data public class VeiculoDTO {
    @NotBlank private String placa;
}

// 3. Repository
@Repository
public interface VeiculoRepository extends JapeRepository {
    Optional findByPlaca(String placa);
}

// 4. Componente de negócio
@Component
public class VeiculoService {
    private final VeiculoRepository repository;
    @Inject public VeiculoService(VeiculoRepository repository) { this.repository = repository; }
    public void cadastrar(VeiculoDTO dto) {
        Veiculo v = new Veiculo(); v.setPlaca(dto.getPlaca());
        repository.save(v);
    }
}

// 5. Controller (ponto de entrada)
@Service(serviceName = "VeiculoServiceSP")
public class VeiculoController {
    private final VeiculoService veiculoService;
    @Inject public VeiculoController(VeiculoService veiculoService) { this.veiculoService = veiculoService; }

    @Transactional
    public void cadastrar(@Valid VeiculoDTO dto) {
        veiculoService.cadastrar(dto);
    }
}
```

---

## Fonte

https://developer.sankhya.com.br/docs/conceitos-fundamentais
