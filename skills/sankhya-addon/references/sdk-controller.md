# SDK Sankhya — Camada de Controller (@Controller)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## O que é

`@Controller` é um alias semântico para `@Service`. Usado para marcar classes que representam pontos de entrada da API, separando controllers de serviços de negócio internos. Recomendado para clareza arquitetural em projetos maiores.

---

## Padrão de Implementação

- Injete dependências via `@Inject` no construtor
- Use `@Transactional` em métodos que alteram dados
- Use DTOs como contratos de entrada e saída — nunca exponha entidades do domínio
- Mantenha lógica de negócio fora do controller — delegue para `@Component`

```java
@Controller
public class EstoqueController {

    private final EstoqueRepository estoqueRepository;
    private final EstoqueBusiness estoqueBusiness;
    private final EstoqueMapper estoqueMapper;

    @Inject
    public EstoqueController(
        EstoqueRepository estoqueRepository,
        EstoqueBusiness estoqueBusiness,
        EstoqueMapper estoqueMapper
    ) {
        this.estoqueRepository = estoqueRepository;
        this.estoqueBusiness = estoqueBusiness;
        this.estoqueMapper = estoqueMapper;
    }

    @Transactional
    public EstoqueDTO atualizarEstoque(@Valid AtualizarEstoqueRequestDTO requestDTO) {
        Estoque estoque = estoqueBusiness.processarAtualizacao(requestDTO);
        Estoque estoqueSalvo = estoqueRepository.save(estoque);
        return estoqueMapper.toDTO(estoqueSalvo);
    }

    public List<EstoqueDTO> listarPorProduto(BigDecimal codProduto) {
        return estoqueRepository.findByProduto(codProduto).stream()
            .map(estoqueMapper::toDTO)
            .collect(Collectors.toList());
    }
}
```

---

## URL de Acesso

```
<dns>/<contexto-addon>/service.sbr?serviceName=<nomeDoServico>.<nomeDoMetodo>&mgeSession=<jsessionid>
```

O `contexto-addon` corresponde ao `rootProject.name` no `settings.gradle`.

## Autenticação

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

O retorno contém `jsessionId` para usar como `mgeSession`. Em ambientes com Gateway, o MobileLogin não é necessário.

---

## Controle Transacional (`transactionType`)

| TransactionType | Descrição | Quando Usar |
|---|---|---|
| `Required` | Usa transação existente ou cria nova | Operações de escrita |
| `NotSupported` | Executa fora de qualquer transação | Consultas — melhor performance |
| `Supported` | Junta-se à transação existente, ou executa sem (padrão) | Leitura que pode ou não estar em transação |

`@Transactional` em um método sempre tem precedência sobre o `transactionType` da classe.

---

## Formato de Requisição e Resposta

### Request
```json
{
    "serviceName": "EstoqueControllerSP.atualizarEstoque",
    "requestBody": {
        "requestDTO": { "codProduto": 100, "quantidade": 50 }
    }
}
```

### Response de sucesso (`status: "1"`)
```json
{
    "serviceName": "EstoqueControllerSP.atualizarEstoque",
    "status": "1",
    "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
    "responseBody": { "codProduto": 100, "saldo": 50 }
}
```

### Response de erro (`status: "0"`)
```json
{
    "serviceName": "EstoqueControllerSP.atualizarEstoque",
    "status": "0",
    "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
    "statusMessage": "Produto não encontrado"
}
```

Status: `"1"` = Sucesso, `"0"` = Erro, `"3"` = Timeout, `"4"` = Cancelado.

---

## Antipadrões

- Retornar entidades do domínio diretamente
- Colocar lógica de negócio complexa no controller
- Capturar exceções de negócio sem relançá-las

---

## Fonte

https://developer.sankhya.com.br/docs/camada-de-controller-controller
