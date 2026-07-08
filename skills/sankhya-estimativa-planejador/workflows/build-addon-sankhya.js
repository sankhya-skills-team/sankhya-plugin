export const meta = {
  name: 'build-addon-sankhya',
  description: 'Gera um addon Sankhya completo a partir de um backlog, em ondas (dados -> backend/BI -> frontend), usando os agents especialistas. Le o backlog de args; cai num work-list embutido se args nao vier.',
  phases: [
    { title: 'Dados',    detail: 'skeleton oficial + datadictionary + dbscripts (barreira)' },
    { title: 'Backend',  detail: 'EJB Service beans + Listeners por epic (paralelo)' },
    { title: 'BI',       detail: 'relatorios e dashboards HTML5 (paralelo com backend)' },
    { title: 'Frontend', detail: 'telas vc que chamam os EJB (apos backend)' },
  ],
}

// ---------------------------------------------------------------------------
// CONFIG VIA args (preferencial). Passar no campo `args` da tool Workflow como
// VALOR JSON REAL (objeto), nunca string JSON. Formato esperado:
//   {
//     addonPath: '/caminho/do/addon',
//     partner:   'Nome Parceiro',
//     dataPrompt: 'instrucao da onda de dados...',
//     backend:  [ { epic, prompt }, ... ],
//     bi:       [ { epic, prompt }, ... ],
//     frontend: [ { epic, prompt }, ... ],
//   }
// Se args vier vazio/malformado, usa FALLBACK abaixo (work-list embutido) — assim
// o script nunca quebra por args ausente (pegadinha do harness em alguns ambientes).
// ---------------------------------------------------------------------------

const FALLBACK = {
  addonPath: '/home/daniel/c/Projetos/Clientes/exemplo/addon_teste_skill',
  partner: 'Parceiro Exemplo',
  dataPrompt: `O skeleton e a entidade ControleOS (AD_CTROS) JA EXISTEM. ESTENDA com dbscripts/V2.xml incremental (dual-dialect, SE_NAO_EXISTIR) + datadictionary, sem recriar AD_CTROS:
- AD_MACROGRUPO (CODIGO PK seq, DESCRICAO)
- AD_PARTNAME (CODIGO PK seq, CODMACRO FK->AD_MACROGRUPO, DESCRICAO)
- AD_CTROSPECA (CODIGO PK seq, NUOS FK->AD_CTROS, CODPROD FK TGFPRO, QTD, VLRUNIT, VLRTOTAL)
- AD_CTROSSERV (CODIGO PK seq, NUOS FK->AD_CTROS, CODSERV, QTD, VLRUNIT, VLRTOTAL)
- AD_CTROSFOTO (CODIGO PK seq, NUOS FK->AD_CTROS, ETAPA char(1) P/E/F, LEGENDA, IMAGEM)
Registre as novas entidades no menu.xml como dynamicForm. Valide CODPROD/TGFPRO via MCP. Reporte EntityNames e campos exatos.`,
  backend: [
    { epic: 'service-providers', prompt: `Garanta vc/src/main/webapp/WEB-INF/resources/service-providers.xml registrando todos os EJB *SPBean do addon. Nao recriar beans existentes.` },
    { epic: 'estoque-compras', prompt: `EJB Service bean (TransferenciaCompraOSSPBean + Service POJO) para gerar pedido de transferencia das pecas da OS (AD_CTROSPECA) ao local Oficina e pedido de compra das pecas sem estoque. Registrar em service-providers.xml. TODO onde depender de parametro de TOP/local.` },
    { epic: 'sla-fila', prompt: `EJB Service bean (PrazoOSSPBean + Service POJO) que calcula o prazo acumulado de conclusao da OS somando os prazos das OS anteriores na fila. Registrar em service-providers.xml.` },
  ],
  bi: [
    { epic: 'relatorio-orcamento', prompt: `Relatorio Jasper (.jrxml) de Orcamento da OS: dados gerais (OS, cliente, equipamento), pecas (AD_CTROSPECA) e servicos (AD_CTROSSERV) com valores e total. TODO para fotos da peritagem (modelo visual do cliente).` },
    { epic: 'dashboard-oficina', prompt: `Dashboard de OS por status (P/O/E/F) com contagem, em HTML5 com visual moderno (ver regra de dashboard HTML5 do agent BI). Query sobre AD_CTROS validada via MCP. Sem glifo Unicode.` },
  ],
  frontend: [
    { epic: 'tela-os-guias', prompt: `Tela vc de Controle de OS com guias (Geral, Pecas, Servicos, Fotos). Pecas/Servicos listam e adicionam itens via sk-dataset (AD_CTROSPECA/AD_CTROSSERV). Botoes chamam os EJB via ServiceProxy.callService('<rootProjectName>@<Servico>SP.metodo', {...}). Status via SVG.` },
  ],
}

// Resolve config: args real (objeto) tem prioridade; senao, fallback.
const cfg = (args && typeof args === 'object' && args.addonPath) ? args : FALLBACK
const usouFallback = cfg === FALLBACK
log(usouFallback
  ? 'args ausente/invalido -> usando work-list embutido (FALLBACK)'
  : `config via args -> addon ${cfg.addonPath}`)

const addon = cfg.addonPath
const backendList = Array.isArray(cfg.backend) ? cfg.backend : []
const biList = Array.isArray(cfg.bi) ? cfg.bi : []
const frontendList = Array.isArray(cfg.frontend) ? cfg.frontend : []

const base = `Addon Studio oficial em ${addon}. Parceiro: ${cfg.partner || ''}. Partir do template oficial; gravar ISO-8859-1 via iconv/Python (NUNCA Write/Edit nativo) em .java/.xml/.gradle/.sql e UTF-8 em .js/.html/.css; validar entidades via MCP sankhya-schema; acesso a dados JAPE-first (NativeSql so com API verificada); Javadoc/JSDoc + comentarios do porque; sem emoji/glifo Unicode; nomes PT-BR. Verificar encoding (file --mime-encoding + LC_ALL=C grep U+FFFD) ao final e reportar.`

// ---- Onda 1: DADOS (barreira — backend/frontend dependem da estrutura) ----
phase('Dados')
const dados = await agent(
  `${base}\n\nONDA DADOS: ${cfg.dataPrompt}\nGere/estenda skeleton, datadictionary (tables/nativeTable/menu) e dbscripts dual-dialect idempotente. Reporte EntityNames e campos exatos.`,
  { agentType: 'sankhya-data-dev', label: 'dados:estrutura', phase: 'Dados' }
)

// ---- Onda 2: BACKEND (paralelo por epic) + BI (paralelo) ----
const [backend] = await parallel([
  () => parallel(backendList.map((b) => () =>
    agent(`${base}\n\nESTRUTURA CRIADA:\n${dados}\n\nONDA BACKEND (${b.epic}): ${b.prompt}\nRegra: tela custom vc => EJB *SPBean (service-providers.xml); evento => Listener (extension-listeners.xml).`,
      { agentType: 'sankhya-backend-dev', label: `backend:${b.epic}`, phase: 'Backend' }))),
  () => parallel(biList.map((r) => () =>
    agent(`${base}\n\nESTRUTURA CRIADA:\n${dados}\n\nONDA BI/RELATORIO (${r.epic}): ${r.prompt}`,
      { agentType: 'sankhya-bi-report-dev', label: `bi:${r.epic}`, phase: 'BI' }))),
])
const backendResumo = (backend || []).filter(Boolean).join('\n---\n')

// ---- Onda 3: FRONTEND (apos backend — JS chama os EJB criados) ----
const frontend = await parallel(frontendList.map((f) => () =>
  agent(`${base}\n\nESTRUTURA:\n${dados}\n\nEJBS CRIADOS (use os nomes de servico reais):\n${backendResumo}\n\nONDA FRONTEND (${f.epic}): ${f.prompt}\nA tela vc chama o EJB via ServiceProxy.callService('<rootProjectName>@<Servico>SP.metodo', {...}).`,
    { agentType: 'sankhya-frontend-dev', label: `frontend:${f.epic}`, phase: 'Frontend' })))

return {
  addon,
  usouFallback,
  dados: typeof dados === 'string' ? dados.slice(0, 400) : null,
  backend: (backend || []).filter(Boolean).length,
  bi: biList.length,
  frontend: (frontend || []).filter(Boolean).length,
}
