# JAPE — Framework de Persistência Sankhya

> Fonte oficial: https://developer.sankhya.com.br/docs/jape
> **Regra de ouro deste pipeline:** acesso a dados em backend Sankhya é feito por
> **JAPE** (`JapeFactory`/`JapeWrapper`, `EntityFacade`/`DynamicVO`, `FinderWrapper`).
> `NativeSql` é **último recurso** e **só** com assinatura verificada contra o jar real.
> Nunca inventar método de `NativeSql`/utilitário.

## O que é

JAPE é o framework de persistência da Sankhya. Mapeia classes Java em tabelas
relacionais e expõe consulta, inserção, alteração e exclusão sem escrever SQL.
Trabalha sobre entidades do Dicionário de Dados (nativas ou adicionais do addon).

## Controle de sessão (padrão obrigatório)

Toda operação fora de um serviço transacional abre/fecha sessão e roda dentro de um bloco de transação:

```java
SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    hnd.execWithTX(new JapeSession.TXBlock() {
        public void doWithTx() throws Exception {
            // operacoes em entidades ou NativeSql
        }
    });
} finally {
    JapeSession.close(hnd);
}
```

Evitar timeout em processo longo:

```java
hnd.setCanTimeout(false);
```

Transação autônoma (commit independente da transação corrente — usar com cautela,
ex.: auditoria, reprocessamento idempotente exclui+regera):

```java
hnd.execWithAutonomousTX(new JapeSession.TXBlock() {
    public void doWithTx() throws Exception { /* ... */ }
});
```

Propriedades de sessão usadas por regras/gatilhos:

```java
JapeSession.putProperty("usuario_logado", CODUSU);
JapeSession.putProperty("emp_usu_logado", usuVO.getCODEMP());
JapeSession.putProperty("dh_atual", new Timestamp(System.currentTimeMillis()));
```

## EntityFacade — API canônica (CRUD)

Obter a fachada:

```java
EntityFacade dwfFacade = EntityFacadeFactory.getDWFFacade();
```

### Instância vazia com defaults

```java
DynamicVO finVO = (DynamicVO) dwfFacade.getDefaultValueObjectInstance(
        DynamicEntityNames.FINANCEIRO);
```

### Buscar por chave primária (somente leitura)

```java
DynamicVO finVO = (DynamicVO) dwfFacade.findEntityByPrimaryKeyAsVO(
        DynamicEntityNames.FINANCEIRO, new Object[]{ nuFin });
```

### Buscar por critério (FinderWrapper)

```java
FinderWrapper finder = new FinderWrapper(
        DynamicEntityNames.FINANCEIRO,
        "this.CODPARC = ? AND this.DTVENC > ?",
        new Object[]{ codParc, dtVenc });
Collection<DynamicVO> financeiros = dwfFacade.findByDynamicFinderAsVO(finder);
```

> O alias da própria entidade é `this.`. Os `?` são posicionais, na ordem do array.

### Criar

```java
DynamicVO finVO = (DynamicVO) dwfFacade.getDefaultValueObjectInstance(
        DynamicEntityNames.FINANCEIRO);
finVO.setProperty("DTNEG", dtNeg);
finVO.setProperty("DTVENC", dtVenc);
dwfFacade.createEntity(DynamicEntityNames.FINANCEIRO, (EntityVO) finVO);
```

### Atualizar (entidade gerenciada — alteração faz dirty-check)

```java
PersistentLocalEntity finEntity = dwfFacade.findEntityByPrimaryKey(
        DynamicEntityNames.FINANCEIRO, new Object[]{ nuFin });
DynamicVO finVO = (DynamicVO) finEntity.getValueObject();
finVO.setProperty("CODTIPTIT", codTipTit);
finEntity.setValueObject((EntityVO) finVO);
```

### Remover por PK

```java
dwfFacade.removeEntity(DynamicEntityNames.FINANCEIRO, new Object[]{ nuFin });
```

### Remover por critério

```java
FinderWrapper finder = new FinderWrapper(
        DynamicEntityNames.FINANCEIRO,
        "this.CODPARC = ? AND this.DTVENC >= ?",
        new Object[]{ codParc, dtVenc });
dwfFacade.removeByCriteria(finder);
```

## JapeWrapper / JapeFactory — API fluente (preferir para leitura simples)

```java
JapeWrapper empresaDAO = JapeFactory.dao(DynamicEntityNames.EMPRESA);
DynamicVO empresa = empresaDAO.findByPK(BigDecimal.ZERO);
```

`JapeFactory.dao(entityName)` retorna um `JapeWrapper` com `findByPK`, busca por
campo e `prepareToCreate`/`prepareToUpdate` fluentes — mais legível que o tripé do
`EntityFacade` para casos diretos.

## NativeSql — ÚLTIMO recurso (API real)

Use somente quando JAPE não expressa a consulta (agregações complexas, joins
pesados de leitura). API **verdadeira** (não inventar métodos):

```java
NativeSql sql = new NativeSql(jdbc);
sql.appendSql("SELECT * FROM TSIUSU WHERE CODUSU = :CODUSU");
sql.setNamedParameter("CODUSU", BigDecimal.ZERO);
ResultSet rset = sql.executeQuery();
```

Métodos existentes na classe: `appendSql(String)`, `setNamedParameter(String, Object)`,
`executeQuery()` (retorna `ResultSet`). **Não existem** `getColumnsAsMap(...)` nem
`MapUtils.getMapValueAsBigDecimal(...)` — se precisar de um valor escalar, leia do
`ResultSet` ou prefira `JapeFactory`/`FinderWrapper`. SQL nativo exige parâmetro
nomeado (anti-injection); nunca concatenar entrada do usuário.

## Entity Listener (gatilho de persistência)

Estender `PersistenceEventAdapter` e sobrescrever só o necessário:

```java
public class BeneficioListener extends PersistenceEventAdapter {
    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        validaBeneficio((DynamicVO) event.getVo());
    }
}
```

Registro no XML da entidade (módulo tradicional):

```xml
<entity name="Beneficio" main-object="Beneficio" commit-type="D">
    <event-listener class="br.com.sankhya.beneficio.model...BeneficioListener" />
</entity>
```

No Addon Studio o gatilho é via `@Listener` (ver `references/listeners.md`).

Métodos da interface `PersistenceEventListener`:
`beforeInsert`/`afterInsert`, `beforeUpdate`/`afterUpdate`,
`beforeDelete`/`afterDelete`, `afterLoadValueObject`/`afterRetrieveValueObject`.

Para interceptar **buscas** (filtros/ordenação antes da query) use o
`BeforeLoadListener` — ver `references/before-load-listener.md`.

## Checklist antes de codar acesso a dados

1. A entidade existe no Dicionário? Validar via MCP `sankhya-schema`
   (`describe_table`/`search_entities`). Nunca inventar tabela/campo.
2. Operação expressável em JAPE? Então **JAPE** (EntityFacade/JapeFactory + FinderWrapper).
3. Só se não for: `NativeSql` com parâmetro nomeado e assinatura verificada no jar.
4. Escrita sempre dentro de `execWithTX` (ou `execWithAutonomousTX` quando justificado).
5. `MGEModelException` para erro de regra; nunca engolir exceção.
