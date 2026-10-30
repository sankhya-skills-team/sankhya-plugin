import type { EngineInterface, Register } from 'claude-code'

import { findViolations, isExcludedPath } from './guard-rules'

// Bloqueios de escrita em projetos Sankhya; o encoding ISO-8859-1 fica no register.ts
const GUARDED_EXTENSIONS = new Set(['.java', '.xml', '.properties'])
const SANKHYA_GRADLE = /br\.com\.sankhya|maven\.sankhya\.com\.br/
const SANKHYA_SKILL = /sankhya-(conversao-flex-addon|addon|js|dicionario|modulo-java|jape|bi|relatorio|doc-entrega)/

type ProjectKind = { isSankhya: boolean; isAddon: boolean }

// Mesmos sinais do pre-commit global; o resultado fica em cache por raiz
const projectCache = new Map<string, ProjectKind>()

async function fileMatches($: EngineInterface, path: string, pattern: RegExp): Promise<boolean> {
  try {
    return (await $.fs.exists(path)) && pattern.test(await $.fs.read(path))
  } catch {
    return false
  }
}

// Add-on: as mesmas pastas marcadoras que o plugin Sankhya usa
async function detectProject($: EngineInterface, root: string): Promise<ProjectKind> {
  const cached = projectCache.get(root)
  if (cached) return cached
  const isAddon = (await $.fs.exists(`${root}/datadictionary`)) || (await $.fs.exists(`${root}/dbscripts`))
  const isSankhya =
    isAddon ||
    (await fileMatches($, `${root}/build.gradle`, SANKHYA_GRADLE)) ||
    (await fileMatches($, `${root}/build.gradle.kts`, SANKHYA_GRADLE)) ||
    (await fileMatches($, `${root}/CLAUDE.md`, SANKHYA_SKILL))
  const kind = { isSankhya, isAddon }
  projectCache.set(root, kind)
  return kind
}

function extensionOf(path: string): string {
  const match = /\.[^./\\]+$/.exec(path)
  return match ? match[0].toLowerCase() : ''
}

function relativeTo(root: string, path: string): string | null {
  const normalizedRoot = root.replaceAll('\\', '/').replace(/\/+$/, '').toLowerCase()
  const normalizedPath = path.replaceAll('\\', '/')
  if (!normalizedPath.toLowerCase().startsWith(`${normalizedRoot}/`)) return null
  return normalizedPath.slice(normalizedRoot.length + 1)
}

async function guardedTarget($: EngineInterface, filePath: string) {
  const extension = extensionOf(filePath)
  if (!GUARDED_EXTENSIONS.has(extension)) return null
  const root = await $.session.cwd()
  const relative = relativeTo(root, filePath)
  if (relative === null || isExcludedPath(relative)) return null
  const project = await detectProject($, root)
  return project.isSankhya ? { extension, isAddon: project.isAddon } : null
}

// Motivo da recusa, ou undefined quando a escrita pode seguir
async function motivoDeBloqueio($: EngineInterface, filePath: string, content: string): Promise<string | undefined> {
  const target = await guardedTarget($, filePath)
  if (!target) return undefined
  const violations = findViolations(content, target)
  if (violations.length === 0) return undefined
  return `sankhya-guard bloqueou a escrita em ${filePath}:\n- ${violations.join('\n- ')}\nCorrija e tente de novo.`
}

export const registrarGuard: Register = on => {
  on('tool.call', { tool: 'Write' }, async ($, e, next) => {
    const deny = await motivoDeBloqueio($, e.file_path, e.content)
    return deny === undefined ? next(e) : { deny }
  }).catch(($, e, next) => next(e)) // falha da guarda nunca impede o trabalho
  on('tool.call', { tool: 'Edit' }, async ($, e, next) => {
    const deny = await motivoDeBloqueio($, e.file_path, e.new_string)
    return deny === undefined ? next(e) : { deny }
  }).catch(($, e, next) => next(e))
}
