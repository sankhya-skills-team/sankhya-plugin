# Método para Extrair Escopo a Partir de Contexto Bruto

## 1. Leitura inicial

Separar o material recebido em blocos:

- Problema reportado.
- Solicitação explícita.
- Solução imaginada pelo usuário.
- Limitações do processo atual.
- Artefatos existentes citados.
- Arquivos anexos ou caminhos locais.
- Decisões já tomadas.
- Pontos que ainda precisam de validação.

Preservar a intenção do usuário, mas transformar texto solto em uma proposta objetiva.

## 2. Classificação

Classificar cada trecho:

- Objetivo de negócio: resultado esperado pelo cliente.
- Requisito funcional: comportamento observável do sistema.
- Regra de negócio: condição, exceção, filtro, cálculo ou bloqueio.
- Detalhe técnico: tabela, campo, procedure, classe, entidade, tela, arquivo.
- Dependência: item que precisa existir ou ser validado.
- Premissa: hipótese usada para o documento avançar.
- Risco: ponto que pode causar erro, retrabalho, inconsistência ou problema operacional.
- Fora do escopo: item relacionado, mas não entregue nesta etapa.

## 3. Análise de arquivos técnicos

Quando houver SQL:

- Listar procedures, views e tabelas usadas.
- Identificar onde os dados são gerados, filtrados, apagados ou recalculados.
- Procurar `INSERT`, `UPDATE`, `DELETE`, `COMMIT`, `ROLLBACK`, `JOIN`, parâmetros e campos de chave.
- Avaliar se o processamento é melhor em SQL, Java ou híbrido.
- Registrar riscos de transação, duplicidade, execução repetida e auditoria.

Quando houver DOCX:

- Extrair com `pandoc --track-changes=accept` quando disponível.
- Se `pandoc` não estiver instalado, usar `scripts/docx_to_markdown_fallback.py` para gerar Markdown simples com títulos, parágrafos, listas e tabelas.
- Identificar estrutura, títulos, tabelas e estilos.
- Reaproveitar o arquivo como template se o usuário indicar que a formatação está correta.

Quando houver código Java Sankhya:

- Identificar artefato: botão de ação, evento, regra, job, component, service, repository.
- Separar orquestração, regra de negócio e persistência.
- Validar necessidade de permissões, mensagens e transação.

## 4. Decisão de arquitetura

Usar critérios práticos:

- Botão Java: melhor para execução manual, confirmação, mensagem, validação, permissão e orquestração.
- Procedure/View: melhor para volume, agregação, processamento set-based e reaproveitamento de SQL existente.
- Híbrido: melhor quando o usuário precisa controle operacional e já existe rotina SQL relevante.
- Addon Studio: usar somente se houver nova interface customizada além do comportamento operacional.
- Configuração: usar quando campo, parâmetro ou preferência resolver sem desenvolvimento.

Documentar a recomendação final e também o que foi descartado.

## 5. Redação

Escrever em português claro:

- Começar pelo resultado esperado do negócio.
- Explicar por que a solução foi escolhida.
- Usar nomes técnicos para rastreabilidade, não para impressionar.
- Colocar dúvidas como "Dependências e Validações Pendentes".
- Colocar alertas como "Pontos Técnicos de Atenção".
- Usar estimativa como faixa e indicar premissas da estimativa.

## 6. Validação final

Antes de entregar:

- Conferir se o escopo reflete a última decisão do usuário.
- Conferir se regras invertidas ou exceções foram escritas sem ambiguidade.
- Conferir se não sobrou conteúdo de outro cliente/demanda.
- Conferir se o DOCX abre e mantém estilos.
- Conferir se o Markdown extraído representa corretamente o texto. Preferir `pandoc`; usar fallback Python quando o ambiente não tiver `pandoc`.
