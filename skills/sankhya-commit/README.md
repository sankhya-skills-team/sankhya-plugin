# sankhya-commit

Skill para Claude Code que conduz o **commit Git** de forma interativa e gera a mensagem no padrão Conventional Commits.

## O que esta skill faz

- Lê o estado do repositório e pergunta quais arquivos entram no stage
- Analisa o diff e propõe a mensagem de commit no padrão Conventional Commits com emoji
- Verifica o encoding dos arquivos em stage antes de commitar

## Quando acionar

> fazer commit · gerar commit · commit · mensagem de commit

Invocação direta: `/sankhya:commit`

## Estrutura da skill

```
sankhya-commit/
├── SKILL.md                           Instruções da skill (carregadas pelo Claude Code)
├── README.md                          Este arquivo
├── verifica_encoding_staged.py        Classifica o encoding dos arquivos em stage
└── test_verifica_encoding_staged.py   Testes do verificador
```
