# Camada de Controller (@Controller)

> **Substituto oficial de `@Service`.** A anotação `@Service` foi marcada como `@Deprecated` e será removida em versões futuras — a própria plataforma recomenda migrar para `@Controller`. Use `@Controller` em todo código novo.

## O que é

`@Controller` marca classes que representam pontos de entrada da API interna do add-on. Cada método público é auto-exposto como um endpoint de serviço. Controllers **orquestram** o fluxo da requisição — **nunca** contêm lógica de negócio (essa vai para `@Component`/camada de serviço).

Roda sobre o mesmo runtime do antigo `@Service`, mas com um modelo mais limpo: injeção de dependência via `@Inject` no construtor, controle transacional granular por método (`@Transactional`) e retorno tipado via DTO — sem o boilerplate de `ServiceContext` + `JapeSession` manual do padrão clássico.

---

## Anatomia / Imports

```java
import br.com.sankhya.studio.annotations.Controller;
import br.com.sankhya.studio.annotations.enums.EJBTransactionType;
import br.com.sankhya.studio.persistence.Transactional;
import com.google.inject.Inject;
import javax.validation.Valid;

@Controller(
    serviceName = "EstoqueControllerSP",            // Obrigatório, sufixo "SP"
    transactionType = EJBTransactionType.Supports    // Opcional (Supports é o padrão)
)
public class EstoqueController {

    private final EstoqueRepository estoqueRepository;   // dependências como final
    private final EstoqueBusiness estoqueBusiness;
    private final EstoqueMapper estoqueMapper;

    @Inject                                              // injeção via construtor
    public EstoqueController(
        EstoqueRepository estoqueRepository,
        EstoqueBusiness estoqueBusiness,
        EstoqueMapper estoqueMapper
    ) {
        this.estoqueRepository = estoqueRepository;
        this.estoqueBusiness = estoqueBusiness;
        this.estoqueMapper = estoqueMapper;
    }

    @Transactional                                       // métodos que alteram dados
    public EstoqueDTO atualizarEstoque(@Valid AtualizarEstoqueRequest request) {
        Estoque estoque = estoqueBusiness.processarAtualizacao(request);
        Estoque salvo = estoqueRepository.save(estoque);
        return estoqueMapper.toDTO(salvo);               // Domain -> DTO
    }

    public List<EstoqueDTO> listarPorProduto(BigDecimal codProduto) {
        return estoqueRepository.findByProduto(codProduto).stream()
            .map(estoqueMapper::toDTO)
            .collect(Collectors.toList());
    }
}
```

---

## `serviceName` (obrigatório, sufixo `SP`)

Nome do serviço registrado na plataforma. **Deve** terminar com `SP`. Define a URL de acesso: cada método público vira `<serviceName>.<nomeDoMetodo>`.

```java
@Controller(serviceName = "PedidoControllerSP")   // -> PedidoControllerSP.criar, PedidoControllerSP.cancelar, ...
```

`serviceName` sem sufixo `SP` = endpoint retorna 404.

---

## URL de Acesso

```
<dns>/<contexto-addon>/service.sbr?serviceName=<serviceName>.<nomeDoMetodo>&mgeSession=<jsessionid>
```

O `contexto-addon` corresponde ao `rootProject.name` no `settings.gradle`.

**Exemplo:** `http://localhost:8080/meu-addon/service.sbr?serviceName=PedidoControllerSP.criar&mgeSession=ABC123`

## Autenticação

Toda requisição exige `mgeSession`. O `jsessionId` é obtido com `MobileLogin`:

```bash
curl --location 'http://localhost:8080/mge/service.sbr?serviceName=MobileLoginSP.login&outputType=json' \
--header 'Content-Type: application/json' \
--data '{
    "requestBody": {
        "NOMUSU": {"$": "USUARIO"},
        "INTERNO": {"$": "SENHA_DO_USUARIO"}
    }
}'
```

O retorno contém `jsessionId` para usar como `mgeSession`. Em ambientes com Gateway Sankhya, o MobileLogin não é necessário — o Gateway gerencia o token.

---

## Controle Transacional (`transactionType`)

Define o comportamento transacional **padrão** de todos os métodos da classe.

| TransactionType | Descrição | Quando usar |
|---|---|---|
| `Supports` | (Padrão) Junta-se à transação existente, ou executa sem. | Controllers que misturam leitura + escrita |
| `Required` | Usa transação existente ou cria nova. | Controllers 100% escrita |
| `NotSupported` | Executa fora de qualquer transação (suspende se existir). | Controllers 100% leitura (melhor performance) |

`@Transactional` em um método **sempre tem precedência** sobre o `transactionType` da classe.

```java
@Controller(serviceName = "MeuControllerSP", transactionType = EJBTransactionType.NotSupported)
public class MeuController {

    public List<MeuDTO> listar() { ... }                 // usa o padrão da classe (sem transação)

    @Transactional
    public MeuDTO criar(@Valid MeuRequest request) { ... }  // sobrepõe — transação própria

    @Transactional(Transactional.TxType.REQUIRES_NEW)
    public void processarBatch() { ... }                 // transação nova, isolada
}
```

### Quando usar `@Transactional`

| Operação | `@Transactional`? | Motivo |
|---|---|---|
| Create / Update / Delete | Sim | Garante atomicidade |
| Leitura simples | Não | Sem necessidade de transação |
| Leitura + escrita no mesmo método | Sim | Garante consistência |
| Operação idempotente (sem side effects) | Não | Desnecessário |

---

## DTOs (Request / Response)

Controllers **nunca** expõem entidades do domínio. Use DTOs como contratos de entrada/saída.

### Request DTO — Lombok `@Data` + validação `javax.validation`

```java
import lombok.Data;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.DecimalMin;
import java.math.BigDecimal;

@Data
public class CriarPedidoRequest {

    @NotNull(message = "O código do parceiro é obrigatório.")
    private BigDecimal codParceiro;

    @NotBlank(message = "A descrição é obrigatória.")
    private String descricao;

    @DecimalMin(value = "0.01", message = "O valor deve ser maior que zero.")
    private BigDecimal valor;

    private String observacao;   // opcional — sem validação
}
```

### Response DTO — `@Data`, sem validação

```java
@Data
public class CriarPedidoResponse {
    private BigDecimal numeroPedido;
    private BigDecimal valorTotal;
    private String status;
}
```

### Anotações de validação comuns

| Anotação | Uso |
|---|---|
| `@NotNull` | Campo obrigatório (qualquer tipo) |
| `@NotBlank` | String obrigatória e não vazia |
| `@NotEmpty` | Collection/String não vazia |
| `@DecimalMin` | Valor mínimo (BigDecimal) |
| `@Size` | Tamanho min/max de String ou Collection |
| `@Valid` | Validação em cascata (objetos nested) — **ativa a validação no parâmetro do método** |

`@Valid` no parâmetro faz o framework validar antes de executar o método. Falha = erro retornado sem chegar a rodar o corpo.

---

## Formato de Requisição e Resposta

> **Gotcha crítico:** a chave dentro de `requestBody` é o **nome do parâmetro Java**, não o nome da classe DTO. Método `criar(CriarPedidoRequest request)` → chave `"request"`. Se fosse `criar(CriarPedidoRequest pedido)` → chave `"pedido"`. Errar a chave = binding silencioso para `null`.

### Request
```json
{
    "serviceName": "PedidoControllerSP.criar",
    "requestBody": {
        "request": { "codParceiro": 12345, "descricao": "Pedido teste", "valor": 150.50 }
    }
}
```

### Response de sucesso (`status: "1"`)
```json
{
    "serviceName": "PedidoControllerSP.criar",
    "status": "1",
    "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
    "responseBody": { "numeroPedido": 987654, "valorTotal": 551.00, "status": "PENDENTE" }
}
```

### Response de erro (`status: "0"`)
```json
{
    "serviceName": "PedidoControllerSP.criar",
    "status": "0",
    "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
    "statusMessage": "Erro de validação: a descrição é obrigatória"
}
```

Status: `"1"` = Sucesso, `"0"` = Erro, `"3"` = Timeout, `"4"` = Cancelado por concorrência. Em erro, `responseBody` não vem — a mensagem fica em `statusMessage`.

---

## Tipo de Retorno dos Métodos

- Método que retorna dados → retorna o **DTO de resposta diretamente** (o framework serializa em `responseBody`).
- Método sem dados de saída → `void`.

```java
public PedidoResponse criar(@Valid CriarPedidoRequest request) { ...; return mapper.toResponse(r); }

@Transactional
public void cancelar(@Valid CancelarPedidoRequest request) { cancelarService.execute(request.getNuPedido()); }
```

### Catálogo de formas de método

| Forma | Assinatura típica |
|---|---|
| Entrada + saída (CRUD) | `PedidoResponse criar(@Valid CriarPedidoRequest req)` |
| Só entrada (ação sem retorno) | `void cancelar(@Valid CancelarPedidoRequest req)` |
| Só saída (consulta) | `List<ProdutoDTO> listar()` |
| Sem entrada e sem saída (trigger) | `void sincronizar()` |

### Impressão / arquivo na resposta (`ServiceContext`)

```java
@Transactional
public EmitirPedidoResponse emitir(@Valid EmitirPedidoRequest request) {
    Resultado resultado = emitirService.execute(request.getNuPedido());
    Impressao impressao = gerarPdfService.execute(resultado);

    ServiceContext ctx = ServiceContext.getCurrent();
    ctx.putHttpSessionAttribute(impressao.getLabel(), impressao.getFile());

    return mapper.toEmitirResponse(resultado);
}
```

---

## Tratamento de Exceções

**Nunca** capture exceção de negócio no controller — deixe propagar para o `@ControllerAdvice`. Ver `sdk-controller-advice.md` (handler não pode retornar `void`, rollback automático, proibição de `Exception.class`).

---

## Convenções de Nome

| Convenção | Padrão | Exemplo |
|---|---|---|
| Classe | `<Feature>Controller` | `PedidoController` |
| `serviceName` | `<Feature>ControllerSP` | `PedidoControllerSP` |
| Request DTO | `<Ação>Request` ou `<Ação><Feature>Request` | `CriarPedidoRequest` |
| Response DTO | `<Ação>Response` ou `<Ação><Feature>Response` | `EmitirPedidoResponse` |
| Mapper | `<Feature>RestMapper` | `PedidoRestMapper` |

---

## Checklist: Novo Controller

1. [ ] Anotar com `@Controller(serviceName = "<Feature>ControllerSP")` (sufixo `SP`).
2. [ ] Definir `transactionType` adequado (ou usar padrão `Supports`).
3. [ ] Injetar dependências via construtor com `@Inject` (campos `final`).
4. [ ] Request DTOs com validação (`@NotNull`, `@NotBlank`, ...).
5. [ ] Response DTOs (sem validação).
6. [ ] `@Valid` no parâmetro dos métodos que recebem DTOs.
7. [ ] `@Transactional` nos métodos que alteram dados.
8. [ ] Retorno adequado (DTO de resposta ou `void`).
9. [ ] **NÃO** colocar lógica de negócio — delegar para a camada de serviço.
10. [ ] **NÃO** capturar exceções — deixar o `@ControllerAdvice` tratar.

---

## Antipadrões

| Antipadrão | Correção |
|---|---|
| Retornar entidade do domínio diretamente | Response DTO + mapper |
| Lógica de negócio no controller | Mover para `@Component`/camada de serviço |
| `try/catch` de exceção de negócio no controller | Deixar o `@ControllerAdvice` tratar |
| Controller acessando Repository diretamente | Intermediar via serviço |
| Controller chamando Gateway diretamente | Intermediar via serviço |
| `serviceName` sem sufixo `SP` | Sempre `<Nome>SP` |
| Esquecer `@Transactional` em método de escrita | Adicionar |
| Esquecer `@Valid` no parâmetro | Adicionar para ativar validação |
| Adicionar `@Component` no controller | `@Controller` já é gerenciado — não misturar |
| Capturar exceção e retornar `null` | Deixar propagar para o `@ControllerAdvice` |

---

## Fonte

https://developer.sankhya.com.br/docs/camada-de-controller-controller
