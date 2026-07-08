# SDK Sankhya — Serviço de Logs Remotos

> **Acesso Antecipado (Beta):** Não habilitado automaticamente para todos os projetos.

## Visão Geral

Permite enviar logs de forma centralizada para análise, auditoria e monitoramento. O SDK intercepta mensagens dos loggers suportados, enriquece com contexto (usuário, transação, módulo) e envia para o serviço remoto.

Não é necessário alterar o código de logging existente — a configuração ocorre automaticamente.

---

## Loggers Suportados

| Framework | Suporte |
|---|---|
| Log4J 1.x | Suportado |
| JUL (`java.util.logging`) | Suportado |

---

## Ativação

1. Configure o componente de logs na **Área do Desenvolvedor** da Sankhya
2. Após aprovação, o serviço é ativado sem alterações no código

Para verificar se está ativo: gere um log de nível `INFO` ou superior e consulte o painel de observabilidade.

---

## Recomendações

- Use níveis de log de forma consistente (`ERROR` para exceções reais, `INFO` para operações normais)
- Inclua contexto útil nas mensagens (ID do pedido, usuário, etapa do processo)
- Evite logar objetos grandes ou dados sigilosos
- Logs excessivos aumentam custos e impactam performance

---

## Fonte

https://developer.sankhya.com.br/docs/servi%C3%A7o-de-logs-remotos
