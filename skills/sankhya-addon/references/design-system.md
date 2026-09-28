# Sankhya Design System — Índice

Biblioteca de web components (React 18 + pipeline Node) para telas no Sankhya Om. Dois prefixos:

- **`ez-`** — UI genérica (`@sankhyalabs/ezui`)
- **`snk-`** — blocos acoplados ao ERP: dicionário, DataUnit, serviços (`@sankhyalabs/sankhyablocks`)

> **Não é o padrão.** Telas personalizadas usam **sankhya-js** por padrão. Design System só quando o projeto já tem pipeline Node **e** o usuário pediu explicitamente. Ver `SKILL.md`, seção "Telas Personalizadas — Pergunta Obrigatória".

---

## Como usar

1. **Sempre leia primeiro `references/design-system/guia.md`**: setup correto, regras HTML × React, receita de tela `snk-*`, DataUnit e as armadilhas da doc oficial.
2. Localize o componente/classe em `references/design-system/INDICE.md` e leia **só** o arquivo dele. Cada arquivo traz a doc oficial completa: exemplos React, tabelas de Properties (com o atributo HTML), Events, Methods, Slots e CSS Variables.
3. Prefira os exemplos de código às frases da prosa quando divergirem, e confira a seção 5 do guia antes de copiar qualquer exemplo.

| Pasta | Conteúdo |
|---|---|
| `design-system/componentes/` | Um arquivo por componente: `ez-*.md` (70) e `snk-*.md` (19) |
| `design-system/layout/` | Classes de layout (flex, grid, box, content, margin, padding, text, title, labels, icons) e tokens Acorde (`acorde-*.md`; `acorde-tokens.md` é **depreciado**) |
| `design-system/setup/` | `configure.md`, `overview.md`, `collaborate.md`, `onboarding-bff.md` |
| `design-system/core/` | TypeDoc de `@sankhyalabs/core`: `classes/`, `interfaces/`, `enumerations/`, `functions/`, `type-aliases/`, `variables/`, `namespaces/`; guias de DataUnit em `core/guias/` |
| `design-system/api-java/` | `sankhya-bff` (5 interfaces) e `sanmodule` (`BootModuleListener`) |

---

## Atualização do snapshot

Os arquivos em `design-system/` (exceto `guia.md`) são **gerados**. Não edite à mão e não os atualize via WebFetch durante uma tarefa: o HTML estático do site não traz os exemplos de código (eles são renderizados por JS), e sobrescrever o arquivo local apagaria conteúdo correto.

Para atualizar, rode `scripts/atualizar-design-system/` (instruções no `README.md` da pasta) e revise o `guia.md` contra o diff.

Fonte online: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ — cada arquivo gerado começa com a URL da página de origem.
