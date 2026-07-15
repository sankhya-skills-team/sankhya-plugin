# Plugin Sankhya

Plugin do Claude Code com skills, agents e hook para desenvolvimento no **ERP Sankhya**.

## Conteúdo

### Skills (`skills/`)
| Skill | Quando aciona |
|---|---|
| `sankhya-addon` | Addon Studio: `@ActionButton`, `@Listener`, `@Job`, `DynamicVO`, `JapeFactory`, SDK Sankhya. |
| `sankhya-modulo-java` | Módulo Java: `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava`, helpers de customização. |
| `sankhya-jape` | Persistência JAPE: `JapeSession`, `NativeSql`, `EntityFacade`, `DynamicVO`, `execWithTX`, transações, macros portáveis Oracle/SQL Server. |
| `sankhya-relatorio` | Relatórios JasperReports / iReport / `.jrxml`, impressão Sankhya. |
| `sankhya-bi` | Dashboards e componentes de BI (gadgets) no Sankhya OM: Construtor de Componentes de BI, gráficos, XML `TSIGDG.CONFIG`, HTML5. |
| `sankhya-dicionario` | Dicionário de dados Sankhya OM: ~730 tabelas mapeadas (campos, PKs, FKs, enums, entityNames), metamodelo TDD, relacionamentos. |
| `sankhya-js` | Framework frontend AngularJS 1.x (`sankhya-js`): telas HTML5, `ServiceProxy`/`FluidBuilder`, componentes (grid, dataset, wizard, popup), MetadataProvider, i18n. |
| `sankhya-estimativa-planejador` | Análise de requisitos funcionais → backlog (epics/stories/critérios), recomendação Addon × Módulo Java e estimativa de horas em 7 fases. |
| `sankhya-gera-escopo` | Geração de documento de escopo `.docx` (proposta técnica) a partir de contexto bruto, preservando template Word padrão. |
| `sankhya-commit` | Commit Git interativo: analisa o diff e gera mensagem Conventional Commits com emojis. |
| `sankhya-doc-entrega` | Gera documento de entrega de desenvolvimento em `.html` interativo ou `.docx` Word (à escolha) para projetos Java Sankhya. |

### Agents (`agents/`)
Suíte de code review para projetos Java Sankhya. `code-review-orchestrator` coordena os demais:
`arch-reviewer`, `clean-code`, `security-scanner`, `perf-analyzer`, `doc-checker`.

### Hooks (`hooks/`)

| Hook | Evento | O que faz |
|---|---|---|
| `sankhya-encoding.js` | `PreToolUse` (Read) · `PostToolUse` (Write/Edit/MultiEdit) · `Stop`/`SessionEnd` | Encoding **bidirecional** ISO-8859-1 ⇄ UTF-8 para `.java/.xml/.kt`. **Antes do Read** (`--pre`): arquivo Latin-1 é exposto como UTF-8 (lossless) para a leitura não corromper acentos. **Após Write/Edit**: converte de volta para **ISO-8859-1** + transliteração ASCII; se detectar `U+FFFD` (leitura corrompida), **aborta** e instrui recuperação em vez de gravar `?`. **No Stop/SessionEnd** (`--flush`): arquivos lidos mas não editados voltam a ISO-8859-1. Gate híbrido: pasta de artefato Sankhya (`datadictionary`/`dbscripts`/`dbquerys`/`dashboards`) ou marcadores Sankhya no conteúdo. Idempotente; nunca bloqueia o fluxo. |
| `sankhya-autoupdate-nudge.js` | `SessionStart` (startup/clear/compact) | Lembra 1×/dia para ligar o auto-update do marketplace, se estiver desligado. Só leitura — nunca edita config. |

Ambos são **Node.js puro** (multi-OS) e exigem só `node` no `PATH`.

## Instalação

```
/plugin marketplace add sankhya-skills-team/sankhya-plugin
/plugin install sankhya@sankhya
```

### Pré-requisito (todos os SO)

Os hooks são **Node.js puro** — funcionam igual em **Windows, Linux e macOS**.
Exige apenas `node` no `PATH`:

| SO | Instalar node |
|---|---|
| Windows | `winget install OpenJS.NodeJS` ou instalador oficial |
| Linux | gerenciador da distro (`apt/dnf/pacman`) ou `nvm` |
| macOS | `brew install node` ou `nvm` |

Verificar: `node --version`. Sem dependência de shell, caminho absoluto ou script `.ps1/.sh`.

## Atualização

Manual:
```
/plugin marketplace update sankhya   # recarrega catálogo
/plugin update sankhya@sankhya       # baixa + aplica
/reload-plugins                      # ativa sem reiniciar
```

### Auto-update (recomendado)

Por padrão o auto-update vem **desligado** em marketplace não-oficial. Com ele ligado,
o Claude Code baixa a versão nova ao iniciar; basta `/reload-plugins`.

Ligar pela UI:
```
/plugin  ->  Marketplaces  ->  sankhya  ->  Enable auto-update
```

Ou no seu `settings.json`:
```json
{
  "extraKnownMarketplaces": {
    "sankhya": {
      "source": { "source": "github", "repo": "sankhya-skills-team/sankhya-plugin" },
      "autoUpdate": true
    }
  }
}
```

> O plugin lembra **1×/dia** no início da sessão se o auto-update estiver desligado
> (hook `sankhya-autoupdate-nudge.js`, só leitura — nunca edita sua config). O aviso
> some sozinho quando você liga.

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

## Autores

Skills, agents e hooks deste plugin são desenvolvidos e mantidos por:

- **Felipe Rosa da Silva**
- **Daniel Ratkevicius**
- **Claiton Trisch Farias**
