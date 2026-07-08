---
name: sankhya-gera-escopo
description: Esta skill deve ser utilizada quando o usuário pedir para "criar documento de escopo", "gerar documento de escopo", "fazer proposta técnica de escopo", "criar escopo Sankhya no modelo padrão", "gerar DOCX de escopo", "usar o modelo v2 de escopo", ou quando fornecer contexto geral de uma demanda e quiser um documento Word com formatação, fonte e estilos padronizados.
version: 0.1.0
---

# Criação de Documento de Escopo

## Objetivo

Gerar documentos de escopo em `.docx` no padrão visual do template, preservando fonte, estilos, cores, tabelas e estrutura de assinatura a partir de um template Word. Transformar contexto bruto de uma demanda em texto claro, funcional e tecnicamente defensável, sem exigir que o usuário detalhe toda a estrutura do documento a cada solicitação.

Usar esta skill para criar escopos de demandas Sankhya ou outras demandas técnicas/funcionais que precisem de proposta técnica com linguagem acessível. O resultado deve explicar o problema, a solução, o escopo funcional, a solução técnica, riscos, premissas, dependências, critérios de aceite e estimativa inicial.

## Skills relacionadas

Acionar ou consultar as skills abaixo conforme a demanda:

- `docx`: obrigatória quando for necessário ler, editar ou gerar documento Word preservando estilos.
- `sankhya-estimativa-planejador`: usar quando o contexto envolver requisito funcional, backlog, critérios de aceite, riscos, dependências ou estimativa.
- `sankhya-modulo-java`: usar quando a solução envolver Módulo Java Sankhya, botão de ação, evento, regra, job, JAPE, metadados ou procedures chamadas por Java.
- `sankhya-doc-entrega`: consultar apenas como referência de linguagem e estrutura documental quando o usuário pedir documento de entrega; não confundir escopo com entrega concluída.

## Entradas esperadas

Aceitar contexto incompleto e organizar perguntas apenas quando houver risco real de documentar algo errado. Preferir inferir uma primeira versão e marcar pendências.

Coletar, quando disponível:

- Título da demanda.
- Cliente/parceiro.
- Solicitante ou usuário chave.
- Contexto do problema.
- Solicitação do usuário.
- Solução imaginada ou restrições técnicas.
- Arquivos de apoio, como `.sql`, `.docx`, `.pdf`, `.md`, prints ou anotações.
- Caminho do template `.docx` a ser usado. Se o usuário não informar, usar `assets/escopo-template.docx`.
- Caminho de saída desejado. Se não informado, gerar no diretório de trabalho com nome derivado do título.

## Fluxo obrigatório

### 1. Preservar o template

Usar sempre um `.docx` como base visual. Não recriar estilos manualmente se houver template. Preservar:

- `styles.xml`, tema, fontes, cores, margens, cabeçalhos, rodapés e tabelas padrão.
- Tabela de identificação do início, se existir.
- Tabela de assinaturas do final, se existir.

Para geração programática, preferir `scripts/create_scope_docx.py`, que copia o template, limpa o corpo e reinsere conteúdo usando estilos existentes.

### 2. Extrair e classificar o contexto

Separar o contexto em:

- Objetivo de negócio.
- Contexto e dor operacional.
- Requisitos funcionais.
- Regras de negócio.
- Solução técnica proposta.
- Artefatos impactados.
- Procedimentos, rotinas ou integrações existentes.
- Dados/tabelas/campos relevantes.
- Critérios de aceite.
- Premissas.
- Fora do escopo.
- Dependências e validações pendentes.
- Riscos técnicos.
- Estimativa inicial.

Quando houver arquivos técnicos, ler os arquivos antes de escrever a solução. Para SQL, mapear `SELECT`, `INSERT`, `UPDATE`, `DELETE`, procedures, views, tabelas, campos, chaves e pontos de transação/commit.

### 3. Escrever para público misto

Usar texto fácil de entender, mesmo com definições técnicas. Explicar termos técnicos em contexto, sem transformar o documento em manual técnico.

Preferir frases objetivas:

- "A rotina fará..."
- "O sistema deverá..."
- "Recomenda-se..."
- "Este item depende de validação..."

Evitar excesso de código, SQL bruto ou nomes internos quando eles não ajudam o leitor funcional. Manter nomes técnicos apenas quando forem necessários para rastreabilidade.

### 4. Escolher a arquitetura de forma defensável

Quando a demanda envolver Sankhya, justificar a abordagem:

- Módulo Java para orquestração, validação, botão de ação, mensagens, permissões e controle de fluxo.
- SQL/procedure/view para processamento em massa set-based, quando já existir rotina ou quando o volume justificar.
- Addon Studio apenas quando houver necessidade clara de nova interface customizada.
- Configuração quando o comportamento puder ser resolvido sem desenvolvimento.

Registrar tradeoffs e riscos. Quando houver procedure existente, avaliar se ela deve ser mantida, ajustada, chamada pelo Java ou descartada.

### 5. Gerar a estrutura padrão

Usar esta ordem salvo se o usuário pedir outro modelo:

1. Identificação
2. Proposta Técnica: `{Título}`
3. Objetivo do Projeto
4. Contexto e Necessidade
5. Escopo Funcional
6. Regras de Negócio
7. Solução Técnica Proposta
8. Artefatos Técnicos Previstos
9. Relação com artefatos existentes, quando houver
10. Fluxo Operacional Proposto
11. Auditoria ou rastreabilidade, quando aplicável
12. Pontos Técnicos de Atenção
13. Critérios de Aceite
14. Premissas
15. Fora do Escopo
16. Dependências e Validações Pendentes
17. Recomendação Final
18. Estimativa Inicial de Desenvolvimento
19. Assinaturas

Usar tabelas para artefatos, arquivos existentes e estimativa. Usar bullets para regras, premissas, riscos e critérios de aceite. Usar numeração textual controlada quando a numeração automática do Word não reiniciar corretamente.

### 6. Verificar o documento

Após gerar o `.docx`:

- Converter para Markdown com `pandoc --track-changes=accept` quando `pandoc` estiver disponível.
- Usar `scripts/docx_to_markdown_fallback.py` quando `pandoc` não estiver disponível; essa extração não preserva todos os recursos avançados do Word, mas é suficiente para revisar texto, títulos, bullets e tabelas.
- Abrir o DOCX com `python-docx` e conferir quantidade de parágrafos/tabelas e estilos principais.
- Confirmar que existem estilos `Normal`, `Heading 1`, `Heading 2`, `List Bullet` e tabelas esperadas.
- Verificar se o documento não contém dados específicos de exemplo que não pertencem à nova demanda.

## Recursos incluídos

- `assets/escopo-template.docx`: template Word sanitizado com estilos, fonte, cores e tabelas padrão.
- `scripts/create_scope_docx.py`: gerador de DOCX a partir de um JSON genérico de conteúdo.
- `scripts/docx_to_markdown_fallback.py`: extrator simples de DOCX para Markdown usando Python, para ambientes sem `pandoc`.
- `references/metodo-escopo.md`: método detalhado para extrair escopo de contexto bruto e arquivos técnicos.
- `references/estrutura-documento.md`: estrutura padrão e orientações de redação.
- `examples/conteudo-exemplo.json`: exemplo genérico sem dados reais de cliente.

## Uso rápido

1. Analisar contexto e arquivos de apoio.
2. Montar um JSON no formato de `examples/conteudo-exemplo.json`.
3. Executar:

```bash
python3 ~/.claude/skills/sankhya-gera-escopo/scripts/create_scope_docx.py \
  --content /caminho/conteudo.json \
  --output /caminho/Escopo\ Nome\ da\ Demanda.docx
```

4. Validar com `pandoc`, se disponível:

```bash
pandoc --track-changes=accept /caminho/Escopo.docx -o /tmp/escopo-verificacao.md
```

5. Se `pandoc` não existir no ambiente, usar o fallback Python:

```bash
python3 ~/.claude/skills/sankhya-gera-escopo/scripts/docx_to_markdown_fallback.py \
  /caminho/Escopo.docx \
  -o /tmp/escopo-verificacao.md
```

6. Revisar o Markdown extraído e conferir estilos/tabelas com `python-docx`.

## Cuidados

- Não salvar informações específicas de uma demanda dentro da skill.
- Não usar o template como repositório de conteúdo de cliente.
- Não substituir análise funcional por transcrição literal do contexto recebido.
- Não prometer regra fiscal, contábil ou legal sem validação especializada.
- Não recomendar reescrita completa em Java quando uma procedure/view existente resolve melhor o processamento em massa.
