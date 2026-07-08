# A Camada de Serviço (@Service)

## Visão Geral

A anotação `@Service` designa uma classe como ponto de entrada (endpoint) para requisições externas. Atua como um "Controller" no padrão MVC, orquestrando a interação entre o mundo exterior e a lógica de negócio.

> **Atenção:** Este arquivo documenta o padrão **Add-on Studio 2.0 clássico**. Se o projeto usar o SDK beta (`@JapeEntity`, `@Repository`, `@Inject`), consulte `references/sdk-controller.md` — o ciclo de vida e as anotações são diferentes.

---

## Padrão Obrigatório — Add-on Studio 2.0 Clássico

No Add-on Studio 2.0 clássico, o `@Service` **sempre** recebe `ServiceContext` como parâmetro. Não existe injeção automática de DTOs, nem `@Transactional` gerenciado pelo framework. O padrão é:

1. Propagar autenticação com `ctx.setAutentication` + `ctx.makeCurrent()`
2. Abrir sessão JAPE com `JapeSession.open()` em try/finally
3. Ler o body com `ctx.getJsonRequestBody()`
4. Delegar para uma classe de aplicação (nunca colocar lógica no `@Service`)
5. Escrever a resposta com `ctx.setJsonResponse()`

```java
@Service(
    serviceName = "com.minhaempresa.modulo.MeuServiceSP",
    transactionType = EJBTransactionType.NotSupported
)
public class MeuService {

    private static final Logger logger = Logger.getLogger(MeuService.class);

    // Colaborador instanciado como campo — stateless, thread-safe, sem overhead por chamada
    private final MeuAplicacaoService aplicacao = new MeuAplicacaoService();

    public void executar(ServiceContext ctx) throws Exception {
        // 1. Propagar autenticação — obrigatório antes de abrir sessão
        ctx.setAutentication(AuthenticationInfo.getCurrent());
        ctx.makeCurrent();

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();

            // 2. Ler e validar o body
            JsonObject input = ctx.getJsonRequestBody();
            if (input == null || !input.has("dto")) {
                throw new MGEModelException("Parâmetro 'dto' é obrigatório.");
            }

            JsonObject dto = input.getAsJsonObject("dto");
            BigDecimal codRegistro = dto.get("CODREGISTRO").getAsBigDecimal();

            // 3. Delegar para a camada de aplicação
            String resultado = aplicacao.processar(codRegistro);

            // 4. Escrever resposta
            JsonObject response = new JsonObject();
            response.addProperty("mensagem", resultado);
            ctx.setJsonResponse(response);

        } finally {
            JapeSession.close(hnd); // sempre fechar, mesmo em caso de exceção
        }
    }
}
```

> **Por que `ctx.setAutentication` + `ctx.makeCurrent()`?** Garante que a sessão JAPE aberta a seguir herde o contexto de segurança do usuário logado. Sem isso, operações de banco podem falhar por falta de contexto de autenticação.

> **Por que não `@Transactional` aqui?** No Add-on Studio 2.0 clássico, o controle transacional é feito via `EJBTransactionType` na anotação `@Service` ou via `hnd.execWithTX()` para blocos específicos. A anotação `@Transactional` do SDK beta **não funciona** neste contexto.

---

## SPBean (Add-on Studio 1.0 — legado)

Projetos mais antigos usam `BaseSPBean` com anotações XDoclet. O padrão interno é idêntico ao `@Service` moderno — apenas a forma de registro muda:

```java
/**
 * @ejb.bean name="MeuServiceSP"
 * jndi-name="br/com/empresa/addon/services/sp/MeuServiceSP"
 * type="Stateless"
 * transaction-type="Container"
 * view-type="remote"
 * @ejb.transaction type="Required"
 * @ejb.util generate="false"
 */
public class MeuServiceSPBean extends BaseSPBean implements SessionBean {

    /**
     * @ejb.interface-method view-type="remote"
     * @ejb.transaction type="Required"
     */
    public void executar(ServiceContext ctx) throws Exception {
        ctx.setAutentication(AuthenticationInfo.getCurrent());
        ctx.makeCurrent();

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            // lógica...
        } finally {
            JapeSession.close(hnd);
        }
    }
}
```

### Tipos de transação EJB no SPBean

Use `@ejb.transaction type="NotSupported"` quando o método gerencia transações manualmente via `hnd.execWithTX()` ou `hnd.execWithFakeTX()` — se o container já gerencia uma transação, o `execWithFakeTX` não consegue fazer rollback corretamente:

```java
/**
 * @ejb.transaction type="NotSupported"
 */
public void processarComFakeTx(ServiceContext ctx) throws Exception {
    // hnd.execWithFakeTX funciona corretamente aqui
}
```

---

## Características Principais

- `serviceName` é **obrigatório** — use o **nome simples** (sem namespace): `"NomeServiceSP"`. O namespace completo causa conflito com o registro EJB gerado pelo XDoclet e impede o roteamento correto.
- Por convenção o nome termina com `SP`
- O nome da **classe Java** deve ser diferente do `serviceName` para evitar conflito com a interface EJB gerada pelo XDoclet. Padrão: `serviceName = "GerarPedidoSP"` → classe `GerarPedidoService`.
- Métodos públicos são automaticamente expostos como ações do serviço

## Registro Automático via service-providers.xml

O Gradle gera automaticamente o `service-providers.xml` com base nas anotações `@Service`. **Nunca crie esse arquivo manualmente** — se existir um arquivo manual em `buildGradle/studioGenerated/resources/WEB-INF/resources/service-providers.xml`, o Gradle detecta e **não sobrescreve**, resultando em um arquivo vazio no WAR e erro `Nenhum provedor foi encontrado para o serviço`.

Se isso ocorrer, delete o arquivo manual e rode `gradlew clean deployAddon`.

O arquivo gerado corretamente terá esta estrutura:

```xml
<provider domain="GerarPedidoSP"
          class="br.com.zanchetta.cotacaozct.services.GerarPedidoSP"
          type="ejb-stateless"
          jndi="br/com/zanchetta/cotacaozct/services/GerarPedidoSP"
          authentication="true"/>
```

## Chamada no Frontend (ServiceProxy)

O formato correto no JS é `'nomeaddon@serviceName.nomeMetodo'` — sem namespace, apenas o `serviceName` simples:

```javascript
.factory('GerarPedidoSPService', ['ServiceProxy', function (ServiceProxy) {
    function gerarPedido(dto) {
        return ServiceProxy.callService('cotacaozct@GerarPedidoSP.gerarPedido', dto || {});
    }
    return { gerarPedido: gerarPedido };
}])
```

> Cada botão físico da tela deve ter seu próprio `.factory` com nome descritivo — nunca um factory genérico com concatenação dinâmica de método (`'SP.' + metodo`).

## URL de Acesso

```
<dns>/<contexto-modulo>/service.sbr?serviceName=<nomeDoServico>.<nomeDoMetodo>
```

Exemplo:
```
http://localhost:8080/meu-addon/service.sbr?serviceName=com.minhaempresa.modulo.MeuServiceSP.executar&mgeSession=<jsessionid>
```

O `contexto-do-addon` corresponde ao valor de `rootProject.name` no `settings.gradle`.

## Autenticação

Todas as requisições devem ser autenticadas via `MobileLoginSP.login`:

```bash
curl --location 'http://localhost:8080/mge/service.sbr?serviceName=MobileLoginSP.login&outputType=json' \
--header 'Content-Type: application/json' \
--data '{
    "requestBody": {
        "NOMUSU": {"$": "USUARIO"},
        "INTERNO": {"$": "SENHA_DO_USUARIO"}
    }
}'
```

O retorno contém `jsessionId`, que deve ser passado como `mgeSession` nas requisições. Em ambientes com Gateway, autenticação via MobileLogin não é necessária.

## Controle Transacional (`transactionType`)

| TransactionType | Descrição | Quando Usar |
|---|---|---|
| `Required` | (Padrão) Usa transação existente ou cria uma nova | Operações de escrita simples |
| `RequiresNew` | Sempre cria uma nova transação | Logs de auditoria independentes |
| `NotSupported` | Executa fora de qualquer transação | Consultas, ou quando usa `execWithTX`/`execWithFakeTX` manualmente |
| `Mandatory` | Exige transação já existente | Raro — garantir contexto transacional |

```java
// Serviço de consulta — sem transação para melhor performance
@Service(serviceName = "com.empresa.RelatorioServiceSP", transactionType = EJBTransactionType.NotSupported)
public class RelatorioService {
    public void consultar(ServiceContext ctx) throws Exception { ... }
}
```

---

## Separação de Camadas — Quando usar

A separação `@Service → AplicacaoService → Repository` é obrigatória quando:
- A lógica de negócio é reutilizada em mais de um ponto de entrada (`@Service`, `@ActionButton`, `@Job`)
- A operação tem múltiplas etapas com regras de negócio não triviais
- O método do `@Service` ultrapassaria ~30 linhas com a lógica inline

Para operações simples — uma query, um update, uma validação — colocar a lógica diretamente no `@Service` é aceitável e mais legível. Não crie `AplicacaoService` para cada pequena tarefa.

O `@Service` nunca contém lógica de negócio complexa. A separação correta quando necessária:

```
@Service → AplicacaoService → Repository → DynamicVO
```

```java
// @Service: apenas HTTP adapter
@Service(serviceName = "com.empresa.ListarItensServiceSP", transactionType = EJBTransactionType.NotSupported)
public class ListarItensService {

    public void listar(ServiceContext ctx) throws Exception {
        ctx.setAutentication(AuthenticationInfo.getCurrent());
        ctx.makeCurrent();

        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();

            List<ItemDto> itens = new ListarItensAplicacaoService().listar();

            JsonArray array = new JsonArray();
            for (ItemDto item : itens) {
                JsonObject obj = new JsonObject();
                obj.addProperty("id",     item.getId());
                obj.addProperty("descricao", item.getDescricao());
                array.add(obj);
            }

            JsonObject response = new JsonObject();
            response.add("itens", array);
            ctx.setJsonResponse(response);

        } finally {
            JapeSession.close(hnd);
        }
    }
}

// AplicacaoService: lógica de negócio — sem ServiceContext, sem JapeSession
public class ListarItensAplicacaoService {

    private final ItemRepository repository = new ItemRepository();

    public List<ItemDto> listar() throws Exception {
        Collection<DynamicVO> vos = repository.buscarAtivos();
        List<ItemDto> result = new ArrayList<>();
        for (DynamicVO vo : vos) {
            result.add(new ItemDto(
                vo.asBigDecimal("CODITEM"),
                vo.asString("DESCRICAO")
            ));
        }
        return result;
    }
}

// Repository: acesso a dados — apenas JapeWrapper/NativeSql
public class ItemRepository {
    public Collection<DynamicVO> buscarAtivos() throws Exception {
        return JapeFactory.dao("MinhaEntidade").find("ATIVO = 'S'");
    }
}
```

> A `AplicacaoService` não recebe `ServiceContext` nem abre `JapeSession` — isso é responsabilidade exclusiva do `@Service`. Isso facilita reuso entre diferentes pontos de entrada (Service, ActionButton, Job).

---

## Formato de Requisição e Resposta

### Request

```json
{
  "serviceName": "com.empresa.MeuServiceSP.executar",
  "requestBody": {
    "dto": {
      "CODREGISTRO": 1
    }
  }
}
```

### Response de sucesso (`status: "1"`)

```json
{
  "serviceName": "com.empresa.MeuServiceSP.executar",
  "status": "1",
  "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
  "responseBody": {
    "mensagem": "Processado com sucesso!"
  }
}
```

### Response de erro (`status: "0"`)

```json
{
  "serviceName": "com.empresa.MeuServiceSP.executar",
  "status": "0",
  "transactionId": "CB0F625A72C214CF8449F0B18E1FA81A",
  "statusMessage": "Registro não encontrado. ID=42"
}
```

| Status | Significado |
|---|---|
| `"1"` | Sucesso |
| `"0"` | Erro de execução |
| `"3"` | Timeout |
| `"4"` | Cancelado por concorrência |

> Lançar `MGEModelException` dentro do `@Service` ou da `AplicacaoService` resulta automaticamente em `status: "0"` com a mensagem em `statusMessage`.

---

## Boas Práticas

- Services de consulta: use `transactionType = EJBTransactionType.NotSupported`
- Mantenha o `@Service` enxuto — apenas abre sessão, lê JSON, delega e escreve resposta
- Lógica de negócio vai na `AplicacaoService` — facilita reuso e testes
- Sempre feche a sessão no `finally`: `JapeSession.close(hnd)`
- Sempre propague autenticação antes de abrir sessão: `ctx.setAutentication` + `ctx.makeCurrent()`
- Use `MGEModelException` para erros de negócio — a plataforma converte automaticamente para `status: "0"`

## Antipadrões

- **Lógica de negócio no `@Service`** — dificulta reuso e testes
- **Abrir `JapeSession` sem `try/finally`** — vaza sessão em caso de exceção
- **Omitir `ctx.setAutentication` + `ctx.makeCurrent()`** — causa falhas de autenticação na sessão JAPE
- **Usar `@Transactional` do SDK** — não funciona no Add-on Studio 2.0 clássico; use `EJBTransactionType` na anotação `@Service`
- **Instanciar `AplicacaoService` dentro do método** em vez de como campo da classe — causa overhead desnecessário a cada chamada

## Fonte

https://developer.sankhya.com.br/docs/09_service
