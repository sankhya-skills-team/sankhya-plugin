# Heurísticas de Estimativa de Horas

> **A saída final segue o template oficial de 7 fases por rotina** (Levantamento, Desenvolvimento, Homologação, Treinamento, Simulação, Documentação, Produção e acompanhamento) — ver `references/template-horas-fases.md`. As tabelas de base e multiplicadores abaixo calculam a coluna **Desenvolvimento**; as demais fases são alocadas por cima (o "+30%" itemizado em fases).
>
> ⚠️ **As faixas abaixo foram calibradas em planilhas VENDIDAS (módulo-java) e SUBESTIMAM o esforço real em ~1,6–2,2× (medido em código entregue).** Para estimativa realista, conferir contra `references/calibracao-real.md` (pesos por artefato medidos, produtividade ~12 LOC/h, EJB e frontend vc) e/ou aplicar fator de realismo, sobretudo quando a abordagem correta for addon com UI própria.

---

## Base por artefato — Módulo Java

Tempo base antes de multiplicadores. Usar sempre como faixa (min–max). Estas faixas alimentam a coluna **Desenvolvimento** do template.

| Artefato | Complexidade | Faixa (h) |
|---|---|---|
| `EventoProgramavelJava` — 1 regra, 1 campo | baixa | 2–4 |
| `EventoProgramavelJava` — cálculo com múltiplos campos | média | 5–9 |
| `EventoProgramavelJava` — lógica com múltiplas entidades, before+after | alta | 10–16 |
| `AcaoRotinaJava` — fluxo linear, 1 ação | baixa | 3–6 |
| `AcaoRotinaJava` — múltiplas validações, confirmação `ctx.confirmarSimNao()` | média | 8–14 |
| `AcaoRotinaJava` — com `PopUpBuilder` (seleção em grid, formulário modal) | média–alta | 14–26 |
| `AcaoRotinaJava` — orquestra múltiplos processos, popup wizard 2 páginas | alta | 20–36 |
| `ScheduledAction` — processamento simples | baixa | 4–7 |
| `ScheduledAction` — processamento em lote com lógica complexa | média | 8–14 |
| `RegraNegocioJava` / `Regra` — validação simples | baixa | 4–7 |
| `RegraNegocioJava` — com alçada/liberação de limite | média | 8–16 |
| `RegraNegocioJava` — ciclo de vida completo (before/after confirmação) | alta | 14–24 |
| `Controller` (endpoint REST/ServiceProvider manual) | média | 8–16 |
| **EJB / bean** (`ServiceProvider` + tripé `SP/SPSession/SPHome` + `Service`) — serviço backend completo | alta | 40–70 |
| **Frontend vc denso** (html/js que integra EJB — ex. dashboard Kanban, painel operacional) | alta | 80–160 |
| **Frontend vc médio** (tela de gestão html/js) | média–alta | 30–70 |
| `Repository`/DAO com SQL Oracle pesado (queries densas, JAPE) | média–alta | 16–40 |
| `Helper` novo (lógica transversal reutilizável) | baixa–média | 3–8 |
| `Repository` novo (JAPE + NativeSql) | baixa–média | 4–10 |
| `Service` novo (regras de negócio puras) | baixa–média | 3–8 |
| XML Construtor de Telas — nova tabela `AD_*` + tela simples | média | 6–12 |
| XML Construtor de Telas — tela com campos relacionados, grid interno | alta | 12–22 |
| Integração externa simples (leitura/push REST 1 endpoint) | média | 10–18 |
| Integração externa bidirecional com retry e tratamento de erro | alta | 24–48 |
| Relatório simples | baixa | 4–8 |
| Geração automática de NF derivada (quebra/rendimento/complemento) — TGFCAB+TGFITE+TOP+local+contrato | alta | 16–28 |
| Geração de NF derivada com reflexo financeiro (títulos TGFFIN) | alta | 22–38 |
| Tela adicional detalhe em tabela nativa (até ~8 campos, 1–2 FKs) | média | 8–14 |
| Tela adicional detalhe + gatilho de gravação na confirmação da nota | média–alta | 14–24 |
| Fluxo de alçada/liberação `TSILIB` + evento personalizado (2 caminhos) | média–alta | 14–26 |
| Rotina idempotente de reprocessamento (ScheduledAction, exclui+regera título, 4+ ramos de estado) | alta | 24–44 |
| Conversão de unidades/volume (KG/SC/TN/BG, bidirecional, preenche campos nativos) | média | 8–16 |
| Configuração de parâmetro/preferência | mínima | 1–2 |
| `[NATIVO/HOMOLOGAÇÃO]` — testar/validar/parametrizar rotina nativa com usuário-chave | — | 4–12 (consultoria) |

---

## Base por artefato — Addon Studio

| Artefato | Complexidade | Faixa (h) |
|---|---|---|
| `@Listener` — 1 evento, 1 campo, lógica simples | baixa | 3–6 |
| `@Listener` — múltiplos campos, lógica derivada, condicionais | média | 6–12 |
| `@Listener` — orquestra múltiplas entidades, side-effects | alta | 12–22 |
| `@Callback` — ciclo de nota simples (confirmar/faturar) | média | 8–16 |
| `@Callback` — com validação fiscal, alçada, rollback | alta | 16–28 |
| `@ActionButton` — ação simples, 1 serviço | baixa | 5–10 |
| `@ActionButton` — com validações, confirmação | média | 10–18 |
| `@ActionButton` — orquestra múltiplos serviços, popup/formulário | alta | 20–36 |
| `@BusinessRule` — validação simples no barramento de regras | baixa | 4–8 |
| `@BusinessRule` — com alçada, múltiplos campos, ciclo de nota | média | 10–18 |
| `@Job` (addon) — processamento simples periódico | baixa | 5–10 |
| `@Job` (addon) — processamento em lote com lógica de negócio | média | 10–20 |
| `DynamicForm` gerada por dicionário de dados | baixa | 3–7 |
| `DBScripts` + `DataDictionary` — nova tabela simples (sem FK complexa) | baixa | 4–8 |
| `DBScripts` + `DataDictionary` — tabela com FKs, campos lista, hierarquia | média | 8–16 |
| `DBScripts` — migration de dados DML idempotente (Oracle + SQL Server) | baixa–média | 3–10 |
| View ou index novo com dual-dialeto | baixa | 3–6 |
| **Conversão de addon legado (framework de terceiro) → Addon Studio oficial** | alta | por escopo — migrar datadictionary, dbscripts, anotações, telas e build; estimar por módulo |

> **Só Addon Studio oficial** para addon novo. Manutenção em addon de terceiro (sem suporte) exige **converter para o oficial primeiro** — somar a conversão à estimativa da manutenção, nunca tratar como ajuste pontual.

---

## Base por artefato — Telas Frontend

### sankhya-js / HTML5 (AngularJS — projetos legados ou híbridos)

| Artefato | Complexidade | Faixa (h) |
|---|---|---|
| `ServiceProxy.callService` + exibição simples (lista readonly) | baixa | 4–8 |
| Tela de lista com filtros + ServiceProxy | média | 10–18 |
| `sk-dataset` standalone — CRUD completo (criar/editar/excluir) | média | 14–24 |
| Formulário com validações + dataset (campos dependentes) | média | 12–20 |
| `sk-datagrid` com colunas customizadas + navegação | média | 10–18 |
| Wizard multi-step (`sk-wizard`, 2–3 passos) | alta | 20–36 |
| Popup customizado (`SanPopup`) | baixa–média | 6–14 |
| Directive customizada simples | baixa | 6–12 |
| Tela completa (lista + formulário + validações + navegação) | alta | 24–44 |
| Integração frontend → backend via `ServiceProxy` (endpoint novo) | baixa | 4–8 |

### Design System (ez-/snk- components — projetos novos)

| Artefato | Complexidade | Faixa (h) |
|---|---|---|
| Tela simples (`snk-form` + campos `ez-`) | baixa–média | 8–16 |
| Tela com grid + navegação (`snk-datagrid`) | média | 12–22 |
| Tela com tabs + form + actions | média–alta | 18–32 |
| Tela completa (lista + form + validações + API Java) | alta | 24–44 |
| API Java (Design System API) + endpoint backend integrado | média | 8–16 |

---

## Base por artefato — BI / Dashboards

| Artefato | Complexidade | Faixa (h) |
|---|---|---|
| Gadget valor pontual (KPI simples, 1 query) | baixa | 2–4 |
| Gadget gráfico simples (pizza, barras, colunas) — 1 query, sem filtros | baixa | 4–7 |
| Gadget gráfico com parâmetros de filtro (período, entidade) | média | 6–12 |
| Gadget tabela com filtros e múltiplas colunas | média | 8–14 |
| Gadget com drill-down (2 níveis de detalhe) | alta | 14–24 |
| Gadget com drill-down multinível (3+ níveis) | alta | 20–36 |
| Dashboard HTML5 simples (tabela operacional, SankhyaJX) | média | 10–18 |
| Dashboard HTML5 complexo (KPI + grid + interatividade + filtros) | alta | 20–40 |
| Dashboard completo (múltiplos gadgets integrados, BI nativo) | alta | 24–48 |
| Query dual-dialeto Oracle + SQL Server | adicional | +20–30% sobre base |

---

## Multiplicadores automáticos

Aplicar sobre a faixa base após identificar os sinais na story/epic:

| Sinal detectado | Multiplicador |
|---|---|
| Mais de 3 regras de negócio na mesma story | × 1.5 |
| Integração externa envolvida | × 2.0 a × 3.0 (conforme complexidade) |
| Integração NF-e / NFS-e / PIX / boleto | × 2.5 a × 3.5 |
| Alçada / liberação de limite | × 1.4 |
| Múltiplos atores com permissões diferentes | × 1.3 |
| Dependência de outra story não entregue | × 1.2 |
| Ponto ambíguo relevante na story | × 1.3 (aplicar sobre o máximo) |
| Acesso a múltiplas entidades nativas (> 3 tabelas) | × 1.4 |
| Processo assíncrono ou com retry | × 1.5 |
| Dual-dialeto Oracle + SQL Server obrigatório | × 1.3 |
| Tela frontend nova (qualquer stack) envolvida | × 1.5 (sobre backend) |
| JAPE com transação autônoma (`execWithAutonomousTX`) | × 1.3 |
| Processamento em lote (`addBatch`, NativeSql em loop) | × 1.5 |
| Chamada a stored procedure (`ProcedureCaller`) | × 1.4 |
| Migration de dados em base existente (DML em produção) | × 1.4 |
| Dashboard com query complexa (JOIN 4+ tabelas, subqueries) | × 1.4 |
| Rotina idempotente de reprocessamento (exclui+regera, ramos de estado) | × 1.5 |
| Geração de documento fiscal derivado (NF de quebra/rendimento/remessa) | × 1.4 |
| Operação multiempresa matriz-filial (escrituração entre empresas) | × 1.5 |
| Conversão de unidades/volume bidirecional | × 1.3 |

**Regra:** aplicar multiplicadores sequencialmente sobre a faixa base. Quando mais de um sinal, multiplicar o resultado do anterior.

### Teto de composição (obrigatório)

A composição multiplicativa explode rápido (ex.: PIX ×3.5 → alçada ×1.4 → ambíguo ×1.3 → frontend ×1.5 = ×9.5). Aplicar teto:

- **Produto dos multiplicadores limitado a ×6.0** por story. Se ultrapassar, fixar em ×6.0.
- Multiplicador ultrapassou o teto → é sinal de que a story está grande demais: **voltar à Etapa 6 e refatiar**, não estimar como monólito.
- Integração externa (`×2.0`–`×3.5`) e frontend (`×1.5`) na mesma story → considerar separar backend e frontend em stories distintas antes de compor.

### Sanity-check pós-cálculo (obrigatório antes de exibir)

Após buffer, validar cada faixa contra a realidade:

| Verificação | Ação se falhar |
|---|---|
| Story isolada > 80h após buffer | Refatiar — nenhuma story unitária deve passar de ~2 semanas-dev |
| `max` > 2× `min` | Faixa larga demais → confiança BAIXO + recomendar Estágio 2 |
| Total do projeto > soma "manual" das stories ±15% | Recalcular — erro de composição |
| Faixa abaixo do mínimo do artefato base | Multiplicador aplicado errado |

Registrar qualquer ajuste de teto/refatiamento nas notas da estimativa.

---

## Overhead de fases (substitui o buffer fixo)

O resultado de `base × multiplicadores` é a coluna **Desenvolvimento**. Sobre ele, alocar as demais fases do template (ver proporções em `template-horas-fases.md`):

- Homologação ~7–12% do dev · Simulação ~5% · Documentação piso ~2h (escala em projeto grande) · Produção e acompanhamento 6–30% · Levantamento/Treinamento ~0 salvo módulo com usuário final novo.
- **Overhead total ≈ 28–30% do dev** em projetos ≥70h; **40–55%** em projetos pequenos (piso fixo não escala para baixo).
- Concentrar Documentação/Treinamento na **rotina-âncora** do módulo, não diluir por linha.

O buffer fixo de +30% serve como **aproximação rápida do overhead total** quando não se quer itemizar fase a fase:

```
total_rapido = base × multiplicadores × 1.30   (≈ dev + overhead de fases)
```

Para a saída final, preferir a tabela de 7 fases. Para estimativa rápida (Estágio 1), o ×1.30 é aceitável.

---

## Confronto com estimativa-âncora do documento

Se o documento trouxer um número pré-fechado (pré-vendas: "totalizando 60h", "packs de plataforma"), **detectar e confrontar** com a estimativa itemizada. Exibir: `âncora do documento: Xh · estimativa itemizada: Yh · divergência Z×`. Divergência grande (caso real: 60h → 360h, 6×) = escopo subdimensionado na pré-venda — sinalizar para revisão de proposta. Nunca aceitar a âncora cega nem omiti-la.

---

## Nível de confiança da estimativa

| Condição | Nível |
|---|---|
| Escopo bem definido, poucos pontos abertos, artefatos claros | ALTO |
| Algumas ambiguidades, 1–3 pontos abertos, artefatos identificáveis | MÉDIO |
| Muitos pontos abertos, integração não detalhada, regras vagas | BAIXO |

Com nível BAIXO, recomendar refinamento por esqueleto (Estágio 2) antes de apresentar ao cliente.

---

## Referência de skills por artefato (Estágio 2)

Consultar a skill correspondente ao gerar o esqueleto para refinamento:

| Artefato identificado | Skill para refinamento |
|---|---|
| `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava`, `ScheduledAction`, `Helper`, `Repository`, `Service`, `Controller`, XML Construtor de Telas | `sankhya-modulo-java` |
| `JapeSession`, `NativeSql`, `EntityFacade`, `DynamicVO`, `execWithTX`, `execWithAutonomousTX`, `ProcedureCaller`, batch | `sankhya-jape` |
| `@Listener`, `@Callback`, `@ActionButton`, `@BusinessRule`, `@Job`, `DynamicForm`, `DBScripts`, `DataDictionary` | `sankhya-addon` |
| Telas sankhya-js / HTML5 (AngularJS): `ServiceProxy`, `sk-dataset`, `sk-datagrid`, `sk-wizard`, `SanPopup`, directives | `sankhya-js` |
| Telas Design System (`ez-`/`snk-` components, API Java backend) | `sankhya-addon` |
| Dashboards / gadgets BI (Construtor de Componentes de BI, HTML5 component) | `sankhya-bi` |
| WildFly deploy, DataDictionary runtime, ordem de módulos, `.dodeploy` | — (deploy/runtime) |
| DB migrations idempotentes, dual-dialect (`dbscripts/`, `datadictionary/`) | `sankhya-dicionario` / dbscripts |
| Estrutura de tabelas Sankhya — validar entidades e campos antes de incluir em stories | `sankhya-dicionario` |

---

## Apresentação ao usuário (Estágio 1)

A tabela abaixo é a **representação rápida** (dev + overhead via ×1.30). A saída final preferida é o template de **7 fases por rotina** (`template-horas-fases.md`); use esta forma compacta quando o usuário quiser só a estimativa rápida. Números abaixo derivam de base × multiplicador × 1.3, respeitando o teto ×6:

```
## 12. Estimativa de horas de desenvolvimento

| Story | Abordagem | Artefato principal | Complexidade | Estimativa (h) | Confiança |
|---|---|---|---|---|---|
| Confirmar NF automaticamente | [MÓDULO JAVA] | EventoProgramavelJava | média | 10–15h | MÉDIO |
| Tela de seleção de lote | [ADDON STUDIO] | @ActionButton + DynamicForm | alta | 26–40h | MÉDIO |
| Dashboard de expedicão | [BI/DASHBOARD] | Gadget tabela + filtros | média | 10–18h | ALTO |
| Integração PIX retorno | [MÓDULO JAVA] | AcaoRotinaJava + Controller | alta | 65–117h ⚠️ | BAIXO |

**Total do projeto: 111–190h (após buffer de 30%)**
**Nível de confiança geral: MÉDIO**

> ⚠️ "Integração PIX retorno": base AcaoRotina alta (20–36h) × PIX (×2.5) × buffer 1.3 = 65–117h. Ultrapassa 80h no `max` — pelo sanity-check, refatiar (separar envio, retorno/conciliação e tratamento de erro em stories distintas) antes de fechar a estimativa.

> Estimativa inicial de planejamento — gerada a partir de análise de requisitos sem geração de código.
```

Depois perguntar:

> "Deseja refinar a estimativa das stories de complexidade MÉDIA ou ALTA gerando esqueletos de código via a skill correspondente? Isso permite uma estimativa mais próxima da realidade. (sim / não)"

---

## Estágio 2 — Refinamento por esqueleto (se usuário aceitar)

Para cada story de complexidade MÉDIA ou ALTA:

1. Identificar o artefato e consultar a tabela **"Referência de skills por artefato"** acima para saber qual skill acionar
2. Gerar o **esqueleto** (não a implementação — apenas estrutura: métodos, helpers chamados, DAOs, integrações, componentes de tela)
3. Contar a partir do esqueleto:
   - Número de helpers/services externos chamados → cada um adiciona 1–2h se não existir
   - Número de DAOs/entidades acessadas → sinal de complexidade de persistência
   - Chamadas a sistemas externos → confirmar/ajustar multiplicador de integração
   - Condicionais e branches → sinal de regras adicionais
   - Componentes de tela listados → verificar existência ou necessidade de criar
4. Recalcular a faixa com base no esqueleto + reaplicar buffer de 30%

### Apresentação lado a lado

```
| Story | Estimativa Rápida | Estimativa Refinada |
|---|---|---|
| Confirmar NF automaticamente | 10–15h | 14–20h |
| Tela de seleção de lote | 26–40h | 32–50h |
| Dashboard de expedição | 10–18h | 10–18h |
| Integração PIX retorno | 65–117h | 78–140h |
| **Total** | **111–190h** | **134–228h** |
```

### Pergunta final

> "Qual estimativa deseja registrar no plano?
> 1. Rápida (XX–XXh) — baseada em análise de requisitos
> 2. Refinada (XX–XXh) — baseada em esqueleto de código
> 3. Ambas — registrar as duas para comparação"

Registrar a escolha do usuário no JSON de saída.

---

## Campo JSON de estimativa (forma rápida, sem itemização de fases)

Use este formato apenas na estimativa rápida (Estágio 1) sem fases. Para a saída final no template de 7 fases, usar o bloco `phases` definido em `references/schema-saida.md`.

```json
"estimated_hours": {
  "stage": "rapida | refinada | ambas",
  "quick_estimate": { "min": 111, "max": 190 },
  "refined_estimate": { "min": 134, "max": 228 },
  "chosen_estimate": { "min": 134, "max": 228 },
  "confidence": "medio",
  "buffer_applied": "30% (aproximação do overhead de fases)",
  "notes": "Forma rápida; itemização por fases em schema-saida.md"
}
```
