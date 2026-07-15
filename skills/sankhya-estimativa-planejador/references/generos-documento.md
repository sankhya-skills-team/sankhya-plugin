# Gêneros de documento e seções canônicas

A localização da informação muda conforme o gênero. **Detectar o gênero na Etapa 1** antes de extrair — e ajustar postura, confiança e se há ou não estimativa a gerar.

## 7 gêneros

| Gênero | Sinais | Postura da skill |
|---|---|---|
| **A. Discovery pré-vendas** (MODELO TECH V2) | Perguntas-guia: "Qual o negócio?", "Qual o problema?", "Como é hoje?", "Por que o nativo não atende?", "Como gostaria que fosse?" | To-be **aspiracional**, não contratado → confiança menor, mais hipóteses/pendências. Estimar itemizado e confrontar âncora |
| **B. Levantamento formal assinado** | "LEVANTAMENTO DE REGRAS PARA PERSONALIZAÇÃO", FAP/OS, Participantes, Processo/Subprocesso, blocos por artefato (BOTÃO DE AÇÃO / REGRA DE NEGÓCIO / DEFINIÇÃO DE DESENVOLVIMENTO), Validação da Etapa | Escopo aprovado/congelado → confiança maior. Backlog + estimativa normais |
| **C. Requisito com controle de versão** | Histórico de Alterações, Glossário, Lista de Aprovadores, "OS de Origem", "Segmento" | Ler a **versão mais recente**. Confiança maior |
| **D. Levantamento com spec de BI/relatório embutida** | Tabelas de Componentes de BI (Nível/Componente/Onclick/Argumentos), expressões SQL, "Estrutura do Relatório" | Spec técnica pronta → tarefas técnicas e estimativa com alta confiança para o entregável visual |
| **E. As-built / Documento de Entrega** | Sumário paginado, seções "Views"/"Triggers"/"Funções" com DDL, tabela "NOME OBJETO/TIPO/OBJETIVO", assinatura D4Sign | **NÃO estimar** — já entregue. Usar como referência técnica/complexidade |
| **F. Manual / Caso de Uso** | "1. Introdução / 2. Telas / 3. Acessos / 4. Caso de Uso", "Caminho: menu >> submenu" | **NÃO estimar** — as-built, foco em operação/permissões |
| **G. Proposta comercial** | "PROPOSTA COMERCIAL DE LICENÇA DE USO/IMPLANTAÇÃO", tabela "REFERÊNCIA/VL. LÍQUIDO/VL. BRUTO", "Anexo I - Funcionalidades", Packs por módulo, "Escopo Fechado", assinatura D4Sign, LICENCIANTE/LICENCIADA | **NÃO estimar dev** — âncora de escopo/teto; ver tratamento abaixo |

Gêneros A–D → gerar backlog + estimativa. Gêneros E–G → não gerar estimativa de desenvolvimento.

## Gênero G — Proposta comercial (tratamento)

Contrato comercial (Licença + Implantação + Anexos de Packs), **não documento técnico**. Contrata **parametrização de funcionalidades nativas ("Escopo Fechado")**, não desenvolvimento. Frase-gatilho: *"customizações... deverão ser tratadas em nova proposta comercial"*.

- **Útil:** módulos/Packs contratados (fronteira de escopo), dimensionamento (acessos simultâneos, filiais, coligadas), valores e horas genéricas (teto contratual), add-ons especiais (DashViewer, Pedido Web, ASIS Tax).
- **Insuficiente:** sem regras de negócio, campos, telas, critérios de aceite, layouts de integração.
- **Conduta:**
  - Usar como **âncora de fronteira e teto contratual**, nunca como fonte de estimativa de dev.
  - **Cruzar com o levantamento detalhado**: requisito detalhado sem Pack correspondente → scope creep / nova proposta; Pack contratado sem levantamento → lacuna de detalhamento.
  - Sinalizar obrigatoriamente: "Proposta é Escopo Fechado de funcionalidades nativas; personalizações exigem levantamento técnico e nova proposta — não estimar dev a partir dela."

## Gêneros menores (não geram backlog de desenvolvimento)

- **Chamado / ticket de suporte** ("Chamado nº", e-mail de inconsistência) — incidente, não escopo.
- **Formulário de personalização** (formulário-padrão Sankhya de pedido de customização) — gatilho para levantamento, ainda superficial.
- **Planilha de validação/homologação de procedimentos** — artefato de teste, não requisito.
- **Template de horas (.xlsx)** — artefato de estimativa (ver `template-horas-fases.md`), não documentação de requisito.

## Perguntas-guia do discovery (gênero A) — mapear para análise

- "Qual o problema a ser resolvido?" / "Como é realizado atualmente?" → **situação as-is** (alimenta Mapa de impacto e justifica prioridade)
- "Por que o nativo não atende?" → sinal de que **não é configuração**; justifica desenvolvimento
- "Como gostaria que fosse?" → **to-be**; aqui mora o detalhe estimável (campos, guias, botões, rotinas)
- "É operacional ou gerencial?" / "Que entrega gera valor?" / "Critérios de sucesso?" → priorização e definição de pronto

## Seções canônicas a sempre procurar

1. **Identificação / Dados do Projeto** — normalizar sinônimos: `Parceiro` (±código), `Nro. Flow`, `Número da FAP`, `Número da OS`, `OS de Origem`, `Segmento`, `Projeto`, `Produto do Projeto`. Ausência em branco é comum — não tratar como erro.
2. **Participantes / Fornecedores de Requisitos / Aprovadores** — Nome/Cargo/Empresa(E-mail). Distinguir papéis Sankhya (Consultor, GP) vs cliente (Usuário-chave, Líder).
3. **Contextualização / História do Processo** — narrativa as-is, fonte do "por que customizar".
4. **Premissas e Responsabilidades** — cláusulas-padrão recorrentes: cliente provê ambiente de teste; novo escopo = novo orçamento; **"não serão desenvolvidos relatórios/dashboards além dos descritos"** (delimitador de escopo crítico).
5. **Teste e Homologação** — "contempla testes, homologação e documentação de entrega" → sempre incluir essas atividades nas fases da estimativa.
6. **Cláusula "segue funcionalidades nativas"** — "as parametrizações se limitam às funcionalidades nativas" → fronteira `[NATIVO/HOMOLOGAÇÃO]`/`[CONFIGURAÇÃO]`, não desenvolvimento.
7. **PONTO DE ATENÇÃO** — riscos técnicos explícitos do consultor → alimentam diretamente a seção de riscos.
8. **Validação da Etapa / Assinaturas** (física ou D4Sign) — marca documento **aprovado/congelado** vs rascunho.
9. **Módulos necessários / Investimento / Prazo** — no discovery vêm **vazios**: são **saídas** que a skill produz, não entradas.

## Higiene de entrada

- **Boilerplate D4Sign:** descartar antes de analisar. Rodapé repetido `D4Sign <uuid> - Para confirmar...` em toda página + bloco final de Assinaturas/Eventos/Hash SHA poluem a classificação de trechos.
- **Template clonado:** detectar quando o **parceiro citado no corpo ≠ parceiro do nome do arquivo** (ex.: doc de "Eucamad" reusado para CASG e EDI Comercial). Não duplicar backlog/estimativa nem atribuir ao parceiro errado. Sinalizar a suspeita de reuso.


## Aprendizado de campo (projeto real, 2026)

### Detecção de as-built técnico disfarçado de levantamento
Um `.docx`/`.pdf` com nome de levantamento pode ser **as-built técnico** (entrega de dev), não requisito. Sinais inequívocos: nomes de tabelas `AD_*` concretos, **caminhos de classe Java** (`br.com.sankhya.dctm....botaoacao.X`), **módulos numerados**, nomes de eventos/botões e preferências (`FS_CODTIPOPER`). As-built **não gera estimativa** — é referência técnica do que já existe. Em um caso real, dois `.docx` eram as-built do módulo-java já em produção; tratá-los como requisito teria duplicado ~700h de escopo.

### Pegadinha do "addon do zero" sobre base as-built
Quando existe base as-built em **módulo-java** e o cliente pede **addon novo sem herança**, surge um epic implícito **E0 = reconstrução da base** (cadastros, telas, eventos já existentes). Isso ~2,3× o custo de simplesmente estender. Sempre **perguntar e flagar E0 explicitamente** antes de estimar; oferecer a alternativa de manter a base no módulo-java e o addon cobrir só o complementar.
