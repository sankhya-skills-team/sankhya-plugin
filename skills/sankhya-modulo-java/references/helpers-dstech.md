# Helpers do Modelo DSTech — br.com.sankhya.dstech.helper

## Visão Geral

O projeto modelo `modelo-dstech-customizacoes` contém um conjunto de helpers transversais prontos
para uso em qualquer projeto. **Sempre verificar aqui antes de criar um helper do zero.**

Pacote: `br.com.sankhya.dstech.helper`

---

## CabecalhoNotaHelper

Operações sobre cabeçalho de notas (TGFCAB).

```java
import br.com.sankhya.dstech.helper.CabecalhoNotaHelper;
import br.com.sankhya.modelcore.dwfdata.vo.CabecalhoNotaVO;

// Buscar VO por NUNOTA (lança MGEModelException se não encontrado)
DynamicVO cabVO = CabecalhoNotaHelper.getVo(nuNota);

// Verificar se existe nota para um contrato
boolean existe = CabecalhoNotaHelper.existeNotaContrato(numContrato);

// Usar interface tipada com getters nativos do Sankhya
CabecalhoNotaVO cabTyped = CabecalhoNotaHelper.mapVoDwfData(cabVO);
// cabTyped.getCODPARC(), cabTyped.getTIPMOV(), etc.
```

---

## ItemNotaHelper

Operações sobre itens de nota (TGFITE).

```java
import br.com.sankhya.dstech.helper.ItemNotaHelper;
import br.com.sankhya.modelcore.dwfdata.vo.ItemNotaVO;

// Buscar item específico por nota + sequência (lança se não encontrado)
DynamicVO itemVO = ItemNotaHelper.getVo(nuNota, sequencia);

// Buscar todos os itens de uma nota (lança se vazio)
Collection<DynamicVO> itens = ItemNotaHelper.getVos(nuNota);

// Buscar itens de uma nota filtrando por produto
Collection<DynamicVO> itensProd = ItemNotaHelper.getVos(nuNota, codProd);

// Usar interface tipada
ItemNotaVO itemTyped = ItemNotaHelper.mapVoDwfData(itemVO);
```

---

## ParceiroHelper

Operações sobre parceiros (TGFPAR).

```java
import br.com.sankhya.dstech.helper.ParceiroHelper;

// Buscar VO de parceiro por código (lança se não encontrado)
DynamicVO parcVO = ParceiroHelper.getVO(codParc);

// Atualizar conta contábil (nroConta: 1 a 4)
ParceiroHelper.atualizaCtaCtb(codParc, codCtaCtb, 1);
```

---

## ProdutoHelper

Operações sobre produtos (TGFPRO).

```java
import br.com.sankhya.dstech.helper.ProdutoHelper;
import br.com.sankhya.modelcore.dwfdata.vo.ProdutoVO;

// Buscar VO do produto (lança se não encontrado)
DynamicVO prodVO = ProdutoHelper.getVO(codProd);

// Ativar/desativar produto
ProdutoHelper.ativarProduto(codProd);
ProdutoHelper.desativarProduto(codProd);

// Usar interface tipada
ProdutoVO prodTyped = ProdutoHelper.mapVoDwfData(prodVO);
```

---

## EmpresaHelper

Operações sobre empresas (TSIEMP).

```java
import br.com.sankhya.dstech.helper.EmpresaHelper;

// Buscar VO da empresa (retorna null se não encontrado)
DynamicVO empVO = EmpresaHelper.getVoEmpresa(codEmp);
```

---

## UsuarioHelper

Operações sobre usuários (TGFUSU).

```java
import br.com.sankhya.dstech.helper.UsuarioHelper;

// Buscar VO do usuário (lança MGEModelException se não encontrado)
DynamicVO usuVO = UsuarioHelper.getUserVO(codUsu);

// Combinar com AuthenticationInfo para buscar o usuário logado
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
BigDecimal codUsu = AuthenticationInfo.getCurrent().getUserID();
DynamicVO usuLogado = UsuarioHelper.getUserVO(codUsu);
String codGrupo = usuLogado.asString("CODGRUPO"); // verificar grupo do usuário
```

---

## TipoOperacaoHelper

Operações sobre tipos de operação (TGFTOP).

```java
import br.com.sankhya.dstech.helper.TipoOperacaoHelper;

// Buscar VO do tipo de operação mais recente (usa MAX(DHALTER))
DynamicVO topVO = TipoOperacaoHelper.getVoTipoOperacao(codTipOper);
```

---

## ContratoArmazemHelper

Operações sobre contratos de armazenagem (TCSCON).

```java
import br.com.sankhya.dstech.helper.ContratoArmazemHelper;

// Buscar VO do contrato por número (retorna null se não encontrado)
DynamicVO contratoVO = ContratoArmazemHelper.getVoContrato(numContrato);
```

---

## ConfirmarNotaHelper

Confirmar notas e verificar contextos de confirmação/faturamento.

> **Atenção:** Não usar em eventos ou regras de negócio. Apenas em Jobs/threads assíncronos.

```java
import br.com.sankhya.dstech.helper.ConfirmarNotaHelper;

// Confirmar nota via BarramentoRegra (silencioso)
ConfirmarNotaHelper.confirmarNota(nuNota);

// Confirmar nota via PlatformService
ConfirmarNotaHelper.confirmarNotaService(nuNota);

// Verificar contexto na JapeSession — útil em Regras de Negócio e Listeners
boolean confirmando = ConfirmarNotaHelper.isConfirmando();
boolean faturando   = ConfirmarNotaHelper.isFaturando();
boolean duplicando  = ConfirmarNotaHelper.isDuplicando();
```

### Constantes disponíveis

```java
ConfirmarNotaHelper.CENTRAL_CONFIRMANDO  // "CabecalhoNota.confirmando.nota"
ConfirmarNotaHelper.CENTRAL_FATURANDO    // "br.com.sankhya.mgecom.centralnotas.NotaFaturamento"
ConfirmarNotaHelper.CENTRAL_DUPLICATE    // "br.com.sankhya.devcenter.central.duplicate"
```

---

## LancarTelaHelper

Gera links HTML para abrir telas nativas do Sankhya com filtro pré-aplicado.
Útil para incluir em `setMensagemRetorno()` de botões de ação.

```java
import br.com.sankhya.dstech.helper.LancarTelaHelper;

// Link simples (filtro por NUNOTA)
String link = LancarTelaHelper.lancarTela(nuNota, LancarTelaHelper.Telas.CENTRAL);
ctx.setMensagemRetorno("Nota criada: " + link);

// Link com texto customizado (retorna "" se nu for null ou zero)
String link = LancarTelaHelper.lancarTelaCustom(
        LancarTelaHelper.Telas.CENTRAL, nuNota, "Abrir nota na central");

// Telas disponíveis no enum
LancarTelaHelper.Telas.CENTRAL         // Central de Notas
LancarTelaHelper.Telas.FINANCEIRO      // Movimentação Financeira
LancarTelaHelper.Telas.PORTALCOMPRAS   // Portal de Compras
LancarTelaHelper.Telas.PORTALVENDAS    // Seleção de Documento (vendas)
```

---

## DwfUtils (br.com.sankhya.dstech.utils)

Utilitário de consulta genérica. Detalhe importante: dois métodos similares com comportamentos distintos.

```java
import br.com.sankhya.dstech.utils.DwfUtils;

// findEntityAsVO — retorna o PRIMEIRO resultado ou NULL (nunca lança para vazio)
DynamicVO vo = DwfUtils.findEntityAsVO(
        "AD_NOMETABELA",
        "CAMPO = ?",
        new Object[]{valor});

// findEntitysAsVO — retorna Collection ou NULL se vazio (atenção: "Entitys" é o nome do método)
Collection<DynamicVO> vos = DwfUtils.findEntitysAsVO(
        DynamicEntityNames.ITEM_NOTA,
        "NUNOTA = ?",
        new Object[]{nuNota});

// findEntitiesAsVO — retorna List (NUNCA null — retorna lista vazia se não encontrar)
List<DynamicVO> lista = DwfUtils.findEntitiesAsVO(
        "AD_NOMETABELA",
        "STATUS = ?",
        new Object[]{"P"});

// findEntitiesAsVO — buscar tudo (sem filtro)
List<DynamicVO> todos = DwfUtils.findEntitiesAsVO("AD_NOMETABELA");

// execWithTx — executar bloco com JapeSession gerenciada
DwfUtils.execWithTx(() -> {
    // operações dentro de transação
    return true;
});
```

### Quando usar cada método

| Método | Retorno se vazio | Quando usar |
|---|---|---|
| `findEntityAsVO` | `null` | Buscar um registro único, testar existência |
| `findEntitysAsVO` | `null` | Coleção — verificar null antes de iterar |
| `findEntitiesAsVO` | `ArrayList` vazio | Coleção — nunca null, pode usar `isEmpty()` diretamente |

---

## MessageUtils (br.com.sankhya.dstech.utils)

Exibe mensagem informativa ao usuário via `ServiceContext`. Usado em Regras de Negócio.

```java
import br.com.sankhya.dstech.utils.MessageUtils;

MessageUtils.showInfo("Operação realizada com sucesso.");

// Dentro de RegraNegocioJava.executa():
ctx.setMensagem(msgError);
MessageUtils.showInfo(msgError);
```

---

## EnviaEmailHelper

Insere e-mail na fila de envio do Sankhya (TMDFMG / `DynamicEntityNames.FILA_MSG`).

```java
import br.com.sankhya.dstech.helper.EnviaEmailHelper;

// Sem servidor SMTP específico
EnviaEmailHelper.insereEmail(
        corpoHtml.toCharArray(),  // mensagem em HTML
        new BigDecimal(3),        // máximo de tentativas de envio
        "Assunto do e-mail",
        "destino@email.com",
        codUsuario);              // CODUSU do remetente

// Com servidor SMTP específico
EnviaEmailHelper.insereEmail(
        corpoHtml.toCharArray(),
        new BigDecimal(3),
        "Assunto",
        "destino@email.com",
        codUsuario,
        codSMTP);                 // código do servidor SMTP (TMESMTP)
```

---

## CotacaoMoedaHelper

Operações sobre cotações de moeda (TGFMOE).

```java
import br.com.sankhya.dstech.helper.CotacaoMoedaHelper;

// Buscar VO de cotação por PK (retorna null se não encontrado)
DynamicVO cotVO = CotacaoMoedaHelper.getVo(codCotacao);

// Verificar se existe cotação para uma moeda
boolean temCotacao = CotacaoMoedaHelper.temCotacao(codMoeda);
```

---

## LancarRelatorioHelper

Cria arquivo em sessão temporária e gera link HTML para visualização/download.
Útil para retornar PDFs, planilhas e outros arquivos em botões de ação.

```java
import br.com.sankhya.dstech.helper.LancarRelatorioHelper;
import java.io.File;

// Lançar arquivo detectando MIME automaticamente
File arquivo = new File("/caminho/relatorio.pdf");
String link = LancarRelatorioHelper.lancarRelatorio(arquivo, "relatorio.pdf");
ctx.setMensagemRetorno(link);

// Lançar com MIME explícito
String link = LancarRelatorioHelper.lancarRelatorio(arquivo, "relatorio.pdf",
        LancarRelatorioHelper.MimeType.PDF.getMimeType());

// MimeType enum — extensões disponíveis
LancarRelatorioHelper.MimeType.PDF    // application/pdf
LancarRelatorioHelper.MimeType.XLSX   // application/vnd.openxmlformats...
LancarRelatorioHelper.MimeType.CSV    // text/csv
LancarRelatorioHelper.MimeType.XML    // application/xml
// ... ver enum completo: PDF, TXT, CSV, XML, JSON, JPG, PNG, DOC, DOCX, XLS, XLSX, ZIP
```

---

## ImpostoItemNotaHelper

Busca impostos de item de nota (TGFIMP) por múltiplas chaves.

```java
import br.com.sankhya.dstech.helper.ImpostoItemNotaHelper;

// Busca imposto específico (lança se não encontrado)
DynamicVO impVO = ImpostoItemNotaHelper.getVO(nuNota, sequencia, codImp, codInc);

// Busca todos os impostos de um item (lança se vazio)
Collection<DynamicVO> impostos = ImpostoItemNotaHelper.getVOs(nuNota, sequencia);
```

---

## ServicoHelper

Operações sobre serviços (TGFPRO com `USOPROD = 'S'`).
Mesmo padrão do `ProdutoHelper`, mas filtra apenas registros de serviço.

```java
import br.com.sankhya.dstech.helper.ServicoHelper;

// Buscar VO do serviço (lança se não encontrado)
DynamicVO servVO = ServicoHelper.getVO(codProd);

// Ativar/desativar serviço
ServicoHelper.ativarProduto(codProd);
ServicoHelper.desativarProduto(codProd);
```

---

## ItemComposicaoProdutoHelper

Operações sobre composição de kit/produto (TGFICP).

```java
import br.com.sankhya.dstech.helper.ItemComposicaoProdutoHelper;

// Buscar todos os componentes de um kit pelo produto pai
Collection<DynamicVO> componentes = ItemComposicaoProdutoHelper.getItensDoKit(codProd);
if (componentes.isEmpty()) {
    // produto não é kit ou não tem componentes
}
```

---

## CompraVendaVariosPedidoHelper

Insere registros de variação (TGFVAR) vinculando nota de origem a nova nota.
Usado em fluxos de compra/venda com vários pedidos.

```java
import br.com.sankhya.dstech.helper.CompraVendaVariosPedidoHelper;

// Copia itens da nota de origem para TGFVAR relacionando com a nova nota
CompraVendaVariosPedidoHelper.incluirVAR(nunotaOrig, nunotaNova);
```

> **Atenção:** Usa `NativeSql` com INSERT direto — executa fora de JapeSession.
> Chamar apenas de Botão de Ação ou Job agendado, nunca de dentro de evento.

---

## wrapInterface — Interface Tipada (DynamicVO → VO nativo)

Permite usar os getters nativos do Sankhya em vez de `asBigDecimal("CAMPO")`.
Disponível nos helpers `mapVoDwfData()`.

```java
import br.com.sankhya.modelcore.dwfdata.vo.CabecalhoNotaVO;
import br.com.sankhya.modelcore.dwfdata.vo.ItemNotaVO;
import br.com.sankhya.modelcore.dwfdata.vo.ProdutoVO;

// Usar interface tipada
CabecalhoNotaVO cab = CabecalhoNotaHelper.mapVoDwfData(cabVO);
String tipMov  = cab.getTIPMOV();
BigDecimal codParc = cab.getCODPARC();

ItemNotaVO item = ItemNotaHelper.mapVoDwfData(itemVO);
BigDecimal vlrUnit = item.getVLRUNIT();

// Ou diretamente via wrapInterface
CabecalhoNotaVO cab = (CabecalhoNotaVO) ((DynamicVO) dynVO).wrapInterface(CabecalhoNotaVO.class);
```
