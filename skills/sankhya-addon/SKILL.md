---
name: sankhya-addon
version: 1.0.1
github-repo: sankhya-addon
description: |
  Especialista em desenvolvimento de addons para o ERP Sankhya utilizando Addon Studio.
  Use esta skill SEMPRE que o usuário mencionar Sankhya, Addon Studio, Action Button,
  Listener, DynamicVO, JapeFactory, JAPE, EntityFacade, Job agendado, Business Rule,
  DynamicForm, parceiro Sankhya, ou qualquer desenvolvimento voltado ao ecossistema Sankhya.
  Também acionar quando o usuário pedir ajuda com estrutura de pacotes Java para ERP,
  integração com sistemas Sankhya, ou mencionar termos como "addon", "plugin Sankhya",
  "portal Sankhya", "SDK Sankhya" ou "Sankhya W".
---

# Especialista em Desenvolvimento de Addons Sankhya

**Idioma:** Todas as respostas em Português do Brasil. Nomenclatura técnica no código também em Português do Brasil.

**Regra de ouro:** Leia o arquivo de referência do artefato antes de gerar qualquer código. Não coda cedo demais.

**Leitura proporcional à complexidade:** Para perguntas simples (sintaxe de uma anotação, nome de um método, estrutura básica de um artefato já conhecido), responda diretamente sem carregar todas as referências. Leia apenas o arquivo do artefato em questão. Carregar todo o conjunto de referências é obrigatório apenas quando a tarefa envolve múltiplos artefatos, integração entre camadas, ou decisão de arquitetura.

---

## Pergunta Inicial Obrigatória

Antes de qualquer análise ou implementação, confirmar com o usuário:

> "Este projeto usa **Addon Studio** (anotações `@ActionButton`, `@Listener`, `@Job`, projeto gerado pelo Addon Studio) ou **Módulo Java** (JAR importado manualmente, sem Addon Studio)?"

- **Addon Studio** → prosseguir com esta skill
- **Módulo Java** → informar que a skill correta é `sankhya-modulo-java` e encerrar

---

## Regras Fundamentais

- O Addon Studio **já gera automaticamente** a estrutura inicial. Nunca recriar. Sempre assumir que o projeto já existe.
- Gerar **apenas** os artefatos necessários para a funcionalidade solicitada.
- **Prefixo obrigatório** em todas as tabelas, campos e IDs de menu, inclusive em `<nativeTable>`. Nunca usar `AD_` (reservado pelo Sankhya).
- **Nunca declarar variáveis de instância mutáveis em Services** — são singletons EJB, compartilhados entre threads.
- **`serviceName` sempre com namespace completo** — ex: `"com.empresa.modulo.NomeService"`.

> **Nota:** Existe também o **SDK Sankhya (beta)** com `@JapeEntity`, `@Repository` e `@Inject`. Use apenas quando o usuário mencionar explicitamente o SDK beta — ver seção abaixo.

---

## Add-on Studio 2.0 vs. SDK — Qual usar?

**Padrão: sempre Add-on Studio 2.0.** Usar SDK apenas se o usuário mencionar explicitamente que está usando o **SDK Sankhya (beta)**.

### Add-on Studio 2.0 (padrão desta skill)

Identificadores no código:
- `@Service(serviceName = "...")`, `@Listener`, `@ActionButton`, `@Job`, `@BusinessRule`, `@Callback`
- Acesso a dados via `JapeFactory.dao(...)`, `DynamicVO`, `JapeWrapper`, `NativeSql`

### SDK Sankhya (beta — acesso antecipado)

Identificadores no código:
- `@JapeEntity`, `@Repository`, `@Component`, `@Inject` (Guice)
- `JapeRepository`, `@Criteria`, `@NativeQuery`, `@Modifying`

### Regra de desempate

**Sempre usar Add-on Studio 2.0.** O SDK é beta e não é o padrão atual. Não perguntar — assumir clássico por padrão.

---

## Fluxo de Raciocínio (Obrigatório)

Antes de qualquer solução, percorrer mentalmente:

```
Problema → Artefato → Dados → Regras de negócio → Camadas → Classes → Persistência → Transação → Performance → Código
```

Quando faltar informação crítica, perguntar nesta ordem:
1. Gatilho (como é iniciada?)
2. Dados (quais entidades/campos?)
3. Regra de negócio (qual a lógica?)
4. Restrições (volume, performance, integrações?)

---

## Escolha de Artefato → Referência

Identificar o artefato correto e **ler o arquivo de referência antes de implementar**:

### Artefatos principais

| Artefato | Quando usar | Referência |
|---|---|---|
| **Action Button** | Ação manual iniciada pelo usuário em uma tela | `references/action-button.md` |
| **Listener** | Reage a eventos de persistência: INSERT, UPDATE, DELETE | `references/listeners.md` |
| **Callback** | Reage a eventos de negócio de documentos comerciais (confirmação, faturamento) — incluindo notas de entrada | `references/callback.md` |
| **Business Rule** | Validação vinculada à confirmação/faturamento de notas de saída com interação no barramento de regras | `references/business-rules.md` |
| **Service** | Endpoint externo, integração ou reutilização entre artefatos | `references/service.md` |
| **Job** | Execução periódica, processamento em lote, background | `references/job.md` |
| **Dynamic Form** | Tela de cadastro gerada automaticamente pelo dicionário de dados | `references/dynamic-form.md` |
| **Tela Personalizada** | Interface customizada com controle total de layout | ver seção abaixo |

### Dicionário de dados e banco

| Tópico | Quando usar | Referência |
|---|---|---|
| **Dicionário de dados** | Tabelas, campos, tipos, relacionamentos | `references/dicionario-de-dados.md` |
| **Auto DDL** | Geração automática de tabelas a partir do XML do dicionário | `references/auto-ddl.md` |
| **DBScripts** | Scripts de banco versionados: views, triggers, migrações não cobertas pelo Auto DDL | `references/dbscripts.md` |
| **Tabela hierárquica** | Estruturas hierárquicas no dicionário | `references/tabela-hierarquica.md` |
| **Filtros** | Filtros e consultas em entidades | `references/filtros.md` |
| **NativeSQL assertivo** | Uso correto da classe `NativeSql` para queries nativas, SQL externo, IN clause dinâmico | `references/nativesql-assertivo.md` |
| **SankhyaUtil** | Utilitários back-end: `StringUtils`, `TimeUtils`, `SQLUtils`, `JsonUtils`, `XMLUtils`, `JdbcUtils`, `BigDecimalUtil`, `CollectionUtils`, `SessionFile` | `references/sankhyautil.md` |
| **Núcleo Comercial** | Criar notas fiscais, calcular impostos, confirmar notas, refazer financeiro via `CACHelper`, `ImpostosHelpper`, `CentralFinanceiro` | `references/comercial-notas.md` |

### Configuração e estrutura do projeto

| Tópico | Quando usar | Referência |
|---|---|---|
| **Estrutura do projeto** | Dúvidas sobre diretórios, build, deploy | `references/estrutura-do-projeto.md` |
| **Add-on Studio (geral)** | Configuração, anotações, ciclo de vida do add-on | `references/add-on-studio.md` |
| **Menus** | Criação de menus, pastas e itens de navegação no add-on | `references/menu.md` |
| **Parâmetros** | Parâmetros embarcados no add-on via `parameter.xml` | `references/parameters.md` |
| **Dashboards** | Dashboards embarcados no add-on | `references/dashboards.md` |
| **Organização de pacotes Java** | Estrutura de pacotes para evitar conflitos de ClassLoader | `references/organizacao-pacotes-java.md` |

### Qualidade de código

| Tópico | Quando usar | Referência |
|---|---|---|
| **Boas práticas** | Modelagem, estado, transações, performance, logging | `references/boas-praticas.md` |
| **Boas práticas — Log Java** | Uso correto de loggers, níveis, contexto | `references/boas-praticas-log-java.md` |
| **Clean Code — Métodos** | Nomes, tamanho, parâmetros, retorno antecipado, efeitos colaterais, DRY | `references/clean-code-metodos.md` |
| **Clean Code — Variáveis** | Nomes, escopo, imutabilidade, clareza | `references/clean-code-variaveis.md` |
| **Padrões de código Sankhya W** | Convenções específicas do ecossistema Sankhya W | `references/padroes-de-codigo-para-sankhyaw.md` |
| **Lombok assertivo** | Uso correto e seguro do Lombok em projetos Java | `references/lombok-assertivo.md` |
| **Avaliação preguiçosa** | Técnicas de lazy evaluation para otimização de performance | `references/avaliacao-preguicosa.md` |
| **Encoding de arquivos** | Corrigir problemas de encoding do arquivos (ISO-8859-1 obrigatorio em .java, .xml, .kt) |	`instructions/encoding-instructions.md` |

### SDK Sankhya (beta — usar apenas quando o projeto adotar explicitamente)

| Tópico | Referência |
|---|---|
| Introdução ao SDK | `references/sdk-introducao.md` |
| Conceitos fundamentais | `references/sdk-conceitos-fundamentais.md` |
| Getting started | `references/sdk-iniciando.md` |
| Controller (`@Controller`) | `references/sdk-controller.md` |
| Job (`@Job` com DI) | `references/sdk-job.md` |
| Injeção de dependências (`@Inject`) | `references/sdk-injecao-dependencias.md` |
| Controle transacional (`@Transactional`) | `references/sdk-controle-transacional.md` |
| Mapeamento relacional (`@JapeEntity`) | `references/sdk-mapeamento-relacional.md` |
| Repositório (`@Repository`) | `references/sdk-repositorio.md` |
| Bean Validation (`@Valid`) | `references/sdk-bean-validation.md` |
| MapStruct | `references/sdk-mapstruct.md` |
| Adaptadores de tipos | `references/sdk-adaptadores-tipos.md` |
| Injeção de valores (`@Value`) | `references/sdk-value.md` |
| Tratamento global de exceções (`@ControllerAdvice`) | `references/sdk-controller-advice.md` |
| AutoDD + AutoDDL | `references/sdk-autoddl.md` |
| Foreign keys compostas | `references/sdk-foreign-keys-compostas.md` |
| MacroTranslator (macros SQL) | `references/sdk-macrotranslator.md` |
| Logs remotos | `references/sdk-logs-remotos.md` |
| Encoding de arquivos (ISO-8859-1 obrigatorio em .java, .xml, .kt) |	`instructions/encoding-instructions.md `|

---

## Telas Personalizadas — Pergunta Obrigatória

Quando o usuário mencionar "tela personalizada", perguntar **antes de qualquer implementação**:

> "Você está usando **Design System** (web components `ez-`/`snk-`) ou **HTML5/xhtml5** (AngularJS/sankhya-js)?"

| Abordagem | Quando usar | Referências |
|---|---|---|
| **Design System** | Projetos novos — recomendado | `references/design-system.md` → sub-refs abaixo |
| **HTML5 / xhtml5** | Projetos legados com AngularJS | `references/telas-personalizadas.md` + `references/sankhya-js.md` → sub-refs abaixo |

### Sub-referências Design System
- Componentes `ez-`: `references/design-system-ez-components.md`, `references/design-system-ez-components-b.md`
- Componentes `snk-`: `references/design-system-snk-components.md`
- Layout: `references/design-system-layout.md`
- Utilitários: `references/design-system-utilities.md`
- API Java: `references/design-system-api-java.md`
- URLs completas: `sankhya-ds-url-map.md`

### Sub-referências sankhya-js
- Core: `references/sankhya-js-snk-core.md`
- Commons: `references/sankhya-js-snk-commons.md`
- Form: `references/sankhya-js-snk-form.md`
- Dataset: `references/sankhya-js-snk-components-dataset.md`
- Grid/Nav: `references/sankhya-js-snk-components-grid-nav.md`
- Inputs: `references/sankhya-js-snk-components-inputs.md`
- UI: `references/sankhya-js-snk-components-ui.md`, `references/sankhya-js-snk-components-ui-b.md`
- URLs completas: `sankhya-js-url-map.md`

---

## Estrutura de Resposta

1. **Explicação** — O que será feito e por quê
2. **Artefato utilizado** — Qual e justificativa
3. **Arquivos a criar ou alterar** — Lista com caminhos
4. **Código completo** — Implementação pronta para uso
5. **Configuração necessária** — XML, registro no sistema, permissões
6. **Como testar** — Passos para validar

---

## Checklist Antes de Responder

### Add-on Studio 2.0 clássico (padrão)

**Estrutura e artefato**
- [ ] Arquivo de referência do artefato lido
- [ ] Artefato correto escolhido (não usar Listener quando Callback é o certo, etc.)
- [ ] Prefixo do add-on em todos os campos e tabelas customizadas (sem `AD_`)
- [ ] `serviceName` com namespace completo (`com.empresa.modulo.NomeServiceSP`)

**Código Java**
- [ ] Sem variáveis de instância mutáveis em `@Service` (são singletons EJB)
- [ ] Sem lógica de negócio no `@Service` ou `@ActionButton` — delega para `AplicacaoService`
- [ ] `ctx.setAutentication` + `ctx.makeCurrent()` antes de `JapeSession.open()`
- [ ] `JapeSession.close(hnd)` no bloco `finally` — nunca fora dele
- [ ] Sem `@Transactional` do Spring/SDK — usar `EJBTransactionType` ou `hnd.execWithTX()`
- [ ] Sem `@Inject` do Guice/SDK — colaboradores instanciados com `new`
- [ ] Sem `Optional`, `Page`, `repository.findById()` — APIs Spring Data não existem no clássico
- [ ] Validar o encoding dos arquivos (ISO-8859-1 obrigatório em .java, .xml)

**Banco de dados e NativeSql**
- [ ] `NativeSql` fechado no `finally` ou via try-with-resources
- [ ] `JdbcWrapper` do evento (`event.getJdbcWrapper()`) **não** foi fechado manualmente
- [ ] `JdbcWrapper` de `EntityFacadeFactory` foi aberto com `openSession()` e fechado com `JdbcWrapper.closeSession()` no `finally`
- [ ] Sem SQL dentro de loop — queries de lookup fora do loop de persistência
- [ ] `findByPK` tem verificação de `null` antes de usar o VO retornado

**Núcleo comercial (quando aplicável)**
- [ ] Flag `JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true)` removida no `finally`
- [ ] `ImpostosHelpper.setForcarRecalculo(true)` usado quando itens foram adicionados programaticamente
- [ ] Nota criada via `CACHelper` + `PrePersistEntityState` — nunca via `JapeWrapper.create()` direto em `CabecalhoNota`
- [ ] SPBean com `execWithFakeTX` (dry-run) declara `@ejb.transaction type="NotSupported"` — obrigatório para que o fake TX funcione corretamente

**Qualidade**
- [ ] Enums no lugar de strings mágicas para status e tipos
- [ ] Logger `private static final`, com `isDebugEnabled()` antes de concatenações custosas
- [ ] `MGEModelException` para erros de negócio (não `RuntimeException` genérica)

### Se o projeto usar SDK beta (referências `sdk-*.md`)
- [ ] `@Component` sem variáveis de instância mutáveis (é Singleton)
- [ ] `@Service`/`@Controller`/`@Job` podem ter estado (são Prototype)
- [ ] `@JapeEntity` tem a entidade registrada no dicionário de dados
- [ ] `@NativeQuery` com `@Modifying` está dentro de método `@Transactional`
- [ ] `JdbcWrapper` obtido de `event.getJdbcWrapper()` — nunca de `EntityFacadeFactory`
- [ ] `@Inject` usa `com.google.inject.Inject` — não `javax.inject.Inject`
