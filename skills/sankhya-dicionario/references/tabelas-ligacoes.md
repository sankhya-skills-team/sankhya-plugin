# Ligações Lógicas e Instâncias Sankhya (TDDLIG + TDDINS + TDDLGC)

Este arquivo documenta o **modelo de navegação lógica** do Sankhya OM.

## Por que isso importa para desenvolvimento Java

- **`TDDINS.NOMEINSTANCIA`** é o `entityName` usado em `JapeFactory.dao("NomeInstancia")`
- **`TDDLIG`** define como telas navegam entre si (não apenas FKs físicas)
- **`TDDLGC`** define os campos exatos que formam cada join
- Uma mesma tabela pode ter **múltiplas instâncias** com papéis diferentes
  (ex: `TGFPAR` aparece como `Parceiro`, `TransportadoraFinal`, `ParceiroRetirada`)

## Tipos de Ligação (`TIPLIGACAO`)

| Código | Tipo | Significado |
|---|---|---|
| `I` | inner | Ligação mestre-detalhe (detalhe pertence ao mestre) |
| `L` | lookup | Chave estrangeira / referência (lookup) |

## Mapeamento Global: Tabela → Instâncias

> Instâncias são os entityNames usados em `JapeFactory.dao()`, `DwfUtils`, `EntityFacade`.

```java
// Exemplos de entityNames mais usados:
JapeFactory.dao("CabecalhoFox")  // TGFCAB — Nota venda do Checkout
JapeFactory.dao("CabecalhoNota")  // TGFCAB — Nota/Pedido
JapeFactory.dao("CabecalhoNota2")  // TGFCAB — Nota/Pedido
JapeFactory.dao("ItemNota")  // TGFITE — Item Nota/Pedido
JapeFactory.dao("ItemNotaOrigem")  // TGFITE — Item da Nota de Origem
JapeFactory.dao("ItensFox")  // TGFITE — Item da Nota de Checkout
JapeFactory.dao("Financeiro")  // TGFFIN — Financeiro
JapeFactory.dao("TimFinanceiro")  // TGFFIN — Financeiro
JapeFactory.dao("TimFinanceiroAluguel")  // TGFFIN — Financeiro Aluguel
JapeFactory.dao("FuncionarioTomador")  // TGFPAR — Funcionario Tomador
JapeFactory.dao("GrupoEconomico")  // TGFPAR — Grupo Economico
JapeFactory.dao("Motorista")  // TGFPAR — Motorista do Veiculo
JapeFactory.dao("Produto")  // TGFPRO — Produto
JapeFactory.dao("Produto3")  // TGFPRO — Produto
JapeFactory.dao("ProdutoApontamento1")  // TGFPRO — Produto/servico para agrupar apontamento 1
JapeFactory.dao("EmpresaFinanceiro")  // TGFEMP — Empresa Financeiro
JapeFactory.dao("TOPDespesa")  // TGFTOP — TOPDespesa
JapeFactory.dao("TOPReceita")  // TGFTOP — TOPReceita
JapeFactory.dao("TipoOperacao")  // TGFTOP — Tipo de Operação
JapeFactory.dao("Natureza")  // TGFNAT — Natureza
JapeFactory.dao("Natureza2")  // TGFNAT — Natureza2
JapeFactory.dao("Natureza3")  // TGFNAT — Natureza3
JapeFactory.dao("Assessor")  // TGFVEN — Assessor
JapeFactory.dao("Gerente")  // TGFVEN — Gerente
JapeFactory.dao("Vendedor")  // TGFVEN — Vendedor
JapeFactory.dao("Contato")  // TGFCTT — Contato
JapeFactory.dao("ContatoEntrega")  // TGFCTT — Contato de Entrega
JapeFactory.dao("LocalBaixaMPProducao")  // TGFLOC — Local de Baixa de MP
JapeFactory.dao("LocalDestinoPerda")  // TGFLOC — LocalDestinoPerda
JapeFactory.dao("LocalDestinoProducao")  // TGFLOC — Local de Destino  do Produção
JapeFactory.dao("UndPrincipalTgwexp")  // TGFVOL — Unidade Principal
JapeFactory.dao("UnidadeCompra")  // TGFVOL — Unidade para compras
JapeFactory.dao("UnidadeMinArmazenagemWMS")  // TGFVOL — Unidade Minima de Armazenagem para WMS
JapeFactory.dao("Estoque")  // TGFEST — Estoque
JapeFactory.dao("OrdemCarga")  // TGFORD — Ordem de Carga
JapeFactory.dao("EspecieTitulo")  // TGFTIT — Especie do Tipo de Titulo
JapeFactory.dao("TipoTitulo")  // TGFTIT — Tipo de Titulo
JapeFactory.dao("TipoTituloArm")  // TGFTIT — Tipos de Titulo Armazenagem
JapeFactory.dao("GrupoProduto")  // TGFGRU — Grupo Produto
JapeFactory.dao("GrupoProduto2")  // TGFGRU — Grupo Produto
JapeFactory.dao("GrupoProduto3")  // TGFGRU — GrupoProduto3
JapeFactory.dao("FamiliaProduto")  // TGFFAM — Familia
JapeFactory.dao("TabelaPreco")  // TGFTAB — Tabela de Preco
JapeFactory.dao("TabelaPrecoMinimo")  // TGFTAB — Tabela de Preco Minimo
JapeFactory.dao("TabelaPrecoPF")  // TGFTAB — Tabela de Preco
JapeFactory.dao("NomeTabelasPreco")  // TGFNTA — Cadastro de Tabela de Preco
JapeFactory.dao("NomeTabelasPrecoFarPop")  // TGFNTA — Nome das Tabelas de Preco
JapeFactory.dao("NomeTabelasPrecoFilha")  // TGFNTA — Nome das Tabelas de Preco
JapeFactory.dao("Veiculo")  // TGFVEI — Veiculos
JapeFactory.dao("VeiculoReboque1")  // TGFVEI — Veiculo Reboque
JapeFactory.dao("VeiculoReboque2")  // TGFVEI — Veiculo Reboque2
JapeFactory.dao("ClaFiscalCombustivelLubrif")  // TGFCFO — Classificação Fiscal Operações Para Combustiveis e Lubrificantes
JapeFactory.dao("ClaFiscalOperacaoEntrada")  // TGFCFO — Classificação Fiscal de Operações Entrada
JapeFactory.dao("ClaFiscalOperacaoEntradaEstado")  // TGFCFO — Classificação Fiscal de Operações de Entrada de Fora do Estado.
JapeFactory.dao("AliquotaISS")  // TGFISS — Aliquotas de ISS
JapeFactory.dao("GrupoCobranca")  // TGFGCB — Grupo Cobranca
JapeFactory.dao("Atendente")  // TSIUSU — Atendente
JapeFactory.dao("Executante")  // TSIUSU — Executante
JapeFactory.dao("ExecutanteRemetente")  // TSIUSU — Executante Remetente
JapeFactory.dao("Empresa")  // TSIEMP — Empresa
JapeFactory.dao("EmpresaBaixa")  // TSIEMP — Empresa para baixa
JapeFactory.dao("EmpresaCadastro")  // TSIEMP — Cadastro de Empresas
JapeFactory.dao("ContaBancaria")  // TSICTA — Conta Bancaria
JapeFactory.dao("ContaBancariaDespesa")  // TSICTA — Contas Bancarias para Despesas
JapeFactory.dao("ContaBancariaIpi")  // TSICTA — Conta Bancaria
JapeFactory.dao("CentroResultado")  // TSICUS — Centro de Resultado
JapeFactory.dao("CentroResultadoArm")  // TSICUS — Centros de Resultado Armazenagem
JapeFactory.dao("CentroResultadoDespesa")  // TSICUS — Centro de Resultado Despesa
JapeFactory.dao("Cidade")  // TSICID — Cidade
JapeFactory.dao("CidadeDestino")  // TSICID — Cidade de Destino
JapeFactory.dao("CidadeFatoGerador")  // TSICID — Municipio do Fato Gerador
JapeFactory.dao("UnidadeFederativa")  // TSIUFS — Unidade Federativa
JapeFactory.dao("UnidadeFederativaDestino")  // TSIUFS — Unidade Federativa Destino
JapeFactory.dao("UnidadeFederativaEmissao")  // TSIUFS — Unidade Federativa Emissão
JapeFactory.dao("Banco")  // TSIBCO — Banco
JapeFactory.dao("BancoIpi")  // TSIBCO — Banco
JapeFactory.dao("CorrespondenteBancario")  // TSIBCO — Correspondente Bancario
JapeFactory.dao("Bairro")  // TSIBAI — Bairro
JapeFactory.dao("BairroRecebimento")  // TSIBAI — Bairro para recebimento
JapeFactory.dao("BairroTrabalho")  // TSIBAI — Bairro Trabalho
JapeFactory.dao("Endereco")  // TSIEND — Endereco
JapeFactory.dao("EnderecoRecebimento")  // TSIEND — Endereco de Recebimento
JapeFactory.dao("EnderecoTrabalho")  // TSIEND — Endereco de Trabalho
```

## Ligações por Tabela

### TGFCAB

**Instâncias (entityName para JapeFactory):**
- `CabecalhoFox` — Nota venda do Checkout
- `CabecalhoNota` — Nota/Pedido
- `CabecalhoNota2` — Nota/Pedido
- `CabecalhoNota3` — Nota/Pedido
- `CabecalhoNotaBaixa` — Nota de Baixa
- `CabecalhoNotaDevVenda` — Nota Devolução Venda
- `CabecalhoNotaModelo` — Cabecalho Nota Modelo
- `CabecalhoNotaModeloAgenda` — Modelo de Notas e Pedidos
- `CabecalhoNotaModeloSaida` — Modelo de nota de saida
- `CabecalhoNotaModeloSaidaBem` — Modelo de nota de saida Bem
- `CabecalhoNotaRetorno` — Nota Retorno
- `CabecalhoNotaSaida` — Nota de Saida
- `CabecalhoNotaWmsEnt` — Nota modelo sobra estoque WMS (Entrada)
- `CabecalhoNotaWmsSai` — Nota modelo perda estoque WMS (Saida)
- `CabecalhoNotaModelo2` — CabecalhoNotaModelo2
- `ModeloEntradaEstoqueComTerc` — Modelo Ajuste de Entrada de Estoque com Terceiros
- `ModeloEntradaEstoqueConsignado` — Modelo Ajuste de Entrada de Estoque Consignado
- `ModeloEntradaEstoqueDeTerc` — Modelo Ajuste de Entrada de Estoque de Terceiros
- `ModeloEntradaReclassificacao` — Modelo Ajuste de Entrada Reclassificação (Registro K220)
- `ModeloEstornoWMSDevCompra` — Modelo Estorno WMS - Dev Compra
- `ModeloRetornoEstoqueWMS` — Modelo Retor. de Est. Gerencial WMS(Venda)
- `ModeloSaidaEstoqueComTerc` — Modelo Ajuste de Saida de Estoque com Terceiros
- `ModeloSaidaEstoqueConsignado` — Modelo Ajuste de Saida de Estoque Consignado
- `ModeloSaidaEstoqueDeTerc` — Modelo Ajuste de Saida de Estoque de Terceiros
- `ModeloSaidaReclassificacao` — Modelo Ajuste de Saida Reclassificação (Registro K220)

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `CabecalhoNota` | `TCSCON` | `Contrato` | inner (filha) | N | — |
| `CabecalhoNota` | `TCSOSE` | `OrdemServico` | inner (filha) | S | — |
| `CabecalhoNota` | `TCSPRJ` | `Projeto` | inner (filha) | S | — |
| `CabecalhoNota` | `TFPFUN` | `Funcionario` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFACH` | `AcertoOrdemCargaHist` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFACT` | `AcompanhamentoNota` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFCAB` | `CabecalhoNota` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFCCM` | `ComissaoMultipla` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFCFO` | `ClassificacaoFiscalOperacao` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFCFR` | `TabelaCalculoFrete` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFCGTVE` | `ComplementosGTVE` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFCMN` | `ControleMultimodal` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFCOM` | `ValorComissaoVendedor` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFCON2` | `CabecalhoConferencia` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFCONT` | `ContainerCTe` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFCTT` | `Contato` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFCTT` | `ContatoEntrega` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFDANT` | `DocumentoAnterior` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFDFAGR` | `DefensivosAgricolas` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFDFN` | `DescontoFinanceiro` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFFIN` | `Financeiro` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFFOP` | `FinalidadeOperacao` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFIGTVE` | `InformacoesGTVE` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFITE` | `ItemNota` | inner (filha) | S | INSERT, UPDATE |
| `CabecalhoNota` | `TGFLACR` | `LacreCTe` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFLNF` | `LoteNotaFiscalEletronica` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFMOT` | `MotoristaCTe` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFNCE` | `ColetaEntregaPorNota` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFNCT` | `NotaConhecimentoTransporte` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFNCTE` | `ArquivoCTe` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFOBS` | `ObservacaoNotasFiscais` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFODP` | `OrdemDespacho` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFORD` | `OrdemCarga` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroRedespacho` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroConsignatario` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroRemetente` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroDestino` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFPAR` | `Motorista` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFPAR` | `Transportadora` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroIntermed` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroDescargaMdfe` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFPAR` | `TransportadoraFinal` | lookup (chave estrangeira) | N | — |
| `CabecalhoNota` | `TGFPAR` | `ParceiroRetirada` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFREFIMP` | `ImpostosReformaTrib` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFSEG` | `SeguroTransporte` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFSFP` | `SimulacaoFormaPagamento` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFTOP` | `TipoOperacao` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFTPD` | `TipoPedido` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFTPV` | `TipoNegociacao` | inner (filha) | S | INSERT |
| `CabecalhoNota` | `TGFUNM` | `UnidadeMedida` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFUTR` | `UnidadeTransporte` | inner (filha) | S | — |
| `CabecalhoNota` | `TGFVALP` | `ValePedagio` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFVEI` | `VeiculoReboque3` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFVEI` | `VeiculoReboque1` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFVEI` | `VeiculoReboque2` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFVEI` | `Veiculo` | inner (filha) | N | — |
| `CabecalhoNota` | `TGFVEN` | `Vendedor` | lookup (chave estrangeira) | S | — |
| `CabecalhoNota` | `TGFVTP` | `ViaTransporte` | inner (filha) | N | — |
| `CabecalhoNota` | `TIMCLA` | `TimContratoVenda` | inner (filha) | S | — |
| `CabecalhoNota` | `TIMLTV` | `TimContratoVendaLote` | inner (filha) | S | — |
| `CabecalhoNota` | `TSICID` | `CidadeTrabalho` | inner (filha) | N | — |
| `CabecalhoNota` | `TSICID` | `CidadeDestino` | inner (filha) | S | — |
| `CabecalhoNota` | `TSICID` | `CidadeFatoGerador` | inner (filha) | S | — |
| `CabecalhoNota` | `TSICID` | `Cidade` | inner (filha) | N | — |
| `CabecalhoNota` | `TSICID` | `CidadeOrigem` | inner (filha) | S | — |
| `CabecalhoNota` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `CabecalhoNota` | `TSIEMP` | `EmpresaNegociacao` | inner (filha) | N | — |
| `CabecalhoNota` | `TSIEMP` | `Empresa` | inner (filha) | N | — |
| `CabecalhoNota` | `TSIEMP` | `EmpresaFuncionario` | inner (filha) | N | — |
| `CabecalhoNota` | `TSIMOE` | `Moeda` | inner (filha) | N | — |
| `CabecalhoNota` | `TSIUFS` | `UnidadeFederativaEmissao` | inner (filha) | S | — |
| `CabecalhoNota` | `TSIUFS` | `UnidadeFederativa` | inner (filha) | N | — |
| `CabecalhoNota` | `TSIUSU` | `Usuario` | inner (filha) | S | — |
| `CabecalhoNota` | `TSIUSU` | `Usuario2` | inner (filha) | N | — |
| `CabecalhoNota3` | `TGFTOP` | `TipoOperacao3` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TCSCON` | `Contrato` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TCSOSE` | `OrdemServico` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TFPFUN` | `Funcionario` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TGFCTT` | `Contato` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TGFORD` | `OrdemCarga` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `Transportadora` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `ParceiroConsignatario` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `ParceiroDestino` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `Motorista` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `ParceiroRedespacho` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFPAR` | `ParceiroRemetente` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFTOP` | `TipoOperacao` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TGFTPV` | `TipoNegociacao` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TGFVEI` | `Veiculo` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TGFVEN` | `Vendedor` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TSICID` | `Cidade` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TSICID` | `CidadeTrabalho` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TSICID` | `CidadeDestino` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TSICID` | `CidadeOrigem` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `CabecalhoNotaModelo` | `TSIEMP` | `EmpresaFuncionario` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TSIEMP` | `EmpresaNegociacao` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TSIEMP` | `Empresa` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TSIMOE` | `Moeda` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TSIUSU` | `Usuario2` | inner (filha) | N | — |
| `CabecalhoNotaModelo` | `TSIUSU` | `Usuario` | inner (filha) | S | — |

  > `CabecalhoNota` → `Contrato`: `NUMCONTRATO` → `NUMCONTRATO`
  > `CabecalhoNota` → `OrdemServico`: `NUMOS` → `NUMOS`
  > `CabecalhoNota` → `Projeto`: `CODPROJ` → `CODPROJ`
  > `CabecalhoNota` → `Funcionario`: `CODEMPFUNC` → `CODEMP`, `CODFUNC` → `CODFUNC`
  > `CabecalhoNota` → `AcertoOrdemCargaHist`: `CODHISTAC` → `CODHIST`
  > `CabecalhoNota` → `AcompanhamentoNota`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `CabecalhoNota`: `NUNOTASUB` → `NUNOTA`
  > `CabecalhoNota` → `ComissaoMultipla`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `ClassificacaoFiscalOperacao`: `CODCFO` → `CODCFO`
  > `CabecalhoNota` → `TabelaCalculoFrete`: `NUCFR` → `NUCFR`
  > `CabecalhoNota` → `ComplementosGTVE`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `ControleMultimodal`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `ValorComissaoVendedor`: `NUNOTA` → `NUNOTAORIG`
  > `CabecalhoNota` → `CabecalhoConferencia`: `NUCONFATUAL` → `NUCONF`
  > `CabecalhoNota` → `ContainerCTe`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `Contato`: `CODPARC` → `CODPARC`, `CODCONTATO` → `CODCONTATO`
  > `CabecalhoNota` → `ContatoEntrega`: `CODPARC` → `CODPARC`, `CODCONTATOENTREGA` → `CODCONTATO`
  > `CabecalhoNota` → `DocumentoAnterior`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `DefensivosAgricolas`: `NUNOTA` → `NUNOTA`
  > `CabecalhoNota` → `DescontoFinanceiro`: `NUNOTA` → `NUNOTA`

### TGFITE

**Instâncias (entityName para JapeFactory):**
- `ItemNota` — Item Nota/Pedido
- `ItemNotaOrigem` — Item da Nota de Origem
- `ItensFox` — Item da Nota de Checkout

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `ItemNota` | `TGFCAB` | `CabecalhoNota` | inner (filha) | N | — |
| `ItemNota` | `TGFCTD` | `CustoDevolucao` | inner (filha) | N | INSERT |
| `ItemNota` | `TGFCUSITE` | `CustoItem` | inner (filha) | S | — |
| `ItemNota` | `TGFDTP` | `PrevisaoEntrega` | inner (filha) | N | INSERT, UPDATE, DELETE |
| `ItemNota` | `TGFFOP` | `FinalidadeOperacao` | inner (filha) | S | — |
| `ItemNota` | `TGFHIP` | `HistoricoItemPendente` | inner (filha) | N | — |
| `ItemNota` | `TGFICM` | `AliquotaICMS` | inner (filha) | N | — |
| `ItemNota` | `TGFIII` | `ImpostosImportacao` | inner (filha) | N | — |
| `ItemNota` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | N | — |
| `ItemNota` | `TGFLOC` | `LocalFinanceiroEntDest` | inner (filha) | N | — |
| `ItemNota` | `TGFNRR` | `CadastroNaturezaRendimentos` | inner (filha) | S | — |
| `ItemNota` | `TGFPRO` | `Produto` | inner (filha) | S | — |
| `ItemNota` | `TGFVEN` | `Vendedor` | inner (filha) | N | — |
| `ItemNota` | `TGFVOL` | `Volume` | inner (filha) | N | — |
| `ItemNota` | `TGWEND` | `EnderecoArmazenagem` | inner (filha) | S | — |
| `ItemNota` | `TSIEMP` | `Empresa` | inner (filha) | N | — |

  > `ItemNota` → `CabecalhoNota`: `NUNOTA` → `NUNOTA`
  > `ItemNota` → `CustoDevolucao`: `NUNOTA` → `NUNOTA`, `SEQUENCIA` → `SEQUENCIA`
  > `ItemNota` → `CustoItem`: `CODPROD` → `CODPROD`, `NUNOTA` → `NUNOTA`, `SEQUENCIA` → `SEQUENCIA`
  > `ItemNota` → `PrevisaoEntrega`: `SEQUENCIA` → `SEQUENCIA`, `NUNOTA` → `NUNOTA`
  > `ItemNota` → `FinalidadeOperacao`: `NUFOP` → `NUFOP`
  > `ItemNota` → `HistoricoItemPendente`: `NUNOTA` → `NUNOTA`, `SEQUENCIA` → `SEQUENCIA`
  > `ItemNota` → `AliquotaICMS`: `IDALIQICMS` → `IDALIQ`
  > `ItemNota` → `ImpostosImportacao`: `NUNOTA` → `NUNOTA`, `SEQUENCIA` → `SEQUENCIA`
  > `ItemNota` → `LocalFinanceiro`: `CODLOCALORIG` → `CODLOCAL`
  > `ItemNota` → `LocalFinanceiroEntDest`: `CODLOCALDEST` → `CODLOCAL`
  > `ItemNota` → `CadastroNaturezaRendimentos`: `CODNATREND` → `CODNATREND`
  > `ItemNota` → `Produto`: `CODPROD` → `CODPROD`
  > `ItemNota` → `Vendedor`: `CODVEND` → `CODVEND`
  > `ItemNota` → `Volume`: `CODVOL` → `CODVOL`
  > `ItemNota` → `EnderecoArmazenagem`: `CODEND` → `CODEND`
  > `ItemNota` → `Empresa`: `CODEMP` → `CODEMP`

### TGFFIN

**Instâncias (entityName para JapeFactory):**
- `Financeiro` — Financeiro
- `TimFinanceiro` — Financeiro
- `TimFinanceiroAluguel` — Financeiro Aluguel
- `TimFinanceiroRepasse` — Financeiro Repasse

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Financeiro` | `TCSCON` | `Contrato` | inner (filha) | S | — |
| `Financeiro` | `TCSPRJ` | `Projeto` | inner (filha) | S | — |
| `Financeiro` | `TFPFUN` | `Funcionario` | inner (filha) | N | — |
| `Financeiro` | `TGFACH` | `AcertoOrdemCargaHist` | inner (filha) | N | — |
| `Financeiro` | `TGFANB` | `AntecipacaoRecebiveis` | inner (filha) | S | — |
| `Financeiro` | `TGFCAB` | `CabecalhoNota` | inner (filha) | N | — |
| `Financeiro` | `TGFCCR` | `CartaoCredito` | inner (filha) | N | — |
| `Financeiro` | `TGFCFO` | `ClassificacaoFiscalOperacao` | inner (filha) | S | — |
| `Financeiro` | `TGFCTT` | `Contato` | inner (filha) | N | — |
| `Financeiro` | `TGFFIN` | `TimFinanceiroRepasse` | inner (filha) | S | — |
| `Financeiro` | `TGFFTC` | `FaturaCartao` | inner (filha) | N | — |
| `Financeiro` | `TGFIMF` | `ImpostoFinanceiro` | inner (filha) | S | INSERT, UPDATE |
| `Financeiro` | `TGFLST` | `ListaServicoSintegra` | inner (filha) | S | — |
| `Financeiro` | `TGFMBC` | `MovimentoBancario` | inner (filha) | S | — |
| `Financeiro` | `TGFNAT` | `Natureza` | inner (filha) | N | — |
| `Financeiro` | `TGFOBS` | `ObservacaoNotasFiscais` | inner (filha) | S | — |
| `Financeiro` | `TGFORD` | `OrdemCarga` | inner (filha) | S | — |
| `Financeiro` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Financeiro` | `TGFPJB` | `BoletoRapido` | inner (filha) | S | — |
| `Financeiro` | `TGFRAT` | `RateioRecDesp` | inner (filha) | S | INSERT, UPDATE, DELETE |
| `Financeiro` | `TGFRAV` | `RateioVeiculo` | inner (filha) | S | INSERT, UPDATE, DELETE |
| `Financeiro` | `TGFRDARF` | `ReceitaDarf` | inner (filha) | S | — |
| `Financeiro` | `TGFREN` | `Renegociacao` | inner (filha) | N | DELETE |
| `Financeiro` | `TGFRNF` | `CompFinancReinf` | inner (filha) | S | INSERT, UPDATE, DELETE |
| `Financeiro` | `TGFTIT` | `TipoTitulo` | inner (filha) | S | — |
| `Financeiro` | `TGFTOP` | `TipoOperacaoBaixa` | inner (filha) | S | — |
| `Financeiro` | `TGFTOP` | `TipoOperacao` | inner (filha) | S | — |
| `Financeiro` | `TGFVEI` | `Veiculo` | inner (filha) | S | — |
| `Financeiro` | `TGFVEN` | `Vendedor` | inner (filha) | S | — |
| `Financeiro` | `TIMADM` | `TimContratoAdm` | inner (filha) | S | — |
| `Financeiro` | `TIMDLV` | `TimRescisao` | inner (filha) | S | — |
| `Financeiro` | `TIMDTL` | `TimDetalhamento` | inner (filha) | S | — |
| `Financeiro` | `TIMFEI` | `TimFechamentoItens` | inner (filha) | S | — |
| `Financeiro` | `TIMIMV` | `TimImovel` | inner (filha) | S | — |
| `Financeiro` | `TIMIPT` | `TimIptu` | inner (filha) | S | — |
| `Financeiro` | `TIMLCR` | `TimNegociacao` | inner (filha) | S | — |
| `Financeiro` | `TIMLDT` | `TimDetalhamentoLoteamento` | inner (filha) | S | — |
| `Financeiro` | `TIMLOC` | `TimLocacao` | inner (filha) | S | — |
| `Financeiro` | `TIMLTV` | `TimContratoVendaLote` | inner (filha) | S | — |
| `Financeiro` | `TIMLVR` | `TimRenegociacao` | inner (filha) | S | — |
| `Financeiro` | `TIMREC` | `TimRescisaoLoc` | inner (filha) | S | — |
| `Financeiro` | `TIMTIN` | `TimTipoIntermed` | inner (filha) | S | — |
| `Financeiro` | `TSIBCO` | `Banco` | inner (filha) | S | — |
| `Financeiro` | `TSICID` | `CidadeDestino` | inner (filha) | S | — |
| `Financeiro` | `TSICID` | `CidadeOrigem` | inner (filha) | S | — |
| `Financeiro` | `TSICTA` | `TimContaBancaria` | inner (filha) | S | — |
| `Financeiro` | `TSICTA` | `ContaBancaria` | inner (filha) | S | — |
| `Financeiro` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `Financeiro` | `TSIEMP` | `EmpresaBaixa` | inner (filha) | S | — |
| `Financeiro` | `TSIEMP` | `ImovelRural` | inner (filha) | S | — |
| `Financeiro` | `TSIEMP` | `Empresa` | inner (filha) | S | — |
| `Financeiro` | `TSILIB` | `LiberacaoLimite` | inner (filha) | N | — |
| `Financeiro` | `TSIMOE` | `Moeda` | inner (filha) | S | — |
| `Financeiro` | `TSIUSU` | `Usuario2` | inner (filha) | S | — |
| `Financeiro` | `TSIUSU` | `UsuarioBaixa` | inner (filha) | S | — |
| `Financeiro` | `TSIUSU` | `Usuario` | inner (filha) | S | — |
| `TimFinanceiroAluguel` | `TIMDTL` | `TimDetalhamento` | inner (filha) | S | — |
| `TimFinanceiroAluguel` | `TIMLCR` | `TimNegociacao` | inner (filha) | S | — |
| `TimFinanceiroAluguel` | `TIMLOC` | `TimLocacao` | inner (filha) | S | — |
| `TimFinanceiroRepasse` | `TGFFIN` | `Financeiro` | inner (filha) | S | — |
| `TimFinanceiroRepasse` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `TimFinanceiroRepasse` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |

  > `Financeiro` → `Contrato`: `NUMCONTRATO` → `NUMCONTRATO`
  > `Financeiro` → `Projeto`: `CODPROJ` → `CODPROJ`
  > `Financeiro` → `Funcionario`: `CODFUNC` → `CODFUNC`, `CODEMP` → `CODEMP`
  > `Financeiro` → `AcertoOrdemCargaHist`: `CODHISTAC` → `CODHIST`
  > `Financeiro` → `AntecipacaoRecebiveis`: `NUFIN` → `NUFINTITORI`
  > `Financeiro` → `CabecalhoNota`: `NUNOTA` → `NUNOTA`
  > `Financeiro` → `CartaoCredito`: `NUCCR` → `NUCCR`
  > `Financeiro` → `ClassificacaoFiscalOperacao`: `CODCFO` → `CODCFO`
  > `Financeiro` → `Contato`: `CODCONTATO` → `CODCONTATO`, `CODPARC` → `CODPARC`
  > `Financeiro` → `TimFinanceiroRepasse`: `NUFIN` → `TIMNUFINORIG`
  > `Financeiro` → `FaturaCartao`: `NUFTC` → `NUFTC`
  > `Financeiro` → `ImpostoFinanceiro`: `NUFIN` → `NUFIN`
  > `Financeiro` → `ListaServicoSintegra`: `CODLST` → `CODLST`
  > `Financeiro` → `MovimentoBancario`: `NUBCO` → `NUBCO`
  > `Financeiro` → `Natureza`: `CODNAT` → `CODNAT`
  > `Financeiro` → `ObservacaoNotasFiscais`: `CODOBSPADRAO` → `CODOBSPADRAO`
  > `Financeiro` → `OrdemCarga`: `CODEMP` → `CODEMP`, `ORDEMCARGA` → `ORDEMCARGA`
  > `Financeiro` → `Parceiro`: `CODPARC` → `CODPARC`
  > `Financeiro` → `BoletoRapido`: `IDUNICO` → `IDUNICO`
  > `Financeiro` → `RateioRecDesp`: `NUFIN` → `NUFIN`

### TGFPAR

**Instâncias (entityName para JapeFactory):**
- `FuncionarioTomador` — Funcionario Tomador
- `GrupoEconomico` — Grupo Economico
- `Motorista` — Motorista do Veiculo
- `Parceiro` — Parceiro
- `Parceiro2` — Parceiro
- `ParceiroAdministrador` — Parc. Administradora
- `ParceiroAtendido` — Parceiro Atendido
- `ParceiroAtivoPj` — Parceiro
- `ParceiroColeta` — Parceiro Coleta CT-e
- `ParceiroConsignatario` — Parceiro Consignatario
- `ParceiroDescargaMdfe` — Parceiro Descarregamento (MDF-e)
- `ParceiroDestinatario` — Parceiro Destinatario CT-e
- `ParceiroDestino` — Parceiro Destino
- `ParceiroEntrega` — Parceiro Entrega CT-e
- `ParceiroExpedidor` — Parceiro Expedidor CT-e
- `ParceiroF2` — Parceiro F2
- `ParceiroFabricante` — ParceiroFabricante
- `ParceiroFornecAprovado` — Fornecedor Aprovado
- `ParceiroFornecedor` — Parceiro Fornecedor
- `ParceiroFornecedorCotacao` — Fornecedor
- `ParceiroIntermed` — Parceiro Destino
- `ParceiroIntermediador` — Parc. Intermediador
- `ParceiroMatriz` — Parceiro Matriz
- `ParceiroMelhorFornec` — Melhor Fornecedor
- `ParceiroOrigem` — Parceiro de Origem
- `ParceiroPagante` — Parceiro Pagante
- `ParceiroPgtoFrete` — Parceiro
- `ParceiroPrestador` — Parceiro Prestador utilizado em contratos com SLA
- `ParceiroRecebedor` — Parceiro Recebedor CT-e
- `ParceiroRedespacho` — Parceiro Redespacho
- `ParceiroRemetente` — Parceiro Remetente
- `ParceiroRemetenteCte` — Parceiro Remetente CT-e
- `ParceiroResponsavel` — Parceiro Responsavel
- `ParceiroRetirada` — Parceiro Retirada
- `ParceiroTransportadora` — Parceiro Transportadora NF-e
- `ParceiroTransportadora2` — Parceiro Transportadora NF-e
- `Procedencia` — Procedencia de pesagem
- `ResponsavelPagador` — Parceiro Responsavel pelo Pagamento
- `TimProprietarioImovel` — Proprietarios dos imoveis
- `Transportadora` — Transportadora
- `TransportadoraFinal` — Transportadora Final

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Parceiro` | `TCBPLA` | `PlanoConta2` | inner (filha) | N | — |
| `Parceiro` | `TCBPLA` | `PlanoConta` | inner (filha) | N | — |
| `Parceiro` | `TCBPLA` | `PlanoConta4` | inner (filha) | N | — |
| `Parceiro` | `TCBPLA` | `PlanoConta3` | inner (filha) | N | — |
| `Parceiro` | `TGCCRED` | `GrupoAnaliseCredito` | inner (filha) | N | — |
| `Parceiro` | `TGCPAR` | `LimiteCredito` | inner (filha) | N | — |
| `Parceiro` | `TGFCAB` | `CabecalhoNotaModelo` | inner (filha) | S | — |
| `Parceiro` | `TGFCPC` | `ConvenioContaParceiro` | inner (filha) | N | — |
| `Parceiro` | `TGFCPL` | `ComplementoParc` | inner (filha) | N | INSERT, UPDATE, DELETE |
| `Parceiro` | `TGFCRT` | `TabelaPrecoCR` | inner (filha) | N | — |
| `Parceiro` | `TGFCTT` | `Contato` | lookup (chave estrangeira) | S | DELETE |
| `Parceiro` | `TGFCTT` | `ContatoEntrega` | inner (filha) | S | — |
| `Parceiro` | `TGFDFP` | `DescontoFinanceiroParcPeriodo` | inner (filha) | N | — |
| `Parceiro` | `TGFDPP` | `DependenteIR` | inner (filha) | S | — |
| `Parceiro` | `TGFFOP` | `FinalidadeOperacao` | inner (filha) | S | — |
| `Parceiro` | `TGFGCB` | `GrupoCobranca` | inner (filha) | S | — |
| `Parceiro` | `TGFIMA` | `AliquotaImposto` | inner (filha) | N | — |
| `Parceiro` | `TGFLCP` | `CreditoPorParceiro` | inner (filha) | N | — |
| `Parceiro` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | N | — |
| `Parceiro` | `TGFMOPC` | `MoedaPortalCotacao` | inner (filha) | S | — |
| `Parceiro` | `TGFNTA` | `NomeTabelasPreco` | inner (filha) | N | — |
| `Parceiro` | `TGFNTA` | `NomeTabelasPrecoFilha` | inner (filha) | N | — |
| `Parceiro` | `TGFPAEM` | `ParceiroEmpresGrupoIcms` | inner (filha) | N | — |
| `Parceiro` | `TGFPAP` | `RelacionamentoParceiroProduto` | inner (filha) | N | — |
| `Parceiro` | `TGFPAR` | `ParceiroMatriz` | inner (filha) | N | — |
| `Parceiro` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Parceiro` | `TGFPAS` | `ParceiroServico` | inner (filha) | N | — |
| `Parceiro` | `TGFPAXN` | `ParceiroAutorizacaoXml` | inner (filha) | S | — |
| `Parceiro` | `TGFPEIN` | `EmpresaParceiroInterdependente` | inner (filha) | S | — |
| `Parceiro` | `TGFPMA` | `MarcaParceiro` | inner (filha) | N | — |
| `Parceiro` | `TGFPPA` | `PerfilParceiro` | lookup (chave estrangeira) | S | INSERT, UPDATE, DELETE |
| `Parceiro` | `TGFPPZ` | `PrazoPorParceiro` | inner (filha) | N | — |
| `Parceiro` | `TGFPRO` | `Servico` | inner (filha) | S | — |
| `Parceiro` | `TGFRTP` | `ParceirosRota` | inner (filha) | N | — |
| `Parceiro` | `TGFTPP` | `Perfil` | inner (filha) | S | — |
| `Parceiro` | `TGFVEN` | `Assessor` | inner (filha) | N | — |
| `Parceiro` | `TGFVEN` | `Vendedor` | inner (filha) | N | — |
| `Parceiro` | `TIMCAR` | `TimCartorio` | inner (filha) | S | — |
| `Parceiro` | `TIMCBL` | `TimContaBancariaLocador` | inner (filha) | S | — |
| `Parceiro` | `TIMPRF` | `TimProfissaoRamoAtividade` | inner (filha) | S | — |
| `Parceiro` | `TSIBAI` | `BairroRecebimento` | inner (filha) | S | — |
| `Parceiro` | `TSIBAI` | `Bairro` | inner (filha) | S | — |
| `Parceiro` | `TSIBCO` | `Banco` | inner (filha) | N | — |
| `Parceiro` | `TSICID` | `Cidade` | inner (filha) | S | — |
| `Parceiro` | `TSICTA` | `ContaBancaria` | inner (filha) | S | — |
| `Parceiro` | `TSIEMP` | `EmpresaPreferencial` | inner (filha) | N | — |
| `Parceiro` | `TSIEMP` | `Empresa` | inner (filha) | N | — |
| `Parceiro` | `TSIEND` | `Endereco` | inner (filha) | S | — |
| `Parceiro` | `TSIPAI` | `Pais` | inner (filha) | S | — |
| `Parceiro` | `TSIREG` | `Regiao` | inner (filha) | N | — |
| `Parceiro` | `TSIRTEF` | `RedesTEF` | inner (filha) | S | — |
| `Parceiro` | `TSIUSU` | `UsuarioCobranca` | inner (filha) | N | — |
| `Parceiro` | `TSIUSU` | `Usuario` | inner (filha) | N | — |

  > `Parceiro` → `PlanoConta2`: `CODCTACTB2` → `CODCTACTB`
  > `Parceiro` → `PlanoConta`: `CODCTACTB` → `CODCTACTB`
  > `Parceiro` → `PlanoConta4`: `CODCTACTB4` → `CODCTACTB`
  > `Parceiro` → `PlanoConta3`: `CODCTACTB3` → `CODCTACTB`
  > `Parceiro` → `GrupoAnaliseCredito`: `CODCRED` → `CODCRED`
  > `Parceiro` → `LimiteCredito`: `CODPARC` → `CODPARC`
  > `Parceiro` → `CabecalhoNotaModelo`: `MODELONOTACOMPRA` → `NUNOTA`
  > `Parceiro` → `ConvenioContaParceiro`: `CODPARC` → `CODPARC`
  > `Parceiro` → `ComplementoParc`: `CODPARC` → `CODPARC`
  > `Parceiro` → `TabelaPrecoCR`: `CODPARC` → `CODPARC`
  > `Parceiro` → `Contato`: `CODPARC` → `CODPARC`
  > `Parceiro` → `ContatoEntrega`: `CODPARC` → `CODPARC`, `CODCONTATOPADCOT` → `CODCONTATO`
  > `Parceiro` → `DescontoFinanceiroParcPeriodo`: `CODPARC` → `CODPARC`
  > `Parceiro` → `DependenteIR`: `CODPARC` → `CODPARC`
  > `Parceiro` → `FinalidadeOperacao`: `NUFOP` → `NUFOP`
  > `Parceiro` → `GrupoCobranca`: `CODGRUPO` → `CODGRUPO`
  > `Parceiro` → `AliquotaImposto`: `CODPARC` → `CODIGO`
  > `Parceiro` → `CreditoPorParceiro`: `CODPARC` → `CODPARC`
  > `Parceiro` → `LocalFinanceiro`: `CODLOCALPADRAO` → `CODLOCAL`
  > `Parceiro` → `MoedaPortalCotacao`: `CODPARC` → `CODPARC`

### TGFPRO

**Instâncias (entityName para JapeFactory):**
- `Produto` — Produto
- `Produto3` — Produto
- `ProdutoApontamento1` — Produto/servico para agrupar apontamento 1
- `ProdutoApontamento2` — Produto/servico para agrupar apontamento 2
- `ProdutoEspecifico` — Produto Especifico
- `ProdutoIntermediario` — Produto Intermediario
- `ProdutoMateriaPrima` — Materia Prima
- `ProdutoSubstituido` — ProdutoSubstituido
- `ProdutoSubstitutoKit` — Produto Substituto do Kit
- `Servico` — Servico
- `TarifasCIP` — Tarifas CIP
- `TimServicoTxAdm` — Servico

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Produto` | `DH_COMPPROD` | `DH_COMPPROD` | inner (filha) | S | DELETE |
| `Produto` | `TCBPLA` | `PlanoContaEmpresa` | inner (filha) | S | — |
| `Produto` | `TCBPLA` | `PlanoContaConta4` | inner (filha) | S | — |
| `Produto` | `TCBPLA` | `PlanoContaEmpresa3` | inner (filha) | S | — |
| `Produto` | `TCBPLA` | `PlanoConta` | inner (filha) | S | — |
| `Produto` | `TCBPLA` | `PlanoContaEmpresa2` | inner (filha) | S | — |
| `Produto` | `TCIBEM` | `Imobilizado` | inner (filha) | N | — |
| `Produto` | `TCIEST` | `EstruturaLote` | inner (filha) | N | — |
| `Produto` | `TCITAX` | `TaxaDepreciacao` | inner (filha) | N | — |
| `Produto` | `TCITAXAJ` | `TaxaDepreciacaoAjuste` | inner (filha) | S | — |
| `Produto` | `TCSPRJ` | `Projeto` | inner (filha) | S | — |
| `Produto` | `TGAGRU` | `GrupoProducaoProduto` | inner (filha) | N | DELETE |
| `Produto` | `TGFAID` | `AliquotaInternaDestino` | inner (filha) | S | — |
| `Produto` | `TGFBAR` | `CodigoBarras` | inner (filha) | S | — |
| `Produto` | `TGFCAT` | `CategoriaMedicamento` | inner (filha) | N | — |
| `Produto` | `TGFCINFCOM` | `CodigoItemNFCom` | inner (filha) | S | — |
| `Produto` | `TGFCLP` | `LigacaoClassificacaoProduto` | inner (filha) | S | — |
| `Produto` | `TGFCPR` | `ClassificacaoMedicamento` | inner (filha) | N | — |
| `Produto` | `TGFCPRB` | `TabelaCPRB` | inner (filha) | S | — |
| `Produto` | `TGFDID` | `DisponibilidadeDiaria` | inner (filha) | N | — |
| `Produto` | `TGFEPI` | `EquipamentoProtecaoIndividual` | inner (filha) | S | — |
| `Produto` | `TGFEST` | `Estoque` | inner (filha) | S | — |
| `Produto` | `TGFFAM` | `FamiliaProduto` | inner (filha) | N | — |
| `Produto` | `TGFFOR` | `FormulaPrecificacao` | inner (filha) | N | — |
| `Produto` | `TGFGRA` | `GradeProduto` | inner (filha) | S | — |
| `Produto` | `TGFGRD` | `ConfiguracaoGradeProduto` | inner (filha) | S | — |
| `Produto` | `TGFGRU` | `GrupoProduto` | inner (filha) | S | — |
| `Produto` | `TGFGXE` | `RelacaoGenericoEspecifico` | inner (filha) | N | — |
| `Produto` | `TGFICP` | `ItemComposicaoProduto` | inner (filha) | N | — |
| `Produto` | `TGFIFE` | `AliquotaPisCofinsCssl3` | inner (filha) | S | — |
| `Produto` | `TGFIFE` | `AliquotaPisCofinsCssl2` | inner (filha) | S | — |
| `Produto` | `TGFIFE` | `AliquotaPisCofinsCssl1` | inner (filha) | S | — |
| `Produto` | `TGFIMA` | `AliquotaImposto` | inner (filha) | S | — |
| `Produto` | `TGFIPI` | `AliquotaIPI` | inner (filha) | N | — |
| `Produto` | `TGFIPP` | `IpiProdutoParceiro` | inner (filha) | S | — |
| `Produto` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | N | — |
| `Produto` | `TGFMAR` | `MarcaProduto` | inner (filha) | N | — |
| `Produto` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `Produto` | `TGFNCM` | `Ncm` | inner (filha) | S | — |
| `Produto` | `TGFNRR` | `CadastroNaturezaRendimentos` | inner (filha) | S | — |
| `Produto` | `TGFNTA` | `NomeTabelasPrecoFilha` | inner (filha) | N | — |
| `Produto` | `TGFPAL` | `ProdutoAlternativo` | inner (filha) | N | — |
| `Produto` | `TGFPAP` | `RelacionamentoParceiroProduto` | inner (filha) | S | — |
| `Produto` | `TGFPAR` | `ParceiroFabricante` | inner (filha) | N | — |
| `Produto` | `TGFPAR` | `ParceiroFornecedor` | inner (filha) | N | — |
| `Produto` | `TGFPAR` | `Parceiro` | inner (filha) | N | — |
| `Produto` | `TGFPAT` | `PrincipioAtivo` | inner (filha) | N | — |
| `Produto` | `TGFPEM` | `EmpresaProdutoImpostos` | inner (filha) | S | — |
| `Produto` | `TGFPLM` | `ProdutoModeloVeiculo` | inner (filha) | N | — |
| `Produto` | `TGFPRD` | `ProdutoData` | inner (filha) | S | — |
| `Produto` | `TGFPRF` | `Flex` | inner (filha) | N | — |
| `Produto` | `TGFPRO` | `Servico` | inner (filha) | N | — |
| `Produto` | `TGFPRO` | `ProdutoSubstitutoKit` | inner (filha) | N | — |
| `Produto` | `TGFPRO` | `Produto3` | inner (filha) | N | — |
| `Produto` | `TGFPRO` | `ProdutoApontamento2` | inner (filha) | S | — |
| `Produto` | `TGFPRO` | `ProdutoApontamento1` | inner (filha) | S | — |
| `Produto` | `TGFPRO0200` | `EFDProduto0200` | inner (filha) | S | — |
| `Produto` | `TGFPUMA` | `UnidadeMovArmazenagemProduto` | inner (filha) | S | — |
| `Produto` | `TGFRASTEMP` | `RastreamentoEmpresa` | inner (filha) | S | — |
| `Produto` | `TGFREA` | `RegimeEspecialIcms` | inner (filha) | N | — |
| `Produto` | `TGFSAZ` | `SazonalidadeProduto` | inner (filha) | S | — |
| `Produto` | `TGFSCA` | `SubCategoriaMedicamento` | inner (filha) | N | — |
| `Produto` | `TGFSPR` | `SubClassificacaoMedicamento` | inner (filha) | N | — |
| `Produto` | `TGFSTE` | `SubClasseTerapeutica` | inner (filha) | N | — |
| `Produto` | `TGFSTG` | `GeneroProduto` | inner (filha) | N | — |
| `Produto` | `TGFTER` | `ClasseTerapeutica` | inner (filha) | N | — |
| `Produto` | `TGFVCS` | `VendaCasada` | inner (filha) | N | — |
| `Produto` | `TGFVOA` | `VolumeAlternativo` | inner (filha) | S | — |
| `Produto` | `TGFVOL` | `UnidadeMinArmazenagemWMS` | inner (filha) | N | — |
| `Produto` | `TGFVOL` | `VolumeKanban` | inner (filha) | S | — |
| `Produto` | `TGFVOL` | `Volume` | inner (filha) | N | — |
| `Produto` | `TGFVOL` | `UnidadeCompra` | inner (filha) | S | — |
| `Produto` | `TGFVOL` | `VolumeResumoEntrega` | inner (filha) | N | — |
| `Produto` | `TGFVOL` | `VolumeFETHAB` | inner (filha) | S | — |
| `Produto` | `TGFVTP` | `ViaTransporte` | inner (filha) | N | — |
| `Produto` | `TGWARS` | `AreaSeparacao` | inner (filha) | N | — |
| `Produto` | `TGWEXP` | `ProdutoEndereco` | inner (filha) | N | — |
| `Produto` | `TGWRFA` | `RegraArmazenagem` | inner (filha) | N | — |
| `Produto` | `TPRCPMP` | `ComponenteManufaturaPA` | inner (filha) | N | — |
| `Produto` | `TPRCPR` | `CapacidadeRecurso` | inner (filha) | N | — |
| `Produto` | `TPRRXP` | `RecursosPA` | inner (filha) | N | — |
| `Produto` | `TSICUS` | `CentroResultado` | inner (filha) | S | INSERT |
| `Produto` | `TSIFOR` | `Formula` | inner (filha) | N | — |
| `Produto` | `TSIFOR` | `FormulaRequisicao` | inner (filha) | N | — |
| `Produto` | `TSIKIT` | `ConfiguracaoKit` | inner (filha) | S | — |
| `Produto` | `TSIMOE` | `Moeda` | inner (filha) | S | — |
| `Produto` | `TSIRFE` | `ModeloEtiqueta` | inner (filha) | S | — |
| `Produto` | `TSIRFE` | `RelatorioEtiquetaSeparacao` | inner (filha) | N | — |
| `ProdutoMateriaPrima` | `TGFGRU` | `GrupoProduto` | inner (filha) | S | — |
| `Servico` | `TCBPLA` | `PlanoConta` | inner (filha) | S | — |
| `Servico` | `TCBPLA` | `PlanoContaEmpresa` | inner (filha) | S | — |
| `Servico` | `TCBPLA` | `PlanoContaConta3` | inner (filha) | S | — |
| `Servico` | `TCBPLA` | `PlanoContaConta4` | inner (filha) | S | — |
| `Servico` | `TCBPLA` | `PLanoContaConta2` | inner (filha) | S | — |
| `Servico` | `TCSPRJ` | `Projeto` | inner (filha) | S | — |
| `Servico` | `TCSSEM` | `RelacionamentoServicoMotivo` | inner (filha) | S | — |
| `Servico` | `TGFCINFCOM` | `CodigoItemNFCom` | inner (filha) | S | — |
| `Servico` | `TGFCIT` | `ClassificacaoItemTelecomunicao` | inner (filha) | N | — |
| `Servico` | `TGFCPRB` | `TabelaCPRB` | inner (filha) | S | — |
| `Servico` | `TGFCSV` | `ComponenteServico` | inner (filha) | S | — |
| `Servico` | `TGFDID` | `DisponibilidadeDiaria` | inner (filha) | N | — |
| `Servico` | `TGFFOR` | `FormulaPrecificacao` | inner (filha) | S | — |
| `Servico` | `TGFGRA` | `GradeProduto` | inner (filha) | S | — |
| `Servico` | `TGFGRU` | `GrupoProduto` | inner (filha) | S | — |
| `Servico` | `TGFICP` | `ItemComposicaoProduto` | inner (filha) | N | — |
| `Servico` | `TGFIMA` | `AliquotaImposto` | inner (filha) | N | — |
| `Servico` | `TGFISS` | `AliquotaISS` | inner (filha) | N | — |
| `Servico` | `TGFLST` | `ListaServicoSintegra` | inner (filha) | S | — |
| `Servico` | `TGFMCS` | `MultiplosComponentesServico` | inner (filha) | S | — |
| `Servico` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `Servico` | `TGFNRR` | `CadastroNaturezaRendimentos` | inner (filha) | S | — |
| `Servico` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Servico` | `TGFPRD` | `ProdutoData` | inner (filha) | S | — |
| `Servico` | `TGFPRO` | `ProdutoApontamento1` | inner (filha) | N | — |
| `Servico` | `TGFPRO` | `ProdutoApontamento2` | inner (filha) | N | — |
| `Servico` | `TGFSEM` | `ConfiguracaoEmpresa` | inner (filha) | S | — |
| `Servico` | `TGFVOL` | `Volume` | inner (filha) | S | — |
| `Servico` | `TGFVTP` | `ViaTransporte` | inner (filha) | N | — |
| `Servico` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `Servico` | `TSIFOR` | `Formula` | inner (filha) | N | — |
| `Servico` | `TSIMOE` | `Moeda` | inner (filha) | S | — |
| `TarifasCIP` | `TCBPLA` | `PlanoContaConta4` | inner (filha) | S | — |
| `TarifasCIP` | `TCBPLA` | `PlanoContaEmpresa2` | inner (filha) | S | — |
| `TarifasCIP` | `TCBPLA` | `PlanoContaEmpresa3` | inner (filha) | N | — |
| `TarifasCIP` | `TCBPLA` | `PlanoContaEmpresa` | inner (filha) | S | INSERT |
| `TarifasCIP` | `TCSPRJ` | `Projeto` | inner (filha) | S | UPDATE |
| `TarifasCIP` | `TGAGRU` | `GrupoProducaoProduto` | inner (filha) | N | DELETE |
| `TarifasCIP` | `TGFFOR` | `FormulaPrecificacao` | inner (filha) | N | — |
| `TarifasCIP` | `TGFGRU` | `GrupoProduto` | inner (filha) | S | — |
| `TarifasCIP` | `TGFIPI` | `AliquotaIPI` | inner (filha) | S | — |
| `TarifasCIP` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | N | — |
| `TarifasCIP` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `TarifasCIP` | `TGFNTA` | `NomeTabelasPrecoFilha` | inner (filha) | N | — |
| `TarifasCIP` | `TGFPAR` | `ParceiroFornecedor` | inner (filha) | N | — |
| `TarifasCIP` | `TGFPRD` | `ProdutoData` | inner (filha) | S | — |
| `TarifasCIP` | `TGFPRO` | `Servico` | inner (filha) | N | — |
| `TarifasCIP` | `TGFREA` | `RegimeEspecialIcms` | inner (filha) | N | — |
| `TarifasCIP` | `TGFSTG` | `GeneroProduto` | inner (filha) | N | — |
| `TarifasCIP` | `TGFVOL` | `UnidadeCompra` | inner (filha) | S | — |
| `TarifasCIP` | `TGFVOL` | `Volume` | inner (filha) | N | — |
| `TarifasCIP` | `TSICUS` | `CentroResultado` | inner (filha) | S | INSERT |
| `TarifasCIP` | `TSIFOR` | `FormulaRequisicao` | inner (filha) | N | — |
| `TarifasCIP` | `TSIFOR` | `FormulaLancamentoContabil` | inner (filha) | S | — |
| `TarifasCIP` | `TSIFOR` | `Formula` | inner (filha) | N | — |
| `TarifasCIP` | `TSIMOE` | `Moeda` | inner (filha) | S | — |

  > `Produto` → `DH_COMPPROD`: `CODPROD` → `CODPROD`
  > `Produto` → `PlanoContaEmpresa`: `CODCTACTB` → `CODCTACTB`
  > `Produto` → `PlanoContaConta4`: `CODCTACTB4` → `CODCTACTB`
  > `Produto` → `PlanoContaEmpresa3`: `CODCTACTB3` → `CODCTACTB`
  > `Produto` → `PlanoConta`: `CODCTACTBEFD` → `CODCTACTB`
  > `Produto` → `PlanoContaEmpresa2`: `CODCTACTB2` → `CODCTACTB`
  > `Produto` → `Imobilizado`: `CODPROD` → `CODPROD`
  > `Produto` → `EstruturaLote`: `CODPROD` → `CODPROD`
  > `Produto` → `TaxaDepreciacao`: `CODPROD` → `CODPROD`
  > `Produto` → `TaxaDepreciacaoAjuste`: `CODPROD` → `CODPROD`
  > `Produto` → `Projeto`: `CODPROJ` → `CODPROJ`
  > `Produto` → `GrupoProducaoProduto`: `CODGPROD` → `CODGPROD`
  > `Produto` → `AliquotaInternaDestino`: `CODPROD` → `CODPROD`
  > `Produto` → `CodigoBarras`: `CODPROD` → `CODPROD`
  > `Produto` → `CategoriaMedicamento`: `CODCAT` → `CODCAT`
  > `Produto` → `CodigoItemNFCom`: `CODIGONFCOM` → `CODIGO`
  > `Produto` → `LigacaoClassificacaoProduto`: `CODPROD` → `CODPROD`
  > `Produto` → `ClassificacaoMedicamento`: `CODCPR` → `CODCPR`
  > `Produto` → `TabelaCPRB`: `CODCPRB` → `CODCPRB`
  > `Produto` → `DisponibilidadeDiaria`: `CODPROD` → `CODPROD`

### TGFEMP

**Instâncias (entityName para JapeFactory):**
- `EmpresaFinanceiro` — Empresa Financeiro

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaBonificacao` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaEmpresa` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaEmpresa2` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaEmpresa3` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaMulta` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaJuro` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TCBPLA` | `PlanoContaDesconto` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFAAXN` | `AutorizacaoAcessoXmlNFe` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloSaidaReclassificacao` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloSaidaEstoqueConsignado` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloSaidaEstoqueDeTerc` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `CabecalhoNotaModeloSaidaBem` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `CabecalhoNotaModeloSaida` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFCAB` | `CabecalhoNotaWmsEnt` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFCAB` | `CabecalhoNotaModelo` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloEntradaEstoqueDeTerc` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `CabecalhoNotaModeloAgenda` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloRetornoEstoqueWMS` | lookup (chave estrangeira) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloEstornoWMSDevCompra` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloEntradaReclassificacao` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloSaidaEstoqueComTerc` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `CabecalhoNotaWmsSai` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloEntradaEstoqueComTerc` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCAB` | `ModeloEntradaEstoqueConsignado` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFCNAE` | `CNAEEmpresa` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFCTENT` | `NotaTecnicaCTe` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFEFB` | `BlocosEscrituracaoFiscal` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFEFR` | `RegistrosEscrituracaoFiscal` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFEMPSN` | `PartilhaSimplesNacXEmp` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFEPS` | `EventoPeriodico` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFFDA` | `FormulaDiferencialAliquota` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFFOR` | `FormulaPrecificacao` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFFSI` | `FundoSociedadeInvestimento` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFHBC` | `HistoricoBancarioDestino` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFHBC` | `HistoricoBancario` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFLCDPRTERC` | `TerceiroProducaoRural` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFLOC` | `LocalEstoqueTerceiro` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFLOC` | `LocalEstoqueWms` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFLOC` | `LocalPadraoEconet` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMIX` | `ModeloImportacaoXML` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloNotaFiscal` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloNotaFiscalEstoque` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloDanfe` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloDACTE` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloDanfeContingencia` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloDanfeNFCeCompleto` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFMON` | `ModeloDanfeNFCeSimplificado` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFNAT` | `NaturezaIpi` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFNAT` | `NaturezaReceitaDespesaICMS` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFNFCOMNT` | `NotaTecnicaNFCom` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFNFENT` | `NotaTecnicaNFe` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFNTA` | `NomeTabelasPreco` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFNTA` | `NomeTabelasPrecoFilha` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFNUM` | `ControleNumeracao` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFPAR` | `Parceiro2` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFPAR` | `Parceiro` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFPAR` | `ParceiroAtivoPj` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFPAR` | `ParceiroEntrega` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFRDARF` | `ReceitaDarfReinf` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFRDARF` | `ReceitaDarf` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFRNT` | `ReintegraPrevidencia` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFTIT` | `TipoTitulo` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFTIT` | `TipoTituloIpi` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFTOP` | `TipoOperacaoPedidoAgrupa` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFTOP` | `TipoOperacaoEntrMerc` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGFTOP` | `TipoOperacaoEFDEmpresa` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFTOP` | `TipoOperacaoIpi` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TGFTPP` | `Perfil` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGMCFG` | `ConfiguracaoMeta` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagemFlutuante` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagemIndefinida` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagemEsp` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoRetornoExpedicao` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagem2` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagem4` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagemIndef` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagemChk` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagem3` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagem` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TGWEND` | `EnderecoArmazenagem5` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIBCO` | `Banco` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIBCO` | `BancoIpi` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSICTA` | `ContaBancariaIpi` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSICTA` | `ContaBancaria` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSICUS` | `CentroResultadoDespesa` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSICUS` | `CentroResultadoEFDEmpresa` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSICUS` | `CentroResultadoIpi` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaModelo` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaMatriz` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaMatrizNfse` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaMatrizGnre` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaNegociacao` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIEMP` | `Empresa` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaCadastro` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIEMP` | `EmpresaSoma` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIFAT` | `FaturamentoCruzado` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIIUF` | `InscricaoUnidadeFederativa` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIRFE` | `RelatorioEtiquetaVolume` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIRFE` | `RelatorioMinutaDespacho` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSIRFE` | `ModeloEtiqueta` | inner (filha) | S | — |
| `EmpresaFinanceiro` | `TSIRIM` | `RoteamentoImpressaoEmpresa` | inner (filha) | N | — |
| `EmpresaFinanceiro` | `TSISMTP` | `ServidorSMTP` | inner (filha) | N | — |

  > `EmpresaFinanceiro` → `PlanoContaBonificacao`: `CODCTACTBBONIF` → `CODCTACTB`
  > `EmpresaFinanceiro` → `PlanoContaEmpresa`: `CODCTACTB_1` → `CODCTACTB`
  > `EmpresaFinanceiro` → `PlanoContaEmpresa2`: `CODCTACTB_2` → `CODCTACTB`
  > `EmpresaFinanceiro` → `PlanoContaEmpresa3`: `CODCTACTB_3` → `CODCTACTB`
  > `EmpresaFinanceiro` → `PlanoContaMulta`: `CODCTACTBMULT` → `CODCTACTB`
  > `EmpresaFinanceiro` → `PlanoContaJuro`: `CODCTACTBJUROS` → `CODCTACTB`
  > `EmpresaFinanceiro` → `PlanoContaDesconto`: `CODCTACTBDESC` → `CODCTACTB`
  > `EmpresaFinanceiro` → `AutorizacaoAcessoXmlNFe`: `CODEMP` → `CODEMP`
  > `EmpresaFinanceiro` → `ModeloSaidaReclassificacao`: `NOTASAIAJUSTERECLAS` → `NUNOTA`
  > `EmpresaFinanceiro` → `ModeloSaidaEstoqueConsignado`: `NOTASAIAJUSTESTCONS` → `NUNOTA`
  > `EmpresaFinanceiro` → `ModeloSaidaEstoqueDeTerc`: `NOTASAIAJUSTESTDTER` → `NUNOTA`
  > `EmpresaFinanceiro` → `CabecalhoNotaModeloSaidaBem`: `NOTASAIAJUSTBEM` → `NUNOTA`
  > `EmpresaFinanceiro` → `CabecalhoNotaModeloSaida`: `NOTASAIAJUSTEST` → `NUNOTA`
  > `EmpresaFinanceiro` → `CabecalhoNotaWmsEnt`: `NOTAENTSOBRAWMS` → `NUNOTA`
  > `EmpresaFinanceiro` → `CabecalhoNotaModelo`: `NOTAENTAJUSTEST` → `NUNOTA`
  > `EmpresaFinanceiro` → `ModeloEntradaEstoqueDeTerc`: `NOTAENTAJUSTESTDTER` → `NUNOTA`
  > `EmpresaFinanceiro` → `CabecalhoNotaModeloAgenda`: `NOTAMODELODAGENDA` → `NUNOTA`
  > `EmpresaFinanceiro` → `ModeloRetornoEstoqueWMS`: `CODMODRETESTWMS` → `NUNOTA`
  > `EmpresaFinanceiro` → `ModeloEstornoWMSDevCompra`: `MODESTCPAWMS` → `NUNOTA`
  > `EmpresaFinanceiro` → `ModeloEntradaReclassificacao`: `NOTAENTAJUSTERECLAS` → `NUNOTA`

### TGFTOP

**Instâncias (entityName para JapeFactory):**
- `TOPDespesa` — TOPDespesa
- `TOPReceita` — TOPReceita
- `TipoOperacao` — Tipo de Operação
- `TipoOperacao2` — Tipo de Operação
- `TipoOperacao3` — Tipo de Operação de (Requisição)
- `TipoOperacaoBaixa` — Tipo de Operação para Baixa
- `TipoOperacaoDenegada` — TOP para NF-e Denegada:
- `TipoOperacaoDenegadaCTe` — TOP para CT-e Denegada:
- `TipoOperacaoDestino` — Tipo de Operação Destino
- `TipoOperacaoEFDEmpresa` — Tipo Operação
- `TipoOperacaoEntrMerc` — TOP de entrada de mercadorias
- `TipoOperacaoIpi` — Tipo de Operação
- `TipoOperacaoPedidoAgrupa` — TOP pedido agrupado p/ enviar ao WMS
- `TipoOperacaoPerda` — TipoOperacaoPerda
- `TipoOperacaoRetorno` — Tipo de operação pendente de retorno.
- `TopAtendimento` — Top de Antedimento
- `TopBackorder` — Top de Back order
- `TopEntrada` — Top de Entrada
- `TopPrincipal` — Tipo Operação Principal
- `TopProducao` — Top de Produção
- `TopSaida` — Top de saida
- `TopSeparacao` — Tipo Operação Separacao
- `grupoTipoOperacao` — Grupos Tipo Operação

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `TipoOperacao` | `TCBPLA` | `PlanoConta` | lookup (chave estrangeira) | S | — |
| `TipoOperacao` | `TGFCAB` | `CabecalhoNotaModelo` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCCO` | `ConfiguracaoConferencia` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalOperacaoSaidaEstado` | inner (filha) | N | UPDATE |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalOperacaoEntrada` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalPrestacaoServico` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalOperacaoTerceiros` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalOperacaoSaida` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalCombustivelLubrif` | inner (filha) | N | — |
| `TipoOperacao` | `TGFCFO` | `ClaFiscalOperacaoEntradaEstado` | inner (filha) | N | — |
| `TipoOperacao` | `TGFFCI` | `SeparacaoFaturamento` | inner (filha) | S | — |
| `TipoOperacao` | `TGFFOP` | `FinalidadeOperacao` | inner (filha) | N | — |
| `TipoOperacao` | `TGFIMA` | `AliquotaImposto` | inner (filha) | N | — |
| `TipoOperacao` | `TGFLAY` | `LayoutNota` | inner (filha) | N | — |
| `TipoOperacao` | `TGFLOC` | `LocalPadraoImportarXML` | inner (filha) | S | — |
| `TipoOperacao` | `TGFLVR` | `LayoutVendaRapida` | inner (filha) | S | — |
| `TipoOperacao` | `TGFMON` | `ModeloNFSe` | inner (filha) | S | — |
| `TipoOperacao` | `TGFMON` | `ModeloRoman` | inner (filha) | S | — |
| `TipoOperacao` | `TGFMON` | `ModeloRPS` | inner (filha) | N | — |
| `TipoOperacao` | `TGFMON` | `ModeloDadosAdicionais` | inner (filha) | N | — |
| `TipoOperacao` | `TGFMON` | `ModeloNotaFiscal` | inner (filha) | N | — |
| `TipoOperacao` | `TGFMON` | `ModeloImpressaoCfeCanc` | inner (filha) | S | — |
| `TipoOperacao` | `TGFOSL` | `OrdemSugestaoLocal` | inner (filha) | N | — |
| `TipoOperacao` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `TipoOperacao` | `TGFSPE` | `SerieEmpresa` | inner (filha) | S | — |
| `TipoOperacao` | `TGFTEM` | `EmailTOP` | inner (filha) | N | — |
| `TipoOperacao` | `TGFTOL` | `LiberacaoPorTipoOperacao` | inner (filha) | N | — |
| `TipoOperacao` | `TGFTOP` | `TopBackorder` | inner (filha) | S | — |
| `TipoOperacao` | `TGFTOP` | `TipoOperacaoRetorno` | inner (filha) | N | — |
| `TipoOperacao` | `TGFTOP` | `TopAtendimento` | inner (filha) | S | — |
| `TipoOperacao` | `TGFTOP` | `TipoOperacaoDenegada` | inner (filha) | N | — |
| `TipoOperacao` | `TGFTOP` | `TipoOperacaoDestino` | inner (filha) | N | — |
| `TipoOperacao` | `TGFTOP` | `TipoOperacaoDenegadaCTe` | inner (filha) | N | — |
| `TipoOperacao` | `TGFTRN` | `TopRegraNegocio` | inner (filha) | N | — |
| `TipoOperacao` | `TGFUSE` | `UsoSeparacao` | inner (filha) | S | — |
| `TipoOperacao` | `TSILIB` | `LiberacaoLimite` | inner (filha) | N | — |
| `TipoOperacao` | `TSIMOE` | `Moeda` | inner (filha) | N | — |
| `TipoOperacao` | `TSIREM` | `FormatadorRemessa` | inner (filha) | N | — |

  > `TipoOperacao` → `PlanoConta`: `CODCTACTBEFD` → `CODCTACTB`
  > `TipoOperacao` → `CabecalhoNotaModelo`: `NUNOTAMODELO` → `NUNOTA`
  > `TipoOperacao` → `ConfiguracaoConferencia`: `NUCCO` → `NUCCO`
  > `TipoOperacao` → `ClaFiscalOperacaoSaidaEstado`: `CODCFO_SAIDA_FORA` → `CODCFO`
  > `TipoOperacao` → `ClaFiscalOperacaoEntrada`: `CODCFO_ENTRADA` → `CODCFO`
  > `TipoOperacao` → `ClaFiscalPrestacaoServico`: `CODCFPS` → `CODCFO`
  > `TipoOperacao` → `ClaFiscalOperacaoTerceiros`: `CODCFO_TERC` → `CODCFO`
  > `TipoOperacao` → `ClaFiscalOperacaoSaida`: `CODCFO_SAIDA` → `CODCFO`
  > `TipoOperacao` → `ClaFiscalCombustivelLubrif`: `CODCFO_COMBUST_LUBRIF` → `CODCFO`
  > `TipoOperacao` → `ClaFiscalOperacaoEntradaEstado`: `CODCFO_ENTRADA_FORA` → `CODCFO`
  > `TipoOperacao` → `SeparacaoFaturamento`: `CODTIPOPER` → `CODTIPOPER`
  > `TipoOperacao` → `FinalidadeOperacao`: `NUFOP` → `NUFOP`
  > `TipoOperacao` → `AliquotaImposto`: `CODTIPOPER` → `CODIGO`
  > `TipoOperacao` → `LayoutNota`: `NULAYOUT` → `NULAYOUT`
  > `TipoOperacao` → `LocalPadraoImportarXML`: `CODLOCALIMPXML` → `CODLOCAL`
  > `TipoOperacao` → `LayoutVendaRapida`: `NULAYOUTCVR` → `NULAYOUT`
  > `TipoOperacao` → `ModeloNFSe`: `CODMODNFSE` → `CODMODNF`
  > `TipoOperacao` → `ModeloRoman`: `CODMODRO` → `CODMODNF`
  > `TipoOperacao` → `ModeloRPS`: `CODMODRPS` → `CODMODNF`
  > `TipoOperacao` → `ModeloDadosAdicionais`: `CODMODDAD` → `CODMODNF`

### TGFNAT

**Instâncias (entityName para JapeFactory):**
- `Natureza` — Natureza
- `Natureza2` — Natureza2
- `Natureza3` — Natureza3
- `NaturezaArm` — Natureza de armazenagem
- `NaturezaExp` — Natureza de armazenagem
- `NaturezaIpi` — Natureza
- `NaturezaReceitaDespesaICMS` — Natureza Despesa Receitas ICMS
- `NaturezaReceitaDespesaICMSST` — Natureza Despesa Receitas ICMS ST

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Natureza` | `TCBHIS` | `HistoricoPadrao` | inner (filha) | S | — |
| `Natureza` | `TCBHIS` | `HistoricoPadrao2` | inner (filha) | S | — |
| `Natureza` | `TCBPLA` | `PlanoConta` | lookup (chave estrangeira) | S | — |
| `Natureza` | `TCBPLA` | `PlanoContaEmpresa2` | inner (filha) | S | — |
| `Natureza` | `TCBPLA` | `PlanoContaEmpresa` | inner (filha) | S | — |
| `Natureza` | `TCSSER` | `ProdutoServico` | inner (filha) | N | — |
| `Natureza` | `TGFDNP` | `DescricaoNaturezaParceiro` | inner (filha) | S | DELETE |
| `Natureza` | `TGFENA` | `RelacaoEmpNatCtaContabil` | inner (filha) | N | — |
| `Natureza` | `TGFGNT` | `GrupoNaturezas` | inner (filha) | N | — |
| `Natureza` | `TGFNATPC` | `RelacaoNatPisCofins` | inner (filha) | S | — |
| `Natureza` | `TGFNCC` | `NaturCentroResultCtaContabil` | inner (filha) | N | — |
| `Natureza` | `TGFNPC` | `NaturezaProjetoCtaContabil` | inner (filha) | N | — |
| `Natureza` | `TGFPRO` | `Servico` | inner (filha) | N | — |

  > `Natureza` → `HistoricoPadrao`: `CODHISTCTB` → `CODHISTCTB`
  > `Natureza` → `HistoricoPadrao2`: `CODHISTCTB2` → `CODHISTCTB`
  > `Natureza` → `PlanoConta`: `CODCTACTBEFD` → `CODCTACTB`
  > `Natureza` → `PlanoContaEmpresa2`: `CODCTACTB2` → `CODCTACTB`
  > `Natureza` → `PlanoContaEmpresa`: `CODCTACTB` → `CODCTACTB`
  > `Natureza` → `ProdutoServico`: `CODNAT` → `CODNAT`
  > `Natureza` → `DescricaoNaturezaParceiro`: `CODNAT` → `CODNAT`
  > `Natureza` → `RelacaoEmpNatCtaContabil`: `CODNAT` → `CODNAT`
  > `Natureza` → `GrupoNaturezas`: `CODGRUPONAT` → `CODGRUPONAT`
  > `Natureza` → `RelacaoNatPisCofins`: `CODNAT` → `CODNAT`
  > `Natureza` → `NaturCentroResultCtaContabil`: `CODNAT` → `CODNAT`
  > `Natureza` → `NaturezaProjetoCtaContabil`: `CODNAT` → `CODNAT`
  > `Natureza` → `Servico`: `CODSERVUNICO` → `CODPROD`

### TGFVEN

**Instâncias (entityName para JapeFactory):**
- `Assessor` — Assessor
- `Gerente` — Gerente
- `Vendedor` — Vendedor
- `VendedorExecutante` — Executante
- `VendedorItem` — Vendedor do item da nota

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Vendedor` | `TFPCGH` | `IdentificacaoCargaHoraria` | inner (filha) | N | — |
| `Vendedor` | `TFPFUN` | `Funcionario` | inner (filha) | N | — |
| `Vendedor` | `TGFCER` | `CertificacaoRegra` | inner (filha) | S | — |
| `Vendedor` | `TGFCVG` | `ComissaoVendedorGrupo` | inner (filha) | S | INSERT |
| `Vendedor` | `TGFFCV` | `FormulaComissaoPremiacao` | inner (filha) | N | — |
| `Vendedor` | `TGFFOC` | `FormulasComissao` | inner (filha) | S | — |
| `Vendedor` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Vendedor` | `TGFRGV` | `VendedorGrupoProduto` | inner (filha) | S | — |
| `Vendedor` | `TGFRPV` | `VendedorParceiro` | inner (filha) | S | — |
| `Vendedor` | `TGFVEN` | `Gerente` | inner (filha) | S | — |
| `Vendedor` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `Vendedor` | `TSIEMP` | `Empresa` | inner (filha) | S | — |
| `Vendedor` | `TSIREG` | `Regiao` | inner (filha) | S | — |
| `Vendedor` | `TSIUSU` | `Usuario` | inner (filha) | N | — |

  > `Vendedor` → `IdentificacaoCargaHoraria`: `CODCARGAHOR` → `CODCARGAHOR`
  > `Vendedor` → `Funcionario`: `CODEMP` → `CODEMP`, `CODFUNC` → `CODFUNC`
  > `Vendedor` → `CertificacaoRegra`: `TIPOCERTIF` → `TIPO`, `CODVEND` → `CHAVE`
  > `Vendedor` → `ComissaoVendedorGrupo`: `CODVEND` → `CODVEND`
  > `Vendedor` → `FormulaComissaoPremiacao`: `CODVEND` → `CODVEND`
  > `Vendedor` → `FormulasComissao`: `CODFORM` → `CODFORM`
  > `Vendedor` → `Parceiro`: `CODPARC` → `CODPARC`
  > `Vendedor` → `VendedorGrupoProduto`: `CODVEND` → `CODVEND`
  > `Vendedor` → `VendedorParceiro`: `CODVEND` → `CODVEND`
  > `Vendedor` → `Gerente`: `CODGER` → `CODVEND`
  > `Vendedor` → `CentroResultado`: `CODCENCUSPAD` → `CODCENCUS`
  > `Vendedor` → `Empresa`: `CODEMP` → `CODEMP`
  > `Vendedor` → `Regiao`: `CODREG` → `CODREG`
  > `Vendedor` → `Usuario`: `CODPARC` → `CODPARC`

### TGFCTT

**Instâncias (entityName para JapeFactory):**
- `Contato` — Contato
- `ContatoEntrega` — Contato de Entrega

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Contato` | `TGFCTTPRO` | `ProdutoContato` | inner (filha) | S | — |
| `Contato` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Contato` | `TGFPAR` | `Parceiro2` | inner (filha) | S | — |
| `Contato` | `TGFPPA` | `PerfilContato` | lookup (chave estrangeira) | S | DELETE |
| `Contato` | `TIMPRF` | `TimProfissaoRamoAtividade` | inner (filha) | S | — |
| `Contato` | `TSIBAI` | `Bairro` | inner (filha) | N | — |
| `Contato` | `TSIBCO` | `Banco` | inner (filha) | S | — |
| `Contato` | `TSICID` | `Cidade` | inner (filha) | N | — |
| `Contato` | `TSIEND` | `Endereco` | inner (filha) | N | — |
| `Contato` | `TSIPAI` | `Pais` | inner (filha) | S | — |
| `Contato` | `TSIREG` | `Regiao` | inner (filha) | N | — |
| `Contato` | `TSIUSU` | `Usuario` | inner (filha) | N | — |

  > `Contato` → `ProdutoContato`: `CODPARC` → `CODPARC`, `CODCONTATO` → `CODCONTATO`
  > `Contato` → `Parceiro`: `CODPARC` → `CODPARC`
  > `Contato` → `Parceiro2`: `TIMPROCURADOR` → `CODPARC`
  > `Contato` → `PerfilContato`: `CODPARC` → `CODPARC`, `CODCONTATO` → `CODCONTATO`
  > `Contato` → `TimProfissaoRamoAtividade`: `TIMPROFISSAO` → `PRFCODIGO`
  > `Contato` → `Bairro`: `CODBAI` → `CODBAI`
  > `Contato` → `Banco`: `TIMBANCO` → `CODBCO`
  > `Contato` → `Cidade`: `CODCID` → `CODCID`
  > `Contato` → `Endereco`: `CODEND` → `CODEND`
  > `Contato` → `Pais`: `TIMNACIONALIDAD` → `CODPAIS`
  > `Contato` → `Regiao`: `CODREG` → `CODREG`
  > `Contato` → `Usuario`: `CODUSU` → `CODUSU`

### TGFLOC

**Instâncias (entityName para JapeFactory):**
- `LocalBaixaMPProducao` — Local de Baixa de MP
- `LocalDestinoPerda` — LocalDestinoPerda
- `LocalDestinoProducao` — Local de Destino  do Produção
- `LocalDestinoProducao2` — Local de Destino Encadeada
- `LocalEstoque` — Local de Estoque
- `LocalEstoqueTerceiro` — Local Especifico Estoque Terceiros
- `LocalEstoqueWms` — Local para ajuste de estoque
- `LocalFinanceiro` — Local
- `LocalFinanceiroEntDest` — Local
- `LocalFinanceiroEntOrig` — Local Entrada Origem da TGFETA
- `LocalFinanceiroSaiDest` — Local
- `LocalFinanceiroSaiOrig` — Local Saida Origem da TGFETA
- `LocalMateriaPrima` — Locais Materia Prima
- `LocalOrigemProducao` — Local
- `LocalPadraoEconet` — Local Padrão Econet
- `LocalPadraoImportarXML` — Local padrão para importar XML

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `LocalFinanceiro` | `TGFNTA` | `NomeTabelasPreco` | inner (filha) | S | — |
| `LocalFinanceiro` | `TGFPAR` | `Parceiro` | inner (filha) | N | — |

  > `LocalFinanceiro` → `NomeTabelasPreco`: `CODTAB` → `CODTAB`
  > `LocalFinanceiro` → `Parceiro`: `CODPARC` → `CODPARC`

### TGFVOL

**Instâncias (entityName para JapeFactory):**
- `UndPrincipalTgwexp` — Unidade Principal
- `UnidadeCompra` — Unidade para compras
- `UnidadeMinArmazenagemWMS` — Unidade Minima de Armazenagem para WMS
- `Volume` — Unidade
- `VolumeFETHAB` — Volume FETHAB
- `VolumeKanban` — Unidade de movimentação padrão
- `VolumeResumoEntrega` — Volume para Resumo de Entrega

### TGFEST

**Instâncias (entityName para JapeFactory):**
- `Estoque` — Estoque

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Estoque` | `TGFEMP` | `EmpresaFinanceiro` | inner (filha) | S | — |
| `Estoque` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | S | — |
| `Estoque` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Estoque` | `TGFPRO` | `Produto` | inner (filha) | S | — |
| `Estoque` | `TSIEMP` | `Empresa` | inner (filha) | N | — |

  > `Estoque` → `EmpresaFinanceiro`: `CODEMP` → `CODEMP`
  > `Estoque` → `LocalFinanceiro`: `CODLOCAL` → `CODLOCAL`
  > `Estoque` → `Parceiro`: `CODPARC` → `CODPARC`
  > `Estoque` → `Produto`: `CODPROD` → `CODPROD`
  > `Estoque` → `Empresa`: `CODEMP` → `CODEMP`

### TGFORD

**Instâncias (entityName para JapeFactory):**
- `OrdemCarga` — Ordem de Carga

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `OrdemCarga` | `TGFCAB` | `CabecalhoNota` | inner (filha) | N | — |
| `OrdemCarga` | `TGFLOC` | `LocalFinanceiro` | inner (filha) | S | — |
| `OrdemCarga` | `TGFPAR` | `ParceiroOrigem` | inner (filha) | N | — |
| `OrdemCarga` | `TGFPAR` | `ParceiroDestino` | inner (filha) | N | — |
| `OrdemCarga` | `TGFPAR` | `Motorista` | inner (filha) | N | — |
| `OrdemCarga` | `TGFPAR` | `Transportadora` | inner (filha) | N | — |
| `OrdemCarga` | `TGFROM` | `RomaneioCarga` | inner (filha) | N | — |
| `OrdemCarga` | `TGFROT` | `Rota` | inner (filha) | S | — |
| `OrdemCarga` | `TGFTOP` | `TipoOperacao` | inner (filha) | N | — |
| `OrdemCarga` | `TGFVEI` | `Veiculo` | inner (filha) | S | — |
| `OrdemCarga` | `TGWDCA` | `Doca` | inner (filha) | S | — |
| `OrdemCarga` | `TSIEMP` | `Empresa` | inner (filha) | N | — |
| `OrdemCarga` | `TSIREG` | `Regiao` | inner (filha) | S | — |

  > `OrdemCarga` → `CabecalhoNota`: `ORDEMCARGA` → `ORDEMCARGA`
  > `OrdemCarga` → `LocalFinanceiro`: `CODLOCAL` → `CODLOCAL`
  > `OrdemCarga` → `ParceiroOrigem`: `CODPARCORIG` → `CODPARC`
  > `OrdemCarga` → `ParceiroDestino`: `CODPARCDEST` → `CODPARC`
  > `OrdemCarga` → `Motorista`: `CODPARCMOTORISTA` → `CODPARC`
  > `OrdemCarga` → `Transportadora`: `CODPARCTRANSP` → `CODPARC`
  > `OrdemCarga` → `RomaneioCarga`: `CODEMP` → `CODEMPOC`, `ORDEMCARGA` → `ORDEMCARGA`
  > `OrdemCarga` → `Rota`: `CODROTA` → `CODROTA`
  > `OrdemCarga` → `TipoOperacao`: `CODTIPOPERTRANSB` → `CODTIPOPER`
  > `OrdemCarga` → `Veiculo`: `CODVEICULO` → `CODVEICULO`
  > `OrdemCarga` → `Doca`: `CODDOCA` → `CODDOCA`
  > `OrdemCarga` → `Empresa`: `CODEMP` → `CODEMP`
  > `OrdemCarga` → `Regiao`: `CODREG` → `CODREG`

### TGFTIT

**Instâncias (entityName para JapeFactory):**
- `EspecieTitulo` — Especie do Tipo de Titulo
- `TipoTitulo` — Tipo de Titulo
- `TipoTituloArm` — Tipos de Titulo Armazenagem
- `TipoTituloExp` — Tipo de Titulo
- `TipoTituloIpi` — Tipo de Titulo

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `TipoTitulo` | `TCBPLA` | `PlanoContaConta3` | inner (filha) | N | — |
| `TipoTitulo` | `TCBPLA` | `PlanoConta2` | inner (filha) | N | — |
| `TipoTitulo` | `TCBPLA` | `PlanoConta` | inner (filha) | N | — |
| `TipoTitulo` | `TGFGTT` | `GruposTipoTitulo` | inner (filha) | N | — |
| `TipoTitulo` | `TGFPAR` | `Parceiro` | inner (filha) | N | — |
| `TipoTitulo` | `TGFRTT` | `RestricaoTipoTitulo` | inner (filha) | N | — |
| `TipoTitulo` | `TSIMOE` | `Moeda` | inner (filha) | N | — |

  > `TipoTitulo` → `PlanoContaConta3`: `CODCTACTB3` → `CODCTACTB`
  > `TipoTitulo` → `PlanoConta2`: `CODCTACTB2` → `CODCTACTB`
  > `TipoTitulo` → `PlanoConta`: `CODCTACTB` → `CODCTACTB`
  > `TipoTitulo` → `GruposTipoTitulo`: `CODGRUPOTIPTIT` → `CODGRUPOTIPTIT`
  > `TipoTitulo` → `Parceiro`: `CODPARCTEF` → `CODPARC`
  > `TipoTitulo` → `RestricaoTipoTitulo`: `CODTIPTIT` → `CODTIPTITORI`
  > `TipoTitulo` → `Moeda`: `CODMOEDA` → `CODMOEDA`

### TGFGRU

**Instâncias (entityName para JapeFactory):**
- `GrupoProduto` — Grupo Produto
- `GrupoProduto2` — Grupo Produto
- `GrupoProduto3` — GrupoProduto3

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `GrupoProduto` | `TCBPLA` | `PlanoConta` | lookup (chave estrangeira) | S | — |
| `GrupoProduto` | `TCSPRJ` | `Projeto` | inner (filha) | S | — |
| `GrupoProduto` | `TGFGEM` | `GrupoProdutoIcmsEmpresa` | inner (filha) | S | — |
| `GrupoProduto` | `TGFIMA` | `AliquotaImposto` | inner (filha) | S | — |
| `GrupoProduto` | `TGFNAT` | `Natureza` | inner (filha) | S | — |
| `GrupoProduto` | `TGFPRO` | `Produto` | inner (filha) | N | — |
| `GrupoProduto` | `TGFRGV` | `VendedorGrupoProduto` | inner (filha) | S | — |
| `GrupoProduto` | `TGFVCS` | `VendaCasada` | inner (filha) | N | — |
| `GrupoProduto` | `TGWRFA` | `RegraArmazenagem` | inner (filha) | N | — |
| `GrupoProduto` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |

  > `GrupoProduto` → `PlanoConta`: `CODCTACTBEFD` → `CODCTACTB`
  > `GrupoProduto` → `Projeto`: `CODPROJ` → `CODPROJ`
  > `GrupoProduto` → `GrupoProdutoIcmsEmpresa`: `CODGRUPOPROD` → `CODGRUPOPROD`
  > `GrupoProduto` → `AliquotaImposto`: `CODGRUPOPROD` → `CODIGO`, `TIPOIMPOSTO` → `TIPO`
  > `GrupoProduto` → `Natureza`: `CODNAT` → `CODNAT`
  > `GrupoProduto` → `Produto`: `CODGRUPOPROD` → `CODGRUPOPROD`
  > `GrupoProduto` → `VendedorGrupoProduto`: `CODGRUPOPROD` → `CODGRUPOPROD`
  > `GrupoProduto` → `VendaCasada`: `CODGRUPOPROD` → `CODORIG`
  > `GrupoProduto` → `RegraArmazenagem`: `CODRFA` → `CODRFA`
  > `GrupoProduto` → `CentroResultado`: `CODCENCUS` → `CODCENCUS`

### TGFFAM

**Instâncias (entityName para JapeFactory):**
- `FamiliaProduto` — Familia

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `FamiliaProduto` | `TGFPRO` | `Produto` | inner (filha) | N | — |

  > `FamiliaProduto` → `Produto`: `CODPRODFILHO` → `CODPROD`

### TGFTAB

**Instâncias (entityName para JapeFactory):**
- `TabelaPreco` — Tabela de Preco
- `TabelaPrecoMinimo` — Tabela de Preco Minimo
- `TabelaPrecoPF` — Tabela de Preco

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `TabelaPreco` | `TGFEXC` | `Excecao` | inner (filha) | S | DELETE |
| `TabelaPreco` | `TGFNTA` | `NomeTabelasPreco` | inner (filha) | N | INSERT, UPDATE |

  > `TabelaPreco` → `Excecao`: `NUTAB` → `NUTAB`
  > `TabelaPreco` → `NomeTabelasPreco`: `CODTAB` → `CODTAB`

### TGFNTA

**Instâncias (entityName para JapeFactory):**
- `NomeTabelasPreco` — Cadastro de Tabela de Preco
- `NomeTabelasPrecoFarPop` — Nome das Tabelas de Preco
- `NomeTabelasPrecoFilha` — Nome das Tabelas de Preco
- `NomeTabelasPrecoPmpf` — Nome das Tabelas de Preco

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `NomeTabelasPreco` | `TGFNTA` | `NomeTabelasPrecoFilha` | inner (filha) | N | — |
| `NomeTabelasPreco` | `TGFTAB` | `TabelaPreco` | inner (filha) | S | — |
| `NomeTabelasPreco` | `TGFTPP` | `Perfil` | inner (filha) | N | INSERT |
| `NomeTabelasPreco` | `TSIMOE` | `Moeda` | inner (filha) | N | — |
| `NomeTabelasPreco` | `TSIREG` | `Regiao` | inner (filha) | N | — |

  > `NomeTabelasPreco` → `NomeTabelasPrecoFilha`: `CODTABFLEX` → `CODTAB`
  > `NomeTabelasPreco` → `TabelaPreco`: `CODTAB` → `CODTAB`
  > `NomeTabelasPreco` → `Perfil`: `CODTIPPARC` → `CODTIPPARC`
  > `NomeTabelasPreco` → `Moeda`: `CODMOEDA` → `CODMOEDA`
  > `NomeTabelasPreco` → `Regiao`: `CODREG` → `CODREG`

### TGFVEI

**Instâncias (entityName para JapeFactory):**
- `Veiculo` — Veiculos
- `VeiculoReboque1` — Veiculo Reboque
- `VeiculoReboque2` — Veiculo Reboque2
- `VeiculoReboque3` — Veiculo Reboque3
- `VeiculoTracao` — Veiculo de Tração

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Veiculo` | `TCIBEM` | `Imobilizado` | inner (filha) | N | — |
| `Veiculo` | `TFPFUN` | `Funcionario` | inner (filha) | S | — |
| `Veiculo` | `TGFEVEVEI` | `EventoVeiculoCadastro` | inner (filha) | S | — |
| `Veiculo` | `TGFPAR` | `Motorista` | inner (filha) | S | — |
| `Veiculo` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Veiculo` | `TGFPRO` | `Produto` | inner (filha) | N | — |
| `Veiculo` | `TGFTFR` | `HistoricoVeiculo` | inner (filha) | N | — |
| `Veiculo` | `TPQQU1` | `QuestionarioVeiculo` | inner (filha) | N | — |
| `Veiculo` | `TSICID` | `Cidade` | inner (filha) | S | — |
| `Veiculo` | `TSICUS` | `CentroResultado` | inner (filha) | N | — |
| `Veiculo` | `TSIEMP` | `Empresa` | inner (filha) | N | — |
| `Veiculo` | `TSIFOR` | `Formula` | inner (filha) | S | — |

  > `Veiculo` → `Imobilizado`: `CODPROD` → `CODPROD`, `CODBEM` → `CODBEM`
  > `Veiculo` → `Funcionario`: `CODEMPFOLHA` → `CODEMP`, `CODFUNC` → `CODFUNC`
  > `Veiculo` → `EventoVeiculoCadastro`: `CODVEICULO` → `CODVEICULO`
  > `Veiculo` → `Motorista`: `CODMOTORISTA` → `CODPARC`
  > `Veiculo` → `Parceiro`: `CODPARCPROPANTT` → `CODPARC`
  > `Veiculo` → `Produto`: `CODPROD` → `CODPROD`
  > `Veiculo` → `HistoricoVeiculo`: `CODVEICULO` → `CODVEICULO`
  > `Veiculo` → `QuestionarioVeiculo`: `CODQUEST` → `CODQUEST`
  > `Veiculo` → `Cidade`: `CODCID` → `CODCID`
  > `Veiculo` → `CentroResultado`: `CODCENCUS` → `CODCENCUS`
  > `Veiculo` → `Empresa`: `CODEMPFOLHA` → `CODEMP`
  > `Veiculo` → `Formula`: `CODFORMFRETE` → `CODFORM`, `TIPFORMFRETE` → `TIPFORM`

### TGFCFO

**Instâncias (entityName para JapeFactory):**
- `ClaFiscalCombustivelLubrif` — Classificação Fiscal Operações Para Combustiveis e Lubrificantes
- `ClaFiscalOperacaoEntrada` — Classificação Fiscal de Operações Entrada
- `ClaFiscalOperacaoEntradaEstado` — Classificação Fiscal de Operações de Entrada de Fora do Estado.
- `ClaFiscalOperacaoSaida` — Classificação Fiscal de Operações Saida
- `ClaFiscalOperacaoSaidaEstado` — Classificação Fiscal de Operações de Saida de Fora do Estado
- `ClaFiscalOperacaoTerceiros` — Classificação Fiscal de Operações Para Produtos Terceiros
- `ClaFiscalPrestacaoServico` — Codigo Fiscal de Prestações de Servico
- `ClassificacaoFiscalOperacao` — Classificação Fiscal de Operações

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `ClassificacaoFiscalOperacao` | `TCBPLA` | `PlanoConta` | inner (filha) | N | — |
| `ClassificacaoFiscalOperacao` | `TCBPLA` | `PlanoContaConta` | inner (filha) | S | — |
| `ClassificacaoFiscalOperacao` | `TGFCLCAT42` | `CodLegalCat42PorCFOP` | inner (filha) | S | — |
| `ClassificacaoFiscalOperacao` | `TGFTAA` | `TermoAcordoApuracao` | inner (filha) | S | — |
| `ClassificacaoFiscalOperacao` | `TGFTCFOP` | `TributacoesPorCFOP` | inner (filha) | S | — |

  > `ClassificacaoFiscalOperacao` → `PlanoConta`: `CODCTACTB` → `CODCTACTB`
  > `ClassificacaoFiscalOperacao` → `PlanoContaConta`: `CODCTACTB` → `CODCTACTB`
  > `ClassificacaoFiscalOperacao` → `CodLegalCat42PorCFOP`: `CODCFO` → `CODCFO`
  > `ClassificacaoFiscalOperacao` → `TermoAcordoApuracao`: `CODCFO` → `CODCFO`
  > `ClassificacaoFiscalOperacao` → `TributacoesPorCFOP`: `CODCFO` → `CODCFO`

### TGFISS

**Instâncias (entityName para JapeFactory):**
- `AliquotaISS` — Aliquotas de ISS

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `AliquotaISS` | `TGFAIP` | `AliquotaISSParceiro` | inner (filha) | S | INSERT |
| `AliquotaISS` | `TGFLST` | `ListaServicoSintegra` | inner (filha) | N | — |
| `AliquotaISS` | `TGFPRO` | `Servico` | inner (filha) | S | — |
| `AliquotaISS` | `TSICID` | `Cidade` | inner (filha) | S | — |
| `AliquotaISS` | `TSIEMP` | `Empresa` | inner (filha) | N | — |

  > `AliquotaISS` → `AliquotaISSParceiro`: `CODPROD` → `CODPROD`, `CODEMP` → `CODEMP`, `CODCID` → `CODCID`
  > `AliquotaISS` → `ListaServicoSintegra`: `CODLST` → `CODLST`
  > `AliquotaISS` → `Servico`: `CODPROD` → `CODPROD`
  > `AliquotaISS` → `Cidade`: `CODCID` → `CODCID`
  > `AliquotaISS` → `Empresa`: `CODEMP` → `CODEMP`

### TGFGCB

**Instâncias (entityName para JapeFactory):**
- `GrupoCobranca` — Grupo Cobranca

### TSIUSU

**Instâncias (entityName para JapeFactory):**
- `Atendente` — Atendente
- `Executante` — Executante
- `ExecutanteRemetente` — Executante Remetente
- `Liberador` — Liberador
- `Responsavel` — Responsavel
- `Solicitante` — Solicitante
- `TimExecutanteSac` — Executantes do SAC
- `TimUsuarioAlteracao` — Usuario de Alteração
- `TimUsuarioInclusao` — Usuario de Inclusão
- `TimUsuarioOrigemSac` — Usuarios que lancaram o SAC
- `UltimoExecutante` — Ultimo Executante
- `Usuario` — Usuario
- `Usuario2` — Usuario 2
- `Usuario3` — Usuario ultima alteração
- `Usuario4` — Usuario responsavle cancelamento
- `UsuarioBaixa` — Usuario Baixa (Financeiro)
- `UsuarioCancelamento` — UsuarioCancelamento
- `UsuarioCobranca` — Unidade de Carregamento
- `UsuarioColeta` — Usuario Coleta
- `UsuarioComprador` — Usuario Comprador
- `UsuarioConferencia` — Usuario Conferencia
- `UsuarioFinal` — Usuario Final
- `UsuarioLiberacao` — Usuario Liberação
- `UsuarioPJLider` — Usuario PJ Lider
- `UsuarioProtocolo` — Usuario Protocolo
- `UsuarioResponsavel` — Usuario Responsavel
- `Usuario_AD001` — Usuario

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Usuario` | `TFPCGH` | `IdentificacaoCargaHoraria` | inner (filha) | N | — |
| `Usuario` | `TFPFUN` | `Funcionario` | inner (filha) | S | — |
| `Usuario` | `TGFCER` | `CertificacaoRegra` | inner (filha) | N | — |
| `Usuario` | `TGFCTT` | `Contato` | inner (filha) | N | — |
| `Usuario` | `TGFEQF` | `CadastroEquipamentoFiscal` | inner (filha) | S | — |
| `Usuario` | `TGFETA` | `EtapaProducao` | inner (filha) | N | — |
| `Usuario` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Usuario` | `TGFPAR` | `ParceiroPrestador` | inner (filha) | N | — |
| `Usuario` | `TGFQPR` | `QuantidadeParceiroUsuario` | inner (filha) | N | — |
| `Usuario` | `TGFSEU` | `ServicoProdutoExecutante` | inner (filha) | S | — |
| `Usuario` | `TGFTOP` | `TOPReceita` | inner (filha) | S | — |
| `Usuario` | `TGFTOP` | `TOPDespesa` | inner (filha) | S | — |
| `Usuario` | `TGFVEN` | `Vendedor` | inner (filha) | N | — |
| `Usuario` | `TGWUSU` | `UsuarioTarefa` | inner (filha) | N | — |
| `Usuario` | `TIMCOR` | `TimCorretor` | inner (filha) | S | — |
| `Usuario` | `TMIAUN` | `AcessoUnidadeGerencial` | inner (filha) | N | — |
| `Usuario` | `TSICUS` | `CentroResultado` | inner (filha) | S | — |
| `Usuario` | `TSIEMP` | `Empresa` | inner (filha) | S | — |
| `Usuario` | `TSIFIL` | `FilaImpressaoBoleta` | inner (filha) | N | — |
| `Usuario` | `TSIGPU` | `GruposPorUsuario` | inner (filha) | S | — |
| `Usuario` | `TSIGRU` | `GrupoUsuario` | inner (filha) | S | — |
| `Usuario` | `TSIRIM` | `RoteamentoImpressaoUsuario` | inner (filha) | N | — |
| `Usuario` | `TSISUPL` | `UsuarioSuplementar` | inner (filha) | N | — |
| `Usuario` | `TSIUCT` | `ContaUsuario` | inner (filha) | N | — |
| `Usuario` | `TSIUFI` | `FilaImpressaoTopUsuario` | inner (filha) | N | — |

  > `Usuario` → `IdentificacaoCargaHoraria`: `CODCARGAACESSO` → `CODCARGAHOR`
  > `Usuario` → `Funcionario`: `CODFUNC` → `CODFUNC`, `CODEMP` → `CODEMP`
  > `Usuario` → `CertificacaoRegra`: `CODUSU` → `CHAVE`
  > `Usuario` → `Contato`: `CODPARCPERFIL` → `CODPARC`, `CODCONTATOPERFIL` → `CODCONTATO`
  > `Usuario` → `CadastroEquipamentoFiscal`: `CODEQUIP` → `CODEQUIP`
  > `Usuario` → `EtapaProducao`: `CODETAPA` → `CODETAPA`
  > `Usuario` → `Parceiro`: `CODPARC` → `CODPARC`
  > `Usuario` → `ParceiroPrestador`: `CODPARCPERFIL` → `CODPARC`
  > `Usuario` → `QuantidadeParceiroUsuario`: `CODUSU` → `CODUSU`
  > `Usuario` → `ServicoProdutoExecutante`: `CODUSU` → `CODUSU`
  > `Usuario` → `TOPReceita`: `TOPBAIXARECEITA` → `CODTIPOPER`
  > `Usuario` → `TOPDespesa`: `TOPBAIXADESPESA` → `CODTIPOPER`
  > `Usuario` → `Vendedor`: `CODVEND` → `CODVEND`
  > `Usuario` → `UsuarioTarefa`: `CODUSU` → `CODUSU`
  > `Usuario` → `TimCorretor`: `CORCODIGO` → `CORCODIGO`
  > `Usuario` → `AcessoUnidadeGerencial`: `CODUSU` → `CODUSU`
  > `Usuario` → `CentroResultado`: `CODCENCUSPAD` → `CODCENCUS`
  > `Usuario` → `Empresa`: `CODEMP` → `CODEMP`
  > `Usuario` → `FilaImpressaoBoleta`: `NOMEFILA` → `NOMEFILA`
  > `Usuario` → `GruposPorUsuario`: `CODUSU` → `CODUSU`

### TSIEMP

**Instâncias (entityName para JapeFactory):**
- `Empresa` — Empresa
- `EmpresaBaixa` — Empresa para baixa
- `EmpresaCadastro` — Cadastro de Empresas
- `EmpresaContablidade` — Empresa Contabilidade
- `EmpresaDestinoEtapaProducao` — Empresa Destino
- `EmpresaFinanceira` — Empresa Financeiro
- `EmpresaFuncionario` — Empresa do funcionario
- `EmpresaFuncionarioLider` — Empresa Funcionario Lider
- `EmpresaGOL` — Empresa para agrupar no GOL
- `EmpresaMatriz` — Empresa Matriz
- `EmpresaMatrizGnre` — Empresa Matriz para GNRE
- `EmpresaMatrizNfse` — Empresa Matriz para Nfse
- `EmpresaModelo` — Empresa Modelo
- `EmpresaNegociacao` — Empresa da Negociação
- `EmpresaOrganograma` — Empresa de Organograma
- `EmpresaOrigemEtapaProducao` — Empresa Origem
- `EmpresaOrigemFuncionario` — Empresa origem do funcionario
- `EmpresaPreferencial` — Empresa Preferencial do parceiro
- `EmpresaSoma` — EmpresaSoma
- `EmpresaSubstituido` — EmpresaSubstituido
- `ImovelRural` — Imovel Rural
- `TLFEmpresaOrigemMovimentoLivro` — Empresa Origem
- `TimEmpresa` — Empresa

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Empresa` | `TFPEMP` | `EmpresaPessoal` | inner (filha) | N | — |
| `Empresa` | `TGFCER` | `CertificacaoRegra` | inner (filha) | N | — |
| `Empresa` | `TGFEMP` | `EmpresaFinanceiro` | inner (filha) | N | — |
| `Empresa` | `TGFIMA` | `AliquotaImposto` | inner (filha) | N | — |
| `Empresa` | `TGFLCR` | `LocalRetirada` | inner (filha) | S | — |
| `Empresa` | `TGFPAR` | `FuncionarioTomador` | inner (filha) | N | — |
| `Empresa` | `TSIBAI` | `Bairro` | inner (filha) | S | — |
| `Empresa` | `TSICID` | `Cidade` | inner (filha) | S | — |
| `Empresa` | `TSIEMP` | `EmpresaGOL` | inner (filha) | N | — |
| `Empresa` | `TSIEMP` | `EmpresaMatriz` | inner (filha) | N | — |
| `Empresa` | `TSIEND` | `Endereco` | inner (filha) | S | — |
| `EmpresaCadastro` | `TFPCHQ` | `ChequeCancelado` | inner (filha) | N | — |
| `EmpresaCadastro` | `TFPEMP` | `EmpresaPessoal` | inner (filha) | N | — |
| `EmpresaFuncionarioLider` | `TFPEMP` | `EmpresaPessoal` | inner (filha) | S | — |
| `EmpresaNegociacao` | `TFPEMP` | `EmpresaPessoal` | inner (filha) | N | — |
| `EmpresaSoma` | `TGFPAR` | `Parceiro` | inner (filha) | N | — |
| `EmpresaSoma` | `TSICID` | `Cidade` | inner (filha) | N | — |

  > `Empresa` → `EmpresaPessoal`: `CODEMP` → `CODEMP`
  > `Empresa` → `CertificacaoRegra`: `CODEMP` → `CHAVE`, `TIPOREGRA` → `TIPO`
  > `Empresa` → `EmpresaFinanceiro`: `CODEMP` → `CODEMP`
  > `Empresa` → `AliquotaImposto`: `CODEMP` → `CODIGO`
  > `Empresa` → `LocalRetirada`: `CODEMP` → `CODEMP`
  > `Empresa` → `FuncionarioTomador`: `CODPARC` → `CODPARC`
  > `Empresa` → `Bairro`: `CODBAI` → `CODBAI`
  > `Empresa` → `Cidade`: `CODCID` → `CODCID`
  > `Empresa` → `EmpresaGOL`: `EMPAGRUPARGOL` → `CODEMP`
  > `Empresa` → `EmpresaMatriz`: `CODEMPMATRIZ` → `CODEMP`
  > `Empresa` → `Endereco`: `CODEND` → `CODEND`
  > `EmpresaCadastro` → `ChequeCancelado`: `CODEMP` → `CODEMP`
  > `EmpresaCadastro` → `EmpresaPessoal`: `CODEMP` → `CODEMP`
  > `EmpresaFuncionarioLider` → `EmpresaPessoal`: `CODEMP` → `CODEMP`
  > `EmpresaNegociacao` → `EmpresaPessoal`: `CODEMP` → `CODEMP`
  > `EmpresaSoma` → `Parceiro`: `CODPARC` → `CODPARC`
  > `EmpresaSoma` → `Cidade`: `CODCID` → `CODCID`

### TSICTA

**Instâncias (entityName para JapeFactory):**
- `ContaBancaria` — Conta Bancaria
- `ContaBancariaDespesa` — Contas Bancarias para Despesas
- `ContaBancariaIpi` — Conta Bancaria
- `ContaBancariaReceita` — Contas Bancarias para Receitas
- `ContaBancarioFgts` — ContaBancarioFgts
- `ContaDestino` — Conta de destino
- `ImplantacaoSaldoConta` — Implantação dos saldos de conta
- `TimContaBancaria` — Conta Bancaria

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `ContaBancaria` | `TCBPLA` | `PlanoContaEmpresa` | inner (filha) | S | — |
| `ContaBancaria` | `TGFCBS` | `CEPsBancoSafra` | inner (filha) | N | — |
| `ContaBancaria` | `TGFCOC` | `ConvenioConta` | inner (filha) | N | — |
| `ContaBancaria` | `TGFHBC` | `HistoricoBancario` | inner (filha) | S | — |
| `ContaBancaria` | `TGFMON` | `ModeloNotaFiscal` | inner (filha) | S | — |
| `ContaBancaria` | `TGFPAR` | `Parceiro` | inner (filha) | S | INSERT |
| `ContaBancaria` | `TGFTOP` | `TipoOperacaoBaixa` | inner (filha) | S | — |
| `ContaBancaria` | `TSIAGE` | `AgenciaBancaria` | inner (filha) | S | — |
| `ContaBancaria` | `TSIBCO` | `Banco` | inner (filha) | N | — |
| `ContaBancaria` | `TSIBCO` | `CorrespondenteBancario` | inner (filha) | N | — |
| `ContaBancaria` | `TSICTA` | `ContaDestino` | inner (filha) | N | — |
| `ContaBancaria` | `TSICTA` | `ContaBancaria` | inner (filha) | S | — |
| `ContaBancaria` | `TSICTA` | `ContaBancariaDespesa` | inner (filha) | N | — |
| `ContaBancaria` | `TSIEMP` | `Empresa` | inner (filha) | S | — |
| `ContaBancaria` | `TSIMOE` | `Moeda` | inner (filha) | S | — |
| `ContaBancaria` | `TSIUSU` | `Usuario` | inner (filha) | S | — |
| `ContaBancaria` | `TSIUSU` | `Usuario2` | inner (filha) | N | — |
| `ContaDestino` | `TSIBCO` | `Banco` | inner (filha) | N | — |

  > `ContaBancaria` → `PlanoContaEmpresa`: `CODCTACTB` → `CODCTACTB`
  > `ContaBancaria` → `CEPsBancoSafra`: `CODCTABCOINT` → `CODCTABCOINT`
  > `ContaBancaria` → `ConvenioConta`: `CODCTABCOINT` → `CODCTABCOINT`
  > `ContaBancaria` → `HistoricoBancario`: `CODLANCBAIXABOLRAP` → `CODLANC`
  > `ContaBancaria` → `ModeloNotaFiscal`: `MODBOLETA` → `CODMODNF`
  > `ContaBancaria` → `Parceiro`: `CODPARC` → `CODPARC`
  > `ContaBancaria` → `TipoOperacaoBaixa`: `CODTIPOPERBAIXABOLRAP` → `CODTIPOPER`
  > `ContaBancaria` → `AgenciaBancaria`: `CODBCO` → `CODBCO`, `CODAGE` → `CODAGE`
  > `ContaBancaria` → `Banco`: `CODBCO` → `CODBCO`
  > `ContaBancaria` → `CorrespondenteBancario`: `CODCORRBCO` → `CODBCO`
  > `ContaBancaria` → `ContaDestino`: `CODCTABCOINTREM` → `CODCTABCOINT`
  > `ContaBancaria` → `ContaBancaria`: `CODCTABAIXA` → `CODCTABCOINT`
  > `ContaBancaria` → `ContaBancariaDespesa`: `CTAMINBOLETA` → `CODCTABCOINT`
  > `ContaBancaria` → `Empresa`: `CODEMP` → `CODEMP`
  > `ContaBancaria` → `Moeda`: `CODMOEDA` → `CODMOEDA`
  > `ContaBancaria` → `Usuario`: `CODUSU` → `CODUSU`
  > `ContaBancaria` → `Usuario2`: `CODOPEREXCL` → `CODUSU`
  > `ContaDestino` → `Banco`: `CODBCO` → `CODBCO`

### TSICUS

**Instâncias (entityName para JapeFactory):**
- `CentroResultado` — Centro de Resultado
- `CentroResultadoArm` — Centros de Resultado Armazenagem
- `CentroResultadoDespesa` — Centro de Resultado Despesa
- `CentroResultadoEFDEmpresa` — Centro Resultado
- `CentroResultadoExp` — Centros de Resultado Armazenagem
- `CentroResultadoFinal` — Centro de Resultado Final
- `CentroResultadoIpi` — Centro de Resultado
- `TimCentroResultadoAdm` — Centro Resultado
- `TimCentroResultadoCorresBanc` — Centro Resultado
- `TimCentroResultadoIncorporador` — Centro Resultado
- `TimCentroResultadoLoteamento` — Centro Resultado
- `TimCentroResultadoRevenda` — Centro Resultado
- `TimCentroResultadoVenda` — Centro Resultado

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `CentroResultado` | `TGFNTA` | `NomeTabelasPreco` | inner (filha) | S | — |
| `CentroResultado` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `CentroResultado` | `TGFPAR` | `ParceiroResponsavel` | inner (filha) | N | — |
| `CentroResultado` | `TGFUNN` | `UnidadeNegocio` | inner (filha) | N | — |
| `CentroResultado` | `TMIUNG` | `UnidadeGerencial` | inner (filha) | S | — |
| `CentroResultado` | `TSILOR` | `LimiteOrcamentarioCR` | inner (filha) | S | — |
| `CentroResultado` | `TSIUSU` | `Usuario` | inner (filha) | N | — |

  > `CentroResultado` → `NomeTabelasPreco`: `CODTAB` → `CODTAB`
  > `CentroResultado` → `Parceiro`: `CODPARC` → `CODPARC`
  > `CentroResultado` → `ParceiroResponsavel`: `CODPARCRESP` → `CODPARC`
  > `CentroResultado` → `UnidadeNegocio`: `CODUNN` → `CODUNN`
  > `CentroResultado` → `UnidadeGerencial`: `CODUNG` → `CODUNG`
  > `CentroResultado` → `LimiteOrcamentarioCR`: `CODCENCUS` → `CODCENCUS`
  > `CentroResultado` → `Usuario`: `CODUSURESP` → `CODUSU`

### TSICID

**Instâncias (entityName para JapeFactory):**
- `Cidade` — Cidade
- `CidadeDestino` — Cidade de Destino
- `CidadeFatoGerador` — Municipio do Fato Gerador
- `CidadeMunicipioFinal` — Municipio de Descarregamento
- `CidadeMunicipioInicial` — Municipio de Coleta
- `CidadeOrigem` — Cidade de Origem
- `CidadeRecebimento` — Cidade para Recebimento
- `CidadeTrabalho` — Cidade Trabalho
- `FuncionarioCidadeNascimento` — Funcionario Cidade de Nascimento
- `FuncionarioNaturalidadeMae` — Naturalidade da Me do Funcionario
- `NaturalidadeParceiro` — Naturalidade do Parceiro
- `TimCidadeImovel` — Cidades dos imoveis

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Cidade` | `TGFISS` | `AliquotaISS` | inner (filha) | N | — |
| `Cidade` | `TGFPAR` | `Parceiro` | inner (filha) | S | — |
| `Cidade` | `TGFRCD` | `SequenciaEntrega` | inner (filha) | N | — |
| `Cidade` | `TSICAN` | `CancelamentoNFSe` | inner (filha) | S | — |
| `Cidade` | `TSIREG` | `Regiao` | inner (filha) | S | — |
| `Cidade` | `TSIUFS` | `UnidadeFederativa` | inner (filha) | S | — |

  > `Cidade` → `AliquotaISS`: `CODCID` → `CODCID`
  > `Cidade` → `Parceiro`: `CODPARCNFSE` → `CODPARC`
  > `Cidade` → `SequenciaEntrega`: `CODCID` → `CODCID`
  > `Cidade` → `CancelamentoNFSe`: `CODCID` → `CODCID`
  > `Cidade` → `Regiao`: `CODREG` → `CODREG`
  > `Cidade` → `UnidadeFederativa`: `UF` → `CODUF`

### TSIUFS

**Instâncias (entityName para JapeFactory):**
- `UnidadeFederativa` — Unidade Federativa
- `UnidadeFederativaDestino` — Unidade Federativa Destino
- `UnidadeFederativaEmissao` — Unidade Federativa Emissão
- `UnidadeFederativaOrigem` — Unidade Federativa Origem
- `UnidadeFederativa_AD001` — Unidade Federativa

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `UnidadeFederativa` | `TGFPAR` | `Parceiro` | inner (filha) | N | — |
| `UnidadeFederativa` | `TGFTIT` | `TipoTitulo` | inner (filha) | S | — |
| `UnidadeFederativa` | `TSIGUF` | `GNREUnidadeFederativa` | inner (filha) | S | — |
| `UnidadeFederativa` | `TSIPAI` | `Pais` | inner (filha) | S | — |
| `UnidadeFederativa` | `TSIUFU` | `UnidadesFiscaisPorUF` | inner (filha) | S | — |

  > `UnidadeFederativa` → `Parceiro`: `CODPARCSECRECEST` → `CODPARC`
  > `UnidadeFederativa` → `TipoTitulo`: `TIPTITGNREFCPST` → `CODTIPTIT`
  > `UnidadeFederativa` → `GNREUnidadeFederativa`: `CODUF` → `CODUF`
  > `UnidadeFederativa` → `Pais`: `CODPAIS` → `CODPAIS`
  > `UnidadeFederativa` → `UnidadesFiscaisPorUF`: `CODUF` → `CODUF`

### TSIBCO

**Instâncias (entityName para JapeFactory):**
- `Banco` — Banco
- `BancoIpi` — Banco
- `CorrespondenteBancario` — Correspondente Bancario
- `TimBanco` — Banco

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Banco` | `TGFCMC7` | `PrefixoCheque` | lookup (chave estrangeira) | S | DELETE |

  > `Banco` → `PrefixoCheque`: `CODBCO` → `CODBCO`

### TSIBAI

**Instâncias (entityName para JapeFactory):**
- `Bairro` — Bairro
- `BairroRecebimento` — Bairro para recebimento
- `BairroTrabalho` — Bairro Trabalho
- `TimBairroImovel` — Bairros dos imoveis
- `TimBairroImovel2` — Bairros com Imoveis

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Bairro` | `TSIREG` | `Regiao` | inner (filha) | S | — |

  > `Bairro` → `Regiao`: `CODREG` → `CODREG`

### TSIEND

**Instâncias (entityName para JapeFactory):**
- `Endereco` — Endereco
- `EnderecoRecebimento` — Endereco de Recebimento
- `EnderecoTrabalho` — Endereco de Trabalho
- `TimEndereco` — Enderecos com Imoveis

**Ligações lógicas:**

| Instância Origem | Tabela Destino | Instância Destino | Tipo | Obrig | Cascata |
|---|---|---|---|---|---|
| `Endereco` | `TFPLGR` | `Logradouro` | inner (filha) | S | — |
| `Endereco` | `TSITEND` | `TipoEndereco` | inner (filha) | N | — |

  > `Endereco` → `Logradouro`: `CODLOGRADOURO` → `CODLOGRADOURO`
  > `Endereco` → `TipoEndereco`: `TIPO` → `TIPO`
