# Heurísticas ERP — Classificação, Domínio e Abordagem Técnica

## Segmentação do documento (Etapa 1)

**Antes de segmentar:** detectar o **gênero** do documento (discovery pré-vendas, levantamento formal, requisito versionado, spec de BI, as-built/manual, proposta comercial) e descartar boilerplate (rodapé/assinaturas D4Sign). Gêneros as-built (E/F) não geram estimativa. Extrair o cabeçalho de identificação normalizando sinônimos (Parceiro, Nro. Flow, FAP, OS de Origem, Segmento). Ver `references/generos-documento.md`.

Identificar e separar no documento:
- objetivo
- contexto
- atores
- processos
- requisitos
- regras de negócio
- exceções
- premissas
- dependências externas
- itens condicionais
- itens fora de escopo
- relatórios e dashboards
- referências técnicas citadas (tabelas, telas, botões, cadastros, rotinas)

---

## Classificação dos trechos (Etapa 2)

Classificar cada trecho em uma das categorias:

| Categoria | Quando aplicar |
|---|---|
| objetivo de negócio | intenção macro, resultado esperado pelo cliente |
| requisito funcional | comportamento observável do sistema |
| regra de negócio | condição, validação, cálculo ou bloqueio |
| detalhe técnico | referência a tabela, campo, classe ou rotina |
| integração | comunicação com sistema externo |
| parametrização | configuração via parâmetro ou preferência |
| permissão ou alçada | controle de acesso, liberação de limite |
| relatório ou dashboard | saída de dados para visualização em relatório nativo |
| dashboard BI ou gadget | visualização analítica via Construtor de Componentes de BI (gráfico, tabela, KPI, drill-down) |
| tela frontend | interface customizada via sankhya-js (AngularJS) ou Design System (ez-/snk-) |
| dependência externa | item que depende de terceiro ou de outra entrega |
| dependência documental | regra remetida a outro documento ("conforme levantamento X", "item Y em diante") |
| homologação de rotina nativa | "rotina nativa testar e validar", "simular com a equipe" — sem dev |
| item extra-escopo | "fora da proposta comercial", "negociação de horas", "após as personalizações" |
| premissa | condição assumida como verdadeira sem confirmação |
| restrição | limitação técnica ou de negócio |
| dúvida ou ambiguidade | trecho vago, conflitante ou incompleto |

---

## Agrupamento por domínio (Etapa 3)

Exemplos de macrodomínios funcionais recorrentes em projetos Sankhya:

- pesagem / classificação / análise de qualidade
- contratos / armazenagem
- financeiro / contas a pagar / contas a receber
- estoque / movimentação
- certificação / laudos
- transferência / romaneio / expedição
- relatórios / dashboards
- integrações com sistemas externos

---

## Heurísticas específicas para personalizações ERP

### Campos adicionais
Classificar como possível criação ou alteração de metadado, tela, validação e persistência. Nunca como story isolada — é tarefa técnica dentro de uma story funcional.

### Botões de ação
Classificar como automação de processo e provável ponto de entrada de regra de negócio. Cada botão tende a virar uma story própria quando entrega valor perceptível.

### Tabelas nativas (TGFCAB, TGFITE, TGFFIN, TGFVAR, TSILIB, etc.)
Classificar como detalhe técnico ou persistência — nunca como story isolada.

### Parâmetros e preferências personalizados
Classificar como dependência de configuração e task técnica. Quando o parâmetro habilita um comportamento funcional, gerar também story de "configurar parâmetro X para ativar funcionalidade Y".

### Dashboards e relatórios
Tratar como épicos ou subentregas separadas, especialmente quando dependem da estabilidade das regras anteriores. Não incluir no mesmo epic que as automações.

### Alçadas e liberações
Tratar como regra funcional (story) e também como dependência de permissão (task técnica de configuração de TSILIB).

### Ações agendadas
Tratar como story separada quando entregam automação de negócio perceptível. Registrar frequência esperada em critérios de aceite.

### Integrações externas
Tratar como epic próprio quando a integração for bidirecional, tiver tratamento de erro ou envolver autenticação. Integrações simples de leitura podem ser tasks técnicas dentro de outra story.

---

## Heurísticas de priorização

Quando o usuário pedir priorização, sugerir a seguinte ordem:

1. fluxo principal operacional (o que trava o processo sem funcionar)
2. automações críticas (redução de trabalho manual imediata)
3. exceções obrigatórias (bloqueios que causam erro ou inconsistência)
4. financeiro vinculado (impacto em caixa ou faturamento)
5. dashboards e relatórios (dependem da estabilidade dos dados anteriores)
6. refinamentos complementares (melhorias e ajustes finos)

---

## Conduta diante de ambiguidade

- Não inventar regra final
- Registrar hipótese com marcação explícita: `[HIPÓTESE: ...]`
- Marcar como validação pendente: `[PENDENTE: confirmar com cliente]`
- Manter a story em nível funcional sem detalhamento técnico prematuro
- Empurrar detalhe duvidoso para seção "10. Itens ambíguos para validação"

---

## Dependência documental e itens extra-escopo

### Referência a outros documentos
Quando o requisito remete a outro documento ("conforme levantamento X", "item 5.2 em diante", "documentos de entrada"), a regra **não está no documento atual**. Registrar em "9. Dependências e riscos" como dependência de leitura e reduzir a confiança da story afetada. Nunca estimar a regra remetida como completa.

### Itens fora do escopo fechado
Sinais: "não constem em proposta comercial", "negociação de horas", "extra escopo", "após as personalizações". Segregar em bloco separado, estimar à parte e **não somar ao total compromissado**. Itens "após personalizações" (relatórios/dashboards) são sequenciados depois, não paralelos.

Ver detalhamento de ambos em `references/padroes-requisito-sankhya.md`.

---

## Exemplo de decomposição

### Entrada do documento
"Ao finalizar a pesagem, o sistema deve confirmar automaticamente a nota de compra."

### Saída correta

```md
Epic: Pesagem de Entrada

Story: Confirmar automaticamente a nota de compra ao finalizar a pesagem
Valor: Eliminar confirmação manual e garantir continuidade do fluxo

Critérios de aceite:
- Dado que a pesagem foi finalizada com sucesso, quando o processo for concluído, então a nota de compra deve ser confirmada automaticamente.
- Dado que a confirmação falhe, quando ocorrer erro de negócio, então o usuário deve ser informado e o processo deve registrar a falha.

Tarefas técnicas:
- Identificar objeto que finaliza a pesagem
- Invocar rotina de confirmação da nota
- Tratar retorno e mensagem de erro
```

---

## Tabela de decisão técnica

| Indicador no escopo | Abordagem | Artefato principal |
|---|---|---|
| "ao confirmar NF", "ao salvar", "ao alterar campo", "listener automático" | `[MÓDULO JAVA]` | `EventoProgramavelJava` |
| "ao confirmar/faturar nota", "callback de documento comercial" | `[ADDON STUDIO]` | `@Callback` |
| "botão de ação", "clique do usuário", "executar manualmente" (módulo) | `[MÓDULO JAVA]` | `AcaoRotinaJava` |
| "botão de ação", "clique do usuário" (addon) | `[ADDON STUDIO]` | `@ActionButton` |
| "processamento automático", "rotina noturna", "job agendado" (módulo) | `[MÓDULO JAVA]` | `ScheduledAction` |
| "processamento agendado", "job periódico" (addon) | `[ADDON STUDIO]` | `@Job` |
| "regra de negócio", "bloquear confirmação", "validar ao confirmar" (módulo) | `[MÓDULO JAVA]` | `RegraNegocioJava` / `Regra` |
| "regra de negócio", "validar nota de saída" (addon) | `[ADDON STUDIO]` | `@BusinessRule` |
| "nova tabela AD_", "campo adicional", "nova entidade" | `[MÓDULO JAVA]` | `AD_*` no dicionário + XML Construtor de Telas |
| "nova tela customizada", "formulário novo", "tela com guias/abas", "campos de imagem", "busca personalizada" | `[MÓDULO JAVA]` | **Construtor de Telas (DWF)** — metadados ZIP. Tela ≠ addon |
| "dicionário de dados versionado", "DBScripts empacotado" **+ distribuição multi-cliente** | `[ADDON STUDIO]` | `DataDictionary` + `DBScripts` (só quando produto distribuível — ver `addon-vs-modulo-java.md`) |
| "UI além do Construtor", "DynamicForm", "componente JS acoplado ao ciclo da entidade" | `[ADDON STUDIO]` | Design System / DynamicForm |
| "dashboard", "gadget", "gráfico de análise", "KPI", "componente de BI" | `[BI/DASHBOARD]` | Construtor de Componentes de BI |
| "dashboard HTML5", "painel operacional customizado" | `[BI/DASHBOARD]` | HTML5 component (SankhyaJX) |
| "relatório nativo Sankhya", "jasper", "iReport" | `[RELATÓRIO]` | Sankhya Relatório nativo |
| "apenas configuração de parâmetro ou preferência" | `[CONFIGURAÇÃO]` | Sem desenvolvimento |
| "rotina nativa testar e validar", "simular com usuários", "opção nativa do ERP" | `[NATIVO/HOMOLOGAÇÃO]` | Homologação/parametrização — sem código |
| "emitir nota de quebra/rendimento/remessa automaticamente" | `[MÓDULO JAVA]` / `[ADDON STUDIO]` | Geração de NF derivada (AcaoRotina/Evento + TGFCAB/TGFITE) |
| "liberação de limites", "alçada", "abono", "evento de liberação" | `[MÓDULO JAVA]` / `[ADDON STUDIO]` | Fluxo de alçada via `TSILIB` + evento personalizado |
| "transferência de posse", "remessa matriz→filial", "escriturar NF-e de terceiro" | `[HÍBRIDO]` | Operação multiempresa — epic próprio, complexidade fiscal |
| "migration de dados", "script de banco", "DML em produção" | `[SCRIPT DB]` | `dbscripts/` idempotente |
| Mix de automação backend + tela nova (Construtor) + dashboard | `[MÓDULO JAVA]` | Backend + Construtor de Telas + gadget BI — tudo módulo-java |
| Mix de backend + dashboard analítico | `[HÍBRIDO]` | Backend + `[BI/DASHBOARD]` |

> **Tela/tabela/dashboard novos não implicam Addon Studio por si.** Mas **processo que diverge do nativo e precisa de telas/UX sob medida** é, sim, sinal de addon — mesmo cliente único e mesmo que o nativo já exista (módulo-java fica amarrado a telas nativas + botão+evento). A escolha addon × módulo-java é decisão de **projeto inteiro**, em dois eixos — aderência ao negócio e distribuição — ver `references/addon-vs-modulo-java.md`. A coluna Abordagem abaixo indica só o **tipo de artefato**.

**Classificações por epic (tipo de artefato):**
- `[MÓDULO JAVA]` — lógica em JAR + telas via Construtor + `AD_*` no dicionário; entrega ponto-a-ponto (default)
- `[ADDON STUDIO]` — só quando o projeto inteiro é produto distribuível/versionado ou exige UI além do Construtor (ver scorecard em `addon-vs-modulo-java.md`)
- `[BI/DASHBOARD]` — gadgets e dashboards via Construtor de Componentes de BI
- `[RELATÓRIO]` — relatórios nativos Sankhya
- `[SCRIPT DB]` — apenas migrations de dados ou DDL, sem lógica Java
- `[CONFIGURAÇÃO]` — parâmetros/preferências, sem desenvolvimento
- `[NATIVO/HOMOLOGAÇÃO]` — testar/validar/parametrizar rotina nativa existente; sem código, consome horas de consultoria
- `[HÍBRIDO]` — combinação de duas ou mais classificações acima

**Regra default:** recomendar **Módulo Java** — inclusive com telas (Construtor), tabelas `AD_*` e dashboards. Só migrar para **Addon Studio** quando o projeto for produto distribuível multi-cliente ou exigir UI além do Construtor de Telas (scorecard em `references/addon-vs-modulo-java.md`).

---

## Heurísticas específicas para BI e dashboards

- "Quero ver/analisar/acompanhar X" sem interação transacional → `[BI/DASHBOARD]`
- "Gráfico de", "evolução de", "comparativo de", "participação de" → gadget gráfico
- "Tabela de acompanhamento", "listagem gerencial" → gadget tabela
- "Valor atual de", "meta realizada", "KPI" → gadget valor pontual
- "Clicar e detalhar", "drill-down", "abrir detalhe" → gadget com drill-down (complexidade sobe)
- "Painel operacional com edição" → HTML5 component (não gadget nativo)
- Sinalizar sempre: Oracle ou SQL Server do cliente? — altera sintaxe SQL e prazo
- Dashboard nunca deve estar no mesmo epic que as automações de negócio que alimentam os dados; criar epic separado

---

## Heurísticas específicas para telas frontend

- "Nova tela", "formulário de cadastro", "tela de gestão" → verificar: projeto legado (sankhya-js) ou novo (Design System)?
- Sem confirmação: perguntar ao usuário antes de estimar — a diferença de prazo pode ser 30–50%
- Tela com edição inline de grid → `sk-datagrid` com `sk-dataset` — complexidade média/alta
- Wizard (múltiplos passos, validação por passo) → sempre alta complexidade
- Popup de seleção ou formulário dentro de action button → `SanPopup` ou `PopUpBuilder` — adicionar ao artefato Java correspondente
- Tela puramente de consulta (read-only) → complexidade baixa mesmo com filtros
- Tela com integração a entidades Sankhya nativas via `MetadataProvider` → adicionar 20–30% à estimativa base
