# Tabelas TGF — Core Comercial e Operacional

Tabelas centrais do backoffice Sankhya: parceiros, produtos, notas fiscais,
financeiro, estoque, ordens de carga, tabelas de preço e configuração operacional.

## Relacionamento Central
```
TGFPAR ←── TGFCAB ──→ TGFTOP (tipo operação)
             │
             ├──→ TGFITE ──→ TGFPRO
             │      └──→ TGFLOC / TGFVOL
             └──→ TGFFIN (títulos financeiros)

TSIEMP (empresa) ←── TGFCAB, TGFITE, TGFFIN
TGFVEN (vendedor) ←── TGFCAB
TGFEST (estoque) = posição por TGFPRO + TGFLOC
```

### TGFPAR
**Parceiros**

**PK:** `CODPARC`  
**Referenciada por:** 152 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `SALDODISPCAC` | Decimal | Saldo disponivel do carrinho |  |
| `PROVACRESCCAC` | Decimal | Provisão do carrinho |  |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro |  |
| `DESCRROTA` | Texto | Descrição da Rota |  |
| `NOMEPARC` | Texto | Nome Parceiro |  |
| `RAZAOSOCIAL` | Texto | Razão social |  |
| `ATIVO` | Texto | Ativo |  |
| `TIPPESSOA` | Texto | Tipo de pessoa |  |
| `CLIENTE` | Texto | Cliente |  |
| `FORNECEDOR` | Texto | Fornecedor |  |
| `VENDEDOR` | Texto | Vendedor |  |
| `USUARIO` | Texto | Usuario |  |
| `TRANSPORTADORA` | Texto | Transportadora |  |
| `AGENCIA` | Texto | Agencia |  |
| `CTAADIANT` | Texto | Conta Adiantamento |  |
| `MOTORISTA` | Texto | Motorista |  |
| `MEDICO` | Texto | Medico |  |
| `AGRONOMO` | Texto | Agronomo |  |
| `CODPARCGRUECONOMICO` | Inteiro | Cod. Grupo Economico | → `TGFPAR`.`CODPARC` |
| `CODPARCMATRIZ` | Inteiro | Matriz | → `TGFPAR`.`CODPARC` |
| `CODVEND` | Inteiro | Vend. Preferencial | → `TGFVEN`.`CODVEND` |
| `CODGRUPO` | Inteiro | Grupo Cobranca | → `TGFGCB`.`CODGRUPO` |
| `CODASSESSOR` | Inteiro | Assessor do Parceiro | → `TGFVEN`.`CODVEND` |
| `CODBCO` | Inteiro | Banco | → `TSIBCO`.`CODBCO` |
| `CODAGE` | Texto | Agencia bancaria |  |
| `NOMEAGE` | Texto | Nome da agencia |  |
| `CODCTABCO` | Texto | Conta bancaria parceiro |  |
| `AGRUPAR` | Texto | Agrupar Pagamentos na geração p/Banco |  |
| `CODCTABCOINT` | Inteiro | Conta bancaria empresa | → `TSICTA`.`CODCTABCOINT` |
| `CGC_CPF` | Texto | CNPJ / CPF |  |
| `CODTIPPARC` | Inteiro | Perfil Principal | → `TGFTPP`.`CODTIPPARC` |
| `IDENTINSCESTAD` | Texto | Insc. Estadual / Identidade |  |
| `TIMDATACI` | Data | Dt. Cart. Identidade |  |
| `INSCESTADNAUF` | Texto | Insc. Estadual na UF |  |
| `CEI` | Texto | Cad. Especifico do INSS - CEI |  |
| `TIMMAE` | Texto | Mõe |  |
| `TIMPAI` | Texto | Pai |  |
| `DIASEM` | Inteiro | Dia Visita |  |
| `TIMPROFISSAO` | Inteiro | Prof. / Ramo Atividade | → `TIMPRF`.`PRFCODIGO` |
| `SELECIONADO` | Texto | Seleção |  |
| `TIMSENHASITE` | Texto | Senha do Site |  |
| `INSCMUN` | Texto | Cad.Mun.Contribuintes |  |
| `CODUNIMED` | Texto | Cod. Unimed |  |
| `TIMSENHADESC` | Texto | Conf. Senha |  |
| `CEP` | Texto | CEP |  |
| `TIMREFERENCIA01` | Texto | Referencia 01 |  |
| `TIMREFERENCIA02` | Texto | Referencia 02 |  |
| `CODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NUMEND` | Texto | Numero |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CODBAI` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CODCID` | Inteiro | Cod. Cidade | → `TSICID`.`CODCID` |
| `CODREG` | Inteiro | Região | → `TSIREG`.`CODREG` |
| `CAIXAPOSTAL` | Texto | Caixa Postal |  |
| `TELEFONE` | Texto | Telefone |  |
| `RAMAL` | Inteiro | Ramal |  |
| `ENVIPEDEMAILTOP` | Texto | Envio email de pedido / nota |  |
| `FAX` | Texto | Celular/Fax |  |
| `EMAIL` | Texto | Email |  |
| `EVENDA` | Texto | Email p/ pedido de venda |  |
| `ECOMPRA` | Texto | Email p/ pedido de compra |  |
| `DTCAD` | Data | Data cadastramento |  |
| `CODUSU` | Inteiro | Cod. Usuario Alteração |  |
| `DTALTER` | H | Data alteração |  |
| `DTNASC` | Data | Data nascimento/Fundação |  |
| `IMPLAUDOLOTE` | Texto | Imprime laudo lote |  |
| `SITUACAO` | Texto | Situação |  |
| `TIMTELEFONE01` | Texto | Telefone 01 |  |
| `DTULTCONTATO` | H | Dt. Ultimo contato |  |
| `TIMTELEFONE02` | Texto | Telefone 02 |  |
| `PRAZOCONTATO` | Inteiro | Prazo p/ contato |  |
| `PRAZOPAG` | Inteiro | Prazo medio pagamento |  |
| `TOLERINADIMP` | Inteiro | Tolerancia p/ inadimplencia |  |
| `CODTAB` | Inteiro | Tabela de Preco | → `TGFNTA`.`CODTAB` |
| `GRUPOAUTOR` | Texto | Grupo de autorização |  |
| `LIMCRED` | Decimal | Limite de credito |  |
| `LIMCREDMENSAL` | Decimal | Limite credito mensal |  |
| `BLOQUEAR` | Texto | Bloquear venda a prazo |  |
| `MOTBLOQ` | Texto | Motivo de Bloqueio |  |
| `DESCBONIF` | Texto | Desconto bonificado |  |
| `DESCFIN` | Decimal | % Desc. Financeiro |  |
| `TIPOFATUR` | Texto | Tipo de faturamento |  |
| `PERCCUSVAR` | Decimal | % de Custo Variavel |  |
| `DIASVARPAGTO` | Inteiro | Antecipação/Atraso recebimento(em dias) |  |
| `CONTACESSO` | Texto | Informações adicionais |  |
| `QTDMAXTITVENCIDOS` | Inteiro | Qtd. max. de titulos vencidos |  |
| `CLASSIFICMS` | Texto | Classificação ICMS |  |
| `CSTIPIENT` | Inteiro | Codigo Sit.Trib.IPI Entrada |  |
| `CSTIPISAI` | Inteiro | Codigo Sit.Trib.IPI Saida |  |
| `CODENQIPIENT` | Inteiro | Codigo Enq. Legal IPI Entrada |  |
| `CODENQIPISAI` | Inteiro | Codigo Enq. Legal IPI Saida |  |
| `INDNATRET` | Texto | Natureza da Retenção na Fonte |  |
| `CODCTACTB` | Inteiro | Conta contabil 1 | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB2` | Inteiro | Conta contabil 2 | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB3` | Inteiro | Conta contabil 3 |  |
| `CODCTACTB4` | Inteiro | Conta contabil 4 |  |
| `CODTABST` | Inteiro | Tabela c/base p/S.T.na venda | → `TGFNTA`.`CODTAB` |
| `MODELONFDES` | Texto | Modelo da nota fiscal |  |
| `SERIENFDES` | Texto | Serie da Nota Fiscal |  |
| `NATUREZAOPERDES` | Texto | Tipo de Negocio |  |
| *... +149 campos adicionais* | | | |

**Opções `AGENCIA`:** `N`=Não, `S`=Sim

**Opções `AGRONOMO`:** `N`=Não, `S`=Sim

**Opções `AGRUPAR`:** `S`=Sim, `N`=Não

**Opções `ALUNO`:** `N`=Não, `S`=Sim

**Opções `APLICLEITRANSP`:** `S`=Sim, `N`=Não

**Opções `ARREDPRIMEIRAPARC`:** `N`=Não, `S`=Sim

### TGFPRO
**Produtos**

**PK:** `CODPROD`  
**Referenciada por:** 123 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROD` 🔑 | Inteiro | Codigo |  |
| `ARMAZELOTE` | Texto | Armazena por Lote |  |
| `ONEROSO` | Texto | Oneroso |  |
| `CORFUNDOCONSPRECO` | Inteiro | Cor do Fundo |  |
| `CODFAB` | Inteiro | Cod. Fabricante | → `TGFPAR`.`CODPARC` |
| `CORFONTCONSPRECO` | Inteiro | Cor da Fonte |  |
| `CONTROLADO` | Texto | Controlado |  |
| `TIPO` | Texto | Tipo |  |
| `IDENCOSME` | Texto | Identificação de Cosmeceutico |  |
| `DESCRPROD` | Texto | Descrição |  |
| `IDENCORRELATO` | Texto | Identificação de Correlato |  |
| `DESCRPRODNFE` | Texto | Descrição para NFE |  |
| `CODPAT` | Inteiro | Princ. Ativo Medicamento | → `TGFPAT`.`CODPAT` |
| `ATIVO` | Texto | Ativo |  |
| `PRODFALTA` | Texto | Produto em Falta |  |
| `DTALTER` | H | Data de Alteração |  |
| `REFMERCMED` | Texto | Referencia no Mercado de Medicamento |  |
| `RENDIMENTO` | Texto | Rendimento |  |
| `IDENOTC` | Texto | Identificação de OTC |  |
| `COMPLDESC` | Texto | Complemento |  |
| `IDENPORTARIA` | Texto | Identificação de Portaria |  |
| `CODGRUPOPROD` | Inteiro | Grupo | → `TGFGRU`.`CODGRUPOPROD` |
| `STATUSMED` | Inteiro | Status do produto |  |
| `CODVOL` | Texto | Unidade padrão | → `TGFVOL`.`CODVOL` |
| `LISTALPM` | Texto | Lista de Procedimentos Medicos |  |
| `CODPARCFORN` | Inteiro | Parceiro Fornecedor preferencial | → `TGFPAR`.`CODPARC` |
| `TERMOLABIL` | Texto | Termolabil |  |
| `REFFORN` | Texto | Referencia do Fornecedor |  |
| `TEMPMINIMA` | Inteiro | Temperatura Minima em C |  |
| `FABRICANTE` | Texto | Fabricante |  |
| `TEMPMAXIMA` | Inteiro | Temperatura Maxima em C |  |
| `REFERENCIA` | Texto | Referencia |  |
| `CODCPR` | Inteiro | Classificação | → `TGFCPR`.`CODCPR` |
| `LOCALIZACAO` | Texto | Localização |  |
| `SEQSPR` | Inteiro | Sub-Classificação |  |
| `SELECIONADO` | Texto | Seleção |  |
| `CODCAT` | Inteiro | Categoria | → `TGFCAT`.`CODCAT` |
| `TEMPOSERV` | H | Tempo Estimado |  |
| `SEQSCA` | Inteiro | Sub-Categoria |  |
| `MARCA` | Texto | Marca |  |
| `CODMARCA` | Inteiro | Marca | → `TGFMAR`.`CODIGO` |
| `CODTER` | Inteiro | Classe Terapeutica | → `TGFTER`.`CODTER` |
| `SEQSTE` | Inteiro | Sub-Terapeutica |  |
| `LOCAL` | Texto | Local |  |
| `USALOCAL` | Texto | Usa local |  |
| `ESTMIN` | Decimal | Estoque Minimo |  |
| `ESTMAX` | Decimal | Estoque Maximo |  |
| `PROMOCAO` | Texto | Promoção |  |
| `DESCMAX` | Decimal | % Desconto Maximo |  |
| `GRUPODESCPROD` | Texto | Grupo Desconto |  |
| `TEMCOMISSAO` | Texto | Calcular comissão |  |
| `COMVEND` | Decimal | % Comissão vendedor |  |
| `COMGER` | Decimal | % Comissão gerente |  |
| `CODMOEDA` | Inteiro | Moeda p/ preco | → `TSIMOE`.`CODMOEDA` |
| `TIPLANCNOTA` | Texto | Digitação na nota |  |
| `PESOBRUTO` | Decimal | Peso bruto |  |
| `ARREDPRECO` | Decimal | Multiplo p/ Preco |  |
| `HOMEPAGE` | Texto | Home Page |  |
| `DECVLR` | Inteiro | Decimais para o valor |  |
| `DECQTD` | Inteiro | Decimais para quantidade |  |
| `ORIGPROD` | Texto | Origem do produto |  |
| `ENDIMAGEM` | Texto | Endereco da Imagem |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `MULTIPVENDA` | Decimal | Multiplicador para venda |  |
| `DECCUSTO` | Inteiro | Decimais para o custo |  |
| `CODFORMPREC` | Inteiro | Formula de precificação | → `TGFFOR`.`CODFORMPREC` |
| `CODFILTRO` | Inteiro | Filtro p/ Calc.Custo baseado no Financeiro |  |
| `CODFILTROREQ` | Inteiro | Filtro p/ Calc.Custo baseado na Requisição |  |
| `MEDAUX` | Decimal | Medida auxiliar |  |
| `HRDOBRADA` | Texto | Hora Dobrada |  |
| `TEMISS` | Texto | Tem ISS |  |
| `TEMIRF` | Texto | Tem IRF |  |
| `PERCIRF` | Decimal | % IRF |  |
| `REDBASEIRF` | Decimal | % Red. Base IRF |  |
| `PRAZOVAL` | Inteiro | Prazo validade/tolerancia |  |
| `MARGLUCRO` | Decimal | % Margem de lucro |  |
| `TIPCONTEST` | Texto | Tipo de controle de estoque |  |
| `USOPROD` | Texto | Usado como |  |
| `PERCAUMENTCUSTO` | Decimal | % Aviso Var. Custo |  |
| `CALCFUNTTELPRO` | Texto | Calcular FUNTTEL |  |
| `BLOQVENDAFRAC` | Texto | Bloquear venda fracionada |  |
| `TIPOITEMSPED` | Texto | Tipo do item p/ SPED |  |
| `TITCONTEST` | Texto | Titulo Controle de estoque |  |
| `CALCFUSTPRO` | Texto | Calcular FUST |  |
| `SERVDESPNTRIB` | Texto | Tratar servico como despesa não tributavel no JSON |  |
| `SERVPRESTTER` | Texto | Servico prestado por terceiro |  |
| `ALIQFETHAB` | Decimal | Aliquota FETHAB |  |
| `ALERTAESTMIN` | Texto | Alerta estoque minimo |  |
| `CODVOLCOMPRA` | Texto | Unid. Compra | → `TGFVOL`.`CODVOL` |
| `CODPRODROI` | Texto | Numero do Item (Portaria 384/01) |  |
| `AGRUPMIN` | Decimal | Agrupamento minimo |  |
| `CODGENERO` | Inteiro | Genero |  |
| `CODCENCUS` | Inteiro | Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODVOLFETHAB` | Texto | Unidade Padrão p/ FETHAB | → `TGFVOL`.`CODVOL` |
| `PRODINTERNO` | Texto | Considerar na Integração Impostos |  |
| `CARACTERISTICAS` | Texto | Caracteristicas |  |
| `IMAGEM` | Blob | Imagem |  |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `GERIMPNRETREINFAQ` | Texto | Gera Imposto não-retido evento 2055 da EFD-Reinf |  |
| `PERCINSSESPECIAL` | Decimal | % INSS Especial |  |
| *... +281 campos adicionais* | | | |

**Opções `ALERTAESTMIN`:** `S`=Sim, `N`=Não

**Opções `AP1RCTEGO`:** `S`=Sim, `N`=Não

**Opções `APLICASAZO`:** `N`=Não, `S`=Sim

**Opções `APRESDETALHE`:** `S`=Sim, `N`=Não

**Opções `APRESFORM`:** `N`=Não, `S`=Sim

**Opções `APURAPRODEPE`:** `01`=Sem incentivo, `02`=Com incentivo

### TGFCAB
**Entrada e Saida de Produto**

**PK:** `NUNOTA`  
**Referenciada por:** 97 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DESCTERMACORD` | Decimal | Desc. ref. termo de acordo CT-e |  |
| `TIMCODPROD` | Inteiro | Servico |  |
| `TIMDESCPROD` | Texto | Descrição (Servico da Nota) |  |
| `CODINTERM` | Inteiro | Intermediador da Transação | → `TGFPAR`.`CODPARC` |
| `INTERMED` | Texto | Indicador de Intermediador/Marketplace |  |
| `DISDESAUTIMPEMB` | Texto | Distribui desconto autom. com impostos embutidos |  |
| `CODCHECKOUT` | Inteiro | Cod. Checkout |  |
| `CLIENTEIDPARCERIA` | Decimal | Id do cliente no parceiro |  |
| `IDDESCPARCERIA` | Decimal | Id de desconto da parceria |  |
| `IDPONTUACAOPARCERIA` | Decimal | Id de pontuação no parceiro |  |
| `VLRDESCPARCERIA` | Decimal | Valor cupom desconto parceria |  |
| `DH_CODPRJETAPA` | Inteiro | Cod. Prj Item Etapa |  |
| `CODPARC` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `CODPARCRETIRADA` | Inteiro | Cod. Parceiro Retirada | → `TGFLCR`.`CODPARCRETIRADA` |
| `INDNEGMODAL` | Texto | Indicador negociavel Multimodal |  |
| `TIPSERVCTE` | Inteiro | Tipo de servico CT-e |  |
| `TIPOCTE` | Texto | Tipo do CT-e |  |
| `VLRFRETETOTAL` | Decimal | Vlr. Frete Total |  |
| `CODPARCTRANSPFINAL` | Inteiro | Transportadora Final | → `TGFPAR`.`CODPARC` |
| `LIBPENDENTE` | Texto | Liberação Pendente |  |
| `NUNOTA` 🔑 | Inteiro | Nro. Unico |  |
| `PEDIDOIMPRESSO` | Texto | Pedido foi impresso |  |
| `SITUACAOWMS` | Inteiro | Situação WMS |  |
| `STATUSCONFERENCIA` | Texto | Status conferencia |  |
| `STATUSWMS` | Texto | Status WMS |  |
| `TIPLIBERACAO` | Texto | Liberação |  |
| `VLRCOMPENSACAO` | Decimal | Valor do credito |  |
| `RETORNADOAC` | Texto | Entregue |  |
| `OBSERVACAOAC` | Texto | Observação |  |
| `DESCRHISTAC` | Texto | Descrição historico |  |
| `NUMNOTA` | Inteiro | Nro. Nota |  |
| `DTNEG` | Data | Dt. Neg. |  |
| `DTESCRCONT` | Data | Dt. Escrituração Contabil. |  |
| `VLRNOTA` | Decimal | Vlr. Nota |  |
| `SERIENFSE` | Texto | Serie NFS-e |  |
| `SERIENOTA` | Texto | Serie da nota |  |
| `CODEMP` | Inteiro | Empresa | → `TGFLCR`.`CODEMP` |
| `CODTIPOPER` | Inteiro | Tipo Operação | → `TGFTOP`.`CODTIPOPER` |
| `CODTIPVENDA` | Inteiro | Tipo Negociação | → `TGFTPV`.`CODTIPVENDA` |
| `CONFIRMADA` | Texto | Confirmada |  |
| `CONTABILIZADO` | Texto | Contabilizado |  |
| `CODVEND` | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `STATUSNOTA` | Texto | Status da Nota |  |
| `CODNAT` | Inteiro | Natureza | → `TGFNAT`.`CODNAT` |
| `CODCENCUS` | Inteiro | Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `TIPMOV` | Texto | Tipo de Movimento |  |
| `CODLOCALORIG` | Inteiro | Local |  |
| `M3AENTREGAR` | Decimal | M3 a Entregar |  |
| `PESOAENTREGAR` | Decimal | Peso a Entregar |  |
| `PESOBRUTOITENS` | Decimal | Peso bruto dos Itens |  |
| `PESOLIQITENS` | Decimal | Peso liq. dos Itens |  |
| `CODMOEDA` | Inteiro | Moeda | → `TSIMOE`.`CODMOEDA` |
| `CODHISTAC` | Inteiro | Historico |  |
| `BASESUBSTIT` | Decimal | Base da Substituição |  |
| `HRMOV` | Data/Hora | Hr. do Movimento |  |
| `BASEICMSSTFRETE` | Decimal | Base do ICMS/ST do Frete |  |
| `BASEICMSFRETE` | Decimal | Base do ICMS do Frete |  |
| `NUMCONTRATO` | Inteiro | Contrato | → `TCSCON`.`NUMCONTRATO` |
| `BASEINSS` | Decimal | Base de INSS |  |
| `OBSERVACAO` | Texto | Observação |  |
| `DTALTER` | H | Dt. de Alteração |  |
| `VLRICMS` | Decimal | Vlr. do ICMS |  |
| `VLRDESCTOT` | Decimal | Desconto no total |  |
| `VENCIPI` | H | Vencimento do IPI |  |
| `VLRVENDOR` | Decimal | Vlr. do Vendor |  |
| `TOTALCUSTOSERV` | Decimal | Custo Total do Servico |  |
| `VENCFRETE` | Data | Vencimento do frete |  |
| `VLRDESCTOTITEM` | Decimal | Desconto total por item |  |
| `NUMCOTACAO` | Inteiro | Nro. da Cotação | → `TGFCOT`.`NUMCOTACAO` |
| `PERCDESC` | Decimal | Percentual de Desconto |  |
| `ICMSFRETE` | Decimal | ICMS sobre o frete |  |
| `ICMSSTFRETE` | Decimal | Vlr. ICMS/ST sobre o frete |  |
| `PESO` | Decimal | Peso |  |
| `VLRSUBST` | Decimal | Vlr. da Substituição |  |
| `DTFATUR` | H | Dt. do Faturamento |  |
| `LOCALENTREGA` | Texto | Local de Entrega |  |
| `VLRREPREDTOT` | Decimal | Desconto Redução de Base |  |
| `BASEISS` | Decimal | Base do ISS |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `IPIEMB` | Decimal | IPI da embalagem |  |
| `CODPARCDEST` | Inteiro | Parceiro Destinatario | → `TGFPAR`.`CODPARC` |
| `LOCALCOLETA` | Texto | Local de coleta |  |
| `VLRFRETECPL` | Decimal | Vlr. Frete Complementar |  |
| `VLRISS` | Decimal | Valor do ISS |  |
| `VLRIRF` | Decimal | Vlr. do IRF |  |
| `VLRFRETE` | Decimal | Vlr. do Frete |  |
| `VLRMERCADORIA` | Decimal | Vlr. da Mercadoria |  |
| `VLREMB` | Decimal | Vlr. da Embalagem |  |
| `COMGER` | Decimal | Comissão Gerente |  |
| `VOLUME` | Texto | Volume |  |
| `BASEICMS` | Decimal | Base do ICMS |  |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `IRFRETIDO` | Texto | o INSS e retido |  |
| `NOTASCF` | Texto | Notas do conhecimento de frete |  |
| `TIPFRETE` | Texto | Tipo do frete |  |
| `VLRJURO` | Decimal | Valor do Juro |  |
| `VLRDESTAQUE` | Decimal | Vlr. Destaque |  |
| `BASEIPI` | Decimal | Base do IPI |  |
| `VLRIPI` | Decimal | Vlr. do IPI |  |
| `BASESUBSTSEMRED` | Decimal | Base Substituição Sem Redução |  |
| *... +286 campos adicionais* | | | |

**Opções `AGRUPFINNOTA`:** `S`=Sim, `N`=Não

**Opções `APROVADO`:** `N`=Não, `S`=Sim

**Opções `CIF_FOB`:** `R`=Transp. Proprio Remetente, `F`=FOB - Contratação do Frete por conta do Destinatario, `C`=CIF - Contratação do Frete por conta do Remetente, `S`=Sem Frete, `T`=Terceiros, `D`=Transp. Proprio Destinatario

**Opções `CODDOCARRECAD`:** `0`=Documento Estadual de Arrecadação, `1`=GNRE

**Opções `CONFIRMADA`:** `N?o`=Não, `Sim`=Sim

**Opções `CONFIRMNOTAFAT`:** `N`=Não, `S`=Sim

### TGFITE
**Itens de Entrada e Saida de Produto**

**PK:** `NUNOTA`, `SEQUENCIA`  
**Referenciada por:** 60 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DH_ITENSKIT` | Texto | Itens do Kit |  |
| `CODBARRAPDV` | Texto | Cod. de Barras |  |
| `IDDESCPARCERIA` | Decimal | Id de desconto da parceria |  |
| `VLRDESCPARCERIA` | Decimal | Valor cupom desconto parceria |  |
| `VLRFUST` | Decimal | Valor FUST |  |
| `VLRFUNTTEL` | Decimal | Valor FUNTTEL |  |
| `BASEFUST` | Decimal | Base FUST |  |
| `BASEFUNTTEL` | Decimal | Base FUNTTEL |  |
| `ALIQFUST` | Decimal | Aliquota FUST |  |
| `ALIQFUNTTEL` | Decimal | Aliquota FUNTTEL |  |
| `DH_SEQITEMETAPA` | Inteiro | Seq. Itens da Etapa |  |
| `DH_CODPRJETAPA` | Inteiro | Cod. Prj Item Etapa |  |
| `STATUSPROC` | Texto | Situação Atual da Produção |  |
| `RESERVADO` | Decimal | Qtd. Reservada |  |
| `OPERATUAL` | Texto | Operação Atual da Produção |  |
| `NROPROCESSO` | Texto | Nro do Processo Judicial/Adm (ISS) |  |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `CODVOLPAD` | Texto | Unidade padrão |  |
| `COMPLDESC` | Texto | Complemento |  |
| `CODEMP` | Inteiro | Cod.Empresa | → `TGFEMP`.`CODEMP` |
| `NUNOTA` 🔑 | Inteiro | Nro unico |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `REFFORN` | Texto | Referencia do Fornecedor |  |
| `REFERENCIA` | Texto | Referencia do produto |  |
| `ESTOQUE` | Decimal | Estoque |  |
| `CODNATREND` | Inteiro | Codigo Natureza de Rendimento |  |
| `QTDPENDENTE` | Decimal | Qtd. pendente |  |
| `QTDNEG` | Decimal | Quantidade |  |
| `QTDFORMULA` | Decimal | Qtd. formula |  |
| `QTDCONFERIDA` | Decimal | Qtd. corte |  |
| `VLRUNIT` | Decimal | Vlr. unitario |  |
| `VLRTOT` | Decimal | Vlr. total |  |
| `VLRTOTMOE` | Decimal | Vlr. Tot. Moeda |  |
| `PERCDESC` | Decimal | % desconto |  |
| `CODVOL` | Texto | Unidade | → `TGFVOL`.`CODVOL` |
| `CODVEND` | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `CODLOCALORIG` | Inteiro | Local origem | → `TGFLOC`.`CODLOCAL` |
| `CODLOCALDEST` | Inteiro | Local destino |  |
| `CONTROLE` | Texto | Controle |  |
| `CONTROLEDEST` | Texto | Controle destino |  |
| `BASEICMS` | Decimal | Base ICMS |  |
| `ALIQICMS` | Decimal | Aliq. ICMS |  |
| `VLRICMS` | Decimal | Vlr. ICMS |  |
| `BASEIPI` | Decimal | Base do IPI |  |
| `ALIQIPI` | Decimal | Aliq. IPI |  |
| `VLRIPI` | Decimal | Vlr. IPI |  |
| `BASESUBSTIT` | Decimal | Base substituição |  |
| `VLRSUBST` | Decimal | Vlr. substituição |  |
| `CODTRIB` | Inteiro | Tributação |  |
| `CODEXEC` | Inteiro | Executante | → `TGFVEN`.`CODVEND` |
| `ATUALESTOQUE` | Inteiro | Atualiza estoque |  |
| `DTVIGOR` | Data | Ultima Dt. Vigor |  |
| `VLRSUGERIDO` | Decimal | Vlr. Sugerido |  |
| `CODCFO` | Inteiro | CFOP | → `TGFCFO`.`CODCFO` |
| `CODOBSPADRAO` | Inteiro | Obs Padrão | → `TGFOBS`.`CODOBSPADRAO` |
| `CUSTO` | Decimal | Custo |  |
| `FATURAR` | Texto | Faturar |  |
| `M3` | Decimal | Metro Cubico |  |
| `NUTAB` | Inteiro | Tabela | → `TGFTAB`.`NUTAB` |
| `OBSERVACAO` | Texto | Observação |  |
| `PENDENTE` | Texto | Pendente |  |
| `QTDENTREGUE` | Decimal | Qtd. entregue |  |
| `RESERVA` | Texto | Reserva |  |
| `PERCREDVLRIPI` | Decimal | % Redução de Vlr. IPI |  |
| `STATUSNOTA` | Texto | Status da Nota |  |
| `USOPROD` | Texto | Uso do Produto |  |
| `VLRCUS` | Decimal | Vlr. custos |  |
| `VLRDESC` | Decimal | Vlr. desconto |  |
| `VLRDESCMOE` | Decimal | Vlr. Desc. Moeda |  |
| `VLRDESCBONIF` | Decimal | Bonificação |  |
| `VLRREPRED` | Decimal | Vlr. redução |  |
| `VLRTOTLIQ` | Decimal | Total liq. |  |
| `VLRTOTLIQMOE` | Decimal | Total liq. Moeda |  |
| `VLRUNITLIQ` | Decimal | Preco liq. |  |
| `VLRUNITMOE` | Decimal | Vlr. Unit. Moeda |  |
| `VLRUNITLIQMOE` | Decimal | Preco Liq. Moeda |  |
| `ALIQICMSRED` | Decimal | Aliq. ICMS Reduzida |  |
| `CODPARCEXEC` | Inteiro | Cod. Parceiro Exec | → `TGFPAR`.`CODPARC` |
| `CODMOTDESONERAST` | Inteiro | Cod. Mot. Desoneração do ICMS ST |  |
| `BASESUBSTSEMRED` | Decimal | Base ST S/Redução |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | H | Dt. Alteração |  |
| `SOLCOMPRA` | Texto | Solic. compra |  |
| `CODTRIBISS` | Inteiro | Cod. trib. ISS |  |
| `CODCFPS` | Inteiro | Cod. CFPS |  |
| `ALIQISS` | Decimal | Aliq. ISS |  |
| `ATUALESTTERC` | Texto | Estoque terc. |  |
| `TERCEIROS` | Texto | Terceiros |  |
| `PERCDESCBONIF` | Decimal | % desc. bonif. |  |
| `ENDIMAGEM` | Texto | End. imagem |  |
| `ALTURA` | Decimal | Altura |  |
| `LARGURA` | Decimal | Largura |  |
| `ESPESSURA` | Decimal | Espessura |  |
| `CODCAV` | Inteiro | Cod. cavalete | → `TGFCAV`.`CODCAV` |
| `CODPROC` | Inteiro | Cod. processo | → `TGPCAB`.`CODPROC` |
| `QTDPECA` | Decimal | Qtd. peca |  |
| `PRECOBASE` | Decimal | Preco base |  |
| `VLRACRESCDESC` | Decimal | Vlr. acresc./desc. |  |
| `VLRRETENCAO` | Decimal | Vlr. retenção |  |
| `CSTIPI` | Inteiro | C.S.T IPI |  |
| *... +120 campos adicionais* | | | |

**Opções `ALTPRECO`:** `M`=Atualiza maior, `N`=Não Atualiza, `B`=Atualiza menor

**Opções `CODANTECIPST`:** `5`=5-Substituição tributaria interna motivada por regime especial de tributação, `A`=A-ST informada pelo substituto/substituido que não incorra em nenhuma das situações anteriores, `6`=6-ICMS pago na importação, `1`=1-Pgto de ST efetuado pelo destinatario quando não efetuado ou efetuado a menor pelo substituto, `2`=2-Antecip. tribut. efetuada pelo destinatario apenas como complemento do diferencial de aliquota, `3`=3-Antecip. tribut. com MVA efetuada pelo destinatario sem encerrar a fase de tributação, `4`=4-Antecip. tribut. com MVA efetuada pelo destinatario encerrando a fase de tributação, `N`=N-(Não Usa) Operação não envolve ST

**Opções `CODDOCARRECAD`:** `1`=GNRE, `0`=Documento Estadual de Arrecadação

**Opções `CODMOTDESONERAICMS`:** `7`=SUFRAMA, `6`=Utilitarios e Motocicletas da Amazonia Ocidental e Areas de Livre Comercio, `1`=Taxi, `9`=Outros, `90`=Solicitado pelo Fisco, `16`=Olimpiadas Rio 2016, `2`=Deficiente Fisico, `5`=Diplomatico/Consular, `4`=Frotista/Locadora, `8`=Venda a Orgãos Publicos, `3`=Produtor Agropecuario

**Opções `CODMOTDESONERAST`:** `3`=Uso na agropecuaria, `9`=Outros, `12`=Fomento agropecuario

**Opções `CODSIT08EFD`:** `S`=Sim, `N`=Não

### TGFFIN
**Financeiro**

**PK:** `NUFIN`  
**Referenciada por:** 36 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMOCORRENCIAS` | Texto | Nr. da Ocorrencia Caixa |  |
| `NUFIN` 🔑 | Inteiro | Nro Unico |  |
| `METODOCALCIRRF` | Texto | Metodo de Calculo IRRF |  |
| `NUCAIXA` | Inteiro | Num. Caixa | → `TGFCAI`.`NUCAIXA` |
| `NUMNOTA` | Inteiro | Nro Nota |  |
| `SERIENOTA` | Texto | Serie da Nota |  |
| `SANGDESPDV` | Texto | Sangria de despesa PDV |  |
| `CODPARC` | Inteiro | Parceiro | → `TGFCTT`.`CODPARC` |
| `CGC_CPF_PARC` | Texto | CNPJ / CPF |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CONTABILIZADOPDD` | Texto | Titulo contabilizado PDD |  |
| `PERTENCEAC` | Texto | Pertence ao acerto de carga |  |
| `DESCRHISTAC` | Texto | Descrição historico |  |
| `OBSERVACAOAC` | Texto | Observação |  |
| `RETORNADOAC` | Texto | Retornado |  |
| `STATUSLIB` | Inteiro | Status liberação |  |
| `RECDESP` | Inteiro | Receita/Despesa |  |
| `PROVISAO` | Texto | Provisão |  |
| `DTVENC` | Data | Dt. Vencimento |  |
| `DTNEG` | Data | Dt. Negociação |  |
| `DHBAIXA` | Data | Data Baixa |  |
| `DHMOV` | H | Dt/Hr Movimentação |  |
| `DTBAIXAPREV` | H | Dt. Prevista p/ Baixa |  |
| `CODPARCMATRIZ` | Inteiro | Cod. Parceiro Matriz |  |
| `DTENTSAI` | Data | Dt. Entrada e Saida |  |
| `VLRDESDOB` | Decimal | Vlr do Desdobramento |  |
| `NROCESSAOFDIC` | Texto | Nro. Cessao FDIC |  |
| `CONTABILIZADO` | Texto | Contabilizado |  |
| `VLRDESDOBCALC` | Decimal | Vlr do Desdobramento Calc |  |
| `VLRATUAL` | Inteiro | Vlr. Atual |  |
| `VLRDESC` | Decimal | Vlr Desconto |  |
| `VLRMULTA` | Decimal | Vlr Multa |  |
| `VLRJURO` | Decimal | Vlr Juros |  |
| `VLRVENDOR` | Decimal | Vlr Vendor |  |
| `VLRALIBERAR` | Decimal | Vlr. a liberar |  |
| `VLRBAIXA` | Decimal | Vlr Baixa |  |
| `VLRLIQUIDO` | Decimal | Valor Liquido |  |
| `DESDOBDUPL` | Texto | Desdob. Duplicata |  |
| `ATRASO` | Inteiro | Atraso (dias) |  |
| `HISTORICO` | Texto | Historico |  |
| `CODHISTAC` | Inteiro | Historico |  |
| `CODTIPOPER` | Inteiro | Tipo Operação | → `TGFTOP`.`CODTIPOPER` |
| `CODTIPTIT` | Inteiro | Tipo de Titulo | → `TGFTIT`.`CODTIPTIT` |
| `CODNAT` | Inteiro | Natureza | → `TGFNAT`.`CODNAT` |
| `BASEICMS` | Decimal | Base ICMS |  |
| `CODCENCUS` | Inteiro | Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `NUMCONTRATO` | Inteiro | Nro Contrato | → `TCSCON`.`NUMCONTRATO` |
| `REFATCON` | Data | Ref. Faturamento do Contrato |  |
| `ORIGEM` | Texto | Origem |  |
| `CODVEND` | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `CODREGUA` | Inteiro | Regua |  |
| `CODCBE` | Inteiro | Acerto Beneficio | → `TFPCBE`.`CODCBE` |
| `AUTORIZADO` | Texto | Autorizado |  |
| `CARTA` | Inteiro | Nro Carta |  |
| `CODOBSPADRAO` | Inteiro | Observação padrão | → `TGFOBS`.`CODOBSPADRAO` |
| `VALORPRESENTE` | Decimal | Valor Presente |  |
| `DTINITREFAPURACAO` | H | Data apuração |  |
| `JUROSAVP` | Decimal | Juros Ajuste do Valor Presente |  |
| `BLOQVAR` | Texto | Bloq. Calculo Variação |  |
| `INDRECEFDCONT` | Texto | Indicador de Receita (registro F525 - EFD Cont.) |  |
| `NUCOMPENS` | Inteiro | Nro Compensação/Acerto |  |
| `INFCOMPLEFDCONT` | Texto | Informação complementar do Indic. comp. receita recebida |  |
| `CODFUNC` | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODCONTATO` | Inteiro | Contato | → `TGFCTT`.`CODCONTATO` |
| `PDD` | Texto | PDD |  |
| `CODIMOVELRURAL` | Inteiro | Imovel Rural | → `TGFEMP`.`CODEMP` |
| `RECADIANTAMENTORURAL` | Texto | Receita de Adiantamentos |  |
| `CONCILIADO` | Texto | Conciliado |  |
| `DHCONCIL` | H | Dh. Conciliação |  |
| `IDTRANSACAOPIX` | Texto | TXID Pix |  |
| `ANTECIPADO` | Texto | Antecipado |  |
| `DTANTECIPACAO` | Data | Dt. antecipação |  |
| `NUANTBANC` | Inteiro | Nro. unico antecipação |  |
| `M2` | Decimal | Metro Quadrado |  |
| `CODMOEDA` | Inteiro | Moeda | → `TSIMOE`.`CODMOEDA` |
| `PRAZO` | Inteiro | Prazo |  |
| `VLRJUROCALC` | Decimal | Juros Calculados |  |
| `VLRVARCAMBIAL` | Decimal | Variação Cambial |  |
| `VLRMOEDA` | Decimal | Vlr Moeda |  |
| `VLRMULTACALC` | Decimal | Multa Calculada |  |
| `TIPJURO` | Texto | Tipo Juro |  |
| `VLRTOTALCALC` | Decimal | Total Calculado |  |
| `TIPMULTA` | Texto | Tipo Multa |  |
| `VLRTROCO` | Decimal | Vlr Troco |  |
| `VLRMULTAEMBUT` | Decimal | Vlr Multa Embutida |  |
| `VLRJUROEMBUT` | Decimal | Vlr Juros Embutidos |  |
| `NUMTRANSF` | Inteiro | Nro da Transferencia |  |
| `VLRJUROLIB` | Decimal | Vlr Perdão de Juros |  |
| `CODLANC` | Inteiro | Cod. Lancamento |  |
| `VLRMULTALIB` | Decimal | Vlr Perdão de Multa |  |
| `DHTIPOPERBAIXA` | H | Dt/Hr Tipo Operação | → `TGFTOP`.`DHALTER` |
| `VLRJURONEGOC` | Decimal | Vlr Juros Negociados |  |
| `DESCRLANCBCO` | Texto | Desc. Lanc. Bancario |  |
| `VLRMULTANEGOC` | Decimal | Vlr Multa Negociada |  |
| `CTABCOBAIXA` | Texto | Conta Baixa |  |
| `RECDESPFILTER` | Texto | Rec Desp p/ o Filtro |  |
| `CODUSUBAIXA` | Inteiro | Usuario Baixa | → `TSIUSU`.`CODUSU` |
| `CODTIPOPERBAIXA` | Inteiro | Tipo Operação Baixa | → `TGFTOP`.`CODTIPOPER` |
| `RATEADO` | Texto | Rateado |  |
| *... +183 campos adicionais* | | | |

**Opções `ANTECIPADO`:** `S`=Sim, `N`=Não

**Opções `AUTORIZADO`:** `N`=Não, `S`=Sim

**Opções `BLOQVAR`:** `S`=Sim, `N`=Não

**Opções `CODTRIB`:** `0`=00-Tributada integralmente, `02`=02-Tributação monofasica propria sobre combustiveis, `10`=10-Tributada e c/cobranca por substituição, `15`=15-Tributação monofasica propria e com responsabilidade pela retenção sobre combustiveis, `20`=20-Com redução de base de calculo, `30`=30-Isenta e não tribut.e c/cobranca por subst., `40`=40-Isenta, `41`=41-Não tributada, `50`=50-Suspensão, `51`=51-Diferimento, `53`=53-Tributação monofasica sobre combustiveis com recolhimento diferido, `60`=60-ICMS cobrado anteriormente por substituição

**Opções `CONCILIADO`:** `S`=Sim, `N`=Não

**Opções `CONTABILIZADO`:** `N`=Não, `S`=Sim

### TGFEMP
**Empresa Financeiro**

**PK:** `CODEMP`  
**Referenciada por:** 102 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPOIMPKITFOX` | Texto | Tipo Kit |  |
| `CODMODEMAILNFE` | Inteiro | Modelo de e-mail para NF-e | → `TSIMEM`.`CODMODELO` |
| `MODEMAILLIBLIM` | Inteiro | Modelo de E-mail p/ Liberação de Limites |  |
| `EFDCODBCO` | Inteiro | Banco |  |
| `EFDCODCENCUS` | Inteiro | Centro Resultado |  |
| `EFDCODCTABCOINT` | Inteiro | Conta Bancaria |  |
| `ALIQFUNTTEL` | Decimal | Aliquota FUNTTEL |  |
| `ALIQFUST` | Decimal | Aliquota FUST |  |
| `ALIQPISBONIF` | Decimal | Aliquota de Pis |  |
| `TIPICMSFENVALBEM` | Inteiro | Tipo do ICMS do Frete Extra Nota no valor de aquisição/depreciação do bem |  |
| `CODEMP` 🔑 | Inteiro | Codigo | → `TSIEMP`.`CODEMP` |
| `GERCIAPCOMPEFD` | Texto | Gerar CIAP de componentes para SPED |  |
| `CONTBAIBEMSUBIMPREC` | Texto | Contabilização da baixa do bem subtraindo os impostos recuperaveis |  |
| `USAVLRMEDTRANSFEMP` | Texto | Usa valor medio de venda nas transferencias entre empresas do mesmos grupo |  |
| `ESTRNCREDICMSST` | Texto | Considerar TOPs de Estorno para Credito de ICMS/ST |  |
| `ATIVO` | Texto | Ativo |  |
| `CODCTACTBBONIF` | Inteiro | Conta Contabil |  |
| `ALIQCFBONIF` | Decimal | Aliquota de COFINS |  |
| `CALCICMS` | Texto | Calcula ICMS |  |
| `EFDCODTIPTIT` | Inteiro | Tipo de Titulo |  |
| `CODSTPISCFBONIF` | Texto | Cod. Sit. Tribut. PIS/COFINS Bonificação |  |
| `TRABCOMIPI` | Texto | Trabalha com IPI |  |
| `EFDCODTIPOPER` | Inteiro | Tipo Operação |  |
| `IPIINCICMS` | Texto | IPI incide no ICMS |  |
| `DESTIPIDEVCOM` | Texto | Destacar o IPI na tag <vIPIDevol> em devoluções |  |
| `TRIBPISCFBONIF` | Texto | Tributa PIS/COFINS sobre Aquisições em Bonificações |  |
| `EFDCODNATDESPRECICMS` | Inteiro | Natureza Despesa Receitas ICMS |  |
| `CALCIRRF` | Texto | Calcula IRRF |  |
| `DESCRICAO` | Texto | DescricaoConta |  |
| `CALCFUNRURAL` | Texto | Calcula FUNRURAL/INSS |  |
| `DESCRNAT` | Texto | DescricaoNatureza |  |
| `ICMSSCTTD` | Texto | Habilita Aliq. incidencia ICMS SC nas TTDs 409, 410 e 411 |  |
| `CODLANCBCOREC` | Inteiro | Lancamento bancario receitas | → `TGFHBC`.`CODLANC` |
| `CODLANCBCOPAG` | Inteiro | Lancamento bancario despesas | → `TGFHBC`.`CODLANC` |
| `EFDDIAVENC` | Inteiro | Dia de vencimento |  |
| `CALCISS` | Texto | ISS |  |
| `TOPSANGSUPRI` | Inteiro | TOP para sangria / suprimento |  |
| `TOPDESPESA` | Inteiro | TOP para despesa |  |
| `CSTIPISAI` | Inteiro | Codigo Sit.Trib.IPI Saida |  |
| `CSTIPIENT` | Inteiro | Codigo Sit.Trib.IPI Entrada |  |
| `CODENQIPIENT` | Inteiro | Codigo Enq. Legal IPI Entrada |  |
| `CODENQIPISAI` | Inteiro | Codigo Enq. Legal IPI Saida |  |
| `TEMPIS` | Texto | Calcula PIS |  |
| `TEMCOFINS` | Texto | Calcula COFINS |  |
| `EMITNFSENACIONAL` | Texto | Emitir NFS-e Padrão Nacional |  |
| `PREFIXSERIENACIONAL` | Texto | Prefixo Serie NFS-e Padrão Nacional |  |
| `TEMCSSL` | Texto | Calcula CSLL |  |
| `SERIEACOMPCF` | Texto | Serie p/ Nota de Acomp. de CF |  |
| `CODTIPOPERACOMP` | Inteiro | Cod.Tipo Operação Nota de Acomp. de CF |  |
| `SALDOLIVQUINZ` | Texto | Frequencia saldo livro ICMS |  |
| `SALDOLIVQUINZIPI` | Texto | Frequencia saldo livro IPI |  |
| `ULTPAGLIVISS` | Inteiro | Ultima pagina do livro ISS |  |
| `ULTPAGLIVSAIDA` | Inteiro | Ultima pagina do registro de saidas |  |
| `ULTPAGLIVENTRAD` | Inteiro | Ultima pagina do registro de entradas |  |
| `ULTPAGCIAPMODC` | Inteiro | Ultima Pagina do CIAP Modelo C |  |
| `GEROBSIPIREGENT` | Texto | Gerar Observação de IPI no registro de entrada |  |
| `GERARLIVROS` | Texto | Gerar livros |  |
| `RECMINTARE` | Texto | Tem convenio TARE na geração do livro fiscal |  |
| `LIVRO1PARA1TGFITE` | Texto | Gerar linhas da Nota separadamente no Livro Fiscal |  |
| `GERAGNRE` | Texto | Gerar GNRE |  |
| `CALCVLRAQUISBEM` | Inteiro | Calcular o valor de aquisição do bem |  |
| `REG54SEQ997ST` | Texto | Reg.54.Seq.997 p/ ST |  |
| `CODCTACTB_1` | Inteiro | Conta contabil 1 | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB_2` | Inteiro | Conta contabil 2 | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB_3` | Inteiro | Conta contabil 3 | → `TCBPLA`.`CODCTACTB` |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODCENCUSDESP` | Inteiro | Centro Resultado desp. |  |
| `ULTDUPL` | Inteiro | Ultima duplicata |  |
| `MODDUPL` | Inteiro | Modelo duplicata |  |
| `IMPEXPED` | Texto | Impressora |  |
| `MODEXPED` | Inteiro | Modelo |  |
| `TIPOIMPRESSORA` | Texto | Tipo de Imp. |  |
| `EMPSOMA` | Inteiro | Empresa para agrupar estoque |  |
| `CODTABCALC` | Inteiro | Tabela de preco padrão | → `TGFNTA`.`CODTAB` |
| `CODFORMPREC` | Inteiro | Formula de Custo/Preco | → `TGFFOR`.`CODFORMPREC` |
| `CODTAB` | Inteiro | Tabela de preco para venda | → `TGFNTA`.`CODTAB` |
| `CODPARCCTB` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `NOMECONTADOR` | Texto | Nome do Contador |  |
| `CPFCONTADOR` | Texto | CPF |  |
| `UFCRCCONTADOR` | Texto | UF CRC |  |
| `CRCCONTADOR` | Texto | CRC |  |
| `TELCONTADOR` | Texto | Telefone |  |
| `EMAILCONTADOR` | Texto | Email |  |
| `ALTCONTADOR` | Texto | Alterou |  |
| `EMITEEXPED` | Texto | Emite expedição |  |
| `PARTICMETA` | Decimal | Participação na meta |  |
| `ULTPAGLIVICMS` | Inteiro | Ultima Pagina Livro ICMS |  |
| `CALPERCPIS` | Inteiro | Calcula percentual do PIS |  |
| `PERPROJ` | Texto | Periodicidade projeção |  |
| `PROJONLINE` | Texto | Projeção Online |  |
| `CODCTABCOIPAD` | Inteiro | Conta bancaria padrão | → `TSICTA`.`CODCTABCOINT` |
| `ULTPAGLIVIPI` | Inteiro | Ultima Pagina Livro IPI |  |
| `ULTAUTORPAG` | Inteiro | Ultima autorização de pagamento |  |
| `PERCCUSVAR` | Decimal | % Custo Variavel |  |
| `PERCMARGEM` | Decimal | % Outros |  |
| `PERCPIS` | Decimal | % PIS |  |
| `PERCCSL` | Decimal | % CSLL (Contrib. Social s/Lucro) |  |
| `PERCCOFINS` | Decimal | % COFINS |  |
| `PERCCFSERVICO` | Decimal | % Custo Fixo Servico |  |
| `PERCCFFAB` | Decimal | % Custo Fixo Fabricação |  |
| *... +497 campos adicionais* | | | |

**Opções `AGRUPASERVFAT`:** `S`=Sim, `N`=Não

**Opções `ALTCONTADOR`:** `S`=Sim, `N`=Não

**Opções `AMBIENTEGNRE`:** `null`=Não usa, `2`=Homologação, `1`=Produção

**Opções `AMBIENTEREINF`:** `1`=Produção, `2`=Produção restrita - dados reais, `3`=Produção restrita - dados ficticios

**Opções `APLCALCDIFALIQFRT`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Nao

### TGFTOP
**Tipos de Operação**

**PK:** `CODTIPOPER`, `DHALTER`  
**Referenciada por:** 16 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPOPER` 🔑 | Inteiro | Cod.Tipo Operação |  |
| `DH_REQPRJ` | Texto | Requisição de Projeto |  |
| `NATEFDCONTM410M810` | Inteiro | Cod. Natureza (PIS/COFINS M410/M810) |  |
| `DESCROPER` | Texto | Descrição |  |
| `DH_FATPRJ` | Texto | Faturamento de Projeto |  |
| `DH_COMPRJ` | Texto | Compra para Projeto |  |
| `TIPMOV` | Texto | Tipo de movimento |  |
| `DH_TIPMOVPRJ` | Texto | Tipo de Movimento |  |
| `ORCAMENTO` | Texto | Orcamento |  |
| `DHALTER` 🔑 | H | Data e hora alteração |  |
| `ATIVO` | Texto | Ativo |  |
| `GRUPO` | Texto | Grupo |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `ATUALFIN` | Inteiro | Financeiro |  |
| `TIPATUALFIN` | Texto | Atualização do financeiro |  |
| `ATUALEST` | Texto | Atualização do Estoque |  |
| `ATUALESTMP` | Inteiro | Atualiza estoque MP |  |
| `ATUALBEM` | Texto | Atualização do Bem |  |
| `ATUALCOM` | Texto | Comissão |  |
| `PRECIFICA` | Texto | Precifica |  |
| `MOVENDFLUTUANTE` | Texto | Movimentação de Enderecos Flutuantes |  |
| `IGNORAMPPVPA` | Texto | Ignora MP no preco de venda do PA |  |
| `ARMTIPAPU` | Texto | Tipo de Movimento Armazenagem |  |
| `PENDENTE` | Texto | A nota fica como pendente |  |
| `ALTNFCONF` | Texto | Permitir Alteração apos confirmar |  |
| `SALVARCONFSEMPERG` | Texto | Salvar doc. confirmado sem perguntar |  |
| `ATUALPRECOFAT` | Texto | Recalcular preco prod. ao faturar |  |
| `CUPOMFISCAL` | Texto | TOP de Cupom Fiscal |  |
| `BONIFICACAO` | Texto | Bonificação |  |
| `OPERACAOAMOSTRA` | Texto | TOP de Amostra Gratis |  |
| `ADIARATUALEST` | Texto | Atualizar Estoq.a partir da Confirmação |  |
| `RATAUTPROD` | Texto | Ratear automaticamente por produto |  |
| `OBTERVLRMOEDAFAT` | Texto | Obter valor da moeda ao faturar |  |
| `CODTIPOPERDESTINO` | Inteiro | Cod.Tipo Operação Faturamento |  |
| `CODTIPOPERSEPARACAO` | Inteiro | Tipo Operação Separação |  |
| `USOPRODSEPARACAO` | Texto | Uso da Separação |  |
| `GOLDEV` | Inteiro | Identificador de Devolução |  |
| `GOLSINAL` | Inteiro | Tipo para analise |  |
| `GOLMPSINAL` | Inteiro | Tipo para analise de MP |  |
| `USARPRECOCUSTO` | Texto | Usar como Preco |  |
| `ATUALULTIMACOMP` | Texto | Atualizar Ultima Compra |  |
| `ATUALULTIMAVEND` | Texto | Atualizar Ultima Venda |  |
| `ANALISEGIRO` | Inteiro | Analise de Giro |  |
| `ATUALACDC` | Texto | Atualizar Acrescimos/Decrescimos |  |
| `FATENTPROD` | Texto | Na Entrada de Produtos |  |
| `INFCONTRATO` | Texto | Informar Contrato na Nota |  |
| `VALIDAATRASO` | Texto | Atraso |  |
| `PRODREP` | Texto | Aceitar Produto Repetido |  |
| `OC` | Texto | Tipo de Ordem de Carga |  |
| `ATUALTRANSG` | Inteiro | Saldo de Transgenico |  |
| `EXIGECOTACAO` | Texto | Exige Cotação |  |
| `PODEPESAGEM` | Texto | Tipo de Pesagem |  |
| `EXIGETRANSP` | Texto | Exige Transportadora |  |
| `VENDITE` | Texto | Exige vendedor nos itens |  |
| `EXECITE` | Texto | Exige executante nos itens |  |
| `EXIGECONF` | Texto | Exige conferencia |  |
| `VALIDAAGRUPMIN` | Texto | Valida agrupamento minimo |  |
| `EXIGELIB` | Texto | Exigir Liberação antes da Confirmação |  |
| `EXIGELAUDO` | Texto | Exige Laudo de analise |  |
| `LAUDOITEM` | Texto | Laudo por item |  |
| `VALIDAMEDIANEGOC` | Texto | Validar Media de Negociações Mensais |  |
| `VLRMINAP` | Decimal | Valor minimo p/Autorização de Pagamento |  |
| `FATESTCONF` | Texto | Fatura Produtos com Estoque na Confirmação |  |
| `SOLCOMPRA` | Texto | Gera Solicitação de Compra na Confirmação |  |
| `EDITANALISERENTAB` | Texto | Permite edição de analise de rentabilidade |  |
| `EXIGEGAR` | Texto | Exige garantia |  |
| `EXIGEDTVAL` | Texto | Exige data de validade |  |
| `USARCONFCEGA` | Texto | Usa conferencia Cega |  |
| `EXIGEPEDFRET` | Texto | Exige Pedido de Frete p/Frete Extra Nota |  |
| `PEDFRETE` | Texto | Pedido de Frete |  |
| `GERAGNRE` | Texto | Gerar GNRE |  |
| `PODETRANSFENT` | Texto | Pode Transformar Entradas |  |
| `PODEFIXAR` | Texto | Pode Fixar Preco |  |
| `REFNFE` | Texto | Buscar NF de origem p/ referenciar na NFe |  |
| `MPNUMAUTLOTE` | Texto | Numerar automaticamente MP por Lote |  |
| `EMPFUNCDIF` | Texto | Permitir Req. Func. de outra Empresa |  |
| `GERARTAGJNFE` | Texto | Gerar tag na NFe para Negociação de Veiculos Novos |  |
| `EXIGANALITENS` | Texto | Exigir liberação com analise dos itens antes da confirmação |  |
| `ENVIARWMSCONF` | Texto | Enviar automaticamente para o WMS na Confirmação |  |
| `VALEST` | Texto | Validar Estoque p/ Reservar |  |
| `EXIGELIBSEMPRE` | Texto | Sempre exigir Liberação |  |
| `TEMFINORIGEM` | Texto | Atualiza Financeiro na TOP de Origem |  |
| `AUTDIGITAL` | Texto | Autorização por Digital |  |
| `DIGINFIMPORTA` | Texto | Digitar informações sobre Importação |  |
| `CODCONTARURAL` | Texto | Classificação da conta Produtor Rural |  |
| `NFESEMDTENTSAI` | Texto | Imprimir NF-e sem Data de Entrada/Saida |  |
| `CONTLAUDOSINT` | Texto | Participa da contagem de laudos internos |  |
| `AVISARCOMP` | Texto | Avisar sobre componentes |  |
| `CONFIMPOSTO` | Texto | Exige Conferencia de Impostos |  |
| `CALCFUNTTELTOP` | Texto | Calcular FUNTTEL |  |
| `CALCFUSTTOP` | Texto | Calcular FUST |  |
| `TOPPISCOFREDAQUIS` | Texto | Calcula PIS/COFINS red. pela aquisição |  |
| `CONFCFOP` | Texto | Exige Conferencia de CFOP |  |
| `NAOINCCONF` | Texto | Nunca incluir Confirmada |  |
| `PROVISENTREGA` | Texto | Exige previsão de entregas |  |
| `COPIARLIBER` | Texto | Copiar liberações quando faturando individualmente |  |
| `PESAITEM` | Texto | Pesagem por item |  |
| `DIGPUREZA` | Texto | Digitar % Pureza e % Germinação |  |
| `BLOQESTVENC` | Texto | Bloqueia saida de estoque vencido |  |
| `VALVCTLAUDOEST` | Texto | Valida laudo vencido na baixa de estoque |  |
| *... +268 campos adicionais* | | | |

**Opções `ACEITAFATACIMA`:** `S`=Sim, `N`=Não

**Opções `ADIARATUALEST`:** `S`=Sim, `N`=Não

**Opções `AGRUPAPRODNFE`:** `N`=Não, `S`=Sim

**Opções `AGRUPASERVFAT`:** `N`=Não, `S`=Sim

**Opções `AJUSTAVP`:** `F`=Fim do Periodo, `A`=Anual, `N`=Não Ajusta, `V`=Vencimento, `M`=Mensal

**Opções `ALTITEMPARCFAT`:** `S`=Sim, `N`=Não

### TGFNAT
**Natureza de Receitas e Despesas**

**PK:** `CODNAT`  
**Referenciada por:** 26 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNAT` 🔑 | Inteiro | Cod. Natureza |  |
| `DESCRNAT` | Texto | Descrição |  |
| `ATIVA` | Texto | Ativa |  |
| `ANALITICA` | Texto | Analitica |  |
| `INCRESULT` | Texto | Incide no resultado |  |
| `CODCTACTB` | Inteiro | Conta contabil | → `TCBPLA`.`CODCTACTB` |
| `CODCTACTB2` | Inteiro | Conta contabil 2 |  |
| `CODHISTCTB` | Inteiro | Cod. Historico 1 | → `TCBHIS`.`CODHISTCTB` |
| `CODHISTCTB2` | Inteiro | Cod. Historico 2 |  |
| `GRUPOMKP` | Texto | Grupo MKP |  |
| `SUBGRUPOMKP` | Texto | Sub Grupo MKP |  |
| `DECVLR` | Inteiro | Decimal para Valor |  |
| `GRAU` | Inteiro | Grau |  |
| `CODNATPAI` | Inteiro | Cod. Natureza Pai |  |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `FORMULA` | Texto | Formula |  |
| `CODSERVUNICO` | Inteiro | Servico unico faturamento | → `TGFPRO`.`CODPROD` |
| `CODGRUPONAT` | Inteiro | Grupo da Natureza | → `TGFGNT`.`CODGRUPONAT` |
| `TIPNAT` | Texto | Tipo de natureza |  |
| `CSTPIS` | Inteiro | Cod. Sit. Tribut. PIS |  |
| `ALIQPIS` | Decimal | Aliquota de PIS |  |
| `CODCTACTBEFD` | Inteiro | Conta Contabil para EFD | → `TCBPLA`.`CODCTACTB` |
| `CSTCOFINS` | Inteiro | Cod. Sit. Tribut. COFINS |  |
| `ALIQCOFINS` | Decimal | Aliquota de COFINS |  |
| `NATBCCRED` | Texto | Natureza da Base de Calculo do Credito de PIS/COFINS |  |
| `REGIMEEFD` | Texto | Regime (EFD PIS/COFINS) |  |
| `GERALCDPR` | Texto | Gera informações para o Livro Caixa Digital Produtor Rural |  |
| `RECADIANTRURAL` | Texto | Receita de Adiantamentos para o Livro Caixa Digital Produtor Rural |  |
| `NATEFDCONTM410M810` | Inteiro | Cod. Natureza (PIS/COFINS M410/M810) |  |

**Opções `ANALITICA`:** `S`=Sim, `N`=Não

**Opções `ATIVA`:** `N`=Não, `S`=Sim

**Opções `GERALCDPR`:** `N`=Não, `S`=Sim

**Opções `INCRESULT`:** `N`=Não, `S`=Sim

**Opções `RECADIANTRURAL`:** `N`=Não, `S`=Sim

**Opções `REGIMEEFD`:** `C`=Regime de Competencia (Dt.Entrada/Saida), `A`=Regime de Caixa, `B`=Regime de Competencia (Dt.Negociação)

### TGFVEN
**Vendedores Representantes**

**PK:** `CODVEND`  
**Referenciada por:** 22 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `PROVACRESCCAC` | Decimal | Provisão do carrinho |  |
| `CODVEND` 🔑 | Inteiro | Codigo |  |
| `SALDODISPCAC` | Decimal | Saldo Diponivel do Carrinho |  |
| `APELIDO` | Texto | Apelido |  |
| `TIPOCERTIF` | Texto | Tipo p/ certificação |  |
| `ATIVO` | Texto | Ativo |  |
| `CODREG` | Inteiro | Região | → `TSIREG`.`CODREG` |
| `COMVENDA` | Decimal | Comissão venda |  |
| `COMGER` | Decimal | Comissão gerencia |  |
| `VLRHORA` | Decimal | Valor hora p/ comissão de O.S. |  |
| `CODFORM` | Inteiro | Formula Comissão | → `TGFFOC`.`CODFORM` |
| `CODCARGAHOR` | Inteiro | Carga Horaria |  |
| `DIACOM` | Inteiro | Dia inicial p/periodo de comissão |  |
| `CODEMP` | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODGER` | Inteiro | Gerente | → `TGFVEN`.`CODVEND` |
| `CODPARC` | Inteiro | Parceiro |  |
| `CODFUNC` | Inteiro | Funcionario |  |
| `CODCENCUSPAD` | Inteiro | Centro Resultado Padrão | → `TSICUS`.`CODCENCUS` |
| `PERCCUSVAR` | Decimal | % Custo Variavel |  |
| `EMAIL` | Texto | Email |  |
| `SALDODISP` | Decimal | Saldo Disponivel |  |
| `PROVACRESC` | Decimal | Provisão acrescimo |  |
| `DESCMAX` | Decimal | Desconto maximo |  |
| `TIPVALOR` | Texto | Usar valor p/ comissão de OS |  |
| `ACRESCMAX` | Decimal | Acrescimo maximo |  |
| `TIPVEND` | Texto | Tipo |  |
| `GRUPORETENCAO` | Texto | Grupo de retenção |  |
| `DTALTER` | H | Data de alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `PARTICMETA` | Decimal | Participação na meta |  |
| `SENHA` | Inteiro | Senha |  |
| `ATUACOMPRADOR` | Texto | Atua tambem como comprador |  |
| `TIPCALC` | Texto | Pagamento de Comissão por data de |  |
| `GRUPODESCVEND` | Texto | Grupo Desc. Vendedor |  |
| `COMCM` | Texto | Recebe comissão em CM |  |
| `RECHREXTRA` | Texto | Recebe Hora Dobrada |  |
| `TIPFECHCOM` | Texto | Tipo de fechamento de comissão |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `ATUACOMPRADOR`:** `N`=Não, `S`=Sim

**Opções `COMCM`:** `N`=Não, `S`=Sim

**Opções `RECHREXTRA`:** `S`=Sim, `N`=Não

**Opções `TIPCALC`:** `B`=Baixa, `N`=Negociação

**Opções `TIPFECHCOM`:** `P`=Folha, `F`=Financeiro, `N`=Nenhuma

### TGFCTT
**Contatos dos Parceiros**

**PK:** `CODPARC`, `CODCONTATO`  
**Referenciada por:** 16 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONTATO` 🔑 | Inteiro | Contato |  |
| `TIPPESSOA` | Texto | Tipo de pessoa |  |
| `ATIVO` | Texto | Ativo |  |
| `NOMECONTATO` | Texto | Nome Contato |  |
| `TELEFONE` | Texto | Telefone |  |
| `TELRESID` | Texto | Telefone Residencial |  |
| `NIVELCOB` | Inteiro | Nivel p/cobranca |  |
| `CARGO` | Texto | Cargo |  |
| `EMAIL` | Texto | Email |  |
| `APELIDO` | Texto | Apelido |  |
| `DTNASC` | Data | Data Nascimento |  |
| `CPF` | Texto | CPF |  |
| `CNPJ` | Texto | CNPJ |  |
| `INSCESTAD` | Texto | Inscrição Estadual |  |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CEP` | Texto | CEP |  |
| `CODCID` | Inteiro | Cod. Cidade |  |
| `CODBAI` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NUMEND` | Texto | Numero |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `FAX` | Texto | Fax |  |
| `RAMAL` | Inteiro | Ramal |  |
| `CELULAR` | Texto | Celular |  |
| `DTCAD` | H | Data Cadastro |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `POSSUIACESSOBT` | Texto | Possui Acesso Banco Talentos |  |
| `SENHAACESSO` | Texto | Senha de acesso |  |
| `CODUSU` | Inteiro | Cod. Usuario B2B | → `TSIUSU`.`CODUSU` |
| `RECEBENOTAEMAIL` | Texto | Recebe Nota por email |  |
| `RECEBEBOLETOEMAIL` | Texto | Recebe boleto/Pix p/ email |  |
| `SOCIO` | Texto | Socio |  |
| `LATITUDE` | Texto | Latitude |  |
| `LONGITUDE` | Texto | Longitude |  |
| `CODREG` | Inteiro | Cod. Região | → `TSIREG`.`CODREG` |
| `RESPCOBRANCA` | Texto | Responsavel pela cobranca |  |
| `TIMRG` | Texto | RG |  |
| `TIMPROFISSAO` | Inteiro | Profissão | → `TIMPRF`.`PRFCODIGO` |
| `ENVIANOTIFCOTA` | Texto | Enviar notificações de cotação |  |
| `HABPLANENTCESTAS` | Texto | Participa plan. entrega cesta |  |
| `TIMNACIONALIDAD` | Inteiro | Nacionalidade | → `TSIPAI`.`CODPAIS` |
| `TIMAGENCIA` | Texto | Agencia |  |
| `QTDENTREGACESTAS` | Inteiro | Quantidade Cestas |  |
| `RECEMAILIMPPED` | Texto | Recebe e-mails de importação de pedidos |  |
| `TIMBANCO` | Inteiro | Banco | → `TSIBCO`.`CODBCO` |
| `TIMTIPO` | Inteiro | Tipo de Conta |  |
| `TIMCONTA` | Texto | Conta |  |
| `TIMBENEFICIARIO` | Texto | Benef. Repasse |  |
| `TIMPROCURADOR` | Inteiro | Procurador |  |
| `TIMREPRESENTANTE` | Texto | Representante |  |
| `DHALTER` | H | Dt. Alteração |  |
| `CODUSUALT` | Inteiro | Cod. Usuario Alteração |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `ENVIANOTIFCOTA`:** `N`=Não, `S`=Sim

**Opções `HABPLANENTCESTAS`:** `S`=Sim, `N`=Não

**Opções `POSSUIACESSOBT`:** `N`=Não, `S`=Sim

**Opções `RECEBEBOLETOEMAIL`:** `S`=Sim, `N`=Não

**Opções `RECEBENOTAEMAIL`:** `S`=Sim, `N`=Não

### TGFLOC
**Locais**

**PK:** `CODLOCAL`  
**Referenciada por:** 39 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLOCAL` 🔑 | Inteiro | Cod. Local |  |
| `DESCRLOCAL` | Texto | Descrição |  |
| `DH_SOMARSALEST` | Texto | Somar no Saldo de Estoque |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `CODTAB` | Inteiro | Tabela de preco | → `TGFNTA`.`CODTAB` |
| `VLRCUS` | Decimal | Valor de custo |  |
| `VLRVENDA` | Decimal | Valor de venda |  |
| `INCSOBREIRF` | Texto | Incide sobre IRF |  |
| `CODLOCALPAI` | Inteiro | Local Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `VALESTINDEP` | Texto | Val.Est.Independente |  |
| `DIASPRODUCAO` | Inteiro | Prazo de entrega (em dias) |  |
| `CAPACIDADEPRODUCAO` | Decimal | Capacidade de Produção |  |
| `DOMINGO` | Texto | Domingo |  |
| `SEGUNDA` | Texto | Segunda |  |
| `TERCA` | Texto | Terca |  |
| `QUARTA` | Texto | Quarta |  |
| `QUINTA` | Texto | Quinta |  |
| `SEXTA` | Texto | Sexta |  |
| `SABADO` | Texto | Sabado |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `ACEITANOVAPROD` | Texto | Aceita Novas Produções |  |
| `UTILIZAWMS` | Texto | Controlado pelo WMS |  |

**Opções `ACEITANOVAPROD`:** `S`=Sim, `N`=Não

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `DH_SOMARSALEST`:** `S`=Sim, `N`=Não

**Opções `DOMINGO`:** `N`=Não, `S`=Sim

**Opções `INCSOBREIRF`:** `S`=Sim, `N`=Não

### TGFVOL
**Volumes**

**PK:** `CODVOL`  
**Referenciada por:** 29 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODVOL` 🔑 | Texto | Sigla da Unidade |  |
| `DESCRVOL` | Texto | Descrição |  |
| `UTILIREGVOLWMS` | Texto | Utiliza no Registro de Volumes WMS |  |
| `DECQTD` | Inteiro | Decimais para quantidade |  |
| `CODVOLFCI` | Texto | Unidade para FCI |  |
| `UTILICONFPESO` | Texto | Utiliza Conferencia por peso |  |
| `ATUNUVERSAO` | Texto | Atualizar versão |  |
| `NUVERSAO` | Inteiro | Versão |  |

**Opções `UTILICONFPESO`:** `N`=Não, `S`=Sim

**Opções `UTILIREGVOLWMS`:** `N`=Não, `S`=Sim

### TGFEST
**Estoque**

**PK:** `CODEMP`, `CODPROD`, `CODLOCAL`, `CONTROLE`, `CODPARC`, `TIPO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ESTDOCAWMS` | Inteiro | Estoque em docas de entrada do WMS |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `CODLOCAL` 🔑 | Inteiro | Local | → `TGFLOC`.`CODLOCAL` |
| `CODPROD` 🔑 | Inteiro | Cod. Prod. | → `TGFPRO`.`CODPROD` |
| `CONTROLE` 🔑 | Texto | Controle |  |
| `ESTOQUE` | Decimal | Estoque |  |
| `RESERVADO` | Decimal | Reservado |  |
| `ESTMIN` | Decimal | Estoque Minimo |  |
| `ESTMAX` | Decimal | Estoque Maximo |  |
| `CODBARRA` | Texto | Cod. de Barras |  |
| `ATIVO` | Texto | Ativo |  |
| `DTVAL` | Data | Data de Validade |  |
| `CODPARC` 🔑 | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `TIPO` 🔑 | Texto | Tipo |  |
| `PERCPUREZA` | Decimal | % Pureza |  |
| `PERCGERMIN` | Decimal | % Germinação |  |
| `DTFABRICACAO` | Data | Data de Fabricação |  |
| `STATUSLOTE` | Texto | Status Lote |  |
| `WMSBLOQUEADO` | Decimal | Bloqueado no WMS |  |
| `CODAGREGACAO` | Texto | Cod. de Agregação |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `TIPO`:** `P`=Proprio, `T`=Terceiro

### TGFORD
**Ordens de Carga**

**PK:** `CODEMP`, `ORDEMCARGA`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TGFEMP`.`CODEMP` |
| `TOTALCARGA` | Decimal | Total da carga |  |
| `ORDEMCARGA` 🔑 | Inteiro | Ordem de carga |  |
| `TEMTRANSBORDO` | Texto | Transbordo |  |
| `DTINIC` | Data | Data inicio |  |
| `DTPREVSAIDA` | Data | Data prevista para saida |  |
| `CODVEICULO` | Inteiro | Veiculo | → `TGFVEI`.`CODVEICULO` |
| `CODREG` | Inteiro | Região | → `TSIREG`.`CODREG` |
| `CODPARCTRANSP` | Inteiro | Parceiro Transportadora | → `TGFPAR`.`CODPARC` |
| `CODPARCMOTORISTA` | Inteiro | Parceiro Motorista | → `TGFPAR`.`CODPARC` |
| `CODPARCORIG` | Inteiro | Parceiro Origem da Rota | → `TGFPAR`.`CODPARC` |
| `NROFROTA` | Inteiro | Nro. da Frota |  |
| `ROTEIRO` | Texto | Roteiro |  |
| `CODDOCA` | Inteiro | Doca p/ separação | → `TGWDCA`.`CODDOCA` |
| `ENTSAI` | Texto | Tipo de OC |  |
| `TIPCARGA` | Texto | Tipo de Carga |  |
| `SITUACAO` | Texto | Situação |  |
| `TIPEMBALAGEM` | Texto | Tipo de Embalagem |  |
| `KMINIC` | Decimal | Km Inicial |  |
| `KMFIN` | Decimal | Km Final |  |
| `HORASAIDA` | H | Hora da saida |  |
| `PESOMAX` | Decimal | Peso maximo |  |
| `M3MAX` | Decimal | Metros Cubicos Maximo |  |
| `VINCROT` | Texto | Gerar vinculação automatica da rota para ordem de carga |  |
| `TIPCALCFRETE` | Inteiro | Tipo de Calculo de Frete |  |
| `TIPDIST` | Texto | Tipo de Distancia p/ Valor Manual/Tabela |  |
| `CODROTA` | Inteiro | Rota | → `TGFROT`.`CODROTA` |
| `VLRFRETE` | Decimal | Valor do Frete |  |
| `CODLOCAL` | Inteiro | Local | → `TGFLOC`.`CODLOCAL` |
| `CODPARCDEST` | Inteiro | Parceiro Destino da Rota | → `TGFPAR`.`CODPARC` |
| `SEQCARGA` | Inteiro | Sequencia Carga |  |
| `ORDEMCARGAPAI` | Inteiro | Ordem Carga Pai |  |
| `CODTIPOPERTRANSB` | Inteiro | Tipo Operação |  |
| `DHINICIALPESAGEM` | H | Data e hora inicial Pesagem |  |
| `DHFINALPESAGEM` | H | Data e hora final Pesagem |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DTALTER` | H | Data de Alteração |  |
| `DTALTERROTCAT` | H | Data Alteração Erro Rotas |  |
| `FRETECALC` | Texto | Frete Calculo |  |
| `NUFINACERTO` | Inteiro | Numero Financeiro Acerto |  |
| `VLRDIFACERTO` | Decimal | Valor diferenca acerto |  |
| `NUCAIXA` | Inteiro | Numero do Caixa | → `TGFCAI`.`NUCAIXA` |
| `CODUSURETORNO` | Inteiro | Cod. Usuario Retorno | → `TSIUSU`.`CODUSU` |
| `DTRETORNO` | H | Data de Retorno |  |
| `QTDENTREGA` | Inteiro | Qtd. Entrega |  |
| `STATUSAVAL` | Texto | Avaliação de Veiculo/Motorista |  |
| `OBSMOTORISTA` | Texto | Observações |  |
| `JUSTIFICATIVA` | Texto | Justificativa de escolha-Veiculo/Motorista |  |
| `IDORDEMCARGA` | Texto | Cod. Barras |  |
| `ENVIOWMS` | Texto | Enviado p/ WMS |  |
| `PRIORIDADE` | Inteiro | Prioridade |  |
| `NUVIAG` | Inteiro | Numero da Viagem | → `TGFVIAG`.`NUVIAG` |
| `CODEMPPAI` | Inteiro | Empresa Pai |  |

**Opções `ENTSAI`:** `S`=Saida, `A`=Ambos, `E`=Entrada

**Opções `ENVIOWMS`:** `S`=Sim, `N`=Não

**Opções `SITUACAO`:** `F`=Fechada, `A`=Aberta

**Opções `STATUSAVAL`:** `S`=Avaliado, `N`=Aguardando nova avaliação, `null`=Aguardando avaliação

**Opções `TEMTRANSBORDO`:** `S`=Sim, `N`=Não

**Opções `TIPCALCFRETE`:** `8`=8 - Valor Fixo Mensal Tabela, `7`=7 - Valor Manual/Rateio por Valor, `6`=6 - Valor Manual/Rateio por Peso, `4`=4 - Valor por Rota/Rateio por Peso, `3`=3 - Valor por Formula/Ganho Logistico, `2`=2 - Valor por Formula/Rateio por Valor, `0`=0 - Escolha Manual, `1`=1 - Valor por Formula/Rateio por Peso, `5`=5 - Valor por Rota/Rateio por Valor

### TGFTIT
**Tipos de Titulo**

**PK:** `CODTIPTIT`  
**Referenciada por:** 16 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTIPTIT` 🔑 | Inteiro | Tipo de Titulo |  |
| `ATIVO` | Texto | Ativo |  |
| `DESCRTIPTIT` | Texto | Descrição |  |
| `SUBTIPOVENDA` | Texto | Subtipo |  |
| `ESPDOC` | Texto | Especie |  |
| `CREDENCIADORACFE` | Texto | Instituição Credenciadora do Cartão |  |
| `CARENCIA` | Inteiro | Float(Carencia) |  |
| `FISCAL` | Texto | Forma Pagamento TEF |  |
| `CONSDIASUTEIS` | Texto | Considerar dias uteis |  |
| `CARTAOTAXA` | Decimal | % Taxa Administradora |  |
| `VALIDAQTDMAXTITVENCIDOS` | Texto | Validar Qtd. Max. Titulos Vencidos |  |
| `EXIBBAIX` | Texto | Mensagem p/exibir na tela de baixa |  |
| `GRUPOLIMCRED` | Texto | Grupo p/Limite Credito |  |
| `CODMOEDA` | Inteiro | Moeda | → `TSIMOE`.`CODMOEDA` |
| `PERCJUROS` | Decimal | % Juros |  |
| `PERCMULTA` | Decimal | % Multa |  |
| `EXPTES` | Texto | Exportação para TES |  |
| `EXPGRS` | Inteiro | Exportação para GRS |  |
| `EXIGBAIXAACERTO` | Texto | Valor Baixado deve ser igual ao Retornado |  |
| `TRANSFDIF` | Texto | Transferir a diferenca entre o valor Retornado e o Baixado |  |
| `INDTIT` | Inteiro | Indicador do Tipo de Titulo |  |
| `TRANSFPEND` | Texto | Pode transferir titulo pendente |  |
| `TRANSFBAIX` | Texto | Pode transferir depois de baixado |  |
| `CODGRUPOTIPTIT` | Inteiro | Grupo | → `TGFGTT`.`CODGRUPOTIPTIT` |
| `CODCTACTB` | Inteiro | Conta Contabil 1 |  |
| `CODCTACTB2` | Inteiro | Conta Contabil 2 |  |
| `CODCTACTB3` | Inteiro | Conta Contabil 3 |  |
| `BAIXACERTO` | Texto | Pode Baixar |  |
| `CARTAODESC` | Decimal | Taxa Administradora |  |
| `PERCCUSVAR` | Decimal | % Custo variavel |  |
| `VLRCUSVAR` | Decimal | Valor Custo Variavel |  |
| `FASTUSA` | Texto | Utiliza no Fast Service |  |
| `FASTBAIXA` | Texto | Baixa automatica |  |
| `CONFERENCIA` | Texto | Conferencia |  |
| `IMPCOMPROVANTE` | Texto | Imprime comprovante |  |
| `IMPBOLRENEG` | Texto | Imprimir Pix/Boleto/Duplicata p/os titulos renegociados |  |
| `IMAGEM` | Blob | Imagem |  |
| `CODPARCTEF` | Inteiro | Parc.Administradora | → `TGFPAR`.`CODPARC` |
| `CODRECGNRE` | Inteiro | Codigo da Receita (GNRE) |  |
| `CODDETRECGNRE` | Inteiro | Codigo Detalhamento Receita (GNRE) |  |
| `CODPRODGNRE` | Inteiro | Codigo do Produto (GNRE) |  |
| `AJUSTAVP` | Texto | Ajusta Valor Presente |  |
| `TPAGNFCE` | Texto | Tipo de pgto para NFC-e / NF-e / CF-e |  |
| `PRAZO` | Inteiro | Prazo |  |
| `UTILIZAPOS` | Texto | Utiliza POS |  |
| `TIMUSADOLOCACAO` | Texto | Utilizado na Locação |  |
| `NROPARCELAS` | Inteiro | Nro. Parcelas |  |
| `NSUOPCIONALPOS` | Texto | Informar NSU opcional |  |
| `INTEGRAECONECT` | Texto | Integração EConect |  |
| `CODFINALIZADORA` | Inteiro | Cod. Finalizadora |  |
| `GRUPOFINALIZADORA` | Inteiro | Grupo Finalizadora |  |
| `CODBANDEIRAECONECT` | Texto | Bandeira Cartão |  |
| `CONVENIOECONECT` | Texto | Convenio |  |
| `DIAVENC` | Inteiro | Vencimento |  |
| `OPERACAOCTF` | Texto | Operação CTF |  |
| `TIPVENC` | Texto | Tipo vencimento |  |
| `QTDPARCELCTF` | Inteiro | Qtd. parcelas |  |
| `RECEBANTAPROV` | Texto | Receber antes de aprovar a nota |  |
| `ARREDPRIMEIRAPARC` | Texto | Ajusta arredondamento na 1 parcela |  |
| `TRUNCPARCELA` | Texto | Truncar valores no parcelamento |  |
| `TIPDOCRURAL` | Texto | Tipo Documento Rural |  |
| `DESCRTPAGNFCE` | Texto | Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) |  |
| `PROIBIMPBOL` | Texto | Proibir impressão boleto |  |
| `ULTILIZAPDVWEB` | Texto | Tip. titulo cartão principal PDV Web |  |
| `INFCOMPLEFDCONT` | Texto | Informações complem. (registro F525 - EFD Cont.) |  |
| `NROPARCELASMAX` | Inteiro | Qtd de parcelas Maxima |  |
| `ALTERASIMULTPV` | Texto | Permite alteração no tipo de negociação |  |
| `INDRECEFDCONT` | Texto | Indicador de Receita (registro F525 - EFD Cont.) |  |
| `VLRPARCMINCART` | Decimal | Valor de parcela minima para cartões |  |
| `INFCMC7` | Texto | Informar CMC7 |  |

**Opções `AJUSTAVP`:** `N`=Não, `S`=Sim

**Opções `ALTERASIMULTPV`:** `S`=Sim, `N`=Não

**Opções `ARREDPRIMEIRAPARC`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `BAIXACERTO`:** `S`=Sim, `N`=Não

**Opções `CONFERENCIA`:** `N`=Não, `S`=Sim

### TGFGRU
**Grupos de Produtos**

**PK:** `CODGRUPOPROD`  
**Referenciada por:** 12 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPOIMPOSTO` | Texto | Tipo de Imposto |  |
| `CODGRUPAI` | Inteiro | Grupo pai |  |
| `CODGRUPOPROD` 🔑 | Inteiro | Cod. do Grupo Produto |  |
| `DESCRGRUPOPROD` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `APRPRODVDA` | Texto | Apresenta produtos desse grupo na venda consultiva |  |
| `VISIVELAPPOS` | Texto | Apresentar produtos no aplicativo de Ordem de Servico |  |
| `GRUPOICMS` | Inteiro | Grupo de ICMS |  |
| `PERCCMTNAC` | Decimal | % Carga Media Trib. Nacional |  |
| `PERCCMTFED` | Decimal | % Carga Media Trib. Federal |  |
| `PERCCMTEST` | Decimal | % Carga Media Trib. Estadual |  |
| `PERCCMTMUN` | Decimal | % Carga Media Trib. Municipal |  |
| `PERCCMTIMP` | Decimal | % Carga Media Trib. Importação |  |
| `VALEST` | Texto | Valida estoque |  |
| `SOLCOMPRA` | Texto | Solicita Compra |  |
| `PEDIRLIB` | Texto | Pedir confirmação de liberação |  |
| `AGRUPALOCVALEST` | Texto | Agrupar local na validação de estoque |  |
| `CODNAT` | Inteiro | Cod. Natureza | → `TGFNAT`.`CODNAT` |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODRFA` | Inteiro | Regra armazenagem | → `TGWRFA`.`CODRFA` |
| `PARTICMETA` | Decimal | Participação na meta |  |
| `LIMCURVA_C` | Decimal | Limite Curva C |  |
| `PERCMETA` | Decimal | Meta percentual |  |
| `IMAGEM` | Blob | Imagem |  |
| `PERCMETACONTRIB` | Decimal | Meta contribuição |  |
| `QTDEXPOSICAO` | Decimal | Quantidade em exposição |  |
| `COMCURVA_B` | Decimal | Comissão curva B |  |
| `AREAOCUPUNID` | Inteiro | Area ocupada por unidade |  |
| `METAQTD` | Decimal | Meta quantitativa |  |
| `COMCURVA_A` | Decimal | Comissão curva A |  |
| `LIMCURVA_B` | Decimal | Limite Curva B |  |
| `GRAU` | Inteiro | Grau |  |
| `COMCURVA_C` | Decimal | Comissão curva C |  |
| `CODCTACTBEFD` | Inteiro | Conta Contabil para EFD | → `TCBPLA`.`CODCTACTB` |
| `CONSGRUPRODCAT42` | Texto | Considerar grupo de produto/servico na geração da Cat 42 |  |
| `DHALTER` | H | Dt. Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario Alteração |  |
| `CALRUPTURAESTOQUE` | Texto | Calcula Ruptura de Estoque |  |

**Opções `AGRUPALOCVALEST`:** `N`=Não, `S`=Sim

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `APRPRODVDA`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `CALRUPTURAESTOQUE`:** `N`=Não, `S`=Sim

**Opções `CONSGRUPRODCAT42`:** `S`=Sim, `N`=Não

### TGFFAM
**Familia de Produtos**

**PK:** `CODPRODPAI`, `CODPRODFILHO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPRODPAI` 🔑 | Inteiro | Produto pai | → `TGFPRO`.`CODPROD` |
| `CODPRODFILHO` 🔑 | Inteiro | Produto filho | → `TGFPRO`.`CODPROD` |
| `COMPLDESC` | Texto | Complemento |  |
| `MARCA` | Texto | Marca |  |
| `REFERENCIA` | Texto | Referencia |  |

### TGFTAB
**TabelaPreco**

**PK:** `NUTAB`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUTAB` 🔑 | Inteiro | Nro. Unico |  |
| `DTVIGOR` | Data | Dt. Vigor |  |
| `PERCENTUAL` | Decimal | Percentual % |  |
| `UTILIZADECCUSTO` | Texto | Utiliza decimais do custo para preco |  |
| `CODTABORIG` | Inteiro | Tabela de Origem | → `TGFNTA`.`CODTAB` |
| `DTALTER` | Data | Dt. Alteração |  |
| `CODTAB` | Inteiro | Codigo Tabela | → `TGFNTA`.`CODTAB` |
| `JAPE_ID` | Texto | JAPE_ID |  |

### TGFNTA
**Nome das Tabelas de Preco**

**PK:** `CODTAB`  
**Referenciada por:** 30 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODREG` | Inteiro | Região | → `TSIREG`.`CODREG` |
| `DECVENDA` | Inteiro | Casas decimais |  |
| `CODTAB` 🔑 | Inteiro | Codigo |  |
| `NOMETAB` | Texto | Nome |  |
| `OBS` | Texto | Observação |  |
| `ATIVO` | Texto | Ativo |  |
| `CODTIPPARC` | Inteiro | Perfil | → `TGFTPP`.`CODTIPPARC` |
| `CODTABFLEX` | Inteiro | Tabela p/ Flex | → `TGFNTA`.`CODTAB` |
| `INTEGRAECONECT` | Texto | Integrar com EConect |  |
| `CODMOEDA` | Inteiro | Moeda |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `INTEGRAECONECT`:** `S`=Sim, `N`=Não

### TGFVEI
**Veiculos**

**PK:** `CODVEICULO`  
**Referenciada por:** 16 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPOVEICULO` | Texto | Tipo Veiculo |  |
| `CODVEICULO` 🔑 | Inteiro | Codigo do Veiculo |  |
| `MARCAPLACA` | Texto | Marca [Placa] |  |
| `PLACA` | Texto | Placa |  |
| `CODCID` | Inteiro | Cidade Emplacamento |  |
| `MARCAMODELO` | Texto | Marca Modelo |  |
| `ESPECIETIPO` | Texto | Especie e Tipo |  |
| `CAPPOTCIL` | Texto | Cap/Pot/Cil |  |
| `COR` | Texto | Cor |  |
| `CATEGORIA` | Texto | Categoria |  |
| `PESOMAX` | Decimal | Peso Maximo |  |
| `M3MAX` | Decimal | Metros Cubicos Maximo |  |
| `ANOFABRIC` | Inteiro | Ano Fabricação |  |
| `ANOMOD` | Inteiro | Ano Modelo |  |
| `CHASSIS` | Texto | Chassis |  |
| `VLRDEPRECMENSAL` | Decimal | Depreciação mensal do veiculo |  |
| `NUMMOTOR` | Texto | Numero do Motor |  |
| `CODFORMFRETE` | Inteiro | Formula p/calculo de Frete | → `TSIFOR`.`CODFORM` |
| `RENAVAM` | Texto | RENAVAM |  |
| `CODMOTORISTA` | Inteiro | Motorista | → `TGFPAR`.`CODPARC` |
| `PROPRIO` | Texto | Veiculo da empresa |  |
| `CODPARC` | Inteiro | Parceiro ou Empresa |  |
| `CODPARCPROPANTT` | Inteiro | Parceiro ANTT | → `TGFPAR`.`CODPARC` |
| `VIATRANSP` | Texto | Via de Transporte |  |
| `COMBUSTIVEL` | Texto | Combustivel |  |
| `TIPO` | Texto | Tipo |  |
| `CODFUNC` | Inteiro | Funcionario |  |
| `CODEMPFOLHA` | Inteiro | Empresa |  |
| `ANTT` | Texto | RNTRC |  |
| `EMITEEXPED` | Texto | Emite Expedição |  |
| `CODMARCAMOD` | Inteiro | Cod.Marca/Modelo |  |
| `CORFAB` | Texto | Cor Fabricante |  |
| `POTENCIA` | Texto | Potencia |  |
| `DISTEIXOS` | Texto | Distancia entre Eixos |  |
| `SERIAL` | Texto | Serial |  |
| `CMKG` | Texto | Cap. Max. de Tração |  |
| `TIPINT` | Texto | Tipo Pintura |  |
| `TIPVEI` | Inteiro | Tipo de Veiculo |  |
| `ESPVEI` | Inteiro | Especie de Veiculo |  |
| `EMPPARC` | Texto | Empresa ou Parceiro |  |
| `CONDVIN` | Texto | Condição do VIN |  |
| `CONDVEI` | Inteiro | Condição do Veiculo |  |
| `DESCR_EMP_PARC` | Texto | Descrição do campo Parceiro ou Empresa |  |
| `VLRSEGMENSAL` | Decimal | Valor do Seguro Mensal |  |
| `TIPFORMFRETE` | Texto | Tipo de Formula de Frete | → `TSIFOR`.`TIPFORM` |
| `ATIVO` | Texto | Ativo |  |
| `VOLTAGEM` | Texto | Voltagem |  |
| `CODQUEST` | Inteiro | Questionario | → `TPQQU1`.`CODQUEST` |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `TIPOCOMBUST` | Inteiro | Tipo de Combustivel (Tabela RENAVAM) |  |
| `CORDENATRAN` | Inteiro | Codigo da Cor (Tabela DENATRAN) |  |
| `MAXLOTACAO` | Inteiro | Capacidade Maxima de Lotação |  |
| `RESTRICAO` | Inteiro | Restrição |  |
| `TIPOROD` | Texto | Tipo de Rodado |  |
| `TIPOCAR` | Texto | Tipo de Carroceria |  |
| `TIPOPROP` | Texto | Tipo de Proprietario |  |
| `TARA` | Decimal | Tara do veiculo |  |
| `CODCENCUS` | Inteiro | Centro Resultado |  |
| `AFERICAO` | Texto | Aferição |  |
| `TIPOAFERICAO` | Texto | Tipo Aferição |  |
| `CODBEM` | Texto | Codigo do bem |  |
| `CODEMBARCACAO` | Texto | Cod. Embarcação |  |
| `TIPOEMBARCACAO` | Inteiro | Tipo Embarcação |  |
| `NOMEEMBARCACAO` | Texto | Nome Embarcação |  |

**Opções `AFERICAO`:** `N`=Não Usa, `P`=Permitida, `O`=Obrigatoria

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `CONDVEI`:** `2`=2 - Inacabado, `3`=3 - Semi-Acabado, `1`=1 - Acabado

**Opções `CONDVIN`:** `R`=Remarcado, `N`=Normal

**Opções `EMITEEXPED`:** `N`=Não, `S`=Sim

**Opções `EMPPARC`:** `E`=Empresa, `P`=Parceiro

### TGFCFO
**Codigo Fiscal de Operações**

**PK:** `CODCFO`  
**Referenciada por:** 13 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCFO` 🔑 | Inteiro | Codigo |  |
| `DESCRCFO` | Texto | Descrição da CFOP |  |
| `TRIBUTADASCIAP` | Texto | Utilizar nas Tributadas do CIAP |  |
| `TIPICMS` | Texto | ICMS p/ o Livro Fiscal |  |
| `CODCTACTB` | Inteiro | Conta Contabil |  |
| `GRUPOCFO` | Inteiro | Grupo da CFOP |  |
| `TIPO` | Texto | Tipo |  |
| `CONVPRODUZ` | Texto | Convenio Produzir |  |
| `CALCDIFICMS` | Texto | Calcular Diferenca de ICMS |  |
| `DESCONSIDERARCFOREG47` | Texto | Desconsiderar CFOP na geração do registro 47 da DIME-SC |  |
| `RECBRUTAEFDBLOCOP` | Texto | Receita bruta p/EFD Contribuições |  |
| `TIPOPERPRODEPE` | Texto | Tipo de Operação PRODEPE |  |
| `MOVIMFISICA` | Texto | Movimentação Fisica do Item/Produto (IND_MOV C170 EFD) |  |
| `EMPCODSIT08EFD` | Texto | Empresas para considerar a situação do documento '08' nos EFDs |  |
| `RECBRUTACIAP` | Texto | Receita Bruta p/ CIAP |  |
| `INDAQUISICAO` | Texto | Indicador de Aquisição |  |
| `OPERESSACOMP` | Texto | Operação com Ressarcimento/Complemento de ST |  |

**Opções `CALCDIFICMS`:** `N`=Não, `S`=Sim

**Opções `CONVPRODUZ`:** `S`=Sim, `N`=Não

**Opções `DESCONSIDERARCFOREG47`:** `N`=Não, `S`=Sim

**Opções `GRUPOCFO`:** `700`=7.00 - Saida para o exterior, `500`=5.00 - Saida para o estado, `600`=6.00 - Saida para outro estado, `200`=2.00 - Entrada de outro estado, `300`=3.00 - Entrada do exterior, `100`=1.00 - Entrada do estado, `0`=0.00 - Definição Automatica

**Opções `INDAQUISICAO`:** `1`=1-Aquisição da produção de produtor rural pessoa fisica ou segurado especial em geral, `2`=2-Aquisição da produção de produtor rural PF ou segurado especial em geral por Entidade do PAA, `3`=3-Aquisição da produção de produtor rural pessoa juridica por Entidade do PAA, `4`=4-Aquisição de produção de produtor rural pessoa fisica ou segurado especial em geral, `5`=5-Aquisição de produção de produtor rural pessoa fisica ou segurado especial por entidade do PAA, `6`=6-Aquisição de produção de produtor rural pessoa juridica por entidade do PAA - Produção isenta, `7`=7-Aquisição de produção de produtor rural pessoa fisica ou segurado especial para fins de exportação

**Opções `MOVIMFISICA`:** `S`=Sim, `N`=Não, `null`=Não se aplica

### TGFSER
**Serie Produto**

**PK:** `NUNOTA`, `SEQUENCIA`, `SERIE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNOTA` 🔑 | Inteiro | Nro unico Nota |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `SERIE` 🔑 | Texto | Serie |  |
| `CODPROD` | Inteiro | Produto | → `TGFPRO`.`CODPROD` |
| `ATUALESTOQUE` | Inteiro | Atualiza estoque |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DTALTER` | H | Data/Hora da alteração |  |
| `SMARTCARD` | Texto | SmartCard |  |
| `SERIEFAB` | Texto | Serie do fabricante |  |
| `AVARIADO` | Texto | Avariado |  |

**Opções `AVARIADO`:** `N`=Não, `S`=Sim
