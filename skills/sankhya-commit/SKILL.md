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

#### Verificação de encoding dos arquivos staged

Roda **depois** do `git add`, porque a corrupção pode ocorrer justamente nele (caso
do `git add` interceptado pelo `rtk`: disco íntegro, blob staged corrompido). O script
lê o conteúdo do **índice** (`git show :caminho`), nunca o do disco.

Executar na raiz do repositório (o script fica na pasta desta skill):
```bash
python <diretório-da-skill>/verifica_encoding_staged.py
```

Se `python` não existir ou o script falhar ao executar, avisar o usuário que a
verificação não rodou e seguir para a Etapa 4. Nunca bloquear o fluxo por falha do
próprio script.

Regras aplicadas pelo script:

| Achado | Severidade |
|--------|------------|
| `U+FFFD` no conteúdo staged | ERRO |
| Encodings misturados no mesmo arquivo | ERRO |
| Divergência da política em `.java`, `.kt` ou `.xml` Sankhya | ERRO |
| Divergência da política em outros tipos (só se o `.editorconfig` declarar `charset`) | AVISO |
| Mojibake (`Ã§`, `Ã£`) | AVISO |
| Encoding mudou em relação ao HEAD (Latin-1 ↔ UTF-8) | AVISO |

Política: `charset` do `.editorconfig` para o caminho (última seção que casa vence). Sem
`charset` declarado, valem os padrões do ecossistema: `.java` em ISO-8859-1, `.kt` em
UTF-8 e `.xml` sob `datadictionary`/`dbscripts`/`dbquerys`/`dashboards` em ISO-8859-1.
Demais tipos sem `charset` declarado: só as regras de caractere.

- Sem achados (`Encoding OK.`) → seguir para a Etapa 4.
- Só AVISO → exibir os avisos e pedir confirmação para prosseguir.
- Com ERRO → parar antes da mensagem de commit:

```
ATENÇÃO: encoding inconsistente nos arquivos staged.

[lista de achados do script, ERRO primeiro]

O que fazer com os arquivos com ERRO?
  1 - Cancelar o commit para corrigir
  2 - Re-adicionar ao stage a partir do disco (se o disco estiver íntegro e o índice corrompido)
  3 - Prosseguir mesmo assim (não recomendado)
```

- `1` → encerrar sem commit.
- `2` → executar `git add <arquivo>` para cada arquivo com ERRO e rodar o script de novo.
  Se o ERRO persistir, o problema está no disco: tratar como `1`.
- `3` → prosseguir para a Etapa 4.

Orientação em caso de `U+FFFD` no disco: é perda real, não há conversão que recupere.
Restaurar o trecho de uma versão limpa do histórico, lendo em bytes via `subprocess`
(`git show <commit>:arquivo`, **nunca** com redirecionamento `>` do shell, que corrompe
bytes multibyte neste ambiente), e mapear as palavras pelo contexto.

O script **só avisa**: nunca reconverte arquivo automaticamente.

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
  Exibir output do git. Seguir para Etapa 7.

- `2` → perguntar o que alterar e regerar. Voltar ao início da Etapa 6.

- `3` → encerrar sem commit.

### Etapa 7 — Tag (somente se `version.properties` estiver no diff commitado)

Verificar se `version.properties` está entre os arquivos do commit recém-criado
(`git show --stat HEAD` ou o diff já obtido na Etapa 3). Se **não** estiver, encerrar
— não perguntar sobre tag fora desse caso.

Se estiver, extrair o valor da versão alterada (ex.: `OrdemDeServico=1.0.116`) e perguntar:

```
Esse commit alterou version.properties (nova versão: 1.0.116).

Tag Git é um rótulo fixo num commit — serve pra, se um dia precisar
recuperar exatamente esse ponto do código (ex.: voltar pra um JAR
antigo), não precisar caçar hash de commit. Não guarda o .jar em si,
só marca o código-fonte daquele momento.
(a tag marca esse commit exato — se mudar algo no código depois sem
comitar de novo, o build não vai mais bater com essa tag)

Criar a tag v1.0.116 pra esse commit?
  1 - Sim
  2 - Não
```

- `1` → executar:
  ```bash
  git tag -a v1.0.116 -m "<primeira linha da mensagem de commit>"
  ```
  Depois perguntar:
  ```
  Enviar a tag pro remoto agora (git push origin v1.0.116)?
  Sem isso ela fica só local, nesse computador.
    1 - Sim
    2 - Não, depois
  ```
  - `1` → executar `git push origin <tag>`. Exibir output. Encerrar.
  - `2` → informar que a tag ficou local e encerrar.

- `2` → encerrar sem criar tag.

Pra **recuperar** o código de uma tag antiga depois (rebuildar um JAR de versão
passada), usar a skill `sankhya-recuperar-versao` — não é escopo desta skill.

---

## Regras Gerais

- Sem "Ótima pergunta!", "Claro!", "Vou ajudar", ou qualquer filler.
- Nunca inventar mudanças que não estejam no diff.
- Nunca commitar arquivos `.env`, credenciais ou secrets — alertar se detectado no stage.
- Mensagem sempre em português do Brasil (código e identificadores técnicos permanecem em inglês/original).
- Corpo sempre presente — mensagem commit-only sem corpo não é aceita.
