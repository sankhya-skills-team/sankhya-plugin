> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/IDataUnitCrudListener/ (snapshot 2026-09-28)

# IDataUnitCrudListener

Interface que define interceptadores para operações CRUD em um `DataUnit`.

## beforeInsert

Executado antes de uma operação de inserção ser realizada.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class InsertValidationInterceptor implements IDataUnitCrudListener {

    @Override
    public void beforeInsert(DataUnitCrudListenerContext ctx) throws Exception {
        Object valorTotal = ctx.getVO().getProperty("VALOR_TOTAL");
        if (valorTotal == null || ((BigDecimal) valorTotal).compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("O campo VALOR_TOTAL deve ser maior que zero.");
        }
    }
}
```

## afterInsert

Executado após uma operação de inserção ser concluída com sucesso.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class NotifyAfterInsertInterceptor implements IDataUnitCrudListener {

    @Override
    public void afterInsert(DataUnitCrudListenerContext ctx) throws Exception {
        String cliente = (String) ctx.getVO().getProperty("NOME_CLIENTE");
        System.out.println("Notificação enviada: Novo cliente cadastrado - " + cliente);
    }
}
```

## beforeUpdate

Executado antes de uma operação de atualização ser realizada.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class BlockOldRecordsInterceptor implements IDataUnitCrudListener {

    @Override
    public void beforeUpdate(DataUnitCrudListenerContext ctx) throws Exception {
        LocalDate dataCriacao = (LocalDate) ctx.getVO().getProperty("DATA_CRIACAO");
        if (dataCriacao != null && dataCriacao.isBefore(LocalDate.now().minusYears(5))) {
            throw new IllegalStateException("Não é permitido atualizar registros com mais de 5 anos.");
        }
    }
}
```

## afterUpdate

Executado após uma operação de atualização ser concluída com sucesso.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class AuditUpdateInterceptor implements IDataUnitCrudListener {

    @Override
    public void afterUpdate(DataUnitCrudListenerContext ctx) throws Exception {
        ctx.getVO().setProperty("DATA_ATUALIZACAO", LocalDateTime.now());
        ctx.getVO().setProperty("USUARIO_ATUALIZACAO", ctx.getUser().getUsername());
    }
}
```

## beforeDelete

Executado antes de uma operação de exclusão ser realizada.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class PreventDeleteInterceptor implements IDataUnitCrudListener {

    @Override
    public void beforeDelete(DataUnitCrudListenerContext ctx) throws Exception {
        Object status = ctx.getVO().getProperty("STATUS_FATURA");
        if ("PENDENTE".equalsIgnoreCase((String) status)) {
            throw new IllegalStateException("Não é possível excluir registros com faturas pendentes.");
        }
    }
}
```

## afterDelete

Executado após uma operação de exclusão ser concluída com sucesso.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class LogAfterDeleteInterceptor implements IDataUnitCrudListener {

    @Override
    public void afterDelete(DataUnitCrudListenerContext ctx) throws Exception {
        System.out.println("Registro excluído: ID " + ctx.getVO().getPrimaryKey());
    }
}
```

## beforeFind

Executado antes de uma operação de busca ser realizada. + Pode ser utilizado para manipular filtros ou ajustar critérios de pesquisa.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class ActiveRecordsFinderInterceptor implements IDataUnitCrudListener {

    @Override
    public void beforeFind(DataUnitCrudListenerContext ctx) throws Exception {
        ctx.getFinder().setAdditionalWhere("STATUS = 'ATIVO'");
    }
}
```

## afterLoadVOs

Executado após a carga de uma coleção de `VO`.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class AddNoteAfterLoadInterceptor implements IDataUnitCrudListener {

    @Override
    public void afterLoadVOs(Collection result) throws Exception {
        for (Object vo : result) {
            ((DynamicVO) vo).setProperty("OBSERVACAO", "Registro revisado automaticamente.");
        }
    }
}
```

## loadCustomData

Permite carregar os dados customizados com base nos critérios fornecidos.

```java
@DataUnitCrudListener(entity = "MovimentoBancario", resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class CustomDataLoaderInterceptor implements IDataUnitCrudListener {

    @Override
    public Collection loadCustomData(FinderWrapper finder) throws Exception {
        finder.setAdditionalWhere("TIPO_CLIENTE = 'VIP'");
        return List.of();  // Substitua por lógica real de carregamento
    }
}
```
