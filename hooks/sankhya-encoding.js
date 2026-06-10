#!/usr/bin/env node
// Hook PostToolUse: converte arquivos de projeto Addon Studio Sankhya para ISO-8859-1.
// Gate: so age se o arquivo estiver dentro de um projeto Sankhya (ancestral com
//       pasta "datadictionary" ou "dbscripts"). Fora disso, sai silencioso.
// Padrao definido na skill sankhya-addon (instructions/encoding-instructions.md).
// Nunca bloqueia o fluxo: qualquer erro -> exit 0.

const fs = require("fs");
const path = require("path");

// Extensoes que seguem o padrao ISO-8859-1 do Sankhya.
const EXTENSOES = new Set([".java", ".xml", ".kt"]);
// Pastas que marcam a raiz de um projeto Addon Studio.
const MARCADORES = ["datadictionary", "dbscripts"];

function lerStdin() {
  try {
    return fs.readFileSync(0, "utf8");
  } catch {
    return "";
  }
}

// Sobe a arvore a partir de "inicio" procurando um ancestral que contenha
// uma pasta marcadora. Retorna true se for projeto Sankhya.
function ehProjetoSankhya(inicio) {
  let dir = inicio;
  while (true) {
    for (const marcador of MARCADORES) {
      const alvo = path.join(dir, marcador);
      try {
        if (fs.existsSync(alvo) && fs.statSync(alvo).isDirectory()) {
          return true;
        }
      } catch {
        /* ignora */
      }
    }
    const pai = path.dirname(dir);
    if (pai === dir) return false; // chegou na raiz do filesystem
    dir = pai;
  }
}

// Decodifica buffer como UTF-8 estrito. Retorna null se nao for UTF-8 valido
// (provavelmente ja esta em ISO-8859-1 -> nao mexer).
function decodificarUtf8Estrito(buffer) {
  try {
    return new TextDecoder("utf-8", { fatal: true }).decode(buffer);
  } catch {
    return null;
  }
}

function main() {
  const entrada = lerStdin();
  if (!entrada) return;

  let dados;
  try {
    dados = JSON.parse(entrada);
  } catch {
    return;
  }

  const file =
    dados?.tool_input?.file_path ||
    dados?.tool_response?.filePath ||
    dados?.tool_response?.file_path;
  if (!file) return;

  const ext = path.extname(file).toLowerCase();
  if (!EXTENSOES.has(ext)) return;

  let arquivo;
  try {
    arquivo = fs.realpathSync(file);
  } catch {
    arquivo = file; // arquivo pode nao existir mais; segue com o path cru
  }

  if (!fs.existsSync(arquivo)) return;
  if (!ehProjetoSankhya(path.dirname(arquivo))) return; // gate Sankhya

  const buffer = fs.readFileSync(arquivo);
  let conteudo = decodificarUtf8Estrito(buffer);
  if (conteudo === null) return; // ja em ISO-8859-1 (ou binario): nao converte

  // XML: garante encoding ISO-8859-1 na declaracao.
  if (ext === ".xml") {
    if (/<\?xml[^>]*\bencoding\s*=\s*["'][^"']*["']/i.test(conteudo)) {
      conteudo = conteudo.replace(
        /(<\?xml[^>]*\bencoding\s*=\s*["'])[^"']*(["'])/i,
        "$1ISO-8859-1$2"
      );
    } else if (/^\s*<\?xml[^>]*\?>/.test(conteudo)) {
      conteudo = conteudo.replace(
        /(<\?xml[^>]*?)(\s*\?>)/,
        '$1 encoding="ISO-8859-1"$2'
      );
    }
  }

  // UTF-8 -> ISO-8859-1: cada code point < 256 vira 1 byte Latin-1.
  // Acentos pt-br (U+00C0..U+00FF) cabem; chars fora da faixa viram "?".
  const saida = Buffer.from(
    Array.from(conteudo, (c) => {
      const cp = c.codePointAt(0);
      return cp <= 0xff ? cp : 0x3f; // 0x3f = '?'
    })
  );

  // So grava se mudou de fato (idempotente).
  if (!buffer.equals(saida)) {
    fs.writeFileSync(arquivo, saida);
    process.stderr.write(
      `[sankhya-encoding] ${path.basename(arquivo)} convertido para ISO-8859-1.\n`
    );
  }
}

try {
  main();
} catch {
  /* nunca quebra o fluxo */
}
process.exit(0);
