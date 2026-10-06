// Testes do hook sankhya-encoding.js. Executar: node --test hooks/
const test = require("node:test");
const assert = require("node:assert");
const fs = require("fs");
const os = require("os");
const path = require("path");
const { spawnSync } = require("child_process");

const HOOK = path.join(__dirname, "sankhya-encoding.js");
const CODIGO_SANKHYA_UTF8 = Buffer.from("package br.com.sankhya.x;\n// ação\n", "utf8");
const CODIGO_SANKHYA_LATIN1 = Buffer.from("package br.com.sankhya.x;\n// ação\n", "latin1");
const MODO_POS = [];
const MODO_PRE = ["--pre"];
const MODO_FLUSH = ["--flush"];

let contadorSessao = 0;

function criarProjeto(editorconfig) {
  const raiz = fs.mkdtempSync(path.join(os.tmpdir(), "hook-enc-"));
  if (editorconfig !== undefined) fs.writeFileSync(path.join(raiz, ".editorconfig"), editorconfig);
  return raiz;
}

function gravar(raiz, relativo, conteudo) {
  const destino = path.join(raiz, relativo);
  fs.mkdirSync(path.dirname(destino), { recursive: true });
  fs.writeFileSync(destino, conteudo);
  return destino;
}

function executarHook(modo, arquivo, sessao) {
  const entrada = JSON.stringify({ tool_input: { file_path: arquivo }, session_id: sessao });
  return spawnSync("node", [HOOK, ...modo], { input: entrada });
}

function novaSessao() {
  contadorSessao += 1;
  return `teste-${process.pid}-${contadorSessao}`;
}

const EDITORCONFIG_TESTE_UTF8 = "root = true\n[**/Java/src/**]\ncharset = latin1\n[**/Java/test/**]\ncharset = utf-8\n";

test("sem .editorconfig, .java com marcador Sankhya em UTF-8 vira Latin-1", () => {
  const raiz = criarProjeto();
  const arquivo = gravar(raiz, "Java/src/A.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_LATIN1);
});

test("charset utf-8 declarado para a pasta de teste: Write/Edit não converte", () => {
  const raiz = criarProjeto(EDITORCONFIG_TESTE_UTF8);
  const arquivo = gravar(raiz, "Java/test/ATest.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
});

test("charset latin1 declarado para Java/src: continua convertendo", () => {
  const raiz = criarProjeto(EDITORCONFIG_TESTE_UTF8);
  const arquivo = gravar(raiz, "Java/src/A.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_LATIN1);
});

test("Read + flush num arquivo utf-8 declarado não regrava em Latin-1", () => {
  const raiz = criarProjeto(EDITORCONFIG_TESTE_UTF8);
  const arquivo = gravar(raiz, "Java/test/ATest.java", CODIGO_SANKHYA_UTF8);
  const sessao = novaSessao();
  executarHook(MODO_PRE, arquivo, sessao);
  executarHook(MODO_FLUSH, arquivo, sessao);
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
});

test("Read num arquivo Latin-1 de Java/src continua expondo como UTF-8 e flush volta", () => {
  const raiz = criarProjeto(EDITORCONFIG_TESTE_UTF8);
  const arquivo = gravar(raiz, "Java/src/A.java", CODIGO_SANKHYA_LATIN1);
  const sessao = novaSessao();
  executarHook(MODO_PRE, arquivo, sessao);
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
  executarHook(MODO_FLUSH, arquivo, sessao);
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_LATIN1);
});

test("a última seção que casa vence: utf-8 depois de latin1 preserva UTF-8", () => {
  const raiz = criarProjeto("[*.java]\ncharset = latin1\n[**/Java/test/**]\ncharset = utf-8\n");
  const arquivo = gravar(raiz, "Java/test/ATest.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
});

test("a última seção que casa vence: latin1 depois de utf-8 converte", () => {
  const raiz = criarProjeto("[**/Java/test/**]\ncharset = utf-8\n[*.java]\ncharset = latin1\n");
  const arquivo = gravar(raiz, "Java/test/ATest.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_LATIN1);
});

test("o .editorconfig da raiz vale para arquivo em subpasta profunda", () => {
  const raiz = criarProjeto(EDITORCONFIG_TESTE_UTF8);
  const arquivo = gravar(raiz, "demanda/Java/test/br/com/x/ATest.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
});

test("o .editorconfig mais próximo prevalece sobre o da raiz", () => {
  const raiz = criarProjeto("[*.java]\ncharset = latin1\n");
  gravar(raiz, "Java/test/.editorconfig", "[*.java]\ncharset = utf-8\n");
  const arquivo = gravar(raiz, "Java/test/ATest.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
});

test("root = true interrompe a busca nos .editorconfig dos pais", () => {
  const raiz = criarProjeto("[*.java]\ncharset = utf-8\n");
  gravar(raiz, "sub/.editorconfig", "root = true\n");
  const arquivo = gravar(raiz, "sub/A.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_LATIN1);
});

test(".editorconfig sem charset não muda o comportamento", () => {
  const raiz = criarProjeto("[*]\nindent_style = space\n");
  const arquivo = gravar(raiz, "Java/src/A.java", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_LATIN1);
});

test(".kt continua fora do tratamento do hook", () => {
  const raiz = criarProjeto();
  const arquivo = gravar(raiz, "Kotlin/src/A.kt", CODIGO_SANKHYA_UTF8);
  executarHook(MODO_POS, arquivo, novaSessao());
  assert.deepStrictEqual(fs.readFileSync(arquivo), CODIGO_SANKHYA_UTF8);
});
