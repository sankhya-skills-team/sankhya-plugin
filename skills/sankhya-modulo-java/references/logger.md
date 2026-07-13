# Logger — br.com.sankhya.customizacao.utils.Logger

## Localização

Classe estática compartilhada, disponível em todos os módulos:

```
shared/Java/src/br/com/sankhya/customizacao/utils/Logger.java
```

Incluída automaticamente em todo JAR gerado pelo `build.gradle`.

## Dependências de Setup

Antes de usar, o ambiente precisa ter:

1. **Tela adicional AD_LOG** importada via Construtor de Telas (arquivo em `shared/Telas Adicionais/`)
2. **Preferência LOGDEBUGATV** cadastrada no TSIPAR — valor `N` desativa (padrão: ativo)

Sem a tela AD_LOG, o INSERT falha silenciosamente — sem erro na aplicação.

## Configuração

```java
import br.com.sankhya.customizacao.utils.Logger;

// Uso estático — sem instância
Logger.info("Mensagem");
Logger.error("Mensagem", e);
```

Não usar `java.util.logging.Logger` nem `org.apache.log4j.Logger` em módulos Java.

---

## Níveis disponíveis

| Nível | Método | Quando usar |
|---|---|---|
| `INFO` | `Logger.info(msg)` | Rastreamento de fluxo, eventos de negócio relevantes, início/fim de operações |
| `ERROR` | `Logger.error(msg, e)` | Todo bloco `catch` com exceção real — sempre passar o objeto `e` |

---

## Exemplos ruins

### 1. Sem contexto
```java
// Ruim: o que falhou? qual registro?
Logger.error("Erro ao processar");
```

### 2. Exceção sem passar o objeto
```java
// Ruim: perde a stack trace
Logger.error("Erro: " + e.getMessage());
```

### 3. Dados sensíveis no log
```java
// Ruim: nunca logar senhas, tokens, CPFs
Logger.info("Login: " + usuario + " | Senha: " + senha);
```

### 4. Log dentro de loop sem critério
```java
// Ruim: pode gerar milhares de linhas
for (DynamicVO vo : lista) {
    Logger.info("Processando: " + vo.asBigDecimal("ID"));
}
```

---

## Exemplos bons

### 1. Mensagem com contexto
```java
Logger.info("Operacao executada | id=" + id + " | status=" + status);
```

### 2. Exceção com objeto completo
```java
try {
    processarOperacao(id);
} catch (NomeDemandaException e) {
    Logger.error("Falha ao processar | id=" + id, e);
    throw MGEModelException.prettyMsg(e.getMessage(), e);
}
```

### 3. Rastreamento de fluxo com resumo em lote
```java
Logger.info("Lote iniciado | total=" + lista.size());
int falhas = 0;
for (DynamicVO vo : lista) {
    try {
        processarItem(vo);
    } catch (Exception e) {
        Logger.error("Falha no item | id=" + vo.asBigDecimal("ID"), e);
        falhas++;
    }
}
Logger.info("Lote concluido | processados=" + (lista.size() - falhas) + " | falhas=" + falhas);
```

### 4. Rastreamento de fluxo
```java
Logger.info("Iniciando validacao | id=" + id);
nomeService.validar(vo);
Logger.info("Validacao concluida | id=" + id);
```

---

## Regras críticas

- **Todo `catch` com exceção real** deve ter `Logger.error(mensagem, e)` — nunca só `Logger.error(e.getMessage())`
- **Nunca engolir exceção em bloco vazio** — se logar, relançar ou converter
- **Nunca logar dados sensíveis** — senhas, tokens, CPF completo
- **`Logger.info()` no início de operações críticas** — facilita diagnóstico em produção
- **Logar resumo em loops**, não cada item individualmente
