# Schema JSON de saída do backlog

Estrutura completa do arquivo `[nome-projeto]-backlog.json`. Cada story deve conter todos os campos do schema — nunca omitir `acceptance_criteria` nem `technical_tasks`.

```json
{
  "project_summary": {
    "title": "nome do escopo",
    "objective": "objetivo consolidado",
    "domains": ["dominio1", "dominio2"],
    "technical_approach": {
      "overall": "modulo_java",
      "cost_level": "baixo"
    }
  },
  "epics": [
    {
      "epic_id": "EPIC-001",
      "name": "Nome do epic",
      "objective": "Objetivo do epic",
      "technical_approach": {
        "classification": "[MÓDULO JAVA]",
        "key_artifacts": ["AcaoRotinaJava"],
        "justification": "Automação sem nova UI"
      },
      "story_map": {
        "backbone": ["passo 1", "passo 2"],
        "exceptions": ["excecao 1"]
      },
      "stories": [
        {
          "story_id": "STORY-001",
          "title": "Título da story",
          "user_value": "Valor entregue",
          "description": "Descrição curta",
          "complexity": "media",
          "acceptance_criteria": ["Dado ... quando ... então ..."],
          "technical_tasks": ["Task técnica 1"],
          "dependencies": ["Dependência 1"],
          "risks": ["Risco 1"],
          "source_refs": ["1.1.5"],
          "technical_approach": {
            "recommendation": "modulo_java",
            "key_artifacts": ["AcaoRotinaJava"],
            "justification": "Botão de ação sem nova UI"
          },
          "estimated_hours": {
            "stage": "rapida",
            "quick_estimate": { "min": 8, "max": 14 },
            "refined_estimate": null,
            "chosen_estimate": { "min": 8, "max": 14 },
            "confidence": "medio",
            "buffer_applied": "30% (forma rápida; ver bloco phases para o template de 7 fases)"
          }
        }
      ]
    }
  ],
  "project_estimated_hours": {
    "stage": "rapida",
    "quick_estimate": { "min": 90, "max": 136 },
    "refined_estimate": null,
    "chosen_estimate": { "min": 90, "max": 136 },
    "confidence": "medio"
  },
  "open_questions": ["Pergunta 1"]
}
```

## Campos obrigatórios por story

`story_id`, `title`, `user_value`, `description`, `complexity`, `acceptance_criteria[]`, `technical_tasks[]`, `dependencies[]`, `risks[]`, `source_refs[]`, `technical_approach`, `estimated_hours`.

## Campo `estimated_hours` com refinamento (Estágio 2 aplicado)

```json
"estimated_hours": {
  "stage": "ambas",
  "quick_estimate": { "min": 111, "max": 190 },
  "refined_estimate": { "min": 134, "max": 228 },
  "chosen_estimate": { "min": 134, "max": 228 },
  "confidence": "medio",
  "buffer_applied": "30%",
  "notes": "Refinamento via esqueleto aplicado nas stories de complexidade média e alta"
}
```

## Estimativa no template de 7 fases (por rotina)

Quando a estimativa segue o template oficial, registrar as fases por rotina e o confronto com a âncora:

```json
"estimated_hours": {
  "stage": "rapida",
  "phases": {
    "levantamento": 1, "desenvolvimento": 44, "homologacao": 9,
    "treinamento": 4, "simulacao": 6, "documentacao": 18, "producao_acompanhamento": 2
  },
  "total": 84,
  "anchor_estimate": { "value": 60, "source": "pré-vendas (packs de plataforma)", "divergence": "1.4x" },
  "confidence": "medio"
}
```

`anchor_estimate` é null quando o documento não traz número pré-fechado. Para gêneros as-built, `estimated_hours` é null (não estimar).

## Validação de entidades (quando MCP sankhya-schema usado)

Opcional: registrar em cada story quais entidades foram confirmadas contra o schema real, para rastreabilidade da confiança.

```json
"schema_validation": {
  "validated": true,
  "entities_confirmed": ["TGFCAB", "TGAPES"],
  "fields_to_create": ["AD_CODLOTE"],
  "not_found": []
}
```
