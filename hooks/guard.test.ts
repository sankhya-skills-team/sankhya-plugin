import { expect, test } from 'claude-code/testing'

import { findViolations, isExcludedPath } from './guard-rules'

const ADDON_JAVA = { extension: '.java', isAddon: true }
const MODULE_JAVA = { extension: '.java', isAddon: false }

test('SQL só-Oracle barra só em addon e só dentro de string', () => {
  expect(findViolations('sql.appendSql("SELECT NVL(VLR, 0) FROM TGFCAB");', ADDON_JAVA)).toHaveLength(1)
  expect(findViolations('String s = "WHERE DTNEG < SYSDATE";', ADDON_JAVA)).toHaveLength(1)
  expect(findViolations('sql.appendSql("SELECT NVL(VLR, 0) FROM TGFCAB");', MODULE_JAVA)).toHaveLength(0)
  expect(findViolations('BigDecimal v = nvl(valor);', ADDON_JAVA)).toHaveLength(0)
  expect(findViolations('sql.appendSql("SELECT COALESCE(VLR, 0) FROM TGFCAB");', ADDON_JAVA)).toHaveLength(0)
})

test('credencial em texto puro', () => {
  expect(findViolations('String senha = "Sk@2024forte";', MODULE_JAVA)).toHaveLength(1)
  expect(findViolations('<conexao password="abc123"/>', { extension: '.xml', isAddon: false })).toHaveLength(1)
  expect(findViolations('String senha = "";', MODULE_JAVA)).toHaveLength(0)
  expect(findViolations('password="${DB_PASSWORD}"', { extension: '.xml', isAddon: false })).toHaveLength(0)
})

test('NativeSql concatenado', () => {
  expect(findViolations('sql.appendSql("SELECT * FROM TGFPAR WHERE CODPARC = " + codParc);', MODULE_JAVA)).toHaveLength(1)
  expect(findViolations('sql.executeQuery(query + " ORDER BY 1");', MODULE_JAVA)).toHaveLength(1)
  expect(findViolations('sql.appendSql("SELECT * FROM " + TABELA_PARCEIRO);', MODULE_JAVA)).toHaveLength(0)
  expect(findViolations('sql.appendSql("WHERE CODPARC = :CODPARC");', MODULE_JAVA)).toHaveLength(0)
})

test('marcador libera o trecho', () => {
  expect(findViolations('// sankhya-guard: ignore\nString senha = "Sk@2024forte";', MODULE_JAVA)).toHaveLength(0)
})

test('exclusões de pasta', () => {
  expect(isExcludedPath('FonteLegado/Financeiro/build.xml')).toBe(true)
  expect(isExcludedPath('build\\classes\\A.java')).toBe(true)
  expect(isExcludedPath('src/main/java/A.java')).toBe(false)
})

test('bloqueia escrita com violação e deixa passar o resto', async ($, on) => {
  const root = 'C:/proj/addon'
  on('session.cwd', () => ({ value: root }))
  on('fs.exists', (_engine, e) => ({ value: e.path.endsWith('dbscripts') }))
  on('tool.call', () => ({ result: {} }))

  const denied = await $.tool.call({ tool: 'Write', file_path: `${root}/src/A.java`, content: 'String senha = "Sk@2024forte";' })
  expect(denied.deny).toContain('Credencial em texto puro')

  const addonSql = await $.tool.call({ tool: 'Edit', file_path: `${root}/src/B.java`, old_string: 'x', new_string: 'sql.appendSql("SELECT NVL(A, 0)");', replace_all: false })
  expect(addonSql.deny).toContain('SQL só-Oracle')

  const allowed = await $.tool.call({ tool: 'Write', file_path: `${root}/src/C.java`, content: 'String nome = "ação";' })
  expect(allowed.deny).toBe(undefined)
})
