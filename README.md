# Plugin Sankhya

Plugin do Claude Code com skills, agents e hook para desenvolvimento no **ERP Sankhya**.

## Conteúdo

### Skills (`skills/`)
| Skill | Quando aciona |
|---|---|
| `sankhya-addon` | Addon Studio: `@ActionButton`, `@Listener`, `@Job`, `DynamicVO`, `JapeFactory`, SDK Sankhya. |
| `sankhya-modulo-java` | Módulo Java: `EventoProgramavelJava`, `AcaoRotinaJava`, `RegraNegocioJava`, helpers dstech. |
| `sankhya-relatorio` | Relatórios JasperReports / iReport / `.jrxml`, impressão Sankhya. |
| `sankhya-dicionario` | Dicionário de dados: tabelas/campos/relacionamentos (`TGF*`, `TSI*`, `AD_*`), `entityName` para JAPE. |
| `sankhya-bi` | Construtor de Componentes de BI: dashboards, gadgets, gráficos, HTML5 component. |
| `sankhya-estimativa-planejador` | Escopo/requisitos → backlog, épicos/stories, estimativa de horas, addon × módulo. |
| `sankhya-doc-entrega` | Gera documento de entrega de desenvolvimento em `.docx`. |
| `sankhya-js` | Frontend AngularJS sankhya-js (`sk-*`, `ServiceProxy`, telas html5 `vc`). |
| `sankhya-gera-escopo` | Gera documento de escopo em `.docx` a partir do contexto da demanda. |
| `sankhya-jape` | Persistência JAPE: `JapeSession`, `NativeSql`, `EntityFacade`, `DynamicVO`, transações, macros. |
| `sankhya-padroes-seguranca` | Padrões de vulnerabilidade específicos do Sankhya (bypass de contexto, SQLi, PCI/PDV, SEFAZ). |
| `sankhya-commit` | Commit Git interativo: analisa o diff e gera mensagem Conventional Commits com emojis. |
| `sankhya-doc-entrega-html` | Gera documento de entrega de desenvolvimento em `.html` para projetos Java Sankhya. |

### Agents (`agents/`)

**Code review** — `code-review-orchestrator` coordena: `arch-reviewer`, `clean-code`, `security-scanner`, `perf-analyzer`, `doc-checker`.

**Desenvolvimento Sankhya** — `sankhya-orchestrator-agent-dev` planeja e roteia do escopo ao código; `sankhya-backend-dev`, `sankhya-data-dev`, `sankhya-bi-report-dev` especializados; `sankhya-frontend-dev` roteia entre `sankhya-frontend-angular` (sankhya-js legado) e `sankhya-frontend-design-system` (EzUI/Node).

### Hooks (`hooks/`)

| Hook | Evento | O que faz |
|---|---|---|
| `sankhya-encoding.js` | `PreToolUse` (Read) · `PostToolUse` (Write/Edit/MultiEdit) · `Stop`/`SessionEnd` | Encoding **bidirecional** ISO-8859-1 ⇄ UTF-8 para `.java/.xml/.kt`. **Antes do Read** (`--pre`): arquivo Latin-1 é exposto como UTF-8 (lossless) para a leitura não corromper acentos. **Após Write/Edit**: converte de volta para **ISO-8859-1** + transliteração ASCII; se detectar `U+FFFD` (leitura corrompida), **aborta** e instrui recuperação em vez de gravar `?`. **No Stop/SessionEnd** (`--flush`): arquivos lidos mas não editados voltam a ISO-8859-1. Gate híbrido: pasta de artefato Sankhya (`datadictionary`/`dbscripts`/`dbquerys`/`dashboards`) ou marcadores Sankhya no conteúdo. Idempotente; nunca bloqueia o fluxo. |
| `sankhya-autoupdate-nudge.js` | `SessionStart` (startup/clear/compact) | Lembra 1×/dia para ligar o auto-update do marketplace, se estiver desligado. Só leitura — nunca edita config. |

Ambos são **Node.js puro** (multi-OS) e exigem só `node` no `PATH`.

## Autores

- Felipe Rosa
- Daniel Ratkevicius
- Claiton Farias

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
