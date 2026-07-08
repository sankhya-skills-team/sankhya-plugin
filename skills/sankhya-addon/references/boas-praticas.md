# Guia de Boas Práticas — Desenvolvimento de Add-ons Sankhya

> Este guia é específico para **Add-on Studio 2.0 clássico**. As APIs aqui documentadas (`JapeFactory`, `DynamicVO`, `JapeSession`, `NativeSql`) são as disponíveis nesse contexto. Não use Spring, JPA, Bean Validation ou `@Inject` — essas APIs pertencem ao SDK beta e não funcionam no clássico.

---

## 1. Modelagem de Dados

- Use prefixo único em todas as tabelas e campos customizados (ex: `MKT_`)
- **Nunca use `AD_`** — reservado internamente pelo Sankhya
- Para campos adicionais em tabelas nativas, use `<nativeTable>` (não criar tabela separada)
- Prefixe também os campos de `<nativeTable>`:

```xml
<!-- BOM -->
<nativeTable name="TGFCAB">
    <field name="MKT_CAMPANHAVINCULADA" type="NUMBER(10)" />
</nativeTable>

<!-- RUIM: tabela separada para campos simples -->
<table name="MKT_CAB_EXTRA">
    <field name="NUNOTA" />
</table>
```

- Evite defaults em tabelas nativas — causam falhas no processo de instalação
- Normalize adequadamente (3ª Forma Normal geralmente suficiente)
- Tipos recomendados: `BigDecimal` para monetário e PKs, `Timestamp` para datas

---

## 2. Gestão de Estado em Services — CRÍTICO

**`@Service` no Add-on Studio 2.0 clássico é um singleton EJB. Variáveis de instância mutáveis são compartilhadas entre threads e causam race conditions.**

```java
// PÉSSIMO — variável de instância mutável em singleton
@Service(serviceName = "com.empresa.PedidoServiceSP")
public class PedidoService {
    private BigDecimal ultimoCodigo; // compartilhado entre threads!
    private List<String> erros;      // compartilhado entre threads!
}

// BOM — apenas constantes e colaboradores imutáveis como campos
@Service(serviceName = "com.empresa.PedidoServiceSP")
public class PedidoService {
    private static final Logger logger = Logger.getLogger(PedidoService.class);

    // Colaboradores instanciados como campo são OK se forem stateless
    private final PedidoAplicacaoService aplicacao = new PedidoAplicacaoService();

    public void processar(ServiceContext ctx) throws Exception {
        // Variáveis locais — thread-safe
        BigDecimal codRegistro = ctx.getJsonRequestBody()
            .getAsJsonObject("dto").get("CODREGISTRO").getAsBigDecimal();
        List<String> errosLocais = new ArrayList<>(); // local, não compartilhado
    }
}
```

> Não existe `@Inject` no Add-on Studio 2.0 clássico. Colaboradores são instanciados diretamente com `new`. Ver seção 12.

---

## 3. Nomenclatura e Isolamento

### Nome de service com namespace completo

```java
// BOM: evita conflitos entre add-ons
@Service(serviceName = "com.minhaempresa.financeiro.CobrancaServiceSP")

// RUIM: genérico, pode conflitar com outro add-on
@Service(serviceName = "CobrancaServiceSP")
```

### Isolamento de ClassLoader

Add-ons rodam isolados do sistema. Cada add-on tem seu próprio ClassLoader. **Acesse apenas APIs públicas do Sankhya:**

```java
// RUIM — não funciona (classe de outro add-on ou do sistema)
import br.com.empresa.custom.MinhaClassePersonalizada;

// BOM
import br.com.sankhya.jape.EntityFacade;
import com.meuaddon.service.MinhaClasseDoAddon;
```

---

## 4. Logging

### Configuração

```java
import org.apache.log4j.Logger;

public class MeuServico {
    private static final Logger logger = Logger.getLogger(MeuServico.class);
}
```

### Níveis de Log

| Nível | Uso |
|---|---|
| `TRACE`/`DEBUG` | Diagnóstico detalhado — apenas desenvolvimento |
| `INFO` | Eventos significativos — confirmações, ciclo de vida |
| `WARN` | Situações anormais — fallbacks, valores padrão |
| `ERROR` | Erros bloqueadores — exceções, falhas críticas |

### Antipadrões de Logging — CRÍTICO

**Concatenação é executada ANTES da verificação do nível de log:**

```java
// PÉSSIMO: toString() executado mesmo com DEBUG desabilitado
logger.debug("Processando: " + objetoComplexo.toString());

// PÉSSIMO: em loop, gera dezenas de MB de lixo
for (DynamicVO vo : listaGrande) {
    logger.debug("Processando: " + vo.asString("DESCRICAO"));
}

// PÉSSIMO: engole a exceção
try {
    operacao();
} catch (Exception e) { }

// PÉSSIMO: sem stack trace
logger.error("Erro: " + e.getMessage());
```

**Forma correta:**

```java
// Verificar nível antes de concatenações custosas
if (logger.isDebugEnabled()) {
    logger.debug("Processando: " + vo.asString("DESCRICAO"));
}

// Sempre incluir exceção completa
logger.error("Erro ao processar ID=" + codRegistro, e);

// Para coleções, logar tamanho
logger.info("Processando " + lista.size() + " registros.");
```

### Boas práticas de logging

- Use níveis apropriados (não abuse ERROR)
- Inclua contexto: IDs, valores relevantes
- Nunca logue dados sensíveis (senhas, tokens, CPF completo)
- Mensagens claras: `"Registro 12345 não encontrado"` (não genérico)
- Sempre passe a exceção como segundo parâmetro: `logger.error("msg", exception)`

---

## 5. Transações no Add-on Studio 2.0 Clássico

No clássico **não existe** `@Transactional` do Spring/SDK. O controle transacional é feito via:

### Opção 1 — `EJBTransactionType` na anotação `@Service`

```java
// Operações de escrita — transação gerenciada pelo container
@Service(serviceName = "com.empresa.GravarServiceSP",
         transactionType = EJBTransactionType.Required)
public class GravarService {
    public void gravar(ServiceContext ctx) throws Exception {
        // toda a execução do método participa da mesma transação
    }
}

// Consultas — sem transação para melhor performance
@Service(serviceName = "com.empresa.ConsultarServiceSP",
         transactionType = EJBTransactionType.NotSupported)
public class ConsultarService {
    public void consultar(ServiceContext ctx) throws Exception { ... }
}
```

### Opção 2 — `hnd.execWithTX()` para controle granular

Use quando precisar de múltiplas transações independentes dentro do mesmo método:

```java
JapeSession.SessionHandle hnd = JapeSession.open();
try {
    // Bloco 1 — commit independente
    hnd.execWithTX(() -> {
        JapeFactory.dao("MinhaEntidade")
            .prepareToUpdateByPK(codRegistro)
            .set("STATUS", "P")
            .update();
    });

    // Bloco 2 — outro commit independente
    hnd.execWithTX(() -> {
        JapeFactory.dao("MinhaEntidadeLog").create()
            .set("CODREGISTRO", codRegistro)
            .set("ACAO", "PROCESSADO")
            .save();
    });
} finally {
    JapeSession.close(hnd);
}
```

> **Comportamento com exceção:** se o lambda lançar uma exceção, o `execWithTX` executa **rollback automático** da transação e repropaga a exceção. Não é necessário capturar e fazer rollback manualmente.

### Opção 3 — `hnd.execWithFakeTX()` para dry-run

Executa operações de banco sem commit — útil para calcular sem persistir. Se o lambda lançar exceção, o rollback também é automático:

```java
AtomicReference<BigDecimal> resultado = new AtomicReference<>();
hnd.execWithFakeTX(() -> {
    // tudo aqui é revertido ao final — com ou sem exceção
    BigDecimal calc = calcularSemPersistir();
    resultado.set(calc);
});
// resultado.get() disponível, nada foi persistido
```

### Regras gerais

- Evite transações longas — causam locks e deadlocks
- Valide os dados **antes** de abrir a transação — não desperdice locks com validações
- Use `EJBTransactionType.NotSupported` quando usar `execWithTX`/`execWithFakeTX` manualmente

---

## 6. Performance

### Evite N+1 queries — use NativeSql com JOIN

```java
// RUIM: N+1 queries — 1 query para listar + N queries para buscar detalhes
Collection<DynamicVO> registros = JapeFactory.dao("MinhaEntidade").find("ATIVO = 'S'");
for (DynamicVO vo : registros) {
    DynamicVO detalhe = JapeFactory.dao("MinhaEntidadeDetalhe")
        .findByPK(vo.asBigDecimal("CODREGISTRO")); // query por registro!
}

// BOM: uma única query com JOIN via NativeSql
try (NativeSql ns = new NativeSql(jdbc)) {
    ns.appendSql(
        "SELECT R.CODREGISTRO, R.DESCRICAO, D.CAMPO_DETALHE " +
        "FROM MINHA_ENTIDADE R " +
        "JOIN MINHA_ENTIDADE_DETALHE D ON R.CODREGISTRO = D.CODREGISTRO " +
        "WHERE R.ATIVO = 'S'"
    );
    try (ResultSet rs = ns.executeQuery()) {
        while (rs.next()) { ... }
    }
}
```

### Processamento em lote — coletar e persistir fora do loop de leitura

```java
// RUIM: query dentro de loop de persistência
for (BigDecimal id : ids) {
    DynamicVO vo = JapeFactory.dao("MinhaEntidade").findByPK(id); // query por iteração
    JapeFactory.dao("MinhaEntidade").prepareToUpdateByPK(id).set("STATUS", "P").update();
}

// BOM: buscar tudo de uma vez com NativeSql, persistir em lote separado
List<BigDecimal> paraAtualizar = buscarIdsParaProcessar(jdbc);
for (BigDecimal id : paraAtualizar) {
    JapeFactory.dao("MinhaEntidade").prepareToUpdateByPK(id).set("STATUS", "P").update();
}
```

### Cache de parâmetros

```java
// Em um @Service (singleton), cache de parâmetros é seguro se imutável após carga
private final Map<String, String> cacheParametros = new ConcurrentHashMap<>();

public String getParametro(String chave) {
    return cacheParametros.computeIfAbsent(chave, k -> buscarParametroDoBanco(k));
}
```

---

## 7. Validação de Entrada

No Add-on Studio 2.0 clássico **não existe Bean Validation** (`@NotNull`, `@Positive`, etc.). Validação é feita manualmente no `@Service` ou na `AplicacaoService`:

```java
// Validação manual no início do método — antes de abrir transação
private void validarDto(JsonObject dto) throws MGEModelException {
    if (!dto.has("CODPARC") || dto.get("CODPARC").isJsonNull()) {
        throw new MGEModelException("Código do parceiro é obrigatório.");
    }
    BigDecimal codParc = dto.get("CODPARC").getAsBigDecimal();
    if (codParc.compareTo(BigDecimal.ZERO) <= 0) {
        throw new MGEModelException("Código do parceiro inválido: " + codParc);
    }
    if (!dto.has("ITENS") || !dto.get("ITENS").isJsonArray()
            || dto.getAsJsonArray("ITENS").size() == 0) {
        throw new MGEModelException("O pedido deve conter ao menos um item.");
    }
}
```

### Mascaramento de dados sensíveis

```java
public String getCpfMascarado(String cpf) {
    if (cpf == null || cpf.length() < 11) return "***";
    return cpf.substring(0, 3) + ".***.**" + cpf.substring(9);
}
```

---

## 8. Null Safety com DynamicVO

No Add-on Studio 2.0 clássico **não existe `Optional`** do Spring Data. Null safety é feita explicitamente:

```java
// findByPK retorna null se não encontrar — sempre verificar
DynamicVO vo = JapeFactory.dao("MinhaEntidade").findByPK(codRegistro);
if (vo == null) {
    throw new MGEModelException("Registro não encontrado. ID=" + codRegistro);
}

// asBigDecimal/asString retornam null se o campo for nulo no banco
BigDecimal valor = vo.asBigDecimal("VALOR");
if (valor == null) {
    valor = BigDecimal.ZERO; // default explícito
}

// Ou use BigDecimalUtil para null-safe
BigDecimal valor2 = BigDecimalUtil.getValueOrZero(vo.asBigDecimal("VALOR"));

// Para String, sempre verificar antes de usar
String status = vo.asString("STATUS");
if (status == null || status.trim().isEmpty()) {
    throw new MGEModelException("Status não preenchido para ID=" + codRegistro);
}
```

---

## 9. Versionamento de dbscripts

Use convenção incremental:

```
dbscripts/
  V1__criar_tabelas_iniciais.xml
  V2__adicionar_campo_observacao.xml
  V3__criar_indice_performance.xml
  V4__corrigir_tipo_campo.xml
```

### AppKey e Contexto

O contexto de add-on é único por `appkey`. Alterar `appkey` sem mudar o contexto causa erro na instalação — mantenha ambos consistentes.

---

## 10. Qualidade de Código

- Métodos com no máximo ~50 linhas
- Classes com no máximo ~500 linhas
- Code review antes de merge
- Evite código duplicado e complexidade ciclomática alta
- Recursos externos: sempre use try-with-resources

```java
try (BufferedReader reader = new BufferedReader(new FileReader(caminho))) {
    // reader fechado automaticamente
} catch (IOException e) {
    logger.error("Erro ao processar: " + caminho, e);
    throw new MGEModelException("Erro ao processar arquivo", e);
}
```

## Fonte

https://developer.sankhya.com.br/docs/guia-de-boas-praticas

---

## 11. JapeWrapper — Operações CRUD Completas

`JapeWrapper` é a API principal para persistência no Add-on Studio 2.0. Obtido via `JapeFactory.dao("NomeDaEntidade")`.

### INSERT

```java
JapeWrapper dao = JapeFactory.dao("MinhaEntidade");

DynamicVO vo = dao.create()
    .set("REFERENCIA",   referencia)   // Timestamp
    .set("TIPREGISTRO",  "N")          // String
    .set("STATUS",       "P")
    .set("NUMCONTRATO",  numContrato)  // BigDecimal
    .set("CODEMP",       codEmp)
    .set("CODPARC",      codParc)
    .save();

// Ler o PK gerado após o save
BigDecimal codRegistro = vo.asBigDecimal("CODREGISTRO");
```

### UPDATE por PK (sem buscar o VO antes)

```java
// Atualiza apenas os campos informados — não toca nos demais
JapeFactory.dao("MinhaEntidade")
    .prepareToUpdateByPK(codRegistro)
    .set("STATUS", "A")
    .set("NUNOTA", nuNota)
    .update();
```

### UPDATE a partir de um VO existente

```java
DynamicVO vo = dao.findByPK(codRegistro);
vo.setProperty("STATUS", "C");
dao.prepareToUpdate(vo).update();
```

### SELECT por PK

```java
DynamicVO vo = JapeFactory.dao("MinhaEntidade").findByPK(codRegistro);
if (vo == null) {
    throw new MGEModelException("Registro não encontrado: " + codRegistro);
}
String status      = vo.asString("STATUS");
BigDecimal codParc = vo.asBigDecimal("CODPARC");
Timestamp referencia = vo.asTimestamp("REFERENCIA");
```

### SELECT por PK com múltiplas chaves

```java
// Entidade com PK composta (CODEMP + CODFUNC)
DynamicVO funcionario = JapeFactory.dao(DynamicEntityNames.FUNCIONARIO)
    .findByPK(codEmp, codFunc);
```

### SELECT com filtro WHERE

```java
// Retorna Collection<DynamicVO>
Collection<DynamicVO> itens = JapeFactory.dao("MinhaEntidade")
    .find("NOT EXISTS (SELECT 1 FROM OUTRA_TAB WHERE CAMPO = TAB.CAMPO)");
```

### Leitura de campos do DynamicVO

```java
DynamicVO vo = dao.findByPK(pk);
BigDecimal valor    = vo.asBigDecimal("VLREVENTO");
String     status   = vo.asString("STATUS");
Timestamp  referencia = vo.asTimestamp("REFERENCIA");
char[]     obs      = (char[]) vo.getProperty("OBSERVACAO"); // campos CLOB
```

### Escrita de campo CLOB (char[])

```java
dao.create()
    .set("OBSERVACAO", texto != null ? texto.toCharArray() : null)
    .save();
```

### find com parâmetro posicional

Alternativa ao `find(whereString)` quando há um parâmetro simples:

```java
// Com ? posicional — mais seguro que concatenação
Collection<DynamicVO> financeiros = JapeFactory.dao(DynamicEntityNames.FINANCEIRO)
    .find("NUNOTA = ?", nuNota);
```

---

## 12. Composição de Dependências — instanciação com `new`

No Add-on Studio 2.0 clássico não existe injeção de dependências automática. Colaboradores são instanciados diretamente com `new`:

```java
@Service(serviceName = "com.empresa.MeuServiceSP")
public class MeuService {
    // Instanciação direta como campo — stateless, thread-safe
    private final MeuAplicacaoService aplicacao = new MeuAplicacaoService();
}

// AplicacaoService instancia seus próprios colaboradores
public class MeuAplicacaoService {
    private final MeuRepository repository = new MeuRepository();
    private final OutroRepository outroRepo = new OutroRepository();
}
```

> Não use `ApplicationFactory` ou qualquer padrão de fábrica centralizada — viola a separação de camadas e dificulta a leitura. Cada classe instancia seus próprios colaboradores diretos.

---

## 13. Rastreabilidade com MDC (Mapped Diagnostic Context)

Para correlacionar logs de uma mesma operação (especialmente em processamentos em lote), use MDC:

```java
import org.apache.log4j.MDC;

// No início da operação — adiciona contexto a todos os logs subsequentes
MDC.put("traceId", UUID.randomUUID().toString().substring(0, 8));
MDC.put("codRegistro", codRegistro.toPlainString());

try {
    logger.info("Iniciando processamento");
    // ... lógica ...
    logger.info("Processamento concluído");
} finally {
    // Sempre limpar — o MDC é thread-local mas pode vazar entre requisições
    MDC.remove("traceId");
    MDC.remove("codRegistro");
}
```

Configure o `log4j.properties` para incluir o MDC no padrão de log:

```properties
log4j.appender.FILE.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%X{traceId}] [%X{codRegistro}] %-5p %c - %m%n
```

---

## 14. Operações em Lote com Falhas Parciais

Quando uma operação processa múltiplos registros, o padrão é coletar sucessos e falhas separadamente — não abortar tudo na primeira falha:

```java
List<BigDecimal> sucessos = new ArrayList<>();
List<String>     falhas   = new ArrayList<>();

for (BigDecimal codRegistro : idList) {
    try {
        service.processar(codRegistro);
        JapeFactory.dao("MinhaEntidade")
            .prepareToUpdateByPK(codRegistro)
            .set("STATUS", "P")
            .update();
        sucessos.add(codRegistro);
        logger.info("Registro processado com sucesso. ID=" + codRegistro);
    } catch (Exception e) {
        logger.error("Falha ao processar ID=" + codRegistro + ". Motivo: " + e.getMessage(), e);
        falhas.add("ID " + codRegistro + ": " + e.getMessage());
    }
}

// Se nenhum teve sucesso, lança exceção
if (sucessos.isEmpty()) {
    throw new MGEModelException(
        "Nenhum registro processado. Falhas: " + String.join(" | ", falhas));
}

// Resposta com sucessos e falhas parciais
JsonObject response = new JsonObject();
response.addProperty("mensagem", sucessos.size() + " registro(s) processado(s) com sucesso.");
if (!falhas.isEmpty()) {
    response.addProperty("falhas", String.join("\n", falhas));
}
ctx.setJsonResponse(response);
```

> O frontend pode verificar `resp.responseBody.falhas` para exibir avisos parciais sem tratar como erro total.

---

## 15. SPBean (Add-on Studio 1.0) vs. `@Service` (Add-on Studio 2.0)

| Característica | SPBean (1.0) | `@Service` (2.0) |
|---|---|---|
| Registro | Anotações XDoclet `@ejb.bean` | Anotação `@Service(serviceName=...)` |
| Transação | `@ejb.transaction type="Required"` | `transactionType = EJBTransactionType.Required` |
| Padrão interno | Idêntico — `ServiceContext`, `JapeSession` | Idêntico — `ServiceContext`, `JapeSession` |
| Quando usar | Projetos legados (Add-on Studio 1.0) | Projetos novos (Add-on Studio 2.0) |

O padrão interno de ambos é o mesmo — a diferença é apenas na forma de registro. Ver `references/service.md` para exemplos completos de ambos.

---

## 16. Encoding — cp1252 vs UTF-8

Projetos Add-on Studio compilados no Windows frequentemente usam **cp1252 (Windows-1252)** como encoding padrão. Isso causa caracteres corrompidos (`?` no lugar de acentos) em strings hardcoded no código Java.

### Sintomas

```java
// No código fonte (cp1252):
throw new MGEModelException("Não é possível excluir");

// No log/tela (se o servidor espera UTF-8):
// "N?o ? poss?vel excluir"
```

### Solução 1 — Configurar encoding no build

No `build.gradle`:

```groovy
compileJava.options.encoding = 'UTF-8'
```

No `gradle.properties`:

```properties
org.gradle.jvmargs=-Dfile.encoding=UTF-8
```

### Solução 2 — Evitar acentos em strings de código

Para mensagens de erro e log, prefira strings sem acentos ou use constantes:

```java
// Sem acento — funciona em qualquer encoding
throw new MGEModelException("Registro nao encontrado. ID=" + codRegistro);

// Com acento — só funciona se o encoding estiver configurado corretamente
throw new MGEModelException("Registro não encontrado. ID=" + codRegistro);
```

### Solução 3 — Strings com escape Unicode

```java
// Funciona independente do encoding do arquivo fonte
throw new MGEModelException("Não é possível excluir este registro.");
```

### Arquivos SQL externos

Arquivos `.sql` carregados via `NativeSql.loadSql()` devem ser salvos em **UTF-8**. O `lerRecurso()` já usa `StandardCharsets.UTF_8` — garanta que o editor salve o arquivo nesse encoding.

---

## 17. EntityFacade — Operações Avançadas

Para operações que o `JapeWrapper` não cobre diretamente, use `EntityFacade` via `EntityFacadeFactory.getDWFFacade()`:

### Criar entidade com defaults via EntityFacade

```java
EntityFacade dwf = EntityFacadeFactory.getDWFFacade();

// Instancia VO com todos os defaults da entidade (equivalente a abrir novo registro na tela)
EntityVO evo = dwf.getDefaultValueObjectInstance("RateioRecDesp");
DynamicVO vo = (DynamicVO) evo;

vo.setProperty("NUFIN",      nuFin);
vo.setProperty("PERCRATEIO", percentual);
vo.setProperty("CODCENCUS",  codCenCus);
vo.setProperty("ORIGEM",     "F");
vo.setProperty("DIGITADO",   "S");

dwf.createEntity("RateioRecDesp", evo); // persiste via EntityFacade
```

### Buscar entidade por PK via EntityFacade

```java
DynamicVO fin = (DynamicVO) EntityFacadeFactory.getDWFFacade()
    .findEntityByPrimaryKeyAsVO("Financeiro", nuFin);
BigDecimal vlrDesdob = fin.asBigDecimal("VLRDESDOB");
```

### Deletar registros por critério via EntityFacade

```java
import br.com.sankhya.jape.util.FinderWrapper;

// Remove todos os rateios do título financeiro
FinderWrapper fw = new FinderWrapper("RateioRecDesp", "NUFIN = ?", new Object[]{ nuFin });
EntityFacadeFactory.getDWFFacade().removeByCriteria(fw);
```

> `removeByCriteria` é útil quando você precisa deletar múltiplos registros por critério sem iterar. Requer `JapeSession` aberta.

---

## 18. BigDecimalUtil — Null-safe para BigDecimal

```java
import com.sankhya.util.BigDecimalUtil;

// Retorna BigDecimal.ZERO se o valor for null
BigDecimal valor = BigDecimalUtil.getValueOrZero(vo.asBigDecimal("VLREVENTO"));

// Equivalente manual (quando BigDecimalUtil não estiver disponível)
BigDecimal valor2 = vo.asBigDecimal("VLREVENTO") != null
    ? vo.asBigDecimal("VLREVENTO") : BigDecimal.ZERO;
```

---

## 19. Desserializar JsonArray do payload

Quando o frontend envia um array no DTO:

```java
JsonObject dto = ctx.getJsonRequestBody().getAsJsonObject("dto");

// Validar que é array
if (!dto.has("CODREGISTRO") || !dto.get("CODREGISTRO").isJsonArray()) {
    throw new MGEModelException("Campo 'CODREGISTRO' deve ser um array");
}

// Desserializar para List<BigDecimal>
JsonArray arr = dto.getAsJsonArray("CODREGISTRO");
List<BigDecimal> idList = new ArrayList<>(arr.size());
for (JsonElement el : arr) {
    if (el.isJsonPrimitive() && el.getAsJsonPrimitive().isNumber()) {
        idList.add(el.getAsBigDecimal());
    } else {
        idList.add(new BigDecimal(el.getAsString()));
    }
}

// Ler booleano
boolean agrupar = dto.get("AGRUPAR").getAsBoolean();
```

---

## 20. DynamicEntityNames — Referência Completa por Categoria

Use sempre as constantes de `br.com.sankhya.modelcore.util.DynamicEntityNames` em vez de strings literais.

### Comercial / Notas
```java
DynamicEntityNames.CABECALHO_NOTA           // "CabecalhoNota"
DynamicEntityNames.ITEM_NOTA                // "ItemNota"
DynamicEntityNames.IMPOSTO_NOTA             // "ImpostoNota"
DynamicEntityNames.IMPOSTO_ITEM_NOTA        // "ImpostoItemNota"
DynamicEntityNames.TIPO_OPERACAO            // "TipoOperacao" (TOP)
DynamicEntityNames.NATUREZA                 // "Natureza"
DynamicEntityNames.COMPRA_VENDA_VARIOS_PEDIDO // "CompraVendavariosPedido"
DynamicEntityNames.CABECALHO_NOTA_EXCLUIDA  // "CabecalhoNotaExcluida"
```

### Financeiro
```java
DynamicEntityNames.FINANCEIRO               // "Financeiro"
DynamicEntityNames.FINANCEIRA               // "Financeira"
DynamicEntityNames.RATEIO_REC_DESP          // "RateioRecDesp"  (TGFRAT)
DynamicEntityNames.IMPOSTO_FINANCEIRO       // "ImpostoFinanceiro"
DynamicEntityNames.TIPO_TITULO              // "TipoTitulo"
DynamicEntityNames.LOCAL_FINANCEIRO         // "LocalFinanceiro"
DynamicEntityNames.PARCELA_PAGAMENTO        // "ParcelaPagamento"
```

### Cadastros principais
```java
DynamicEntityNames.EMPRESA                  // "Empresa"
DynamicEntityNames.PARCEIRO                 // "Parceiro"
DynamicEntityNames.PRODUTO                  // "Produto"
DynamicEntityNames.USUARIO                  // "Usuario"
DynamicEntityNames.VENDEDOR                 // "Vendedor"
DynamicEntityNames.TRANSPORTADORA           // "Transportadora"
DynamicEntityNames.CONTATO                  // "Contato"
```

### RH / Pessoal
```java
DynamicEntityNames.FUNCIONARIO              // "Funcionario"
DynamicEntityNames.DEPARTAMENTO             // "Departamento"
DynamicEntityNames.CARGO                    // "Cargo"
DynamicEntityNames.FUNCAO                   // "Funcao"
DynamicEntityNames.CONTRATO                 // "Contrato"
DynamicEntityNames.LOTACAO                  // "Lotacao"
DynamicEntityNames.BENEFICIO                // "Beneficio"
```

### Estoque / Logística
```java
DynamicEntityNames.ESTOQUE                  // "Estoque"
DynamicEntityNames.LOTE                     // "Lote"
DynamicEntityNames.VOLUME                   // "Volume"
DynamicEntityNames.SERIE_PRODUTO            // "SerieProduto"
DynamicEntityNames.LOCAL_ESTOQUE            // "LocalEstoque"
```

### Contabilidade
```java
DynamicEntityNames.LANCAMENTO               // "Lancamento"
DynamicEntityNames.PLANO_CONTA              // "PlanoConta"
DynamicEntityNames.CENTRO_RESULTADO         // "CentroResultado"
DynamicEntityNames.HISTORICO_PADRAO         // "HistoricoPadrao"
```

### Utilitários
```java
DynamicEntityNames.PARAMETRO_SISTEMA        // "ParametroSistema"
DynamicEntityNames.CIDADE                   // "Cidade"
DynamicEntityNames.UNIDADE_FEDERATIVA       // "UnidadeFederativa"
DynamicEntityNames.PAIS                     // "Pais"
DynamicEntityNames.BANCO                    // "Banco"
DynamicEntityNames.CONTA_BANCARIA           // "ContaBancaria"
DynamicEntityNames.ANEXO                    // "Anexo"
```

---

## 21. Padrão Objeto Nulo com Defaults

Quando uma query pode não retornar resultado, retorne um objeto com valores padrão em vez de `null` — evita `NullPointerException` no chamador:

```java
public class TaxasEventoData {
    public final String incideTaxa;
    public final BigDecimal percTaxa;
    public final String incideImp;
    public final BigDecimal percTributo;

    public TaxasEventoData(String incideTaxa, BigDecimal percTaxa,
                           String incideImp, BigDecimal percTributo) {
        this.incideTaxa  = incideTaxa;
        this.percTaxa    = percTaxa;
        this.incideImp   = incideImp;
        this.percTributo = percTributo;
    }

    // Objeto nulo com valores seguros — usado quando o registro não existe
    public static TaxasEventoData defaults() {
        return new TaxasEventoData("N", BigDecimal.ZERO, "N", BigDecimal.ZERO);
    }
}

// No repositório:
try (ResultSet rs = ns.executeQuery()) {
    if (rs.next()) {
        return new TaxasEventoData(
            rs.getString("INCIDETAXA"),
            rs.getBigDecimal("PERCTAXA"),
            rs.getString("INCIDEIMP"),
            rs.getBigDecimal("PERCTRIBUTO")
        );
    }
    return TaxasEventoData.defaults(); // nunca retorna null
}
```

---

## 22. Aceitar ID como array ou valor simples (compatibilidade)

Quando o frontend pode enviar tanto um único valor quanto um array, use um helper de parsing:

```java
private static List<BigDecimal> parseIdList(JsonObject dto) throws MGEModelException {
    if (!dto.has("CODREGISTRO") || dto.get("CODREGISTRO").isJsonNull()) {
        throw new MGEModelException("Parâmetro 'CODREGISTRO' é obrigatório");
    }
    if (dto.get("CODREGISTRO").isJsonArray()) {
        List<BigDecimal> list = new ArrayList<>();
        for (JsonElement el : dto.getAsJsonArray("CODREGISTRO")) {
            list.add(el.getAsBigDecimal());
        }
        return list;
    }
    // valor simples — embrulha em lista
    return Collections.singletonList(dto.get("CODREGISTRO").getAsBigDecimal());
}
```

---

## 23. Validação de Máquina de Estados

Para operações que dependem do status atual do registro, valide a transição antes de executar:

```java
private static String obterStatus(BigDecimal codRegistro) throws Exception {
    DynamicVO vo = JapeFactory.dao("MinhaEntidade").findByPK(codRegistro);
    if (vo == null) throw new MGEModelException("Registro não encontrado. ID=" + codRegistro);
    String status = vo.asString("STATUS");
    return status == null ? null : status.trim();
}

private static void validarTransicao(BigDecimal codRegistro, String statusAtual,
                                     String statusEsperado, String nomeAcao)
        throws MGEModelException {
    if (!statusEsperado.equals(statusAtual)) {
        throw new MGEModelException(
            "Transição inválida para " + nomeAcao
            + ". ID=" + codRegistro
            + ", status atual=" + (statusAtual == null ? "<null>" : statusAtual)
            + ", status esperado=" + statusEsperado
        );
    }
}

// Uso:
String statusAtual = obterStatus(codRegistro);
validarTransicao(codRegistro, statusAtual, "E", "retorno para provisão");
JapeFactory.dao("MinhaEntidade").prepareToUpdateByPK(codRegistro).set("STATUS", "R").update();
```

---

## 24. @ActionButton para Scripts de Migração Pontuais

Para migrações de dados que precisam ser executadas uma única vez em produção, um `@ActionButton` temporário é uma solução prática — mais segura que executar SQL direto no banco:

```java
@ActionButton(
    description = "TEMPORARIO - Migrar dados legados",
    instanceName = "MinhaEntidade",
    accessControlled = false,
    transactionType = TransactionType.AUTOMATIC,
    refreshType = RefreshTypeEnum.ALL_ITEMS
)
public class MigracaoDadosAction implements AcaoRotinaJava {

    private static final Logger logger = Logger.getLogger(MigracaoDadosAction.class);

    @Override
    public void doAction(ContextoAcao contexto) throws Exception {
        EntityFacade facade = EntityFacadeFactory.getDWFFacade();
        JdbcWrapper jdbc = facade.getJdbcWrapper();
        jdbc.openSession();

        try (NativeSql sql = new NativeSql(jdbc)) {
            sql.appendSql("UPDATE MINHA_TABELA SET CAMPO = 'NOVO' WHERE CAMPO = 'ANTIGO'");
            sql.executeUpdate();
            logger.info("[Migracao] Registros atualizados com sucesso");
        } finally {
            JdbcWrapper.closeSession(jdbc);
        }

        contexto.setMensagemRetorno("Migração concluída. Verifique os logs do servidor.");
    }
}
```

> Remova o botão após a execução em produção — deixe um comentário no código indicando quando foi executado.

---

## 25. SPBean — Tipos de Transação EJB

O tipo de transação do SPBean afeta como o `JapeSession` e o `execWithTX`/`execWithFakeTX` se comportam:

```java
/**
 * @ejb.transaction type="Required"      ← transação gerenciada pelo container (padrão)
 * @ejb.transaction type="NotSupported"  ← sem transação — necessário quando o código
 *                                          gerencia transações manualmente via execWithTX
 * @ejb.transaction type="Supports"      ← participa de transação existente se houver
 */
```

Use `NotSupported` quando o SPBean usa `hnd.execWithTX()` ou `hnd.execWithFakeTX()` — se o container já gerencia uma transação, o `execWithFakeTX` não consegue fazer rollback corretamente.

```java
/**
 * @ejb.bean name="ProcessaImpostoDsSP"
 * type="Stateless"
 * transaction-type="Container"
 * @ejb.transaction type="NotSupported"
 */
public class MeuProcessoSPBean extends BaseSPBean implements SessionBean {

    public void executar(ServiceContext ctx) throws Exception {
        ctx.setAutentication(AuthenticationInfo.getCurrent());
        ctx.makeCurrent();

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            // hnd.execWithFakeTX e hnd.execWithTX funcionam corretamente aqui
            // porque não há transação de container interferindo
            MeuProcessoHelper helper = new MeuProcessoHelper(hnd);
            helper.processar(codRegistro);
        } finally {
            JapeSession.close(hnd);
        }
    }
}
```

---

## 26. Testes

O Add-on Studio 2.0 clássico **não tem suporte a testes unitários sem um servidor Sankhya em execução**. As APIs de persistência (`JapeFactory`, `DynamicVO`, `NativeSql`) dependem do container EJB e do banco de dados — não é possível mocká-las de forma simples.

**O que é possível testar sem servidor:**
- Lógica pura em classes utilitárias que não dependem de `JapeFactory` ou `NativeSql`
- Cálculos, formatações, validações de regras de negócio isoladas em métodos estáticos ou classes sem dependências de infraestrutura

**O que requer servidor:**
- Qualquer operação com `JapeFactory.dao()`, `NativeSql`, `JapeSession`, `EntityFacade`
- Listeners, ActionButtons, Services — todos dependem do container

**Estratégia recomendada:**
- Isole a lógica de negócio pura em métodos sem dependências de infraestrutura — esses podem ser testados com JUnit
- Valide o restante com testes manuais em ambiente local (Docker + WildFly via `./gradlew deployAddon`)

