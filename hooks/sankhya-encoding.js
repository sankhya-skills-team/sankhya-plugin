#!/usr/bin/env node
// Hook de encoding Sankhya (ISO-8859-1) — BIDIRECIONAL.
//
// Por que bidirecional: Claude Code le e grava arquivos SEMPRE em UTF-8.
// Um arquivo em ISO-8859-1 lido pelo tool Read vira U+FFFD (�) nos acentos;
// se o modelo edita e grava, o U+FFFD acabava convertido para "?" — corrompendo
// todos os acentos a cada ciclo Read->Edit. A conversao pos-escrita sozinha
// causava o problema que tentava resolver.
//
// Modos (argv[2]):
//   --pre    PreToolUse(Read): arquivo Sankhya em Latin-1 -> regrava em UTF-8
//            (conversao lossless) ANTES da leitura, para o Read ver os acentos
//            corretos. Registra o arquivo como pendencia de reconversao.
//   (vazio)  PostToolUse(Write|Edit|MultiEdit): UTF-8 -> ISO-8859-1 (como
//            sempre). Guarda anti-corrupcao: conteudo com U+FFFD NAO e
//            convertido; exit 2 devolve instrucao de recuperacao ao modelo.
//   --flush  Stop/SessionEnd: reconverte para ISO-8859-1 as pendencias que
//            foram lidas mas nao editadas (sem isso ficariam UTF-8 no disco).
//
// Gate por tipo de arquivo (igual nos tres modos):
//   .xml:      so dentro de pasta de artefato Sankhya
//              (datadictionary/dbscripts/dbquerys/dashboards).
//   .java/.kt: gate hibrido (basta UM) -> pasta marcadora ancestral
//              (datadictionary/dbscripts) OU conteudo com marcadores Sankhya.
// Padrao definido na skill sankhya-addon (instructions/encoding-instructions.md).
// Nunca bloqueia o fluxo: qualquer erro inesperado -> exit 0.

const fs = require("fs");
const os = require("os");
const path = require("path");

// Extensoes que seguem o padrao ISO-8859-1 do Sankhya.
const EXTENSOES = new Set([".java", ".xml", ".kt"]);
// Pastas que marcam a raiz de um projeto Addon Studio.
const MARCADORES = ["datadictionary", "dbscripts"];
// Pastas onde XML e SEMPRE artefato Sankhya em Latin-1. Cobre os artefatos
// reais sem pegar pom.xml (raiz) nem .idea/*.xml (config de IDE).
const PASTAS_XML_SANKHYA = new Set([
  "datadictionary",
  "dbscripts",
  "dbquerys",
  "dashboards",
]);

// Marcadores de CONTEUDO Sankhya (.java/.kt): import/package sankhya,
// anotacoes do Addon Studio, APIs core.
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

// XML so e Sankhya se estiver DENTRO de uma das pastas de artefato
// (PASTAS_XML_SANKHYA). Sobe a arvore conferindo o nome de cada ancestral.
function xmlSankhyaPorPasta(inicio) {
  let dir = inicio;
  while (true) {
    if (PASTAS_XML_SANKHYA.has(path.basename(dir).toLowerCase())) return true;
    const pai = path.dirname(dir);
    if (pai === dir) return false; // chegou na raiz do filesystem
    dir = pai;
  }
}

// O conteudo tem marcadores Sankhya? Olha so os primeiros 64KB
// (suficiente p/ imports/anotacoes; barato em arquivo grande).
function temConteudoSankhya(conteudo) {
  const amostra = conteudo.length > 65536 ? conteudo.slice(0, 65536) : conteudo;
  return RE_CODIGO_SANKHYA.test(amostra);
}

// Gate unico usado pelos tres modos. "conteudo" e o texto ja decodificado
// (UTF-8 ou Latin-1, conforme o modo) — usado so no gate de conteudo.
function arquivoSankhya(arquivo, conteudo) {
  const ext = path.extname(arquivo).toLowerCase();
  if (!EXTENSOES.has(ext)) return false;
  if (ext === ".xml") return xmlSankhyaPorPasta(path.dirname(arquivo));
  return (
    ehProjetoSankhya(path.dirname(arquivo)) || temConteudoSankhya(conteudo)
  );
}

// Decodifica buffer como UTF-8 estrito. Retorna null se nao for UTF-8 valido
// (provavelmente ja esta em ISO-8859-1).
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

// Garante encoding ISO-8859-1 na declaracao <?xml ...?>.
function garantirDeclaracaoXml(conteudo) {
  if (/<\?xml[^>]*\bencoding\s*=\s*["'][^"']*["']/i.test(conteudo)) {
    return conteudo.replace(
      /(<\?xml[^>]*\bencoding\s*=\s*["'])[^"']*(["'])/i,
      "$1ISO-8859-1$2"
    );
  }
  if (/^\s*<\?xml[^>]*\?>/.test(conteudo)) {
    return conteudo.replace(
      /(<\?xml[^>]*?)(\s*\?>)/,
      '$1 encoding="ISO-8859-1"$2'
    );
  }
  return conteudo;
}

// ---------------------------------------------------------------------------
// State file: pendencias de reconversao (arquivos expostos como UTF-8 pelo
// modo --pre e ainda nao reconvertidos pelo PostToolUse). Um por sessao.
// ---------------------------------------------------------------------------

function statePath(sessionId) {
  const id = String(sessionId || "global").replace(/[^a-zA-Z0-9_-]/g, "_");
  return path.join(os.tmpdir(), `sankhya-encoding-${id}.json`);
}

function lerPendencias(arquivoState) {
  try {
    const lista = JSON.parse(fs.readFileSync(arquivoState, "utf8"));
    return Array.isArray(lista) ? lista : [];
  } catch {
    return [];
  }
}

function salvarPendencias(arquivoState, lista) {
  try {
    if (lista.length === 0) {
      fs.rmSync(arquivoState, { force: true });
    } else {
      fs.writeFileSync(arquivoState, JSON.stringify(lista));
    }
  } catch {
    /* state e otimizacao; nunca quebra o fluxo */
  }
}

function registrarPendencia(sessionId, arquivo) {
  const p = statePath(sessionId);
  const lista = lerPendencias(p);
  if (!lista.includes(arquivo)) lista.push(arquivo);
  salvarPendencias(p, lista);
}

function removerPendencia(sessionId, arquivo) {
  const p = statePath(sessionId);
  const lista = lerPendencias(p);
  const filtrada = lista.filter((item) => item !== arquivo);
  if (filtrada.length !== lista.length) salvarPendencias(p, filtrada);
}

// ---------------------------------------------------------------------------
// Conversao UTF-8 -> ISO-8859-1 (clean), compartilhada por post e flush.
// ---------------------------------------------------------------------------

// Retorna { status, perdidos?, transliterados? }:
//   "convertido"  gravou em ISO-8859-1.
//   "sem-mudanca" ja estava ok (ASCII puro ou identico).
//   "ja-latin1"   nao e UTF-8 valido (ja convertido ou binario): nao mexe.
//   "fora-do-gate" nao e arquivo Sankhya.
//   "corrompido"  conteudo tem U+FFFD: NAO converte (viraria "?").
function limparParaLatin1(arquivo) {
  const buffer = fs.readFileSync(arquivo);
  let conteudo = decodificarUtf8Estrito(buffer);
  if (conteudo === null) return { status: "ja-latin1" };
  if (!arquivoSankhya(arquivo, conteudo)) return { status: "fora-do-gate" };
  if (conteudo.includes("�")) return { status: "corrompido" };
  if (path.extname(arquivo).toLowerCase() === ".xml") {
    conteudo = garantirDeclaracaoXml(conteudo);
  }
  const { buffer: saida, perdidos, transliterados } = paraLatin1(conteudo);
  if (buffer.equals(saida)) return { status: "sem-mudanca" };
  fs.writeFileSync(arquivo, saida);
  return { status: "convertido", perdidos, transliterados };
}

function avisarConversao(arquivo, resultado) {
  const nome = path.basename(arquivo);
  let msg = `[sankhya-encoding] ${nome} convertido para ISO-8859-1`;
  if (resultado.transliterados > 0) {
    msg += ` (${resultado.transliterados} char(s) transliterado(s))`;
  }
  process.stderr.write(msg + ".\n");
  if (resultado.perdidos && resultado.perdidos.size > 0) {
    process.stderr.write(
      `[sankhya-encoding] AVISO: ${nome} tem char(s) sem equivalente Latin-1, ` +
        `substituido(s) por "?": ${[...resultado.perdidos].join(", ")}.\n`
    );
  }
}

// ---------------------------------------------------------------------------
// Resolucao do arquivo alvo a partir do payload do hook.
// ---------------------------------------------------------------------------

function resolverArquivo(dados) {
  const file =
    dados?.tool_input?.file_path ||
    dados?.tool_response?.filePath ||
    dados?.tool_response?.file_path;
  if (!file) return null;
  if (!EXTENSOES.has(path.extname(file).toLowerCase())) return null;
  let arquivo;
  try {
    arquivo = fs.realpathSync(file);
  } catch {
    arquivo = file; // arquivo pode nao existir; segue com o path cru
  }
  return fs.existsSync(arquivo) ? arquivo : null;
}

// ---------------------------------------------------------------------------
// Modos
// ---------------------------------------------------------------------------

// PreToolUse(Read): expoe arquivo Latin-1 como UTF-8 para a leitura nao
// corromper acentos. Lossless: todo byte Latin-1 tem codepoint UTF-8.
function modoPre(dados) {
  const arquivo = resolverArquivo(dados);
  if (!arquivo) return;

  const buffer = fs.readFileSync(arquivo);
  if (buffer.includes(0)) return; // binario: nao mexe

  const comoUtf8 = decodificarUtf8Estrito(buffer);
  if (comoUtf8 !== null) {
    // Ja esta em UTF-8. Se tem acentos e e arquivo Sankhya, registra para o
    // --flush reconverter no fim do turno (cobre arquivo lido e nao editado
    // e tambem arquivos que ficaram UTF-8 orfaos de sessoes anteriores).
    if (/[^\x00-\x7F]/.test(comoUtf8) && arquivoSankhya(arquivo, comoUtf8)) {
      registrarPendencia(dados?.session_id, arquivo);
    }
    return;
  }

  const conteudo = buffer.toString("latin1");
  if (!arquivoSankhya(arquivo, conteudo)) return;

  fs.writeFileSync(arquivo, Buffer.from(conteudo, "utf8"));
  registrarPendencia(dados?.session_id, arquivo);
  process.stderr.write(
    `[sankhya-encoding] ${path.basename(arquivo)} exposto como UTF-8 para ` +
      `leitura; volta para ISO-8859-1 ao final do turno.\n`
  );
}

// PostToolUse(Write|Edit|MultiEdit): converte para ISO-8859-1 com guarda
// anti-corrupcao. Exit 2 devolve o aviso ao modelo como feedback acionavel.
function modoPost(dados) {
  const arquivo = resolverArquivo(dados);
  if (!arquivo) return;

  const resultado = limparParaLatin1(arquivo);
  if (resultado.status !== "corrompido") {
    removerPendencia(dados?.session_id, arquivo);
  }

  if (resultado.status === "convertido") {
    avisarConversao(arquivo, resultado);
    return;
  }
  if (resultado.status === "corrompido") {
    const nome = path.basename(arquivo);
    process.stderr.write(
      `[sankhya-encoding] ERRO: ${nome} contem U+FFFD (caractere de ` +
        `substituicao) — sintoma de arquivo ISO-8859-1 lido como UTF-8. ` +
        `Conversao ABORTADA para nao trocar acentos por "?". Recupere o ` +
        `trecho original (git diff / git restore) e regrave o arquivo com ` +
        `os acentos corretos no lugar de cada �.\n`
    );
    process.exit(2);
  }
}

// Stop/SessionEnd: reconverte pendencias (arquivos expostos como UTF-8 pelo
// --pre que nenhum Write/Edit reconverteu).
function modoFlush(dados) {
  const arquivoState = statePath(dados?.session_id);
  for (const arquivo of lerPendencias(arquivoState)) {
    try {
      if (!fs.existsSync(arquivo)) continue;
      const resultado = limparParaLatin1(arquivo);
      if (resultado.status === "convertido") avisarConversao(arquivo, resultado);
      if (resultado.status === "corrompido") {
        process.stderr.write(
          `[sankhya-encoding] AVISO: ${path.basename(arquivo)} contem U+FFFD; ` +
            `mantido em UTF-8 para nao corromper. Revise manualmente.\n`
        );
      }
    } catch {
      /* segue para o proximo */
    }
  }
  try {
    fs.rmSync(arquivoState, { force: true });
  } catch {
    /* ignora */
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

  const modo = process.argv[2];
  if (modo === "--pre") return modoPre(dados);
  if (modo === "--flush") return modoFlush(dados);
  return modoPost(dados);
}

try {
  main();
} catch {
  /* nunca quebra o fluxo */
}
process.exit(0);
