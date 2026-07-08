# Parâmetros do Sistema — MGECoreParameter

API oficial Sankhya para leitura de parâmetros do TSIPAR (Parâmetros do Sistema).

```
Pacote: br.com.sankhya.modelcore.util.MGECoreParameter
JAR:    mgecore.jar (disponível no classpath do módulo Java)
```

---

## Quando usar

Sempre que precisar ler um parâmetro configurado em **Preferências → Parâmetros do Sistema** (TSIPAR).  
Não usar `JapeFactory.dao("Parametros").findOne(...)` — essa abordagem acessa a entidade diretamente
sem passar pela camada de cache e abstração da plataforma.

---

## Métodos estáticos principais

| Método | Tipo TSIPAR | Retorno |
|---|---|---|
| `MGECoreParameter.getParameter(String chave)` | Qualquer (auto-detecta por `TIPO`) | `Object` — cast conforme tipo |
| `MGECoreParameter.getParameterAsString(String chave)` | `T` (TEXTO) | `String` |
| `MGECoreParameter.getParameterAsInt(String chave)` | `I` (INTEIRO) | `int` |
| `MGECoreParameter.getParameterAsBoolean(String chave)` | `L` (LOGICO) | `boolean` |

Constantes de tipo disponíveis na própria classe:

```java
MGECoreParameter.TEXTO   // 'T'
MGECoreParameter.INTEIRO // 'I'
MGECoreParameter.FLOAT   // 'F'
MGECoreParameter.LOGICO  // 'L'
MGECoreParameter.DATA    // 'D'
MGECoreParameter.LISTA   // 'C'
```

---

## Padrão de uso com fallback para valor padrão

Parâmetros podem não estar cadastrados — sempre usar try-catch com fallback.

```java
import br.com.sankhya.modelcore.util.MGECoreParameter;
import java.math.BigDecimal;
import java.util.logging.Level;
import java.util.logging.Logger;

private static final Logger LOG = Logger.getLogger(MinhaClasse.class.getName());

// Parâmetro FLOAT (tipo F) → retorna BigDecimal
private BigDecimal buscarParamReal(String chave, BigDecimal valorDefault) {
    try {
        Object valor = MGECoreParameter.getParameter(chave);
        if (valor instanceof BigDecimal) return (BigDecimal) valor;
        if (valor instanceof Number) return new BigDecimal(valor.toString());
    } catch (Exception e) {
        LOG.log(Level.WARNING, "Parametro TSIPAR nao encontrado: " + chave + ". Usando default.", e);
    }
    return valorDefault;
}

// Parâmetro TEXTO (tipo T) → retorna String
private String buscarParamTexto(String chave, String valorDefault) {
    try {
        String valor = MGECoreParameter.getParameterAsString(chave);
        if (valor != null && !valor.trim().isEmpty()) return valor.trim();
    } catch (Exception e) {
        LOG.log(Level.WARNING, "Parametro TSIPAR nao encontrado: " + chave + ". Usando default.", e);
    }
    return valorDefault;
}
```

---

## Onde usar no projeto

Camada correta: **`repository/`** — leitura de parâmetros é acesso a dados.  
O `repository/` lê os parâmetros e monta um DTO que é passado para `service/` e `component/`.

```
repository/ → busca params via MGECoreParameter → monta DTO
service/    → recebe DTO, executa cálculo (sem acesso a banco)
component/  → orquestra repository + service
```

---

## Antipadrões

```java
// ERRADO: acesso direto à entidade — não usa cache, acopla ao nome interno
DynamicVO vo = JapeFactory.dao("Parametros").findOne("this.CHAVE = ?", new Object[]{"AD_PCTICMS"});
BigDecimal valor = BigDecimalUtil.getBigDecimal(vo.getProperty("REAL"));

// CORRETO
Object valor = MGECoreParameter.getParameter("AD_PCTICMS"); // BigDecimal para tipo F

// ERRADO: sem fallback — quebra se parâmetro não cadastrado
BigDecimal pct = (BigDecimal) MGECoreParameter.getParameter("AD_PCTICMS");

// CORRETO: com fallback
BigDecimal pct = buscarParamReal("AD_PCTICMS", new BigDecimal("19.0"));
```
