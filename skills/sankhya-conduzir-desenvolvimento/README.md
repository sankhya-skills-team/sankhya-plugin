# sankhya-conduzir-desenvolvimento

Skill para Claude Code que **conduz o desenvolvimento de uma demanda Sankhya em fases**, uma fase por execução, e garante o code review antes de mesclar e de entregar.

## O que esta skill faz

- Lê o escopo aprovado e aponta lacunas; chama o `sankhya-orchestrator-agent-dev` para o plano, com as horas aprovadas como orçamento (sem reestimar)
- Cada fase em uma branch própria (`feature/f<n>-<slug>`), delegando ao especialista do plano
- **Code review obrigatório quando há `.java`**, sempre pelo agent `code-review-orchestrator` (cinco revisores); registra a resolução dos achados
- Resumo da fase no registro de decisões, commit, merge `--no-ff` na base e atualização do card (Satori, opcional)
- No fim da última fase: review do conjunto, JAR (Módulo Java), documento de entrega, commit, push e tag
- Evidências por fase **opcionais**, decididas no planejamento (`Evidências:` no `CLAUDE.md` do projeto)

## Quando acionar

Só manualmente, digitando o comando **no início da mensagem**:

```
/sankhya:sankhya-conduzir-desenvolvimento <caminho do escopo> <horas>h
/sankhya:sankhya-conduzir-desenvolvimento            (continua o plano ou fecha o que foi codificado)
```

## Configuração no `CLAUDE.md` do projeto

`Tipo:` (Módulo Java ou Addon), `Base:`, `Entrega:`, `Fluxo de branch:`, `Plano:`, `Registro de decisões:`, `Evidências:`. Sem `Tipo:`, a skill pergunta uma vez e oferece criar o arquivo.

## Hook

O `gate-review` (em `hooks/`) bloqueia `git commit` e `git tag` com `.java` alterado sem review atualizado.

## Estado de validação

Validada em projeto **Addon**. O caminho de **Módulo Java** (JAR, `inc-`, `version.properties`, tag) ainda não foi exercitado de ponta a ponta: relatar qualquer comportamento diferente do descrito.

## Estrutura da skill

```
sankhya-conduzir-desenvolvimento/
├── SKILL.md      Instruções da skill (carregadas pelo Claude Code)
└── README.md     Este arquivo
```
