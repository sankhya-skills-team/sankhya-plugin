# Metamodelo Sankhya — Tabelas TDD

As tabelas `TDD*` formam o **metamodelo interno do Sankhya OM** — definem tabelas,
campos, instâncias, menus, relacionamentos e permissões. São lidas pela plataforma
em tempo de execução para montar telas, validar permissões e resolver navegação.

> **Regra:** Nunca escrever diretamente nessas tabelas em código customizado.
> Usar Construtor de Telas ou `datadictionary/` do Addon Studio.

### TDDCAM
**Descrição de Campos**

**PK:** `NUCAMPO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REQUERIDO` | Texto | Requerido |  |
| `NUCAMPO` 🔑 | Inteiro | Num. do campo |  |
| `NOMETAB` | Texto | Nome da Tabela Pai |  |
| `NOMECAMPO` | Texto | Nome do campo |  |
| `DESCRCAMPO` | Texto | Descrição do campo |  |
| `TIPCAMPO` | Texto | Tipo do Campo |  |
| `MASCARA` | Texto | Mascara |  |
| `EXPRESSAO` | Texto | Expressão |  |
| `PERMITEPESQUISA` | Texto | Permite pesquisa |  |
| `CALCULADO` | Texto | Campo calculado |  |
| `PERMITEPADRAO` | Texto | Permite padrão |  |
| `APRESENTACAO` | Texto | Campo Apresentação |  |
| `ORDEM` | Inteiro | Ordem |  |
| `VISIVELGRIDPESQUISA` | Texto | Aparece no grid de pesquisa |  |
| `TAMANHO` | Inteiro | Tamanho |  |
| `TIPOAPRESENTACAO` | Texto | Tipo de apresentação |  |
| `SISTEMA` | Texto | Campo de sistema |  |
| `ADICIONAL` | Texto | Adicional |  |

### TDDCAMI18N
**Descrição de Campos (Internacional)**

**PK:** `NOMETAB`, `NOMECAMPO`, `LOCALE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMETAB` 🔑 | Texto | Nome da Tabela |  |
| `NOMECAMPO` 🔑 | Texto | Nome do Campo |  |
| `LOCALE` 🔑 | Texto | Linguagem |  |
| `TEXTO` | Texto | Texto |  |

### TDDI18N
**Verbetes Internacionais de Uso Geral**

**PK:** `CHAVE`, `LOCALE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CHAVE` 🔑 | Texto | Chave |  |
| `LOCALE` 🔑 | Texto | Linguagem |  |
| `TEXTO` | Texto | Texto |  |

### TDDINS
**Mapeamento de Instancias**

**PK:** `NUINSTANCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUINSTANCIA` 🔑 | Inteiro | Num. da Instancia |  |
| `NOMEINSTANCIA` | Texto | Nome da Instancia |  |
| `DESCRINSTANCIA` | Texto | Descrição da Instancia |  |
| `NOMETAB` | Texto | Nome da Tabela |  |
| `RAIZ` | Texto | Raiz |  |
| `FILTRO` | Texto | Filtro |  |
| `ATIVO` | Texto | Instancia e Ativa |  |
| `EXPRESSAO` | Texto | Expressão |  |
| `NUINSTANCIAPAI` | Inteiro | Num. Instancia Pai |  |
| `NOMESCRIPTCHAVE` | Texto | Nome Script Chave |  |
| `NUINSTANCIAEXT` | Inteiro | Instancia de Extensão |  |
| `ADICIONAL` | Texto | Campo Adicional |  |
| `RESOURCEID` | Texto | ID do cadastro |  |
| `DEFINICAOINST` | Texto | Definição Instancia |  |
| `ISLIB` | Texto | isLib |  |
| `DESCRTELA` | Texto | DESCRTELA |  |
| `CATEGORIA` | Texto | CATEGORIA |  |
| `TIPOFORM` | Texto | TIPOFORM |  |

### TDDINSI18N
**Descrição de Instancias (Internacional)**

**PK:** `NOMEINSTANCIA`, `LOCALE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMEINSTANCIA` 🔑 | Texto | Nome da Instancia |  |
| `LOCALE` 🔑 | Texto | Linguagem |  |
| `TEXTO` | Texto | Texto |  |

### TDDLGC
**Campos de ligação**

**PK:** `NUINSTORIG`, `NUCAMPOORIG`, `NUINSTDEST`, `NUCAMPODEST`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUINSTORIG` 🔑 | Inteiro | Num. Instancia origem |  |
| `NUCAMPOORIG` 🔑 | Inteiro | Num. campo origem |  |
| `NUINSTDEST` 🔑 | Inteiro | Num. Instancia destino |  |
| `NUCAMPODEST` 🔑 | Inteiro | Num. campo destino |  |
| `ORIG_OBRIGATORIA` | Texto | Origem obrigatoria |  |
| `ORDEM` | Inteiro | Ordem do campo na ligação |  |

### TDDLIG
**Ligação de tabelas**

**PK:** `NUINSTORIG`, `NUINSTDEST`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUINSTORIG` 🔑 | Inteiro | Numero da instancia de origem |  |
| `NUINSTDEST` 🔑 | Inteiro | Numero da instancia de destino |  |
| `TIPLIGACAO` | Texto | Tipo de Ligação |  |
| `EXPRESSAO` | Texto | Expressão |  |
| `INSERIR` | Texto | Inserir |  |
| `ALTERAR` | Texto | Alterar |  |
| `EXCLUIR` | Texto | Excluir |  |
| `OBRIGATORIA` | Texto | Obrigatoria |  |
| `CONDICAO` | Texto | Condição |  |
| `ADICIONAL` | Texto | Adicional |  |
| `NOMELIGACAO` | Texto | Nome da ligação |  |

### TDDOPC
**Opção de campos**

**PK:** `NUCAMPO`, `VALOR`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCAMPO` 🔑 | Inteiro | NUCAMPO |  |
| `VALOR` 🔑 | Texto | VALOR |  |
| `OPCAO` | Texto | OPCAO |  |
| `PADRAO` | Texto | PADRAO |  |
| `ORDEM` | Inteiro | ORDEM |  |

### TDDOPCI18N
**Opção de campos (Internacional)**

**PK:** `NOMETAB`, `NOMECAMPO`, `VALOR`, `LOCALE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMETAB` 🔑 | Texto | Nome da Tabela |  |
| `NOMECAMPO` 🔑 | Texto | Nome do Campo |  |
| `VALOR` 🔑 | Texto | Valor da Opção |  |
| `LOCALE` 🔑 | Texto | Linguagem |  |
| `TEXTO` | Texto | Texto |  |

### TDDPCO
**Atributos de campo**

**PK:** `NUCAMPO`, `NOME`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCAMPO` 🔑 | Inteiro | Numero do campo |  |
| `NOME` 🔑 | Texto | Nome |  |
| `VALOR` | Texto | Valor |  |

### TDDPERBK
**Backup Permissão**

**PK:** `NUNICO`, `CODUSU`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNICO` 🔑 | Inteiro | NUNICO |  |
| `CODUSU` 🔑 | Inteiro | Cod. Usuario |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `IDACESSO` | Texto | IDACESSO |  |
| `CODGRUPO` | Inteiro | CODGRUPO |  |
| `ACESSO` | Texto | ACESSO |  |
| `VERSAO` | Inteiro | VERSAO |  |

### TDDPIN
**Propriedades de Instancia**

**PK:** `NUINSTANCIA`, `NOME`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUINSTANCIA` 🔑 | Inteiro | NUINSTANCIA |  |
| `NOME` 🔑 | Texto | NOME |  |
| `VALOR` | Texto | VALOR |  |
| `FROMUSER` | Texto | FROMUSER |  |

### TDDTAB
**Descrição de Tabelas**

**PK:** `NOMETAB`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMETAB` 🔑 | Texto | Nome da Tabela |  |
| `DESCRTAB` | Texto | Descrição da Tabela |  |
| `TIPONUMERACAO` | Texto | Tipo de Numeração |  |
| `NUCAMPONUMERACAO` | Inteiro | Cod. Campo Numeração |  |
| `ADICIONAL` | Texto | Adicional |  |

### TDDTABI18N
**Descrição de Tabelas (Internacional)**

**PK:** `NOMETAB`, `LOCALE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMETAB` 🔑 | Texto | Nome da Tabela |  |
| `LOCALE` 🔑 | Texto | Linguagem |  |
| `TEXTO` | Texto | Texto |  |

## Instâncias das Tabelas Principais (TDDINS)

| Tabela | Instância (entityName) | Descrição |
|---|---|---|
| `TGFCAB` | `CabecalhoFox` | Nota venda do Checkout |
| `TGFCAB` | `CabecalhoNota` | Nota/Pedido |
| `TGFCAB` | `CabecalhoNota2` | Nota/Pedido |
| `TGFCAB` | `CabecalhoNota3` | Nota/Pedido |
| `TGFCAB` | `CabecalhoNotaBaixa` | Nota de Baixa |
| `TGFCAB` | `CabecalhoNotaDevVenda` | Nota Devolução Venda |
| `TGFCAB` | `CabecalhoNotaModelo` | Cabecalho Nota Modelo |
| `TGFCAB` | `CabecalhoNotaModeloAgenda` | Modelo de Notas e Pedidos |
| `TGFCAB` | `CabecalhoNotaModeloSaida` | Modelo de nota de saida |
| `TGFCAB` | `CabecalhoNotaModeloSaidaBem` | Modelo de nota de saida Bem |
| `TGFCAB` | `CabecalhoNotaRetorno` | Nota Retorno |
| `TGFCAB` | `CabecalhoNotaSaida` | Nota de Saida |
| `TGFCAB` | `CabecalhoNotaWmsEnt` | Nota modelo sobra estoque WMS (Entrada) |
| `TGFCAB` | `CabecalhoNotaWmsSai` | Nota modelo perda estoque WMS (Saida) |
| `TGFCAB` | `CabecalhoNotaModelo2` | CabecalhoNotaModelo2 |
| `TGFCAB` | `ModeloEntradaEstoqueComTerc` | Modelo Ajuste de Entrada de Estoque com Terceiros |
| `TGFCAB` | `ModeloEntradaEstoqueConsignado` | Modelo Ajuste de Entrada de Estoque Consignado |
| `TGFCAB` | `ModeloEntradaEstoqueDeTerc` | Modelo Ajuste de Entrada de Estoque de Terceiros |
| `TGFCAB` | `ModeloEntradaReclassificacao` | Modelo Ajuste de Entrada Reclassificação (Registro K220) |
| `TGFCAB` | `ModeloEstornoWMSDevCompra` | Modelo Estorno WMS - Dev Compra |
| `TGFCAB` | `ModeloRetornoEstoqueWMS` | Modelo Retor. de Est. Gerencial WMS(Venda) |
| `TGFCAB` | `ModeloSaidaEstoqueComTerc` | Modelo Ajuste de Saida de Estoque com Terceiros |
| `TGFCAB` | `ModeloSaidaEstoqueConsignado` | Modelo Ajuste de Saida de Estoque Consignado |
| `TGFCAB` | `ModeloSaidaEstoqueDeTerc` | Modelo Ajuste de Saida de Estoque de Terceiros |
| `TGFCAB` | `ModeloSaidaReclassificacao` | Modelo Ajuste de Saida Reclassificação (Registro K220) |
| `TGFITE` | `ItemNota` | Item Nota/Pedido |
| `TGFITE` | `ItemNotaOrigem` | Item da Nota de Origem |
| `TGFITE` | `ItensFox` | Item da Nota de Checkout |
| `TGFFIN` | `Financeiro` | Financeiro |
| `TGFFIN` | `TimFinanceiro` | Financeiro |
| `TGFFIN` | `TimFinanceiroAluguel` | Financeiro Aluguel |
| `TGFFIN` | `TimFinanceiroRepasse` | Financeiro Repasse |
| `TGFPAR` | `FuncionarioTomador` | Funcionario Tomador |
| `TGFPAR` | `GrupoEconomico` | Grupo Economico |
| `TGFPAR` | `Motorista` | Motorista do Veiculo |
| `TGFPAR` | `Parceiro` | Parceiro |
| `TGFPAR` | `Parceiro2` | Parceiro |
| `TGFPAR` | `ParceiroAdministrador` | Parc. Administradora |
| `TGFPAR` | `ParceiroAtendido` | Parceiro Atendido |
| `TGFPAR` | `ParceiroAtivoPj` | Parceiro |
| `TGFPAR` | `ParceiroColeta` | Parceiro Coleta CT-e |
| `TGFPAR` | `ParceiroConsignatario` | Parceiro Consignatario |
| `TGFPAR` | `ParceiroDescargaMdfe` | Parceiro Descarregamento (MDF-e) |
| `TGFPAR` | `ParceiroDestinatario` | Parceiro Destinatario CT-e |
| `TGFPAR` | `ParceiroDestino` | Parceiro Destino |
| `TGFPAR` | `ParceiroEntrega` | Parceiro Entrega CT-e |
| `TGFPAR` | `ParceiroExpedidor` | Parceiro Expedidor CT-e |
| `TGFPAR` | `ParceiroF2` | Parceiro F2 |
| `TGFPAR` | `ParceiroFabricante` | ParceiroFabricante |
| `TGFPAR` | `ParceiroFornecAprovado` | Fornecedor Aprovado |
| `TGFPAR` | `ParceiroFornecedor` | Parceiro Fornecedor |
| `TGFPAR` | `ParceiroFornecedorCotacao` | Fornecedor |
| `TGFPAR` | `ParceiroIntermed` | Parceiro Destino |
| `TGFPAR` | `ParceiroIntermediador` | Parc. Intermediador |
| `TGFPAR` | `ParceiroMatriz` | Parceiro Matriz |
| `TGFPAR` | `ParceiroMelhorFornec` | Melhor Fornecedor |
| `TGFPAR` | `ParceiroOrigem` | Parceiro de Origem |
| `TGFPAR` | `ParceiroPagante` | Parceiro Pagante |
| `TGFPAR` | `ParceiroPgtoFrete` | Parceiro |
| `TGFPAR` | `ParceiroPrestador` | Parceiro Prestador utilizado em contratos com SLA |
| `TGFPAR` | `ParceiroRecebedor` | Parceiro Recebedor CT-e |
| `TGFPAR` | `ParceiroRedespacho` | Parceiro Redespacho |
| `TGFPAR` | `ParceiroRemetente` | Parceiro Remetente |
| `TGFPAR` | `ParceiroRemetenteCte` | Parceiro Remetente CT-e |
| `TGFPAR` | `ParceiroResponsavel` | Parceiro Responsavel |
| `TGFPAR` | `ParceiroRetirada` | Parceiro Retirada |
| `TGFPAR` | `ParceiroTransportadora` | Parceiro Transportadora NF-e |
| `TGFPAR` | `ParceiroTransportadora2` | Parceiro Transportadora NF-e |
| `TGFPAR` | `Procedencia` | Procedencia de pesagem |
| `TGFPAR` | `ResponsavelPagador` | Parceiro Responsavel pelo Pagamento |
| `TGFPAR` | `TimProprietarioImovel` | Proprietarios dos imoveis |
| `TGFPAR` | `Transportadora` | Transportadora |
| `TGFPAR` | `TransportadoraFinal` | Transportadora Final |
| `TGFPRO` | `Produto` | Produto |
| `TGFPRO` | `Produto3` | Produto |
| `TGFPRO` | `ProdutoApontamento1` | Produto/servico para agrupar apontamento 1 |
| `TGFPRO` | `ProdutoApontamento2` | Produto/servico para agrupar apontamento 2 |
| `TGFPRO` | `ProdutoEspecifico` | Produto Especifico |
| `TGFPRO` | `ProdutoIntermediario` | Produto Intermediario |
| `TGFPRO` | `ProdutoMateriaPrima` | Materia Prima |
| `TGFPRO` | `ProdutoSubstituido` | ProdutoSubstituido |
| `TGFPRO` | `ProdutoSubstitutoKit` | Produto Substituto do Kit |
| `TGFPRO` | `Servico` | Servico |
| `TGFPRO` | `TarifasCIP` | Tarifas CIP |
| `TGFPRO` | `TimServicoTxAdm` | Servico |
| `TGFEMP` | `EmpresaFinanceiro` | Empresa Financeiro |
| `TGFTOP` | `TOPDespesa` | TOPDespesa |
| `TGFTOP` | `TOPReceita` | TOPReceita |
| `TGFTOP` | `TipoOperacao` | Tipo de Operação |
| `TGFTOP` | `TipoOperacao2` | Tipo de Operação |
| `TGFTOP` | `TipoOperacao3` | Tipo de Operação de (Requisição) |
| `TGFTOP` | `TipoOperacaoBaixa` | Tipo de Operação para Baixa |
| `TGFTOP` | `TipoOperacaoDenegada` | TOP para NF-e Denegada: |
| `TGFTOP` | `TipoOperacaoDenegadaCTe` | TOP para CT-e Denegada: |
| `TGFTOP` | `TipoOperacaoDestino` | Tipo de Operação Destino |
| `TGFTOP` | `TipoOperacaoEFDEmpresa` | Tipo Operação |
| `TGFTOP` | `TipoOperacaoEntrMerc` | TOP de entrada de mercadorias |
| `TGFTOP` | `TipoOperacaoIpi` | Tipo de Operação |
| `TGFTOP` | `TipoOperacaoPedidoAgrupa` | TOP pedido agrupado p/ enviar ao WMS |
| `TGFTOP` | `TipoOperacaoPerda` | TipoOperacaoPerda |
| `TGFTOP` | `TipoOperacaoRetorno` | Tipo de operação pendente de retorno. |
| `TGFTOP` | `TopAtendimento` | Top de Antedimento |
| `TGFTOP` | `TopBackorder` | Top de Back order |
| `TGFTOP` | `TopEntrada` | Top de Entrada |
| `TGFTOP` | `TopPrincipal` | Tipo Operação Principal |
| `TGFTOP` | `TopProducao` | Top de Produção |
| `TGFTOP` | `TopSaida` | Top de saida |
| `TGFTOP` | `TopSeparacao` | Tipo Operação Separacao |
| `TGFTOP` | `grupoTipoOperacao` | Grupos Tipo Operação |
| `TGFNAT` | `Natureza` | Natureza |
| `TGFNAT` | `Natureza2` | Natureza2 |
| `TGFNAT` | `Natureza3` | Natureza3 |
| `TGFNAT` | `NaturezaArm` | Natureza de armazenagem |
| `TGFNAT` | `NaturezaExp` | Natureza de armazenagem |
| `TGFNAT` | `NaturezaIpi` | Natureza |
| `TGFNAT` | `NaturezaReceitaDespesaICMS` | Natureza Despesa Receitas ICMS |
| `TGFNAT` | `NaturezaReceitaDespesaICMSST` | Natureza Despesa Receitas ICMS ST |
| `TGFVEN` | `Assessor` | Assessor |
| `TGFVEN` | `Gerente` | Gerente |
| `TGFVEN` | `Vendedor` | Vendedor |
| `TGFVEN` | `VendedorExecutante` | Executante |
| `TGFVEN` | `VendedorItem` | Vendedor do item da nota |
| `TGFCTT` | `Contato` | Contato |
| `TGFCTT` | `ContatoEntrega` | Contato de Entrega |
| `TGFLOC` | `LocalBaixaMPProducao` | Local de Baixa de MP |
| `TGFLOC` | `LocalDestinoPerda` | LocalDestinoPerda |
| `TGFLOC` | `LocalDestinoProducao` | Local de Destino  do Produção |
| `TGFLOC` | `LocalDestinoProducao2` | Local de Destino Encadeada |
| `TGFLOC` | `LocalEstoque` | Local de Estoque |
| `TGFLOC` | `LocalEstoqueTerceiro` | Local Especifico Estoque Terceiros |
| `TGFLOC` | `LocalEstoqueWms` | Local para ajuste de estoque |
| `TGFLOC` | `LocalFinanceiro` | Local |
| `TGFLOC` | `LocalFinanceiroEntDest` | Local |
| `TGFLOC` | `LocalFinanceiroEntOrig` | Local Entrada Origem da TGFETA |
| `TGFLOC` | `LocalFinanceiroSaiDest` | Local |
| `TGFLOC` | `LocalFinanceiroSaiOrig` | Local Saida Origem da TGFETA |
| `TGFLOC` | `LocalMateriaPrima` | Locais Materia Prima |
| `TGFLOC` | `LocalOrigemProducao` | Local |
| `TGFLOC` | `LocalPadraoEconet` | Local Padrão Econet |
| `TGFLOC` | `LocalPadraoImportarXML` | Local padrão para importar XML |
| `TGFVOL` | `UndPrincipalTgwexp` | Unidade Principal |
| `TGFVOL` | `UnidadeCompra` | Unidade para compras |
| `TGFVOL` | `UnidadeMinArmazenagemWMS` | Unidade Minima de Armazenagem para WMS |
| `TGFVOL` | `Volume` | Unidade |
| `TGFVOL` | `VolumeFETHAB` | Volume FETHAB |
| `TGFVOL` | `VolumeKanban` | Unidade de movimentação padrão |
| `TGFVOL` | `VolumeResumoEntrega` | Volume para Resumo de Entrega |
| `TGFEST` | `Estoque` | Estoque |
| `TGFORD` | `OrdemCarga` | Ordem de Carga |
| `TGFTIT` | `EspecieTitulo` | Especie do Tipo de Titulo |
| `TGFTIT` | `TipoTitulo` | Tipo de Titulo |
| `TGFTIT` | `TipoTituloArm` | Tipos de Titulo Armazenagem |
| `TGFTIT` | `TipoTituloExp` | Tipo de Titulo |
| `TGFTIT` | `TipoTituloIpi` | Tipo de Titulo |
| `TGFGRU` | `GrupoProduto` | Grupo Produto |
| `TGFGRU` | `GrupoProduto2` | Grupo Produto |
| `TGFGRU` | `GrupoProduto3` | GrupoProduto3 |
| `TGFFAM` | `FamiliaProduto` | Familia |
| `TGFTAB` | `TabelaPreco` | Tabela de Preco |
| `TGFTAB` | `TabelaPrecoMinimo` | Tabela de Preco Minimo |
| `TGFTAB` | `TabelaPrecoPF` | Tabela de Preco |
| `TGFNTA` | `NomeTabelasPreco` | Cadastro de Tabela de Preco |
| `TGFNTA` | `NomeTabelasPrecoFarPop` | Nome das Tabelas de Preco |
| `TGFNTA` | `NomeTabelasPrecoFilha` | Nome das Tabelas de Preco |
| `TGFNTA` | `NomeTabelasPrecoPmpf` | Nome das Tabelas de Preco |
| `TGFVEI` | `Veiculo` | Veiculos |
| `TGFVEI` | `VeiculoReboque1` | Veiculo Reboque |
| `TGFVEI` | `VeiculoReboque2` | Veiculo Reboque2 |
| `TGFVEI` | `VeiculoReboque3` | Veiculo Reboque3 |
| `TGFVEI` | `VeiculoTracao` | Veiculo de Tração |
| `TGFCFO` | `ClaFiscalCombustivelLubrif` | Classificação Fiscal Operações Para Combustiveis e Lubrificantes |
| `TGFCFO` | `ClaFiscalOperacaoEntrada` | Classificação Fiscal de Operações Entrada |
| `TGFCFO` | `ClaFiscalOperacaoEntradaEstado` | Classificação Fiscal de Operações de Entrada de Fora do Estado. |
| `TGFCFO` | `ClaFiscalOperacaoSaida` | Classificação Fiscal de Operações Saida |
| `TGFCFO` | `ClaFiscalOperacaoSaidaEstado` | Classificação Fiscal de Operações de Saida de Fora do Estado |
| `TGFCFO` | `ClaFiscalOperacaoTerceiros` | Classificação Fiscal de Operações Para Produtos Terceiros |
| `TGFCFO` | `ClaFiscalPrestacaoServico` | Codigo Fiscal de Prestações de Servico |
| `TGFCFO` | `ClassificacaoFiscalOperacao` | Classificação Fiscal de Operações |
| `TGFISS` | `AliquotaISS` | Aliquotas de ISS |
| `TGFGCB` | `GrupoCobranca` | Grupo Cobranca |
| `TSIUSU` | `Atendente` | Atendente |
| `TSIUSU` | `Executante` | Executante |
| `TSIUSU` | `ExecutanteRemetente` | Executante Remetente |
| `TSIUSU` | `Liberador` | Liberador |
| `TSIUSU` | `Responsavel` | Responsavel |
| `TSIUSU` | `Solicitante` | Solicitante |
| `TSIUSU` | `TimExecutanteSac` | Executantes do SAC |
| `TSIUSU` | `TimUsuarioAlteracao` | Usuario de Alteração |
| `TSIUSU` | `TimUsuarioInclusao` | Usuario de Inclusão |
| `TSIUSU` | `TimUsuarioOrigemSac` | Usuarios que lancaram o SAC |
| `TSIUSU` | `UltimoExecutante` | Ultimo Executante |
| `TSIUSU` | `Usuario` | Usuario |
| `TSIUSU` | `Usuario2` | Usuario 2 |
| `TSIUSU` | `Usuario3` | Usuario ultima alteração |
| `TSIUSU` | `Usuario4` | Usuario responsavle cancelamento |
| `TSIUSU` | `UsuarioBaixa` | Usuario Baixa (Financeiro) |
| `TSIUSU` | `UsuarioCancelamento` | UsuarioCancelamento |
| `TSIUSU` | `UsuarioCobranca` | Unidade de Carregamento |
| `TSIUSU` | `UsuarioColeta` | Usuario Coleta |
| `TSIUSU` | `UsuarioComprador` | Usuario Comprador |
| `TSIUSU` | `UsuarioConferencia` | Usuario Conferencia |
| `TSIUSU` | `UsuarioFinal` | Usuario Final |
| `TSIUSU` | `UsuarioLiberacao` | Usuario Liberação |
| `TSIUSU` | `UsuarioPJLider` | Usuario PJ Lider |
| `TSIUSU` | `UsuarioProtocolo` | Usuario Protocolo |
| `TSIUSU` | `UsuarioResponsavel` | Usuario Responsavel |
| `TSIUSU` | `Usuario_AD001` | Usuario |
| `TSIEMP` | `Empresa` | Empresa |
| `TSIEMP` | `EmpresaBaixa` | Empresa para baixa |
| `TSIEMP` | `EmpresaCadastro` | Cadastro de Empresas |
| `TSIEMP` | `EmpresaContablidade` | Empresa Contabilidade |
| `TSIEMP` | `EmpresaDestinoEtapaProducao` | Empresa Destino |
| `TSIEMP` | `EmpresaFinanceira` | Empresa Financeiro |
| `TSIEMP` | `EmpresaFuncionario` | Empresa do funcionario |
| `TSIEMP` | `EmpresaFuncionarioLider` | Empresa Funcionario Lider |
| `TSIEMP` | `EmpresaGOL` | Empresa para agrupar no GOL |
| `TSIEMP` | `EmpresaMatriz` | Empresa Matriz |
| `TSIEMP` | `EmpresaMatrizGnre` | Empresa Matriz para GNRE |
| `TSIEMP` | `EmpresaMatrizNfse` | Empresa Matriz para Nfse |
| `TSIEMP` | `EmpresaModelo` | Empresa Modelo |
| `TSIEMP` | `EmpresaNegociacao` | Empresa da Negociação |
| `TSIEMP` | `EmpresaOrganograma` | Empresa de Organograma |
| `TSIEMP` | `EmpresaOrigemEtapaProducao` | Empresa Origem |
| `TSIEMP` | `EmpresaOrigemFuncionario` | Empresa origem do funcionario |
| `TSIEMP` | `EmpresaPreferencial` | Empresa Preferencial do parceiro |
| `TSIEMP` | `EmpresaSoma` | EmpresaSoma |
| `TSIEMP` | `EmpresaSubstituido` | EmpresaSubstituido |
| `TSIEMP` | `ImovelRural` | Imovel Rural |
| `TSIEMP` | `TLFEmpresaOrigemMovimentoLivro` | Empresa Origem |
| `TSIEMP` | `TimEmpresa` | Empresa |
| `TSICTA` | `ContaBancaria` | Conta Bancaria |
| `TSICTA` | `ContaBancariaDespesa` | Contas Bancarias para Despesas |
| `TSICTA` | `ContaBancariaIpi` | Conta Bancaria |
| `TSICTA` | `ContaBancariaReceita` | Contas Bancarias para Receitas |
| `TSICTA` | `ContaBancarioFgts` | ContaBancarioFgts |
| `TSICTA` | `ContaDestino` | Conta de destino |
| `TSICTA` | `ImplantacaoSaldoConta` | Implantação dos saldos de conta |
| `TSICTA` | `TimContaBancaria` | Conta Bancaria |
| `TSICUS` | `CentroResultado` | Centro de Resultado |
| `TSICUS` | `CentroResultadoArm` | Centros de Resultado Armazenagem |
| `TSICUS` | `CentroResultadoDespesa` | Centro de Resultado Despesa |
| `TSICUS` | `CentroResultadoEFDEmpresa` | Centro Resultado |
| `TSICUS` | `CentroResultadoExp` | Centros de Resultado Armazenagem |
| `TSICUS` | `CentroResultadoFinal` | Centro de Resultado Final |
| `TSICUS` | `CentroResultadoIpi` | Centro de Resultado |
| `TSICUS` | `TimCentroResultadoAdm` | Centro Resultado |
| `TSICUS` | `TimCentroResultadoCorresBanc` | Centro Resultado |
| `TSICUS` | `TimCentroResultadoIncorporador` | Centro Resultado |
| `TSICUS` | `TimCentroResultadoLoteamento` | Centro Resultado |
| `TSICUS` | `TimCentroResultadoRevenda` | Centro Resultado |
| `TSICUS` | `TimCentroResultadoVenda` | Centro Resultado |
| `TSICID` | `Cidade` | Cidade |
| `TSICID` | `CidadeDestino` | Cidade de Destino |
| `TSICID` | `CidadeFatoGerador` | Municipio do Fato Gerador |
| `TSICID` | `CidadeMunicipioFinal` | Municipio de Descarregamento |
| `TSICID` | `CidadeMunicipioInicial` | Municipio de Coleta |
| `TSICID` | `CidadeOrigem` | Cidade de Origem |
| `TSICID` | `CidadeRecebimento` | Cidade para Recebimento |
| `TSICID` | `CidadeTrabalho` | Cidade Trabalho |
| `TSICID` | `FuncionarioCidadeNascimento` | Funcionario Cidade de Nascimento |
| `TSICID` | `FuncionarioNaturalidadeMae` | Naturalidade da Me do Funcionario |
| `TSICID` | `NaturalidadeParceiro` | Naturalidade do Parceiro |
| `TSICID` | `TimCidadeImovel` | Cidades dos imoveis |
| `TSIUFS` | `UnidadeFederativa` | Unidade Federativa |
| `TSIUFS` | `UnidadeFederativaDestino` | Unidade Federativa Destino |
| `TSIUFS` | `UnidadeFederativaEmissao` | Unidade Federativa Emissão |
| `TSIUFS` | `UnidadeFederativaOrigem` | Unidade Federativa Origem |
| `TSIUFS` | `UnidadeFederativa_AD001` | Unidade Federativa |
| `TSIBCO` | `Banco` | Banco |
| `TSIBCO` | `BancoIpi` | Banco |
| `TSIBCO` | `CorrespondenteBancario` | Correspondente Bancario |
| `TSIBCO` | `TimBanco` | Banco |
| `TSIBAI` | `Bairro` | Bairro |
| `TSIBAI` | `BairroRecebimento` | Bairro para recebimento |
| `TSIBAI` | `BairroTrabalho` | Bairro Trabalho |
| `TSIBAI` | `TimBairroImovel` | Bairros dos imoveis |
| `TSIBAI` | `TimBairroImovel2` | Bairros com Imoveis |
| `TSIEND` | `Endereco` | Endereco |
| `TSIEND` | `EnderecoRecebimento` | Endereco de Recebimento |
| `TSIEND` | `EnderecoTrabalho` | Endereco de Trabalho |
| `TSIEND` | `TimEndereco` | Enderecos com Imoveis |