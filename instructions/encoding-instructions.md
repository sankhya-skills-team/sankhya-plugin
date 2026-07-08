---
applyTo: "**/*.java,**/*.xml"
---

# Codificacao de Arquivos — Modulo Java Sankhya

> **REGRA CRITICA — SEM EXCECOES**

Todo arquivo `.java` e `.xml` em projetos de modulo Java Sankhya **deve ser salvo em ISO-8859-1 (Latin-1)**.

---

## Por que ISO-8859-1

O servidor Sankhya (Wildfly legado) e o compilador Java do modulo esperam Latin-1. Arquivo salvo em UTF-8 causa corrupcao de acentos e falha silenciosa em runtime. Isso vale para `.java` e para os XMLs do Construtor de Telas.

---

## Regras

| Tipo de arquivo | Regra |
|:----------------|:------|
| `.java` | Salvo em ISO-8859-1. Acentos diretamente no encoding. |
| `.xml` (Construtor de Telas) | Salvo em ISO-8859-1. Cabecalho **obrigatorio**: `<?xml version="1.0" encoding="ISO-8859-1" ?>` |

---

## O problema com LLMs

LLMs geram arquivos em UTF-8 por padrao. Apos criar ou editar qualquer `.java` ou `.xml`, **converta o encoding** antes de usar.

### Windows — Python3

```python
# Arquivo especifico
python3 -c "
import sys
p = sys.argv[1]
c = open(p, 'r', encoding='utf-8', errors='ignore').read()
open(p, 'w', encoding='iso-8859-1', errors='replace').write(c)
" arquivo.java
```

```python
# Todos os .java e .xml do projeto (rodar na raiz)
python3 -c "
import os, glob
for ext in ('**/*.java', '**/*.xml'):
    for p in glob.glob(ext, recursive=True):
        try:
            c = open(p, 'r', encoding='utf-8').read()
            open(p, 'w', encoding='iso-8859-1', errors='replace').write(c)
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
"
```

### Mac / Linux — `iconv`

```bash
# Arquivo especifico
iconv -f UTF-8 -t ISO-8859-1 arquivo.java -o arquivo.java

# Todos os .java e .xml
find . \( -name "*.java" -o -name "*.xml" \) -not -path "*/build/*" \
  -exec sh -c 'iconv -f UTF-8 -t ISO-8859-1 "$1" -o "$1.tmp" && mv "$1.tmp" "$1"' _ {} \;
```

---

## Verificar encoding de um arquivo

```bash
file -i NomeArquivo.java
# Esperado: charset=iso-8859-1
# Problema:  charset=utf-8
```

---

## Cabecalho obrigatorio em XMLs do Construtor de Telas

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
```

Nunca alterar para `UTF-8` mesmo que o editor sugira.

---

## Caracteres especiais em Java

**REGRA ABSOLUTA — SEM EXCECOES:** Escrever acentos **diretamente** no arquivo apos salvar em ISO-8859-1.

**PROIBIDO em qualquer hipotese:** escapes Unicode (`ã`, `ç`, etc.) em arquivos `.java` ou `.xml`.

- Escapes unicode mascaram o encoding real e causam confusao.
- O compilador Java aceita acentos literais em ISO-8859-1 sem necessidade de escapes.

**Fluxo correto:**
1. Gerar o arquivo com acentos literais (LLM gera em UTF-8 com acentos literais).
2. Converter para ISO-8859-1 com Python3 (Windows) ou `iconv` (Mac/Linux).
3. Os acentos permanecem literais, agora em ISO-8859-1.

---

## Anti-patterns

| Errado | Correto |
|:-------|:--------|
| Salvar `.java` / `.xml` em UTF-8 | Sempre ISO-8859-1 |
| XML sem cabecalho `encoding="ISO-8859-1"` | Cabecalho obrigatorio em todo XML |
| Alterar cabecalho XML para `encoding="UTF-8"` | Manter `ISO-8859-1` sem excecao |
| Deixar arquivo gerado por LLM sem converter | Rodar Python3 (Windows) ou `iconv` (Mac/Linux) apos cada criacao/edicao |
