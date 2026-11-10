# sankhya-apontamento-os

Skill para Claude Code que transforma o relato livre do consultor em um **apontamento de Ordem de Serviço (OS)** de consultoria de implantação, pronto para colar no sistema.

## O que esta skill faz

- Organiza o relato (data, horários, participantes, atividades, pendências) no formato padrão da OS
- Mantém o texto fiel ao que foi informado: não inventa participante, validação, prazo nem responsável
- Respeita o limite de **4.000 caracteres** do campo, sem Markdown, e confere o tamanho com contagem real
- Confere os horários e avisa quando a jornada passa de 8h, sem alterar o que foi informado
- Pergunta antes de gerar quando falta informação crítica

## Quando acionar

> apontar OS · apontamento de OS · registrar OS · fazer apontamento · colar um relato de atendimento pedindo para organizar

Invocação direta: `/sankhya:apontamento-os`

## Estrutura da skill

```
sankhya-apontamento-os/
├── SKILL.md      Instruções da skill (carregadas pelo Claude Code)
└── README.md     Este arquivo
```
