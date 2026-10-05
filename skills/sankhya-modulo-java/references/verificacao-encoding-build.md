# Verificação de encoding no build (Gradle)

Barreira que impede gerar o JAR com fonte corrompido. Já vem no projeto modelo
`modelo-dstech-customizacoes`; este snippet serve para projetos existentes que não a têm.

## Política

| Pasta | Encoding |
|-------|----------|
| `<demanda>/Java/src` | ISO-8859-1 |
| `<demanda>/Kotlin/src` | UTF-8 (o compilador Kotlin lê fonte em UTF-8) |

A task falha o build quando encontra:
- `U+FFFD` (caractere perdido, não recuperável a partir do arquivo);
- encodings misturados no mesmo arquivo (linhas UTF-8 e ISO-8859-1);
- encoding diferente do padrão da pasta.

## Como aplicar

1. Colar o bloco das tasks **depois** da criação das tasks `gerar-jar-<demanda>` (usa `modulesToBuild`).
2. Colar as funções junto das funções auxiliares do `build.gradle`.
3. Adicionar `.editorconfig` na raiz (IDE e skill de commit usam a mesma política):

```ini
root = true

[**/Java/src/**]
charset = latin1

[**/Kotlin/src/**]
charset = utf-8
```

## Tasks (colar no `build.gradle`)

```groovy
// ==================================================================
// VERIFICAÇÃO DE ENCODING — barreira antes de gerar o JAR
// Java/src em ISO-8859-1, Kotlin/src em UTF-8. Falha o build se houver
// U+FFFD, encodings misturados no mesmo arquivo ou encoding fora do padrão.
// ==================================================================

def ENCODING_LATIN1 = 'ISO-8859-1'
def ENCODING_UTF8 = 'UTF-8'

modulesToBuild.each { moduleName ->
    def verificacao = tasks.register("verificar-encoding-${moduleName}") {
        group = moduleName
        description = "Verificar encoding dos fontes (Java ISO-8859-1, Kotlin UTF-8)"

        doLast {
            def problemas = []
            problemas.addAll(verificarEncodingDaPasta(file("${moduleName}/Java/src"), '**/*.java', ENCODING_LATIN1))
            problemas.addAll(verificarEncodingDaPasta(file("${moduleName}/Kotlin/src"), '**/*.kt', ENCODING_UTF8))

            if (!problemas.isEmpty()) {
                throw new GradleException("Encoding inconsistente na demanda '${moduleName}':\n  " + problemas.join("\n  "))
            }
        }
    }

    // O JAR só é gerado depois da verificação, e a compilação não começa antes dela.
    tasks.named("gerar-jar-${moduleName}") { dependsOn verificacao }
    tasks.matching { it.name == 'compileJava' || it.name == 'compileKotlin' }.configureEach {
        mustRunAfter verificacao
    }
}
```

## Funções auxiliares (colar no `build.gradle`)

```groovy
// --- VERIFICAÇÃO DE ENCODING ---

/**
 * Retorna a lista de problemas de encoding dos arquivos da pasta que casam com o padrão.
 * Pasta inexistente não é problema: nem toda demanda tem Kotlin.
 */
def verificarEncodingDaPasta(File pasta, String padraoArquivos, String encodingEsperado) {
    def problemas = []
    if (!pasta.exists()) return problemas

    fileTree(pasta).matching { include padraoArquivos }.each { arquivo ->
        def conteudo = arquivo.bytes
        def caminho = rootDir.toPath().relativize(arquivo.toPath()).toString().replace(File.separator, '/')

        def substituicoes = contarCaractereSubstituicao(conteudo)
        if (substituicoes > 0) {
            problemas << "${caminho}: U+FFFD x${substituicoes} (caractere perdido; não recuperável a partir do arquivo)"
        }

        def encodingReal = classificarEncoding(conteudo)
        if (encodingReal == 'misto') {
            problemas << "${caminho}: encodings misturados no mesmo arquivo (linhas UTF-8 e ISO-8859-1)"
        } else if (encodingReal != 'ascii' && encodingReal != encodingEsperado) {
            problemas << "${caminho}: esperado ${encodingEsperado}, mas o arquivo está em ${encodingReal}"
        }
    }
    return problemas
}

/** Conta ocorrências da sequência UTF-8 do caractere de substituição (EF BF BD). */
def contarCaractereSubstituicao(byte[] conteudo) {
    int quantidade = 0
    for (int i = 0; i + 2 < conteudo.length; i++) {
        if (conteudo[i] == (byte) 0xEF && conteudo[i + 1] == (byte) 0xBF && conteudo[i + 2] == (byte) 0xBD) {
            quantidade++
        }
    }
    return quantidade
}

/** Retorna 'ascii', 'UTF-8', 'ISO-8859-1' ou 'misto' (linhas UTF-8 válidas e inválidas no mesmo arquivo). */
def classificarEncoding(byte[] conteudo) {
    int linhasUtf8 = 0
    int linhasLatin1 = 0
    int inicio = 0
    for (int i = 0; i <= conteudo.length; i++) {
        if (i < conteudo.length && conteudo[i] != (byte) 10) continue
        def linha = java.util.Arrays.copyOfRange(conteudo, inicio, i)
        inicio = i + 1
        if (!linha.any { it < 0 }) continue
        if (ehUtf8Valido(linha)) linhasUtf8++ else linhasLatin1++
    }
    if (linhasUtf8 > 0 && linhasLatin1 > 0) return 'misto'
    if (linhasUtf8 > 0) return 'UTF-8'
    if (linhasLatin1 > 0) return 'ISO-8859-1'
    return 'ascii'
}

def ehUtf8Valido(byte[] linha) {
    try {
        java.nio.charset.Charset.forName('UTF-8').newDecoder()
            .onMalformedInput(java.nio.charset.CodingErrorAction.REPORT)
            .onUnmappableCharacter(java.nio.charset.CodingErrorAction.REPORT)
            .decode(java.nio.ByteBuffer.wrap(linha))
        return true
    } catch (java.nio.charset.CharacterCodingException ignored) {
        return false
    }
}
```

Rodar isolado: `./gradlew verificar-encoding-<demanda>`. Roda sozinha antes de `gerar-jar-<demanda>`.
