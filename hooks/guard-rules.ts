// Regras puras, sem acesso ao engine: o que barra uma escrita

// Marcador para liberar um trecho que a guarda acusou por engano
export const IGNORE_MARKER = 'sankhya-guard: ignore'

const STRING_LITERAL = /"""[\s\S]*?"""|"(?:[^"\\\n]|\\.)*"/g
const ORACLE_ONLY_SQL = /\b(NVL2?|DECODE)\s*\(|\b(SYSDATE|ROWNUM)\b/i
const HARDCODED_CREDENTIAL = /\b(password|senha|passwd|pwd|secret|api_?key|token)\b\s*[:=]\s*"([^"${}\s][^"${}]{3,})"/i
// Concatenação de variável (identificador minúsculo) dentro da chamada; CONSTANTES passam
const CONCATENATED_SQL = /\b(appendSql|executeQuery|executeUpdate|executeSql|prepareStatement)\s*\(([^;]*?"\s*\+\s*[a-z_]\w*|\s*[a-z_]\w*\s*\+\s*")/

const LEGACY_AND_BUILD_DIRS = ['FonteLegado/', 'build/', 'ejbsrc/', 'target/']

export type GuardContext = { extension: string; isAddon: boolean }

export function findViolations(content: string, context: GuardContext): string[] {
  if (content.includes(IGNORE_MARKER)) return []
  const violations: string[] = []
  const literals = context.extension === '.java' ? (content.match(STRING_LITERAL) ?? []).join('\n') : ''

  if (context.isAddon && ORACLE_ONLY_SQL.test(literals)) {
    violations.push('SQL só-Oracle (NVL, NVL2, DECODE, SYSDATE ou ROWNUM) em addon, que precisa rodar em Oracle e SQL Server: use COALESCE, CASE e CURRENT_TIMESTAMP, ou passe a data pelo Java como parâmetro.')
  }
  if (HARDCODED_CREDENTIAL.test(content)) {
    violations.push('Credencial em texto puro: leia de parâmetro do sistema, preferência (MGECoreParameter) ou variável de ambiente.')
  }
  if (context.extension === '.java' && CONCATENATED_SQL.test(content)) {
    violations.push('NativeSql/query montada com concatenação de variável (risco de SQL injection): use parâmetros nomeados (:PARAM + setNamedParameter) ou bind.')
  }
  return violations
}

export function isExcludedPath(relativePath: string): boolean {
  const normalized = relativePath.replaceAll('\\', '/')
  return LEGACY_AND_BUILD_DIRS.some(prefix => normalized.toLowerCase().startsWith(prefix.toLowerCase()))
}
