# SDK Sankhya — Iniciando (Getting Started)

> **Acesso Antecipado (Beta):** Requer Add-on Studio plugin versão **2.0.0+**.

## Pré-requisito

```groovy
// build.gradle
buildscript {
    dependencies {
        classpath "br.com.sankhya.studio:gradle-plugin:2.0.+"
    }
}
```

---

## Estrutura de um Serviço Completo

Um serviço SDK é composto por quatro camadas: Entidade → Repositório → DTO → Service.

### 1. Entidade (`@JapeEntity`)

POJOs anotados, similares ao padrão JPA. Substituem o `DynamicVO`.

> A entidade ainda precisa ser definida no Dicionário de Dados para que a plataforma a reconheça.

```java
@Data
@JapeEntity(entity = "Veiculo", table = "TGFVEI")
public class Veiculo {

    @Id
    @Column(name = "CODVEICULO")
    private Long id;

    @Column(name = "PLACA")
    private String placa;

    @Column(name = "ATIVO")
    private boolean ativo;
}
```

**Tipos suportados:** primitivos (`long`, `int`, `boolean`), wrappers (`Long`, `Integer`), `BigDecimal`, `BigInteger`, `String`, `Timestamp`, `LocalDate`, `LocalDateTime`, enums.

### 2. Repositório (`@Repository`)

Interface que estende `JapeRepository`. O SDK gera a implementação automaticamente.

```java
@Repository
public interface VeiculoRepository extends JapeRepository<Long, Veiculo> {

    // busca automática por campo
    Optional<Veiculo> findByPlaca(String placa);

    // consulta com critério JAPE
    @Criteria("this.ATIVO = 'S' AND this.PLACA LIKE :placa")
    List<Veiculo> findAtivosPorPlaca(String placa);

    // exclusão customizada
    @Delete("this.PLACA = :placa")
    void deleteByPlaca(String placa);
}
```

Retornos possíveis: `Optional<T>`, POJO único, `List<T>`.

### 3. DTO com Bean Validation

```java
@Data
public class VeiculoDTO {

    @NotBlank(message = "A placa não pode ser vazia.")
    @Size(min = 7, max = 8, message = "A placa deve ter entre 7 e 8 caracteres.")
    private String placa;

    private boolean ativo;
}
```

### 4. Service (`@Service`)

Injeção de dependências via construtor (`@Inject`). Lógica de negócio com `@Transactional` e validação com `@Valid`.

```java
@Service
public class VeiculoService {

    private final VeiculoRepository repository;

    @Inject
    public VeiculoService(VeiculoRepository repository) {
        this.repository = repository;
    }

    @Transactional
    public Long cadastrarNovoVeiculo(@Valid VeiculoDTO dto) {
        if (repository.findByPlaca(dto.getPlaca()).isPresent()) {
            throw new IllegalStateException("Veículo com esta placa já existe.");
        }

        Veiculo novoVeiculo = new Veiculo();
        novoVeiculo.setPlaca(dto.getPlaca());
        novoVeiculo.setAtivo(dto.isAtivo());

        return repository.save(novoVeiculo).getId();
    }
}
```

---

## Resumo do Fluxo

```
Request → @Service (@Valid DTO) → Repository (@Criteria/@Query) → @JapeEntity → JAPE/BD
```

- `@Service` — ponto de entrada, orquestra
- `@Valid` — valida o DTO automaticamente
- `@Transactional` — gerencia a transação
- `@Repository` — acesso a dados sem boilerplate
- `@JapeEntity` — mapeamento da tabela

---

## Fonte

https://developer.sankhya.com.br/docs/iniciando
