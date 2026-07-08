# Calibração real de esforço (medida em código de projetos entregues)

Base empírica medida em projetos reais de clientes (addons e módulos de portes variados). Corrige a subestimação das faixas calibradas em planilhas *vendidas*.

## Achado central: as planilhas vendidas subestimam

As faixas de `heuristicas-estimativa.md` foram calibradas nas planilhas `Template horas` — que são estimativas **vendidas** em módulo-java, não esforço medido. Medindo o código entregue:

- **Projeto A (módulo-java):** planilha = 282h dev / 360h total. Bottom-up do código real = **460–610h dev**. Subestimação **1,6–2,2×**.
- Causas: repositories/DAO com SQL Oracle pesado somem nas linhas funcionais; frontend/dashboards não itemizados; "estrutura de OS = 8h" virou 21 tabelas AD_ / 240 campos (~50h).

**Regra:** o total da planilha (e do buffer +30%) é **piso comercial**, não esforço real. Para estimativa realista, usar o método bottom-up abaixo **ou** aplicar fator de realismo **×1,6–2,2** sobre a base vendida — especialmente quando a abordagem correta é addon.

## Produtividade observada

- **Java de negócio Sankhya** (com JAPE, queries Oracle, EntityFacade, teste manual): **~12 LOC efetivas/hora**.
- **Frontend (JSP/JS/markup):** ~25–30 LOC/hora (parte é markup repetitivo).
- Inverter LOC/produtividade dá o piso de horas; somar fases (template de 7 fases) por cima.

## Peso relativo por artefato (unidade = botão de ação simples ≈ 100 LOC ≈ 1,0×)

| Artefato | LOC médio medido | Peso | Dev (h) aprox. |
|---|---|---|---|
| Botão de ação simples (baixa) | 86–114 | 1,0× | 8–12 |
| Botão complexo (gera financeiro/documento, alta) | 120–160 | 1,5–2× | 16–24 |
| Evento / Listener | 71–115 | 0,7–1,1× | 6–14 |
| Regra de negócio | 83 | 0,8× | 6–12 |
| Helper / Service simples | 62–134 | 0,5–1,3× | 5–14 |
| Service de negócio (lógica densa) | 197 (até 486) | 1,5–4× | 16–40 |
| Repository / DAO com SQL Oracle pesado | 176 (até 515) | 1,5–4× | 16–40 |
| **EJB stub** (tripé Session/Home/SP gerado) | 23 cada | 0,7× (boilerplate) | 4–8 |
| **EJB bean + Service completo** (serviço backend) | 400–700 | **4–6×** | **40–70** |
| Relatório jrxml composto | 217–490 | ~5× | 16–24 (conjunto até 40) |
| Dashboard BI gadget | — | 2–3× | 16–24 |
| **Frontend vc denso** (html/js que integra EJB; ex. dashboard Kanban) | 3.000–4.100 | **8–16×** em horas | **80–160** |
| Frontend vc médio (tela de gestão) | 750–1.700 | — | 30–70 |
| Tela Construtor de Telas (metadados) | — | — | ~1/tabela + campos |
| Tabela AD_ / datadictionary | — | — | 2–6 (com FKs) |

> Critério de complexidade por LOC efetivas: **baixa <80 · média 80–250 · alta >250**.

## Pegadinhas confirmadas

1. **EJB pesa pela camada Service que expõe, não pelo bean isolado.** O tripé stub é boilerplate barato (~23 LOC); o custo está no `Service` (até 486 LOC). Um "serviço EJB completo" vale **4–6 botões de ação**.
2. **Frontend vc é o artefato dominante e mais caro** em addon com UI própria. Num addon de gestão de projetos medido, o frontend (~25.850 LOC) é **maior que todo o backend** (15.160 LOC) — pode concentrar >50% do esforço. Uma tela vc densa equivale a dezenas de botões.
3. **Repositories/DAO com SQL Oracle** são a maior fatia oculta de esforço — não aparecem nas "linhas funcionais" da planilha.
4. **Telas/tabelas (Construtor) não são mensuráveis por LOC** — o esforço está em desenho de campos/abas, não em código. Estimar por nº de tabelas/campos.

## Uplift por abordagem

- **Módulo-java** medido com as faixas acima (já realistas, não as vendidas).
- **Addon com UI própria (frontend vc / DynamicForm):** o frontend vc domina — somar as telas vc explicitamente, não tratar como "tela de 4h". É o que faz um addon real (ex.: controle de OS) chegar a 600h+ enquanto a planilha vendida em módulo-java dizia 360h.

## Limitações honestas

- Horas derivadas de LOC/produtividade, **não cronometradas** — bandas refletem incerteza.
- Amostra de pareamento hora↔código é pequena (vários projetos sem código no repo). O ponto mais sólido: **botão Java que gera financeiro/altera nota ≈ 16–20h (~14h/100 SLOC)** e **produtividade ~12 LOC/h** no Java de negócio.


## Multiplicadores medidos por esqueleto (Projeto B, addon do zero)

Estágio 2 (geração de esqueleto Addon Studio) vs estimativa rápida do piso comercial:

| Arquétipo | Rápida | Refinada (addon) | Fator |
|---|---:|---:|---:|
| NF derivada quebra/rendimento (listener+service+helpers+CACHelper+TGFFIN+TGFVAR) | 28h | ~95-100h | ~3,5× |
| ScheduledAction financeira idempotente (5 ramos, TX autônoma) | 28h | ~67h | ~2,4× |
| Camada de dados saldo (2 tabelas AD_, 24 campos, repo FIFO+estorno) | 40h | ~59h | ~1,5× |
| Tela vc própria densa (wizard + validação tempo real + popups + assinatura) | 28h | 80-126h | ~3,8× |
| Pacote de dashboards BI (3 dash, 13 gadgets) | 72h | 32-49h | <1× |

**Regra prática:** UI vc própria e regra financeira sobre núcleo comercial são os maiores fatores de subestimação (3-4×). BI tende a ficar igual ou abaixo do piso. Sempre somar E0 (rebuild) quando addon-from-scratch sobre base existente.
