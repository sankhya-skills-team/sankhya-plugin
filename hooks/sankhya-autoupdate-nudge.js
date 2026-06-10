#!/usr/bin/env node
// Hook SessionStart: lembra o dev de ligar o autoUpdate do marketplace sankhya.
// NAO escreve nada na config do usuario (read-only). So avisa.
// Para de avisar sozinho quando o dev liga o autoUpdate. Nudge no maximo 1x/24h.
//
// Saida VISIVEL ao usuario: JSON { hookSpecificOutput: { hookEventName: "SessionStart",
//   additionalContext: "..." } } no stdout (exit 0). Esse e o canal que o Claude Code
//   renderiza no inicio da sessao (mesmo formato usado por outros plugins). systemMessage
//   NAO e exibido em SessionStart.
// Descoberta do config dir (settings.json): nao depende de CLAUDE_CONFIG_DIR (nao garantida
//   em hook). Deriva do transcript_path do stdin + fallbacks ~/.claude-snk e ~/.claude.
// Nunca bloqueia: qualquer erro -> exit 0 sem saida.

const fs = require("fs");
const path = require("path");
const os = require("os");

const JANELA_MS = 24 * 60 * 60 * 1000; // 1 nudge por dia no maximo
const REPO_MARCADOR = "sankhya-plugin"; // identifica nossa marketplace no settings

function lerStdinJson() {
  try {
    return JSON.parse(fs.readFileSync(0, "utf8"));
  } catch {
    return {};
  }
}

// Sobe a partir de "inicio" ate achar um dir que contenha settings.json. Retorna o dir ou null.
function subirAteSettings(inicio) {
  let dir = inicio;
  while (dir) {
    try {
      if (fs.existsSync(path.join(dir, "settings.json"))) return dir;
    } catch {
      /* ignora */
    }
    const pai = path.dirname(dir);
    if (pai === dir) break;
    dir = pai;
  }
  return null;
}

// Lista de candidatos a diretorio de config, em ordem de prioridade.
function dirsConfig(stdin) {
  const cands = [];
  // 1. derivado do transcript_path (<configdir>/projects/<...>/<id>.jsonl)
  const tp = stdin && stdin.transcript_path;
  if (tp) {
    const d = subirAteSettings(path.dirname(tp));
    if (d) cands.push(d);
  }
  // 2. env (quando existir)
  if (process.env.CLAUDE_CONFIG_DIR) cands.push(process.env.CLAUDE_CONFIG_DIR);
  // 3. fallbacks conhecidos
  cands.push(path.join(os.homedir(), ".claude-snk"));
  cands.push(path.join(os.homedir(), ".claude"));
  return [...new Set(cands)];
}

// Procura a marketplace sankhya nos settings dos candidatos.
// Retorna: true (autoUpdate on), false (off), null (nao achou em lugar nenhum).
function autoUpdateLigado(stdin) {
  for (const dir of dirsConfig(stdin)) {
    try {
      const j = JSON.parse(fs.readFileSync(path.join(dir, "settings.json"), "utf8"));
      const mkts = j.extraKnownMarketplaces || {};
      for (const cfg of Object.values(mkts)) {
        const repo = (cfg && cfg.source && cfg.source.repo) || "";
        if (repo.toLowerCase().includes(REPO_MARCADOR)) {
          return cfg.autoUpdate === true;
        }
      }
    } catch {
      /* tenta o proximo candidato */
    }
  }
  return null;
}

// Marcador de "ja avisei recentemente" no diretorio persistente do plugin.
function caminhoMarcador() {
  const base = process.env.CLAUDE_PLUGIN_DATA || os.tmpdir();
  return path.join(base, ".sankhya-autoupdate-nudge");
}

function avisouRecente() {
  try {
    const ts = parseInt(fs.readFileSync(caminhoMarcador(), "utf8"), 10);
    return Number.isFinite(ts) && Date.now() - ts < JANELA_MS;
  } catch {
    return false;
  }
}

function marcarAviso() {
  try {
    const m = caminhoMarcador();
    fs.mkdirSync(path.dirname(m), { recursive: true });
    fs.writeFileSync(m, String(Date.now()));
  } catch {
    /* ignora */
  }
}

function main() {
  const stdin = lerStdinJson();

  const estado = autoUpdateLigado(stdin);
  if (estado === true) return; // ja ligado: silencio (auto-resolvido)
  if (estado === null) return; // marketplace nao encontrada: nao incomoda
  if (avisouRecente()) return; // ja avisou nas ultimas 24h

  marcarAviso();
  const msg = [
    "[plugin sankhya] auto-update DESLIGADO para este marketplace.",
    "Para o plugin atualizar sozinho (skills/agents/hook), ligue em:",
    "  /plugin  ->  Marketplaces  ->  sankhya  ->  Enable auto-update",
    "(este aviso some quando ligar; no maximo 1x/dia)",
  ].join("\n");

  // Formato identico ao claude-mem (comprovado renderizando no terminal):
  //   systemMessage      -> bloco VISIVEL ao usuario no terminal
  //   additionalContext  -> contexto pro modelo
  // Requer matcher no SessionStart do plugin.json (sem matcher nada e ecoado).
  const saida = JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "SessionStart",
      additionalContext: msg,
    },
    systemMessage: msg,
  });
  process.stdout.write(saida);
}

try {
  main();
} catch {
  /* nunca quebra o fluxo */
}
process.exit(0);
