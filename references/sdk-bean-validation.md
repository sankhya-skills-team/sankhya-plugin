# Bean Validation (SDK Sankhya)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## O que é

Bean Validation permite definir regras de validação diretamente nos DTOs e entidades usando anotações (JSR 303/380). O SDK executa a validação automaticamente antes de chamar o método do `@Service`.

## Como Ativar

Anote o parâmetro com `@Valid` no método do `@Service`:

```java
@Service(name = "UsuarioServiceSP")
public class UsuarioService {

    @Transactional
    public void cadastrarUsuario(@Valid UsuarioDTO usuario) {
        // só executa se o objeto passar em todas as validações
        businessService.salvar(usuario);
    }
}
```

Se qualquer validação falhar, o SDK lança exceção automaticamente com mensagem de erro clara.

---

## Anotações Disponíveis

### Nulidade e Conteúdo

| Anotação | Aplica-se a | Descrição |
|---|---|---|
| `@NotNull` | Qualquer tipo | Não pode ser `null` |
| `@NotBlank` | `String` | Não pode ser `null`, vazia ou só espaços |
| `@NotEmpty` | `String`, coleções, arrays | Não pode ser `null` nem vazia |

```java
@NotNull(message = "O ID é obrigatório.")
private Long id;

@NotBlank(message = "O nome é obrigatório.")
private String nome;

@NotEmpty(message = "O pedido deve ter pelo menos um item.")
private List<ItemDTO> itens;
```

### Tamanho

```java
@Size(min = 3, max = 50, message = "Nome deve ter entre 3 e 50 caracteres.")
private String nome;

@Size(max = 5, message = "Máximo 5 tags.")
private List<String> tags;

// Hibernate Validator — específico para String
@Length(min = 10, max = 500, message = "Descrição deve ter entre 10 e 500 caracteres.")
private String descricao;
```

### Numérico

```java
@Min(value = 1, message = "Quantidade mínima é 1.")
private int quantidade;

@Max(value = 99, message = "Desconto máximo é 99%.")
private double desconto;

@DecimalMin(value = "0.01", message = "Valor mínimo é 0.01.")
private BigDecimal valor;

@DecimalMax(value = "999999.99", inclusive = false, message = "Valor deve ser menor que 999999.99.")
private BigDecimal limite;

@Digits(integer = 10, fraction = 2, message = "Máximo 10 dígitos inteiros e 2 decimais.")
private BigDecimal preco;

@Positive(message = "ID deve ser positivo.")
private Long id;

@PositiveOrZero(message = "Saldo não pode ser negativo.")
private BigDecimal saldo;
```

### Formato

```java
@Email(message = "Formato de e-mail inválido.")
private String email;

@Pattern(regexp = "[A-Z]{2}[0-9]{4}", message = "Placa deve seguir o formato AA1234.")
private String placa;
```

### Data e Hora

```java
@Future(message = "A data de entrega deve ser no futuro.")
private LocalDate dataEntrega;

@PastOrPresent(message = "A data de nascimento não pode ser no futuro.")
private LocalDate dataNascimento;
```

---

## Validação Aninhada

Use `@Valid` no campo para validar objetos dentro de outros objetos:

```java
public class PedidoDTO {
    @NotNull
    private Long idCliente;

    @Valid       // valida cada ItemDTO da lista
    @NotEmpty
    private List<ItemDTO> itens;
}

public class ItemDTO {
    @NotNull
    private Long idProduto;

    @Positive(message = "A quantidade deve ser positiva.")
    private int quantidade;
}
```

---

## Boas Práticas

- Aplique as anotações nos **DTOs**, não nas entidades de persistência
- Sempre forneça uma `message` clara e útil
- Combine anotações no mesmo campo quando necessário (ex: `@NotNull` + `@Size`)
- Para regras complexas de negócio, crie anotações de validação customizadas

---

## Fonte

https://developer.sankhya.com.br/docs/bean-validation
