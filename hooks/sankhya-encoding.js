#!/usr/bin/env node
// Hook PostToolUse: converte arquivos relacionados ao Sankhya para ISO-8859-1.
// Gate por tipo de arquivo:
//   .xml:      SO converte se estiver dentro de pasta de artefato Sankhya
//              (datadictionary/dbscripts/dbquerys/dashboards).
//   .java/.kt: gate hibrido (basta UM) -> pasta ancestral "datadictionary"/"dbscripts"
//              (projeto Addon Studio) OU conteudo com marcadores de codigo Sankhya.
// Padrao definido na skill sankhya-addon (instructions/encoding-instructions.md).
// Nunca bloqueia o fluxo: qualquer erro -> exit 0.

const fs = require("fs");
const path = require("path");

// Extensoes que seguem o padrao ISO-8859-1 do Sankhya.
const EXTENSOES = new Set([".java", ".xml", ".kt"]);
// Pastas que marcam a raiz de um projeto Addon Studio.
const MARCADORES = ["datadictionary", "dbscripts"];
// Pastas onde XML e SEMPRE artefato Sankhya em Latin-1. Se algum ancestral
// bater, o XML e convertido. Cobre os artefatos reais sem pegar pom.xml (raiz)
// nem .idea/*.xml (config de IDE).
const PASTAS_XML_SANKHYA = new Set([
  "datadictionary",
  "dbscripts",
  "dbquerys",
  "dashboards",
]);

// Marcadores de CONTEUDO Sankhya (gate 2), por tipo de arquivo.
// .java/.kt: import/package sankhya, anotacoes do Addon Studio, APIs core.
const RE_CODIGO_SANKHYA =
  /(?:\b(?:import|package)\s+[\w.]*sankhya)|@(?:ActionButton|Listener|Job|BusinessRule|DynamicForm|ServiceDefinition|Crud)\b|\b(?:JapeFactory|JapeSession|JapeWrapper|JapeWrapperFactory|DynamicVO|EntityFacade|MGEModelException|JdbcWrapper|NativeSql|DwfUtils|FluidCreateVO|AcaoRotinaJava|EventoProgramavelJava|RegraNegocioJava)\b/i;

// Transliteracao de chars FORA do Latin-1 (> U+00FF) para equivalente ASCII.
// Pontuacao tipografica de copy-paste (Word/web). Evita virar "?" e perder sentido.
const TRANSLITERACAO = {
  0x2010: "-", 0x2011: "-", 0x2012: "-", 0x2013: "-", 0x2014: "--", 0x2015: "--", // tracos
  0x2018: "'", 0x2019: "'", 0x201a: "'", 0x201b: "'", // aspas simples curvas
  0x201c: '"', 0x201d: '"', 0x201e: '"', 0x201f: '"', // aspas duplas curvas
  0x2032: "'", 0x2033: '"', // prime
  0x2026: "...", // reticencias
  0x2022: "*", 0x00b7: "*", // bullet
  0x2190: "<-", 0x2192: "->", 0x2194: "<->", // setas
  0x21d0: "<=", 0x21d2: "=>", // setas duplas
  0x2212: "-", // sinal de menos
  0x20ac: "EUR", 0x2122: "(TM)", 0x2120: "(SM)", // simbolos
  0x2009: " ", 0x200a: " ", 0x2007: " ", 0x2008: " ", 0x202f: " ", // espacos finos
};

function lerStdin() {
  try {
    return fs.readFileSync(0, "utf8");
  } catch {
    return "";
  }
}

// Sobe a arvore a partir de "inicio" procurando um ancestral que contenha
// uma pasta marcadora. Retorna true se for projeto Sankhya (gate 1).
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

// XML so converte se estiver DENTRO de uma das pastas de artefato Sankhya
// (PASTAS_XML_SANKHYA). Sobe a arvore a partir de "inicio" e confere o nome
// de cada ancestral.
function xmlSankhyaPorPasta(inicio) {
  let dir = inicio;
  while (true) {
    if (PASTAS_XML_SANKHYA.has(path.basename(dir).toLowerCase())) return true;
    const pai = path.dirname(dir);
    if (pai === dir) return false; // chegou na raiz do filesystem
    dir = pai;
  }
}

// Gate 2: o conteudo do arquivo tem marcadores Sankhya? Olha so os primeiros
// 64KB (suficiente p/ imports/anotacoes; barato em arquivo grande).
function temConteudoSankhya(conteudo, ext) {
  const amostra = conteudo.length > 65536 ? conteudo.slice(0, 65536) : conteudo;
  return RE_CODIGO_SANKHYA.test(amostra); // .java / .kt (XML usa gate de pasta)
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

// UTF-8 -> ISO-8859-1, sem escape unicode:
//   cp <= 0xFF        -> 1 byte Latin-1 direto (acentos pt-br sao lossless aqui).
//   cp na tabela      -> transliteracao ASCII (ex: "—" -> "--").
//   resto (> 0xFF)    -> "?" e registra o char perdido para avisar.
function paraLatin1(conteudo) {
  const bytes = [];
  const perdidos = new Set();
  let transliterados = 0;
  for (const ch of conteudo) {
    const cp = ch.codePointAt(0);
    if (cp <= 0xff) {
      bytes.push(cp);
    } else if (TRANSLITERACAO[cp] !== undefined) {
      for (let i = 0; i < TRANSLITERACAO[cp].length; i++) {
        bytes.push(TRANSLITERACAO[cp].charCodeAt(i));
      }
      transliterados++;
    } else {
      bytes.push(0x3f); // '?'
      perdidos.add("U+" + cp.toString(16).toUpperCase().padStart(4, "0"));
    }
  }
  return { buffer: Buffer.from(bytes), perdidos, transliterados };
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

  const buffer = fs.readFileSync(arquivo);
  let conteudo = decodificarUtf8Estrito(buffer);
  if (conteudo === null) return; // ja em ISO-8859-1 (ou binario): nao converte

  // XML: gate por pasta. So converte se algum ancestral for pasta de artefato
  // Sankhya (PASTAS_XML_SANKHYA). Fora delas, XML fica UTF-8 (pom.xml, .idea/*).
  if (ext === ".xml") {
    if (!xmlSankhyaPorPasta(path.dirname(arquivo))) return;
  } else {
    // .java/.kt: gate hibrido (pasta Sankhya OU conteudo Sankhya).
    if (
      !ehProjetoSankhya(path.dirname(arquivo)) &&
      !temConteudoSankhya(conteudo, ext)
    ) {
      return;
    }
  }

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

  const { buffer: saida, perdidos, transliterados } = paraLatin1(conteudo);

  // So grava se mudou de fato (idempotente).
  if (!buffer.equals(saida)) {
    fs.writeFileSync(arquivo, saida);
    const nome = path.basename(arquivo);
    let msg = `[sankhya-encoding] ${nome} convertido para ISO-8859-1`;
    if (transliterados > 0) msg += ` (${transliterados} char(s) transliterado(s))`;
    process.stderr.write(msg + ".\n");
    if (perdidos.size > 0) {
      process.stderr.write(
        `[sankhya-encoding] AVISO: ${nome} tem char(s) sem equivalente Latin-1, ` +
          `substituido(s) por "?": ${[...perdidos].join(", ")}.\n`
      );
    }
  }
}

try {
  main();
} catch {
  /* nunca quebra o fluxo */
}
process.exit(0);
