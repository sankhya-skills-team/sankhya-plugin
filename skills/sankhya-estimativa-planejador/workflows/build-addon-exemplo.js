export const meta = {
  name: 'build-addon-exemplo',
  description: 'Gera o addon Sankhya de Controle de OS (exemplo) em ondas: dados -> backend/BI -> frontend',
  phases: [
    { title: 'Dados',    detail: 'datadictionary + dbscripts (barreira)' },
    { title: 'Backend',  detail: 'EJB Service beans (paralelo)' },
    { title: 'BI',       detail: 'relatorio + dashboard (paralelo)' },
    { title: 'Frontend', detail: 'tela vc (apos backend)' },
  ],
}

// Work-list embutido (args do harness nao chega ao script neste ambiente).
const addon = '/home/daniel/c/Projetos/Clientes/exemplo/addon_teste_skill'
const base = `Addon Studio oficial em ${addon}. Partir do template oficial; gravar ISO-8859-1 via iconv/Python (NUNCA Write/Edit nativo) em .java/.xml/.gradle/.sql e UTF-8 em .js/.html; validar entidades via MCP sankhya-schema; Javadoc/JSDoc + comentarios do porque; sem emoji/glifo Unicode; nomes PT-BR. Verificar encoding (file --mime-encoding + LC_ALL=C grep U+FFFD) ao final e reportar.`

const dataPrompt = `O skeleton e a entidade ControleOS (AD_CTROS) JA EXISTEM nesta pasta. ESTENDA a estrutura com dbscripts/V2.xml incremental (dual-dialect, SE_NAO_EXISTIR) + novos arquivos datadictionary, sem recriar AD_CTROS:
- AD_MACROGRUPO (CODIGO PK seq, DESCRICAO)
- AD_PARTNAME (CODIGO PK seq, CODMACRO FK->AD_MACROGRUPO, DESCRICAO)
- AD_CTROSPECA (CODIGO PK seq, NUOS FK->AD_CTROS, CODPROD FK produto TGFPRO, QTD, VLRUNIT, VLRTOTAL)
- AD_CTROSSERV (CODIGO PK seq, NUOS FK->AD_CTROS, CODSERV, QTD, VLRUNIT, VLRTOTAL)
- AD_CTROSFOTO (CODIGO PK seq, NUOS FK->AD_CTROS, ETAPA char(1) P/E/F, LEGENDA, IMAGEM)
Registre as novas entidades no menu.xml como dynamicForm. Valide CODPROD/TGFPRO via MCP. Reporte os EntityNames e campos exatos.`

const backendList = [
  { epic: 'service-providers', prompt: `O EJB OrcamentoOSSP ja existe em serviceprovider/. NAO recriar. Crie/garanta vc/src/main/WEB-INF/resources/service-providers.xml registrando OrcamentoOSSP e os demais EJB do addon.` },
  { epic: 'estoque-compras', prompt: `Crie EJB Service bean (TransferenciaCompraOSSPBean + Service POJO) para gerar pedido de transferencia das pecas da OS (AD_CTROSPECA) para o local Oficina e pedido de compra das pecas sem estoque. Registrar em service-providers.xml. TODO onde depender de parametro de TOP/local.` },
  { epic: 'sla-fila', prompt: `Crie EJB Service bean (PrazoOSSPBean + Service POJO) que calcula o prazo acumulado de conclusao da OS somando os prazos das OS anteriores na fila. Registrar em service-providers.xml.` },
]
const biList = [
  { epic: 'relatorio-orcamento', prompt: `Crie relatorio Jasper (.jrxml) de Orcamento da OS: dados gerais (OS, cliente, equipamento), pecas (AD_CTROSPECA) e servicos (AD_CTROSSERV) com valores e total. Sub-relatorios. TODO para fotos da peritagem (modelo visual do cliente).` },
  { epic: 'dashboard-oficina', prompt: `Crie gadget/dashboard de OS por status (P/O/E/F) com contagem; query sobre AD_CTROS validada via MCP. Sem glifo Unicode (SVG/entidades).` },
]
const frontendList = [
  { epic: 'tela-os-guias', prompt: `Crie a tela vc de Controle de OS com guias (Geral, Pecas, Servicos, Fotos). Pecas/Servicos listam e adicionam itens via sk-dataset (AD_CTROSPECA/AD_CTROSSERV). Botoes chamam os EJB (orcamento/transferencia/compra) via ServiceProxy.callService('controleos@<Servico>SP.metodo', {...}). Status via SVG.` },
]

phase('Dados')
const dados = await agent(`${base}\n\nONDA DADOS: ${dataPrompt}`,
  { agentType: 'sankhya-data-dev', label: 'dados:estrutura', phase: 'Dados' })

const [backend] = await parallel([
  () => parallel(backendList.map((b) => () =>
    agent(`${base}\n\nESTRUTURA CRIADA:\n${dados}\n\nONDA BACKEND (${b.epic}): ${b.prompt}\nRegra: tela custom vc => EJB *SPBean (service-providers.xml); evento => Listener (extension-listeners.xml).`,
      { agentType: 'sankhya-backend-dev', label: `backend:${b.epic}`, phase: 'Backend' }))),
  () => parallel(biList.map((r) => () =>
    agent(`${base}\n\nESTRUTURA CRIADA:\n${dados}\n\nONDA BI (${r.epic}): ${r.prompt}`,
      { agentType: 'sankhya-bi-report-dev', label: `bi:${r.epic}`, phase: 'BI' }))),
])
const backendResumo = (backend || []).filter(Boolean).join('\n---\n')

const frontend = await parallel(frontendList.map((f) => () =>
  agent(`${base}\n\nESTRUTURA:\n${dados}\n\nEJBS CRIADOS:\n${backendResumo}\n\nONDA FRONTEND (${f.epic}): ${f.prompt}`,
    { agentType: 'sankhya-frontend-dev', label: `frontend:${f.epic}`, phase: 'Frontend' })))

return {
  addon,
  backend: (backend || []).filter(Boolean).length,
  bi: biList.length,
  frontend: (frontend || []).filter(Boolean).length,
}
