> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/IDataUnitInterceptor/ (snapshot 2026-09-28)

# IDataUnitInterceptor

Interface que define _interceptadores_ para ações relacionadas a um `DataUnit`.

## interceptFieldMetadata

Intercepta e permite manipular os metadados de um campo específico durante a construção do `DataUnit`.

```java
@DataUnitInterceptor(entity = "Financeiro", resourceId = "br.com.sankhya.fin.cad.movimentacaoFinanceira")
public class CustomFieldMetadataInterceptor implements IDataUnitInterceptor {

    @Override
    public void interceptFieldMetadata(DataUnitField duField) {
        if ("VALOR_TOTAL".equalsIgnoreCase(duField.getName())) {
            duField.setRequired(true); // Define o campo como obrigatório
            duField.setLabel("Valor Total (R$)");
        }
    }
}
```

## interceptFieldsMetadata

Intercepta e permite manipular os metadados de uma lista de campos durante a construção do `DataUnit`.

```java
@DataUnitInterceptor(entity = "Financeiro", resourceId = "br.com.sankhya.fin.cad.movimentacaoFinanceira")
public class MultipleFieldsMetadataInterceptor implements IDataUnitInterceptor {

    @Override
    public void interceptFieldsMetadata(List<DataUnitField> duFields) {
        duFields.forEach(field -> {
            if (field.getName().startsWith("PERCENTUAL")) {
                field.setLabel(field.getLabel() + " (%)");
            }
        });
    }
}
```

## isIgnoredField

Determina se um campo específico deve ser ignorado durante os fluxos de execução.

```java
@DataUnitInterceptor(entity = "Financeiro", resourceId = "br.com.sankhya.fin.cad.movimentacaoFinanceira")
public class IgnoreSensitiveDataInterceptor implements IDataUnitInterceptor {

    @Override
    public boolean isIgnoredField(DataUnitField duField) {
        return "SENHA".equalsIgnoreCase(duField.getName())
            || "TOKEN".equalsIgnoreCase(duField.getName());
    }
}
```

## isInvisibleChild

Determina se um elemento filho deve ser invisível durante a manipulação do `DataUnit`.

```java
@DataUnitInterceptor(entity = "Financeiro", resourceId = "br.com.sankhya.fin.cad.movimentacaoFinanceira")
public class InvisibleChildInterceptor implements IDataUnitInterceptor {

    @Override
    public boolean isInvisibleChild(String masterName, DataUnitChild child) {
        return "CLIENTE_VIP".equalsIgnoreCase(masterName)
            && "DESCONTO_ESPECIAL".equalsIgnoreCase(child.getName());
    }
}
```

## getFieldMap

Retorna um mapeamento customizado de campos para o `DataUnit`.

```java
@DataUnitInterceptor(entity = "Financeiro", resourceId = "br.com.sankhya.fin.cad.movimentacaoFinanceira")
public class CustomFieldMappingInterceptor implements IDataUnitInterceptor {

    @Override
    public List<DataUnitFieldMap> getFieldMap() {
        return List.of(
            new DataUnitFieldMap("PRECO_UNITARIO", "VALOR_UNITARIO"),
            new DataUnitFieldMap("QTD_ESTOQUE", "ESTOQUE_ATUAL")
        );
    }
}
```
