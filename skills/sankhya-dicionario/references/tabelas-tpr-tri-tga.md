# Tabelas TPR (Produção), TRI (REINF) e TGA (Agronegócio)

TPR* — Manufatura e Produção.
TRI* — EFD-REINF (obrigações fiscais).
TGA* — Agronegócio: pesagem, safra, classificação de produto.

## TPR — Produção / Manufatura

### TPRPRC
**Metainformações sobre um processo produtivo.**

**Referenciada por:** 13 tabelas  
**entityName:** `ProcessoProdutivo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDPROC` | Inteiro | Numero Unico |  |
| `VALIDAVERSAO` | Texto | VALIDAVERSAO |  |
| `CODPRC` | Inteiro | Codigo |  |
| `TIPOPROC` | Texto | Tipo de Processo |  |
| `DESCRLONGA` | Texto | Descrição Completa |  |
| `DESCRABREV` | Texto | Descrição |  |
| `VERSAOANT` | Inteiro | Versão Anterior |  |
| `VERSAO` | Inteiro | Versão |  |
| `IDRPAINICIAL` | Inteiro | Repositorio Inicial |  |
| `CODPLP` | Inteiro | Planta de Manufatura |  |
| `CODLOCALALMOXARIFE` | Inteiro | Local de Almoxarifado |  |
| `CODLOCALMANUFATURA` | Inteiro | Local de Manufatura |  |
| `MULTIPA` | Texto | Aceita Multiplos PAs |  |
| `MULTICONTROLE` | Texto | Aceita Multiplos Controles de PA |  |
| `TIPOINICIA` | Texto | Tipo de inicialização |  |
| `DHCAD` | Data/Hora | Data e Hora Inclusão |  |
| `DHALTER` | Data/Hora | Data e Hora Alteração |  |
| `CODUSUCAD` | Inteiro | Usuario Resp. Cadastro |  |
| `CODUSUALT` | Inteiro | Usuario Ultima Alteração |  |
| `XMLBPMN` | C | XMLBPMN |  |
| `XMLBPMNUI` | C | XMLBPMNUI |  |
| `IDWFLOW` | Texto | IDWFLOW |  |
| `ATIVO` | Texto | Ativo |  |
| `TIPONROLOTE` | Texto | Tipo do Nro. Lote |  |
| `MASCNROLOTE` | Texto | Mascara Nro. Lote |  |
| `PRODPARATERCEIRO` | Texto | Produção para Terceiro |  |
| `PROCDESMONTE` | Texto | Desmonte |  |
| `PROCREPARO` | Texto | Reprocessamento/reparo |  |
| `CODPRCPRODUCAO` | Inteiro | Processo de Produção Relacionado |  |
| `TIPOFRAGNROLOTE` | Texto | Reiniciar numeração |  |
| `USATERCEIRO` | Texto | Produção terceirizada |  |
| `DEFTERCEIRO` | Texto | Definição de Terceiro |  |
| `EXIGEPEDIDO` | Texto | Exige pedido de venda |  |
| `PADRAO` | Texto | Padrão |  |
| `PERCDESVIOINF` | Decimal | % Desvio Inferior |  |
| `LOTECURINGA` | Texto | Lote Curinga |  |
| `LIBERADESVIO` | Texto | Solicitar liberação ao exceder desvio |  |
| `PERCDESVIOSUP` | Decimal | % Desvio Superior |  |
| `USALOTECURINGA` | Texto | Usa Lote Curinga |  |
| `IDFORMULA` | Inteiro | Formula p/ Ajuste Tamanho de Lote |  |
| `ROTEIROHTML5` | Texto | Editado em HTML5 |  |
| `USACONFNROLOTESP` | Texto | Utilizar essa configuração para Subproduto |  |
| `TIPONROLOTESP` | Texto | Tipo do Nro. Lote |  |
| `MASCNROLOTESP` | Texto | Mascara Nro. Lote |  |
| `TIPOFRAGNROLOTESP` | Texto | Reiniciar numeração |  |
| `TIPEXECATV` | Texto | Tipo de Execução das Atividades |  |
| `PEREDICAO` | Texto | Periodo permitido para realizar a edição |  |
| `PADRAOPRODUTO` | Texto | Padrão por Produto |  |
| `QTDDIAS` | Inteiro | Qtd. Dias |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `DEFTERCEIRO`:** `A`=Por Operação, `O`=Por OP

**Opções `EXIGEPEDIDO`:** `S`=Sempre, `N`=Nunca, `O`=Opcional

**Opções `LIBERADESVIO`:** `N`=Não, `S`=Sim

**Opções `MULTICONTROLE`:** `S`=Sim, `N`=Não

### TPRWCP
**Work Center de produção**

**PK:** `CODWCP`  
**Referenciada por:** 13 tabelas  
**entityName:** `WorkCenter`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `QTDALOCADA` | Inteiro | Quantidade de Alocações |  |
| `DISPONIBILIDADE` | Texto | Disponibilidade |  |
| `CODWCP` 🔑 | Inteiro | Codigo |  |
| `CODCWC` | Inteiro | Categoria | → `TPRCWC`.`CODCWC` |
| `NOME` | Texto | Descrição |  |
| `CODPLP` | Inteiro | Planta | → `TPRPLP`.`CODPLP` |
| `CODCAP` | Inteiro | Capacidade | → `TPRCAP`.`CODCAP` |
| `QTDCAPACIDADEMIN` | Decimal | Capacidade Minima |  |
| `QTDCAPACIDADEPAD` | Decimal | Capacidade Padrão |  |
| `QTDCAPACIDADEMAX` | Decimal | Capacidade Maxima |  |
| `QTDCARGAMIN` | Decimal | Carga Minima |  |
| `CAPACIDADEHORA` | Decimal | Capacidade por Hora |  |
| `QTDCARGAMAX` | Decimal | Carga Maxima |  |
| `CODVOL` | Texto | Unidade |  |
| `RESTRINGECARGA` | Texto | Restringir uso pela Capacidade de Carga |  |
| `CODUSURESP` | Inteiro | Usuario Responsavel |  |
| `CODCENCUS` | Inteiro | Centro de Resultado |  |
| `CODCARGAHOR` | Inteiro | Carga Horaria |  |
| `TIPOSETUP` | Texto | Tipo de Setup |  |
| `EXIGECLEANUP` | Texto | Exige Cleanup |  |
| `TEMPOSETUP` | Inteiro | Tempo Padrão de Setup |  |
| `TEMPOCLEANUP` | Inteiro | Tempo Padrão de Cleanup |  |
| `INDICEOEE` | Decimal | OEE |  |
| `NOMEIMPRESSORA` | Texto | Nome da Impressora |  |
| `NUMQP` | Inteiro | Maquina Principal | → `TPRMQP`.`CODMQP` |
| `SETUPPRONTO` | Texto | SETUPPRONTO |  |
| `CODLOCALWC` | Inteiro | Local de Estoque |  |
| `OPERACAO` | Texto | Operação |  |

**Opções `EXIGECLEANUP`:** `S`=Sim, `N`=Não

**Opções `OPERACAO`:** `E`=Exclusivo, `C`=Compartilhado

**Opções `RESTRINGECARGA`:** `N`=Não, `S`=Sim

**Opções `TIPOSETUP`:** `S`=Sempre, `C`=Condicional, `N`=Nunca

### TPRATV
**Atividade do processo produtivo**

**PK:** `IDEFX`  
**Referenciada por:** 10 tabelas  
**entityName:** `Atividade`, `ProcessoAtividade`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDEFX` 🔑 | Inteiro | Codigo | → `TPREFX`.`IDEFX` |
| `OPERCQ` | Texto | Operação a ser realizada |  |
| `SUBAPOPORCONF` | Texto | Tipo de Apontamento |  |
| `IDRPADEST` | Inteiro | Repositorio de destino | → `TPRRPA`.`IDRPA` |
| `DATAHORAAPONTAMENTO` | Texto | Data/Hora de Apontamento |  |
| `IDRPAOPER` | Inteiro | Repositorio da operação | → `TPRRPA`.`IDRPA` |
| `IDAWC` | Inteiro | Alocação de C. Trabalho |  |
| `PERMITEPARCIAL` | Texto | Permite fluxo parcial |  |
| `TIPOTEMPO` | Texto | Tipo de tempo |  |
| `TEMPOATIVIDADE` | Decimal | Tempo da atividade |  |
| `UNTEMPO` | Texto | Unidade de tempo |  |
| `QTDBASEAPON` | Texto | Quantidade base para apontamento |  |
| `APONTAMP` | Texto | Aponta materia-prima |  |
| `APONTAPA` | Texto | Exige apontamento de PA |  |
| `APONTACOMP` | Texto | Aponta componente de manufatura |  |
| `APONTASP` | Texto | Aponta subproduto |  |
| `PERMITENOVOPA` | Texto | Apontar PA diferente em relação ao inicio do processo |  |
| `PROIBEAPONT` | Texto | Proibir apontamento a maior |  |
| `TIPOREPROCESSO` | Texto | Tipo de reprocesso |  |
| `ALTSTATUSPROC` | Texto | Status do processo |  |
| `CODUSULOGON` | Inteiro | Usuario para logon |  |
| `LISTAMPPADRAO` | Texto | Lista de materia-prima padrão |  |
| `LIBERARWCFINAL` | Texto | Libera centro de trabalho no final da atividade |  |
| `LIBERARWCMANUAL` | Texto | Libera centro de trabalho manualmente |  |
| `INICIALIZARPA` | Texto | Inicializa repositorio de produtos acabados |  |
| `CODPRCSUB` | Inteiro | Subprocesso | → `TPRPRC`.`IDPROC` |
| `IDCCQ` | Inteiro | Ciclo controle de qualidade | → `TPRCCQ`.`IDCCQ` |
| `VALIDACQ` | Texto | Validar ciclo de controle de qualidade |  |
| `IDPROC` | Inteiro | IDPROC | → `TPRPRC`.`IDPROC` |
| `EXECTERCEIRO` | Texto | Execução Terceirizada |  |
| `CONCLUICQ` | Texto | Conclui Ciclo de Controle de Qualidade |  |
| `CONTCUMULATIVA` | Texto | Contagem Cumulativa |  |
| `TIPOCONFERENCIA` | Texto | Tipo de Conferencia |  |
| `QTDCONFIGUAIS` | Inteiro | Qtd. de conferencias iguais |  |
| `QTDRECONTAGENS` | Inteiro | Qtd. de recontagens |  |
| `USASEQCODBAR` | Texto | Usar seq. lote no cod. barras |  |
| `SEPSEQCODBAR` | Texto | Separador |  |
| `APONTARECWC` | Texto | Aponta Recursos do Centro de Trabalho |  |
| `MULTITURNO` | Texto | Multi-turno |  |
| `CODMTPFINTURNO` | Inteiro | Motivo de parada (fim de turno) | → `TPRMTP`.`CODMTP` |
| `SETUP` | Texto | Considerar atividades de Setup no OEE |  |
| `PERMITEPERDATOTAL` | Texto | Permitir apontamento de 100% de perda |  |
| `PERMITEALTLOCMP` | Texto | Permite alterar local de baixa da MP |  |
| `DESCRICAO` | Texto | Descrição |  |
| `SEQEXECUCAO` | Texto | Sequencia de Execução |  |
| `GERAMLAUDO` | Texto | Gerar registro de Amostra e Laudo. |  |
| `APROVARSTATUSLOTE` | Texto | Aprova/Reprova 'Status do Lote' no Final do Ciclo |  |

**Opções `ALTSTATUSPROC`:** `M`=Mantem o status atual, `S`=Suspenso, `A`=Em andamento, `C`=Cancelado

**Opções `APONTACOMP`:** `N`=Não, `S`=Sim

**Opções `APONTAMP`:** `N`=Não aponta MP, `O`=Aponta as MPs da OP, `A`=Aponta as MPs da Atividade

**Opções `APONTAPA`:** `S`=Sim, `N`=Não

**Opções `APONTARECWC`:** `O`=Aponta os Recursos de CT da OP, `N`=Não aponta, `A`=Aponta os Recursos de CT da Atividade

### TPREFX
**Elemento Basico de fluxo**

**PK:** `IDEFX`  
**Referenciada por:** 13 tabelas  
**entityName:** `ElementoFluxo`, `ElementoFluxo2`, `ElementoFluxoDestino`, `ElementoFluxoOrigem`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDEFX` 🔑 | Inteiro | Codigo |  |
| `IDPROC` | Inteiro | Processo | → `TPRPRC`.`IDPROC` |
| `TIPO` | Inteiro | Tipo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `X1POS` | Decimal | X1POS |  |
| `Y1POS` | Decimal | Y1POS |  |
| `X2POS` | Decimal | X2POS |  |
| `Y2POS` | Decimal | Y2POS |  |
| `CORPREENCHIMENTO` | Texto | CORPREENCHIMENTO |  |
| `TAMFONTE` | Inteiro | TAMFONTE |  |
| `CORFONTE` | Texto | CORFONTE |  |
| `IDEFXLANE` | Inteiro | IDEFXLANE | → `TPRLND`.`IDEFX` |
| `WAYPOINTS` | C | WAYPOINTS |  |

### TPRIATV
**Mantem dados sobre uma instancia de atividade de usuario.**

**PK:** `IDIATV`  
**Referenciada por:** 8 tabelas  
**entityName:** `InstanciaAtividade`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDIPROC` | Inteiro | Nro. OP | → `TPRIPROC`.`IDIPROC` |
| `SITUACAO` | Texto | Situação |  |
| `STATUSINSTCICLOCONTQUAL` | Texto | Status Instancia Ciclo Controle de Qualidade |  |
| `DESCRGRUPOPRODPA` | Texto | Descr. Grupo do Produto |  |
| `DESCRPRODPA` | Texto | Descrição do Produto |  |
| `REFERENCIA` | Texto | Referencia do Produto |  |
| `IDIATV` 🔑 | Inteiro | Codigo |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `NROLOTE` | Texto | Nro. Lote |  |
| `CODPRODPA` | Inteiro | Cod. Produto |  |
| `CONTROLEPA` | Texto | Controle |  |
| `CODGRUPOPRODPA` | Inteiro | Grupo do Produto |  |
| `COMPLDESCPA` | Texto | Complemento do Produto |  |
| `CODVOLPA` | Texto | Un. Lote |  |
| `QTDPRODUZIR` | Decimal | Tam. Lote |  |
| `MULTIPRODUTO` | Texto | Multi-produto |  |
| `DHINCLUSAO` | Data/Hora | Dh. Entrada Atividade |  |
| `DHACEITE` | Data/Hora | Dh. Aceite Atividade |  |
| `CODPARCTERC` | Inteiro | Cod. Parceiro Terceiro | → `TGFPAR`.`CODPARC` |
| `DHINICIO` | Data/Hora | Dh. Inicio Atividade |  |
| `CODUSU` | Inteiro | Cod. Usuario Inicial | → `TSIUSU`.`CODUSU` |
| `DHFINAL` | Data/Hora | Dh. Fim Atividade |  |
| `DHINIPREV` | Data/Hora | Dt./Hr. Inicio Prev. |  |
| `DHFINPREV` | Data/Hora | Dt./Hr. Final Prev. |  |
| `IDEFX` | Inteiro | Atividade | → `TPRATV`.`IDEFX` |
| `CODWCP` | Inteiro | Centro de Trabalho | → `TPRWCP`.`CODWCP` |
| `IDEXECWFLOW` | Texto | Token |  |
| `CODEXEC` | Inteiro | Executante |  |
| `TEMPOGASTOMIN` | Inteiro | Tempo Gasto em Minutos |  |
| `CODUSUFIN` | Inteiro | Cod. Usuario Final | → `TSIUSU`.`CODUSU` |
| `CODULTEXEC` | Inteiro | Ultimo Executante | → `TSIUSU`.`CODUSU` |
| `CODMTP` | Inteiro | Motivo Parada | → `TPRMTP`.`CODMTP` |

**Opções `MULTIPRODUTO`:** `N`=Não, `S`=Sim

**Opções `SITUACAO`:** `I`=Iniciada, `F`=Finalizada, `G`=Aguardando aceite, `P`=Parada, `A`=Aceita

**Opções `STATUSINSTCICLOCONTQUAL`:** `R`=Reprovado, `E`=Aprovado com Ressalvas, `P`=Em Andamento, `A`=Aprovado, `I`=Não Iniciado

### TPRAPA
**Apontamento de PA**

**PK:** `NUAPO`, `SEQAPA`  
**Referenciada por:** 10 tabelas  
**entityName:** `ApontamentoPA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAPO` 🔑 | Inteiro | Nro. unico | → `TPRAPO`.`NUAPO` |
| `SEQAPA` 🔑 | Inteiro | Sequencia |  |
| `CODPRODPA` | Inteiro | Cod. Produto (PA) |  |
| `REFERENCIA` | Texto | Referencia do Produto |  |
| `CONTROLEPA` | Texto | Controle (PA) |  |
| `QTDAPONTADA` | Decimal | Qtd. apontada |  |
| `QTDPERDA` | Decimal | Qtd. Total de Perda |  |
| `QTDFAT` | Decimal | Qtd. Baixada (PA) |  |
| `QTDFATSP` | Decimal | Qtd. Baixada (SP) |  |
| `QTDMPE` | Inteiro | Qtd. de Motivos de Perda |  |
| `CODMPE` | Inteiro | Motivo de perda |  |

### TPRILOP
**Item de lancamento de OP**

**PK:** `NULOP`, `SEQOP`  
**Referenciada por:** 8 tabelas  
**entityName:** `ItemDeLancamentoDeOP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NULOP` 🔑 | Inteiro | NULOP | → `TPRLOP`.`NULOP` |
| `SEQOP` 🔑 | Inteiro | Sequencia |  |
| `SEQCOP` | Inteiro | Seq. Produção Conjunta |  |
| `CODPLP` | Inteiro | Cod. Planta | → `TPRPLP`.`CODPLP` |
| `TIPOOP` | Texto | Tipo de Ordem |  |
| `ORDEM` | Inteiro | ORDEM |  |
| `COMPARTILHA` | Texto | COMPARTILHA |  |
| `IDPROC` | Inteiro | IDPROC | → `TPRPRC`.`IDPROC` |
| `NUNOTA` | Inteiro | Nro. Pedido |  |
| `SEQNOTA` | Inteiro | Sequencia do Item |  |
| `TEMPOATRAVESS` | Decimal | Tempo de Atravessamento (min) |  |
| `CODPROD` | Inteiro | Cod.Produto |  |
| `CODPARCTERC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `DESCRPROD` | Texto | Produto Acabado |  |
| `REFERENCIA` | Texto | Referencia do Produto |  |
| `TAMLOTE` | Decimal | Tam.Lote |  |
| `DTINICIOMAX` | Data/Hora | Dh. Inicialização (max) |  |
| `DTPREVENT` | Data/Hora | Previsão de Entrega |  |
| `QTDPA` | Inteiro | Qtd. Produtos |  |
| `CONTROLE` | Texto | Controle |  |

**Opções `COMPARTILHA`:** `S`=Sim, `N`=Não

**Opções `TIPOOP`:** `P`=Produção, `D`=Desmonte, `PC`=Produção Conjunta, `R`=Reprocessamento/Reparo

### TPRPLOP
**Produtos para lancamento de OP**

**Referenciada por:** 8 tabelas  
**entityName:** `ProdutoLancamentoDeOP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NULOP` | Inteiro | Lancamento |  |
| `SEQOP` | Inteiro | Sequencia |  |
| `CODFORMULA` | Inteiro | Cod.Formula |  |
| `CODPRODPA` | Inteiro | Cod.Produto |  |
| `CONTROLEPA` | Texto | Controle |  |
| `ESTOQUE` | Decimal | Qtd.Estoque |  |
| `NROLOTE` | Texto | Nro. Lote |  |
| `CALCTAMLOTE` | Decimal | Tam. Lote Ajustado |  |
| `TAMLOTE` | Decimal | Tam. Lote |  |
| `MULTLOTE` | Decimal | Multiplo de Lote |  |
| `MINLOTE` | Decimal | Lote Minimo |  |
| `TAMLOTEPAD` | Decimal | TAMLOTEPAD |  |
| `TIPOGERASERIE` | Texto | TIPOGERASERIE |  |
| `EDITADO` | Texto | EDITADO |  |
| `QTDPRODMIN` | Decimal | Qtd. Minima |  |

**Opções `EDITADO`:** `S`=Sim, `N`=Não

### TPRPLP
**Planta de manufatura**

**Referenciada por:** 7 tabelas  
**entityName:** `PlantaManufatura`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPLP` | Inteiro | Cod. Planta |  |
| `NOME` | Texto | Nome |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODCARGAHOR` | Inteiro | Carga Horaria Padrão |  |
| `CODCENCUS` | Inteiro | Centro de Resultado |  |

### TPRMPS
**Plano Mestre de produção**

**PK:** `NUMPS`  
**Referenciada por:** 6 tabelas  
**entityName:** `PlanoMestreProducao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMPS` 🔑 | Inteiro | Codigo |  |
| `CODCMPS` | Inteiro | Configuração MPS | → `TPRCMPS`.`CODCMPS` |
| `DHGERMRP` | Data/Hora | Dh. Geração MRP |  |
| `CODPLANTA` | Inteiro | Planta de Manufatura | → `TPRPLP`.`CODPLP` |
| `DESCRICAO` | Texto | Descrição |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | Dh. Alteração |  |
| `DTINICMPS` | Data/Hora | Periodo MPS |  |
| `DTFINMPS` | Data/Hora | Periodo MPS |  |
| `DTINIPED` | Data/Hora | Periodo dos pedidos |  |
| `DTFINPED` | Data/Hora | Periodo dos pedidos |  |
| `SITUACAO` | Texto | Situação |  |
| `PERCAJUSTEDEM` | Decimal | % Ajuste Demanda |  |
| `OBSERVACOES` | Texto | Observações |  |

**Opções `SITUACAO`:** `P`=Pendente, `C`=Confirmado

### TPRLPA
**Produto Acabado**

**PK:** `IDPROC`, `CODPRODPA`, `CONTROLEPA`  
**Referenciada por:** 6 tabelas  
**entityName:** `ProdutoAcabado`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDPROC` 🔑 | Inteiro | Cod. Composição | → `TPRPRC`.`IDPROC` |
| `VALIDAVERSAO` | Texto | VALIDAVERSAO |  |
| `CODPRODPA` 🔑 | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `REFERENCIA` | Texto | Referencia do Produto |  |
| `TAMLOTEPAD` | Decimal | Tamanho de Lote Padrão |  |
| `CONTROLEPA` 🔑 | Texto | Controle |  |
| `MULTIDEAL` | Decimal | Multiplo Ideal |  |
| `QTDPRODMIN` | Decimal | Qtd. Minima |  |
| `TIPOTEMPO` | Texto | Tipo de Tempo |  |
| `TEMPOATRAVESS` | Decimal | Tempo de Atravessamento |  |
| `TEMPOFIXO` | Decimal | Tempo de Atravessamento (parte fixa) |  |
| `UNTEMPOATRAVESS` | Texto | Un. Tempo |  |
| `BASCALCDTVAL` | Texto | Base para calculo da Dt.Validade |  |
| `TIPOGERASERIE` | Texto | Tipo de geração do Nro. de Serie |  |
| `MASCSERIE` | Texto | Mascara do Nro. Serie |  |
| `CODLOCDEST` | Inteiro | Local de Destino |  |
| `IDFORMULA` | Inteiro | Formula p/ Ajuste Tamanho de Lote | → `TPRFTL`.`IDFORMULA` |
| `DHALTER` | Data/Hora | Data e Hora Alteração |  |
| `DHCAD` | Data/Hora | Data e Hora Inclusão |  |
| `CODUSUALT` | Inteiro | Usuario Ultima Alteração |  |
| `CODUSUCAD` | Inteiro | Usuario Resp. Cadastro |  |

**Opções `BASCALCDTVAL`:** `M`=Menor Dt.Validade das MPs, `I`=Data de inicialização da OP, `F`=Data da primeira nota de produção do lote, `N`=Não calcula

**Opções `TIPOGERASERIE`:** `L`=Manual (lancamento), `P`=Manual (apontamento), `A`=Automatica, `G`=Automatico (Serie Global)

**Opções `TIPOTEMPO`:** `Q`=Por Quantidade, `L`=Por Lote

**Opções `UNTEMPOATRAVESS`:** `H`=Horas, `D`=Dias, `M`=Minutos

**Opções `VALIDAVERSAO`:** `N`=Não, `S`=Sim

### TPRIPROC
**Manter dados de tempo de execução de uma ordem**

**PK:** `IDIPROC`  
**Referenciada por:** 16 tabelas  
**entityName:** `CabecalhoInstanciaProcesso`, `CabecalhoInstanciaSubProcesso`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `PERIODOMPS` | Texto | Periodo MPS |  |
| `IDIPROC` 🔑 | Inteiro | Nro. OP |  |
| `DECQTD` | Inteiro | Qtd. Casas Decimais |  |
| `NROLOTE` | Texto | Nro. Lote |  |
| `QTDPRODUZIR` | Decimal | Tam. Lote |  |
| `SALDOOP` | Decimal | Saldo a Produzir |  |
| `STATUSPROC` | Texto | Status |  |
| `CODPRODPA` | Inteiro | Cod. Produto |  |
| `REFERENCIA` | Texto | Referencia do Produto |  |
| `DESCRPRODPA` | Texto | Descr. Produto |  |
| `CONTROLEPA` | Texto | Controle |  |
| `COMPLDESCPA` | Texto | Compl. Produto |  |
| `DHINC` | Data/Hora | Dh. Inclusão |  |
| `DHINST` | Data/Hora | Dh. Inicialização |  |
| `DHTERMINO` | Data/Hora | Dh. Finalização |  |
| `DESCRICAO` | Texto | Operação Atual |  |
| `CODPARCTERC` | Inteiro | Parceiro Terceiro | → `TGFPAR`.`CODPARC` |
| `DTPREVENT` | Data/Hora | Previsão de Entrega |  |
| `TEMPOATRAVESS` | Decimal | Tempo de Atravessamento (min) |  |
| `DTINICIOMAX` | Data/Hora | Dh. Inicialização (max) |  |
| `NUNOTA` | Inteiro | Nro. Pedido |  |
| `CODUSUFINAL` | Inteiro | Usuario Finalizante |  |
| `CODEXEC` | Inteiro | Executante Atual |  |
| `NUMPS` | Inteiro | NUMPS | → `TPRMPS`.`NUMPS` |
| `SEQNOTA` | Inteiro | Sequencia do Item Nota/Pedido |  |
| `NOMEEXEC` | Texto | Nome do Exec. |  |
| `NOMERPA` | Texto | Fase do processo |  |
| `IDICOP` | Inteiro | Nro. OP Conjunta |  |
| `QTDRPA` | Decimal | Qtd. na Fase |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `IDPROC` | Inteiro | Processo | → `TPRPRC`.`IDPROC` |
| `MULTIPRODUTO` | Texto | Multi-produtos |  |
| `CODPLP` | Inteiro | Planta | → `TPRPLP`.`CODPLP` |
| `CODPARC` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `IDWFLOW` | Texto | Codigo do Workflow |  |
| `CODUSUINC` | Inteiro | Usuario |  |
| `IDIPROCPAI` | Inteiro | Nro. OP Principal | → `TPRIPROC`.`IDIPROC` |
| `CODGRUPOPRODPA` | Inteiro | Grupo do Produto (PA) |  |

**Opções `MULTIPRODUTO`:** `N`=Não, `S`=Sim

**Opções `STATUSPROC`:** `S`=Suspenso, `C`=Cancelado, `A`=Em andamento, `S2`=Suspendendo, `P`=Em programação, `P2`=Programado, `AP`=Aguardando programação, `F`=Finalizado, `C2`=Cancelando, `R`=Criado

### TPRCRE
**Categoria de recursos de work center**

**PK:** `CODCRE`  
**Referenciada por:** 7 tabelas  
**entityName:** `CategoriaRecurso`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCRE` 🔑 | Inteiro | Codigo |  |
| `CODCREPAI` | Inteiro | Cod. Recurso Pai |  |
| `NOME` | Texto | Nome |  |
| `TIPO` | Texto | Tipo |  |
| `CODSERVAPONTA` | Inteiro | Servico |  |
| `TIPOAPONTAUSO` | Texto | Tipo Apontamento |  |
| `GRAU` | Inteiro | Grau |  |
| `PARAMSETUP` | Texto | Parametro de Setup |  |
| `ANALITICO` | Texto | Analitico |  |
| `ATIVO` | Texto | Ativo |  |
| `CODVOL` | Texto | Unidade apontamento |  |
| `DECQTD` | Inteiro | Qtd. decimais |  |

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `PARAMSETUP`:** `N`=Não, `S`=Obrigatorio, `O`=Opcional

**Opções `TIPO`:** `M`=Maquina, `E`=Equipamento, `O`=Mão de obra

**Opções `TIPOAPONTAUSO`:** `N`=Não aponta, `M`=Apontamento manual

### TPRARW
**Apontamento Recursos de Work Center**

**PK:** `NUAPO`, `SEQAPA`, `CODWCP`, `CODCRE`  
**Referenciada por:** 4 tabelas  
**entityName:** `ApontamentoRecursosWorkCenter`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `QTDITENSREC` | Inteiro | Qtd. itens Recursos |  |
| `NUAPO` 🔑 | Inteiro | NUAPO | → `TPRAPA`.`NUAPO` |
| `SEQAPA` 🔑 | Inteiro | SEQAPA | → `TPRAPA`.`SEQAPA` |
| `CODWCP` 🔑 | Inteiro | Centro de Trabalho |  |
| `CODCRE` 🔑 | Inteiro | Categoria de Recurso |  |
| `CODVOL` | Texto | Unidade |  |
| `QTDAPONTADA` | Decimal | Qtd. apontada |  |
| `QTDRECAPONTAR` | Inteiro | QTDRECAPONTAR |  |
| `QTDUTILIZADA` | Decimal | Qtd. utilizada (total) |  |

## TRI — EFD-REINF

### TRICAB
**Cabecalho do Reinf**

**PK:** `CODEMP`, `DTREF`, `TPAMB`  
**Referenciada por:** 51 tabelas  
**entityName:** `CabecalhoReinf`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data | Data de Referencia |  |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente |  |
| `VERSAOLAYOUT` | Inteiro | Versão do layout |  |
| `SEQUENCIAATUAL` | Inteiro | Sequencia Atual de Geração Grupo 2000 |  |
| `STATUS` | Inteiro | Status da Referencia Grupo 2000 |  |
| `CONTROLE` | Texto | Controle de Alteração |  |
| `SEQUENCIAATUAL4000` | Inteiro | Sequencia Atual de Geração Grupo 4000 |  |
| `EVTTOTAIS` | Inteiro | Total de Eventos |  |
| `EVTPENDENTE` | Inteiro | Eventos Pendentes |  |
| `STATUS_GRUPO4000` | Inteiro | Status da Referencia Grupo 4000 |  |
| `EVTENVIADO` | Inteiro | Eventos Enviados |  |
| `EVTAGUARCORRECAO` | Inteiro | Eventos Aguard. Correção |  |
| `EVTERROEVTPRIOR` | Inteiro | Eventos c/ Erro em Evento Prioritario |  |
| `EVTFINALIZADO` | Inteiro | Eventos Finalizados |  |

### TRIRES
**Resumo Por Referencia**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`  
**Referenciada por:** 44 tabelas  
**entityName:** `ResumoPorReferencia`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TRICAB`.`CODEMP` |
| `DTREF` 🔑 | Data | Dt. Referencia | → `TRICAB`.`DTREF` |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente | → `TRICAB`.`TPAMB` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSC` | Inteiro | Tipo de Inscrição |  |
| `NRINSC` | Texto | Nro. da Inscrição |  |
| `DHPROCESS` | Data/Hora | Dh. Processamento |  |
| `IDEV` | Texto | ID do Evento |  |
| `NRRECARQBASE` | Texto | Nro. do Recibo |  |
| `INDEXISTINFO` | Inteiro | Ind. de Existencia de Valores de Bases |  |

### TRIPRISET
**Processos Reinf Por Informações de Suspensão de Exibilidade de Tributos**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`, `NUPROCESSO`, `SEQPRISET`  
**Referenciada por:** 63 tabelas  
**entityName:** `ProcReinfInfoSuspExigibTributo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TRIPAJR`.`CODEMP` |
| `DTREF` 🔑 | Data | Dt. Referencia | → `TRIPAJR`.`DTREF` |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente | → `TRIPAJR`.`TPAMB` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia | → `TRIPAJR`.`SEQUENCIA` |
| `CHAVE` 🔑 | Texto | Chave | → `TRIPAJR`.`CHAVE` |
| `NUPROCESSO` 🔑 | Inteiro | Nro. Unico do Processo | → `TRIPAJR`.`NUPROCESSO` |
| `SEQPRISET` 🔑 | Inteiro | Sequencia da Suspensão |  |
| `CODSUSP` | Texto | Cod. da Suspensão |  |
| `INDSUSP` | Inteiro | Indicativo de Suspensão |  |
| `DTDECISAO` | Data | Dt. Decisão |  |
| `INDDEPOSITO` | Texto | Deposito Montante Integral |  |
| `INIVALID` | Data | Dt. Inicial da Vigencia |  |
| `FIMVALID` | Data | Dt. Final da Vigencia |  |

### TRIPAJR
**R1070 - Processos Administrativos/Judiciais Reinf**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`, `NUPROCESSO`  
**Referenciada por:** 6 tabelas  
**entityName:** `ProcessoAdmJudicialReinf`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TRICAB`.`CODEMP` |
| `DTREF` 🔑 | Data | Dt. Referencia | → `TRICAB`.`DTREF` |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente | → `TRICAB`.`TPAMB` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `NUPROCESSO` 🔑 | Inteiro | Nro. Unico do Processo |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `STATUSREG` | Texto | Status do Registro |  |
| `TIPO` | Texto | Tipo de Envio |  |
| `IDEVENTO` | Texto | ID do Evento |  |
| `NRORECIBO` | Texto | Nro. do Recibo |  |
| `NRORECIBOANT` | Texto | Nro. do Recibo Anterior |  |
| `CONTROLE` | Texto | Controle de Alteração |  |
| `TPINSC` | Inteiro | Tipo de Inscrição |  |
| `NRINSC` | Texto | Nro. da Inscrição |  |
| `TPPROC` | Inteiro | Tipo do Processo |  |
| `NRPROC` | Texto | Nro. do Processo |  |
| `INIVALID` | Data | Dt. Inicial da Vigencia |  |
| `FIMVALID` | Data | Dt. Final da Vigencia |  |
| `INDAUTORIA` | Inteiro | Indicador da Autoria |  |
| `UFVARA` | Texto | UF da Seção Judiciaria |  |
| `CODMUNIC` | Inteiro | Cod. do Municipio da Seção Judiciaria |  |
| `IDVARA` | Texto | Cod. de Identificação da Vara |  |
| `INIVALIDNOVO` | Data | Dt. Inicial da Nova Vigencia |  |
| `FIMVALIDNOVO` | Data | Dt. Final da Nova Vigencia |  |
| `MSG` | C | Mensagem |  |
| `XMLEVENTO` | C | XML de Envio |  |
| `XMLRETORNO` | C | XML de Retorno |  |
| `DATACHANGE` | C | Dados alterados |  |

### TRIPNI
**R4040 - Pagamentos/creditos a beneficiarios não identificados**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  
**entityName:** `PagCredBeneficiarioNaoIdent`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TRICAB`.`CODEMP` |
| `DTREF` 🔑 | Data | Dt. Referencia | → `TRICAB`.`DTREF` |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente | → `TRICAB`.`TPAMB` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `STATUSREG` | Texto | Status do Registro |  |
| `IDEVENTO` | Texto | ID do Evento |  |
| `NRORECIBO` | Texto | Nro. do Recibo |  |
| `NRORECIBOANT` | Texto | Nro. do Recibo Anterior |  |
| `CONTROLE` | Texto | Controle |  |
| `TPINSC` | Inteiro | Tipo de Inscrição |  |
| `NRINSC` | Texto | Nro. da Inscrição |  |
| `TPINSCESTAB` | Inteiro | Tipo de Inscrição do Estabelecimento |  |
| `NRINSCESTAB` | Texto | Nro. de Inscrição do Estabelecimento |  |
| `CODEMPESTAB` | Inteiro | Empresa do Estabelecimento |  |
| `PROCEMI` | Inteiro | Tipo Aplicativo |  |
| `VERPROC` | Texto | Versão do processo de emissão do evento |  |
| `PERAPUR` | Texto | Ano/Mes Referencia |  |
| `MSG` | C | Mensagem |  |
| `XMLEVENTO` | C | XML de Envio |  |
| `XMLRETORNO` | C | XML de Retorno |  |
| `TIPO` | Texto | Tipo de Envio |  |
| `VLRTOTALLIQ` | Decimal | Vlr. Total liquido do pagamento |  |
| `VLRTOTALBASEIR` | Decimal | Vlr. Total Base Retenção |  |
| `VLRTOTALIR` | Decimal | Vlr. Total Retenção |  |
| `VLRBASECRRET` | Decimal | Base de calculo |  |
| `VLRBASECRSUSPRET` | Decimal | Base de Calculo c/ Exigibilidade Suspensa |  |
| `VLRCRCALCRET` | Decimal | Vlr Tributo retido Calculado RFB |  |
| `VLRCRSUSPCALCRET` | Decimal | Vlr Tributo c/ Exigibilidade Susp Calc RFB |  |
| `DATACHANGE` | C | Dados alterados |  |
| `INDRETIF` | Inteiro | Controle de Alteração |  |

### TRICPPR
**R2050 - Comercialização Produção Produtor Rural**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  
**entityName:** `ComProducaoProdutorRural`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TRICAB`.`CODEMP` |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia | → `TRICAB`.`DTREF` |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente | → `TRICAB`.`TPAMB` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `STATUSREG` | Texto | Status do Registro |  |
| `TIPO` | Texto | Tipo de Envio |  |
| `IDEVENTO` | Texto | ID do Evento |  |
| `NRORECIBO` | Texto | Nro. do Recibo |  |
| `NRORECIBOANT` | Texto | Nro. do Recibo Anterior |  |
| `CONTROLE` | Texto | Controle de Alteração |  |
| `TPINSC` | Inteiro | Tipo de Inscrição |  |
| `NRINSC` | Texto | Nro. da Inscrição |  |
| `TPINSCESTAB` | Inteiro | Tipo de Inscrição do Estabelecimento |  |
| `NRINSCESTAB` | Texto | Nro. da Inscrição do Estabelecimento |  |
| `CODEMPESTAB` | Inteiro | Empresa do Estabelecimento |  |
| `VLRRECBRUTATOTAL` | Decimal | Vlr. Receita Bruta Total |  |
| `VLRBASECPAPUR` | Decimal | Vlr. Base Contribuição Previdenciaria |  |
| `VLRCPAPUR` | Decimal | Vlr. Contribuição Previdenciaria |  |
| `VLRBASERATAPUR` | Decimal | Vlr. Base Contribuição Previdenciaria GILRAT |  |
| `VLRRATAPUR` | Decimal | Vlr. Contribuição Previdenciaria GILRAT |  |
| `VLRBASESENARAPUR` | Decimal | Vlr. Base Contribuição Previdenciaria SENAR |  |
| `VLRSENARAPUR` | Decimal | Vlr. Contribuição Previdenciaria SENAR |  |
| `VLRCPSUSPTOTAL` | Decimal | Vlr. Contribuição c/ Exigibilidade Suspensa |  |
| `VLRRATSUSPTOTAL` | Decimal | Vlr. Contribuição GILRAT c/ Exigibilidade Suspensa |  |
| `VLRSENARSUSPTOTAL` | Decimal | Vlr. Contribuição SENAR c/ Exigibilidade Suspensa |  |
| `VLRCPAPURRET` | Decimal | Vlr. Contribuição Previdenciaria |  |
| `VLRRATAPURRET` | Decimal | Vlr. Contribuição Previdenciaria GILRAT |  |
| `VLRSENARAPURRET` | Decimal | Vlr. Contribuição Previdenciaria SENAR |  |
| `VLRCPSUSPTOTALRET` | Decimal | Vlr. Contribuição c/ Exigibilidade Suspensa |  |
| `VLRRATSUSPTOTALRET` | Decimal | Vlr. Contribuição GILRAT c/ Exigibilidade Suspensa |  |
| `VLRSENARSUSPTOTALRET` | Decimal | Vlr. Contribuição SENAR c/ Exigibilidade Suspensa |  |
| `MSG` | C | Mensagem |  |
| `XMLEVENTO` | C | XML de Envio |  |
| `XMLRETORNO` | C | XML de Retorno |  |
| `DATACHANGE` | C | Dados alterados |  |

### TRIICR
**R1000 - Informações do Contribuinte**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  
**entityName:** `InformacaoContribuinte`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TRICAB`.`CODEMP` |
| `DTREF` 🔑 | Data | Dt. Referencia | → `TRICAB`.`DTREF` |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente | → `TRICAB`.`TPAMB` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `STATUSREG` | Texto | Status do Registro |  |
| `TIPO` | Texto | Tipo de Envio |  |
| `IDEVENTO` | Texto | ID do Evento |  |
| `NRORECIBO` | Texto | Nro. do Recibo |  |
| `NRORECIBOANT` | Texto | Nro. do Recibo Anterior |  |
| `CONTROLE` | Texto | Controle de Alteração |  |
| `DTTRANSFFINSLUCR` | Data | Data transformação da entidade em fins lucrativos |  |
| `INDUNIAO` | Inteiro | Entidade Vinculada a União |  |
| `DTOBITO` | Data | Data Obito do Contribuinte |  |
| `TPINSC` | Inteiro | Tipo de Inscrição |  |
| `NRINSC` | Texto | Nro. da Inscrição |  |
| `INIVALID` | Data | Dt. Inicial da Vigencia |  |
| `FIMVALID` | Data | Dt. Final da Vigencia |  |
| `CLASSTRIB` | Inteiro | Classificação Tributaria |  |
| `INDESCRITURACAO` | Inteiro | Indicativo da Escrituração |  |
| `INDDESONERACAO` | Inteiro | Desoneração da Folha - CPRB |  |
| `INDACORDOISENMULTA` | Inteiro | Indicativo do Acordo de Isenção de Multa |  |
| `INDSITPJ` | Inteiro | Indicativo da Situação de PJ |  |
| `NMCTT` | Texto | Nome do Contato |  |
| `CPFCTT` | Texto | CPF do Contato |  |
| `FONEFIXOCTT` | Texto | Telefone Fixo do Contato |  |
| `FONECEL` | Texto | Celular do Contato |  |
| `EMAILCTT` | Texto | Email do Contato |  |
| `IDEEFR` | Texto | Ente Federativo Responsavel |  |
| `CNPJEFR` | Texto | CNPJ do Ente Federativo Responsavel |  |
| `INIVALIDNOVO` | Data | Dt. Inicial da Nova Vigencia |  |
| `FIMVALIDNOVO` | Data | Dt. Final da Nova Vigencia |  |
| `MSG` | C | Mensagem |  |
| `XMLEVENTO` | C | XML de Envio |  |
| `XMLRETORNO` | C | XML de Retorno |  |
| `DATACHANGE` | C | Dados alterados |  |

## TGA — Agronegócio

### TGASAF
**Cadastro Safra**

**PK:** `CODSAF`  
**Referenciada por:** 11 tabelas  
**entityName:** `Safra`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSAF` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `DTINICIO` | Data | Data Inicio |  |
| `DTFINAL` | Data | Data Final |  |
| `STATUS` | Texto | Ativo |  |
| `DTALTER` | Data/Hora | Data Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |

### TGACUL
**Culturas**

**PK:** `CODPARC`, `CODSAF`, `SEQPLANEJ`  
**Referenciada por:** 6 tabelas  
**entityName:** `Cultura`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARC` 🔑 | Inteiro | Cod.Parceiro | → `TGAARE`.`CODPARC` |
| `CODPROD` | Inteiro | Cod.Produto | → `TGFPRO`.`CODPROD` |
| `CODAREA` | Inteiro | Cod.Area | → `TGAARE`.`CODAREA` |
| `CONTROLE` | Texto | Controle |  |
| `SAFRA` | Texto | Safra |  |
| `VARIEDADE` | Texto | Variedade |  |
| `PRODUTIVIDADE` | Decimal | Produtividade |  |
| `ANOPREVCOLHEITA` | Inteiro | Ano Previsto Colheita |  |
| `MESPREVCOLHEITA` | Inteiro | Mes Previsto Colheita |  |
| `SACASPREV` | Decimal | Sacas Previstas |  |
| `SACASREAL` | Decimal | Sacas Real |  |
| `FINANCIADA` | Texto | Financiada |  |
| `OBSERVACAO` | Texto | Observação |  |
| `AREAPLANTIO` | Inteiro | Area de Plantio |  |
| `CODPARCAGRON` | Inteiro | Cod. Parceiro Agronomo | → `TGFPAR`.`CODPARC` |
| `CODPROJ` | Inteiro | CODPROJ | → `TCSPRJ`.`CODPROJ` |
| `STATUS` | Texto | Status |  |
| `VLRSACA` | Decimal | Valor saca |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | DTALTER |  |
| `CODSAF` 🔑 | Inteiro | Cod. Safra | → `TGASAF`.`CODSAF` |
| `SEQPLANEJ` 🔑 | Inteiro | Sequencia Planejamento |  |

### TGADIG
**Referencias agricolas do produto**

**PK:** `NUDIG`, `TIPO`  
**Referenciada por:** 16 tabelas  
**entityName:** `DiagnosticoAgricolaProduto`, `DiagnosticoClasseAgrotoxico`, `DiagnosticoClasseToxica`, `DiagnosticoGrupoQuimico`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDIG` 🔑 | Inteiro | Codigo |  |
| `DESCRDIG` | Texto | Descrição |  |
| `CIENTIFICO` | Texto | Nome Cientifico |  |
| `TIPO` 🔑 | Texto | Tipo |  |

### TGACLT
**Tipos de Classificação de Produto**

**PK:** `CODCLT`  
**Referenciada por:** 6 tabelas  
**entityName:** `PadraoClassificacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCLT` 🔑 | Inteiro | Codigo |  |
| `DESCRCLT` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `SIGLA` | Texto | Sigla |  |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODGRUPOPROD` | Inteiro | Grupo de produtos | → `TGFGRU`.`CODGRUPOPROD` |
| `CLASSIFICACAO` | Inteiro | Classificação |  |
| `OBSERVACAO` | Texto | Observação |  |
| `FORMULA` | Texto | Formula |  |
| `TIPOLAUDO` | Texto | Tipo de Laudo |  |
| `EXIGELIB` | Texto | Exige Liberação |  |
| `CONFNEGADO` | Texto | Permite confirmar quando laudo for rejeitado |  |
| `TIPOREFPRZVAL` | Texto | Calcular o Prazo de validade a partir da |  |
| `PRAZOVAL` | Inteiro | Prazo de validade |  |
| `CODGPC` | Inteiro | Grupo P. Class | → `TGAGPC`.`CODGPC` |

### TGAARE
**Area de Plantio**

**PK:** `CODPARC`, `CODAREA`  
**Referenciada por:** 6 tabelas  
**entityName:** `AreaPlantio`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `teste` | Inteiro | t |  |
| `CODPARC` 🔑 | Inteiro | Cod.Parceiro | → `TGFPAR`.`CODPARC` |
| `CODAREA` 🔑 | Inteiro | Cod.Area |  |
| `CODVOL` | Texto | Cod.Volume | → `TGFVOL`.`CODVOL` |
| `NOME` | Texto | Nome |  |
| `TIPAREA` | Texto | Tipo Area |  |
| `AREATOTAL` | Inteiro | Area Total |  |
| `AREAPRODUTIVA` | Inteiro | Area Produtiva |  |
| `OBSERVACAO` | Texto | Observação |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `LIVRO` | Texto | LIVRO |  |
| `INCRA` | Texto | INCRA |  |
| `VALOR` | Decimal | VALOR |  |

### TGACLC
**Classificação Produto Caracteristica Analisavel**

**PK:** `CODCLC`  
**Referenciada por:** 6 tabelas  
**entityName:** `CaracteristicaAnalisavel`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCLC` 🔑 | Inteiro | Codigo |  |
| `NOMECLC` | Texto | Descrição |  |
| `OBSERVACAO` | Texto | Observação |  |
| `CODVINC` | Inteiro | Vinculado a | → `TGACLC`.`CODCLC` |
| `EXIGLIB` | Texto | Exibe Liberação |  |
| `SIGLA` | Texto | Sigla |  |
| `CODGRUPOCLC` | Inteiro | Grupo | → `TGACLC`.`CODCLC` |
| `ORDEM` | Inteiro | Ordem |  |
| `ANALISETERC` | Texto | Analise de Terceiros/REPORT SUPPLIER |  |
| `DECQTD` | Inteiro | Qtd. Decimais |  |
| `CARACTCONFORME` | Texto | Caracteristica Conforme - Não Conforme |  |

### TGACLL
**Laudo de Classificação Produto**

**PK:** `NUCLL`  
**Referenciada por:** 3 tabelas  
**entityName:** `CabecalhoLaudo`, `LaudoClassificacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCLL` 🔑 | Inteiro | Nro. Laudo |  |
| `CODEMP` | Inteiro | Empresa |  |
| `NUNOTA` | Inteiro | Nro. Unico Nota |  |
| `DHANALISE` | Data/Hora | Dh. Termino Analise |  |
| `CODCLT` | Inteiro | Padrão de Classificação | → `TGACLT`.`CODCLT` |
| `CODPROD` | Inteiro | Cod.Produto | → `TGFPRO`.`CODPROD` |
| `REFERENCIA` | Texto | Referencia do Produto |  |
| `PESOBRUTO` | Decimal | Peso Bruto |  |
| `TARA` | Decimal | Tara |  |
| `NOTAROMANEIO` | Inteiro | Numero Nota Romaneio |  |
| `STATUS` | Texto | Status |  |
| `APROVADO` | Texto | Aprovado |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `CODPROJ` | Inteiro | Cod. Projeto | → `TCSPRJ`.`CODPROJ` |
| `NUAMOSTRA` | Inteiro | Nro. Amostra |  |
| `NULAUDOPAI` | Inteiro | Nro. Laudo Pai | → `TGACLP`.`NULAUDOPAI` |
| `NURAM` | Inteiro | Nro. Amostra | → `TGFRAM`.`NURAM` |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHALTER` | Data/Hora | Dh. Alteração |  |
| `CODPARC` | Inteiro | Cod Parceiro |  |
| `TRANSGENIA` | Texto | Transgenia |  |
| `NUMPESAGEM` | Inteiro | Numero Pesagem |  |
| `NUMCONTRATO` | Inteiro | Contrato |  |
| `CODPORT` | Inteiro | Senha Portaria |  |
| `NUMPORT` | Inteiro | Senha Portaria |  |
| `MOTIVOREPROV` | Texto | Motivo Reprovação |  |
| `MODULO` | Texto | Modulo |  |
| `NUMNOTATRANS` | Inteiro | Nota de Transporte |  |
| `CODVEIC` | Inteiro | Veiculo |  |

### TGAPES
**Pesagem Armazenagem**

**PK:** `NUMPESAGEM`  
**entityName:** `PesagemMultipla`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` | Inteiro | Nro. Nota |  |
| `NUMPESAGEM` 🔑 | Inteiro | Ticket |  |
| `CODPORT` | Inteiro | Nro. Portaria |  |
| `NUMPORT` | Inteiro | Senha Portaria |  |
| `CODEMP` | Inteiro | Empresa |  |
| `TIPO` | Texto | Tipo de Movimentação |  |
| `PESOBRUTO` | Decimal | Peso Bruto |  |
| `DHPESOBRUTO` | Data/Hora | Data Peso Bruto |  |
| `CODVEIC` | Inteiro | Veiculo |  |
| `PESAGEMMANUAL` | Texto | Pesagem Manual |  |
| `CODMOTO` | Inteiro | Motorista |  |
| `CODUSUPB` | Inteiro | Usuario Peso Bruto |  |
| `BALANCAPB` | Inteiro | Balanca Peso Bruto |  |
| `TARA` | Decimal | Tara |  |
| `DHTARA` | Data/Hora | Data Tara |  |
| `NOMEUSUTARA` | Texto | Nome Usuario Tara |  |
| `NOMEUSUPB` | Texto | Nome Usuario Peso Bruto |  |
| `CODUSUTARA` | Inteiro | Usuario Tara |  |
| `BALANCATARA` | Inteiro | Balanca Tara |  |
| `PESOLIQ` | Decimal | Peso Liquido |  |
| `PLACA` | Texto | Placa |  |
| `NMBALTARA` | Texto | Balanca Tara |  |
| `NMBALPESBRUTO` | Texto | Balanca Peso Bruto |  |
| `MOTORISTA` | Texto | Motorista |  |
| `CODUF` | Inteiro | Estado |  |
| `OBSERVACAO` | Texto | Observação |  |
| `PESODESCONTO` | Decimal | Descontos |  |
| `PESOCORRIGIDO` | Decimal | Peso Corrigido |  |
| `NOMEBALANCA` | Texto | Nome Balanca |  |
| `RETENCOES` | Decimal | Retenções |  |
| `MODALIDADE` | Texto | Modalidade do Contrato |  |
| `STATUS` | Texto | Status |  |
| `DHCANCEL` | Data/Hora | Data Cancelamento |  |
| `CODUSUCANCEL` | Inteiro | Usuario Cancelamento |  |
| `NOMEUSUCANCEL` | Texto | Nome Usuario Cancelamento |  |
| `MOTIVOCANCEL` | Texto | Motivo do Cancelamento |  |

### TGAPEA
**Pesagem Avulsa**

**PK:** `CODPESAV`  
**entityName:** `PesagemAvulsa`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPESAV` 🔑 | Inteiro | Ticket |  |
| `PESAGEMMANUAL` | Texto | Pesagem Manual |  |
| `NOMEBALANCA` | Texto | Balanca |  |
| `TIPO` | Texto | Tipo de Pesagem |  |
| `STATUS` | Texto | Status da Pesagem |  |
| `CODEMP` | Inteiro | Cod Empresa | → `TSIEMP`.`CODEMP` |
| `CODVEI` | Texto | Veiculo |  |
| `CODMOTO` | Inteiro | Motorista |  |
| `CODPARC` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CODPROD` | Texto | Produto |  |
| `KMINICIAL` | Texto | Km Inicial |  |
| `KMFINAL` | Texto | Km Final |  |
| `KMPERCORRIDO` | Texto | Km Percorrido |  |
| `PESODECLARADO` | Texto | Peso Declarado |  |
| `OBSERVACAO` | Texto | Observação |  |
| `PESINI` | Decimal | Peso Bruto |  |
| `TARA` | Decimal | Tara |  |
| `PESFIN` | Decimal | Peso Liquido |  |
| `CPF` | Texto | CPF |  |
| `DHPEFIM` | Data/Hora | Data Tara |  |
| `DHPEINIC` | Data/Hora | Data Movimento |  |
| `MOTORIS` | Texto | Motorista |  |
| `PLACA` | Texto | Placa |  |
| `PRODUTO` | Texto | Produto |  |
| `NOMEUSUPB` | Texto | Nome Usuario Peso Bruto |  |
| `NOMEUSUTARA` | Texto | Nome Usuario Tara |  |
| `CODUSUPB` | Inteiro | Usuario Peso Bruto |  |
| `CODUSUTARA` | Inteiro | Usuario Tara |  |
| `DHPESAGEM` | Data/Hora | Data Peso Bruto |  |
| `NMBALPESBRUTO` | Texto | Balanca Peso Bruto |  |
| `NMBALTARA` | Texto | Balanca Tara |  |
| `DHCANCEL` | Data/Hora | Data Cancelamento |  |
| `CODUSUCANCEL` | Inteiro | Usuario Cancelamento |  |

### TGARPO
**Controle de Portaria**

**Referenciada por:** 1 tabelas  
**entityName:** `ControlePortaria`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMPESAGEM` | Inteiro | N Pesagem |  |
| `NUCLL` | Inteiro | N Laudo |  |
| `NUMPORT` | Inteiro | Senha Portaria |  |
| `CODPORT` | Inteiro | Contador Portaria |  |
| `CODEMP` | Inteiro | Empresa |  |
| `TIPO` | Texto | Tipo de Movimentação |  |
| `MODALIDADE` | Texto | Modalidade do Contrato |  |
| `CODVEIC` | Inteiro | Veiculo |  |
| `CODMOTO` | Inteiro | Motorista |  |
| `DHCHEGA` | Data/Hora | Dt. Chegada |  |
| `DHENTRA` | Data/Hora | Dt. Entrada |  |
| `DHPESOBRUTO` | Data/Hora | Dt. Peso Bruto |  |
| `DHTARA` | Data/Hora | Dt. Tara |  |
| `OBSERV` | Texto | Observação |  |
| `DHSAIDA` | Data/Hora | Dt. Saida |  |
| `CODUSU` | Inteiro | Usuario |  |
| `STATUS` | Texto | Status |  |
| `MOTORISTA` | Texto | Motorista |  |
| `MOTIVO` | Texto | Motivo |  |
| `PLACA` | Texto | Placa |  |
| `CODUF` | Inteiro | UF Veiculo |  |

### TGAAPC
**Apuração de contratos armazenagem**

**PK:** `CODFATCONT`  
**entityName:** `ApuracaoContratoArmarzenagem`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFATCONT` 🔑 | Inteiro | Nu Fat Contrato |  |
| `CODSERV` | Inteiro | Codigo Servico |  |
| `CONTRATO` | Inteiro | Num Contrato |  |
| `TIPO` | Texto | Tipo |  |
| `PERCOBRA` | Texto | Nome |  |
| `TIPCOBR` | Texto | TIPCOBR |  |
| `STATUS` | Texto | Status |  |
| `NOME` | Texto | Nome |  |
| `CODUSU` | Inteiro | Cod Usuario |  |
| `CODEMP` | Inteiro | Cod Empresa |  |
| `CODPARC` | Inteiro | Parceiro |  |
| `TOTALRETENCAO` | Decimal | Total Retenção |  |
| `VALORSERVICO` | Decimal | Valor Servico |  |
| `TOTALSACAS` | Decimal | Total Sacas |  |
| `VLRTRANSORIG` | Decimal | Cod. Mov Origem |  |
| `VLRTRANS` | Decimal | Vlr. Transferido |  |
| `PESOTOTAL` | Decimal | Peso Total |  |
| `CODTRANSORIG` | Decimal | Cod. Trans Origem |  |
| `VLRLIQ` | Decimal | Vlr. Liquido |  |
| `VLRLIQFAT` | Decimal | Vlr. Liquido a Faturar |  |
| `VLRFATURADO` | Decimal | Vlr. Faturado" |  |
| `VLRDESC` | Decimal | Vlr. Descontos |  |
| `DATAINICIO` | Data/Hora | Data Inicio |  |
| `DATAFINAL` | Data/Hora | Data Final |  |

## TSE — Serasa/Bureau de Crédito

### TSERINGR
**Informações Gerais Serasa**

**PK:** `NUCONSULTA`  
**entityName:** `InformacaoGeralSerasa`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` 🔑 | Inteiro | NUCONSULTA |  |
| `DESCRSITRF` | Texto | Situação |  |
| `SITUACAORF` | Inteiro | Situação da empresa |  |
| `NOME` | Texto | Nome |  |
| `RAZAO` | Texto | Razão social |  |
| `DATANASC` | Data | Data de nascimento |  |
| `NOMEMAE` | Texto | Nome da me |  |
| `NOMEFANTASIA` | Texto | Nome fantasia |  |
| `RAMOATV` | Texto | Ramo de atividade |  |
| `SEXO` | Texto | Sexo |  |
| `TIPRELATO` | Texto | Tipo de Relato |  |
| `TIPOSOCIEDADE` | Texto | Tipo de sociedade |  |
| `NRUTRG` | Texto | Registro |  |
| `SITCPF` | Inteiro | Situação do Cpf |  |
| `DTUTRG` | Data | Data do registro |  |
| `NIRE` | Texto | Nire |  |
| `ENDERECO` | Texto | Endereco |  |
| `BAIRRO` | Texto | Bairro |  |
| `CIDADE` | Texto | Cidade |  |
| `UF` | Texto | UF |  |
| `CEP` | Texto | Cep |  |
| `FONECOM` | Texto | Telefone |  |
| `NRFAX` | Texto | Fax |  |
| `HOMEPAGE` | Texto | Home Page |  |
| `DATAFUND` | Data | Data de fundação |  |
| `FILIAIS` | Texto | Filiais |  |
| `NROFILIAIS` | Inteiro | Qtde. Filiais |  |
| `RG` | Texto | RG |  |
| `NUMEMPREGADOS` | Inteiro | Qtde. empregados |  |
| `NRODEPENDENTES` | Inteiro | Qtde. dependentes |  |
| `OPCAOTRIBUTARIA` | Texto | Opção tributaria |  |
| `CNAE` | Texto | CNAE |  |
| `TIPODOC` | Texto | Tipo de documento |  |
| `CODSERASA` | Texto | Cod. Atividade Serasa |  |
| `PERCIMPORT` | Inteiro | Imp. s/ Compras |  |
| `EMISRG` | Texto | Orgão emissor |  |
| `DTRG` | Data | Data de emissão |  |
| `PERCEXPORT` | Inteiro | Exp. s/ Vendas |  |
| `UFRG` | Texto | UF RG |  |
| `ESTADOCIVIL` | Texto | Estado civil |  |
| `ESCOLARIDADE` | Texto | Escolaridade |  |
| `MUNNASC` | Texto | Cidade de nascimento |  |
| `UFNASC` | Texto | UF Nascimento |  |
| `CPFCONJUGE` | Texto | CPF Conjuge |  |
| `DDDRES` | Texto | DDD Residencial |  |
| `FONERES` | Texto | Telefone residencial |  |
| `DDDCOM` | Texto | DDD Comercial |  |
| `CNPJ` | Texto | CNPJ |  |
| `RAMAL` | Inteiro | Ramal |  |
| `DTATUALIZACAO` | Data | Data Atualização |  |
| *... +8 campos* | | | |

### TSERBUR
**Bureau**

**PK:** `NUCONSULTA`  
**entityName:** `Bureau`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` 🔑 | Inteiro | NUCONSULTA |  |
| `OCUPACAO` | Texto | Ocupação |  |
| `CCBANCO1` | Texto | Banco |  |
| `BANCO1CHQESP` | Texto | Banco do Cheque Especial |  |
| `RENDA` | Decimal | Renda |  |
| `CCBANDEIRA1` | Texto | Bandeira |  |
| `LIMITE1CHQESP` | Decimal | Limite do Cheque Especial |  |
| `CCBANCO2` | Texto | Banco |  |
| `BANCO2CHQESP` | Texto | Banco do Cheque Especial |  |
| `CTSERIE` | Texto | Serie da Carteira de Trabalho |  |
| `CARGO` | Texto | Cargo |  |
| `CCBANDEIRA2` | Texto | Bandeira |  |
| `NUMCT` | Texto | Carteira de Trabalho |  |
| `LIMITE2CHQESP` | Decimal | Limite do Cheque Especial |  |
| `CCOUTREMIS` | Texto | Outro emissor do Cartão de Credito |  |
| `EMPRESA` | Texto | Empresa |  |
| `CCBANDEIRA3` | Texto | Bandeira |  |
| `DTADMISSAO` | Texto | Data admissão |  |
| `PROFISSAO` | Texto | Profissão |  |
| `CCTIPOSEGURO` | Texto | Tipo de seguro |  |
| `TIPOSEG` | Texto | Tipo de seguro |  |
| `TIPOSEG2` | Texto | Tipo de seguro |  |
| `TIPOSEG3` | Texto | Tipo de seguro |  |
| `TIPOSEG4` | Texto | Tipo de seguro |  |
| `TIPOSEG5` | Texto | Tipo de seguro |  |
| `OUTRRENDA` | Decimal | Valor de Outras Rendas |  |
| `RCSMSGFRASE` | Texto | Msg. de risco |  |
| `RCSFATOR` | Inteiro | Score |  |
| `PERIODIC` | Data | Periodicidade das Outras Rendas |  |
| `ORIGEM1` | Texto | Origem da 1 Outra Renda |  |
| `CODIGODERETORNO` | Texto | Codigo de retorno |  |
| `TIPOSCORE` | Texto | Descrição do Scoring escolhido |  |
| `TAXA` | Texto | Probabilidade de inadimplencia |  |
| `REFPESSOAL1` | Texto | Referencia pessoal |  |
| `REFDDD1` | Inteiro | DDD |  |
| `REFFONE1` | Inteiro | Telefone |  |
| `REFRAMAL1` | Inteiro | Ramal |  |
| `REFPESSOAL2` | Texto | Referencia pessoal |  |
| `REFDDD2` | Inteiro | DDD |  |
| `REFFONE2` | Inteiro | Telefone |  |
| `REFRAMAL2` | Inteiro | Ramal |  |
| `ORIGEM2` | Texto | Origem da 2 Outra Renda |  |
| `RENDAFAML` | Decimal | Outra renda familiar |  |
| `FAMILIAR1` | Texto | Descrição do 1  familiar que contribui com renda |  |
| `FAMILIAR2` | Texto | Descrição do 2  familiar que contribui com renda |  |

### TSERRLT
**Relato**

**PK:** `NUCONSULTA`  
**entityName:** `Relato`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` 🔑 | Inteiro | NUCONSULTA |  |
| `DATAULTATCS` | Data | Dt. ult. atualização das informações |  |
| `VRCAPSOCCS` | Decimal | Vlr. capital social |  |
| `VRCAPREACS` | Decimal | Vlr. capital realizado |  |
| `VRCAPAUTCS` | Decimal | Vlr. capital autorizado |  |
| `DESCDNACS` | Texto | Descr. nacionalidade |  |
| `DESCDCRAOCS` | Texto | Descr. origem |  |
| `DESCPARCS` | Texto | Descr. natureza |  |
| `TIPRETCS` | Texto | Controle societario c/ base na junta comercial |  |
| `DHRISKSCO` | Data/Hora | Data RiskScoring |  |
| `FATORRISKSCO` | Decimal | Fator RiskScoring |  |
| `VLFATP` | Decimal | Valor faturamento |  |
| `FATPRESPONTOS` | Inteiro | Pontuação |  |
| `LIMCREDDHCALCULO` | Data/Hora | Data do limite de credito |  |
| `LIMCREDVALOR` | Decimal | Limite de credito |  |
| `LIMCREDOBS` | Texto | Obs. limite de credito |  |
| `FRASEALERTA` | Texto | Frase alerta |  |
| `DATAALERTA` | Data | Data de alerta |  |
| `IDPJPONTUACAO` | Inteiro | Pontuação |  |
| `IDPJMENSPROD` | Texto | Mensagem do produto |  |
| `IDPJFRASE` | Texto | Mensagem |  |
| `IDPJVISAO` | Texto | Visão |  |
| `IRCPONTUACAO` | Inteiro | Pontuação |  |
| `IRCCLASSE` | Texto | Classe |  |
| `IRCINTERPRETACAO` | Texto | Interpretação |  |
| `IRCCODMENSAGEM` | Inteiro | Cod. mensagem |  |
| `IRCMENSAGEM` | Texto | Mensagem |  |
| `IRMVALOR` | Texto | Valor |  |
| `RCSFATOR` | Inteiro | Score |  |
| `RCSPRINY` | Decimal | Valor priny |  |
| `RCSMSGFRASE` | Texto | Msg. de risco |  |
| `FATPRESMSG` | Texto | Mensagem |  |
| `IRMFRASE` | Texto | Frase |  |
| `IRMDTATUALIZACAO` | Data/Hora | Data de atualização |  |
| `FATPRESFAIXADE` | Inteiro | Faixa da pontuação DE |  |
| `FATPRESFAIXAATE` | Inteiro | Faixa da pontuação ATE |  |
| `FATPRESFRASENCALC` | Texto | Motivo de não calculo |  |
| `CODIGODERETORNO` | Texto | Codigo de retorno |  |
| `MENSAGEMGERENCIE` | Texto | Mensagem de retorno do gerencie |  |
| `MENSAGEMCONFIE` | Texto | Mensagem de retorno do confie |  |

### TSERHPV
**Historico de pagamentos por valores**

**PK:** `NUCONSULTA`, `SEQUENCIA`  
**entityName:** `HistoricoPagamentoValores`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` 🔑 | Inteiro | NUCONSULTA |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `MES` | Data/Hora | Mes/Ano |  |
| `DESCR1` | Texto | Pontual |  |
| `VALOR1` | Decimal | Valor |  |
| `PERC1` | Inteiro | % |  |
| `DESCR2` | Texto | 8-15 |  |
| `VALOR2` | Decimal | Valor |  |
| `PERC2` | Inteiro | % |  |
| `DESCR3` | Texto | 16-30 |  |
| `VALOR3` | Decimal | Valor |  |
| `PERC3` | Inteiro | % |  |
| `DESCR4` | Texto | 31-60 |  |
| `VALOR4` | Decimal | Valor |  |
| `PERC4` | Inteiro | % |  |
| `DESCR5` | Texto | +60 |  |
| `VALOR5` | Decimal | Valor |  |
| `PERC5` | Inteiro | % |  |
| `DESCR6` | Texto | P.M.A |  |
| `VALOR6` | Decimal | Valor |  |
| `PERC6` | Inteiro | % |  |
| `DESCR7` | Texto | A VISTA |  |
| `VALOR7` | Decimal | Valor |  |
| `PERC7` | Inteiro | % |  |
| `TOTAL` | Decimal | Total Mes |  |

### TSERQRA
**Quadro administrativo**

**PK:** `NUCONSULTA`, `SEQUENCIA`  
**entityName:** `QuadroAdministrativo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` 🔑 | Inteiro | NUCONSULTA |  |
| `TIPPESSOA` | Texto | IDENTADM |  |
| `CPFCNPJ` | Texto | CPF / CNPJ |  |
| `SEQCNPJ` | Texto | CNPJSEQADM |  |
| `DIGCPFCNPJ` | Texto | DIGCPFADM |  |
| `NOME` | Texto | Administração |  |
| `CARGO` | Texto | Cargo |  |
| `NACIONALIDADE` | Texto | Nacionalidade |  |
| `ESTADOCIVIL` | Texto | Estado Civil |  |
| `DTINIMANDATO` | Data | Inicio mandato |  |
| `DTFIMMANDATO` | Data | Fim mandato |  |
| `RESTRICAO` | Texto | Restrição |  |
| `CARGOADMIX` | Texto | Cargo |  |
| `SITUACAORF` | Texto | CDSITRF |  |
| `DTADMISSAO` | Data | Entrada |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `MANDATO` | Texto | Mandato |  |
| `IDENTIDADE` | Texto | Identidade |  |
| `DTNASCIMENTO` | Data | Data Nasc |  |
| `NATURALDE` | Texto | Natural de |  |
| `TELEFONE` | Texto | Telefone |  |
| `VINCULO` | Texto | Vinculo |  |
| `ENDERECO` | Texto | Endereco |  |

### TSERPROT
**Protestos**

**entityName:** `Protestos`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` | Inteiro | NUCONSULTA |  |
| `QTDPROTESTO` | Inteiro | OCORPROT |  |
| `DATAPROTESTO` | Data | Data do Protesto |  |
| `VALOR` | Decimal | Valor |  |
| `CARTORIO` | Texto | Cartorio |  |
| `MOEDA` | Texto | MOEDPROT |  |
| `CIDUFPROT` | Texto | Cidade/UF |  |
| `CIDADE` | Texto | CIDAPROT |  |
| `UF` | Texto | UFPROT |  |
| `MSGSUBJUDICE` | Texto | MSGSUBJUDICE |  |
| `PRACASUBJUDICE` | Texto | PRACAPRO |  |
| `DISTRITOSUBJUDICE` | Texto | DISTRPRO |  |
| `VARASUBJUDICE` | Texto | VARAPRO |  |
| `DATASUBJUDICE` | Data/Hora | DATAPRO |  |
| `PROCESSOSUBJUDICE` | Texto | PROCPRO |  |
| `CODNATUREZA` | Texto | CDNATUPRO |  |
| `TIPCARTAANUENCIA` | Texto | TPANUEPROT |  |
| `DTRECEBANUENCIA` | Data/Hora | DTANUEPROT |  |
| `MSGSUBJUDICE2` | Texto | MSGSUBJUD |  |
| `SEQUENCIA` | Inteiro | SEQUENCIA |  |
| `VALORTOTAL` | Decimal | VALORTOTAL |  |
| `CPFCNPJ` | Texto | CPFCNPJ |  |

### TSERHPQ
**Historico de pagamentos por quantidade**

**PK:** `NUCONSULTA`, `SEQUENCIA`  
**entityName:** `HistoricoPagamentoQuantidade`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` 🔑 | Inteiro | NUCONSULTA |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `DESCR1` | Texto | Pontual |  |
| `VALOR1` | Decimal | Qtde |  |
| `PERC1` | Inteiro | % |  |
| `DESCR2` | Texto | 8-15 |  |
| `VALOR2` | Decimal | Qtde |  |
| `PERC2` | Inteiro | % |  |
| `DESCR3` | Texto | 16-30 |  |
| `VALOR3` | Decimal | Qtde |  |
| `PERC3` | Inteiro | % |  |
| `DESCR4` | Texto | 31-60 |  |
| `VALOR4` | Decimal | Qtde |  |
| `PERC4` | Inteiro | % |  |
| `DESCR5` | Texto | +60 |  |
| `VALOR5` | Decimal | Qtde |  |
| `PERC5` | Inteiro | % |  |
| `DESCR6` | Texto | A Vista |  |
| `VALOR6` | Decimal | Qtde |  |
| `QTDFONTESHISTPAG` | Decimal | Fontes consultadas |  |
| `PERC6` | Inteiro | % |  |

### TSERPFIN
**Pendencias financeiras**

**entityName:** `PendenciasFinanceiras`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONSULTA` | Inteiro | NUCONSULTA |  |
| `QTDPENDENCIA` | Inteiro | QTDEOCOR |  |
| `QTDULTOCOR` | Inteiro | ULTOCOR |  |
| `DTOCORRENCIA` | Data | Data |  |
| `DESCRICAO` | Texto | Modalidade |  |
| `AVALISTA` | Texto | Avalista |  |
| `VALOR` | Decimal | Valor |  |
| `CONTRATO` | Texto | Contrato |  |
| `ORIGEM` | Texto | Origem |  |
| `FILIAL` | Texto | FILIAL |  |
| `MSGSUBJUDICE` | Texto | MSGSUBJUDICE |  |
| `PRACA` | Texto | PRACAPEF |  |
| `DISTRITO` | Texto | DISTRPEF |  |
| `VARA` | Texto | VARAPEF |  |
| `DATASUBJUDICE` | Data | Data |  |
| `PROCESSO` | Texto | PROCPEF |  |
| `NATUREZA` | Texto | CDNATUPEF |  |
| `MSGSUBJUDICE2` | Texto | MSGSUBJUD |  |
| `VALORTOTAL` | Decimal | QTDEVALO |  |
| `SEQUENCIA` | Inteiro | SEQUENCIA |  |
| `CPFCNPJ` | Texto | CPFCNPJ |  |
