# CLAUDE.md — sankhya-plugin

Instruções do projeto para agentes que trabalham neste repositório.

## Commits

- **Nunca** incluir menção ao Claude/IA nas mensagens de commit. Sem linha `Co-Authored-By: Claude`, sem "Generated with Claude Code", sem emoji de robô.
- Conventional Commits. Assunto ≤50 chars, corpo só quando o "porquê" não é óbvio.
- Idioma PT-BR.

## Release / distribuição

- Este plugin é distribuído aos colegas via marketplace (auto-update do git).
- **Todo commit que altera `skills/`, `agents/` ou `hooks/` DEVE bumpar `version` em `.claude-plugin/plugin.json`.**
- Sem bump, versão idêntica impede a detecção de update → colegas não recebem as mudanças.
- SemVer: skill/agent novo = MINOR; fix = PATCH; breaking = MAJOR.

## Frontmatter de skill (SKILL.md)

- Usar **apenas** `name` e `description` (campos que o Claude Code lê).
- **Não** incluir `version` na skill — versão é única em `plugin.json`. Version na skill é decorativo, ninguém lê, e confunde com o version que dispara distribuição.
