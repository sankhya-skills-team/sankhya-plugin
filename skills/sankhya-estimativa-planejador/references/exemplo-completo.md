# Exemplo end-to-end — escopo → 13 seções

Referência de saída esperada. Demonstra o nível de detalhe, rastreabilidade (`source_refs`), uso da Etapa 2.5 (MCP) e o formato das 13 seções. Domínio: pesagem de café (Módulo Java). Adaptar ao escopo real — não copiar números.

---

## Escopo de entrada (documento bruto recebido)

> **1. Pesagem de entrada**
> 1.1 Ao finalizar a pesagem do caminhão, o sistema deve confirmar automaticamente a nota de compra vinculada.
> 1.2 Se a diferença entre peso bruto e tara estiver fora da tolerância do contrato, bloquear a confirmação e avisar o operador.
> 1.3 Operadores com perfil "Supervisão" podem liberar pesagens fora da tolerância.
>
> **2. Acompanhamento**
> 2.1 A gerência quer um painel com o total pesado por dia e por procedência.

---

## Saída estruturada

### 0. Identificação
- **Parceiro:** Cafeicultura Modelo Ltda
- **Processo / Subprocesso:** Controle de Armazenagem / Pesagem de Entrada (cód. 30xxx)
- **Usuário-chave:** (responsável por validar a regra de tolerância)
- **Responsável pela área:** (patrocinador)
- **Status de validação:** escopo aprovado em ata
- **Documentos de entrada referenciados:** Levantamento de Regras — Pesagem (sem dependência documental pendente neste recorte)

### 1. Resumo executivo
Automatizar a confirmação da nota de compra ao concluir a pesagem de entrada de café, com bloqueio por tolerância de contrato e liberação por alçada, mais um painel gerencial de volume pesado. Predominância backend → **Módulo Java**; painel isolado em epic de BI.

### 2. Domínios funcionais identificados
- Pesagem de entrada (automação + regra)
- Acompanhamento gerencial (BI)

### 3. Mapa de impacto
| Domínio | Objetivo operacional | Atores | Impacto | Entregas candidatas |
|---|---|---|---|---|
| Pesagem | Eliminar confirmação manual da NF | Operador de balança, Supervisão | Fluxo encerra sem ação manual; exceção controlada | Listener de finalização, regra de tolerância, liberação por alçada |
| Acompanhamento | Visibilidade de volume | Gerência | Decisão sobre dados consolidados | Gadget BI |

### 4. Epics propostos
- **EPIC-001 — Pesagem de entrada automatizada** `[MÓDULO JAVA]`
- **EPIC-002 — Painel de acompanhamento de pesagem** `[BI/DASHBOARD]`

### 5. Story map por epic
**EPIC-001 — Backbone:** finalizar pesagem → validar tolerância → confirmar NF.
Exceções: fora da tolerância (bloqueio); liberação por supervisão.

### 6. Stories propostas
- **STORY-001** — Confirmar automaticamente a NF de compra ao finalizar a pesagem (`source_refs: 1.1`)
- **STORY-002** — Bloquear confirmação quando peso fora da tolerância do contrato (`source_refs: 1.2`)
- **STORY-003** — Liberar pesagem fora de tolerância por alçada de Supervisão (`source_refs: 1.3`)
- **STORY-004** — Gadget de total pesado por dia e procedência (`source_refs: 2.1`)

Fatiamento por fluxo (happy path 001, exceção 002/003) + plataforma (004 isolado).

### 7. Critérios de aceite (exemplo STORY-002)
- 🟢 Dado que a pesagem foi finalizada, quando a diferença bruto−tara exceder a tolerância do contrato, então a confirmação da NF deve ser bloqueada e o operador avisado com a tolerância esperada × medida.
- 🟢 Dado bloqueio por tolerância, quando o operador não tiver perfil Supervisão, então a liberação não deve ser oferecida.

(funcional e não-funcional separados; sem termos vagos)

### 8. Tarefas técnicas iniciais
**Validação via MCP (Etapa 2.5):** `search_entities("pesagem")` → `TGAPES` (PesagemMultipla), `TGAPESI` (ItensPesagem); nota = `TGFCAB`. Tolerância de contrato: campo não localizado em `describe_table` → **criar `AD_PESOTOLER`** (campo adicional).

- EPIC-001
  - [ ] `EventoProgramavelJava` no after-update de `TGAPES` (status finalizado)
  - [ ] `ConfirmarNotaHelper` — invocar confirmação de `TGFCAB` vinculada
  - [ ] Regra de tolerância lendo `AD_PESOTOLER` do contrato (campo a criar)
  - [ ] Checagem de perfil via `TSILIB` para liberação
- EPIC-002
  - [ ] Gadget tabela com query por dia × procedência (`TGFPAR` procedência)

### 9. Dependências e riscos
- Campo `AD_PESOTOLER` inexistente — depende de definição da fórmula de tolerância. `[PENDENTE: confirmar com cliente]`
- Oracle ou SQL Server? altera SQL do gadget.

### 10. Itens ambíguos para validação
- 1.2: "tolerância do contrato" — percentual fixo, faixa por produto ou por procedência? `[HIPÓTESE: percentual por contrato]`

### 11. Recomendação de abordagem técnica
**Abordagem geral:** HÍBRIDO (Módulo Java + BI)

| Epic | Abordagem | Artefatos | Justificativa |
|---|---|---|---|
| EPIC-001 | [MÓDULO JAVA] | EventoProgramavelJava, Helper, Regra | Automação backend, sem UI nova |
| EPIC-002 | [BI/DASHBOARD] | Gadget tabela + filtros | Visualização analítica |

### 12. Estimativa de horas (template de 7 fases)
Estágio 1 — ponto médio da faixa de dev por rotina; demais fases por cima (Doc/Treino concentrados na rotina-âncora STORY-001).

| Rotina | Abordagem | Lev. | Dev. | Homol. | Trein. | Simul. | Doc. | Prod. | Total |
|---|---|---|---|---|---|---|---|---|---|
| Confirmar NF ao finalizar pesagem (âncora) | [MÓDULO JAVA] | 1 | 13 | 2 | 2 | 1 | 6 | 2 | 27 |
| Bloquear fora da tolerância + campo AD | [MÓDULO JAVA] | – | 12 | 1 | – | 1 | – | 1 | 15 |
| Liberar por alçada (TSILIB) | [MÓDULO JAVA] | – | 14 | 2 | – | 1 | – | 1 | 18 |
| Gadget total pesado | [BI/DASHBOARD] | – | 11 | 1 | – | – | 1 | 1 | 14 |
| **Total** | | **1** | **50** | **6** | **2** | **3** | **7** | **5** | **74** |

**Total do projeto: 74h** · **Âncora do documento:** não informada · **Confiança geral: MÉDIO**
Overhead não-dev (24h / 50h dev = 48%) coerente com projeto pequeno; nenhuma rotina > 80h.

### 13. Estrutura para integração com cards
Ver schema em `references/schema-saida.md`. Cada story preenchida com `acceptance_criteria`, `technical_tasks`, `source_refs` e, quando MCP usado, `schema_validation` (`entities_confirmed: [TGAPES, TGAPESI, TGFCAB]`, `fields_to_create: [AD_PESOTOLER]`).
