# SDK Sankhya — Adaptadores de Tipos

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Visão Geral

Adaptadores de tipo convertem valores entre formatos JSON, objetos Java e valores compatíveis com o Jape. Use quando precisar de tipos não suportados nativamente pelo SDK ou pelo Gson.

---

## Adaptadores Globais (Customizados)

Anote a classe com `@GlobalTypeAdapter`. Pode implementar uma ou mais interfaces:

| Interface | Finalidade |
|---|---|
| `TypeAdapter<T>` | Converte entre tipo Java e valor Jape (`fromVO` / `toVO`) |
| `JsonSerializer<T>` | Define como o tipo é serializado para JSON |
| `JsonDeserializer<T>` | Define como o tipo é desserializado do JSON |

```java
@GlobalTypeAdapter
public class ZonedDateTimeAdapter
        implements JsonSerializer<ZonedDateTime>, TypeAdapter<ZonedDateTime>, JsonDeserializer<ZonedDateTime> {

    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ISO_OFFSET_DATE_TIME;

    @Override
    public ZonedDateTime fromVO(Object o) {
        if (o == null) return null;
        return ((Timestamp) o).toInstant().atZone(ZoneId.systemDefault());
    }

    @Override
    public Object toVO(ZonedDateTime zonedDateTime) {
        if (zonedDateTime == null) return null;
        return Timestamp.from(zonedDateTime.toInstant());
    }

    @Override
    public void setType(Class<? extends ZonedDateTime> aClass) {}

    @Override
    public ZonedDateTime deserialize(JsonElement json, Type type, JsonDeserializationContext ctx) throws JsonParseException {
        return ZonedDateTime.parse(json.getAsString(), FORMATTER);
    }

    @Override
    public JsonElement serialize(ZonedDateTime value, Type type, JsonSerializationContext ctx) {
        return new JsonPrimitive(FORMATTER.format(value));
    }
}
```

> Adaptadores globais têm precedência sobre os nativos.

---

## Adaptadores Nativos (Built-in)

Aplicados automaticamente quando não há adaptador customizado registrado.

| Adapter | Tipo Java | Tipo Jape/VO | Observações |
|---|---|---|---|
| `BooleanAdapter` | `Boolean` | `String ("S"/"N")` | Lê 'S' como `true`; escreve `"S"`/`"N"` |
| `ByteArrayAdapter` | `byte[]` | `Blob`, `InputStream`, `byte[]` | — |
| `CharArrayAdapter` | `char[]` | `String`, `Clob` | — |
| `DateAdapter` | `LocalDate`, `LocalDateTime`, `LocalTime` | `Timestamp` | Tipo exato depende de `setType` |
| `DurationAdapter` | `Duration` | `String ISO-8601` ou segundos | `toVO` retorna ISO; `fromVO` aceita ISO ou segundos |
| `EnumAdapter` | `Enum<?>` | `String`/`Number` | Usa `getValue()` se existir, senão `name()` |
| `HashValueAdapter` | `HashValue` | `String "ALGORITHM:hex"` | Ex: `"SHA-256:a665..."` |
| `InputStreamAdapter` | `InputStream` | `Blob`, `byte[]` | — |
| `InstantAdapter` | `Instant` | `String ISO-8601` ou epoch millis | — |
| `JsonElementAdapter` | `JsonElement` | `String JSON` | Strings vazias → `JsonObject` vazio |
| `JsonObjectAdapter` | `JsonObject` | `String JSON (objeto)` | Exige JSON de objeto |
| `NumberAdapter` | `int`, `long`, `double`, `BigDecimal`, etc. | `BigDecimal` | Converte para o tipo numérico do campo |
| `PeriodAdapter` | `Period` | `String ISO-8601 (P...)` | — |
| `URLAdapter` | `URL` | `String` | Valida e normaliza URLs |
| `UUIDAdapter` | `UUID` | `String` canônico ou `byte[16]` | — |

---

## Fonte

https://developer.sankhya.com.br/docs/%EF%B8%8F-adaptadores-de-tipos
