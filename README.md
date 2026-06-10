# Plugin Sankhya

Plugin do Claude Code com skills, agents e hook para desenvolvimento no **ERP Sankhya**.

## Conteúdo

### Skills (`skills/`)
| Skill | Quando aciona |
|---|---|
| `sankhya-addon` | Addon Studio: `@ActionButton`, `@Listener`, `@Job`, `DynamicVO`, `JapeFactory`, SDK Sankhya. |
| `sankhya-modulo-java` | Módulo Java: `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava`, helpers dstech. |
| `sankhya-relatorio` | Relatórios JasperReports / iReport / `.jrxml`, impressão Sankhya. |
| `sankhya-bi` | Dashboards e componentes de BI no Sankhya OM (Construtor de Componentes). |

### Agents (`agents/`)
Suíte de code review para projetos Java Sankhya. `code-review-orchestrator` coordena os demais:
`arch-reviewer`, `clean-code`, `security-scanner`, `perf-analyzer`, `doc-checker`.

### Hook (`hooks/sankhya-encoding.js`)
`PostToolUse` (Write/Edit/MultiEdit). Converte `.java/.xml/.kt` para **ISO-8859-1** —
padrão de encoding do Addon Studio. Só age dentro de projeto Sankhya (ancestral com pasta
`datadictionary` ou `dbscripts`). Idempotente; nunca bloqueia o fluxo.

## Instalação

```
/plugin marketplace add sankhya-skills-team/sankhya-plugin
/plugin install sankhya@sankhya
```

Requer `node` no PATH (para o hook).

## Atualização

```
/plugin update sankhya
```

## Como adicionar conteúdo ao plugin

| Adicionar | Onde | Edita plugin.json? |
|---|---|---|
| Skill | `skills/<nome>/SKILL.md` | Não (auto-load) |
| Command `/x` | `commands/x.md` | Não (auto-load) |
| Agent | `agents/x.md` (frontmatter `name`/`description`) | Não (auto-load) |
| Refs/assets de skill | dentro da própria `skills/<nome>/` (caminho relativo) | Não |
| Hook | script em `hooks/`, registrar bloco `hooks` | Sim |
| MCP server | bloco `mcpServers` | Sim |

Após adicionar: bump `version` em `.claude-plugin/plugin.json` → commit → push → devs rodam `/plugin update`.

## Pendente

- **MCP `sankhya-schema`**: ainda **não** incluído. Projeto Python separado (Oracle instantclient
  ~80 MB + credenciais), instalado à parte. Avaliar integração futura via `mcpServers` apontando
  para install externa.
