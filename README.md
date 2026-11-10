# Plugin Sankhya

[![release](https://img.shields.io/github/v/release/sankhya-skills-team/sankhya-plugin?label=release&color=blue)](https://github.com/sankhya-skills-team/sankhya-plugin/releases/latest)

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
| `sankhya-kit` | Kit de produtos no core do Sankhya OM: composição (`TIPOKIT`, `TGFICP`), kit independente (`TSIKIT`), abertura dos componentes `USOPROD='D'`, reserva e baixa de estoque no pedido e na nota, `INIBESELECUSOPD`, `TIPOIMPKIT` e erros `CORE_E01199`/`CORE_E04505`/`CORE_E03881`. |
| `sankhya-dicionario` | Dicionário de dados Sankhya OM: ~730 tabelas mapeadas (campos, PKs, FKs, enums, entityNames), metamodelo TDD, relacionamentos. |
| `sankhya-js` | Framework frontend AngularJS 1.x (`sankhya-js`): telas HTML5, `ServiceProxy`/`FluidBuilder`, componentes (grid, dataset, wizard, popup), MetadataProvider, i18n. |
| `sankhya-estimativa-planejador` | Análise de requisitos funcionais → backlog (epics/stories/critérios), recomendação Addon × Módulo Java e estimativa de horas em 7 fases. |
| `sankhya-gera-escopo` | Geração de documento de escopo `.docx` (proposta técnica) a partir de contexto bruto, preservando template Word padrão. |
| `sankhya-commit` | Commit Git interativo: analisa o diff e gera mensagem Conventional Commits com emojis. |
| `sankhya-doc-entrega` | Gera documento de entrega de desenvolvimento em `.html` interativo ou `.docx` Word (à escolha), para Addon Studio e Módulo Java. Coleta as evidências de homologação pelo navegador e embute nos dois formatos. |
| `sankhya-gerar-btnacao-banco` | Botão de Ação por procedure (*Rotina no Banco de dados*): assinatura `P_CODUSU/P_IDSESSAO/P_QTDLINHAS/P_MENSAGEM`, `ACT_*_FIELD`/`ACT_*_PARAM`, confirmação `ACT_ESCOLHER_SIMNAO`, teste sem a tela via `EXECPARAMS`. Invocação: `/sankhya:gerar-btnacao-banco`. |
| `sankhya-gerar-trigger` | Trigger Oracle no padrão das nativas do Sankhya: `TRG_<INC|UPD|DLT>_<TABELA>_<SUFIXO>`, guarda `STP_GET_ATUALIZANDO`, `FPODEVALIDAR`, erro `-20101`, `:NEW/:OLD`, sem COMMIT nem SELECT na própria tabela. Invocação: `/sankhya:gerar-trigger`. |
| `sankhya-apontamento-os` | Apontamento de OS de consultoria de implantação: transforma o relato livre do consultor em registro fiel e rastreável, até 4.000 caracteres, sem Markdown, com validação de horários e contagem real. Invocação: `/sankhya:apontamento-os`. |

### Agents (`agents/`)

**Suíte de code review** para projetos Java Sankhya. `code-review-orchestrator` coordena os demais:
`arch-reviewer`, `clean-code`, `security-scanner`, `perf-analyzer`, `doc-checker`.

**Agents de desenvolvimento** — geram/alteram código Sankhya por especialidade:

| Agent | Quando aciona |
|---|---|
| `sankhya-orchestrator-agent-dev` | Planeja e roteia o desenvolvimento a partir de escopo/backlog: decide Addon × Módulo Java, fatia por artefato e aciona os especialistas abaixo. |
| `sankhya-backend-dev` | Backend Java: `AcaoRotinaJava`, botão de ação, `EventoProgramavelJava`, `RegraNegocioJava`, ações agendadas, Helper/Service/Repository, `@ActionButton`/`@Listener`/`@Job`. Módulo Java e Addon Studio. |
| `sankhya-data-dev` | Estrutura de dados e persistência: tabelas `AD_`, DataDictionary, DBScripts dual-dialect (Oracle/SQL Server), migrations, repositórios JAPE, views/triggers/functions. |
| `sankhya-bi-report-dev` | BI e relatórios: dashboards/gadgets (Construtor de Componentes de BI) e JasperReports/iReport. |
| `sankhya-frontend-angular` | **Padrão** para telas. Telas HTML5 AngularJS `sankhya-js` **sem** Node/Design System: `sk-application`, `sk-datagrid`, `sk-wizard`, `ServiceProxy`. |
| `sankhya-frontend-design-system` | Telas no Design System EzUI/Acorde (`ez-`/`snk-` web components) com pipeline Node (npm/Vite). |

### Hooks (`hooks/`)

| Hook | Evento | O que faz |
|---|---|---|
| `register.ts` (mod) + `sankhya-encoding.js` | `tool.call` de Read, Edit e Write | Encoding ISO-8859-1 dos fontes Sankhya. Em volta de cada Read, Edit e Write, o mod converte o arquivo para UTF-8 logo antes da ferramenta e de volta para **ISO-8859-1** logo depois (com transliteração ASCII de pontuação tipográfica): o arquivo só fica em UTF-8 durante a chamada, inclusive em subagent. Se o conteúdo tiver `U+FFFD`, **não converte** e devolve ao modelo a instrução de recuperação. Gate: `.xml` só nas pastas de artefato (`datadictionary/dbscripts/dbquerys/dashboards`); `.java` com pasta `datadictionary`/`dbscripts` ancestral, caminho `Java/src` (Módulo Java) ou conteúdo Sankhya. `.kt` e o charset `utf-8` do `.editorconfig` ficam de fora. |
| `guard.ts` + `guard-rules.ts` (mod, `sankhya-guard`) | `tool.call` de Write e Edit | Em projeto Sankhya (`datadictionary`/`dbscripts` na raiz, `build.gradle` com `br.com.sankhya` ou `CLAUDE.md` citando as skills), **recusa** a gravação de `.java`/`.xml`/`.properties` com: SQL só-Oracle (`NVL`, `NVL2`, `DECODE`, `SYSDATE`, `ROWNUM`) em string Java de addon; credencial em texto puro; `NativeSql`/query montada concatenando variável. Ignora `FonteLegado/`, `build/`, `ejbsrc/`, `target/`. Para liberar um trecho acusado por engano: `sankhya-guard: ignore` no conteúdo. |
| `sankhya-autoupdate-nudge.js` | `SessionStart` (startup/clear/compact) | Lembra 1×/dia para ligar o auto-update do marketplace, se estiver desligado. Só leitura — nunca edita config. |

Os scripts `.js` são **Node.js puro** (multi-OS) e exigem só `node` no `PATH`; o `register.ts` roda no motor de mods do Claude Code.

## Instalação

```
/plugin marketplace add sankhya-skills-team/sankhya-plugin
/plugin install sankhya@sankhya
```

### Pré-requisito (todos os SO)

Os scripts dos hooks são **Node.js puro** — funcionam igual em **Windows, Linux e macOS**.
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

## Versionamento

SemVer, uma tag git por release (`v1.16.0`, ...). O push de um bump de `version` em `plugin.json` gera a tag e a [release](https://github.com/sankhya-skills-team/sankhya-plugin/releases) automaticamente, com changelog dos commits. **Changelog completo nas [releases](https://github.com/sankhya-skills-team/sankhya-plugin/releases).**

## Autores

Skills, agents e hooks deste plugin são desenvolvidos e mantidos por:

- **Felipe Rosa da Silva**
- **Daniel Ratkevicius**
- **Claiton Trisch Farias**
