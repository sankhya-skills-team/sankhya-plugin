# XMLUtils

**Pacote:** `com.sankhya.util.XMLUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.XMLUtils;
import org.jdom.Element;
import org.jdom.Document;
```

> **Atenção crítica:** tipo usado é `org.jdom.Element` (JDOM 1.x), **não** `org.w3c.dom.Element` (W3C DOM).
> Importar `org.w3c.dom` causa `ClassCastException` em runtime.

---

## Parse de String/Stream para Document/Element

```java
// String XML → Document
Document doc = XMLUtils.buildDocumentFromString(xmlString);          // throws Exception
Document doc2 = XMLUtils.buildDocumentFromString(xmlString, false);  // validar DTD

// InputStream → Document
Document doc3 = XMLUtils.buildDocumentFromStream(inputStream);       // throws Exception

// String XML → Element raiz diretamente
Element el = XMLUtils.stringToElement(xmlString);                    // throws Exception

// Document/Element → String
String xmlStr  = XMLUtils.documentToString(doc);   // throws Exception
String xmlStr2 = XMLUtils.elementToString(el);     // throws Exception
String xmlStr3 = XMLUtils.documentToString(doc, "UTF-8");
```

---

## Ler atributos de Element

```java
// Retorna null se atributo ausente
String codigo    = XMLUtils.getAttributeAsString(el, "CODPROD");
BigDecimal preco = XMLUtils.getAttributeAsBigDecimal(el, "VLRUNIT");
boolean ativo    = XMLUtils.getAttributeAsBoolean(el, "ATIVO");
Timestamp data   = XMLUtils.getAttributeAsTimestamp(el, "DTENT");

// Lança exceção se atributo ausente (required)
String codReq    = XMLUtils.getRequiredAttributeAsString(el, "CODPROD");   // throws Exception
BigDecimal precoR = XMLUtils.getRequiredAttributeAsBigDecimal(el, "VLRUNIT"); // throws Exception
Timestamp dataR  = XMLUtils.getRequiredAttributeAsTimestamp(el, "DTENT");  // throws Exception

// Atributo zero-safe
BigDecimal precoZ = XMLUtils.getAttributeAsBigDecimalOrZero(el, "VLRUNIT"); // null → zero
```

---

## Ler conteúdo de texto de Element

```java
// Conteúdo do próprio Element
String texto     = XMLUtils.getContentAsString(el);
BigDecimal val   = XMLUtils.getContentAsBigDecimal(el);
Boolean flag     = XMLUtils.getContentAsBoolean(el);
Timestamp ts     = XMLUtils.getContentAsTimeStamp(el);

// Conteúdo de filho por nome (child element text)
String textoFilho = XMLUtils.getContentChildAsString(el, "DESCRICAO");
BigDecimal valF   = XMLUtils.getContentChildAsBigDecimal(el, "VLRTOTAL");
Boolean flagF     = XMLUtils.getContentChildAsBoolean(el, "ATIVO");
Timestamp tsF     = XMLUtils.getContentChildAsTimeStamp(el, "DTENT");

// Required versions — lançam exceção se ausente/nulo
String req   = XMLUtils.getRequiredContentAsString(el);
String reqF  = XMLUtils.getRequiredContentChildAsString(el, "CAMPO");
BigDecimal reqBD = XMLUtils.getRequiredContentChildAsBigDecimal(el, "VALOR");
```

---

## Navegar filhos

```java
// Obter filho por nome (retorna null se ausente)
Element filho = XMLUtils.getChild(el, "ITENS");                        // throws Exception
Element filho2 = XMLUtils.getChild(el, "nsPrefixo", "ITENS");         // com namespace

// Required — lança exceção se ausente
Element req   = XMLUtils.getRequiredChild(el, "ITENS");                // throws Exception
Element req2  = XMLUtils.getRequiredChild(el, "nsPrefixo", "ITENS");

// Iterar filhos com callback
XMLUtils.iterateOnChildren("ITEM", el, (itemEl) -> {
    String cod = XMLUtils.getAttributeAsString(itemEl, "CODPROD");
    // processar cada ITEM
}); // throws Exception

// Coleções de conteúdo de filhos
Collection<String> nomes  = XMLUtils.getChildrenContentAsStringCollection(el, "NOME");
Collection<BigDecimal> vals = XMLUtils.getChildrenContentAsBigDecimalCollection(el, "VALOR");
```

---

## Escrever/modificar Element

```java
// Setar atributo
XMLUtils.setAttibuteValue(el, "STATUS", "PROCESSADO");         // Object → String
XMLUtils.setAttibuteValueIfNotEmpty(el, "OBS", obs);           // só se não vazio
XMLUtils.setAttibuteIfNotEmpty(el, "OBS", (String) obs);       // String overload

// Adicionar filho com atributo
XMLUtils.addAttributeElement(el, "ITEM", valor);               // <ITEM valor="..."/>

// Adicionar filho com conteúdo de texto
XMLUtils.addContentElement(el, "DESCRICAO", "Produto A");      // <DESCRICAO>Produto A</DESCRICAO>
XMLUtils.addContentElement(el, "CAMPO", resultSet);            // throws Exception

// Adicionar CDATA (para HTML ou XML embutido)
XMLUtils.addCDATAContentElement(el, "HTML", conteudoHtml);     // throws Exception
XMLUtils.addCDATAContentElementIfNotEmpty(el, "OBS", obs);

// Texto direto no Element
XMLUtils.setText(el, "conteudo");
```

---

## Serializar para OutputStream

```java
// Document → OutputStream
XMLUtils.writeToStream(doc, outputStream);                    // throws Exception
XMLUtils.writeToStream(doc, outputStream, "ISO-8859-1");

// Element → OutputStream
XMLUtils.writeToStream(el, outputStream);                     // throws Exception
```

---

## Validação

```java
boolean xmlValido = XMLUtils.isXMLValid(xmlString);
String  seguro    = XMLUtils.escapeInvalidXMLChars(xmlString);
String  limpo     = XMLUtils.keepingValidXMLChars(xmlString);
```

---

## Antipadrões

```java
// ERRADO — tipo errado
import org.w3c.dom.Element; // incompatível com XMLUtils
// CORRETO
import org.jdom.Element;

// ERRADO — set com typo inventado
element.setAttribute("STATUS", "X");
// CORRETO — método real tem typo no JAR: setAttibuteValue (dois t)
XMLUtils.setAttibuteValue(element, "STATUS", "X");

// ERRADO — get sem null check
element.getChild("ITENS").getText()  // NullPointerException se ausente
// CORRETO
XMLUtils.getRequiredChild(element, "ITENS"); // lança exceção descritiva
```
