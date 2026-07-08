# Boas Práticas — Módulos Java Sankhya

## Tratamento de Erros

### Hierarquia de tratamento

```java
// 1. Erro de validação de negócio — mensagem exibida ao usuário
throw new MGEModelException("Não é possível realizar esta operação: motivo específico.");

// 1b. Erro de negócio no service — lançar exceção de domínio (nunca MGEModelException aqui)
throw NomeModuloException.statusInvalido("A", "finalizar");

// 1c. Na borda (actionbutton/, event/) — converter para MGEModelException
} catch (NomeModuloException e) {
    throw MGEModelException.prettyMsg(e.getMessage(), e);
}

// 2. Relançar exceção preservando stack trace (em helpers)
} catch (Exception e) {
    MGEModelException.throwMe(e);
}

// 3. Relançar com mensagem amigável (em botões de ação — suporta HTML)
} catch (Exception e) {
    throw MGEModelException.prettyMsg("Erro ao processar: <br>" + e.getMessage(), e);
}

// 4. No catch externo do botão de ação — logar e relançar
} catch (Exception e) {
    e.printStackTrace();  // log no servidor
    MGEModelException.throwMe(e);
}
```

### Nunca engolir exceção

```java
// RUIM
try {
    operacao();
} catch (Exception e) {
    // silêncio
}

// BOM
try {
    operacao();
} catch (Exception e) {
    Logger.error("Erro em operacao()", e);
    MGEModelException.throwMe(e);
}
```

---

## Logging

```java
import br.com.sankhya.utils.Logger;

// Uso estático — sem instância, sem declaração de campo
// Níveis corretos
Logger.debug("Detalhes de diagnóstico");          // apenas desenvolvimento
Logger.info("Operação iniciada para ID: " + id);  // eventos significativos
Logger.warn("Valor nulo, usando zero como fallback para campo PESO"); // situação anormal
Logger.error("Erro ao processar registro " + id, e); // sempre com exceção

// Em loops — logar resumo, não cada item
Logger.info("Processando lote de " + itens.size() + " itens");
```

---

## Verificação de Campos

```java
// CORRETO — verificar existência antes de acessar
if (vo.containsProperty("CAMPO_OPCIONAL")) {
    BigDecimal val = vo.asBigDecimal("CAMPO_OPCIONAL");
}

// ERRADO — nunca usar try-catch para verificar existência
try {
    BigDecimal val = vo.asBigDecimal("CAMPO_OPCIONAL"); // lança se não existir
} catch (Exception e) {
    // antipadrão
}

// Para campos BigDecimal — verificar nulo ou zero
if (!BigDecimalUtil.isNullOrZero(vo.asBigDecimal("CAMPO"))) {
    // processar
}
```

---

## JapeSession — Regras

```java
// CORRETO — sempre com finally
JapeSession.SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    // operações...
} finally {
    JapeSession.close(hnd); // seguro se hnd for null
}

// ERRADO — sem finally
hnd = JapeSession.open();
// operações...
JapeSession.close(hnd); // não executado se exceção for lançada

// ERRADO — usar dentro de evento (sessão já existe)
public void beforeInsert(PersistenceEvent pEvent) throws Exception {
    JapeSession.SessionHandle hnd = JapeSession.open(); // desnecessário e perigoso
    // ...
}
```

---

## Performance

### Nunca consultar dentro de loop

```java
// RUIM — N consultas ao banco
for (DynamicVO item : itens) {
    DynamicVO pedido = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA)
            .findByPK(item.asBigDecimal("NUNOTA")); // N queries
}

// BOM — consultar fora do loop quando possível
BigDecimal nuNota = itens.iterator().next().asBigDecimal("NUNOTA");
DynamicVO pedido = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);
for (DynamicVO item : itens) {
    // usar pedido já carregado
}

// BOM — acumular resultado no loop sem consulta adicional
BigDecimal total = BigDecimal.ZERO;
for (DynamicVO item : itens) {
    BigDecimal valor = item.asBigDecimal("VLRITEM");
    if (valor != null) total = total.add(valor);
}
```

### Evitar transações longas

```java
// Transações longas bloqueiam registros no banco
// Para processamento em lote: dividir em lotes menores ou usar JdbcWrapper
// Para operações independentes: usar JapeSession.open()/close() por unidade
```

---

## Helpers — Design Correto

```java
// CORRETO — construtor privado, métodos estáticos
public class MeuHelper {
    private MeuHelper() {
        throw new UnsupportedOperationException("Não é permitido instanciar esta classe");
    }
    public static BigDecimal calcular(DynamicVO vo) throws Exception { ... }
}

// ERRADO — helper instanciável
public class MeuHelper {
    public BigDecimal calcular(DynamicVO vo) throws Exception { ... } // método de instância
}

// ERRADO — state em helper (não é thread-safe)
public class MeuHelper {
    private static BigDecimal ultimoValor; // compartilhado entre threads
}
```

---

## Enums — Boas Práticas

```java
// CORRETO — enum no lugar de String mágica
if (StatusAmostra.APROVADO.getCodigo().equals(vo.asString("STATUS"))) {
    // processar aprovado
}

// ERRADO — String mágica
if ("A".equals(vo.asString("STATUS"))) { // "A" o que significa?
    // processar aprovado
}

// CORRETO — null-safe ao comparar
String statusAtual = vo.asString("STATUS");
if (StatusAmostra.APROVADO.getCodigo().equals(statusAtual)) { // equals no enum, não no null
    // seguro
}

// ERRADO — NullPointerException se statusAtual for null
if (statusAtual.equals(StatusAmostra.APROVADO.getCodigo())) {
    // risco de NPE
}
```

---

## Comentário Javadoc de Configuração

Toda classe que precisa de registro manual no Sankhya deve ter o comentário padronizado:

```java
/**
 * Breve descrição do que a classe faz.
 *
 * Regras de negócio: descrever as validações e transformações aplicadas.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA
 *   Tipo        : Before Insert, Before Update
 *   Classe Java : br.com.empresa.dctm.modulo.event.NomeEvento
 */
public class NomeEvento implements EventoProgramavelJava { ... }
```

Isso facilita re-registro após atualizações de servidor.

---

## Transações Granulares — execWithTX e execWithFakeTX

Use quando precisar de múltiplas transações independentes dentro do mesmo fluxo, ou executar operações sem persistir (dry-run).

### execWithTX — commit independente por bloco

```java
JapeSession.SessionHandle hnd = null;
try {
    hnd = JapeSession.open();

    // Bloco 1 — commit independente
    hnd.execWithTX(() -> {
        JapeFactory.dao("AD_NOMETABELA")
            .prepareToUpdateByPK(id)
            .set("STATUS", "P")
            .update();
    });

    // Bloco 2 — outro commit independente
    hnd.execWithTX(() -> {
        JapeFactory.dao("AD_LOG").create()
            .set("CODREGISTRO", id)
            .set("ACAO", "PROCESSADO")
            .save();
    });
} finally {
    JapeSession.close(hnd);
}
```

> Se o lambda lançar exceção, `execWithTX` faz rollback automático e repropaga. Não precisa capturar e fazer rollback manualmente.

### execWithFakeTX — dry-run sem persistir

Executa operações de banco sem commit — útil para calcular ou validar sem efeito colateral.

```java
AtomicReference<BigDecimal> resultado = new AtomicReference<>();
hnd.execWithFakeTX(() -> {
    // tudo aqui é revertido ao final — com ou sem exceção
    BigDecimal calc = calcularSemPersistir();
    resultado.set(calc);
});
// resultado.get() disponível, nada foi persistido
```

---

## Performance — N+1 Queries

Nunca buscar registros relacionados dentro de loop. Use NativeSql com JOIN quando precisar de dados de múltiplas entidades.

```java
// RUIM — N+1: 1 query para listar + N queries para buscar detalhe
Collection<DynamicVO> registros = DwfUtils.findEntitysAsVO("AD_ORDEM", "this.STATUS = ?", new Object[]{"P"});
for (DynamicVO vo : registros) {
    DynamicVO parceiro = JapeFactory.dao(DynamicEntityNames.PARCEIRO)
        .findByPK(vo.asBigDecimal("CODPARC")); // query por registro!
}

// BOM — 1 query com JOIN via NativeSql
Collection<Map<String, Object>> linhas = NativeSql.getResultSetAsCollection(
    "o.IDORDEM, o.STATUS, p.NOMEPARC",
    "AD_ORDEM o JOIN TGFPAR p ON p.CODPARC = o.CODPARC",
    "o.STATUS = ?",
    new Object[]{"P"},
    jdbc
);
```

---

## Operações em Lote com Falhas Parciais

Ao processar múltiplos registros — especialmente em jobs — coleta sucessos e falhas separados. Não aborta tudo na primeira falha.

```java
List<BigDecimal> sucessos = new ArrayList<>();
List<String> falhas = new ArrayList<>();

for (DynamicVO registro : registros) {
    BigDecimal id = registro.asBigDecimal("ID");
    try {
        nomeComponent.processar(id);
        sucessos.add(id);
        Logger.info("Registro processado. ID=" + id);
    } catch (Exception e) {
        Logger.error("Falha ao processar ID=" + id + ". Motivo: " + e.getMessage(), e);
        falhas.add("ID " + id + ": " + e.getMessage());
    }
}

if (sucessos.isEmpty()) {
    throw new MGEModelException(
        "Nenhum registro processado. Falhas: " + String.join(" | ", falhas));
}

if (!falhas.isEmpty()) {
    MessageUtils.showInfo(sucessos.size() + " registro(s) processado(s). Falhas: "
        + String.join("\n", falhas));
} else {
    MessageUtils.showInfo(sucessos.size() + " registro(s) processado(s) com sucesso.");
}
```

---

## EntityFacade — Operações Avançadas

Para operações que `JapeFactory` não cobre diretamente.

### Criar entidade com defaults (equivalente a "abrir novo registro na tela")

```java
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.vo.EntityVO;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;

EntityFacade dwf = EntityFacadeFactory.getDWFFacade();

EntityVO evo = dwf.getDefaultValueObjectInstance("RateioRecDesp");
DynamicVO vo = (DynamicVO) evo;

vo.setProperty("NUFIN",      nuFin);
vo.setProperty("PERCRATEIO", percentual);
vo.setProperty("CODCENCUS",  codCenCus);
vo.setProperty("ORIGEM",     "F");

dwf.createEntity("RateioRecDesp", evo);
```

### Deletar múltiplos registros por critério

```java
import br.com.sankhya.jape.util.FinderWrapper;

FinderWrapper fw = new FinderWrapper("RateioRecDesp", "NUFIN = ?", new Object[]{ nuFin });
EntityFacadeFactory.getDWFFacade().removeByCriteria(fw);
```

> `removeByCriteria` é útil para deletar lote sem iterar. Requer `JapeSession` aberta.

### Buscar por PK via EntityFacade

```java
DynamicVO fin = (DynamicVO) EntityFacadeFactory.getDWFFacade()
    .findEntityByPrimaryKeyAsVO("Financeiro", nuFin);
```

---

## Padrão Objeto Nulo com Defaults

Quando uma query pode não retornar resultado, retorne objeto com valores padrão em vez de `null` — evita `NullPointerException` no chamador.

```java
public class TaxasDto {
    public final String incideTaxa;
    public final BigDecimal percentual;

    public TaxasDto(String incideTaxa, BigDecimal percentual) {
        this.incideTaxa = incideTaxa;
        this.percentual = percentual;
    }

    public static TaxasDto defaults() {
        return new TaxasDto("N", BigDecimal.ZERO);
    }
}

// No repository:
Map<String, Object> dados = NativeSql.getColumnsAsMap(
    "INCIDETAXA, PERCENTUAL", "AD_TAXAS", "CODTAXA = ?", codTaxa, jdbc
);
if (dados.isEmpty()) return TaxasDto.defaults(); // nunca retorna null
return new TaxasDto(
    MapUtils.getMapValueAsString(dados, "INCIDETAXA"),
    MapUtils.getMapValueAsBigDecimal(dados, "PERCENTUAL")
);
```

---

## Validação de Máquina de Estados

Para operações que dependem do status atual, valide a transição antes de executar.

```java
// No service/:
public void validarTransicaoParaProcessamento(DynamicVO vo) throws NomeDemandaException {
    String statusAtual = vo.asString("STATUS");
    if (!StatusOrdem.PENDENTE.getCodigo().equals(statusAtual)) {
        throw NomeDemandaException.transicaoInvalida(
            vo.asBigDecimal("ID"), statusAtual, StatusOrdem.PENDENTE.getCodigo(), "processar");
    }
}

// Na NomeDemandaException — fábrica de mensagem padronizada:
public static NomeDemandaException transicaoInvalida(
        BigDecimal id, String statusAtual, String statusEsperado, String acao) {
    return new NomeDemandaException(String.format(
        "[MOD_0010] Transição inválida para '%s'. ID=%s, status atual=%s, esperado=%s",
        acao, id, statusAtual == null ? "<null>" : statusAtual, statusEsperado));
}
```

---

## Null Safety com DynamicVO

`findByPK` retorna `null` se não encontrar — sempre verificar. `asBigDecimal`/`asString` retornam `null` se o campo for nulo no banco.

```java
// Sempre verificar findByPK
DynamicVO vo = JapeFactory.dao("AD_NOMETABELA").findByPK(id);
if (vo == null) throw NomeDemandaException.naoEncontrado("NomeDemanda", id);

// BigDecimal com default explícito
BigDecimal valor = vo.asBigDecimal("VALOR");
if (valor == null) valor = BigDecimal.ZERO;
// ou:
BigDecimal valor2 = BigDecimalUtil.getValueOrZero(vo.asBigDecimal("VALOR"));

// String — sempre verificar antes de comparar
String status = vo.asString("STATUS");
if (status == null || status.trim().isEmpty())
    throw NomeDemandaException.statusInvalido(null, "processar");
```

---

## Testes

APIs de persistência do módulo (`JapeFactory`, `NativeSql`, `JapeSession`) dependem do container Sankhya em execução — não são mockáveis de forma simples.

**O que pode ser testado sem servidor:**
- Lógica pura em `service/` que não depende de `JapeFactory` ou banco
- Cálculos, validações de regra de negócio, transformações em métodos estáticos

**O que requer servidor:**
- Qualquer operação com `JapeFactory.dao()`, `NativeSql`, `JapeSession`
- `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava` — dependem do container

**Estratégia:** isole regras de negócio puras em `service/` sem dependências de infraestrutura — esses métodos podem ser testados com JUnit. O restante valide com testes manuais em ambiente com o JAR importado.

---

## Checklist de Code Review

- [ ] helper/ transversal com construtor privado e métodos estáticos — service/ e repository/ são instanciáveis
- [ ] `JapeSession.open()` com `finally { JapeSession.close(hnd); }`
- [ ] `MGEModelException` para erros de negócio e relançamento
- [ ] `vo.containsProperty()` antes de campos opcionais
- [ ] `BigDecimalUtil.isNullOrZero()` antes de operar com decimais
- [ ] Sem consulta dentro de loop
- [ ] `Logger.error(mensagem, e)` em todo bloco `catch` com exceção real — nunca só `e.getMessage()`
- [ ] Enum no lugar de strings mágicas
- [ ] Javadoc de configuração em eventos e botões de ação
- [ ] Sem lógica de negócio em eventos/botões — delegar para service/ e repository/
- [ ] Nenhuma referência a frontend, sankhya-js ou Design System
