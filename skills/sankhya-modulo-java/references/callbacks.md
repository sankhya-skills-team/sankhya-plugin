# Callbacks customizados — `ICustomCallBack`

Ponto de extensão do core que executa uma classe do Módulo Java em momentos fixos do fluxo
comercial (cabeçalho da nota, confirmação, faturamento, XML da NF-e, preço do item, Flex,
impostos). O vínculo entre o ponto e a classe é um **parâmetro em Preferências**.

Conferido no bytecode de `mge-modelcore-4.36b208`, `mgecom-model-5.28.3` (erpcore) e
`mgeliv-model-5.53.0`. O que vem só da documentação da Sankhya está marcado como tal.

---

## Quando usar

| Necessidade | Use |
|---|---|
| Reagir a um dos 11 pontos do catálogo abaixo | Callback |
| Reagir a insert/update/delete de uma entidade | `EventoProgramavelJava` (`references/event-java.md`) |
| Regra no barramento de regras da nota, com liberação de limite | `RegraNegocioJava` (`references/regra-negocio.md`) |

A confirmação pela Central grava `STATUSNOTA = 'L'` por procedure e não gera evento JAPE.
Um `EventoProgramavelJava` de `CabecalhoNota` não vê essa confirmação; o callback
`central.processarConfirmacao.*` vê.

**Addon Studio:** a anotação `@Callback` só cobre os quatro eventos do enum `CallbackEvent`
(SDK 2.20.1). Os callbacks `portal.xmlnfe.after` e os três `mgecom.*` só funcionam por
Módulo Java, como descrito aqui.

---

## Implementação

```java
package br.com.sankhya.customizacao.nomedemanda.callback;

import java.math.BigDecimal;
import java.util.Map;

import br.com.sankhya.modelcore.custommodule.ICustomCallBack;

public class ValidaConfirmacaoCallback implements ICustomCallBack {

    @Override
    public Object call(String id, Map<String, Object> data) {
        BigDecimal nunota = (BigDecimal) data.get("nunota");
        // delegar a regra para o component/
        return null;
    }
}
```

Regras da classe:

- **Construtor público sem argumentos.** O core instancia por reflexão (`Class.newInstance()`).
- **`call` não declara `throws`.** A interface não declara exceção checada, então
  `throws Exception` na implementação não compila. Para abortar a operação lance uma
  exceção não checada (`IllegalStateException`). `MGEModelException` é checada: capture e
  relance embrulhada.
- **`id`** é o identificador do ponto de disparo (coluna "Id" do catálogo). Use-o quando a
  mesma classe atende mais de um ponto.
- **`data` não é tipado.** Cada valor exige cast para o tipo indicado no catálogo. As chaves
  diferenciam maiúsculas de minúsculas (`bregras` e `bRegras` são chaves diferentes).
- **O efeito vem de alterar os objetos recebidos.** Os VOs e o `pui` chegam por referência e
  as alterações valem para o restante do fluxo. O retorno só é lido em
  `mgecom.validaDescontoAcrescimo.before`.

Organize como os demais artefatos: a classe do callback extrai os dados do `Map` e delega
para o `component/`.

---

## Registro

1. Gere o JAR e importe como Módulo Java. Anote o `NUMODULO`.
2. Peça à Sankhya a **liberação da chave do parâmetro** para a base. Sem a liberação, a
   operação falha com `CORE_E07912` ("Esta regra de negócio exige autorização pelo
   administrador do sistema! Código da regra: `<chave>` Base: `<domínio>`").
3. Em Preferências, preencha o parâmetro da chave (descrição `Callback: <id>`) com
   `<NUMODULO>@<classe completa>`:

```
12@br.com.sankhya.customizacao.nomedemanda.callback.ValidaConfirmacaoCallback
```

Para encadear implementações no mesmo ponto, separe por `;`:

```
12@br.com.cliente.CallbackA;12@br.com.cliente.CallbackB
```

Como o core lê o valor (`CustomCallBackUtils.fire`):

- O parâmetro é `call_back.<id>`. O valor é dividido por `;` e cada entrada por `@`.
- **Entrada sem `@` é ignorada em silêncio.** Erro de digitação no valor não gera erro: o
  callback apenas não roda.
- Classe não encontrada no módulo gera `CORE_E06556`.
- A checagem de liberação só roda quando o parâmetro está preenchido. Parâmetro vazio não
  executa nada e não custa nada relevante (o valor é cacheado).
- Executam primeiro as classes do parâmetro, na ordem escrita, e depois os callbacks
  registrados por addon. **Vale o retorno da última execução.**

---

## Catálogo

| Id | Parâmetro | Dispara em |
|---|---|---|
| `central.cabecalho.before` | `CBACKCABBEF` | Inclusão/alteração do cabeçalho da nota, antes |
| `central.cabecalho.after` | `CBACKCABAFT` | Inclusão/alteração do cabeçalho da nota, depois |
| `central.processarConfirmacao.before` | `CBACKPRCCONFBEF` | Confirmação pela Central, antes |
| `central.processarConfirmacao.after` | `CBACKPRCCONFAFT` | Confirmação pela Central, depois |
| `central.confirmacao_portal.before` | `CBACKCONFPORBEF` | Confirmação em lote pelo portal, antes |
| `central.confirmacao_portal.after` | `CBACKCONFPORAFT` | Confirmação em lote pelo portal, depois |
| `portal.processarFaturamento.before` | `CBACKPRCFATDOC` | Início do faturamento |
| `portal.xmlnfe.after` | `CBACKXMLNFEAFT` | Depois de montar o XML da NF-e |
| `mgecom.inicializaProduto.flex.before` | `CBACKINIPRDFLX` | Inicialização do item, antes do Conta Corrente Flex |
| `mgecom.validaDescontoAcrescimo.before` | `CBACKVLDDESCAC` | Antes da validação de desconto/acréscimo Flex |
| `mgecom.impostosConfirmacao.after` | `CBACKIMPCONFAFT` | Confirmação, depois do cálculo nativo dos impostos |

Os três `mgecom.*` saíram no `erpcore-5.27.4` e no `mgeliv-5.52.3` (KB-183204). Na 4.36 o
cliente precisa atualizar esses dois módulos. A documentação da Sankhya cita os ids como
`central.*`; o `id` que chega no `call` é `mgecom.*`.

---

## Callbacks de nota

### `central.cabecalho.before` / `.after`

Disparados em `CACHelper.incluirAlterarCabecalho`, pela lógica de negócio da Central (não
por CRUD do JAPE).

| Chave | Tipo | Disponível em |
|---|---|---|
| `cabState` | `PrePersistEntityState` | before, after |
| `oldCabVO` | `DynamicVO` | after |
| `bRegras` | `BarramentoRegra` | after |

### `central.processarConfirmacao.before` / `.after`

Disparados em `CACHelper.processarConfirmacao`, que atende o botão Confirmar da Central.
Portal em lote e API não passam por aqui.

| Chave | Tipo | Disponível em |
|---|---|---|
| `nunota` | `BigDecimal` | before, after |
| `bregras` | `BarramentoRegra` | before, after |
| `cab_state` | estado do cabeçalho (tipo não conferido) | after |
| `error` | `Exception`, preenchido se a confirmação falhou | after |

- **O `after` roda fora de transação** ("Operação requer uma transação ativa"). Para gravar,
  use `SessionHandle.execEnsuringTX`.
- Confirmação com liberação pendente para sem avisar (só um WARN do `LiberacaoAlcadaHelper`).
  Releia o `STATUSNOTA` antes de assumir que a nota foi confirmada.

### `central.confirmacao_portal.before` / `.after`

Disparados na confirmação em lote do portal (`DocumentoEletronicoHelper`). A Central não os
dispara.

| Chave | Tipo | Disponível em |
|---|---|---|
| `nunota` | `BigDecimal` | before, after |
| `bregras` | `BarramentoRegra` | before, after |
| `error` | `Exception`, preenchido se a confirmação falhou | after |

### `portal.processarFaturamento.before`

Disparado no início do faturamento (`SelecaoDocumentoSPBean`). Não existe `after`.

| Chave | Tipo |
|---|---|
| `notasSelecao` | `Collection<BigDecimal>` |
| `itensEditados` | `Map<String, BigDecimal>` — chave `nunota-sequencia`, valor é a quantidade a faturar |

### `portal.xmlnfe.after`

Disparado em `GeradorXmlNFe2`, depois de montar o grupo `infNFe`.

| Chave | Tipo |
|---|---|
| `rsetCab` | `ResultSet` do cabeçalho (TGFCAB) |
| `xml` | XML em montagem (tipo não conferido) |
| `parcVO` | `DynamicVO` do parceiro |
| `topVO` | `DynamicVO` da TOP |
| `empVO` | `DynamicVO` da empresa |
| `finalidade` | `String` |

---

## Callbacks de preço, Flex e impostos

Os dois primeiros ficam em caminho de altíssima frequência: disparam por item, a cada
interação na Central. Mantenha a implementação enxuta, sem consulta pesada nem chamada
remota.

### `mgecom.inicializaProduto.flex.before`

Permite ajustar o preço unitário antes de o Conta Corrente Flex calcular o preço base.
Disparado em `CentralItemNota.inicializaProduto(IParamsInicializacaoProduto)`, depois do
cálculo de preço (tabela, promoção, taxa do tipo de negociação, IPI/ST embutido) e
imediatamente antes de `new ContaCorrenteFlexHelper()`. Retorno ignorado.

| Chave | Tipo | Descrição |
|---|---|---|
| `pui` | `IPrecoUnitarioInfo` | Preço calculado. É o objeto a alterar: `setVlrUnit`, `setPercDesc`, `setVlrCus`, `setPrecoBase` |
| `cabVO` | `DynamicVO` | Cabeçalho (TGFCAB) |
| `params` | `IParamsInicializacaoProduto` | `getCodProd`, `getCodVol`, `getControle`, `getQtdNeg`, `getNuNota`, `getSeqNota`, `isChamadoPelaTela`, `isCarrinho` |
| `prodVO` | `DynamicVO` | Produto (TGFPRO) |
| `codProd` | `BigDecimal` | Atalho para `params.getCodProd()` |
| `descFOB` | `Boolean` | Indica desconto FOB aplicado |

Ambos os tipos ficam em `br.com.sankhya.modelcore.comercial.proxyconnect`.

```java
IPrecoUnitarioInfo pui = (IPrecoUnitarioInfo) data.get("pui");
DynamicVO cabVO = (DynamicVO) data.get("cabVO");

if ("V".equals(cabVO.asString("TIPMOV"))) {
    pui.setVlrUnit(pui.getVlrUnit().multiply(FATOR_AJUSTE));
}
return null;
```

**Quando não dispara** (o método retorna antes do ponto de disparo):

- Parâmetro `mgecom.usa.cache.inicializacao.produto` ligado e o mesmo item já inicializado
  na transação. A chave do cache é `nunota:codprod:controle:codvol:codlocal:usoprod`.
- `params.isBuscarApenasPreco()` verdadeiro.
- TOP com `USARPRECOCUSTO = 'N'` e `params.isForcarCalcPreco()` falso (leitura do bytecode,
  sem o fonte).
- Preço por local ligado, produto com `USALOCAL` e local de origem zerado.
- Preço por controle ligado e item ainda sem controle informado.

### `mgecom.validaDescontoAcrescimo.before`

Permite substituir a validação padrão de desconto/acréscimo Flex. É o único callback cujo
retorno é lido. Disparado em `ContaCorrenteFlexHelper.calculaVlrAcresDesconto`, depois de
gravar `VLRACRESCDESC` no item e antes de `validaDescontoAcrescimo()`.

| Chave | Tipo | Descrição |
|---|---|---|
| `itemVO` | `DynamicVO` | Item (TGFITE), já com `VLRACRESCDESC`. Alterável |
| `cabVO` | `DynamicVO` | Cabeçalho (TGFCAB) |
| `topVO` | `DynamicVO` | TOP (TGFTOP) |
| `prodVO` | `DynamicVO` | Produto (TGFPRO), com `DESCMAXFLEX` e `ACRESCMAX` |
| `vendedorVO` | `DynamicVO` | Vendedor (TGFVEN), com `SALDODISP`, `DESCMAX`, `GRUPORETENCAO` |
| `parcVO` | `DynamicVO` | Parceiro (TGFPAR) |
| `pui` | `IPrecoUnitarioInfo` | **Pode vir `null`** |
| `vlrAcresDescAnt` | `Double` | Valor de acréscimo/desconto anterior à alteração |
| `modoCarrinhoCompra` | `Boolean` | Operação veio do carrinho |

Contrato do retorno (o core testa `Boolean.FALSE.equals(retorno)`):

| Retorno | Efeito |
|---|---|
| `Boolean.FALSE` | `validaDescontoAcrescimo()` **não** roda |
| `null`, `Boolean.TRUE` ou qualquer outro objeto | `validaDescontoAcrescimo()` roda normalmente |

```java
DynamicVO itemVO = (DynamicVO) data.get("itemVO");
Double vlrAnterior = (Double) data.get("vlrAcresDescAnt");

if (descontoAcimaDoPermitido(itemVO, vlrAnterior)) {
    throw new IllegalStateException("Desconto acima do permitido para este cliente.");
}
itemVO.setProperty("VLRRETENCAO", calcularRetencao(itemVO));
return Boolean.FALSE;
```

Cuidados:

- **`VLRRETENCAO` passa a ser responsabilidade do callback.** `validaDescontoAcrescimo()`
  não só valida: zera `VLRRETENCAO` quando o valor é desconto e aplica o percentual de
  `com.perc.retencao.acrescimo` quando é acréscimo. Ao devolver `Boolean.FALSE`, grave o
  campo no `itemVO`.
- **Vários callbacks no mesmo parâmetro:** só o retorno do último decide. Não espalhe a
  decisão entre implementações.
- **`PRECOBASEQTD` não é calculado em TOP de bonificação** (`TGFTOP.BONIFICACAO = 'S'`).
  Nesse caso `VLRACRESCDESC` vale `-PRECOBASE * QTDNEG` e o callback dispara assim mesmo.

**Quando não dispara:**

- Nota sem Flex (`temFlex()` falso). O core zera `VLRACRESCDESC` e `VLRRETENCAO`.
- Flex Dinâmico ativo na empresa (`CalculoFlexDinamico`): o fluxo desvia antes do ponto.
- Chamada interna com `validar = false` (a sobrecarga de dois argumentos passa `true`).

### `mgecom.impostosConfirmacao.after`

Permite gravar impostos customizados na TGFDIN durante a confirmação. Disparado no fim de
`ImpostosConfirmacaoNotaRegra.beforeUpdate`, depois do cálculo nativo (PIS, COFINS, CSLL,
reforma tributária, ICMS efetivo, ICMS antecipado, FETHAB, FUST/FUNTTEL). A regra está
registrada em três fluxos: confirmação pela Central, aprovação e faturamento silencioso.
Retorno ignorado.

| Chave | Tipo | Descrição |
|---|---|---|
| `ctx` | `ContextoRegra` | Dá acesso a `getPrePersistEntityState()` e `getBarramentoRegra()` |
| `cabVO` | `DynamicVO` | Cabeçalho (TGFCAB) em pré-persistência |
| `nunota` | `BigDecimal` | Número único da nota |
| `impostosHelpper` | `br.com.sankhya.modelcore.comercial.impostos.ImpostosHelpper` | Helper já com a nota referenciada |
| `impostosViaProcedure` | `Boolean` | `true` quando `mge.calcular.impostos.via.procedure` está ligado e o cálculo nativo em Java foi pulado |

Existe outra classe `ImpostosHelpper` em `br.com.sankhya.mgecomercial.model.impostos`. O
cast para ela gera `ClassCastException`; importe a de `modelcore.comercial.impostos`.

Gravação na TGFDIN (entidade `ImpostoItemNota`, PK `NUNOTA, SEQUENCIA, CODIMP, CODINC`):

```java
BigDecimal nunota = (BigDecimal) data.get("nunota");
EntityFacade dwf = EntityFacadeFactory.getDWFFacade();

DynamicVO dinVO = (DynamicVO) dwf.getDefaultValueObjectInstance("ImpostoItemNota");
dinVO.setProperty("NUNOTA", nunota);
dinVO.setProperty("SEQUENCIA", sequenciaDoItem);
dinVO.setProperty("CODIMP", codImpostoCustomizado);
dinVO.setProperty("CODINC", codIncidencia);
dinVO.setProperty("BASE", base);
dinVO.setProperty("ALIQUOTA", aliquota);
dinVO.setProperty("VALOR", valor);
dwf.createEntity("ImpostoItemNota", (EntityVO) dinVO);
```

Cuidados:

- **`(NUNOTA, SEQUENCIA)` tem FK para a TGFITE.** O item precisa existir.
- **`CODIMP` não tem FK para a TGFIMP no banco.** A documentação da Sankhya pede que o
  código exista na TGFIMP; a base não impede gravar um código inexistente, então valide.
- **Verifique se o registro já existe antes do `createEntity`.** A regra roda em três
  fluxos (aprovação, confirmação, faturamento silencioso); se a mesma nota passar por mais
  de um, o segundo `createEntity` estoura a PK.
- **`DIGITADO = 'S'` protege o registro.** As rotinas nativas que removem ou atualizam
  TGFDIN filtram `DIGITADO <> 'S'`. O default da coluna é `'N'`.
- **O total da nota não é afetado** (segundo a documentação da Sankhya): o ajuste que soma a
  TGFDIN de volta para a TGFCAB só considera os `CODIMP` fixos e já rodou antes deste ponto.

**Quando não dispara:**

- O barramento tem liberações solicitadas (`getLiberacoesSolicitadas()` não vazio).
- Aprovação de nota que é cupom fiscal.

---

## Regras gerais

- **Exceção aborta a operação.** Qualquer exceção lançada no `call` sobe embrulhada em
  `IllegalStateException` com o código `CORE_E05913` e derruba a operação inteira (inclusão
  do item, cálculo do Flex, confirmação). Use isso para validação de negócio; trate dentro
  do `call` o que não deve abortar.
- **Transação.** Os callbacks `mgecom.*` rodam na transação corrente da operação: a gravação
  participa do mesmo commit ou rollback, e não se abre transação própria. A exceção
  conhecida é `central.processarConfirmacao.after`, que roda fora de transação.
- **Telemetria.** Cada execução é registrada na telemetria de customizações com a classe e o
  tempo gasto. Execução medida em 0 ms é descartada, então um callback muito rápido pode
  não aparecer.

## Erros

| Código | Causa |
|---|---|
| `CORE_E07912` | Parâmetro preenchido sem liberação da chave pela Sankhya |
| `CORE_E06556` | Classe do valor do parâmetro não encontrada no módulo |
| `CORE_E05913` | Exceção lançada dentro do callback (ou qualquer erro ao montar/executar) |

Callback que não executa e não gera erro: confira se o valor do parâmetro tem o `@`, se o
`NUMODULO` é o do módulo importado e se o caso cai em algum "Quando não dispara".
