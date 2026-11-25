// Testes do gate de review. Rodar: node --test ~/.claude/hooks/gate-review.test.js
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { execFileSync, spawnSync } = require('node:child_process');
const { avaliar } = require('./gate-review.js');

const CODIGO_LIBERA = 0;
const CODIGO_BLOQUEIO = 2;
const UM_MINUTO_MS = 60 * 1000;

function git(cwd, ...args) {
  return execFileSync('git', ['-c', 'user.name=t', '-c', 'user.email=t@t', '-c', 'commit.gpgsign=false', ...args], {
    cwd,
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'],
  });
}

function criarProjeto({ declaraTipo = true } = {}) {
  const raiz = fs.mkdtempSync(path.join(os.tmpdir(), 'gate-review-'));
  git(raiz, 'init', '-q');
  fs.writeFileSync(path.join(raiz, 'CLAUDE.md'), declaraTipo ? '# Projeto\n\nTipo: Módulo Java\n' : '# Projeto\n');
  git(raiz, 'add', '-A');
  git(raiz, 'commit', '-q', '-m', 'inicial');
  return raiz;
}

function gravarJava(raiz, nome = 'Exemplo.java') {
  const arquivo = path.join(raiz, 'Java', 'src', nome);
  fs.mkdirSync(path.dirname(arquivo), { recursive: true });
  fs.writeFileSync(arquivo, 'class Exemplo {}\n');
  return arquivo;
}

function gravarRelatorio(raiz, mtimeMs) {
  const pasta = path.join(raiz, 'docs', 'reviews');
  fs.mkdirSync(pasta, { recursive: true });
  const arquivo = path.join(pasta, '2026-10-22_10-00.md');
  fs.writeFileSync(arquivo, '# review\n');
  fs.utimesSync(arquivo, new Date(mtimeMs), new Date(mtimeMs));
}

function definirMtime(arquivo, mtimeMs) {
  fs.utimesSync(arquivo, new Date(mtimeMs), new Date(mtimeMs));
}

const entrada = (comando, cwd) => ({ tool_name: 'Bash', tool_input: { command: comando }, cwd });

test('comando que não é commit nem tag é liberado', () => {
  const raiz = criarProjeto();
  gravarJava(raiz);
  assert.equal(avaliar(entrada('git status', raiz)).codigo, CODIGO_LIBERA);
  assert.equal(avaliar(entrada('./gradlew pesagemavulsa', raiz)).codigo, CODIGO_LIBERA);
});

test('projeto que não declara o Tipo é liberado', () => {
  const raiz = criarProjeto({ declaraTipo: false });
  gravarJava(raiz);
  assert.equal(avaliar(entrada('git commit -m x', raiz)).codigo, CODIGO_LIBERA);
});

test('sem .java alterado, o commit é liberado', () => {
  const raiz = criarProjeto();
  fs.writeFileSync(path.join(raiz, 'LEIAME.md'), 'x\n');
  assert.equal(avaliar(entrada('git commit -m x', raiz)).codigo, CODIGO_LIBERA);
});

test('.java alterado sem relatório bloqueia o commit', () => {
  const raiz = criarProjeto();
  gravarJava(raiz);
  const resultado = avaliar(entrada('git add -A && git commit -m x', raiz));
  assert.equal(resultado.codigo, CODIGO_BLOQUEIO);
  assert.match(resultado.mensagem, /sankhya-conduzir-desenvolvimento/);
});

test('relatório mais novo que o .java libera o commit', () => {
  const raiz = criarProjeto();
  const java = gravarJava(raiz);
  const agora = Date.now();
  definirMtime(java, agora - UM_MINUTO_MS);
  gravarRelatorio(raiz, agora);
  assert.equal(avaliar(entrada('git commit -m x', raiz)).codigo, CODIGO_LIBERA);
});

test('relatório mais antigo que o .java bloqueia o commit', () => {
  const raiz = criarProjeto();
  const java = gravarJava(raiz);
  const agora = Date.now();
  gravarRelatorio(raiz, agora - UM_MINUTO_MS);
  definirMtime(java, agora);
  assert.equal(avaliar(entrada('git commit -m x', raiz)).codigo, CODIGO_BLOQUEIO);
});

test('git tag para listar é liberado e para criar é bloqueado', () => {
  const raiz = criarProjeto();
  gravarJava(raiz);
  assert.equal(avaliar(entrada('git tag', raiz)).codigo, CODIGO_LIBERA);
  assert.equal(avaliar(entrada('git tag -l "v1*"', raiz)).codigo, CODIGO_LIBERA);
  assert.equal(avaliar(entrada('git tag -a v1.0.5 -m x', raiz)).codigo, CODIGO_BLOQUEIO);
});

test('git -C aponta para outro projeto', () => {
  const raiz = criarProjeto();
  gravarJava(raiz);
  const fora = fs.mkdtempSync(path.join(os.tmpdir(), 'gate-fora-'));
  assert.equal(avaliar(entrada(`git -C "${raiz}" commit -m x`, fora)).codigo, CODIGO_BLOQUEIO);
});

test('arquivo marcador libera uma vez e é consumido', () => {
  const raiz = criarProjeto();
  gravarJava(raiz);
  const marcador = path.join(raiz, '.git', 'pular-review');
  fs.writeFileSync(marcador, '');
  assert.equal(avaliar(entrada('git commit -m x', raiz)).codigo, CODIGO_LIBERA);
  assert.equal(fs.existsSync(marcador), false);
  assert.equal(avaliar(entrada('git commit -m x', raiz)).codigo, CODIGO_BLOQUEIO);
});

test('entrada inválida nunca bloqueia', () => {
  assert.equal(avaliar(null).codigo, CODIGO_LIBERA);
  assert.equal(avaliar({}).codigo, CODIGO_LIBERA);
  assert.equal(avaliar(entrada('git commit -m x', path.join(os.tmpdir(), 'nao-existe-xyz'))).codigo, CODIGO_LIBERA);
});

test('execução como hook: stdin com JSON bloqueia com código 2 e mensagem no stderr', () => {
  const raiz = criarProjeto();
  gravarJava(raiz);
  const resultado = spawnSync('node', [path.join(__dirname, 'gate-review.js')], {
    input: JSON.stringify(entrada('git commit -m x', raiz)),
    encoding: 'utf8',
  });
  assert.equal(resultado.status, CODIGO_BLOQUEIO);
  assert.match(resultado.stderr, /review/i);
});

test('execução como hook: stdin lixo sai com código 0', () => {
  const resultado = spawnSync('node', [path.join(__dirname, 'gate-review.js')], { input: 'nao e json', encoding: 'utf8' });
  assert.equal(resultado.status, CODIGO_LIBERA);
});
