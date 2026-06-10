# Plugin Sankhya

Plugin do Claude Code com skills, agents e hook para desenvolvimento no **ERP Sankhya**.

## Conteúdo

### Skills (`skills/`)
| Skill | Quando aciona |
|---|---|
| `sankhya-addon` | Addon Studio: `@ActionButton`, `@Listener`, `@Job`, `DynamicVO`, `JapeFactory`, SDK Sankhya. |
| `sankhya-modulo-java` | Módulo Java: `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava`, helpers dstech. |
| `sankhya-relatorio` | Relatórios JasperReports / iReport / `.jrxml`, impressão Sankhya. |

### Agents (`agents/`)
Suíte de code review para projetos Java Sankhya. `code-review-orchestrator` coordena os demais:
`arch-reviewer`, `clean-code`, `security-scanner`, `perf-analyzer`, `doc-checker`.

### Hooks (`hooks/`)

| Hook | Evento | O que faz |
|---|---|---|
| `sankhya-encoding.js` | `PostToolUse` (Write/Edit/MultiEdit) | Converte `.java/.xml/.kt` para **ISO-8859-1** (encoding do Addon Studio) + transliteração ASCII de acentos. Gate híbrido por conteúdo: só age dentro de projeto Sankhya (ancestral com `datadictionary`/`dbscripts`) ou arquivo com marcadores Sankhya. Idempotente; nunca bloqueia o fluxo. |
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

## Pendente

- **MCP `sankhya-schema`**: ainda **não** incluído. Projeto Python separado (Oracle instantclient
  ~80 MB + credenciais), instalado à parte. Avaliar integração futura via `mcpServers` apontando
  para install externa.
