# sankhya-modulo-java

Skill para Claude Code especializada em desenvolvimento de **módulos Java complementares para o ERP Sankhya OM** — sem Addon Studio, com registro manual de artefatos.

---

## O que esta skill faz

Transforma o Claude em um especialista em módulos Java Sankhya OM, capaz de:

- Criar **EventoProgramavelJava** (eventos CRUD em entidades)
- Criar **AcaoRotinaJava** (botões de ação manuais)
- Criar **RegraNegocioJava** / **Regra** (lógica no ciclo de confirmação/faturamento)
- Criar **ScheduledAction** (jobs agendados via Cuckoo)
- Estruturar as camadas **service**, **repository**, **exception** e **dto**
- Gerar **XML do Construtor de Telas** (criação de tabelas e telas via metadados)
- Criar **popups personalizados** via `PopUpBuilder` (confirmação, seleção em grid, formulário, wizard)
- Seguir os **antipadrões proibidos** e boas práticas da plataforma

---

## Estrutura da Skill

```
sankhya-modulo-java/
├── SKILL.md                            Instruções principais da skill
├── README.md                           Este arquivo
│
├── instructions/
│   └── encoding-instructions.md        ISO-8859-1 obrigatório — regras e comandos de conversão
│
├── evals/
│   └── evals.json                      Casos de teste para avaliação da skill
│
├── examples/                           Templates Java prontos para copiar
│   ├── Modelo_ActionButton.java        AcaoRotinaJava — valida UI, abre sessão, delega para component/
│   ├── Modelo_Event.java               EventoProgramavelJava com 7 métodos, delega para component/
│   ├── Modelo_Job.java                 ScheduledAction — abre sessão, delega para component/
│   ├── Modelo_RegraNegocio.java        RegraNegocioJava completo
│   ├── Modelo_RegraPreferencia.java    Interface Regra via preferência
│   ├── Modelo_Service.java             Service — regras puras sem acesso a banco
│   ├── Modelo_Repository.java          Repository — acesso a dados para entidades AD_*
│   ├── Modelo_Exception.java           Exceção de domínio com códigos rastreáveis [MOD_NNNN]
│   ├── Modelo_Dto.java                 DTO com construtor a partir de DynamicVO
│   ├── Modelo_JapeHelper.java          Gerência de sessão e transação
│   ├── Modelo_PopUpHelper.java         Popup via PopUpBuilder
│   └── PopUpBuilder.java               Utilitário não nativo — copiar para utils/
│
├── assets/
│   └── popup/                          Templates HTML/JS de popup
│       ├── PopUpConfirmacao.html / .js
│       ├── PopUpSelecao.html / .js
│       ├── PopUpFormulario.html / .js
│       ├── PopUpDetalhes.html / .js
│       └── PopUpWizard2Paginas.html / .js
│
└── references/                         Documentação técnica detalhada
    ├── estrutura-modulo.md             Pacotes, diretórios, build.gradle, deploy
    ├── event-java.md                   EventoProgramavelJava, padrões, ModifyingFields
    ├── action-button.md                AcaoRotinaJava, ContextoAcao, padrões
    ├── component.md                    Component — orquestração, padrões por artefato
    ├── controller.md                   Controller — endpoint REST/serviço, registro manual
    ├── service-repository.md           Service (puro), Repository, Exception, DTO
    ├── regra-negocio.md                RegraNegocioJava, Regra, ScheduledAction
    ├── acesso-dados.md                 JapeFactory, DwfUtils, EntityFacade, JdbcWrapper
    ├── nativesql-assertivo.md          NativeSql utilitários, MapUtils, IN chunking — quando JAPE não resolve
    ├── boas-praticas.md                Erros, logging, transações, performance, lote, EntityFacade, máquina de estados
    ├── logger.md                       Logger (br.com.sankhya.utils.Logger), níveis, exemplos
    ├── entidades-sistema.md            DynamicEntityNames, campos TGFCAB/TGFITE/TGFFIN
    ├── construtor-de-telas.md          XML de metadados, campos, relacionamentos
    ├── popup-personalizado.md          PopUpBuilder, HTML/JS, Angular, regras críticas
    ├── sankhyautil.md                  StringUtils, TimeUtils, SQLUtils, JsonUtils e outros
    ├── comercial-notas.md              CACHelper, ImpostosHelpper, CentralFinanceiro, confirmar nota
    ├── organizacao-pacotes-java.md     Conflitos de ClassLoader, segmento nomedemanda obrigatório
    ├── clean-code-metodos.md           Nomes, tamanho, return early, SRP, efeitos colaterais
    └── clean-code-variaveis.md         Nomes, constantes, booleanos, escopo, convenções Sankhya
```

---

## Arquitetura de Camadas

```
br.com.sankhya.dstech.
  nomedemanda/
    actionbutton/    ← AcaoRotinaJava — validação de UI, abre sessão, delega para component/
    component/       ← Hub obrigatório — orquestra service/ e repository/; chamado por todos os artefatos
    controller/      ← Endpoint REST/serviço via ServiceProvider manual — delega para component/
    event/           ← EventoProgramavelJava — extrai VO, delega para component/
    job/             ← ScheduledAction — abre sessão, delega para component/
    regra/           ← RegraNegocioJava / Regra — delega para component/
    service/         ← Regras de negócio puras — cálculos, validações; sem acesso a banco
    repository/      ← Acesso a dados — entidades AD_* e queries nativas via NativeSql
    exception/       ← Exceções de domínio com código rastreável [MOD_XXXX]
    dto/             ← Transferência de dados entre camadas
    enums/           ← AdicionalEntityNames, StatusXxx, TipoXxx
    helper/          ← Helpers de apresentação (PopUpHelper) compartilhados na demanda
    utils/           ← DwfUtils (consultas genéricas), MessageUtils (feedback ao usuário)
```

> Para entidades nativas (TGFCAB, TGFPAR, TGFPRO, etc.) o `component/` acessa `JapeFactory` ou
> `DwfUtils` diretamente — sem `repository/` dedicado. O `repository/` customizado é focado em
> entidades `AD_*` e queries que precisam de NativeSql.
>
> SQL complexo: arquivos `.sql` ficam em `Java/resources/sql/` e são carregados via
> `getResourceAsStream("/sql/nome-query.sql")` no `repository/`.

---

## Módulo Java vs. Addon Studio

| Aspecto | Módulo Java | Addon Studio |
|---|---|---|
| Registro de artefatos | Manual via UI do Sankhya | Automático via anotações |
| Eventos | `EventoProgramavelJava` (manual) | `@Listener` (automático) |
| Botões de ação | `AcaoRotinaJava` (manual) | `@ActionButton` (automático) |
| Jobs agendados | `ScheduledAction` org.cuckoo.core | `@Job` (automático) |
| Regras de negócio | `RegraNegocioJava` / `Regra` (manual) | `@BusinessRule` (automático) |
| Frontend | Popups via `PopUpBuilder` | xhtml5, SankhyaJS, Design System |
| Telas/Tabelas | XML Construtor de Telas (manual) | `datadictionary/` (deploy automático) |
| Build | Gradle → JAR → importação manual | Gradle → deploy automático |
| Pacote raiz | `br.com.sankhya.dstech` | `br.com.empresa.addon` |

---

## Licença

Uso interno — DSTech Soluções.
