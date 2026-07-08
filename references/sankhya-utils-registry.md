<system_instruction>
Sempre responda em PORTUGUESE (PT-BR).
</system_instruction>

# Sankhya Util Library — com.sankhya.util

**Rule:** Before accepting any manual validation, null-check, formatting or conversion code, check this index for an equivalent utility. If it exists, use it.

Source of truth: `$SANKHYAW_REPO_PATH/SankhyaUtil/src/com/sankhya/util/`

## Available classes

| Class | Purpose |
|-------|---------|
| `BigDecimalUtil` | Null-safe BigDecimal: conversions, rounding, zero-defaults |
| `StringUtils` | String validations (isEmpty, isNotEmpty, getEmptyAsNull), formatting |
| `ObjectUtils` | Null-safe comparison between heterogeneous objects |
| `CollectionUtils` | Null/empty collection checks, split, transform |
| `ListUtils` | Split lists into batches, ResultSet → List<Map> |
| `MapUtils` | Null/empty map checks, key lookup |
| `WrapperUtils` | Null-safe Boolean unboxing |
| `DateUtils` | Date diff, zero hour, interval check |
| `JdbcUtils` | Safe close of ResultSet, Statement, Connection |
| `ComparationUtils` | SankhyaOm and SankhyaNFe version comparison |

## Quick substitution table

| Manual code | Utility equivalent |
|-------------|-------------------|
| `qtd != null && qtd > 0` | `BigDecimalUtil.getIntOrZero(qtd) > 0` |
| `value == null \|\| value.compareTo(BigDecimal.ZERO) == 0` | `BigDecimalUtil.isEmpty(value)` |
| `value != null ? value : BigDecimal.ZERO` | `BigDecimalUtil.getValueOrZero(value)` |
| `str == null \|\| str.trim().isEmpty()` | `StringUtils.isEmpty(str)` |
| `str != null && !str.trim().isEmpty()` | `StringUtils.isNotEmpty(str)` |
| `str != null ? str.trim() : null` | `StringUtils.getEmptyAsNull(str)` |
| `str != null ? str : ""` | `StringUtils.getNullAsEmpty(str)` |
| `s1 != null && s1.equals(s2)` | `StringUtils.safelyEquals(s1, s2)` |
| `o1 != null && o1.equals(o2)` | `ObjectUtils.safelyEquals(o1, o2)` |
| `lista == null \|\| lista.isEmpty()` | `CollectionUtils.isEmpty(lista)` |
| `map == null \|\| map.isEmpty()` | `MapUtils.isEmpty(map)` |
| `boolObj != null && (Boolean) boolObj` | `WrapperUtils.getBooleanOrFalse(boolObj)` |
| `(d2.getTime() - d1.getTime()) / 86400000` | `DateUtils.diffDatesDays(d1, d2)` |
| `try { rs.close() } catch...` in finally | `JdbcUtils.closeResultSet(rs)` |

## BigDecimalUtil — `import com.sankhya.util.BigDecimalUtil;`

| Method | Signature | Replaces |
|--------|-----------|---------|
| `getIntOrZero` | `(Integer value) : int` | `qtd != null && qtd > 0` |
| `getValueOrZero` | `(BigDecimal value) : BigDecimal` | `value != null ? value : BigDecimal.ZERO` |
| `isEmpty` | `(BigDecimal value) : boolean` | null or zero check |
| `isNullOrZero` | `(BigDecimal arg) : boolean` | semantic alias of `isEmpty` |
| `safelyEquals` | `(BigDecimal v1, BigDecimal v2) : boolean` | null-safe compareTo |
| `getValue` | `(BigDecimal value, BigDecimal default) : BigDecimal` | null-safe with default |
| `getBigDecimalOrZero` | `(Object value) : BigDecimal` | null-safe Object cast |
| `getBigDecimal` | `(Object value) : BigDecimal` | null-safe cast (null if null) |
| `getRounded` | `(BigDecimal value, int scale) : BigDecimal` | HALF_UP rounding |
| `truncate` | `(BigDecimal value, int scale) : BigDecimal` | ROUND_DOWN truncation |
| `divide` | `(BigDecimal dividend, BigDecimal divider) : BigDecimal` | safe division, scale 2 |
| `porcentagem` | `(BigDecimal parte, BigDecimal todo) : BigDecimal` | percentage calculation |
| `toCurrency` | `(BigDecimal value) : String` | format as currency `#,##0.00` |
| `max` / `min` | `(BigDecimal a, BigDecimal b) : BigDecimal` | null-safe max/min |

Constants: `BigDecimalUtil.ZERO_VALUE`, `BigDecimalUtil.CEM_VALUE`

## StringUtils — `import com.sankhya.util.StringUtils;`

| Method | Signature | Replaces |
|--------|-----------|---------|
| `isEmpty` | `(String s) : boolean` | `str == null \|\| str.trim().isEmpty()` |
| `isNotEmpty` | `(Object s) : boolean` | negation of isEmpty |
| `getEmptyAsNull` | `(String s) : String` | returns null if blank, trims |
| `getNullAsEmpty` | `(String arg0) : String` | `str != null ? str : ""` |
| `safelyEquals` | `(String s1, String s2) : boolean` | null-safe equals |
| `safelyEqualsIgnoreCase` | `(String s1, String s2) : boolean` | null-safe case-insensitive |
| `formataCgcCpf` | `(String cgccpf) : String` | format CPF (11 digits) or CNPJ (14 digits) |
| `formataCep` | `(String cep) : String` | format CEP `##.###-###` |
| `convertToBigDecimal` | `(String s) : BigDecimal` | string with/without punctuation → BigDecimal |
| `getCollectionCommaSeparated` | `(Collection<?> col) : String` | join with comma |
| `replaceAccentuatedChars` | `(String text) : String` | remove accents |
| `left` / `right` | `(Object value, int count) : String` | first/last N chars |
| `padl` / `padr` / `padc` | `(Object value, int width) : String` | left/right/center align |

## CollectionUtils — `import com.sankhya.util.CollectionUtils;`

| Method | Signature |
|--------|-----------|
| `isEmpty` | `(Collection c) : boolean` |
| `isNotEmpty` | `(Collection c) : boolean` |
| `splitList` | `(List<BigDecimal> list, int size) : Collection<Collection<BigDecimal>>` |
| `inArray` | `(String needle, String[] haystack) : boolean` (case-insensitive) |

## DateUtils — `import com.sankhya.util.DateUtils;`

| Method | Signature |
|--------|-----------|
| `diffDatesDays` | `(Date d1, Date d2) : long` |
| `diffDatesHours` | `(Date d1, Date d2) : long` |
| `diffDatesMinutes` | `(Date d1, Date d2) : long` |
| `zeraHora` | `(Date date) : void` (mutable) |
| `checkIfDateIsBetweenTwoDates` | `(Date dtStart, Date dtEnd, Date dtTarget) : boolean` |

## JdbcUtils — `import com.sankhya.util.JdbcUtils;`

| Method | Signature |
|--------|-----------|
| `closeResultSet` | `(ResultSet rset) : void` |
| `closeStatement` | `(Statement st) : void` |
| `closeConnection` | `(Connection conn) : void` |

## MapUtils — `import com.sankhya.util.MapUtils;`

| Method | Signature |
|--------|-----------|
| `isEmpty` | `(Map map) : boolean` |
| `isNotEmpty` | `(Map map) : boolean` |
| `containsSomeKey` | `(Object[] keys, Map targetMap) : boolean` |
| `containsAllKeys` | `(Collection keys, Map targetMap) : boolean` |
| `getMapValueAsBigDecimal` | `(Map map, String key) : BigDecimal` |
| `getMapValueAsTimestamp` | `(Map map, String key) : Timestamp` |
| `getMapValueAsString` | `(Map map, String key) : String` |

> **Warning:** `getMapValue*` methods do **cast**, not conversion. A String `"123"` in `getMapValueAsBigDecimal()` throws `ClassCastException`.

## WrapperUtils — `import com.sankhya.util.WrapperUtils;`

| Method | Signature |
|--------|-----------|
| `getBooleanOrFalse` | `(Object boolObj) : boolean` |

## ObjectUtils — `import com.sankhya.util.ObjectUtils;`

| Method | Signature |
|--------|-----------|
| `safelyEquals` | `(Object o1, Object o2) : boolean` (BigDecimal uses compareTo) |
