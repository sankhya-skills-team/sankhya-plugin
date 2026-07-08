# Tabelas TSI — Configuração do Sistema

Tabelas `TSI*` — base de configuração do Sankhya OM: usuários, empresas, grupos,
cidades, estados, bancos, endereços, parâmetros e controle de acesso.

### TSI001
**Autorização de Api**

**PK:** `NUAUT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAUT` 🔑 | Inteiro | Nu.Aut |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `PROVEDOR` | Texto | Provedor |  |
| `SERVICO` | Texto | Servico |  |
| `ATRIBUTO` | Texto | Atributo |  |
| `TIPOATRIBUTO` | Texto | Tipo Atributo |  |
| `CODUSUALTER` | Inteiro | Usuario de alteração | → `TSIUSU`.`CODUSU` |
| `TOTALACESSOS` | Inteiro | Quantidade de Servicos |  |
| `DHALTER` | H | Dh. Alteração |  |
| `METODO` | Texto | Metodo |  |

**Opções `TIPOATRIBUTO`:** `E`=Entidade, `T`=Texto, `S`=Sem Atributo, `N`=Numero

### TSIAGE
**Agencias Bancarias**

**PK:** `CODAGE`, `CODBCO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAGE` 🔑 | Texto | Agencia |  |
| `CODBCO` 🔑 | Inteiro | Banco | → `TSIBCO`.`CODBCO` |
| `NOMEAGE` | Texto | Nome da Agencia |  |
| `NOMEGER` | Texto | Nome do Gerente |  |
| `TELEFONE` | Texto | Telefone |  |
| `FAX` | Texto | Fax |  |
| `EMAIL` | Texto | Email |  |
| `CODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NUMEND` | Texto | Numero |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CEP` | Texto | CEP |  |
| `CODBAI` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CODCID` | Inteiro | Cod. Cidade |  |

### TSIARF
**TABLE TSIARF**

**PK:** `NURFE`, `SEQUENCIA`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `EMAILMANUAL` | C | EMAILMANUAL |  |
| `NURFE` 🔑 | Inteiro | NURFE | → `TSIRFE`.`NURFE` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `DHINI` | H | DHINI |  |
| `DHFIM` | H | DHFIM |  |
| `AGENDAMENTO` | Texto | AGENDAMENTO |  |
| `PROXEXEC` | H | PROXEXEC |  |
| `EXECUNICA` | Texto | EXECUNICA |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `ARQMODEMAIL` | Texto | ARQMODEMAIL |  |
| `CODUSURESP` | Inteiro | Usuario responsavel |  |
| `CODSMTP` | Inteiro | CODSMTP | → `TSISMTP`.`CODSMTP` |

**Opções `EXECUNICA`:** `S`=Sim, `N`=Não

### TSIAVI
**Avisos do sistema**

**PK:** `NUAVISO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUAVISO` 🔑 | Inteiro | Aviso |  |
| `DTEXPIRACAO` | Data | Dt. Expiração |  |
| `DTNOTIFICACAO` | Data | Dt. Notificação |  |
| `ORDEM` | Inteiro | Ordem |  |
| `TITULO` | Texto | Titulo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `SOLUCAO` | Texto | Solução |  |
| `IMPORTANCIA` | Inteiro | Importancia |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `CODGRUPO` | Inteiro | Grupo | → `TSIGRU`.`CODGRUPO` |
| `IDENTIFICADOR` | Texto | Identificador |  |
| `DHCRIACAO` | H | Dh. Criação |  |
| `TIPO` | Texto | Tipo |  |
| `CODUSUREMETENTE` | Inteiro | Remetente |  |
| `NUAVISOPAI` | Inteiro | Aviso Pai | → `TSIAVI`.`NUAVISO` |

### TSIBAI
**Bairros**

**PK:** `CODBAI`  
**Referenciada por:** 9 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODBAI` 🔑 | Inteiro | Codigo do Bairro |  |
| `NOMEBAI` | Texto | Nome |  |
| `CODREG` | Inteiro | Região | → `TSIREG`.`CODREG` |
| `DESCRICAOCORREIO` | Texto | Nome do Correio |  |
| `DTALTER` | H | Data de alteração |  |
| `ATUNUVERSAO` | Texto | Atualizar versão |  |

### TSIBCO
**Bancos**

**PK:** `CODBCO`  
**Referenciada por:** 12 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODBCO` 🔑 | Inteiro | Cod. Banco |  |
| `ABREVIATURA` | Texto | Abreviatura |  |
| `NOMEBCO` | Texto | Descrição |  |
| `CTACMC7INI` | Inteiro | Pos. Inicial (Conta CMC7) |  |
| `CTACMC7FIM` | Inteiro | Pos. Final (Conta CMC7) |  |

### TSICFA
**Liberação de Filtros**

**PK:** `CODFIL`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFIL` 🔑 | Inteiro | Cod. Filtro |  |
| `NUINSTANCIA` | Inteiro | Instancia |  |
| `NOMEFILTRO` | Texto | Nome do Filtro |  |
| `ATIVO` | Texto | Ativo |  |
| `EXPRESSAO` | C | Expressão |  |
| `AUTOR` | Inteiro | Autor Filtro |  |
| `DTCRIACAO` | H | Data Criação |  |
| `ALTERADOPOR` | Inteiro | Alterado Por |  |
| `DTALTERACAO` | H | Data Alteração |  |
| `OBSERVACAO` | Texto | Observação |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

### TSICID
**Cidades**

**PK:** `CODCID`  
**Referenciada por:** 29 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `UFNOMECID` | Texto | Cidade - UF |  |
| `CODCID` 🔑 | Inteiro | Cod. Cidade |  |
| `NOMECID` | Texto | Nome |  |
| `UF` | Inteiro | Cod. UF | → `TSIUFS`.`CODUF` |
| `DDD` | Texto | DDD |  |
| `CODREG` | Inteiro | Região | → `TSIREG`.`CODREG` |
| `DISTANCIA` | Inteiro | Distancia |  |
| `SEQENTREGA` | Inteiro | Sequencia de entrega |  |
| `POPULACAO` | Inteiro | População |  |
| `CODMUNFIS` | Inteiro | Mun. domicilio fiscal |  |
| `CODMUNSIAFI` | Inteiro | Cod. municipio SIAFI |  |
| `CODMUNDMS` | Inteiro | Cod. municipio DMS |  |
| `DESCRICAOCORREIO` | Texto | Nome do correio |  |
| `DTALTER` | H | Data de alteração |  |
| `VLRFRETEMIN` | Decimal | Valor de frete minimo |  |
| `VLRFRETETON` | Decimal | Valor de frete por tonelada |  |
| `TIPOFRETE` | Texto | Tipo de frete |  |
| `METARREDVLRISS` | Texto | Metodo de arredondamento do valor ISS |  |
| `VLRFRETEKM` | Decimal | Valor de frete por KM |  |
| `VLRTAXAENT` | Decimal | Valor taxa de entrada |  |
| `LINKAGUA` | Texto | Link conta agua |  |
| `TEMSUBSTITNFSE` | Texto | Tem substituição NFS-e |  |
| `LINKENERGIA` | Texto | Link conta energia |  |
| `QTDSUB` | Inteiro | Quantidade de substituições permitidas |  |
| `LINKIPTU` | Texto | Link conta IPTU |  |
| `QTDDIASSUB` | Inteiro | Prazo para substituição de NFS-e |  |
| `LATITUDE` | Texto | Latitude |  |
| `LONGITUDE` | Texto | Longitude |  |
| `VENDAMIN` | Decimal | Venda Minima |  |
| `AD_UF` | Texto | Nome + UF |  |
| `TIPCANCNFSE` | Texto | Tipo de cancelamento para NFS-e |  |
| `VLRLIMCANCNFSE` | Decimal | Valor limite para cancelamento NFS-e |  |
| `MOTCANCSUBNFSE` | Texto | Motivo de cancelamento para substituição de NFS-e |  |
| `TIMPARCPREFEITURA` | Inteiro | Parceiro Prefeitura | → `TGFPAR`.`CODPARC` |
| `ACTCANEXNT` | Texto | Permite cancelamento extemporaneo |  |
| `MAXNOTALOTENFSE` | Inteiro | Qtd. maxima de notas em um lote NFS-e |  |
| `GERCODNATISSJSON` | Texto | Gerar Codigo Natureza Operação ISS no Json |  |
| `NOINSCMUNPAR` | Texto | Não enviar insc. mun. quando ISS não incidir no municipio do parceiro |  |
| `TIPOCNAE` | Inteiro | Tipo de envio do CNAE |  |
| `NOFORMATLC116` | Texto | Não formatar LC116 |  |
| `CNAEFULLNFSE` | Texto | Usar CNAE completo |  |
| `ENVITENSSEPJSON` | Texto | Enviar itens de NFS-e separados no Json |  |
| `GERNUNFSEINFCPM` | Texto | Gerar o n da NFSe nas Inf. Complementares da Substituição |  |
| `ENVFPJSON` | Texto | Enviar forma de pagamento no Json |  |
| `QTDMAXENVITENSJSON` | Inteiro | Quantidade Maxima p/ enviar itens NFS-e no Json |  |
| `VMINRETENCAOISS` | Decimal | Valor minimo para retenção |  |
| `INFQTDVLRUNIJSON` | Texto | Enviar quantidade e valor unitario no Json |  |
| `JSONSEMALIDENMUN` | Texto | Envia aliquota no Json apenas quando o ISS for devido a outro municipio |  |
| `ENVTAGDESCONJSON` | Texto | Enviar tag descontoCondicionado no metadados do Json |  |
| `ENVMULEMAILJSON` | Texto | Envia multiplos e-mails no Json |  |
| *... +12 campos adicionais* | | | |

**Opções `ACTCANEXNT`:** `S`=Sim, `N`=Não

**Opções `CNAEFULLNFSE`:** `N`=Não, `S`=Sim

**Opções `ENVCODIGONBSJSON`:** `S`=Sim, `N`=Não

**Opções `ENVFPJSON`:** `N`=Não, `S`=Sim

**Opções `ENVITENSSEPJSON`:** `S`=Sim, `N`=Não

**Opções `ENVMULEMAILJSON`:** `N`=Não, `S`=Sim

### TSICLA
**Classificação de campos proteção de dados**

**PK:** `CODCLA`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCLA` 🔑 | Inteiro | Codigo da Classificação |  |
| `DESCCLA` | Texto | Descrição da Classificação |  |
| `CODUSUCRIAC` | Inteiro | Codigo usuario criação |  |
| `DTCRIAC` | H | Data criação |  |
| `CODUSUALTER` | Inteiro | Codigo usuario alteração |  |
| `DTALTER` | H | Data alteração |  |

### TSICPO
**Configuração de Pedido Offline**

**PK:** `CODCONFIG`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONFIG` 🔑 | Inteiro | Cod. Config |  |
| `DESCRCONFIG` | Texto | Descrição |  |
| `CODEMP` | Inteiro | Cod. Empresa | → `TSIEMP`.`CODEMP` |
| `PADRAO` | Texto | Padrão |  |
| `CAPTURAGEO` | Texto | Capturar geolocalização |  |
| `FOTOPRODUTO` | Texto | Sincronizar fotos dos produtos |  |
| `PARCEIROEXP` | Texto | Parceiros |  |
| `PRODUTOEXP` | Texto | Produtos |  |
| `TIPONEGOCIACAOEXP` | Texto | Tipos de Negociação |  |

**Opções `CAPTURAGEO`:** `S`=Sim, `N`=Não

**Opções `FOTOPRODUTO`:** `S`=Sim, `N`=Não

**Opções `PADRAO`:** `S`=Sim, `N`=Não

### TSICTA
**Contas Bancarias**

**PK:** `CODCTABCOINT`  
**Referenciada por:** 32 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCTABCOINT` 🔑 | Inteiro | Codigo da conta bancaria |  |
| `LOGOURL` | Texto | Guarda logomarca |  |
| `TIPOBOLETO` | Texto | Tipo Boleto |  |
| `PJBCRED` | Texto | Credencial |  |
| `PJBCONBAIXCRED` | Texto | Conciliar a baixa do titulo ao receber o credito |  |
| `PJBCHAVE` | Texto | Chave |  |
| `BJBBAIBOLPAG` | Texto | Baixar o tilulo quando o boleto for pago |  |
| `CODCTABCO` | Texto | Conta |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODBCO` | Inteiro | Banco | → `TSIAGE`.`CODBCO` |
| `CODAGE` | Texto | Agencia bancaria | → `TSIAGE`.`CODAGE` |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `CODCTACTB` | Inteiro | Conta contabil | → `TCBPLA`.`CODCTACTB` |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `DTIMPLANT` | Data | Referencia p/ aceitar lancamentos |  |
| `SALDOBCO` | Decimal | Saldo do banco na referencia |  |
| `SALDOREAL` | Decimal | Saldo real na referencia |  |
| `EXCLUSIVA` | Texto | Exclusiva da empresa |  |
| `ATIVA` | Texto | Ativa |  |
| `CLASSE` | Texto | Tipo de conta |  |
| `NUMCHEQ` | Inteiro | Ultimo nro. cheque |  |
| `CODOPEREXCL` | Inteiro | Operador exclusivo |  |
| `CODMOEDA` | Inteiro | Moeda | → `TSIMOE`.`CODMOEDA` |
| `CODCORRBCO` | Inteiro | Correspondente bancario |  |
| `CARTEIRA` | Inteiro | Carteira |  |
| `CONVENIO` | Inteiro | Convenio |  |
| `INSTRUCAOI` | Inteiro | Instrução I |  |
| `INSTRUCAOII` | Inteiro | Instrução II |  |
| `DIASPROT` | Inteiro | Dias para protesto |  |
| `CODCTABCOINTREM` | Inteiro | Conta p/controlar a seq.de remessa |  |
| `SEQREM` | Inteiro | Sequencia remessa |  |
| `REMFINAL` | Inteiro | Nro max.p/seq.remessa |  |
| `SEQREM2` | Inteiro | Sequencia remessa alternativa |  |
| `REMFINAL2` | Inteiro | Nro max.p/seq.remessa alternativa |  |
| `CODLANCBAIXABOLRAP` | Inteiro | Lancamento baixa boleto |  |
| `REMBCO` | Inteiro | Ultimo boleto |  |
| `CODTIPOPERBAIXABOLRAP` | Inteiro | TOP Baixa boleto |  |
| `REMBCOMAX` | Inteiro | Numero maximo |  |
| `ZERARAUT` | Texto | Zerar automaticamente |  |
| `EMITEBOLETA` | Texto | Emite |  |
| `CTADEFEMIBOL` | Texto | Conta padrão para emissão |  |
| `IMPBOLETA` | Texto | Impressora |  |
| `TIPOIMPRESSORA` | Texto | Tipo impressora |  |
| `MODBOLETA` | Inteiro | Modelo |  |
| `VLRMINBOLETA` | Decimal | Valor minimo |  |
| `CTAMINBOLETA` | Inteiro | Alterar p/outra conta | → `TSICTA`.`CODCTABCOINT` |
| `TAXA` | Decimal | Ou cobrar taxa |  |
| `NURFEMODCHEQG` | Inteiro | Modelo de cheque | → `TSIRFE`.`NURFE` |
| `DTALTER` | Data | Data alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| *... +65 campos adicionais* | | | |

**Opções `APIBAIXAAUTOMATICA`:** `R`=Realizar na data de pagamento, `N`=Não realizar, `C`=Realizar na data do credito em conta

**Opções `APICONCILIACAOAUTOMATICA`:** `C`=Realizar na data do credito em conta, `N`=Não realizar, `R`=Realizar na data de pagamento

**Opções `ATIVA`:** `S`=Sim, `N`=Não

**Opções `CLASSE`:** `C`=Corrente, `G`=Garantida, `S`=Socios, `A`=Aplicação, `O`=Outros, `X`=Caixa-Tesouraria, `E`=Emprestimo, `D`=Adiantamento, `M`=Comissões, `Z`=Caixa (PDV)

**Opções `CODCONTARURAL`:** `999`=999 - Em transito, `000`=000 - Caixa

**Opções `CONCAUTRECEBPIX`:** `S`=Sim, `N`=Não

### TSICUS
**Centros de Resultado**

**PK:** `CODCENCUS`  
**Referenciada por:** 30 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCENCUS` 🔑 | Inteiro | Codigo |  |
| `DESCRCENCUS` | Texto | Descrição |  |
| `CALCELALURPARTEA` | Texto | CR para calculo e-LALUR (Parte A) |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `VEICULO` | Texto | Veiculo Obrigatorio |  |
| `CODUSURESP` | Inteiro | Usuario Responsavel | → `TSIUSU`.`CODUSU` |
| `CODPARCRESP` | Inteiro | Parceiro Responsavel | → `TGFPAR`.`CODPARC` |
| `AREA` | Decimal | Area |  |
| `CODUNN` | Inteiro | Unidade de negocio | → `TGFUNN`.`CODUNN` |
| `DTINCLUSAO` | H | Dt. Inclusão |  |
| `AREAREAL` | Decimal | Area Real |  |
| `AREACONT` | Decimal | Area Contabil |  |
| `CODTAB` | Inteiro | Tabela de Preco | → `TGFNTA`.`CODTAB` |
| `AREAPERM` | Decimal | Area Permutada |  |
| `FRACGEREN` | Decimal | Fração Real |  |
| `FRACCONT` | Decimal | Fração Contabil |  |
| `GRAU` | Inteiro | Grau |  |
| `CODUNG` | Inteiro | Unidade Gerencial | → `TMIUNG`.`CODUNG` |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODCENCUSPAI` | Inteiro | Cod.Centro Resultado Pai |  |
| `AD_IDEXTERNO` | Texto | ID do registro no sistema legado |  |

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `CALCELALURPARTEA`:** `S`=Sim, `N`=Não

**Opções `VEICULO`:** `S`=Sim, `N`=Não

### TSIDSB
**Tabela de Dashboards**

**PK:** `NUDSB`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDSB` 🔑 | Inteiro | Dashboard |  |
| `TITULO` | Texto | Titulo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `LAYOUT` | C | Layout |  |
| `GRUPO` | Texto | Grupo |  |
| `CODUSUINC` | Inteiro | Cod. Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | Data/Hora Modificação |  |

### TSIEMP
**Empresas**

**PK:** `CODEMP`  
**Referenciada por:** 38 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod. Empresa |  |
| `COOPERATIVA` | Texto | Cooperativa |  |
| `TIPOREGRA` | Texto | Tipo p/ Certificação de Regra |  |
| `NOMEFANTASIA` | Texto | Nome Fantasia |  |
| `RAZAOSOCIAL` | Texto | Razão Social |  |
| `RAZAOABREV` | Texto | Razão Abreviada |  |
| `CODEMPMATRIZ` | Inteiro | Empresa Matriz | → `TSIEMP`.`CODEMP` |
| `RAZAOSOCIALCOMPLETA` | Texto | Razão Social Completa |  |
| `NUMPROPR` | Inteiro | Numero de Proprietarios |  |
| `USARAZAOSOCIAL` | Texto | Usar como Razão Social o campo |  |
| `PRINCTITULAR` | Texto | Principal Titular |  |
| `CGC` | Texto | CNPJ/CPF |  |
| `INSCESTAD` | Texto | Inscrição Estadual |  |
| `INSCMUN` | Texto | Inscrição Municipal |  |
| `CODCNL` | Texto | Codigo Nacional Localidade |  |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `EMPAGRUPARGOL` | Inteiro | Empresa p/ Agrupar no GOL |  |
| `LIMCURVA_B` | Decimal | Limite Curva B |  |
| `LIVROSFISCAIS` | Texto | Livros Fiscais |  |
| `CODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NUMEND` | Texto | Numero |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CODBAI` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CODCID` | Inteiro | Cod. Cidade | → `TSICID`.`CODCID` |
| `CEP` | Texto | CEP |  |
| `TELEFONE` | Texto | Telefone |  |
| `FAX` | Texto | Fax |  |
| `TELEX` | Texto | Telex |  |
| `EMAIL` | Texto | Email |  |
| `HOMEPAGE` | Texto | Home Page |  |
| `CODMUN` | Inteiro | Cod. Municipio |  |
| `NATESTAB` | Inteiro | Natureza Estabelecimento |  |
| `NATJUR` | Inteiro | Natureza Juridica |  |
| `RAMOATIV` | Texto | Ramo de Atividade |  |
| `CNAEPREPON` | Inteiro | CNAE Preponderante |  |
| `ATIVECON` | Inteiro | Atividade Economica |  |
| `REGJUNTACOM` | Texto | Reg. Junta Comercial (NIRE) |  |
| `DTREGJUNTA` | Data | Data Registro na Junta (NIRE) |  |
| `DTCONVSOC` | Data | Data Conversão (Sociedade Simples p/ Empresaria) |  |
| `SIMPLES` | Texto | Optante pelo SIMPLES |  |
| `SIMPLESNACNAUF` | Texto | Tem convenio Simples Nacional no Estado |  |
| `CODREGTRIB` | Inteiro | Cod. Regime Tribut. |  |
| `INDCOOP` | Inteiro | Cooperativa |  |
| `TIPOSN` | Inteiro | Tipo de Partilha/Anexo SN |  |
| `SERIENFDES` | Texto | Serie NF DES-BH |  |
| `INDCONSTR` | Inteiro | Construtora |  |
| `INFOOBRA` | Inteiro | Contribuição Patronal |  |
| `MODELONFDES` | Texto | Modelo Nota Fiscal |  |
| `ACDINTISENMULTA` | Inteiro | Acordo internacional Isenção |  |
| `ESTOQUE` | Texto | Estoque |  |
| *... +26 campos adicionais* | | | |

**Opções `ACDINTISENMULTA`:** `null`=Não se Aplica, `0`=Sem acordo, `1`=Com acordo

**Opções `CARGAS`:** `S`=Sim, `N`=Não

**Opções `CODREGTRIB`:** `3`=Regime Normal, `2`=Simples Nacional - Sublimite, `1`=Simples Nacional

**Opções `COMISSOES`:** `S`=Sim, `N`=Não

**Opções `COOPERATIVA`:** `N`=Não, `S`=Sim

**Opções `DUPLIV`:** `N`=Não, `S`=Sim

### TSIEND
**Enderecos**

**PK:** `CODEND`  
**Referenciada por:** 9 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEND` 🔑 | Inteiro | Cod.Endereco |  |
| `TIPOENDERECO` | Texto | Endereco |  |
| `NOMEEND` | Texto | Nome |  |
| `TIPO` | Texto | Tipo |  |
| `DESCRICAOCORREIO` | Texto | Nome do correio |  |
| `DTALTER` | H | Data de Alteração |  |
| `CODLOGRADOURO` | Texto | Cod. Logradouro p/ E-social | → `TFPLGR`.`CODLOGRADOURO` |
| `ATUNUVERSAO` | Texto | Atualizar versão |  |

### TSIEVE
**Eventos para Calculo de Frete**

**PK:** `CODEVENTO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEVENTO` 🔑 | Inteiro | Cod. Evento |  |
| `DESCREVENTO` | Texto | Descrição |  |
| `GRUPO` | Texto | Grupo |  |
| `CODSERV` | Inteiro | Servico | → `TGFPRO`.`CODPROD` |
| `SINAL` | Inteiro | Sinal |  |

**Opções `SINAL`:** `1`=Receita, `-1`=Despesa, `0`=Neutro

### TSIFIL
**Fila de Impressão de Boleto**

**PK:** `NOMEFILA`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMEFILA` 🔑 | Texto | Nome Fila |  |
| `CODCTABCOINT` | Inteiro | Conta | → `TSICTA`.`CODCTABCOINT` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data | Data de Alteração |  |
| `REMBCO` | Inteiro | Ultimo boleto impresso |  |
| `REMFINAL` | Inteiro | Ultimo boleto no formulario |  |
| `TIPOIMPRESSORA` | Texto | Tipo Impressora |  |
| `IMPRESSORA` | Texto | Impressora |  |

**Opções `TIPOIMPRESSORA`:** `7`=XEROX LAZER, `3`=RIMA/ITAUTEC, `1`=ELEBRA/RIMA, `2`=EPSON, `4`=ELGIN, `5`=OUTRAS, `6`=DESKJET

### TSIFOR
**Tabela de Formulas Generica**

**PK:** `TIPFORM`, `CODFORM`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFORM` 🔑 | Inteiro | Codigo |  |
| `DESCRFORM` | Texto | Descrição da Formula |  |
| `TIPFORM` 🔑 | Texto | Tipo Formula |  |
| `TIPDIST` | Texto | Tipo distribuição |  |
| `FORMULA` | Texto | Formula |  |
| `FORMULAWEB` | Texto | Formula Web |  |
| `INDCUSTO` | Decimal | Perc. do valor a ser usado no custo |  |
| `CONSIDERARRATEIO` | Texto | Considerar regras de rateio ao apropriar CIP |  |

**Opções `CONSIDERARRATEIO`:** `N`=Não, `S`=Sim

**Opções `TIPDIST`:** `A`=Entre parceiros ou cidades, `N`=Não calcular Distancia, `C`=Entre cidades, `P`=Entre parceiros

### TSIFTM
**Formatador de Master**

**PK:** `CODIGO`, `MODULO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Codigo |  |
| `MODULO` 🔑 | Texto | Modulo |  |
| `TITULO` | Texto | Titulo |  |
| `TAMREGISTRO` | Inteiro | Tamanho do Registro |  |
| `PROGRAMA` | Texto | Programa |  |
| `CODBCO` | Inteiro | Codigo do banco |  |
| `GRAU` | Inteiro | Grau |  |

### TSIGBC
**Perguntas Aprendidas pela BIA**

**PK:** `CODGBC`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGBC` 🔑 | Inteiro | Codigo |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `NUDSB` | Inteiro | Dashboard | → `TSIDSB`.`NUDSB` |
| `RESOURCEID` | Texto | ID da Tela |  |
| `PERGUNTA` | Texto | Pergunta |  |
| `QTDUSO` | Inteiro | Quantidade de uso da pergunta |  |

### TSIGBI
**Informações de Gadgets p/ BIA**

**PK:** `CODGBI`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGBI` 🔑 | Inteiro | Codigo |  |
| `NUGDG` | Inteiro | Gadget | → `TSIGDG`.`NUGDG` |
| `IDLVL` | Texto | ID do Nivel |  |
| `IDCMP` | Texto | ID do Componente |  |
| `IDINFOBIA` | Texto | ID da Informação |  |
| `DESCRGBI` | Texto | Descrição |  |
| `CAMPOVALOR` | Texto | Campo para Valor |  |
| `CAMPOAGRUP` | Texto | Campo para Agrupamento |  |

### TSIGDG
**Tabela de Gadgets**

**PK:** `NUGDG`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUGDG` 🔑 | Inteiro | Codigo |  |
| `TEMHTML5` | Texto | Possui HTML5 |  |
| `TITULO` | Texto | Titulo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CONFIG` | C | Configuração (XML) |  |
| `THUMBNAIL` | Blob | Thumbnail |  |
| `CATEGORIA` | Texto | Categoria |  |
| `ATIVO` | Texto | Ativo |  |
| `CODUSUINC` | Inteiro | Cod. Usuario Inclusão | → `TSIUSU`.`CODUSU` |
| `CODUSU` | Inteiro | Cod. Usuario Modificação | → `TSIUSU`.`CODUSU` |
| `DHALTER` | H | Dt./Hora Modificação |  |
| `URLCOMPONENTE` | Texto | URL do Componente |  |
| `QTDANALISESUTILIZADAS` | Inteiro | Quantidade de Analises |  |
| `HTML5` | Blob | HTML5 |  |
| `EVOCARD` | Texto | Cartão Inteligente |  |
| `LAYOUT` | Texto | Layout |  |
| `GDGASSINADO` | Texto | Assinado |  |
| `APVNC` | Texto | Atualiza Preco pela Nota de compra |  |

**Opções `APVNC`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `GDGASSINADO`:** `N`=Não, `S`=Sim

**Opções `TEMHTML5`:** `N`=Não, `S`=Sim

### TSIGRE
**Grupo de Relatorios**

**PK:** `CODGRUPOREL`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOREL` 🔑 | Inteiro | Cod.Grupo Relatorio |  |
| `DESCRGRUPOREL` | Texto | Descrição |  |
| `CODGRUPORELPAI` | Inteiro | Cod.Grupo Relatorio Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Não

### TSIGRU
**Grupos de usuarios**

**PK:** `CODGRUPO`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOMEGRUPO` | Texto | Nome |  |
| `EMAIL` | Texto | Email |  |
| `CODGRUPO` 🔑 | Inteiro | Codigo |  |
| `CODUNN` | Inteiro | Unidade de negocio | → `TGFUNN`.`CODUNN` |
| `USER_NAME` | Texto | Nome do Usuario |  |
| `ATIVO` | Texto | Ativo |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

### TSIGUF
**GNRE Unidade Federativa**

**PK:** `CODGUF`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGUF` 🔑 | Inteiro | Codigo GNRE Unidade Federativa |  |
| `CODSTGNRE` | Texto | Codigo da Receita (GNRE) |  |
| `CODRECDIME` | Inteiro | Codigo da Receita (DIME) |  |
| `CODCLSVENCDIME` | Inteiro | Codigo Classe Vencimento (DIME) |  |
| `CODDETGNRE` | Inteiro | Codigo Detalhamento Receita (GNRE) |  |
| `CODPRODGNRE` | Inteiro | Codigo do Produto (GNRE) |  |
| `CODUF` | Inteiro | Cod. Unidade Federativa | → `TSIUFS`.`CODUF` |
| `PROTOCOLOCONVENIO` | Texto | Protocolo/Convenio (GNRE) |  |
| `CODCAMPOEXTRAGNRE` | Inteiro | Codigo (Campos Extras GNRE) |  |
| `CODCAMPOEXTRAGNRE2` | Inteiro | Codigo (Campos Extras GNRE 2) |  |
| `VALORCAMPOEXTRA` | Texto | Valor para Campo Extra GNRE |  |
| `VLRPERSGNRE` | Texto | Valor personalizado GNRE |  |
| `VERSAOGNRE` | Texto | Versão GNRE |  |
| `CODFCPSTGNRE` | Inteiro | Codigo da Receita (GNRE) p/ FCP ST |  |
| `TIPODOC` | Inteiro | Tipo de documento |  |
| `CODRECDIMEFCPST` | Inteiro | Codigo da Receita (DIME) para FCP ST |  |
| `CODCLSVENCDIMEFCPST` | Inteiro | Codigo Classe Vencimento (DIME) p/ FCP ST |  |
| `TIPOINFO` | Texto | Tipo da Informação |  |
| `GERINFCAMPADICGNRE` | Texto | Gera Informação dos Campos Adicionais na GNRE |  |
| `TIPAPURACAO` | Texto | Tipo Apuração |  |
| `CODOBR` | Inteiro | Codigo |  |

**Opções `CODOBR`:** `2`=ICMS da substituição tributaria pelas saidas para o Estado, `999`=ICMS da substituição tributaria pelas saidas para outro Estado, `0`=ICMS normal a recolher, `1`=ICMS da substituição tributaria pelas entradas, `3`=Antecipação do diferencial de aliquotas do ICMS, `4`=Antecipação do ICMS da importação, `5`=Antecipação tributaria, `6`=ICMS resultante da aliquota adicional dos itens incluidos no Fundo de Combate a Pobreza, `90`=Outras obrigações do ICMS

**Opções `GERINFCAMPADICGNRE`:** `S`=Sim, `N`=Não

**Opções `TIPAPURACAO`:** `C`=ICMS, `S`=ICMS ST, `D`=ICMS DIFAL, `F`=ICMS FCP, `B`=ST FCP Interno, `T`=ICMS ST FCP, `A`=ICMS FCP Interno

**Opções `TIPOINFO`:** `C`=Chave do documento, `N`=Nota Fiscal (Numero da nota)

**Opções `VALORCAMPOEXTRA`:** `D`=Data de Emissão, `O`=Observação, `C`=Chave NF-e/CT-e, `null`=Chave NF-e/CT-e e Observação

**Opções `VERSAOGNRE`:** `200`=2.0, `100`=1.0

### TSIHCF
**Historico de Copia de Configuração**

**PK:** `NUNICO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNICO` 🔑 | Inteiro | Num. Unico |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `DHALTER` | H | Data Criação |  |
| `TIPO` | Texto | Tipo |  |
| `ABASEG` | Texto | Conf. Seguranca |  |
| `REMOVEANT` | Texto | Remover Conf. Atuais |  |
| `CHAVE` | Texto | Chave |  |
| `SELECAOTELAS` | Texto | Seleção de telas |  |
| `CONFTOP` | Texto | Configurações de Top |  |

**Opções `ABASEG`:** `S`=Sim, `N`=Não

**Opções `CONFTOP`:** `S`=Sim, `N`=Não

**Opções `REMOVEANT`:** `S`=Sim, `N`=Não

**Opções `TIPO`:** `F`=Filtros, `P`=Personalizações, `A`=Acessos, `C`=Tela/Filtros, `O`=Exceções/Restrições da Top, `X`=Personalizações/Acessos, `T`=Tela

### TSIIMP
**Formatador de Relatorios**

**PK:** `CODREL`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ACESSOCUBO` | Texto | Acessos do cubo |  |
| `TEMLAYOUTSW` | Texto | Usa modelo IReport |  |
| `TIPO` | Texto | Tipo |  |
| `CODREL` 🔑 | Inteiro | Cod.Relatorio |  |
| `NOME` | Texto | Nome |  |
| `CODGRUPOREL` | Inteiro | Grupo Relatorio | → `TSIGRE`.`CODGRUPOREL` |
| `ESCOLHIDOS` | Texto | Escolhidos |  |
| `ORDEM` | Texto | Ordem |  |
| `RESUMO` | Texto | Resumo |  |
| `FILTROS` | Texto | Filtros |  |
| `CONTASBCO` | Texto | Contas Bancarias |  |
| `FILTROS2` | Texto | Filtros2 |  |
| `PARAMSGEN` | Texto | ParamsGen |  |
| `LISTA1` | Texto | Lista1 |  |
| `LISTA2` | Texto | Lista2 |  |
| `LISTA3` | Texto | Lista3 |  |
| `LISTA4` | Texto | Lista4 |  |
| `ORIENTACAO` | Texto | Orientação do relatorio |  |
| `TIPOFONTE` | Texto | Tipo da Fonte |  |
| `TAMFONTE` | Inteiro | Tamanho da fonte |  |
| `PERSONALIZADO` | Texto | Personalizado |  |
| `LAYOUT` | Blob | Layout |  |
| `GRAFIC` | Blob | Grafico |  |
| `DTINICIAL` | H | Data inicial |  |
| `DTFINAL` | H | Data final |  |
| `CODEMP` | Inteiro | Cod.Empresa |  |
| `ORIGEM` | Inteiro | Origem |  |
| `NIVEL` | Inteiro | Nivel |  |
| `SANKHYA` | Texto | Modelo |  |
| `OBSERVACAO` | Texto | Observação |  |
| `LAYOUTSW` | Blob | Arquivo IReport |  |
| `FASTSERVICE` | Texto | Fast Service |  |
| `QTDVISUALIZACOES` | Inteiro | Qtd. visualizações |  |
| `AD_IDEXTERNO` | Texto | ID do registro no sistema legado |  |

**Opções `FASTSERVICE`:** `N`=Não, `S`=Sim

**Opções `SANKHYA`:** `N`=Não, `S`=Sim

### TSIIRT
**SI Detalhes do Retorno Movimento Bancario com Hierarquia**

**PK:** `CODIGO`, `SEQUENCIA`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Codigo | → `TSIRET`.`CODIGO` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `NOME` | Texto | Nome do Campo |  |
| `QTDDEC` | Inteiro | Decimais |  |
| `POSINI` | Inteiro | Inicio |  |
| `POSFIM` | Inteiro | Fim |  |
| `IDLINHA` | Texto | Identificador |  |
| `IDVALOR` | Texto | Conteudo p/Identificação |  |

**Opções `IDLINHA`:** `N`=Não, `S`=Sim

### TSIITA
**Acessos - Importador de Dados Tabelas**

**PK:** `CODITA`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODITA` 🔑 | Inteiro | Id tabela acesso |  |
| `DESCRICAO` | Texto | Descrição |  |

### TSIKIT
**Configuração de Kit**

**PK:** `CODCONFKIT`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONFKIT` 🔑 | Inteiro | Codigo |  |
| `DESCRCONFKIT` | Texto | Descrição |  |
| `CALCIMPKIT` | Texto | Calcula imposto do componente |  |
| `SOMACUSTOCOMPKIT` | Texto | Soma custo do componente ao kit |  |
| `SOMAPRECOCOMPKIT` | Texto | Soma preco do componente ao kit |  |
| `DISTRIBUIKITCOMP` | Texto | Distribuir preco do kit nos componentes |  |
| `DISTDESCKITCOMP` | Texto | Distribuir desconto do kit nos componentes |  |
| `UTILPRECOABACOMP` | Texto | Utiliza preco sugerido na aba 'Componentes' |  |
| `EXPLODCOMP` | Texto | Explodir componentes na grade de materia prima da central |  |
| `SOMAICMSCOMPKIT` | Texto | Soma ICMS do componente ao kit (Art. 42 do RICMS/2002-MG) |  |
| `FAKITESTCOMP` | Texto | Faturar apenas KIT com estoque de todos os componentes |  |

**Opções `CALCIMPKIT`:** `N`=Não, `S`=Sim

**Opções `DISTDESCKITCOMP`:** `N`=Não, `S`=Sim

**Opções `DISTRIBUIKITCOMP`:** `N`=Não, `S`=Sim

**Opções `EXPLODCOMP`:** `S`=Sim, `N`=Não

**Opções `FAKITESTCOMP`:** `S`=Sim, `N`=Não

**Opções `SOMACUSTOCOMPKIT`:** `S`=Sim, `N`=Não

### TSILBO
**Limite de liberação de bonificação**

**PK:** `NULBO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NULBO` 🔑 | Inteiro | Numero liberação de bonificação |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTINICIAL` | Data | Data Inicial |  |
| `DTFINAL` | Data | Data Final |  |
| `VLRLIMITE` | Decimal | Limite Bonificação |  |
| `EVENTO` | Inteiro | Evento |  |

### TSILIL
**Log importação legacy**

**PK:** `CODLIL`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLIL` 🔑 | Inteiro | Id importação |  |
| `DHEVENTO` | H | Data importação |  |
| `NOMEARQUIVO` | Texto | Arquivo processado |  |
| `EVENTO` | Texto | Evento |  |
| `TOTREG` | Inteiro | Total de registros |  |
| `TOTREGPROC` | Inteiro | Registros inseridos |  |
| `TOTATUALIZADO` | Inteiro | Registros atualizados |  |
| `TOTREJEITADO` | Inteiro | Registros rejeitados |  |
| `TEMPOTOTAL` | Texto | Tempo de execução |  |
| `ATUALIZAR` | Texto | Atualizar registros existentes |  |
| `REGRAS` | Texto | Validação de regras de negocio |  |
| `LOGFINAL` | Texto | Processo de importação |  |
| `REGRAENDERECO` | Texto | Regra de Importação de Endereco |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |

### TSIMEM
**Modelo e-mail**

**PK:** `CODMODELO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMODELO` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `TIPO` | Texto | Tipo de modelo |  |
| `CODSMTP` | Inteiro | Conta SMTP | → `TSISMTP`.`CODSMTP` |
| `ASSUNTO` | Texto | Assunto |  |
| `CONTEUDO` | C | Conteudo |  |
| `RESPONDERPARA` | Texto | Responder para |  |
| `CODUSUREMET` | Inteiro | Cod. Usuario Remetente |  |

### TSIMOD
**Modulo Adicional**

**PK:** `CODMODULO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMODULO` 🔑 | Inteiro | Modulo |  |
| `RESOURCEID` | Texto | Identificador |  |
| `DESCRMODULO` | Texto | Descrição |  |

### TSIMOE
**Moedas**

**PK:** `CODMOEDA`  
**Referenciada por:** 9 tabelas  

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

### TSIPAI
**Paises**

**PK:** `CODPAIS`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPAIS` 🔑 | Inteiro | Codigo do pais |  |
| `DESCRICAO` | Texto | Descrição |  |
| `ABREVIATURA` | Texto | Abreviatura |  |
| `CODPAISFIS` | Inteiro | Pais Domicilio Fiscal |  |
| `TIMNACIONALIDAD` | Texto | Nacionalidade |  |

### TSIPSQ
**Pesquisa Inteligente**

**PK:** `CODCFG`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCFG` 🔑 | Inteiro | Codigo CFG |  |
| `URI` | Texto | URL |  |
| `PORTA` | Inteiro | Porta |  |
| `USUARIO` | Texto | Usuario |  |
| `SENHA` | Texto | Senha |  |
| `ATIVO` | Texto | Ativo |  |
| `CRON` | Texto | Expressão de Gatilho |  |
| `STATUS` | Texto | Status |  |

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `STATUS`:** `W`=Configurado, `I`=Inativo, `P`=Parcialmente Ativo, `A`=Ativo

### TSIREG
**Regiões**

**PK:** `CODREG`  
**Referenciada por:** 9 tabelas  

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

### TSIREM
**Formatador de Remessa**

**PK:** `MODULO`, `CODIGO`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Codigo |  |
| `MODULO` 🔑 | Texto | Modulo |  |
| `TITULO` | Texto | Titulo |  |
| `TAMREGISTRO` | Inteiro | Tamanho do Registro |  |
| `CODPAI` | Inteiro | Cod.Formatador pai |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Detalhe |  |
| `GRAU` | Inteiro | Grau |  |
| `FILTRO` | Texto | Filtro |  |
| `COMGROUPBY` | Texto | Com Group By |  |
| `COMHAVING` | Texto | Com Having |  |
| `NOMEARQ` | Texto | Nome do arquivo |  |
| `COMSELECT` | Texto | Com Select |  |
| `COMORDERBY` | Texto | Com Order By |  |
| `UTILIZASEQALT` | Texto | Utiliza Sequencia Alternativa |  |
| `UTILIZASEQINFO` | Texto | Utiliza Sequencia Informada |  |
| `SEQINFO` | Inteiro | Sequencia Informada |  |
| `ORDENAR` | Texto | Ordenar |  |
| `FICHA` | Texto | Primeira coluna somente p/ ordenação |  |
| `ARQPORLAYOUTDETALHE` | Texto | Gerar um arquivo p/cada detalhe do layout |  |
| `ARQPORLINHA` | Texto | Gerar um arquivo p/cada linha |  |
| `INICARQREM` | Texto | Iniciais do arquivo p/ nome automatico |  |
| `CONF` | Texto | Configuração |  |
| `CONSULTASQLLOTE` | Texto | Consulta SQL |  |
| `AD_VERSAOLAYOUT` | Texto | VERSO DO LAYOUT |  |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ARQPORLAYOUTDETALHE`:** `S`=Sim, `N`=Não

**Opções `ARQPORLINHA`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `FICHA`:** `N`=Não, `S`=Sim

**Opções `ORDENAR`:** `N`=Não, `S`=Sim

### TSIRET
**Retorno Movimento Bancario com Hierarquia**

**PK:** `CODIGO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Cod.Layout |  |
| `TITULO` | Texto | Titulo do Layout |  |
| `SP_CHAMADA` | Texto | Stored Chamada |  |
| `CODPAI` | Inteiro | Cod.Pai |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `GRAU` | Inteiro | Grau |  |
| `USASQLNUFIN` | Texto | Usa SQL Para Numero Unico |  |
| `CONCEXTBANC` | Texto | Conciliação Extrato Bancario |  |
| `CONFIGTAXAADMIN` | Texto | Taxa Administrativa |  |
| `AD_VERSAOLAYOUT` | Texto | VERSO DO LAYOUT |  |

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `CONCEXTBANC`:** `N`=Não, `S`=Sim

**Opções `CONFIGTAXAADMIN`:** `G`=Considerar configuração global, `+`=Somar ao valor recebido, `-`=Subtrair do valor recebido, `D`=Destacar, `N`=Nada a fazer

**Opções `USASQLNUFIN`:** `S`=Sim, `N`=Não

### TSIRFE
**Relatorios**

**PK:** `NURFE`  
**Referenciada por:** 12 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CONFIG` | C | Configuração |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CATEGORIA` | Texto | Categoria |  |
| `DHALTER` | H | Data/Hora alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario |  |
| `NUINSTANCIA` | Inteiro | Instancia |  |
| `IDTELA` | Texto | IDTELA |  |
| `NURFEDEPENDENTE` | Inteiro | Nro relatorio dependente | → `TSIRFE`.`NURFE` |
| `FORMATO` | Texto | Formato de arquivo |  |
| `DSNAME` | Texto | Fonte de Dados |  |
| `PREFIXOANEXO` | Texto | Nome do anexo para e-mail |  |
| `TIPO` | Texto | Tipo |  |
| `NURFE` 🔑 | Inteiro | Numero |  |
| `NOMEIMPRESSORA` | Texto | Impressora |  |
| `EXPFILTROINSTANCIA` | Texto | Mostrar na Tela/Instancia quando |  |

**Opções `FORMATO`:** `E`=Excel (.xlsx), `P`=PDF, `X`=Excel (.xls), `W`=Word (.docx)

### TSIRHI
**Relatorios Hierarquicos**

**PK:** `CODUNI`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUNI` 🔑 | Inteiro | Cod.Unico |  |
| `PROGRAMA` | Texto | Programa |  |
| `CODCAMPO` | Inteiro | Cod.Campo |  |
| `CODCAMPOPAI` | Inteiro | Cod.Campo Pai |  |
| `SOHIERARQUIA` | Texto | So Hierarquia |  |
| `DESCRICAO` | Texto | Descrição |  |
| `TAMANHO` | Inteiro | Tamanho |  |
| `TIPO` | Texto | Tipo |  |
| `ALINHAMENTO` | Inteiro | Alinhamento |  |
| `TOTALIZA` | Texto | Totaliza/Filtro |  |
| `MASCARA` | Texto | Mascara |  |
| `EXPRESSAO` | Texto | Expressão |  |
| `TABELAS` | Texto | Tabelas |  |
| `LIGACAO` | Texto | Ligação |  |
| `SANKHYA` | Texto | Modelo Sankhya |  |
| `ZERARNAQUEBRA` | Texto | Zerar na quebra |  |

**Opções `ALINHAMENTO`:** `2`=Centro, `1`=Direita, `0`=Esquerda

**Opções `SANKHYA`:** `N`=Não, `S`=Sim

**Opções `SOHIERARQUIA`:** `S`=Sim, `N`=Não

**Opções `TIPO`:** `B`=Imagem, `$`=Dinheiro, `T`=Data/Hora, `D`=Data, `S`=Letras, `R`=Rich Text, `F`=Numero, `M`=Memo, `L`=Lista, `I`=Inteiro

**Opções `TOTALIZA`:** `N`=Não Totaliza, `X`=Não filtra, `S`=Totaliza

**Opções `ZERARNAQUEBRA`:** `N`=Não, `S`=Sim

### TSIRLG
**log acessos**

**PK:** `CODUSU`, `SEQACESSO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUSU` 🔑 | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `SEQACESSO` 🔑 | Inteiro | Sessão |  |
| `LOGIN` | H | Dh. Entrada |  |
| `LOGOUT` | H | Dh. Saida |  |
| `IP` | Texto | Endereco IP |  |
| `AGENTE` | Texto | Navegador |  |
| `EVENTO` | Texto | Evento |  |
| `SESSIONID` | Texto | SESSIONID |  |

**Opções `EVENTO`:** `B`=Bloqueado, `F`=Falha de login, `L`=Login, `D`=Desbloqueado

### TSIROT
**Tabela de Rotinas**

**PK:** `CODROT`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODROT` 🔑 | Inteiro | Cod.Rotina |  |
| `DESCRICAO` | Texto | Descrição |  |
| `COMANDO` | Texto | Camando a ser executado |  |

### TSIRTEF
**RedesTEF**

**PK:** `REDE`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REDE` 🔑 | Texto | Rede |  |
| `DESCRICAO` | Texto | Descrição |  |

### TSIRTM
**Mestre de Retorno**

**PK:** `CODIGO`, `TIPREG`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Cod.Layout |  |
| `TIPREG` 🔑 | Texto | Tipo de Registro |  |
| `TITULO` | Texto | Titulo do Layout |  |
| `TAMREG` | Inteiro | Tamanho Registro |  |
| `POSINITIPREG` | Inteiro | Pos Ini Tipo Registo |  |
| `SP_CHAMADA` | Texto | Stored Chamada |  |

### TSISMTP
**tabela servidor smtp**

**PK:** `CODSMTP`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSMTP` 🔑 | Inteiro | Cod. Conta |  |
| `SERVIDOR` | Texto | Servidor SMTP |  |
| `PORTA` | Inteiro | Porta |  |
| `TIPO` | Texto | Tipo de Conexão |  |
| `IGNORACERTIFICADO` | Texto | Ignorar validação do certificado do servidor |  |
| `REMETENTE` | Texto | Remetente |  |
| `USUARIO` | Texto | Usuario |  |
| `SENHA` | Texto | Senha |  |
| `UTILDOWNXML` | Texto | Utilizar para download de XML de DF-e |  |
| `SERVIDORPOP` | Texto | Servidor |  |
| `PORTAPOP` | Inteiro | Porta |  |
| `PADRAO` | Texto | Conta padrão |  |
| `USEOAUTH` | Texto | Autenticar com OAuth |  |
| `CODATH` | Inteiro | Configurações OAuth |  |
| `REFRESHTOKENV2` | C | Refresh Token V2 |  |
| `REFRESHTOKEN` | Texto | Refresh Token |  |
| `ACCESSTOKEN` | Texto | Refresh Token |  |
| `ACCESSTOKENV2` | C | Refresh Token V2 |  |
| `EXPIRESIN` | Texto | Expira em |  |

**Opções `IGNORACERTIFICADO`:** `N`=Não, `S`=Sim

**Opções `PADRAO`:** `N`=Não, `S`=Sim

**Opções `TIPO`:** `T`=Segura com TLS, `S`=Segura com SSL, `P`=Comum

**Opções `USEOAUTH`:** `S`=Sim, `N`=Não

**Opções `UTILDOWNXML`:** `N`=Não, `S`=Sim

### TSITHD
**Threads do Sistema**

**PK:** `ID`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Texto | Cod. Thread |  |
| `NAME` | Texto | Descrição |  |
| `DHINSERT` | Data | Dt. Captura |  |
| `STACKTRACE` | Blob | Trace |  |

### TSIUFS
**Unidade Federativa**

**PK:** `CODUF`  
**Referenciada por:** 23 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUF` 🔑 | Inteiro | Cod. Unidade Federativa |  |
| `UF` | Texto | Sigla |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODPAIS` | Inteiro | Pais | → `TSIPAI`.`CODPAIS` |
| `CODPARCSECRECEST` | Inteiro | Cod. Parceiro Secretaria da Receita Estadual | → `TGFPAR`.`CODPARC` |
| `CODIBGE` | Inteiro | Codigo IBGE |  |
| `CODSTGNRE` | Texto | Codigo da Receita (GNRE) |  |
| `CODRECDIME` | Inteiro | Codigo da Receita (DIME) |  |
| `CODCLSVENCDIME` | Inteiro | Codigo Classe Vencimento (DIME) |  |
| `CODDETGNRE` | Inteiro | Codigo Detalhamento Receita (GNRE) |  |
| `CODPRODGNRE` | Inteiro | Codigo do Produto (GNRE) |  |
| `VLRPERSGNRE` | Texto | Valor personalizado GNRE |  |
| `PROTOCOLOCONVENIO` | Texto | Protocolo/Convenio (GNRE) |  |
| `CODCAMPOEXTRAGNRE` | Inteiro | Codigo (Campos Extras GNRE) |  |
| `CODCAMPOEXTRAGNRE2` | Inteiro | Codigo (Campos Extras GNRE 2) |  |
| `ESTORNONFE` | Texto | Permite Estorno de NF-e |  |
| `GERINFCAMPADICGNRE` | Texto | Gera Informação dos Campos Adicionais na GNRE |  |
| `VALORCAMPOEXTRA` | Texto | Valor para Campo Extra GNRE |  |
| `VERSAOGNRE` | Texto | Versão GNRE |  |
| `TIPODOC` | Inteiro | Tipo de documento |  |
| `CODFCPSTGNRE` | Inteiro | Codigo da Receita (GNRE) p/ FCP ST |  |
| `CODRECDIMEFCPST` | Inteiro | Codigo da Receita (DIME) para FCP ST |  |
| `CODCLSVENCDIMEFCPST` | Inteiro | Codigo Classe Vencimento (DIME) p/ FCP ST |  |
| `TIPOINFO` | Texto | Tipo da Informação |  |
| `TIPTITGNREFCPST` | Inteiro | Tipo de Titulo p/ indicar GNRE p/ FCP S.T. | → `TGFTIT`.`CODTIPTIT` |
| `USAWEBSERVICEGNRE` | Texto | Utiliza webservice para GNRE |  |
| `TABPRECPMC` | Inteiro | Tabela de Preco PMC |  |
| `TABPRECOPF` | Inteiro | Tabela de Preco PF |  |
| `DHALTREG` | H | Dt. Alteração |  |
| `CODUSUALTREG` | Inteiro | Cod. Usuario Alteração |  |

**Opções `ESTORNONFE`:** `N`=Não, `S`=Sim

**Opções `GERINFCAMPADICGNRE`:** `S`=Sim, `N`=Não

**Opções `TIPOINFO`:** `N`=Nota Fiscal (Numero da nota), `C`=Chave do documento

**Opções `USAWEBSERVICEGNRE`:** `N`=Não, `S`=Sim

**Opções `VALORCAMPOEXTRA`:** `C`=Chave NF-e/CT-e, `O`=Observação, `null`=Chave NF-e/CT-e e Observação

**Opções `VERSAOGNRE`:** `100`=1.0, `200`=2.0

### TSIUSU
**Usuarios**

**PK:** `CODUSU`  
**Referenciada por:** 272 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `GRUPOREDE` | Texto | Grupo de Rede |  |
| `INSTALAPACOTESS` | Texto | Permite instalar pacote Sankhya Store |  |
| `TIMBAIXTITRECABE` | Texto | Baixar tit. reg. lote c/tit. entrada/comissão em aberto |  |
| `CODEQUIP` | Inteiro | Equipamento Fiscal | → `TGFEQF`.`CODEQUIP` |
| `CODUSU` 🔑 | Inteiro | Cod. Usuario |  |
| `USUREDE` | Texto | Usuario de Rede |  |
| `IGNORALDAP` | Texto | Ignorar login via LDAP |  |
| `NOMEUSU` | Texto | Nome |  |
| `ACCOUNTEMAIL` | Texto | Sankhya ID |  |
| `ACESSOPDVCANCITENS` | Texto | Cancelamento de itens |  |
| `ACESSOPDVSANG` | Texto | Sangria |  |
| `DTLIMACESSO` | Data | Data limite de acesso |  |
| `INTERNO` | Texto | Senha |  |
| `ACESSOPDVSUPR` | Texto | Suprimento |  |
| `CODGRUPO` | Inteiro | Grupo | → `TSIGRU`.`CODGRUPO` |
| `DESCTOTALNOTAPDV` | Texto | Desconto no Total |  |
| `ACESSOPDVSANGPDESP` | Texto | Sangria para despesas |  |
| `EMAIL` | Texto | Email |  |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `CODFUNC` | Inteiro | Funcionario |  |
| `CODCENCUSPAD` | Inteiro | Cod.Centro Resultado Padrão | → `TSICUS`.`CODCENCUS` |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `NUVERSAO` | Inteiro | NUVERSAO |  |
| `NOMEFILA` | Texto | Nome Fila p/ num. boleto | → `TSIFIL`.`NOMEFILA` |
| `TOPBAIXARECEITA` | Inteiro | Tipo Operação Baixa Receita |  |
| `TOPBAIXADESPESA` | Inteiro | Tipo Operação Baixa Despesa |  |
| `RENDIASVALJUR` | Inteiro | Dias tol. juros reneg |  |
| `EMAILSOLLIB` | Texto | Email p/ solicitação liberação |  |
| `TIPENVNOTSOL` | Texto | Notificar solicitante de liberações |  |
| `ATUNUVERSAO` | Texto | ATUNUVERSAO |  |
| `NOMEUSUCPLT` | Texto | Nome Completo |  |
| `DTNASC` | Data | Data Nascimento |  |
| `CPF` | Texto | CPF |  |
| `RG` | Texto | RG |  |
| `CODVEND` | Inteiro | Vendedor | → `TGFVEN`.`CODVEND` |
| `CAIXA` | Texto | Caixa |  |
| `TEMECF` | Texto | Tem ECF |  |
| `BAIXAREC` | Texto | Baixa Receita |  |
| `SENHANOVA` | Texto | Senha Nova |  |
| `SENHASMTP` | Texto | Senha SMTP |  |
| `SENHAREPETE` | Texto | Senha Repetir |  |
| `USUARIOSMTP` | Texto | Usuario SMTP |  |
| `SERVIDORSMTP` | Texto | Servidor de SMTP |  |
| `VLRMAXAUT` | Decimal | Valor Maximo de autorização |  |
| `SENHAANTIGA` | Texto | Senha Antiga |  |
| `CONTACESSO` | Texto | Controle |  |
| `DTULTIMASENHA` | H | Data da Ultima senha |  |
| `DTALTER` | H | Data de Alteração |  |
| `NIVEL` | Inteiro | Nivel |  |
| `BAIXADESP` | Texto | Baixa Despesa |  |
| *... +61 campos adicionais* | | | |

**Opções `ABREGAVETA`:** `N`=Não, `S`=Sim

**Opções `ACESSAFORMULAREL`:** `N`=Não, `S`=Sim

**Opções `ACESSOPDVCANCITENS`:** `S`=Sim, `N`=Não

**Opções `ACESSOPDVSANG`:** `S`=Sim, `N`=Não

**Opções `ACESSOPDVSANGPDESP`:** `S`=Sim, `N`=Não

**Opções `ACESSOPDVSUPR`:** `S`=Sim, `N`=Não
