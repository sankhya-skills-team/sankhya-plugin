# skill-sankhya-estimativa-planejador

Skill para Claude Code especializada em **análise de requisitos funcionais para projetos Sankhya OM** — converte documentos de escopo em backlog estruturado com epics, stories, critérios de aceite, recomendação de abordagem técnica (Módulo Java × Addon Studio) e estimativa de horas de desenvolvimento.

---

## O que esta skill faz

Transforma documentação funcional bruta — escopos complementares, levantamentos de regras de negócio, atas de alinhamento, especificações de feature — em um plano de implementação completo e rastreável, pronto para integração com Trello, Jira ou ferramenta equivalente.

---

## Estrutura da Skill

```
sankhya-estimativa-planejador/
├── SKILL.md          Instruções principais e método obrigatório (13 etapas)
└── references/       Heurísticas ERP, calibração real, fatiamento, gêneros de
                      documento, template de horas (7 fases), schema JSON,
                      addon × módulo-java, exemplo end-to-end e padrões Sankhya
```

Ver a tabela de referências ao final do `SKILL.md` para o índice completo dos arquivos.

---

## Resultado da Análise

```
 1. Resumo executivo
 2. Domínios funcionais identificados
 3. Mapa de impacto
 4. Epics propostos
 5. Story map por epic
 6. Stories fatiadas verticalmente
 7. Critérios de aceite (dado / quando / então)
 8. Tarefas técnicas iniciais
 9. Dependências e riscos
10. Itens ambíguos para validação
11. Recomendação de abordagem técnica (Módulo Java × Addon Studio × Híbrido)
12. Estimativa de horas (dois estágios)
13. JSON estruturado para futura integração com cards
```

---

## Recomendação de Abordagem Técnica

A skill classifica automaticamente cada epic com base nos artefatos identificados:

| Classificação | Quando aplicar |
|---|---|
| `[MÓDULO JAVA]` | Automações sem nova UI — eventos, botões, jobs, regras de negócio |
| `[ADDON STUDIO]` | Requer tela customizada, formulário ou dashboard com interface nova |
| `[HÍBRIDO]` | Parte sem UI (Módulo Java) + parte com UI (Addon Studio) |
| `[CONFIGURAÇÃO]` | Apenas parâmetros/preferências, sem desenvolvimento Java |

**Regra default:** sem evidência de necessidade de frontend → **Módulo Java** (menor custo).

---

## Estimativa de Horas — Dois Estágios

### Estágio 1 — Estimativa rápida (sempre executado)

Calculada automaticamente com:
- Faixa base por tipo de artefato
- Multiplicadores detectados no texto (regras, integrações, alçadas, ambiguidades)
- Buffer fixo de +30%
- Nível de confiança (ALTO / MÉDIO / BAIXO) por story

### Estágio 2 — Refinamento por esqueleto (sob demanda)

Após exibir a estimativa rápida, a skill pergunta se o usuário deseja refinar usando `sankhya-modulo-java` ou `sankhya-addon` para gerar esqueletos das classes. A partir do esqueleto real, a estimativa é recalculada e apresentada lado a lado com a estimativa rápida. O usuário escolhe qual registrar.

```
| Story                   | Estimativa Rápida | Estimativa Refinada |
|-------------------------|-------------------|---------------------|
| Botão Gerar Faturamento | 28–42h            | 35–52h              |
| API Integração Externo  | 58–88h            | 72–110h             |
| Total                   | 90–136h           | 111–168h            |
```

---

## Documentos de Entrada Aceitos

- Levantamento de regras de negócio
- Escopo complementar
- Documentação funcional
- Requisitos de personalização
- Especificação de feature
- Atas e documentos de alinhamento funcional

---

## Ativação

A skill é ativada automaticamente quando o usuário menciona:

- "analisar requisitos", "analisar escopo"
- "transformar escopo em backlog"
- "levantar histórias", "gerar épicos e stories"
- "decompor feature", "refinamento técnico"
- "estimar horas de desenvolvimento"
- "quanto tempo vai levar"
- "análise de escopo Sankhya"

Ou via comando:

```
/sankhya-estimativa-planejador
```

---

## Integração com outras Skills

Esta skill pode acionar automaticamente:

- **`sankhya-modulo-java`** — para gerar esqueletos de `EventoProgramavelJava`, `AcaoRotinaJava`, `ScheduledAction`, `RegraNegocioJava` (Estágio 2 da estimativa)
- **`sankhya-addon`** — para gerar esqueletos de ActionButton, Listener, Job do Addon Studio (Estágio 2 da estimativa)
