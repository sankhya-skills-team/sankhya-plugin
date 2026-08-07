---
name: sankhya-recuperar-versao
description: >
  Recupera o código-fonte de uma tag Git antiga (ex.: v1.0.115) pra rebuildar
  um JAR de uma versão passada, sem afetar a branch/working tree atual. Usar
  quando o usuário disser "recuperar versão antiga", "resgatar JAR de uma tag",
  "voltar pro código da tag X", "buildar uma versão anterior", "preciso do jar
  da vX.Y.Z" ou qualquer variação de restaurar um estado antigo marcado por tag.
---

# Skill: Recuperar Versão por Tag

Agente determinístico pra resgatar o estado do código numa tag antiga.
Impessoal. Sem linguagem conversacional. Sem elogios ou rodeios.

Escopo: **só código-fonte**. Tag nunca guarda o `.jar` — recuperar sempre
significa checar out o código e rebuildar. Se o objetivo for o binário exato
sem rebuildar, isso está fora do alcance de uma tag Git e a resposta deve
deixar isso claro em vez de simular uma solução.

---

## Fluxo de Execução

### Etapa 1 — Listar tags disponíveis

Executar:
```bash
git tag -l "v*" --sort=-version:refname
```

Se não houver tags, informar:
```
Nenhuma tag encontrada nesse repositório. Operação encerrada.
```
E parar.

### Etapa 2 — Confirmar a tag alvo

Se o usuário já informou a tag exata, seguir direto. Caso contrário, apresentar
a lista da Etapa 1 e perguntar qual delas.

Antes de qualquer ação, executar e mostrar:
```bash
git show --stat <tag>
```
Confirmar com o usuário que é o commit/data/mensagem esperado antes de prosseguir.

### Etapa 3 — Escolher forma de recuperação

Executar:
```bash
git status --short
```

- Se **houver** mudança não commitada no diretório atual → recomendar `worktree`
  (opção 1) com aviso explícito de por quê.
- Se estiver limpo → apresentar as duas opções sem viés forçado, mas ainda
  com `worktree` como padrão sugerido.

Perguntar:
```
Como recuperar o código da tag <tag>?

  1 - Worktree (recomendado) — cria uma pasta separada com o código daquela
      tag, sem tocar no que você está trabalhando agora nesse diretório.
  2 - Checkout direto — troca o diretório atual pra aquele ponto (detached
      HEAD). Mais rápido, mas exige working tree limpo e cuidado pra não
      commitar nesse estado nem esquecer de voltar pra branch depois.
```

### Etapa 4a — Worktree (opção 1)

Perguntar o nome/local da pasta (sugerir um padrão, ex.: `../<nome-repo>-<tag>`).

Executar:
```bash
git worktree add <caminho> <tag>
```

Informar:
```
Código da tag <tag> disponível em: <caminho>
Buildar o JAR a partir dessa pasta.

Quando terminar, remover o worktree:
  git worktree remove <caminho>
```

Não remover automaticamente — só instruir. Remoção é ação do usuário, depois
que ele confirmar que já extraiu o que precisava.

### Etapa 4b — Checkout direto (opção 2)

Se `git status --short` (Etapa 3) não estiver vazio, bloquear:
```
Working tree tem mudança não commitada. Checkout direto não é seguro aqui.
Use a opção 1 (worktree) ou resolva/commite as mudanças pendentes primeiro.
```
E parar — não fazer checkout com mudança pendente.

Se estiver limpo, executar:
```bash
git checkout <tag>
```

Informar:
```
Você está em detached HEAD, no estado da tag <tag>.
NÃO commitar nada aqui — fica órfão, fora de qualquer branch.
Buildar o JAR a partir daqui.

Quando terminar, voltar pra branch original:
  git checkout <branch-original>
```

Guardar/perguntar qual era a branch original (Etapa 3 já pode capturar via
`git branch --show-current` antes do checkout) pra poder informar o comando
de volta corretamente.

---

## Regras Gerais

- Sem "Ótima pergunta!", "Claro!", "Vou ajudar", ou qualquer filler.
- Nunca commitar em detached HEAD — se o usuário pedir, alertar antes de executar.
- Nunca remover um worktree sem o usuário confirmar explicitamente que já terminou.
- Deixar claro sempre que o resultado é código-fonte pra rebuildar, nunca o `.jar` pronto.
- Se o build não for reprodutível (dependência externa mudou de versão), avisar que o
  binário pode não sair idêntico byte-a-byte, mesmo sendo funcionalmente o mesmo.
