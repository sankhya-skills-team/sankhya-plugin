> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/ITotalsResolver/ (snapshot 2026-09-28)

# ITotalsResolver

Interface que permite a implementação de resolvers específicos para o componente de Totalizador.

## canResolve

Verifica se esta implementação é capaz de resolver a URI fornecida.

```java
@CustomFilterBarResolver(resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class OrderTotalResolver implements ITotalsResolver {

    @Override
    public boolean canResolve(ResourceURI uri) {
        return "pedidos/total".equals(uri.getPath());
    }
}
```

## resolve

Resolve os totalizadores com base nos filtros e no contexto SQL fornecidos.

```java
@CustomFilterBarResolver(resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class StockTotalResolver implements ITotalsResolver {

    @Override
    public List<TotalsResult> resolve(List<DataUnitFilter> filter, TotalsResolverSqlContext sqlContext) throws Exception {
        int totalEstoque = 0;

        // Simulando cálculo de estoque
        for (DataUnitFilter filtro : filter) {
            if ("PRODUTO_ID".equals(filtro.getFieldName())) {
                totalEstoque += 100;  // Simulação de estoque fictício
            }
        }

        TotalsResult result = new TotalsResult("TOTAL_ESTOQUE", totalEstoque);
        List<TotalsResult> results = new ArrayList<>();
        results.add(result);

        return results;
    }
}
```
