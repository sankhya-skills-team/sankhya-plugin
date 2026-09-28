> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/IDataExporterInterceptor/ (snapshot 2026-09-28)

# IDataExporterInterceptor

Interface para interceptar e customizar o comportamento do exportador de dados.

## buildSumExpression

Constrói uma expressão de agregação personalizada (por exemplo, uma função `SUM` para ser aplicada durante a exportação de dados.

```java
@DataExporterInterceptor(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class ConditionalSumExporterInterceptor implements IDataExporterInterceptor {

    @Override
    public String buildSumExpression(String jrFieldName, String expression, Map<String, String> extraParams) {
        if ("DESCONTO".equalsIgnoreCase(jrFieldName)) {
            return String.format("SUM(%s) * 0.9", jrFieldName); // Aplica 10% de desconto
        }
        return String.format("SUM(%s)", jrFieldName);
    }
}
```

## getRequiredColumns

Retorna as colunas obrigatórias que devem estar presentes na exportação de dados.

```java
@DataExporterInterceptor(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class SimpleSumExporterInterceptor implements IDataExporterInterceptor {

    @Override
    public List<ExporterColumMetadata> getRequiredColumns() {
        return List.of(
            new ExporterColumMetadata("TOTAL", "Valor total da compra"),
            new ExporterColumMetadata("QUANTIDADE", "Quantidade total de itens")
        );
    }
}
```
