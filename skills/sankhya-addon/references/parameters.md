# Parâmetros Embarcados no Add-on

## Visão Geral

Parâmetros permitem tornar o add-on flexível, deixando os usuários ajustarem o comportamento do sistema sem alterações no código-fonte. Com o Add-on Studio, você pode embarcar parâmetros diretamente na solução via `parameter.xml`.

---

## Localização do Arquivo

```
model/src/main/resources/META-INF/parameter.xml
```

---

## Estrutura do `parameter.xml`

Adicione quantos parâmetros precisar dentro da tag `<parameters>`. Cada parâmetro é uma tag `<parameter>` com seus atributos.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE parameters >
<parameters group-name="mge.:name"
            data-source="br.com.sankhya.modelcore.util.MGECoreParameter"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:noNamespaceSchemaLocation="../../../../../.gradle/parameters.xsd">

    <!-- Exemplo de parâmetro para máscara de hierarquia -->
    <parameter
        name="addon.mascara.MASKHIERARC"
        key="MASKHIERARC"
        type="string"
        default="##\.##\.##"
        cacheable="true"
        required="false"
        module="B"
        description="Define a máscara para o cadastro de hierarquias."/>

</parameters>
```

## Atributos da Tag `<parameter>`

| Atributo | Descrição | Exemplo |
|---|---|---|
| `name` | Identificador único do parâmetro no sistema. Usado para referenciá-lo no código. | `addon.mascara.MASKHIERARC` |
| `key` | Chave que aparece na tela de **Preferências** do Sankhya. **Máximo de 15 caracteres**. | `MASKHIERARC` |
| `type` | Tipo de dado: `string`, `number`, `date`, `list`, `boolean`, `integer`. | `string` |
| `default` | Valor padrão adotado. | `##\.##\.##` |
| `cacheable` | Se o valor deve ser armazenado em cache para melhorar a performance. | `true` |
| `required` | Se o parâmetro é obrigatório. Se `true`, um `default` deve ser fornecido. | `false` |
| `module` | Módulo do Sankhya ao qual o parâmetro está associado (ex: `C` para Contabilidade, `E` para Comercial, `B` para Configuração). | `B` |
| `description` | Descrição exibida na tela de **Preferências**. **Máximo de 50 caracteres**. | `Define a máscara...` |

> No IntelliJ, ao passar o mouse sobre um atributo no `parameter.xml`, a IDE exibe documentação útil graças ao `parameters.xsd` referenciado no arquivo.

---

## Deploy e Validação

1. Execute o deploy:
   ```shell
   ./gradlew clean deployAddon
   ```

2. Acesse o ambiente Sankhya local, vá para a tela de **Preferências** e procure pelo parâmetro usando a `key` ou a `description` definida.

> **Importante**: Após o deploy, o parâmetro é criado apenas na interface. Ele só é persistido na tabela `TSIPAR` caso o usuário **altere e salve o valor manualmente** pelo menos uma vez. Caso contrário, o valor `default` é carregado da memória.

---

## Boas Práticas

- **Nomenclatura consistente**: use um prefixo nos atributos `name` e `key` para evitar conflitos com parâmetros nativos do Sankhya ou de outros add-ons. Ex: `MEUADDON_NOME_PARAM`
- **Descrições claras**: escreva descrições que ajudem o usuário a entender o que o parâmetro faz sem precisar consultar documentação
- **Use `cacheable="true"`**: para parâmetros lidos com frequência e que não mudam constantemente, o cache melhora significativamente a performance
- **Valores padrão seguros**: defina valores padrão que façam sentido e não quebrem o sistema se o usuário não configurar o parâmetro

## Antipadrões

- **Chaves genéricas**: usar `key` como `PARAM1` ou `TESTE` é má prática — seja específico
- **Descrições vagas**: uma `description` como "Parâmetro do add-on" não ajuda em nada
- **Abusar de parâmetros**: nem tudo precisa ser um parâmetro. Se uma configuração é muito técnica ou raramente muda, talvez deva ser um valor fixo no código
- **Esquecer de persistir o valor**: o parâmetro só é salvo no banco após a primeira alteração manual — se sua lógica depende dele, instrua o usuário a configurá-lo

## Leitura de Parâmetros via Java (Backend)

Para ler parâmetros do `parameter.xml` em código Java (listeners, action buttons, jobs), use `MGECoreParameter` com o `name` exatamente como registrado no XML:

```
Pacote: br.com.sankhya.modelcore.util.MGECoreParameter
```

### Métodos disponíveis

| Método | Tipo `parameter.xml` | Retorno |
|---|---|---|
| `MGECoreParameter.getParameter(String name)` | Qualquer (auto-detecta) | `Object` — cast conforme tipo |
| `MGECoreParameter.getParameterAsString(String name)` | `string` | `String` |
| `MGECoreParameter.getParameterAsInt(String name)` | `integer` | `int` |
| `MGECoreParameter.getParameterAsBoolean(String name)` | `boolean` | `boolean` |

**Regras:**
- Argumento: `name` do `<parameter>` no XML — use o valor exato, sem transformações
- `MGECoreParameter` disponível no classpath via plugin Addon Studio

### Padrão simples

```java
import br.com.sankhya.modelcore.util.MGECoreParameter;

// string
String valor = MGECoreParameter.getParameterAsString("MEUADDON_CHAVE");

// number (retorna BigDecimal para tipo float/number)
BigDecimal pct = (BigDecimal) MGECoreParameter.getParameter("MEUADDON_PCT");

// integer
int limite = MGECoreParameter.getParameterAsInt("MEUADDON_LIMITE");
```

### Padrão com fallback (recomendado quando parâmetro pode não estar persistido)

> O parâmetro só é salvo no banco após a primeira alteração manual pelo usuário.
> Se o código for executado antes disso, `getParameter` pode lançar exceção.
> Use try-catch com valor padrão.

```java
import br.com.sankhya.modelcore.util.MGECoreParameter;
import java.math.BigDecimal;
import java.util.logging.Level;
import java.util.logging.Logger;

private static final Logger LOG = Logger.getLogger(MinhaClasse.class.getName());

// Parâmetro numérico com fallback
private BigDecimal lerParamNumerico(String name, BigDecimal valorDefault) {
    try {
        Object valor = MGECoreParameter.getParameter(name);
        if (valor instanceof BigDecimal) return (BigDecimal) valor;
        if (valor instanceof Number) return new BigDecimal(valor.toString());
    } catch (Exception e) {
        LOG.log(Level.WARNING, "Parametro nao encontrado: " + name + ". Usando default.", e);
    }
    return valorDefault;
}

// Parâmetro texto com fallback
private String lerParamTexto(String name, String valorDefault) {
    try {
        String valor = MGECoreParameter.getParameterAsString(name);
        if (valor != null && !valor.trim().isEmpty()) return valor.trim();
    } catch (Exception e) {
        LOG.log(Level.WARNING, "Parametro nao encontrado: " + name + ". Usando default.", e);
    }
    return valorDefault;
}
```

**Antipadrão:** usar `MGEParameters.asBigDecimal("group", "chave.longa")` — isso era padrão do Flex/EJB antigo (`br.com.sankhya.motazan.model.dao.MGEParameters`). No Addon Studio, use `MGECoreParameter.getParameter("NOME_PARAM")`.

## Fonte

https://developer.sankhya.com.br/docs/03_parameter