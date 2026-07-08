# Boas Práticas de Log em Java

## Configuração usando Log4j

```java
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

public class PedidoService {
    private static final Logger logger = LogManager.getLogger(PedidoService.class);
}
```

---

## ❌ Exemplos Ruins

### 1. Mensagem sem contexto
```java
// Ruim: o que falhou? qual pedido? qual usuário?
logger.error("Erro ao processar pedido");
```

### 2. Logar a stack trace manualmente com concatenação
```java
// Ruim: perde a stack trace formatada e desperdiça recursos
logger.error("Erro: " + e.getMessage());
```

### 3. Concatenação de String no log
```java
// Ruim: a String é concatenada MESMO que o nível DEBUG esteja desativado
logger.debug("Usuário encontrado: " + usuario.getNome() + " | ID: " + usuario.getId());
```

### 4. Logar dados sensíveis
```java
// Ruim: NUNCA logue senhas, tokens ou dados pessoais
logger.info("Login do usuário: " + usuario.getEmail() + " | Senha: " + usuario.getSenha());
```

### 5. Log no nível errado
```java
// Ruim: uma regra de negócio esperada não é um ERROR
logger.error("Produto fora de estoque");

// Ruim: uma falha crítica de banco não é apenas DEBUG
logger.debug("Conexão com banco de dados perdida");
```

### 6. Log dentro de loop sem critério
```java
// Ruim: pode gerar milhões de linhas e derrubar a aplicação
for (Pedido pedido : listaDePedidos) {
    logger.info("Processando pedido: " + pedido.getId());
}
```

---

## ✅ Exemplos Bons

### 1. Mensagem com contexto suficiente
```java
// Bom: quem, o quê e qual o estado
logger.error("Falha ao processar pedido | pedidoId={} | usuarioId={} | status={}",
        pedido.getId(), usuario.getId(), pedido.getStatus());
```

### 2. Passar a exceção como argumento (preserva stack trace)
```java
try {
    processarPagamento(pedido);
} catch (PagamentoException e) {
    // Bom: formata a stack trace corretamente
    logger.error("Falha no pagamento | pedidoId={}", pedido.getId(), e);
}
```

### 3. Usar placeholders `{}` para evitar concatenação desnecessária
```java
// Bom: a String só é montada se o nível DEBUG estiver ativo
logger.debug("Usuário encontrado | userId={} | nome={}", usuario.getId(), usuario.getNome());
```

### 4. Usar o nível correto para cada situação
```java
logger.trace("Entrando no método calcularDesconto()");             // detalhe máximo, só em desenvolvimento
logger.debug("Parâmetros recebidos | quantidade={} | preço={}", qtd, preco); // diagnóstico
logger.info("Pedido criado com sucesso | pedidoId={}", pedido.getId());      // evento de negócio
logger.warn("Tentativa de acesso a recurso inativo | recursoId={}", id);     // situação inesperada mas recuperável
logger.error("Falha crítica ao salvar no banco", e);                         // erro que precisa de atenção
```

### 5. Proteger logs custosos com verificação de nível
```java
// Bom: evita serialização desnecessária de objetos pesados
if (logger.isDebugEnabled()) {
    logger.debug("Payload completo do pedido: {}", toJson(pedido));
}
```

### 6. Log em loops com critério (amostragem ou apenas falhas)
```java
for (Pedido pedido : listaDePedidos) {
    try {
        processarPedido(pedido);
    } catch (Exception e) {
        // Bom: loga apenas os casos que realmente importam
        logger.error("Falha ao processar pedido no lote | pedidoId={}", pedido.getId(), e);
    }
}
logger.info("Lote processado | total={} | falhas={}", total, falhas);
```

---

## Tabela de Referência: Qual nível usar?

| Nível   | Quando usar |
|---------|-------------|
| `TRACE` | Fluxo interno detalhado, entrada/saída de métodos, apenas em dev/debug |
| `DEBUG` | Valores de variáveis, diagnóstico de lógica, desativado em produção |
| `INFO`  | Eventos de negócio relevantes: criação de pedido, login bem-sucedido |
| `WARN`  | Situações inesperadas mas que a aplicação consegue contornar |
| `ERROR` | Falhas que afetam o usuário ou exigem intervenção imediata |

---

## Resumo das Boas Práticas

- **Contexto é rei:** inclua IDs, estados e parâmetros relevantes na mensagem.
- **Use placeholders `{}`** em vez de concatenar Strings.
- **Passe a exceção como último argumento** para preservar a stack trace.
- **Nunca logue dados sensíveis** (senhas, CPFs, tokens, cartões).
- **Escolha o nível correto** — `ERROR` é para erros reais, não validações de negócio.
