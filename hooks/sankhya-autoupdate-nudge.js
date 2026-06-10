#!/usr/bin/env node
// Hook SessionStart: lembra o dev de ligar o autoUpdate do marketplace sankhya.
// NAO escreve nada na config do usuario (read-only). So avisa.
// Para de avisar sozinho quando o dev liga o autoUpdate. Nudge no maximo 1x/24h.
// Nunca bloqueia: qualquer erro -> exit 0.

const fs = require("fs");
const path = require("path");
const os = require("os");

const REPO = "sankhya-skills-team/sankhya-plugin"; // marcador da nossa marketplace
const JANELA_MS = 24 * 60 * 60 * 1000; // 1 nudge por dia no maximo

function consumirStdin() {
  try {
    fs.readFileSync(0, "utf8");
  } catch {
    /* ignora */
  }
}

// Diretorio de config do Claude Code: respeita CLAUDE_CONFIG_DIR, senao ~/.claude.
function dirConfig() {
  return process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude");
}

// Le settings.json e procura a marketplace cujo source.repo casa com REPO.
// Retorna: true (autoUpdate ligado), false (desligado), null (nao achou/erro).
function autoUpdateLigado() {
  try {
    const p = path.join(dirConfig(), "settings.json");
    const j = JSON.parse(fs.readFileSync(p, "utf8"));
    const mkts = j.extraKnownMarketplaces || {};
    for (const cfg of Object.values(mkts)) {
      const repo = cfg?.source?.repo || "";
      if (repo.toLowerCase().includes("sankhya-plugin")) {
        return cfg.autoUpdate === true;
      }
    }
    return null; // marketplace nao encontrada nesse settings
  } catch {
    return null;
  }
}

// Marcador de "ja avisei recentemente" em diretorio persistente do plugin.
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
  consumirStdin();

  const estado = autoUpdateLigado();
  if (estado === true) return; // ja ligado: silencio (auto-resolvido)
  if (estado === null) return; // nao deu pra determinar: nao incomoda
  if (avisouRecente()) return; // ja avisou nas ultimas 24h

  marcarAviso();
  process.stdout.write(
    [
      "",
      "[plugin sankhya] auto-update DESLIGADO para este marketplace.",
      "Para o plugin atualizar sozinho (skills/agents/hook), ligue:",
      "  /plugin  ->  Marketplaces  ->  sankhya  ->  Enable auto-update",
      "Ou no settings.json:",
      '  "extraKnownMarketplaces": { "sankhya": { "source": { "source": "github", "repo": "' +
        REPO +
        '" }, "autoUpdate": true } }',
      "(este aviso some quando ligar; no maximo 1x/dia)",
      "",
    ].join("\n")
  );
}

try {
  main();
} catch {
  /* nunca quebra o fluxo */
}
process.exit(0);
