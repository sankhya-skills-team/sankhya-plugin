> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/ICustomFilterBarResolver/ (snapshot 2026-09-28)

# ICustomFilterBarResolver

Interface para resolver e manipular configurações da `FilterBar`.

## handle

Manipula a configuração da `FilterBar`, permitindo ajustes nos filtros ou demais parâmetros disponíveis.

```java
@CustomFilterBarResolver(resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class CustomFilterBarResolver implements ICustomFilterBarResolver {

  @Override
  public void handle(FilterBarConfig filterBarConfig) throws Exception {

    if(!filterBarConfig){
      System.out.println("Nenhuma configuração informada");
      return;
    }

    System.out.println("Lidando com configurações: " + filterBarConfig);
  }
}
```
