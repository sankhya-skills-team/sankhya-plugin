# Decisão de abordagem: Addon completo × Módulo-Java

Recomendação **no nível do projeto** (a personalização inteira), não por epic. Responde: "vale criar um Addon Studio completo para todo o escopo, ou seguir como módulo-java tradicional?"

## Custo de dev × aderência ao negócio

Em base real de ~96 projetos, **~85% foram entregues como módulo-java** — mas isso reflete o que foi **vendido**, não o que era tecnicamente certo. O módulo-java tem **menor esforço de desenvolvimento** (mais barato/rápido), então é frequentemente vendido mesmo quando o addon seria a escolha correta. **Mais barato ≠ mais adequado.**

Dois eixos de decisão, não um:
1. **Empacotamento/distribuição** — addon quando é produto distribuível/versionado para vários clientes.
2. **Aderência ao negócio / flexibilidade de telas e UX** — addon quando o processo do cliente diverge do nativo e precisa de telas e rotinas **sob medida**, com boa usabilidade. Vale **mesmo para cliente único** e **mesmo que o nativo já exista**.

### Anti-pattern "vendido errado"
Escopo complexo e centrado em telas roteado para módulo-java **só por custo de dev** → entrega amarrada a telas nativas, baixa aderência, retrabalho. Sinalizar o trade-off explicitamente: módulo-java é mais barato de fazer, porém menor aderência; addon custa mais, porém telas/rotinas sob medida ao negócio.

### Casos reais que DEVERIAM ter sido addon (foram módulo-java por custo)
- **Projeto B (pesagem)** — processo de pesagem ficou **amarrado à tela nativa de pesagem avulsa** e às limitações do módulo-java (botão de ação + evento). Complexo o suficiente para caber num addon; a falta de telas próprias prejudicou a aderência. **Deveria ser addon.**
- **Projeto A (controle de OS)** — "Controle de OS" com fluxo próprio (peritagem, fotos, SLA) teria muito mais flexibilidade de telas e rotinas como addon. **Deveria ser addon.**

> Não usar esses dois como prova de que "módulo-java escala". Eles provam o **anti-pattern**: complexidade alta, telas centrais ao negócio, entregues em módulo-java por custo — ficando presos ao nativo.

### Casos reais que CORRETAMENTE viraram addon
- **Addon de faturamento de contrato** (framework de terceiro, lib legada) — o **faturamento de contrato nativo já existia**, mas o cliente precisava de um fluxo próprio (apuração, contestação, ocorrências). Escolheram **addon** para encaixar no negócio e facilitar o uso, com arquitetura limpa por domínio (`action`/`controller`/`model`). Cliente único, nativo existente — e ainda assim addon foi o certo, pela **aderência**. ⚠️ Foi feito em **framework de terceiro (lib legada), hoje sem suporte**; a decisão de *modelo addon* estava certa, mas hoje seria **Addon Studio oficial** (ver restrição abaixo).
- **Addon de gestão de projetos/obra** (Addon Studio oficial) — caso-bandeira. O módulo **nativo de Projetos existe, mas é fraco/limitado**. O addon o transforma em **ferramenta poderosa** de controle de projetos (obras, etapas, kanban, agenda de recursos, faturamento), com **75 tabelas**, 150+ classes, **frontend web próprio** (`.war` — UI além do Construtor), **7 dashboards** e distribuição via **Sankhya Place**. Vira **base/plataforma reusável** para outros segmentos de addon. Combina todos os sinais: nativo fraco a transformar + UI própria + produto distribuível + plataforma.

> **Nativo existente não impede addon.** Que algo já exista no nativo **não significa que não possa ser melhorado**. Nativo **fraco/subutilizado** que é central ao negócio do cliente é candidato legítimo a ser **transformado** por um addon — às vezes virando produto e base para outros.

**Tamanho de código e número de telas não decidem.** O que decide é: precisa de telas/UX sob medida (addon) ou as extensões sobre telas nativas bastam (módulo-java)? E: é produto distribuível (addon) ou entrega para um cliente (tende a módulo-java)?

## O que o módulo-java entrega (não confundir com addon)

| Necessidade | Como o módulo-java resolve |
|---|---|
| Telas multi-guia, abas, campos de imagem, grids | **Construtor de Telas (DWF)** — metadados exportados em ZIP, importados no dicionário. O JAR não contém UI |
| Tabelas/entidades novas | `AD_*` no dicionário de dados (TDDTAB/TDDCAM) |
| Botões de ação | `AcaoRotinaJava` vinculada à tela pelo nome |
| Gatilhos de persistência | `EventoProgramavelJava` (before/after) |
| Regras/validações | `RegraNegocioJava` |
| Dashboards/painéis | Gadget HTML5 BI nativo |
| Relatórios | JasperReports (JRXML) |
| Menu próprio, workflow de status | Dicionário + metadados |

**Teto do módulo-java (importante):** o Construtor de Telas **estende telas nativas** e a lógica gira em torno de **botão de ação + evento**. Não dá telas 100% livres. Quando o processo do cliente **diverge do nativo** (não encaixa numa tela nativa nem em abas/botões sobre ela), o módulo-java vira colete de força — é exatamente o que travou o Projeto B na pesagem avulsa. Aí o addon, com telas próprias, é mais adequado.

Enquanto a UI **encaixar** sobre telas nativas (abas, campos `AD_*`, botões, dashboards) e a entrega for para um cliente, módulo-java vai longe. Quando precisar de **telas próprias divergentes do nativo**, é sinal de addon.

## Quando escolher ADDON COMPLETO

Recomendar Addon Studio para todo o escopo quando houver **≥1 sinal forte**:

| Sinal forte | Por quê |
|---|---|
| **Aderência ao negócio / telas e UX sob medida** (processo diverge do nativo) | Addon dá telas 100% próprias e fluxo desenhado para o cliente; módulo-java ficaria amarrado a telas nativas + botão+evento. Vale mesmo para **cliente único** e mesmo que o **nativo exista** (caso: addon de faturamento de contrato) |
| **Produto distribuível para múltiplos clientes** (mesmo pacote instalado em N clientes) | `appKey`, pacote `.ext`/`.addon` versionado, instalação do mesmo artefato em vários ambientes |
| **Instalação automatizada/reproduzível** de datadictionary + dbscripts | No módulo-java, telas (ZIP), campos `AD_*`, preferências e JAR são artefatos soltos importados manualmente por ambiente — não escala |
| **UI além do Construtor de Telas** | DynamicForm, componentes JS/Design System acoplados ao ciclo da entidade |
| **Governança / releases frequentes / time grande / arquitetura limpa por domínio** | Registro declarativo versionado e organização `action`/`controller`/`model` (caso: addon de faturamento de contrato), em vez de amarração manual no dicionário |
| **Transformar nativo fraco** central ao negócio / **base-plataforma reusável** para outros addons | Nativo subutilizado vira ferramenta poderosa sob medida; addon serve de fundação para outros segmentos (caso: addon de gestão de projetos) |
| **Roadmap de produto** com versionamento de dependências entre módulos | Addon gerencia dependências e versões declarativamente |

> **Restrição atual (obrigatória):** se a decisão for addon, hoje **só o Addon Studio oficial** pode ser usado. Frameworks de anotação de terceiros (ex.: lib de terceiro legada) **não são mais suportados**. Os sinais acima decidem o *modelo* (addon × módulo-java); a *implementação* de um addon novo é sempre Addon Studio oficial.
>
> **Manutenção de addon legado em terceiro:** se um projeto existente usa framework de terceiro (libs legadas) e precisa de manutenção, ele deve ser **totalmente convertido para o Addon Studio oficial**. Essa **conversão entra na estimativa** — é esforço próprio (migrar tabelas/datadictionary, dbscripts, anotações, telas e build), não um ajuste pontual. Sinalizar o custo da conversão antes de orçar a manutenção.

## Quando permanecer MÓDULO-JAVA

Quando **todos** verdadeiros:
- Entrega para **cliente único**, sem revenda/distribuição
- O processo **encaixa sobre telas nativas** (abas, campos, botões) — não exige telas próprias divergentes
- UI cabe no Construtor de Telas + dashboards HTML5 + relatórios Jasper
- Sem necessidade de empacotamento distribuível/versionado

Personalização **pontual** sobre processo nativo (poucas regras, botão+evento, sem telas próprias) → módulo-java é o caminho natural e mais barato.

## Scorecard de recomendação

1. Avaliar os sinais fortes de addon (tabela acima), com peso especial em **aderência ao negócio / telas sob medida** e **distribuição multi-cliente**.
2. **Nenhum sinal + escopo encaixa no nativo → MÓDULO-JAVA** (mais barato, adequado).
3. **Processo diverge do nativo / telas centrais ao negócio / UX sob medida / nativo fraco a transformar → ADDON**, mesmo cliente único, mesmo nativo existente, mesmo custando mais (casos: armazenagem/pesagem, controle de OS, faturamento de contrato, gestão de projetos).
4. **Distribuição multi-cliente, UI além do Construtor, ou base-plataforma reusável → ADDON.**
5. **Só governança/arquitetura, sem os acima → MÓDULO-JAVA com nota** sobre o trade-off.

Registrar a recomendação com a justificativa do sinal decisivo. **Quando o custo empurrar para módulo-java mas a aderência pedir addon, dizer isso explicitamente** — não silenciar o trade-off para baratear a proposta (anti-pattern "vendido errado"). Em decisão limítrofe, expor os dois caminhos.

## Relação com a classificação por epic

A classificação técnica por epic (`[MÓDULO JAVA]`/`[ADDON STUDIO]` em `heuristicas-erp.md`) indica o **tipo de artefato**; esta decisão é de **empacotamento do projeto inteiro**. Um projeto pode ter epics com artefatos "estilo addon" (listener, botão) e ainda assim ser entregue como módulo-java. Não derivar "é addon" só porque há tela ou tabela nova.


## Aprendizado de campo (projeto real, 2026)

- **Decisão do cliente pode contrariar a recomendação técnica.** O scorecard pode apontar "estender módulo-java", mas o cliente pode exigir "addon do zero sem herança". Respeitar, porém **registrar o trade-off e o custo do rebuild (E0)** no documento — o cliente decide com o número na mão.
- **Cadastros simples ⇒ DynamicForm nativo, não vc custom.** Telas de cadastro (classificadores, peneiras, certificações) e telas que hospedam `@ActionButton` devem ficar como `dynamicForm` no menu; criar vc custom quebra o binding dos botões. Reservar frontend vc denso para telas com UX própria (ex.: a Pesagem reformulada).
