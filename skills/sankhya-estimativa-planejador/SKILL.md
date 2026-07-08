---
name: sankhya-estimativa-planejador
description: >
  Esta skill deve ser utilizada quando o usuário enviar documentos funcionais como escopos,
  levantamentos de requisitos, documentações de personalização ou atas de alinhamento e quiser
  transformar o conteúdo em backlog estruturado. Acionar para: "analisar requisitos",
  "transformar escopo em backlog", "decompor feature", "gerar épicos e stories",
  "analisar documento funcional", "levantar histórias", "refinamento técnico",
  "estimar horas de desenvolvimento", "quanto tempo vai levar", "análise de escopo Sankhya".
  Quando o MCP sankhya-schema estiver disponível, valida entidades, tabelas e campos citados no
  escopo contra o schema real antes de gerar tarefas técnicas e estimativas.
  Também recomenda o empacotamento do projeto: "addon completo ou módulo Java", "vale criar um addon",
  "melhor abordagem técnica", comparando distribuição multi-cliente × entrega ponto-a-ponto.
  Não acionar para pedidos de tradução simples, revisão gramatical ou ajuste pontual de task já existente.
license: Proprietary
version: 2.11.0
---

# Sankhya Requirements Backlog Analyzer

## Objetivo

Converter documentação funcional bruta — escopos, levantamentos de regras de negócio, atas de alinhamento, especificações de feature — em um plano estruturado de implementação com backlog, estimativa de horas e recomendação de abordagem técnica (Módulo Java × Addon Studio).

Não partir direto para código. Organizar o problema em camadas antes de qualquer implementação.

---

## Resultado esperado

0. Identificação do escopo (parceiro, processo/subprocesso, usuário-chave, validação, documentos de entrada)
1. Resumo executivo do escopo
2. Domínios funcionais identificados
3. Mapa de impacto
4. Lista de epics
5. Story map por epic
6. Stories fatiadas verticalmente
7. Critérios de aceite
8. Tarefas técnicas iniciais
9. Dependências e riscos
10. Itens ambíguos para validação
11. Recomendação de abordagem técnica por epic + recomendação de empacotamento do projeto (Addon completo × Módulo-Java)
12. Estimativa de horas no template oficial de 7 fases por rotina (dois estágios — rápida e refinada), com confronto à estimativa-âncora do documento
13. Estrutura JSON para futura integração com cards

---

## Princípios de trabalho

- Separar requisito funcional, regra de negócio, detalhe técnico, dependência e premissa
- Priorizar decomposição vertical — evitar fatiamento por camada técnica no nível de story
- Preservar rastreabilidade entre requisito original e entregável proposto
- Sinalizar trechos ambíguos em vez de inventar regra
- Destacar o que é configuração, o que é desenvolvimento e o que depende de validação do cliente
- Tarefas técnicas não substituem stories — ficam dentro delas

---

## Método obrigatório

### Etapa 1 — Leitura e segmentação
**Primeiro, detectar o gênero do documento** (discovery pré-vendas, levantamento formal, requisito versionado, spec de BI, as-built/manual, **proposta comercial**) — define postura, confiança e se há estimativa a gerar. Gêneros as-built (entrega com código-fonte, manual/caso de uso) **não geram estimativa**. Proposta comercial é **Escopo Fechado** — âncora de fronteira/teto contratual, nunca fonte de estimativa de dev; cruzar com o levantamento detalhado para flagar scope creep. Descartar boilerplate D4Sign (rodapé/assinaturas). Detectar template clonado (parceiro do corpo ≠ nome do arquivo). Ver `references/generos-documento.md`.

Capturar o **cabeçalho de identificação** normalizando sinônimos (Parceiro/código, Nro. Flow, FAP, Número da OS, OS de Origem, Segmento, processo/subprocesso, usuário-chave, participantes, status de validação) → seção "0. Identificação". No discovery, capturar também **as-is** ("como é hoje", "por que o nativo não atende") e **to-be** ("como gostaria que fosse") — alimentam o Mapa de impacto.

Identificar e separar: objetivo, contexto, atores, processos, requisitos, regras de negócio, exceções, premissas, dependências externas, **dependências documentais (refs a outros documentos e a modelos visuais .jpg/.pdf)**, **itens extra-escopo**, itens condicionais, itens fora de escopo, relatórios, referências técnicas.

Lista de segmentação em `references/heuristicas-erp.md`; gêneros e seções canônicas em `references/generos-documento.md`; padrões recorrentes em `references/padroes-requisito-sankhya.md`.

### Etapa 2 — Classificação dos trechos
Classificar cada trecho: objetivo de negócio, requisito funcional, regra de negócio, detalhe técnico, integração, parametrização, permissão/alçada, relatório/dashboard, dependência externa, dependência documental, homologação de rotina nativa, item extra-escopo, premissa, restrição, dúvida/ambiguidade.

Reconhecer os padrões recorrentes (geração de NF derivada, alçada TSILIB, reprocessamento idempotente, multiempresa, conversão de unidades, tela detalhe nativa) em `references/padroes-requisito-sankhya.md` — cada um tem artefato e pegadinha de estimativa próprios.

Ver critérios detalhados em `references/heuristicas-erp.md`.

### Etapa 2.5 — Validação de entidades via MCP (quando disponível)

Se o MCP **sankhya-schema** estiver conectado, validar contra o schema real **antes** de gerar tarefas técnicas e estimar. Reduz alucinação de tabela/campo inexistente e ancora a estimativa em estrutura concreta.

Para cada referência técnica citada no escopo (tabela, entidade, campo):

| Citação no escopo | Tool MCP | Uso |
|---|---|---|
| Conceito de negócio sem tabela ("nota fiscal", "pesagem", "parceiro") | `search_entities("conceito")` | Descobrir EntityName/tabela real |
| Tabela ou EntityName citado (`TGFCAB`, `CabeçalhoNota`) | `describe_table("TGFCAB")` | Confirmar campos, tipos, nulabilidade |
| Campo citado sem tabela (`CODPARC`, `DTFATUR`) | `search_columns("CODPARC")` | Localizar em quais tabelas existe |
| Query/JOIN proposto numa tarefa técnica | `validate_query("SELECT ...")` | Validar sintaxe e existência via EXPLAIN PLAN |

Regras:
- Campo `AD_*` citado e **não encontrado** → marcar como criação de campo adicional (tarefa técnica), não como existente.
- Tabela citada inexistente → registrar em "10. Itens ambíguos para validação", não inventar estrutura.
- MCP indisponível → seguir com a skill **sankhya-dicionario** e sinalizar que entidades não foram validadas contra schema real (baixa a confiança da estimativa).

Não validar exaustivamente todo campo — focar nos que dirigem decisão técnica ou estimativa.

### Etapa 3 — Agrupamento por domínio
Agrupar em macrodomínios funcionais (pesagem, contratos, financeiro, estoque, relatórios, integrações, etc.).

### Etapa 4 — Impact Mapping
Para cada domínio gerar: objetivo operacional, atores impactados, comportamento que precisa mudar, entregas candidatas.

```md
## Domínio
### Objetivo operacional
### Atores
### Impactos esperados
### Entregas candidatas
```

### Etapa 5 — Story Mapping
Para cada epic, montar a jornada funcional em alto nível com backbone e fluxos alternativos.

```md
## Epic
### Backbone da jornada
1. passo 1 / 2. passo 2 / 3. passo 3
### Fluxos alternativos ou exceções
```

### Etapa 6 — Story Slicing
Diagnosticar complexidade do epic e fatiar pela técnica adequada (por fluxo, CRUD, ator, plataforma ou híbrido). Aplicar o **teste de valor independente** a cada story: se nenhum usuário percebe valor entregando-a isolada, é tarefa técnica (Etapa 8), não story. Evitar fatiamento por camada técnica, micro-stories e spike disfarçado.

Diagnóstico, 5 técnicas, teste de valor e anti-patterns detalhados em `references/fatiamento-criterios.md`.

### Etapa 7 — Critérios de aceite
Antes de escrever, inventariar e classificar cada critério (🔴 crítico / 🟡 atenção / 🟢 ok); refinar todo 🔴 antes de registrar. Critérios orientados a comportamento (dado / quando / então). Nunca misturar critério funcional e não-funcional no mesmo AC.

Tabela de níveis e anti-patterns de AC em `references/fatiamento-criterios.md`.

### Etapa 8 — Tarefas técnicas
Após stories, listar tarefas técnicas: criar campo, alterar rotina, implementar serviço, criar job, criar parâmetro, ajustar tela, criar relatório, criar integração.

Quando o MCP **sankhya-schema** estiver disponível, ancorar cada tarefa de persistência na estrutura validada na Etapa 2.5: citar a tabela/campo real confirmado, e diferenciar explicitamente campo existente de campo `AD_*` a criar. Tarefa técnica sobre tabela inexistente é sinal de ambiguidade — empurrar para a seção 10.

### Etapa 9 — Riscos, dependências e pontos abertos
Registrar: dependências de definição funcional, layout, parâmetros indefinidos, regras financeiras/fiscais a validar, trechos conflitantes ou vagos, **dependências documentais** (regra remetida a outro documento — story afetada entra com confiança reduzida) e **itens extra-escopo** (fora da proposta comercial — segregados do total compromissado).

### Etapa 10 — Recomendação de abordagem técnica

**Por epic** — classificar o tipo de artefato (Etapa 8). Classificações (lista canônica): `[MÓDULO JAVA]` | `[ADDON STUDIO]` | `[BI/DASHBOARD]` | `[RELATÓRIO]` | `[SCRIPT DB]` | `[CONFIGURAÇÃO]` | `[NATIVO/HOMOLOGAÇÃO]` | `[HÍBRIDO]`. Ver tabela de decisão em `references/heuristicas-erp.md`.

**Do projeto inteiro — Addon × Módulo-Java.** Decisão de projeto, em **dois eixos** (não só empacotamento):
1. **Aderência ao negócio / telas e UX sob medida** — se o processo do cliente diverge do nativo e precisa de telas próprias (não encaixa em abas/botões sobre tela nativa), recomendar **addon**, mesmo cliente único e mesmo que o nativo exista. Nativo existente **não impede** addon: nativo fraco central ao negócio é candidato a ser **transformado** (casos de projetos reais — um deles vira plataforma/base para outros addons).
2. **Distribuição/empacotamento** — produto distribuível multi-cliente, instalação versionada ou UI além do Construtor → **addon**.

Módulo-java é mais barato de desenvolver e cabe para personalização **pontual sobre processo nativo** (botão+evento, sem telas próprias). **Não rotear escopo complexo e screen-centric para módulo-java só por custo** — é o anti-pattern "vendido errado": surgir o trade-off (módulo-java mais barato porém baixa aderência; addon mais caro porém sob medida). Aplicar o scorecard de `references/addon-vs-modulo-java.md` e registrar a justificativa do sinal decisivo.

**Se a decisão for addon, hoje só o Addon Studio oficial** — frameworks de terceiros (ex.: lugh-lib) não têm mais suporte. Manutenção em addon de terceiro existente exige **conversão total para o oficial**, e a **conversão entra na estimativa** (não é ajuste pontual).

**Stack de frontend (decisão explícita por projeto).** Sempre que houver tela própria, escolher e **registrar** a stack na seção 11 e no handoff:
1. **AngularJS `sankhya-js` (DEFAULT)** — framework proprietário 1.x, **sem pipeline Node**. Estrutura de tela: `html5/<Nome>/<Nome>.html` + launcher + entrada de menu `.xhtml5`. Roteia ao agente **`sankhya-frontend-angular`**.
2. **Design System** — componentes modernos; **exige pipeline Node** (build/transpile/toolchain). Só escolher quando o projeto já o adota ou o cliente exige, e **somar o custo do toolchain Node na estimativa**. Roteia ao agente **`sankhya-frontend-design-system`**.

⚠️ **Design System sem Node configurado não builda.** Não rotear para ele projeto sem toolchain Node — na dúvida, manter o default AngularJS `sankhya-js`. Registrar o sinal decisivo da escolha.

### Etapa 11 — Estimativa de horas (dois estágios)

Gêneros as-built (entrega/manual) **não geram estimativa** — pular esta etapa e usar o documento como referência técnica.

**Estágio 1 — Estimativa rápida (sempre executar):**

Itemizar por **rotina** (1 artefato = 1 linha) e estimar na estrutura oficial de **7 fases** (Levantamento, Desenvolvimento, Homologação, Treinamento, Simulação, Documentação, Produção e acompanhamento). Para cada rotina:
1. **Desenvolvimento** = faixa base do artefato × multiplicadores detectados (com teto ×6)
2. Demais fases por cima conforme proporções (Homologação 7–12%, Simulação ~5%, Documentação piso, Produção 6–30%; Levantamento/Treinamento ~0) — concentrar Doc/Treino na rotina-âncora
3. **Confrontar com a estimativa-âncora** do documento, se houver número pré-fechado (exibir divergência)

Exibir a tabela de 7 fases por rotina + total do projeto + nível de confiança. Modelo completo e proporções em `references/template-horas-fases.md`.

⚠️ **As faixas de base vêm de planilhas vendidas e subestimam o real em ~1,6–2,2×.** Conferir contra os pesos medidos por artefato em `references/calibracao-real.md` (botão simples 8–12h; botão complexo 16–24h; **EJB/bean+Service 40–70h**; **frontend vc denso 80–160h**; repository SQL pesado 16–40h; produtividade ~12 LOC/h). Quando a abordagem for **addon com UI própria**, somar as telas vc explicitamente — é o que leva o real a 600h+ (caso Projeto A: vendida 360h × real ~460–610h). Estimar realista, não o piso comercial.

Após exibir, perguntar ao usuário:
> "Deseja refinar a estimativa das stories de complexidade MÉDIA ou ALTA gerando esqueletos de código via `sankhya-modulo-java` ou `sankhya-addon`? Isso permite uma estimativa mais próxima da realidade. (sim / não)"

**Estágio 2 — Refinamento por esqueleto (somente se usuário aceitar):**

Para cada story de complexidade MÉDIA/ALTA, consultar a tabela **"Referência de skills por artefato"** em `references/heuristicas-estimativa.md` para identificar qual skill acionar. Gerar o esqueleto do artefato (classe Java, componente frontend, gadget BI, XML DataDictionary — conforme o tipo). A partir do esqueleto, contar helpers, DAOs, componentes de tela e integrações identificadas. Recalcular a faixa e exibir estimativa rápida × refinada lado a lado. Perguntar qual o usuário deseja registrar (rápida / refinada / ambas).

Ver tabelas de base por artefato, multiplicadores, referência de skills e formato de apresentação em `references/heuristicas-estimativa.md`.

---

## Formato de saída padrão

Exemplo completo de escopo de entrada → 13 seções preenchidas em `references/exemplo-completo.md`. Consultar para ancorar nível de detalhe, rastreabilidade e uso da validação via MCP.

```md
# Análise Estruturada do Escopo

## 0. Identificação
Parceiro · Processo/Subprocesso (código) · Usuário-chave · Responsável · Status de validação · Documentos de entrada referenciados

## 1. Resumo executivo
## 2. Domínios funcionais identificados
## 3. Mapa de impacto
## 4. Epics propostos
## 5. Story map por epic
## 6. Stories propostas
## 7. Critérios de aceite
## 8. Tarefas técnicas iniciais
## 9. Dependências e riscos
## 10. Itens ambíguos para validação
## 11. Recomendação de abordagem técnica

**Abordagem geral:** [MÓDULO JAVA | ADDON STUDIO | BI/DASHBOARD | RELATÓRIO | SCRIPT DB | CONFIGURAÇÃO | NATIVO/HOMOLOGAÇÃO | HÍBRIDO]
**Empacotamento do projeto:** [MÓDULO-JAVA (default) | ADDON COMPLETO] — justificar com o sinal decisivo (scorecard addon × módulo)
**Stack de frontend:** [ANGULARJS sankhya-js (default, sem Node) | DESIGN SYSTEM (requer pipeline Node)] — registrar a escolha, o sinal decisivo e o agente de rota (`sankhya-frontend-angular` × `sankhya-frontend-design-system`)

| Epic | Abordagem | Artefatos principais | Justificativa |
|---|---|---|---|

## 12. Estimativa de horas (template oficial de 7 fases)

| Rotina (artefato) | Abordagem | Lev. | Dev. | Homol. | Trein. | Simul. | Doc. | Prod. | Total |
|---|---|---|---|---|---|---|---|---|---|

**Total do projeto: XXh** · **Âncora do documento: Yh · divergência Z×** (se houver número pré-fechado)
**Confiança geral: ALTO / MÉDIO / BAIXO**

## 13. Estrutura para integração com cards
```

---

## JSON de saída

Schema completo do backlog, campo `estimated_hours` (com e sem refinamento) e bloco opcional de validação de entidades via MCP em `references/schema-saida.md`. Replicar a estrutura por inteiro ao salvar o `[nome-projeto]-backlog.json` — nenhum campo obrigatório pode faltar.

---

## Persistência de artefatos — OBRIGATÓRIO

Ao concluir a análise (após estimativas finais e refinamento, se houver), salvar **sempre** os seguintes arquivos no diretório de documentação do projeto. Usar o Write tool — não deixar o conteúdo apenas na conversa.

### Artefato 1 — Documento completo de análise (SEMPRE salvar)

**Arquivo:** `[NomeProjeto]-AnaliseCompleta.md` (ou equivalente no padrão do projeto)

**Deve conter obrigatoriamente TODAS as 13 seções do formato de saída padrão:**
- Seções 1–11: resumo, domínios, mapa de impacto, epics, story map, stories, critérios de aceite, **tarefas técnicas com `- [ ]` por epic**, dependências, pontos abertos, abordagem técnica
- Seção 12: estimativa de horas — se refinamento foi feito, exibir rápida × refinada lado a lado; caso contrário apenas rápida
- Seção 13: JSON embutido ou referência ao arquivo JSON separado

> **NUNCA salvar apenas o documento de estimativa e omitir o documento completo.** Documentos parciais (só estimativa, só backlog) são complementares e podem ser gerados adicionalmente, mas não substituem este artefato.

### Artefato 2 — JSON do backlog (SEMPRE salvar)

**Arquivo:** `[nome-projeto]-backlog.json`

**Cada story no JSON deve conter todos os campos do schema:**
`story_id`, `title`, `user_value`, `description`, `complexity`, `acceptance_criteria[]`, `technical_tasks[]`, `dependencies[]`, `risks[]`, `source_refs[]`, `technical_approach`, `estimated_hours`

> **Nunca salvar o JSON omitindo `acceptance_criteria` e `technical_tasks`.** Esses campos são obrigatórios no schema — sem eles o JSON é incompleto para importação futura.

### Artefatos complementares (opcionais, sob demanda)

Gerar apenas se o usuário solicitar explicitamente ou se fizer sentido pelo contexto:
- `[NomeProjeto]-EstimativaRapida.md` — tabela de estimativas estágio 1 por epic/story
- `[NomeProjeto]-EstimativaRefinada.md` — comparativo rápida × refinada com notas de refinamento
- `trello-import.json` — formato Power-Up Trello

---

## Handoff para geração de código (sob permissão explícita)

**NUNCA gerar código (gastar tokens) sem permissão explícita do usuário.** Após salvar o MD e o `backlog.json`, **perguntar** — nunca gerar automaticamente.

Dois pontos de pergunta:
1. **Refinar a estimativa?** — gerar **esqueletos** das stories média/alta (Estágio 2) para recalibrar com pesos reais. Perguntar: *"Deseja refinar gerando esqueletos de código? (sim/não)"*.
2. **Iniciar desenvolvimento?** — somente se confiança ≥ **MÉDIO-ALTO**. Perguntar: *"Confiança {nível}. Deseja gerar o código pré-pronto para entregar ao dev? (sim/não)"*.

**Gate de confiança:**
- **ALTO** → ofertar build completo em **ondas** (dados → backend → frontend → BI), com verificação de encoding e checkpoint por onda.
- **MÉDIO-ALTO / MÉDIO** → ofertar build das stories de alta confiança + esqueleto do resto; confirmar antes de artefatos pesados (frontend vc denso, EJB).
- **BAIXO** → **não ofertar build**; listar bloqueios a resolver (modelos visuais `.jpg/.pdf`, ambiguidades, dependências documentais).

**Execução:** o contrato de entrada é o `[projeto]-backlog.json`. Quem executa é o agent **`sankhya-orchestrator-agent-dev`** (invocado no fluxo principal), que decide addon×módulo, **lê a stack de frontend registrada na seção 11** e roteia aos especialistas (`sankhya-data-dev`, `sankhya-backend-dev`, `sankhya-bi-report-dev` e, para tela própria, **`sankhya-frontend-angular`** quando AngularJS `sankhya-js` ou **`sankhya-frontend-design-system`** quando Design System) e gera em ondas com verificação de encoding ISO-8859-1.

**Stack de frontend no handoff:** repassar ao orchestrator a decisão da Etapa 10 — **AngularJS `sankhya-js`** (default, sem Node) × **Design System** (requer pipeline Node). Tela própria segue a estrutura `html5/<Nome>/<Nome>.html` + launcher + entrada de menu `.xhtml5`. ⚠️ Design System exige toolchain Node configurado; sem ele o build falha — não rotear projeto sem Node para `sankhya-frontend-design-system`.

**Entrega "pré-pronta" ao dev:** Java com **Javadoc** (classe e método: o que faz, `@param`/`@return`/`@throws`) + **comentários inline** explicando o porquê das decisões; encoding ISO-8859-1; metodologia do usuário (Clean Code, SOLID, nomes PT-BR).

## Regras de qualidade

- Cada epic possui objetivo claro
- Cada story tem valor funcional identificável e cabe em pequena entrega
- Cada story passa no critério INVEST: Independente, Negociável, Valiosa, Estimável, Pequena, Testável
- Todos os requisitos identificados possuem story correspondente — nenhum requisito órfão
- Quando requisito não tem story: criar nova story, incorporar em existente, ou registrar como fora do escopo
- Critérios de aceite não são vagos — nenhum 🔴 CRÍTICO sem refinar
- Critério funcional separado de não-funcional nos ACs
- Tarefas técnicas não substituem stories
- Dependências externas estão visíveis
- Gênero do documento detectado; as-built não estimado; boilerplate D4Sign descartado; template clonado não duplicado
- Dependências documentais (refs a outros documentos e a modelos visuais) registradas; stories afetadas com confiança reduzida
- Itens extra-escopo segregados do total compromissado
- Rotinas nativas a homologar classificadas como `[NATIVO/HOMOLOGAÇÃO]`, não como dev
- Estimativa itemizada por rotina nas 7 fases; estimativa-âncora do documento confrontada quando presente
- Estimativa realista (não o piso comercial): faixas vendidas conferidas contra `calibracao-real.md`; EJB/bean e frontend vc estimados pelo peso medido; uplift quando addon com UI própria
- Recomendação Addon × Módulo-Java feita no nível do projeto, nos dois eixos (aderência ao negócio e distribuição), com justificativa; escopo complexo/screen-centric não roteado para módulo-java só por custo (anti-pattern "vendido errado"), com trade-off explícito
- Proposta comercial tratada como âncora de escopo/teto, não como fonte de estimativa de dev
- Addon novo só em Addon Studio oficial; manutenção em addon de terceiro inclui o custo de conversão para o oficial na estimativa
- Ambiguidades foram explicitadas
- Há rastreabilidade para os itens do documento
- Estimativa itemizada nas 7 fases (ou aproximação rápida dev + overhead ~30% no Estágio 1) e nível de confiança explícito

---

## Saída mínima aceitável

Mesmo com documento incompleto, devolver no mínimo: resumo executivo, lista de domínios, epics propostos, pelo menos uma story por epic, riscos e dúvidas, recomendação de abordagem e estimativa rápida.

---

## Referências

| Tópico | Arquivo / Skill |
|---|---|
| Segmentação, classificação de trechos, domínios ERP, priorização, ambiguidade, tabela de decisão técnica completa (Módulo Java, Addon Studio, BI, Frontend, Script DB) | `references/heuristicas-erp.md` |
| Tabelas de base por artefato (Módulo Java, Addon Studio, Frontend, BI), multiplicadores, teto de composição, sanity-check, referência de skills por artefato, Estágio 2 | `references/heuristicas-estimativa.md` |
| Schema JSON completo do backlog, campos obrigatórios, bloco de validação de entidades | `references/schema-saida.md` |
| Exemplo end-to-end: escopo de entrada → 13 seções de saída | `references/exemplo-completo.md` |
| Diagnóstico e técnicas de fatiamento de stories; níveis e anti-patterns de critérios de aceite | `references/fatiamento-criterios.md` |
| Template oficial de estimativa (7 fases por rotina), proporções, confronto de âncora | `references/template-horas-fases.md` |
| Calibração real medida em código entregue: pesos por artefato, produtividade, EJB e frontend vc, fator de subestimação das planilhas vendidas | `references/calibracao-real.md` |
| Gêneros de documento (discovery, formal, versionado, BI, as-built/manual, proposta comercial), seções canônicas, sinônimos de identificação, higiene D4Sign/clones | `references/generos-documento.md` |
| Decisão de empacotamento Addon completo × Módulo-Java (scorecard, o que o módulo-java entrega, sinais de addon) | `references/addon-vs-modulo-java.md` |
| Estrutura de um projeto Addon Studio válido: skeleton, build.gradle/settings, formatos de datadictionary (table/nativeTable/view), dbscripts dual-dialect, menu, nomenclatura | `references/addon-studio-estrutura.md` |
| Padrões recorrentes de escopo Sankhya: cabeçalho, dependência documental, extra-escopo, homologação nativa, NF derivada, alçada TSILIB, reprocessamento idempotente, multiempresa, conversão de unidades, tela detalhe nativa | `references/padroes-requisito-sankhya.md` |
| Validação de entidades/tabelas/campos contra schema Oracle real (`search_entities`, `describe_table`, `search_columns`, `validate_query`) — Etapa 2.5 | MCP: **sankhya-schema** |
| Estrutura de tabelas Sankhya (campos, PKs, FKs, enums) — fallback quando MCP indisponível | skill: **sankhya-dicionario** |
| Módulos Java: `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava`, `ScheduledAction`, `Helper`, `Repository`, `Service`, XML Construtor de Telas | skill: **sankhya-modulo-java** |
| Addon Studio: `@Listener`, `@Callback`, `@ActionButton`, `@BusinessRule`, `@Job`, `DynamicForm`, `DBScripts`, `DataDictionary`, Design System | skill: **sankhya-addon** |
| JAPE: `JapeSession`, `NativeSql`, `EntityFacade`, `DynamicVO`, `execWithTX`, `execWithAutonomousTX`, `ProcedureCaller`, batch | skill: **sankhya-jape** |
| Frontend AngularJS: `ServiceProxy`, `sk-dataset`, `sk-datagrid`, `sk-wizard`, `SanPopup`, directives | skill: **sankhya-js** |
| Estrutura de tela própria (`html5/<Nome>/<Nome>.html` + launcher + entrada de menu `.xhtml5`) e decisão de stack de frontend: AngularJS sankhya-js (default, sem Node) × Design System (⚠️ requer pipeline/toolchain Node) | skill: **sankhya-js** · agentes: **sankhya-frontend-angular**, **sankhya-frontend-design-system** |
| BI / Dashboards: gadgets, gráficos, tabelas, drill-down, HTML5 component, Construtor de Componentes de BI | skill: **sankhya-bi** |
| Deploy WildFly, DataDictionary runtime, ordem de módulos, diagnóstico de erros | deploy/runtime (sem skill dedicada no pacote) |
| DB migrations idempotentes, dual-dialect Oracle/SQL Server, dbscripts, datadictionary | dbscripts + datadictionary |
