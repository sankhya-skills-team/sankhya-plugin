# StringUtils

**Pacote:** `com.sankhya.util.StringUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.StringUtils;
```

---

## Verificações null/vazio

```java
// null-safe: trata null e "" como vazio
boolean vazio    = StringUtils.isEmpty(vo.asString("CAMPO"));   // Object ou String
boolean temValor = StringUtils.isNotEmpty(vo.asString("EMAIL")); // Object

// retorna null se vazio ou nulo — útil para gravar null no banco
String valor = StringUtils.getEmptyAsNull(vo.asString("OBS"));   // Object ou String

// retorna "" se nulo — útil para concatenação segura
String desc  = StringUtils.getNullAsEmpty(vo.asString("DESC"));  // Object ou String

// retorna segundo param se primeiro for null/vazio
String s = StringUtils.getValueOrDefault(vo.asString("CAMPO"), "padrao");

// comparação null-safe
boolean igual     = StringUtils.safelyEquals(a, b);            // Object ou String
boolean igualCI   = StringUtils.safelyEqualsIgnoreCase(a, b);  // String
boolean contem    = StringUtils.safeContains(texto, trecho);
boolean inicia    = StringUtils.safeStartsWith(texto, prefixo);
```

---

## Formatação de documentos e campos

```java
String cnpj  = StringUtils.formataCgcCpf("12345678000195");  // formata CNPJ ou CPF
String cep   = StringUtils.formataCep("01310100");
String cfop  = StringUtils.formataCfop("5102", 4);
String tel   = StringUtils.formataTelefone("11912345678");
String placa = StringUtils.formataPlaca("ABC1234");

// Converter para formato oficial
String cnpjF = StringUtils.toCNPJ("12345678000195"); // throws IllegalArgumentException
String cpfF  = StringUtils.toCPF("12345678901");     // throws IllegalArgumentException

// apenas números (remove pontuação/letras)
String nums  = StringUtils.onlyNumber("(11) 912-3456"); // throws Exception
boolean soNum = StringUtils.isNumeric("12345");
String semPont = StringUtils.removePontuacao("ABC-123.DEF");
```

---

## Manipulação de strings

```java
// substituição (static, não regex)
String sql  = StringUtils.replaceString(template, ":PARCEIRO", nuParc.toString());
// substituição regex
String res  = StringUtils.replaceAll(texto, "\\s+", " ");
String res2 = StringUtils.replaceLast(texto, "OLD", "NEW");

// left/right/substring seguro
String ini  = StringUtils.left(obj, 5);                     // Object
String fim  = StringUtils.right(obj, 3);                    // Object
String sub  = StringUtils.secureSubstring(texto, 0, 10);    // não lança IndexOutOfBounds
String lim  = StringUtils.limitSize(texto, 100);            // trunca em 100 chars

// trim especializado
String t    = StringUtils.trim(texto);
String rt   = StringUtils.rtrim(texto);
String lt   = StringUtils.ltrim(texto);

// padding
String pad  = StringUtils.padl(obj, 10, '0');  // "0000000123"
String padr = StringUtils.padr(obj, 10, ' ');  // "123       "
String padc = StringUtils.padc(obj, 10, '-');  // "---123----"

// replicar caractere/string
String rep  = StringUtils.replicate("AB", 3);  // "ABABAB"
```

---

## Acentuação e caracteres especiais

```java
String semAcento    = StringUtils.replaceAccentuatedChars(texto);    // remove acentos
String semEspecial  = StringUtils.onlyStringWithoutAccent(texto);    // alfanum sem acento
boolean temEspecial = StringUtils.hasSpecialCharacter(texto);
String nomeArq      = StringUtils.normalizeFileName(texto);          // seguro p/ sistema de arquivos
String valido       = StringUtils.getValidFileName(texto);
```

---

## SQL e escaping

```java
// duplica aspas simples — escape para SQL Oracle
String sqlSafe = StringUtils.duplicarAspasSimples(valorUsuario);

// HTML
String html    = StringUtils.htmlScape(texto);
String sem     = StringUtils.reverseHtmlScape(texto);
String url     = StringUtils.urlScape(texto);

// boolean string
boolean b = StringUtils.toBoolean("S"); // "S","s","true","1","yes" → true
```

---

## Coleções como String

```java
// Collection → "val1,val2,val3"
String csv = StringUtils.getCollectionCommaSeparated(colecao);

// "val1,val2,val3" → Collection<String>
Collection<String> col = StringUtils.commaSeparetedToCollection(csv);

// Object[] com separador customizado
String joined = StringUtils.joinArray(arr, ", ");
String joined2 = StringUtils.join(arr, " | ");
```

---

## CLOB

```java
// ler campo CLOB do ResultSet como String
String conteudo = StringUtils.getClobFromStream(rs, "CAMPO_CLOB"); // throws Exception
String c2       = StringUtils.clobAsString(clob);                  // throws Exception
```

---

## Debug

```java
// stacktrace como String (para logar exceção no banco/arquivo)
String stack = StringUtils.parseStackTraceToString(e);
```

---

## Antipadrões

```java
// ERRADO
if (str == null || str.trim().isEmpty()) { ... }
// CORRETO
if (StringUtils.isEmpty(str)) { ... }

// ERRADO — escape SQL manual
"WHERE NOME = '" + nome + "'"
// CORRETO
"WHERE NOME = '" + StringUtils.duplicarAspasSimples(nome) + "'"
```
