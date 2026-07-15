# SankhyaUtil — Índice de Bibliotecas Utilitárias

Pacote central de utilitários do back-end Sankhya. Disponível em módulos Java e Addon Studio.

> **Todos os pacotes:** `com.sankhya.util.*` (não `br.com.sankhya.util`)
> Verificado via `javap` em `sanutil-4.35.jar`.

---

## Quando usar cada classe

| Classe | Quando usar | Referência |
|---|---|---|
| `StringUtils` | Verificar null/vazio, formatar documentos (CPF/CNPJ/CEP), manipular texto, escape SQL/HTML | `references/sankhyautil/stringutils.md` |
| `TimeUtils` | Manipular datas, timestamps, formatar para exibição, converter parâmetros de ação | `references/sankhyautil/timeutils.md` |
| `SQLUtils` | Montar cláusulas `IN`/`NOT IN` dinâmicas, append AND/OR, escape de aspas | `references/sankhyautil/sqlutils.md` |
| `JsonUtils` | Extrair campos tipados de `JsonObject`/`JsonArray` (Gson) | `references/sankhyautil/jsonutils.md` |
| `XMLUtils` | Ler e escrever atributos/conteúdo em `org.jdom.Element` | `references/sankhyautil/xmlutils.md` |
| `JdbcUtils` | Fechar `ResultSet`/`Statement`/`Connection` com segurança, ler campos tipados | `references/sankhyautil/jdbcutils.md` |
| `BigDecimalUtil` | Arredondamento, divisão segura, porcentagem, null-safe, conversões | `references/sankhyautil/bigdecimalutil.md` |
| `CollectionUtils` | Verificar se coleção está vazia (null-safe), split para batch IN | `references/sankhyautil/collectionutils.md` |
| `SessionFile` | Criar arquivos temporários de sessão (PDF, Excel, etc.) para download | `references/sankhyautil/sessionfile.md` |
| `ListUtils` | Split de lista em lotes, `ResultSet` → `List<Map>` | seção "Utilitários adicionais" abaixo |
| `MapUtils` | Verificar map vazio (null-safe), lookup de chave, ler valor tipado | seção "Utilitários adicionais" abaixo |
| `ObjectUtils` | Comparação null-safe entre objetos heterogêneos | seção "Utilitários adicionais" abaixo |
| `WrapperUtils` | Unboxing null-safe de `Boolean` | seção "Utilitários adicionais" abaixo |
| `ComparationUtils` | Comparação de versão do SankhyaOm / SankhyaNFe | seção "Utilitários adicionais" abaixo |

---

## Armadilhas críticas

| Classe | Armadilha |
|---|---|
| Todas | Pacote é `com.sankhya.util`, não `br.com.sankhya.util` |
| `TimeUtils` | Pacote é `com.sankhya.util.TimeUtils` (confirmar antes de usar) |
| `JdbcUtils` | Nome é `JdbcUtils` (não `JDBCUtils`) |
| `JsonUtils` | Usa `com.google.gson.JsonObject` — **não** `javax.json.JsonObject` |
| `XMLUtils` | Usa `org.jdom.Element` — **não** `org.w3c.dom.Element` |
| `SQLUtils` | Métodos `buildINClause*` exigem nome da coluna como **primeiro parâmetro** |

---

## Antipadrões globais

```java
// ERRADO: verificação null/empty manual
if (str == null || str.trim().isEmpty()) { ... }
// CORRETO
if (StringUtils.isEmpty(str)) { ... }

// ERRADO: IN manual
"NUNOTA IN (" + ids.stream().collect(Collectors.joining(",")) + ")"
// CORRETO
SQLUtils.buildINClauseByValues("NUNOTA", ids)

// ERRADO: não fechar ResultSet
ResultSet rs = stmt.executeQuery(sql); // vaza connection se exceção ocorrer
// CORRETO: usar JdbcUtils.closeResultSet(rs) no finally

// ERRADO: BigDecimal de double direto
new BigDecimal(3.14) // imprecisão de ponto flutuante
// CORRETO
BigDecimalUtil.buildFromDouble(3.14)

// ERRADO: javax.json com JsonUtils
import javax.json.JsonObject; // ClassCastException em runtime
// CORRETO
import com.google.gson.JsonObject;

// ERRADO: org.w3c.dom com XMLUtils
import org.w3c.dom.Element; // ClassCastException em runtime
// CORRETO
import org.jdom.Element;
```

---

## Utilitários adicionais

Classes menores do mesmo pacote `com.sankhya.util`. Antes de escrever comparação,
null-check ou lookup manual, use o equivalente aqui.

### MapUtils — `import com.sankhya.util.MapUtils;`

| Método | Assinatura |
|---|---|
| `isEmpty` | `(Map map) : boolean` |
| `isNotEmpty` | `(Map map) : boolean` |
| `containsSomeKey` | `(Object[] keys, Map targetMap) : boolean` |
| `containsAllKeys` | `(Collection keys, Map targetMap) : boolean` |
| `getMapValueAsBigDecimal` | `(Map map, String key) : BigDecimal` |
| `getMapValueAsTimestamp` | `(Map map, String key) : Timestamp` |
| `getMapValueAsString` | `(Map map, String key) : String` |

> **Atenção:** os `getMapValue*` fazem **cast**, não conversão. Uma `String "123"`
> em `getMapValueAsBigDecimal()` lança `ClassCastException`.

### WrapperUtils — `import com.sankhya.util.WrapperUtils;`

| Método | Assinatura | Substitui |
|---|---|---|
| `getBooleanOrFalse` | `(Object boolObj) : boolean` | `boolObj != null && (Boolean) boolObj` |

### ObjectUtils — `import com.sankhya.util.ObjectUtils;`

| Método | Assinatura | Substitui |
|---|---|---|
| `safelyEquals` | `(Object o1, Object o2) : boolean` (BigDecimal usa `compareTo`) | `o1 != null && o1.equals(o2)` |

### ListUtils — `import com.sankhya.util.ListUtils;`

Split de lista em lotes e conversão `ResultSet` → `List<Map>`. Assinaturas não
confirmadas via `javap` — verificar no jar antes de usar; não inventar método.

### ComparationUtils — `import com.sankhya.util.ComparationUtils;`

Comparação de versão do SankhyaOm e do SankhyaNFe. Assinaturas não confirmadas via
`javap` — verificar no jar antes de usar; não inventar método.
