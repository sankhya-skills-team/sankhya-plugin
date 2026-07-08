# Fatiamento de stories e critérios de aceite

Detalhe operacional das Etapas 6 (Story Slicing) e 7 (Critérios de aceite).

---

## Etapa 6 — Story Slicing

### Diagnóstico de complexidade antes de fatiar
- [ ] Epic tem múltiplos fluxos alternativos (happy path + variações)?
- [ ] Contém várias operações CRUD independentes na mesma entidade?
- [ ] Envolve múltiplos atores com necessidades distintas?
- [ ] Abrange múltiplas camadas ou plataformas (backend + frontend + BI)?
- [ ] Cada parte potencial entrega valor se entregue isolada?

### 5 técnicas de fatiamento — aplicar a mais adequada

| Técnica | Quando usar | Resultado esperado |
|---|---|---|
| **Por fluxo** | Happy path + múltiplas exceções ou variações | Entregar happy path primeiro, exceções depois |
| **Por CRUD** | Várias operações independentes na mesma entidade | Priorizar a operação mais crítica para o negócio |
| **Por ator** | Perfis/personas com necessidades distintas | Persona de maior impacto primeiro |
| **Por plataforma** | Backend + frontend + dashboard no mesmo epic | Backend/API primeiro, clients depois |
| **Híbrido** | Complexidade em múltiplas dimensões | Combinar 2+ técnicas conforme contexto |

### Teste de valor independente (obrigatório por story)
"Se entregarmos apenas esta story, algum usuário percebe valor?"
- ✅ Sim → story válida, prosseguir
- ❌ Não → é tarefa técnica, não story — mover para Etapa 8

### Anti-patterns de fatiamento
- Fatiamento por camada técnica (banco → API → frontend) — nenhuma camada entrega valor isolada
- Micro-stories (1 botão = 1 story, 1 validação = 1 story) — overhead supera o valor
- Spike disfarçado de story ("pesquisar tecnologia X") — separar spike da story de implementação

Cada story representa: uma automação observável, uma regra relevante, uma exceção crítica, uma integração específica ou uma operação de usuário ponta a ponta.

---

## Etapa 7 — Critérios de aceite

### Inventário de critérios antes de escrever — classificar cada um

| Nível | Sinal | Ação |
|---|---|---|
| 🔴 CRÍTICO | Termos subjetivos ("correto", "rápido", "fácil"), resultado não verificável | Refinar antes de registrar |
| 🟡 ATENÇÃO | Contexto parcial, ação ou resultado vagos | Refinar |
| 🟢 OK | Given-When-Then completo, sem termos vagos, verificável por testes | Preservar |

**Regra obrigatória:** nunca misturar critério funcional e não-funcional no mesmo AC. Separar em itens distintos.

### Anti-patterns de critérios de aceite

| Anti-pattern | Problema | Correção |
|---|---|---|
| `"O sistema deve ser rápido"` | Subjetivo, não verificável | Definir comportamento observável esperado |
| `"Validação deve funcionar corretamente"` | Tautológico, sem expectativa definida | 1 critério por regra de validação |
| `"Usuário pode criar, editar e excluir"` | Múltiplos cenários em 1 AC | Separar: AC-criar, AC-editar, AC-excluir |
| `"Quando clicar Salvar → item salvo"` | Sem Given — quem? qual item? tem permissão? | Adicionar Given com papel, item e pré-condição |
| `"Implementar com cache Redis"` | Descreve implementação, não comportamento | Reescrever como resultado observável pelo usuário |

Cada story recebe critérios orientados a comportamento (dado / quando / então).
