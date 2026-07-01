---
name: sankhya-modulo-java
description: |
  Esta skill deve ser utilizada quando o usuário mencionar módulo Java Sankhya,
  EventoProgramavelJava, AcaoRotinaJava, RegraNegocioJava, ScheduledAction, JapeFactory,
  DwfUtils, MGEModelException, DynamicEntityNames, AdicionalEntityNames, CustomModuleLoader,
  Construtor de Telas, JapeSession, EntityFacade, helpers dstech, ou qualquer desenvolvimento
  Java para Sankhya OM que não utiliza as anotações @ActionButton/@Listener/@Job do Addon Studio.
  Também acionar para: "módulo java", "evento programável", "botão de ação manual",
  "tela personalizada", "metadados sankhya", "importar módulo", "criar evento",
  "criar trigger", "registrar botão ação", "construtor de telas",
  "JAR sankhya", "deploy módulo java", "módulo complementar sankhya".
  Também acionar para segurança (SQL injection em NativeSql, audit trail, deserialização
  insegura, PCI/PDV, certificado SEFAZ, upload de anexo) e compatibilidade SQL
  Oracle/SQL Server (type mapping, funções proibidas como NVL/DECODE/SYSDATE).
---

# Módulos Java Sankhya OM

Especialidade: desenvolvimento de módulos Java complementares para Sankhya OM sem Addon Studio.
Domínio: API interna Sankhya, eventos programáveis, botões de ação manuais, regras de negócio,
jobs agendados, helpers reutilizáveis e criação de telas via Construtor de Telas (XML).

**Idioma:** Respostas em Português do Brasil. Nomenclatura técnica no código permanece em inglês.

**Regra de ouro:** Completar o fluxo de raciocínio antes de gerar qualquer código.

**Leitura proporcional à complexidade:** Para perguntas simples (sintaxe de um método, nome de um campo, estrutura básica de um artefato já conhecido), responda diretamente sem carregar todas as referências. Leia apenas o arquivo do artefato em questão. Carregar todo o conjunto de referências é obrigatório apenas quando a tarefa envolve múltiplos artefatos, integração entre camadas, ou decisão de arquitetura.

> **NUNCA** usar anotações `@ActionButton`, `@Listener`, `@Job`, `@Service`, `@BusinessRule`.
> **NUNCA** sugerir sankhya-js, Design System, xhtml5 ou qualquer artefato do Addon Studio.

---

## Pergunta Inicial Obrigatória

Antes de qualquer análise ou implementação, confirmar com o usuário:

> "Este projeto usa **Módulo Java** (JAR importado manualmente, sem Addon Studio) ou **Addon Studio** (projeto gerado pelo Addon Studio com anotações `@ActionButton`, `@Listener`, `@Job`)?"

- **Módulo Java** → prosseguir com esta skill
- **Addon Studio** → informar que a skill correta é `sankhya-addon` e encerrar

---

## Pacote Padrão

Raiz: `br.com.sankhya.dstech`. Substituir `nomedemanda` pelo nome real do módulo
(ex: `ordemcoleta`, `registroamostra`, `contratos`).

```
br.com.sankhya.dstech.
  nomedemanda/
    actionbutton/		← AcaoRotinaJava
    component/			← Hub de orquestração — chamado por todos os artefatos
    controller/			← Endpoints REST/serviço (ServiceProvider manual)
	enums/				← AdicionalEntityNames, StatusXxx, TipoXxx
	exception/			← Exceções
    event/				← EventoProgramavelJava 
	dto/				← representar entidade de domínio / transferência de dados
	job/				← ScheduledAction (org.cuckoo.core) 
	regra/				← Ligada a Regra nas Centrais
	repository/			← Operação de persistência de dados 
	service/			← Regras de negócio puras de domínio
	helper/				← Helpers transversais reutilizáveis
	utils/				← DwfUtils, MessageUtils
  
```

Detalhes de build, Gradle e deploy → `references/estrutura-modulo.md`

---

## Responsabilidade por Camada

| Camada | Responsabilidade | Proibido |
|---|---|---|
| `actionbutton/` | Recebe `ContextoAcao`, Validações de UI/interação: "nenhuma linha selecionada", "campo obrigatório do formulário vazio". Confirmações de intenção do usuário | Regras de negócio, Acesso a banco de dados, Lógica que poderia ser reutilizada por outro lugar|
| `component/` | Hub de orquestração. Ponto de entrada para todos os artefatos (`actionbutton/`, `event/`, `job/`, `regra/`, `controller/`). Coordena chamadas entre `service/` e `repository/`. Trata exceções de infraestrutura e dá-lhes significado de negócio | Regras de negócio puras (delegar para `service/`), acesso direto a banco (usar `repository/`) |
| `controller/` | Expõe operações como endpoints REST/serviço via `ServiceProvider` manual. Gerencia sessão com `JapeHelper`. Delega toda lógica para `component/` | Regras de negócio, acesso a banco de dados |
| `enums/` | Enums de domínio, `AdicionalEntityNames` | — |
| `event/` | Recebe `PersistenceEvent`, extrai `DynamicVO`. Validações e `.set()` na própria entidade do evento. Delega para `component/`. 7 métodos obrigatórios | Regras de negócio complexas, orquestração entre múltiplas entidades |
| `exception/` | Estende `Exception`, tratar mensagens para o usuário de exceções | Regras de negócio |
| `dto/` | Representar entidade de domínio | Regras de negócio |
| `job/` | `onTime()`, delega para `component/` | Regras de negócio |
| `regra/` | `executa()` ou `afterUpdate()`, delega para `component/` | Regras de negócio |
| `repository/` | Acesso a dados | Regras de negócio |
| `service/` | Regras de negócio puras de domínio: cálculos, validações complexas, transformações. Sem acesso a banco, sem orquestração | Acesso a banco de dados, chamadas a `repository/`, orquestração entre entidades |
| `helper/` | Lógica reutilizável entre módulos/demandas. Para lógica interna à demanda, usar `service/` e `repository/`. **Exceção:** helpers de apresentação (`PopUpHelper`) que são compartilhados por múltiplos artefatos da mesma demanda (`actionbutton/`, `event/`, `regra/`) | - |
| `utils/` | `DwfUtils` (consultas genéricas), `MessageUtils` (feedback) | — |


---

## Fluxo de Raciocínio (Obrigatório)

Percorrer antes de gerar qualquer código:

```
Problema
→ Artefato correto (actionbutton/ / component/ / controller/ / enums / event / DTO / job / regra / repository / service / helper / utils)
→ Entidade(s) — DynamicEntityNames ou AdicionalEntityNames
→ Dados e campos necessários
→ Regras de negócio
→ Camadas envolvidas (action/event/job/regra/controller → component → service → repository)
→ Tratamento de erros (MGEModelException)
→ Registro manual necessário (tipo, entidade, classe)
→ XML Construtor de Telas (se nova tabela/tela for necessária)
→ Código
```

Se faltar informação crítica — entidade alvo, tipo de evento, campos, regra esperada —
perguntar antes de implementar.

---

## Heurísticas de Escolha de Artefato

| Artefato | Quando usar |
|---|---|
| `AcaoRotinaJava` | Ação manual disparada pelo botão "Ações" em uma tela. É a interface entre o usuário e o sistema. Recebe a requisição, valida o mínimo necessário para a interação e delega o trabalho real para `component/`. |
| Component | Classe Java simples (sem anotação). Hub de orquestração chamado por todos os artefatos. Coordena `service/` e `repository/`. Use quando múltiplos artefatos precisam disparar a mesma operação. |
| Controller | Classe Java simples registrada manualmente via `ServiceProvider`. Use quando a operação precisa ser exposta como endpoint REST/serviço acessível externamente ao módulo. Gerencia sessão com `JapeHelper`. |
| Enum | Estados, tipos e valores fixos — substituir strings mágicas |
| Exception | Mensagens de exceções para o usuário. |
| `EventoProgramavelJava` | Lógica automática em CRUD de uma entidade (before/after insert/update/delete). Delega para `component/`. |
| dto | Quando precisas agrupar campos para trafegar entre camadas. Quando um Registro[] do JAPE não é suficiente para representar o que precisas. Para mapear resultado de queries complexas |
| `ScheduledAction` | Tarefa/Ações agendada — processamento periódico |
| `RegraNegocioJava` / `Regra` | Lógica no ciclo de confirmação/faturamento de nota |
| Repository | Operações de persistência — queries, inserts, updates, deletes via JAPE ou NativeSql, preferência JAPE para desencadear outros eventos, usar NativeSql quando não quiser desencadear outros eventos |
| Service | Regras de negócio puras: cálculos, validações de domínio, transformações. Sem acesso a banco, sem orquestração. |
| Helper estático | Lógica reutilizável entre artefatos; métodos estáticos, construtor privado |
| XML Construtor de Telas | Criar/atualizar tabela e tela; empacotar no ZIP de metadados |
| `PopUpBuilder` | UI rica em botão de ação: seleção em grid, formulário, confirmação complexa |

**Regra de UI:** `ctx.confirmarSimNao()` só existe em `AcaoRotinaJava`. Em `EventoProgramavelJava`
e `RegraNegocioJava`, usar `PopUpBuilder` via `MessageUtils.showInfo()` para perguntas e coleta
de dados do usuário. Detalhes → `references/popup-personalizado.md`

---

## Padrões Críticos

Padrões mínimos — usados mesmo sem carregar referências completas.

### Padrão 1 — AcaoRotinaJava

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    if (ctx.getLinhas().length == 0) {
        ctx.setMensagemRetorno("Selecione ao menos um registro!");
        return;
    }
    BigDecimal id = BigDecimalUtil.getBigDecimal(ctx.getLinhas()[0].getCampo("ID_CAMPO"));

    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();
        NomeComponent component = new NomeComponent();
        ctx.setMensagemRetorno(component.executarOperacao(id));
    } catch (NomeDemandaException e) {
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        throw MGEModelException.prettyMsg("Erro inesperado: <br>" + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

### Padrão 2 — EventoProgramavelJava (7 métodos obrigatórios)

```java
public class NomeEvento implements EventoProgramavelJava {

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        BigDecimal id = vo.asBigDecimal("ID_CAMPO");
        if (BigDecimalUtil.isNullOrZero(id)) return;

        NomeComponent component = new NomeComponent();
        component.processarEvento(id, vo);
    }

    @Override public void beforeInsert(PersistenceEvent event) throws Exception {}
    @Override public void afterInsert(PersistenceEvent event) throws Exception {}
    @Override public void afterUpdate(PersistenceEvent event) throws Exception {}
    @Override public void beforeDelete(PersistenceEvent event) throws Exception {}
    @Override public void afterDelete(PersistenceEvent event) throws Exception {}
    @Override public void beforeCommit(TransactionContext tranCtx) throws Exception {}
}
```

### Padrão 3 — Component (hub de orquestração)

```java
public class NomeComponent {

    private final NomeRepository nomeRepository = new NomeRepository();
    private final NomeService nomeService = new NomeService();

    public String executarOperacao(BigDecimal id) throws Exception {
        DynamicVO vo = nomeRepository.buscarPorId(id);
        if (vo == null) throw NomeDemandaException.naoEncontrado("NomeDemanda", id);

        nomeService.validar(vo);
        nomeRepository.atualizarStatus(id, "P");
        return "Operação executada com sucesso.";
    }
}
```

---

## Encoding

Todas as classes Java criadas devem usar **ISO-8859-1** como encoding do arquivo fonte (declaração `// -*- coding: ISO-8859-1 -*-` ou configuração do editor/build). Strings literais com acentos devem ser escritas diretamente — nunca usar escapes Unicode (`\uXXXX`) para caracteres do português.

---

## Antipadrões Proibidos

- Lógica de negócio em eventos ou botões — sempre delegar para `component/`
- Artefato (`actionbutton/`, `event/`, `job/`, `regra/`) chamando `repository/` diretamente — passar pelo `component/`
- `component/` com lógica de negócio pura — extrair para `service/`
- SQL ou consulta dentro de loop — usar `IN` ou processar fora do loop
- `JapeSession.open()` sem `finally { JapeSession.close(hnd); }`
- Capturar `Exception` sem relançar — nunca engolir silenciosamente
- `try-catch` para verificar campo em `DynamicVO` — usar `vo.containsProperty("CAMPO")`
- Helpers instanciáveis — construtor privado lançando `UnsupportedOperationException`
- Criar `component/` ou `controller/` sem antes verificar `references/component.md` e `references/controller.md`
- Criar `service/` ou `repository/` sem antes verificar `references/service-repository.md`
- Usar NativeSql/JdbcWrapper quando o objetivo é exatamente NÃO disparar eventos Sankhya — nunca para "economizar código".

---

## Checklist Antes de Responder

### Artefato e estrutura
- [ ] Artefato correto com justificativa
- [ ] Pacote correto (`nomedemanda/event/`, `nomedemanda/actionbutton/`, etc.)
- [ ] Javadoc com bloco `Configuração no Sankhya` (entidade, tipo, classe)
- [ ] Instruções de registro manual incluídas na resposta

### Código Java
- [ ] Evento implementa todos os 7 métodos de `EventoProgramavelJava`
- [ ] Helper com construtor privado e métodos estáticos
- [ ] Enum no lugar de strings mágicas
- [ ] Encoding do arquivo fonte: **ISO-8859-1** (nunca UTF-8) — converter com Python3/iconv após geração → `instructions/encoding-instructions.md`
- [ ] Pacote inclui segmento `nomedemanda` — nunca classes direto em `br.com.sankhya.dstech.{camada}`

### Camadas e fluxo
- [ ] Artefatos Sankhya delegam para `component/` — nunca acessam `repository/` ou `service/` diretamente
- [ ] `component/` orquestra `service/` (regras puras) e `repository/` (dados) — sem lógica de negócio inline
- [ ] `service/` sem acesso a banco, `repository/` sem regras de negócio

### JapeSession e transação
- [ ] `JapeSession.open()` com `finally { JapeSession.close(hnd); }`

### Núcleo comercial (quando aplicável)
- [ ] Nota criada via `CACHelper` + `PrePersistEntityState` — nunca via `JapeWrapper.create()` direto em `CabecalhoNota`
- [ ] `ImpostosHelpper.setForcarRecalculo(true)` quando itens foram adicionados programaticamente
- [ ] Flag `JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true)` removida no `finally`

### Acesso a dados e exceções
- [ ] `NomeModuloException` lançada no `service/`, convertida para `MGEModelException` na borda (`actionbutton/`, `event/`)
- [ ] `MGEModelException` para erros de negócio, sem engolir exceções
- [ ] `vo.containsProperty()` antes de acessar campos opcionais
- [ ] Sem SQL dentro de loop

### Qualidade
- [ ] Logger: usar `br.com.sankhya.dstech.utils.Logger` — `Logger.info()` para rastreamento de fluxo, `Logger.error(mensagem, e)` em todo bloco catch com exceção real

---

## Estrutura de Resposta

1. **Explicação** — O que será feito e por quê
2. **Artefato escolhido** — Com justificativa
3. **Arquivos a criar ou alterar** — Caminhos e pacotes completos
4. **Código completo** — Com Javadoc `Configuração no Sankhya`
5. **XML do Construtor de Telas** — Se nova tabela/tela for necessária
6. **Como registrar no Sankhya** — Passos pós-deploy do JAR
7. **Como testar** — Validação do funcionamento

---

## Exemplos

**Artefatos Sankhya** — em `examples/`:

| Arquivo | O que demonstra |
|---|---|
| `Modelo_Event.java` | `EventoProgramavelJava` com 7 métodos e delegação para `component/` |
| `Modelo_ActionButton.java` | `AcaoRotinaJava` com validação, JapeSession, delegação para `component/` e catches separados |
| `Modelo_Job.java` | `ScheduledAction` com `JapeSession` e logger |
| `Modelo_RegraNegocio.java` | `RegraNegocioJava`: sucesso/msgError, isItem, confirmação, limite |
| `Modelo_RegraPreferencia.java` | Interface `Regra` via preferência `MODREGCENTRAL` |

**Camadas de arquitetura** — em `examples/`:

| Arquivo | O que demonstra |
|---|---|
| `Modelo_Service.java` | Service com regras de negócio puras — validação, cálculo e transformação sem acesso a banco |
| `Modelo_Repository.java` | Repository com leitura, escrita JAPE (dispara eventos) e NativeSql (não dispara eventos) |
| `Modelo_Exception.java` | Exceção de domínio com códigos rastreáveis e fábrica de mensagens |
| `Modelo_Dto.java` | DTO com construtor a partir de DynamicVO — quando usar e quando não usar |

**Utilitários** — em `examples/`:

| Arquivo | O que demonstra |
|---|---|
| `Modelo_JapeHelper.java` | Gerência de sessão e transação — `executeWithTx`, `executeWithoutTx` |
| `PopUpBuilder.java` | Classe utilitária não nativa — copiar para `utils/` antes de usar popups |
| `Modelo_PopUpHelper.java` | Popup via `PopUpBuilder` — helper de apresentação compartilhado entre artefatos |

**Templates HTML/JS de popup** — em `assets/popup/`:
`PopUpConfirmacao`, `PopUpSelecao`, `PopUpFormulario`, `PopUpDetalhes`

---

## Referências

Carregar o arquivo ao aprofundar um tópico:

| Tópico | Quando carregar | Arquivo |
|---|---|---|
| Estrutura do projeto, diretórios, `build.gradle`, deploy | Dúvidas sobre organização de diretórios, Gradle ou processo de importação do JAR | `references/estrutura-modulo.md` |
| `EventoProgramavelJava` — padrões, registro, `ModifyingFields` | Ao criar ou modificar evento CRUD em qualquer entidade | `references/event-java.md` |
| `AcaoRotinaJava` — `ContextoAcao`, formulário de parâmetros, confirmação | Ao criar ou modificar botão de ação | `references/action-button.md` |
| `RegraNegocioJava`, `Regra`, `ScheduledAction`, `Job` | Ao criar regra no ciclo de notas ou job agendado | `references/regra-negocio.md` |
| `JapeFactory`, `DwfUtils`, `EntityFacade`, `JdbcWrapper`, `JapeSession` | Ao lidar com persistência, queries nativas, sessão ou transação | `references/acesso-dados.md` |
| `NativeSql` assertivo — `getResultSetAsCollection`, `getColumnsAsMap`, `MapUtils`, `IN` clause chunking | Ao escrever queries nativas no `repository/` quando JAPE não resolve | `references/nativesql-assertivo.md` |
| Component — orquestração, padrões por artefato, tratamento de exceções | Ao criar ou revisar a camada `component/` | `references/component.md` |
| Controller — endpoint REST/serviço, registro manual, gestão de sessão | Ao criar ou revisar endpoint exposto via `ServiceProvider` | `references/controller.md` |
| Service, Repository, Exception, DTO — responsabilidades e integração | Ao criar qualquer uma dessas camadas ou decidir onde colocar lógica | `references/service-repository.md` |
| Boas práticas — erros, logging, transações, performance | Qualquer decisão de "como fazer certo" — logging, transações, antipadrões | `references/boas-praticas.md` |
| Entidades nativas — `DynamicEntityNames`, campos `TGFCAB`/`TGFITE`/`TGFFIN` | Quando precisar de nomes corretos de entidades ou campos nativos | `references/entidades-sistema.md` |
| Popups — `PopUpBuilder`, HTML/JS, `ServiceProxy` | Ao criar popup de confirmação, seleção em grid ou formulário modal | `references/popup-personalizado.md` |
| XML Construtor de Telas — campos, relacionamentos, deploy com JAR | Ao criar nova tabela `AD_*` ou tela via metadados | `references/construtor-de-telas.md` |
| Logger — níveis, boas práticas, exemplos certo/errado | Ao adicionar logging em qualquer classe | `references/logger.md` |
| SankhyaUtil — `StringUtils`, `TimeUtils`, `SQLUtils`, `JsonUtils`, `XMLUtils`, `JDBCUtils`, `BigDecimalUtil`, `CollectionUtils`, `SessionFile` | Ao manipular strings, datas, decimais, JSON, XML ou coleções | `references/sankhyautil.md` |
| Núcleo comercial — `CACHelper`, `ImpostosHelpper`, `CentralFinanceiro`, confirmar nota, `execWithTX`/`execWithFakeTX` | Ao criar ou faturar notas programaticamente | `references/comercial-notas.md` |
| Parâmetros do Sistema — `MGECoreParameter`, leitura TSIPAR com fallback | Ao ler parâmetros configurados em Preferências → Parâmetros do Sistema | `references/parametros-sistema.md` |
| Organização de pacotes — conflitos de ClassLoader, segmento `nomedemanda` | Ao criar novo módulo ou adicionar camadas | `references/organizacao-pacotes-java.md` |
| Clean Code — métodos: nomes, tamanho, return early, SRP, efeitos colaterais | Em qualquer revisão ou criação de método | `references/clean-code-metodos.md` |
| Clean Code — variáveis: nomes, constantes, booleanos, escopo, coleções | Em qualquer revisão ou criação de variável | `references/clean-code-variaveis.md` |
| Encoding de arquivos — ISO-8859-1 obrigatório em `.java` e `.xml`, como converter, antipadrões | Ao criar ou editar qualquer arquivo `.java` ou `.xml` | `instructions/encoding-instructions.md` |