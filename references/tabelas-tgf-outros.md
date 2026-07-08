# Tabelas TGF — Complementares

Tabelas TGF complementares: fiscal, tributação, comissões, MDF-e, NF-e,
cobrança, tarefas agendadas, alíquotas e configurações adicionais.

### TGFAAXN
**Autorização de Acesso ao XML da NF-e**

**PK:** `CODEMP`, `CODPARC`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODPARC` 🔑 | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |

### TGFACO
**Acordos**

**PK:** `NUACORDO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUACORDO` 🔑 | Inteiro | Numero do Acordo |  |
| `DTACORDO` | H | Data do Acordo |  |
| `DHVAL` | H | Data de Validade |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFCTT`.`CODPARC` |
| `CODCONTATO` | Inteiro | Contato | → `TGFCTT`.`CODCONTATO` |
| `VLRMINPED` | Decimal | Valor minimo do pedido |  |
| `VIAPEDIDO` | Texto | Via para o Pedido |  |
| `EXIGEAPROVPED` | Texto | Exige Aprovação do Pedido |  |
| `CODUSURESP` | Inteiro | Cod. Usuario Responsavel | → `TSIUSU`.`CODUSU` |
| `CODTIPOPER` | Inteiro | Cod.Tipo Operação |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODNAT` | Inteiro | Cod. Natureza | → `TGFNAT`.`CODNAT` |
| `TIPEST` | Texto | Tipo de Estoque |  |
| `ANALISARGIRO` | Inteiro | Analisar giro |  |
| `DIASAVISOVALIDADE` | Inteiro | Dias de aviso para validade |  |
| `GERARPED` | Texto | Gerar pedido |  |
| `CODLOCALORIG` | Inteiro | Local Origem | → `TGFLOC`.`CODLOCAL` |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `CODUSUCOT` | Inteiro | CODUSUCOT | → `TSIUSU`.`CODUSU` |
| `CODUSU` | Inteiro | Cod. Usuario |  |

### TGFACPRB
**Ajustes p/ CPRB**

**PK:** `CODEMP`, `DTREF`, `CODCPRB`, `CODOBRA`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `DTREF` 🔑 | Data | Periodo |  |
| `CODCPRB` 🔑 | Texto | Codigo de atividade | → `TGFCPRB`.`CODCPRB` |
| `CODOBRA` 🔑 | Texto | Codigo da obra |  |
| `VLRTOTEXCLUSAO` | Decimal | Valor Total das Exclusões |  |
| `VLRTOTADICAO` | Decimal | Valor Total das Adições |  |

### TGFACR
**Acerto Carga**

**PK:** `CODEMP`, `ORDEMCARGA`, `CODTIPTIT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPTIT` 🔑 | Inteiro | Tipo Titulo | → `TGFTIT`.`CODTIPTIT` |
| `DESCRTIPTIT` | Texto | Descrição do Titulo |  |
| `VALOR` | Decimal | Valor retornado |  |
| `ESPERADO` | Decimal | Esperado |  |
| `BAIXADO` | Decimal | Baixado |  |
| `TRANSF` | Decimal | Transferencia |  |
| `TRANSFDIF` | Texto | Transferir diferenca entre Retornado e Baixado |  |
| `ORDEMCARGA` 🔑 | Inteiro | Ordem de Carga |  |
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `TROCO` | Decimal | Troco |  |

**Opções `TRANSFDIF`:** `N`=Não, `S`=Sim

### TGFACT
**Acompanhamento de Notas**

**PK:** `NUNOTA`, `SEQUENCIA`, `DHOCOR`, `HRACT`  

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

### TGFAEV
**Acompanhamento de Eventos de NFe**

**PK:** `NUNOTA`, `CODEVENTO`, `SEQEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `OCORRENCIA` | C | Ocorrenvia |  |
| `NUNOTA` 🔑 | Inteiro | NUNOTA | → `TGFCAB`.`NUNOTA` |
| `CODEVENTO` 🔑 | Inteiro | CODEVENTO |  |
| `SEQEVENTO` 🔑 | Inteiro | SEQEVENTO |  |
| `DHOCOR` | H | DHOCOR |  |

### TGFAGE
**(sem descrição)**

**PK:** `CODAGENDA`  
**Referenciada por:** 2 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFAJA
**Ajuste Apuração**

**PK:** `NUAJA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAJA` 🔑 | Inteiro | Nro. unico ajuste |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `DTREF` | Data | Referencia |  |
| `TIPAJUSTE` | Inteiro | Tipo ajuste |  |
| `TIPIMPOSTO` | Texto | Tipo imposto |  |
| `TIPAPURACAO` | Inteiro | Tipo apuração |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `NUMDA` | Texto | Nro doc. arrecadação |  |
| `CODUF` | Inteiro | UF | → `TSIUFS`.`CODUF` |
| `NUMPROCESSO` | Texto | Numero processo |  |
| `ORIGPROCESSO` | Inteiro | Origem processo |  |
| `DESCRPROCESSO` | Texto | Descrição processo |  |
| `CODOBSPADRAO` | Inteiro | Observação padrão | → `TGFOBS`.`CODOBSPADRAO` |
| `APURACAOUF` | Texto | Apuração por UF |  |
| `VLRAJUSTE` | Decimal | Valor ajuste |  |
| `OBSERVACAO` | Texto | Observação |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | H | Data alteração |  |
| `CODAJUSTE` | Texto | Codigo ajuste |  |
| `DEBESP` | Texto | Debitos especiais |  |
| `SUBAPURACAO` | Texto | Sub-Apuração |  |
| `INDSUBAPURACAO` | Texto | Indicador de Sub-Apuração |  |
| `CODCFG` | Decimal | Codigo Configuração Ajuste Apuração |  |
| `REGAJDIME` | Texto | Registro do Ajuste na DIME SC |  |

**Opções `APURACAOUF`:** `null`=Não, `S`=Sim

**Opções `DEBESP`:** `N`=Não, `S`=Sim

**Opções `INDSUBAPURACAO`:** `3`=Apuração 1, `4`=Apuração 2, `5`=Apuração 3, `6`=Apuração 4, `7`=Apuração 5, `8`=Apuração 6

**Opções `ORIGPROCESSO`:** `1`=Justica Federal, `9`=Outros, `0`=Sefaz, `2`=Justica Estadual

**Opções `REGAJDIME`:** `60`=Item 60 - Outros Estornos de Credito, `65`=Item 65 - Estorno de Credito da Entrada em Decorrencia da Utilização de Credito Presumido

**Opções `SUBAPURACAO`:** `S`=Sim, `N`=Não

### TGFAJC
**Tabela de Controle Creditos Fiscais**

**PK:** `NUAJA`, `SEQUENCIA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAJA` 🔑 | Inteiro | Nro. unico ajuste | → `TGFAJA`.`NUAJA` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `SALDOCREDANT` | Decimal | Saldo Cred. Ant. |  |
| `CREDAPROPRIADO` | Decimal | Credito Apropriado |  |
| `CREDRECEBIDO` | Decimal | Credito Recebido |  |
| `CREDUTILIZADO` | Decimal | Credito Utilizados |  |
| `SALDOCREDPROX` | Decimal | Saldo Cred. Prox. |  |
| `CODUSU` | Inteiro | Cod. usuario |  |
| `DTALTER` | Data | Dt. Alteração |  |

### TGFALI
**Aliquotas**

**PK:** `NUNOTA`, `ALIQUOTA`, `TIPO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Numero da nota |  |
| `ALIQUOTA` 🔑 | Decimal | Aliquota |  |
| `BASEIMP` | Decimal | Base do imposto |  |
| `VLRIMP` | Decimal | Valor do imposto |  |
| `TIPO` 🔑 | Texto | Tipo |  |

### TGFANB
**Antecipação de recebiveis**

**PK:** `NUANTBANC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUANTBANC` 🔑 | Inteiro | Nro. unico |  |
| `DTANTBANC` | Data | Dt. Antecipação |  |
| `NUFINTITORI` | Inteiro | Titulo Original | → `TGFFIN`.`NUFIN` |
| `NUFINTITBAN` | Inteiro | Antecipação | → `TGFFIN`.`NUFIN` |
| `NUFINDESPOP` | Inteiro | Demais Despesas Operacionais |  |
| `NUFINTITJUR` | Inteiro | Taxas de Antecipação | → `TGFFIN`.`NUFIN` |
| `NUFINTITOBR` | Inteiro | Obrigação ao Banco | → `TGFFIN`.`NUFIN` |
| `DOCANTBANC` | Texto | Nro. documento |  |
| `NUFINDESPADIC` | Inteiro | Despesa adicional |  |
| `STATUSANT` | Texto | Status antecipação |  |
| `NUFINTITIOF` | Inteiro | Despesa com IOF |  |

**Opções `STATUSANT`:** `A`=Antecipado, `B`=Antecipado e baixado, `N`=Antecipado não pago

### TGFAPU
**Usuario por Tipo de Amostra**

**PK:** `CODTIPAMOSTRA`, `CODUSUAPU`, `TIPOMANIPULACAO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUSUAPU` 🔑 | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `CODTIPAMOSTRA` 🔑 | Inteiro | Tipo de Amostra | → `TGFTAM`.`CODTIPAMOSTRA` |
| `TIPOMANIPULACAO` 🔑 | Texto | Tipo Manipulação |  |
| `CODUSU` | Inteiro | Usuario Alteração | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | Data e Hora de Alteração |  |

**Opções `TIPOMANIPULACAO`:** `F`=Verificador, `C`=Amostrador, `T`=Analista

### TGFARE
**Analise de Rentabilidade**

**PK:** `NUNOTA`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Numero Unico da Nota | → `TGFITE`.`NUNOTA` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia | → `TGFITE`.`SEQUENCIA` |
| `VLRUNIT` | Decimal | Valor Unitario |  |
| `VLRCPA` | Decimal | Valor da Compra |  |
| `VLRCUSTO` | Decimal | Calor de Custo |  |

### TGFARM
**Apuração da Receita Mensal**

**PK:** `NUAPURACAO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAPURACAO` 🔑 | Inteiro | Nro. Apuração |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `DTREF` | Data | Referencia |  |
| `STATUS` | Texto | Status da Apuração |  |
| `TIPOINSERCAO` | Texto | Tipo da Inserção |  |
| `FATORR` | Decimal | Fator R |  |
| `ATIVO` | Texto | Ativo |  |
| `VLRTOTRECMENINT` | Decimal | Total da Receita Bruta Mensal |  |
| `VLRTOTRECPROJINT` | Decimal | Total da Receita Bruta Mensal Projetada |  |
| `VLRTOTRECACUMINT` | Decimal | Total da Receita Bruta Acumulada (12 meses) |  |
| `VLRTOTRECMENEXT` | Decimal | Total da Receita Bruta Mensal |  |
| `VLRTOTRECPROJEXT` | Decimal | Total da Receita Bruta Mensal Projetada |  |
| `VLRTOTRECACUMEXT` | Decimal | Total da Receita Bruta Acumulada (12 meses) |  |
| `VLRTOTRECMEN` | Decimal | Total da Receita Bruta Mensal |  |
| `VLRTOTRECPROJ` | Decimal | Total da Receita Bruta Mensal Projetada |  |
| `VLRTOTRECACUM` | Decimal | Total da Receita Bruta Acumulada (12 meses) |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `STATUS`:** `F`=Fechada, `A`=Aberta

**Opções `TIPOINSERCAO`:** `M`=Manual, `A`=Automatica

### TGFAVE
**Averbações do Seguro MDF-e**

**PK:** `NUVIAG`, `SEQMDFE`, `NUMAPOLICE`, `NUMAVERB`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUVIAG` 🔑 | Inteiro | Nro. Viagem | → `TGFMDFESEG`.`NUVIAG` |
| `SEQMDFE` 🔑 | Inteiro | Sequencia do manifesto | → `TGFMDFESEG`.`SEQMDFE` |
| `NUMAPOLICE` 🔑 | Texto | Nro. Apolice | → `TGFMDFESEG`.`NUMAPOLICE` |
| `NUMAVERB` 🔑 | Texto | Nro. Averbação |  |

### TGFB460
**Dedução do ISSQN**

**PK:** `CODEMP`, `DTINICIO`, `SEQUENCIA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `DTINICIO` 🔑 | Data | Data Inicial |  |
| `IND_DEDUCAO` | Inteiro | Indicador de Dedução |  |
| `VLRAJUSTE` | Decimal | Valor da Dedução |  |
| `NUM_PROC` | Texto | N do Processo |  |
| `IND_PROC` | Inteiro | Indicador do Processo |  |
| `DESC_PROC` | Texto | Descrição do Processo |  |
| `COD_INF_OBS` | Inteiro | Cod. Referencia da Obs |  |
| `INDOBRIGACAO` | Inteiro | Ajustes de Apuração do ISSQN |  |

**Opções `COD_INF_OBS`:** `0`=Entradas e aquisições, `1`=Saidas e prestações

**Opções `INDOBRIGACAO`:** `0`=0-ISS Proprio, `1`=1-ISS substituto (devido pelas aquisições de servicos do declarante), `2`=2-ISS Uniprofissionais

**Opções `IND_DEDUCAO`:** `0`=Compensação do ISSQN calculado a maior, `1`=Beneficio fiscal por incentivo a cultura, `2`=Decisão administrativa ou judicial, `9`=Outros

**Opções `IND_PROC`:** `0`=Sefaz, `1`=Justica Federal, `2`=Justica Estadual, `9`=Outros

### TGFCAI
**Controle de Caixas**

**PK:** `NUCAIXA`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCAIXA` 🔑 | Inteiro | Num. Caixa |  |
| `CODPDV` | Inteiro | Codigo do PDV | → `TGFPDV`.`CODPDV` |
| `DTABERTURA` | H | Dt. Abertura |  |
| `DTFECHAMENTO` | H | Dt. Fechamento |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `CODCTABCOINT` | Inteiro | Conta | → `TSICTA`.`CODCTABCOINT` |
| `SALDOINICIAL` | Decimal | Saldo Inicial |  |
| `RECEITA` | Decimal | Receita |  |
| `DESPESA` | Decimal | Despesa |  |
| `CONFERIDO` | Texto | Conferido |  |

**Opções `CONFERIDO`:** `N`=Não, `S`=Sim

### TGFCES
**Estrutura**

**PK:** `NUEST`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUEST` 🔑 | Inteiro | Numero da Estrutura |  |
| `DESCRICAO` | Texto | Descrição |  |
| `TIPVISUAL` | Texto | TIPVISUAL |  |
| `DESCRROOT` | Texto | Descrição Root |  |

### TGFCFI
**(sem descrição)**

**PK:** `NUFIDEL`  
**Referenciada por:** 2 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFCFR
**Tabela Calculo de Frete**

**PK:** `NUCFR`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCFR` 🔑 | Inteiro | Cod. Calculo de frete |  |
| `DESCRCALCFRET` | Texto | Descrição |  |
| `OBSERVACAO` | Texto | Observação |  |
| `SERVICOECT` | Texto | Servico Correios | → `TGFECT`.`CODSERVICO` |
| `CRITERIORATFRETE` | Texto | Rateio frete |  |

**Opções `CRITERIORATFRETE`:** `M`=Metro cubico, `P`=Peso, `V`=Valor da nota

### TGFCFRC
**Regiao Rota Calculo Frete**

**PK:** `NUCFR`, `CODREG`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCFR` 🔑 | Inteiro | Cod. Rota | → `TGFCFR`.`NUCFR` |
| `CODREG` 🔑 | Inteiro | Cod. Região |  |
| `NOMEREG` | Texto | Região |  |

### TGFCIPM
**Codigo do Item IPM**

**PK:** `CODUF`, `CODIGOITEM`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUF` 🔑 | Inteiro | Codigo UF | → `TSIUFS`.`CODUF` |
| `CODIGOITEM` 🔑 | Texto | Codigo Item |  |
| `DESCRICAO` | Texto | Descrição |  |
| `DTINICIAL` | Data | Dt. Inicial |  |
| `DTFINAL` | Data | Dt. Final |  |
| `FORMULAIPM` | Texto | Formula |  |

### TGFCMB
**(sem descrição)**

**PK:** `CODCOMBO`  
**Referenciada por:** 2 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFCMP
**(sem descrição)**

**PK:** `CODCMP`  
**Referenciada por:** 2 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFCMV
**Config. Consolidação de movimentos**

**PK:** `CODCONFIG`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONFIG` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `DHULTEXEC` | H | Dt. ult. execução |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHALTER` | Data | Dt. Alteração |  |
| `AGRUPAPARC` | Texto | Parceiro |  |
| `AGRUPAVENDEDOR` | Texto | Vendedor |  |
| `AGRUPACENCUS` | Texto | Centro de Resultado |  |
| `AGRUPANATUREZA` | Texto | Natureza |  |
| `AGRUPAPROJETO` | Texto | Projeto |  |
| `AGRUPATOP` | Texto | Tipo Operação |  |
| `AGRUPASUBTIPVEN` | Texto | Subtipo de Negociação |  |
| `AGRUPALOCAL` | Texto | Local Estoque |  |
| `TIPDTVEN` | Inteiro | Na venda |  |
| `TIPDTCOM` | Inteiro | Na compra |  |
| `TIPDTDEVVEN` | Inteiro | Na devolução da venda |  |
| `TIPDTDEVCOM` | Inteiro | Na devolução da compra |  |
| `TIPDTGASTOFIX` | Inteiro | Data para Gastos Fixos |  |
| `TIPOCUSTO` | Inteiro | Custo a ser considerado |  |
| `TEMCOMISSAO` | Inteiro | Tem comissão |  |
| `IMPRETNOTA` | Texto | Considerar impostos retidos no valor da nota |  |
| `FORMGASTOFIX` | Inteiro | Formação do gasto fixo |  |
| `RATGASTOFIX` | Decimal | Rateio do Gasto Fixo no periodo |  |
| `PERCUSTOFIX` | Decimal | % de Custo Fixo |  |
| `COMISSAOPOR` | Inteiro | Comissão por |  |
| `PERCCOMISSAO` | Decimal | Porcentagem |  |
| `HORAAGENDA1` | Texto | Hora primeira atualização (diario) |  |
| `HORAAGENDA2` | Texto | Hora segunda atualização (diario) |  |
| `TEMPOPROCESSAMENTO` | Inteiro | Tempo de processamento (minutos) |  |
| `DHPROXEXEC` | H | Dt. prox. execução |  |
| `INTERVALOATUALIZACAO` | Inteiro | Qtd. meses a retroagir |  |
| `TIPCONFIG` | Inteiro | Inicio da consolidação |  |
| `DTCONS` | Data | Data inicial |  |
| `QTDMESESCONSOLIDAR` | Inteiro | Qtd. meses consolidar |  |
| `AUTOMATICO` | Texto | Consolidação inserida automaticamente |  |
| `TIPFATPER` | Inteiro | Faturamento Personalizado |  |
| `USACONFNATRECDESP` | Texto | Usar as configurações do cadastro de Naturezas de Receitas e Despesas |  |

**Opções `AUTOMATICO`:** `S`=Sim, `N`=Não, `I`=Inativo

**Opções `TIPCONFIG`:** `0`=Fixa, `1`=Variavel

**Opções `TIPFATPER`:** `0`=Faturamento Bruto, `2`=Faturamento liquido (sem impostos), `1`=Faturamento Bruto sem IPI e ICMS ST

### TGFCOC
**ConvenioConta**

**PK:** `CODCTABCOINT`, `CONVENIO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCTABCOINT` 🔑 | Inteiro | Conta bancaria | → `TSICTA`.`CODCTABCOINT` |
| `CONVENIO` 🔑 | Inteiro | Convenio |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | H | Data alteração |  |
| `REMBCO` | Inteiro | Ultimo boleto |  |
| `REMBCOMAX` | Inteiro | Numero maximo |  |
| `ZERARAUT` | Texto | Zerar automaticamente |  |

**Opções `ZERARAUT`:** `N`=Não, `S`=Sim

### TGFCOI2
**Item conferencia**

**PK:** `NUCONF`, `SEQCONF`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONF` 🔑 | Inteiro | Nro conferencia | → `TGFCON2`.`NUCONF` |
| `SEQCONF` 🔑 | Inteiro | Sequencia |  |
| `CODBARRA` | Texto | Cod. Barras |  |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODVOL` | Texto | UN | → `TGFVOL`.`CODVOL` |
| `CONTROLE` | Texto | Controle |  |
| `QTDCONFVOLPAD` | Decimal | Qtd UN padrão |  |
| `QTDCONF` | Decimal | Qtd conferida |  |
| `COPIA` | Texto | Copia |  |
| `DHALTER` | H | Dt. Alteração |  |

### TGFCON
**Conferencia de Pedidos**

**PK:** `NUCONF`, `SEQUENCIA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONF` 🔑 | Inteiro | Numero unico de conferencia de Pedido |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia unica de conferencia de Pedido |  |
| `CODBARRA` | Texto | Codigo de Barras |  |
| `QTD` | Decimal | Quantidade do pedido |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHCONF` | Data | Dt. Conferencia |  |
| `TIPOCONF` | Texto | Tipo |  |

### TGFCON2
**Cabecalho conferencia**

**PK:** `NUCONF`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONF` 🔑 | Inteiro | Nro conferencia |  |
| `NUNOTAORIG` | Inteiro | Nro nota conferencia | → `TGFCAB`.`NUNOTA` |
| `STATUS` | Texto | Status |  |
| `NUCONFORIG` | Inteiro | Nro conferencia origem | → `TGFCON2`.`NUCONF` |
| `DHINICONF` | H | Data hora inicio |  |
| `DHFINCONF` | H | Data hora final |  |
| `CODUSUCONF` | Inteiro | Cod. Conferente | → `TSIUSU`.`CODUSU` |
| `QTDVOL` | Inteiro | Qtd. volume da conferencia |  |
| `NUPEDCOMP` | Inteiro | Num. pedido complementar |  |
| `NUNOTADEV` | Inteiro | Num. nota de devolução |  |

### TGFCOT
**Cabecalho Cotação**

**PK:** `NUMCOTACAO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCOTACAO` 🔑 | Inteiro | Nro. da Cotação |  |
| `DHINIC` | Data | Data inicial da cotação |  |
| `DHFINAL` | Data | Data final da cotação |  |
| `CODUSURESP` | Inteiro | Usuario Responsavel | → `TSIUSU`.`CODUSU` |
| `CODUSUREQ` | Inteiro | Usuario Comprador | → `TSIUSU`.`CODUSU` |
| `PESOPRECO` | Inteiro | Preco |  |
| `PESOCONDPAG` | Inteiro | Condições de pagamento |  |
| `PESOTAXAJURO` | Inteiro | Taxa de Juro |  |
| `PESOPRAZOENTREG` | Inteiro | Prazo de entrega |  |
| `PESOQUALPROD` | Inteiro | Qualidade do Produto |  |
| `PESOCONFIABFORN` | Inteiro | Confiabilidade do fornecedor |  |
| `PESOQUALATEND` | Inteiro | Qualidade Atendimento |  |
| `PESOGARANTIA` | Inteiro | Garantia |  |
| `PESOPRAZOMED` | Inteiro | Prazo Medio |  |
| `SITUACAO` | Texto | Situação |  |
| `DTALTER` | H | Data de alteração |  |
| `GERPEDREAL` | Texto | Gera Pedido Real |  |
| `CODNAT` | Inteiro | Natureza | → `TGFNAT`.`CODNAT` |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `OBSERVACAO` | Texto | Observações |  |
| `CODUSU` | Inteiro | Usuario Lancamento | → `TSIUSU`.`CODUSU` |
| `CODCENCUS` | Inteiro | Centro de Resultado | → `TSICUS`.`CODCENCUS` |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `NUNOTAORIG` | Inteiro | Nro Unico do Pedido Origem | → `TGFCAB`.`NUNOTA` |
| `NUMNOTAORIG` | Inteiro | Nro do Pedido de Origem |  |
| `OBSMOTCANC` | Texto | Observação Motivo de Cancelamento |  |
| `VALPROPOSTA` | Inteiro | Validade Proposta |  |
| `CODMOTCAN` | Inteiro | Codigo Motivo de Cancelamento | → `TGFMTC`.`CODIGO` |
| `CODTIPVENDA` | Inteiro | Forma de Pagamento |  |
| `PRAZOENTREGA` | Inteiro | Prazo de Entrega |  |
| `MODFRETE` | Texto | Modalidade de Frete |  |

**Opções `SITUACAO`:** `A`=Aberta, `C`=Cancelada, `E`=Em aprovação, `P`=Aprovada, `F`=Fechada

### TGFCPRB
**Tabela Atividades, Prods. e Sers. p/ CPRB**

**PK:** `CODCPRB`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCPRB` 🔑 | Texto | Cod. Atividade (Prest. Servicos e Produtos) |  |
| `DTINICIAL` | Data | Data Inicial |  |
| `DTFINAL` | Data | Data Final |  |
| `CODRECOLHIMENTO` | Inteiro | Codigo de Recolhimento |  |
| `ALIQUOTA` | Decimal | Aliquota |  |
| `CODCTACTB` | Inteiro | Conta contabil |  |
| `DESCATIVIDADE` | Texto | Desc. Atividade (Prest. Servicos e Produtos) |  |

### TGFCRPC
**Credito de PIS e COFINS**

**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` | Inteiro | Empresa |  |
| `TIPO` | Texto | Tipo |  |
| `PER_APU_CRED` | Data | Periodo de Apuração |  |
| `ORIG_CRED` | Texto | Origem do Credito |  |
| `CNPJ_SUC` | Texto | CNPJ Sucessão |  |
| `CNPJ` | Texto | CNPJ |  |
| `COD_CRED` | Inteiro | Codigo do Credito |  |
| `VL_CRED_APU` | Decimal | Vlr. Total do Credito Apurado |  |
| `VL_CRED_EXT_APU` | Decimal | Vlr. do Credito Extemporaneo Apurado |  |
| `SALDO` | Decimal | Saldo |  |

**Opções `ORIG_CRED`:** `01`=01 - Credito decorrente de operações proprias, `02`=02 - Credito transferido por pessoa juridica sucedida

**Opções `TIPO`:** `P`=PIS, `C`=COFINS

### TGFCVG
**Comissão Vendedor Grupo**

**PK:** `CODVEND`, `CODGRUPOPROD`, `CODTIPPARC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPPARC` 🔑 | Inteiro | Perfil Principal Parceiro | → `TGFTPP`.`CODTIPPARC` |
| `CODGRUPOPROD` 🔑 | Inteiro | Grupo de Produtos | → `TGFGRU`.`CODGRUPOPROD` |
| `CODVEND` 🔑 | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `COMISSAO` | Decimal | Comissão do Vendedor |  |

### TGFDACPRB
**Detalhes dos Ajustes p/ CPRB**

**PK:** `CODEMP`, `DTREF`, `CODCPRB`, `CODOBRA`, `TIPOAJUSTE`, `CODAJUSTE`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFACPRB`.`CODEMP` |
| `DTREF` 🔑 | Data | Periodo | → `TGFACPRB`.`DTREF` |
| `CODCPRB` 🔑 | Texto | Codigo de atividade | → `TGFACPRB`.`CODCPRB` |
| `CODOBRA` 🔑 | Texto | Codigo da obra | → `TGFACPRB`.`CODOBRA` |
| `TIPOAJUSTE` 🔑 | Inteiro | Tipo do ajuste |  |
| `CODAJUSTE` 🔑 | Inteiro | Codigo do ajuste |  |
| `VLRAJUSTE` | Decimal | Valor do ajuste |  |
| `DESCRAJUSTE` | Texto | Descrição do ajuste |  |

**Opções `CODAJUSTE`:** `1`=1 - Ajuste da CPRB: Adoção do Regime de Caixa, `2`=2 - Ajuste da CPRB: Diferimento de Valores a recolher no periodo, `3`=3 - Adição de valores Diferidos em Periodo(s) Anteriores(es), `4`=4 - Exportações diretas, `5`=5 - Transporte internacional de cargas, `6`=6 - Vendas canceladas e os descontos incondicionais concedidos, `7`=7 - IPI, se incluido na receita bruta, `8`=8 - ICMS, quando cobrado na condição de substituto, `9`=9 - Receita bruta reconhecida pela construção, recuperação, reforma, etc, `10`=10 - O valor do aporte de recursos realizado nos termos do art 6 3 inciso III da Lei 11.079/2004, `11`=11 - Demais ajustes oriundos da Legislação Tributaria, estorno ou outras situações

**Opções `TIPOAJUSTE`:** `0`=0 - Ajuste de Exclusão, `1`=1 - Ajuste de Adição

### TGFDCTF
**DCTF - Configurações**

**PK:** `CODEMP`, `DTREF`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `REPROCESSATOT` | Texto | Reprocessar totalizadores |  |
| `DTREF` 🔑 | Data | Referencia |  |
| `RETIFICADORA` | Texto | Retificadora |  |
| `NUMRECIBO` | Texto | Numero do Recibo |  |
| `REPRESENTANTEPJ` | Texto | Representante da PJ |  |
| `CODSIGREPRESENTANTE` | Inteiro | Signatario |  |
| `RESPONSAVELPR` | Texto | Responsavel pelo Preenchimento |  |
| `CODSIGPREENCHIMENTO` | Inteiro | Signatario |  |
| `SITUACAO` | Texto | Situação da Empresa |  |
| `DTEVENTO` | Data | Data do Evento |  |
| `FORMATRIB` | Texto | Forma de Tributação do Lucro |  |
| `QUALIFICACAOPJ` | Texto | Qualificação da Pessoa Juridica |  |
| `PJBALANCO` | Texto | PJ levantou Balanco/Balancete de suspensão no mes |  |
| `PJDEBITOS` | Texto | PJ com debitos de SCP a serem declarados |  |
| `PJOPTANTESN` | Texto | PJ optante pelo Simples Nacional |  |
| `PJINATIVA` | Texto | PJ inativa no mes da declaração |  |
| `TIPOREGIME` | Texto | Criterio Rec. Variações Monet. Taxa de Cambio |  |
| `REGIMEAPURACAO` | Texto | Regime de Apuração da Contribuição para o PIS/Pasep e/ou da Cofins |  |
| `SITUACAOPJMES` | Texto | Situação da PJ no mes da declaração |  |
| `BALANCORED` | Texto | Balanco de Redução |  |
| `TIPODIVSALDO` | Texto | O saldo deste debito sera dividido em quotas |  |
| `DEBITOSCPINC` | Texto | Debito de SCP/INC |  |
| `ENVIARCPRB` | Texto | Enviar CPRB na  DCTF |  |
| `PJCPRB` | Texto | PJ optante pela CPRB |  |

**Opções `BALANCORED`:** `N`=Não, `S`=Sim

**Opções `DEBITOSCPINC`:** `2`=INC, `0`=Não e SCP nem INC, `1`=SCP

**Opções `ENVIARCPRB`:** `N`=Não, `S`=Sim

**Opções `FORMATRIB`:** `3`=Arbitrado, `8`=Declarante não e Contribuinte do IRPJ, `4`=Imune do IRPJ, `5`=Isenta do IRPJ, `9`=Não preenchido, `2`=Presumido, `1`=Real / Estimativa, `0`=Real / Trimestral

**Opções `PJBALANCO`:** `N`=Não, `S`=Sim

**Opções `PJCPRB`:** `N`=Não, `S`=Sim

### TGFDCTFR10
**DCTF - Registro R10**

**PK:** `CODEMP`, `DTREF`, `REG`, `CNPJCONTRIB`, `CODRECEITA`  
**Referenciada por:** 15 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFDCTF`.`CODEMP` |
| `DTREF` 🔑 | Data | Periodo de Referencia | → `TGFDCTF`.`DTREF` |
| `REG` 🔑 | Texto | Registro |  |
| `CNPJCONTRIB` 🔑 | Texto | CNPJ do Contribuinte |  |
| `CODRECEITA` 🔑 | Texto | Codigo da Receita |  |
| `ORDEMESTB` | Texto | Ordem do Estabelecimento |  |
| `CNPJCEI` | Texto | CNPJ da Incorporação/Matricula CEI |  |
| `VALORDEBITO` | Decimal | Valor do Debito |  |
| `BALANCORED` | Texto | Balanco de Redução |  |
| `TIPODIVSALDO` | Texto | Tipo de divisão de saldo |  |
| `DEBITOSCPINC` | Texto | Debito de SCP/INC |  |
| `DIGITADO` | Texto | Digitado |  |

**Opções `DIGITADO`:** `S`=Sim, `N`=Não

### TGFDITB
**Integração Tributo Detalhe**

**PK:** `CODEMP`, `TIPOIMP`, `DHIMPORT`  
**Referenciada por:** 9 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Codigo da Empresa | → `TGFCITB`.`CODEMP` |
| `TIPOIMP` 🔑 | Inteiro | Tipo |  |
| `DHIMPORT` 🔑 | H | Data |  |
| `CODUSU` | Inteiro | Usuario |  |
| `STATUS` | Texto | Status |  |

**Opções `STATUS`:** `null`=Pendente, `L`=Liberada

### TGFDMG
**Desconto Maximo Por Grupo e Tabela de Preco**

**PK:** `DTINICIAL`, `CODEMP`, `CODGRUPOPROD`, `CODTAB`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTINICIAL` 🔑 | Data | Data Inicial |  |
| `DTFINAL` | Data | Data Final |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODGRUPOPROD` 🔑 | Inteiro | Grupo Produto | → `TGFGRU`.`CODGRUPOPROD` |
| `CODTAB` 🔑 | Inteiro | Tabela | → `TGFNTA`.`CODTAB` |
| `DESCMAX` | Decimal | % Desconto Maximo |  |
| `BONIFMAX` | Decimal | % Bonificação Maxima |  |

### TGFDVCAB
**Divergencias Cabecalho**

**PK:** `CODEMP`, `REFERENCIA`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `REFERENCIA` 🔑 | Data | Dt. de Referencia |  |

### TGFEFB
**Blocos Escrituracao Fiscal Digital**

**PK:** `CODEMP`, `BLOCO`, `TIPO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TSIEMP`.`CODEMP` |
| `BLOCO` 🔑 | Texto | Bloco |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `DESCRICAO` | Texto | Descrição |  |
| `GERARBLOCO` | Texto | Gerar Bloco |  |
| `TIPO` 🔑 | Inteiro | Tipo |  |

**Opções `GERARBLOCO`:** `N`=Não, `S`=Sim

### TGFENFE
**Eventos de Nota Fiscal Eletronica**

**PK:** `NUNOTA`, `CODEVENTO`, `SEQEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | NUNOTA | → `TGFCAB`.`NUNOTA` |
| `TEXTOCORRECAO` | C | Texto Carta de Correção |  |
| `CODEVENTO` 🔑 | Inteiro | CODEVENTO |  |
| `SEQEVENTO` 🔑 | Inteiro | SEQEVENTO |  |
| `NULOTE` | Inteiro | NULOTE |  |
| `PROCESSADO` | Texto | PROCESSADO |  |
| `NROPROTAUT` | Texto | Nro. Protocolo de Autorização do Evento |  |

### TGFEPP
**Plano de Manutenção**

**PK:** `CODPROD`, `NUMEQ`, `SEQUENCIA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMEQ` 🔑 | Inteiro | Num. Equipamento | → `TGFMEQ`.`NUMEQ` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `PARADA` | Texto | Parada |  |
| `TEMPOESTIMADO` | Inteiro | Tempo estimado |  |
| `OBSERVACAO` | Texto | Observação |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | Dt. Alteração |  |
| `CODVOL` | Texto | Volume | → `TGFVOL`.`CODVOL` |
| `CODPROD` 🔑 | Inteiro | Servico | → `TGFPRO`.`CODPROD` |
| `MINIMO` | Decimal | Minimo |  |
| `MAXIMO` | Decimal | Maximo |  |
| `MULTIPLO` | Texto | Multiplo |  |
| `CODPTC` | Inteiro | Ponto de Controle | → `TGFPTC`.`CODPTC` |
| `PERIODICIDADE` | Inteiro | Periocidade |  |
| `LIMITE` | Decimal | Limite |  |

### TGFEPR
**Etapas do Produto**

**PK:** `CODPROD`, `VARIACAO`, `CODLOCAL`, `CONTROLE`, `CODETAPA`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `VARIACAO` 🔑 | Inteiro | Variação | → `TGFFCP`.`VARIACAO` |
| `CODLOCAL` 🔑 | Inteiro | Local | → `TGFFCP`.`CODLOCAL` |
| `CONTROLE` 🔑 | Texto | Controle | → `TGFFCP`.`CONTROLE` |
| `CODETAPA` 🔑 | Inteiro | Etapa | → `TGFETA`.`CODETAPA` |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `CICLOPRODUCAO` | Decimal | Ciclo de Produção |  |
| `UNIDCICLO` | Texto | Unidade do Ciclo de Produção |  |
| `OBRIGATORIA` | Texto | Obrigatoria |  |
| `FINAL` | Texto | Final |  |
| `ONDEEXEC` | Texto | Executa em |  |

**Opções `FINAL`:** `S`=Sim, `N`=Não

**Opções `OBRIGATORIA`:** `N`=Não, `S`=Sim

**Opções `UNIDCICLO`:** `M`=Minutos, `H`=Horas, `D`=Dias, `E`=Meses, `S`=Segundos

### TGFEQF
**Cadastro Equipamento Fiscal**

**PK:** `CODEQUIP`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEQUIP` 🔑 | Inteiro | Cod. Equipamento |  |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `TIPOEQUIP` | Texto | Tipo equipamento |  |
| `DESCRICAO` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `TIPOEQUIP`:** `MFE`=MFE, `SAT`=SAT, `ECF`=ECF

### TGFETA
**Etapas de Produção**

**PK:** `CODETAPA`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODETAPA` 🔑 | Inteiro | Cod. Etapa |  |
| `NOMEETAPA` | Texto | Nome Etapa |  |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `TIPO` | Texto | Tipo |  |
| `TOPENTRADA` | Inteiro | TOP de Entrada |  |
| `PENDENTEENT` | Texto | A nota fica pendente de confirmação |  |
| `LOCALORIGENT` | Texto | Origem Parceiro Entrada |  |
| `TOPSAIDA` | Inteiro | TOP de Saida |  |
| `PENDENTESAI` | Texto | A nota fica pendente de confirmação |  |
| `LOCALORIGSAI` | Texto | Origem Parceiro Saida |  |
| `CODEMPORIG` | Inteiro | Empresa Origem |  |
| `CODEMPDEST` | Inteiro | Empresa Destino |  |
| `OBSERVACAO` | Texto | Observação |  |
| `CODLOCALENTORIG` | Inteiro | Local Entrada Origem | → `TGFLOC`.`CODLOCAL` |
| `USALOCENTORIGPA` | Texto | Usar Local Entrada Origem da Produção |  |
| `CODLOCALENTDEST` | Inteiro | Local Entrada Destino | → `TGFLOC`.`CODLOCAL` |
| `USALOCENTDESTPA` | Texto | Usar Local Entrada Destino da Produção |  |
| `CODLOCALSAIORIG` | Inteiro | Local Saida Origem | → `TGFLOC`.`CODLOCAL` |
| `USALOCSAIORIGPA` | Texto | Usar Local Saida Origem da Produção |  |
| `CODLOCALSAIDEST` | Inteiro | Local Saida Destino | → `TGFLOC`.`CODLOCAL` |
| `USALOCSAIDESTPA` | Texto | Usar Local Saida Destino da Produção |  |
| `TOPPRODUCAO` | Inteiro | TOP de Produção |  |
| `CODETAPAMP` | Inteiro | Etapa p/Seleção de MPs | → `TGFETA`.`CODETAPA` |
| `AJUSTARMPS` | Texto | Ajustar MPs da Produção com Local.Ent.Destino |  |
| `VALIDAWMS` | Texto | Verifica pendencia no WMS na Saida da Etapa |  |
| `SEQOTICA` | Inteiro | Sequencia Otica |  |
| `TOPDEVMP` | Inteiro | TOP para Devolução de Materia Prima |  |
| `GERARAMOSTRA` | Texto | Gerar Amostra |  |

**Opções `AJUSTARMPS`:** `N`=Não, `S`=Sim

**Opções `GERARAMOSTRA`:** `N`=Não Gerar, `S`=Na Saida, `A`=Em Ambas, `E`=Na Entrada

**Opções `LOCALORIGENT`:** `P`=Local da Produção, `O`=Local de Origem, `D`=Local de Destino

**Opções `LOCALORIGSAI`:** `O`=Local de Origem, `P`=Local da Produção, `D`=Local de Destino

**Opções `PENDENTEENT`:** `S`=Sim, `N`=Não

**Opções `PENDENTESAI`:** `S`=Sim, `N`=Não

### TGFEXPN
**Informações de Nota de Exportação**

**PK:** `NUNOTA`, `NRORE`, `NRODECLARACAO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NRODECLARACAO` 🔑 | Texto | Nro Declaração | → `TGFEXPR`.`NRODECLARACAO` |
| `NRORE` 🔑 | Texto | Nro Registro | → `TGFEXPR`.`NRORE` |
| `NUNOTA` 🔑 | Inteiro | Nro Unico Nota | → `TGFCAB`.`NUNOTA` |
| `DTCONHEC` | Data | Data Conhecimento |  |
| `NROCONHEC` | Texto | Nro Conhecimento |  |
| `TIPOCONHEC` | Inteiro | Tipo Conhecimento |  |

### TGFFCP
**Formula de Composição do Produto**

**PK:** `CODPROD`, `VARIACAO`, `CODLOCAL`, `CONTROLE`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODLOCAL` 🔑 | Inteiro | Local | → `TGFLOC`.`CODLOCAL` |
| `CONTROLE` 🔑 | Texto | Controle |  |
| `VARIACAO` 🔑 | Inteiro | Variação |  |
| `CICLOPRODUCAO` | Decimal | Ciclo de produção |  |
| `UNIDCICLO` | Texto | Unidade do Ciclo |  |
| `MULTIPLOIDEAL` | Inteiro | Multiplo Ideal |  |
| `PRODUCAOMIN` | Decimal | Produção Minima |  |
| `FORMPRINCIPAL` | Texto | Formula principal |  |
| `MARGLUCRO` | Decimal | Margem de lucro |  |
| `ATIVO` | Texto | Ativo |  |
| `DESVIO` | Decimal | Desvio Sup.(%) |  |
| `DESVIOINF` | Decimal | Desvio Inf.(%) |  |
| `OBSERVACAO` | Texto | Observação |  |
| `MENORDTVAL` | Texto | Considerar Menor Dt. Validade |  |
| `REGMAPA` | Texto | Registrada no M.A.P.A |  |
| `VARIACAOREL` | Inteiro | Variação Relacionada |  |
| `CODEST` | Inteiro | Estrutura de Produção | → `TGFESP`.`CODEST` |
| `CODPRC` | Inteiro | Cod. Processo |  |
| `IDPROC` | Inteiro | IDPROC |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `FORMPRINCIPAL`:** `S`=Sim, `N`=Não

**Opções `MENORDTVAL`:** `N`=Não, `S`=Sim

**Opções `REGMAPA`:** `N`=Não, `S`=Sim

**Opções `UNIDCICLO`:** `S`=Segundos, `E`=Meses, `D`=Dias, `H`=Horas, `M`=Minutos

### TGFFDA
**Formulas diferencial de Aliquota / Base de ICMS AT**

**PK:** `CODFORM`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFORM` 🔑 | Inteiro | Codigo da formula |  |
| `DESCRFORM` | Texto | Descrição da formula |  |
| `FORMULA` | Texto | Formula |  |

### TGFFDM
**Formulas para Calculo de Desconto Maximo**

**PK:** `CODFORM`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DESCRFORM` | Texto | Descrição da Formula |  |
| `CODFORM` 🔑 | Inteiro | Codigo |  |
| `FORMULA` | Texto | Formula |  |

### TGFFOP
**Finalidade de Operação**

**PK:** `NUFOP`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUFOP` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `SIGLA` | Texto | Sigla |  |

### TGFGAL
**(sem descrição)**

**PK:** `GALAO`, `LOTE`, `ANO`  
**Referenciada por:** 3 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFGCB
**Grupo Cobranca**

**PK:** `CODGRUPO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPO` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |

### TGFGEM
**Grupo Produtos e Icms por Empresa**

**PK:** `CODEMP`, `CODGRUPOPROD`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODGRUPOPROD` 🔑 | Inteiro | Grupo de produtos | → `TGFGRU`.`CODGRUPOPROD` |
| `GRUPOICMS` | Inteiro | Grupo de ICMS |  |
| `PERCCMTNAC` | Decimal | % Carga Media Trib. Nacional |  |
| `PERCCMTFED` | Decimal | % Carga Media Trib. Federal |  |
| `PERCCMTEST` | Decimal | % Carga Media Trib. Estadual |  |
| `PERCCMTMUN` | Decimal | % Carga Media Trib. Municipal |  |
| `PERCCMTIMP` | Decimal | % Carga Media Trib. Importação |  |
| `CODCTACTBEFD` | Inteiro | Conta Contabil para EFD | → `TCBPLA`.`CODCTACTB` |

### TGFGIAST
**Configurações da GIA-ST**

**PK:** `CODEMP`, `DTREF`, `UF`  
**Referenciada por:** 15 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `DTREF` 🔑 | Data | Referencia |  |
| `UF` 🔑 | Texto | UF |  |
| `TIPODECLARANTE` | Texto | Declarante |  |
| `CODSIG` | Inteiro | Signatario |  |
| `TIPOMOV` | Texto | Tipo Movimento |  |
| `DISTCOMBTRR` | Texto | Distribuidor de Combustiveis ou TRR com operação a UF Favorecida |  |
| `TIPODECLARACAOICMSST` | Texto | ICMS/ST e FCP e declarado junto |  |
| `HOUVEOPERCONSFINAL` | Texto | Houve operações que destinem bens ou servicos a consumidor final |  |
| `TRANSFFILIAL` | Texto | Houve transferencias para filial |  |

**Opções `DISTCOMBTRR`:** `S`=Sim, `N`=Não

**Opções `HOUVEOPERCONSFINAL`:** `S`=Sim, `N`=Não

**Opções `TIPODECLARACAOICMSST`:** `N`=Não, `S`=Sim

**Opções `TIPODECLARANTE`:** `S`=Signatario, `C`=Contador

**Opções `TIPOMOV`:** `S`=Substituição, `N`=Normal, `M`=Sem movimento

**Opções `TRANSFFILIAL`:** `S`=Sim, `N`=Não

### TGFGNT
**Grupo de Naturezas**

**PK:** `CODGRUPONAT`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPONAT` 🔑 | Inteiro | Grupo de natureza |  |
| `DESCRGRUPONAT` | Texto | Descrição |  |
| `CODGRUPONATPAI` | Inteiro | Grupo de natureza pai |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `GRAU` | Inteiro | GRAU |  |
| `TIPNAT` | Texto | Tipo de natureza |  |

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `TIPNAT`:** `R`=Receita, `D`=Despesa

### TGFGRD
**Tabela Grade Produto**

**PK:** `IDGRADE`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDGRADE` 🔑 | Inteiro | Nro. unico |  |
| `NOMGRD` | Texto | Nome Grade |  |
| `USAMASCARA` | Texto | Usar mascara no campo controle |  |
| `CODUSU` | Inteiro | Usuario |  |
| `DHCAD` | H | Dh. cadastro |  |
| `NUVERSAO` | Inteiro | Versão |  |
| `ATUNUVERSAO` | Texto | Atualizar versão |  |

**Opções `USAMASCARA`:** `S`=Sim, `N`=Não

### TGFGTT
**Grupos de Tipo de Titulos**

**PK:** `CODGRUPOTIPTIT`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOTIPTIT` 🔑 | Inteiro | Grupo de Tipo de Titulo |  |
| `DESCRGRUPOTIPTIT` | Texto | Descrição |  |
| `IMAGEM` | Blob | Imagem |  |

### TGFGVC
**CriterioPreAcordoVerba**

**PK:** `NUCRITERIO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCRITERIO` 🔑 | Inteiro | Nro Criterio |  |
| `NUPREACORDO` | Inteiro | Nro Pre-Acordo | → `TGFGVP`.`NUPREACORDO` |
| `TIPOCRITERIO` | Texto | Tipo de Criterio |  |
| `TIPOMETA` | Texto | Tipo de Meta |  |
| `DESCRICAO` | Texto | Descrição |  |

**Opções `TIPOCRITERIO`:** `G`=Gatilho, `C`=Complementar

**Opções `TIPOMETA`:** `V`=Valor, `Q`=Quantidade

### TGFHBC
**Historicos Lancamentos Bancarios**

**PK:** `CODLANC`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLANC` 🔑 | Inteiro | Codigo |  |
| `DESCRLANCBCO` | Texto | Descrição |  |
| `TIPLANC` | Inteiro | Tipo do Lancamento |  |
| `ACEITADEV` | Texto | Aceita Devolução Individual |  |

**Opções `ACEITADEV`:** `S`=Sim, `N`=Não

**Opções `TIPLANC`:** `1`=Credito, `-1`=Debito

### TGFHCO
**Historico de comissões**

**PK:** `CODHISTCOM`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODHISTCOM` 🔑 | Inteiro | Codigo |  |
| `DESCRHIST` | Texto | Descrição |  |

### TGFHFT
**Historico de Faturamento de Contratos**

**PK:** `NUAGENDAMENTO`, `TIPOAGE`, `SEQUENCIA`, `NUHISTORICO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAGENDAMENTO` 🔑 | Inteiro | NUAGENDAMENTO | → `TGFTAG`.`NUAGENDAMENTO` |
| `NUHISTORICO` 🔑 | Inteiro | Nro. Unico Agend. |  |
| `DHINIEXEC` | H | Dh. Ini. Execução |  |
| `DHFIMEXEC` | H | Dh. Fim Execução |  |
| `DHREFERENCIA` | H | Mes de Referencia |  |
| `QTDCONTRATOS` | Inteiro | Contratos Faturados |  |
| `QTDCOMIMPEDIMENTO` | Inteiro | Contratos com Impedimento |  |
| `QTDFATURASGERADAS` | Inteiro | Faturas Geradas |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFTAG`.`SEQUENCIA` |
| `TIPOAGE` 🔑 | Texto | TIPOAGE | → `TGFTAG`.`TIPOAGE` |
| `OBSERVACAO` | Texto | Observação |  |
| `CONFIG` | C | Configuração |  |

### TGFHIS
**TABLE TGFHIS**

**PK:** `NUAGENDAMENTO`, `TIPOAGE`, `SEQUENCIA`, `NUHISTORICO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAGENDAMENTO` 🔑 | Inteiro | NUAGENDAMENTO | → `TGFTAG`.`NUAGENDAMENTO` |
| `TIPOAGE` 🔑 | Texto | TIPOAGE | → `TGFTAG`.`TIPOAGE` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFTAG`.`SEQUENCIA` |
| `NUHISTORICO` 🔑 | Inteiro | Nro. Unico Agend. |  |
| `DHINIEXEC` | H | Dh. Ini. Execução |  |
| `DHFIMEXEC` | H | Dh. Fim Execução |  |
| `QTDCONTRATOS` | Inteiro | Qtd. Contratos |  |
| `QTDPRODUTOS` | Inteiro | Qtd. Produtos |  |
| `QTDREAJUSTADOS` | Inteiro | Qtd. Reajustados |  |
| `QTDNAOREAJUSTADOS` | Inteiro | Qtd. Não Reajustados |  |

### TGFHNP
**TABLE TGFHNP**

**PK:** `NUAGENDAMENTO`, `TIPOAGE`, `SEQUENCIA`, `NUHISTORICO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAGENDAMENTO` 🔑 | Inteiro | Nro. Unico Agend. | → `TGFTAG`.`NUAGENDAMENTO` |
| `TIPOAGE` 🔑 | Texto | TIPOAGE | → `TGFTAG`.`TIPOAGE` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFTAG`.`SEQUENCIA` |
| `NUHISTORICO` 🔑 | Inteiro | Nro. Unico Historico |  |
| `DHINIEXEC` | H | Dh. Ini. Execução |  |
| `DHFIMEXEC` | H | Dh. Fim Execução |  |
| `QTDPEDIDOS` | Inteiro | Qtd. Pedidos |  |
| `QTDPEDNAOPEND` | Inteiro | Qtd. Pedidos Não Pendentes |  |
| `QTDPEDPEND` | Inteiro | Qtd. Pedidos Pendentes |  |

### TGFHRF
**HistoricoRessuprimentoFiliais**

**PK:** `NUAGENDAMENTO`, `TIPOAGE`, `SEQUENCIA`, `NUHISTORICO`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAGENDAMENTO` 🔑 | Inteiro | Nro. Agendamento | → `TGFTAG`.`NUAGENDAMENTO` |
| `TIPOAGE` 🔑 | Texto | TIPOAGE | → `TGFTAG`.`TIPOAGE` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFTAG`.`SEQUENCIA` |
| `NUHISTORICO` 🔑 | Inteiro | Nro Execução |  |
| `DHINIEXEC` | H | Dh. Ini. Execução |  |
| `DHFIMEXEC` | H | Dh. Fim Execução |  |
| `QTDDOCSSAIDA` | Inteiro | Qtd. Docs. Saida |  |
| `QTDDOCSENTRADA` | Inteiro | Qtd. Docs. Entrada |  |
| `QTDPRODATEND` | Inteiro | Qtd. Produtos Atendidos |  |
| `ERRO` | Texto | Erro |  |
| `QTDPRODNAOATEND` | Inteiro | Qtd. Produtos Não Atendidos |  |

### TGFIDI
**Declaração de Importação**

**PK:** `NUNOTA`, `SEQUENCIA`, `SEQDI`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | NUNOTA | → `TGFIII`.`NUNOTA` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TGFIII`.`SEQUENCIA` |
| `SEQDI` 🔑 | Inteiro | Seq. DI |  |
| `NRODOCUMENTO` | Texto | Nro. Doc. Importação |  |
| `DTREGISTRO` | H | Dt. Registro |  |
| `LOCDESEMBARACO` | Texto | Local Desembaraco |  |
| `CODUFDESEMB` | Inteiro | UF Desembaraco | → `TSIUFS`.`CODUF` |
| `DTDESEMBARACO` | H | Dt. Desembaraco |  |
| `CODEXPORTADOR` | Texto | Codigo do Exportador |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | DHALTER |  |
| `DOCIMP` | Inteiro | Tipo |  |
| `VLRPISIMP` | Decimal | Vlr. PIS Importação |  |
| `VLRCOFINSIMP` | Decimal | Vlr. COFINS Importação |  |
| `NUMACDRAW` | Texto | Nro. Ato Conc. regime DrawBack |  |
| `DTPAGPIS` | H | Dt. Pagto. PIS |  |
| `DTPAGCOFINS` | H | Dt. Pagto. COFINS |  |
| `VIATRANSP` | Texto | Tipo de Transporte |  |
| `TIPPROCIMP` | Texto | Tipo Processo de Importação |  |
| `CNPJADQUIRENTE` | Texto | CNPJ/CPF do Adquirente |  |
| `UFADQUIRENTE` | Texto | UF do Adquirente |  |
| `VLRAFRMM` | Decimal | Vlr AFRMM |  |

**Opções `DOCIMP`:** `0`=Normal, `1`=Simplificada, `2`=Unica

**Opções `TIPPROCIMP`:** `O`=Conta e Ordem, `E`=Encomenda, `C`=Compra e Venda

**Opções `VIATRANSP`:** `01`=Maritima, `02`=Fluvial, `03`=Lacustre, `04`=Aerea, `05`=Postal, `06`=Ferroviaria, `07`=Rodoviaria, `08`=Conduto / Rede Transmissão, `09`=Meios Proprios, `10`=Entrada / Saida ficta, `11`=Courier, `12`=Handcarry

### TGFIGTV
**InformacoesGTV**

**PK:** `NUNOTA`, `NUMINFGTV`, `IDINFGTV`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico | → `TGFGTV`.`NUNOTA` |
| `NUMINFGTV` 🔑 | Texto | Numero da GTV |  |
| `IDINFGTV` 🔑 | Texto | Identificador da GTV |  |
| `SERINFGTV` | Texto | Serie da GTV |  |
| `SUBSERINFGTV` | Texto | Subserie da GTV |  |
| `DIGVERINFGTV` | Inteiro | Numero do Digito Verificador |  |
| `CARGAINFGTV` | Decimal | Quantidade de volumes/malotes |  |
| `CODVEICULO` | Inteiro | Codigo do Veiculo | → `TGFVEI`.`CODVEICULO` |

### TGFIGTVE
**Informações da GTV-e**

**PK:** `NUNOTA`, `IDGTVE`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico | → `TGFCAB`.`NUNOTA` |
| `IDGTVE` 🔑 | Inteiro | ID Informacoes GTV-e |  |
| `CHAVECTE` | Texto | Chave de acesso da GTV-e |  |

### TGFIMC
**Cadastro de Imposto**

**PK:** `CODIMP`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REGRA` | Texto | Tipo |  |
| `NOMEIMP` | Texto | Nome do Imposto |  |
| `F600EFD` | Texto | Gerar reg. F600 p/EFD Contribuições |  |
| `CODCTACTB1` | Inteiro | Conta Contabil 1 |  |
| `CODCTACTB2` | Inteiro | Conta Contabil 2 |  |
| `CODIMP` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição do Imposto |  |
| `USARPRECOCUSTO` | Texto | Usar Preco de Custo |  |
| `TIPOIMPOSTO` | Inteiro | Tipo Imposto |  |
| `CODTAB` | Inteiro | Tab.p/Pauta | → `TGFNTA`.`CODTAB` |
| `IMPBAIXAPARCIAL` | Texto | Destaque do Imposto |  |
| `GRUPOVLRMIN` | Texto | Grupo Vlr Minimo |  |
| `CONSIDERARIMP` | Texto | Considerar Impostos |  |
| `IMPFRETE` | Texto | Proporcionalizar imposto dos itens ao Frete |  |
| `BASEIMPFIN` | Texto | Base do Imposto no Financeiro |  |
| `CODREC` | Texto | Codigo Receita (Darf) |  |
| `REGCALCIMPRET` | Texto | Registrar calculo quando o imposto retido for inferior ao valor minimo |  |
| `VLRMAXINSS` | Decimal | Valor Maximo INSS |  |
| `ACUMBASEIPI` | Texto | Acumular na Base IPI |  |
| `CALCBASDIA` | Texto | Calcular com Base Diaria |  |
| `ATIVO` | Texto | Ativo |  |
| `CALCBASEMENSAL` | Texto | Calcular com Base Mensal |  |
| `ACUMBASEICMS` | Texto | Acumular na Base ICMS |  |
| `VLRMIN` | Decimal | Valor Minimo do Imposto |  |

**Opções `BASEIMPFIN`:** `null`=Valor do pagamento, `D`=Valor do documento

**Opções `CONSIDERARIMP`:** `F`=Financeiro, `N`=Nota, `A`=Ambos

**Opções `F600EFD`:** `E`=Entrada, `U`=Usar da TOP, `S`=Saida, `N`=Não Gerar

**Opções `IMPBAIXAPARCIAL`:** `B`=Destaca imposto na baixa, `D`=Destaca imposto na pendencia, `P`=Proporcionaliza o imposto na baixa

**Opções `IMPFRETE`:** `null`=Não, `S`=Sim

**Opções `REGCALCIMPRET`:** `N`=Não, `S`=Sim

### TGFIPC
**Itens Planejamento de Compra**

**PK:** `NUPCA`, `CODPROD`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPCA` 🔑 | Inteiro | Num. Planejamento | → `TGFPCA`.`NUPCA` |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `GIROMED` | Decimal | Giro Medio |  |
| `GIROMEDREC` | Decimal | Giro Medio Recente |  |
| `DESVIO` | Decimal | Desvio |  |
| `PEDEFETIVO` | Decimal | Pedido Efetivo |  |
| `LEADTIME` | Decimal | Lead Time |  |
| `LOTECOMPRAS` | Decimal | Lote Compras |  |
| `ESTSEG` | Decimal | Estoque Seguranca |  |
| `DEMANDA` | Decimal | Demanda |  |
| `ESTFISICO` | Decimal | Estoque Fisico |  |
| `PEDCOMPEN` | Decimal | Pedidos Compra Pendente |  |
| `PEDVENPEN` | Decimal | Pedidos Venda Pendente |  |
| `ESTPREVISTO` | Decimal | Estoque Previsto |  |
| `ESTFUTURO` | Decimal | Estoque Futuro |  |
| `ESTFUTUROAJU` | Decimal | Estoque Futuro Ajustado |  |
| `SUGCOMPRA` | Decimal | Sugestão Compra |  |
| `COMPRA` | Decimal | Pedido |  |
| `RUPCRITICA` | Inteiro | Ruptura Critica |  |
| `RUPACEITAVEL` | Inteiro | Ruptura Aceitavel |  |
| `COMPRAPREVISTA` | Decimal | Pedido Revisto |  |

### TGFISS
**Tabela de ISS**

**PK:** `CODCID`, `CODPROD`, `CODEMP`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDALIQ` | Inteiro | Codigo Aliquota |  |
| `CODCID` 🔑 | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `CODPROD` 🔑 | Inteiro | Servico |  |
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `PERCINSS` | Decimal | Percentual de ISS |  |
| `CODTRIBISS` | Inteiro | Cod. Tributação ISS |  |
| `PERCDEDUCAO` | Decimal | Perc. de dedução na base do ISS |  |
| `TIPODEDUCAO` | Texto | Tipo de dedução de base do ISS |  |
| `CODTRIBMUNISS` | Texto | Cod. Trib. Municipio |  |
| `CODLST` | Inteiro | Tipo de Servico | → `TGFLST`.`CODLST` |
| `NAOCALCULA` | Texto | Não Calcula |  |

**Opções `CODTRIBISS`:** `0`=00 - Tributado, `6`=06 - Isento, `7`=07 - Não Tributado, `1`=01 - Tributado com ISS Retido

**Opções `NAOCALCULA`:** `S`=Sim, `N`=Não

**Opções `TIPODEDUCAO`:** `M`=Materiais, `P`=Por percentual, `S`=Sub-Empreito

### TGFITC
**Itens da Cotação**

**PK:** `NUMCOTACAO`, `CODPROD`, `CODPARC`, `CONTROLE`, `CODLOCAL`, `CABECALHO`, `DIFERENCIADOR`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `NUNOTACPA` | Inteiro | Nro. do Item na Nota do Pedido |  |
| `SEQNOTACPA` | Inteiro | Sequencia da nota de compra |  |
| `COMPLDESC` | Texto | Complemento |  |
| `CODPARC` 🔑 | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CODVOL` | Texto | Volume | → `TGFVOL`.`CODVOL` |
| `DTCOLETAPRECO` | H | Data Coleta |  |
| `TIPOCOLPRECO` | Texto | Coleta de preco |  |
| `QTDCOTADA` | Decimal | Quantidade |  |
| `PRAZOVALPROP` | Inteiro | Prazo Validade |  |
| `PRECOMOE` | Decimal | Preco em moeda |  |
| `PRECO` | Decimal | Preco |  |
| `CODMOEDA` | Inteiro | Moeda |  |
| `VLRMOEDA` | Inteiro | Valor Moeda |  |
| `CONDPAGT` | Texto | Condição de pagamento |  |
| `PRAZOPARC` | Inteiro | Intervalo pagamento |  |
| `QTDPARCPAGT` | Inteiro | Parcelas |  |
| `PERCACRESC` | Decimal | % Acrescimo |  |
| `VLRACRESC` | Decimal | Valor do Acrescimo |  |
| `TOTALPRODUTO` | Decimal | Total |  |
| `VLRDESCMOE` | Decimal | Vlr. Desc. Moeda |  |
| `VLRDESC` | Decimal | Valor do Desconto |  |
| `PERCDESC` | Decimal | % Desconto |  |
| `DTLIMPRECO` | Data | Data limite preco |  |
| `IPI` | Decimal | IPI unitario |  |
| `ICMS` | Decimal | ICMS Unitario |  |
| `FRETE` | Decimal | Frete Unitario |  |
| `OUTROS` | Decimal | Outros |  |
| `TAXAJURO` | Decimal | Taxa Juro |  |
| `PRAZOMEDIO` | Inteiro | Prazo Medio |  |
| `PRAZOENTREGA` | Inteiro | Prazo Entrega |  |
| `QUALPROD` | Inteiro | Qual. Produto |  |
| `MODFRETE` | Texto | Modalidade de frete |  |
| `CONFIABFORN` | Inteiro | Conf. Fornecedor |  |
| `GARANTIA` | Inteiro | Garantia |  |
| `FATMINIMO` | Decimal | Fat. Minimo |  |
| `SITUACAO` | Texto | Situação |  |
| `MELHOR` | Texto | Melhor Cotação |  |
| `RESULTCOT` | Decimal | Resultado |  |
| `CODTIPVENDA` | Inteiro | Tipo Negociação |  |
| *... +53 campos adicionais* | | | |

**Opções `CABECALHO`:** `S`=Sim, `N`=Não

**Opções `CONDPAGT`:** `Z`=A Prazo, `P`=Parcelada, `V`=A Vista

**Opções `MELHOR`:** `N`=Não, `I`=Empate, `S`=Sim

**Opções `MODFRETE`:** `C`=Por conta do emitente (CIF), `T`=Por conta de terceiros, `S`=Sem frete, `R`=Transp. proprio pelo remetente, `D`=Transp. proprio pelo destinatario, `F`=Por conta do destinatario (FOB)

**Opções `SITUACAO`:** `E`=Enviada, `G`=Negociar, `N`=Reprovada, `P`=Pendente, `R`=Respondida, `F`=Faturada, `C`=Recusada, `A`=Aprovada

**Opções `STATUSPRODCOT`:** `O`=Aberta, `A`=Aprovada, `C`=Cancelada, `E`=Enviada, `F`=Fechada, `P`=Precificada

### TGFLCR
**LocalRetirada**

**PK:** `CODEMP`, `CODPARCRETIRADA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Codigo | → `TSIEMP`.`CODEMP` |
| `CODPARCRETIRADA` 🔑 | Inteiro | Cod. Parceiro Retirada | → `TGFPAR`.`CODPARC` |
| `ATIVO` | Texto | Ativo |  |

**Opções `ATIVO`:** `N`=Nao, `S`=Sim

### TGFLIV
**Movimento Livros Fiscais**

**PK:** `NUNOTA`, `ORIGEM`, `SEQUENCIA`, `CODEMP`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro unico Nota |  |
| `ORIGEM` 🔑 | Texto | Origem |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `NUMNOTA` | Inteiro | Nro. da nota |  |
| `NUMNOTA2` | Inteiro | Nro. da nota 2 |  |
| `SERIENOTA` | Texto | Serie da nota |  |
| `DTDOC` | Data | Dt. do documento |  |
| `DHMOV` | Data | Dt. do movimento |  |
| `EMPPARC` | Texto | Destino |  |
| `CODPARC` | Inteiro | Empresa/Parceiro |  |
| `CODCFO` | Inteiro | CFOP |  |
| `NUMLANC` | Inteiro | Nro. do lancamento |  |
| `ESPDOC` | Texto | Especie do documento |  |
| `CODTRIB` | Inteiro | Cod. de tributação |  |
| `TIPICMS` | Texto | Tipo de ICMS |  |
| `BASEICMS` | Decimal | Base do ICMS |  |
| `ALIQICMS` | Decimal | Aliquota ICMS |  |
| `VLRICMS` | Decimal | Vlr. do ICMS |  |
| `ISENTASICMS` | Decimal | Isentas de ICMS |  |
| `OUTRASICMS` | Decimal | Outras ICMS |  |
| `BASERETENCAO` | Decimal | Base retenção |  |
| `ICMSRETENCAO` | Decimal | ICMS retenção |  |
| `TIPIPI` | Texto | Tipo de IPI |  |
| `BASEIPI` | Decimal | Base do IPI |  |
| `ALIQIPI` | Decimal | Aliquota de IPI |  |
| `VLRIPI` | Decimal | Vlr. do IPI |  |
| `ISENTASIPI` | Decimal | Isentas de IPI |  |
| `OUTRASIPI` | Decimal | Outras IPI |  |
| `VLRCTB` | Decimal | Vlr. contabil |  |
| `CODCTACTB` | Inteiro | Conta contabil |  |
| `OBSERVACAO` | Texto | Observação |  |
| `DIGITADO` | Texto | Digitado |  |
| `ENTSAI` | Texto | Entrada/Saida |  |
| `DIFICMS` | Decimal | Diferenca ICMS |  |
| `UFORIGEM` | Texto | UF de Origem |  |
| `UFDESTINO` | Texto | UF de Destino |  |
| `GTOTECF` | Decimal | Grande total |  |
| `DTFILT` | H | Dt. p/ filtro do tipo de movimento |  |
| `CODEMPORIG` | Inteiro | Empresa de Origem |  |
| *... +28 campos adicionais* | | | |

**Opções `CODANTECIPST`:** `2`=2-Antecip. tribut. efetuada pelo destinatario apenas como complemento do diferencial de aliquota, `4`=4-Antecip. tribut. com MVA efetuada pelo destinatario encerrando a fase de tributação, `5`=5-Substituição tributaria interna motivada por regime especial de tributação, `6`=6-ICMS pago na importação, `A`=A-ST informada pelo substituto/substituido que não incorra em nenhuma das situações anteriores, `3`=3-Antecip. tribut. com MVA efetuada pelo destinatario sem encerrar a fase de tributação, `1`=1-Pgto de ST efetuado pelo destinatario quando não efetuado ou efetuado a menor pelo substituto, `N`=N-(Não Usa) Operação não envolve ST

**Opções `CODTRIB`:** `0`=00-Tributada integralmente, `02`=02-Tributação monofasica propria sobre combustiveis, `10`=10-Tributada e c/cobranca por substituição, `15`=15-Tributação monofasica propria e com responsabilidade pela retenção sobre combustiveis, `20`=20-Com redução de base de calculo, `30`=30-Isenta e não tribut. e c/cobranca por subst., `40`=40-Isenta, `41`=41-Não tributada, `50`=50-Suspensão, `51`=51-Diferimento, `53`=53-Tributação monofasica sobre combustiveis com recolhimento diferido, `60`=60-ICMS cobrado anteriormente por substituição

**Opções `DIGITADO`:** `S`=Sim, `N`=Não

**Opções `EMPPARC`:** `P`=Parceiro, `E`=Empresa

**Opções `ENTSAI`:** `E`=Entrada, `S`=Saida

**Opções `ORIGEM`:** `A`=Complemento, `E`=Estoque, `F`=Financeiro, `C`=Cancelada, `Z`=Redução Z, `D`=Devolução

### TGFLNF
**LoteNotaFiscalEletronica**

**PK:** `NULOTE`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NULOTE` 🔑 | Inteiro | Nro. Lote |  |
| `NUMRECEB` | Texto | Nro.Receb.Lote NF-e |  |
| `DHRECEB` | H | Dt.Receb.Lote NF-e |  |
| `OBSERVACAO` | Texto | Observação |  |
| `GUID` | Texto | Guid |  |
| `NUMLOTEPROVEDOR` | Inteiro | NUMLOTEPROVEDOR |  |

### TGFLREA
**Aliquota REA/DF**

**PK:** `NUNOTA`, `ORIGEM`, `SEQUENCIA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. unico da nota | → `TGFLREA`.`NUNOTA` |
| `ORIGEM` 🔑 | Texto | Origem | → `TGFLREA`.`ORIGEM` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia | → `TGFLREA`.`SEQUENCIA` |
| `NUMITEMREA` | Inteiro | Nro. Item REA |  |
| `CODCFO` | Inteiro | CFO | → `TGFCFO`.`CODCFO` |
| `BASE` | Decimal | Base |  |
| `ALIQUOTA` | Decimal | Aliquota |  |
| `VALOR` | Decimal | Valor |  |
| `ATUALREA` | Inteiro | Atualiza REA |  |

### TGFLST
**Lista de Servicos**

**PK:** `CODLST`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLST` 🔑 | Inteiro | Codigo |  |
| `DESDNAC` | Texto | Desdobro Nacional |  |
| `DESCRLST` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `CODLSTPAI` | Inteiro | Codigo Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `INFORMACODOBRA` | Texto | Exige Cod. da Obra |  |
| `TIPOREPASSE` | Inteiro | Tipo de repasse |  |
| `GERAVLRTOTREC` | Texto | A tag "Valor Total Recebido" e obrigatoria para NFSe SP |  |

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `GERAVLRTOTREC`:** `N`=Não, `S`=Sim

**Opções `INFORMACODOBRA`:** `S`=Sim, `N`=Não

**Opções `TIPOREPASSE`:** `1`=1 - Patrocinio, `2`=2 - Licenciamento de marcas e simbolos, `3`=3 - Publicidade, `4`=4 - Propaganda, `5`=5 - Transmissão de espetaculos

### TGFMAQ
**Cadastro de Maquinas**

**PK:** `CODMAQ`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEQUIP` | Inteiro | Cod. Maquina | → `TGFEQF`.`CODEQUIP` |
| `CODMAQ` 🔑 | Inteiro | Cod. Maquina |  |
| `ATIVO` | Texto | Ativo |  |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `MARCA` | Texto | Marca |  |
| `MODELO` | Texto | Modelo Equipamento |  |
| `TIPOECF` | Texto | Tipo Equipamento ECF |  |
| `CODNACIONALIDENT` | Texto | Codigo CNIEE |  |
| `NROSERIE` | Texto | Numero de Serie |  |
| `MODDOC` | Texto | Modelo do Documento |  |
| `TIPDOC` | Texto | Tipo do Documento |  |
| `FUSOHORARIO` | Inteiro | Fuso Horario |  |
| `NROCAIXA` | Inteiro | Numero do ECF |  |
| `NUMUSUECF` | Inteiro | Numero Usuario |  |
| `INDLIVRO` | Texto | Considera apuração |  |
| `MD5PAF` | Texto | MD5 Paf |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `INDLIVRO`:** `N`=Não, `S`=Sim

**Opções `MARCA`:** `DARUMA`=DARUMA, `BEMATECH`=BEMATECH, `DATAREGIS`=DATAREGIS, `URANO`=URANO, `INTERWAY`=INTERWAY, `ELGIN`=ELGIN, `SWEDA`=SWEDA

**Opções `MODDOC`:** `2B`=2B, `2D`=2D, `2C`=2C

**Opções `TIPDOC`:** `PDV`=PDV, `ECF`=ECF

### TGFMBC
**Movimento Bancario**

**PK:** `NUBCO`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCTABCOCONTRA` | Inteiro | Cod. conta bancaria |  |
| `NUCAIXA` | Inteiro | Num. Caixa | → `TGFCAI`.`NUCAIXA` |
| `SALDO` | Decimal | Saldo |  |
| `CODPDV` | Inteiro | Cod. PDV |  |
| `NUBCOCP` | Inteiro | Num. Banco |  |
| `ORIGMOV` | Texto | Tipo de Movimento |  |
| `NUMTRANSF` | Inteiro | Numero |  |
| `DTLANC` | Data | Dt. Lancamento |  |
| `CODTIPOPER` | Inteiro | Cod.Tipo Operação | → `TGFTOP`.`CODTIPOPER` |
| `NUMDOC` | Inteiro | Num. Documento |  |
| `VLRLANC` | Decimal | Vlr. Lancamento |  |
| `HISTORICO` | Texto | Historico |  |
| `CODCTABCOINT` | Inteiro | Conta Origem | → `TSICTA`.`CODCTABCOINT` |
| `CODLANC` | Inteiro | Lanc. Origem | → `TGFHBC`.`CODLANC` |
| `CODCTABCOINTDEST` | Inteiro | Conta Destino |  |
| `CODLANCDEST` | Inteiro | Lanc. Destino |  |
| `CONCILIADO` | Texto | Conciliado |  |
| `CONCILIADODEST` | Texto | Conciliado Destino |  |
| `VLRMOEDA` | Decimal | Vlr. Moeda |  |
| `VLRLANC_DESTINO` | Decimal | Vlr. Lanc. Destino |  |
| `RECDESP` | Inteiro | Receita/Despesa |  |
| `NUBCO` 🔑 | Inteiro | Num. Unico Bancario |  |
| `DTINCLUSAO` | H | Dt. Inclusão |  |
| `DHTIPOPER` | H | Dh. Operação | → `TGFTOP`.`DHALTER` |
| `DTCONTAB` | H | Dt. Contabilização |  |
| `PREDATA` | H | Pre-Data |  |
| `DHCONCILIACAO` | H | Dh. Conciliação |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `CONTABILIZADO` | Texto | Contabilizado |  |
| `TALAO` | Inteiro | Talão |  |
| `DTALTER` | H | Dt. Alteração |  |
| `VLRTROCO` | Decimal | Vlr. Troco |  |
| `VLRCHEQUE` | Decimal | Vlr. Cheque |  |
| `NROIMPORT` | Inteiro | Nro da importação |  |

**Opções `CONCILIADO`:** `S`=Sim, `N`=Não

**Opções `CONCILIADODEST`:** `S`=Sim, `N`=Não

**Opções `CONTABILIZADO`:** `S`=Sim, `N`=Não

**Opções `ORIGMOV`:** `S`=Saque, `R`=Resgate, `T`=Transferencia, `F`=Financeiro, `A`=Aplicação, `D`=Deposito

**Opções `RECDESP`:** `1`=Receita, `-1`=Despesa

### TGFMDFE
**MDF-e**

**PK:** `NUVIAG`, `SEQMDFE`  
**Referenciada por:** 26 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUVIAG` 🔑 | Inteiro | Nro. Viagem | → `TGFVIAG`.`NUVIAG` |
| `SEQMDFE` 🔑 | Inteiro | Sequencia do manifesto |  |
| `NUMMDFE` | Inteiro | Nro. MDF-e |  |
| `STATUSMDFE` | Texto | Status MDF-e |  |
| `NUMALEATORIO` | Inteiro | Nro. Aleatorio |  |
| `CHAVEMDFE` | Texto | Chave MDF-e |  |
| `NRORECIBO` | Texto | Nro. Recibo |  |
| `DHRECIBO` | H | Dt. e Hora do Recbto. |  |
| `DHEMISS` | H | Dt. e Hora da emissão |  |
| `TIPEMISS` | Texto | Tipo de emissão |  |
| `UFINICIAL` | Inteiro | UF de Coleta | → `TSIUFS`.`CODUF` |
| `MUNINICIAL` | Inteiro | Municipio de Coleta |  |
| `UFFINAL` | Inteiro | UF de Descarregamento | → `TSIUFS`.`CODUF` |
| `MUNFINAL` | Inteiro | Municipio de Descarregamento |  |
| `DHALTER` | H | Data de Alteração |  |
| `XML` | C | XML |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `NULOTEMDFE` | Inteiro | Nro. Lote |  |
| `XMLPROTAUT` | C | XMLPROTAUT |  |
| `XMLENVCLI` | C | XMLENVCLI |  |
| `UNMED` | Texto | Unidade de Medida |  |
| `PESOBRUTOTOT` | Decimal | Peso Bruto Total |  |
| `USAPESOBRUTONFE` | Texto | Considerar Peso Bruto Total para NF-e |  |
| `CODCIDENCERRAMENTO` | Inteiro | Cod. Cidade Encerramento |  |
| `CODPORTOEMBARQUE` | Texto | Cod. Porto Embarque |  |
| `CODPORTODESTINO` | Texto | Cod. Porto Destino |  |
| `QRCODE` | Texto | QRCODE |  |
| `CODPORTOTRANSBORDO` | Texto | Cod. Porto Transbordo |  |
| `TIPONAVEGACAO` | Inteiro | Tipo Navegação |  |
| `IRINNAVIO` | Texto | N IRIN |  |
| `TPCARGA` | Texto | Tipo de Carga |  |
| `DESCPROD` | Texto | Descrição do Produto |  |
| `EAN` | Texto | EAN |  |
| `NCM` | Texto | NCM |  |
| `CEPCAR` | Texto | CEP |  |
| `LATCAR` | Decimal | Latitude |  |
| `LONGCAR` | Decimal | Longitude |  |
| `CEPDESCAR` | Texto | CEP |  |
| `LATDESCAR` | Decimal | Latitude |  |
| `LONDESGCAR` | Decimal | Longitude |  |
| *... +2 campos adicionais* | | | |

**Opções `INDCARREGPOST`:** `S`=Sim, `N`=Nao

**Opções `STATUSMDFE`:** `3`=Autorizado, `4`=Aguardando correção, `7`=Denegado, `9`=Enviado em contingencia, `8`=Com erro de validação, `6`=Encerrado, `0`=Não transmitido, `5`=Cancelado, `2`=Aguardando autorização, `1`=Enviado

**Opções `TIPEMISS`:** `2`=Contingencia, `1`=Normal

**Opções `TIPONAVEGACAO`:** `0`=Interior, `1`=Cabotagem

**Opções `TPCARGA`:** `05`=Carga Geral, `04`=Conteinerizada, `10`=Perigosa (conteineirazada), `11`=Perigosa (carga geral), `08`=Perigosa (granel liquido), `09`=Perigosa (carga frigorificada), `07`=Perigosa (granel solido), `02`=Granel liquido, `06`=Neogranel, `12`=Granel Pressurizada, `03`=Frigorificada, `01`=Granel solido

**Opções `UNMED`:** `02`=TON, `01`=KG

### TGFMDFESEG
**Seguro MDF-e**

**PK:** `NUVIAG`, `SEQMDFE`, `NUMAPOLICE`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUVIAG` 🔑 | Inteiro | Nro. Viagem | → `TGFMDFE`.`NUVIAG` |
| `SEQMDFE` 🔑 | Inteiro | Sequencia do manifesto | → `TGFMDFE`.`SEQMDFE` |
| `NUMAPOLICE` 🔑 | Texto | Nro. Apolice |  |
| `CODPARCSEG` | Inteiro | Seguradora | → `TGFPAR`.`CODPARC` |
| `CODPARCRESPSEG` | Inteiro | Responsavel do seguro | → `TGFPAR`.`CODPARC` |

### TGFMEQ
**Tabela de Maquinas e Equipamentos**

**PK:** `NUMEQ`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMEQ` 🔑 | Inteiro | Nro. do Equipamento |  |
| `DESCRMEQ` | Texto | Desc. da Maquina/Equipamento |  |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODVEICULO` | Inteiro | Cod. Veiculo |  |
| `TERCEIRO` | Texto | Indica de o Equipmento pertence a um Terceiro |  |
| `CODPARC` | Inteiro | Cod. Parceiro Relacionando a Maq/Eqpto. | → `TGFPAR`.`CODPARC` |
| `CODUSU` | Inteiro | Cod. Usuario que Realizou a Operação | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | Dat. de Inclusão/Alteração do Registro |  |
| `CODBEM` | Texto | Cod. do Bem | → `TCIBEM`.`CODBEM` |
| `CODPROD` | Inteiro | Cod. Produto | → `TGFPRO`.`CODPROD` |
| `OBSERVACAO` | Texto | Obs. sobre Maquinas e Equipamentos |  |

### TGFMMS
**GF Movimento Mensal Sintetico**

**PK:** `DTAM`, `CODPARC`, `CODGRUPOPROD`, `GRUPO`, `CODEMP`, `TIPMOV`, `MES`, `ANO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTAM` 🔑 | H | Data ano e mes |  |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODGRUPOPROD` 🔑 | Inteiro | Grupo Produtos | → `TGFGRU`.`CODGRUPOPROD` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `TIPMOV` 🔑 | Texto | Tipo de Movimento |  |
| `MES` 🔑 | Inteiro | Mes |  |
| `ANO` 🔑 | Inteiro | Ano |  |
| `VLRMOV` | Decimal | Valor do movimento |  |
| `GRUPO` 🔑 | Texto | Grupo |  |

### TGFMON
**GF Modelo para notas fiscais**

**PK:** `CODMODNF`  
**Referenciada por:** 12 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CAMINHO` | Texto | Caminho |  |
| `CODMODNF` 🔑 | Inteiro | Modelo |  |
| `CAMINHOSW` | Texto | Caminho Rep. Arquivos |  |
| `NOME` | Texto | Nome |  |
| `TIPOIMPRESSORA` | Texto | Tipo de impressora |  |
| `NURFE` | Inteiro | Numero do relatorio modelo | → `TSIRFE`.`NURFE` |

**Opções `TIPOIMPRESSORA`:** `6`=DESKJET, `2`=EPSON, `4`=ELGIN, `3`=RIMA/ITAUTEC, `5`=OUTRAS, `7`=XEROX LASER, `1`=ELEBRA/RIMA

### TGFMOP
**Movimento de Ocorrencias de Parceiros**

**PK:** `NUMOV`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMOV` 🔑 | Inteiro | Nro. Movimento |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `TIPO` | Texto | Tipo |  |
| `CPF_CNPJ` | Texto | CPF / CNPJ |  |
| `DHMOV` | H | Dh. Movimento |  |
| `DIGITADO` | Texto | Digitado |  |
| `CODOCC` | Inteiro | Ocorrencia | → `TGFOCC`.`CODOCC` |
| `EVENTOEXEC` | Texto | Executado |  |

**Opções `DIGITADO`:** `S`=Sim, `N`=Não

**Opções `EVENTOEXEC`:** `S`=Sim, `N`=Não

**Opções `TIPO`:** `P`=Parceiro, `S`=Socio

### TGFMTC
**TABLE TGFMTC**

**PK:** `CODIGO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Codigo |  |
| `MOTIVO` | Texto | Motivo de Cancelamento |  |

### TGFNFE
**Arquivos XML de NFe**

**PK:** `NUNOTA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `XMLPROTCANC` | C | XMLPROTCANC |  |
| `XMLPROTAUTCARTA` | C | Xml de Autorização de Carta de Correção |  |
| `XMLENVCLICARTA` | C | Xml de Distribuição da Carta de Correção |  |
| `XMLENVCLICANC` | C | XMLENVCLICANC |  |
| `NUNOTA` 🔑 | Inteiro | NUNOTA |  |
| `XMLCANC` | C | XMLCANC |  |
| `XMLENVCARTA` | C | Xml Envio Carta de Correção |  |
| `CHAVENFE` | Texto | CHAVENFE |  |
| `XML` | C | XML |  |
| `XMLPROTAUTNOT` | C | XMLPROTAUTNOT |  |
| `XMLENVCLI` | C | XMLENVCLI |  |
| `QRCODE` | Texto | QRCODE |  |
| `XMLENVEPEC` | C | XMLENVEPEC |  |
| `XMLPROTAUTEPEC` | C | XMLPROTAUTEPEC |  |
| `XMLENVPRORROG` | C | Xml de envio do Evento de Prorrogação de Prazo de Suspensão do Icms |  |
| `XMLENVCANCPRORROG` | C | Xml de envio do Cancelamento do Evento de Prorrogação de Prazo de Suspensão do Icms |  |
| `XMLPROTAUTPRORROG` | C | Xml de Autorização do Evento de Prorrogação de Prazo de Suspensão do Icms |  |
| `XMLENVCLICANCPRORROG` | C | XMLENVCLICANCPRORROG |  |
| `XMLPROTAUTCANCPRORROG` | C | Xml de Autorização do Cancelamento do Evento de Prorrogação de Prazo de Suspensão do Icms |  |
| `XMLENVCLIPRORROG` | C | XMLENVCLIPRORROG |  |

### TGFNMDFE
**Notas MDF-e**

**PK:** `NUVIAG`, `SEQMDFE`, `NUNOTA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro. Unico da Nota | → `TGFCAB`.`NUNOTA` |
| `ORDEMCARGA` | Inteiro | Ordem de Carga |  |
| `NUVIAG` 🔑 | Inteiro | Nro. Viagem | → `TGFMDFE`.`NUVIAG` |
| `CODEMP` | Inteiro | Cod. Empresa |  |
| `RAZAOSOCIAL` | Texto | Descrição da empresa |  |
| `CODPARC` | Inteiro | Cod. Parceiro |  |
| `RAZAOSOCIALPARC` | Texto | Descrição do parceiro |  |
| `VLRNOTA` | Decimal | Valor da nota |  |
| `NUMNOTA` | Inteiro | Nro. Nota |  |
| `PESOBRUTO` | Decimal | Peso Bruto |  |
| `SEQMDFE` 🔑 | Inteiro | Sequencia do manifesto | → `TGFMDFE`.`SEQMDFE` |
| `INDREENTREGA` | Texto | Id. Reentrega |  |
| `STATUSENVIO` | Texto | Status de Envio |  |

**Opções `INDREENTREGA`:** `S`=Sim, `N`=Não

**Opções `STATUSENVIO`:** `null`=Normal, `P`=Por evento, `D`=Não enviado

### TGFOBS
**Observações para Notas**

**PK:** `CODOBSPADRAO`  
**Referenciada por:** 8 tabelas  

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

### TGFPAEM
**Grupo ICMS/ISS por Empresa**

**PK:** `CODEMP`, `CODPARC`  

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

### TGFPAP
**Interação Parceiro Produto**

**PK:** `CODPARC`, `CODPROD`, `SEQUENCIA`  
**Referenciada por:** 3 tabelas  

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

### TGFPDV
**TGFPDV**

**PK:** `CODPDV`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPDV` 🔑 | Inteiro | Codigo do PDV |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `ATIVO` | Texto | Ativo |  |
| `PDVTERCEIRO` | Texto | PDV Terceiro |  |
| `CODCONTAPDV` | Inteiro | Conta PDV | → `TSICTA`.`CODCTABCOINT` |
| `CODCONTATES` | Inteiro | Conta Tesouraria | → `TSICTA`.`CODCTABCOINT` |
| `IDMAQUINALOCAL` | Texto | Identificação PDV |  |
| `DTINCID` | H | Data da inclusão do ID. da alteração |  |
| `DTALTER` | H | Data e Hora de inclusão/alteração |  |
| `CODUSUALTER` | Inteiro | Usuario de inclusão/alteração | → `TSIUSU`.`CODUSU` |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `PDVTERCEIRO`:** `N`=Não, `S`=Sim

### TGFPLAC
**Cabecalho do Planejamento de Entrega**

**PK:** `NUPLAN`, `CODPARCFAT`, `CODCONTATO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPLAN` 🔑 | Inteiro | Nro. Planejamento | → `TGFPLAN`.`NUPLAN` |
| `DISTRIBUICAOCONTATO` | Inteiro | Verifica se Houve Distribuição para o Contato |  |
| `CODPARCFAT` 🔑 | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CODCONTATO` 🔑 | Inteiro | Contato | → `TGFCTT`.`CODCONTATO` |
| `GRUPO` | Inteiro | Grupo |  |
| `NUNOTA` | Inteiro | N.Unico Nota | → `TGFCAB`.`NUNOTA` |
| `CODREG` | Inteiro | Região |  |
| `CODCID` | Inteiro | Cidade |  |
| `CODBAI` | Inteiro | Bairro |  |
| `CODEND` | Inteiro | Endereco |  |
| `NUMEND` | Inteiro | Nro. Endereco |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DTALTER` | H | Data de Alteração |  |

### TGFPLC
**(sem descrição)**

**PK:** `NUCESTA`  
**Referenciada por:** 2 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFPMT
**Produtos com Mudanca de Tributação**

**PK:** `CODEMP`, `DTMTP`, `CODPROD`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFMTP`.`CODEMP` |
| `DTMTP` 🔑 | H | Dt. Mud. Tributação | → `TGFMTP`.`DTMTP` |
| `CODPROD` 🔑 | Inteiro | Produto |  |
| `CODGRUPOPROD` | Inteiro | Grupo |  |
| `NCM` | Texto | NCM |  |
| `CODVOL` | Texto | Unidade padrão |  |
| `USOPROD` | Texto | Usado como |  |
| `QTDEST` | Decimal | Estoque |  |
| `VLRUNITCUSTO` | Decimal | Vlr. Custo |  |
| `DIGITADO` | Texto | Digitado |  |
| `IDALIQ` | Inteiro | Cod. Aliq. ICMS |  |
| `CST` | Inteiro | Tributação |  |
| `BASEICMS` | Decimal | Base ICMS |  |
| `ALIQICMS` | Decimal | Aliquota ICMS |  |
| `VLRICMS` | Decimal | Vlr. ICMS |  |
| `MVA` | Decimal | MVA |  |
| `BASEICMSST` | Decimal | Base Substituição |  |
| `IDALIQANTERIOR` | Inteiro | Cod. Aliq. ICMS Anterior |  |
| `ALIQST` | Decimal | Aliquota ST |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `VLRICMSST` | Decimal | Vlr. Substituição |  |
| `CSTANTERIOR` | Inteiro | Tributação Anterior |  |
| `DTALTER` | H | Dt. Alteração |  |
| `BASESTESTOQUE` | Decimal | Base de ST Total |  |
| `VLRSTTOTEST` | Decimal | Vlr. ST Total |  |
| `BASESUBSTITCOMPRA` | Decimal | Base ST Unit. |  |
| `VLRICMSSTREC` | Decimal | Vlr. ST Unit. |  |
| `BASEICMSREC` | Decimal | Base ICMS Total |  |
| `VLRICMSREC` | Decimal | Vlr. ICMS Total |  |
| `BASEICMSUNIT` | Decimal | Base ICMS Unit. |  |
| `VLRICMSCOMPRA` | Decimal | Vlr. ICMS. Unit. |  |
| `NUNOTACOMPRA` | Inteiro | Nro. Unico compra |  |
| `CODPARCCOMPRA` | Inteiro | Parceiro da Compra |  |
| `BASESUBSTIT` | Decimal | Base Substituição (Nota/Media) |  |
| `VLRICMSUNIT` | Decimal | Vlr. ICMS Unit. (Calculado) |  |
| `VLRCUSUTIL` | Texto | Valor de custo utilizado |  |

**Opções `DIGITADO`:** `N`=Não, `S`=Sim

**Opções `USOPROD`:** `O`=Outros insumos, `2`=Prod.Intermediario, `V`=Venda (fabricação propria), `T`=Terceiros, `R`=Revenda, `P`=Em Processo, `1`=Subproduto, `M`=Materia prima, `I`=Imobilizado, `F`=Brinde (NF), `E`=Embalagem, `D`=Revenda (por formula)

**Opções `VLRCUSUTIL`:** `N`=Não, `S`=Sim

### TGFPPL
**Planejamento de produção**

**PK:** `NUPLAN`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTAORIG` | Inteiro | Nota Origem |  |
| `QTDPRODUZIDO` | Decimal | Produzido |  |
| `QTDEMPROD` | Decimal | Em produção |  |
| `PEDIDOORIGEM` | Inteiro | Pedido |  |
| `SEQUENCIAORIG` | Inteiro | Item Origem |  |
| `NUPLAN` 🔑 | Inteiro | Nro Plan. |  |
| `DTMOV` | Data | Dt Movimento |  |
| `QTD` | Decimal | Quantidade |  |
| `QTDGERADA` | Decimal | Qtd. ja Gerada |  |
| `DTPLA` | Data | Dt Plan. |  |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CONTROLE` | Texto | Controle |  |
| `LIBPRODUCAO` | Texto | Lib. Produção |  |
| `LIBLOGISTICA` | Texto | Lib. logistica |  |
| `VARIACAO` | Inteiro | Variação |  |
| `ORDEM` | Inteiro | Ordem |  |
| `CODLOCAL` | Inteiro | Local |  |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `CODPARCTRANSP` | Inteiro | Cod. Parceiro Transportadora | → `TGFPAR`.`CODPARC` |
| `OBS` | Texto | Observação |  |
| `PROBLEMA` | Texto | Problema |  |
| `NUNOTA` | Inteiro | Nota Gerada na Produção | → `TGFCAB`.`NUNOTA` |
| `DTREF` | Data | Dt Refencia |  |
| `SALDOPEDIDO` | Decimal | Saldo Pedido |  |
| `NUPLANORIG` | Inteiro | Plan. Origem |  |
| `PLANDEMAND` | Texto | Plan. por demanda |  |
| `VARIACAOMAPA` | Inteiro | Variação |  |
| `SEQPREV` | Inteiro | Seq. Previsão |  |
| `CODUSULIBLOG` | Inteiro | Cod. Usuario Liberador (Logistica) | → `TSIUSU`.`CODUSU` |
| `CODUSULIBPROD` | Inteiro | Cod. Usuario Liberador (Produção) | → `TSIUSU`.`CODUSU` |
| `DHLIBLOG` | H | Dt/Hora Lib (Logistica) |  |
| `DHLIBPROD` | H | Dt/Hora Lib. (Produção) |  |

**Opções `LIBLOGISTICA`:** `N`=Não, `S`=Sim

**Opções `LIBPRODUCAO`:** `N`=Não, `S`=Sim

**Opções `PLANDEMAND`:** `S`=Sim, `N`=Não

### TGFRDARF
**Codigos de Receita - DARF**

**PK:** `CODRECEITA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODRECEITA` 🔑 | Texto | Codigo Receita e Variação |  |
| `DESCRRECEITA` | Texto | Descrição |  |
| `TIPOPESSOA` | Texto | Pessoa Fisica/Juridica |  |
| `TIPIMPOSTO` | Texto | Tipo Imposto |  |
| `PERIODICIDADE` | Texto | Periodicidade |  |

**Opções `PERIODICIDADE`:** `D`=Diario, `S`=Semanal, `X`=Decendial, `Q`=Quinzenal, `M`=Mensal, `T`=Trimestral, `A`=Anual, `U`=Quadrimestral, `B`=Bimestral, `E`=Semestral

**Opções `TIPIMPOSTO`:** `01`=IRPJ, `02`=IRRF, `03`=IPI, `04`=IOF, `05`=CSLL, `06`=PIS/PASEP, `07`=COFINS, `08`=CPMF, `09`=CIDE, `10`=RET/PAGAMENTO UNIFICADO DE TRIBUTOS, `11`=CSRF, `12`=COSIRF

**Opções `TIPOPESSOA`:** `J`=Pessoa Juridica, `F`=Pessoa Fisica

### TGFREG
**Regras**

**PK:** `CODREGRA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODREGRA` 🔑 | Inteiro | Regra |  |
| `DESCRREGRA` | Texto | Descrição |  |
| `INSTPRINC` | Texto | Instancia Principal |  |
| `INSTSEC` | Texto | Instancia Secundaria |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DTALTER` | H | Data da Alteração |  |
| `TIPO` | Texto | Permissão |  |

**Opções `TIPO`:** `R`=Proibido, `P`=Permitido

### TGFROT
**Rota**

**PK:** `CODROTA`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ATIVO` | Texto | Ativo |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DISTANCIA` | Inteiro | Distancia (Km) |  |
| `DTALTER` | H | Data/Hora |  |
| `CODROTA` 🔑 | Inteiro | Codigo da rota |  |
| `DESCRROTA` | Texto | Descrição |  |
| `OBS` | Texto | Observação |  |
| `CODROTAANTERIOR` | Inteiro | Cod. Rota Anterior |  |
| `CODROTAPOSTERIOR` | Inteiro | Cod. Rota Posterior |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

### TGFRPC
**Registro de pecas**

**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPECA` | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição da peca |  |
| `TIPO` | Texto | Tipo da peca |  |
| `COMPRIMENTO` | Decimal | Comprimento |  |
| `DIAMETROEXT` | Decimal | Diametro externo |  |
| `DIAMETROINT` | Decimal | Diametro Interno |  |
| `DIAMETROCINTA` | Decimal | Diametro da cinta |  |
| `COMPRIMENTOORELHA1` | Decimal | Comprimento orelha 1 |  |
| `COMPRIMENTOORELHA2` | Decimal | Comprimento orelha 2 |  |
| `IMAGEM` | Blob | Imagem |  |
| `UNIDADE` | Texto | Unid. Medida |  |

**Opções `TIPO`:** `V`=Cinta de vergalhão, `B`=Vergalhão dobrado, `D`=Disco, `A`=Anel, `C`=Chapa dobrada

**Opções `UNIDADE`:** `MM`=Milimetro, `CM`=Centimetro

### TGFRRC
**Registro retorno cartão**

**PK:** `NUARC`, `SEQREG`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUARC` 🔑 | Inteiro | Nro. unico | → `TGFARC`.`NUARC` |
| `SEQREG` 🔑 | Inteiro | Sequencia |  |
| `TIPO` | Texto | Tipo |  |
| `LARGTOTAL` | Inteiro | Largura total |  |
| `SQLPARAMS` | C | Parametros |  |
| `OBRIGATORIO` | Texto | Obrigatorio |  |
| `QUERYEXPORTACAO` | C | Consulta de exportação |  |
| `DATASOURCE` | Texto | Fonte de dados |  |

**Opções `OBRIGATORIO`:** `S`=Sim, `N`=Não

**Opções `TIPO`:** `F`=Footer, `H`=Header, `D`=Detalhe

### TGFSIT
**LocalObraSite**

**PK:** `CODSITE`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSITE` 🔑 | Inteiro | Cod. Site |  |
| `NOMESITE` | Texto | Nome Site |  |
| `ABREVIATURA` | Texto | Abreviatura |  |
| `CODEND` | Inteiro | Cod. Endereco | → `TSIEND`.`CODEND` |
| `NUMEND` | Texto | Numero endereco |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CODBAI` | Inteiro | Cod. Bairro | → `TSIBAI`.`CODBAI` |
| `CODCID` | Inteiro | Cod. Cidade | → `TSICID`.`CODCID` |
| `CEP` | Texto | CEP |  |
| `TELEFONE` | Texto | Telefone |  |
| `RAMAL` | Inteiro | Ramal |  |
| `FAX` | Texto | FAX |  |
| `EMAIL` | Texto | EMAIL |  |
| `ATIVO` | Texto | Ativo |  |
| `DTCAD` | H | Data cadastro |  |
| `CELULAR` | Texto | Celular |  |
| `CNPJ` | Texto | CNPJ |  |
| `INSCESTAD` | Texto | Inscrição estadual |  |
| `OBSERVACOES` | Texto | Observações |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | H | Data alteração |  |
| `GRAU` | Inteiro | Grau |  |
| `ANALITICO` | Texto | Analitico |  |
| `CODSITEPAI` | Inteiro | Cod. Site pai |  |

### TGFSTMV
**Configuração de base ST pela media de venda**

**PK:** `NROUNICO`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NROUNICO` 🔑 | Inteiro | Nro. Unico |  |
| `DHALTER` | H | Dt. Alteração |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `ATIVO` | Texto | Ativo |  |
| `EXECAUT` | Texto | Executa processamento automatico |  |
| `LISPRODEXC` | Texto | Lista de produtos a serem desconsiderados |  |
| `SUBSTCOMPVEND` | Texto | Subst. na compra e na venda (Calculo na Compra e na Venda) |  |
| `SUBSTVENDA` | Texto | Venda com subst. tributaria (Calculo de Subst. na Venda) |  |
| `SUBSTCOMPRA` | Texto | Revenda com subst. tributaria (Calculo de Subst. na Compra) |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `EXECAUT`:** `S`=Sim, `N`=Não

**Opções `SUBSTCOMPRA`:** `S`=Sim, `N`=Não

**Opções `SUBSTCOMPVEND`:** `S`=Sim, `N`=Não

**Opções `SUBSTVENDA`:** `S`=Sim, `N`=Não

### TGFTAG
**Tarefas Agendadas**

**PK:** `NUAGENDAMENTO`, `TIPOAGE`, `SEQUENCIA`  
**Referenciada por:** 24 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAGENDAMENTO` 🔑 | Inteiro | Nro. agendamento |  |
| `TIPOAGE` 🔑 | Texto | Tipo Agendamento |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `DESCRICAO` | Texto | Descrição agendamento |  |
| `CONFIG` | C | Configuração |  |
| `DHPROXEXEC` | H | Proxima execução em |  |
| `DHULTEXEC` | H | Data Final de Execução |  |
| `CODEMP` | Inteiro | Empresa |  |
| `GERALOTEPARA` | Texto | Gerar Lote para |  |
| `DIASEMANA` | Texto | Agendar os dias da Semana |  |
| `HORARIO` | Texto | Agendar os Horarios |  |
| `DIAMES` | Texto | Agendar os Dias do Mes |  |
| `MES` | Texto | Agendar os Meses |  |
| `TIPOEXEC` | Texto | Tipo Execução |  |
| `DHEXECUCAO` | H | Data da ultima execução |  |
| `STATUSULTEXEC` | Texto | Status Ultima Execução |  |
| `INFO` | C | Informações |  |
| `ATIVO` | Texto | Ativo |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `GERALOTEPARA`:** `S`=NFS-e, `P`=NF-e

**Opções `STATUSULTEXEC`:** `F`=Finalizado, `E`=Erro

**Opções `TIPOAGE`:** `ENF`=ENF, `CTZ`=CTZ, `LIV`=LIV, `REL`=REL, `AMD`=AMD

**Opções `TIPOEXEC`:** `B`=Ambos, `M`=Manual, `A`=Automatico

### TGFTAM
**TGFTAM**

**PK:** `CODTIPAMOSTRA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPAMOSTRA` 🔑 | Inteiro | Cod. Tipo Amostra |  |
| `DESCRAMOSTRA` | Texto | Descrição |  |
| `DESMEMBRA` | Texto | Desmembrar |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | Data e Hora Alteração |  |

**Opções `DESMEMBRA`:** `N`=Não, `S`=Sim

### TGFTCF
**Controle das Financeiras**

**PK:** `CODTCF`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTCF` 🔑 | Inteiro | Codigo |  |
| `VLRTAC` | Decimal | Valor Taxa Abertura Credito |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `VLRSEG` | Decimal | Valor Seguro |  |
| `ATIVO` | Texto | Ativo |  |
| `NOMETAB` | Texto | Nome Tabela |  |
| `VLRBOL` | Decimal | Valor boleto |  |
| `TAXAJUR` | Decimal | Taxa Juro |  |

### TGFTDOCSTA
**Totais de documentos por Status**

**PK:** `CODEMP`, `REFERENCIA`, `SERIENOTA`, `CODMODDOC`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMODDOC` 🔑 | Inteiro | Modelo do Doc. |  |
| `SERIENOTA` 🔑 | Texto | Serie da nota |  |
| `QTDAPRO` | Inteiro | Qtd. Aprovadas |  |
| `QTDCANC` | Inteiro | Qtd. Canceladas |  |
| `QTDDENE` | Inteiro | Qtd. Denegadas |  |
| `QTDINUT` | Inteiro | Qtd. Inutilizadas |  |
| `QTDTOTNUMUTIL` | Inteiro | Qtd. Total de Numeros Utilizados |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFDVCAB`.`CODEMP` |
| `REFERENCIA` 🔑 | Data | Dt. de Referencia | → `TGFDVCAB`.`REFERENCIA` |

### TGFTDT
**Tipo de Datas**

**PK:** `CODTIPDT`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPDT` 🔑 | Inteiro | Tipo Data |  |
| `DESCRTIPDT` | Texto | Descrição Tipo Data |  |
| `PODEDTFIM` | Texto | Pode Data Fim |  |
| `PODEMEDICAO` | Texto | Pode Medição |  |
| `PODEOBS` | Texto | Pode Observação |  |
| `CORFUNDODTINICIO` | Texto | Cor Fundo Data Inicio |  |
| `CORFONTEDTINICIO` | Texto | Cor Fonte Data Inicio |  |
| `CORFUNDODTFIM` | Texto | Cor Fundo Data Fim |  |
| `CORFONTEDTFIM` | Texto | Cor Fonte Data Fim |  |
| `OBS` | Texto | Observação |  |

### TGFTIP
**(sem descrição)**

**PK:** `CODTIP`  
**Referenciada por:** 3 tabelas  

*(Campos não mapeados no dicionário TDDCAM)*

### TGFTPP
**Tipos de Parceiros**

**PK:** `CODTIPPARC`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DHALTREG` | H | Dt. Alteração |  |
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

### TGFTPV
**Tipos de Negociação**

**PK:** `CODTIPVENDA`, `DHALTER`  
**Referenciada por:** 6 tabelas  

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
| `DHALTER` 🔑 | H | Data e hora alteração |  |
| `APRESTRANSP` | Texto | Apresenta transportadora |  |
| *... +16 campos adicionais* | | | |

**Opções `APRESTRANSP`:** `N`=Não, `S`=Sim

**Opções `ARREDPRIMEIRAPARC`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `BAIXA`:** `S`=Sim, `N`=Não

**Opções `BASEPRAZO`:** `4`=Fora o mes, `3`=Fora a quinzena, `2`=Fora a dezena, `1`=Fora a semana, `0`=A partir do dia

**Opções `DESCPROM`:** `M`=Considerar Maior, `Q`=Considerar por Qtde Somando, `N`=Não considerar, `L`=Limitante, `O`=Somar os dois, `S`=Considerar sempre, `D`=Considerar por Qtde/Desconto

### TGFVIAG
**Viagem**

**PK:** `NUVIAG`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUVIAG` 🔑 | Inteiro | Nro. Viagem |  |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `SERIE` | Texto | Serie |  |
| `STATUSDOC` | Texto | Status Doc. |  |
| `CODVEIPRIN` | Inteiro | Veiculo de tração | → `TGFVEI`.`CODVEICULO` |
| `CODVEIREB1` | Inteiro | Reboque 1 | → `TGFVEI`.`CODVEICULO` |
| `CODVEIREB2` | Inteiro | Reboque 2 | → `TGFVEI`.`CODVEICULO` |
| `CODVEIREB3` | Inteiro | Reboque 3 | → `TGFVEI`.`CODVEICULO` |
| `TIPAMB` | Texto | Tip. Amb. MDF-e |  |
| `DHALTER` | H | Data de Alteração |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `USACIOTCTEVINC` | Texto | Usar CIOTs dos CT-e vinculados ao MDF-e |  |
| `USATOMSERVCONTR` | Texto | Usar tomadores de serv. como contratantes |  |
| `CONTEMDOCTERC` | Texto | Contem documentos de terceiros |  |
| `TIPMODALMDFE` | Texto | Tipo Modal MDFe |  |

**Opções `CONTEMDOCTERC`:** `N`=Não, `S`=Sim

**Opções `STATUSDOC`:** `C`=Confirmado, `E`=Em edição

**Opções `TIPAMB`:** `1`=Produção, `0`=Não Usa, `2`=Homologação

**Opções `TIPMODALMDFE`:** `3`=Aquaviario, `1`=Rodoviario

**Opções `USACIOTCTEVINC`:** `S`=Sim, `N`=Não

**Opções `USATOMSERVCONTR`:** `N`=Não, `S`=Sim

### TGFVOA
**Volume Alternativo**

**PK:** `CODPROD`, `CODVOL`, `CONTROLE`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODVOL` 🔑 | Texto | Unidade | → `TGFVOL`.`CODVOL` |
| `DIVIDEMULTIPLICA` | Texto | Operação |  |
| `QUANTIDADE` | Decimal | Quantidade |  |
| `M3` | Decimal | Metros Cubicos |  |
| `SELECIONADO` | Texto | Seleção |  |
| `MULTIPVLR` | Decimal | Multiplicador do valor |  |
| `ATIVO` | Texto | Ativo |  |
| `CODBARRA` | Texto | Codigo de Barras |  |
| `TIPCODBARRA` | Texto | Tipo do codigo de barras |  |
| `CONTROLE` 🔑 | Texto | Controle |  |
| `UNIDTRIB` | Texto | Unid. Tributação |  |
| `UNIDSELO` | Texto | Unid. Selo |  |
| `TIPGTINNFE` | Inteiro | EAN/GTIN Unid.Tributação |  |
| `LASTRO` | Inteiro | Lastro |  |
| `CAMADAS` | Inteiro | Camadas |  |
| `OPCAOSEP` | Texto | Apresentar nas tarefas do WMS |  |
| `DESCRDANFE` | Texto | Descrição de unidade/qtd. para o DANFE |  |
| `UNTRIBEXPORTACAO` | Texto | Un. Tributação Exportação em Toneladas |  |
| `QTDDECIMAISUPF` | Inteiro | Qtd Casas Decimais UPF |  |
| `DESCRUNTRIBEXPORT` | Texto | Descrição Un. Tributação Exportação |  |
| `OPCOESGERAR0220` | Texto | Opções para gerar Registros 0220 |  |
| `UNDTRIBRECOB` | Texto | Unidade de Tributação para RECOB |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `DESCRUNTRIBEXPORT`:** `UN`=UN, `TON`=TON, `1000UN`=1000UN, `DUZIA`=DUZIA, `G`=G, `KG`=KG, `LT`=LT, `M2`=M2, `QUILAT`=QUILAT, `PARES`=PARES, `MWHORA`=MWHORA, `METRO`=METRO

**Opções `DIVIDEMULTIPLICA`:** `M`=Multiplica, `D`=Divide

**Opções `OPCAOSEP`:** `N`=Não, `S`=Sim

**Opções `OPCOESGERAR0220`:** `null`=Utiliza Unidade Alternativa, `2`=Utiliza UND do Produto Equivalente, `3`=A partir da função

**Opções `TIPCODBARRA`:** `B`=EAN14, `A`=EAN13

### TGFVTP
**Via de transporte**

**PK:** `CODVTP`  
**Referenciada por:** 2 tabelas  

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
