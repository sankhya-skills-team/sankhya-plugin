# Padrões de requisito recorrentes em escopos Sankhya

Padrões destilados de escopos reais de personalização (armazenagem, beneficiamento, comercialização). Cada padrão: **sinais no texto** → **artefato Sankhya** → **pegadinha de estimativa**. Consultar ao classificar (Etapa 2), gerar tarefas técnicas (Etapa 8) e estimar (Etapa 11).

---

## Cabeçalho de identificação do escopo (Etapa 1)

Quase todo escopo Sankhya abre com bloco canônico. Extrair como contexto de projeto — não é requisito, mas dá rastreabilidade e responsáveis:

| Campo | Uso |
|---|---|
| Parceiro / Cliente | Identificação do projeto |
| Processo / Subprocesso / Código | Macroclassificação funcional (ex.: "Controle de Armazenagem / Beneficiamento", cód. 30757) |
| Usuário Chave | Quem valida regras de negócio na dúvida |
| Responsável pela área / Patrocinador | Decisor de escopo |
| Participantes (consultor, GP, key user) | Stakeholders |
| Documentos de Entrada | **Dependência documental** — ver padrão abaixo |
| Validação da Etapa (assinaturas) | Marca escopo aprovado vs rascunho |

Registrar na seção **0. Identificação** do output.

---

## Dependência documental (referências cruzadas)

**Sinais:** "conforme levantamento X", "item 5.2 em diante do documento Y", "detalhado no escopo Z", "documentos de entrada", "Extra Escopo".

**Conduta:** o requisito referenciado **não está neste documento**. Registrar como dependência de leitura em "9. Dependências e riscos" e marcar a story afetada com confiança reduzida. Nunca estimar a regra remetida como se estivesse completa — `[PENDENTE: ler documento X item Y]`.

---

## Itens extra-escopo / negociação de horas

**Sinais:** "não constem em proposta comercial", "objeto de negociação de horas", "extra escopo", "após a criação das personalizações", "poderá ser desenvolvido".

**Conduta:** segregar do total compromissado. Listar em bloco separado "Itens fora do escopo fechado / a negociar". Estimar à parte, sinalizando que **não entram no total principal**. Relatórios/dashboards marcados como "após personalizações" são sequenciados depois, não paralelos.

---

## Classificação `[NATIVO/HOMOLOGAÇÃO]`

**Sinais:** "rotina nativa deverá ser testada e validada", "será repassada e simulada com a equipe", "opção nativa do ERP", "configurada conforme cronograma", "relatório nativo não passível de alteração".

**Conduta:** não é desenvolvimento Java. É **homologação/parametrização/teste** — consome horas de consultoria, não de dev. Classificar `[NATIVO/HOMOLOGAÇÃO]` e estimar pela faixa de teste/parametrização (ver heuristicas-estimativa). Não jogar como zero nem como dev.

> Distinção: `[CONFIGURAÇÃO]` = ajustar parâmetro/preferência. `[NATIVO/HOMOLOGAÇÃO]` = testar e validar rotina nativa existente com o usuário-chave.

---

## Geração automática de documento fiscal derivado

**Sinais:** "emitir automaticamente a nota de quebra/rendimento/complemento", "gerar nota de remessa", "geração automática de NF", lista de definições (TOP, quantidade, valor unitário, local, lote, empresa, parceiro, contrato, financeiro).

**Artefato:** `AcaoRotinaJava` / `EventoProgramavelJava` que monta `CabecalhoNota` (TGFCAB) + itens (TGFITE) via `EntityFacade` / regra de inclusão, define TOP por parâmetro, replica vínculos (contrato, financeiro TGFFIN).

**Pegadinha:** cada "definição" da lista é uma regra de cópia/cálculo. Alta complexidade quando envolve financeiro (títulos TGFFIN) e vínculo de contrato. Não é "1 insert" — é orquestração de documento comercial. Multiplicador de geração de documento fiscal derivado (ver estimativa).

---

## Fluxo de alçada / liberação via TSILIB

**Sinais:** "liberação de limites", "alçada", "evento personalizado de abono/liberação", "usuário liberador", "solicitação de liberação", TSILIB.

**Artefato:** evento personalizado de liberação + inserção de solicitação na `TSILIB` + leitura de alçada do usuário executante + gravação do liberador. Frequentemente acoplado a tela detalhe (registra valor liberado + usuário).

**Pegadinha:** dois caminhos (executante tem alçada → libera direto; não tem → cria solicitação para terceiro). Mais o efeito pós-liberação (gera título, atualiza status). Multiplicador alçada já existe (×1.4), mas o **artefato de liberação tem esforço próprio** — somar à base, não só multiplicar.

---

## Rotina idempotente de reprocessamento (máquina de estado)

**Sinais:** "ação agendada deverá verificar se já existe número único", "se o título estiver baixado", "excluir o título gerado anteriormente e regerar", "abono parcial / 100%", múltiplos "Caso... caso..." sobre o mesmo registro.

**Artefato:** `ScheduledAction` / `@Job` com ramos sobre estado persistido (existe? baixado? valor mudou?) que **exclui e regera** registros financeiros.

**Pegadinha:** é a maior fonte de subestimação. Cada ramo é um cenário de teste; exclusão+regeração de título financeiro exige cuidado transacional (`execWithAutonomousTX`), idempotência e tratamento de concorrência. Tratar sempre como **alta complexidade** e aplicar multiplicador de reprocessamento idempotente.

---

## Operação multiempresa matriz-filial

**Sinais:** "remessa matriz → filial", "nota de saída da matriz e entrada na filial", "escrituração de NF-e emitida pelo cliente", "transferência de posse", "cenário 1 / cenário 2", referência cruzada entre empresas/contratos.

**Artefato:** orquestração de múltiplos `CabecalhoNota` entre empresas, com referenciamento (observações/TGFVAR), escrituração de NF-e de terceiros, vínculo de contrato origem/destino.

**Pegadinha:** complexidade fiscal alta (NF-e, CFOP, impostos por cenário). Cada cenário é um fluxo completo. Combina com multiplicador NF-e e multiempresa. Tende a virar epic próprio, nunca uma story.

---

## Conversão de unidades / volume

**Sinais:** "KG, SC, TN, BG", "calcular quantidade correspondente em quilos/sacas/toneladas", "valor por quilo/saca/tonelada", "unidades alternativas", "conversão de volume".

**Artefato:** campos de unidade ligados a tabela de volumes + lógica de conversão (evento/derivação) que preenche campos nativos automaticamente.

**Pegadinha:** conversão bidirecional e arredondamento. Erro de conversão propaga para pedido, nota e financeiro. Multiplicador de conversão de unidades.

---

## Tela adicional / aba detalhe em tabela nativa

**Sinais:** "tela adicional detalhe da TCSCON", "aba descontos de classificação", lista de campos com PK sequencial + FKs para tabelas nativas (TGFCAB, TGFITE, TCSCON).

**Artefato:** tabela `AD_*` + XML Construtor de Telas (módulo) ou `DataDictionary` + `DBScripts` (addon), vinculada como detalhe/aba de entidade nativa.

**Pegadinha:** estimar por número de campos e FKs. Campo que referencia tabela nativa exige carga/derivação. Tela detalhe acoplada a regra de gravação (gatilho na confirmação da nota) soma o esforço do evento que a alimenta.

---

## Campo adicional em tabela nativa com destino explícito

**Sinais:** "campo adicional na TGFTOP", "AD_ na TGFCAB", "campo Status Glifosato na aba geral", "ligação na TGFVAR".

**Conduta (Etapa 2.5 / MCP):** validar via `describe_table` se o campo já existe. Citado e ausente → **criação de campo adicional** (tarefa técnica + metadado + tela + persistência), nunca tratar como existente. Confirmar a tabela destino real via MCP antes de incluir na estimativa.

---

## Hierarquia mãe/filha com agregação (OS/SubOS, kit, projeto)

**Sinais:** "OS mãe e SubOS filha", numeração automática + nível hierárquico, "orçamento da mãe consolida as filhas", "macrogrupo → peças".

**Artefato:** entidade auto-referente (campo pai), regra de numeração automática, e **agregação recursiva** (orçamento/pedido da mãe soma filhas; gerar só de uma filha é independente).

**Pegadinha:** a rotina que cria a estrutura hierárquica é **rotina-âncora** (concentra Documentação/Treinamento do módulo — ver `template-horas-fases.md`). A agregação recursiva e a rastreabilidade "nenhum item omitido no faturamento" são a parte cara, não o cadastro.

---

## Tela multi-guia com upload de fotos

**Sinais:** "tela com guias", "campos de imagem", "6 grids para anexar fotos com legenda", "Fotos Recebimento/Peritagem/Finalização".

**Artefato:** tela personalizada com N guias; campos tipados por guia (imagem/upload, integração a cadastro, não-editável/consulta, texto livre). Anexos exigem storage/gestão de arquivo.

**Pegadinha:** estimar por **guia** (cada aba ≈ 4h dev na calibração real) + a estrutura. Guias de upload de imagem custam mais que guias de campo simples. Relatório que exibe as fotos é linha separada.

---

## Orquestração intra-Sankhya (entre módulos nativos)

**Sinais:** botão que "gera pedido de venda no portal", "gera requisição de transferência", "gera pedido de compra para reposição", "reserva estoque na aprovação".

**Artefato:** botão de ação que orquestra módulos nativos (Vendas/Compras/Estoque/Portais) — não é integração externa. Cada botão ≈ 16h dev (calibração).

**Pegadinha:** não confundir com integração externa (sem retry/autenticação de terceiro). Mas envolve regras de reserva, local de estoque (ex.: transferir para local "Oficina" só na aprovação) e rastreabilidade do número gerado de volta na tela.

---

## Retorno simbólico + explosão de lotes (FIFO)

**Sinais:** "Gerar Retorno Simbólico", "explodir lote na confirmação", "FIFO dos lotes", "depósito fechado", par de notas espelhadas.

**Artefato:** botão em `TGFCAB` + procedures + evento de confirmação que bloqueia lote nulo. Par de notas saída/entrada com empresa/parceiro **invertidos**; FIFO por data de lote; validação de saldo por depósito.

**Pegadinha:** a lógica de saldo/FIFO por depósito é o custo, não a geração da nota. TOPs em Central de Parâmetros, nunca hardcode.

---

## Recálculo / atualização de custo (Kardex)

**Sinais:** "atualização dos valores de entrada", "custos do Kardex corretos", "substituir valor unitário", "marcação na TOP".

**Artefato:** tela (produto+empresa+período) + botão que faz UPDATE em movimentos + flag na TOP.

**Pegadinha:** **idempotência crítica** — "não permitir reexecutar / não gerar registro duplo", gravar usuário+horário (auditoria). Reprocessar Kardex tem efeito cascata em custo médio — não é UPDATE trivial. Casa com o multiplicador de reprocessamento idempotente.

---

## Memória de cálculo de custo (CMV/CPV por fase de produção)

**Sinais:** "memória de cálculo do produto acabado", "detalhamento de CMV/CPV", "custo por fase de apontamento de produção".

**Artefato:** dashboard BI multinível (drill orçamento→item→MP→produção) + relatório iReport imprimível em **dois pontos de entrada** (portal + central).

**Pegadinha:** composição MP+produção+gastos fixos/variáveis+margem; custo por fase (ordem de produção). Impressão tem de funcionar nos dois pontos.

---

## Integração contábil / arquivo de remessa (Questor e congêneres)

**Sinais:** "lançamentos para contabilidade", "configuração de arquivo de remessa", geração de **.txt** por período, layout posicional de terceiro, "Receita=C, Despesa=F".

**Artefato:** tela nativa **"Configuração Arquivo Remessa"** (EDI) — layout sintético+detalhe, aba Query, aba Campos.

**Pegadinha:** classificar `[NATIVO/HOMOLOGAÇÃO]`/`[CONFIGURAÇÃO]`, **não desenvolvimento Java**. O esforço é montar a query e o layout posicional (posições/CNPJ-CPF condicional/histórico fixo). Não estimar como dev.

---

## Empréstimos / financiamento (parcelas, juros, mútuo)

**Sinais:** "Controle de Empréstimos", "Gerar Parcelas/Juros", "Tipo de Amortização (SAC/Price)", "carência", "Empréstimos Mútuos", "Empresa Credora".

**Artefato:** tela com abas (Geral/Condições/Pagamentos/Mútuo) + botões que geram financeiro (`TGFFIN`).

**Pegadinha:** cálculo de amortização (SAC/Price), carência, juros a.a.; **mútuo intercompany** gera financeiro nas duas empresas. Botão "Gerar Parcelas/Juros" ≈ 32h dev (calibração — está no topo da faixa).

---

## Ordem de carga / coleta / viagem (logística)

**Sinais:** "Ordem de Carga", "Ordem de Coleta", "conferência na coleta", "docas", "assinatura do motorista", "data prevista de entrega".

**Artefato:** relatório formatado (iReport) vinculado à Ordem de Carga; vínculo Pedido ↔ Ordem ↔ doca.

**Pegadinha:** o entregável é **relatório de impressão para o motorista**, não tela. "Tomar como referência o modelo do cliente" = layout fechado → ver dependência de modelo visual abaixo.

---

## Kit promocional com bonificação

**Sinais:** "kits promocionais", "campo Bonificação/desconto na aba componente", "explosão dos kits na nota", "preço por tipo de negociação".

**Artefato:** campo adicional na aba componente do Kit + regra de preço por tabela/tipo de negociação + explosão na nota.

**Pegadinha:** bonificação 100% + preço puxado da tabela correta por tipo de negociação; soma componentes no valor do kit. Parte fiscal costuma ser premissa "já configurada" — registrar.

---

## Dependência de modelo visual (anexo .jpg/.pdf)

**Sinais:** "modelo de orçamento/etiqueta em anexo", "tomar como referência o modelo atual", arquivos `.jpg`/`.pdf` de layout citados.

**Conduta:** a IA **não vê** o anexo visual → relatório/etiqueta **não estimável com precisão** sem o modelo. Registrar como dependência documental de artefato visual em "9. Dependências" e marcar a estimativa do relatório com confiança reduzida. Layout fechado de terceiro = risco de retrabalho.

---

## Ponto de entrada não autenticado no Sankhya OM

**Sinais:** "consulta pública", "validar documento sem login", "regerar boleto por link", "endpoint externo sem autenticação Sankhya", servlet/serviço acessível sem sessão nativa.

**Artefato:** servlet/serviço (ex.: `javax.servlet`, `sanws`) que entra no Sankhya OM **sem autenticar nativamente** — padrão útil para validação de documento, 2ª via de boleto, consulta pública. Caso de referência: um projeto real.

**Pegadinha (segurança — crítico):** entrada sem autenticação é **superfície de ataque**. Exige obrigatoriamente: validação/sanitização de entrada (evitar `NativeSql` injection), rate limiting, token/assinatura no link, escopo mínimo de dados expostos, sem credenciais no código. Cruzar com a skill `sankhya-padroes-seguranca`. Registrar como risco de segurança em "9. Dependências e riscos" e estimar o esforço de hardening, não só o caminho feliz.
