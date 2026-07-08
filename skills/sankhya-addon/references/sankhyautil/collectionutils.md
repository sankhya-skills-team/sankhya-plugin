# CollectionUtils

**Pacote:** `com.sankhya.util.CollectionUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.CollectionUtils;
import java.util.Collection;
import java.util.List;
```

---

## Verificações null-safe

```java
List<DynamicVO> registros = repository.buscarPendentes();

if (CollectionUtils.isEmpty(registros)) {
    throw new MGEModelException("Nenhum registro encontrado.");
}

if (CollectionUtils.isNotEmpty(registros)) {
    registros.forEach(this::processar);
}
```

---

## Verificar se elemento está em array

```java
String[] status = {"ATIVO", "PENDENTE", "BLOQUEADO"};
boolean valido = CollectionUtils.inArray(statusRecebido, status);

if (!CollectionUtils.inArray(tipo, new String[]{"NF", "NFS", "CT"})) {
    throw new MGEModelException("Tipo de documento inválido: " + tipo);
}
```

---

## Split de lista para batch (Oracle IN clause)

Oracle limita `IN` a 1000 parâmetros. Usar `splitList` para processar em lotes.

```java
import java.math.BigDecimal;
import java.util.Collection;

List<BigDecimal> todosIds = /* lista com > 1000 itens */;

// Divide em sublistas de até 500 itens
Collection<Collection<BigDecimal>> lotes = CollectionUtils.splitList(todosIds, 500);

for (Collection<BigDecimal> lote : lotes) {
    String in = SQLUtils.buildINClauseByValues("NUNOTA", lote);
    // executar query por lote...
}
```

---

## Transformar coleção (map)

```java
import com.sankhya.util.CollectionUtils.CollectionTransformer;

Collection<String> codigos = CollectionUtils.map(registros,
    vo -> vo.asString("CODPROD")
);
```

---

## Antipadrões

```java
// ERRADO — verificação manual
if (lista == null || lista.isEmpty()) { ... }
// CORRETO
if (CollectionUtils.isEmpty(lista)) { ... }

// ERRADO — IN com lista > 1000 sem split
String in = SQLUtils.buildINClauseByValues("ID", listaGrande); // ORA-01795 se > 1000
// CORRETO
Collection<Collection<BigDecimal>> lotes = CollectionUtils.splitList(listaGrande, 999);
// processar por lote
```
