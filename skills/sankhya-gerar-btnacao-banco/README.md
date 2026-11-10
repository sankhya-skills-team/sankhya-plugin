# sankhya-gerar-btnacao-banco

Skill para Claude Code que gera a procedure PL/SQL de um **Botão de Ação do tipo "Rotina no Banco de dados"** do Sankhya OM, no padrão oficial.

## O que esta skill faz

- Escreve a procedure com a assinatura `P_CODUSU`, `P_IDSESSAO`, `P_QTDLINHAS`, `P_MENSAGEM`
- Lê as linhas selecionadas na grade com as funções `ACT_*_FIELD`
- Lê os parâmetros do formulário com `ACT_*_PARAM` e pede confirmação com `ACT_ESCOLHER_SIMNAO`
- Devolve a mensagem ao usuário por `P_MENSAGEM`
- Traz um roteiro para testar a procedure sem abrir a tela

## Quando acionar

> botão de ação · botão de ação procedure · rotina de banco · ação na grade · procedure para a tela · `STP_` · `ACT_INT_FIELD` · `P_IDSESSAO`

Invocação direta: `/sankhya:gerar-btnacao-banco`

Não usar para botão de ação em Java (`AcaoRotinaJava`, `@ActionButton`) nem para triggers.

## Estrutura da skill

```
sankhya-gerar-btnacao-banco/
├── SKILL.md                    Instruções da skill (carregadas pelo Claude Code)
├── README.md                   Este arquivo
└── examples/
    ├── STP_ENCERRA_OS.sql      Exemplo: encerramento de OS
    ├── STP_TOTALIZA_NOTAS.sql  Exemplo: totalização de notas selecionadas
    └── teste_execparams.sql    Roteiro de teste sem a tela
```

## Skills relacionadas

- `sankhya-gerar-trigger`: trigger Oracle no padrão das nativas
- `sankhya-modulo-java` e `sankhya-addon`: botão de ação em Java
