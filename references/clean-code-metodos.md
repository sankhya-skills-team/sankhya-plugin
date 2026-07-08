# Clean Code: Boas Práticas para Criar Métodos

## 1. Nomes Significativos e Descritivos

O nome deve expressar claramente o que o método faz. Use verbos no infinitivo para ações.

```java
// RUIM
public void proc(DynamicVO vo) { }
public BigDecimal calc(DynamicVO vo) { }

// BOM
public void validarStatusParaAprovacao(DynamicVO vo) throws NomeModuloException { }
public BigDecimal calcularPesoTotalDaOrdem(BigDecimal nuNota) throws Exception { }
```

---

## 2. Faça Uma Coisa Apenas (Single Responsibility)

Se você precisa usar "e" para descrever o método, ele está fazendo demais.

```java
// RUIM
public void validarEAtualizarENotificar(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao(ENTIDADE).findByPK(id);
    if ("F".equals(vo.asString("STATUS"))) throw new NomeModuloException("...");
    JapeFactory.dao(ENTIDADE).prepareToUpdateByPK(id).set("STATUS", "P").update();
    MessageUtils.showInfo("Registro processado.");
}

// BOM
public void processarRegistro(BigDecimal id) throws Exception {
    DynamicVO vo = nomeRepository.buscarPorId(id);
    nomeService.validarParaProcessamento(vo);
    nomeRepository.atualizarStatus(id, "P");
}
```

---

## 3. Métodos Pequenos

Idealmente menos de 20 linhas. Extraia responsabilidades para métodos auxiliares.

```java
// RUIM
public void processarLote(List<DynamicVO> itens) throws Exception {
    // 60 linhas: validação, cálculo de peso, atualização de status,
    // geração de nota, cálculo de impostos, log...
}

// BOM
public void processarLote(List<DynamicVO> itens) throws Exception {
    List<DynamicVO> validos = filtrarItensValidos(itens);
    for (DynamicVO item : validos) {
        processarItem(item);
    }
}

private List<DynamicVO> filtrarItensValidos(List<DynamicVO> itens) { ... }
private void processarItem(DynamicVO item) throws Exception { ... }
```

---

## 4. Poucos Parâmetros

Limite a 0–2. Se precisar de mais, encapsule em DTO.

```java
// RUIM
public BigDecimal criarOrdem(BigDecimal codEmp, BigDecimal codParc,
                              BigDecimal codProd, BigDecimal quantidade,
                              BigDecimal vlrUnit, String observacao) throws Exception { }

// BOM
public BigDecimal criarOrdem(OrdemColetaDto dados) throws Exception { }

// DTO agrupa os parâmetros
public class OrdemColetaDto {
    private BigDecimal codEmp;
    private BigDecimal codParc;
    private BigDecimal codProd;
    private BigDecimal quantidade;
    private BigDecimal vlrUnit;
    private String observacao;
}
```

---

## 5. Return Early (Retorno Antecipado)

Retorne imediatamente quando uma condição de guarda é satisfeita. Evita aninhamento.

```java
// RUIM
public void processarEvento(DynamicVO vo) throws Exception {
    if (vo != null) {
        BigDecimal id = vo.asBigDecimal("ID");
        if (!BigDecimalUtil.isNullOrZero(id)) {
            String status = vo.asString("STATUS");
            if ("P".equals(status)) {
                // lógica real aqui — enterrada em 3 níveis
            }
        }
    }
}

// BOM
public void processarEvento(DynamicVO vo) throws Exception {
    if (vo == null) return;

    BigDecimal id = vo.asBigDecimal("ID");
    if (BigDecimalUtil.isNullOrZero(id)) return;

    String status = vo.asString("STATUS");
    if (!"P".equals(status)) return;

    // lógica real aqui — sem aninhamento
}
```

---

## 6. Evite Efeitos Colaterais Ocultos

Métodos não devem fazer mais do que o nome indica.

```java
// RUIM — validar não deveria persistir
public boolean validarRegistro(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao(ENTIDADE).findByPK(id);
    if (vo == null) return false;
    JapeFactory.dao(ENTIDADE).prepareToUpdateByPK(id)
        .set("DTVALIDACAO", TimeUtils.getNow()) // efeito colateral!
        .update();
    return true;
}

// BOM — responsabilidades separadas
public void validarRegistro(DynamicVO vo) throws NomeModuloException {
    if (vo == null) throw NomeModuloException.naoEncontrado("Registro", null);
}

public void registrarValidacao(BigDecimal id) throws Exception {
    JapeFactory.dao(ENTIDADE).prepareToUpdateByPK(id)
        .set("DTVALIDACAO", TimeUtils.getNow())
        .update();
}
```

---

## 7. Use Exceções ao Invés de Códigos de Erro

Códigos de retorno numéricos tornam o fluxo confuso. Use `NomeModuloException`.

```java
// RUIM
public int processarOrdem(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao(ENTIDADE).findByPK(id);
    if (vo == null) return -1;
    if ("F".equals(vo.asString("STATUS"))) return -2;
    // processar...
    return 0;
}

// BOM
public void processarOrdem(BigDecimal id) throws Exception {
    DynamicVO vo = nomeRepository.buscarPorId(id);
    nomeService.validarParaProcessamento(vo); // lança NomeModuloException se inválido
    nomeRepository.atualizarStatus(id, "E");
}
```

---

## 8. Não Repita Código (DRY)

Extraia lógica repetida para `service/` ou `repository/`.

```java
// RUIM — mesma validação em dois lugares
public void aprovarAmostra(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao(ENTIDADE).findByPK(id);
    if (vo == null) throw new MGEModelException("Amostra não encontrada: " + id);
    if ("A".equals(vo.asString("STATUS")))
        throw new MGEModelException("Amostra já aprovada: " + id);
    JapeFactory.dao(ENTIDADE).prepareToUpdateByPK(id).set("STATUS", "A").update();
}

public void reprovarAmostra(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao(ENTIDADE).findByPK(id);
    if (vo == null) throw new MGEModelException("Amostra não encontrada: " + id); // duplicado
    if ("R".equals(vo.asString("STATUS")))
        throw new MGEModelException("Amostra já reprovada: " + id);
    JapeFactory.dao(ENTIDADE).prepareToUpdateByPK(id).set("STATUS", "R").update();
}

// BOM — busca e validação de existência extraídas para o repository/service
public void aprovarAmostra(BigDecimal id) throws Exception {
    DynamicVO vo = amostraRepository.buscarPorId(id); // lança se não encontrar
    amostraService.validarParaAprovacao(vo);
    amostraRepository.atualizarStatus(id, StatusAmostra.APROVADO);
}

public void reprovarAmostra(BigDecimal id) throws Exception {
    DynamicVO vo = amostraRepository.buscarPorId(id);
    amostraService.validarParaReprovacao(vo);
    amostraRepository.atualizarStatus(id, StatusAmostra.REPROVADO);
}
```

---

## 9. Comentários Não Substituem Código Ruim

Se precisa comentar o que o código faz, o código não está claro.

```java
// RUIM
// verifica se o status é P e se tem peso maior que zero
public boolean check(DynamicVO vo) {
    return "P".equals(vo.asString("STATUS"))
        && !BigDecimalUtil.isNullOrZero(vo.asBigDecimal("PESOBRUTO"));
}

// BOM
public boolean estaAguardandoPesagem(DynamicVO vo) {
    return StatusOrdem.PENDENTE.getCodigo().equals(vo.asString("STATUS"))
        && !BigDecimalUtil.isNullOrZero(vo.asBigDecimal("PESOBRUTO"));
}
```

---

## 10. Mantenha o Mesmo Nível de Abstração

Não misture chamadas de alto nível (service, component) com operações de baixo nível
(manipulação de string, acesso campo a campo) no mesmo método.

```java
// RUIM — alto e baixo nível misturados
public void executarOperacao(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao(ENTIDADE).findByPK(id); // baixo nível
    String status = vo.asString("STATUS");                  // baixo nível
    if ("F".equals(status)) throw new NomeModuloException("..."); // baixo nível
    nomeRepository.atualizarStatus(id, "P");                // alto nível
    MessageUtils.showInfo("OK");                            // alto nível
}

// BOM — component orquestra em alto nível; detalhes ficam no service/repository
public void executarOperacao(BigDecimal id) throws Exception {
    DynamicVO vo = nomeRepository.buscarPorId(id);   // alto nível
    nomeService.validarParaExecucao(vo);              // alto nível
    nomeRepository.atualizarStatus(id, "P");          // alto nível
}
```

---

## Checklist

Ao criar um método:

- [ ] O nome deixa claro o que ele faz?
- [ ] O método faz apenas uma coisa?
- [ ] Tem menos de 20 linhas?
- [ ] Tem no máximo 2–3 parâmetros (ou DTO)?
- [ ] Usa return early para evitar aninhamento?
- [ ] Não tem efeitos colaterais não descritos no nome?
- [ ] Usa `NomeModuloException` em vez de código de retorno de erro?
- [ ] Não há lógica duplicada — extraída para `service/` ou `repository/`?
- [ ] Comentários só existem para o porquê, não para o quê?
- [ ] Todos os elementos estão no mesmo nível de abstração?
