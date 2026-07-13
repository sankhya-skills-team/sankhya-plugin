# component/

Hub de orquestração da demanda. Ponto de entrada único para todos os artefatos.

## Responsabilidade

- Ser chamado por `actionbutton/`, `event/`, `job/`, `regra/` e `controller/`
- Coordenar chamadas a `service/` (regras de negócio puras) e `repository/` (acesso a dados)
- Tratar exceções de infraestrutura e dar-lhes significado de negócio

## Proibido

- Regras de negócio puras — extrair para `service/`
- Acesso direto ao banco — usar `repository/`

## Skeleton base

```java
package br.com.sankhya.customizacao.nomedemanda.component;

import br.com.sankhya.customizacao.nomedemanda.exception.NomeDemandaException;
import br.com.sankhya.customizacao.nomedemanda.repository.NomeRepository;
import br.com.sankhya.customizacao.nomedemanda.service.NomeService;
import br.com.sankhya.jape.vo.DynamicVO;

import java.math.BigDecimal;

/**
 * Component: [Descrição do que este component orquestra]
 */
public class NomeComponent {

    private final NomeRepository nomeRepository = new NomeRepository();
    private final NomeService nomeService = new NomeService();

    /**
     * [Descrição da operação]
     *
     * @throws NomeDemandaException quando [condição de negócio inválida]
     */
    public String executarOperacao(BigDecimal id) throws Exception {
        DynamicVO vo = nomeRepository.buscarPorId(id);
        if (vo == null) throw NomeDemandaException.naoEncontrado("NomeDemanda", id);

        nomeService.validarParaExecucao(vo);
        nomeRepository.atualizarStatus(id, "P");
        return "Operação executada com sucesso.";
    }
}
```

---

## Padrões por Contexto de Chamada

### Chamado por `actionbutton/` — recebe `Registro[]`

O `actionbutton/` extrai o ID do `Registro` e passa para o component. Para lote, passa o array inteiro.

```java
// Operação em registro único
public String executarOperacao(BigDecimal id) throws Exception {
    DynamicVO vo = nomeRepository.buscarPorId(id);
    if (vo == null) throw NomeDemandaException.naoEncontrado("NomeDemanda", id);

    nomeService.validar(vo);
    nomeRepository.atualizarStatus(id, "P");
    return "Registro <b>" + id + "</b> processado com sucesso.";
}

// Operação em lote — retorna contagem para mensagem do botão
public int processarLote(Registro[] registros) throws Exception {
    int processados = 0;
    for (Registro registro : registros) {
        BigDecimal id = BigDecimalUtil.getBigDecimal(registro.getCampo("ID_CAMPO"));
        DynamicVO vo = nomeRepository.buscarPorId(id);
        if (vo == null) continue;

        nomeService.validar(vo);
        nomeRepository.atualizarStatus(id, "P");
        processados++;
    }
    return processados;
}
```

### Chamado por `event/` — recebe `DynamicVO` ou DTO

Em operações simples (set de campo na própria entidade), o evento age direto no VO sem component.
O component entra quando a operação envolve outras entidades ou lógica condicional.

```java
// Recebe VO diretamente quando a operação é sobre a própria entidade do evento
public void processarInsercao(BigDecimal id) throws Exception {
    nomeService.validarEstadoInicial(id);
    nomeRepository.criarRegistrosFilhos(id);
}

// Recebe DTO quando o event extrai dados antes de delegar
public void processarAtualizacao(NomeDto dto) throws Exception {
    nomeService.validarTransicao(dto.getStatusAnterior(), dto.getStatusNovo());
    nomeRepository.atualizarDadosDerivados(dto.getId(), dto);
}
```

### Chamado por `job/` — processa lote sem contexto de usuário

```java
// Sem parâmetros ou com filtro de data/status passado pelo job
public void processarPendentes() throws Exception {
    List<DynamicVO> pendentes = nomeRepository.listarPorStatus("P");
    for (DynamicVO vo : pendentes) {
        BigDecimal id = vo.asBigDecimal("ID_CAMPO");
        try {
            nomeService.processarItem(vo);
            nomeRepository.atualizarStatus(id, "C");
        } catch (NomeDemandaException e) {
            // Logar e continuar — não abortar o lote inteiro por um item
            Logger.error("Falha ao processar item | id=" + id + " | " + e.getMessage(), e);
            nomeRepository.atualizarStatus(id, "E"); // status de erro
        }
    }
}
```

### Chamado por `controller/` — recebe parâmetros de request externo

```java
// Parâmetros já validados e extraídos pelo controller
public String executarViaServico(BigDecimal id, String parametro) throws Exception {
    DynamicVO vo = nomeRepository.buscarPorId(id);
    if (vo == null) throw NomeDemandaException.naoEncontrado("NomeDemanda", id);

    nomeService.validarParametro(parametro);
    nomeRepository.atualizarComParametro(id, parametro);
    return "Operação concluída para " + id;
}
```

---

## Tratamento de exceções

O component **não converte** `NomeDemandaException` para `MGEModelException`.
A conversão é feita na borda pelos artefatos Sankhya.

```java
// Em actionbutton/, event/ ou regra/:
} catch (NomeDemandaException e) {
    throw MGEModelException.prettyMsg(e.getMessage(), e);
} catch (Exception e) {
    throw MGEModelException.prettyMsg("Erro inesperado: " + e.getMessage(), e);
}
```

## Regra de ouro

> Todos os artefatos Sankhya passam pelo `component/`.
> Nenhum artefato acessa `service/` ou `repository/` diretamente.
