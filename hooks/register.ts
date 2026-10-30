import type { EngineInterface, Register, ToolCallResult } from 'claude-code'

// Encoding ISO-8859-1 dos fontes Sankhya: o gate e a conversao ficam em
// sankhya-encoding.js (testado com node --test); aqui so a volta da ferramenta
const CONVERSOR = 'hooks/sankhya-encoding.js'
const EXTENSOES = /\.(java|xml)$/i
const AVISO_RELEITURA =
  'sankhya-encoding: o arquivo foi gravado de volta em ISO-8859-1. Se uma releitura mostrar os acentos como U+FFFD, é só a exibição; o arquivo não está corrompido.'

type Conversao = { exitCode: number; stderr: string }

function converter($: EngineInterface, modo: '--pre' | '--post', arquivo: string): Promise<Conversao> {
  const argumentos = modo === '--pre' ? [modo] : []
  return $.process.run(['node', `${$.plugin.root}/${CONVERSOR}`, ...argumentos], {
    stdin: JSON.stringify({ tool_input: { file_path: arquivo } }),
  })
}

// O arquivo so fica em UTF-8 no disco durante a ferramenta
async function envolver($: EngineInterface, arquivo: string, ehLeitura: boolean, executar: () => Promise<ToolCallResult>): Promise<ToolCallResult> {
  await converter($, '--pre', arquivo)
  const resultado = await executar()
  const { exitCode, stderr } = await converter($, '--post', arquivo)
  if (resultado.deny !== undefined) return resultado

  const avisos = exitCode !== 0 || stderr.includes('AVISO') ? [stderr.trim()] : []
  if (!ehLeitura && stderr.includes('convertido')) avisos.push(AVISO_RELEITURA)
  if (avisos.length === 0) return resultado
  return { ...resultado, context: [...(resultado.context ?? []), ...avisos] }
}

export const register: Register = on => {
  on('tool.call', { tool: 'Read' }, ($, e, next) =>
    EXTENSOES.test(e.file_path) ? envolver($, e.file_path, true, () => next(e)) : next(e),
  ).catch(($, e, next) => next(e)) // falha do mod nunca impede o trabalho
  on('tool.call', { tool: 'Edit' }, ($, e, next) =>
    EXTENSOES.test(e.file_path) ? envolver($, e.file_path, false, () => next(e)) : next(e),
  ).catch(($, e, next) => next(e))
  on('tool.call', { tool: 'Write' }, ($, e, next) =>
    EXTENSOES.test(e.file_path) ? envolver($, e.file_path, false, () => next(e)) : next(e),
  ).catch(($, e, next) => next(e))
}
