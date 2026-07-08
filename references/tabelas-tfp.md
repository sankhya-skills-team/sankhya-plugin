# Tabelas TFP — Folha de Pagamento e Pessoal

Tabelas `TFP*` — módulo de Recursos Humanos e Folha de Pagamento do Sankhya OM.
Cobrem: funcionários, folha, eventos, afastamentos, férias, ponto, eSocial, CAT,
sindicatos, lotações, cargos, escalas, horários e integração com TCB (contabilidade).

## Entidade Central
```
TFPFUN (Funcionário) ──→ TFPDEP (Departamento)
        │                └──→ TFPLOT (Lotação)
        │                └──→ TFPCAR (Cargo)
        │                └──→ TFPHOR (Horário)
        │
        └──→ TFPFOL (Eventos da Folha) ──→ TFPEVE (Tipos de Eventos)
        └──→ TFPFER (Férias)
        └──→ TFPPON (Ponto)
        └──→ TFPCAT (CAT)
        └──→ TFPASO (Atestado de Saúde)
        └──→ TFPAFA (Afastamentos)
```

## Tabelas Prioritárias

### TFPFUN
**Funcionarios**

**PK:** `CODEMP`, `CODFUNC`  
**Referenciada por:** 160 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CPF` | Texto | CPF |  |
| `DTFIMREMUN` | Data | Data fim remuneração |  |
| `NATATIVIDADEANT` | Texto | NATATIVIDADEANT |  |
| `CODCATEGESOCIALANT` | Inteiro | CODCATEGESOCIALANT |  |
| `CODFUNC` 🔑 | Inteiro | Codigo |  |
| `NOMEFUNC` | Texto | Nome |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `MATRICULA` | Inteiro | Matricula |  |
| `SITUACAO` | Texto | Situação |  |
| `SITUACAOANT` | Texto | Situação Anterior |  |
| `IMAGEM` | Blob | Imagem |  |
| `DEPENDCONVMED` | Inteiro | Quantidade de dependentes de convenio medico |  |
| `SINDICALIZADO` | Texto | Filiado ao Sindicato de Classe |  |
| `DTSENTPROCTRAB` | Data | DTSENTPROCTRAB |  |
| `AFASTFGTSANT` | Texto | AFASTFGTSANT |  |
| `CAUSAAFASTANT` | Inteiro | CAUSAAFASTANT |  |
| `AFASTRAISANT` | Inteiro | AFASTRAISANT |  |
| `MOTDESLIGESOCIALANT` | Texto | MOTDESLIGESOCIALANT |  |
| `MOTDESLIGESOCIAL` | Texto | Motivo de desligamento E-Social |  |
| `NRPROCTRABDESLIG` | Texto | N Processo Trabalhista (desligamento) |  |
| `NRPROCTRABANT` | Texto | N do processo p/ admissão por decisão judicial (Anterior) |  |
| `CODMADDEM` | Inteiro | Motivos de Admissão/Demissão |  |
| `HORASSEMCPU` | Decimal | Qtd Horas Semanais sem redução |  |
| `OBSERVACAOMP` | Texto | Observação MP |  |
| `REPLIDER` | Texto | Substituto de Lider |  |
| `SALBASECPU` | Decimal | Salario Base sem redução |  |
| `DTDEMJUD` | Data | Data demissão (Decisão Judicial) |  |
| `INDADMISSAOANT` | Inteiro | Indicativo de Admissão (Anterior a decisão judicial) |  |
| `IDCONSIG` | Texto | ID Consignado |  |
| `INSCONSIG` | Texto | Matricula consignataria |  |
| `NMSOCIAL` | Texto | Nome Social |  |
| `NRCONTR` | Texto | Contrato Consig.FGTS |  |
| `NUPROCESSOJUD` | Inteiro | Nro. Processo Juridico | → `TFPPSS`.`NUPROCESSO` |
| `NUPROCESSOTRAB` | Inteiro | Nro. Processo Trabalhista | → `TFPPSS`.`NUPROCESSO` |
| `NUREQUISICAO` | Inteiro | Nro. Requisição | → `TRSREQ`.`NUREQUISICAO` |
| `CAGEDADM` | Texto | Gerou CAGED |  |
| `DSCATIVDES` | Texto | Descrição Atividades |  |
| `DTVENCEXP1OR` | Data | DTVENCEXP1OR |  |
| `DTVENCEXP2OR` | Data | DTVENCEXP2OR |  |
| `DEPENDSALFAM` | Inteiro | Quantidade de dependentes de salario familia |  |
| `CODCONVENIO` | Inteiro | Cod. Convenio | → `TFPCON`.`CODCONVENIO` |
| `SALAJUSTADOSIND` | Decimal | Salario ajustado Sindicato |  |
| `SALBASEANTERIOR` | Decimal | Salario Base Anterior |  |
| `DTNASC` | Data | Data de Nascimento |  |
| `PVD` | Texto | Programa de Demissão Voluntaria |  |
| `MATANOTJUD` | Texto | Matricula Anotação Judicial |  |
| `APRENDCONTRIND` | Texto | Contratação Indireta de Aprendiz |  |
| `CODTPRJUD` | Inteiro | Tipo de Rescisão (Decisão Judicial) |  |
| `SEXO` | Texto | Sexo |  |
| `TPINSCAPREND` | Inteiro | Tipo de Inscrição |  |
| `RACAFUNCIONARIO` | Inteiro | Raca/Etnia |  |
| `ORIENTACAOSEXUAL` | Texto | Orientação Sexual |  |
| `POSSUIFILHOS` | Texto | Possui Filhos |  |
| `NRINSCAPREND` | Texto | Numero de Inscrição |  |
| `IDENTIDADEGENERO` | Texto | Identidade de Genero |  |
| `ESTADOCIVIL` | Inteiro | Estado Civil |  |
| `CNPJENTQUAL` | Texto | CNPJ Entidade Qualificadora |  |
| `NIVESC` | Inteiro | Escolaridade |  |
| `CODPAISNAC` | Inteiro | Pais de Nascimento | → `TSIPAI`.`CODPAIS` |
| `CNPJPRAT` | Texto | CNPJ Entidade Pratica |  |
| `NACIONALIDADE` | Inteiro | Nacionalidade |  |
| `APRENDIZGRAVIDA` | Texto | Aprendiz Gravida |  |
| `MESDIA` | Inteiro | Mes e dia nascimento |  |
| `CIDNASC` | Inteiro | Naturalidade |  |
| `CODTOMADOR` | Inteiro | Tomador | → `TGFPAR`.`CODPARC` |
| `TELEFONE` | Texto | Telefone |  |
| `CELULAR` | Texto | Celular |  |
| `DIACADPIS` | Inteiro | Dia de cadastro no PIS |  |
| `EMAIL` | Texto | Email |  |
| `DEFICIENTEFISICO` | Texto | PCD - Pessoa Com Deficiencia |  |
| `TIPDEFICIENCIA` | Inteiro | Tipo de Deficiencia |  |
| `OBSDEFICIENCIA` | Texto | Observações da Deficiencia |  |
| `STEP` | Texto | STEP |  |
| `IDENTIDADE` | Texto | Numero da Identidade |  |
| `ORGAORG` | Texto | Orgão Expedidor |  |
| `DTRG` | Data | Data de Emissão da Identidade |  |
| `UFRG` | Inteiro | UF da Identidade | → `TSIUFS`.`CODUF` |
| `NOMEMAE` | Texto | Nome da Mõe |  |
| `NACIONALPAIS` | Inteiro | Naturalidade da Mõe |  |
| `NOMEPAI` | Texto | Nome do Pai |  |
| *... +259 campos adicionais* | | | |

**Opções `ACESSOPORTALRH`:** `S`=Sim, `N`=Não

**Opções `ADERIMP927`:** `S`=Sim, `N`=Não

**Opções `AJUDACOMP`:** `N`=Não, `S`=Sim

**Opções `APRENDCONTRIND`:** `N`=Não, `S`=Sim

**Opções `APRENDIZGRAVIDA`:** `N`=Não, `S`=Sim

**Opções `BLOQUEIABATIDAONLINE`:** `S`=Sim, `N`=Não

### TFPFOL
**FP Eventos da Folha**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPFOLHA`, `CODEVENTO`, `SEQUENCIA`, `TIPEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `UNIDADE` | Texto | Unidade |  |
| `VLRCALCULO` | Decimal | Valor do calculo |  |
| `NUFIN` | Inteiro | NUFIN | → `TGFFIN`.`NUFIN` |
| `NUOCOR` | Inteiro | NUOCOR |  |
| `REFERENCIAORIG` | Data/Hora | REFERENCIAORIG |  |
| `TIPFOLHAORIG` | Texto | TIPFOLHAORIG |  |
| `SEQUENCIAORIG` | Inteiro | SEQUENCIAORIG |  |
| `CODEVENTOORIG` | Inteiro | CODEVENTOORIG |  |
| `VLRORIGINAL` | Decimal | VLRORIGINAL |  |
| `INDORIGINAL` | Decimal | INDORIGINAL |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `DIGITADO` | Texto | DIGITADO |  |
| `CODUSU` | Inteiro | CODUSU |  |
| `PROTEGIDO` | Texto | PROTEGIDO |  |
| `USADOESOCIAL` | Texto | USADOESOCIAL |  |
| `EHCOMPLEMENTAR` | Texto | E COMPLEMENTAR |  |
| `OBS` | Texto | Observação |  |
| `PRAZO` | Inteiro | Prazo |  |
| `REFERENCIA` 🔑 | Data/Hora | Referencia | → `TFPBAS`.`REFERENCIA` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TIPEVENTO` 🔑 | Inteiro | Tipo de evento |  |
| `TIPFOLHA` 🔑 | Texto | Tipo de folha | → `TFPBAS`.`TIPFOLHA` |
| `VLREVENTO` | Decimal | Valor do evento |  |
| `SEQROE` | Inteiro | SEQROE |  |
| `CODPARCPENS` | Inteiro | ParceiroPensao |  |
| `NROINFODESCFOL` | Inteiro | Informação do emprestimo em folha |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `CODEVENTO` 🔑 | Inteiro | Evento |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPBAS`.`CODFUNC` |
| `INDICE` | Decimal | Indice |  |

**Opções `EHCOMPLEMENTAR`:** `S`=Sim, `N`=Não

**Opções `TIPFOLHA`:** `L`=Resilição, `P`=Pensionista, `N`=Mensal, `D`=Decimo terceiro, `F`=Ferias, `A`=Adiantamento, `R`=Rescisão, `S`=Semanal

### TFPCAB
**Cabecalho do ESocial**


| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` | Inteiro | Empresa |  |
| `DTREF` | Data/Hora | Data de Referencia |  |
| `TPAMB` | Texto | Tipo de Ambiente |  |
| `CONTROLE` | Texto | Controle de Alteração |  |
| `SEQUENCIAATUAL` | Inteiro | Sequencia Atual de Geração |  |
| `EVTPENDENTE` | Inteiro | Eventos Pendentes p/ Sequencia Atual |  |
| `EVTENVIADO` | Inteiro | Eventos Enviados	p/ Sequencia Atual |  |
| `EVTAGUARCORRECAO` | Inteiro | Eventos Aguard. Correção  p/ Sequencia Atual |  |
| `EVTFINALIZADO` | Inteiro | Eventos Finalizados  p/ Sequencia Atual |  |
| `FINALIZADOSUCESSO` | Inteiro | Finalizado com Sucesso |  |
| `EMPROCESSAMENTO` | Inteiro | Em Processamento |  |
| `FINALIZADOERRO` | Inteiro | Finalizado com Erro |  |

### TFPEVE
**Eventos**

**PK:** `CODEVENTO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `INFCOMPLRAIS2` | Decimal | INFCOMPLRAIS2 |  |
| `INSSSEFIP` | Texto | INSSSEFIP |  |
| `INTEGRACTB` | Texto | INTEGRACTB |  |
| `ISS` | Texto | ISS |  |
| `PENSAOSALBRUTO` | Texto | PENSAOSALBRUTO |  |
| `PENSAOSALLIQUIDO` | Texto | PENSAOSALLIQUIDO |  |
| `PENSAOSALMINIMO` | Texto | PENSAOSALMINIMO |  |
| `PLR` | Texto | PLR |  |
| `REFLEXIVOS` | Texto | REFLEXIVOS |  |
| `TIPOINSS` | Inteiro | INSS |  |
| `TIPOIRRF` | Inteiro | IRRF |  |
| `USADOESOCIAL` | Texto | USADOESOCIAL |  |
| `CODEVENTO` 🔑 | Inteiro | Codigo do evento |  |
| `CODEVECORRELATO` | Inteiro | CODEVECORRELATO |  |
| `DSCSALVAR` | Texto | DSCSALVAR |  |
| `PIS` | Texto | PIS |  |
| `CODINCPIS` | Texto | Codigo incidencia pis |  |
| `PISDECTERCEIRO` | Texto | PIS 13 |  |
| `CODEVEFLFER` | Texto | CODEVEFLFER |  |
| `INDENIZACAOAPI` | Texto | Evento de indenização integrante do Aviso Previo Indenizado |  |
| `INTERMITENTE` | Texto | INTERMITENTE |  |
| `BASESEFIP` | Inteiro | Base SEFIP |  |
| `CODEVECOMPLEMENTO` | Inteiro | CODEVECOMPLEMENTO | → `TFPEVE`.`CODEVENTO` |
| `CODNATRUBRICA` | Texto | CODNATRUBRICA |  |
| `COMPLEMENTAR` | Texto | COMPLEMENTAR |  |
| `CONTRIBSIND` | Texto | CONTRIBSIND |  |
| `FGTS` | Texto | FGTS |  |
| `FGTSDECTERCEIRO` | Texto | FGTSDECTERCEIRO |  |
| `FGTSRESCISAO` | Texto | FGTSRESCISAO |  |
| `FGTSSEFIP` | Texto | FGTSSEFIP |  |
| `DESCREVENTO` | Texto | Descrição |  |
| `TIPEVENTO` | Inteiro | Tipo |  |
| `UNIDADE` | Texto | Unidade |  |
| `DTALTER` | Data/Hora | Data de alteracao |  |
| `INCSOBREMEDIAS` | Texto | Incide sobre medias |  |
| `PROTEGIDO` | Texto | Protegido |  |
| `BASEINFREND` | Texto | Base informe rendimentos |  |
| `VLREVENTO` | Decimal | Valor do evento |  |
| `BASEMARGCONSIG` | Texto | Base Margem Consignavel |  |
| `SEQCALCULO` | Decimal | Sequencia para calculo |  |
| `ADIANTAMENTO` | Texto | Adiantamento |  |
| `CODFORM` | Inteiro | Formula |  |
| `ACUMULADOR` | Texto | Acumulador |  |
| `FERIAS` | Texto | E Folha de Ferias |  |
| `BASERAIS` | Texto | Base da rais |  |
| `IMPHOLLERIT` | Texto | Imprime hollerit |  |
| `DECTERC` | Texto | E Folha de Decimo Terceiro |  |
| `TEMCOMPLEMENTO` | Texto | Tem Complementar |  |
| `BASELIQUIDO` | Texto | Base Liquida |  |
| `INDICEADMEDIAS` | Decimal | INDICEADMEDIAS |  |
| `INDICE` | Decimal | Indice |  |
| `FOLHA` | Texto | E Folha Normal |  |
| `RESCISAO` | Texto | E Folha de Rescisão |  |
| `SEMANAL` | Texto | E Folha Semanal |  |
| `REGCALCULO` | Texto | Reg. Calculo |  |
| `DOCUMENTACAO` | Texto | Documentação |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODNAT` | Inteiro | Cod. Natureza | → `TGFNAT`.`CODNAT` |
| `PENSAO` | Texto | Pensão |  |
| `PROVISAOFIN` | Inteiro | Como Participa de Provisão do Financeiro |  |
| `INCORPORA` | Texto | Incorpora |  |
| `COMPLEMENTORESC` | Texto | Complemento Resilição |  |
| `CODEVERESILICAO` | Inteiro | Cod. Eve. Resilição | → `TFPEVE`.`CODEVENTO` |
| `RESILICAO` | Texto | Resilição |  |
| `ATIVO` | Texto | ATIVO |  |
| `SANKHYA` | Texto | SANKHYA |  |
| `IDENTIFICACAO` | Inteiro | IDENTIFICACAO |  |
| `PROVIFERIAS` | Texto | PROVIFERIAS |  |
| `PROVIDECTERSAL` | Texto | PROVIDECTERSAL |  |
| `GRRFMES` | Texto | Mes da Rescisão |  |
| `GRRFMESANTERIOR` | Texto | Mes Anterior a Rescisão |  |
| `GRRFINDENIZACAO` | Texto | Indenizações |  |
| `GRUPOMEDIAS` | Texto | GRUPOMEDIAS |  |
| `CODINCCP` | Texto | CODINCCP |  |
| `CODINCIRRF` | Texto | CODINCIRRF |  |
| `CODINCFGTS` | Texto | CODINCFGTS |  |
| `CODINCSIND` | Texto | CODINCSIND |  |
| `GRUPOEVENTO` | Inteiro | Grupo |  |
| `CHECKSUM` | Texto | Soma de Verificação |  |
| *... +25 campos adicionais* | | | |

**Opções `ACUMULADOR`:** `S`=Sim, `N`=Não

**Opções `ADIANTAMENTO`:** `S`=Sim, `N`=Não

**Opções `AVULSO`:** `N`=Não, `S`=Sim

**Opções `BASEAUXILIAR`:** `S`=Sim, `N`=Não

**Opções `BASELIQUIDO`:** `S`=Sim, `N`=Não

**Opções `BASEMARGCONSIG`:** `F`=Facultativo, `N`=Não incide, `O`=Obrigatorio

### TFPDEP
**Departamentos**

**PK:** `CODDEP`  
**Referenciada por:** 14 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPROJ` | Inteiro | Projeto |  |
| `CODDEP` 🔑 | Inteiro | Departamento |  |
| `DESCRDEP` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `GRAU` | Inteiro | Grau |  |
| `CODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `CODDEPPAI` | Inteiro | Departamento Pai |  |
| `NUMEND` | Texto | Numero |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CODCENCUS` | Inteiro | Centro de Resultado | → `TSICUS`.`CODCENCUS` |
| `CODREGFIS` | Inteiro | Registro fiscal | → `TFPFIS`.`CODREGFIS` |
| `CODPARC` | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `TIPLOTACAO` | Inteiro | Tipo Lotação |  |
| `TPINSCPROP` | Inteiro | Tip. Inscr. Prop |  |
| `NRINSCPROP` | Texto | Codigo |  |
| `NRINSCCONTRAT` | Texto | Codigo |  |
| `DHALTER` | Data/Hora | Data de alteração |  |
| `TPINSCCONTRAT` | Inteiro | Tip. Inscr. Contratante |  |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `TPINSCCONTRAT`:** `2`=CPF, `1`=CNPJ

**Opções `TPINSCPROP`:** `1`=CNPJ, `2`=CPF

### TFPLOT
**Lotações**

**PK:** `CODEMP`, `CODFUNC`, `CODCARGO`, `DTPOSSE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODCARGO` 🔑 | Inteiro | Cod.Cargo | → `TFPCAR`.`CODCARGO` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `DTPOSSE` 🔑 | Data/Hora | Data da Posse |  |
| `DTSAIDA` | Data/Hora | Data de Saida |  |
| `NUOCOR` | Inteiro | Numero da Ocorrencia | → `TFPOCO`.`NUOCOR` |

### TFPCAR
**Cargos**

**PK:** `CODCARGO`  
**Referenciada por:** 11 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCARGO` 🔑 | Inteiro | Cargo |  |
| `DESCRCARGO` | Texto | Descrição |  |
| `ATIVO` | Texto | Ativo |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `POSSUINIVEL` | Texto | Possui nivelamento |  |
| `CODCBO` | Inteiro | CBO | → `TFPCBO`.`CODCBO` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `ORIGATIV` | Inteiro | Origem das Atividades p/ E-Social |  |
| `TEMPOASO` | Inteiro | Tempo Val. ASO |  |
| `CODGRUPOCARGO` | Inteiro | Cod. Grupo Cargo | → `TFPGCA`.`CODGRUPOCARGO` |
| `CONTAGEMTEMPO` | Texto | Contagem Tempo |  |
| `TECNICOCIENTIFICO` | Texto | Tecnico cientifico |  |
| `CODESCALA` | Inteiro | Cod. Escala | → `TGPESC`.`CODESCALA` |
| `SITCARGO` | Inteiro | Situação |  |
| `USADOESOCIAL` | Texto | Compõe E-Social |  |
| `APOSENTAESP` | Texto | Aposentad. Esp. |  |
| `OBS` | Texto | Descrição do Cargo |  |
| `RESPONSABILIDADES` | Texto | Responsabilidades |  |
| `CODCARREIRA` | Inteiro | Cod. Carreira | → `TFPCRR`.`CODCARREIRA` |
| `CODNIVELINI` | Inteiro | Nivel Inicial | → `TFPNIV`.`CODNIVELREF` |
| `CODNIVELFIM` | Inteiro | Nivel Final | → `TFPNIV`.`CODNIVELREF` |
| `DEDICACAOEXC` | Texto | Dedicação Exc. |  |
| `ACUMCARGO` | Inteiro | Acum. Cargo |  |
| `CONTAGEMESP` | Inteiro | Contagem Esp. |  |
| `NRLEI` | Texto | Numero da Lei |  |
| `DTLEI` | Data | Data da Lei |  |

**Opções `APOSENTAESP`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `DEDICACAOEXC`:** `S`=Sim, `N`=Não

**Opções `ORIGATIV`:** `1`=Procedimentos, `0`=Tarefas

**Opções `POSSUINIVEL`:** `S`=Sim, `N`=Não

**Opções `TECNICOCIENTIFICO`:** `1`=Sim, `0`=Não

### TFPHOR
**Carga Horaria**

**PK:** `CODCARGAHOR`, `DIASEM`, `TURNO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DIASEM` 🔑 | Inteiro | Dia da semana - Sequencia |  |
| `TURNO` 🔑 | Inteiro | Turno |  |
| `ENTRADA` | Inteiro | Entrada turno |  |
| `SAIDA` | Inteiro | Saida turno |  |
| `VALENTRADA` | Texto | Valida entrada |  |
| `VALSAIDA` | Texto | Valida saida |  |
| `DESCANSOSEM` | Texto | Descanso semanal |  |
| `CODCARGAHOR` 🔑 | Inteiro | Cod.Carga horaria | → `TFPCGH`.`CODCARGAHOR` |
| `CARGAHORARIA` | Data/Hora | Carga |  |
| `DURJORNADAESOCIAL` | Inteiro | Duração da Jornada para o E-Social |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |

**Opções `DESCANSOSEM`:** `S`=Sim, `N`=Não

**Opções `TURNO`:** `4`=4, `3`=3, `2`=2, `1`=1

**Opções `VALENTRADA`:** `N`=Não, `S`=Sim

**Opções `VALSAIDA`:** `N`=Não, `S`=Sim

### TFPFER
**Tabela de Ferias**

**PK:** `CODEMP`, `CODFUNC`, `DTINIAQUI`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `DTINIAQUI` 🔑 | Data | Data Inicial do Periodo Aquisitivo |  |
| `DTFINAQUI` | Data | Data Final do Periodo Aquisitivo |  |
| `SALDODIAS` | Inteiro | Saldo de Dias de Ferias |  |
| `DTPREVISTA` | Data | Data Prevista das Ferias |  |
| `DTSAIDA` | Data | Data de Saida das Ferias |  |
| `FALTPER` | Inteiro | Faltas no Periodo Aquisitivo |  |
| `ABONOPEC` | Inteiro | Dias de Abono Pecuniario |  |
| `NUMDIASFER` | Inteiro | Quantidade de Dias de Ferias |  |
| `ADIANTA13SAL` | Texto | Adianta 13 Salario |  |
| `ATUALFERGOZ` | Texto | Atualiza Ferias Gozadas |  |
| `ABONOINICIO` | Texto | Dias de Abono no Inicio das Ferias |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `QTDPARCELAS` | Inteiro | Quantidade de Parcelas do Emprestimo |  |
| `NUMDIASLICREM` | Inteiro | Dias de Licenca Remunerada |  |
| `NUMDIASFERCOL` | Inteiro | Dias ferias coletivas |  |
| `NUOCOR` | Inteiro | Numero da Ocorrencia |  |
| `REFERENCIA` | Data | Referencia das Ferias |  |
| `DIGITADO` | Texto | Digitado Manualmente |  |
| `APROVADO` | Texto | Requisição Aprovada |  |
| `QTDDIASSOLFERIAS` | Inteiro | Dias de Ferias Solicitados |  |
| `DTLIMGOZFER` | Data | Data Limite para Gozo de Ferias |  |
| `PERQUITADO` | Texto | Periodo Aquisitivo Quitado |  |
| `CODFERVINC` | Inteiro | Codigo de Vinculação de Dois Calculos |  |
| `NUMDIASFERREAL` | Decimal | Dias de Ferias Real |  |
| `NUMDIASLICREMREAL` | Decimal | Dias de Licenca Remunerada Real |  |

**Opções `ABONOINICIO`:** `N`=Não, `S`=Sim

**Opções `ADIANTA13SAL`:** `S`=Sim, `N`=Não

**Opções `APROVADO`:** `N`=Não, `S`=Sim

**Opções `ATUALFERGOZ`:** `N`=Não, `S`=Sim

**Opções `DIGITADO`:** `N`=Não, `S`=Sim

**Opções `PERQUITADO`:** `N`=Não, `S`=Sim

### TFPPON
**FP Controle de Ponto**

**PK:** `CODEMP`, `CODFUNC`, `DTMOV`, `TURNO`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODHISTOCOR` | Inteiro | Historico de ocorrencias | → `TFPHIS`.`CODHISTOCOR` |
| `DTMOV` 🔑 | Data/Hora | Data do movimento |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `NUMOS` | Inteiro | NUMOS |  |
| `NUMITEM` | Inteiro | NUMITEM |  |
| `ENTRADA` | Inteiro | Entrada |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `FALTA` | Texto | Falta |  |
| `TURNO` 🔑 | Inteiro | Turno |  |
| `SAIDA` | Inteiro | Saida |  |
| `NUOCOR` | Inteiro | Ponto | → `TFPOCO`.`NUOCOR` |

**Opções `FALTA`:** `S`=Sim, `N`=Não

**Opções `TURNO`:** `4`=Madrugada, `1`=Manha, `3`=Noite, `2`=Tarde

### TFPFOL
**FP Eventos da Folha**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPFOLHA`, `CODEVENTO`, `SEQUENCIA`, `TIPEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `UNIDADE` | Texto | Unidade |  |
| `VLRCALCULO` | Decimal | Valor do calculo |  |
| `NUFIN` | Inteiro | NUFIN | → `TGFFIN`.`NUFIN` |
| `NUOCOR` | Inteiro | NUOCOR |  |
| `REFERENCIAORIG` | Data/Hora | REFERENCIAORIG |  |
| `TIPFOLHAORIG` | Texto | TIPFOLHAORIG |  |
| `SEQUENCIAORIG` | Inteiro | SEQUENCIAORIG |  |
| `CODEVENTOORIG` | Inteiro | CODEVENTOORIG |  |
| `VLRORIGINAL` | Decimal | VLRORIGINAL |  |
| `INDORIGINAL` | Decimal | INDORIGINAL |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `DIGITADO` | Texto | DIGITADO |  |
| `CODUSU` | Inteiro | CODUSU |  |
| `PROTEGIDO` | Texto | PROTEGIDO |  |
| `USADOESOCIAL` | Texto | USADOESOCIAL |  |
| `EHCOMPLEMENTAR` | Texto | E COMPLEMENTAR |  |
| `OBS` | Texto | Observação |  |
| `PRAZO` | Inteiro | Prazo |  |
| `REFERENCIA` 🔑 | Data/Hora | Referencia | → `TFPBAS`.`REFERENCIA` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TIPEVENTO` 🔑 | Inteiro | Tipo de evento |  |
| `TIPFOLHA` 🔑 | Texto | Tipo de folha | → `TFPBAS`.`TIPFOLHA` |
| `VLREVENTO` | Decimal | Valor do evento |  |
| `SEQROE` | Inteiro | SEQROE |  |
| `CODPARCPENS` | Inteiro | ParceiroPensao |  |
| `NROINFODESCFOL` | Inteiro | Informação do emprestimo em folha |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `CODEVENTO` 🔑 | Inteiro | Evento |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPBAS`.`CODFUNC` |
| `INDICE` | Decimal | Indice |  |

**Opções `EHCOMPLEMENTAR`:** `S`=Sim, `N`=Não

**Opções `TIPFOLHA`:** `L`=Resilição, `P`=Pensionista, `N`=Mensal, `D`=Decimo terceiro, `F`=Ferias, `A`=Adiantamento, `R`=Rescisão, `S`=Semanal

### TFPCAT
**Categoria**

**PK:** `CODCATEG`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCATEG` 🔑 | Inteiro | Cod.Categoria |  |
| `DESCRCATEG` | Texto | Descricao da categoria |  |

### TFPSIN
**Sindicatos**

**PK:** `CODSIND`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSIND` 🔑 | Inteiro | Codigo do sindicato |  |
| `NOMESIND` | Texto | Nome |  |
| `CODPREF` | Inteiro | Regra de Calculo | → `TFPPRE`.`CODPREF` |
| `CGC` | Texto | CNPJ |  |
| `CODSINDICAL` | Texto | Cod. Sindical |  |
| `CODPARC` | Inteiro | Parceiro | → `TGFPAR`.`CODPARC` |
| `EVENTOCONTASSOC` | Texto | Evento Contrib. Associativa |  |
| `EVENTOCONTSIND` | Texto | Evento Contrib. Sindical |  |
| `EVENTOCONTASSIS` | Texto | Evento Contrib. Assistencial |  |
| `EVENTOCONTCONF` | Texto | Evento Contrib. Confederativa |  |
| `PONTOALTERNATIVO` | Texto | Utiliza Registro Eletronico de Ponto Alternativo |  |
| `REGRAADNOTURNO` | Texto | Regra Ad. Noturno |  |
| `TIPHORANOTURNA` | Texto | Tipo Hor. Noturno |  |
| `DHALTER` | Data/Hora | Data de alteração |  |

**Opções `PONTOALTERNATIVO`:** `N`=Não, `S`=Sim

**Opções `REGRAADNOTURNO`:** `N`=Não, `S`=Sim

**Opções `TIPHORANOTURNA`:** `L`=Rural(Lavoura), `U`=Urbano, `P`=Rural(Pecuaria)

### TFPCON
**TABLE TFPCON**

**PK:** `CODCONVENIO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONVENIO` 🔑 | Inteiro | Codigo |  |
| `CNPJ` | Texto | CNPJ |  |
| `RAZAOSOCIAL` | Texto | Razão Social |  |
| `REGANS` | Inteiro | Reg. Ag. Nac. Saude |  |
| `DESCRCONVENIO` | Texto | Tipo |  |
| `CODEVENTO` | Inteiro | Cod. Evento |  |
| `LISEVENTOS` | Texto | Evento |  |
| `LISEVEREEMBOLSO` | Texto | Eventos Reemb. |  |
| `LISEVEREEMBANTERIOR` | Texto | Eventos Reemb. Anterior |  |

### TFPSAL
**FP Saldos de Provisão**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `CODCTACTB`, `CODCENCUS`, `CODPROJ`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMLOTE` | Inteiro | Numero do Lote |  |
| `TIPPROVISAO` | Texto | Tipo da Provisão |  |
| `CODCENCUS` 🔑 | Inteiro | Centro de Custo |  |
| `CODPROJ` 🔑 | Inteiro | Projeto |  |
| `CODCTACTB` 🔑 | Inteiro | Conta Contabil | → `TCBPLA`.`CODCTACTB` |
| `SALDO` | Decimal | Saldo |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CREDITO` | Decimal | Valor de Credito |  |
| `DEBITO` | Decimal | Valor de Debito |  |
| `REFERENCIA` 🔑 | Data/Hora | Referencia |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |

### TFPAGE
**Agendamento de Folhas de Pgto**

**PK:** `CODEMP`, `CODFUNC`, `REFERENCIA`, `TIPFOLHA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPEMP`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `REFERENCIA` 🔑 | Data/Hora | REFERENCIA |  |
| `TIPFOLHA` 🔑 | Texto | TIPFOLHA |  |
| `PARAMETROS` | Blob | PARAMETROS |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DTAGEND` | Data/Hora | DTAGEND |  |
| `DTPRONTO` | Data/Hora | DTPRONTO |  |
| `CONCLUIDO` | Texto | CONCLUIDO |  |

### TFPAFA
**Codigos de Afastamento**

**PK:** `TIPTAB`, `CODAFAST`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAFAST` 🔑 | Texto | Cod.Afastamento |  |
| `DESCRAFAST` | Texto | Descrição |  |
| `DIRFERMENANO` | Texto | Direito a ferias com menos de um ano |  |
| `CODGOVERNO` | Texto | Codigo Governamental |  |
| `DIRAVISOPREVIO` | Texto | Direito ao aviso previo |  |
| `TIPTAB` 🔑 | Texto | Tipo de tabela |  |
| `ABATEMESMEDIA` | Texto | Abate nos Meses das Medias |  |
| `DTALTER` | Data/Hora | Data da Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DIRDECTERC` | Texto | Direito ao decimo terceiro |  |
| `DIRMULTAFGTS` | Texto | Direito a multa do FGTS |  |
| `CODAFAHOMOLOGNET` | Texto | Codigo HomologNet |  |

**Opções `ABATEMESMEDIA`:** `S`=Sim, `N`=Não

**Opções `CODAFAHOMOLOGNET`:** `RI2`=RI2 Rescisão Indireta, `RA2`=RA2 Rescisão antecipada, pelo empregador, `RA1`=RA1 Rescisão antecipada, pelo empregado, `PD0`=PD0 Extinção normal do contrato de trabalho por prazo determinado, `NC0`=NC0 Rescisão por nulidade do contrato de trabalho, declarada em decisão judicial, `JC2`=JC2 Despedida por justa causa, pelo empregador, `FT1`=FT1 Rescisão por falecimento do empregado, `FM0`=FM0 Rescisão por forca maior, `FE2`=FE2 Rescisão falec. empregador ind. sem continuação, `FE1`=FE1 Rescisão falec. empregador ind. opeção do empregado, `CR0`=CR0 Rescisão por culpa reciproca, `SJ1`=SJ1 Rescisão contratual a pedido do empregado

**Opções `DIRAVISOPREVIO`:** `S`=Sim, `N`=Não

**Opções `DIRDECTERC`:** `N`=Não, `S`=Sim

**Opções `DIRFERMENANO`:** `N`=Não, `S`=Sim

**Opções `DIRMULTAFGTS`:** `S`=Sim, `N`=Não

### TFPASO
**Atestado de Saude Ocupacional**

**PK:** `NUASO`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUASO` 🔑 | Inteiro | NUASO |  |
| `CODEMP` | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `DTASO` | Data/Hora | DTASO |  |
| `DTVENCASO` | Data/Hora | DTVENCASO |  |
| `TIPASO` | Inteiro | TIPASO |  |
| `RESULTADOASO` | Inteiro | RESULTADOASO |  |
| `MEDICOASO` | Texto | MEDICOASO |  |
| `TELMEDICOASO` | Texto | TELMEDICOASO |  |
| `CRMMEDICOASO` | Texto | CRMMEDICOASO |  |
| `UFCRMMEDASO` | Texto | UFCRMMEDASO |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODCNES` | Texto | CODCNES |  |
| `FRMCTTUNIDATEND` | Texto | FRMCTTUNIDATEND |  |
| `EMAILUNIDATEND` | Texto | EMAILUNIDATEND |  |
| `TPEXAME` | Inteiro | TPEXAME |  |
| `CPFMED` | Texto | CPFMED |  |
| `NISMED` | Texto | NISMED |  |
| `INDRECUSA` | Texto | INDRECUSA |  |
| `MEDICOASOMON` | Texto | MEDICOASOMON |  |
| `TELMEDICOASOMON` | Texto | TELMEDICOASOMON |  |
| `CRMMEDICOASOMON` | Texto | CRMMEDICOASOMON |  |
| `UFCRMMEDASOMON` | Texto | UFCRMMEDASOMON |  |
| `CPFMEDMON` | Texto | CPFMEDMON |  |

### TFPAUD
**Auditoria E-Social**

**PK:** `CODEMP`, `DTREF`, `CHAVE`, `CODAVISO`, `CODUSU`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAUDLOG` | Inteiro | CODAUDLOG |  |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPEMP`.`CODEMP` |
| `CODAVISO` 🔑 | Inteiro | CODAVISO | → `TFPAUDAVI`.`CODAVISO` |
| `DTREF` 🔑 | Data | DTREF |  |
| `DHALTER` | Data/Hora | DTALTER |  |
| `CODUSU` 🔑 | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `CODEVENTO` | Texto | CODEVENTO |  |
| `INFOAVISO` | Texto | INFOAVISO |  |
| `INFOPESQ` | Texto | INFOPESQ |  |
| `GRUPO` | Texto | GRUPO |  |

### TFPACU
**Acumulados do Ano**

**PK:** `CODEMP`, `CODFUNC`, `CODEVENTO`, `TIPEVENTO`, `SEQUENCIA`, `ANO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPEMP`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODEVENTO` 🔑 | Inteiro | Cod.Evento |  |
| `TIPEVENTO` 🔑 | Inteiro | Tipo de evento |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `ANO` 🔑 | Inteiro | Ano de Referencia |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `VLRJANEIRO` | Decimal | Janeiro |  |
| `VLRFEVEREIRO` | Decimal | Fevereiro |  |
| `VLRMARCO` | Decimal | Marco |  |
| `VLRABRIL` | Decimal | Abril |  |
| `VLRMAIO` | Decimal | Maio |  |
| `VLRJUNHO` | Decimal | Junho |  |
| `VLRJULHO` | Decimal | Julho |  |
| `VLRAGOSTO` | Decimal | Agosto |  |
| `VLRSETEMBRO` | Decimal | Setembro |  |
| `VLROUTUBRO` | Decimal | Outubro |  |
| `VLRNOVEMBRO` | Decimal | Novembro |  |
| `VLRDEZEMBRO` | Decimal | Dezembro |  |
| `INDJANEIRO` | Decimal | Indice de janeiro |  |
| `INDFEVEREIRO` | Decimal | Indice de fevereiro |  |
| `INDMARCO` | Decimal | Indice de marco |  |
| `INDABRIL` | Decimal | Indice de abril |  |
| `INDMAIO` | Decimal | Indice de maio |  |
| `INDJUNHO` | Decimal | Indice de junho |  |
| `INDJULHO` | Decimal | Indice de julho |  |
| `INDAGOSTO` | Decimal | Indice de agosto |  |
| `INDSETEMBRO` | Decimal | Indice de setembro |  |
| `INDOUTUBRO` | Decimal | Indice de outubro |  |
| `INDNOVEMBRO` | Decimal | Indice de novembro |  |
| `INDDEZEMBRO` | Decimal | Indice de dezembro |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TFPAUT
**Eventos Padrões**

**PK:** `TIPREG`, `CHAVE`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPREG` 🔑 | Texto | Tipo do registro |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `DESCRPAR` | Texto | Descrição |  |
| `CODEVENTO` | Inteiro | Cod.Evento |  |

## Tabelas Complementares

*244 tabelas complementares com campos mapeados no TDDCAM:*

### TFPACA
**Agentes Causadores CAT**

**PK:** `NUCAT`, `CODAGENTECAUSADOR`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCAT` 🔑 | Inteiro | NUCAT |  |
| `CODAGENTECAUSADOR` 🔑 | Texto | Codigo |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPADV
**Advogados e Escritorios**

**PK:** `CODIGO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Inteiro | Codigo |  |
| `TIPOINSCRICAO` | Inteiro | Tipo de inscrição |  |
| `NROINSCRICAO` | Texto | Numero da inscrição |  |
| `DESCRICAO` | Texto | Descrição |  |

### TFPAEVE
**Alteracao Eventos**

**PK:** `CARACTERISTICA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CARACTERISTICA` 🔑 | Texto | Caracteristica |  |
| `CODEVENTO` | Inteiro | Codigo do evento |  |
| `PADRONIZAR` | Texto | Padronizar |  |
| `REVERTER` | Texto | Reverter |  |
| `CODEVENTOANT` | Inteiro | Codigo do evento Anterior |  |
| `TROCACTX` | Texto | TROCACTX |  |

### TFPAFDT
**TABLE TFPAFDT**

**PK:** `CODEMP`, `CODFUNC`, `DTMOV`, `HORA`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `DTMOV` 🔑 | Data/Hora | DTMOV |  |
| `HORA` 🔑 | Inteiro | HORA |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TIPREGISTRO` | Texto | TIPREGISTRO |  |
| `TIPMARCACAO` | Texto | TIPMARCACAO |  |
| `SEQTIPMARCACAO` | Inteiro | SEQTIPMARCACAO |  |
| `NURELOGIO` | Texto | NURELOGIO |  |
| `NUOCOR` | Inteiro | NUOCOR | → `TFPOCO`.`NUOCOR` |
| `CODUSU` | Inteiro | CODUSU |  |
| `DTALTER` | Data/Hora | DTALTER |  |
| `FECHADO` | Texto | FECHADO |  |
| `DIGITADO` | Texto | DIGITADO |  |
| `DTINIJORNADA` | Data/Hora | DTINIJORNADA |  |
| `DTFECHAMENTO` | Data/Hora | DTFECHAMENTO |  |
| `CRCEMP` | Texto | CRCEMP |  |
| `CRCFUNC` | Texto | CRCFUNC |  |
| `GEOLOC` | Texto | GEOLOC |  |

### TFPAFG
**Alteração Função Gratificada**

**PK:** `CODEMP`, `CODFUNC`, `DTPROM`, `TIPREG`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTPROM` 🔑 | Data | Data da promoção |  |
| `CODGRAT` | Inteiro | Gratificação |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPPUB`.`CODFUNC` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPPUB`.`CODEMP` |
| `ATOADMIN` | Texto | Ato Administrativo |  |
| `TIPREG` 🔑 | Texto | Tipo de registro |  |

### TFPAGC
**Agentes Causadores**

**PK:** `CODAGENTECAUSADOR`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAGENTECAUSADOR` 🔑 | Inteiro | Codigo |  |
| `DESCRAGENTECAUSADOR` | Texto | Descrição do agente causador |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPAGNOC
**TABLE TFPAGNOC**

**PK:** `CODAGNOC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAGNOC` 🔑 | Texto | CODAGNOC |  |
| `DSCAGNOC` | Texto | DSCAGNOC |  |
| `ATIVO` | Texto | ATIVO |  |

### TFPAGNOCATR
**TABLE TFPAGNOCATR**

**PK:** `CODAMB`, `CODAGNOC`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TPAVAL` | Inteiro | Tipo de avaliação |  |
| `CODAGNOC` 🔑 | Texto | Cod. Agente Nocivo |  |
| `NRPROCJUD` | Texto | Numero Processo Adm/Judicial |  |
| `INTCONC` | Decimal | Intensidade ou concentração da exposição |  |
| `LIMTOT` | Decimal | Limite de Tolerancia |  |
| `UNMED` | Inteiro | Unidade de medida intensidade ou concentração |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `TECMEDICAO` | Texto | Tecnica Medição da intensidade ou concentração |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `USAEPC` | Inteiro | Utiliza EPC |  |
| `EFICEPC` | Texto | Os EPCs são eficazes na neutralização do risco ao trabalhador |  |
| `USAEPI` | Inteiro | Utiliza EPI |  |
| `CODAMB` 🔑 | Inteiro | CODAMB | → `TFPAMB`.`CODAMB` |

**Opções `EFICEPC`:** `N`=0 - Não, `S`=1 - Sim

**Opções `TPAVAL`:** `1`=1 - Criterio quantitativo, `2`=2 - Criterio qualitativo

**Opções `USAEPC`:** `0`=0 - Não se aplica, `1`=1 - Não implementa, `2`=2 - Implementa

**Opções `USAEPI`:** `0`=0 - Não se aplica, `1`=1 - Não utilizado, `2`=2 - Utilizado

### TFPALTCPF
**TABLE TFPALTCPF**

**PK:** `CODEMPORIG`, `CODFUNCORIG`, `CODEMPDEST`, `CODFUNCDEST`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMPORIG` 🔑 | Inteiro | CODEMPORIG |  |
| `CODFUNCORIG` 🔑 | Inteiro | CODFUNCORIG |  |
| `CODEMPDEST` 🔑 | Inteiro | CODEMPDEST |  |
| `CODFUNCDEST` 🔑 | Inteiro | CODFUNCDEST |  |

### TFPALUNO
**TABLE TFPALUNO**

**PK:** `NROUNICO`, `CODEMP`, `CODFUNC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NROUNICO` 🔑 | Inteiro | NROUNICO | → `TFPTREI`.`NROUNICO` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPAMB
**Ambiente de Trabalho**

**PK:** `CODAMB`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DSCATIVDES` | Texto | Descrição das Atividades desempenhadas |  |
| `CODAMB` 🔑 | Inteiro | Codigo |  |
| `INIVALID` | Data/Hora | INIVALID |  |
| `NMAMB` | Texto | Nome do Ambiente |  |
| `FIMVALID` | Data/Hora | FIMVALID |  |
| `CODEMP` | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `TPINSC` | Inteiro | Tipo |  |
| `LOCALAMB` | Inteiro | Local |  |
| `NRINSCR` | Texto | Numero Inscrição |  |
| `CODPARC` | Inteiro | Parceiro Tomador | → `TGFPAR`.`CODPARC` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `USADOESOCIAL` | Texto | USADOESOCIAL |  |
| `DSCAMB` | Texto | Descrição do Ambiente |  |
| `OBSERVACAO` | Texto | Observação(ões) periculosa(s), insalubre(s) ou especial(is) desempenhada(s) |  |
| `METERG` | Texto | Metodologia utilizada para o levantamento dos riscos ergonomicos |  |

**Opções `LOCALAMB`:** `1`=1 - Estabelecimento do proprio empregador, `2`=2 - Estabelecimento de Terceiros

**Opções `TPINSC`:** `3`=CAEPF, `1`=CNPJ, `4`=CNO

### TFPAMBR
**TABLE TFPAMBR**

**PK:** `CODAMB`, `CPFRESP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAMB` 🔑 | Inteiro | CODAMB | → `TFPAMB`.`CODAMB` |
| `CPFRESP` 🔑 | Texto | CPF Responsavel | → `TFPRRA`.`CPFRESP` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPAMF
**TABLE TFPAMF**

**PK:** `CODAMB`, `CODEMP`, `CODFUNC`, `DTINICONDICAO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAMB` 🔑 | Inteiro | Ambiente de Trabalho | → `TFPAMB`.`CODAMB` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DTINICONDICAO` 🔑 | Data | Data Inicio da Condição |  |
| `DTFIMCONDICAO` | Data | Data Fim da Condição |  |

### TFPANA
**Analises Folha**

**PK:** `CODANA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODANA` 🔑 | Inteiro | CODANA |  |
| `NOMEANALISE` | Texto | NOMEANALISE |  |
| `SCORE` | Inteiro | SCORE |  |
| `SEQUENCIA` | Inteiro | SEQUENCIA |  |
| `SQLCONSULTA` | Blob | SQLCONSULTA |  |
| `DETALHEANALISE` | Texto | DETALHEANALISE |  |
| `CHARTTYPE` | Texto | CHARTTYPE |  |
| `AVISO` | Texto | AVISO |  |

### TFPANX
**Tabela de anexos das requisições**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `REQID` | Inteiro | REQID | → `TFPREQ`.`ID` |
| `ANEXO` | Blob | ANEXO |  |
| `FILETYPE` | Texto | FILETYPE |  |
| `FILENAME` | Texto | FILENAME |  |
| `TIPOORIGEM` | Texto | Origem do documento |  |
| `DOCORIGEM` | Texto | Documento |  |

**Opções `DOCORIGEM`:** `1`=Anexo RG, `2`=Anexo CPF, `3`=Anexo CNH, `4`=Anexo Titulo Eleitor, `5`=Anexo do Comprovante de Residencia, `6`=Anexo da Conta Bancaria, `7`=Anexo do Exame Admissional, `8`=Anexo Oficio Pensão Alimenticia

**Opções `TIPOORIGEM`:** `D`=Dependente, `U`=Usuario

### TFPANXDPD
**Tabela de anexos do dependente**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `IDDPD` | Inteiro | Sequencia do Dependente |  |
| `REQID` | Inteiro | REQID | → `TFPREQ`.`ID` |
| `ANEXO` | Blob | ANEXO |  |
| `FILETYPE` | Texto | FILETYPE |  |
| `FILENAME` | Texto | FILENAME |  |
| `DOCORIGEM` | Texto | Documento |  |

**Opções `DOCORIGEM`:** `1`=Anexo RG, `2`=Anexo CPF, `3`=Anexo CNH

### TFPANXURL
**Tabela de URL de anexos**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `URL` | Texto | URL |  |
| `TENTATIVAS` | Inteiro | Tentativas |  |
| `STATUS` | Inteiro | Status |  |
| `DHALTER` | Data/Hora | Data de Alteração |  |

### TFPATIV
**TABLE TFPATIV**

**PK:** `CODAMB`, `CODATIV`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAMB` 🔑 | Inteiro | CODAMB | → `TFPAMB`.`CODAMB` |
| `CODATIV` 🔑 | Texto | Cod. Atividade |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPATR
**TABLE TFPATR**

**PK:** `CODEMP`, `CODFUNC`, `DTATRASO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `DTATRASO` 🔑 | Data | Data do Atraso |  |
| `MINUTOS` | Inteiro | Atrasos / Saidas Antecipadas (hrs) |  |
| `HORAATRASO` | Data/Hora | Atrasos / Saidas Antecipadas (hrs) |  |
| `ORIGEM` | Texto | Origem |  |
| `DTALTER` | Data/Hora | DTALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `PERDEDSR` | Texto | Perde DSR |  |

**Opções `ORIGEM`:** `P`=Ponto, `M`=Manual

**Opções `PERDEDSR`:** `S`=Sim, `N`=Não

### TFPATV
**TABLE TFPATV**

**PK:** `CODATIV`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODATIV` 🔑 | Texto | CODATIV |  |
| `DESCRATIV` | Texto | DESCRATIV |  |
| `DESCRCOMPLETA` | Texto | DESCRCOMPLETA |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPAUDAVI
**Avisos Auditoria E-Social**

**PK:** `CODAVISO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAVISO` 🔑 | Inteiro | CODAVISO |  |
| `DESCRAVISO` | Texto | DESCRAVISO |  |
| `ATIVO` | Texto | CODAVISO |  |

### TFPAUDLOG
**Log Auditoria E-Social**

**PK:** `CODAUDLOG`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAUDLOG` 🔑 | Inteiro | CODAUDLOG |  |
| `CODEMP` | Inteiro | CODEMP | → `TFPEMP`.`CODEMP` |
| `CODAVISO` | Inteiro | CODAVISO | → `TFPAUDAVI`.`CODAVISO` |
| `DTREF` | Data | DTREF |  |
| `DHAUD` | Data/Hora | DTAUD |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TFPAVI
**Tabela de Aviso Previo**

**PK:** `CODEMP`, `CODFUNC`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODTPR` | Inteiro | Tipo Rescisão | → `TFPTPR`.`CODTPR` |
| `PVD` | Texto | Programa de Demissão Voluntaria |  |
| `TIPAVISO` | Inteiro | Tipo Aviso |  |
| `DTNOTIFICACAO` | Data | Data Notificação Aviso Previo |  |
| `DTAVISO` | Data | Data Inicio Aviso Previo |  |
| `INICIATIVA` | Texto | Iniciativa do Aviso |  |
| `TIPREDUCAO` | Texto | Opção p/ Red. Jornada |  |
| `DIASAVISO` | Inteiro | Dias Aviso |  |
| `DTFIMAVISO` | Data | Fim das Atividades |  |
| `DTHOMOLOGA` | Data | Data Homologação |  |
| `DTQUITACAO` | Data | Quitação Rescisão (Data Prevista) |  |
| `INDCUMPRPARC` | Inteiro | Indicador de cumprimento de Aviso Previo |  |
| `DIASAVITRABIND` | Inteiro | Dias de Aviso a serem indenizados pelo Empregador |  |
| `NRPROCESSO` | Texto | N Processo Trabalhista |  |
| `DTALTER` | Data | Data Alteração |  |
| `OBSERVACAODET` | Texto | Observação |  |
| `FGTSSALDO` | Decimal | Saldo FGTS |  |
| `FGTSMESANTERIOR` | Texto | Calcula mes Anterior |  |
| `INDSITREMUNDESLIG` | Inteiro | Indicativo de situação de remuneração apos desligamento |  |
| `DTFIMREMUN` | Data | Data fim remuneração |  |
| `NUPRT` | Inteiro | Nro. Unico Processo |  |
| `DTCANCEL` | Data | Data |  |
| `CODUSU` | Inteiro | Codigo do Usuario | → `TSIUSU`.`CODUSU` |
| `CODREL` | Inteiro | CODREL | → `TSIIMP`.`CODREL` |
| `MOTIVOCANCEL` | Inteiro | Motivo |  |
| `OBSERVACAOCANC` | Texto | Observação |  |

**Opções `FGTSMESANTERIOR`:** `S`=Sim, `N`=Não

**Opções `INDCUMPRPARC`:** `3`=Outras hipoteses de cumprimento parcial do aviso, `0`=Cumprimento total, `1`=Cumprimento parcial em razão de novo emprego, `2`=Cumprimento parcial por iniciativa da empresa, `4`=Aviso previo indenizado ou não exigivel

**Opções `INDSITREMUNDESLIG`:** `1`=Quarentena, `2`=Desligamento/Termino legal com data anterior a competencias com remunerações informadas no eSocial

**Opções `INICIATIVA`:** `F`=Colaborador, `E`=Empresa

**Opções `MOTIVOCANCEL`:** `1`=Reconsideração Prevista no artigo 489 da CLT, `9`=Outros, `3`=Cumprimento de norma legal, `2`=Determinação Judicial

**Opções `PVD`:** `N`=Não, `S`=Sim

### TFPBAS
**Tabela para Base de calculo da folha**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPFOLHA`  
**Referenciada por:** 8 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NAORECALCULA` | Texto | NAORECALCULA |  |
| `REFERENCIA` 🔑 | Data/Hora | Referencia |  |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `TIPFOLHA` 🔑 | Texto | Tipo de Folha |  |
| `DIASTRAB` | Inteiro | Dias Trabalhados |  |
| `SALBRUTO` | Decimal | Salario Bruto |  |
| `SALLIQ` | Decimal | Salario Liquido |  |
| `SALBASE` | Decimal | Salario base |  |
| `CODBCO` | Inteiro | Cod.Banco | → `TSIBCO`.`CODBCO` |
| `NUMCHEQ` | Inteiro | Numero do cheque |  |
| `STATUS` | Inteiro | Status |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `DIGITADO` | Texto | Define calculo automatico ou digitado |  |
| `DTPAGAMENTO` | Data/Hora | Data Pagamento |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `NUFIN` | Inteiro | Numero Unico Financeiro | → `TGFFIN`.`NUFIN` |
| `RECALCULA` | Texto | Recalcular |  |
| `SEFIP650` | Texto | SEFIP650 |  |
| `PARAMETROS` | C | Parametros |  |
| `NUFINIRRF` | Inteiro | NUFINIRRF | → `TGFFIN`.`NUFIN` |
| `NUFINFGTS` | Inteiro | NUFINFGTS | → `TGFFIN`.`NUFIN` |
| `NUFINGRCSAVA` | Inteiro | NUFINGRCSAVA | → `TGFFIN`.`NUFIN` |
| `NUFINGRCSSIN` | Inteiro | NUFINGRCSSIN | → `TGFFIN`.`NUFIN` |
| `NUFINGRCSAAAL` | Inteiro | NUFINGRCSAAAL | → `TGFFIN`.`NUFIN` |
| `NUFINGRCSCON` | Inteiro | NUFINGRCSCON | → `TGFFIN`.`NUFIN` |
| `NUFINIRRFPLR` | Inteiro | NUFINIRRFPLR | → `TGFFIN`.`NUFIN` |
| `DISSIDIO` | Texto | DISSIDIO |  |
| `BLOQUEIAPORTALRH` | Texto | BLOQUEIAPORTALRH |  |
| `PARCDECTERC` | Inteiro | PARCDECTERC |  |
| `CODCONV` | Inteiro | CODCONV | → `TFPCTI`.`CODCONV` |
| `CODLOG` | Inteiro | CODLOG | → `TFPLOGCALC`.`CODLOG` |
| `BLOQUEIAPORTALPTO` | Texto | BLOQUEIAPORTALPTO |  |
| `INDMV` | Inteiro | INDMV |  |
| `CODSIND` | Inteiro | CODSIND |  |
| `DSC` | Texto | DSC |  |
| `LIBESOCIAL` | Texto | LIBESOCIAL |  |
| `GERARPARESCISAO` | Texto | GERARPARESCISAO |  |
| `RESCISAODEFINITIVA` | Texto | RESCISAODEFINITIVA |  |
| `CODFUNCPRINC` | Inteiro | CODFUNCPRINC |  |
| *... +5 campos adicionais* | | | |

**Opções `STATUS`:** `1`=Fechadas, `6`=Pronto para o fechamento, `5`=Pronto para a integração contabil, `4`=Com avisos, `0`=Pronto para a integração financeira, `7`=Reabertas, `3`=Com erro

### TFPBASTESTE
**TABLE TFPBASTESTE**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPFOLHA`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | REFERENCIA |  |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `TIPFOLHA` 🔑 | Texto | TIPFOLHA |  |
| `DIASTRAB` | Inteiro | DIASTRAB |  |
| `SALBRUTO` | Decimal | SALBRUTO |  |
| `SALLIQ` | Decimal | SALLIQ |  |
| `SALBASE` | Decimal | SALBASE |  |
| `CODBCO` | Inteiro | CODBCO | → `TSIBCO`.`CODBCO` |
| `NUMCHEQ` | Inteiro | NUMCHEQ |  |
| `STATUS` | Inteiro | STATUS |  |
| `DTALTER` | Data/Hora | DTALTER |  |
| `DIGITADO` | Texto | DIGITADO |  |
| `DTPAGAMENTO` | Data/Hora | DTPAGAMENTO |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `NUFIN` | Inteiro | NUFIN |  |
| `NAORECALCULA` | Texto | NAORECALCULA |  |
| `SEFIP650` | Texto | SEFIP650 |  |
| `NUFINIRRF` | Inteiro | NUFINIRRF |  |
| `NUFINFGTS` | Inteiro | NUFINFGTS |  |
| `NUFINGRCSAVA` | Inteiro | NUFINGRCSAVA |  |
| `NUFINGRCSSIN` | Inteiro | NUFINGRCSSIN |  |
| `NUFINGRCSAAAL` | Inteiro | NUFINGRCSAAAL |  |
| `NUFINGRCSCON` | Inteiro | NUFINGRCSCON |  |
| `NUFINIRRFPLR` | Inteiro | NUFINIRRFPLR |  |
| `DISSIDIO` | Texto | DISSIDIO |  |
| `BLOQUEIAPORTALRH` | Texto | BLOQUEIAPORTALRH |  |
| `PARCDECTERC` | Inteiro | PARCDECTERC |  |
| `CODCONV` | Inteiro | CODCONV | → `TFPCTI`.`CODCONV` |
| `CODLOG` | Inteiro | CODLOG | → `TFPLOGCALC`.`CODLOG` |
| `BLOQUEIAPORTALPTO` | Texto | BLOQUEIAPORTALPTO |  |
| `INDMV` | Inteiro | INDMV |  |
| `PARAMETROS` | C | PARAMETROS |  |
| `RECALCULA` | Texto | RECALCULA |  |
| `LOGCALC` | C | LOGCALC |  |
| `CODFUNCPRINC` | Inteiro | CODFUNCPRINC |  |
| `RESCISAODEFINITIVA` | Texto | RESCISAODEFINITIVA |  |
| `GERARPARESCISAO` | Texto | GERARPARESCISAO |  |
| `CODSIND` | Inteiro | CODSIND |  |
| `DSC` | Texto | DSC |  |
| *... +1 campos adicionais* | | | |

### TFPBEN
**Beneficio**

**PK:** `CODBEN`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODBCO` | Inteiro | Banco | → `TSIBCO`.`CODBCO` |
| `CODBEN` 🔑 | Inteiro | Codigo |  |
| `CODCENCUS` | Inteiro | Centro de Resultado | → `TSICUS`.`CODCENCUS` |
| `CODCENCUSDIF` | Inteiro | Centro de Custo Diferenca | → `TSICUS`.`CODCENCUS` |
| `CODCTABCOINT` | Inteiro | Conta | → `TSICTA`.`CODCTABCOINT` |
| `CODEVENTO` | Inteiro | Evento Beneficiario |  |
| `CODEVENTOEMP` | Inteiro | Evento Empresa |  |
| `CODNAT` | Inteiro | Natureza | → `TGFNAT`.`CODNAT` |
| `CODPARCEMP` | Inteiro | Parceiro Empresa |  |
| `CODPROJ` | Inteiro | Projeto | → `TCSPRJ`.`CODPROJ` |
| `CODTIPOPER` | Inteiro | Tipo Operação |  |
| `CODTIPTIT` | Inteiro | Tipo de Titulo | → `TGFTIT`.`CODTIPTIT` |
| `VALIDAAFASTAMENTO` | Texto | Desconta Afastamento |  |
| `FORMULA` | Texto | Formula |  |
| `FORMULAIND` | Texto | Formula de Indice |  |
| `VLRPARTEEMPRESA` | Decimal | Valor Parte Empresa |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODTBE` | Inteiro | Tipo de Beneficio | → `TFPTBE`.`CODTBE` |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `CODPARC` | Inteiro | Fornecedor | → `TGFPAR`.`CODPARC` |
| `DESCHRCARGA` | Texto | Desconsidera dia com carga < 6h |  |
| `TIPOBENEFICIO` | Inteiro | Tipo Beneficio |  |

**Opções `DESCHRCARGA`:** `N`=Não, `S`=Sim

**Opções `VALIDAAFASTAMENTO`:** `N`=Nao, `S`=Sim

### TFPBHM
**Movimento**

**PK:** `CODEMP`, `CODFUNC`, `REFERENCIA`, `SEQUENCIA`, `AUTORIZADO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `REFERENCIA` 🔑 | Data/Hora | Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `HORAS` | Inteiro | Horas |  |
| `MINUTOS` | Inteiro | Minutos |  |
| `CREDDEBBCH` | Inteiro | Credito ou Debito Banco de Horas |  |
| `AUTORIZADO` 🔑 | Texto | AUTORIZADO |  |

### TFPBHS
**FP Tabela de Saldo**

**PK:** `CODEMP`, `CODFUNC`, `REFERENCIA`, `AUTORIZADO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `COMPACRESCIMOMIN` | Inteiro | COMPACRESCIMOMIN |  |
| `BAIXAACRESCMIN` | Inteiro | BAIXAACRESCMIN |  |
| `AUTORIZADO` 🔑 | Texto | AUTORIZADO |  |
| `ACRESCIMOMIN` | Inteiro | ACRESCIMOMIN |  |
| `SALDOINIACRESCMIN` | Inteiro | SALDOINIACRESCMIN |  |
| `PAGAMENTOMIN` | Inteiro | PAGAMENTOMIN |  |
| `FALTASHOR` | Inteiro | FALTASHOR |  |
| `FALTASMIN` | Inteiro | FALTASMIN |  |
| `PAGAMENTOHOR` | Inteiro | PAGAMENTOHOR |  |
| `DTPERIODOINI` | Data | DTPERIODOINI |  |
| `DTPERIODOFIM` | Data | DTPERIODOFIM |  |
| `SALDOINICMESMIN` | Inteiro | Saldo Inicial do Mes Minutos |  |
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `SALDOINICMESHOR` | Inteiro | Saldo Inicial do Mes Horas |  |
| `DEBITOSMIN` | Inteiro | Debitos Minutos |  |
| `DEBITOSHOR` | Inteiro | Debitos Horas |  |
| `CREDITOSMIN` | Inteiro | Creditos Minutos |  |
| `CREDITOSHOR` | Inteiro | Creditos Horas |  |

### TFPCATR
**Comunicação de Acidente de Trabalho**

**PK:** `NUCAT`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTCAT` | Data | Data da CAT |  |
| `TIPCAT` | Inteiro | Tipo de CAT |  |
| `NUCATORIG` | Inteiro | CAT Origem | → `TFPCATR`.`NUCAT` |
| `NUMEROCAT` | Texto | Numero da CAT |  |
| `TIPACIDENTE` | Inteiro | Tipo de Acidente |  |
| `INICIATCAT` | Inteiro | Iniciativa da CAT |  |
| `DTACIDENTE` | Data | Data do Acidente |  |
| `HRACIDENTE` | Inteiro | Hora do Acidente |  |
| `HORASTRAB` | Inteiro | Horas Trabalhadas |  |
| `DTULTDIATRAB` | Data | Ultimo dia Trabalhado |  |
| `HOUVEAFAST` | Texto | Houve Afastamento |  |
| `INDCATOBITO` | Texto | Indica Obito |  |
| `COMUNPOLICIAL` | Texto | Houve Comunicação Policial |  |
| `CODSITGERADORA` | Texto | Situação Geradora do Acidente |  |
| `CODAGENTECAUSADOR` | Texto | Agente Causador |  |
| `DESCLESAO` | Texto | Descrição complementar / natureza da lesão |  |
| `DESCRLOCALCAT` | Texto | Especificação do Local |  |
| `TIPLOCALCAT` | Inteiro | Tipo de Local |  |
| `CEP` | Texto | CEP |  |
| `CODENDLOCALCAT` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NUMENDLOCALCAT` | Texto | Numero |  |
| `CODBAI` | Inteiro | Bairro |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CODCIDLOCALCAT` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `CODPAIS` | Inteiro | Pais |  |
| `CODPOSTAL` | Texto | Codigo Postal |  |
| `DTATENDIMENTO` | Data | Data de Atendimento |  |
| `HRATENDIMENTO` | Inteiro | Hora Atendimento |  |
| `INDINTERNACAO` | Texto | Houve internação |  |
| `DURTRATAMENTO` | Inteiro | Duração do tratamento (em dias) |  |
| `CODNATLESAO` | Texto | Descrição da lesão |  |
| `CODCIDATESTADO` | Texto | CID |  |
| `DESCLESAOCOMP` | Texto | Descrição complementar / natureza da lesão |  |
| `CPFEMITENTE` | Texto | Medico / Dentista |  |
| `NOMEEMITENTE` | Texto | Medico/Dentista |  |
| `NROC` | Texto | Inscrição no Orgão de Classe/Registro do MS(RMS) |  |
| `INDAFASTAMENTO` | Texto | Indicativo de repouso durante o tratamento |  |
| `IDEOC` | Inteiro | Orgão de Classe |  |
| `DIAGPROVAVEL` | Texto | Diagnostico Provavel |  |
| `UFOC` | Texto | UF Orgão de classe |  |
| *... +17 campos adicionais* | | | |

**Opções `COMUNPOLICIAL`:** `S`=Sim, `N`=Não

**Opções `EMITENTE`:** `1`=Empregador, `2`=Sindicato trab. avulso não portuarios, `3`=Medico assistente, `4`=Empregado, `5`=Autoridade publica, `9`=Dependente do empregado, `8`=Entidade sindical competente, `7`=Orgão gestor de mão de obra, `6`=Cooperativa

**Opções `HOUVEAFAST`:** `S`=Sim, `N`=Não

**Opções `IDEOC`:** `1`=1 - Conselho Regional de Medicina - CRM, `2`=2 - Conselho Regional de Odontologia - CRO, `3`=3 - Registro do Ministerio da Saude - RMS

**Opções `INDAFASTAMENTO`:** `S`=Sim, `N`=Não

**Opções `INDCATOBITO`:** `N`=Não, `S`=Sim

### TFPCBE
**Central Beneficio**

**PK:** `CODCBE`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `STATUS` | Texto | Status |  |
| `VLRDIF` | Decimal | Vlr. Diferenca |  |
| `NUMNOTA` | Inteiro | Nro. Nota |  |
| `DTVENC` | Data | Dt. Vencimento |  |
| `CODCBE` 🔑 | Inteiro | Nro. Unico |  |
| `CODBEN` | Inteiro | Beneficio | → `TFPBEN`.`CODBEN` |
| `REFERENCIA` | Data | Referencia |  |
| `VLRNOTA` | Decimal | Vlr. Nota |  |
| `VLRBEN` | Decimal | Vlr. Beneficiarios |  |
| `VLREMP` | Decimal | Vlr. Empresa |  |
| `VLRFECHAMENTO` | Decimal | Vlr. Fechamento |  |
| `DTINI` | Data | Dt. Inicio Referencia |  |
| `DTFIM` | Data | Dt. Fim Referencia |  |
| `VLREXTRABEN` | Decimal | Valor Extra Beneficiario |  |
| `VLREXTRAEMP` | Decimal | Valor Extra Empresa |  |
| `TIPOBENEFICIO` | Inteiro | Tipo Beneficio |  |
| `DTFIMAPUBEN` | Data | Data de fim da Apuração dos Beneficios |  |
| `DTINIAFASTFAL` | Data | Data de inicio da Apuração de Faltas, Atestados e Afastamentos |  |
| `DTFIMAFASTFAL` | Data | Data de fim da Apuração de Faltas, Atestados e Afastamentos |  |
| `DTINIAPUBEN` | Data | Data de inicio da Apuração dos Beneficios |  |
| `DESCRICAO` | Texto | Descrição |  |

**Opções `STATUS`:** `CO`=Concluido, `PE`=Pendente

### TFPCBO
**CBO Codigo Brasileiro de Ocupação**

**PK:** `CODCBO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCBO` 🔑 | Inteiro | Codigo |  |
| `DESCRCBO` | Texto | Descrição |  |
| `TIPHORANOTURNA` | Texto | Tipo do Horario Noturno |  |

**Opções `TIPHORANOTURNA`:** `U`=Urbano, `P`=Rural (Pecuaria), `L`=Rural (Lavoura)

### TFPCERT
**Certificados Digitais**

**PK:** `NROUNICO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ARQUIVO` | Texto | Arquivo |  |
| `CERTIFICADO` | Blob | Certificado |  |
| `CNPJ` | Texto | CNPJ |  |
| `SENHA` | Texto | Senha |  |
| `NOME` | Texto | Nome |  |
| `EMISSOR` | Texto | Emissor |  |
| `CIDADE` | Texto | Cidade |  |
| `ESTADO` | Texto | Estado |  |
| `DTVALINI` | Data | Data Inicial de Validade |  |
| `DTVALFIM` | Data | Data Final de Validade |  |
| `ALIAS` | Texto | Alias |  |
| `APLICACAO` | Texto | Aplicação |  |
| `CODEMP` | Inteiro | Codigo da Empresa |  |
| `NROUNICO` 🔑 | Inteiro | Numero Unico |  |

**Opções `APLICACAO`:** `W`=SankhyaOm, `S`=Sanesocial

### TFPCEV
**Cargos Eventos**

**PK:** `CODEMP`, `CODCARGO`, `CODEVENTO`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPEMP`.`CODEMP` |
| `CODCARGO` 🔑 | Inteiro | Cod.Cargo | → `TFPCAR`.`CODCARGO` |
| `CODEVENTO` 🔑 | Inteiro | Cod.Evento |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `VLRMOV` | Decimal | Valor do Movimento |  |
| `INDICE` | Decimal | Indice |  |
| `UNIDADE` | Texto | Unidade |  |
| `OBS` | Texto | Observações |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TFPCGH
**Identificação da Carga Horaria**

**PK:** `CODCARGAHOR`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCARGAHOR` 🔑 | Inteiro | Cod.Carga Horaria |  |
| `DESCRCARGAHOR` | Texto | Descrição |  |
| `TIPCARGAHOR` | Texto | Tipo Carga Horaria |  |
| `ATIVO` | Texto | Ativa |  |
| `ESCALONAR` | Texto | Escalonar Dias de Trabalho |  |
| `DIASTRAB` | Inteiro | Dias de Trabalho |  |
| `DIASFOLGA` | Inteiro | Dias de Folga |  |
| `QTDTURNO` | Inteiro | Qtde de Turnos |  |
| `USAROCORRENCIA` | Texto | Ocorrencia |  |
| `CONSIDERAFERIADOS` | Texto | Considera Ocorrencias nos Feriados |  |
| `ALTERNAJORNADA` | Texto | Alternar Jornadas |  |
| `ALTERNATIVA` | Inteiro | C.Hor. Alternativa | → `TFPCGH`.`CODCARGAHOR` |
| `NAOCONFORMAFDT` | Texto | Não Conform. Afdt |  |
| `FOLGAPERCDSR` | Texto | Considerar Folga com percentual de DSR/Feriado |  |
| `TIPINTERVALO` | Inteiro | Tipo |  |
| `DURINTERVALO` | Inteiro | Duração em minutos |  |
| `SUMULA444` | Texto | Considera Sumula n444 TST |  |
| `RECESSO` | Texto | Dias de Recesso |  |
| `TPJORNADA` | Inteiro | Tipo de Jornada |  |
| `PERHORFLEXIVEL` | Texto | Permite flexibilidade de horario |  |
| `USAHRNOTURNA` | Texto | Possui Horario Noturno (Total ou Parcial) |  |
| `USAPAUSA` | Texto | Possui pausa nos turnos |  |
| `TOLERANCIANAPAUSA` | Texto | Aplica Tolerancia |  |
| `USAEXTRAPAUSA` | Texto | Aplica Extra |  |
| `USAATRASOPAUSA` | Texto | Aplica Atraso |  |
| `INIINTERV` | Inteiro | Inicio intervalo |  |
| `TERMINTERV` | Inteiro | Temino Intervalo |  |
| `REDHRSNOT` | Texto | Considera redução de horas noturnas para calculo de jornada |  |
| `USADOESOCIAL` | Texto | Compõe E-Social |  |
| `COMPRAVAVTFERIADO` | Texto | Considerar feriado VA e VT |  |
| `TOLERANCIANOINTERV` | Texto | Aplica Tolerancia |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |

**Opções `ALTERNAJORNADA`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `COMPRAVAVTFERIADO`:** `S`=Sim, `N`=Não

**Opções `CONSIDERAFERIADOS`:** `S`=Sim, `N`=Não

**Opções `ESCALONAR`:** `N`=Não, `S`=Sim

**Opções `FOLGAPERCDSR`:** `N`=Não, `S`=Sim

### TFPCHQ
**FP Cheques Cancelados**

**PK:** `CODEMP`, `CODFUNC`, `NUMCHEQ`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODBCO` | Inteiro | Banco | → `TSIBCO`.`CODBCO` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `VLRCHEQ` | Decimal | Valor do cheque |  |
| `NUMCHEQ` 🔑 | Inteiro | Numero do cheque |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |

### TFPCMS
**Confirma Mensagem do Portal RH**

**PK:** `CODCONFMENSAGEM`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONFMENSAGEM` 🔑 | Inteiro | CODCONFMENSAGEM |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `CODMENSAGEM` | Inteiro | CODMENSAGEM |  |

### TFPCMV
**Beneficiario**

**PK:** `CODCMV`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DEPENDENTE` | Texto | Dependente |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODEMP` | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `CODCBE` | Inteiro | Central | → `TFPCBE`.`CODCBE` |
| `VLRBEN` | Decimal | Valor. Beneficario |  |
| `CODCMV` 🔑 | Inteiro | Cod. CMV |  |
| `VLREMP` | Decimal | Valor. Empresa |  |
| `MANUAL` | Texto | Lancamento Manual |  |
| `CODEVENTO` | Inteiro | Evento |  |
| `VLREXTRAEMP` | Decimal | Valor. Extra Empresa |  |
| `VLREXTRABEN` | Decimal | Valor. Extra Beneficiario |  |
| `QTDITE` | Decimal | Quantidade |  |
| `INDBEN` | Decimal | Indice Beneficiario |  |
| `INDEMP` | Decimal | Indice Empresa |  |

**Opções `DEPENDENTE`:** `N`=Não, `S`=Sim

**Opções `MANUAL`:** `N`=Não, `G`=Grupo, `S`=Sim

### TFPCNV
**TABLE TFPCNV**

**PK:** `CODSIND`, `PROCESSO`, `SEQUENCIA`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CARACTERISTICA` | Texto | Caracteristica |  |
| `PROCESSO` 🔑 | Texto | Processo |  |
| `VARA` | Texto | Vara/JCJ |  |
| `TPACCONV` | Texto | Tipo |  |
| `ANO` | Inteiro | Ano |  |
| `DTDATABASE` | Data | Data Base |  |
| `DTASSINATURA` | Data | Data Assinatura |  |
| `PERCCNV` | Decimal | Percentual |  |
| `DTREAJUSTE` | Data | Ref. Reajuste |  |
| `REAJSINDICAL` | Texto | Reaj. Sindical |  |
| `DTREFFAIXA` | Data | Ref. Tab. Faixa |  |
| `CODTABFAIXA` | Inteiro | Cod. Tab. Faixa |  |
| `DTEFACCONV` | Data | Data de Entrada em Vigor |  |
| `USATABMISTA` | Texto | Tab. Perc. e Valor |  |
| `DTCALCDIFERENCASINI` | Data | Considerar diferencas inicial: |  |
| `DTCALCDIFERENCASFIM` | Data | Considerar diferencas final: |  |
| `DTREFSALBASE` | Data | Ref. Salario Base |  |
| `DSC` | Texto | Descrição do Instrumento |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `PERCANTECIPACAO` | Decimal | Perc. Antecipação |  |
| `DTANTECIPACAO` | Data | Data Ref. Antecipação |  |
| `CODHISTANTECIPA` | Inteiro | Cod. Hist. Antecipação | → `TFPHIS`.`CODHISTOCOR` |
| `CODSIND` 🔑 | Inteiro | CODSIND |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `VALORLIMITETETO` | Decimal | Valor limite do teto: |  |
| `VALORAPLICADOTETO` | Decimal | Valor aplicado a partir do limite do teto: |  |
| `TIPOPROCESSORRA` | Inteiro | Tipo de Processo |  |
| `NROPROCESSORRA` | Texto | Numero do Processo para eSocial |  |
| `DESCRICAORRA` | Texto | Descrição dos Rendimentos Recebidos Acumuladamente - RRA |  |
| `VLRDESPESAJUD` | Decimal | Valor das Despesas de Custas Judiciais |  |
| `VLRDESPESAADV` | Decimal | Valor Total das Despesas com Advogado(s) |  |

**Opções `REAJSINDICAL`:** `S`=Sim, `N`=Não

**Opções `TIPOPROCESSORRA`:** `1`=Administrativo, `2`=Judicial

**Opções `TPACCONV`:** `D`=D - Sentenca Normativa - Dissidio, `A`=A - Acordo Coletivo de Trabalho, `C`=C - Convenção coletiva de Trabalho

**Opções `USATABMISTA`:** `S`=Sim, `N`=Não

### TFPCNVADV
**Convenção Coletiva Advogados e Escritorios**

**PK:** `CODSIND`, `PROCESSO`, `SEQUENCIA`, `CODADV`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSIND` 🔑 | Inteiro | Codigo Sindicato | → `TFPCNV`.`CODSIND` |
| `PROCESSO` 🔑 | Texto | Processo | → `TFPCNV`.`PROCESSO` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia | → `TFPCNV`.`SEQUENCIA` |
| `CODADV` 🔑 | Inteiro | Advogado | → `TFPADV`.`CODIGO` |
| `VLRADV` | Decimal | Valor das Despesas com Advogado |  |

### TFPCRE
**Criterio de Rateio**

**PK:** `CODCRIRATEIO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCRIRATEIO` 🔑 | Inteiro | Codigo |  |
| `DESCRRATEIO` | Texto | Descrição |  |

### TFPCRR
**TABLE TFPCRR**

**PK:** `CODCARREIRA`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCARREIRA` 🔑 | Inteiro | Codigo |  |
| `DESCRCARREIRA` | Texto | Descrição da carreira |  |
| `DTALTER` | Data/Hora | DTALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `LEICARR` | Texto | Lei Carreira |  |
| `DTLEICARR` | Data | Dt. Lei Carreira |  |
| `SITCARR` | Texto | Sit. Carreira |  |
| `USADOESOCIAL` | Texto | eSocial |  |

**Opções `USADOESOCIAL`:** `N`=Não, `S`=Sim

### TFPCTA
**FP Contas**

**PK:** `CODCTACTB`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCTACTB` 🔑 | Inteiro | Cod.Conta Contabil | → `TCBPLA`.`CODCTACTB` |

### TFPCTB
**FP Contas Contabeis na Folha**

**PK:** `CODREGFIS`, `SEQUENCIA`, `TIPCONTABIL`, `CODGRUPOCTBZ`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOCTBZ` 🔑 | Inteiro | Cod.Grupo Contabilização |  |
| `CODEVENTO` | Inteiro | Cod.Evento |  |
| `HISTORICOCREDITO` | Inteiro | Historico do credito | → `TCBHIS`.`CODHISTCTB` |
| `CONTACREDITO` | Inteiro | Conta de credito | → `TCBPLA`.`CODCTACTB` |
| `HISTORICODEBITO` | Inteiro | Historico do Debito | → `TCBHIS`.`CODHISTCTB` |
| `CONTADEBITO` | Inteiro | Conta do Debito | → `TCBPLA`.`CODCTACTB` |
| `CODREGFIS` 🔑 | Inteiro | Cod.Registro Fiscal |  |
| `FORMULA` | Texto | Formula |  |
| `TIPCONTABIL` 🔑 | Texto | Tipo de Contabilização |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `FORMULAID` | Inteiro | Formula Contabil | → `TFPCTBFOR`.`FORMID` |

**Opções `TIPCONTABIL`:** `N`=Normal, `D`=Provisão de decimo terceiro, `F`=Provisão de ferias

### TFPCTBFOR
**Formulas Contabeis**

**PK:** `FORMID`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `FORMID` 🔑 | Inteiro | FORMID |  |
| `DESCR` | Texto | DESCR |  |
| `INCORPORACAO` | Texto | INCORPORACAO |  |
| `TERCOFERIAS` | Texto | TERCOFERIAS |  |
| `MULTIPLICADOR` | Inteiro | MULTIPLICADOR |  |
| `PERFGTS` | Texto | PERFGTS |  |
| `PERINSS` | Texto | PERINSS |  |
| `PERINSS13` | Texto | PERINSS13 |  |
| `PERGRPS` | Texto | PERGRPS |  |
| `PERSEGU` | Texto | PERSEGU |  |
| `PERFAP` | Texto | PERFAP |  |
| `PERRAT` | Texto | PERRAT |  |
| `CODUSU` | Inteiro | CODUSU |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `PERPIS` | Texto | PERPIS |  |
| `PERPIS_2` | Texto | PERPIS_2 |  |

### TFPCTG
**TABLE TFPCTG**

**PK:** `CODCATEGESOCIAL`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCATEGESOCIAL` 🔑 | Inteiro | Codigo |  |
| `DESCRCATEGESOCIAL` | Texto | Descrição |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPCTI
**TABLE TFPCTI**

**PK:** `CODCONV`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONV` 🔑 | Inteiro | Codigo |  |
| `DESCRCONV` | Texto | Descrição |  |
| `CODEMP` | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `CODEND` | Inteiro | Endereco |  |
| `NUMEND` | Texto | Numero |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `CODBAI` | Inteiro | Bairro |  |
| `CODCID` | Inteiro | Cidade |  |
| `CEP` | Texto | CEP |  |
| `DTPREVPGTO` | Data/Hora | DTPREVPGTO |  |

### TFPDDE
**Deduções com exigibilidade suspensa**

**PK:** `NUDDE`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDDE` 🔑 | Inteiro | No. unico Dedução |  |
| `NURNE` | Inteiro | No. unico Retenção | → `TFPRNE`.`NURNE` |
| `INDTPDEDUCAO` | Texto | Tipo de dedução |  |
| `VLRDEDSUSP` | Decimal | Valor da dedução |  |
| `CNPJENTIDPC` | Texto | CNPJ Entidade de Previdencia Complementar |  |

**Opções `INDTPDEDUCAO`:** `4`=4 - Fundação de Previdencia Complementar do Servidor Publico - Funpresp, `5`=5 - Pensão alimenticia, `7`=7 - Dependentes, `3`=3 - Fundo de Aposentadoria Programada Individual - FAPI, `2`=2 - Previdencia privada, `1`=1 - Previdencia oficial

### TFPDDES
**Detalhamento das deduções com exigibilidade suspensa**

**PK:** `NUDDES`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDDES` 🔑 | Inteiro | Numero Unico TFPDDES |  |
| `NUIVRDJ` | Inteiro | Numero Unico TFPIVRDJ | → `TFPIVRDJ`.`NUIVRDJ` |
| `INDTPDEDUCAO` | Texto | Indicativo de dedução |  |
| `VLRDEDSUSP` | Decimal | Valor da dedução suspensa |  |

**Opções `INDTPDEDUCAO`:** `7`=7 - Dependente, `1`=1 - Previdencia Oficial, `5`=5 - Pensão alimenticia

### TFPDDESD
**Informação das deduções suspensas por dependentes e beneficiarios da pensão alimenticia**

**PK:** `NUDDESD`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDDESD` 🔑 | Inteiro | Numero Unico TFPDDESD |  |
| `NUDDES` | Inteiro | Numero Unico TFPDDES | → `TFPDDES`.`NUDDES` |
| `CPFDEP` | Texto | CPF do Dependente |  |
| `VLRDEPENSUSP` | Decimal | Valor da dedução ou pensão suspensa |  |
| `NMDEP` | Texto | Nome do Dependente |  |

### TFPDFB
**Dependente Beneficio**

**PK:** `CODEMP`, `CODFUNC`, `CODBEN`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DESCRDEPENDENTE` | Texto | Nome Dependente |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPDPD`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPDPD`.`CODFUNC` |
| `CODBEN` 🔑 | Inteiro | Beneficio | → `TFPFBE`.`CODBEN` |
| `SEQUENCIA` 🔑 | Inteiro | Dependente | → `TFPDPD`.`SEQUENCIA` |

### TFPDIV
**Divisões**

**PK:** `CODDIV`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DESCRDIV` | Texto | Descrição |  |
| `CODDIV` 🔑 | Inteiro | Codigo da divisão |  |

### TFPDOCSIGN
**Assinatura Digital Folha**

**PK:** `ID`, `CODEMP`, `CODFUNC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `ID` 🔑 | Inteiro | ID |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario |  |
| `FILENAME` | Texto | Nome do Arquivo |  |
| `FILETYPE` | Texto | Tipo do Arquivo |  |
| `ANEXO` | Blob | Anexo |  |
| `DHALTER` | Data | Data de Alteracao |  |

### TFPDPD
**Dependentes**

**PK:** `CODEMP`, `CODFUNC`, `SEQUENCIA`  
**Referenciada por:** 12 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `NOMEDEPEND` | Texto | Nome |  |
| `CPF` | Texto | CPF |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `SEXO` | Texto | Sexo |  |
| `DTNASC` | Data | Data de nascimento |  |
| `ADOTIVO` | Texto | Filho Adotivo |  |
| `GRAUPARENTESCO` | Inteiro | Grau de parentesco |  |
| `DESCRDPD` | Texto | Descrição da Dependencia |  |
| `NACIONALIDADE` | Inteiro | Nacionalidade |  |
| `CODCID` | Inteiro | Naturalidade |  |
| `RACAETNIA` | Inteiro | Raca/Etnia |  |
| `DEPENDIRF` | Texto | Dependente de IRRF |  |
| `NOMEMAE` | Texto | Nome da Mõe |  |
| `DEPRPPS` | Texto | Dependente de Fins Previdenciarios |  |
| `CONVENIO` | Texto | Dependente de Convenio Medico |  |
| `AUXCRE` | Texto | Tem Auxilio Creche |  |
| `INCTRAB` | Texto | Possui Incapacidade Fisica ou Mental para o Trabalho |  |
| `CARTORIO` | Texto | Cartorio |  |
| `OBSDEFICIENCIA` | Texto | Observação da Deficiencia |  |
| `PENSIONISTA` | Texto | Pensionista |  |
| `NROFOLHAREG` | Inteiro | Numero da Folha do Livro de Registro |  |
| `NROLIVROREG` | Texto | Numero do Livro de Registro |  |
| `NROREG` | Texto | Numero do Registro |  |
| `DTINICDEPEND` | Data | Data Inicial da Dependencia |  |
| `DTFIMDEPEND` | Data | Data Final da Dependencia |  |
| `SALFAM` | Texto | Dependente de Salario familia |  |
| `DTLIMAUXCRE` | Data | Data Limite do Auxilio Creche |  |
| `DTLIMIRF` | Data | Data limite do IRRF |  |
| `DTLIMSALFAM` | Data | Data Limite do Salario Familia |  |
| `MOTIVOINICIO` | Inteiro | Motivo do Inicio da Dependencia |  |
| `MOTIVOFIM` | Inteiro | Motivo do Fim da Dependencia |  |
| `IDADEESCOLAR` | Texto | Possui Idade Escolar |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `MESDIA` | Inteiro | Mes e dia do nascimento |  |
| `PERCHNETFGTS` | Decimal | Percentual do FGTS |  |
| `VLRPENSAOFGTS` | Decimal | Valor do FGTS |  |
| `SEMATESTADO` | Texto | Não Apresentou Atestado |  |
| `SEMATESTCRECHE` | Texto | Não Apresentou Atestado |  |
| *... +15 campos adicionais* | | | |

**Opções `ADOTIVO`:** `N`=Não, `S`=Sim

**Opções `AUXCRE`:** `S`=Sim, `N`=Não

**Opções `CONVENIO`:** `N`=Não, `S`=Sim

**Opções `DEPENDIRF`:** `S`=Sim, `N`=Não

**Opções `DEPRPPS`:** `N`=Não, `S`=Sim

**Opções `IDADEESCOLAR`:** `S`=Sim, `N`=Não

### TFPDPEN
**Deduções suspensas por dependentes e beneficiarios da pensão alimenticia**

**PK:** `NUDPEN`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDPEN` 🔑 | Inteiro | No unico dependente pensão alimenticia |  |
| `NUDDE` | Inteiro | No. unico Dedução | → `TFPDDE`.`NUDDE` |
| `SEQUENCIA` | Inteiro | Beneficiario |  |
| `VLRDEPENSUSP` | Decimal | Valor da dedução |  |
| `CODEMP` | Inteiro | Codigo da empresa |  |
| `CODFUNC` | Inteiro | Codigo do funcionario |  |

### TFPDPT
**Timeline do DP**

**PK:** `ID`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `TITULO` | Texto | TITULO |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `TIPO` | Texto | TIPO |  |
| `PKS` | Texto | PKS |  |
| `DHCRIACAO` | Data/Hora | DHCRIACAO |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPDRTD
**Dedução do rendimento tributavel relativa a dependentes**

**PK:** `NUDRTD`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDRTD` 🔑 | Inteiro | NUDRTD |  |
| `NUITCR` | Inteiro | NUITCR | → `TFPITCR`.`NUITCR` |
| `NMDEP` | Texto | Dependente |  |
| `TPREND` | Texto | Tipo de rendimento |  |
| `CPFDEP` | Texto | CPF |  |
| `VLRDEDUCAO` | Decimal | Valor da Dedução |  |

**Opções `TPREND`:** `12`=12 - 13 salario, `11`=11 - Remuneração mensal

### TFPEBA
**Bases de Calculo**

**PK:** `CODEVENTOACUM`, `CODEVENTOCOMP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEVENTOACUM` 🔑 | Inteiro | Evento Acumulador |  |
| `DTALTER` | Data/Hora | Data de atleração |  |
| `CODEVENTOCOMP` 🔑 | Inteiro | Evento Componente |  |

### TFPECL
**Eventos de Calculo**


| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCALC` | Inteiro | CODCALC |  |
| `CODEMP` | Inteiro | CODEMP |  |
| `DTREF` | Data/Hora | DTREF |  |
| `TIPOFOL` | Texto | TIPOFOL |  |
| `STATUSFOL` | Texto | STATUSFOL |  |

**Opções `STATUSFOL`:** `P`=Pendente, `A`=Agendada, `C`=Confirmada

**Opções `TIPOFOL`:** `N`=Normal, `L`=Resilição, `F`=Ferias, `D`=Decimo Terceiro, `A`=Adiantamento, `R`=Rescisão, `S`=Semanal, `P`=Pensionista

### TFPEMP
**Empresa Pessoal**

**PK:** `CODEMP`  
**Referenciada por:** 57 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TSIEMP`.`CODEMP` |
| `CODREGFIS` | Inteiro | Reg.Fiscal Apro/Guia | → `TFPFIS`.`CODREGFIS` |
| `TPAMBESOCIAL` | Texto | Ambiente |  |
| `CONTPCD` | Texto | Contratação de PCD |  |
| `USADOESOCIAL` | Texto | Compõe eSocial |  |
| `NUPROCESSOPCD` | Inteiro | Processo Judicial PCD | → `TFPPSS`.`NUPROCESSO` |
| `DEBSUSESOCIAL` | Texto | Possui debitos suspensos no eSocial |  |
| `CODPREF` | Inteiro | Regra de Calculo | → `TFPPRE`.`CODPREF` |
| `CGCANT` | Texto | CNPJ Anterior |  |
| `CONTAPR` | Texto | Contratação de Aprendiz |  |
| `GRUPOESOCIAL` | Texto | Grupo do eSocial |  |
| `SUGEREDATPAG` | Texto | Sugerir data de pagamento |  |
| `DTINICIOESOCIAL` | Data | Implantação Primeira Fase E-Social |  |
| `CONTENTED` | Texto | Contratação por intermedio de Entidade Educativa |  |
| `DTCARGAINICIAL` | Data | Implantação Segunda Fase E-Social |  |
| `TIPDIAPAG` | Texto | Tipo Dia Pagamento |  |
| `DIAPAGMENSAL` | Inteiro | Mensal |  |
| `DTTERCEIRAFASE` | Data | Implantação Terceira Fase E-Social |  |
| `INDENTED` | Texto | Inscrição Entidade Educativa |  |
| `NMENTE` | Texto | Nome da Entidade Educativa |  |
| `DIAPAGSEM` | Inteiro | Semanal |  |
| `DTSESMT` | Data | Data do SESMT |  |
| `IMPORTAPONTO` | Texto | Realiza Importação Automatica |  |
| `DIAPAGQUINZ` | Inteiro | Quinzenal 1 |  |
| `NUPROCESSOAPR` | Inteiro | Processo Judicial Aprendiz | → `TFPPSS`.`NUPROCESSO` |
| `DIAPAGQUINZ_2` | Inteiro | Quinzenal 2 |  |
| `PASTADOPONTO` | Texto | Diretorio de Origem |  |
| `PERIODOIMPPONTO` | Inteiro | Periodicidade |  |
| `CODCTABCOINT` | Inteiro | Conta Bancaria Intercambio | → `TSICTA`.`CODCTABCOINT` |
| `DHULTIMAIMPPTO` | Data | Data Ultima Execução |  |
| `NUMCONVINT` | Inteiro | Numero Convenio para Intercambio |  |
| `CTAFGTS` | Inteiro | Conta do FGTS |  |
| `INDETT` | Texto | Empresa de Trabalho Temporario |  |
| `CATEGFGTS` | Inteiro | Categoria FGTS |  |
| `NRREGETT` | Texto | Numero de registro ETT |  |
| `MODHOLLERIT` | Inteiro | Modelo hollerit |  |
| `MODPONTO` | Inteiro | Modelo ponto |  |
| `REFERENCIA` | Data | Data Referencia |  |
| `CODCENCUS` | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `EMPDESTINOCTB` | Inteiro | Empresa Contabilidade | → `TSIEMP`.`CODEMP` |
| *... +127 campos adicionais* | | | |

**Opções `ALTEROUEND`:** `N`=Não, `S`=Sim

**Opções `APROVADP`:** `S`=Sim, `N`=Não

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `BLOQACESSORH`:** `N`=Não, `S`=Sim

**Opções `BLOQACESSOSNK`:** `S`=Sim, `N`=Não

**Opções `BLOQEXIBANIV`:** `S`=Sim, `N`=Não

### TFPEP
**TABLE TFPEP**

**PK:** `CODEP`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEP` 🔑 | Inteiro | Codigo |  |
| `TPEP` | Inteiro | Tipo de Proteção |  |
| `DSCEP` | Texto | Descrição do Equipamento |  |
| `EFICEP` | Texto | E eficaz na neutralização dos riscos ao trabalhador |  |
| `CAEPI` | Texto | Certificado de Aprovação do EPI |  |
| `MEDPROTECAO` | Texto | Foram implementadas medidas coletiva, optando-se pelo EPI por inviabilidade tecnica, insuficiencia ou interinidade |  |
| `CONDFUNCTO` | Texto | Observadas condições de funcionamento e uso ininterrupto do EPI, ajustada as condições do tempo |  |
| `PRZVALID` | Texto | Observado prazo de validade, conforme CA do MTE |  |
| `PERIODICTROCA` | Texto | Observada a periodicidade de troca, comprovada mediante recibo assinado pelo usuario em epoca propria |  |
| `HIGIENIZACAO` | Texto | Observada a higienização |  |
| `MANUTENCAO` | Texto | Observada a manutenção |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

**Opções `CONDFUNCTO`:** `S`=Sim, `N`=Não

**Opções `EFICEP`:** `S`=Sim, `N`=Não

**Opções `HIGIENIZACAO`:** `S`=Sim, `N`=Não

**Opções `MANUTENCAO`:** `S`=Sim, `N`=Não

**Opções `MEDPROTECAO`:** `S`=Sim, `N`=Não

**Opções `PERIODICTROCA`:** `S`=Sim, `N`=Não

### TFPEPI
**TABLE TFPEPI**

**PK:** `CODAMB`, `CODFATRISCO`, `CAEPI`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFATRISCO` 🔑 | Texto | CODFATRISCO | → `TFPFATR`.`CODFATRISCO` |
| `CAEPI` 🔑 | Texto | Certificado de aprovação |  |
| `EFICACIAEPI` | Texto | E eficaz na neutralização do risco ao trabalhador |  |
| `CODEP` | Inteiro | Codigo Equipamento | → `TFPEP`.`CODEP` |
| `MEDPROTECAO` | Texto | Foram implementadas medidas coletiva, optando-se pelo EPI por inviabilidade tecnica, insuficiencia ou interinidade |  |
| `CONDFUNCTO` | Texto | Observadas condições de funcionamento ao longo do tempo |  |
| `PRZVALID` | Texto | Observado prazo de validade, conforme CA do MTE |  |
| `PERIODICTROCA` | Texto | Observada a periodicidade de troca, comprovada mediante recibo assinado pelo usuario em epoca propria |  |
| `HIGIENIZACAO` | Texto | Observada a higienização |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `CODAMB` 🔑 | Inteiro | CODAMB | → `TFPFATR`.`CODAMB` |
| `MANUTENCAO` | Texto | Manutenção |  |
| `USOININT` | Texto | Observado uso ininterrupto ao longo do tempo |  |

**Opções `CONDFUNCTO`:** `S`=Sim, `N`=Não

**Opções `EFICACIAEPI`:** `S`=Sim, `N`=Não

**Opções `HIGIENIZACAO`:** `S`=Sim, `N`=Não

**Opções `MANUTENCAO`:** `S`=Sim, `N`=Não

**Opções `MEDPROTECAO`:** `S`=Sim, `N`=Não

**Opções `PERIODICTROCA`:** `S`=Sim, `N`=Não

### TFPEPIAGNOC
**TABLE TFPEPIAGNOC**

**PK:** `CODAMB`, `CODAGNOC`, `CAEPI`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODAGNOC` 🔑 | Texto | CODAGNOC | → `TFPAGNOCATR`.`CODAGNOC` |
| `CODEP` | Inteiro | Codigo Equipamento | → `TFPEP`.`CODEP` |
| `CAEPI` 🔑 | Texto | Certificado de aprovação |  |
| `EFICACIAEPI` | Texto | E eficaz na neutralização do risco ao trabalhador |  |
| `MEDPROTECAO` | Texto | Foram implementadas medidas coletiva, optando-se pelo EPI por inviabilidade tecnica, insuficiencia ou interinidade |  |
| `CONDFUNCTO` | Texto | Observadas condições de funcionamento ao longo do tempo |  |
| `PRZVALID` | Texto | Observado prazo de validade, conforme CA do MTE |  |
| `PERIODICTROCA` | Texto | Observada a periodicidade de troca, comprovada mediante recibo assinado pelo usuario em epoca propria |  |
| `HIGIENIZACAO` | Texto | Observada a higienização |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `CODAMB` 🔑 | Inteiro | CODAMB | → `TFPAGNOCATR`.`CODAMB` |
| `MANUTENCAO` | Texto | Manutenção |  |
| `USOININT` | Texto | Observado uso ininterrupto ao longo do tempo |  |

**Opções `CONDFUNCTO`:** `S`=Sim, `N`=Não

**Opções `EFICACIAEPI`:** `N`=Não, `S`=Sim

**Opções `HIGIENIZACAO`:** `S`=Sim, `N`=Não

**Opções `MANUTENCAO`:** `N`=Não, `S`=Sim

**Opções `MEDPROTECAO`:** `N`=Não, `S`=Sim

**Opções `PERIODICTROCA`:** `S`=Sim, `N`=Não

### TFPEPR
**TABLE TFPEPR**

**PK:** `NUPROCESSO`, `CODEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPROCESSO` 🔑 | Inteiro | NUPROCESSO | → `TFPPSS`.`NUPROCESSO` |
| `CODEVENTO` 🔑 | Inteiro | Evento |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPEQP
**TABLE TFPEQP**

**PK:** `CODEQP`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEQP` 🔑 | Inteiro | Codigo |  |
| `CODEMP` | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `DESCREQP` | Texto | Descrição |  |
| `MARCA` | Inteiro | Marca/Modelo |  |
| `IP` | Texto | Endereco IP / DDNS |  |
| `PORTA` | Inteiro | Porta TCP |  |
| `ATIVO` | Texto | Ativo |  |
| `SERIAL` | Texto | Nro Fabricação |  |
| `NSR` | Inteiro | NSR Prox. Coleta |  |
| `AUTH` | Texto | Requer autenticação |  |
| `USUARIO` | Texto | Usuario |  |
| `SENHA` | Texto | Senha |  |
| `HRVERAO` | Texto | HRVERAO |  |
| `DTINICHRVERAO` | Data/Hora | DTINICHRVERAO |  |
| `DTFINALHRVERAO` | Data/Hora | DTFINALHRVERAO |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DATAINI` | Data/Hora | DATAINI |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `AUTH`:** `S`=Sim, `N`=Não

**Opções `MARCA`:** `1`=Henry - Hexa / Hexa Adv. / Prisma SF / Prisma SF Adv. / Compacto S, `2`=Control ID - iDClass REP, `3`=Orion 6 - Henry

### TFPEST
**Dados estagiarios**

**PK:** `CODEMP`, `CODFUNC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod. Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod. Funcionario | → `TFPFUN`.`CODFUNC` |
| `NIVESTAGIO` | Texto | Nivel do Estagio |  |
| `NATESTAGIO` | Texto | Natureza de Estagio |  |
| `DTPREVTERM` | Data | Data Prevista de Termino |  |
| `AREAATUACAO` | Texto | Area de Atuação |  |
| `NRAPOL` | Texto | Numero da Apolice |  |
| `VLRBOLSA` | Decimal | Valor da Bolsa |  |
| `DHALTER` | Data/Hora | Data de Alteração |  |
| `NMRAZAOINSTENS` | Texto | Razão Social da Instituição de Ensino |  |
| `CNPJINSTENSINO` | Texto | CNPJ da Instituição de Ensino |  |
| `CEPINSTENS` | Texto | CEP |  |
| `CODENDINSTENS` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NRLOGRADINSTENS` | Texto | Numero |  |
| `CODBAIINSTENS` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CODCIDINSTENS` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `NMRAZAOAGTINTEG` | Texto | Razão Social do Agente de Integração |  |
| `CNPJAGTINTEG` | Texto | CNPJ do Agente de Integração |  |
| `CEPAGTINTEG` | Texto | CEP |  |
| `CODENDAGTINTEG` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NRLOGRADAGTINTEG` | Texto | Numero |  |
| `CODBAIAGTINTEG` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `CODCIDAGTINTEG` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `NMSUPERVISOR` | Texto | Nome do Supervisor |  |
| `CPFSUPERVISOR` | Texto | CPF do Supervisor |  |

**Opções `NATESTAGIO`:** `O`=Obrigatorio, `N`=Não Obrigatorio

**Opções `NIVESTAGIO`:** `3`=Formação Profissional, `2`=Medio, `4`=Superior, `1`=Fundamental

### TFPEXA
**Exames Periodicos**

**PK:** `NUASO`, `SEQEXAME`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUASO` 🔑 | Inteiro | Numero ASO | → `TFPASO`.`NUASO` |
| `SEQEXAME` 🔑 | Inteiro | Sequencia do Exame |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODFUNC` | Inteiro | Funcionario |  |
| `DESCREXAME` | Texto | Descrição Exame |  |
| `DTEXAME` | Data | Data do exame |  |
| `CNPJLAB` | Texto | CNPJ do laboratorio |  |
| `CODUSU` | Inteiro | Codigo Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | Data de Alteração |  |
| `CODEXAME` | Texto | Cod. do exame |  |
| `NMMED` | Texto | Nome do medico |  |
| `DTVENCIMENTO` | Data/Hora | Data Vencimento |  |
| `CRM` | Texto | Numero do CRM |  |
| `UFCRM` | Texto | UF do CRM |  |
| `TOXICOLOGICO` | Texto | Toxicologico |  |
| `CNPJBASE36` | Texto | Prefixo Cod. Exame |  |
| `SERIALSEQ` | Texto | Serial da Sequencia |  |
| `CODEXAMEESOCIAL` | Inteiro | Cod. Exame e-Social |  |
| `ORDEXAME` | Inteiro | Ordem do Exame |  |
| `INDRESULT` | Inteiro | Resultado Indiciativo |  |
| `DIASVENC` | Inteiro | Dia do Vencimento |  |
| `RECIBOESOCIAL` | Texto | Nro. Recibo eSocial |  |
| `DESCREXAMEESOCIAL` | Texto | Descrição Exame e-Social |  |

### TFPFAI
**FP Tabela de Faixas**

**PK:** `CODTAB`, `REFERENCIA`, `LIMFAIXA`, `TIPOTAB`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTAB` 🔑 | Inteiro | Codigo da Tabela |  |
| `DESCRTAB` | Texto | Descrição da Tabela |  |
| `TIPOTAB` 🔑 | Texto | Tipo da tabela |  |
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `LIMFAIXA` 🔑 | Decimal | Limite da faixa |  |
| `VALOR1` | Decimal | Valor 1 |  |
| `VALOR2` | Decimal | Valor 2 |  |
| `VALOR3` | Decimal | Valor 3 |  |
| `VALOR4` | Decimal | Valor 4 |  |
| `VALOR5` | Decimal | Valor 5 |  |
| `VALOR6` | Decimal | Valor 6 |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `VALOR7` | Decimal | Valor 7 |  |
| `VALOR8` | Decimal | Valor 8 |  |
| `VALOR9` | Decimal | Valor 9 |  |
| `VALOR10` | Decimal | Valor 10 |  |
| `VALOR11` | Decimal | Valor 11 |  |

### TFPFAL
**Faltas**

**PK:** `CODEMP`, `CODFUNC`, `DTFALTA`, `TIPREG`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario |  |
| `DTFALTA` 🔑 | Data/Hora | Data da Falta |  |
| `TIPREG` 🔑 | Inteiro | Tipo de Registro |  |
| `NUFALTA` | Inteiro | Nro Lancamento |  |
| `CODHIS` | Inteiro | Codigo do Historico |  |
| `DTALTER` | Data/Hora | Data da Alteração |  |
| `DESCRHISTOCOR` | Texto | Descrição do Historico |  |
| `CODUSU` | Inteiro | Codigo Usuario |  |
| `ORIGEM` | Texto | Origem |  |
| `PERDEDSR` | Texto | Perde DSR |  |
| `SUSPDISCIPLINAR` | Texto | Suspensão Disciplinar |  |
| `HORAS` | Decimal | Quantidade de Horas |  |

**Opções `PERDEDSR`:** `S`=Marcado, `N`=Desmarcado

**Opções `SUSPDISCIPLINAR`:** `S`=Marcado, `N`=Desmarcado

**Opções `TIPREG`:** `1`=Restituição, `-1`=Falta

### TFPFATR
**TABLE TFPFATR**

**PK:** `CODAMB`, `CODFATRISCO`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFATRISCO` 🔑 | Texto | Cod. Fator de Risco |  |
| `TECMEDICAO` | Texto | Tecnica Medição da intensidade ou concentração |  |
| `UTILIZAEPI` | Inteiro | Utilização de EPI |  |
| `UTILIZAEPC` | Inteiro | Utilização de EPC |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `TIPOFATOR` | Inteiro | TIPOFATOR |  |
| `CODAMB` 🔑 | Inteiro | CODAMB | → `TFPAMB`.`CODAMB` |
| `TPAVAL` | Inteiro | Tipo de avaliação |  |
| `UNMED` | Inteiro | Unidade de medida intensidade ou concentração |  |
| `INSALUBRIDADE` | Texto | Insalubridade |  |
| `PERICULOSIDADE` | Texto | Periculosidade |  |
| `HIERUSO` | Texto | Usa Hierarquia |  |
| `APOSENTESP` | Texto | Aposentadoria Especial |  |
| `LIMTOT` | Decimal | Limite de Tolerancia |  |
| `EFICEPC` | Texto | Os EPCs são eficazes na neutralização dos riscos |  |
| `INTCONC` | Decimal | Intensidade ou concentração da exposição |  |
| `DSCFATRISC` | Texto | Descrição complementar do Fator de Risco |  |

**Opções `APOSENTESP`:** `S`=Sim, `N`=Não

**Opções `EFICEPC`:** `S`=Sim, `N`=Não

**Opções `HIERUSO`:** `S`=Sim, `N`=Não

**Opções `INSALUBRIDADE`:** `S`=Sim, `N`=Não

**Opções `PERICULOSIDADE`:** `N`=Não, `S`=Sim

**Opções `TPAVAL`:** `1`=1 - Criterio quantitativo, `2`=2 - Criterio qualitativo

### TFPFBE
**Funcionario Beneficio**

**PK:** `CODEMP`, `CODFUNC`, `CODBEN`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODBEN` 🔑 | Inteiro | Codigo Beneficio | → `TFPBEN`.`CODBEN` |
| `NOMEFUNC` | Texto | Nome Funcionario |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |

### TFPFCA
**Tabela de Funções para Cargos**

**PK:** `CODCARGO`, `CODFUNCAO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCARGO` 🔑 | Inteiro | Cargo | → `TFPCAR`.`CODCARGO` |
| `CODFUNCAO` 🔑 | Inteiro | Função | → `TFPFCO`.`CODFUNCAO` |

### TFPFCO
**Funções**

**PK:** `CODFUNCAO`  
**Referenciada por:** 11 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFUNCAO` 🔑 | Inteiro | Codigo da função |  |
| `DESCRFUNCAO` | Texto | Descrição |  |
| `CODCBO` | Inteiro | CBO | → `TFPCBO`.`CODCBO` |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `PODESUPEMP` | Texto | Pode ser supervisor de turma |  |
| `PODEENCEMP` | Texto | Pode ser encarregado de turma |  |
| `INCAPONT` | Texto | Incluir no apontamento |  |

**Opções `INCAPONT`:** `S`=Sim, `N`=Não

**Opções `PODEENCEMP`:** `S`=Sim, `N`=Não

**Opções `PODESUPEMP`:** `N`=Não, `S`=Sim

### TFPFCR
**Função e Curso**

**PK:** `CODFUNCAO`, `CODCUR`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `PERCREVISAO` | Inteiro | Percentual de Revisão |  |
| `CODFUNCAO` 🔑 | Inteiro | Função e Curso | → `TFPFCO`.`CODFUNCAO` |
| `PERCAPROV` | Inteiro | Percentual de Aproveitamento |  |
| `CODCUR` 🔑 | Texto | Codigo Curso | → `TCACUR`.`CODCUR` |

### TFPFCTI
**TABLE TFPFCTI**

**PK:** `CODCONV`, `CODEMP`, `CODFUNC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONV` 🔑 | Inteiro | CODCONV | → `TFPCTI`.`CODCONV` |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Codigo Funcionario | → `TFPFUN`.`CODFUNC` |
| `DTINICIO` | Data | Inicio |  |
| `DTFIM` | Data | Fim |  |
| `COMPARECEU` | Texto | Compareceu ao trabalho |  |
| `TIPLOCALTRAB` | Texto | Local de prestação do trabalho |  |
| `DTPREVPGTO` | Data | Previsão de Pagamento |  |

**Opções `COMPARECEU`:** `S`=Sim, `N`=Não

### TFPFDEF
**Dados das deficiencias dos funcionarios**

**PK:** `CODEMP`, `CODFUNC`, `TIPODEFICIENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Codigo Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Codigo Funcionario | → `TFPFUN`.`CODFUNC` |
| `TIPODEFICIENCIA` 🔑 | Inteiro | Deficiencia |  |

**Opções `TIPODEFICIENCIA`:** `1`=Fisica, `2`=Visual, `6`=Reabilitado, `4`=Mental, `5`=Intelectual, `3`=Auditiva

### TFPFGHT
**Fila para geração do historico de alterações do trabalhador**


| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DHINC` | Data/Hora | Data e hora de inclusão |  |
| `NOMETAB` | Texto | Nome da tabela de origem da alteração |  |
| `CHAVE` | C | Chave do registro que gerou a alteração |  |
| `DTESOCIAL` | Data | Data da alteração |  |
| `TIPO` | Texto | Tipo do gatilho que incluiu o item na fila |  |
| `EVENTO` | Texto | Evento afetado pela alteração |  |
| `CAMPOS` | C | Lista de campos alterados |  |
| `SITUACAO` | Texto | Situação |  |

**Opções `SITUACAO`:** `P`=Pendente, `E`=Erro

**Opções `TIPO`:** `E`=Exclusão, `I`=Inclusão, `A`=Alteração

### TFPFHO
**Tabela de carga horaria historica**

**PK:** `CODEMP`, `CODFUNC`, `DHALTER`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCARGAHOR` | Inteiro | Carga Horaria |  |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa |  |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario |  |
| `DHALTER` 🔑 | Data/Hora | Data |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTINIESCALA` | Data | Data de Inicio |  |
| `DTFOLGA` | Data | Data da Folga |  |
| `TIPCONTROLE` | Texto | Tipo controle |  |

**Opções `TIPCONTROLE`:** `E`=Escala, `C`=Carga horaria

### TFPFIN
**Cadastro de Integração com Financeiro**

**PK:** `CODTFPFIN`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DHALTER` | Data | data top | → `TGFTOP`.`DHALTER` |
| `CODTIPTIT` | Inteiro | tipo titulo | → `TGFTIT`.`CODTIPTIT` |
| `TIPOMARCCH` | Texto | tipo marc. |  |
| `HISTORICO` | Texto | hitorico |  |
| `CODTIPOPER` | Inteiro | cod top. | → `TGFTOP`.`CODTIPOPER` |
| `CODTFPFIN` 🔑 | Inteiro | cod. tfpfin |  |
| `CODPROJ` | Inteiro | codigo projeto | → `TCSPRJ`.`CODPROJ` |
| `CODPARC` | Inteiro | cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `CODNAT` | Inteiro | codigo natureza | → `TGFNAT`.`CODNAT` |
| `CODCTABCOINT` | Inteiro | conta banco | → `TSICTA`.`CODCTABCOINT` |
| `CODCENCUS` | Inteiro | Cod. Centro Resultado | → `TSICUS`.`CODCENCUS` |

### TFPFIS
**Registro fiscal**

**PK:** `CODREGFIS`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODREGFIS` 🔑 | Inteiro | Cod.Registro |  |
| `DESCRICAO` | Texto | Descrição |  |
| `CODCID` | Inteiro | Cidade |  |
| `CGCOUCEI` | Texto | Tipo CNPJ/CEI |  |
| `CGC_CEI` | Texto | CNPJ/CEI |  |
| `OBRAPROPRIA` | Texto | Obra Propria |  |
| `AD_CEI` | Texto | AD_CEI |  |
| `ATIVIBGE` | Inteiro | CNAE/IBGE |  |
| `ATIVIRF` | Inteiro | IRF |  |
| `CNPJRESP` | Texto | CNPJ Responsavel |  |
| `ATIVINSS` | Inteiro | Cod. FPAS |  |
| `CODGRPS` | Inteiro | INSS Terceiros |  |
| `CODSAT` | Inteiro | SAT |  |
| `CODPAGGPS` | Inteiro | GPS |  |
| `RAT15` | Decimal | 15 Anos |  |
| `RAT20` | Decimal | 20 Anos |  |
| `RAT25` | Decimal | 25 Anos |  |
| `OPTSIMPLES` | Inteiro | Codigo das opções pelo Simples |  |
| `INDCONTSIMPLES` | Inteiro | Indicador de contribuição Simples Nacional |  |
| `INDSUBSTPATR` | Inteiro | Indicativo de substituição da Contribuição Previd. Patronal |  |
| `TPCAEPF` | Texto | Tipo de CAEPF |  |
| `TAXAGRPS` | Decimal | Taxa Terceiros - INSS |  |
| `PERCINSS` | Decimal | Percentual de INSS |  |
| `TAXASEG` | Decimal | Taxa de seguro |  |
| `PERPAGTOFGTS` | Decimal | Percentual FGTS |  |
| `PERFGTSMENOR` | Decimal | Percentual do FGTS para Menor Aprendiz |  |
| `PERCISEFIL` | Decimal | Percentual Isenção Filantropia |  |
| `FATORFAP` | Decimal | Fator Acidentario de Prevenção (FAP) |  |
| `ISSAUTONOMO` | Inteiro | ISS Autonomo-Responsavel pela retenção |  |
| `PERCRECBRUTAINSS` | Decimal | Percentual da  Receita Bruta para INSS |  |
| `VLRINSSRECBRUTA` | Decimal | Valor do INSS da Receita Bruta |  |
| `FATORMES` | Decimal | Fator Mes |  |
| `PERCRECBRUTAINSS13` | Decimal | Percentual da Receita Bruta para INSS |  |
| `PERCINSSPATRONAL` | Decimal | Percentual de INSS |  |
| `DTALTER` | Data | Referencia do Enquadramento |  |
| `VLRINSSRECBRUTA13` | Decimal | Valor do INSS da Receita Bruta |  |
| `FATOR13` | Decimal | Fator 13 |  |
| `CODRECOLHIMENTO` | Inteiro | Codigo de  Recolhimento |  |
| `SIMPLES` | Texto | Optante pelo Simples |  |
| `DTENQUADRAMENTO` | Data | Data Enquadramento |  |
| *... +13 campos adicionais* | | | |

**Opções `BAIXAFERIASANTECIPADAS`:** `S`=Sim, `N`=Não

**Opções `CALCINSSEMPFUNC`:** `N`=Não, `S`=Sim

**Opções `CALCINSSEMPINDIV`:** `N`=Não, `S`=Sim

**Opções `CGCOUCEI`:** `A`=CAEPF, `F`=CNO, `E`=CEI, `C`=CNPJ

**Opções `INDCONTSIMPLES`:** `3`=3 - Contribuição não substituida concomitante com contribuição substituida, `2`=2 - Contribuição não substituida, `1`=1 - Contribuição Substituida Integralmente

**Opções `INDSUBSTPATR`:** `2`=2 - Parcialmente substituida, `1`=1 - Integralmente substituida

### TFPFOLTESTE
**TABLE TFPFOLTESTE**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPFOLHA`, `CODEVENTO`, `SEQUENCIA`, `TIPEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | REFERENCIA | → `TFPBASTESTE`.`REFERENCIA` |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPEMP`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPBASTESTE`.`CODFUNC` |
| `TIPFOLHA` 🔑 | Texto | TIPFOLHA | → `TFPBASTESTE`.`TIPFOLHA` |
| `CODEVENTO` 🔑 | Inteiro | CODEVENTO |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `VLREVENTO` | Decimal | VLREVENTO |  |
| `INDICE` | Decimal | INDICE |  |
| `UNIDADE` | Texto | UNIDADE |  |
| `PRAZO` | Inteiro | PRAZO |  |
| `VLRCALCULO` | Decimal | VLRCALCULO |  |
| `OBS` | Texto | OBS |  |
| `NUFIN` | Inteiro | NUFIN |  |
| `TIPEVENTO` 🔑 | Inteiro | TIPEVENTO |  |
| `NUOCOR` | Inteiro | NUOCOR |  |
| `REFERENCIAORIG` | Data/Hora | REFERENCIAORIG |  |
| `TIPFOLHAORIG` | Texto | TIPFOLHAORIG |  |
| `SEQUENCIAORIG` | Inteiro | SEQUENCIAORIG |  |
| `CODEVENTOORIG` | Inteiro | CODEVENTOORIG |  |
| `VLRORIGINAL` | Decimal | VLRORIGINAL |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `INDORIGINAL` | Decimal | INDORIGINAL |  |
| `DIGITADO` | Texto | DIGITADO |  |
| `CODUSU` | Inteiro | CODUSU |  |
| `PROTEGIDO` | Texto | PROTEGIDO |  |
| `USADOESOCIAL` | Texto | USADOESOCIAL |  |
| `EHCOMPLEMENTAR` | Texto | E COMPLEMENTAR |  |
| `SEQROE` | Inteiro | SEQROE |  |
| `CODPARCPENS` | Inteiro | ParceiroPensao |  |
| `NROINFODESCFOL` | Inteiro | Informação do emprestimo em folha |  |

**Opções `EHCOMPLEMENTAR`:** `S`=Sim, `N`=Não

### TFPFOR
**FP Formulas de Calculo**

**PK:** `CODFORM`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `SANKHYA` | Texto | SANKHYA |  |
| `CODFORM` 🔑 | Inteiro | Codigo |  |
| `CODFORMIND` | Texto | Cod.Formula IND |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DESCRFORM` | Texto | Descrição |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `FORMULA` | Texto | Formula |  |
| `FORMULANTERIOR` | Texto | Formula anterior |  |

**Opções `SANKHYA`:** `N`=Não, `S`=Sim

### TFPFRE
**TABLE TFPFRE**

**PK:** `CODREINT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` | Inteiro | CODEMP |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `CODREINT` 🔑 | Inteiro | Codigo da Reintegração |  |
| `DTREFERENCIA` | Data | Referencia da Reintegração |  |
| `DTRETORNO` | Data | Data de Retorno |  |
| `DTDEM` | Data | Data do Desligamento |  |
| `AFASTFGTS` | Texto | Motivo do Afastamento para FGTS |  |
| `TIPFOLHA` | Texto | Tipo de Folha |  |
| `SALLIQ` | Decimal | Salario Liquido |  |
| `SALBRUTO` | Decimal | Salario Bruto |  |

### TFPFTR
**TABLE TFPFTR**

**PK:** `CODFATRISCO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFATRISCO` 🔑 | Texto | CODFATRISCO |  |
| `DESCRFATRISCO` | Texto | DESCRFATRISCO |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPFTRC
**Treinamento e Capacitação Esocial**

**PK:** `CODEMP`, `CODFUNC`, `CODTREICAP`, `DHALTER`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODTREICAP` 🔑 | Inteiro | Codigo do Treinamento/Capacitação no eSocial |  |
| `DHALTER` 🔑 | Data | Data de Alteracao |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TFPGCA
**TABLE TFPGCA**

**PK:** `CODGRUPOCARGO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOCARGO` 🔑 | Inteiro | CODGRUPOCARGO |  |
| `DESCRGRUPOCARGO` | Texto | DESCRGRUPOCARGO |  |
| `ATIVO` | Texto | ATIVO |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | DTALTER |  |

### TFPGCB
**TABLE TFPGCB**

**PK:** `CODGRUPOCTBZ`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOCTBZ` 🔑 | Inteiro | Codigo |  |
| `DESCRGRUPOCTBZ` | Texto | Descrição |  |

### TFPGHO
**Grupos de Historicos de Ocorrencias**

**PK:** `CODGRUPOOCO`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOOCO` 🔑 | Inteiro | Cod.Grupo de Ocorrencia |  |
| `DESCRGRUPOOCO` | Texto | Descrição do Grupo de Ocorrencias |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `CODGRUPOOCOPAI` | Inteiro | Cod.Grupo de Ocorrencia Pai |  |
| `GRAU` | Inteiro | Grau |  |
| `MODULO` | Texto | Modulo |  |

**Opções `ANALITICO`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

### TFPGHR
**TABLE TFPGHR**

**PK:** `CODGRUPOHORARIO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRUPOHORARIO` 🔑 | Inteiro | CODGRUPOHORARIO |  |
| `DESCRGRUPOHR` | Texto | DESCRGRUPOHR |  |
| `DTINICIO` | Data/Hora | DTINICIO |  |
| `QTDDIAS` | Inteiro | QTDDIAS |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPGPS
**Guia de Recolhimento do PIS**

**PK:** `REFERENCIA`, `CODEMP`, `CODPARC`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | Referencia |  |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPEMP`.`CODEMP` |
| `CODPARC` 🔑 | Inteiro | Cod.Parceiro | → `TGFPAR`.`CODPARC` |
| `CREDITO` | Decimal | Credito |  |
| `SALDO` | Decimal | Saldo |  |
| `DEBITO` | Decimal | Debito |  |
| `VLRDIGITADO` | Decimal | Valor do credito digitado na GPS |  |

### TFPGRA
**Gratificações**

**PK:** `CODGRAT`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODGRAT` 🔑 | Inteiro | Cod.Gratificação |  |
| `CODFUNCAO` | Inteiro | Codigo da função | → `TFPFCO`.`CODFUNCAO` |
| `DESCRGRAT` | Texto | Descrição |  |
| `PERCENTUAL` | Decimal | Percentual |  |

### TFPGRD
**Gratificações por Departamento**

**PK:** `CODDEP`, `CODGRAT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODDEP` 🔑 | Inteiro | Departamento | → `TFPDEP`.`CODDEP` |
| `CODGRAT` 🔑 | Inteiro | Gratificação | → `TFPGRA`.`CODGRAT` |
| `TOTDISP` | Decimal | Total disponivel |  |
| `TOTGERAL` | Decimal | Total geral |  |

### TFPGRUEVE
**Grupo de Eventos**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `DESCRICAO` | Texto | DESCRICAO |  |

### TFPHASH
**Hash Arquivos Folha**

**PK:** `NOME`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NOME` 🔑 | Texto | NOME |  |
| `HASH_VALUE` | Texto | HASH VALUE |  |
| `DATA_ATUALIZACAO` | Data | DATA DE ATUALIZACAO |  |

### TFPHCP
**tab faixa hora extra**

**PK:** `NULIMITEHR`, `NUCOMPHR`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NULIMITEHR` 🔑 | Inteiro | NULIMITEHR | → `TFPHLM`.`NULIMITEHR` |
| `NUCOMPHR` 🔑 | Inteiro | NUCOMPHR |  |
| `DESCRCOMPHR` | Texto | DESCRCOMPHR |  |
| `EXTRA` | Texto | EXTRA |  |
| `EXCEDENTE` | Texto | EXCEDENTE |  |
| `DOMFER` | Texto | DOMFER |  |
| `EXTRANOT` | Texto | EXTRANOT |  |
| `EXCEDENTENOT` | Texto | EXCEDENTENOT |  |
| `DOMFERNOT` | Texto | DOMFERNOT |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPHFE
**Tabela de Ferias**

**PK:** `CODEMP`, `CODFUNC`, `REFERENCIA`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa |  |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario |  |
| `DTINIAQUI` | Data | Data inicio aquisição |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `DTFINAQUI` | Data | Data final aquisição |  |
| `DTPREVISTA` | Data | Data prevista |  |
| `DTSAIDA` | Data | Data da saida |  |
| `FALTPER` | Inteiro | Faltas no periodo |  |
| `ABONOPEC` | Inteiro | Abono pecuniario |  |
| `NUMDIASFER` | Inteiro | Numero de dias de ferias |  |
| `ADIANTA13SAL` | Texto | Adianta 13 salario |  |
| `ATUALFERGOZ` | Texto | Atualiza ferias gozadas |  |
| `ABONOINICIO` | Texto | Dias  abono inicio ou fim |  |
| `QTDPARCELAS` | Inteiro | Quantidade de parcelas do emprestimo |  |
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `DIGITADO` | Texto | Digitado |  |
| `APROVADO` | Texto | Aprovado |  |
| `QTDDIASSOLFERIAS` | Inteiro | Qtd. dias solicitação ferias |  |
| `DTLIMGOZFER` | Data | Data limite para gozo de ferias |  |
| `PERQUITADO` | Texto | Periodo quitado |  |

**Opções `ABONOINICIO`:** `N`=Não, `S`=Sim

**Opções `ADIANTA13SAL`:** `N`=Não, `S`=Sim

**Opções `APROVADO`:** `S`=Sim, `N`=Não

**Opções `ATUALFERGOZ`:** `S`=Sim, `N`=Não

**Opções `DIGITADO`:** `S`=Sim, `N`=Não

**Opções `PERQUITADO`:** `N`=Não, `S`=Sim

### TFPHFI
**TABLE TFPHFI**

**PK:** `REFERENCIA`, `CODREGFIS`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `CODREGFIS` 🔑 | Inteiro | CODREGFIS |  |
| `CODSAT` | Inteiro | Cod. Sat |  |
| `PERCINSS` | Decimal | Perc.INSS |  |
| `CODGRPS` | Inteiro | Cod. GRPS |  |
| `TAXAGRPS` | Decimal | Taxa GRPS |  |
| `TAXASEG` | Decimal | Taxa Seguro |  |
| `ATIVIRF` | Inteiro | Ativ.IRF |  |
| `ATIVIBGE` | Inteiro | Ativ.IBGE |  |
| `ATIVINSS` | Inteiro | Ativ.INSS |  |
| `PERPAGTOFGTS` | Decimal | Perc.FGTS |  |
| `CODPAGGPS` | Inteiro | Cod.Pagto GPS |  |
| `PERCISEFIL` | Decimal | Perc.Isenção Filantropia |  |
| `OPTSIMPLES` | Inteiro | Opt. Simples |  |
| `PERFGTSMENOR` | Decimal | Perc.FGTS Menor Aprendiz |  |
| `RAT15` | Decimal | Rat15 |  |
| `RAT20` | Decimal | Rat20 |  |
| `RAT25` | Decimal | Rat25 |  |
| `FATORFAP` | Decimal | Fator FAP |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | DTALTER |  |
| `VLRINSSRECBRUTA` | Decimal | Vlr INSS Rec. Bruta |  |
| `PERCINSSPATRONAL` | Decimal | Perc. INSS Patronal 13 |  |
| `VLRINSSRECBRUTA13` | Decimal | Vlr INSS Rec. Bruta 13 |  |
| `PERCRECBRUTAINSS` | Decimal | Percentual da  Receita Bruta para INSS |  |
| `PERCRECBRUTAINSS13` | Decimal | Percentual da Receita Bruta para INSS 13 |  |
| `CODRECOLHIMENTO` | Inteiro | Codigo de  Recolhimento |  |
| `PERCPISFOLHA` | Decimal | Perc. PIS Sobre a Folha |  |
| `FATORMES` | Decimal | Fator Mes |  |
| `ISEMPRESACONTRIBUINTE` | Texto | Empresa contribuinte |  |
| `FATOR13` | Decimal | Fator 13 |  |
| `CODRECEITASOBFOLHA` | Inteiro | Cod. Receita Sobre Folha |  |

**Opções `ISEMPRESACONTRIBUINTE`:** `N`=Não, `S`=Sim

### TFPHFU
**Historico do funcionario**

**PK:** `CODEMP`, `CODFUNC`, `REFERENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | Referencia |  |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `TIPSAL` | Texto | Tipo salario |  |
| `SALBASE` | Decimal | Salario base |  |
| `REMUMINIMA` | Decimal | Remuneração minima |  |
| `SITSIND` | Texto | Situação Sindicato |  |
| `CODSIND` | Inteiro | Cod.Sindicato | → `TFPSIN`.`CODSIND` |
| `CODDEP` | Inteiro | Cod.Departamento | → `TFPDEP`.`CODDEP` |
| `CODCARGO` | Inteiro | Cod.Cargo | → `TFPCAR`.`CODCARGO` |
| `CODFUNCAO` | Inteiro | Cod.Função | → `TFPFCO`.`CODFUNCAO` |
| `CODCATEG` | Inteiro | Cod.Categoria | → `TFPCAT`.`CODCATEG` |
| `HORASSEM` | Decimal | Horas Semanais |  |
| `CODADMFGTS` | Texto | Tabela de ocorrencia [FGTS] |  |
| `CODADMFGTSII` | Texto | Tabela de categoria [FGTS] |  |
| `TRABOUTRAEMP` | Texto | Trabalha em Outra Empresa |  |
| `PARTPAT` | Texto | Progr. de Alimentação do Trab. |  |
| `CODCBO` | Inteiro | Cod.Banco |  |
| `NIVESC` | Inteiro | Escolaridade |  |
| `ESTADOCIVIL` | Inteiro | Estado Civil |  |
| `TIPDEFICIENCIA` | Inteiro | Deficiencia |  |
| `CODCIDTRAB` | Inteiro | Cod. Cidade Trabalho | → `TSICID`.`CODCID` |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `SITUACAO` | Texto | Situação |  |
| `TPINSCAPREND` | Inteiro | Tipo de Inscrição |  |
| `NRINSCAPREND` | Texto | Numero de Inscrição |  |
| `CNPJENTQUAL` | Texto | CNPJ Entidade Qualificadora |  |
| `CNPJPRAT` | Texto | CNPJ Entidade Pratica |  |
| `REGIMEJOR` | Inteiro | Regime de Jornada |  |
| `DTTERMINO` | Data | Data Termino do Contrato |  |
| `OBSVARIAVEL` | Texto | Observação da Remuneração Variavel |  |
| `APRENDCONTRIND` | Texto | Contratação Indireta de Aprendiz |  |

### TFPHIS
**Historicos Ocorrencias**

**PK:** `CODHISTOCOR`  
**Referenciada por:** 7 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODHISTOCOR` 🔑 | Inteiro | Historico |  |
| `DESCRHISTOCOR` | Texto | Descrição |  |
| `TIPTAB` | Texto | Tipo de tabela | → `TFPAFA`.`TIPTAB` |
| `AFASTAMENTO` | Texto | Afastamento |  |
| `CODAFAST` | Texto | Codigo de afastamento | → `TFPAFA`.`CODAFAST` |
| `CODAFARAIS` | Inteiro | Codigo Afastamento RAIS |  |
| `CODAFACAUSA` | Inteiro | Codigo Afastamento Causa |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `FALTA` | Texto | Falta |  |
| `CODGRUPOOCO` | Inteiro | CODGRUPOOCO | → `TFPGHO`.`CODGRUPOOCO` |
| `BAIXAPROVISAO` | Texto | BAIXAPROVISAO |  |
| `ABSENTEISMO` | Texto | ABSENTEISMO |  |
| `TIPREG` | Texto | TIPREG |  |
| `OCORRENCIAAFDT` | Texto | OCORRENCIAAFDT |  |
| `DIREITOADN` | Texto | DIREITOADN |  |
| `QUITAFERLICREM` | Texto | QUITAFERLICREM |  |
| `REDUZDIASTRAB` | Texto | REDUZDIASTRAB |  |
| `ABATEAVISOPREVIO` | Texto | ABATEAVISOPREVIO |  |
| `APELIDO` | Texto | APELIDO |  |
| `COR` | Texto | COR |  |
| `UTILIZAMOTIVO` | Texto | UTILIZAMOTIVO |  |
| `DEDUZDIASAVISO` | Texto | Deduz dias de Aviso previo lei 12.506/2011 |  |
| `CODMOTAFAST` | Texto | CODMOTAFAST |  |
| `INDENIZAESTAB` | Texto | INDENIZAESTAB |  |
| `QTDMESESESTAB` | Inteiro | QTDMESESESTAB |  |
| `APARECEPORTAL` | Texto | APARECEPORTAL |  |
| `REAJSALSIND` | Texto | REAJSALSIND |  |
| `ANEXOOBRIGATORIO` | Texto | ANEXOOBRIGATORIO |  |
| `DESCARTAOPONTO` | Texto | DESCARTAOPONTO |  |
| `SUSPCOMRESIDUO` | Texto | SUSPCOMRESIDUO |  |
| `COMPNPROG` | Texto | COMPNPROG |  |
| `HRCOMPL` | Inteiro | HRCOMPL |  |
| `QFERAFART133` | Texto | QFERAFART133 |  |

**Opções `AFASTAMENTO`:** `N`=Não e afastamento, `D`=Doenca acima de 15 dias, `F`=Ferias, `L`=Faltas, `S`=Sem remuneração, `G`=Licenca gestante, `A`=Acidente de trabalho, `P`=Licenca paternidade, `M`=Servico militar

**Opções `FALTA`:** `S`=Sim, `N`=Não

### TFPHLM
**TABLE TFPHLM**

**PK:** `NULIMITEHR`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NULIMITEHR` 🔑 | Inteiro | NULIMITEHR |  |
| `DESCRLIMITEHR` | Texto | DESCRLIMITEHR |  |
| `TIPOLIMITE` | Inteiro | TIPOLIMITE |  |
| `USAHORADIARIA` | Texto | USAHORADIARIA |  |
| `USALIMITEMENSAL` | Texto | USALIMITEMENSAL |  |
| `SOMAACRESCLIMITE` | Texto | SOMAACRESCLIMITE |  |

### TFPHTR
**Historico de Transferencias**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | Identificador |  |
| `CODEMP` | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `AFASTFGTS` | Texto | Motivo do Afastamento para FGTS |  |
| `AFASTRAIS` | Texto | Motivo do Afastamento para RAIS |  |
| `CAUSAAFAST` | Texto | Causa do Afastamento |  |
| `SITUACAO` | Texto | Situação |  |
| `DTTRANSFERENCIA` | Data | Data da Transferencia |  |
| `CODEMPDEST` | Inteiro | Empresa de Destino |  |
| `CODFUNCDEST` | Inteiro | Codigo funcionario de destino |  |

**Opções `SITUACAO`:** `1`=Atividade normal, `2`=Afastado sem remuneração, `4`=Afastado para servico militar, `5`=Afastado por licenca gestante, `6`=Afastado por doenca acima de 15 dias, `7`=Outros, `8`=Transferido, `0`=Demitido, `9`=Aposentadoria por Invalidez, `3`=Afastado por acidente de trabalho

### TFPIBPA
**Informação dos beneficiarios da pensão alimenticia**

**PK:** `NUIBPA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUIBPA` 🔑 | Inteiro | NUIBPA |  |
| `NUITCR` | Inteiro | NUITCR | → `TFPITCR`.`NUITCR` |
| `NMDEP` | Texto | Dependente |  |
| `TPREND` | Texto | Tipo de rendimento |  |
| `CPFDEP` | Texto | CPF |  |
| `VLRPENSAO` | Decimal | Valor da Pensão |  |

### TFPICRT
**Informações complementares Rendimentos Tributaveis**

**PK:** `NUCRT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCRT` 🔑 | Inteiro | NUCRT |  |
| `NUITCR` | Inteiro | NUITCR | → `TFPITCR`.`NUITCR` |
| `VRRENDTRIB` | Decimal | Rendimento tributavel mensal do Imposto de Renda |  |
| `VRRENDTRIB13` | Decimal | Rendimento tributavel do IR de 13 - Tributação exclusiva |  |
| `VRRENDMOLEGRAVE` | Decimal | Rendimento isento para portador de molestia grave com laudo. |  |
| `VRRENDISEN65` | Decimal | Parcela isenta de aposentadora - Benef. com 65 anos ou mais |  |
| `VRJUROSMORA` | Decimal | Juros de mora por atraso de pagamento de salario |  |
| `VRRENDISENNTRIB` | Decimal | Outros rendimentos isentos ou não tributaveis |  |
| `DESCISENNTRIB` | Texto | Descrição de rendimentos isentos ou não tributaveis |  |
| `VRPREVOFICIAL` | Decimal | Previdencia Oficial |  |
| `VRRENDMOLEGRAVE13` | Decimal | Rendimento isento, portador molestia grave c/ laudo - 13 salario |  |
| `VRRENDISEN65DEC` | Decimal | Parcela isenta de aposentadoria - Benef. com 65 anos ou mais - 13 salario |  |
| `VRJUROSMORA13` | Decimal | Juros de mora por atraso de pagamento de salario - 13 salario |  |
| `VLRABONOPEC` | Decimal | Valor relativo ao abono pecuniario |  |
| `VLRDIARIAS` | Decimal | Valor relativo a diarias |  |
| `VLRAUXMORADIA` | Decimal | Valor relativo ao auxilio moradia |  |
| `VRPREVOFICIAL13` | Decimal | Previdencia oficial - 13 salario |  |
| `VLRINDRESCONTRATO` | Decimal | Valor relativo a indenização e rescisão de contrato, PDV e acidentes de trabalho |  |
| `VLRAJUDACUSTO` | Decimal | Valor relativo a ajuda de custo |  |

### TFPINC
**Incidencias da Pensão**

**PK:** `CODEMP`, `CODFUNC`, `SEQUENCIA`, `CODEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPDPD`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPDPD`.`CODFUNC` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia | → `TFPDPD`.`SEQUENCIA` |
| `CODEVENTO` 🔑 | Inteiro | Cod.Evento |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `ORIGPENS` | Texto | ORIGPENS |  |

### TFPINCCP
**PREVIDENCIA**

**PK:** `CODIGO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Texto | CODIGO |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPINCFGTS
**FGTS**

**PK:** `CODIGO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Texto | CODIGO |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPINCIRRF
**IRFF**

**PK:** `CODIGO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Texto | CODIGO |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPINCPIS
**PIS**

**PK:** `CODIGO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Texto | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `DHALTER` | Data/Hora | Data de alteração |  |
| `CODUSU` | Inteiro | Codigo usuario | → `TSIUSU`.`CODUSU` |

### TFPINCSIND
**INCIDENCIA SINDICAL**

**PK:** `CODIGO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODIGO` 🔑 | Texto | CODIGO |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPINF
**Informações Fiscais**

**PK:** `CODINFFISC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODINFFISC` 🔑 | Inteiro | Codigo |  |
| `CODPARC` | Inteiro | Parceiro |  |
| `CODCENCUS` | Inteiro | C.R: |  |
| `NUMNOTA` | Inteiro | Numera lista |  |
| `HISTORICO` | Texto | Historico |  |
| `CODTIPOPER` | Inteiro | T.Op |  |
| `CODNAT` | Inteiro | Natureza |  |
| `CODPROJ` | Inteiro | Projeto |  |
| `CODTIPTIT` | Inteiro | Tipo de Titulo |  |
| `CODCTABCOINT` | Inteiro | Conta |  |
| `TIPOCHEQUE` | Texto | Tipo Marc. Ch. |  |
| `DTNEG` | Data | Dt. Negociação |  |
| `DTVENC` | Data | Dt. Vencimento |  |
| `DTENTSAI` | Data | Dt. Entrada e Saida |  |

**Opções `TIPOCHEQUE`:** `I`=Sem emitir cheque, `D`=Agrupar nominal ao bco de pagto, `A`=Nominal ao fornecedor, `B`=Agrupar nominal ao fornecedor, `K`=Agrupar nominal a empresa, `J`=Nominal a empresa, `C`=Nominal ao bco de pagto, `H`=Agrupar nominal ao historico, `G`=Nominal ao historico, `F`=Agrupar não nominal, `E`=Não nominal

### TFPIPA
**Inconsistencias do Processo de Auditoria da Folha**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Texto | ID |  |
| `CHAVE` | Texto | Chave |  |
| `TIPO` | Texto | Tipo |  |
| `NOMEFUNC` | Texto | Nome do Funcionario |  |
| `DETALHES` | Texto | Detalhes |  |
| `ARTIGO` | Texto | Artigo |  |
| `CODUSU` | Inteiro | Codigo de usuario | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | Data de alteração |  |

### TFPIPRRDJ
**Informações de processos relacionados a não retenção de tributos ou a depositos judiciais**

**PK:** `NUIPRRDJ`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUIPRRDJ` 🔑 | Inteiro | Numero Unico TFPIPRRDJ |  |
| `NUITCR` | Inteiro | Numero Unico TFPITCR | → `TFPITCR`.`NUITCR` |
| `TPPROCRET` | Texto | Tipo de Processo |  |
| `NRPROCRET` | Texto | Numero do Processo |  |
| `CODSUSP` | Texto | Codigo Indicativo de Suspensão |  |
| `DESCPROCRET` | Texto | Descrição do Processo |  |

**Opções `TPPROCRET`:** `1`=1 - Administrativo, `2`=2 - Judicial

### TFPIRRA
**Informações complementares relativas a Rendimentos Recebidos Acumuladamente - RRA**

**PK:** `NURRA`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NURRA` 🔑 | Inteiro | NURRA |  |
| `NUITCR` | Inteiro | NUITCR | → `TFPITCR`.`NUITCR` |
| `DESCRRA` | Texto | Descrição dos Rendimentos Recebidos Acumuladamente |  |
| `QTDMESESRRA` | Inteiro | Quantidade de meses relativos ao RRA |  |
| `VLRDESPCUSTAS` | Decimal | Valor das custas judiciais |  |
| `VLRDESPADVOGADOS` | Decimal | Valor total das despesas com advogados |  |

### TFPITADV
**Identificação dos advogados**

**PK:** `NUITADV`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUITADV` 🔑 | Inteiro | NUITADV |  |
| `NURRA` | Inteiro | NURRA | → `TFPIRRA`.`NURRA` |
| `TIPOINSCR` | Texto | Tipo Inscrição |  |
| `CNPJCPF` | Texto | Numero de Inscrição |  |
| `VLRDESP` | Decimal | Valor da despesa |  |
| `NMADV` | Texto | Nome Adv/Empresa |  |

**Opções `TIPOINSCR`:** `1`=1 - CNPJ, `2`=2 - CPF

### TFPITCR
**Valor por Receita dos Tributos do Processo Trabalhista**

**PK:** `NUITCR`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUITCR` 🔑 | Inteiro | Nro. Unico |  |
| `NUITPRT` | Inteiro | Nro. Unico Informações de Tributos | → `TFPITPRT`.`NUITPRT` |
| `NUITPBC` | Inteiro | Nro. Unico Informações Base Calculo de Tributo | → `TFPITPBC`.`NUITPBC` |
| `TPVALOR` | Texto | Tipo |  |
| `CODRECEITA` | Inteiro | Codigo da Receita |  |
| `VALOR` | Decimal | Valor - Remuneração |  |
| `VALOR13` | Decimal | Valor - 13 Salario |  |

**Opções `TPVALOR`:** `2`=Redimento Tributavel, `1`=Previdenciaria/Outras Bases

### TFPITPBC
**Identificação Base Calculo dos Tributos do Processo Trabalhista**

**PK:** `NUITPBC`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUITPBC` 🔑 | Inteiro | Nro. Unico |  |
| `NUITPRT` | Inteiro | Nro. Unico Informações de Tributos | → `TFPITPRT`.`NUITPRT` |
| `DTREFCALC` | Data | Referencia da informação |  |
| `VLRBASCALCPREV` | Decimal | Base de Calculo Contribuição Previdenciaria - Remuneração |  |
| `VLRBASCALCPREV13` | Decimal | Base de Calculo Contribuição Previdenciaria - 13 Salario |  |
| `VLRREDTRIB` | Decimal | Rendimento Tributavel |  |
| `VLRREDTRIB13` | Decimal | Rendimento tributavel - 13 Salario |  |

### TFPITPRT
**Informações dos Tributos do Processo Trabalhista**

**PK:** `NUITPRT`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDESEQPROC` | Inteiro | Numero do grupo processo coletivo |  |
| `NUITPRT` 🔑 | Inteiro | Nro. Unico |  |
| `NUPRT` | Inteiro | Nro. Unico do Processo Trabalhista | → `TFPPRT`.`NUPRT` |
| `DTREFPGTO` | Data | Referencia de pagamento |  |
| `INCPORTALESOCIAL` | Texto | Inclusão realizada via Portal do eSocial |  |
| `OBSERVACAO` | Texto | Observação |  |
| `NRORECIBOESOCIAL` | Texto | Numero do Recibo eSocial (S-2501) |  |
| `CONFIRMADO` | Texto | Confirmado |  |
| `REGPASSIVO13` | Texto | REGPASSIVO13 |  |

**Opções `CONFIRMADO`:** `N`=Não, `S`=Sim

**Opções `INCPORTALESOCIAL`:** `N`=Não, `S`=Sim

### TFPIVRDJ
**Informações de valores relacionados a não retenção de tributos ou a depositos judiciais**

**PK:** `NUIVRDJ`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUIVRDJ` 🔑 | Inteiro | Numero Unico TFPIVRDJ |  |
| `NUIPRRDJ` | Inteiro | Numero Unico TFPIPRRDJ | → `TFPIPRRDJ`.`NUIPRRDJ` |
| `INDAPURACAO` | Texto | Periodo de apuração |  |
| `VLRNRETIDO` | Decimal | Valor de IR que deixou de ser retido |  |
| `VLRDEPJUD` | Decimal | Valor do deposito judicial |  |
| `VLRCMPANOCAL` | Decimal | Valor de compensação - ano calendario |  |
| `VLRCMPANOANT` | Decimal | Valor compensação - anos anteriores |  |
| `VLRRENDSUSP` | Decimal | Valor rendimento com exigibilidade suspensa |  |

**Opções `INDAPURACAO`:** `1`=1 - Mensal, `2`=2 - Anual

### TFPLBE
**Lancamento Beneficio**

**PK:** `CODLBE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `SITUACAOFUNC` | Inteiro | Situação Funcionario |  |
| `CODFUNC` | Inteiro | Cod. Funcionario |  |
| `NOMEFUNC` | Texto | Nome Funcionario |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `NOMEDEPEND` | Texto | Nome Dependente |  |
| `CODEVENTO` | Inteiro | Cod. Evento |  |
| `CODEMP` | Inteiro | Cod. Empresa |  |
| `DTREFEMP` | Data/Hora | Referencia Emp |  |
| `VLRTITULAR` | Decimal | Vlr. Titular |  |
| `VLRDEPEN` | Decimal | Vlr. Dependente |  |
| `CODCBE` | Inteiro | Cod. Central Beneficio |  |
| `CODBEN` | Inteiro | Cod. Beneficio |  |
| `CODDEP` | Inteiro | Cod. Departamento |  |
| `CODCARGO` | Inteiro | Cod. Cargo |  |
| `CODFUNCAO` | Inteiro | Cod. Função |  |
| `CODLBE` 🔑 | Inteiro | Cod. Lancamento Beneficio |  |

**Opções `SITUACAOFUNC`:** `9`=Aposentadoria por invalidez, `8`=Transferido, `7`=Outros, `6`=Afastado por doenca acima de 15 dias, `5`=Afastado por licenca gestante, `4`=Afastado para servico militar, `0`=Demitido, `3`=Afastado por acidente de trabalho, `2`=Afastado sem remuneração, `1`=Atividade normal

### TFPLFU
**Lotação Funcionario**

**PK:** `NUNO`, `CODEMP`, `CODFUNC`, `DTENTRADA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUNO` 🔑 | Inteiro | NUNO | → `TGFNES`.`NUNO` |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `DTENTRADA` 🔑 | Data/Hora | DTENTRADA |  |
| `DTSAIDA` | Data/Hora | DTSAIDA |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPLGR
**Logradouro**

**PK:** `CODLOGRADOURO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLOGRADOURO` 🔑 | Texto | Codigo |  |
| `DESCRLOGRADOURO` | Texto | Descrição |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | Dh. alteração |  |

### TFPLIDER
**Lideres**


| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` | Inteiro | Codigo da Empresa do Funcionario |  |
| `CODFUNC` | Inteiro | Codigo do Funcionario |  |
| `NOMEFUNC` | Texto | Nome do Funcionario |  |
| `CPFFUNC` | Texto | CPF do Funcionario |  |
| `CODEMPLIDER` | Inteiro | Codigo da Empresa Lider |  |
| `CODFUNCLIDER` | Inteiro | Codigo do Funcionario Lider |  |
| `NOMEFUNCLIDER` | Texto | Nome do Lider |  |
| `CPFLIDER` | Texto | CPF do Lider |  |
| `CODIGOPJ` | Inteiro | Codigo do Vinculo a PJ |  |

### TFPLIN
**Linhas de Onibus**

**PK:** `CODLINHA`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLINHA` 🔑 | Inteiro | Codigo |  |
| `TIPO` | Texto | Tipo de Vale |  |
| `DESCRLINHA` | Texto | Descrição |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `VLRTARIFA` | Decimal | Valor da Tarifa |  |

**Opções `TIPO`:** `T`=Transporte, `A`=Alimentação

### TFPLOGCALC
**Logs do calculo da folha**

**PK:** `CODLOG`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLOG` 🔑 | Inteiro | Codigo Log |  |
| `LOG` | C | LOG |  |
| `REFERENCIA` | Data | Referencia |  |

### TFPMAD
**TABLE TFPMAD**

**PK:** `CODMAD`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMAD` 🔑 | Inteiro | CODMAD |  |
| `DESCRMAD` | Texto | DESCRMAD |  |
| `UTILIZAEM` | Inteiro | UTILIZAEM |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPMEN
**FP Mensagens do Hollerit**

**PK:** `CODMENS`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMENS` 🔑 | Inteiro | Cod.Mensagem |  |
| `DESCRMENS` | Texto | Descrição |  |
| `MENSWGE` | Texto | Utilizada mensagem no Sankhya-W |  |

**Opções `MENSWGE`:** `N`=Nao, `S`=Sim

### TFPMOV
**Movimentos e Fixos**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPMOV`, `CODEVENTO`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | Data e hora de Referencia |  |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODEVENTO` 🔑 | Inteiro | Evento |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TIPEVENTO` | Inteiro | Tipo de evento |  |
| `VLRMOV` | Decimal | Valor |  |
| `INDICE` | Decimal | Indice |  |
| `DIGITADO` | Texto | Origem lancamento |  |
| `ORIGEMLANCAMENTO` | Texto | Origem lancamento |  |
| `UNIDADE` | Texto | Unidade |  |
| `PRAZO` | Inteiro | Prazo |  |
| `CODBCO` | Inteiro | Banco | → `TSIBCO`.`CODBCO` |
| `NUMCHEQ` | Inteiro | Numero do cheque |  |
| `PRAZOTOTAL` | Inteiro | Prazo total |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `OBS` | Texto | Observação |  |
| `CODUSU` | Inteiro | Codigo de Usuario | → `TSIUSU`.`CODUSU` |
| `NUFIN` | Inteiro | NUFIN | → `TGFFIN`.`NUFIN` |
| `NUOCOR` | Inteiro | Numero de Ocorrencia | → `TFPOCO`.`NUOCOR` |
| `PROVISAO` | Texto | PROVISO |  |
| `NUFALTA` | Inteiro | Numero de Faltas |  |
| `DIASUTEIS` | Inteiro | Dias Uteis |  |
| `DIASNAOUTEIS` | Inteiro | Dias Não Uteis |  |
| `TIPMOV` 🔑 | Texto | Tipo de movimento |  |
| `SEQFOLHA` | Inteiro | Sequencia Folha |  |
| `MANTEMPROXIMAREF` | Texto | Mantem Proxima Referencia |  |
| `CODCBE` | Inteiro | Acerto Beneficio | → `TFPCBE`.`CODCBE` |
| `INSCONSIG` | Texto | Matricula consignataria |  |
| `NRCONTR` | Texto | Contrato Consig.FGTS |  |
| `INDICEHORA` | Decimal | Indice Hora |  |
| `ORIGEM` | Texto | Origem |  |
| `SEQFER` | Inteiro | Seq. Ferias |  |
| `REFERENCIAORIG` | Data/Hora | Referencia de Origem |  |
| `TIPFOLHAORIG` | Texto | Tipo Folha Origem |  |
| `SEQUENCIAORIG` | Inteiro | Sequencia Origem |  |
| `CODPARCPENS` | Inteiro | ParceiroPensao |  |
| `TIPFOLHAFIXO` | Texto | Tipo Folha Fixo |  |
| `REFCOMPLEMENTAR` | Data/Hora | Data da Referencia de Origem |  |
| `NROINFODESCFOL` | Inteiro | Informação do emprestimo em folha |  |
| *... +1 campos adicionais* | | | |

**Opções `DIGITADO`:** `S`=Sim, `N`=Não

**Opções `MANTEMPROXIMAREF`:** `S`=Sim, `N`=Não

**Opções `ORIGEMLANCAMENTO`:** `C`=Importador Credito do Trabalhador, `W`=Importador Credito do Trabalhador WebService, `M`=Lancamento manual, `F`=Fechamento da referencia, `I`=Importador generico

**Opções `TIPEVENTO`:** `1`=Provento, `0`=Neutro, `-1`=Desconto

**Opções `TIPMOV`:** `V`=Avulso, `U`=Participação nos Lucros, `T`=Movimento Complementar, `S`=Suplementar, `P`=Produção, `O`=Dissidio, `C`=Rescisão Complementar, `F`=Fixo, `R`=Rescisão, `D`=13 Salario, `A`=Adiantamento, `M`=Mensal

**Opções `UNIDADE`:** `Q`=Quantidade, `V`=Valor, `H`=Horas, `D`=Dias

### TFPMOVANT
**Movimentos fixos anteriores**


| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` | Data/Hora | Data e hora de Referencia |  |
| `CODEMP` | Inteiro | Cod.Empresa |  |
| `CODFUNC` | Inteiro | Cod.Funcionario |  |
| `TIPMOV` | Texto | Tipo de movimento |  |
| `CODEVENTO` | Inteiro | Cod.Evento |  |
| `SEQUENCIA` | Inteiro | Sequencia |  |
| `TIPEVENTO` | Inteiro | Tipo de evento |  |
| `VLRMOV` | Decimal | Valor |  |
| `INDICE` | Decimal | Indice |  |
| `UNIDADE` | Texto | Unidade |  |
| `PRAZO` | Inteiro | Prazo |  |
| `CODBCO` | Inteiro | Cod.Banco |  |
| `NUMCHEQ` | Inteiro | Numero do cheque |  |

### TFPMRH
**Mensagens Portal RH**

**PK:** `CODMENSAGEM`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODMENSAGEM` 🔑 | Inteiro | Codigo |  |
| `CODEMP` | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODDEP` | Inteiro | Departamento | → `TFPDEP`.`CODDEP` |
| `CODFUNC` | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `DTENVIO` | Data/Hora | Dt. de Alteração |  |
| `TITULO` | Texto | Titulo |  |
| `DESCRICAO` | Texto | Mensagem |  |
| `CODUSU` | Inteiro | Usuario |  |

### TFPMTA
**Motivos de Afastamento**

**PK:** `CODMOTAFAST`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTFIMVALIDADE` | Data | Data Fim Validade |  |
| `DHALTER` | Data | Data da Ultima Alteração |  |
| `CODUSU` | Inteiro | Codigo do Usuario que Alterou por ultimo | → `TSIUSU`.`CODUSU` |
| `CODMOTAFAST` 🔑 | Texto | Codigo do Motivo de Afastamento |  |
| `DESCRMOTAFAST` | Texto | Descrição do Motivo do Afastamento |  |

### TFPMTD
**Motivos Desligamento (eSocial)**

**PK:** `CODMOTDESLIG`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUSU` | Inteiro | Codigo do Usuario da Ultima Alteração | → `TSIUSU`.`CODUSU` |
| `DESCRMOTDESLIG` | Texto | Descrição do Motivo de Desligamento |  |
| `DHALTER` | Data | Data Hora da Ultima Alteração |  |
| `CODMOTDESLIG` 🔑 | Texto | Codigo do Motivo de Desligamento |  |

### TFPNCO
**TABLE TFPNCO**

**PK:** `CODNATCOMP`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNATCOMP` 🔑 | Inteiro | Codigo |  |
| `DESCRNATCOMP` | Texto | Descrição |  |

### TFPNEWFORM
**TABLE TFPNEWFORM**

**PK:** `CODFORM`, `PSEUDOCODFORM`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFORM` 🔑 | Inteiro | CODFORM |  |
| `PSEUDOCODFORM` 🔑 | Inteiro | PSEUDOCODFORM |  |
| `DESCRFORM` | Texto | DESCRFORM |  |
| `FORMULA` | Blob | FORMULA |  |
| `INDICE` | Blob | INDICE |  |
| `DTALTER` | Data/Hora | DTALTER |  |
| `PKG` | Inteiro | PKG | → `TFPPKGFORM`.`CODPKG` |

### TFPNEWMED
**Nova Tabela de Medias**

**PK:** `CODEMP`, `CODFUNC`, `REFERENCIA`, `ORIGEM`, `TIPOMEDIA`, `MELHOR`, `CODEVENTO`, `SEQUENCIA`, `CATEGORIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `REFERENCIA` 🔑 | Data/Hora | REFERENCIA |  |
| `CODEVENTO` 🔑 | Inteiro | CODEVENTO |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `ORIGEM` 🔑 | Texto | ORIGEM |  |
| `TIPOMEDIA` 🔑 | Texto | TIPOMEDIA |  |
| `SALBASEMEDIA` | Decimal | SALBASEMEDIA |  |
| `VLR01` | Decimal | VLR01 |  |
| `VLR02` | Decimal | VLR02 |  |
| `VLR03` | Decimal | VLR03 |  |
| `VLR04` | Decimal | VLR04 |  |
| `VLR05` | Decimal | VLR05 |  |
| `VLR06` | Decimal | VLR06 |  |
| `VLR07` | Decimal | VLR07 |  |
| `VLR08` | Decimal | VLR08 |  |
| `VLR09` | Decimal | VLR09 |  |
| `VLR10` | Decimal | VLR10 |  |
| `VLR11` | Decimal | VLR11 |  |
| `VLR12` | Decimal | VLR12 |  |
| `MESANO01` | Texto | MESANO01 |  |
| `MESANO02` | Texto | MESANO02 |  |
| `MESANO03` | Texto | MESANO03 |  |
| `MESANO04` | Texto | MESANO04 |  |
| `MESANO05` | Texto | MESANO05 |  |
| `MESANO06` | Texto | MESANO06 |  |
| `MESANO07` | Texto | MESANO07 |  |
| `MESANO08` | Texto | MESANO08 |  |
| `MESANO09` | Texto | MESANO09 |  |
| `MESANO10` | Texto | MESANO10 |  |
| `MESANO11` | Texto | MESANO11 |  |
| `MESANO12` | Texto | MESANO12 |  |
| `IND01` | Decimal | IND01 |  |
| `IND02` | Decimal | IND02 |  |
| `IND03` | Decimal | IND03 |  |
| `IND04` | Decimal | IND04 |  |
| `IND05` | Decimal | IND05 |  |
| `IND06` | Decimal | IND06 |  |
| `IND07` | Decimal | IND07 |  |
| `IND08` | Decimal | IND08 |  |
| *... +13 campos adicionais* | | | |

### TFPNIV
**Niveis de Referencia**

**PK:** `CODNIVELREF`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNIVELREF` 🔑 | Inteiro | Codigo do nivel |  |
| `DESCRNIV` | Texto | Descrição |  |

### TFPNTL
**Descrição de lesões**

**PK:** `CODNATLESAO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNATLESAO` 🔑 | Inteiro | Codigo |  |
| `DESCRNATLESAO` | Texto | Descrição |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPOCO
**FP Registros de Ocorrencias**

**PK:** `NUOCOR`  
**Referenciada por:** 16 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFUNC` | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CODHISTOCOR` | Inteiro | Codigo da Ocorrencia | → `TFPHIS`.`CODHISTOCOR` |
| `CODEMP` | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `DTINICOCOR` | Data/Hora | Data Inicial da Ocorrencia |  |
| `DTINTERROMPEFER` | Data/Hora | Data Interrupção Periodo Ferias |  |
| `DTPREVRET` | Data/Hora | Data Final Prevista da Ocorrencia |  |
| `DTFINALOCOR` | Data/Hora | Data Final da Ocorrencia |  |
| `RECORRENTE` | Texto | Recorrente |  |
| `NUREINCID` | Inteiro | Numero Unico da Ocorrencia Reincidente | → `TFPOCO`.`NUOCOR` |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DIASPREVRET` | Inteiro | Dias previsto |  |
| `DIGITADO` | Texto | Digitado Manualmente |  |
| `SEQUENCIACNV` | Inteiro | Sequencia CNV | → `TFPCNV`.`SEQUENCIA` |
| `DESCROCOR` | Texto | Descrição da Ocorrencia |  |
| `NUOCOR` 🔑 | Inteiro | Numero Unico |  |
| `NUMANEJO` | Inteiro | Numero de Manejo | → `TFPMAN`.`NUMANEJO` |
| `NUOCORORIG` | Inteiro | Numero da Ocorrencia de Origem | → `TFPOCO`.`NUOCOR` |
| `INDEFEITORETRO` | Texto | Indicador Efeito Retroativo |  |
| `REAJUSTECCT` | Texto | Reajuste CCT |  |
| `NUFALTA` | Inteiro | Numero Falta |  |
| `ORIGRETIF` | Inteiro | Origem da Retificação |  |
| `CODSIND` | Inteiro | Codigo Sindicato | → `TFPCNV`.`CODSIND` |
| `NUPROCESSO` | Inteiro | Numero do Processo | → `TFPPSS`.`NUPROCESSO` |
| `ENVESOCIAL` | Texto | Envia pro Esocial |  |
| `ESPECIALIDADE` | Texto | Especialidade |  |
| `FORCADTFIM` | Texto | Forca Data Fim |  |
| `CID` | Texto | CID |  |
| `PROCESSOCNV` | Texto | Processo CNV | → `TFPCNV`.`PROCESSO` |

**Opções `ENVESOCIAL`:** `N`=Não, `S`=Sim

**Opções `FORCADTFIM`:** `N`=Não, `S`=Sim

**Opções `INDEFEITORETRO`:** `N`=Não, `S`=Sim

**Opções `REAJUSTECCT`:** `N`=Não, `S`=Sim

**Opções `RECORRENTE`:** `S`=Sim, `N`=Não

### TFPORG
**Orgãos**

**PK:** `CODORGAO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODORGAO` 🔑 | Inteiro | Orgão |  |
| `CATEGORIA` | Texto | Categoria |  |
| `NOMEORGAO` | Texto | Nome |  |

### TFPPAA
**Partes do Corpo Lesionadas**

**PK:** `NUCAT`, `CODPARTEATINGIDA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCAT` 🔑 | Inteiro | NUCAT |  |
| `CODPARTEATINGIDA` 🔑 | Texto | Cod. Parte do Corpo |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `LATERALIDADE` | Inteiro | Lateralidade |  |

**Opções `LATERALIDADE`:** `3`=3 - Ambas, `0`=0 - Não aplicavel, `1`=1 - Esquerda, `2`=2 - Direita

### TFPPCA
**Padrões de Cadastro de Funcionario**

**PK:** `NUPADRAO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPOCAD` | Texto | Tipo de Cadastro |  |
| `NUPADRAO` 🔑 | Inteiro | Codigo |  |
| `SANKHYA` | Texto | Padrão do Sistema |  |
| `INDADMISSAO` | Inteiro | Indicativo de Admissão |  |
| `DESCRPADRAO` | Texto | Descrição |  |
| `CODCATEGESOCIAL` | Inteiro | Categoria para o eSocial |  |
| `CODBAI` | Inteiro | Bairro | → `TSIBAI`.`CODBAI` |
| `SITESOCIAL` | Texto | Situação no eSocial |  |
| `CODCID` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `SEXO` | Texto | Sexo |  |
| `VINCULO` | Inteiro | Vinculo |  |
| `REGIMETRAB` | Inteiro | Regime Trabalhista |  |
| `ESTADOCIVIL` | Inteiro | Estado Civil |  |
| `REGIMEJOR` | Inteiro | Regime de Jornada |  |
| `NACIONALIDADE` | Inteiro | Nacionalidade |  |
| `NIVESC` | Inteiro | Escolaridade |  |
| `REGIME` | Inteiro | Regime Previdenciario |  |
| `TIPDEFICIENCIA` | Inteiro | Deficiencia |  |
| `RACAFUNCIONARIO` | Inteiro | Raca |  |
| `SALBASE` | Decimal | Salario Base |  |
| `DIASEXPER1` | Inteiro | Dias para vencimento do 1 Periodo |  |
| `HORASSEM` | Decimal | Horas Semanais |  |
| `CONVMED` | Texto | Convenio Medico |  |
| `DIASEXPER2` | Inteiro | Dias para vencimento do 2 Periodo |  |
| `REMUMINIMA` | Decimal | Remuneração Minima Assegurada |  |
| `PERCCONV` | Decimal | Percentual Convenio |  |
| `REMUNBASE` | Decimal | Bolsa Estagio / Pro-Labore |  |
| `TIPSAL` | Texto | Tipo de Salario |  |
| `COMPSALARIO` | Inteiro | Tipo de Remuneração |  |
| `CODADMFGTSII` | Texto | Tabela de Categoria (FGTS) |  |
| `TIPRECEB` | Texto | Tipo de Recebimento |  |
| `CODADMFGTS` | Texto | Tabela de Ocorrencias (FGTS) |  |
| `PERCADIANTAMENTO` | Decimal | % Adiantamento |  |
| `OPTFGTS` | Inteiro | Optante pelo FGTS |  |
| `PERCINSAL` | Decimal | % Insalubridade |  |
| `PERCPERIC` | Decimal | % Periculosidade |  |
| `CODDEP` | Inteiro | Departamento | → `TFPDEP`.`CODDEP` |
| `CODCARGO` | Inteiro | Cargo |  |
| `PARTPAT` | Texto | Participa do Programa de Alimentação do Trabalhador |  |
| `CODFUNCAO` | Inteiro | Função | → `TFPFCO`.`CODFUNCAO` |
| *... +16 campos adicionais* | | | |

**Opções `CODADMFGTS`:** `05`=05 Não exposição a agente nocivo, ja esteve mult. vinculo, `06`=06 Exposição a agente nocivo (apos. aos 15) mult. vinculo, `07`=07 Exposição a agente nocivo (apos. aos 20) mult. vinculo, `08`=08 Exposição a agente nocivo (apos. aos 25) mult. vinculo, `04`=04 Exposição a agente nocivo (aposentadoria aos 25), `01`=01 Não exposição a agente nocivo, mas ja esteve, `02`=02 Exposição a agente nocivo (aposentadoria aos 15), `03`=03 Exposição a agente nocivo (aposentadoria aos 20), `00`=00 Não exposição a agente nocivo

**Opções `COMPSALARIO`:** `1`=Salario Fixo, `2`=Variavel, `3`=Sal. Fixo + Variavel

**Opções `CONVMED`:** `N`=Não, `S`=Sim

**Opções `ESTADOCIVIL`:** `6`=Divorciado(a), `7`=Outros, `1`=Solteiro(a), `2`=Casado(a), `3`=Viuvo(a), `5`=Desquitado(a), `4`=Separado(a) judicialmente

**Opções `INDADMISSAO`:** `1`=Normal, `2`=Decorrente Ação Fiscal, `3`=Decorrente Descisão Judicial

**Opções `NIVESC`:** `1`=Analfabeto, `10`=Mestrado, `11`=Doutorado, `2`=Primario Incompleto, `3`=Primario Completo, `9`=Superior Completo, `5`=Ginasial Completo, `6`=Colegial Incompleto, `7`=Colegial Completo, `8`=Superior Incompleto, `4`=Ginasial Incompleto

### TFPPCAT
**Partes do corpo lesionadas**

**PK:** `CODPARTEATINGIDA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPARTEATINGIDA` 🔑 | Inteiro | Codigo |  |
| `DESCRPARTEATINGIDA` | Texto | Descrição da Parte do Corpo |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPPCG
**Perfil do Cargo**

**PK:** `CODCARGO`, `CODPERFIL`, `DTINICIO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `IMPRESCINDIVEL` | Texto | Imprescindivel |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `DTINICIO` 🔑 | Data | Data de Inicio |  |
| `CODCARGO` 🔑 | Inteiro | Cod.Cargo | → `TFPCAR`.`CODCARGO` |
| `TIPOPERIODO` | Texto | Tipo de Periodo |  |
| `DTFIM` | Data | Data Final |  |
| `CODPERFIL` 🔑 | Inteiro | Cod.Perfil | → `TFPPER`.`CODPERFIL` |
| `OBS` | Texto | Observação |  |
| `PESO` | Inteiro | Peso |  |
| `PERIODICIDADE` | Inteiro | Periodicidade |  |

**Opções `IMPRESCINDIVEL`:** `S`=Sim, `N`=Não

**Opções `TIPOPERIODO`:** `A`=Anual, `M`=Mensal

### TFPPER
**Perfil para Folha de Pagamento**

**PK:** `CODPERFIL`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPERFIL` 🔑 | Inteiro | Cod.Perfil |  |
| `DESCRPERFIL` | Texto | Descrição do Perfil |  |
| `CODPERFILPAI` | Inteiro | Cod.Perfil Pai |  |
| `ATIVO` | Texto | Ativo |  |
| `ANALITICO` | Texto | Analitico |  |
| `REQUISITO` | Texto | Requisito |  |
| `EXAME` | Texto | Exame |  |
| `NIVELHIER` | Texto | Nivel Hierarquico |  |
| `AREAPROF` | Texto | Area Profissional |  |
| `CODHISTOCOR` | Inteiro | Cod.Historico de Ocorrencia | → `TFPHIS`.`CODHISTOCOR` |
| `OBS` | Texto | Observação |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `GRAU` | Inteiro | Grau |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

**Opções `ANALITICO`:** `S`=Sim, `N`=Não

**Opções `AREAPROF`:** `N`=Não, `S`=Sim

**Opções `ATIVO`:** `N`=Não, `S`=Sim

**Opções `EXAME`:** `N`=Não, `S`=Sim

**Opções `NIVELHIER`:** `N`=Não, `S`=Sim

**Opções `REQUISITO`:** `N`=Não, `S`=Sim

### TFPPKGFORM
**TABLE TFPPKGFORM**

**PK:** `CODPKG`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPKG` 🔑 | Inteiro | CODPKG |  |
| `RAIZCNPJ` | Texto | RAIZCNPJ |  |
| `FINALCNPJ` | Texto | FINALCNPJ |  |
| `DESCRPKG` | Texto | DESCRPKG |  |

### TFPPLS
**Plano de Saude**

**PK:** `CODEMP`, `CODFUNC`, `SEQUENCIA`, `CODCONVENIO`, `REFERENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCONVENIO` 🔑 | Inteiro | Codigo do Convenio | → `TFPCON`.`CODCONVENIO` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `REFERENCIA` 🔑 | Data | Referencia Inicial |  |
| `REFERENCIAFIM` | Data | Referencia Final |  |
| `TABFAIXA` | Inteiro | Tabela de Faixa |  |
| `CODFAIXA` | Inteiro | Codigo da Faixa |  |
| `PARTICIPACAO` | Decimal | Percentual da Empresa |  |
| `CODUSU` | Inteiro | Codigo Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data | Data de Alteração |  |
| `CODFAIXAPROVENTO` | Inteiro | Faixa do Provento |  |

### TFPPONRAIO
**Locais Ponto Pessoal Mais**

**PK:** `ID`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | Codigo do local |  |
| `DESCRICAO` | Texto | Descrição |  |
| `GEOLOC` | Texto | Geolocalização |  |
| `CODDEP` | Inteiro | Departamento | → `TFPDEP`.`CODDEP` |
| `DESCRDEP` | Texto | Descrição do departamento |  |
| `CODEMP` | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `RAIO` | Inteiro | Raio |  |
| `CEP` | Texto | Cep |  |
| `CODEND` | Inteiro | Codigo do endereco |  |
| `NUMEND` | Texto | Numero do Endereco |  |
| `COMPLEMENTO` | Texto | Complemento do endereco |  |
| `CODBAI` | Inteiro | Codigo do bairro |  |
| `UFENDERECO` | Inteiro | Unidade Federativa Endereco |  |
| `CODCID` | Inteiro | Codigo da cidade |  |
| `CODPAIS` | Inteiro | Codigo do pais |  |
| `DTCRIACAO` | Data/Hora | Data de Criação |  |
| `TEMCONTROLEPONTO` | Texto | Tem controle de Ponto |  |
| `DHALTER` | Data/Hora | Data de alteração |  |

**Opções `TEMCONTROLEPONTO`:** `S`=Sim, `N`=Não

### TFPPPRG
**Paradas Programadas**

**PK:** `CODCARGAHOR`, `DIASEM`, `TURNO`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DESCRICAO` | Texto | Descrição |  |
| `INICIO` | Data/Hora | Hora Inicio |  |
| `FIM` | Data/Hora | Hora Fim |  |
| `DURACAO` | Inteiro | Duração (Min) |  |
| `CODCARGAHOR` 🔑 | Inteiro | Cod.Carga horaria | → `TFPHOR`.`CODCARGAHOR` |
| `DIASEM` 🔑 | Inteiro | Dia da semana - Sequencia | → `TFPHOR`.`DIASEM` |
| `TURNO` 🔑 | Inteiro | Turno | → `TFPHOR`.`TURNO` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |

### TFPPRE
**Regras de Calculo**

**PK:** `CODPREF`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `PAGATRASO` | Inteiro | Pagamento em Atraso |  |
| `PAGHSEXTRA` | Inteiro | Pagamento Hora Extra |  |
| `MESESMEDIARESC2` | Inteiro | Meses para medias de rescisão 2 periodo |  |
| `MESESMEDIARESC` | Inteiro | Numero de meses para media na rescisão |  |
| `MESESMEDIAFER2` | Inteiro | Meses para medias de ferias 2 periodo |  |
| `MESESMEDIAFER` | Inteiro | Numero de meses para media nas ferias |  |
| `MESESMEDIA13S2` | Inteiro | Meses para medias de 13 2 periodo |  |
| `PROVFERMEDIAS` | Texto | Provisionar ferias e 13 salario com medias |  |
| `QTDMAIORES` | Inteiro | Quantidade para considerar os maiores valores |  |
| `REMUMINIMA` | Decimal | Remuneração Minima Assegurada |  |
| `RESPFOLHA` | Texto | Responsavel pela folha |  |
| `TIPARRED` | Texto | Tipo de arredondamento |  |
| `TIPMES` | Texto | Tipo de mes |  |
| `TIPMOVMEDIAS` | Texto | Tipo de incidencia do movimento nas medias |  |
| `ATUMOVMEN` | Texto | Atualiza Movimentação Mensal |  |
| `CALCFERPERAQUI` | Texto | Calcular medias de ferias sobre perido aquisitivo |  |
| `CALCPARCFER` | Texto | Aceitar calculo parcial de ferias |  |
| `CALCRESIDUO` | Texto | Calcular residuo quando mes com 31 ou 28 dias |  |
| `CENTIRF` | Texto | Centavos no IRF |  |
| `CENTVALORES` | Texto | Centavos nos valores |  |
| `CODEVENBHORAS` | Inteiro | Evento para Banco de Horas |  |
| `CODEVENCRED` | Inteiro | Evento para credito |  |
| `CODEVENDEB` | Inteiro | Evento para Debito |  |
| `CODEVENDOMIN` | Inteiro | Codigo Evento Domingo |  |
| `CODEVENNOTUR` | Inteiro | Codigo Evento Noturno |  |
| `CODEVENPOSPRI` | Inteiro | Codigo Evento Apos Primeiras |  |
| `CODEVENPRI` | Inteiro | Codigo Evento Primeiras |  |
| `CODPREF` 🔑 | Inteiro | Cod.Preferencia |  |
| `COMPENSACAO` | Texto | Compensação |  |
| `DESCRICAO` | Texto | Descrição |  |
| `ARREDSALLIQ` | Decimal | Arredondamento do salario liquido |  |
| `DIARETIRADPD` | Inteiro | Dia limite para retirar dependentes |  |
| `FERPROPERAQUI` | Texto | Calcula Ferias Proporcionais por Periodo Aquisitivo |  |
| `FORMACALCMEDIAS` | Texto | Forma de calculo de medias |  |
| `IRFMIN` | Decimal | IRF Minimo |  |
| `LANCFERADIANT` | Texto | Lancar parte das ferias como adiatamento |  |
| `LIMMINHEXTRA` | Inteiro | Limite Minimo de Hora Extra |  |
| `LIMMINTOLATR` | Inteiro | Limite Minimo de Tolerancia de Atraso |  |
| `MEDIAARITIM13` | Texto | Calcular medias aritimeticas |  |
| `MEDIAPERFERIAS` | Texto | Media Periodo Ferias |  |
| *... +6 campos adicionais* | | | |

**Opções `ATUMOVMEN`:** `N`=Nenhum, `B`=Banco de Horas, `F`=Folha

**Opções `CALCFERPERAQUI`:** `S`=Sim, `N`=Não

**Opções `CALCPARCFER`:** `S`=Sim, `N`=Não

**Opções `CALCRESIDUO`:** `S`=Sim, `N`=Não

**Opções `CENTIRF`:** `S`=Sim, `N`=Não

**Opções `CENTVALORES`:** `N`=Não, `S`=Sim

### TFPPROF
**TABLE TFPPROF**

**PK:** `CPFPROF`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CPFPROF` 🔑 | Texto | CPF |  |
| `NMPROF` | Texto | Nome |  |
| `TPPROF` | Inteiro | Tipo |  |
| `MATRICULA` | Texto | Matricula |  |
| `FORMPROF` | Texto | Formação Profissional |  |
| `CODCBO` | Texto | CBO |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `NACPROF` | Inteiro | Nacionalidade |  |

**Opções `NACPROF`:** `1`=1 - Brasileiro, `2`=2 - Estrangeiro

**Opções `TPPROF`:** `2`=2 - Profissional sem vinculo emprego/estatutario com o declarante, `1`=1 - Profissional empregado  do declarante

### TFPPRT
**Processo Trabalhista**

**PK:** `NUPRT`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDESEQTRAB` | Inteiro | Numero sequencial |  |
| `NUPRT` 🔑 | Inteiro | Nro. Unico |  |
| `CODEMP` | Inteiro | Codigo da Empresa |  |
| `INCPORTALESOCIAL` | Texto | Inclusão realizada via Portal do eSocial |  |
| `RESPINDIRETA` | Texto | Ha responsabilidade indireta |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de inscrição |  |
| `NRPROCESSO` | Texto | Numero do processo |  |
| `NRINSCEMPREGADOR` | Texto | Numero de inscrição |  |
| `ORIGPROCESSO` | Inteiro | Origem do processo |  |
| `MATRESPDIR` | Texto | Matricula no empregador de origem |  |
| `DTADMRESPDIR` | Data | Data de admissão do trabalhador no empregador de origem |  |
| `NRORECIBOESOCIAL` | Texto | Numero do Recibo eSocial (S-2500) |  |
| `OBSPROCESSO` | Texto | Obs. Processo Trabalhista |  |
| `DTSENTENCA` | Data | Data da sentenca |  |
| `UFVARA` | Texto | UF da Vara |  |
| `CODCID` | Inteiro | Codigo da Cidade |  |
| `IDVARA` | Inteiro | Identificação da Vara |  |
| `DTLAUDOMOLESTIA` | Data | Data da molestia grave atribuida pelo laudo |  |
| `DTCONCILIACAO` | Data | Data da conciliação |  |
| `AMBITOCELEBRACAO` | Inteiro | Ambito de celebração do acordo |  |
| `CNPJSINDCATO` | Texto | CNPJ do sindicato |  |
| `TRABCONTRATDECL` | Texto | Trabalhador contratado pelo declarante |  |
| `CODEMPTRAB` | Inteiro | Codigo Empresa do Trabalhador |  |
| `CODFUNCTRAB` | Inteiro | Codigo do Trabalhador |  |
| `CPFTRAB` | Texto | CPF do Trabalhador |  |
| `NOMETRAB` | Texto | Nome do Trabalhador |  |
| `DTNASCTOTRAB` | Data | Data de nascimento |  |
| `CONFIRMADO` | Texto | Confirmado |  |

**Opções `AMBITOCELEBRACAO`:** `3`=NINTER, `1`=CCP no ambito de empresa, `2`=CCP no ambito de sindicato

**Opções `CONFIRMADO`:** `S`=Sim, `N`=Não

**Opções `INCPORTALESOCIAL`:** `S`=Sim, `N`=Não

**Opções `ORIGPROCESSO`:** `2`=Demanda submetida a CCP ou NINTER, `1`=Processo Judicial

**Opções `RESPINDIRETA`:** `N`=Não, `S`=Sim

**Opções `TPINSCEMPREGADOR`:** `1`=CNPJ, `2`=CPF

### TFPPRTABONO
**TFPPRTABONO**

**PK:** `NUABONO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUABONO` 🔑 | Inteiro | Numero unico Abono Salarial |  |
| `NUICT` | Inteiro | Nro. Unico Info. Contrato Trabalho | → `TFPPRTICT`.`NUICT` |
| `ANOBASE` | Data | Ano base indenização substitutiva abono salarial |  |

### TFPPRTC
**TABLE TFPPRTC**

**PK:** `NUPROCESSO`, `CODREGFIS`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPROCESSO` 🔑 | Inteiro | Numero unico | → `TFPPSS`.`NUPROCESSO` |
| `CODREGFIS` 🔑 | Inteiro | CODREGFIS | → `TFPFIS`.`CODREGFIS` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPPRTDPD
**Dependente do Trabalhador**

**PK:** `NUDPD`, `NUPRT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUDPD` 🔑 | Inteiro | Nro. Unico |  |
| `NUPRT` 🔑 | Inteiro | Nro. Unico Processo | → `TFPPRT`.`NUPRT` |
| `TIPODPD` | Inteiro | Tipo de Dependente |  |
| `CPFDPD` | Texto | CPF do Dependente |  |
| `NOMEDPD` | Texto | Nome do Dependente |  |
| `DESCDPD` | Texto | Descrição da Dependencia |  |
| `DTNASC` | Data/Hora | Data de nascimento |  |
| `DEPENDIRF` | Texto | E Dependente IRRF |  |
| `IDADEESCOLAR` | Texto | Idade Escolar |  |
| `DTLIMIRF` | Data/Hora | Data limite IRRF |  |

**Opções `DEPENDIRF`:** `S`=Sim, `N`=Não

**Opções `IDADEESCOLAR`:** `N`=Não, `S`=Sim

**Opções `TIPODPD`:** `3`=Filho(a) ou enteado(a), `4`=Filho(a) ou enteado(a), universitario(a) ou cursando escola tecnica de 2 grau, `6`=Irmão(), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial, `7`=Irmão(), neto(a) ou bisneto(a) sem arrimo dos pais, universitario(a) ou cursando escola tecnica, `9`=Pais, avos e bisavos, `99`=Agregado/Outros, `2`=Companheiro(a) com o(a) qual tenha filho ou viva ha mais de 5 (cinco) anos, `12`=Ex-conjuge, `11`=A pessoa absolutamente incapaz, da qual seja tutor ou curador, `1`=Conjuge, `10`=Menor pobre do qual detenha a guarda judicial

### TFPPRTIBC
**Informações Base de Calculo**

**PK:** `NUIBC`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUIBC` 🔑 | Inteiro | Nro. Unico |  |
| `NUICT` | Inteiro | Nro. Unico Info. Contrato Trabalho | → `TFPPRTICT`.`NUICT` |
| `DTREF` | Data | Periodo |  |
| `VLRBASECONTPREV` | Decimal | Base de calculo da contribuição previdenciaria - Remuneração |  |
| `VLRBASECONTPREV13` | Decimal | Base de calculo da contribuição previdenciaria - 13 salario |  |
| `VLRBASECALCFGTS` | Decimal | Base de calculo do FGTS - Remuneração |  |
| `VLRBASECALCFGTS13` | Decimal | Base de calculo do FGTS - 13 salario |  |
| `GRAUEXPAGNOC` | Inteiro | Grau de exposição aos agentes nocivos |  |
| `VLRBASECALCGUIAFGTS` | Decimal | Base de calculo guia do FGTS - Remuneração |  |
| `VLRBASECALCGUIAFGTS13` | Decimal | Base de calculo guia do FGTS - 13 salario |  |
| `FGTSPAGOTRAB` | Texto | FGTS transacionado pago diretamente ao trabalhador |  |
| `CODCATEG` | Inteiro | Codigo categoria do trabalhador |  |
| `VLRREMUNPREVGFIP` | Decimal | Valor da remuneração para fins previdenciarios declarada em GFIP ou em S-1200 |  |
| `VRBCFGTSPROCTRAB` | Decimal | FGTS não declarado em SEFIP/eSocial reconhecido no proc. trabalhista |  |
| `VRBCFGTSSEFIP` | Decimal | FGTS declarado apenas em SEFIP (não em eSocial) e não recolhido |  |
| `VRBCFGTSDECANT` | Decimal | FGTS declarado anteriormente no eSocial e não recolhido |  |

**Opções `FGTSPAGOTRAB`:** `N`=Não, `S`=Sim

**Opções `GRAUEXPAGNOC`:** `1`=Não ensejador de aposentadoria especial, `2`=Ensejador de aposentadoria especial - FAE15_12% (15 anos de contribuição e aliquota de 12%), `3`=Ensejador de aposentadoria especial - FAE20_09% (20 anos de contribuição e aliquota de 9%), `4`=Ensejador de aposentadoria especial - FAE25_06% (25 anos de contribuição e aliquota de 6%)

### TFPPRTICT
**Informações do Contrato de Trabalho**

**PK:** `NUICT`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUICT` 🔑 | Inteiro | Nro. Unico |  |
| `NUPRT` | Inteiro | Nro. Unico Processo | → `TFPPRT`.`NUPRT` |
| `TIPOCONTRATO` | Inteiro | Tipo de Contrato |  |
| `INFOCONTENVESOCIAL` | Texto | Informações sobre o contrato de trabalho enviados ao eSocial |  |
| `DTDEMJUD` | Data | Data desligamento (Decisão Judicial) |  |
| `DTADMJUD` | Data | Data admissão (Decisão Judicial) |  |
| `DTADMORIG` | Data | Data admissão original |  |
| `HOUVEREINT` | Texto | Houve reintegração |  |
| `HOUVERECCATEG` | Texto | Houve reconhecimento de categoria do trabalhador diferente do eSocial/GFIP |  |
| `HOUVERECNATATIV` | Texto | Houve reconhecimento de natureza de atividade diferente da informada pelo declarante |  |
| `HOUVERECMOTDESLIG` | Texto | Houve reconhecimento de motivo de desligamento diferente da informada pelo declarante |  |
| `CODTPRJUD` | Inteiro | Tipo de Rescisão (Decisão Judicial) |  |
| `HOUVERECUNCONTR` | Texto | Houve reconhecimento de unicidade contratual |  |
| `MATRICULATRAB` | Texto | Matricula do trabalhador |  |
| `CODCATEGTRABJUD` | Inteiro | Codigo de categoria do trabalhador (Decisão judicial) |  |
| `CODCATEGTRAB` | Inteiro | Codigo de categoria do trabalhador |  |
| `DTINICIOTSVE` | Data | Data de inicio do TSVE |  |
| `CODCBO` | Inteiro | CBO |  |
| `CODNATATIVIDADEJUD` | Texto | Natureza da atividade (Decisão Judicial) |  |
| `CODNATATIVIDADE` | Inteiro | Natureza da atividade |  |
| `TIPOREGTRAB` | Inteiro | Tipo de regime trabalhista |  |
| `DTADM` | Data | Data de admissão |  |
| `TIPOREGPREV` | Inteiro | Tipo de regime previdenciario |  |
| `TIPOCONTRPARC` | Inteiro | Tipo de contrato em tempo parcial |  |
| `TIPOCONTRTRAB` | Inteiro | Tipo de contrato de trabalho |  |
| `DTTERMCONTR` | Data | Data de termino (prazo determinado) |  |
| `CONTRPRAZOTERM` | Texto | Contrato por prazo determinado com clausula assecuratoria |  |
| `OBJDETCONTRTERM` | Texto | Objeto determinante da contratação por prazo determinado |  |
| `OBSCONTRTRAB` | Texto | Observações do contrato de trabalho |  |
| `TIPOINSC` | Inteiro | Tipo de inscrição |  |
| `NROINSC` | Texto | Numero de inscrição |  |
| `CODMATRICULAANT` | Texto | Matricula anterior |  |
| `DTTRANSF` | Data | Data de transferencia |  |
| `DTDESLIG` | Data | Data de desligamento |  |
| `MTVDESLIG` | Texto | Motivo de desligamento |  |
| `PENSALIM` | Texto | Indicativo de pensão alimenticia para fins de retenção de FGTS |  |
| `PERCALIMENT` | Decimal | Percentual a ser destinado a pensão alimenticia |  |
| `VRALIM` | Decimal | Valor da pensão alimenticia |  |
| `DTFIMAVISOPREV` | Data | Data fim do Aviso Previo Indenizado |  |
| `DTTERM` | Data | Data de termino |  |
| *... +19 campos adicionais* | | | |

**Opções `CODNATATIVIDADE`:** `1`=Trabalho urbano, `2`=Trabalho rural

**Opções `CODNATATIVIDADEJUD`:** `2`=Trabalho rural, `1`=Trabalho urbano

**Opções `CONTRPRAZOTERM`:** `N`=Não, `S`=Sim

**Opções `HOUVERECCATEG`:** `N`=Não, `S`=Sim

**Opções `HOUVERECMOTDESLIG`:** `N`=Não, `S`=Sim

**Opções `HOUVERECNATATIV`:** `N`=Não, `S`=Sim

### TFPPRTINTERM
**Informações relativas ao trabalho intermitente**

**PK:** `NUINTERM`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUINTERM` 🔑 | Inteiro | Numero unico do Intermitente |  |
| `NUIBC` | Inteiro | Numero unico da Base de Calculo | → `TFPPRTIBC`.`NUIBC` |
| `DIA` | Inteiro | Dia |  |
| `HORASTRAB` | Texto | Horas trabalhadas |  |

### TFPPRTIVI
**Informações Vinculos/Contratos Incorporados do Trabalhador**

**PK:** `NUIVI`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUIVI` 🔑 | Inteiro | Nro. Unico |  |
| `NUICT` | Inteiro | Nro. Unico Info. Contrato Trabalho | → `TFPPRTICT`.`NUICT` |
| `CODMATINC` | Texto | Matricula Incorporada |  |
| `CODCATEG` | Inteiro | Codigo categoria do trabalhador |  |
| `DTINITSVE` | Data | Data de inicio (TSVE) |  |

### TFPPRTMCA
**Mudanca Categoria do Trabalhador**

**PK:** `NUMCA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUMCA` 🔑 | Inteiro | Nro. Unico |  |
| `NUICT` | Inteiro | Nro. Unico Info. Contrato Trabalho | → `TFPPRTICT`.`NUICT` |
| `CODCATEG` | Inteiro | Codigo categoria do trabalhador |  |
| `NATATIVIDADE` | Inteiro | Natureza da atividade |  |
| `DTINIMUDCATEG` | Data | Data inicio da categoria ou natureza |  |

**Opções `NATATIVIDADE`:** `1`=Trabalho urbano, `2`=Trabalho rural

### TFPPRTR
**TABLE TFPPRTR**

**PK:** `NROUNICO`, `CPFPROF`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NROUNICO` 🔑 | Inteiro | NROUNICO | → `TFPTREI`.`NROUNICO` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CPFPROF` 🔑 | Texto | CPF | → `TFPPROF`.`CPFPROF` |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPPRTREM
**Remunerações do Trabalhador**

**PK:** `NUREM`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUREM` 🔑 | Inteiro | Nro. Unico |  |
| `NUICT` | Inteiro | Nro. Unico Info. Contrato Trabalho | → `TFPPRTICT`.`NUICT` |
| `DTINIREMUN` | Data | Data inicio da remuneração |  |
| `VLRSALBASE` | Decimal | Salario base |  |
| `UNDPGTO` | Inteiro | Unidade de pagamento |  |
| `DSCSALVAR` | Texto | Descrição do salario variavel |  |

**Opções `UNDPGTO`:** `1`=Por hora, `2`=Por dia, `3`=Por semana, `7`=Não aplicavel - Salario exclusivamente variavel, `5`=Por mes, `6`=Por tarefa, `4`=Por quinzena

### TFPPRV
**TABLE TFPPRV**

**PK:** `CODPREVIDENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODPREVIDENCIA` 🔑 | Inteiro | Codigo |  |
| `RAZAOSOCIAL` | Texto | Razão Social |  |
| `CNPJ` | Texto | CNPJ |  |
| `LISEVENTOS` | Texto | Evento |  |
| `CODUSU` | Inteiro | Codigo do usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data | Data de alteração |  |

### TFPPSC
**Tabela de Perfil por cargo**

**PK:** `CODCARGO`, `CODPERFIL`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCARGO` 🔑 | Inteiro | Cod.Cargo | → `TFPCAR`.`CODCARGO` |
| `CODPERFIL` 🔑 | Inteiro | Cod.Perfil | → `TFPPER`.`CODPERFIL` |

### TFPPSF
**TABLE TFPPSF**

**PK:** `CODEMP`, `CODFUNC`, `NUPROCESSO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `NUPROCESSO` 🔑 | Inteiro | Codigo do Processo | → `TFPPSS`.`NUPROCESSO` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPPSS
**TABLE TFPPSS**

**PK:** `NUPROCESSO`  
**Referenciada por:** 17 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPROCESSO` 🔑 | Inteiro | Numero unico |  |
| `ABRANPROCESSO` | Inteiro | Identificação do Processo |  |
| `TIPOPROCESSO` | Texto | Tipo |  |
| `ATIVO` | Texto | Ativo |  |
| `INDAUTORIA` | Inteiro | Autor da Ação |  |
| `NUMPROCESSO` | Texto | Numero do Processo |  |
| `DESCRPROCESSO` | Texto | Descrição |  |
| `IDVARA` | Inteiro | Codigo da Vara |  |
| `INDMATPROC` | Inteiro | Materia do Processo ou Alvara Judicial (E-Social) |  |
| `RECIBOESOCIAL` | Texto | Nro. recibo eSocial |  |
| `DTINICIO` | Data/Hora | DTINICIO |  |
| `DTFIM` | Data/Hora | DTFIM |  |
| `DTDESCISAO` | Data | Data Decisão |  |
| `DCCONTRPATR` | Texto | Contrib. Patronais |  |
| `DCCONTRPATRSEG` | Texto | Contrib. Patronais - Segurados |  |
| `DCNFSERVTOMADO` | Texto | DCNFSERVTOMADO |  |
| `DCNFSERVPRESTADO` | Texto | DCNFSERVPRESTADO |  |
| `INDDESCISAO` | Inteiro | INDDESCISAO |  |
| `INDDEPINTEGRAL` | Texto | Deposito de Montante Integral |  |
| `CODCIDSECAOJUD` | Inteiro | Municipio | → `TSICID`.`CODCID` |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `TIPINSS` | Inteiro | INSS |  |
| `TIPIRRF` | Inteiro | TIPIRRF |  |
| `USADOESOCIAL` | Texto | USADOESOCIAL |  |
| `TPTRIB` | Inteiro | TPTRIB |  |
| `EXCLUSIVOEMP` | Texto | Exclusivo do Empregador |  |
| `USALIMITESALMIN` | Texto | Contribuição a Outras Entidades limitada a base de 20 salarios minimos |  |
| `VLRSALMINIMO` | Decimal | Salario Minimo Vigente |  |
| `INSSEMPRESA` | Texto | INSS Empresa |  |
| `FGTS` | Texto | FGTS |  |
| `CONTRIBSINDICAL` | Texto | Contribuição Sindical |  |
| `INSSTRABALHADOR` | Texto | INSS Retido (Trabalhador) |  |
| `IRRF` | Texto | IRRF |  |
| `PISPASEP` | Texto | PIS/PASEP |  |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `CONTRIBSINDICAL`:** `N`=Não, `S`=Sim

**Opções `DCCONTRPATR`:** `S`=Sim, `N`=Não

**Opções `DCCONTRPATRSEG`:** `S`=Sim, `N`=Não

**Opções `EXCLUSIVOEMP`:** `S`=Sim, `N`=Não

**Opções `FGTS`:** `N`=Não, `S`=Sim

### TFPPTANP
**Pagamento de Trabalhador Avulso Não Portuario**

**PK:** `NUPTANP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPTANP` 🔑 | Inteiro | Nro. Unico |  |
| `CODEMP` | Inteiro | Codigo da Empresa |  |
| `DTREF` | Data | Data de Referencia |  |
| `VLRBASEREMUN` | Decimal | Base Remuneração |  |
| `VLRBASEREMUN13` | Decimal | Base 13 Salario |  |
| `VLRBASEFGTS` | Decimal | Base Calculo FGTS |  |
| `VLRTOTDESCINSS` | Decimal | Total Descontos INSS |  |
| `VLRBASEAPOS15` | Decimal | Base Apos 15 Anos |  |
| `VLRBASEAPOS20` | Decimal | Base Apos 20 Anos |  |
| `VLRBASEAPOS25` | Decimal | Base Apos 25 Anos |  |

### TFPPTPR
**TABLE TFPPTPR**

**PK:** `NUPROCESSO`, `CODEMP`  
**Referenciada por:** 4 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPROCESSO` 🔑 | Inteiro | NUPROCESSO | → `TFPPSS`.`NUPROCESSO` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPPUB
**Dados Funcionarios Publicos**

**PK:** `CODEMP`, `CODFUNC`  
**Referenciada por:** 6 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CATEGORIA` | Texto | Categoria |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `CEDIDOREQ` | Texto | Cedido ou requisitado |  |
| `CLT_ESTAT` | Texto | CLT ou estatutario |  |
| `CODDEC_1` | Inteiro | Decimo 1 |  |
| `CODDEC_10` | Inteiro | Decimo 10 |  |
| `CODDEC_2` | Inteiro | Decimo 2 |  |
| `CODDEC_3` | Inteiro | Decimo 3 |  |
| `CODDEC_4` | Inteiro | Decimo 4 |  |
| `CODDEC_5` | Inteiro | Decimo 5 |  |
| `CODDEC_6` | Inteiro | Decimo 6 |  |
| `CODDEC_7` | Inteiro | Decimo 7 |  |
| `CODDEC_8` | Inteiro | Decimo 8 |  |
| `CODDEC_9` | Inteiro | Decimo 9 |  |
| `CODDEP` | Inteiro | Departamento de origem | → `TFPDEP`.`CODDEP` |
| `CODDIV` | Inteiro | Divisão | → `TFPDIV`.`CODDIV` |
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `CODGRAT` | Inteiro | Gratificação | → `TFPGRA`.`CODGRAT` |
| `CODNIVELREF` | Inteiro | Nivel de referencia | → `TFPNIV`.`CODNIVELREF` |
| `CODORGAO` | Inteiro | Orgão | → `TFPORG`.`CODORGAO` |
| `CODORGORIGGRAT` | Inteiro | Orgão de origem da gratificação | → `TFPORG`.`CODORGAO` |
| `CODSITESTAT` | Inteiro | Situação estatutario | → `TFPSIT`.`CODSITESTAT` |
| `DEPENDACIMA65A` | Inteiro | Dependentes acima de 65 A |  |
| `DEPENDACIMA65B` | Inteiro | Dependentes acima de 65 B |  |
| `DEPENDCONVMED` | Inteiro | DEPENDCONVMED calculado |  |
| `DTAPOSENTADORIA` | Data/Hora | Data da aposentadoria |  |
| `DTDESIGNACAO` | Data/Hora | Data da designação |  |
| `DTEXERC` | Data/Hora | Data do exercicio |  |
| `DTINICREQ` | Data/Hora | Inicio da requisição |  |
| `DTPOSSE` | Data/Hora | Data da posse |  |
| `DTREDIST` | Data/Hora | Data da redistribuição |  |
| `DTTERMREQ` | Data/Hora | Termino da requisição |  |
| `DTVACANCIA` | Data/Hora | Data da vacancia |  |
| `FIMREQ` | Texto | Fim da requisição |  |
| `INDDEC_1` | Decimal | Indice de Decimos |  |
| `INDDEC_10` | Decimal | Indice de Decimos10 |  |
| `INDDEC_2` | Decimal | Indice de Decimos2 |  |
| `INDDEC_3` | Decimal | Indice de Decimos3 |  |
| `INDDEC_4` | Decimal | Indice de Decimos4 |  |
| `INDDEC_5` | Decimal | Indice de Decimos5 |  |
| *... +13 campos adicionais* | | | |

**Opções `ATIVO`:** `S`=Sim, `N`=Não

**Opções `CATEGORIA`:** `S`=Servidor, `J`=Juiz

**Opções `CEDIDOREQ`:** `L`=Lotado, `C`=Cedido, `R`=Requisitado

**Opções `CLT_ESTAT`:** `E`=Estatuario, `C`=CLT

**Opções `FIMREQ`:** `S`=Sim, `N`=Não

**Opções `OPCAOGRAT`:** `N`=Não, `S`=Sim

### TFPRCT
**Receita Reclamatoria Trabalhista**

**PK:** `CODRECEITA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODRECEITA` 🔑 | Inteiro | Codigo da Receita |  |
| `DESCRECEITA` | Texto | Descrição |  |
| `ALIQUOTA` | Texto | Aliquota |  |
| `TPRECEITA` | Texto | Tipo |  |

**Opções `TPRECEITA`:** `2`=Redimento Tributavel, `1`=Previdenciaria/Outras Bases

### TFPRDEF
**Dados das deficiencias dos funcionarios na requisição de admissão**

**PK:** `IDREQADM`, `TIPODEFICIENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `IDREQADM` 🔑 | Inteiro | Identificador da requisição de admissão | → `TFPREQADM`.`ID` |
| `TIPODEFICIENCIA` 🔑 | Inteiro | Deficiencia |  |

**Opções `TIPODEFICIENCIA`:** `5`=Intelectual, `6`=Reabilitado, `4`=Mental, `2`=Visual, `3`=Auditiva, `1`=Fisica

### TFPREGCALC
**Nova Tabela de Regras para Calculo**

**PK:** `CODREGCALC`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ABATEACRESCCRED` | Texto | ABATEACRESCCRED |  |
| `PER13SRESC` | Texto | PER13SRESC |  |
| `PERFERRESC` | Texto | PERFERRESC |  |
| `QTDULTMESPER13S2` | Inteiro | QTDULTMESPER13S2 |  |
| `QTDULTMESPER13S3` | Inteiro | QTDULTMESPER13S3 |  |
| `QTDULTMESPERFER2` | Inteiro | QTDULTMESPERFER2 |  |
| `QTDULTMESPERFER3` | Inteiro | QTDULTMESPERFER3 |  |
| `QTDULTMESPERRESC2` | Inteiro | QTDULTMESPERRESC2 |  |
| `QTDULTMESPERRESC3` | Inteiro | QTDULTMESPERRESC3 |  |
| `QTDULTMESRESD` | Inteiro | QTDULTMESRESD |  |
| `QTDULTMESRESD2` | Inteiro | QTDULTMESRESD2 |  |
| `QTDULTMESRESD3` | Inteiro | QTDULTMESRESD3 |  |
| `QTDULTMESRESF` | Inteiro | QTDULTMESRESF |  |
| `QTDULTMESRESF2` | Inteiro | QTDULTMESRESF2 |  |
| `QTDULTMESRESF3` | Inteiro | QTDULTMESRESF3 |  |
| `TIPODIVD13SRESC` | Texto | TIPODIVD13SRESC |  |
| `ABATEFERDIVD` | Texto | ABATEFERDIVD |  |
| `ABATEFERDIVS` | Texto | ABATEFERDIVS |  |
| `CODREGCALC` 🔑 | Inteiro | Codigo |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `CONSIDERAMEDIAPROV` | Texto | CODUSU |  |
| `DESCRICAO` | Texto | DESCRICAO |  |
| `DOISPER13S` | Texto | DOISPER13S |  |
| `DOISPERFER` | Texto | DOISPERFER |  |
| `DOISPERRESC` | Texto | DOISPERRESC |  |
| `MAIORVALQTD13S` | Inteiro | MAIORVALQTD13S |  |
| `MAIORVALQTDFER` | Inteiro | MAIORVALQTDFER |  |
| `MAIORVALQTDRESC` | Inteiro | MAIORVALQTDRESC |  |
| `MOVMEDIAS` | Texto | MOVMEDIAS |  |
| `PER13S` | Texto | PER13S |  |
| `PERFER` | Texto | PERFER |  |
| `PERRESC` | Texto | PERRESC |  |
| `QTDULTMESPER13S` | Inteiro | QTDULTMESPER13S |  |
| `QTDULTMESPERFER` | Inteiro | QTDULTMESPERFER |  |
| `QTDULTMESPERRESC` | Inteiro | QTDULTMESPERRESC |  |
| `RESPFOLHA` | Texto | RESPFOLHA |  |
| `TIPODIVD13S` | Texto | TIPODIVD13S |  |
| `TIPODIVDFER` | Texto | TIPODIVDFER |  |
| `TIPODIVDRESC` | Texto | TIPODIVDRESC |  |
| `TIPODIVS13S` | Texto | TIPODIVS13S |  |
| *... +175 campos adicionais* | | | |

**Opções `BATIDAEXCECAO`:** `S`=Sim, `N`=Não

**Opções `FERIASABONO`:** `N`=Não, `S`=Sim

**Opções `SUSPCONTDEC`:** `N`=Não, `S`=Sim

**Opções `SUSPCONTFER`:** `S`=Sim, `N`=Não

### TFPREI
**Reintegração de funcionarios**

**PK:** `CODREINT`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODREINT` 🔑 | Inteiro | Codigo |  |
| `CODEMP` | Inteiro | Empresa |  |
| `CODFUNC` | Inteiro | Funcionario |  |
| `TPREINT` | Inteiro | Tipo de Reintegração |  |
| `PROCJUD` | Texto | Numero do Processo Judicial |  |
| `LEIANISTIA` | Inteiro | Lei de Anistia |  |
| `DTEFETRETORNO` | Data | Data do Efetivo Retorno |  |
| `DTEFEITO` | Data | Data do Efeito |  |
| `INDPAGTOJUIZO` | Texto | Pagamento das remunerações e contribuições em juizo |  |
| `CODHISTOCOR` | Inteiro | Historico de Ocorrencia |  |
| `CODUSU` | Inteiro | CODUSU |  |
| `DHALTER` | Data/Hora | DHALTER |  |

**Opções `INDPAGTOJUIZO`:** `N`=Não, `S`=Sim

**Opções `LEIANISTIA`:** `4`=4 - LEI 10.559/2002, `3`=3 - LEI 8.878/1994, `5`=5 - LEI 10.790/2003, `6`=6 - LEI 11.282/2006, `2`=2 - LEI 8.632/1993, `1`=1 - LEI 6.683/1979

**Opções `TPREINT`:** `9`=9 - Outros, `5`=5 - Reinclusão de Militar, `4`=4 - Recondução de Servidor Publico, `3`=3 - Resersão de Servidor Publico, `2`=2 - Reintegração por Anistia Legal, `1`=1 - Reintegração por Decisão Judicial

### TFPREQ
**Tabela das requisições**

**PK:** `ID`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `DTCRIACAO` | Data/Hora | DTCRIACAO |  |
| `CODFUNC` | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `CODEMP` | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `STATUS` | Inteiro | STATUS |  |
| `PRIORIDADE` | Inteiro | PRIORIDADE |  |
| `DTLIMITE` | Data/Hora | DTLIMITE |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `ORIGEMTIPO` | Texto | ORIGEMTIPO |  |
| `ORIGEMID` | Inteiro | ORIGEMID |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

### TFPREQACS
**Requisição de alteração de cargo e salario**

**PK:** `ID`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ID` 🔑 | Inteiro | ID |  |
| `CODEMP` | Inteiro | Codigo da Empresa do Funcionario |  |
| `CODFUNC` | Inteiro | Codigo do Funcionario |  |
| `DHSOLICIT` | Data/Hora | Data e Hora da Solicitação |  |
| `STATUS` | Texto | Status |  |
| `CARGO` | Inteiro | Codigo do Cargo do Funcionario |  |
| `CARGOANTIGO` | Inteiro | Codigo antigo do Cargo do Funcionario |  |
| `CODHISTOCORCAR` | Inteiro | Codigo Historico Ocorrencia Cargo |  |
| `DESCRHISTOCORCAR` | Texto | Descrição Historico Ocorrencia Cargo |  |
| `SALARIO` | Decimal | Salario |  |
| `SALARIOANTIGO` | Decimal | Salario Antigo |  |
| `CODHISTOCORSAL` | Inteiro | Codigo Historico Ocorrencia Salario |  |
| `DESCRHISTOCORSAL` | Texto | Descrição Historico Ocorrencia Salario |  |
| `DTEFETIVACAO` | Data/Hora | Data de Efetivação |  |
| `EFETIVADO` | Texto | Efetivado |  |
| `FUNCAO` | Inteiro | Codigo da Função do Funcionario | → `TFPFCO`.`CODFUNCAO` |
| `FUNCAOANTIGA` | Inteiro | Codigo da Função Antiga do Funcionario | → `TFPFCO`.`CODFUNCAO` |
| `CODHISTOCORFUN` | Inteiro | Codigo Historico Ocorrencia Função |  |
| `DESCRHISTOCORFUN` | Texto | Descrição Historico Ocorrencia Função |  |

### TFPREQADM
**Requisição de admissão**

**PK:** `ID`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` | Inteiro | Codigo da Empresa do Funcionario | → `TSIEMP`.`CODEMP` |
| `CODDEP` | Inteiro | Codigo do Departamento | → `TFPDEP`.`CODDEP` |
| `CODCARGO` | Inteiro | Codigo do Cargo do Funcionario | → `TFPCAR`.`CODCARGO` |
| `DTADM` | Data | Data da Admissão do Funcionario |  |
| `SALBASE` | Decimal | Salario Base do Funcionario |  |
| `NOMEFUNC` | Texto | Nome do Funcionario |  |
| `CPF` | Texto | CPF do Funcionario |  |
| `EMAIL` | Texto | Email pessoal do Funcionario |  |
| `OBSERVACAO` | Texto | Observação Livre |  |
| `ID` 🔑 | Inteiro | ID |  |
| `TMPRESIDTRABESTRANG` | Texto | Tempo de Residencia do Trabalhador Estrangeiro |  |
| `FILHOSBR` | Texto | Filhos no Brasil |  |
| `CASADOBR` | Texto | Casado no Brasil |  |
| `CATEGORIACNH` | Texto | Categoria CNH |  |
| `CELULAR` | Texto | Celular |  |
| `CEP` | Texto | Cep |  |
| `CIDNASC` | Inteiro | Cidade Nascimento |  |
| `CLASSTRABESTRANG` | Inteiro | Classificação de trabalhadores estrangeiros |  |
| `CODADMFGTS` | Texto | Tabela de Ocorrencia FGTS |  |
| `CODADMFGTSII` | Texto | Tabela de Categoria FGTS |  |
| `CODAGE` | Inteiro | Codigo da agencia |  |
| `CODBAI` | Inteiro | Codigo do bairro | → `TSIBAI`.`CODBAI` |
| `CODBCO` | Inteiro | Codigo do banco |  |
| `CODCARGAHOR` | Inteiro | Codigo de identificação da carga horaria | → `TFPCGH`.`CODCARGAHOR` |
| `CODCATEG` | Inteiro | Codigo da categoria | → `TFPCAT`.`CODCATEG` |
| `CODCATEGESOCIAL` | Inteiro | Codigo de Categoria eSocial | → `TFPCTG`.`CODCATEGESOCIAL` |
| `CODCID` | Inteiro | Codigo da cidade | → `TSICID`.`CODCID` |
| `CODCIDTRAB` | Inteiro | Codigo da cidade de trabalho | → `TSICID`.`CODCID` |
| `CODCTABCO` | Inteiro | Numero da conta bancaria |  |
| `CODEND` | Inteiro | Codigo do endereco | → `TSIEND`.`CODEND` |
| `CODFUNCAO` | Inteiro | Codigo da função | → `TFPFCO`.`CODFUNCAO` |
| `CODGRUPOCTBZ` | Inteiro | Codigo do grupo contabil |  |
| `CODPAIS` | Inteiro | Codigo do pais | → `TSIPAI`.`CODPAIS` |
| `CODSIND` | Inteiro | Codigo do sindicato | → `TFPSIN`.`CODSIND` |
| `COMPLEMENTO` | Texto | Complemento do endereco |  |
| `COMPLEMENTORG` | Texto | Complemento RG |  |
| `CTPSDIGITAL` | Texto | CTPS Digital |  |
| `DEFICIENTEFISICO` | Texto | Deficiente fisico |  |
| `DISPPEREXP` | Texto | Dispensa periodo de experiencia |  |
| `DTCHEGPAIS` | Data | Data de chegada ao pais |  |
| *... +86 campos adicionais* | | | |

**Opções `CADINI`:** `N`=Não, `S`=Sim

**Opções `CASADOBR`:** `N`=Não, `S`=Sim

**Opções `CLASSTRABESTRANG`:** `4`=4 - Beneficiado pelo acordo entre paises do Mercosul, `5`=5- Dependente de agente diplomatico e/ou consular com acordo de reciprocidade e atividade remunerada, `6`=6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre o Brasil e Portugal, `3`=3 - Permanencia no Brasil em razão de reunião familiar, `7`=7 - Outra condição, `2`=2 - Solicitante de refugio, `1`=1 - Refugiado

**Opções `CODADMFGTS`:** `02`=Exposição a agente nocivo (aposentadoria aos 15), `01`=Não exposição a agente nocivo, mas ja esteve, `06`=Exposição a agente nocivo (apos. aos 15) mult.vinculo, `07`=Exposição a agente nocivo (apos. aos 20) mult.vinculo, `05`=Não exposição a agente nocivo ja esteve mult.vinculo, `00`=Não exposição a agente nocivo, `03`=Exposição a agente nocivo (aposentadoria aos 20), `04`=Exposição a agente nocivo (aposentadoria aos 25), `08`=Exposição a agente nocivo (apos. aos 25) mult.vinculo

**Opções `CTPSDIGITAL`:** `N`=Não, `S`=Sim

**Opções `DEFICIENTEFISICO`:** `S`=Sim, `N`=Não

### TFPREQADMDPD
**Dependente da Requisição de Admissão**

**PK:** `IDREQADM`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `ADOTIVO` | Texto | Filho Adotivo |  |
| `AUXCRE` | Texto | Tem Auxilio Creche |  |
| `CODEMPFUNCRESPONSAVEL` | Inteiro | Codigo de empresa do funcionario responsavel | → `TFPEMP`.`CODEMP` |
| `CONVENIO` | Texto | Dependente de Convenio Medico |  |
| `CPF` | Texto | CPF |  |
| `CPFFUNCRESPONSAVEL` | Texto | CPF do responsavel |  |
| `DEPENDIRF` | Texto | Dependente de IRRF |  |
| `DESCRDPD` | Texto | Descrição da Dependencia |  |
| `DTNASC` | Data | Data de nascimento |  |
| `GRAUPARENT` | Inteiro | Grau de parentesco |  |
| `IDADEESCOLAR` | Texto | Em idade escolar |  |
| `IDREQADM` 🔑 | Inteiro | Codigo da requisição de admissão |  |
| `INCTRAB` | Texto | Possui Incapacidade Fisica ou Mental para o Trabalho |  |
| `NOME` | Texto | Nome |  |
| `NOMEMAE` | Texto | Nome da Mõe |  |
| `PENSIONISTA` | Texto | Pensionista |  |
| `PERCPENSAO` | Decimal | Percentual da Pensão |  |
| `RACAETNIA` | Inteiro | Raca/Etnia |  |
| `REPSALPENSIONISTA` | Texto | Repassa Salario Familia ao Pensionista |  |
| `SALFAM` | Texto | Dependente de Salario familia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `SEXO` | Texto | Sexo |  |
| `VLRPENSAO` | Decimal | Valor da Pensão |  |
| `CARTORIO` | Texto | Nome do cartorio |  |
| `CODCID` | Inteiro | Naturalidade |  |
| `CODFUNCPENS` | Inteiro | Codigo do Pensionista |  |
| `CODPARC` | Inteiro | Parceiro Responsavel pelo recebimento da Pensão |  |
| `DNV` | Texto | DNV |  |
| `DTFIMDEPEND` | Data | Data Final da Dependencia |  |
| `DTINICDEPEND` | Data | Data Inicial da Dependencia |  |
| `DTLIMAUXCRE` | Data | Data Limite do Auxilio Creche |  |
| `DTLIMIRF` | Data | Data limite do IRRF |  |
| `DTLIMSALFAM` | Data | Data Limite do Salario Familia |  |
| `MOTIVOFIM` | Inteiro | Motivo do Fim da Dependencia |  |
| `MOTIVOINICIO` | Inteiro | Motivo do Inicio da Dependencia |  |
| `NACIONALIDADE` | Inteiro | Nacionalidade |  |
| `NROFOLHAREG` | Inteiro | Numero da Folha do Livro de Registro |  |
| `NROLIVROREG` | Texto | Numero do Livro de Registro |  |
| `NROREG` | Texto | Numero do Registro |  |
| `PERCHNETFGTS` | Decimal | Percentual do FGTS |  |
| *... +5 campos adicionais* | | | |

**Opções `ADOTIVO`:** `N`=Não, `S`=Sim

**Opções `AUXCRE`:** `S`=Sim, `N`=Não

**Opções `CONVENIO`:** `N`=Não, `S`=Sim

**Opções `DEPENDIRF`:** `S`=Sim, `N`=Não

**Opções `IDADEESCOLAR`:** `S`=Sim, `N`=Não

**Opções `INCTRAB`:** `S`=Sim, `N`=Não

### TFPRGPR
**TABLE TFPRGPR**

**PK:** `CODREGPRELIMINAR`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODREGPRELIMINAR` 🔑 | Inteiro | Codigo |  |
| `CODEMP` | Inteiro | Empresa | → `TFPEMP`.`CODEMP` |
| `MATRICULA` | Inteiro | Matricula |  |
| `NOMEFUNC` | Texto | Nome do Funcionario |  |
| `CPF` | Texto | CPF |  |
| `DTADM` | Data | Data de Admissão |  |
| `DTNASC` | Data | Data de Nascimento |  |
| `VINCULO` | Inteiro | Vinculo |  |
| `CODCATEGESOCIAL` | Inteiro | Codigo de Categoria para o eSocial |  |
| `CODFCO` | Inteiro | Codigo de Função do Funcionario |  |
| `CODCAR` | Inteiro | Codigo do Cargo do Funcionario |  |
| `DTTERMINO` | Data | Data Termino Contrato |  |
| `NATATIVIDADE` | Texto | Natureza da Atividade |  |
| `TIPSAL` | Texto | Tipo de salario |  |
| `SALBASE` | Decimal | Salario base |  |
| `SALPROFESSOR` | Decimal | Salario Professor |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODFUNC` | Inteiro | Codigo do funcionario |  |

**Opções `NATATIVIDADE`:** `U`=Urbano, `P`=Rural

**Opções `TIPSAL`:** `1`=Mensal, `2`=Quinzenal, `3`=Semanal, `4`=Diarista, `5`=Horista, `6`=Tarefa

### TFPRNE
**Processos- Tributos (S-1210)**

**PK:** `NURNE`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NURNE` 🔑 | Inteiro | No. unico Retenção |  |
| `NUPROCESSO` | Inteiro | Nro. unico processo | → `TFPPSS`.`NUPROCESSO` |
| `CODEMP` | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `DTPAGAMENTO` | Data | Data de Pagamento |  |
| `REFERENCIA` | Data | Referencia |  |
| `INDAPURACAO` | Texto | Indicativo de periodo de apuração |  |
| `VLRNAORETIDO` | Decimal | Imposto de Renda não retido |  |
| `VLRDEPJUD` | Decimal | Deposito Judicial |  |
| `VLRCMPANOCAL` | Decimal | Compensação Ano Atual |  |
| `VLRCMPANOANT` | Decimal | Compensação Anos Anteriores |  |
| `VLRRENDSUSP` | Decimal | Rendimento com exigibilidade suspensa |  |
| `TIPOPROCESSO` | Texto | Tipo do Processo |  |
| `INDDEPOSITO` | Texto | Deposito de montante integral |  |

**Opções `INDAPURACAO`:** `2`=2 - Anual (13 salario), `1`=1 - Mensal

### TFPROE
**TABLE TFPROE**

**PK:** `CODEMP`, `CODFUNC`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CGCCPF` | Texto | CNPJ / CPF |  |
| `CODCATEG` | Inteiro | Categoria do eSocial |  |
| `CODUSU` | Inteiro | Usuario | → `TSIUSU`.`CODUSU` |
| `DTDEM` | Data | Data do Desligamento |  |

### TFPRRA
**TABLE TFPRRA**

**PK:** `CPFRESP`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CPFRESP` 🔑 | Texto | CPF Responsavel |  |
| `NISRESP` | Texto | NIS Responsavel |  |
| `NMRESP` | Texto | Nome Responsavel |  |
| `IDEOC` | Inteiro | Orgão de Classe |  |
| `DSCOC` | Texto | Descrição do Orgão de Classe |  |
| `NROC` | Texto | Inscrição no Orgão de Classe |  |
| `UFOC` | Texto | UF Orgão de Classe |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

**Opções `IDEOC`:** `1`=1 - Conselho Regional de Medicina (CRM), `2`=2 - Conselho Regional de Odontologia (CRO), `3`=3 - Registro do Ministerio da Saude (RMS), `4`=4 - Conselho Regional de Engenharia e Agronomia (CREA), `9`=9 - Outros

### TFPRTE
**Composição Rateio**

**PK:** `CODCRIRATEIO`, `CODEVENTO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODCRIRATEIO` 🔑 | Inteiro | CODCRIRATEIO | → `TFPCRE`.`CODCRIRATEIO` |
| `CODEVENTO` 🔑 | Inteiro | Evento Base |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DTALTER` | Data/Hora | DTALTER |  |

### TFPRTF
**Rateio por Funcionario**

**PK:** `CODEMP`, `CODFUNC`, `CODCENCUS`, `CODPROJ`, `DHALTER`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcinario | → `TFPFUN`.`CODFUNC` |
| `CODCENCUS` 🔑 | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODPROJ` 🔑 | Inteiro | Cod.Projeto | → `TCSPRJ`.`CODPROJ` |
| `DHALTER` 🔑 | Data/Hora | Data e hora da alteração |  |
| `PERCRATEIO` | Decimal | Percentual de Rateio |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TFPRTM
**Rateio na TFPMOV**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `CODEVENTO`, `SEQUENCIA`, `CODCENCUS`, `CODPROJ`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | Referencia |  |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `CODEVENTO` 🔑 | Inteiro | CODEVENTO |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `CODCENCUS` 🔑 | Inteiro | Cod.Centro Resultado | → `TSICUS`.`CODCENCUS` |
| `CODPROJ` 🔑 | Inteiro | CODPROJ | → `TCSPRJ`.`CODPROJ` |
| `PERCRATEIO` | Decimal | PERCRATEIO |  |
| `DTALTER` | Data/Hora | DTALTER |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |

### TFPRUB
**Natureza Rubrica**

**PK:** `CODNATRUBRICA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODNATRUBRICA` 🔑 | Inteiro | CODNATRUBRICA |  |
| `NOMENATRUBRICA` | Texto | NOMENATRUBRICA |  |
| `DESCRNATRUBRICA` | Texto | DESCRNATRUBRICA |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `DTFIMVALIDADERUB` | Data/Hora | Data Fim da Validade da Rubrica |  |

### TFPS1000
**S-1000 - Empregador**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr de Inscrição do Empregador |  |
| `NMRAZAO` | Texto | Razão Social |  |
| `CLASSTRIB` | Texto | Classificação Tributaria |  |
| `NATJURID` | Inteiro | Natureza Juridica do Contribuinte |  |
| `INDCOOP` | Inteiro | Ind. Cooperativa |  |
| `INDCONSTR` | Inteiro | Ind. Construtora |  |
| `INDDESFOLHA` | Inteiro | Ind. Desoneração da Folha |  |
| `INDOPTREGELETRON` | Inteiro | Ind. Opção Registro Eletronico |  |
| `INDENTED` | Texto | Ind. Entidade Educativa |  |
| `INDETT` | Texto | Ind. Emp. Trabalho Temporario |  |
| `NRREGETT` | Texto | Nr. Reg. Empresa de Trabalho |  |
| `IDEMINLEI` | Texto | ID. Ministerio ou Lei |  |
| `NRCERTIF` | Texto | Nr. Certificado |  |
| `DTEMISCERTIF` | Data/Hora | Dt. Emissão do Certificado |  |
| `DTVENCCERTIF` | Data/Hora | Dt. Vencimeto do Certificado |  |
| `NRPROTRENOV` | Texto | Nr. Protocolo de Renovação |  |
| `DTPROTRENOV` | Data/Hora | Dt. Protocolo de Renovação |  |
| `DTDOU` | Data/Hora | Dt. Diario Oficial da União |  |
| `PAGDOU` | Inteiro | Pag. Diario Oficial da União |  |
| `NMCTT` | Texto | Contato na Empresa |  |
| `CPFCTT` | Texto | CPF - Contato |  |
| `FONEFIXO` | Texto | Telefone Fixo |  |
| `EMAIL` | Texto | Email |  |
| `NRSIAFI` | Inteiro | Nr. SIAFI |  |
| `IDEEFR` | Texto | ID. Ente Federativo Responsavel |  |
| `CNPJEFR` | Texto | CNPJ - Ente Federativo Responsavel |  |
| `NMENTE` | Texto | Ente Federativo |  |
| `UF` | Texto | UF |  |
| `CODMUNIC` | Inteiro | Cod. Municipio |  |
| `INDRPPS` | Texto | Ind. Regime Proprio Previdencia Social |  |
| `SUBTETO` | Inteiro | Subteto |  |
| `VRSUBTETO` | Decimal | Vr. Subteto |  |
| `INDACORDOISENMULTA` | Inteiro | Ind. Acordo Isenção de Multa |  |
| `INDSITPJ` | Inteiro | Ind. Situação PJ |  |
| `INDSITPF` | Inteiro | Ind. Situação PF |  |
| `STATUS` | Texto | Status |  |
| *... +7 campos adicionais* | | | |

### TFPS1005
**S-1005 - Estabelecimentos**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `TPINSCESTABELECIMENTO` | Inteiro | Tipo Inscrição do Estabelecimento |  |
| `NRINSCESTABELECIMENTO` | Texto | Nr. Inscrição do Estabelecimento |  |
| `CNAEPREP` | Inteiro | CNAE Preponderante |  |
| `ALIQRAT` | Inteiro | Aliquota do RAT |  |
| `ALIQRAT2` | Inteiro | ALIQRAT2 |  |
| `FAP` | Decimal | Fator Acidentario de Prevenção |  |
| `ALIQRATAJUST` | Decimal | Aliquota do RAT apos ajuste |  |
| `TPPROCRAT` | Inteiro | Tipo Processo RAT |  |
| `NRPROCRAT` | Texto | Nr. Processo RAT |  |
| `CODSUSPRAT` | Inteiro | Cod. Suspensão RAT |  |
| `TPPROCFAP` | Inteiro | Tipo Processo FAP |  |
| `NRPROCFAP` | Texto | Nr. Processo FAP |  |
| `CODSUSPFAP` | Inteiro | Cod. Suspensão FAP |  |
| `TPCAEPF` | Inteiro | Tipo de CAEPF |  |
| `INDSUBSTPATROBRA` | Inteiro | Ind. Substituição Patronal de Obra |  |
| `REGPT` | Inteiro | Registro de Ponto |  |
| `CONTAPR` | Inteiro | Contratação de Aprendiz |  |
| `NUPROCJUDAPR` | Texto | Nr. Processo Judicial Aprendiz |  |
| `CONTENTED` | Texto | Entidade Educativa |  |
| `CONTPCD` | Inteiro | Contratação de PCD |  |
| `NUPROCJUDPCD` | Texto | Nr. Processo Judicial PCD |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente |  |
| `DATACHANGE` | C | Mudanca de Dados |  |

### TFPS1010
**S-1010 - Rubricas**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODRUBR` | Texto | Cod Rubrica |  |
| `IDETABRUBR` | Texto | ID. Rubrica |  |
| `DSCRUBR` | Texto | Descrição da Rubrica |  |
| `NATRUBR` | Inteiro | Natureza das Rubricas |  |
| `TPRUBR` | Inteiro | Tipo de Rubrica |  |
| `CODINCCP` | Texto | Cod. Incidencia CP |  |
| `CODINCIRRF` | Texto | Cod. Incidencia IRRF |  |
| `CODINCFGTS` | Texto | Cod. Incidencia FGTS |  |
| `CODINCSIND` | Texto | Cod. Incidencia Sindical |  |
| `REPDSR` | Texto | Rubrica DSR |  |
| `REP13` | Texto | Rubrica 13 |  |
| `REPFERIAS` | Texto | Rubrica Ferias |  |
| `REPAVISO` | Texto | Rubrica Aviso Previo |  |
| `OBSERVACAO` | Texto | Observações |  |
| `CODEVENTO` | Inteiro | Cod. Evento |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente |  |
| `DATACHANGE` | C | Mudanca de Dados |  |

### TFPS1010_CP
**Rubricas - Contribuição Previdenciaria**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CODEVENTO`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPS1010`.`CODEMP` |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia | → `TFPS1010`.`DTREF` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia | → `TFPS1010`.`SEQUENCIA` |
| `CHAVE` 🔑 | Texto | Chave |  |
| `TPPROCCP` | Inteiro | Tipo Processo CP |  |
| `NRPROCCP` | Texto | Nr. Processo CP |  |
| `EXTDESCISAOCP` | Inteiro | Decisão Extrajudiciaria CP |  |
| `CODSUSPCP` | Inteiro | Cod. Suspensão CP |  |
| `CODEVENTO` 🔑 | Inteiro | Cod. Evento | → `TFPS1010`.`CHAVE` |
| `TPAMB` 🔑 | Texto | Tipo Ambiente | → `TFPS1010`.`TPAMB` |

### TFPS1020
**S-1020 - Lotações Tributarias**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODLOTACAO` | Texto | Cod. Lotação |  |
| `TPLOTACAO` | Texto | Tipo de Lotação |  |
| `TPLOTACAO_2` | Inteiro | Tipo de Lotação 2 |  |
| `TPINSCLOTACAO` | Inteiro | Tipo Inscrição da Lotação |  |
| `NRINSCLOTACAO` | Texto | Inscrição da Lotação |  |
| `FPAS` | Inteiro | Cod Relativo ao FPAS |  |
| `CODTERCS` | Texto | Cod. de Terceiros |  |
| `CODTERCSSUSP` | Texto | Cod. de Terceiros Suspenso |  |
| `TPINSCCONTRAT` | Inteiro | Tipo Inscrição do Contratante |  |
| `NRINSCCONTRAT` | Texto | Nr. Inscrição do Contratante |  |
| `TPINSCPROP` | Inteiro | Tipo Inscrição do Proprietario |  |
| `NRINSCPROP` | Texto | Nr. Inscrição do Proprietario |  |
| `CODREGFIS` | Inteiro | Cod. Registro Fiscal |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `TIPOREGISTRO` | Texto | Tipo do Registro |  |
| `CODIGO` | Inteiro | Codigo |  |
| `DESCRLOTACAO` | Texto | Descrição da Lotação |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente |  |
| `DATACHANGE` | C | Mudanca de Dados |  |

### TFPS1030
**S-1030 - Cargos**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODCARGO` | Texto | Cod Cargo |  |
| `NMCARGO` | Texto | Nome Cargo |  |
| `CODCBO` | Texto | Cod. CBO |  |
| `ACUMCARGO` | Inteiro | Acumulação de Cargos |  |
| `CONTAGEMESP` | Inteiro | Contagem Especial |  |
| `DEDICEXCL` | Texto | Dedicação Exclusiva |  |
| `NRLEI` | Texto | Nr. Lei |  |
| `DTLEI` | Data/Hora | Dt. da Lei |  |
| `SITCARGO` | Inteiro | Situação do Cargo |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo de Ambiente |  |

### TFPS1035
**S-1035 - Carreiras Publicas**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODCARREIRA` | Texto | Cod. da Carreira |  |
| `DSCCARREIRA` | Texto | Descrição da Carreira |  |
| `LEICARR` | Texto | Lei da Carreira |  |
| `DTLEICARR` | Data/Hora | Dt. Lei da Carreira |  |
| `SITCARR` | Inteiro | Situação da Carreira |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo Ambiente |  |

### TFPS1040
**S-1040 - Funções/Cargos em Comissão**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODFUNCAO` | Texto | Cod. da Função |  |
| `DSCFUNCAO` | Texto | Descrição da Função |  |
| `CODCBO` | Texto | Cod CBO |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterios |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo Ambiente |  |

### TFPS1050
**S-1050 - Horarios**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODHORCONTRAT` | Texto | Cod. Horario Contratual |  |
| `HRENTR` | Texto | Hora de Entrada |  |
| `HRSAIDA` | Texto | Hora de Saida |  |
| `DURJORNADA` | Inteiro | Duração da Jornada |  |
| `PERHORFLEXIVEL` | Texto | Permitido Horario Flexivel |  |
| `TPINTERV` | Inteiro | Tipo Intervalo da Jornada |  |
| `DURINTERV` | Inteiro | Duração do Intervalo |  |
| `INIINTERV` | Texto | Inicio do Intervalo |  |
| `TERMINTERV` | Texto | Termino do Intervalo |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CODCARGAHOR` | Inteiro | Cod. Carga Horaria |  |
| `DESCRCARGAHOR` | Texto | Descrição da Carga Horaria |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo Ambiente |  |

### TFPS1060
**S-1060 - Ambientes de Trabalho**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `CODAMB` | Texto | Cod. Ambiente |  |
| `DSCAMB` | Texto | Descrição Ambiente de Trabalho |  |
| `LOCALAMB` | Inteiro | Local do Ambiente |  |
| `TPINSC` | Inteiro | Tipo de Inscrição |  |
| `NRINSC` | Texto | Nr. Inscrição |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo Ambiente |  |

### TFPS1070
**S-1070 - Processos Adm/Jud**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Dt. Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição do Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Nr. de Inscrição do Empregador |  |
| `TPPROC` | Inteiro | Tipo de Processo |  |
| `NRPROC` | Texto | Nr. do Processo |  |
| `INDAUTORIA` | Inteiro | Ind. Autoria da Ação Judicial |  |
| `INDMATPROC` | Inteiro | Ind. Materia do Processo |  |
| `UFVARA` | Texto | ID. UF Seção Judiciaria |  |
| `CODMUNIC` | Inteiro | Cod. Municipio |  |
| `IDVARA` | Texto | ID. Vara |  |
| `STATUS` | Texto | Status |  |
| `NRORECIBO` | Texto | Nr. Recibo |  |
| `NRORECIBO_ANT` | Texto | Nr. Recibo Anterior |  |
| `ACAO` | Texto | Ação |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `CONTROLE` | Texto | Controle |  |
| `TPAMB` 🔑 | Texto | Tipo Ambiente |  |
| `DATACHANGE` | C | Mudanca de Dados |  |

### TFPS1200
**TABLE TFPS1200**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `INDAPURACAO` | Inteiro | INDAPURACAO |  |
| `PERAPUR` | Texto | PERAPUR |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | NRINSC |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `INDMV` | Inteiro | INDMV |  |
| `NMTRAB` | Texto | NMTRAB |  |
| `DTNASCTO` | Data/Hora | DTNASCTO |  |
| `CODCBO` | Texto | CODCBO |  |
| `NATATIVIDADE` | Inteiro | NATATIVIDADE |  |
| `QTDDIASTRAB` | Inteiro | QTDDIASTRAB |  |
| `CNPJEMPREGANT` | Texto | CNPJEMPREGANT |  |
| `MATRICANT` | Texto | MATRICANT |  |
| `DTADM` | Data/Hora | DTADM |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `QTDDIASINTERM` | Inteiro | QTDDIASINTERM |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `TPINSCANT` | Inteiro | TPINSCANT |  |

### TFPS1210
**Pagamentos de Rendimentos do Trabalho**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  
**Referenciada por:** 5 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPAMB` 🔑 | Texto | Ambiente |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `INDAPURACAO` | Inteiro | INDAPURACAO |  |
| `PERAPUR` | Texto | Periodo de apuração |  |
| `TPINSC` | Inteiro | Tipo de inscrição |  |
| `NRINSC` | Texto | Nro. de inscrição |  |
| `CPFBENEF` | Texto | CPF Beneficiario (Trabalhador) |  |
| `VRDEDDEP` | Decimal | VRDEDDEP |  |
| `DESCREVT` | Texto | Descrição do evento |  |
| `STATUS` | Texto | Situação |  |
| `NRORECIBO` | Texto | N Recibo Original |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | Ação |  |
| `CONTROLE` | Texto | Controle |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS1210_ANT
**Pagamentos de Rendimentos do Trabalho - Historico**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`, `DTREFRET`, `SEQUENCIARET`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREFRET` 🔑 | Data/Hora | Referencia Ret |  |
| `DTREF` 🔑 | Data/Hora | Referencia |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `SEQUENCIARET` 🔑 | Inteiro | Sequencia Ret |  |
| `TPAMB` 🔑 | Texto | Ambiente |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `INDAPURACAO` | Inteiro | INDAPURACAO |  |
| `PERAPUR` | Texto | Periodo de apuração |  |
| `TPINSC` | Inteiro | Tipo de inscrição |  |
| `NRINSC` | Texto | Nro. de inscrição |  |
| `CPFBENEF` | Texto | CPF Beneficiario (Trabalhador) |  |
| `VRDEDDEP` | Decimal | VRDEDDEP |  |
| `STATUS` | Texto | Situação |  |
| `DESCREVT` | Texto | Descrição do evento |  |
| `NRORECIBO` | Texto | N Recibo Original |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | Ação |  |
| `CONTROLE` | Texto | Controle |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS1250
**TABLE TFPS1250**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | NRINSC |  |
| `TPINSCADQ` | Inteiro | TPINSCADQ |  |
| `NRINSCADQ` | Texto | NRINSCADQ |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS1250_NFS
**TABLE TFPS1250_NFS**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE1250`, `INDAQUIS`, `CHAVEIDEPROD`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPS1250_IDEPRODUTOR`.`CODEMP` |
| `DTREF` 🔑 | Data/Hora | DTREF | → `TFPS1250_IDEPRODUTOR`.`DTREF` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TFPS1250_IDEPRODUTOR`.`SEQUENCIA` |
| `TPAMB` 🔑 | Texto | TPAMB | → `TFPS1250_IDEPRODUTOR`.`TPAMB` |
| `CHAVE1250` 🔑 | Texto | CHAVE1250 | → `TFPS1250_IDEPRODUTOR`.`CHAVE1250` |
| `INDAQUIS` 🔑 | Texto | INDAQUIS | → `TFPS1250_IDEPRODUTOR`.`INDAQUIS` |
| `CHAVEIDEPROD` 🔑 | Texto | CHAVEIDEPROD | → `TFPS1250_IDEPRODUTOR`.`CHAVE` |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `SERIE` | Texto | SERIE |  |
| `NRDOCTO` | Texto | NRDOCTO |  |
| `DTEMISNF` | Data/Hora | DTEMISNF |  |
| `NUNOTA` | Inteiro | NUNOTA |  |
| `VLRBRUTO` | Decimal | VLRBRUTO |  |
| `VRCPDESCPR` | Decimal | VRCPDESCPR |  |
| `VRRATDESCPR` | Decimal | VRRATDESCPR |  |
| `VRSENARDESC` | Decimal | VRSENARDESC |  |

### TFPS1260
**TABLE TFPS1260**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSCESTABRURAL` | Texto | NRINSCESTABRURAL |  |
| `NRINSC` | Texto | NRINSC |  |

### TFPS1270
**TABLE TFPS1270**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `INDRETIF` | Inteiro | INDRETIF |  |
| `INDAPURACAO` | Inteiro | INDAPURACAO |  |
| `PERAPUR` | Texto | PERAPUR |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS1280
**TABLE TFPS1280**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `INDAPURACAO` | Inteiro | INDAPURACAO |  |
| `PERAPUR` | Texto | PERAPUR |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `INDSUBSTPATR` | Inteiro | INDSUBSTPATR |  |
| `PERCREDCONTRIB` | Decimal | PERCREDCONTRIB |  |
| `FATORMES` | Decimal | FATORMES |  |
| `FATOR13` | Decimal | FATOR13 |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS1300
**TABLE TFPS1300**

**PK:** `CODEMP`, `DTREF`, `SEQUENCIA`, `TPAMB`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `INDRETIF` | Inteiro | INDRETIF |  |
| `INDAPURACAO` | Inteiro | INDAPURACAO |  |
| `PERAPUR` | Texto | PERAPUR |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2190
**TABLE TFPS2190**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `STATUS` | Texto | STATUS |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `DTNASCTO` | Data/Hora | DTNASCTO |  |
| `DTADM` | Data/Hora | DTADM |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2200
**TABLE TFPS2200**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTALTERACAO` | Data | Data da Ocorrencia |  |
| `DTREF` 🔑 | Data/Hora | Periodo |  |
| `STATUSENVIO` | Texto | Status envio eSocial |  |
| `STATUSEVENTO` | Texto | Status eSocial |  |
| `STATUS` | Texto | Status eSocial |  |
| `ACAO` | Texto | Ação |  |
| `NRORECIBO` | Texto | N do Recibo |  |
| `NMTRAB` | Texto | Nome do trabalhador |  |
| `CPFTRAB` | Texto | CPF |  |
| `DTNASCTONASCIMENTO` | Data | Data de nascimento |  |
| `DTADM` | Data | Data de inicio (data de admissão) |  |
| `CODCATEG` | Inteiro | Categoria eSocial |  |
| `SEXO` | Texto | Sexo |  |
| `RACACOR` | Inteiro | Raca/Etnia |  |
| `ESTCIV` | Inteiro | Estado Civil |  |
| `GRAUINSTR` | Texto | Escolaridade |  |
| `NMSOC` | Texto | Nome Social |  |
| `PAISNASCTONASCIMENTO` | Inteiro | Cod. Nacionalidade (Tabela 06 - Paises) |  |
| `PAISNACNASCIMENTO` | Inteiro | Cod. Pais de Nascimento (Tabela 06 - Paises) |  |
| `TPLOGRADBRASIL` | Texto | Tipo de Logradouro |  |
| `DSCLOGRADBRASIL` | Texto | Descrição do logradouro |  |
| `NRLOGRADBRASIL` | Texto | Numero |  |
| `COMPLEMENTOBRASIL` | Texto | Complemento |  |
| `UFBRASIL` | Texto | UF |  |
| `BAIRROBRASIL` | Texto | Bairro |  |
| `CEPBRASIL` | Texto | CEP |  |
| `CODMUNICBRASIL` | Texto | Cod. do Municipio Brasil (Tabela do IBGE) |  |
| `DEFFISICA` | Texto | Deficiencia fisica |  |
| `TMPRESID` | Texto | Tempo de residencia do Trabalhador Imigrante |  |
| `CONDING` | Texto | Condição de ingresso do trabalhador imigrante |  |
| `DEFVISUAL` | Texto | Deficiencia visual |  |
| `DEFAUDITIVA` | Texto | Deficiencia auditiva |  |
| `DEFMENTAL` | Texto | Deficiencia mental |  |
| `DEFINTELECTUAL` | Texto | Deficiencia intelectual |  |
| `REABREADAP` | Texto | Reabilitado/Readaptado |  |
| `INFOCOTA` | Texto | Cota |  |
| `FONEPRINC` | Texto | Fone principal |  |
| `EMAILPRINC` | Texto | Email Principal |  |
| `CADINI` | Texto | Cadastramento inicial |  |
| `MATRICULA` | Texto | Matricula |  |
| *... +138 campos adicionais* | | | |

**Opções `ACAO`:** `A`=Retificação, `E`=Exclusão, `I`=Inclusão

**Opções `CADINI`:** `N`=Não, `S`=Sim

**Opções `CLAUASSEG`:** `N`=Não, `S`=Sim

**Opções `CONDING`:** `4`=4 - Beneficiado pelo acordo entre paises do Mercosul, `7`=7 - Outra condição, `6`=6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre o Brasil e Portugal, `5`=5- Dependente de agente diplomatico e/ou consular com acordo de reciprocidade e atividade remunerada, `3`=3 - Permanencia no Brasil em razão de reunião familiar, `2`=2 - Solicitante de refugio, `1`=1 - Refugiado

**Opções `DEFAUDITIVA`:** `N`=Não, `S`=Sim

**Opções `DEFFISICA`:** `N`=Não, `S`=Sim

### TFPS2205
**TABLE TFPS2205**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTALTERACAO` | Data | Data de alteração |  |
| `STATUSENVIO` | Texto | Status envio eSocial |  |
| `STATUS` | Texto | Status eSocial |  |
| `STATUSEVENTO` | Texto | Status eSocial |  |
| `ACAO` | Texto | Ação |  |
| `NRORECIBO` | Texto | Numero do Recibo |  |
| `NMTRAB` | Texto | Nome do trabalhador |  |
| `CPFTRAB` | Texto | CPF |  |
| `DTNASCTONASCIMENTO` | Data | Data de nascimento |  |
| `SEXO` | Texto | Sexo |  |
| `RACACOR` | Inteiro | Raca/Etnia |  |
| `ESTCIV` | Inteiro | Estado Civil |  |
| `GRAUINSTR` | Texto | Escolaridade |  |
| `NMSOC` | Texto | Nome Social |  |
| `PAISNASCTONASCIMENTO` | Texto | Cod. Nacionalidade (Tabela 06 - Paises) |  |
| `PAISNACNASCIMENTO` | Texto | Cod. Pais de Nascimento (Tabela 06 - Paises) |  |
| `TPLOGRADBRASIL` | Texto | Tipo de Logradouro |  |
| `DSCLOGRADBRASIL` | Texto | Descrição do logradouro |  |
| `NRLOGRADBRASIL` | Texto | Numero |  |
| `COMPLEMENTOBRASIL` | Texto | Complemento |  |
| `UFBRASIL` | Texto | UF |  |
| `BAIRROBRASIL` | Texto | Bairro |  |
| `TMPRESID` | Texto | Tempo de residencia do Trabalhador Imigrante |  |
| `CEPBRASIL` | Texto | CEP |  |
| `CONDING` | Texto | Condição de Ingresso do Trabalhador Imigrante |  |
| `DEFFISICA` | Texto | Deficiencia fisica |  |
| `CODMUNICBRASIL` | Inteiro | Cod. do Municipio Brasil (Tabela do IBGE) |  |
| `DEFVISUAL` | Texto | Deficiencia visual |  |
| `DEFAUDITIVA` | Texto | Deficiencia auditiva |  |
| `DEFMENTAL` | Texto | Deficiencia mental |  |
| `DEFINTELECTUAL` | Texto | Deficiencia intelectual |  |
| `REABREADAP` | Texto | Reabilitado/Readaptado |  |
| `INFOCOTA` | Texto | Cota |  |
| `OBSERVACAO` | Texto | Observação |  |
| `FONEPRINC` | Texto | Telefone principal |  |
| `EMAILPRINC` | Texto | Email Principal |  |
| `PAISRESID` | Texto | Pais de Residencia |  |
| `DSCLOGRADEXTERIOR` | Texto | Descrição do logradouro Exterior |  |
| `NRLOGRADEXTERIOR` | Texto | Numero do logradouro Exterior |  |
| *... +52 campos adicionais* | | | |

**Opções `ACAO`:** `E`=Exclusão, `A`=Retificação, `I`=Inclusão

**Opções `CONDING`:** `6`=6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre o Brasil e Portugal, `5`=5- Dependente de agente diplomatico e/ou consular com acordo de reciprocidade e atividade remunerada, `4`=4 - Beneficiado pelo acordo entre paises do Mercosul, `7`=7 - Outra condição, `3`=3 - Permanencia no Brasil em razão de reunião familiar, `2`=2 - Solicitante de refugio, `1`=1 - Refugiado

**Opções `DEFAUDITIVA`:** `S`=Sim, `N`=Não

**Opções `DEFFISICA`:** `S`=Sim, `N`=Não

**Opções `DEFINTELECTUAL`:** `S`=Sim, `N`=Não

**Opções `DEFMENTAL`:** `N`=Não, `S`=Sim

### TFPS2206
**TABLE TFPS2206**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTALTERACAO` | Data | Data de alteração |  |
| `STATUSEVENTO` | Texto | Status eSocial |  |
| `STATUS` | Texto | Status eSocial |  |
| `STATUSENVIO` | Texto | Status envio eSocial |  |
| `ACAO` | Texto | Ação |  |
| `NRORECIBO` | Texto | Numero do Recibo |  |
| `CPFTRAB` | Texto | CPF |  |
| `CODCATEG` | Inteiro | Categoria eSocial |  |
| `TPREGPREV` | Inteiro | Regime previdenciario |  |
| `TPREGJOR` | Inteiro | Regime de Jornada |  |
| `NATATIVIDADE` | Inteiro | Natureza da Atividade |  |
| `DTBASE` | Inteiro | Data Base |  |
| `CNPJSINDTRAB` | Texto | CNPJ do Sindicato |  |
| `DTEF` | Data | Data dos efeitos remuneratorios da alteração contratual |  |
| `DSCALT` | Texto | Descrição da Alteração |  |
| `JUSTPRORR` | Texto | Justificativa para a Prorrogação |  |
| `INDAPREND` | Inteiro | Indicativo de Contratação Aprendiz |  |
| `CNPJENTQUAL` | Texto | CNPJ Entidade Qualificadora |  |
| `TPINSCAPREND` | Inteiro | Tipo de Inscrição Aprendiz |  |
| `CNPJPRAT` | Texto | CNPJ Atividades Praticas |  |
| `DESCRCARGO` | Texto | Cargo |  |
| `CBOCARGO` | Texto | CBO Cargo |  |
| `DESCRFUNCAO` | Texto | Função |  |
| `CBOFUNCAO` | Texto | CBO Função |  |
| `VRSALFX` | Decimal | Salario base |  |
| `UNDSALFIXO` | Inteiro | Unidade de Pagamento |  |
| `DSCSALVAR` | Texto | Descrição do salario |  |
| `TPCONTR` | Inteiro | Tipo de Contrato |  |
| `DTTERM` | Data | Data de termino |  |
| `OBJDET` | Texto | Objeto determinante |  |
| `TPINSCLOCALTRABGERAL` | Inteiro | Tipo de Inscrição |  |
| `DSCLOGRADLOCALTRABDOM` | Texto | Logradouro |  |
| `NRLOGRADLOCALTRABDOM` | Texto | Numero |  |
| `COMPLEMENTOLOCALTRABDOM` | Texto | Complemento |  |
| `BAIRROLOCALTRABDOM` | Texto | Bairro |  |
| `CEPLOCALTRABDOM` | Texto | CEP |  |
| `CODMUNICLOCALTRABDOM` | Inteiro | Cidade |  |
| `UFLOCALTRABDOM` | Texto | UF |  |
| `QTDHRSSEM` | Decimal | Horas Semanais |  |
| *... +37 campos adicionais* | | | |

**Opções `ACAO`:** `A`=Retificação, `I`=Inclusão, `E`=Exclusão

**Opções `DTBASE`:** `1`=Janeiro, `2`=Fevereiro, `3`=Marco, `4`=Abril, `5`=Maio, `6`=Junho, `7`=Julho, `8`=Agosto, `9`=Setembro, `10`=Outubro, `11`=Novembro, `12`=Dezembro

**Opções `HRNOTURNO`:** `N`=Não, `S`=Sim

**Opções `INDAPREND`:** `2`=Contratação indi. apren. por enti. sem fins lucra. ou pratica despor. servi. estab. cumpridor cota, `1`=Contratação direta: contrat. do aprendiz efetivada pelo estab. cumpridor da cota de aprendizagem

**Opções `NATATIVIDADE`:** `2`=Trabalho rural, `1`=Trabalho urbano

**Opções `STATUS`:** `P`=Pendente de envio, `I`=Enviando para o e-Social, `F`=Finalizado

### TFPS2210
**TABLE TFPS2210**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  
**Referenciada por:** 10 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `STATUS` | Texto | STATUS |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | Numero da Inscrição |  |
| `CODEMPFUNC` | Inteiro | CODEMPFUNC |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `CPFTRAB` | Texto | CPF |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCATEG` | Inteiro | Categoria e-Social |  |
| `DTACID` | Data/Hora | Data do Acidente |  |
| `TPACID` | Texto | Tipo de Acidente |  |
| `HRACID` | Texto | Hora do Acidente |  |
| `HRSTRABANTESACID` | Texto | Horas Trabalhadas |  |
| `TPCAT` | Inteiro | Tipo de CAT |  |
| `INDCATOBITO` | Texto | Indica Obito |  |
| `DTOBITO` | Data/Hora | Data Obito |  |
| `INDCOMUNPOLICIA` | Texto | Houve Comunicação Policial |  |
| `CODSITGERADORA` | Inteiro | Situação Geradora do Acidente |  |
| `INICIATCAT` | Inteiro | Iniciativa da CAT |  |
| `OBSERVACAO` | Texto | Observações |  |
| `TPLOCAL` | Inteiro | Tipo de Local |  |
| `DSCLOCAL` | Texto | Especificação do Local |  |
| `CODAMB` | Texto | Ambiente de Trabalho |  |
| `DSCLOGRAD` | Texto | Logradouro |  |
| `NRLOGRAD` | Texto | Numero Endereco |  |
| `COMPLEMENTO` | Texto | Complemento |  |
| `BAIRRO` | Texto | Bairro |  |
| `CEP` | Texto | CEP |  |
| `CODMUNIC` | Inteiro | Cidade |  |
| `UF` | Texto | UF |  |
| *... +26 campos adicionais* | | | |

**Opções `IDEOC`:** `1`=1 - Conselho Regional de Medicina - CRM, `2`=2 - Conselho Regional de Odontologia - CRO, `3`=3 - Registro do Ministerio da Saude - RMS

**Opções `TPACID`:** `1`=Tipico, `2`=Doenca, `3`=Trajeto

**Opções `TPCAT`:** `1`=Inicial, `2`=Reabertura, `3`=Comunicação de Obito

**Opções `TPLOCAL`:** `1`=1 - Estab. do empregador no Brasil, `2`=2 - Estab. do empregador no Exterior, `3`=3 - Estab. de terceiros onde presta servico, `4`=4 - Via publica, `5`=5 - Area rural, `8`=8 - Embarcação, `9`=9 - Outros

### TFPS2210_AC
**TABLE TFPS2210_AC**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE2210`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPS2210`.`CODEMP` |
| `DTREF` 🔑 | Data/Hora | DTREF | → `TFPS2210`.`DTREF` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TFPS2210`.`SEQUENCIA` |
| `TPAMB` 🔑 | Texto | TPAMB | → `TFPS2210`.`TPAMB` |
| `CHAVE2210` 🔑 | Texto | CHAVE2210 | → `TFPS2210`.`CHAVE` |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `CODAGNTCAUSADOR` | Inteiro | Agente Causador |  |

### TFPS2210_PA
**TABLE TFPS2210_PA**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE2210`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPS2210`.`CODEMP` |
| `DTREF` 🔑 | Data/Hora | DTREF | → `TFPS2210`.`DTREF` |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA | → `TFPS2210`.`SEQUENCIA` |
| `TPAMB` 🔑 | Texto | TPAMB | → `TFPS2210`.`TPAMB` |
| `CHAVE2210` 🔑 | Texto | CHAVE2210 | → `TFPS2210`.`CHAVE` |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `CODPARTEATING` | Inteiro | Parte Atingida |  |
| `LATERALIDADE` | Inteiro | Lateralidade |  |

**Opções `LATERALIDADE`:** `0`=0 - Não aplicavel, `1`=1 - Esquerda, `2`=2 - Direita, `3`=3 - Ambas

### TFPS2220
**TABLE TFPS2220**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `STATUS` | Texto | STATUS |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | NRINSC |  |
| `CODEMPFUNC` | Inteiro | CODEMPFUNC |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCATEG` | Inteiro | CODCATEG |  |
| `TPEXAMEOCUP` | Inteiro | TPEXAMEOCUP |  |
| `DTASO` | Data/Hora | DTASO |  |
| `RESASO` | Inteiro | RESASO |  |
| `CPFMED` | Texto | CPFMED |  |
| `NISMED` | Texto | NISMED |  |
| `NMMED` | Texto | NMMED |  |
| `NRCRM` | Texto | NRCRM |  |
| `UFCRM` | Texto | UFCRM |  |
| `CPFRESP` | Texto | CPFRESP |  |
| `NMRESP` | Texto | NMRESP |  |
| `NRCRMRESPMONIT` | Texto | NRCRMRESPMONIT |  |
| `UFCRMRESPMONIT` | Texto | UFCRMRESPMONIT |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2221
**TABLE TFPS2221**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `STATUS` | Texto | STATUS |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | NRINSC |  |
| `CODEMPFUNC` | Inteiro | CODEMPFUNC |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCATEG` | Inteiro | CODCATEG |  |
| `DTEXAME` | Data/Hora | DTEXAME |  |
| `CNPJLAB` | Texto | CNPJLAB |  |
| `CODSEQEXAME` | Texto | CODSEQEXAME |  |
| `NMMED` | Texto | NMMED |  |
| `NRCRM` | Texto | NRCRM |  |
| `UFCRM` | Texto | UFCRM |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `INDRECUSA` | Texto | INDRECUSA |  |

### TFPS2230
**TABLE TFPS2230**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `STATUS` | Texto | STATUS |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCATEG` | Inteiro | CODCATEG |  |
| `DTINIAFAST` | Data/Hora | DTINIAFAST |  |
| `CODMOTAFAST` | Texto | CODMOTAFAST |  |
| `INFOMESMOMTV` | Texto | INFOMESMOMTV |  |
| `TPACIDTRANSITO` | Inteiro | TPACIDTRANSITO |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `CNPJCESS` | Texto | CNPJCESS |  |
| `INFONUS` | Inteiro | INFONUS |  |
| `CNPJSIND` | Texto | CNPJSIND |  |
| `INFONUSREMUN` | Inteiro | INFONUSREMUN |  |
| `ORIGRETIF` | Inteiro | ORIGRETIF |  |
| `TPPROC` | Texto | TPPROC |  |
| `NRPROC` | Texto | NRPROC |  |
| `TEM2300` | Inteiro | TEM2300 |  |
| `DTTERMAFAST` | Data/Hora | DTTERMAFAST |  |
| `CHAVE2200` | Texto | CHAVE2200 |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2240
**TABLE TFPS2240**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `STATUS` | Texto | STATUS |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `CODEMPFUNC` | Inteiro | CODEMPFUNC |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | NRINSC |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCATEG` | Inteiro | CODCATEG |  |
| `DTINICONDICAO` | Data/Hora | DTINICONDICAO |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2245
**TABLE TFPS2245**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `STATUS` | Texto | STATUS |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `TPINSC` | Inteiro | TPINSC |  |
| `NRINSC` | Texto | NRINSC |  |
| `CODEMPFUNC` | Inteiro | CODEMPFUNC |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `NROUNICOTREIN` | Inteiro | NROUNICOTREIN |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCATEG` | Inteiro | CODCATEG |  |
| `CODTREICAP` | Texto | CODTREICAP |  |
| `DTTREICAP` | Data/Hora | DTTREICAP |  |
| `DURTREICAP` | Decimal | DURTREICAP |  |
| `MODTREICAP` | Inteiro | MODTREICAP |  |
| `TPTREICAP` | Inteiro | TPTREICAP |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `INDTREINANT` | Texto | INDTREINANT |  |

### TFPS2250
**TABLE TFPS2250**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `STATUS` | Texto | STATUS |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `DTAVPRV` | Data/Hora | DTAVPRV |  |
| `DTPREVDESLIG` | Data/Hora | DTPREVDESLIG |  |
| `TPAVPREVIO` | Inteiro | TPAVPREVIO |  |
| `OBSERVACAODET` | Texto | OBSERVACAODET |  |
| `DTCANCAVPRV` | Data/Hora | DTCANCAVPRV |  |
| `OBSERVACAOCANC` | Texto | OBSERVACAOCANC |  |
| `MTVCANCAVPREVIO` | Inteiro | MTVCANCAVPREVIO |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2260
**TABLE TFPS2260**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `CODEMPFUNC` | Inteiro | CODEMPFUNC |  |
| `CODFUNC` | Inteiro | CODFUNC |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `CODCONV` | Texto | CODCONV |  |
| `DTINICIO` | Data/Hora | DTINICIO |  |
| `DTFIM` | Data/Hora | DTFIM |  |
| `CODHORCONTRAT` | Texto | CODHORCONTRAT |  |
| `DSCJORNADA` | Texto | DSCJORNADA |  |
| `INDLOCAL` | Texto | INDLOCAL |  |
| `TPLOGRAD` | Texto | TPLOGRAD |  |
| `DSCLOGRAD` | Texto | DSCLOGRAD |  |
| `NRLOGRAD` | Texto | NRLOGRAD |  |
| `COMPLEMENTO` | Texto | COMPLEMENTO |  |
| `BAIRRO` | Texto | BAIRRO |  |
| `CEP` | Texto | CEP |  |
| `CODMUNIC` | Texto | CODMUNIC |  |
| `UF` | Texto | UF |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTPREVPGTO` | Data/Hora | DTPREVPGTO |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2298
**TABLE TFPS2298**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `TPREINT` | Texto | TPREINT |  |
| `NRPROCJUD` | Texto | NRPROCJUD |  |
| `NRLEIANISTIA` | Texto | NRLEIANISTIA |  |
| `DTEFETRETORNO` | Data/Hora | DTEFETRETORNO |  |
| `DTEFEITO` | Data/Hora | DTEFEITO |  |
| `INDPAGTOJUIZO` | Texto | INDPAGTOJUIZO |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |

### TFPS2299
**TABLE TFPS2299**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `MATRICULA` | Texto | MATRICULA |  |
| `MTVDESLIG` | Texto | MTVDESLIG |  |
| `DTDESLIG` | Data/Hora | DTDESLIG |  |
| `INDPAGTO` | Texto | INDPAGTO |  |
| `DTPROJFIMAPI` | Data/Hora | DTPROJFIMAPI |  |
| `PENSALIM` | Texto | PENSALIM |  |
| `PERCALIM` | Decimal | PERCALIM |  |
| `VRALIM` | Decimal | VRALIM |  |
| `NRCERTOBITO` | Texto | NRCERTOBITO |  |
| `PRPROCTRAB` | Texto | PRPROCTRAB |  |
| `INDCUMPRPARC` | Texto | INDCUMPRPARC |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `CNPJSUCESSORA` | Texto | CNPJSUCESSORA |  |
| `CPFSUBSTITUTO` | Texto | CPFSUBSTITUTO |  |
| `DTNASCTOSUBSTITUTO` | Data/Hora | DTNASCTOSUBSTITUTO |  |
| `IDCONSIG` | Texto | IDCONSIG |  |
| `INSCONSIG` | Texto | INSCONSIG |  |
| `NRCONTR` | Texto | NRCONTR |  |
| `DTFIMQUAR` | Data/Hora | DTFIMQUAR |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `QTDDIASINTERM` | Texto | QTDDIASINTERM |  |
| `INDMV` | Inteiro | INDMV |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `NOVOCPF` | Texto | NOVOCPF |  |
| `TPINSCSUC` | Inteiro | TPINSCSUC |  |

### TFPS2300
**TABLE TFPS2300**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTALTERACAO` | Data | Data da Ocorrencia |  |
| `STATUSEVENTO` | Texto | Status eSocial |  |
| `STATUS` | Texto | Status eSocial |  |
| `STATUSENVIO` | Texto | Status envio eSocial |  |
| `ACAO` | Texto | Ação |  |
| `NRORECIBO` | Texto | N do Recibo |  |
| `NMTRAB` | Texto | Nome do trabalhador |  |
| `CPFTRAB` | Texto | CPF |  |
| `DTNASCTONASCIMENTO` | Data | Data de nascimento |  |
| `CODCATEG` | Inteiro | Categoria eSocial |  |
| `SEXO` | Texto | Sexo |  |
| `RACACOR` | Inteiro | Raca/Etnia |  |
| `ESTCIV` | Inteiro | Estado Civil |  |
| `GRAUINSTR` | Texto | Escolaridade |  |
| `PAISNASCTONASCIMENTO` | Inteiro | Cod. Nacionalidade (Tabela 06 - Paises) |  |
| `PAISNACNASCIMENTO` | Inteiro | Cod. Pais de Nascimento (Tabela 06 - Paises) |  |
| `TPLOGRADBRASIL` | Texto | Tipo de Logradouro |  |
| `DSCLOGRADBRASIL` | Texto | Descrição do logradouro |  |
| `NRLOGRADBRASIL` | Texto | Numero |  |
| `COMPLEMENTOBRASIL` | Texto | Complemento |  |
| `UFBRASIL` | Texto | UF |  |
| `BAIRROBRASIL` | Texto | Bairro |  |
| `CEPBRASIL` | Texto | CEP |  |
| `DEFFISICA` | Texto | Deficiencia fisica |  |
| `CODMUNICBRASIL` | Inteiro | Cod. do Municipio Brasil (Tabela do IBGE) |  |
| `DEFVISUAL` | Texto | Deficiencia visual |  |
| `TMPRESID` | Texto | Tempo de residencia do Trabalhador Imigrante |  |
| `DEFAUDITIVA` | Texto | Deficiencia auditiva |  |
| `CONDING` | Texto | Condição de ingresso do trabalhador imigrante |  |
| `DEFMENTAL` | Texto | Deficiencia mental |  |
| `DEFINTELECTUAL` | Texto | Deficiencia intelectual |  |
| `REABREADAP` | Texto | Reabilitado/Readaptado |  |
| `FONEPRINC` | Texto | Fone principal |  |
| `EMAILPRINC` | Texto | Email Principal |  |
| `CADINI` | Texto | Cadastramento inicial |  |
| `MATRICULA` | Texto | Matricula |  |
| `NRPROCTRAB` | Texto | N Processo Trabalhista |  |
| `NATATIVIDADE` | Inteiro | Natureza da Atividade |  |
| `DESCRCARGO` | Texto | Nome do Cargo |  |
| `CBOCARGO` | Texto | CBO do Cargo |  |
| *... +112 campos adicionais* | | | |

**Opções `ACAO`:** `A`=Retificação, `E`=Exclusão, `I`=Inclusão

**Opções `CADINI`:** `N`=Não, `S`=Sim

**Opções `CONDING`:** `2`=2 - Solicitante de refugio, `3`=3 - Permanencia no Brasil em razão de reunião familiar, `4`=4 - Beneficiado pelo acordo entre paises do Mercosul, `5`=5- Dependente de agente diplomatico e/ou consular com acordo de reciprocidade e atividade remunerada, `6`=6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre o Brasil e Portugal, `7`=7 - Outra condição, `1`=1 - Refugiado

**Opções `DEFAUDITIVA`:** `S`=Sim, `N`=Não

**Opções `DEFFISICA`:** `N`=Não, `S`=Sim

**Opções `DEFINTELECTUAL`:** `N`=Não, `S`=Sim

### TFPS2306
**TABLE TFPS2306**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `DTALTERACAO` | Data | Data de alteração |  |
| `STATUSEVENTO` | Texto | Status eSocial |  |
| `STATUS` | Texto | Status eSocial |  |
| `STATUSENVIO` | Texto | Status envio eSocial |  |
| `ACAO` | Texto | Ação |  |
| `NRORECIBO` | Texto | Numero do Recibo |  |
| `CPFTRAB` | Texto | CPF |  |
| `CODCATEG` | Inteiro | Categoria eSocial |  |
| `NATATIVIDADE` | Inteiro | Natureza da Atividade |  |
| `DESCRCARGO` | Texto | Cargo |  |
| `CBOCARGO` | Texto | CBO Cargo |  |
| `DESCRFUNCAO` | Texto | Função |  |
| `CBOFUNCAO` | Texto | CBO Função |  |
| `VRSALFX` | Decimal | Salario base |  |
| `UNDSALFIXO` | Inteiro | Unidade de Pagamento |  |
| `DSCSALVAR` | Texto | Descrição do salario |  |
| `NATESTAGIO` | Texto | Natureza do estagio |  |
| `NIVESTAGIO` | Texto | Nivel do estagio |  |
| `AREAATUACAO` | Texto | Area de atuação |  |
| `NRAPOL` | Texto | Numero da apolice de seguro |  |
| `DTPREVTERM` | Data/Hora | Data prevista termino do estagio |  |
| `CNPJINSTENSINO` | Texto | CNPJ Instituição de Ensino |  |
| `NMRAZAOINSTENS` | Texto | Razão Social |  |
| `DSCLOGRADINSTENS` | Texto | Endereco |  |
| `NRLOGRADINSTENS` | Texto | Numero |  |
| `BAIRROINSTENS` | Texto | Bairro |  |
| `CODMUNICINSTENS` | Inteiro | Cidade |  |
| `UFINSTENS` | Texto | UF |  |
| `CNPJAGNTINTEG` | Texto | CNPJ Agente de Integração |  |
| `CPFSUPERVISOR` | Texto | CPF Supervisor do estagio |  |
| `TPREGPREV` | Inteiro | Regime previdenciario |  |
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data/Hora | Periodo |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Numero de inscrição empregador |  |
| `NISTRAB` | Texto | Numero de inscrição do segurado - NIS |  |
| `DTEF` | Data/Hora | Data dos efeitos remuneratorios da alteração contratual |  |
| `EXCLMANUAL` | Texto | Exclusão manual |  |
| `CODCARGO` | Texto | Cargo |  |
| *... +24 campos adicionais* | | | |

**Opções `ACAO`:** `E`=Exclusão, `A`=Retificação, `I`=Inclusão

**Opções `NATATIVIDADE`:** `2`=Trabalho rural, `1`=Trabalho urbano

**Opções `NATESTAGIO`:** `O`=Obrigatorio, `N`=Não Obrigatorio

**Opções `NIVESTAGIO`:** `3`=Formação Profissional, `4`=Superior, `2`=Medio, `1`=Fundamental

**Opções `STATUS`:** `P`=Pendente de envio, `I`=Enviando para o e-Social, `F`=Finalizado

**Opções `STATUSEVENTO`:** `S`=Pendente de envio - erro no envio, `P`=Pendente de envio, `I`=Enviando para o e-Social, `F`=Finalizado

### TFPS2399
**TABLE TFPS2399**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `SEQUENCIA`, `CHAVE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NISTRAB` | Texto | NISTRAB |  |
| `CODCATEG` | Inteiro | CODCATEG |  |
| `DTTERMINO` | Data/Hora | DTTERMINO |  |
| `MTVDESLIG` | Texto | MTVDESLIG |  |
| `DTFIMQUAR` | Data/Hora | DTFIMQUAR |  |
| `INDMV` | Inteiro | INDMV |  |
| `STATUS` | Texto | STATUS |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `ACAO` | Texto | ACAO |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `NOVOCPF` | Texto | NOVOCPF |  |
| `PENSALIM` | Texto | PENSALIM |  |
| `PERCALIM` | Decimal | PERCALIM |  |
| `VRALIM` | Decimal | VRALIM |  |

### TFPS2500
**TABLE TFPS2500**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `CHAVE`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `STATUS` | Texto | STATUS |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `INDRETIF` | Inteiro | INDRETIF |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `TPINSCCONTRIBUINTE` | Inteiro | TPINSCCONTRIBUINTE |  |
| `NRINSCCONTRIBUINTE` | Texto | NRINSCCONTRIBUINTE |  |
| `ORIGEM` | Inteiro | ORIGEM |  |
| `NRPROCTRAB` | Texto | NRPROCTRAB |  |
| `OBSPROCTRAB` | Texto | OBSPROCTRAB |  |
| `DTSENT` | Data/Hora | DTSENT |  |
| `UFVARA` | Texto | UFVARA |  |
| `CODMUNIC` | Inteiro | CODMUNIC |  |
| `IDVARA` | Inteiro | IDVARA |  |
| `DTCCP` | Data/Hora | DTCCP |  |
| `TPCCP` | Inteiro | TPCCP |  |
| `CNPJCCP` | Texto | CNPJCCP |  |
| `CPFTRAB` | Texto | CPFTRAB |  |
| `NMTRAB` | Texto | NMTRAB |  |
| `DTNASCTO` | Data/Hora | DTNASCTO |  |

### TFPS2501
**TABLE TFPS2501**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `CHAVE`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP |  |
| `DTREF` 🔑 | Data/Hora | DTREF |  |
| `TPAMB` 🔑 | Texto | TPAMB |  |
| `CHAVE` 🔑 | Texto | CHAVE |  |
| `SEQUENCIA` 🔑 | Inteiro | SEQUENCIA |  |
| `NRORECIBO_ANT` | Texto | NRORECIBO_ANT |  |
| `SEQUENCIA_ANT` | Inteiro | SEQUENCIA_ANT |  |
| `DTREF_ANT` | Data/Hora | DTREF_ANT |  |
| `STATUS` | Texto | STATUS |  |
| `ACAO` | Texto | ACAO |  |
| `CONTROLE` | Texto | CONTROLE |  |
| `DATACHANGE` | C | DATACHANGE |  |
| `INDRETIF` | Inteiro | INDRETIF |  |
| `NRORECIBO` | Texto | NRORECIBO |  |
| `TPINSCEMPREGADOR` | Inteiro | TPINSCEMPREGADOR |  |
| `NRINSCEMPREGADOR` | Texto | NRINSCEMPREGADOR |  |
| `NRPROCTRAB` | Texto | NRPROCTRAB |  |
| `PERAPURPGTO` | Texto | PERAPURPGTO |  |
| `OBS` | Texto | OBS |  |

### TFPS2555
**TABLE TFPS2555**

**PK:** `CODEMP`, `DTREF`, `TPAMB`, `CHAVE`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa |  |
| `DTREF` 🔑 | Data | Periodo |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `STATUS` | Texto | Status eSocial |  |
| `TPAMB` 🔑 | Texto | Identificação do Ambiente |  |
| `CHAVE` 🔑 | Texto | Chave |  |
| `ACAO` | Texto | Ação |  |
| `CONTROLE` | Texto | Controle de Alteração |  |
| `DATACHANGE` | C | Mudanca de Dados |  |
| `NRORECIBO` | Texto | Numero do Recibo |  |
| `NRORECIBO_ANT` | Texto | Numero do Recibo Anterior |  |
| `DTREF_ANT` | Data | Periodo Anterior |  |
| `SEQUENCIA_ANT` | Inteiro | Sequencia Anterior |  |
| `TPINSCEMPREGADOR` | Inteiro | Tipo de Inscrição Empregador |  |
| `NRINSCEMPREGADOR` | Texto | Numero de inscrição empregador |  |
| `NRPROCTRAB` | Texto | N do processo trabalhista |  |
| `PERAPURPGTO` | Texto | Periodo de Apuração do Pagamento |  |

### TFPSFE
**Solicitacao de ferias**

**PK:** `CODEMP`, `CODFUNC`, `NUSOLICIT`, `DTINIAQUI`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `NUSOLICIT` 🔑 | Inteiro | Solicitação |  |
| `DHSOLICIT` | Data | Data da solicitação |  |
| `STATUS` | Texto | Situação |  |
| `PREVINICIO` | Data | Inicio da ferias |  |
| `DIASSOLICITADOS` | Inteiro | Qtd. dias |  |
| `ADIANTADECTERC` | Texto | Adiantar 13 |  |
| `ABONOPECUNIARIO` | Texto | Vender 10 dias |  |
| `DTINIAQUI` 🔑 | Data | Inicio per. aquisitivo |  |
| `OBSERVACAO` | Texto | Observação |  |
| `DIASABONOPEC` | Inteiro | Dias de abono |  |
| `SEQFER` | Inteiro | Seq. Programação |  |
| `ID` | Inteiro | ID |  |

**Opções `ABONOPECUNIARIO`:** `N`=Não, `S`=Sim

**Opções `ADIANTADECTERC`:** `S`=Sim, `N`=Não

**Opções `STATUS`:** `P`=Pendente, `N`=Não Aprovado, `A`=Aprovado

### TFPSGA
**Situação Geradora**

**PK:** `CODSITUACAOGERADORA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSITUACAOGERADORA` 🔑 | Inteiro | Codigo |  |
| `DESCRSITUACAOGERADORA` | Texto | Descrição |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPSIT
**Situação Estatutaria**

**PK:** `CODSITESTAT`  
**Referenciada por:** 1 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODSITESTAT` 🔑 | Inteiro | Codigo da situação |  |
| `DESCRSIT` | Texto | Descrição |  |
| `PARCELA1_13SAL` | Inteiro | 1 Parcela 13 salario |  |
| `PARCELA2_13SAL` | Inteiro | 2 Parcela 13 salario |  |
| `PARCUNICA13SAL` | Inteiro | Parcela unica 13 salario |  |

### TFPSUB
**Tabela de substituição de funcionario**

**PK:** `CODEMP`, `CODFUNC`, `CODEMPSUB`, `CODFUNCSUB`, `DTINICIO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMPSUB` 🔑 | Inteiro | Empresa substituida | → `TFPPUB`.`CODEMP` |
| `CODFUNCSUB` 🔑 | Inteiro | Funcionario substituido | → `TFPPUB`.`CODFUNC` |
| `CONTRACHQ` | Texto | Apresentou contra cheque |  |
| `DTFIM` | Data/Hora | Data Final da substituição |  |
| `DTINICIO` 🔑 | Data/Hora | Data inicial da substituição |  |
| `CODFUNC` 🔑 | Inteiro | Funcionario substituto | → `TFPPUB`.`CODFUNC` |
| `CODEMP` 🔑 | Inteiro | Empresa substituta | → `TFPPUB`.`CODEMP` |
| `REFERENCIA` | Data/Hora | Referencia |  |

**Opções `CONTRACHQ`:** `S`=Sim, `N`=Não

### TFPSUSP
**TABLE TFPSUSP**

**PK:** `NUPROCESSO`, `CODSUSP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPROCESSO` 🔑 | Inteiro | NUPROCESSO | → `TFPPSS`.`NUPROCESSO` |
| `CODSUSP` 🔑 | Texto | Codigo Indicativo de Suspensão |  |
| `INDSUSP` | Texto | Indicativo de suspensão de exigibilidade |  |
| `DTDESCISAO` | Data | Data de decisão |  |
| `INDDEPOSITO` | Texto | Deposito de Montante Integral |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

**Opções `INDDEPOSITO`:** `N`=Não, `S`=Sim

**Opções `INDSUSP`:** `01`=Liminar em mandado de seguranca, `02`=Deposito judicial do montante integral, `03`=Deposito administrativo do montante integral, `04`=Antecipação de tutela, `05`=Liminar em medida cautelar, `08`=Sentenca em mandado de seguranca favoravel ao contribuinte, `09`=Sentenca em ação ordinaria favoravel ao contribuinte e confirmada pelo TRF, `10`=Acordão do TRF favoravel ao contribuinte, `11`=Acordão do STJ em recurso especial favoravel ao contribuinte, `12`=Acordão do STF em recurso extraordinario favoravel ao contribuinte, `13`=Sentenca 1 instancia não transitada em julgado com efeito suspensivo, `14`=Contestação administrativa FAP

### TFPTAT
**Testemunhas CAT**

**PK:** `NUCAT`, `SEQUENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUCAT` 🔑 | Inteiro | NUCAT |  |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `NOMETESTEMUNHA` | Texto | Nome da Testemunha |  |
| `CODEND` | Inteiro | Endereco | → `TSIEND`.`CODEND` |
| `NUMEND` | Texto | Numero Endereco |  |
| `CODBAI` | Inteiro | Bairro |  |
| `CODCID` | Inteiro | Cidade | → `TSICID`.`CODCID` |
| `CEP` | Texto | CEP |  |
| `TELEFONE` | Texto | Telefone |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPTBE
**Tipo de Beneficio**

**PK:** `CODTBE`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTBE` 🔑 | Inteiro | Codigo |  |
| `DESCRICAO` | Texto | Descrição |  |
| `TIPO` | Inteiro | Tipo |  |

**Opções `TIPO`:** `1`=Vale Refeição, `4`=Plano de Saude, `0`=Vale Alimentação, `5`=Outros Beneficios, `2`=Vale Transporte, `3`=Vale Combustivel

### TFPTERC
**TABLE TFPTERC**

**PK:** `NUPROCESSO`, `CODTERC`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NUPROCESSO` 🔑 | Inteiro | NUPROCESSO | → `TFPPSS`.`NUPROCESSO` |
| `CODTERC` 🔑 | Texto | Codigo de Terceiro |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `PERCENTUAL` | Decimal | Percentual |  |

**Opções `CODTERC`:** `0001`=0001 - Salario- Educação, `0002`=0002 - INCRA, `0004`=0004 - SENAI, `0008`=0008 - SESI, `0016`=0016 - SENAC, `0032`=0032 - SESC, `0064`=0064 - SEBRAE, `0128`=0128 - DPC, `0256`=0256 - Fundo Aeroviario, `0512`=0512 - SENAR, `1024`=1024 - SEST, `2048`=2048 - SENAT

### TFPTLT
**TABLE TFPTLT**

**PK:** `CODLOTACAO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODLOTACAO` 🔑 | Inteiro | Cod. Lotação |  |
| `DESCRRESUMIDA` | Texto | DESCRRESUMIDA |  |
| `DESCRLOTACAO` | Texto | DESCRLOTACAO |  |
| `USADO` | Texto | USADO |  |
| `CODUSU` | Inteiro | CODUSU |  |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPTOM
**Tomador**

**PK:** `CODEMP`, `CODFUNC`, `CODPARC`, `DTINICIO`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `CODPARC` 🔑 | Inteiro | Cod. Parceiro | → `TGFPAR`.`CODPARC` |
| `DTINICIO` 🔑 | Data/Hora | DTINICIO |  |
| `DTFIM` | Data/Hora | DTFIM |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `CODUSU` | Inteiro | Cod. Usuario | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPTPA
**Tipo de Acidente de Trabalho**

**PK:** `TIPACIDENTE`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPACIDENTE` 🔑 | Texto | TIPACIDENTE |  |
| `DESCRTIPACIDENTE` | Texto | Descrição |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |

### TFPTPR
**Tipo de Rescisão**

**PK:** `CODTPR`  
**Referenciada por:** 3 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTPR` 🔑 | Inteiro | Cod.Tipo Rescisão |  |
| `DESCRTIPRESC` | Texto | Descrição |  |
| `CODAFASTRAIS` | Texto | Cod.Afastamento da RAIS |  |
| `CODAFASTFGTS` | Texto | Cod.Afastamento FGTS |  |
| `CODAFASTCAGED` | Texto | Cod.Causa do Afastamento |  |
| `CODSAQUEFGTS` | Inteiro | Cod.Saque |  |
| `GERAPREVISAO` | Texto | Permite gerar previsão |  |
| `CODMOTDESLIGESOCIAL` | Texto | Motivo desligamento E-Social |  |

**Opções `GERAPREVISAO`:** `S`=Sim, `N`=Não

### TFPTRC
**TABLE TFPTRC**

**PK:** `CODTREICAP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODTREICAP` 🔑 | Inteiro | CODTREICAP |  |
| `DESCRTREICAP` | Texto | DESCRTREICAP |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `ATIVO` | Texto | Ativo |  |

### TFPTREI
**TABLE TFPTREI**

**PK:** `NROUNICO`  
**Referenciada por:** 2 tabelas  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `NROUNICO` 🔑 | Inteiro | Numero unico do treinamento |  |
| `DTTREIN` | Data | Data de inicio do treinamento |  |
| `CODTREICAP` | Inteiro | Codigo do Treinamento/Capacitação no eSocial |  |
| `DURTREICAP` | Decimal | Duração em horas |  |
| `MODTREICAP` | Inteiro | Modalidade |  |
| `TPTREICAP` | Inteiro | Tipo de treinamento |  |
| `OBSERVACAO` | Texto | Observação |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |

**Opções `MODTREICAP`:** `3`=3 - Mista, `2`=2 - Educação a Distancia (EAD), `1`=1 - Presencial

**Opções `TPTREICAP`:** `2`=2 - Periodico, `3`=3 - Reciclagem, `4`=4 - Eventual, `5`=5 - Outros, `1`=1 - Inicial

### TFPTTB
**Tipo de tabelas**

**PK:** `TIPOTAB`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `TIPOTAB` 🔑 | Texto | Tipo da tabela |  |
| `DESCRTAB` | Texto | Descrição da tabela |  |
| `CATEGTAB` | Texto | Categoria da tabela |  |
| `CODEVEINSS` | Inteiro | Codigo do evento de INSS |  |
| `CODEVEDEBADIAN` | Inteiro | Codigo do evento de adiantamento |  |
| `REGFISCAL` | Inteiro | Região fiscal |  |
| `DTALTER` | Data/Hora | Data de alteração |  |
| `PERCINSS` | Decimal | Percentual de INSS |  |

**Opções `CATEGTAB`:** `P`=Privada, `U`=Publica

### TFPVAL
**Tabela de Vale Transporte**

**PK:** `CODEMP`, `CODFUNC`, `CODLINHA`, `REFERENCIA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | Empresa | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Funcionario | → `TFPFUN`.`CODFUNC` |
| `TIPO` | Texto | Tipo |  |
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `CODLINHA` 🔑 | Inteiro | Descrição | → `TFPLIN`.`CODLINHA` |
| `PASSESDIA` | Inteiro | Vales por dia |  |
| `DTALTER` | Data/Hora | Data de Alteração |  |
| `QTDDIAS` | Decimal | Quantidade de dias |  |
| `VALOR` | Decimal | Valor da Tarifa |  |
| `MANTEMPROXIMAREF` | Texto | Mantem Proxima Referencia |  |

**Opções `MANTEMPROXIMAREF`:** `S`=Sim, `N`=Não

**Opções `TIPO`:** `A`=Alimentação, `T`=Transporte

### TFPVCA
**Variavel de Calculo**

**PK:** `REFERENCIA`, `CODEMP`, `CODFUNC`, `TIPFOLHA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `REFERENCIA` 🔑 | Data/Hora | Referencia | → `TFPBAS`.`REFERENCIA` |
| `CODEMP` 🔑 | Inteiro | Cod.Empresa | → `TFPBAS`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | Cod.Funcionario | → `TFPFUN`.`CODFUNC` |
| `TIPFOLHA` 🔑 | Texto | Tipo de Folha | → `TFPBAS`.`TIPFOLHA` |
| `VARIAVEIS` | Texto | Variaveis |  |

### TFPVGR
**Variação de Gratificação**

**PK:** `TIPREG`, `CODGRAT`, `DTMOV`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `VLRGRAT` | Decimal | Valor da Gratificação |  |
| `DTMOV` 🔑 | Data/Hora | Data do movimento |  |
| `CODGRAT` 🔑 | Inteiro | Gratificação |  |
| `TIPREG` 🔑 | Texto | Tipo de registro |  |
| `REDUCAO2` | Decimal | Redução 2 |  |
| `REDUCAO` | Decimal | Redução |  |
| `ATOADMIN` | Texto | Ato Administrativo |  |
| `COMPLEMENTO` | Decimal | Complemento |  |
| `VLROPCIONAL` | Decimal | Valor Opcional |  |

**Opções `TIPREG`:** `D`=Decimos, `G`=Gratificação, `N`=Nivel de Referencia

### TFPVPJ
**TABLE TFPVPJ**

**PK:** `CODVPJ`, `CODEMP`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODVPJ` 🔑 | Inteiro | CODVPJ |  |
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPEMP`.`CODEMP` |
| `CODDEP` | Inteiro | CODDEP | → `TFPDEP`.`CODDEP` |
| `NOME` | Texto | NOME |  |
| `CODUSU` | Inteiro | Codigo Usuario |  |
| `CPF` | Texto | CPF |  |
| `CNPJ` | Texto | CNPJ |  |
| `SEXO` | Texto | Sexo |  |
| `EMAIL` | Texto | EMAIL |  |
| `TELEFONE` | Texto | TELEFONE |  |
| `IMAGEM` | Blob | IMAGEM |  |
| `DTNASC` | Data/Hora | DTNASC |  |
| `DTINICIO` | Data/Hora | DTINICIO |  |
| `DTFIM` | Data/Hora | DTFIM |  |
| `OBSERVACAO` | Texto | OBSERVACAO |  |
| `MODIFPOR` | Inteiro | MODIFPOR |  |
| `DHALTER` | Data/Hora | DHALTER |  |
| `PERTENCEDP` | Texto | Pertence ao DP/RH |  |

**Opções `PERTENCEDP`:** `N`=Não, `S`=Sim

**Opções `SEXO`:** `F`=Feminino, `M`=Masculino

### TFPVPS
**TABLE TFPVPS**

**PK:** `CODEMP`, `CODFUNC`, `SEQUENCIA`, `CODCONVENIO`, `REFERENCIA`, `TIPFOLHA`  

| Campo | Tipo | Descrição | FK |
|---|---|---|---|
| `CODEMP` 🔑 | Inteiro | CODEMP | → `TFPFUN`.`CODEMP` |
| `CODFUNC` 🔑 | Inteiro | CODFUNC | → `TFPFUN`.`CODFUNC` |
| `SEQUENCIA` 🔑 | Inteiro | Sequencia |  |
| `CODCONVENIO` 🔑 | Inteiro | Cod. Convenio | → `TFPCON`.`CODCONVENIO` |
| `REFERENCIA` 🔑 | Data | Referencia |  |
| `VALOR` | Decimal | Valor do Plano |  |
| `DIGITADO` | Texto | DIGITADO |  |
| `CODUSU` | Inteiro | CODUSU | → `TSIUSU`.`CODUSU` |
| `DHALTER` | Data/Hora | DHALTER |  |
| `VALORPROVENTO` | Decimal | Valor Provento |  |
| `TIPFOLHA` 🔑 | Texto | Tipo de Folha |  |

**Opções `TIPFOLHA`:** `1`=Ferias 1, `2`=Ferias 2, `D`=Dec. Terceiro, `N`=Mensal, `R`=Rescisão, `F`=Ferias
