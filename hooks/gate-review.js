// Hook PreToolUse (Bash): bloqueia git commit e git tag em projeto Sankhya quando há
// .java alterado sem um relatório de review mais novo em docs/reviews/.
// Só age em projeto que declara "Tipo: Módulo Java" ou "Tipo: Addon" no CLAUDE.md.
// Nunca atrapalha o fluxo por erro próprio: qualquer falha inesperada libera.
//
// Saída de emergência (vale uma vez): criar o arquivo .git/pular-review no projeto.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const CODIGO_LIBERA = 0;
const CODIGO_BLOQUEIO = 2;
const PASTA_RELATORIOS = path.join('docs', 'reviews');
const MARCADOR_PULAR = 'pular-review';
const EXTENSAO_REVISADA = '.java';
const ARQUIVOS_DO_TIPO = ['CLAUDE.md', 'CLAUDE.local.md'];

const RE_TIPO = /^\s*[*_]*tipo[*_]*\s*:\s*[*_]*\s*(m[oó]dulo java|add-?on)/im;
const OPCOES_GIT = String.raw`(?:\s+(?:-C\s+("[^"]+"|'[^']+'|\S+)|-c\s+\S+|--no-pager))*`;
const RE_COMMIT = new RegExp(String.raw`\bgit\b${OPCOES_GIT}\s+commit\b`);
const RE_TAG = new RegExp(String.raw`\bgit\b${OPCOES_GIT}\s+tag\b([^|;&\n]*)`);
const RE_TAG_SOMENTE_LEITURA = /(^|\s)(-l|--list|-d|--delete|-v|--verify)(\s|$)/;

const liberar = () => ({ codigo: CODIGO_LIBERA, mensagem: '' });

function pastaAlvo(comando, cwd) {
  const pedido = /\bgit\b(?:\s+(?:-c\s+\S+|--no-pager))*\s+-C\s+("[^"]+"|'[^']+'|\S+)/.exec(comando);
  if (!pedido) return cwd;
  return path.resolve(cwd, pedido[1].replace(/^["']|["']$/g, ''));
}

function ehCommitOuTagDeCriacao(comando) {
  if (RE_COMMIT.test(comando)) return true;
  const tag = RE_TAG.exec(comando);
  if (!tag) return false;
  const argumentos = tag[tag.length - 1].trim();
  return argumentos !== '' && !RE_TAG_SOMENTE_LEITURA.test(argumentos);
}

function git(cwd, ...args) {
  return execFileSync('git', args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
}

function raizDoProjeto(cwd) {
  return path.resolve(git(cwd, 'rev-parse', '--show-toplevel').trim());
}

function declaraTipo(raiz) {
  return ARQUIVOS_DO_TIPO.some((nome) => {
    const arquivo = path.join(raiz, nome);
    return fs.existsSync(arquivo) && RE_TIPO.test(fs.readFileSync(arquivo, 'utf8'));
  });
}

// Formato -z: "XY caminho\0", e renomeações trazem o caminho de origem no registro seguinte.
function javaAlterados(raiz) {
  const registros = git(raiz, 'status', '--porcelain=v1', '-z', '--untracked-files=all').split('\0').filter(Boolean);
  const arquivos = [];
  for (let i = 0; i < registros.length; i++) {
    const situacao = registros[i].slice(0, 2);
    const caminho = registros[i].slice(3);
    if (/[RC]/.test(situacao)) i++;
    if (situacao.includes('D')) continue;
    if (caminho.toLowerCase().endsWith(EXTENSAO_REVISADA)) arquivos.push(path.join(raiz, caminho));
  }
  return arquivos.filter((arquivo) => fs.existsSync(arquivo));
}

function relatorioMaisRecenteMs(raiz) {
  const pasta = path.join(raiz, PASTA_RELATORIOS);
  if (!fs.existsSync(pasta)) return 0;
  return fs
    .readdirSync(pasta)
    .filter((nome) => nome.endsWith('.md'))
    .reduce((maior, nome) => Math.max(maior, fs.statSync(path.join(pasta, nome)).mtimeMs), 0);
}

function consumirMarcador(raiz) {
  const marcador = path.join(raiz, '.git', MARCADOR_PULAR);
  if (!fs.existsSync(marcador)) return false;
  fs.unlinkSync(marcador);
  return true;
}

function mensagemDeBloqueio(quantidade, relatorioMs) {
  const ultimo = relatorioMs ? new Date(relatorioMs).toLocaleString('pt-BR') : 'nenhum';
  return (
    `Bloqueado: ${quantidade} arquivo(s) ${EXTENSAO_REVISADA} alterado(s) sem review atualizado (último relatório: ${ultimo}). ` +
    `Faça o fechamento com /sankhya:sankhya-conduzir-desenvolvimento antes de commitar ou criar tag. ` +
    `Para pular uma única vez, crie o arquivo .git/${MARCADOR_PULAR} no projeto.`
  );
}

function avaliar(entrada) {
  try {
    const comando = entrada && entrada.tool_input && entrada.tool_input.command;
    if (typeof comando !== 'string' || !ehCommitOuTagDeCriacao(comando)) return liberar();

    const raiz = raizDoProjeto(pastaAlvo(comando, entrada.cwd || process.cwd()));
    if (!declaraTipo(raiz)) return liberar();

    const alterados = javaAlterados(raiz);
    if (alterados.length === 0) return liberar();
    if (consumirMarcador(raiz)) return liberar();

    const fonteMaisNovaMs = Math.max(...alterados.map((arquivo) => fs.statSync(arquivo).mtimeMs));
    const relatorioMs = relatorioMaisRecenteMs(raiz);
    if (relatorioMs >= fonteMaisNovaMs) return liberar();

    return { codigo: CODIGO_BLOQUEIO, mensagem: mensagemDeBloqueio(alterados.length, relatorioMs) };
  } catch {
    return liberar();
  }
}

function executarComoHook() {
  let texto = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (parte) => (texto += parte));
  process.stdin.on('end', () => {
    let entrada = null;
    try {
      entrada = JSON.parse(texto);
    } catch {
      process.exit(CODIGO_LIBERA);
    }
    const { codigo, mensagem } = avaliar(entrada);
    if (mensagem) process.stderr.write(mensagem + '\n');
    process.exit(codigo);
  });
}

if (require.main === module) executarComoHook();

module.exports = { avaliar };
