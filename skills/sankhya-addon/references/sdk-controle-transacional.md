# SDK Sankhya — Controle Transacional (@Transactional)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Visão Geral

`@Transactional` garante atomicidade: ou todas as operações são salvas, ou nenhuma. Em caso de exceção não checada, rollback automático.

```java
@Transactional
public void criarNovoPedido(PedidoDTO dto) {
    cabecalhoRepository.save(dto.getCabecalho());

    if (dto.getItens().isEmpty()) {
        throw new IllegalStateException("Pedido deve ter pelo menos um item.");
        // rollback automático — o cabeçalho salvo acima é desfeito
    }

    dto.getItens().forEach(item -> itemRepository.save(item));
}
```

---

## Tipos de Propagação

```java
import br.com.sankhya.studio.transaction.TransactionType;

@Transactional(type = TransactionType.REQUIRES_NEW)
public void meuMetodo() { ... }
```

| `TransactionType` | Descrição | Quando Usar |
|---|---|---|
| `REQUIRED` | **(Padrão)** Usa transação existente ou cria nova | Maioria dos casos — operações de escrita |
| `REQUIRES_NEW` | Sempre cria nova transação, suspendendo a atual | Log de auditoria independente da transação principal |
| `NOT_SUPPORTED` | Executa fora de qualquer transação | Consultas somente leitura — melhor performance |
| `SUPPORTS` | Junta-se à transação existente, ou executa sem | Raro — método que pode ou não precisar de transação |
| `MANDATORY` | Exige transação já existente; lança exceção se não houver | Garantir que o método só seja chamado em contexto transacional |
| `NEVER` | Lança exceção se transação estiver ativa | Garantir que o método nunca execute em transação |

---

## Exemplo: `REQUIRES_NEW` para Auditoria

```java
@Component
public class AuditoriaService {

    @Transactional(type = TransactionType.REQUIRES_NEW)
    public void registrarErro(String operacao, String erro) {
        // Salvo mesmo se a transação principal sofrer rollback
    }
}

@Service(serviceName = "ProcessamentoServiceSP")
public class ProcessamentoService {

    private final AuditoriaService auditoriaService;

    @Inject
    public ProcessamentoService(AuditoriaService auditoriaService) {
        this.auditoriaService = auditoriaService;
    }

    @Transactional
    public void processarDados() {
        try {
            // lógica de negócio...
            throw new RuntimeException("Erro de negócio!");
        } finally {
            auditoriaService.registrarErro("processarDados", "Erro de negócio!");
            // log salvo mesmo com rollback da transação principal
        }
    }
}
```

---

## Boas Práticas

- Use `@Transactional` na **camada de serviço** (`@Component`, `@Service`)
- Só funciona em métodos **`public`** — métodos privados não herdam o comportamento
- Para consultas somente leitura, use `NOT_SUPPORTED` para melhor performance
- Mantenha transações **curtas** — evite locks longos no banco
- Use `REQUIRES_NEW` para logs de auditoria que devem ser salvos independentemente

## Antipadrões

- Transações muito longas com operações lentas (I/O, chamadas externas)
- Capturar exceções sem relançar dentro de um método `@Transactional` — impede o rollback
- Usar `@Transactional` em métodos privados — não tem efeito

---

## Fonte

https://developer.sankhya.com.br/docs/controle-transacional
