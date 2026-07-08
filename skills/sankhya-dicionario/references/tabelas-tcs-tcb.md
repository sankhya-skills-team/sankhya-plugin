# Tabelas TCS (CRM/Contratos/Serviços) e TCB (Contabilidade)

TCS* — CRM, ordens de serviço, contratos, projetos, SLA.
TCB* — Contabilidade: plano de contas, lançamentos, períodos contábeis.

## TCS — CRM e Serviços

### TCSCON
**Contratos**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`  
**Referenciada por:** 25 tabelas  
**entityName:** `ContradosOrigem`, `Contrato`, `ContratoArmazenagemGeral`, `ContradosOrigem`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `PERCOBRA` | Texto | Periodicidade de Cobranca |  |
| `COLORFATFORASEQ` | Texto | Colorir Faturamento Fora da Sequencia |  |
| `TEMCRIRATESP` | Texto | Possui criterio de rateio especifico |  |
| `NUMCSTC` | Inteiro | Caracteristica de Servico de Tele/Comunicação | → `TCSCSTC`.`NUMCSTC` |
| `TOTNEG` | Decimal | Valor Total Negociado |  |
| `VALNEGSC` | Decimal | Valor Negociado/SC |  |
| `QTDNEG` | Decimal | Quantidade Negociada |  |
| `PERCTOLEXCED` | Decimal | % Tolerancia Excedente |  |
| `CONTCOMPLETO` | Inteiro | Instalações ate o Periodo |  |
| `INSCEST` | Texto | Inscrição Estadual |  |
| `DTREFULTFAT` | Data | Referencia ultimo faturamento |  |
| `ENDERECO` | Texto | Endereco |  |
| `CODPROD` | Inteiro | Produto |  |
| `NOMEPARC` | Texto | Nome Parceiro |  |
| `CODSAF` | Inteiro | Safra | → `TGASAF`.`CODSAF` |
| `QTDGERARPREV` | Inteiro | Qtd. Provisões a Gerar |  |
| `SITCONT` | Texto | Situação do contrato |  |
| `VLRFINPEND` | Decimal | Valor Pend. Fin. |  |
| `DEFTIPA` | Texto | Tipo de Armazenador |  |
| `QTDFINPEND` | Inteiro | Qtd. Fin. Pendentes |  |
| `MODALIDADE` | Texto | Modalidade do Contrato |  |
| `PARCELAFAT` | Inteiro | Parcela Fat. |  |
| `DTVENCTO` | Data | Data Vencimento |  |
| `QTDPREV` | Inteiro | Qtd. Provisões |  |
| `REFERENCIA` | Texto | Referencia |  |
| `VLRTOTAL` | Decimal | Valor Total |  |
| `PADCLASS` | Inteiro | Padrão de Classificação |  |
| `REGLAUDSAIDA` | Texto | Regra p/ Laudo nas Saidas |  |
| `CODNATEX` | Inteiro | Natureza |  |
| `CONTDESINSTAL` | Inteiro | Desinstalações no Periodo |  |
| `CONTINSTAL` | Inteiro | Instalações no Periodo |  |
| `NUMCONTRATO` 🔑 | Inteiro | Numero do contrato |  |
| `VALOR` | Decimal | Valor |  |
| `VLRORIGINAL` | Decimal | Valor original |  |
| `VLRSERVICOS` | Decimal | Valor dos servicos |  |
| `AMBIENTE` | Texto | Ambiente |  |
| `UNICONVSC` | Decimal | Unidade de Conversão p/ SC |  |
| `ATIVO` | Texto | Ativo |  |
| `VALPEDFIN` | Texto | Valida pendencia financeira x estoque disponivel |  |
| `DTFINENTREGA` | Data | Data Final da Entrega |  |
| `DTINIENTREGA` | Data | Data Inicio da Entrega |  |
| `DTCONTRATO` | Data | Data do contrato |  |
| `TIPQUEBRA` | Texto | Tipo de Quebra |  |
| `CODPARC` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `QUEBRATEC` | Decimal | % Quebra Tecnica |  |
| `NUMCONTIN` | Texto | Contrato Interno |  |
| `QTDEPREVISTA` | Decimal | Qtd. Prevista |  |
| `NUNOTA` | Inteiro | Pedido de Captação |  |
| `CODCLC` | Inteiro | Caracteristica Analisavel |  |
| `UMIDPADRA` | Decimal | % Umidade Padrão Quebra de Massa |  |
| *... +108 campos* | | | |

**Opções `ACESSAHISTSUBOS`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `CIF_FOB`:** `R`=Transp. Proprio Remetente, `S`=Sem Frete, `D`=Transp. Proprio Destinatario, `C`=CIF, `F`=FOB, `T`=Terceiros

**Opções `COBPROPORCAR`:** `S`=Sobre o Saldo, `E`=Sobre a Entrada, `I`=Isento

**Opções `COBPROQUE`:** `S`=Sim, `N`=Não

### TCSOSE
**Ordem de Servico**

**PK:** `NUMOS`, `NUMOS`  
**Referenciada por:** 16 tabelas  
**entityName:** `OrdemServico`, `OrdemServico`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `NUMOS` 🔑 | Inteiro | Num. da OS |  |
| `STATUSNEG` | Texto | Status |  |
| `CODCOS` | Inteiro | Cod. Status OS | → `TCSCOS`.`CODCOS` |
| `NUMCONTRATO` | Inteiro | Num. Contrato | → `TCSCON`.`NUMCONTRATO` |
| `NUMETAPA` | Inteiro | Numero Etapa |  |
| `POSSUISLA` | Texto | Possui SLA |  |
| `TEMPOGASTOSLA` | Inteiro | Tempo Gasto SLA |  |
| `TEMPOSLA` | Inteiro | Tempo SLA |  |
| `DHCHAMADA` | Data/Hora | Dt/Hr Chamada |  |
| `CODPAP` | Inteiro | Cod. Prospect | → `TCSCTT`.`CODPAP` |
| `TEMPGASTO` | Inteiro | Tempo gasto na OS |  |
| `IDENTIFICADOR` | Texto | Identificador |  |
| `TIPO` | Texto | Tipo |  |
| `TELCONTATO` | Texto | Tel. Contato |  |
| `SITUACAO` | Texto | Situação |  |
| `CODBEM` | Texto | Bem |  |
| `DTFECHAMENTO` | Data/Hora | Data de fechamento |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `NUMOSCLIENTE` | Texto | Num. OS Cliente |  |
| `TEMPPREVISTO` | Inteiro | Tempo previsto |  |
| `ENDERECO` | Texto | Endereco |  |
| `BAIRRO` | Texto | Bairro |  |
| `CIDADE` | Texto | Cidade |  |
| `CODATEND` | Inteiro | Atendente | → `TSIUSU`.`CODUSU` |
| `CONTATO` | Texto | Contato |  |
| `DTPREVISTA` | Data/Hora | Dt/Hr limite OS |  |
| `CODUSUALTER` | Inteiro | Cod. Usuario Alteração |  |
| `CODCONTATO` | Inteiro | Cod. Contato |  |
| `DESCRICAO` | Texto | Problema |  |
| `NUFAP` | Inteiro | Numero Unico FAP |  |
| `DTALTER` | Data/Hora | Dt alteração |  |
| `CODUSUFECH` | Inteiro | Cod. Usuario Fechamento | → `TSIUSU`.`CODUSU` |
| `CODUSURESP` | Inteiro | Cod. Usuario Responsavel |  |
| `NUNOTA` | Inteiro | Nro.unico do pedido |  |
| `SERIE` | Texto | Serie |  |
| `CODVEND` | Inteiro | Gerente de Contas | → `TGFVEN`.`CODVEND` |
| `NOMECONTATO` | Texto | Nome Contato |  |
| `CODCONTATOPAP` | Inteiro | Cod. Contato Prospect | → `TCSCTT`.`CODCONTATO` |
| `DHFECHAMENTOSLA` | Data/Hora | Fechamento SLA |  |
| `CODCOSANT` | Inteiro | CODCOSANT | → `TCSCOS`.`CODCOS` |
| `NUMOSRELACIONADA` | Inteiro | OS Relacionada | → `TCSOSE`.`NUMOS` |
| `CODSERVFLUXO` | Inteiro | CODSERVFLUXO |  |
| `VARIACAOFLUXO` | Inteiro | VARIACAOFLUXO |  |
| `CODUSUSOLICITANTE` | Inteiro | Cod. Usuario Solicitante | → `TSIUSU`.`CODUSU` |
| `CODTPN` | Inteiro | CODTPN | → `TCSTPN`.`CODTPN` |
| `CODOAT` | Inteiro | Cod. Origem de Atendimento | → `TCSOAT`.`CODOAT` |
| `CODPARCATEND` | Inteiro | Cod. Parceiro Atendido | → `TGFPAR`.`CODPARC` |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `NOMEMODELO` | Texto | Nome do Modelo |  |
| *... +6 campos* | | | |

**Opções `MODELOVISIVELAPPOS`:** `N`=Não, `S`=Sim

**Opções `POSSUISLA`:** `N`=Não, `S`=Sim

**Opções `SITUACAO`:** `F`=Fechada, `P`=Aberta

**Opções `TIPO`:** `A`=Atendimento, `I`=Interno, `P`=Pre-Venda, `T`=Todas

### TCSITE
**Itens da Ordem de Servico**

**PK:** `NUMOS`, `NUMOS`, `NUMITEM`, `NUMITEM`  
**Referenciada por:** 16 tabelas  
**entityName:** `ItemOrdemServico`, `ItemOrdemServico`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCENCUSPAD` | Inteiro | Cod.Centro Resultado Padrão |  |
| `DESCRCENCUS` | Texto | Centro de Resultado |  |
| `CODVEND` | Inteiro | Cod.Vendedor |  |
| `CODUNNEXEC` | Inteiro | Cod. un. negocio executante |  |
| `CODUNNOS` | Inteiro | Cod. un. negocio OS |  |
| `TEMPOGASTOSLASUB` | Inteiro | TEMPOGASTOSLASUB |  |
| `VLRCOMISSAO` | Decimal | Vlr. Comissão |  |
| `PRODUTIVIDADE` | Decimal | Produtividade |  |
| `NUMOS` 🔑 | Inteiro | Num. OS | → `TCSOSE`.`NUMOS` |
| `NUMITEM` 🔑 | Inteiro | Sub-OS |  |
| `INICEXEC` | Data | Dt execução |  |
| `HRINICIAL` | Data/Hora | Hora Inicial |  |
| `HRFINAL` | Data/Hora | Hora Final |  |
| `TIPOOS` | Texto(15) | Tipo OS |  |
| `CODUSU` | Inteiro | Cod. Usuario Executante | → `TSIUSU`.`CODUSU` |
| `CLASSIFICACAO` | Texto(25) | Classificação |  |
| `CODSERV` | Inteiro | Cod. Servico | → `TGFPRO`.`CODPROD` |
| `CODPROD` | Inteiro | Cod. Produto | → `TGFPRO`.`CODPROD` |
| `SOLUCAO` | Texto | Solução |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `CODPROJ` | Inteiro | Cod. Projeto | → `TCSPRJ`.`CODPROJ` |
| `CODOCOROS` | Inteiro | Motivo | → `TCSOOS`.`CODOCOROS` |
| `COBRAR` | Texto | Cobrar |  |
| `CODUSUALTER` | Inteiro | Cod. Usuario |  |
| `DESCSERV` | Texto | Problema |  |
| `DHPREVISTA` | Data/Hora | Agendamento |  |
| `DTALTER` | Data/Hora | Dt. alteração do item |  |
| `DTPREVFECHAMENTO` | Data/Hora | Data Limite Sub OS |  |
| `EXECUTANTE` | Texto | Executante (Painel de filtros) |  |
| `GRAUDIFIC` | Inteiro | Grau de dificuldade |  |
| `INTERVALO` | Inteiro | Intervalo |  |
| `LIBERADO` | Texto | Liberado |  |
| `QTDSERV` | Decimal | Quantidade servico |  |
| `RETRABALHO` | Texto | Retrabalho |  |
| `SERIE` | Texto | Serie |  |
| `QTDHORA` | Data/Hora | Qtd. Horas |  |
| `TEMPGASTO` | Inteiro | Tempo gasto |  |
| `QTDHORAEXT` | Decimal | Qtd. Horas Extras |  |
| `TEMPPREVISTO` | Data/Hora | Tempo previsto para executar a OS |  |
| `TERMEXEC` | Data/Hora | Termino da execução |  |
| `QTDHORABONIF` | Decimal | Qtd. Horas Bonif. |  |
| `QTDHORAEXTBONIF` | Decimal | Qtd. Horas Extras Bonif. |  |
| `TIPO` | Texto | Tipo |  |
| `QTDHORACOMBONIF` | Decimal | Qtd.Horas Com.Bonif. |  |
| `VLRCOBRADO` | Decimal | Valor a ser cobrado |  |
| `CODUSUREM` | Inteiro | Cod. Usuario Remetente | → `TSIUSU`.`CODUSU` |
| `QTDHORAEXTCOMBONIF` | Decimal | Qtd.Horas Extras Com.Bonif. |  |
| `DHENTRADA` | Data/Hora | Dt Entrada Sub-OS |  |
| `VLRHORAFAT` | Decimal | Vlr. Hora |  |
| `VLRHORAEXTFAT` | Decimal | Vlr. Hora Extra |  |
| *... +20 campos* | | | |

**Opções `CLASSIFICACAO`:** `N`=Não Conformidade, `I`=Indeterminado, `S`=Servicos Complementares, `C`=Conformidade

**Opções `COBRAR`:** `N`=Não, `S`=Sim

**Opções `EXECUTANTE`:** `R`=Responsavel, `E`=Executante, `F`=Executante e Filas que participa, `A`=Atendente

**Opções `LIBERADO`:** `S`=Sim, `N`=Não

**Opções `RETRABALHO`:** `N`=Não, `S`=Sim

### TCSPRJ
**Cadastro de Projetos**

**PK:** `CODPROJ`, `CODPROJ`  
**Referenciada por:** 42 tabelas  
**entityName:** `Projeto`, `Projeto2`, `Projeto3`, `Projeto`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROJ` 🔑 | Inteiro | Projeto |  |
| `IDENTIFICACAO` | Texto | Identificação |  |
| `AMOSTRACUSMAX` | Inteiro | Amostras por Custodia |  |
| `ABREVIATURA` | Texto | Abreviação Projeto |  |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `DTINICIO` | Data/Hora | Data Inicio |  |
| `DTTERMINO` | Data/Hora | Data de Termino |  |
| `LIMBONIF` | Decimal | Limite de Bonificação |  |
| `GRAU` | Inteiro | Grau |  |
| `CODCLT` | Inteiro | Padrão de Classificação | → `TGACLT`.`CODCLT` |
| `CODUSURESP` | Inteiro | Cod. Usuario Responsavel | → `TSIUSU`.`CODUSU` |
| `ULTIMORDO` | Inteiro | Ultimo numero RDO |  |
| `HRINICIALMIN` | Inteiro | Hora Inicial Minima |  |
| `HRFINALMAX` | Inteiro | Hora Final Maxima |  |
| `INTERVALOMIN` | Inteiro | Intervalo Minimo |  |
| `INTERVALOMAX` | Inteiro | Intervalo Maximo |  |
| `CARGAHORMAX` | Inteiro | Carga Horaria Maxima |  |
| `RETENCAOATIVA` | Texto | Retenção Ativa |  |
| `PERCRETENCAO` | Decimal | Percentual de Retenção |  |
| `CODPROJPAI` | Inteiro | Projeto pai |  |
| `CODCTACTB` | Inteiro | Conta Contabil 1 | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB2` | Inteiro | Conta Contabil 2 | → `TCBPLA`.`CODCTACTB` |
| `NUQUE` | Inteiro | Questionario | → `TGFQUE`.`NUQUE` |
| `TIMCONTACOMPART` | Texto | Conta Compartilhada |  |
| `TIMTXPART` | Decimal | Participação % |  |
| `TIMPARCPROJ` | Inteiro | Parceiro | → `TSIEMP`.`CODEMP` |
| `TIMNMCTACOMP` | Inteiro | Conta Bancaria | → `TSICTA`.`CODCTABCOINT` |
| `DH_CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `DH_DTPREVISTA` | Data | Dt. Prevista Conclusão |  |
| `DH_ADITIVO` | Texto | Aditivo |  |
| `DH_CODPRJPRINC` | Inteiro | Projeto Principal | → `TCSPRJ`.`CODPROJ` |
| `DH_STATUSPROJ` | Texto | Status Projeto |  |
| `DH_CUSTOTOTETAPAS` | Decimal | Custo Total Itens Etapas |  |
| `DH_REALTOTETAPAS` | Decimal | Realizado Total Itens Etapas |  |
| `DH_VLRFATPRJ` | Decimal | Vlr. Faturado |  |
| `DH_VLRFATURARPRJ` | Decimal | Vlr. a Faturar |  |
| `DH_VLRPROJ` | Decimal | Vlr. Inicial Projeto |  |
| `DH_VLRTOTFINAL` | Decimal | Saldo Projeto |  |
| `DH_OBSERVACAO` | Texto | Observação |  |
| `DH_CODNAT` | Inteiro | Cod. Natureza | → `TGFNAT`.`CODNAT` |
| `DH_CODCENCUS` | Inteiro | Cod. Centro de Resultado | → `TSICUS`.`CODCENCUS` |
| `DH_CODTIPVENDA` | Inteiro | Tipo de Negociação |  |
| `DH_CODTIPCONT` | Inteiro | Cod. Tipo Contrato |  |
| `DH_VLRCUSTOTPREVPRE` | Decimal | Vlr. Custo Total Previsto Precificação |  |
| `DH_VLRCUSTOTPREVPRO` | Decimal | Vlr. Custo Total Previsto Projeto |  |
| `DH_VLRCUSTOTLIB` | Decimal | Vlr. Custo Total Liberado |  |
| `DH_CODUSULIB` | Inteiro | Usuario Liberador | → `TSIUSU`.`CODUSU` |
| *... +1 campos* | | | |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `DH_ADITIVO`:** `S`=Sim, `N`=Não

**Opções `DH_STATUSLIB`:** `L`=Aguardando Liberação, `R`=Reprovado, `S`=Liberação não Necessaria, `N`=Liberação Necessaria, `A`=Aprovado

**Opções `DH_STATUSPROJ`:** `R`=Reaberto, `G`=Concluido em Garantia, `I`=A Iniciar, `E`=Em Andamento, `C`=Finalizado

### TCSFET
**Etapa de Projeto**

**PK:** `NUFAP`, `NUFAP`, `NUMETAPA`, `NUMETAPA`  
**Referenciada por:** 22 tabelas  
**entityName:** `EtapaProjeto`, `EtapaProjeto`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DESCRICAO` | Texto | Descrição |  |
| `VALOR` | Decimal | Valor |  |
| `DTCEDOINIPREV` | Data | Inicio |  |
| `DTCEDOFIMPREV` | Data | Fim |  |
| `CONCLUIDA` | Texto | Concluida |  |
| `CODPROD` | Inteiro | Servico |  |
| `DTTARDEINIPREV` | Data | Inicio Limite |  |
| `DTTARDEFIMPREV` | Data | Fim Limite |  |
| `NUFAP` 🔑 | Inteiro | Numero da FAP | → `TCSFAP`.`NUFAP` |
| `NUMETAPA` 🔑 | Inteiro | Numero da Etapa |  |
| `NUMETAPAPAI` | Inteiro | Numero da Etapa Pai |  |
| `NUMSEQ` | Inteiro | Sequencia |  |
| `SUPLEMENTA` | Texto | Empresta |  |
| `SUPLEMENTADO` | Texto | Pega Emprestado |  |
| `TIPVALOR` | Texto | Tipo de Valor |  |
| `VLRSUPLEMENTA` | Decimal | Hrs. Suplementa |  |
| `VLRSUPLEMENTADO` | Decimal | Hrs. Suplementado |  |
| `VLRSUPLEMENTADOREA` | Decimal | Hrs. Suplementado Real |  |
| `VLRSUPLEMENTAREA` | Decimal | Hrs. Suplementa Real |  |
| `CONCLUSAOAUTOMATICA` | Texto | Concluir ao fechar Sub-OS |  |
| `CHAVEIMP` | Inteiro | Chave para importação do Project |  |
| `EXIGEREQ` | Texto | Exigir requisito em Sub-OS |  |
| `OBSERVACAO` | Texto | Observação |  |
| `NUMMODELO` | Inteiro | Numero do Modelo |  |

**Opções `CONCLUIDA`:** `S`=Sim, `N`=Não

**Opções `CONCLUSAOAUTOMATICA`:** `N`=Não, `S`=Sim

**Opções `EXIGEREQ`:** `N`=Não, `S`=Sim

**Opções `SUPLEMENTA`:** `S`=Sim, `N`=Não

**Opções `SUPLEMENTADO`:** `N`=Não, `S`=Sim

### TCSFAP
**Projeto Servico (FAP)**

**PK:** `NUFAP`, `NUFAP`  
**Referenciada por:** 11 tabelas  
**entityName:** `ProjetoServico`, `ProjetoServico`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUFAP` 🔑 | Inteiro | Numero do Projeto |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFCTT`.`CODPARC` |
| `QTDHORAS` | Inteiro | Quantidade de Horas |  |
| `CODMETOD` | Inteiro | Modelo | → `TCSMET`.`CODMETOD` |
| `STATUS` | Texto | Status |  |
| `OBSERVACAO` | Texto | Observação |  |
| `CODCONTATO` | Inteiro | Contato | → `TGFCTT`.`CODCONTATO` |
| `CODCOORD` | Inteiro | Coordenador |  |
| `IMPLANTADOR` | Texto | Implantador |  |
| `NUNOTA` | Inteiro | Numero da Nota | → `TGFCAB`.`NUNOTA` |
| `LIMITAPROD` | Texto | Limitar Produtos |  |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `COR` | Texto | Cor das etapas (no grafico) |  |

**Opções `IMPLANTADOR`:** `S`=Sim, `N`=Não

**Opções `LIMITAPROD`:** `N`=Não, `S`=Sim

**Opções `STATUS`:** `S`=Suspenso, `C`=Concluido, `E`=Cancelado, `NC`=Não Configurado, `P`=Em Andamento

### TCSPAD
**Parcelas Adicionais**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `SEQUENCIA`, `SEQUENCIA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ATIVO` | Texto | Ativo |  |
| `CODNAT` | Inteiro | Natureza | → `TGFNAT`.`CODNAT` |
| `REFERENCIA` | Data | Dt. referencia |  |
| `DTREAJUSTE` | Data | Dt. base reajuste |  |
| `VENCTO` | Inteiro | Prazo vencto |  |
| `DIAPAG` | Inteiro | Dia do pagto |  |
| `PERIODICIDADE` | Texto | Periodicidade |  |
| `NUMCONTRATO` 🔑 | Inteiro | Contrato | → `TCSCON`.`NUMCONTRATO` |
| `QTDGERARPREV` | Inteiro | Qtd. provisões a gerar |  |
| `QTDPREV` | Inteiro | Qtd. provisões |  |
| `VALOR` | Decimal | Valor |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHALTER` | Data/Hora | Dt. alteração |  |
| `DTVENCTO` | Data | Data vencimento |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `PERIODICIDADE`:** `T`=Trimestral, `Q`=Quadrimestral, `S`=Semestral, `M`=Mensal, `A`=Anual, `B`=Bimestral, `P`=Parcela Unica

### TCSPIT
**Itens Parcelas Adicionais**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `SEQUENCIA`, `SEQUENCIA`, `CODPROD`, `CODPROD`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCONTRATO` 🔑 | Inteiro | Contrato | → `TCSCON`.`NUMCONTRATO` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `QUANTIDADE` | Inteiro | Quantidade |  |
| `VALOR` | Decimal | Valor |  |
| `VLRIGUALPARC` | Texto | Valor igual a Parcela |  |
| `PARCPROP` | Texto | 1 Parc. Proporcional |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHALTER` | Data/Hora | Dt. Alteração |  |

**Opções `PARCPROP`:** `N`=Não, `S`=Sim

**Opções `VLRIGUALPARC`:** `N`=Não, `S`=Sim

### TCSRSL
**Regra SLA**

**PK:** `NUSLA`, `NUSLA`, `NUMREG`, `NUMREG`  
**Referenciada por:** 6 tabelas  
**entityName:** `RegraSLA`, `RegraSLAPadrao`, `RegraSLA`, `RegraSLAPadrao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUSLA` 🔑 | Inteiro | Nro. Unico SLA | → `TCSSLA`.`NUSLA` |
| `NUMREG` 🔑 | Inteiro | Num. Regra |  |
| `ORDEM` | Inteiro | Ordem de Classificação |  |
| `BASECALCTEMPO` | Texto | Base de Calculo para Tempo |  |
| `CODPROD` | Inteiro | Produto |  |
| `CODSERV` | Inteiro | Servico |  |
| `CODGRUPOPROD` | Inteiro | Grupo de Produtos |  |
| `CODOCOROS` | Inteiro | Motivo |  |
| `PADRAO` | Texto | Regra Padrão |  |
| `TIPOTEMPO` | Texto | Tipo de Tempo |  |
| `VALORTEMPO` | Inteiro | Tempo |  |
| `USAREGRAPADRAO` | Texto | Usar em conjunto com a regra |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `TEMPOTOTAL` | Inteiro | TEMPOTOTAL |  |
| `CODCARGAHOR` | Inteiro | Carga Horaria | → `TFPCGH`.`CODCARGAHOR` |

**Opções `BASECALCTEMPO`:** `O`=Dt. Chamada OS, `S`=Dt. Chegada Sub-OS

**Opções `TIPOTEMPO`:** `H`=Horas, `D`=Dias

### TCSSLT
**Tempo de SLA**

**PK:** `NUMOS`, `NUMOS`, `NUMITEM`, `NUMITEM`  
**entityName:** `TempoSLA`, `TempoSLA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMOS` 🔑 | Inteiro | OS | → `TCSITE`.`NUMOS` |
| `NUMITEM` 🔑 | Inteiro | Sub-OS | → `TCSITE`.`NUMITEM` |
| `TEMPOSLA` | Inteiro | Tempo de SLA |  |
| `SLADECORRIDO` | Inteiro | SLA Decorrido |  |
| `SLARESTANTE` | Inteiro | SLA Restante |  |
| `HORASUTEIS` | Texto | HORASUTEIS |  |

**Opções `HORASUTEIS`:** `N`=Não, `S`=Sim

### TCSSLA
**Cadastro de SLA**

**PK:** `NUSLA`, `NUSLA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUSLA` 🔑 | Inteiro | Nro. Unico SLA |  |
| `DESCRICAO` | Texto | Descrição |  |
| `TIPOFILTRO` | Texto | Tipo de Filtragem de Regras |  |
| `CODCARGAHOR` | Inteiro | Carga Horaria | → `TFPCGH`.`CODCARGAHOR` |

**Opções `TIPOFILTRO`:** `T`=Todas Regras combinando, `P`=Primeira Regra combinando

### TCSSER
**Produtos e Servicos**

**PK:** `CODNAT`, `CODNAT`, `CODPROD`, `CODPROD`  
**entityName:** `ProdutoServico`, `ProdutoServico`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNAT` 🔑 | Inteiro | Cod. Natureza | → `TGFNAT`.`CODNAT` |
| `CODPROD` 🔑 | Inteiro | Servico | → `TGFPRO`.`CODPROD` |
| `LIMITANTE` | Texto | Limitante |  |
| `QTDEPREVISTA` | Decimal | Quantidade prevista |  |
| `FREQUENCIA` | Inteiro | Frequencia |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `TIPO` | Texto | Tipo |  |
| `USAOSPORTAL` | Texto | Usado em OS no portal |  |

**Opções `LIMITANTE`:** `N`=Não, `S`=Sim

**Opções `USAOSPORTAL`:** `N`=Não, `S`=Sim

### TCSCOM
**Comissões**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `CODPARC`, `CODPARC`, `CODPROD`, `CODPROD`  
**entityName:** `Comissao`, `Comissao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCONTRATO` 🔑 | Inteiro | Numero do Contrato | → `TCSCON`.`NUMCONTRATO` |
| `CODPARC` 🔑 | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `PERCCOM` | Decimal | Percentual de Comissão |  |
| `VLRCOMISSAO` | Decimal | Valor da Comissão |  |

### TCSCCF
**Comissão Faturamento**

**PK:** `NUNOTA`, `NUNOTA`, `NUMCONTRATO`, `NUMCONTRATO`, `CODPROD`, `CODPROD`, `CODVEND`, `CODVEND`, `SEQUENCIA`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | NUNOTA | → `TGFCCM`.`NUNOTA` |
| `NUMCONTRATO` 🔑 | Inteiro | NUMCONTRATO | → `TCSVPC`.`NUMCONTRATO` |
| `CODPROD` 🔑 | Inteiro | CODPROD | → `TCSVPC`.`CODPROD` |
| `CODVEND` 🔑 | Inteiro | CODVEND | → `TGFCCM`.`CODVEND` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TCSVPC`.`SEQUENCIA` |

### TCSCPA
**Comercial Parceiro**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `SEQUENCIA`, `SEQUENCIA`  
**Referenciada por:** 2 tabelas  
**entityName:** `ComercialParceiro`, `ParceiroInstalacao`, `ComercialParceiro`, `ParceiroInstalacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCONTRATO` 🔑 | Inteiro | Numero do Contrato | → `TCSCGR`.`NUMCONTRATO` |
| `GRUPO` | Inteiro | Grupo | → `TCSCGR`.`GRUPO` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `DTPREVINST` | Data | Data Prevista Instalação |  |
| `DTINST` | Data | Data Instalação |  |
| `OBS1` | Texto | Observação |  |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `CONTATO` | Texto | Contato |  |
| `TELEFONE` | Texto | Telefone |  |
| `CIDADE_PARC` | Texto | Cidade Parceiro |  |
| `ESTADO_PARC` | Texto | Estado |  |
| `TIPO_PARC` | Texto | Tipo |  |
| `ENDERECO_PARC` | Texto | Endereco |  |
| `NUMERO_PARC` | Texto | Numero |  |
| `COMPLEMENTO_PARC` | Texto | Complemento |  |
| `CEP_PARC` | Texto | Cep |  |
| `CGC_CPF` | Inteiro | CGC CPF |  |
| `TELEFONE_PARC` | Texto | Telefone Parc. |  |

### TCSCPR
**Comercial Produto**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `GRUPO`, `GRUPO`, `CODPROD`, `CODPROD`  
**entityName:** `ComercialProduto`, `ComercialProduto`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCONTRATO` 🔑 | Inteiro | Numero do Contrato | → `TCSCGR`.`NUMCONTRATO` |
| `GRUPO` 🔑 | Inteiro | Grupo | → `TCSCGR`.`GRUPO` |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODFORN` | Inteiro | Fornecedor | → `TGFPAR`.`CODPARC` |
| `QTDNEG` | Decimal | Quantidade Cliente |  |
| `QTDPEDIR` | Decimal | Quantidade P/ Gerar Ped |  |
| `QTDPED` | Decimal | Quantidade Requisitada |  |
| `DTPREVINST` | Data | Data Prevista |  |
| `QTDPEDVDA` | Decimal | Quantidade Entregue |  |
| `PRINCIPAL` | Texto | Principal |  |
| `VALOR` | Decimal | Valor |  |
| `IMPNOTA` | Texto | Imprime na Nota |  |
| `IMPOS` | Texto | Imprime na Ordem de Servico |  |
| `COMPLDESC` | Texto | Complemento |  |

**Opções `IMPNOTA`:** `S`=Sim, `N`=Não

**Opções `IMPOS`:** `N`=Não, `S`=Sim

**Opções `PRINCIPAL`:** `N`=Não, `S`=Sim

### TCSPSC
**Produtos e Servicos do Contrato**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `CODPROD`, `CODPROD`  
**Referenciada por:** 14 tabelas  
**entityName:** `ProdutoServicoContrato`, `ProdutoServicoContrato2`, `ProdutoServicoContrato`, `ProdutoServicoContrato2`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUSUALTREG` | Inteiro | Cod. Usuario Alteração |  |
| `NUMCONTRATO` 🔑 | Inteiro | Numero do contrato | → `TCSCON`.`NUMCONTRATO` |
| `DHALTREG` | Data/Hora | Dt. Alteração |  |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `SITPROD` | Texto | Situação |  |
| `QTDEPREVISTA` | Decimal | Qtd. Prevista |  |
| `LIMITANTE` | Texto | Limitante |  |
| `PRODPRINC` | Texto | Produto principal |  |
| `CODPARCPREF` | Inteiro | Cod. Parceiro Fornecedor preferencial | → `TGFPAR`.`CODPARC` |
| `QTDMESES` | Inteiro | Quantidade de meses do contrato |  |
| `FREQUENCIA` | Inteiro | Frequencia |  |
| `VERSAO` | Texto | Versão |  |
| `DTVERSAO` | Data | Data da versão |  |
| `VLRUNIT` | Decimal | Valor unitario |  |
| `NUMUSUARIOS` | Decimal | Numero de usuarios |  |
| `QTDUSU` | Inteiro | Quantidade de usuario / login |  |
| `NUMSERIE` | Texto | Numero de serie |  |
| `IMPRNOTA` | Texto | Imprimir nota |  |
| `IMPROS` | Texto | Imprimir OS |  |
| `GRUPIMPRESSAO` | Inteiro | Grupo de impressão |  |
| `OBSERVACAO` | Texto | Local de instalação |  |
| `TOPFATURCON` | Inteiro | TOP para faturamento em contratos |  |
| `SERFATURCON` | Texto | Serie para faturamento em contratos |  |

**Opções `IMPRNOTA`:** `S`=Sim, `N`=Não

**Opções `IMPROS`:** `S`=Sim, `N`=Não

**Opções `LIMITANTE`:** `S`=Sim, `N`=Não

**Opções `PRODPRINC`:** `N`=Não, `S`=Sim

**Opções `SITPROD`:** `S`=Suspenso, `C`=Cancelado, `B`=Bonificado, `A`=Ativo

### TCSVPC
**Vendedores do Produto do Contrato**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `CODPROD`, `CODPROD`, `CODVEND`, `CODVEND`, `SEQUENCIA`, `SEQUENCIA`  
**Referenciada por:** 4 tabelas  
**entityName:** `VendedorProdutoContrato`, `VendedorProdutoContrato`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCONTRATO` 🔑 | Inteiro | Contrato | → `TCSCON`.`NUMCONTRATO` |
| `CODPROD` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODVEND` 🔑 | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TIPO` | Texto | Tipo |  |
| `VLRBASE` | Decimal | Valor Base p/ Comissão |  |
| `PERCCOM` | Decimal | Percentual de Comissão |  |
| `DTINI` | Data | Data Inicial |  |
| `DTFIM` | Data | Data Final |  |
| `NUNOTA` | Inteiro | Nro. Unico Pedido | → `TGFCAB`.`NUNOTA` |
| `OBSERVACAO` | Texto | Observação |  |
| `QTDFAT` | Inteiro | Qtd. Faturada |  |
| `DHALTER` | Data/Hora | Dt./Hora Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario Alteração | → `TSIUSU`.`CODUSU` |

**Opções `TIPO`:** `R`=Renegociação, `A`=Produto Adicional, `N`=Nova Negociação, `U`=Usuario Adicional

### TCSCOS
**Classificação de OS**

**PK:** `CODCOS`, `CODCOS`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCOS` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `SUSPENDERSLA` | Texto | Suspender SLA |  |
| `FECHARSLA` | Texto | Fechar SLA |  |

**Opções `FECHARSLA`:** `N`=Não, `S`=Sim

**Opções `SUSPENDERSLA`:** `S`=Sim, `N`=Não

### TCSGEC
**Grupo Economico**

**PK:** `NUMCONTRATO`, `NUMCONTRATO`, `CODPARC`, `CODPARC`  
**entityName:** `GrupoEconomicoContrato`, `GrupoEconomicoContrato`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCONTRATO` 🔑 | Inteiro | Numero do contrato | → `TCSCON`.`NUMCONTRATO` |
| `CODPARC` 🔑 | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `PERCCUSTO` | Decimal | % de custo |  |

## TCB — Contabilidade

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
| `CLASSIFIRPJ` | Texto | Classificação IRPJ |  |
| `CLASSIFCSLL` | Texto | Classificação CSLL |  |
| `ADICOESIRPJ` | Texto | ( + ) Adições |  |
| `EXCLUSOESIRPJ` | Texto | ( - ) Exclusões |  |
| `PAT4IRPJ` | Texto | PAT 4% |  |
| `CONRESULTIRPJ` | Texto | Conta de Resultado |  |
| `ZERACRIRPJ` | Texto | Zeramento de Contas de Resultado |  |
| `ADICOESCSLL` | Texto | ( + ) Adições |  |
| `EXCLUSOESCSLL` | Texto | ( - ) Exclusões |  |
| `CONRESULTCSLL` | Texto | Conta de Resultado |  |
| *... +2 campos* | | | |

**Opções `ADICOESCSLL`:** `N`=Não, `S`=Sim

**Opções `ADICOESIRPJ`:** `S`=Sim, `N`=Não

**Opções `ANALITICA`:** `N`=Não, `S`=Sim

**Opções `ATIVA`:** `S`=Sim, `N`=Não

**Opções `BEMORIGINAL`:** `S`=Sim, `N`=Não

### TCBEMP
**Empresas (contabilidade)**

**PK:** `CODEMP`  
**Referenciada por:** 26 tabelas  
**entityName:** `EmpresaContabilidade`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod. Empresa | → `TSIEMP`.`CODEMP` |
| `DTABERTURA` | Data | Data da abertura |  |
| `DTINICPERCTB` | Data | Inicio do periodo contabil |  |
| `DTFIMPERCTB` | Data | Fim do periodo contabil |  |
| `REFERENCIA` | Data | Referencia |  |
| `NUMDIARIO` | Inteiro | Numero do diario |  |
| `ULTPAGDIARIO` | Inteiro | Ultima pagina do diario |  |
| `CONTADOR` | Texto | Contador |  |
| `CRC` | Texto | CRC |  |
| `MASCCTA` | Texto | Mascara da conta |  |
| `DIGCTA` | Texto | Digito da conta |  |
| `CODEMPPLACTA` | Inteiro | Empresa do plano de contas | → `TSIEMP`.`CODEMP` |
| `PERALTQDCOM` | Texto | Permitir alteração por outras empresas quando compartilhado |  |
| `EMPCOPPLA` | Inteiro | Empresa p/ copiar o plano de contas |  |
| `CTAREDAUT` | Texto | Conta reduzida automatica |  |
| `ACEITARHISTZERO` | Texto | Aceitar historico zero |  |
| `UTILCENCUS` | Texto | Utiliza Centro de resultado |  |
| `UTILPROJ` | Texto | Utiliza Projeto |  |
| `NUMLOTESAUT` | Texto | Numeração dos Mestres de Lote |  |
| `ULTIMONUMEROUSADO` | Inteiro | Ultimo Numero Usado |  |
| `SIMBVLRNEG` | Texto | Simbolo para valores negativos |  |
| `ACEITARVLRLANC` | Texto | Aceitar valor lancamento zero |  |
| `TIPATUALSALDOS` | Texto | Tipo de atualização de saldos |  |
| `EMPCONSOLIDA` | Texto | Consolida empresa |  |
| `CODEMPORIG` | Inteiro | Cod. Empresa Origem |  |
| `PERCRATEIO` | Inteiro | % Rateio |  |
| `NROORDEM` | Inteiro | N. Ordem Instrumento Escrituração (G) |  |
| `NROORDEM_R` | Inteiro | N. Ordem Instrumento Escrituração (R) |  |
| `UFCRCCONTADOR` | Texto | UF CRC |  |
| `CODINSTRESP` | Texto | Instituição Resp. Man. Plano Contas Referencial |  |
| `NROLOTEMNUALINI` | Inteiro | Inicio do numero do lote manual |  |
| `TIPPERIODO` | Texto | Periodo de Geração das Demonstrações Contabeis |  |
| `NROLOTEMNUALFIM` | Inteiro | Fim do numero do lote manual |  |
| `TPOEMPRESA` | Inteiro | Tipo de Empresa |  |
| `CABDEM` | Texto | Cabecalho das Demonstrações |  |
| `CODCTACTBENCRES` | Inteiro | Conta Contabil de Encerramento de Resultado | → `TCBPLA`.`CODCTACTB` |
| `OPTREFIS` | Texto | Optante pelo REFIS |  |
| `OPTPAES` | Texto | Optante pelo PAES |  |
| `FORMATRIB` | Inteiro | Forma de Tributação |  |
| `FORMAAPUR` | Texto | Indicador do Periodo de Apuração de IRPJ e da CSLL |  |
| `TIPESCPRE` | Texto | Escrituração |  |
| `TIPENT` | Texto | Tipo de Pessoa Juridica Imune ou Isenta |  |
| `FORMAAPURI` | Texto | Apuração do IRPJ para Imunes ou Isentas |  |
| `APURCSLL` | Texto | Apuração do CSLL para Imunes ou Isentas |  |
| `PJSUJEITACSLL` | Texto | PJ Sujeita a Aliquota da CSLL de 9% ou 17% ou 20% em 31/12/2015 |  |
| `OPTEXTRTT` | Texto | Optante pela extinção do RTT no ano-calendario de 2014 |  |
| `DIFFCONT` | Texto | Existe diferencas entre a contabilidade societaria e Fcont |  |
| `INDALIQCSLL` | Texto | PJ Sujeita a Aliquota da CSLL de 15% |  |
| `INDADMFUNCLU` | Texto | Administradora de Fundos e Clubes de Investimento |  |
| `INDPARTCONS` | Texto | Participações em Consorcios de Empresas |  |
| *... +61 campos* | | | |

**Opções `ACEITARHISTZERO`:** `N`=Não, `S`=Sim

**Opções `ACEITARVLRLANC`:** `N`=Não, `S`=Sim

**Opções `ALIQCSLL`:** `9`=9%, `15`=15%

**Opções `APURCSLL`:** `A`=A - Anual, se optou pela apuração da CSLL sobre a base de calculo estimada, `D`=D - Desobrigada, na hipotese de pessoa juridica imune ou isenta da CSLL, `T`=T - Trimestral, no caso de ter adotada apuração trimestral da CSLL

**Opções `CODINSTRESP`:** `0`=Nenhuma, `1`=1 - PJ em Geral, `2`=2 - PJ em Geral - Lucro Presumido, `3`=3 - Financeiras, `4`=4 - Seguradoras ou Entidades Abertas de Previdencia Complementar, `5`=5 - Imunes e Isentas em Geral, `6`=6 - Imunes e Isentas - Financeiras, `7`=7 - Imunes e Isentas - Seguradoras, `8`=8 - Entidades Fechadas de Previdencia Complementar, `9`=9 - Partidos Politicos, `10`=10 - Financeiras - Lucro Presumido

### TCBPCT
**Periodo Contabil**

**PK:** `NUPERIODOCTB`  
**Referenciada por:** 16 tabelas  
**entityName:** `PeriodoContabil`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPERIODOCTB` 🔑 | Inteiro | Nro periodo contabil |  |
| `CODEMP` | Inteiro | Codigo Empresa | → `TCBEMP`.`CODEMP` |
| `INICIOPERIODO` | Data | Inicio periodo contabil |  |
| `FIMPERIODO` | Data | Fim periodo contabil |  |
| `DHALTER` | Data/Hora | Dh. alteração |  |
| `CODUSU` | Inteiro | Codigo Usuario |  |
| `DESCRICAO` | Texto | Descrição |  |

### TCBLOT
**Mestres de Lotes**

**PK:** `CODEMP`, `REFERENCIA`, `NUMLOTE`  
**Referenciada por:** 9 tabelas  
**entityName:** `MestreLote`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TCBEMP`.`CODEMP` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `NUMLOTE` 🔑 | Inteiro | Nro. Lote |  |
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `DTMOV` | Data | Dt. Movimento |  |
| `TOTLOTE` | Decimal | Total do lote |  |
| `SITUACAO` | Texto | Situação |  |
| `ULTLANC` | Inteiro | Ult. Lancamento |  |
| `VLRDEBITO` | Decimal | Debito |  |
| `VLRCREDITO` | Decimal | Credito |  |
| `VLRDIFERENCA` | Decimal | Diferenca |  |
| `QTDLANC` | Inteiro | Qtd. Lancamentos |  |
| `CODEMPCONSOLID` | Inteiro | Empresa Origem (Consolidação)] |  |
| `COMENTARIOS` | Texto | Observação |  |

**Opções `SITUACAO`:** `A`=Aberto, `F`=Fechado

### TCBLAN
**Lancamentos**

**PK:** `CODEMP`, `REFERENCIA`, `NUMLOTE`, `NUMLANC`, `TIPLANC`, `SEQUENCIA`  
**Referenciada por:** 6 tabelas  
**entityName:** `Lancamento`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCTACTB` | Inteiro | Conta Contabil (Red.) | → `TCBPLA`.`CODCTACTB` |
| `NUMDOC` | Inteiro | Num. Documento |  |
| `VENCIMENTO` | Data | Vencimento |  |
| `VLRLANC` | Decimal | Valor Lancamento |  |
| `TIPLANC` 🔑 | Texto | Tip. Lancamento |  |
| `LIBERADO` | Texto | Liberado |  |
| `CODHISTCTB` | Inteiro | Historico | → `TCBHIS`.`CODHISTCTB` |
| `REFERENCIA` 🔑 | Data | Referencia | → `TCBLOT`.`REFERENCIA` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TCBLOT`.`CODEMP` |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DTMOV` | Data | Data Movimento |  |
| `NUMLOTE` 🔑 | Inteiro | Num. Lote | → `TCBLOT`.`NUMLOTE` |
| `NUMLANC` 🔑 | Inteiro | Num. Lancamento |  |
| `CODCONPAR` | Inteiro | Conta Contrapartida | → `TCBPLA`.`CODCTACTB` |
| `COMPLHIST` | Texto | Complemento |  |
| `CODCENCUS` | Inteiro | Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `PARTLALUR_A` | Texto | Parte A do e-LALUR |  |
| `VLRCRED` | Decimal | Valor Credito |  |
| `EXTEMPORANEO` | Texto | Extemporaneo |  |
| `VLRDEB` | Decimal | Valor Debito |  |
| `DTEXTEMPORANEO` | Data | Dt. Ocorrencia Extem. |  |
| `CODEMPORIG` | Inteiro | Empresa de Origem |  |
| `AD_CODPROD` | Inteiro | Cod. Produto | → `TGFPRO`.`CODPROD` |
| `CHAVE` | Texto | Chave |  |
| `CONCILIADO` | Texto | Conciliado |  |
| `AD_CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `INDESTORNADO` | Texto | Estorno |  |
| `CODRASTROESTORNO` | Inteiro | Cod. Rastreamento Estorno |  |
| `CHAVRATROESTORNO` | Texto | Chave de Rastreamento do Estorno |  |

**Opções `CONCILIADO`:** `N`=Não, `S`=Sim

**Opções `EXTEMPORANEO`:** `S`=Sim, `N`=Não

**Opções `INDESTORNADO`:** `A`=Estorno e foi estornado, `F`=Foi estornado, `N`=Não e um estorno, `S`=E um estorno

**Opções `LIBERADO`:** `S`=Sim, `N`=Não

**Opções `PARTLALUR_A`:** `S`=Sim, `N`=Não

### TCBHIS
**Historico**

**PK:** `CODHISTCTB`  
**Referenciada por:** 5 tabelas  
**entityName:** `HistoricoPadrao`, `HistoricoPadrao2`, `HistoricoPadraoCredito`, `HistoricoPadraoDebito`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODHISTCTB` 🔑 | Inteiro | Codigo |  |
| `HISTORICO` | Texto | Descrição |  |

### TCBDMT
**Hierarquia de Demonstrativos**

**PK:** `CODEMP`, `CODTDM`, `CODDMT`  
**Referenciada por:** 3 tabelas  
**entityName:** `HierarquiaDemonstrativo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Codigo Empresa | → `TCBEMP`.`CODEMP` |
| `CODTDM` 🔑 | Inteiro | Cod. Tipo Demonstrativo | → `TCBTDM`.`CODTDM` |
| `CODDMT` 🔑 | Texto | Codigo |  |
| `DESCRDMT` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `CODDMTPAI` | Texto | Codigo Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `SITUACAO` | Texto | Situação |  |
| `INDGRUBAL` | Texto | Grupo Balanco |  |
| `AGRUPDLPA` | Texto | Agrupamento p/ DLPA |  |
| `GRUPODEMONST` | Texto | Grupo p/ Demonstrativo |  |
| `GERADRA` | Texto | Gera DRA |  |
| `INVERTVLRALT` | Texto | Inverter valor automatico |  |
| `GRUPDEMONSDFC` | Texto | Grupo p/ Demonstrativo |  |
| `SITDFC` | Texto | Situação |  |
| `INDGRPDRE` | Texto | Indicador de grupo da DRE |  |
| `NUORDEM` | Inteiro | Numero da Ordem |  |
| `INDDCCTAINI` | Texto | Classificação do Saldo Inicial |  |
| `INDDCCTAFIN` | Texto | Classificação do Saldo Final |  |

**Opções `AGRUPDLPA`:** `S`=Sim, `N`=Não

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `GERADRA`:** `S`=Sim, `N`=Não

**Opções `GRUPDEMONSDFC`:** `1`=Atividades Operacionais, `2`=Atividades De Investimento, `3`=Atividades De Financiamento, `5`=Outras Atividades, `4`=Totalizador das Atividades Principais

### TCBGRU
**Grupo dos demonstrativos**

**PK:** `CODEMP`, `CODGRUPOCTA`  
**Referenciada por:** 2 tabelas  
**entityName:** `GrupoDemonstrativo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOCTA` 🔑 | Inteiro | Cod.Grupo |  |
| `DESCRGRUPOCTA` | Texto | Descrição |  |
| `DESCRACUM` | Texto | Descrição do acumulado |  |
| `CODDEMONST` | Inteiro | Cod.Demonstrativo | → `TCBDEM`.`CODDEMONST` |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TCBDEM`.`CODEMP` |

### TCBFCT
**Fato Contabil**

**PK:** `CODEMP`, `CODFATOCONTB`  
**Referenciada por:** 2 tabelas  
**entityName:** `FatoContabil`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Codigo Empresa | → `TSIEMP`.`CODEMP` |
| `CODFATOCONTB` 🔑 | Texto | Codigo Fato Contabil |  |
| `DESCFATCONTB` | Texto | Desc. Fato Contabil |  |
| `SITUACAO` | Texto | Situação |  |
| `TIPOFATO` | Texto | Tipo |  |

**Opções `SITUACAO`:** `T`=Subtotal ou total, `A`=Automatico

**Opções `TIPOFATO`:** `N`=Normal, `I`=Saldo inicial, `F`=Saldo final

### TCBCRP
**Cabecalho Relatorios Personalizados**

**PK:** `NUPERIODOCTB`, `TABELA`  
**Referenciada por:** 2 tabelas  
**entityName:** `CabRelatoriosPersonalizados`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPERIODOCTB` 🔑 | Inteiro | Nro periodo contabil | → `TCBPCT`.`NUPERIODOCTB` |
| `CODUSU` | Inteiro | Codigo Usuario |  |
| `DHALTER` | Data/Hora | Dh. alteração |  |
| `TABELA` 🔑 | Inteiro | Tabela |  |

**Opções `TABELA`:** `1`=AtivoImobilizado, `2`=AtivoIntangivel, `3`=Bens, `4`=CaixaEquivalentesDeCaixa, `5`=ClientesContasReceber, `6`=CustoServicosVendidos, `7`=EmprestimosFinanciamentos, `8`=ImpostosRendaContribuicao, `9`=ImpostosContribuicoes, `10`=MovimentacaoContingencia, `11`=ReceitasOperacionais, `12`=ReceitaLiquida

### TCBECF
**Configurador de Blocos e Registros**

**PK:** `CODEMP`, `BLOCO`, `REGISTRO`, `CODIGO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod. Empresa |  |
| `BLOCO` 🔑 | Texto | Bloco |  |
| `REGISTRO` 🔑 | Inteiro | Registro |  |
| `CODIGO` 🔑 | Texto | Codigo |  |
| `TIPO` | Texto | Tipo de Dados |  |
| `ATIVO` | Texto | Ativo |  |
| `PERMVLRZERADO` | Texto | Permite gerar registro com valor zerado |  |
| `ARQUIVOSKW` | Texto | Arquivo |  |
| `CMDSQL` | Texto | SQL |  |
| `VALOR` | Decimal | Valor |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `TABELA` | Texto | Tabela |  |
| `DTALTER` | Data/Hora | Dt. Alteração |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `BLOCO`:** `V`=V, `Q`=Q, `W`=W, `Y`=Y, `X`=X, `U`=U, `T`=T, `P`=P, `N`=N

**Opções `PERMVLRZERADO`:** `S`=Sim, `N`=Não

**Opções `TIPO`:** `P`=P - Plano de contas, `S`=S - Comando sql, `V`=V - Valor, `A`=A - Arquivo texto

### TCBLUCPRES
**Apuração do Regime Normal - Lucro Presumido**

**PK:** `CODEMP`, `DTREF`, `TRIMESTRE`  
**Referenciada por:** 3 tabelas  
**entityName:** `ApuracaoLucroPresumido`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Inteiro | Referencia |  |
| `TRIMESTRE` 🔑 | Texto | Trimestre |  |
| `TIPDATA` | Texto | Tipo de Data |  |
| `DTINI` | Data | Data Inicio |  |
| `DTFIM` | Data | Data Fim |  |
| `STATUSAPUR` | Texto | Status Apuração |  |
| `JSONCSLL` | C | JsonCsll |  |
| `JSONIRPJ` | C | JsonIrpj |  |

**Opções `STATUSAPUR`:** `null`=Aberto, `P`=Processado, `F`=Fechado

**Opções `TIPDATA`:** `null`=Data Entrada e Saida, `M`=Data de Movimento, `N`=Data de Negociação

**Opções `TRIMESTRE`:** `1`=1 Trimestre, `2`=2 Trimestre, `3`=3 Trimestre, `4`=4 Trimestre
