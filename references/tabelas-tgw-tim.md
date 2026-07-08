# Tabelas TGW (WMS) e TIM (Imobiliário)

TGW* — Gestão de Armazém (WMS): endereços, separações, recebimentos.
TIM* — Módulo Imobiliário: imóveis, locações, contratos de venda.

## TGW — WMS (Gestão de Armazém)

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
| `CONEXAOENTRADA` | Texto | Utiliza endereco de conexão para Entrada |  |
| `NROMAXPROD` | Inteiro | Nro. maximo de produtos |  |
| `REABPICK` | Texto | Reabastecido por Picking |  |
| `LOTEUNICO` | Texto | Lote Unico |  |
| `UTILIZAUMA` | Texto | Utiliza UMA |  |
| `QTDMAXUMA` | Inteiro | Qtd. maxima de UMAs permitidas no endereco |  |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `APENASCONTPORPROD`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `BLOQUEADO`:** `S`=Bloqueado, `N`=Disponivel

**Opções `CONEXAOENTRADA`:** `S`=Sim, `N`=Não

### TGWITT
**Itens de Tarefa**

**PK:** `NUTAREFA`, `SEQUENCIA`  
**Referenciada por:** 16 tabelas  
**entityName:** `ItemTarefa`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUTAREFA` 🔑 | Inteiro | Nro. Tarefa | → `TGWTAR`.`NUTAREFA` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `NURECEBIMENTO` | Inteiro | Nro. Recebimento |  |
| `CODPROD` | Inteiro | Cod.Produto | → `TGFPRO`.`CODPROD` |
| `CODENDORIGEM` | Inteiro | Cod.End.Origem | → `TGWEND`.`CODEND` |
| `CODENDDESTINO` | Inteiro | Cod.End.Destino | → `TGWEND`.`CODEND` |
| `QTDORIG` | Inteiro | Qtd. Origem |  |
| `CODVOLORIG` | Texto | Un. Origem | → `TGFVOL`.`CODVOL` |
| `QTDDEST` | Inteiro | Qtd. Destino |  |
| `CODVOLDEST` | Texto | Un. Destino | → `TGFVOL`.`CODVOL` |
| `SITUACAO` | Texto | Situação |  |
| `CODUSUEXEC` | Inteiro | Cod.Executante | → `TSIUSU`.`CODUSU` |
| `DHINICIALEXEC` | Data/Hora | Dh.Inicial |  |
| `DHFINALEXEC` | Data/Hora | Dh.Final |  |
| `CODEMP` | Inteiro | Cod.Empresa | → `TGFEMP`.`CODEMP` |
| `CODLOCAL` | Inteiro | Local | → `TGFLOC`.`CODLOCAL` |
| `CONTROLE` | Texto | Controle |  |
| `CODEQUIP` | Inteiro | Equipamento | → `TGWEQP`.`CODEQUIP` |
| `TIPTAREFA` | Texto | Tipo |  |
| `QTDVOLCOMPRA` | Decimal | Qtd. Vol. Compra |  |
| `CODVOLCOMPRA` | Texto | Un. Compra |  |
| `CODBARRAVOLCOMPRA` | Texto | Cod. Barras Vol. Compra |  |
| `FASETAREFA` | Inteiro | Fase |  |
| `CODAREASEP` | Inteiro | Area de Separação | → `TGWARS`.`CODAREASEP` |
| `IDPALETE` | Inteiro | ID. Palete | → `TGWRPL`.`IDPALETE` |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `OCORRENCIA` | Texto | Alterado via Ocorrencia |  |
| `QTDVOLPAD` | Decimal | Qtd. Vol. Padrão |  |
| `CODARMAZENAGEM` | Inteiro | Armazenamento Expresso | → `TGWARE`.`CODARMAZENAGEM` |
| `TRIADO` | Texto | TRIADO |  |
| `IDMAPA` | Inteiro | Nro. Mapa |  |
| `DHIMPMAPA` | Data/Hora | Dh. Imp. Mapa |  |
| `DHINICIOMAPA` | Data/Hora | Dh. Inicio Mapa |  |
| `DHFIMMAPA` | Data/Hora | Dh. Fim Mapa |  |

**Opções `SITUACAO`:** `A`=Aberta, `E`=Em execução, `C`=Cancelada, `F`=Fechada

### TGWREC
**Recebimentos**

**PK:** `NURECEBIMENTO`  
**Referenciada por:** 8 tabelas  
**entityName:** `Recebimento`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NURECEBIMENTO` 🔑 | Inteiro | Nro. Recebimento |  |
| `SITUACAO` | Inteiro | Situação |  |
| `DESCRSITUACAO` | Texto | Situação |  |
| `CODDOCA` | Inteiro | Cod. Doca | → `TGWDCA`.`CODDOCA` |
| `CODENDDOCA` | Inteiro | End. Doca | → `TGWEND`.`CODEND` |
| `DTRECEBIMENTO` | Data | Dt. Recebimento |  |
| `NUCONFERENCIA` | Inteiro | Conferencia | → `TGWCON`.`NUCONFERENCIA` |
| `CODPARC` | Inteiro | Parceiro |  |
| `NOMEPARC` | Texto | Descr. Parceiro |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Dt. Alteração |  |
| `NUTAREFA` | Inteiro | Nro. Tarefa | → `TGWTAR`.`NUTAREFA` |
| `NUNOTA` | Inteiro | Nro. Unico Nota |  |
| `NUMPEDIDO2` | Texto | Nro. Pedido |  |
| `NUTAREFACAN` | Inteiro | Nro. Tarefa Cancelada |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `OBSERVACAO` | Texto | Observação |  |
| `STATUSCONF` | Inteiro | Status Conferencia |  |
| `CONFFINAL` | Texto | Conferencia Final |  |
| `TIPONOTA` | Inteiro | Tipo de Nota |  |
| `USACONFPARCIAL` | Texto | Usa conferencia parcial |  |

**Opções `CONFFINAL`:** `S`=Sim, `N`=Não

**Opções `SITUACAO`:** `0`=Aguardando conferencia, `4`=Enviado para armazenagem, `5`=Armazenado, `1`=Em processo de conferencia, `2`=Conferencia com divergencia, `6`=Concluido, `3`=Aguardando armazenagem

**Opções `TIPONOTA`:** `1`=Normal, `2`=Retorno Devolução de Compra, `3`=Retorno Cancelamento de Venda

**Opções `USACONFPARCIAL`:** `N`=Não, `S`=Sim

### TGWCOI
**Itens de conferencia**

**PK:** `NUCONFERENCIA`, `CODPROD`, `CODBARRA`, `SEQUENCIA`, `TIPOVOLUME`, `CODVOLUME`, `CONTROLE`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCONFERENCIA` 🔑 | Inteiro | Nro. Conferencia | → `TGWCON`.`NUCONFERENCIA` |
| `CODPROD` 🔑 | Inteiro | Cod. Produto |  |
| `CODBARRA` 🔑 | Texto | Cod. Barra |  |
| `QTDECONF` | Inteiro | Qtde. Conferida |  |
| `RECONTAGEM` | Texto | Recontagem |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `IGNORAR` | Texto | IGNORAR |  |
| `CODVOLCOMPRA` | Texto | CODVOLCOMPRA |  |
| `TIPOVOLUME` 🔑 | Texto | TIPOVOLUME |  |
| `CODVOLUME` 🔑 | Inteiro | Cod. Volume |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CONTROLE` 🔑 | Texto | Controle |  |
| `QTDAVARIA` | Inteiro | Qtde. Avariada |  |
| `RECEBERAVARIA` | Texto | RECEBERAVARIA |  |
| `DEVOLVER` | Texto | DEVOLVER |  |
| `DTVAL` | Data | Dt. Validade |  |
| `DTVALMIN` | Data | Dt. Val. Minima |  |
| `CODUSUDIV` | Inteiro | CODUSUDIV | → `TSIUSU`.`CODUSU` |
| `ACEITARDIF` | Texto | ACEITARDIF |  |
| `QTDEDIF` | Inteiro | QTDEDIF |  |
| `CODMDIV` | Inteiro | Cod. Divergencia | → `TGWMDIV`.`CODMDIV` |
| `QTDPECAS` | Inteiro | Qtd. de Pecas |  |

**Opções `RECONTAGEM`:** `S`=Sim, `N`=Não

### TGWSEP
**Separações**

**PK:** `NUSEPARACAO`  
**Referenciada por:** 4 tabelas  
**entityName:** `Separacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUSEPARACAO` 🔑 | Inteiro | Nro. Sep. |  |
| `ENVIADODOCA` | Texto | Enviado p/ Doca |  |
| `NUNOTA` | Inteiro | Nro. Unico | → `TGFCAB`.`NUNOTA` |
| `DESCRSITUACAO` | Inteiro | Situação |  |
| `CODDOCA` | Inteiro | Cod. Doca | → `TGWDCA`.`CODDOCA` |
| `CODENDDOCA` | Inteiro | Cod. End. Doca |  |
| `ORDEMCARGA` | Inteiro | O.C |  |
| `TIPOSEP` | Texto | Tipo Separação |  |
| `PESOBRUTO` | Decimal | Peso Bruto |  |
| `M3BRUTO` | Decimal | M3 Bruto |  |
| `QTDTAREFAS` | Inteiro | Qtd. Tarefas |  |
| `NUMNOTA` | Inteiro | Nro. Nota |  |
| `CODAREACONF` | Inteiro | Area | → `TGWARC`.`CODAREACONF` |
| `SITUACAO` | Inteiro | Situação |  |
| `DTSEPARACAO` | Data/Hora | Dt. Separação |  |
| `NUTAREFA` | Inteiro | Nro Tarefa | → `TGWTAR`.`NUTAREFA` |
| `NUCONFERENCIA` | Inteiro | Conferencia | → `TGWCON`.`NUCONFERENCIA` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Dh. Alteração |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `STATUSCONF` | Inteiro | Status Conferencia |  |
| `FLOWRACK` | Texto | Flow Rack |  |
| `QTDCXSFLOWRACK` | Inteiro | Qtd. Cxs. Flow Rack |  |
| `CODEMPOC` | Inteiro | Cod. Emp OC |  |
| `CODAREASEP` | Inteiro | Cod. Area Sep | → `TGWARS`.`CODAREASEP` |
| `LIBERADA` | Texto | Liberada |  |
| `TIPOSPLIT` | Inteiro | Tipo de Split de Tarefas |  |
| `NROPALETE` | Inteiro | Nro. Palete |  |
| `LIBERAREAB` | Texto | Reabastecimento Liberado |  |
| `QTDCHECKOUTS` | Inteiro | Qtd. Checkouts |  |
| `NUSEPMAE` | Inteiro | Nro. Separação Me |  |
| `CODONDA` | Inteiro | Cod. Onda | → `TGWOND`.`CODONDA` |
| `TRIADO` | Texto | Triagem Realizada |  |
| `CANCELADA` | Texto | Cancelada |  |
| `OBSERVACAO` | Texto | Observação |  |
| `CODUSUCONF` | Inteiro | Cod. Conferente |  |
| `NOMEUSUCONF` | Texto | Conferente |  |
| `CODPARC` | Inteiro | Cod. Parceiro Destino |  |
| `SITUACAOANT` | Inteiro | Situação Cancelamento Sep |  |

**Opções `CANCELADA`:** `S`=Sim, `N`=Não

**Opções `ENVIADODOCA`:** `S`=Sim, `N`=Não

**Opções `SITUACAO`:** `2`=Aguardando conferencia, `3`=Em processo de conferencia, `5`=Conferencia validada, `6`=Concluido, `0`=Aguardando separação, `1`=Em processo de separação, `8`=Pedido totalmente cortado, `7`=Aguardando conferencia de volumes

**Opções `SITUACAOANT`:** `4`=Conferencia com divergencia, `3`=Em processo de conferencia, `2`=Aguardando conferencia, `1`=Em processo de separação, `0`=Aguardando separação, `8`=Aguardando recontagem, `7`=Aguardando conferencia de volumes, `5`=Conferencia validada

**Opções `TIPOSEP`:** `B`=Balção, `P`=Pedido, `O`=Ordem Carga

### TGWARS
**Area de Separação**

**PK:** `CODAREASEP`  
**Referenciada por:** 6 tabelas  
**entityName:** `AreaSeparacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAREASEP` 🔑 | Inteiro | Cod. Area Separação |  |
| `NOMEAREASEP` | Texto | Descrição |  |
| `CODAREACONF` | Inteiro | Cod. Area Conferencia | → `TGWARC`.`CODAREACONF` |
| `DHALTER` | Data/Hora | Dt. Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `TIPOSEP` | Texto | Tipo Separação |  |
| `M3MAX` | Decimal | Metros cubicos maximo |  |
| `PESOMAX` | Decimal | Peso maximo |  |
| `IMPRESSORAETQVOL` | Texto | Impressora da Etiqueta de Volume |  |
| `MODETQVOL` | Inteiro | Modelo de Etiqueta de Volume | → `TSIRFE`.`NURFE` |
| `USASEPAGRUPROD` | Texto | Utiliza separação agrupada por produto |  |
| `QTCHECKSEP` | Inteiro | Quantidade max. de checkouts por separação |  |
| `VOLCHECKSEPROD` | Decimal | Volumetria max. do checkout por separação(M3) |  |
| `QTDUMAPED` | Inteiro | Quantidade de Checkout por Pedido |  |
| `PESMAXSEPAGRU` | Decimal | Peso max. do checkout por separação |  |
| `QTPEDSEPAGR` | Inteiro | Quantidade de pedidos por separação |  |
| `VOLCONTINUO` | Texto | Volume Continuo |  |
| `AGRUPARPEDIDOSWMS` | Texto | Agrupar pedidos |  |
| `POSESTEIRASEP` | Texto | Posição na esteira de separação |  |
| `IMPRESSORAETQSEP` | Texto | Impressora p/ etiqueta de separação |  |
| `IMPETIQFECHVOL` | Texto | Imprimir etiqueta no fechamento do volume |  |
| `QUEBRAPORNORMA` | Texto | Quebra por Norma/Palete |  |
| `QTDSKU` | Inteiro | Quantidade de SKUs por separação |  |
| `TOLERANCIASKU` | Inteiro | Quantidade Tolerancia de SKUs por separação |  |

**Opções `AGRUPARPEDIDOSWMS`:** `N`=Não, `S`=Sim

**Opções `IMPETIQFECHVOL`:** `A`=Sim, conforme area de separação, `N`=Não usa, `S`=Sim, conforme empresa

**Opções `POSESTEIRASEP`:** `I`=Inicial, `M`=Intermediaria, `T`=Terminal, `N`=Nenhuma

**Opções `QUEBRAPORNORMA`:** `S`=Sim, `N`=Não

**Opções `TIPOSEP`:** `P`=Por Pedido, `L`=Por Produto

### TGWARA
**Area de Armazenagem**

**PK:** `NUAREA`  
**Referenciada por:** 4 tabelas  
**entityName:** `AreaArmazenagem`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAREA` 🔑 | Inteiro | Cod. Area Armazenagem |  |
| `DESCRICAO` | Texto | Descrição Area |  |
| `TIPO` | Texto | Tipo Armazenagem |  |
| `DHALTER` | Data/Hora | Dt. Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `REGRAPRODUTO` | Texto | Regra Produto |  |
| `REGRAGRUPO` | Texto | Regra Grupo de Produto |  |
| `REGRAPARCEIRO` | Texto | Parceiros Relacionados |  |

**Opções `REGRAGRUPO`:** `R`=Permitir, `P`=Proibir, `E`=Exclusivo

**Opções `REGRAPARCEIRO`:** `R`=Permitir, `P`=Proibir, `E`=Exclusivo

**Opções `REGRAPRODUTO`:** `R`=Permitir, `P`=Proibir, `E`=Exclusivo

**Opções `TIPO`:** `P`=Propria, `T`=Terceiros

### TGWARC
**Areas de Conferencia**

**PK:** `CODAREACONF`  
**Referenciada por:** 4 tabelas  
**entityName:** `AreaConferencia`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAREACONF` 🔑 | Inteiro | Cod. Area |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `NOMEAREACONF` | Texto | Descrição |  |
| `DHALTER` | Data/Hora | Data e Hora de Alteração |  |
| `IMPSEP` | Texto | Impressora padrão de etiquetas |  |

### TGWRPL
**Registros de Paletes**

**Referenciada por:** 5 tabelas  
**entityName:** `RegistroPalete`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDPALETE` | Inteiro | ID. Palete |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODPROD` | Inteiro | Produto |  |
| `CONTROLE` | Texto | Controle |  |
| `CODVOL` | Texto | Volume |  |
| `SEQPALETE` | Inteiro | Sequencia Palete |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `IMPRESSO` | Texto | Impresso |  |

**Opções `IMPRESSO`:** `S`=Sim, `N`=Não

### TGWIVT
**Inventarios do WMS**

**PK:** `NUIVT`  
**Referenciada por:** 3 tabelas  
**entityName:** `Inventario`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUIVT` 🔑 | Inteiro | Nro. Inventario |  |
| `DTINICIO` | Data/Hora | Dt. Inicial |  |
| `DTFINAL` | Data/Hora | Dt. Final |  |
| `TIPO` | Texto | Tipo |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODUSURESP` | Inteiro | Cod. Usuario Responsavel |  |
| `OBSERVACAO` | Texto | Observação |  |

**Opções `TIPO`:** `G`=Global, `R`=Rotativo, `I`=Implantação

### TGWTTR
**Tipos de Tarefa**

**PK:** `CODTAREFA`  
**Referenciada por:** 3 tabelas  
**entityName:** `TipoTarefa`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTAREFA` 🔑 | Inteiro | Cod. Tarefa |  |
| `DESCRTAREFA` | Texto | Descrição |  |

### TGWTAR
**TABLE TGWTAR**

**PK:** `NUTAREFA`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUTAREFA` 🔑 | Inteiro | Nro. Tarefa |  |
| `CODTAREFA` | Inteiro | Cod.Tarefa | → `TGWTTR`.`CODTAREFA` |
| `SITUACAO` | Texto | Situação |  |
| `NUTAREFAORIGEM` | Inteiro | Nro. Tarefa Origem |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `NUCONFERENCIA` | Inteiro | Nro. Conferencia | → `TGWCON`.`NUCONFERENCIA` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `CODPARC` | Inteiro | Parceiro |  |
| `DTALTER` | Data/Hora | Dt. Alteração |  |
| `DTTAREFA` | Data/Hora | Dh.Geração Tarefa |  |
| `SEQUENCIADEP` | Inteiro | Sequencia Dependente | → `TGWITT`.`SEQUENCIA` |
| `NUTAREFADEP` | Inteiro | Nro. Tarefa Dependente | → `TGWITT`.`NUTAREFA` |
| `NUIVT` | Inteiro | Nro.Inventario | → `TGWIVT`.`NUIVT` |
| `CODEMPOC` | Inteiro | Empresa OC | → `TGFORD`.`CODEMP` |
| `ORDEMCARGA` | Inteiro | Ordem de carga | → `TGFORD`.`ORDEMCARGA` |
| `PROATIVA` | Texto | Pro-ativa |  |

**Opções `SITUACAO`:** `C`=Cancelada, `A`=Em aberto, `E`=Em execução, `F`=Concluido

### TGWIVR
**Inventarios Rotativos do WMS**

**PK:** `NUIVT`, `SEQUENCIA`  
**entityName:** `InventarioRotativo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPODIVERGENCIA` | Texto | Tipo de Divergencia |  |
| `CODEND` | Inteiro | Endereco | → `TGWEND`.`CODEND` |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODVOL` | Texto | Volume | → `TGFVOL`.`CODVOL` |
| `CONTROLE` | Texto | Controle |  |
| `QTDESTCONTADA` | Decimal | Qtd. Contada |  |
| `QTDESTLOGICA` | Decimal | Qtd. Logica |  |
| `QTDESTLOGICAUMA` | Decimal | Qtd. Logica UMA |  |
| `QTDESTLOGICAUMAPAD` | Decimal | Qtd. Logica UMA Vol. Padrão |  |
| `DIVERGENCIA` | Decimal | Divergencia |  |
| `DHCONTAGEM` | Data/Hora | Data da Contagem |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `ATIVA` | Texto | Ativa |  |
| `NUIVT` 🔑 | Inteiro | Nro. Inventario | → `TGWIVT`.`NUIVT` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `NUAJUSTE` | Inteiro | Nro. Ajuste |  |
| `CODLOCAL` | Inteiro | Local | → `TGFLOC`.`CODLOCAL` |
| `QTDESTCONTADAPAD` | Decimal | Qtd. Contada Vol. Padrão |  |
| `QTDESTLOGICAPAD` | Decimal | Qtd. Logica Vol. Padrão |  |
| `DTREC` | Data | Dt. FIFO |  |
| `DIVERGENCIAPAD` | Decimal | Divergencia Vol. Padrão |  |
| `IDPALETE` | Inteiro | Id. Palete | → `TGWRPL`.`IDPALETE` |
| `DTVAL` | Data | Dt. Validade |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |

**Opções `ATIVA`:** `N`=Não, `S`=Sim

## TIM — Imobiliário

### TIMIMV
**Imoveis**

**PK:** `IMVCODIGO`  
**Referenciada por:** 22 tabelas  
**entityName:** `TimImovel`, `TimImovelPesquisa`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IMVCAPTADORVENDA` | Inteiro | Captador para Venda |  |
| `IMVGARAGEMCOBERTA` | Inteiro | Garagens Cobertas |  |
| `IMVCAPTADORLOC` | Inteiro | Captador de Locação |  |
| `IMVCARTDTREGISTRO` | Data | Data de Registro no Cartorio |  |
| `IMVCARTREGISTRO` | Texto | Registro do Imovel |  |
| `IMVCARTMATRICULA` | Texto | Matricula do Imovel |  |
| `IMVCARTLIVRO` | Texto | Livro de Registro no Cartorio |  |
| `IMVCARTFOLHA` | Texto | Folha do Livro de Registro |  |
| `IMVGARAGEMDESCOBERTA` | Inteiro | Garagens Descobertas |  |
| `IMVCONDFECHADO` | Texto | Condominio Fechado |  |
| `IMVCOZINHA` | Texto | Cozinha |  |
| `IMVPORTARIA` | Texto | Portaria |  |
| `IMVENDFINAL` | Texto | Endereco |  |
| `IMVUNIDADEMEDIDA` | Inteiro | Unidade de medida |  |
| `IMVBAIRRO` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `IMVIFEMURO` | Texto | Muro |  |
| `IMVESTAGIO` | Texto | Estagio |  |
| `IMVCODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `IMVINTMAPA` | Texto | Mostrar Mapa |  |
| `IMVIFESOL` | Texto | Sol |  |
| `IMVCIDADE` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `IMVEDIFICIO` | Inteiro | Edificio | → `TIMEDG`.`EDGCODIGO` |
| `IMVIFEDIVARMCOZINHA` | Texto | Armarios Cozinha |  |
| `IMVIFEDIVQTCOMARMARIO` | Inteiro | Quartos com armario |  |
| `IMVEDICULA` | Texto | Edicula |  |
| `IMVIFEDIVESTADO` | Texto | Estado Conservação |  |
| `IMVEMPREENDIMENTO` | Inteiro | Empreendimento | → `TIMEPR`.`EPRCODIGO` |
| `IMVDTFIMRESERVA` | Data | Fim Reserva |  |
| `IMVOBSERVACAO` | Texto | Ponto Referencia |  |
| `IMVREGISTROIPTU` | Texto | Registro IPTU |  |
| `IMVIFEDIVVAGASGARAGEM` | Inteiro | Vagas Garagem |  |
| `IMVIFEDIVPISCINA` | Texto | Piscina |  |
| `IMVASSINATURA` | Texto | Assinatura Anuncio |  |
| `IMVIFEDIVSUITES` | Inteiro | Suites |  |
| `IMVAPTO` | Inteiro | Apartamento |  |
| `IMVURLGOOGLEMAP` | Texto | URL Google Map |  |
| `IMVIFEGABARITO` | Texto | Gabarito |  |
| `IMVIFEDIVSALATV` | Texto | Sala de TV / Home Teather |  |
| `IMVIFEDIVQUARTOS` | Inteiro | Quartos |  |
| `IMVIFEESQUINA` | Texto | Esquina |  |
| `IMVIFEDIVEMPREGADA` | Texto | Dep. Empregada |  |
| `IMVIFEDIVREVERSIVEL` | Inteiro | Quartos Reversiveis |  |
| `IMVAREACONSTRUIDA` | Decimal | Area construida (m) |  |
| `IMVIFEFRENTE` | Texto | Frente |  |
| `IMVFRACAOIDEAL` | Texto | Fração Ideal |  |
| `IMVAREAPRIVTOTAL` | Decimal | Area privativa interna (m) |  |
| `IMVDOCUMENTACAO` | Inteiro | Documentação |  |
| `IMVIFEAREACONSTRUIDA` | Decimal | Area Construida (m) |  |
| `IMVIFEDIVSALAS` | Inteiro | Salas |  |
| `IMVDFVLCONDOMINIO` | Decimal | Vlr. Condominio |  |
| *... +62 campos* | | | |

**Opções `IMVATIVO`:** `N`=Não, `S`=Sim

**Opções `IMVCONDFECHADO`:** `N`=Não, `S`=Sim

**Opções `IMVCOZINHA`:** `S`=Sim, `N`=Não

**Opções `IMVEDICULA`:** `N`=Não, `S`=Sim

**Opções `IMVESTADO`:** `1`=Conservado, `2`=Mal conservado, `3`=Novo, `4`=Não informado, `0`=Bem conservado

### TIMLOC
**Locações**

**PK:** `LOCCODIGO`  
**Referenciada por:** 19 tabelas  
**entityName:** `TimLocacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `LOCTIPOIRRF` | Texto | Tipo do IRRF |  |
| `LOCRENEGOCIACAO` | Inteiro | Renegociação Ativa |  |
| `LOCCARENCIA` | Inteiro | Dias de Carencia p/ contrato |  |
| `LOCCODIGO` 🔑 | Inteiro | Numero |  |
| `LOCCARCORMONE` | Inteiro | Carencia p/ correção monetaria |  |
| `LOCENVIAJUR` | Texto | Envia Juridico Fech. aberto |  |
| `LOCAPRESENTACAO` | Texto | Descr. Contrato |  |
| `LOCESTAGIO` | Texto | Estagio |  |
| `LOCDATAENCERRAMENTO` | Data | Dt. Encerr. Contrato |  |
| `LOCIMOVEL` | Inteiro | Nro. Imovel | → `TIMIMV`.`IMVCODIGO` |
| `LOCCONTRATOADM` | Inteiro | Nro. Contrato Adm. | → `TIMADM`.`ADMNUCONTRATO` |
| `LOCPASTA` | Inteiro | Pasta Fisica |  |
| `LOCGARJUSTIFICATIVA` | Texto | Lembrete de Problema |  |
| `LOCIMOBILIARIA` | Inteiro | Imobiliaria | → `TIMIMB`.`IMBCODIGO` |
| `LOCCONTACORRENTE` | Inteiro | Conta Corrente | → `TSICTA`.`CODCTABCOINT` |
| `LOCCORRETOR` | Inteiro | Ger. de Carteira | → `TIMCOR`.`CORCODIGO` |
| `LOCATENDENTE` | Inteiro | Atendente | → `TIMCOR`.`CORCODIGO` |
| `LOCSEMBOLETO` | Texto | Bloquear Boleto |  |
| `LOCMOTIVOBLOQUEIO` | Texto | Motivo Bloqueio |  |
| `LOCTRANSFERENCIA` | Texto | E Transferencia |  |
| `LOCULTIMAAPRES` | Data | Dt. ultima apres. de contas |  |
| `LOCDHINC` | Data/Hora | Dh. Inclusão |  |
| `LOCCODUSUINC` | Inteiro | Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `LOCDHALTER` | Data/Hora | Dh. Alteração |  |
| `LOCUSUARIO` | Inteiro | Usuario Alteração | → `TSIUSU`.`CODUSU` |
| `LOCTIPOFPP` | Texto | Tipo FPP |  |
| `LOCVLRFPP` | Decimal | Vlr. FPP |  |
| `LOCPERCFPP` | Decimal | % FPP |  |
| `LOCCRD` | Decimal | CRD |  |
| `LOCDIAVENCCE` | Inteiro | Dia Venc. Condominio Especifico |  |
| `LOCDIAVENCCC` | Inteiro | Dia Venc. Condominio Comum |  |
| `LOCDIAVENCFPP` | Inteiro | Dia Venc. FPP |  |
| `LOCDIAVENCAP` | Inteiro | Dia Venc. AP |  |
| `LOCCRDAREA` | Decimal | Area |  |
| `LOCCRDLOCAL` | Decimal | Localização |  |
| `LOCCRDFORMATO` | Decimal | Formato |  |
| `LOCCRDVITRINE` | Decimal | Tamanho Vitrine |  |
| `LOCCRDATIVIDADE` | Decimal | Atividade |  |
| `LOCPRAZODELOCACAO` | Inteiro | Qtd. meses de locação |  |
| `LOCVALORMERCADO` | Decimal | Vlr. Aluguel |  |
| `LOCAVENCER` | Texto | Pagamento Antecipado |  |
| `LOCDIADEPAGAMENTO` | Inteiro | Dia de Vcto. |  |
| `LOCINDEXADOR` | Inteiro | Indice de Correção | → `TSIMOE`.`CODMOEDA` |
| `LOCREAJUSTE` | Texto | Periodicidade Reajuste |  |
| `LOCGARANTIA` | Texto | Tipo Garantia |  |
| `LOCDESTINACAO` | Texto | Destinação |  |
| `LOCATIVIDADE` | Texto | Atividade |  |
| `LOCDTINICPRIREAJUSTE` | Data | Dt. Inicio. Primeiro Reajuste |  |
| `LOCULTIMOREAJUSTE` | Data | Dt. Ultimo Reajuste |  |
| `LOCDATABASE` | Data | Dt. Proximo Reajuste |  |
| *... +27 campos* | | | |

**Opções `LOCAVENCER`:** `S`=Sim, `N`=Não

**Opções `LOCDESTINACAO`:** `2`=Misto, `1`=Residencial, `0`=Comercial

**Opções `LOCENVIAJUR`:** `N`=Não, `S`=Sim

**Opções `LOCESTAGIO`:** `ED`=Extinto - No juridico, `EF`=Ativo, `EJ`=Não Utilizar Este Estagio, `EX`=Extinto, `JU`=Ativo - No juridico, `RE`=Renegociado, `CA`=Cadastro, `SU`=Suspenso

**Opções `LOCGARANTIA`:** `OU`=Outros, `PO`=Caução/Poupanca, `SE`=Seguro, `SF`=Sem Fianca, `TC`=Titulo de Capitalização, `IM`=Imovel Caução, `FI`=Fiadores

### TIMCOR
**Corretores**

**PK:** `CORCODIGO`  
**Referenciada por:** 22 tabelas  
**entityName:** `TimCaptador`, `TimCaptadorImovel`, `TimCorretor`, `TimCorretor2`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CORCODIGO` 🔑 | Inteiro | Codigo |  |
| `CORNOMECARTAOVISITA` | Texto | Nome Cartão |  |
| `COREMAILCARTAOVISITA` | Texto | E-mail Cartão |  |
| `CORPARCEIRO` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CORIMOBILIARIA` | Inteiro | Imobiliaria | → `TIMIMB`.`IMBCODIGO` |
| `CORESTAGIO` | Texto | Ativo |  |
| `CORGERENTE` | Inteiro | Superior Imediato | → `TIMCOR`.`CORCODIGO` |
| `CORCENTROCUSTO` | Inteiro | Centro de Resultado |  |
| `CORDATAADMISSAO` | Data | Dt. Admissão |  |
| `CORDATADESLIGAMENTO` | Data | Dt. Desligamento |  |
| `CORREGIAO` | Inteiro | Região |  |
| `CORCRECI` | Inteiro | CRECI |  |
| `COREXPIRACRECI` | Data | Dt. Expiração |  |
| `CORLOCACAO` | Texto | Locação |  |
| `CORVENDA` | Texto | Venda |  |
| `CORECOLABORADOR` | Texto | Colaborador |  |
| `COREGERENTE` | Texto | Gerente |  |
| `CORSUPERVISOR` | Texto | Supervisor |  |
| `CORADMINISTRATIVO` | Texto | Administrativo |  |
| `CORCAPTADOR` | Texto | Captador |  |
| `CORCORRETOR` | Texto | Corretor |  |
| `CORESTAGIARIO` | Texto | Estagiario |  |
| `COREXTERNO` | Texto | Externo |  |
| `CORINDICADOR` | Texto | Indicador |  |
| `CORPASTA` | Inteiro | Nro. Pasta Fisica |  |
| `CORPROCESSO` | Inteiro | Nro. Processo |  |
| `CORPERIODO` | Texto | Periodo Atuação |  |
| `CORDTINICIOCONT` | Data | Dt. Inicio Contrato |  |
| `CORFIMCONTRATO` | Data | Dt. Fim Contrato |  |
| `COREPAUNIDGER` | Inteiro | Unidade gerencial |  |
| `COREPAINDICVENDA` | Texto | Indicador de venda |  |
| `COREPAVLRMETAIND` | Texto | Vlr. da meta individual |  |
| `COREPAVLRMETAGERENTE` | Texto | Vlr. da meta do gerente |  |
| `CORUSUARIO` | Inteiro | Usuario Inclusão |  |
| `CORUSUARIOALT` | Inteiro | Usuario Alteração |  |
| `CORDTINCLUSAO` | Data | Dt. Inclusão |  |

**Opções `CORADMINISTRATIVO`:** `S`=Sim, `N`=Não

**Opções `CORCAPTADOR`:** `S`=Sim, `N`=Não

**Opções `CORCORRETOR`:** `N`=Não, `S`=Sim

**Opções `CORECOLABORADOR`:** `S`=Sim, `N`=Não

**Opções `COREGERENTE`:** `N`=Não, `S`=Sim

### TIMLTV
**Contrato de Venda de Lote**

**PK:** `LTVCODIGO`  
**Referenciada por:** 15 tabelas  
**entityName:** `TimContratoVendaLote`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `FILTROCAMPRADOR` | Inteiro | Comprador |  |
| `FILTROLOTE` | Texto | Lote |  |
| `FILTROLOTEAMENTO` | Inteiro | Loteamento |  |
| `FILTROOLDCOMPRADOR` | Inteiro | Antigo Comprador |  |
| `FILTROQUADRA` | Texto | Quadra |  |
| `LTVGEROUPARCS` | Texto | Gerou Parcelas |  |
| `FILTROCPFPARCEIRO` | Texto | CPF Comprador |  |
| `LTVAPLICARFRUICAO` | Texto | Rescisão Conforme Lei do Distrato (n 13.786/2018) |  |
| `LTVCARENCIA` | Inteiro | Dias de Carencia p/ contrato |  |
| `LTVCODIGO` 🔑 | Inteiro | Codigo |  |
| `LTVCONTRATO` | Inteiro | Contrato |  |
| `LTVLOTE` | Inteiro | Lote | → `TIMLTE`.`LTECODIGO` |
| `LTVESTAGIO` | Texto | Estagio |  |
| `LTVDESCRICAO` | Texto | Descrição |  |
| `LTVLEGADO` | Texto | Legado |  |
| `LTVCODIGOSISLOTE` | Inteiro | Codigo SISLOTE |  |
| `LTVIMVESTIMENTO` | Texto | Comprou Para |  |
| `LTVUSUINCLUSAO` | Inteiro | Usuario Inclusão |  |
| `LTVUSUALTERACAO` | Inteiro | Usuario Alteração |  |
| `LTVDHINCLUSAO` | Data/Hora | Dh. Inclusão |  |
| `LTVDHALTERACAO` | Data/Hora | Dh. Alteração |  |
| `LTVDATANOTIFICACAO` | Data | Dt. Notificação |  |
| `LTVPROTOCOLO` | Texto | Protocolo |  |
| `LTVSITUACAO` | Texto | Sit. (Situação) |  |
| `LTVIMOBILIARIA` | Inteiro | Imobiliaria | → `TIMIMB`.`IMBCODIGO` |
| `LTVPRAZOESCRITURA` | Texto | Prazo de Escrituração |  |
| `LTVDATACADASTRO` | Data | Dt. Cadastro |  |
| `LTVASSINADOPROPRIETARIO` | Data | Dt. Ass. Proprietario |  |
| `LTVCCA` | Texto | Corte Concil. Arbitragem |  |
| `LTVPE` | Texto | Por. Edital |  |
| `LTVNC` | Texto | Notif. Cartorial |  |
| `LTVURGENCIA` | Texto | Urgencia |  |
| `LTVNAOCOBRAR` | Texto | Não cobrar |  |
| `LTVVISTORIA` | Texto | Vistoria |  |
| `LTVEMISSAOCONTRATO` | Data | Dt. Emissão escritura |  |
| `LTVJUSTICACOMUM` | Texto | Justica Comum |  |
| `LTVDTOCUPADO` | Data | Dt. Ocupação |  |
| `LTVDATADAVENDA` | Data | Dt. Venda |  |
| `LTVPRECODOLOTE` | Decimal | Vlr. Lote |  |
| `LTVDESCONTO` | Decimal | Vlr. Desconto |  |
| `LTVPERCDESCONTO` | Decimal | Vlr. Desconto % |  |
| `LTVPQDESCONTO` | Texto | Justif. Desconto |  |
| `LTVPRECOVENDIDO` | Decimal | Vlr. Venda |  |
| `LTVVALORFECHAMENTO` | Decimal | Vlr. Fechamento |  |
| `LTVTIPORECA` | Texto | Tipo Comissão |  |
| `LTVGERARECA` | Texto | Comissionar por |  |
| `LTVRECAADM` | Decimal | Vlr. Comissão Adminis. |  |
| `LTVRECAFRANQUIA` | Decimal | Vlr. Comissão Franquia |  |
| `LTVRECACORRETOR` | Decimal | Vlr. Comissão Corretor |  |
| `LTVCOMADMRECA` | Decimal | Comissão Adminis. % |  |
| *... +35 campos* | | | |

**Opções `LTVAPLICARFRUICAO`:** `N`=Não, `S`=Sim

**Opções `LTVCCA`:** `AJ`=Acordo Judicial, `SB`=Sobrestamento, `AD`=Audiencia, `ST`=Sentenca, `AR`=Arquivado, `HA`=Homologação de Acordo, `NI`=<Não informado>, `OU`=Outros

**Opções `LTVCOREXTERNO`:** `S`=Sim, `N`=Não

**Opções `LTVESTAGIO`:** `CO`=Contrato, `CA`=Cancelado, `CP`=Contrato para assinar, `CS`=Contrato assinado, `EC`=Em cobranca, `ES`=Escriturado, `HI`=Historico, `JU`=Juridico, `PC`=Proposta Cancelada, `PR`=Proposta, `PV`=Pre-Venda, `QI`=Quitado

**Opções `LTVGERARECA`:** `S`=Nota de Comissão RECA, `N`=Parcelas Diferenciadas

### TIMCLA
**Contratos de Venda**

**PK:** `CLACODIGO`  
**Referenciada por:** 13 tabelas  
**entityName:** `TimContratoVenda`, `TimContratoVendaAvaLocacao`, `TimContratoVendaAvaVenda`, `TimContratoVendaCorrespBanc`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CLACODIGO` 🔑 | Inteiro | Codigo |  |
| `FILTROVENDEDOR` | Inteiro | Vendedor |  |
| `FILTROCOMPRADOR` | Inteiro | Comprador |  |
| `CLADESCRICAO` | Texto | Descrição |  |
| `CLAIMOVEL` | Inteiro | Imovel | → `TIMIMV`.`IMVCODIGO` |
| `CLACONTRATOADM` | Inteiro | Contrato de Adm. | → `TIMADM`.`ADMNUCONTRATO` |
| `CLAEMPREENDIMENTO` | Inteiro | Empreendimento | → `TIMEPR`.`EPRCODIGO` |
| `CLATIPO` | Texto | Tipo do Contrato |  |
| `CLAINVESTIMENTO` | Texto | Finalidade |  |
| `CLAESTAGIO` | Texto | Estagio |  |
| `CLAVALORTOTAL` | Decimal | Vlr. Total |  |
| `CLACOMISSAO` | Decimal | Comissão (%) |  |
| `CLACOMISSAOVALOR` | Decimal | Vlr. Comissão Recebida |  |
| `CLACORRETOR` | Inteiro | Corretor | → `TIMCOR`.`CORCODIGO` |
| `CLACORRBANCARIO` | Decimal | Vlr. Corresp. Bancario |  |
| `CLAGERENTECOR` | Inteiro | Supervisor | → `TIMCOR`.`CORCODIGO` |
| `CLAGERGERCOR` | Inteiro | Gerente | → `TIMCOR`.`CORCODIGO` |
| `CLAPERCENTUALPARCERIA` | Decimal | Parceria (%) |  |
| `CLAVALORMETA` | Decimal | Vlr. Final |  |
| `CLAVGV` | Decimal | Valor Geral de Venda |  |
| `CLADATAMOTIFICADAO` | Data | Dt. Notificação |  |
| `CLANAOCOBRAR` | Texto | Não Cobrar |  |
| `CLANC` | Texto | Notif. Cartorial |  |
| `CLAPE` | Texto | Por Edital |  |
| `CLAPROTOCOLO` | Inteiro | Protocolo |  |
| `CLAJUSTICACOMUN` | Texto | Justica Comum |  |
| `CLAACC` | Texto | Ação de Conciliação |  |
| `CLAIMOBILIARIA` | Inteiro | Imobiliaria | → `TIMIMB`.`IMBCODIGO` |
| `CLACONDICOESDAVENDA` | Texto | Condições Venda |  |
| `CLACONDICOESDAPOSSE` | Texto | Condições Posse |  |
| `CLAENTREGACHAVES` | Data | Dt. Entrega de Chaves |  |
| `CLADATAASSINATURA` | Data | Dt. Assinatura |  |
| `CLADATADAPROPOSTA` | Data | Dt. Proposta |  |
| `CLADATACANCELAMENTO` | Data | Dt. Cancelamento |  |
| `CLADATADIGITACAO` | Data/Hora | Dh. Cadastro |  |
| `CLADHALTER` | Data/Hora | Dh. Alteração |  |
| `CLAVALORDOSINAL` | Decimal | Vlr. Sinal |  |
| `CLANUCHECKLIST` | Inteiro | CheckList do contrato | → `TIMCHK`.`CHKNUCHECK` |

**Opções `CLAACC`:** `AC`=Acordo Judicial, `AR`=Arquivado, `AU`=Audiencia, `HO`=Homologação de Acordo, `OU`=Outros, `SO`=Sobrestamento, `SE`=Sentenca

**Opções `CLAESTAGIO`:** `PR`=Proposta Assinada, `PE`=Pendente, `HA`=Habite-se, `FZ`=Finalizado, `FI`=Financiamento, `ES`=Escrituração, `RE`=Registro, `CA`=Cancelado, `CO`=Contrato

**Opções `CLAINVESTIMENTO`:** `IN`=Investimento, `FA`=Uso Familia, `AL`=Aluguel, `MO`=Moradia

**Opções `CLAJUSTICACOMUN`:** `N`=Não, `S`=Sim

**Opções `CLANAOCOBRAR`:** `N`=Não, `S`=Sim

### TIMADM
**Contrato de Administração do Imovel**

**PK:** `ADMNUCONTRATO`  
**Referenciada por:** 7 tabelas  
**entityName:** `TimContratoAdm`, `TimContratoAdmAtivo`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ADMIMOVEL` | Inteiro | Nro. Imovel | → `TIMIMV`.`IMVCODIGO` |
| `ADMCARENCIALOC` | Inteiro | Dias de Carencia p/ contrato |  |
| `ADMDESCRIMOVEL` | Texto | Descrição Imovel |  |
| `ADMNUCONTRATO` 🔑 | Inteiro | Nro. Contrato |  |
| `ADMDATA` | Data | Dt. Contrato |  |
| `ADMLOCACAO` | Texto | Imovel para locação |  |
| `ADMDATADESOCUPADO` | Data | Dt. Baixa Locação |  |
| `ADMVENDA` | Texto | Imovel para venda |  |
| `ADMDIASUTEISCALCPROP` | Texto | Qtd. Dias Mes Proporcionalizar |  |
| `ADMDATADESOCUPADOVENDA` | Data | Dt. Baixa Venda |  |
| `ADMESTAGIO` | Texto | Estagio |  |
| `ADMCAPTADOR` | Inteiro | Captador | → `TIMCOR`.`CORCODIGO` |
| `ADMDESTINACAO` | Texto | Destinação |  |
| `ADMPRAZOADM` | Inteiro | Vigencia p/ Adm em Meses |  |
| `ADMPRAZOLOC` | Inteiro | Vigencia p/ Locação em Meses |  |
| `ADMDATALIBERACAO` | Data | Dt. Captação |  |
| `ADMTIPOTXADM` | Texto | Tipo de Tx Adm |  |
| `ADMIMOBILIARIA` | Inteiro | Imobiliaria Locação | → `TIMIMB`.`IMBCODIGO` |
| `ADMDFCOMISSAOADM` | Decimal | Tx. Adm. (%) |  |
| `ADMDFPRECOALUGUEL` | Decimal | Vlr. Aluguel |  |
| `ADMINDICETXADM` | Inteiro | Indice para Tx Adm | → `TSIMOE`.`CODMOEDA` |
| `ADMEXCLUSIVOLOC` | Texto | Loc. Exclusiva |  |
| `ADMTXADMVLR` | Decimal | Tx Adm (Valor) |  |
| `ADMPORQUEDESOCUPOU` | Texto | Motivo Baixa Locação |  |
| `ADMCONDLOC` | Texto | Condições Locação |  |
| `ADMDIASREPASSE` | Inteiro | Qtd. dias ate o repasse |  |
| `ADMDIASUTEIS` | Texto | Tipo Dias |  |
| `ADMPRIMEIROALUGUEL` | Texto | Cobrar Tx. Interm. |  |
| `ADMTAXADIFERENTE` | Decimal | Tx. Interm. (%) |  |
| `ADMPRIPARPRI` | Inteiro | Nro. parcela de inicio de cobranca |  |
| `ADMQTDPARPRI` | Inteiro | Diluido em (qtd. parc.) |  |
| `ADMJUSTIFICAINTER` | Texto | Justificativa Intermediação |  |
| `ADMIMOB2` | Inteiro | Imobiliaria Venda | → `TIMIMB`.`IMBCODIGO` |
| `ADMDFPRECODEVENDA` | Decimal | Vlr. Venda |  |
| `ADMDFCOMISSAO` | Decimal | Comissão (%) |  |
| `ADMDFQUITADO` | Texto | Quitado |  |
| `ADMDFFINANCIAMENTO` | Texto | Financiamento |  |
| `ADMDFPRESTACAO` | Decimal | Vlr. Prestação Financiamento |  |
| `ADMFINANCIAMENTOBCO` | Inteiro | Banco Financiamento |  |
| `ADMDFPOUPANCA` | Decimal | Vlr. Poupanca |  |
| `ADMDFSALDODEVEDOR` | Decimal | Vlr. saldo devedor |  |
| `ADMEXCLUSIVO` | Texto | Ven. Exclusiva |  |
| `ADMDIASOPCAO` | Inteiro | Qtd. dias exclusividade |  |
| `ADMDATAFIMOPCAO` | Data | Dt. Fim Exclusividade |  |
| `ADMCORRESPBANCARIO` | Texto | Correspondente Bancario |  |
| `ADMDFAGENTEFINANCEIRO` | Inteiro | Agente Financeiro |  |
| `ADMPQDESOCUPOU` | Texto | Motivo Baixa Venda |  |
| `ADMCONDICOESDAVENDA` | Texto | Condições Venda |  |
| `ADMVISITAS` | Texto | Visitas |  |
| `ADMOBSVISITAS` | Texto | Obs. sobre visitas |  |
| *... +21 campos* | | | |

**Opções `ADMCHAVES`:** `S`=Sim, `N`=Não

**Opções `ADMCOMPIMOVELDIFF`:** `S`=Sim, `N`=Não

**Opções `ADMCORRESPBANCARIO`:** `S`=Sim, `N`=Não

**Opções `ADMDESTAQUE`:** `S`=Sim, `N`=Não

**Opções `ADMDESTINACAO`:** `3`=Não Informado, `2`=Ambos, `0`=Comercial, `1`=Residencial

### TIMLOT
**TimLoteamento**

**PK:** `LOTCODIGO`  
**Referenciada por:** 6 tabelas  
**entityName:** `TimLoteamento`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `LOTCODIGO` 🔑 | Inteiro | Codigo |  |
| `LOTAPLICARFRUICAO` | Texto | Aplicar taxas de fruição |  |
| `LOTCARENCIA` | Inteiro | Dias de Carencia p/ contrato |  |
| `LOTESTAGIOAPRES` | Texto | Estagio de Lote apos rescisão |  |
| `LOTLOTEAMENTE` | Texto | Descrição |  |
| `LOTABREVIADO` | Texto | Descr. Abreviada |  |
| `LOTPROJETO` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `LOTPODEESCRITURAR` | Texto | Pode escriturar |  |
| `LOTESTAGIO` | Texto | Estagio |  |
| `LOTIMOBILIARIA` | Inteiro | Imobiliaria | → `TIMIMB`.`IMBCODIGO` |
| `LOTAVULSO` | Texto | Loteamento |  |
| `LOTGERENTE` | Inteiro | Gerente | → `TIMCOR`.`CORCODIGO` |
| `LOTEMPRESA` | Inteiro | Empresa p/ NF | → `TSIEMP`.`CODEMP` |
| `LOTPROPRIO` | Texto | Tipo de Contrato |  |
| `LOTPERCFRUICAO` | Decimal | Fruição % |  |
| `LOTDATADECADASTRO` | Data | Dt. Cadastro |  |
| `LOTCIDADE` | Inteiro | Cidade |  |
| `LOTBAIRRO` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `LOTLOCALIZACAO` | Texto | Localização |  |
| `LOTCARTORIOSUGE` | Inteiro | Cartorio Sugerido | → `TIMCAR`.`CARCODIGO` |
| `LOTMDLIVRO` | Texto | Livro |  |
| `LOTDATADECRETO` | Data | Dt. Decreto |  |
| `LOTDECRETO` | Texto | Decreto |  |
| `LOTMDREGISTRO` | Texto | Registro |  |
| `LOTMDDATA` | Data | Dt. Registro |  |
| `LOTMDCARTORIO` | Inteiro | Cartorio | → `TIMCAR`.`CARCODIGO` |
| `LOTMDFOLHA` | Texto | Folha |  |
| `LOTARQARQUIVO` | Inteiro | Arquivo |  |
| `LOTARQPASTA` | Texto | Pasta |  |
| `LOTARQGAVETA` | Inteiro | Gaveta |  |
| `LOTDTNAOCOBRAR` | Data/Hora | Definido Em |  |
| `LOTSEMBOLETO` | Texto | Bloquear Boleto |  |
| `LOTNAOCOBRAR` | Texto | Não cobrar |  |
| `LOTPQNAOCOBRAR` | Texto | Motivo |  |
| `LOTTOTALDAAREA` | Decimal | Total da Area |  |
| `LOTQUANTIDADEDELOTES` | Inteiro | Qtd. lotes |  |
| `LOTSOMACOMISSOES` | Decimal | Soma Comissões % |  |
| `LOTENTRADA` | Decimal | Total Comissões % |  |
| `LOTRECAADM` | Decimal | Comissão Adminis. % |  |
| `LOTSINAL` | Decimal | Comissão Corretor % |  |
| `LOTGERARECA` | Texto | Comissionar por |  |
| `LOTRECAPARCEIRO` | Decimal | Comissão Franqueada % |  |
| `LOTENTRADACOMPOE` | Texto | Compe o preco |  |
| `LOTPREMIO` | Decimal | Premio % |  |
| `LOTDESCPARCELA` | Decimal | Desconto por Pontualidade % |  |
| `LOTPLANOS` | Texto | Planos |  |
| `LOTTAXAPARTIC` | Decimal | Participação % |  |
| `LOTRECPARCELAS` | Texto | Onde Receber Parc. |  |
| `LOTTAXAADM` | Decimal | Tx. de Administração % |  |
| `LOTCONTACOMP` | Texto | Compartilhada |  |
| *... +24 campos* | | | |

**Opções `LOTAPLICARFRUICAO`:** `S`=Sim, `N`=Não

**Opções `LOTAVULSO`:** `FE`=Fechado, `NI`=<Não informado>, `AV`=Avulso

**Opções `LOTBASEPRICORR`:** `DV`=Desde Data da Venda, `VP`=Entre Venda e Primeira Parcela, `PP`=Desde Primeira Parcela

**Opções `LOTBASEPRIJUROS`:** `DV`=Desde Data da Venda, `PP`=Desde Primeira Parcela

**Opções `LOTCONTACOMP`:** `N`=Não, `S`=Sim

### TIMEPR
**Empreendimentos**

**PK:** `EPRCODIGO`  
**Referenciada por:** 8 tabelas  
**entityName:** `TimEmpreendimento`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `EPRCODIGO` 🔑 | Inteiro | Codigo |  |
| `EPREMPREENDIMENTO` | Texto | Empreendimento |  |
| `EPRDATADELANCAMENTO` | Data | Dt. Lancamento |  |
| `EPRDATADEENTREGA` | Data | Dt. Entrega |  |
| `EPREDIFICIO` | Inteiro | Edificio | → `TIMEDG`.`EDGCODIGO` |
| `EPRENDERECO` | Texto | Endereco |  |
| `EPRCODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `EPRCOMPLEMENTO` | Texto | Complemento |  |
| `EPRNUMERO` | Texto | Numero |  |
| `EPRCEP` | Texto | C.E.P. |  |
| `EPRBAIRRO` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `EPRCIDADE` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `EPRTIPO` | Texto | Tipo do empreendimento |  |
| `EPRAREA` | Decimal | Area |  |
| `EPRTORRES` | Inteiro | Torres |  |
| `EPRPAVIMENTOS` | Inteiro | Pavimentos por torre |  |
| `EPRANDARES` | Inteiro | Andares |  |
| `EPRAPTOPORANDAR` | Inteiro | Apartamentos por andar |  |
| `EPRSUBSOLO` | Inteiro | Sub-solo |  |
| `EPRELEVADORES` | Inteiro | Elevadores por torre |  |
| `EPRCOMISSAOVENDA` | Decimal | Comissão de venda |  |
| `EPRCOMISSAOCAPTACAO` | Decimal | Comissão de captação |  |
| `EPRRESUMIDO` | Texto | Nome resumido |  |
| `EPRIVV` | Inteiro | Indice de Velocidade de Vendas |  |
| `EPRMAXPARCELAS` | Inteiro | Maximo de parcelas |  |
| `EPRTIPOCOMISSAO` | Inteiro | Tipo de comissão |  |
| `EPRESTAGIO` | Texto | Estagio |  |
| `EPRUNIDADES` | Inteiro | Unidades |  |
| `EPRLANCAMENTO` | Texto | Lancamento |  |
| `EPRCOMISSAOGERENTE` | Decimal | Comissão do gerente |  |
| `EPRCOMISSAOSUPERVIS` | Decimal | Comissão do supervisor |  |
| `EPRGERENTEEMP` | Inteiro | Gerente do empreendimento |  |
| `EPRPROJETO` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `EPRCONTACORRENTE` | Inteiro | Conta corrente |  |
| `EPRUSUARIO` | Inteiro | Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `EPRUSUARIOALT` | Inteiro | Usuario Alteração | → `TSIUSU`.`CODUSU` |
| `EPRINDICEATECHAVES` | Inteiro | Indice ate as chaves |  |
| `EPRINDICEAPOSCHAVES` | Inteiro | Indice apos as chaves |  |
| `EPRJUROSATECHAVES` | Inteiro | Juros ate as chaves |  |
| `EPRJUROSAPOSCHAVES` | Inteiro | Juros apos as chaves |  |
| `EPRPERIODICIDADEATE` | Inteiro | Periodicidade ate as chaves |  |
| `EPRPERIODICIDADEAPOS` | Inteiro | Periodicidade apos as chaves |  |
| `EPRPROJCORBANCARIO` | Inteiro | Projeto Correspondente Bancario | → `TCSPRJ`.`CODPROJ` |
| `EPRNUFINMODCCV` | Inteiro | Financeiro Mod. CCV |  |
| `EPRNUFINMODCE` | Inteiro | Financeiro Mod. CE |  |
| `EPRNUFINMODCCF` | Inteiro | Financeiro Mod. CCF |  |
| `EPRNUFINMODFPPP` | Inteiro | Financeiro Mod. FPPP |  |
| `EPRNUFINMODFPPF` | Inteiro | Financeiro Mod. FPPF |  |
| `EPRNUFINMODAP` | Inteiro | Financeiro Mod. AP |  |
| `EPRNUFINMODCDU` | Inteiro | Financeiro Mod. CDU |  |

**Opções `EPRESTAGIO`:** `CA`=Cadastro, `CC`=Cancelado, `NE`=Negociação, `SE`=<SEM ESTAGIO>, `SU`=Suspenso, `AP`=Aprovação

**Opções `EPRLANCAMENTO`:** `N`=Não, `S`=Sim

**Opções `EPRTIPO`:** `LO`=Lote, `CX`=Caixa Economica Federal, `PA`=Predio de Apartamentos, `SH`=Shopping, `CF`=Condominio Fechado, `AL`=Aluguel, `AP`=Apartamentos, `CA`=Casas

**Opções `EPRTIPOCOMISSAO`:** `2`=Ambos, `1`=Lancamento, `0`=Rateio

### TIMDTL
**Detalhamentos**

**PK:** `DTLPARCELA`, `DTLCODIGO`  
**Referenciada por:** 8 tabelas  
**entityName:** `TimDetalhamento`, `TimDetalhamentoReneg`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTLDATAINCLUSAO` | Data/Hora | Dh. Inclusão |  |
| `DTLUSUARIOALT` | Inteiro | Usuario Alteração | → `TSIUSU`.`CODUSU` |
| `DTLUSUARIO` | Inteiro | Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `DTLTAXAADM` | Texto | Incide na tx. adm. |  |
| `DTLSERVICO` | Inteiro | Codigo da OS |  |
| `DTLREPASSAPARA` | Texto | Repassa para |  |
| `DTLRECEBEDE` | Texto | Recebe de |  |
| `DTLREAJUSTE` | Inteiro | Nro. Reajuste |  |
| `DTLRATEADO` | Inteiro | DTLRATEADO |  |
| `DTLPROPORCIONAL` | Texto | Proporcional |  |
| `DTLPARCELA` 🔑 | Inteiro | ID Parcela | → `TGFFIN`.`NUFIN` |
| `DTLORIGEM` | Texto | Tipo Parcela |  |
| `DTLIDENTIFICADOR` | Inteiro | DTLIDENTIFICADOR |  |
| `DTLHISTORICO` | Inteiro | Tipo do Detalhamento | → `TIMHCB`.`HCBCODIGO` |
| `DTLESTAGIO` | Inteiro | DTLESTAGIO |  |
| `DTLDTINIC` | Data | Dt. Inicio Periodo |  |
| `DTLDTFIM` | Data | Dt. Fim Periodo |  |
| `DTLDETALHAMENTO` | Inteiro | Detalhamento de origem |  |
| `DTLDATAMOV` | Data | Dt. Atual |  |
| `DTLVALOR` | Decimal | Valor |  |
| `DTLIRRF` | Texto | Incide no IRRF |  |
| `DTLJUROSMULTA` | Texto | Incide em juros e multa |  |
| `DTLNEGOCIACAO` | Inteiro | Negociação | → `TIMLCR`.`LCRCONTADOR` |
| `DLTRECALCIRRF` | Texto | Recalcular IRRF |  |
| `DTLCODIGO` 🔑 | Inteiro | Codigo |  |
| `DTLCOMPLEMENTO` | Texto | Complemento |  |
| `DTLCONTRATOLOC` | Inteiro | Contrato de Locação | → `TIMLCR`.`LCRCONTRATO` |
| `DTLDATAALTERACAO` | Data/Hora | Dh. Alteração |  |
| `DTLPARCEIRO` | Inteiro | Parceiro (Proprietario) | → `TGFPAR`.`CODPARC` |
| `DTLINCTXMINIMA` | Texto | Incide tx. minima adm. |  |
| `DTLDESVINCULADO` | Inteiro | Fin. Desvinculado | → `TGFFIN`.`NUFIN` |
| `DTLGARANTIDO` | Texto | Garantido |  |
| `DTLDHGERREPASSE` | Data/Hora | Dh. Ger. Repasse |  |
| `DTLCODIPTU` | Inteiro | Cod. IPTU | → `TIMPIP`.`PIPIPTU` |
| `DTLCODORIGEM` | Inteiro | Dtl. Origem | → `TIMDTL`.`DTLCODIGO` |
| `DTLIMOVEL` | Inteiro | Imovel | → `TIMPIP`.`PIPIMOVEL` |
| `DTLPARCELAIPTU` | Inteiro | Cod. Parcela IPTU | → `TIMPIP`.`PIPCODIGO` |
| `DTLFINDESP` | Inteiro | Despesa Gerada | → `TGFFIN`.`NUFIN` |
| `DTLCOMISSAOIPTU` | Decimal | Vlr. Comissão Iptu |  |
| `DTLORIGCOMISSAO` | Inteiro | Dtl Origem Comissão | → `TIMDTL`.`DTLCODIGO` |
| `DTLCOMPADM` | Texto | Compensação Adm |  |
| `DTLORIGRENEG` | Texto | Repactuação |  |
| `DTLPARCDESP` | Inteiro | Parceiro para despesa |  |
| `DTLDTVENCDESP` | Data | Dt. Vencimento Despesa |  |
| `DTLRENEG` | Inteiro | Detalhamento Origem Reneg. |  |
| `DTLNUFINRENEG` | Inteiro | Financeiro Origem Reneg. |  |
| `DTLCONTATO` | Inteiro | Contato (Beneficiario) | → `TGFCTT`.`CODCONTATO` |
| `DTLNUACERTO` | Inteiro | Nro. Acerto Compensação |  |

**Opções `DLTRECALCIRRF`:** `S`=Sim, `N`=Não

**Opções `DTLCOMPADM`:** `S`=Sim, `N`=Não

**Opções `DTLGARANTIDO`:** `S`=Sim, `N`=Não

**Opções `DTLINCTXMINIMA`:** `S`=Sim, `N`=Não

**Opções `DTLIRRF`:** `N`=Não, `S`=Sim

### TIMIMB
**Imobiliarias**

**PK:** `IMBCODIGO`  
**Referenciada por:** 10 tabelas  
**entityName:** `TimImobiliaria`, `TimImobiliariaFilial`, `TimImobiliariaMatriz`, `TimImobiliariaVenda`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IMBPARCEIRO` | Inteiro | Parceiro Imobiliaria | → `TGFPAR`.`CODPARC` |
| `IMBCODIGO` 🔑 | Inteiro | Codigo |  |
| `IMBIMOBILIARIA` | Texto | Descrição |  |
| `IMBCODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `IMBESTAGIO` | Texto | Ativo |  |
| `IMBGERENTE` | Inteiro | Gerente | → `TIMCOR`.`CORCODIGO` |
| `IMBIMOBILIARIAMATRIZ` | Inteiro | Imobiliaria Matriz |  |
| `IMBOBSERVACAO` | C | Observação |  |
| `IMBREGIAO` | Inteiro | Região |  |
| `IMBCRECI` | Inteiro | CRECI |  |
| `IMBEXPIRACRECI` | Data | Dt. Expiração |  |
| `IMBCODCENCUSADM` | Inteiro | Administrativo | → `TSICUS`.`CODCENCUS` |
| `IMBCODCENCUSLOCACAO` | Inteiro | Locação | → `TSICUS`.`CODCENCUS` |
| `IMBCODCENCUSVENDA` | Inteiro | Venda | → `TSICUS`.`CODCENCUS` |
| `IMBCODCENCUSREVENDA` | Inteiro | Revenda | → `TSICUS`.`CODCENCUS` |
| `IMBCODCENCUSLOTEAMENTO` | Inteiro | Loteamento | → `TSICUS`.`CODCENCUS` |
| `IMBCODCENCUSCORBANCARIO` | Inteiro | Corresp. Bancario | → `TSICUS`.`CODCENCUS` |
| `IMBCODCENCUSINCORPORA` | Inteiro | Incorporadora | → `TSICUS`.`CODCENCUS` |
| `IMBCODSERVTXADM` | Inteiro | Cod. Servico Tx. Adm | → `TGFPRO`.`CODPROD` |
| `IMBCODSERVTXINTER` | Inteiro | Cod. Servico Tx. Intermed. | → `TGFPRO`.`CODPROD` |
| `IMBSERIENOTATXADM` | Texto | Serie Nota Tx. Adm. |  |
| `IMBSERIENOTATXINTER` | Texto | Serie Nota Tx. Intermed. |  |
| `IMBTXMINADM` | Decimal | Taxa Minima Adm |  |
| `IMBTXALUPROP` | Texto | Tx. minima s/ aluguel proporcional |  |
| `IMBIDWIMOVEIS` | Texto | Cod. Wimoveis |  |
| `IMBIDIMOVELWEB` | Texto | Cod. Imovelweb |  |

**Opções `IMBESTAGIO`:** `N`=Não, `S`=Sim

**Opções `IMBTXALUPROP`:** `NC`=Não Cobrar, `CI`=Cobrar Integral, `CP`=Cobrar Proporcional

### TIMLTE
**Lotes**

**PK:** `LTECODIGO`  
**Referenciada por:** 4 tabelas  
**entityName:** `TimLote`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `LTECODIGO` 🔑 | Inteiro | Codigo |  |
| `LTEDESCRICAO` | Texto | Descrição |  |
| `LTEQUADRA` | Texto | Quadra |  |
| `LTELOTE` | Texto | Lote |  |
| `LTELOTEAMENTO` | Inteiro | Loteamento | → `TIMLOT`.`LOTCODIGO` |
| `LTEDHALTERACAO` | Data/Hora | Dh. Alteração |  |
| `LTEUSUINCLUSAO` | Inteiro | Usuario Inclusão |  |
| `LTEUSUALTERACAO` | Inteiro | Usuario Alteração |  |
| `LTEDATADECADASTRO` | Data/Hora | Dt. Cadastro |  |
| `LTEBENFEITORIAS` | Texto | Benfeitorias |  |
| `LTEENERGIA` | Texto | Energia |  |
| `LTESITUACAO` | Texto | Situação |  |
| `LTETIPOZONA` | Inteiro | Zona de uso | → `TIMTZL`.`TZLCODIGO` |
| `LTEOBS` | Texto | Observação |  |
| `LTEREGISTROITUIPTU` | Texto | Registro ITU/IPTU |  |
| `LTEULTIMOIPTU` | Data/Hora | Dh. Ultimo IPTU |  |
| `LTEBENFEITORIA` | Texto | Benfeitoria |  |
| `LTEAGUA` | Texto | Agua |  |
| `LTECOMPLEMENTO` | Texto | Complemento |  |
| `LTECEP` | Texto | C.E.P |  |
| `LTERUA` | Texto | Rua |  |
| `LTENUMERO` | Texto | Numero |  |
| `LTECODEND` | Inteiro | Endereco |  |
| `LTEBAIRRO` | Inteiro | Bairro |  |
| `LTECIDADE` | Inteiro | Cidade |  |
| `LTEX` | Inteiro | X |  |
| `LTEY` | Inteiro | Y |  |
| `LTEAREA` | Decimal | Area (m) |  |
| `LTEPRECODOMETRO` | Decimal | Vlr. M2 |  |
| `LTEVALORCOMPRA` | Decimal | Vlr. Compra |  |
| `LTEDESCPARCELA` | Decimal | Vlr. Desc. Parcelas |  |
| `LTEVLRLOTE` | Decimal | Vlr. Lote |  |
| `LTECNFFRENTE` | Texto | Conf. Frente |  |
| `LTECNFFUNDO` | Texto | Conf. Fundo |  |
| `LTECNFESQUERDA` | Texto | Conf. Esquerda |  |
| `LTECNFDIREITA` | Texto | Conf. Direita |  |
| `LTECNFCHANFRO` | Texto | Conf. Chanfro |  |
| `LTECNFVARIANTE` | Texto | Conf. Variante |  |
| `LTEMEDFRENTE` | Texto | Med. Frente |  |
| `LTEMEDFUNDO` | Texto | Med. Fundo |  |
| `LTEMEDESQUERDA` | Texto | Med. Esquerda |  |
| `LTEMEDDIREITA` | Texto | Med. Direita |  |
| `LTEMEDCHANFRO` | Texto | Med. Chanfro |  |
| `LTEMEDVARIANTE` | Texto | Med. Variante |  |
| `LTELIVRO` | Texto | Livro |  |
| `LTECARTORIO` | Inteiro | Cartorio | → `TIMCAR`.`CARCODIGO` |
| `LTEDATAREGISTRO` | Data | Dt. Registro |  |
| `LTEREGISTRO` | Texto | Registro |  |
| `LTEFOLHA` | Texto | Folha |  |
| `LTEESQUINA` | Texto | Esquina |  |
| *... +1 campos* | | | |

**Opções `LTEBENFEITORIA`:** `S`=Sim, `N`=Não

**Opções `LTEESQUINA`:** `S`=Sim, `N`=Não

### TIMEDG
**Edificios e Galerias**

**PK:** `EDGCODIGO`  
**Referenciada por:** 5 tabelas  
**entityName:** `TimEdificioGaleria`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `EDGCODIGO` 🔑 | Inteiro | Codigo |  |
| `EDGEDIFICIO` | Texto | Edificio / Galeria |  |
| `EDGCONSTRUTORA` | Inteiro | Construtora |  |
| `EDGEMPREENDIMENTO` | Inteiro | Empreendimento |  |
| `EDGPODEANIMAIS` | Texto | Pode animais |  |
| `EDGANDARES` | Inteiro | Andares |  |
| `EDGPAVIMENTOS` | Inteiro | Pavimentos |  |
| `EDGAPTOPORANDAR` | Inteiro | Aptos por Andar |  |
| `EDGELEVADORES` | Inteiro | Elevadores |  |
| `EDGTORRES` | Inteiro | Torres |  |
| `EDGSUBSOLO` | Inteiro | Sub-solos |  |
| `EDGANOCONSTRUCAO` | Inteiro | Ano Construção |  |
| `EDGIFEAREACONSTRUIDA` | Decimal | Area Construida Total (m) |  |
| `EDGCEP` | Texto | CEP |  |
| `EDGENDFINAL` | Texto | Endereco |  |
| `EDGENDERECO` | Texto | Endereco |  |
| `EDGCODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `EDGCOMPL` | Texto | Complemento |  |
| `EDGNUMERO` | Inteiro | Numero |  |
| `EDGBAIRRO` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `EDGCIDADE` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `EDGSINDICO` | Texto | Nome |  |
| `EDGTELEFONES` | Texto | Telefone |  |
| `EDGEMAIL` | Texto | E-Mail |  |
| `EDGADMNOME` | Texto | Nome |  |
| `EDGADMFONE` | Texto | Telefone |  |
| `EDGADMEMAIL` | Texto | E-Mail |  |
| `EDGCTBNOME` | Texto | Nome |  |
| `EDGCTBFONE` | Texto | Telefone |  |
| `EDGCTBEMAIL` | Texto | E-mail |  |
| `EDGRATEARPARA` | Inteiro | Ratear para |  |
| `EDGSEGINCTPCOB` | Inteiro | Tipo de cobranca do Seguro Incendio |  |
| `EDGGASNOME` | Texto | Fornecedor |  |
| `EDGGASFONE` | Texto | Telefone |  |
| `EDGGASEMAIL` | Texto | E-Mail |  |
| `EDGCODPARCEIRO` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |

**Opções `EDGPODEANIMAIS`:** `S`=Sim, `N`=Não

### TIMLVR
**Renegociações de Saldo**

**PK:** `LVRCODIGO`, `LVRCONTRATO`  
**Referenciada por:** 4 tabelas  
**entityName:** `TimRenegociacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `LVRQTDPARCABERTO` | Inteiro | Qtd. Parc's. Aberto |  |
| `LVRRENEGOCIACAO` | Texto | Renegociação |  |
| `LVRTXRENEG` | Decimal | Vlr. Tx. Juros Reneg. |  |
| `LVRCODIGO` 🔑 | Inteiro | Codigo |  |
| `LVRCONTRATO` 🔑 | Inteiro | Contrato | → `TIMLTV`.`LTVCODIGO` |
| `LVRALTERATABELA` | Texto | Altera para Price |  |
| `LVRDATA` | Data | Dt. Reneg. |  |
| `LVRSMJURMUL` | Decimal | Vlr. Soma Juros Multa |  |
| `LVRMAXDESC` | Decimal | Vlr. Limite Desconto |  |
| `LVRVALORPAGO` | Decimal | Vlr. Pago |  |
| `LVRVLPAGORENEGOC` | Decimal | Vlr. Amort. Saldo Dev. |  |
| `LVRQTDPARPAGAS` | Inteiro | Qtd. Parc's. Pagas |  |
| `LVRVALOREMATRASO` | Decimal | Vlr. Em Atraso |  |
| `LVRPARCELASEMATRASO` | Inteiro | Qtd. Parc's. Atraso |  |
| `LVRVLRTOTALINTERMED` | Decimal | Vlr. Total Intermediarias |  |
| `LVRDESCONTO` | Decimal | Vlr. Desconto |  |
| `LVRPQDESCONTO` | Texto | Justificativa Desconto |  |
| `LVRJUROS` | Decimal | Tx. Reneg. % |  |
| `LVRAPROVEITASALDO` | Texto | Aproveit. Saldo |  |
| `LVRVALOREMABERTO` | Decimal | Vlr. Em Aberto |  |
| `LVRMAISJUROS` | Decimal | Tx. Juros % |  |
| `LVRVALORPARCELA` | Decimal | Vlr. Parcela |  |
| `LVRDTPRIPARCELA` | Data | Dt. Primeira Parc. |  |
| `LVRPRIPARCELA` | Inteiro | Nro. Primeira Parc. |  |
| `LVRESTAGIO` | Texto | Estagio |  |
| `LVRNUACERTO` | Inteiro | Nro. Acerto |  |
| `LVRFINCOMPENSAMORT` | Inteiro | Nro. Fin. Compensar | → `TGFFIN`.`NUFIN` |
| `LVROLDPROXREAJUSTE` | Data/Hora | Dt. Old Prox. Reajuste |  |
| `LVRCORRECAO` | Decimal | Vlr. Correção |  |
| `LVRDESCAP` | Decimal | Vlr. Descaptalização |  |
| `LVRDTAMORTSALDO` | Data | Dt. Amort. Saldo Dev. |  |
| `LVRFINBANCODEVOLVER` | Inteiro | Nro. Fin. Devolver Banco |  |
| `LVRNURENEG` | Inteiro | Nro. Reneg. Skw |  |
| `LVRVLRBANCOFECHADO` | Decimal | Vlr. Fechado Banco |  |
| `LVRFECHAMENTOBANCO` | Texto | Fechamento Banco |  |
| `LVRVLRBANCODIFER` | Decimal | Vlr. Diferenca Banco |  |
| `LVRVLRBANCOATUAL` | Decimal | Vlr. Atual Banco |  |
| `LVRVLRBANCODEVOLVER` | Decimal | Vlr. Devolver Banco |  |
| `LVRQTDPARCELAS` | Inteiro | Qtd. Parcelas |  |
| `LVROLDJUROS` | Decimal | Tx. Juros Anterior % |  |
| `LVRVLAPARCELAR` | Decimal | Vlr. Refinanciar |  |
| `LVRVLRTOTALBALAO` | Decimal | Vlr. Total Balões |  |

**Opções `LVRALTERATABELA`:** `S`=Sim, `N`=Não

**Opções `LVRAPROVEITASALDO`:** `S`=Sim, `N`=Não

**Opções `LVRESTAGIO`:** `AB`=Aberta, `CA`=Cancelada, `CP`=Com Parcelas, `EF`=Efetivada

**Opções `LVRFECHAMENTOBANCO`:** `S`=Sim, `N`=Não

### TIMFAC
**Ficha de Atendimento ao Cliente**

**PK:** `FACCODIGO`  
**Referenciada por:** 4 tabelas  
**entityName:** `TimFichaAtendimentoCliente`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `FACCODIGO` 🔑 | Inteiro | Codigo |  |
| `FACNOMEPPROSPECT` | Texto | Nome Prospect |  |
| `FACPROSPECT` | Inteiro | Prospect |  |
| `FACBUSCAPOR` | Texto | Interesse em |  |
| `FACCORRETOR` | Inteiro | Corretor | → `TIMCOR`.`CORCODIGO` |
| `FACESTAGIO` | Texto | Estagio |  |
| `FACORIGEM` | Texto | Origem |  |
| `FACVEICULO` | Inteiro | Veiculo de Comunicação | → `TIMVCO`.`VCOCODIGO` |
| `FACCAPTACAO` | Texto | Captação |  |
| `FACCODPARC` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `FACRETORNAR` | Data/Hora | Dt. Retorno |  |
| `FACOBSERVACAO` | Texto | Observação |  |
| `FACTIPOIMOVEL` | Inteiro | Tipo de imovel | → `TIMTPI`.`TPICODIGO` |
| `FACVALORPEDIDO` | Decimal | Valor pedido |  |
| `FACQUARTOS` | Inteiro | Quartos |  |
| `FACBAIRROIMOVEL` | Inteiro | Bairro do imovel | → `TSIBAI`.`CODBAI` |
| `FACEMPREENDIMENTO` | Inteiro | Empreendimento | → `TIMEPR`.`EPRCODIGO` |
| `FACEDIFICIO` | Inteiro | Edificio | → `TIMEDG`.`EDGCODIGO` |
| `FACUSUARIO` | Inteiro | Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `FACLANCAMENTO` | Data/Hora | Dh. Inclusão |  |
| `FACUSUALTER` | Inteiro | Usuario Alteração | → `TSIUSU`.`CODUSU` |
| `FACDHALTER` | Data/Hora | Dh. Alteração |  |
| `FACSITUACAOCHAVE` | Texto | Situação Chaves |  |
| `FACDOCCHAVE` | Texto | Doc. Entrega Chaves |  |
| `FACDHENTCHAVE` | Data/Hora | Dh. Entrega Chaves |  |
| `FACDHDEVCHA` | Data/Hora | Dh. Dev. Chaves |  |
| `FACMEDIAALUGFAC` | Decimal | Media Vlr. Alugueis Imoveis Fac |  |

**Opções `FACBUSCAPOR`:** `CB`=Corresp. Bancario, `CL`=Captação para locação, `AL`=Avaliação para locação, `AV`=Avaliação para venda, `CO`=Comprar, `LO`=Alugar, `VE`=Captação para Venda

**Opções `FACESTAGIO`:** `F`=Com Sucesso, `R`=Retorno Futuro, `D`=Sem Sucesso, `C`=Em Proposta, `E`=Em Atendimento, `P`=Prospecção, `N`=Negociação, `I`=Em Visita

**Opções `FACORIGEM`:** `P`=Plano Piloto, `X`=Feirão Caixa, `I`=Lista Telefonica, `F`=Redes Sociais, `C`=Prospecção Rua, `B`=Parceria, `L`=Ligação, `V`=Visita, `S`=Internet, `R`=Prospecção Telefone

**Opções `FACSITUACAOCHAVE`:** `D`=Desistiu, `R`=Reservou, `E`=Entregue

### TIMLCR
**Negociações**

**PK:** `LCRCONTRATO`, `LCRCONTADOR`  
**Referenciada por:** 4 tabelas  
**entityName:** `TimNegociacao`, `TimUltimaNegociacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `LCRCODIGO` | Inteiro | Codigo |  |
| `LCRCONTRATO` 🔑 | Inteiro | Contrato | → `TIMLOC`.`LOCCODIGO` |
| `LCRCONTADOR` 🔑 | Inteiro | Nro. Negociação |  |
| `LCRESTAGIO` | Texto | Estagio |  |
| `LCRDIAVENC` | Inteiro | Dia de Vcto. |  |
| `LCRDTPRIVENC` | Data | Dt. Primeiro Venc. |  |
| `LCRDATAINICIO` | Data | Dt. Inicio Vigencia |  |
| `LCRPRAZOLOCACAO` | Inteiro | Qtd. meses de locação |  |
| `LCRDATATERMINO` | Data | Dt. Termino Vigencia |  |
| `LCRVALORALUGUEL` | Decimal | Vlr. Aluguel Negociado |  |
| `LCRISENTATARIFABOL` | Texto | Isenta tarifa do boleto |  |
| `LCRAPOLICE` | Texto | Apolice |  |
| `LCRVALORSEGURO` | Decimal | Vlr. Seguro |  |
| `LCRINICIOSEGURO` | Data | Dt. Inicio Seguro |  |
| `LCRTERMINOSEGURO` | Data | Dt. Termino Seguro |  |
| `LCRSEGADM` | Texto | Feito com a administradora |  |
| `LCROBSERVACAO` | Texto | Observação |  |
| `LCRGEROUPARCELAS` | Texto | Gerou parcelas |  |
| `LCRSEGURADORA` | Texto | Seguradora |  |
| `LCRDATARENEGOCIACAO` | Data/Hora | Dh. Inclusão |  |
| `LCRCODUSUINC` | Inteiro | Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `LCRDHALTER` | Data/Hora | Dh. Alteração |  |
| `LCRUSUARIO` | Inteiro | Usuario Alteração | → `TSIUSU`.`CODUSU` |
| `LCRQTDMPRO` | Inteiro | Qtd. Meses Prorrogados |  |
| `LCRVALORALUGUELATUAL` | Decimal | Vlr. Aluguel Atualizado |  |

**Opções `LCRESTAGIO`:** `EX`=Extinto, `JU`=Ativo - No juridico, `RE`=Renegociado, `SU`=Suspenso, `VE`=Vencido, `EJ`=Não Utilizar Este Estagio, `CA`=Cadastro, `EC`=Aguardando Exclusão, `ED`=Extinto - No juridico, `EF`=Ativo

**Opções `LCRGEROUPARCELAS`:** `S`=Sim, `N`=Não

**Opções `LCRISENTATARIFABOL`:** `N`=Não, `S`=Sim

**Opções `LCRSEGADM`:** `S`=Sim, `N`=Não

### TIMCAR
**Cartorios**

**PK:** `CARCODIGO`  
**Referenciada por:** 5 tabelas  
**entityName:** `TimCartorio`, `TimCartorioAverbacao`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CARCODIGO` 🔑 | Inteiro | Codigo |  |
| `CARPARCEIRO` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CARCARTORIO` | Texto | Descrição |  |
| `CARCEP` | Texto | CEP |  |
| `CARENDFINAL` | Texto | Endereco |  |
| `CARCODEND` | Inteiro | Endereco |  |
| `CARENDERECO` | Texto | Endereco |  |
| `CARCOMPLEMENTO` | Texto | Complemento |  |
| `CARNUMEND` | Texto | Numero |  |
| `CARBAIRRO` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CARCIDADE` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `CARTELEFONES` | Texto | Telefone |  |
| `CAROBSERVACAO` | Texto | Observação |  |

### TIMPRF
**Profissões e Ramos de Atividade**

**PK:** `PRFCODIGO`  
**Referenciada por:** 5 tabelas  
**entityName:** `TimProfissaoAtividadeGrupo`, `TimProfissaoConjuge`, `TimProfissaoRamoAtividade`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `PRFCODIGO` 🔑 | Inteiro | Codigo |  |
| `PRFTIPO` | Inteiro | Tipo |  |
| `PRFAGRUPADOR` | Inteiro | Agrupador | → `TIMPRF`.`PRFCODIGO` |
| `PRFPROFISSAO` | Texto | Profissão |  |

**Opções `PRFTIPO`:** `1`=Profissão/ramo de atividade, `0`=Agrupador
