# Micromódulo Sankhya — abordagem legada EJB2

> **Escopo:** cobre a abordagem **legada** EJB2/XDoclet. Para a abordagem moderna
> (anotações `@Service`, `@Repository`, `@Listener`), veja `references/micromodule-sdk.md`.

## Quando usar

- Criar ou alterar SPBeans, EntityListeners, ServiceWrappers, Jobs
- Escrever `service-providers.xml`, `mgeschedule-cfg.xml`, `BootModuleListener`
- Configurar `build.gradle`, `settings.gradle` de projetos micromódulo
- Entender uso de `BaseSPBean`, `ServiceContext`, `DynamicVO`

## O que é um micromódulo

Componente autônomo publicado como EAR no ambiente WildFly do cliente. Estende o
SankhyaOm via classpath compartilhado sem alterar o monolito. Deve ter
**responsabilidade única** e ser o mais enxuto possível.

## Estrutura do projeto

```
{nome}-model/
  ejbsrc/br/.../
    model/facades/    # *SP.java, *SPHome.java, *SPSession.java (gerados por XDoclet)
    job/              # interfaces de Job (geradas)
  src/main/java/br/.../
    entity/           # modelo rico (sem sufixo obrigatório)
    repository/       # camada de acesso a dados (sufixo Repository)
    service/          # orquestrador de domínio (sufixo Service)
    controller/       # entrypoints EJB finos (sufixo SPBean)
    job/              # *JobSPBean.java
  src/main/resources/
    META-INF/
      ejb-jar.xml
      mgeschedule-cfg.xml
    br/.../
      sql/            # arquivos .sql nomeados (prefixo: que*, ins*, upd*, del*)
      dd/             # configuração interna de entidade
      parameters/     # parameter.xml
{nome}-vc/
  src/main/java/br/.../
    servlet/          # BootModuleListener
    graphql/          # resolvers GraphQL (opcional)
  webapp/WEB-INF/
    web.xml
    resources/
      service-providers.xml   ← CRÍTICO
datadictionary/       # um .xml por tabela/view
dbscripts/
  oracle.sql
  mssqlserver.sql
build.gradle
settings.gradle
```

## Componentes-chave

| Componente | Descrição |
|-----------|-----------|
| `*SPBean.java` | endpoint de serviço EJB2 |
| `BootModuleListener` | registra todos os componentes na inicialização |
| `EntityListener` | ganchos de persistência (before/afterInsert, etc.) |
| `ServiceWrapper` | pré/pós-processamento em torno de serviços existentes |
| `service-providers.xml` | expõe SPBeans como endpoints HTTP |
| `ServiceContext` (read/write) | API de requisição/resposta |

## Convenções de nomenclatura

| Artefato | Padrão | Exemplo |
|----------|--------|---------|
| Service bean | `*SPBean.java` | `FiscalSPBean.java` |
| Interface remota (gerada) | `*SP.java` | `FiscalSP.java` |
| Interface home (gerada) | `*SPHome.java` | `FiscalSPHome.java` |
| Session wrapper (gerado) | `*SPSession.java` | `FiscalSPSession.java` |
| Job bean | `*JobSPBean.java` | `ConsultCnpjJobSPBean.java` |
| Arquivo SQL | `que*.sql`, `ins*.sql` | `queSeqMaximaICMS.sql` |
| Tabela | prefixo único em MAIÚSCULAS | `TTKREGRA`, `TTKNOT` |
| JNDI | `{modulo}/model/ejb/session/{Nome}SP` | `turnkey/model/ejb/session/FiscalSP` |

## Padrão JapeSession (obrigatório em todos os SPBeans)

```java
JapeSession.SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    // lógica de negócio
} finally {
    JapeSession.close(hnd);   // SEMPRE fechar no finally
}
```

## Tratamento de erros em micromódulos

```java
import br.com.sankhya.internal.sdk.exceptions.TransactionRollbackException;

try {
    hnd = JapeSession.open();
    // lógica
} catch (MGEModelException e) {
    throw e;   // erro de negócio: propagar limpo (container commita — ok se não há escrita)
} catch (Exception e) {
    throw new TransactionRollbackException(e);  // inesperado: RuntimeException → ROLLBACK
} finally {
    JapeSession.close(hnd);
}
```

> **NÃO use `throwExceptionRollingBack(e)`** em micromódulos — `SessionContext` não é
> injetado pelo TinyEJB.
> **NÃO use `MGEModelException.throwMe(e)`** para erros inesperados — o TinyEJB faz
> COMMIT em vez de rollback.

## Regras inegociáveis

1. **Sempre estender `BaseSPBean`** em micromódulos — fornece `throwExceptionRollingBack()` e `setupContext()`
2. **`JapeSession` sempre fechado no `finally`** — sem exceções
3. **`next()` sempre chamado no ServiceWrapper** salvo se for substituir o serviço por completo
4. **Lógica de negócio em classes Helper/Service**, não no SPBean
5. **Para detalhes de persistência** → use a skill `sankhya-jape`
6. **Para schema de banco (dbscripts, datadictionary)** → use dbscripts + datadictionary (SQL portável Oracle/MSSQL via macros)
7. **Para utilitários null-safe** → use os helpers null-safe do SDK (`StringUtils`, `BigDecimalUtil`, etc.)

## Checklist de implementação

- [ ] `service-providers.xml` criado com `domain`, `class`, `type`, `jndi`, `authentication`
- [ ] JNDI no `service-providers.xml` bate com o `jndi-name` da anotação xdoclet
- [ ] `JapeSession` sempre fechado no `finally` com `JapeSession.close(hnd)`
- [ ] `JdbcWrapper` sempre fechado no `finally` com `JdbcWrapper.closeSession(jdbc)`
- [ ] `next()` chamado no ServiceWrapper
- [ ] Componentes registrados no `BootModuleListener` via `MicroModuleUtils`
- [ ] `moduleLib` vs `implementation` revisados no `build.gradle`
- [ ] Cada classe Java tem uma classe `*Test` correspondente
- [ ] Exceções: `TransactionRollbackException` para rollback; `MGEModelException` para erro de negócio

## Avisos críticos

> **Listeners** bloqueiam transações do usuário — performance é essencial.
> **Atualizações** pausam transações do listener por até 2 minutos.
> **`publishModule`** distribui para TODOS os clientes — publique com extrema cautela.
> **JNDI divergente** no `service-providers.xml` causa erro silencioso de lookup.
