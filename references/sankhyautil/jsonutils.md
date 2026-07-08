# JsonUtils

**Pacote:** `com.sankhya.util.JsonUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.JsonUtils;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
```

> **Atenção crítica:** tipo usado é `com.google.gson.JsonObject` (Gson), **não** `javax.json.JsonObject` (Jakarta).
> Importar `javax.json` causa `ClassCastException` em runtime.

---

## Extrair campos de JsonObject

```java
JsonObject params = /* recebido via requisição */;

// Retorna null se ausente
String codigo       = JsonUtils.getString(params, "codigo");
BigDecimal valor    = JsonUtils.getBigDecimal(params, "valor");
BigDecimal valorZ   = JsonUtils.getBigDecimalOrZero(params, "valor"); // null → zero
int qtd             = JsonUtils.getInt(params, "quantidade");
Boolean ativo       = JsonUtils.getBoolean(params, "ativo");
Timestamp data      = JsonUtils.getTimestamp(params, "dataEntrega");
JsonObject filho    = JsonUtils.getJsonObject(params, "endereco");
JsonArray itens     = JsonUtils.getJsonArray(params, "itens");
JsonElement el      = JsonUtils.getJsonElement(params, "campo");

// Lança exceção se ausente (required)
String cod      = JsonUtils.getRequiredString(params, "codigo");
BigDecimal vlr  = JsonUtils.getRequiredBigDecimal(params, "valor");
int n           = JsonUtils.getRequiredInt(params, "quantidade");
JsonObject obj  = JsonUtils.getRequiredJsonObject(params, "endereco");
```

---

## Construir/popular JsonObject

```java
JsonObject obj = new JsonObject();

// Adiciona propriedade (aceita String, Number, Boolean, JsonElement)
JsonUtils.addProperty(obj, "status", "PROCESSADO");
JsonUtils.addProperty(obj, "valor", BigDecimal.TEN);

// Adiciona somente se não nulo/vazio
JsonUtils.addPropertyIfNotEmpty(obj, "obs", vo.asString("OBS"));
JsonUtils.addJsonObjectIfNotEmpty(obj, "endereco", endObj);
JsonUtils.addChildIfNotEmpty(obj, "itens", itensObj);
```

---

## Parse / serialização

```java
// String JSON → JsonObject/JsonArray
JsonObject fromStr  = JsonUtils.convertStringToJsonObject("{\"cod\":1}");
JsonArray fromStr2  = JsonUtils.convertStringToJsonArray("[1,2,3]");
JsonElement el      = JsonUtils.parserString(jsonStr);

// JsonElement → tipado
JsonObject obj2  = JsonUtils.parseJsonObject(element);
JsonArray arr2   = JsonUtils.parseJsonArray(element);

// Objeto Java → String JSON
String json = JsonUtils.converteObjectToString(minhaClasse);

// Gson configurado pela Sankhya (usa para serializar/deserializar)
com.google.gson.Gson gson = JsonUtils.getGson();
```

---

## Deserializar para POJO

```java
// JsonObject → instância de classe (usa Gson internamente)
MinhaClasse obj = JsonUtils.wrap(jsonObject, MinhaClasse.class);

// JsonArray → List<MinhaClasse>
List<MinhaClasse> lista = JsonUtils.wrap(jsonArray, MinhaClasse.class);
```

---

## Trabalhar com ResultSet

```java
// Converte linha atual do ResultSet em JsonObject
JsonObject row = JsonUtils.buildJsonObjectFromResultSet(rs);          // throws Exception
JsonObject row2 = JsonUtils.buildJsonObjectFromResultSet("prefixo", rs); // throws Exception
```

---

## Extrair coleções de JsonArray

```java
// Extrai valores de campo de cada item do array
Collection<String> nomes   = JsonUtils.getChildrenAsStringCollection(params, "nomes");
Collection<BigDecimal> vals = JsonUtils.getChildrenAsBigDecimalCollection(params, "valores");

// A partir de JsonArray diretamente
List<JsonObject> objList = JsonUtils.getJsonObjectList(jsonArray); // throws Exception
```

---

## Verificações

```java
boolean vazio = JsonUtils.isEmpty(jsonObject); // null ou sem campos

// Acesso seguro em array por índice
JsonElement item    = JsonUtils.getSafeValueIndex(jsonArray, 2); // null se fora de range
String itemStr      = JsonUtils.getSafeValueIndexAsString(jsonArray, 0);
```

---

## Antipadrões

```java
// ERRADO — tipo errado
import javax.json.JsonObject; // causa ClassCastException
// CORRETO
import com.google.gson.JsonObject;

// ERRADO — parse manual
JsonObject obj = new JsonParser().parse(str).getAsJsonObject();
// CORRETO
JsonObject obj = JsonUtils.convertStringToJsonObject(str);

// ERRADO — get sem null-check
String cod = params.get("codigo").getAsString(); // NullPointerException se ausente
// CORRETO
String cod = JsonUtils.getString(params, "codigo");       // null se ausente
String cod = JsonUtils.getRequiredString(params, "codigo"); // exceção se ausente
```
