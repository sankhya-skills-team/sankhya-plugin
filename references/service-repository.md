# Service e Repository

## Visão Geral

As camadas `service/` e `repository/` concentram toda a lógica de negócio e acesso a dados
da demanda. Nenhum artefato Sankhya (`actionbutton/`, `event/`, `job/`, `regra/`) deve
conter código dessas responsabilidades — sempre delegam para cá.

---

## `service/` — Regras de Negócio

### Responsabilidade

- Regras de negócio puras: validações, cálculos, transformações
- **NÃO acessa banco** — não chama `repository/`, não usa `JapeFactory`/`DwfUtils`
- **NÃO chama `MGEModelException`** — lança `NomeModuloException` para erros de negócio
- Recebe dados já carregados pelo `component/` e opera sobre eles

### Estrutura

```java
public class NomeService {

    // Sem NomeRepository — service não acessa banco

    // Validação de estado — recebe DynamicVO já carregado pelo component/
    public void validarParaExecucao(DynamicVO vo) throws NomeModuloException {
        String status = vo.asString("STATUS");
        if ("F".equals(status)) {
            throw NomeModuloException.statusInvalido(status, "executar operação");
        }
    }

    // Cálculo puro — sem acesso a dados
    public BigDecimal calcularDesconto(BigDecimal valor, BigDecimal percentual) {
        if (BigDecimalUtil.isNullOrZero(valor) || BigDecimalUtil.isNullOrZero(percentual)) {
            return BigDecimal.ZERO;
        }
        return valor.multiply(percentual).divide(new BigDecimal("100"), 2, RoundingMode.HALF_UP);
    }

    // Validação com múltiplos VOs — ambos carregados pelo component/ antes desta chamada
    public void validarVinculo(DynamicVO voFilho, DynamicVO voPai) throws NomeModuloException {
        String statusPai = voPai.asString("STATUS");
        if ("F".equals(statusPai)) {
            throw NomeModuloException.statusInvalido(statusPai,
                    "vincular registro ID " + voFilho.asBigDecimal("ID"));
        }
    }
}
```

### Fluxo correto via component/

```
actionbutton/  →  component/  →  service.validar(vo)          [puro]
                             →  repository.atualizar(id, ...)  [banco]

event/         →  component/  →  service.calcular(vo)          [puro]
                             →  repository.salvar(...)          [banco]

job/           →  component/  →  repository.listarPendentes()  [banco]
                             →  service.processarItem(vo)       [puro]
                             →  repository.atualizar(id, ...)   [banco]
```

---

## `repository/` — Acesso a Dados

### Responsabilidade

- Operações de persistência: consultas, inserts, updates, deletes
- Sem regras de negócio — não lança `NomeModuloException`
- Retorna `null` ou lista vazia quando não encontrar — quem decide o que fazer é o `service/`
- **Exclusivo para entidades customizadas (`AD_*`)** — para entidades nativas do Sankhya
  (`TGFCAB`, `TGFPAR`, `TGFPRO`, etc.), usar `JapeFactory` ou `DwfUtils` diretamente no `service/`

### JAPE vs NativeSql

| Situação | O que usar |
|---|---|
| Operação que deve disparar outros eventos Sankhya | `JapeFactory` (JAPE) |
| Operação interna que **não** deve disparar outros eventos | `NativeSql` / `JdbcWrapper` |
| "Economizar código" | **Nunca** — usar sempre JAPE nesse caso |

### Leitura

```java
// Por chave primária
public DynamicVO buscarPorId(BigDecimal id) throws Exception {
    return JapeFactory.dao(ENTIDADE).findByPK(id);
}

// Por condição — retorna lista nunca nula
public List<DynamicVO> listarPorStatus(String status) throws Exception {
    Collection<DynamicVO> resultado = JapeFactory.dao(ENTIDADE)
            .find("this.STATUS = ?", new Object[]{status});
    if (resultado == null) return new ArrayList<>();
    return new ArrayList<>(resultado);
}
```

### Escrita via JAPE (dispara eventos)

```java
// Update
public void atualizarStatus(BigDecimal id, String novoStatus) throws Exception {
    JapeFactory.dao(ENTIDADE)
            .prepareToUpdateByPK(id)
            .set("STATUS", novoStatus)
            .update();
}

// Insert — retorna VO com chave gerada
public DynamicVO inserir(BigDecimal codEmp, String descricao) throws Exception {
    return JapeFactory.dao(ENTIDADE).create()
            .set("CODEMP", codEmp)
            .set("DESCRICAO", descricao)
            .set("STATUS", "A")
            .save();
}
```

### Escrita via NativeSql (não dispara eventos)

```java
// Em actionbutton/job: usar JapeSession.SessionHandle para obter o JdbcWrapper
// Em event: usar pEvent.getJdbcWrapper() — nunca abrir nova JapeSession dentro de evento

public void atualizarStatusSemEvento(BigDecimal id, String novoStatus,
                                      JapeSession.SessionHandle hnd) throws Exception {
    hnd.getJdbcWrapper().executeUpdate(
            "UPDATE AD_NOMETABELA SET STATUS = ? WHERE ID = ?",
            new Object[]{novoStatus, id});
}
```

---

## `exception/` — Exceções de Domínio

### Responsabilidade

- Representa erros de negócio previstos (regra violada, estado inválido, registro não encontrado)
- Mensagens com código rastreável — facilita localizar o ponto no fonte sem stack trace
- **Nunca sobe para a plataforma Sankhya** — convertida para `MGEModelException` na borda

### Convenção de código

```
[XXX_NNNN]
 ↑          ↑
 3 letras   sequencial 4 dígitos
 do módulo
```

Exemplos: `[VGM_0001]` para Viagem, `[ENT_0001]` para Entregas, `[NOM_0001]` para NomeDemanda.

### Estrutura com fábrica de mensagens

```java
public class NomeModuloException extends Exception {

    public NomeModuloException(String message) { super(message); }
    public NomeModuloException(String message, Throwable cause) { super(message, cause); }

    public static NomeModuloException naoEncontrado(String entidade, BigDecimal id) {
        return new NomeModuloException("[NOM_0001] " + entidade + " ID " + id + " não encontrado.");
    }

    public static NomeModuloException statusInvalido(String statusAtual, String operacao) {
        return new NomeModuloException(
                "[NOM_0002] Status '" + statusAtual + "' não permite '" + operacao + "'.");
    }

    public static NomeModuloException transicaoInvalida(String de, String para) {
        return new NomeModuloException(
                "[NOM_0003] Transição de '" + de + "' para '" + para + "' não permitida.");
    }
}
```

### Conversão na borda (`actionbutton/` e `event/`)

```java
// actionbutton/
} catch (NomeModuloException e) {
    throw MGEModelException.prettyMsg(e.getMessage(), e);
} catch (Exception e) {
    throw MGEModelException.prettyMsg("Erro inesperado: <br>" + e.getMessage(), e);
}

// event/ (beforeInsert, beforeUpdate, etc.)
} catch (NomeModuloException e) {
    throw new MGEModelException(e.getMessage());
}
```

---

## DTO — Quando usar

Use DTO para trafegar dados entre camadas quando:

- Precisar combinar campos de mais de uma entidade
- Um `DynamicVO` único não for suficiente para representar o que precisa
- Mapear resultado de query complexa com campos calculados

Não criar DTO quando um `DynamicVO` ou apenas o `id` já resolve.

```java
// Construtor a partir de DynamicVO — usado no event/ antes de delegar para service
public NomeDto(DynamicVO vo) throws Exception {
    this.id            = vo.asBigDecimal("ID");
    this.idPai         = vo.asBigDecimal("ID_PAI");
    this.codigoEmpresa = vo.asBigDecimal("CODEMP");
    this.status        = vo.asString("STATUS");
}
```
