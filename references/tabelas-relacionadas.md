# Tabelas Relacionadas a TGFCAB, TGFITE e TGFPAR

Tabelas filhas e lookups das entidades comerciais centrais do Sankhya OM.

## Relacionadas a TGFCAB (Cabeçalho de Nota)

### TGFACT
**Acompanhamento de Notas**

**PK:** `NUNOTA`, `SEQUENCIA`, `DHOCOR`, `HRACT`  
**entityName:** `AcompanhamentoNota`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DHOCOR` 🔑 | Data | Data |  |
| `HRACT` 🔑 | Data/Hora | Hr. acompanhamento |  |
| `OCORRENCIAS` | Texto | Ocorrencias |  |
| `REFERENCIA` | Texto | Referencia |  |
| `NOTAQUALIDADE` | Inteiro | Nota para qualidade |  |
| `NOTAPONTUAL` | Inteiro | Nota para pontualidade |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `NUMNOTA` | Inteiro | Numero Nota |  |
| `NUNOTA` 🔑 | Inteiro | Numero unico Nota | → `TGFCAB`.`NUNOTA` |
| `DIGITADO` | Texto | Digitado |  |

**Opções `REFERENCIA`:** `R`=Produto, `F`=Frete, `I`=Veiculo, `E`=Empresa, `N`=Nota, `P`=Parceiro, `V`=Vendedor, `T`=Transportadora, `C`=Contato

### TGFCCM
**Comissão Multipla**

**PK:** `NUNOTA`, `CODVEND`  
**Referenciada por:** 2 tabelas  
**entityName:** `ComissaoMultipla`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Numero Unico Nota | → `TGFCAB`.`NUNOTA` |
| `CODVEND` 🔑 | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `PERCCOM` | Decimal | Percentual de Comissão |  |
| `OBS` | Texto | Observação |  |

### TGFCFR
**Tabela Calculo de Frete**

**PK:** `NUCFR`  
**Referenciada por:** 4 tabelas  
**entityName:** `TabelaCalculoFrete`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCFR` 🔑 | Inteiro | Cod. Calculo de frete |  |
| `DESCRCALCFRET` | Texto | Descrição |  |
| `OBSERVACAO` | Texto | Observação |  |
| `SERVICOECT` | Texto | Servico Correios | → `TGFECT`.`CODSERVICO` |
| `CRITERIORATFRETE` | Texto | Rateio frete |  |

**Opções `CRITERIORATFRETE`:** `M`=Metro cubico, `P`=Peso, `V`=Valor da nota

### TGFCOM
**Valores de Comissões de Vendedores**

**PK:** `CODVEND`, `NUFINORIG`, `NUNOTAORIG`, `NUFIN`, `NUMOSORIG`, `NUMITEMORIG`, `TIPO`, `CODFORM`  
**entityName:** `ValorComissaoVendedor`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODVEND` 🔑 | Inteiro | Cod. Vendedor |  |
| `NUFINORIG` 🔑 | Inteiro | Financeiro de origem |  |
| `NUNOTAORIG` 🔑 | Inteiro | Nota de origem |  |
| `NUFIN` 🔑 | Inteiro | Numero Financeiro |  |
| `VLRCOM` | Decimal | Valor da comissão |  |
| `REFERENCIA` | Data/Hora | Referencia |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODFUNC` | Inteiro | Funcionario |  |
| `CODEVENTO` | Inteiro | Evento |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `NUMOSORIG` 🔑 | Inteiro | Numero OS Origem |  |
| `NUMITEMORIG` 🔑 | Inteiro | Numero Item Origem |  |
| `TIPO` 🔑 | Texto | Tipo |  |
| `VLRHORA` | Decimal | Valor Hora |  |
| `QTDHORA` | Inteiro | Quantidade de Horas |  |
| `VLRHORAEXTRA` | Decimal | Valor hora extra |  |
| `QTDHORAEXTRA` | Inteiro | Quantidade de Horas extras |  |
| `INDICEPRODUTIVIDADE` | Decimal | Indice de Produtividade |  |
| `CODFORM` 🔑 | Inteiro | Cod. Formula |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHALTER` | Data/Hora | Data do fechamento |  |
| `NUFECHAMENTO` | Inteiro | Nro do fechamento da comissão |  |
| `VLRRESIDUOCOM` | Decimal | Residuo de Comissão |  |

**Opções `TIPO`:** `M`=Multipla, `O`=Outros, `S`=Servico

### TGFDANT
**Documentos Anteriores**

**PK:** `NUNOTA`, `SEQDANT`  
**entityName:** `DocumentoAnterior`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico da Nota | → `TGFCAB`.`NUNOTA` |
| `SEQDANT` 🔑 | Inteiro | Sequencia do Documento |  |
| `CODPARC` | Inteiro | Parceiro Emissor do Documento | → `TGFPAR`.`CODPARC` |
| `CHAVEDANT` | Texto | Chave de Acesso (doc. anterior) |  |
| `CTEREF` | Texto | CT-e Referenciado |  |
| `TPDOCTA` | Texto | Tipo do Documento de Transporte Anterior |  |
| `SERIE` | Texto | Serie da nota |  |
| `NDOC` | Texto | Numero do Documento Fiscal |  |
| `SUBSER` | Texto | Subserie da nota |  |
| `DEMI` | Data/Hora | Data de Emissão |  |

**Opções `CTEREF`:** `S`=Sim, `N`=Não

**Opções `TPDOCTA`:** `07`=07 - ATRE, `08`=08 - DTA (Despacho de Transito Aduaneiro), `09`=09 - Conhecimento Aereo Internacional, `10`=10 - Conhecimento - Carta de Porte Internacional, `11`=11 - Conhecimento Avulso, `12`=12 - TIF (Transporte Internacional Ferroviario), `13`=13 - BL (Bill of Lading)

### TGFDFN
**Descontos Financeiros**

**PK:** `NUNOTA`, `NUFIN`, `CODDESC`  
**entityName:** `DescontoFinanceiro`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro Unico Nota |  |
| `NUFIN` 🔑 | Inteiro | Nro Unico Financeiro | → `TGFDFA`.`NUFIN` |
| `CODDESC` 🔑 | Inteiro | Desconto | → `TGFDFA`.`CODDESC` |
| `VLRDESC` | Decimal | Valor do Desconto |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DTALTER` | Data/Hora | Data da Alteração |  |

### TGFNCE
**Coleta e Entrega por Nota**

**PK:** `NUNOTA`, `SEQUENCIA`  
**entityName:** `ColetaEntregaPorNota`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nota | → `TGFCAB`.`NUNOTA` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TIPO` | Texto | Tipo |  |
| `TIPOTRANSP` | Inteiro | Tipo transporte |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CGC_CPF` | Texto | CNPJ/CPF |  |
| `INSCESTAD` | Texto | Insc. estadual |  |
| `CODMUNFIS` | Inteiro | Mun. domicilio fiscal |  |

**Opções `TIPO`:** `E`=Entrega, `C`=Coleta

**Opções `TIPOTRANSP`:** `5`=Rodo-Ferroviario, `1`=Ferroviario, `2`=Aquaviario, `4`=Aereo, `9`=Outros, `0`=Rodoviario, `3`=Dutoviario

### TGFOBS
**Observações para Notas**

**PK:** `CODOBSPADRAO`  
**Referenciada por:** 8 tabelas  
**entityName:** `ObservacaoNotasFiscais`, `ObservacaoNotasFiscaisAju`, `ObservacaoNotasFiscaisDoc`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODOBSPADRAO` 🔑 | Inteiro | Codigo |  |
| `DTALTER` | Data | Data |  |
| `OBSERVACAO` | Texto | Observação |  |
| `QTDLINHAS` | Inteiro | Qtde de Linhas |  |
| `NROPROCESSO` | Texto | Num. Processo |  |
| `ORIGPROCESSO` | Inteiro | Origem Processo |  |
| `VINCDOCARREC` | Texto | Vincular DAE/GNRE |  |
| `GERAREFD` | Texto | Geração no EFD |  |
| `COMPLEMENTOEFD` | Texto | Carrega Complemento p/ EFD |  |
| `CODREFINFCOMPL` | Texto | Codigo de referencia a informação complementar |  |
| `OPERESSACOMP` | Texto | Operação com Ressarcimento/Complemento de ST |  |

**Opções `COMPLEMENTOEFD`:** `N`=Não, `S`=Sim

**Opções `GERAREFD`:** `I`=Informação Complementar do Documento Fiscal, `O`=Observação do Lancamento Fiscal, `N`=Não Gerar

**Opções `OPERESSACOMP`:** `N`=Não, `S`=Sim

**Opções `ORIGPROCESSO`:** `1`=Justica Federal, `9`=Outros, `0`=Sefaz, `2`=Justica Estadual, `3`=Secex/RFB

**Opções `VINCDOCARREC`:** `S`=Sim, `N`=Não

### TGFODP
**Ordem de Despacho**

**PK:** `NUODP`  
**Referenciada por:** 1 tabelas  
**entityName:** `OrdemDespacho`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUODP` 🔑 | Inteiro | Nro. unico |  |
| `CODPARCTRANSP` | Inteiro | Transportadora | → `TGFPAR`.`CODPARC` |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `STATUS` | Texto | Status |  |
| `DTINCLUSAO` | Data/Hora | Dt. inclusão |  |

**Opções `STATUS`:** `F`=Fechada, `A`=Aberta

### TGFSEG
**Seguros de Transporte**

**PK:** `NUNOTA`, `SEQSEG`  
**entityName:** `SeguroTransporte`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico da Nota | → `TGFCAB`.`NUNOTA` |
| `SEQSEG` 🔑 | Inteiro | Sequencia do Responsavel pelo Seguro |  |
| `RESPSEG` | Texto | Responsavel pelo Seguro |  |
| `NOMESEG` | Texto | Nome da Seguradora |  |
| `NUMAPO` | Texto | Nro. Apolice |  |
| `NUMAVE` | Texto | Nro. Averbação |  |
| `VLRCARGA` | Decimal | Valor da Carga |  |

**Opções `RESPSEG`:** `5`=Tomador de Servico, `4`=Emitente do CT-e, `0`=Remetente, `3`=Destinatario

### TGFSFP
**Simulações de Formas de Pagamento**

**PK:** `NUNOTA`, `CODTIPVENDA`, `PARCELA`  
**entityName:** `SimulacaoFormaPagamento`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico Nota | → `TGFCAB`.`NUNOTA` |
| `CODTIPVENDA` 🔑 | Inteiro | Cod. Tipo Negociação |  |
| `PARCELA` 🔑 | Inteiro | Parcela |  |
| `DTVENC` | Data | Dt. Vencimento |  |
| `VALOR` | Decimal | Valor |  |
| `TAXAJURO` | Decimal | Taxa de Juro |  |
| `VALORLIQUIDO` | Decimal | Valor Liquido |  |

### TGFTPD
**Tipo de pedido**

**PK:** `CODTPD`  
**Referenciada por:** 1 tabelas  
**entityName:** `TipoPedido`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTPD` 🔑 | Inteiro | Cod. Tipo de Pedido |  |
| `DESCRICAO` | Texto | Descrição |  |
| `SIGLA` | Texto | Sigla |  |
| `CODMODPED` | Inteiro | Modelo de pedido |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |

**Opções `SIGLA`:** `P`=Unidade parada, `M`=Mensal, `I`=Inicial, `G`=Garantia

### TGFTPV
**Tipos de Negociação**

**PK:** `CODTIPVENDA`, `DHALTER`  
**Referenciada por:** 6 tabelas  
**entityName:** `TipoNegociacao`, `TipoNegociacao3`, `TipoNegociacaoArm`, `TipoNegociacaoExp`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIMQTDPARC` | Inteiro | Qtd. Parcelas Lancamento |  |
| `CODTIPVENDA` 🔑 | Inteiro | Tipo de Negociação |  |
| `POSSUISIMSALVA` | Texto | Possui Simulação Salva |  |
| `EXVENDAMAIS` | Texto | Exclusivo Venda Mais |  |
| `DESCRTIPVENDA` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `SUBTIPOVENDA` | Texto | Subtipo |  |
| `BASEPRAZO` | Inteiro | Base do prazo |  |
| `VENDAMIN` | Decimal | Valor minimo p/ venda |  |
| `VENDAMAX` | Decimal | Valor maximo p/ venda |  |
| `COMPRAMAX` | Decimal | Valor maximo p/ compra |  |
| `COMISSAO` | Decimal | Comissão |  |
| `GRUPOAUTOR` | Texto | Grupo de autorização |  |
| `SOMAPRAZOCLIENTE` | Texto | Soma prazo de cliente |  |
| `VALPRAZOCLIENTE` | Texto | Valida prazo de cliente |  |
| `FIXAVENC` | Texto | Fixa vencimento |  |
| `PODECONSUMIDOR` | Texto | Pode ser usado por consumidor |  |
| `CODTAB` | Inteiro | Tabela de preco | → `TGFNTA`.`CODTAB` |
| `NUNOTA` | Inteiro | Cabecalho modelo |  |
| `EMITEBOLETA` | Texto | Imprimir Pix/Boleto/Duplicata |  |
| `CODTCF` | Inteiro | Tabela financeira | → `TGFTCF`.`CODTCF` |
| `CODOBSPADRAO` | Inteiro | Observação Padrão | → `TGFOBS`.`CODOBSPADRAO` |
| `PRAZOMEDMAX` | Inteiro | Prazo medio maximo |  |
| `PRAZOMAX` | Inteiro | Prazo maximo |  |
| `LUCROMIN` | Decimal | % Lucro minimo |  |
| `MARGEMMIN` | Decimal | % MC Minima |  |
| `CODFORMDESCMAX` | Inteiro | Formula desc. maximo | → `TGFFDM`.`CODFORM` |
| `CODFORMDESCMAXITENS` | Inteiro | Formula desc. maximo itens | → `TGFFDM`.`CODFORM` |
| `DESCPROM` | Texto | Desconto Promocional |  |
| `DESCMAX` | Decimal | % Desconto maximo |  |
| `TAXAJURO` | Decimal | Taxa em % |  |
| `TIPTAXA` | Texto | Tipo da taxa |  |
| `TIPJURO` | Texto | Apresentação da taxa |  |
| `CODCTACTB_1` | Inteiro | Conta contabil 1 | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB_2` | Inteiro | Conta contabil 2 | → `TCBPLA`.`CODCTACTB` |
| `PERCMINENTRADA` | Decimal | % Min. entrada |  |
| `PRAZOMAXPRIPARC` | Inteiro | Prazo max. 1 parcela |  |
| `NROPARCELAS` | Inteiro | Numero de parcelas |  |
| `DHALTER` 🔑 | Data/Hora | Data e hora alteração |  |
| `APRESTRANSP` | Texto | Apresenta transportadora |  |
| *... +16 campos* | | | |

**Opções `APRESTRANSP`:** `N`=Não, `S`=Sim

**Opções `ARREDPRIMEIRAPARC`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `BAIXA`:** `S`=Sim, `N`=Não

**Opções `BASEPRAZO`:** `4`=Fora o mes, `3`=Fora a quinzena, `2`=Fora a dezena, `1`=Fora a semana, `0`=A partir do dia

### TGFVALP
**Vale Pedagio**

**PK:** `NUNOTA`, `SEQUENCIA`  
**entityName:** `ValePedagio`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico da Nota |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia do Vale Pedagio |  |
| `CODPARCFORN` | Inteiro | Parceiro Fornecedor | → `TGFPAR`.`CODPARC` |
| `NUCOMPRA` | Texto | Nro. Compra |  |
| `TIPPAG` | Texto | Pagante do Pedagio |  |
| `CODPARCPAG` | Inteiro | Parceiro Pagante | → `TGFPAR`.`CODPARC` |
| `VLRPEDAGIO` | Decimal | Valor do Pedagio |  |

**Opções `TIPPAG`:** `O`=Outro, `D`=Destinatario, `B`=Recebedor, `E`=Emitente, `X`=Expedidor, `R`=Remetente

### TGFVTP
**Via de transporte**

**PK:** `CODVTP`  
**Referenciada por:** 2 tabelas  
**entityName:** `ViaTransporte`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODVTP` 🔑 | Inteiro | Cod. Meio de Transporte |  |
| `DESCRICAO` | Texto | Descrição |  |
| `TIPO` | Texto | Via de Transporte |  |
| `LEADTIME` | Inteiro | Lead Time Total |  |
| `LEADTIMECONF` | Inteiro | Lead Time Confirmado |  |
| `LEADTIMEPROC` | Inteiro | Lead Time em Processamento |  |
| `LEADTIMEEMPC` | Inteiro | Lead Time Empacotado |  |
| `LEADTIMEDESP` | Inteiro | Lead Time apos Despacho |  |
| `QTDITENS` | Inteiro | Quantidade de Itens |  |
| `CODMODPED` | Inteiro | Modelo de Pedido | → `TGFCAB`.`NUNOTA` |

**Opções `TIPO`:** `F`=Ferroviario, `R`=Rodoviario, `A`=Aeroviario, `Q`=Aquaviario, `D`=Dutoviario

### TSIMOE
**Moedas**

**PK:** `CODMOEDA`  
**Referenciada por:** 21 tabelas  
**entityName:** `Moeda`, `Moeda2`, `TimMoeda`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMOEDA` 🔑 | Inteiro | Codigo |  |
| `NOMEMOEDA` | Texto | Nome |  |
| `TIPMOEDA` | Texto | Tipo |  |
| `CODINTMOEDA` | Inteiro | Codigo tabela internacional |  |
| `CODTABBCB` | Inteiro | Cod. tabela BCB |  |
| `TIPCALC` | Texto | Tipo do Acumulo |  |
| `TIPOTAXA` | Texto | Tipo de taxa |  |

**Opções `TIPCALC`:** `S`=Simples, `C`=Composto

**Opções `TIPMOEDA`:** `I`=Indice, `V`=Valor

**Opções `TIPOTAXA`:** `V`=Venda, `C`=Compra

## Relacionadas a TGFITE (Itens de Nota)

### TGFICM
**Aliquotas de ICMS**

**PK:** `UFORIG`, `UFDEST`, `TIPRESTRICAO`, `CODRESTRICAO`, `TIPRESTRICAO2`, `CODRESTRICAO2`, `SEQUENCIA`  
**entityName:** `AliquotaICMS`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `UFORIG` 🔑 | Inteiro | UF origem | → `TSIUFS`.`CODUF` |
| `UFDEST` 🔑 | Inteiro | UF destino | → `TSIUFS`.`CODUF` |
| `TIPRESTRICAO` 🔑 | Texto | Tipo de Restrição |  |
| `CODRESTRICAO` 🔑 | Inteiro | Cod. restrição |  |
| `DESCRRESTRICAO` | Texto | Descrição Restrição |  |
| `TIPRESTRICAO2` 🔑 | Texto | Tipo de Restrição 2 |  |
| `CODRESTRICAO2` 🔑 | Inteiro | Cod. restrição 2 |  |
| `DESCRRESTRICAO2` | Texto | Descrição Restrição 2 |  |
| `ALIQUOTA` | Decimal | Aliquota |  |
| `REDBASE` | Decimal | Redução da Base |  |
| `PERCMINSUBTRIB` | Decimal | Percentual Minimo ST (RIOLOG) |  |
| `ALIQFRETE` | Decimal | Aliquota do Frete |  |
| `REDBASEFRETE` | Decimal | Redução da Base do Frete |  |
| `ALIQCONSFIN` | Decimal | Aliquota suportada pelo Consumidor Final |  |
| `MARGLUCRO` | Decimal | Margem de Lucro |  |
| `CODTRIB` | Inteiro | Tributação |  |
| `CODOBSPADRAO` | Inteiro | Observação Padrão | → `TGFOBS`.`CODOBSPADRAO` |
| `ALIQSUBTRIB` | Decimal | Aliquota Debito de ST |  |
| `ALIQICMSLIMITECALCST` | Decimal | Aliq. Limite cred. ICMS p/ dedução no Valor ST |  |
| `REPREDBASE` | Texto | Repassar Redução do Imposto para o cliente |  |
| `REDBASEST` | Decimal | Redução de Base ST |  |
| `CODTAB` | Inteiro | Tabela | → `TGFNTA`.`CODTAB` |
| `MAIORBASEST` | Texto | Maior Base ST |  |
| `REPICMS` | Texto | Repassar ICMS |  |
| `REDICMS` | Texto | Redução ICMS |  |
| `CONSIDIPIVLROPPROP` | Texto | Considerar IPI na comparação conforme portaria Sutri860 |  |
| `CALCSTCONSUTRI` | Texto | Calcular ST Conforme Portaria Sutri860 |  |
| `BASESTRED` | Texto | Base ST Redução |  |
| `NAOCONSIDMVA` | Texto | Considera Pauta para a base de calculo do ICMS ST |  |
| `MAIORBASEICMS` | Texto | Usar a maior base para ICMS |  |
| `OUTORGA` | Decimal | Outorga |  |
| `STSUTRI4302014MG` | Texto | Calcular ST conforme portaria Sutri 430/2014 - MG |  |
| `CONVPRODUZ` | Texto | Convenio Produzir |  |
| `PAUTAVLRSTFIXO` | Texto | Pauta de Valor Fixo do Item - CE |  |
| `CODTABICMS` | Inteiro | Tabela c/base p/ICMS | → `TGFNTA`.`CODTAB` |
| `BASICMMOD` | Inteiro | Modalidade BC ICMS |  |
| `REPREDBASE2` | Texto | Redução da BASE |  |
| `BASICMSTMOD` | Inteiro | Modalidade BC ICMS ST |  |
| `CODTABSTANT` | Inteiro | Tabela c/Base ST Operação Anterior: | → `TGFNTA`.`CODTAB` |
| `CODTABSTUFDEST` | Inteiro | Tabela c/Base ST em Favor da UF de Destino | → `TGFNTA`.`CODTAB` |
| *... +88 campos* | | | |

**Opções `AD_REGRAUT`:** `S`=Sim, `N`=No

**Opções `BASEFCPINT`:** `null`=Valor da Operação, `B`=Base do ICMS

**Opções `BASESTRED`:** `N`=Desconsidera, `S`=Considerar IPI p/ Redução, `D`=Desconsiderar IPI p/ Redução

**Opções `BASESTUFDEST`:** `V`=Valor do Produto, `P`=Pauta

**Opções `BASICMMOD`:** `3`=Valor da Operação, `2`=Preco Tabelado Max. (Valor), `1`=Pauta (Valor)

### TGFIII
**Impostos de Importação**

**PK:** `NUNOTA`, `SEQUENCIA`  
**Referenciada por:** 2 tabelas  
**entityName:** `ImpostosImportacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | NUNOTA | → `TGFITE`.`NUNOTA` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFITE`.`SEQUENCIA` |
| `BASEIMPOSTO` | Decimal | Base de Calculo do Imposto de Importação |  |
| `VLRDESPADUA` | Decimal | Valor das Despesas Aduaneiras |  |
| `VLRIMPOSTO` | Decimal | Valor do Imposto de Importação |  |
| `VLRIOF` | Decimal | Valor do IOF |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `IMPTAGEXCNOTNAC` | Texto | IMPTAGEXCNOTNAC |  |

**Opções `IMPTAGEXCNOTNAC`:** `S`=Sim, `N`=Não

### TGFCTD
**Custo de devolucao**

**PK:** `NUNOTA`, `SEQUENCIA`, `NUNOTAORIG`, `SEQUENCIAORIG`, `DHCUSTO`  
**entityName:** `CustoDevolucao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | NUNOTA | → `TGFITE`.`NUNOTA` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFITE`.`SEQUENCIA` |
| `NUNOTAORIG` 🔑 | Inteiro | NUNOTAORIG |  |
| `SEQUENCIAORIG` 🔑 | Inteiro | SEQUENCIAORIG |  |
| `DHCUSTO` 🔑 | Data/Hora | DHCUSTO |  |
| `VLRCUS` | Decimal | VLRCUS |  |
| `NUNOTACOTACAO` | Inteiro | NUNOTACOTACAO | → `TGFCAB`.`NUNOTA` |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TGFCUSITE
**Custo Item**

**PK:** `NUNOTA`, `SEQUENCIA`, `CODPROD`  
**entityName:** `CustoItem`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Nota |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODPROD` 🔑 | Inteiro | Produto |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODLOCAL` | Inteiro | Local |  |
| `CONTROLE` | Texto | Controle |  |
| `DTATUAL` | Data/Hora | DTATUAL |  |
| `CUSGER` | Decimal | CUSGER |  |
| `CUSVARIAVEL` | Decimal | Custo variavel |  |
| `CUSREP` | Decimal | CUSREP |  |
| `ENTRADACOMICMS` | Decimal | ENTRADACOMICMS |  |
| `ENTRADASEMICMS` | Decimal | ENTRADASEMICMS |  |
| `QTDNEG` | Decimal | Qtd. Negociada |  |
| `FAMILIA` | Texto | FAMILIA |  |
| `ALTPRECO` | Texto | Alt. Preco Igual |  |
| `TIPONOTA` | Texto | TIPONOTA |  |
| `SINAL` | Inteiro | SINAL |  |
| `COMPLCUST` | Inteiro | Complemento de Custo |  |

### TGFDTP
**PrevisaoEntrega**

**PK:** `NUNOTA`, `SEQUENCIA`, `SEQPREV`  
**entityName:** `PrevisaoEntrega`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nota | → `TGFITE`.`NUNOTA` |
| `SEQUENCIA` 🔑 | Inteiro | Seq. Item | → `TGFITE`.`SEQUENCIA` |
| `SEQPREV` 🔑 | Inteiro | Seq. Previsão |  |
| `DTPREV` | Data | Data prevista |  |
| `QTD` | Decimal | Quantidade prevista |  |
| `QTDENTREGUE` | Decimal | Qtd. Entregue |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Data Alteração |  |

### TGFHIP
**Historido de alteração Item Pendente**

**PK:** `NUNOTA`, `SEQHIP`  
**entityName:** `HistoricoItemPendente`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Numero Nota | → `TGFITE`.`NUNOTA` |
| `SEQHIP` 🔑 | Inteiro | Sequencia Justificativa |  |
| `SEQUENCIA` | Inteiro | Sequencia do Item | → `TGFITE`.`SEQUENCIA` |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | Modificado em |  |
| `STATUS` | Texto | Status |  |
| `DESCRICAO` | Texto | Justificativa |  |

**Opções `STATUS`:** `S`=Pendente, `N`=Não Pendente

### TGFNRR
**Cadastro da Natureza de Rendimentos**

**PK:** `CODNATREND`  
**entityName:** `CadastroNaturezaRendimentos`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNATREND` 🔑 | Inteiro | Codigo Natureza Rendimento |  |
| `DESCNATREND` | Texto | Descrição Natureza Rendimento |  |
| `FCI` | Texto | Fundo ou Clube de Investimento |  |
| `DECIMOTERCEIRO` | Texto | Decimo Terceiro |  |
| `RRA` | Texto | Rendimento Recebido Acumuladamente |  |
| `DEDUCAO` | Texto | Tipo de Dedução |  |
| `RENDISENTO` | Texto | Tipo Rendimento Isento |  |
| `TRIBUTO` | Texto | Tipo Tributo |  |
| `BLOCOAPLIC` | Texto | Bloco de aplicação |  |
| `APLICACAO` | Texto | Local de Aplicação |  |
| `DTINICIOVAL` | Data | Data Inicio Validade |  |
| `DTFIMVAL` | Data | Data Fim Validade |  |
| `ATIVO` | Texto | Ativo |  |
| `GERSEMTRIB` | Texto | Gerar sem tributação |  |

**Opções `APLICACAO`:** `F`=Financeiro, `A`=Ambos, `S`=Servico

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `DECIMOTERCEIRO`:** `N`=Não, `S`=Sim

**Opções `FCI`:** `N`=Não, `S`=Sim

**Opções `GERSEMTRIB`:** `N`=Não, `S`=Sim

### TGWEND
**Endereco de Armazenamento**

**PK:** `CODEND`  
**Referenciada por:** 43 tabelas  
**entityName:** `EnderecoArmazenagem`, `EnderecoArmazenagem2`, `EnderecoArmazenagem3`, `EnderecoArmazenagem4`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEND` 🔑 | Inteiro | End. Reduzido |  |
| `POSSUICONTPEND` | Texto | Contagem Pendente |  |
| `ENDERECO` | Texto | Endereco |  |
| `DESCREND` | Texto | Descrição |  |
| `MULTIPROD` | Texto | Multi Produto |  |
| `EXPEDICAO` | Texto | Permite Expedição |  |
| `PICKING` | Texto | Picking |  |
| `CROSSDOCK` | Texto | End. de Crossdocking |  |
| `FRAGMENTAEST` | Texto | Permite Fragmentar Estoque |  |
| `ORDEM` | Inteiro | Ordem |  |
| `NIVEL` | Inteiro | Nivel |  |
| `ALTURA` | Decimal | Altura |  |
| `LARGURA` | Decimal | Largura |  |
| `PROFUNDIDADE` | Decimal | Profundidade |  |
| `M3MAX` | Decimal | Metro Cubico Max. |  |
| `PESOMAX` | Decimal | Peso Maximo |  |
| `CODENDPAI` | Inteiro | Endereco Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `PROIBIRGRUPO` | Texto | Proibir Grupos relacionados |  |
| `PROIBIRPRODUTO` | Texto | Proibir Produtos relacionados |  |
| `PROIBIRLOCAL` | Texto | Proibir Local |  |
| `EXCLCONF` | Texto | Exclusivo p/ Conferencia |  |
| `ENDMOVVERTICAL` | Texto | Movimentação Vertical |  |
| `TIPO` | Texto | Tipo |  |
| `FLOWRACK` | Texto | E flowrack |  |
| `PAR` | Texto | Lado |  |
| `CODLOCAL` | Inteiro | Local | → `TGFLOC`.`CODLOCAL` |
| `PROIBIRCONTROLE` | Texto | Proibir Controle |  |
| `BLOQUEADO` | Texto | Situação do Estoque |  |
| `POSSUIESTOQUE` | Texto | Possui Estoque |  |
| `CODUSUTARCONTAGEM` | Inteiro | Cod. Usuario Contagem |  |
| `APENASCONTPORPROD` | Texto | Permitir apenas contagem por produto |  |
| `CODENDPREF` | Inteiro | Endereco Preferencial |  |
| `CODENDSEC` | Inteiro | Endereco Secundario |  |
| `USAPICKINGINTERMEDIARIO` | Texto | Usa Picking Intermediario |  |
| `PICKINGINTERMEDIARIO` | Texto | Picking Intermediario |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CONEXAOSAIDA` | Texto | Utiliza endereco de conexão para Saida |  |
| *... +6 campos* | | | |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `APENASCONTPORPROD`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `BLOQUEADO`:** `S`=Bloqueado, `N`=Disponivel

**Opções `CONEXAOENTRADA`:** `S`=Sim, `N`=Não

## Relacionadas a TGFPAR (Parceiros)

### TGFTPP
**Tipos de Parceiros**

**PK:** `CODTIPPARC`  
**Referenciada por:** 8 tabelas  
**entityName:** `Perfil`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DHALTREG` | Data/Hora | Dt. Alteração |  |
| `CODUSUALTREG` | Inteiro | Cod. Usuario Alteração |  |
| `CODTIPPARC` 🔑 | Inteiro | Cod. Perfil |  |
| `DESCRTIPPARC` | Texto | Descrição |  |
| `ANALITICO` | Texto | Analitico |  |
| `ATIVO` | Texto | Ativo |  |
| `CODTIPPARCPAI` | Inteiro | Cod. Perfil Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `CODTAB` | Inteiro | Tabela de preco | → `TGFNTA`.`CODTAB` |
| `CODANT` | Inteiro | SGE |  |
| `TIPANT` | Texto | Tipo no SGE |  |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

### TGFCPL
**Dados Complementares de Parceiros**

**PK:** `CODPARC`  
**entityName:** `ComplementoParc`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `SEQENTREGA` | Inteiro | Sequencia de entrega |  |
| `CODINDNIF` | Inteiro | Indicativo do NIF |  |
| `CEPENTREGA` | Texto | CEP p/ entrega |  |
| `CODENDENTREGA` | Inteiro | Endereco p/ entrega | → `TSIEND`.`CODEND` |
| `NUMINDNIF` | Texto | Nro. do NIF  Numero de Identificação Fiscal |  |
| `NUMENTREGA` | Texto | Numero entrega |  |
| `TPFONTEPAG` | Inteiro | Tipo Relação fonte pagadora |  |
| `TPIRRFEXT` | Inteiro | Tributação IRRF - Exterior REINF |  |
| `COMPLENTREGA` | Texto | Complemento entrega |  |
| `CODBAIENTREGA` | Inteiro | Bairro p/ entrega | → `TSIBAI`.`CODBAI` |
| `INFOISENIMUNI` | Inteiro | Informações sobre isenção e imunidade |  |
| `CODCIDENTREGA` | Inteiro | Cod. Cidade Entrega | → `TSICID`.`CODCID` |
| `CEPRECEB` | Texto | CEP p/ recebimento |  |
| `CODENDRECEB` | Inteiro | Endereco p/ recebimento | → `TSIEND`.`CODEND` |
| `NUMRECEB` | Texto | Numero recebimento |  |
| `COMPLRECEB` | Texto | Complemento recebimento |  |
| `CODBAIRECEB` | Inteiro | Bairro p/ recebimento | → `TSIBAI`.`CODBAI` |
| `CODCIDRECEB` | Inteiro | Cod. Cidade Recebimento | → `TSICID`.`CODCID` |
| `LOCALTRAB` | Texto | Local de trabalho |  |
| `CEPTRAB` | Texto | CEP do trabalho |  |
| `CODENDTRAB` | Inteiro | Endereco do trabalho | → `TSIEND`.`CODEND` |
| `NUMTRAB` | Texto | Numero trabalho |  |
| `COMPLTRAB` | Texto | Complemento trabalho |  |
| `CODBAITRAB` | Inteiro | Bairro do trabalho | → `TSIBAI`.`CODBAI` |
| `CODCIDTRAB` | Inteiro | Cod. Cidade Trabalho | → `TSICID`.`CODCID` |
| `TELTRAB` | Texto | Telefone do trabalho |  |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `TEMPORESID` | Data | Data ocupação residencia |  |
| `CODMOEDARENDA` | Inteiro | Moeda p/ renda |  |
| `CODPARCTRANSP` | Inteiro | Cod. Parceiro Transportadora preferencial | → `TGFPAR`.`CODPARC` |
| `NATURALIDADE` | Inteiro | Naturalidade |  |
| `NACIONALIDADE` | Inteiro | Nacionalidade do parceiro | → `TSIPAI`.`CODPAIS` |
| `EXIGEPEDIDO` | Texto | Exige pedido na OS |  |
| `ISENTOTAXAMINBOLETA` | Texto | Isento taxa boleto |  |
| `CODMOEDALIM` | Inteiro | Moeda para limite | → `TSIMOE`.`CODMOEDA` |
| `IMAGEM` | Blob | Imagem |  |
| `CONJUGE` | Texto | Conjuge |  |
| `RAMAL` | Inteiro | Ramal |  |
| `DIAPAG` | Inteiro | Dia para pagamento |  |
| `DIASEMANAPAG` | Inteiro | Dia da semana para pagamento |  |
| *... +41 campos* | | | |

**Opções `CODINDNIF`:** `1`=1 - Beneficiario com NIF, `2`=2 - Beneficiario dispensado do NIF, `3`=3 - Pais não exige NIF

**Opções `DIASEMANAPAG`:** `5`=Quinta-feira, `1`=Indefinido, `2`=Segunda-feira, `3`=Terca-feira, `4`=Quarta-feira, `6`=Sexta-feira

**Opções `EXIGEPEDIDO`:** `S`=Sim, `N`=Não

**Opções `GERARFRETE`:** `N`=Não, `S`=Sim

**Opções `INFOISENIMUNI`:** `1`=1 - Entidade não isenta/não imune - Tributação normal, `2`=2 - Instituição de educação e assistencia social sem fins lucrativos art 12 Lei 9532 de 10 dez 1997, `3`=3 - Instituição filantropica, recreativa, cultural, cientifico e assoc. civis, art 15 Lei 9.532/1997

### TGFPAP
**Interação Parceiro Produto**

**PK:** `CODPARC`, `CODPROD`, `SEQUENCIA`  
**Referenciada por:** 3 tabelas  
**entityName:** `RelacionamentoParceiroProduto`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODPROPARC` | Texto | Cod. Produto Equivalente |  |
| `DESCRPROPARC` | Texto | Descrição do Produto Equivalente |  |
| `UNIDADEPARC` | Texto | Unidade | → `TGFVOL`.`CODVOL` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `PRAZOENT` | Inteiro | Prazo para entrega |  |
| `CODBARRA` | Texto | Cod.Barra |  |
| `DUM14` | Texto | Cod. Barra DUN-14 |  |
| `CONTROLE` | Texto | Controle |  |
| `UNIDADE` | Texto | Unidade do Parceiro |  |
| `UNIDADELOTE` | Texto | Unidade do Lote |  |
| `MULTIPCPA` | Decimal | Multipl. Compra |  |
| `CODBARRAPARC` | Texto | Cod. Barras Parceiro |  |
| `CODEMP` | Inteiro | Codigo Empresa |  |

### TGFPPZ
**Prazo por Parceiro**

**PK:** `CODPARC`, `PRAZO`  
**entityName:** `PrazoPorParceiro`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `PRAZO` 🔑 | Inteiro | Prazo |  |
| `PERCAUMENTO` | Decimal | % aumento |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DTALTER` | Data/Hora | Data de alteração |  |

### TGFPPA
**Parceiro Contato e Tipo de Parceiro**

**PK:** `CODPARC`, `CODCONTATO`, `CODTIPPARC`  
**entityName:** `PerfilContato`, `PerfilParceiro`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPPARC` 🔑 | Inteiro | Perfil | → `TGFTPP`.`CODTIPPARC` |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODCONTATO` 🔑 | Inteiro | Contato |  |

### TGFIMA
**Aliquotas de impostos**

**PK:** `CODIMP`, `TIPO`, `CODIGO`  
**entityName:** `AliquotaImposto`, `AliquotaImpostoEmpresa`, `AliquotaImpostoGrupoProd`, `AliquotaImpostoParceiro`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Codigo |  |
| `CODIMP` 🔑 | Inteiro | Imposto | → `TGFIMC`.`CODIMP` |
| `TIPO` 🔑 | Texto | Tipo |  |
| `IMPNOTA` | Inteiro | Na Nota |  |
| `IMPFINORIGFIN` | Inteiro | No Financeiro Origem Financeiro |  |
| `IMPFINORIGEST` | Inteiro | No Financeiro Origem Estoque |  |
| `TIPIMP` | Inteiro | Tipo do Imposto |  |
| `CODRECEITA` | Texto | Codigo da Receita | → `TGFRDARF`.`CODRECEITA` |
| `REDBASE` | Decimal | Redução da Base de Imposto |  |
| `ALIQUOTA` | Decimal | Aliquota |  |
| `TPIRRFEXT` | Inteiro | Tributação IRRF - Exterior REINF |  |
| `CALCULAR` | Texto | Calcular |  |

**Opções `CALCULAR`:** `N`=Não, `S`=Sim

**Opções `IMPFINORIGEST`:** `-1`=Subtrair, `2`=Nenhum

**Opções `IMPFINORIGFIN`:** `2`=Nenhum, `-1`=Subtrair

**Opções `IMPNOTA`:** `0`=Ja Incluso, `1`=Somar, `2`=Nenhum, `-1`=Subtrair

**Opções `TIPIMP`:** `1`=Somar, `-1`=Subtrair, `0`=Ja Incluso

### TGFLCP
**Limite de Credito por Parceiro**

**PK:** `CODPARC`, `GRUPOLIMCRED`  
**entityName:** `CreditoPorParceiro`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `GRUPOLIMCRED` 🔑 | Texto | Grupo Limite de Credito |  |
| `LIMCRED` | Decimal | Limite de Credito |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Data Alteração |  |

### TGFDFP
**Desconto Financeiro por Parceiro por Periodo**

**PK:** `CODPARC`, `CODDESC`, `DTINICIO`  
**entityName:** `DescontoFinanceiroParcPeriodo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODPARCMATRIZ` | Inteiro | Cod. Parceiro Matriz |  |
| `CODDESC` 🔑 | Inteiro | Desconto | → `TGFDFI`.`CODDESC` |
| `DTINICIO` 🔑 | Data | Data Inicio |  |
| `DTFIM` | Data | Data Fim |  |
| `VLRDESC` | Decimal | Valor de Desconto |  |
| `PERCDESC` | Decimal | Percentual de Desconto |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Data de Alteração |  |

### TGFDPP
**Dependente IR (REINF)**

**PK:** `CODPARC`, `CODDEPEND`  
**Referenciada por:** 2 tabelas  
**entityName:** `DependenteIR`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Codigo Parceiro |  |
| `CODDEPEND` 🔑 | Inteiro | Codigo Dependente |  |
| `NOME` | Texto | Nome Dependente |  |
| `CPF` | Texto | CPF Dependente |  |
| `DEPENDIR` | Texto | Dependente do IR |  |
| `ESTUDANTE` | Texto | Estudante ate 24 Anos |  |
| `DTINIVIG` | Data | Data inicio vigencia |  |
| `DTFIMVIG` | Data | Data fim vigencia |  |
| `RELACIONAMENTO` | Inteiro | Relacionamento |  |
| `DESCRICAO` | Texto | Descrição Outros |  |

**Opções `DEPENDIR`:** `N`=Não, `S`=Sim

**Opções `ESTUDANTE`:** `N`=Não, `S`=Sim

**Opções `RELACIONAMENTO`:** `1`=1 - Conjuge, `2`=2 - Companheiro(a) qual tenha filho ou viva ha mais de 5 anos ou possua declaração de união estavel, `3`=3 - Filho(a) ou enteado(a), `6`=6 - Irmão(), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial, `8`=8 - Pais, `9`=9 - Avos e bisavos, `10`=10 - Menor pobre do qual detenha a guarda judicial, `11`=11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador, `12`=12 - Ex-conjuge, `99`=99 - Agregado/Outros

### TGFPAEM
**Grupo ICMS/ISS por Empresa**

**PK:** `CODEMP`, `CODPARC`  
**entityName:** `ParceiroEmpresGrupoIcms`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `GRUPOICMS` | Inteiro | Grupo de ICMS |  |
| `CODTAB` | Inteiro | Tabela preco | → `TGFNTA`.`CODTAB` |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `INDPRECOEMBUT` | Decimal | Percentual |  |
| `FORMULA` | Texto | Formula |  |
| `CLASSIFICMS` | Texto | Classificação de ICMS |  |
| `RETEMISS` | Texto | Retem ISS |  |
| `AD_GRUPOICMS` | Inteiro | Grupo ICMS do Parceiro |  |

**Opções `CLASSIFICMS`:** `P`=Produtor rural, `R`=Revendedor, `X`=Consumidor Contribuinte, `I`=Isento de ICMS, `Z`=Usar do Parceiro, `C`=Consumidor Final, `T`=Usar a da TOP

**Opções `RETEMISS`:** `S`=Retem ISS, `Z`=Verificar no Parceiro, `N`=Não Retem ISS

### TGFPAS
**Parceiro Servico**

**PK:** `CODPARC`, `CODSERV`  
**entityName:** `ParceiroServico`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODSERV` 🔑 | Inteiro | Servico | → `TGFPRO`.`CODPROD` |

### TSIPAI
**Paises**

**PK:** `CODPAIS`  
**Referenciada por:** 8 tabelas  
**entityName:** `NacionalidadeParceiro`, `Pais`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPAIS` 🔑 | Inteiro | Codigo do pais |  |
| `DESCRICAO` | Texto | Descrição |  |
| `ABREVIATURA` | Texto | Abreviatura |  |
| `CODPAISFIS` | Inteiro | Pais Domicilio Fiscal |  |
| `TIMNACIONALIDAD` | Texto | Nacionalidade |  |

### TSIREG
**Regiões**

**PK:** `CODREG`  
**Referenciada por:** 10 tabelas  
**entityName:** `Regiao`, `Regiao2`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODREG` 🔑 | Inteiro | Cod.Região |  |
| `NOMEREG` | Texto | Nome |  |
| `ATIVA` | Texto | Ativa |  |
| `ANALITICA` | Texto | Analitica |  |
| `CODTAB` | Inteiro | Tabela Preco | → `TGFNTA`.`CODTAB` |
| `CODTABMIN` | Inteiro | Tabela Preco Minimo | → `TGFNTA`.`CODTAB` |
| `FRETEMIN` | Decimal | Frete minimo |  |
| `PERCCUSVAR` | Decimal | % Custo Variavel |  |
| `PERCDESCFOB` | Decimal | % Desc. FOB |  |
| `CODVEND` | Inteiro | Vendedor |  |
| `PERCADICIONAL` | Decimal | Perc. Adicional |  |
| `PERCPREMIO` | Decimal | Perc. Premio |  |
| `GERARRECEITA` | Texto | Tipo |  |
| `VLRANTECIPACAO` | Decimal | Valor |  |
| `GRAU` | Inteiro | Grau |  |
| `CODREGPAI` | Inteiro | Cod.Região Pai |  |
| `SEMANA1_DOM` | Decimal | % Domingo |  |
| `SEMANA1_SEG` | Decimal | % Segunda |  |
| `SEMANA1_TER` | Decimal | % Terca |  |
| `SEMANA1_QUA` | Decimal | % Quarta |  |
| `SEMANA1_QUI` | Decimal | % Quinta |  |
| `SEMANA1_SEX` | Decimal | % Sexta |  |
| `SEMANA1_SAB` | Decimal | % Sabado |  |
| `SEMANA2_DOM` | Decimal | % Domingo |  |
| `SEMANA2_SEG` | Decimal | % Segunda |  |
| `SEMANA2_TER` | Decimal | % Terca |  |
| `SEMANA2_QUA` | Decimal | % Quarta |  |
| `SEMANA2_QUI` | Decimal | % Quinta |  |
| `SEMANA2_SEX` | Decimal | % Sexta |  |
| `SEMANA2_SAB` | Decimal | % Sabado |  |
| `VENDAMIN` | Decimal | Venda Minima |  |

**Opções `ANALITICA`:** `S`=Sim, `N`=Não

**Opções `ATIVA`:** `N`=Não, `S`=Sim

**Opções `GERARRECEITA`:** `N`=Ajuda de Custo, `S`=Adiantamento

### TSIRTEF
**RedesTEF**

**PK:** `REDE`  
**Referenciada por:** 1 tabelas  
**entityName:** `RedesTEF`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REDE` 🔑 | Texto | Rede |  |
| `DESCRICAO` | Texto | Descrição |  |

### TGCCRED
**Grupo para Analise de Credito**

**PK:** `CODCRED`  
**Referenciada por:** 3 tabelas  
**entityName:** `GrupoAnaliseCredito`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCRED` 🔑 | Inteiro | Cod.Credito |  |
| `DESCRCRED` | Texto | Descrição Credito |  |
| `FORMULALC` | Texto | Formula Limite de Credito |  |
| `FORMULALCM` | Texto | Formula Credito Mensal |  |
| `DTALTER` | Data/Hora | Data Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TGCPAR
**GC Limites de Credito**

**PK:** `CODPARC`, `DTCALC`, `CODCRED`  
**entityName:** `LimiteCredito`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod.Parceiro | → `TGFPAR`.`CODPARC` |
| `DTCALC` 🔑 | Data/Hora | Data Calculo |  |
| `CODCRED` 🔑 | Inteiro | Cod.Credito |  |
| `LIMCREDCALC` | Decimal | Calculo Limite Credito |  |
| `LIMCREDMENSALCALC` | Decimal | Calculo Limite Credito Mensal |  |
| `CODUSUCALC` | Inteiro | Cod. Usuario Calculo | → `TSIUSU`.`CODUSU` |
| `DTEFETIVACAO` | Data/Hora | Data Efetivação |  |
| `LIMCRED` | Decimal | Limite Credito |  |
| `LIMCREDMENSAL` | Decimal | Limite Credito Mensal |  |
| `OBS` | Texto | Observação |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TCBPLA
**Plano de contas**

**PK:** `CODCTACTB`  
**Referenciada por:** 42 tabelas  
**entityName:** `PLanoContaConta2`, `PlanoConta`, `PlanoConta2`, `PlanoConta3`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCTACTB` 🔑 | Inteiro | Conta reduzida |  |
| `DESCRCTA` | Texto | Descrição |  |
| `CODLALURB` | Texto | Codigo Parte B do e-LALUR |  |
| `CTACTB` | Texto | Conta contabil |  |
| `PODELANCTOMANUAL` | Texto | Aceita lancamento manual |  |
| `CODCONTA` | Inteiro | Codigo da Conta |  |
| `DESCRCONTA` | Texto | Descrição |  |
| `ANALITICA` | Texto | Analitica |  |
| `TABELALALURB` | Texto | Tabela lalurb |  |
| `PROJOBRIG` | Texto | Projeto obrigatorio |  |
| `CENCUSOBRIG` | Texto | Centro de Resultado obrigatorio |  |
| `BEMORIGINAL` | Texto | Bem Original |  |
| `BEMRESREAV` | Texto | Reserva de Reavaliação |  |
| `BEMOUTROS` | Texto | Outros acrescimos |  |
| `ATIVA` | Texto | Ativa |  |
| `CODGRUPOCTA` | Texto | Grupo de Conta |  |
| `RECDESP` | Texto | Tipo |  |
| `CODCTACTBSUBST` | Inteiro | Conta Substituta |  |
| `DTINCLUSAO` | Data/Hora | Referencia de ativação |  |
| `DTINATIV` | Data/Hora | Referencia de inativação |  |
| `DTALTER` | Data/Hora | Dt. Alteração |  |
| `CODUSU` | Inteiro | Usuario |  |
| `CODEMP` | Inteiro | Codigo da empresa | → `TCBEMP`.`CODEMP` |
| `GRAU` | Inteiro | Grau |  |
| `OBSERVACOES` | Texto | Observação |  |
| `PROCESSO` | Inteiro | Processo |  |
| `PRODUTO` | Inteiro | Produto |  |
| `PLANTA` | Inteiro | Planta |  |
| `CODCTACTBPAI` | Inteiro | Cod. conta reduzida pai |  |
| `CONVSALDOMOEDA` | Texto | Conversão do saldo para moeda |  |
| `DTBASECONVMOEDA` | Texto | Data base conversão de moedas |  |
| `LALUR_A` | Texto | Parte A do e-LALUR |  |
| `LALUR_A_CRED` | Texto | Part A of e-LALUR (Saldo Credor) |  |
| `INDTRIBLALURB` | Texto | Indicador Tributos Parte B do e-LALUR |  |
| `TIPSALALUR` | Inteiro | Tipo de Saldo e-LALUR |  |
| `CODRAZAUX` | Inteiro | Cod. Razão Auxiliar |  |
| `TABELA` | Texto | Tabela |  |
| `TABELACRED` | Texto | Tabela |  |
| `NATUREZAEFD` | Inteiro | Natureza para EFD |  |
| `ESTORNO` | Texto | Conta de estorno |  |
| *... +12 campos* | | | |

**Opções `ADICOESCSLL`:** `N`=Não, `S`=Sim

**Opções `ADICOESIRPJ`:** `S`=Sim, `N`=Não

**Opções `ANALITICA`:** `N`=Não, `S`=Sim

**Opções `ATIVA`:** `S`=Sim, `N`=Não

**Opções `BEMORIGINAL`:** `S`=Sim, `N`=Não
