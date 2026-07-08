# Estrutura Padrão do Documento de Escopo

## Identificação

Tabela curta no início. Campos recomendados:

- Identificação
- Parceiro
- Solicitante
- Módulo / Rotina
- Abordagem técnica sugerida

Manter a tabela do template quando existir. Atualizar apenas os valores.

## Proposta Técnica

Título em destaque:

`Proposta Técnica: {Nome da Demanda}`

## 1. Objetivo do Projeto

Descrever em 1 a 3 parágrafos:

- O que será adequado/criado.
- Qual problema de negócio será resolvido.
- Qual ganho operacional se espera.

## 2. Contexto e Necessidade

Explicar a dor atual, a limitação do processo ou do sistema e por que a mudança é necessária.

## 3. Escopo Funcional

Lista numerada com entregas observáveis. Evitar listar tarefas técnicas puras nesta seção.

Exemplo genérico:

1. Criar parâmetro/campo para controlar o comportamento.
2. Disponibilizar rotina para execução pelo usuário.
3. Aplicar regra de filtro/validação.
4. Registrar auditoria quando houver alteração sensível.
5. Retornar resumo da execução.

## 4. Regras de Negócio

Bullets com regras objetivas:

- Quando valor X, fazer Y.
- Quando não preenchido, aplicar comportamento padrão.
- Quando houver inconsistência, bloquear ou reportar.
- Itens fora da regra permanecem sem alteração.

## 5. Solução Técnica Proposta

Explicar a arquitetura em linguagem acessível:

- Qual componente inicia o fluxo.
- Quais rotinas ou tabelas são usadas.
- Onde a regra será aplicada.
- Como evitar risco de duplicidade, inconsistência ou retrabalho.

## 5.1 Artefatos Técnicos Previstos

Tabela:

| Artefato | Tratamento proposto |
|---|---|
| Campo adicional | Finalidade e regra |
| Botão/rotina | Papel operacional |
| Procedure/view | Papel no processamento |
| Tabela de auditoria | Dados preservados |

## 5.2 Relação com Artefatos Existentes

Usar quando houver SQL, código, relatório, tela ou processo existente.

Tabela:

| Artefato existente | Relação com a demanda | Decisão |
|---|---|---|
| Rotina existente | O que ela faz | Manter / ajustar / descartar / condicional |

## 5.3 Fluxo Operacional Proposto

Lista numerada do fluxo ponta a ponta, do clique/ação inicial até o retorno ao usuário.

## 5.4 Auditoria ou Rastreabilidade

Usar quando houver exclusão, alteração sensível, geração fiscal/financeira, importação ou integração.

Indicar dados mínimos:

- Usuário executor.
- Data/hora.
- Chaves do registro.
- Valor/regra aplicada.
- Motivo.
- Origem da rotina.

## 6. Pontos Técnicos de Atenção

Registrar riscos e cuidados técnicos. Exemplos:

- Chave de busca insegura.
- Rotina que apaga e recria dados.
- Procedure com commits intermediários.
- Dependência de ordem de execução.
- Necessidade de idempotência.
- Necessidade de permissão.

## 7. Critérios de Aceite

Bullets orientados a comportamento:

- Ao executar a rotina, o sistema deve...
- Quando a regra for atendida, o registro deve...
- Quando houver inconsistência, o sistema deve...
- O usuário deve receber...

## 8. Premissas

Condições assumidas para o escopo ser válido.

## 9. Fora do Escopo

Itens relacionados que não serão entregues nesta etapa.

## 10. Dependências e Validações Pendentes

Lista de perguntas ou confirmações necessárias.

## 11. Recomendação Final

Síntese técnica da abordagem escolhida e justificativa.

## 12. Estimativa Inicial de Desenvolvimento

Tabela com faixa de horas:

| Item | Complexidade | Estimativa |
|---|---|---|
| Item funcional/técnico | Baixa/Média/Alta | X-Yh |

Indicar que a estimativa depende das validações pendentes.

## Assinaturas

Manter tabela de assinatura do template.
