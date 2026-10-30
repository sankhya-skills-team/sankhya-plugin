---
applyTo: "**/*.java,**/*.xml"
---

# Codificacao de Arquivos — Addon Studio 2.0

Fontes `.java` e XMLs de artefato em projetos Addon Studio **ficam em ISO-8859-1 (Latin-1)**. O mod `sankhya-encoding` do plugin cuida da conversao: use Read/Edit/Write normalmente.

---

## Por que ISO-8859-1

O servidor Sankhya (Wildfly legado) e o compilador de addons esperam Latin-1. Arquivo salvo em UTF-8 causa corrupção de acentos e falha silenciosa em runtime.

---

## Regras

| Tipo de arquivo | Encoding |
|:----------------|:---------|
| `.java` de fonte | ISO-8859-1. Acentos literais. |
| `.xml` em `datadictionary/`, `dbscripts/`, `dbquerys/`, `dashboards/` | ISO-8859-1. Cabecalho **obrigatorio**: `<?xml version="1.0" encoding="ISO-8859-1" ?>` |
| `.java` de teste, `.kt` | UTF-8 (o compilador de testes e o Kotlin leem UTF-8; converter para Latin-1 corrompe os acentos) |
| `.sql`, `.jrxml`, `.jsp`, `.html`, `.js`, `.css`, `.json` | UTF-8 |

---

## Como o encoding e garantido

1. **Mod `sankhya-encoding` (edicao):** em volta de cada Read, Edit e Write, converte o arquivo ISO para UTF-8 logo antes da ferramenta e de volta para ISO-8859-1 logo depois. O arquivo so fica em UTF-8 durante a chamada, inclusive em subagent. Respeita o `.editorconfig` (`charset = utf-8` tira o arquivo do tratamento).
2. **Task `verificar-encoding-<demanda>` no `build.gradle`:** so nos projetos criados do projeto modelo. Quebra o build se houver U+FFFD, arquivo misto ou encoding fora do padrao.
3. **Skill `sankhya-commit`:** confere o encoding dos arquivos em stage antes do commit.

**Nao converta manualmente** (python/iconv) um arquivo coberto pelo mod. Ele ja converte, e uma segunda conversao gera arquivo misto.

### Arquivo ISO fora da cobertura do mod

O mod so trata `.java` e os XMLs das pastas acima. Arquivo ISO-8859-1 fora disso (ex.: `.properties`, XML em outra pasta; confira os vizinhos com `file --mime-encoding`): nao use Edit/Write. Leia e grave em Latin-1, sem `errors=`, para que um caractere fora do Latin-1 de erro em vez de sumir:

```bash
python3 - <<'PY'
p = "caminho/arquivo.properties"
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

## Cabecalho obrigatorio em XMLs

Todo XML de artefato criado ou modificado **deve manter**:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
```

Nunca alterar para `UTF-8` mesmo que editor sugira.

---

## Caracteres especiais em Java

**Escrever acentos diretamente** no fonte. **Proibido** usar escapes Unicode (`ã`, `ç` etc.) em `.java` ou `.xml`: mascaram o encoding real e confundem a manutencao.

Sem emoji nem caractere fora do Latin-1 em fonte ISO. Pontuacao tipografica comum (travessao, aspas curvas, reticencias) o mod translitera para ASCII; o resto vira `?`.

---

## Anti-patterns

| Errado                                              | Correto                                         |
|:----------------------------------------------------|:------------------------------------------------|
| Salvar `.java` de fonte / XML de artefato em UTF-8  | ISO-8859-1 (o mod converte)                    |
| Converter `.kt` ou `.java` de teste para ISO-8859-1 | UTF-8                                           |
| Regravar com python/iconv arquivo coberto pelo mod | Read/Edit/Write normais                         |
| `errors='ignore'` ou `errors='replace'` na conversao | Sem `errors=`: falhar e corrigir o caractere   |
| XML sem cabecalho `encoding="ISO-8859-1"`           | Cabecalho obrigatorio em todo XML de artefato   |
