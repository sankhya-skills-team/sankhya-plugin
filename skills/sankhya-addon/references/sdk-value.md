# SDK Sankhya — Injeção de Valores (@Value)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## O que é

`@Value` injeta valores de configuração (variáveis de ambiente, propriedades do sistema ou parâmetros Sankhya) diretamente em campos de componentes gerenciados pelo SDK.

---

## Fontes Disponíveis (`ValueType`)

| Tipo | Fonte | Como definir |
|---|---|---|
| `ENV_VAR` | Variável de ambiente | `export DATABASE_URL=...` |
| `SYSTEM_PROPERTY` | Propriedade do sistema | `-Dserver.port=9090` |
| `SANKHYA_PARAM` | Parâmetro do sistema Sankhya | Configurado no sistema |
| `UNDEFINED` | Sempre usa `defaultValue` | — |

---

## Anatomia da Anotação

```java
@Value(
    value        = "PROPERTY_NAME",   // nome da propriedade (alternativa a param)
    param        = "PROPERTY_NAME",   // nome do parâmetro (tem precedência sobre value)
    group        = "GROUP_NAME",      // grupo (apenas para SANKHYA_PARAM)
    type         = ValueType.ENV_VAR, // obrigatório
    defaultValue = "default"          // obrigatório — fallback quando não encontrado
)
```

---

## Injeção Eager vs. Lazy

### Eager — valor resolvido na criação do objeto

```java
@Value(value = "server.port", type = ValueType.SYSTEM_PROPERTY, defaultValue = "8080")
private Integer serverPort;

@Value(value = "debug.enabled", type = ValueType.SYSTEM_PROPERTY, defaultValue = "false")
private Boolean debugEnabled;
```

Use quando o valor é sempre necessário e crítico na inicialização.

### Lazy com cache — `Provider<T>` (recomendado para valores opcionais)

```java
@Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "jdbc:h2:mem:test")
private Provider<String> databaseUrl;

@Value(param = "MAX_CONNECTIONS", type = ValueType.SANKHYA_PARAM, defaultValue = "10")
private Provider<Integer> maxConnections;
```

Valor resolvido apenas na primeira chamada de `.get()`, depois cacheado.

---

## Tipos Suportados

`String`, `Integer`/`int`, `Boolean`/`boolean`, `Long`/`long`, `Double`/`double`, `Float`/`float` — e `Provider<T>` para qualquer um deles.

---

## Exemplos Práticos

### Parâmetros Sankhya com grupo

```java
@Value(param = "TIMEOUT", group = "CONNECTION", type = ValueType.SANKHYA_PARAM, defaultValue = "30")
private Provider<Long> connectionTimeout;
```

### Feature flags

```java
@Value(param = "VALIDACAO_AVANCADA_ATIVA", type = ValueType.SANKHYA_PARAM, defaultValue = "false")
private Provider<Boolean> validacaoAvancadaAtiva;

@Transactional
public void processar(@Valid PedidoDTO pedido) {
    if (validacaoAvancadaAtiva.get()) {
        validadorAvancado.validar(pedido);
    }
}
```

### Configuração de banco

```java
@Component
public class DatabaseConfig {
    @Value(value = "DATABASE_URL", type = ValueType.ENV_VAR, defaultValue = "jdbc:h2:mem:test")
    private Provider<String> databaseUrl;

    @Value(param = "MAX_POOL_SIZE", type = ValueType.SANKHYA_PARAM, defaultValue = "20")
    private Provider<Integer> maxPoolSize;
}
```

---

## Boas Práticas

- Sempre forneça `defaultValue` — evita erros quando a propriedade não está definida
- Use `Provider<T>` (lazy) para valores opcionais ou feature flags
- Use eager para configurações críticas necessárias na inicialização
- Prefira tipos específicos (`Integer`, `Boolean`) em vez de `String`

## Antipadrões

- `@Value` em campos `final` — a injeção não funciona
- Instâncias criadas com `new` — só funciona em objetos gerenciados pelo SDK
- `defaultValue` com JSON complexo inline — prefira múltiplos valores simples

---

## Fonte

https://developer.sankhya.com.br/docs/inje%C3%A7%C3%A3o-de-valores-value
