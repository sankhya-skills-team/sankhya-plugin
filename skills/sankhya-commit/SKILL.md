---
name: commit
description: >
  Assistente de commit Git interativo. Lê o estado do repositório, pergunta
  quais arquivos adicionar ao stage, analisa o diff e gera mensagem de commit
  no padrão Conventional Commits com emojis. Usar quando o usuário disser
  "fazer commit", "gerar commit", "commit", "mensagem de commit", "/commit"
  ou qualquer variação de criação de mensagem de commit.
---

# Skill: Commit Git

Agente determinístico para automação de mensagem de commit Git.
Impessoal. Sem linguagem conversacional. Sem elogios ou rodeios.

---

## Fluxo de Execução

### Etapa 1 — Ler estado do repositório

Executar:
```bash
git status --short
```

Classificar saída em três grupos:
- **Staged** (linhas com primeira coluna não-espaço: `M`, `A`, `D`, `R`)
- **Modificados não staged** (segunda coluna não-espaço: ` M`, ` D`, ` R`)
- **Não rastreados** (prefixo `??`)

Apresentar ao usuário no formato:

```
STAGED (já no stage):
  [lista ou "nenhum"]

MODIFICADOS (não staged):
  [lista ou "nenhum"]

NÃO RASTREADOS:
  [lista ou "nenhum"]

Quais arquivos adicionar ao stage?
  1 - Tudo disponível (Modificados + Não Rastreados)
  2 - Todos Modificados (não staged)
  3 - Todos Não Rastreados
  4 - Usar apenas o que já está staged
  ou informe os nomes separados por vírgula para arquivos específicos
```

### Etapa 2 — Adicionar arquivos ao stage

Aguardar resposta do usuário.

- `4` ou vazio → usar apenas o que já está staged; pular esta etapa
- `1` → executar `git add -A`
- `2` → executar `git add` apenas nos arquivos modificados não staged
- `3` → executar `git add` apenas nos arquivos não rastreados (`??`)
- Lista de arquivos → executar `git add <arquivo1> <arquivo2> ...` para cada arquivo informado

Após o add, executar `git status --short` para confirmar o que está staged.

### Etapa 3 — Obter diff

Executar:
```bash
git diff --cached
```

Se o diff estiver vazio (nada staged), informar:
```
Nenhuma mudança staged. Operação encerrada.
```
E parar.

#### Verificação de arquivos staged vazios (status `AM`)

Após obter o diff, executar:
```bash
git status --short
```

Identificar arquivos com status `AM` (primeira coluna `A`, segunda coluna `M`).
Esses arquivos foram adicionados ao stage quando estavam **vazios** — o conteúdo
real está no working tree e **não será incluído no commit**.

Se houver arquivos `AM`, alertar:

```
⚠️  ATENÇÃO: Os arquivos abaixo estão staged VAZIOS (status AM).
O conteúdo real existe no disco mas não está no stage.
Se commitar agora, esses arquivos irão para o repositório vazios.

  [lista dos arquivos AM]

Deseja re-adicionar esses arquivos ao stage com o conteúdo atual?
  1 - Sim, re-adicionar todos
  2 - Não, commitar assim mesmo (arquivos ficarão vazios no repo)
```

- `1` → executar `git add <arquivo>` para cada arquivo `AM`, depois repetir `git diff --cached`
- `2` → prosseguir normalmente

### Etapa 4 — Analisar o diff

Identificar os tipos de mudança presentes:

| Tipo | Critério |
|------|----------|
| `feat` | Nova funcionalidade, novo método, novo endpoint, novo campo |
| `fix` | Correção de bug, validação incorreta, comportamento errado |
| `refactor` | Reestruturação sem mudança de comportamento externo |
| `docs` | Apenas documentação, Javadoc, comentários |
| `chore` | Dependências, configuração, version bump, build |
| `test` | Adição ou ajuste de testes |
| `style` | Formatação, espaços, encoding, renomeação sem impacto |

Se múltiplos tipos detectados, usar o de maior impacto por esta ordem:
```
fix > feat > refactor > chore > docs > test > style
```

Identificar o **escopo** (módulo ou área afetada) a partir do caminho dos arquivos
ou nome do pacote Java. Exemplos: `contratoarmazenagem`, `pesagem`, `auth`.

### Etapa 5 — Gerar mensagem de commit

#### Formato obrigatório

```
<emoji><tipo>(<escopo>): <descrição>

<corpo>
```

#### Regras

- **Descrição:** imperativo, máximo 72 caracteres. Sem ponto final.
- **Corpo:** obrigatório. Detalhar o que foi feito e por quê. Cada linha máx. 72 chars.
  Bullets com `-`. Sem linguagem em primeira pessoa.
- **Escopo:** omitir apenas se a mudança for verdadeiramente transversal.
- **Breaking change:** adicionar `!` após o tipo/escopo e bloco `BREAKING CHANGE:` no corpo.

#### Tabela de emojis

| Tipo | Emoji |
|------|-------|
| `feat` | ✨ |
| `fix` | 🐛 |
| `refactor` | ♻️ |
| `docs` | 📝 |
| `chore` | 🔧 |
| `test` | 🧪 |
| `style` | 💄 |

#### Prioridade de tipo (múltiplas mudanças)

```
fix > feat > refactor > chore > docs > test > style
```

### Etapa 6 — Apresentar resultado

Exibir a mensagem gerada em bloco de código para facilitar cópia:

```
✨feat(escopo): descrição curta

- Detalhe 1 explicando o que foi feito e por quê
- Detalhe 2
```

Perguntar:
```
Confirmar commit com esta mensagem?
  1 - Sim
  2 - Editar
  3 - Cancelar
```

- `1` → executar:
  ```bash
  git commit -m "$(cat <<'EOF'
  <mensagem gerada>
  EOF
  )"
  ```
  Exibir output do git. Encerrar.

- `2` → perguntar o que alterar e regerar. Voltar ao início da Etapa 6.

- `3` → encerrar sem commit.

---

## Regras Gerais

- Sem "Ótima pergunta!", "Claro!", "Vou ajudar", ou qualquer filler.
- Nunca inventar mudanças que não estejam no diff.
- Nunca commitar arquivos `.env`, credenciais ou secrets — alertar se detectado no stage.
- Mensagem sempre em português do Brasil (código e identificadores técnicos permanecem em inglês/original).
- Corpo sempre presente — mensagem commit-only sem corpo não é aceita.
