# sankhya-recuperar-versao

Skill para Claude Code que **recupera o código-fonte de uma tag Git antiga** para rebuildar o JAR de uma versão passada, sem afetar a branch nem a working tree atual.

## O que esta skill faz

- Localiza a tag pedida (por exemplo `v1.0.115`)
- Recupera o código daquela versão numa worktree separada (recomendado, não mexe na pasta atual) ou por checkout direto
- Deixa o estado antigo pronto para o build do JAR

## Quando acionar

> recuperar versão antiga · resgatar JAR de uma tag · voltar pro código da tag X · buildar uma versão anterior · preciso do jar da vX.Y.Z

## Estrutura da skill

```
sankhya-recuperar-versao/
├── SKILL.md      Instruções da skill (carregadas pelo Claude Code)
└── README.md     Este arquivo
```
