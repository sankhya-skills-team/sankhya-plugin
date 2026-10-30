---
applyTo: "**/*.java,**/*.xml"
---

# Codificacao de Arquivos — Modulo Java Sankhya

Fontes `.java` e XMLs do Construtor de Telas em projetos de modulo Java Sankhya **ficam em ISO-8859-1 (Latin-1)**. Para `.java`, o mod `sankhya-encoding` do plugin cuida da conversao: use Read/Edit/Write normalmente.

---

## Por que ISO-8859-1

O servidor Sankhya (Wildfly legado) e o compilador Java do modulo esperam Latin-1. Arquivo salvo em UTF-8 causa corrupcao de acentos e falha silenciosa em runtime. Isso vale para `.java` e para os XMLs do Construtor de Telas.

---

## Regras

| Tipo de arquivo | Encoding |
|:----------------|:---------|
| `.java` de fonte | ISO-8859-1. Acentos literais. |
| `.xml` (Construtor de Telas) | ISO-8859-1. Cabecalho **obrigatorio**: `<?xml version="1.0" encoding="ISO-8859-1" ?>` |
| `.java` de teste (`Java/test`), `.kt` (`Kotlin/src`) | UTF-8 (o compilador de testes e o Kotlin leem UTF-8; converter para Latin-1 corrompe os acentos) |
| `.sql`, `.jrxml`, `.html`, `.js`, `.css`, `.json` | UTF-8 |

---

## Como o encoding e garantido

1. **Mod `sankhya-encoding` (edicao):** em volta de cada Read, Edit e Write, converte o `.java` ISO para UTF-8 logo antes da ferramenta e de volta para ISO-8859-1 logo depois. O arquivo so fica em UTF-8 durante a chamada, inclusive em subagent. Respeita o `.editorconfig` (`charset = utf-8` tira o arquivo do tratamento).
2. **Task `verificar-encoding-<demanda>` no `build.gradle`:** so nos projetos criados do projeto modelo (snippet para projetos existentes em `references/verificacao-encoding-build.md`). Quebra o build se houver U+FFFD, arquivo misto ou encoding fora do padrao.
3. **Skill `sankhya-commit`:** confere o encoding dos arquivos em stage antes do commit.

**Nao converta manualmente** (python/iconv) um arquivo coberto pelo mod. Ele ja converte, e uma segunda conversao gera arquivo misto.

### Arquivo ISO fora da cobertura do mod

O mod trata `.java` e apenas os XMLs em `datadictionary/`, `dbscripts/`, `dbquerys/` e `dashboards/`. XML do Construtor de Telas em outra pasta, `.properties` ou outro arquivo ISO-8859-1 (confira os vizinhos com `file --mime-encoding`): nao use Edit/Write. Leia e grave em Latin-1, sem `errors=`, para que um caractere fora do Latin-1 de erro em vez de sumir:

```bash
python3 - <<'PY'
p = "caminho/tela.xml"
s = open(p, encoding="iso-8859-1").read()
s = s.replace("ALVO", "NOVO")
open(p, "w", encoding="iso-8859-1").write(s)
PY
```

---

## Verificar encoding de um arquivo

```bash
file --mime-encoding NomeArquivo.java
# Esperado: iso-8859-1 (ou us-ascii, se nao houver acento)
LC_ALL=C grep -l $'\xef\xbf\xbd' NomeArquivo.java || echo "OK sem U+FFFD"
```

Se o mod acusar U+FFFD, corrija o caractere na origem. Nao force a gravacao.

---

## Cabecalho obrigatorio em XMLs do Construtor de Telas

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
```

Nunca alterar para `UTF-8` mesmo que o editor sugira.

---

## Caracteres especiais em Java

**Escrever acentos diretamente** no fonte. **Proibido** usar escapes Unicode (`ã`, `ç` etc.) em `.java` ou `.xml`: mascaram o encoding real e confundem a manutencao.

Sem emoji nem caractere fora do Latin-1 em fonte ISO. Pontuacao tipografica comum (travessao, aspas curvas, reticencias) o mod translitera para ASCII; o resto vira `?`.

---

## Anti-patterns

| Errado | Correto |
|:-------|:--------|
| Salvar `.java` de fonte / XML de tela em UTF-8 | ISO-8859-1 |
| Converter `.kt` ou `.java` de teste para ISO-8859-1 | UTF-8 |
| Regravar com python/iconv arquivo coberto pelo mod | Read/Edit/Write normais |
| `errors='ignore'` ou `errors='replace'` na conversao | Sem `errors=`: falhar e corrigir o caractere |
| XML sem cabecalho `encoding="ISO-8859-1"` | Cabecalho obrigatorio em todo XML de tela |
