# SDK Sankhya — Tratamento Global de Exceções (@ControllerAdvice)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Visão Geral

`@ControllerAdvice` cria um ponto centralizado de tratamento de exceções para todos os `@Service`. Intercepta exceções lançadas durante a execução e retorna respostas padronizadas em JSON.

**Benefícios:**
- Elimina `try-catch` duplicado em cada serviço
- Respostas de erro consistentes em toda a aplicação
- Rollback automático da transação ativa quando uma exceção é capturada
- Serviços focados apenas na lógica de negócio

---

## Como Implementar

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger logger = Logger.getLogger(GlobalExceptionHandler.class.getName());

    @ExceptionHandler({ObjectNotFoundException.class})
    public ErrorResponse handleObjectNotFound(ObjectNotFoundException e) {
        logger.log(Level.WARNING, "Recurso não encontrado", e);
        return new ErrorResponse("NOT_FOUND", "O recurso solicitado não existe.", 404);
    }

    @ExceptionHandler({ValidationException.class})
    public ErrorResponse handleValidation(ValidationException e) {
        logger.log(Level.WARNING, "Erro de validação", e);
        return new ErrorResponse("VALIDATION_ERROR", e.getMessage(), 400);
    }

    @ExceptionHandler({IOException.class, SQLException.class})
    public ErrorResponse handleInfrastructure(Exception e) {
        logger.log(Level.SEVERE, "Erro de infraestrutura", e);
        return new ErrorResponse("INFRASTRUCTURE_ERROR", "Erro ao processar a requisição.", 503);
    }
}
```

**Regras:**
- `@ExceptionHandler` aceita array de classes: `@ExceptionHandler({ExcA.class, ExcB.class})`
- O método recebe a exceção como parâmetro
- **Nunca retorne `void`** — o retorno é serializado para JSON automaticamente via Gson
- Rollback automático da transação ativa quando a exceção é capturada

---

## Serviços ficam limpos

```java
@Service(serviceName = "PedidoServiceSP")
public class PedidoService {

    @Transactional
    public void criarPedido(@Valid PedidoDTO pedido) {
        // Sem try-catch — o GlobalExceptionHandler cuida dos erros
        businessService.criar(pedido);
    }
}
```

---

## Exemplo de DTO de Resposta

```java
public class ErrorResponse {
    private String code;
    private String message;
    private int status;
    private long timestamp;

    public ErrorResponse(String code, String message, int status) {
        this.code = code;
        this.message = message;
        this.status = status;
        this.timestamp = System.currentTimeMillis();
    }
    // getters
}
```

---

## Antipadrões

- **`void` como retorno** — não funciona; sempre retorne um objeto
- **`@ExceptionHandler({Exception.class})`** — captura tudo e impede handlers mais específicos
- **Handlers duplicados para a mesma exceção** — comportamento indefinido
- **Expor stack traces ao usuário** — logue internamente, retorne mensagem genérica
- **Métodos sem `@ExceptionHandler`** em classes `@ControllerAdvice` — são ignorados

---

## Fonte

https://developer.sankhya.com.br/docs/11_controller_advice
