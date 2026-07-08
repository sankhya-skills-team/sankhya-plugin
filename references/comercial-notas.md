# Núcleo Comercial — CACHelper, ImpostosHelpper, CentralFinanceiro

Padrões para criar notas fiscais, calcular impostos, confirmar notas e refazer financeiro
programaticamente a partir de um módulo Java.

> As classes do núcleo comercial (`BarramentoRegra`, `CACHelper`, `ImpostosHelpper`,
> `CentralFinanceiro`) são as mesmas usadas internamente pelo Sankhya. Operar sobre elas
> exige `JapeSession` aberta — nunca chamar fora de um `try/finally` com `JapeSession.close`.

---

## Criar Nota Fiscal via CACHelper

O caminho correto para criar nota programaticamente é via `CACHelper` — nunca via
`JapeWrapper.create()` diretamente na entidade `CabecalhoNota`. O `CACHelper` aciona o
barramento de regras e garante que todos os defaults e validações do Sankhya sejam aplicados.

```java
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.dao.EntityPrimaryKey;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.vo.PrePersistEntityState;
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
import br.com.sankhya.modelcore.comercial.BarramentoRegra;
import br.com.sankhya.modelcore.comercial.centrais.CACHelper;
import br.com.sankhya.modelcore.util.DynamicEntityNames;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import com.sankhya.util.TimeUtils;

public BigDecimal criarNota(BigDecimal codEmp, BigDecimal codParc,
                             BigDecimal codTipVenda, BigDecimal codNat,
                             BigDecimal codTipOper, String tipMov) throws Exception {

    EntityFacade entityFacade = EntityFacadeFactory.getDWFFacade();
    AuthenticationInfo auth   = AuthenticationInfo.getCurrent();
    CACHelper cacHelper       = new CACHelper();

    // 1. Instanciar VO com valores padrao da entidade
    DynamicVO novaCabVo = (DynamicVO) entityFacade
        .getDefaultValueObjectInstance(DynamicEntityNames.CABECALHO_NOTA);

    // 2. Preencher campos obrigatorios
    novaCabVo.setProperty("NUMNOTA",     BigDecimal.ZERO);
    novaCabVo.setProperty("CODEMP",      codEmp);
    novaCabVo.setProperty("CODPARC",     codParc);
    novaCabVo.setProperty("CODTIPVENDA", codTipVenda);
    novaCabVo.setProperty("DTNEG",       TimeUtils.getNow());
    novaCabVo.setProperty("DTALTER",     TimeUtils.getNow());
    novaCabVo.setProperty("CODTIPOPER",  codTipOper);
    novaCabVo.setProperty("CODNAT",      codNat);
    novaCabVo.setProperty("TIPMOV",      tipMov); // "V" = venda, "P" = pedido

    // 3. Construir PrePersistEntityState e acionar o barramento
    PrePersistEntityState ppes = PrePersistEntityState.build(
        entityFacade, DynamicEntityNames.CABECALHO_NOTA, novaCabVo);
    BarramentoRegra barramento = cacHelper.incluirAlterarCabecalho(auth, ppes);

    // 4. Extrair o NUNOTA gerado
    return obterNunota(barramento);
}

private static BigDecimal obterNunota(BarramentoRegra barramento) {
    Collection<EntityPrimaryKey> pks = barramento.getDadosBarramento().getPksEnvolvidas();
    Object[] values = (pks == null || pks.isEmpty())
        ? null : pks.iterator().next().getValues();
    return (values != null && values.length > 0 && values[0] instanceof BigDecimal)
        ? (BigDecimal) values[0] : null;
}
```

> `getDefaultValueObjectInstance` cria VO com todos os defaults da entidade preenchidos —
> equivalente a abrir um novo registro na tela. Sempre use isso em vez de `new DynamicVO()`
> para entidades nativas.

---

## Calcular Impostos e Totalizar Nota

Após criar a nota e adicionar os itens, calcule os impostos e totalize:

```java
import br.com.sankhya.jape.util.JapeSessionContext;
import br.com.sankhya.modelcore.comercial.impostos.ImpostosHelpper;

public void totalizarSalvarImpostos(BigDecimal nuNota) throws Exception {
    JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);
    try {
        ImpostosHelpper helper = new ImpostosHelpper();
        helper.carregarNota(nuNota);
        helper.calcularImpostos(nuNota);
        helper.calcularPIS();
        helper.calcularCOFINS();
        helper.calcularCSSL();
        helper.totalizarNota(nuNota);
        helper.salvarNota();
    } finally {
        JapeSessionContext.removeProperty("br.com.sankhya.com.CentralCompraVenda");
    }
}
```

### Forçar recálculo após adicionar itens programaticamente

```java
ImpostosHelpper helper = new ImpostosHelpper();
helper.setForcarRecalculo(true); // obrigatorio quando itens foram adicionados via codigo
helper.carregarNota(nuNota);
helper.calcularImpostos(nuNota);
helper.calcularPIS();
helper.calcularCOFINS();
helper.calcularCSSL();
helper.calcularISS(nuNota);
helper.totalizarNota(nuNota);
helper.salvarNota();
```

> `setForcarRecalculo(true)` obrigatório quando itens são adicionados programaticamente —
> sem isso o helper pode ignorar os novos itens se já houver impostos calculados.

---

## Refazer Financeiro

```java
import br.com.sankhya.modelcore.comercial.CentralFinanceiro;

public void refazerFinanceiro(BigDecimal nuNota) throws Exception {
    JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);
    try {
        CentralFinanceiro cf = new CentralFinanceiro();
        cf.inicializaNota(nuNota);
        cf.refazerFinanceiro();
    } finally {
        JapeSessionContext.removeProperty("br.com.sankhya.com.CentralCompraVenda");
    }
}
```

---

## Confirmar Nota

### Confirmação via BarramentoRegra (síncrona)

Para confirmar sem exibir popups de liberação:

```java
import br.com.sankhya.modelcore.comercial.BarramentoRegra;
import br.com.sankhya.modelcore.comercial.CentralFaturamento;
import br.com.sankhya.modelcore.comercial.ConfirmacaoNotaHelper;

public void confirmarSilencioso(BigDecimal nuNota) throws Exception {
    AuthenticationInfo auth = AuthenticationInfo.getCurrent();

    BarramentoRegra barramento = BarramentoRegra.build(
        CentralFaturamento.class,
        "regrasConfirmacaoSilenciosa.xml",
        auth
    );
    barramento.setValidarSilencioso(true);
    ConfirmacaoNotaHelper.confirmarNota(nuNota, barramento);
}
```

### Confirmação assíncrona (após commit da transação atual)

Usar quando a nota foi criada na mesma transação e o commit ainda não ocorreu:

```java
import br.com.sankhya.modelcore.PlatformService;
import br.com.sankhya.modelcore.PlatformServiceFactory;

public static void confirmarAsync(BigDecimal nunota, AuthenticationInfo auth) {
    Thread t = new Thread(() -> {
        JapeSession.SessionHandle hnd = null;
        ServiceContext sctx = null;
        try {
            hnd = JapeSession.open();
            auth.makeCurrent();

            sctx = new ServiceContext(null);
            sctx.setAutentication(auth);
            sctx.setRequestBody(new org.jdom.Element("requestBody"));
            sctx.makeCurrent();

            Thread.sleep(1000); // aguarda commit da nota

            PlatformService svc = PlatformServiceFactory.getInstance()
                .lookupService("@core:confirmacao.nota.service");
            svc.set("NUNOTA", nunota);
            svc.execute();

        } catch (Exception e) {
            Logger.error(getClass(), "Falha ao confirmar NUNOTA " + nunota + ": " + e.getMessage(), e);
        } finally {
            if (sctx != null) sctx.unregistry();
            JapeSession.close(hnd);
        }
    }, "ConfirmaNota-" + nunota.toPlainString());
    t.setDaemon(true);
    t.start();
}
```

> Prefira confirmação síncrona. A assíncrona usa `Thread.sleep` como workaround — em alta
> concorrência pode haver race condition entre o sleep e o commit real.

---

## Fluxo Completo de Faturamento

```java
import br.com.sankhya.jape.util.JapeSessionContext;
import br.com.sankhya.modelcore.comercial.BarramentoRegra;
import br.com.sankhya.modelcore.comercial.CentralFinanceiro;
import br.com.sankhya.modelcore.comercial.CentralFaturamento;
import br.com.sankhya.modelcore.comercial.ConfirmacaoNotaHelper;
import br.com.sankhya.modelcore.comercial.centrais.CACHelper;
import br.com.sankhya.modelcore.comercial.impostos.ImpostosHelpper;

public BigDecimal faturar(BigDecimal codRegistro, BigDecimal codEmp, BigDecimal codParc,
                           BigDecimal codTipVenda, BigDecimal codNat,
                           BigDecimal codTipOper, BigDecimal codProd,
                           BigDecimal quantidade, BigDecimal vlrUnitario) throws Exception {

    // 1. Criar cabeçalho via CACHelper — nunca via JapeWrapper direto
    BigDecimal nuNota = criarNota(codEmp, codParc, codTipVenda, codNat, codTipOper, "V");

    // 2. Adicionar itens
    JapeFactory.dao(DynamicEntityNames.ITEM_NOTA).create()
        .set("NUNOTA",  nuNota)
        .set("CODPROD", codProd)
        .set("QTDNEG",  quantidade)
        .set("VLRUNIT", vlrUnitario)
        .save();

    // 3. Calcular impostos, totalizar e refazer financeiro
    JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);
    try {
        ImpostosHelpper helper = new ImpostosHelpper();
        helper.setForcarRecalculo(true);
        helper.carregarNota(nuNota);
        helper.calcularImpostos(nuNota);
        helper.calcularPIS();
        helper.calcularCOFINS();
        helper.calcularCSSL();
        helper.calcularISS(nuNota);
        helper.totalizarNota(nuNota);
        helper.salvarNota();

        CentralFinanceiro cf = new CentralFinanceiro();
        cf.inicializaNota(nuNota);
        cf.refazerFinanceiro();
    } finally {
        JapeSessionContext.removeProperty("br.com.sankhya.com.CentralCompraVenda");
    }

    // 4. Confirmar nota (se a TOP permitir)
    if (deveConfirmar(nuNota)) {
        AuthenticationInfo auth = AuthenticationInfo.getCurrent();
        BarramentoRegra barramento = BarramentoRegra.build(
            CentralFaturamento.class,
            "regrasConfirmacaoSilenciosa.xml",
            auth
        );
        barramento.setValidarSilencioso(true);
        ConfirmacaoNotaHelper.confirmarNota(nuNota, barramento);
    }

    // 5. Marcar registro de origem como faturado
    JapeFactory.dao("AD_MINHAENTIDADE")
        .prepareToUpdateByPK(codRegistro)
        .set("STATUS", "F")
        .set("NUNOTA",  nuNota)
        .set("DHALTER", TimeUtils.getNow())
        .update();

    return nuNota;
}

private boolean deveConfirmar(BigDecimal nuNota) throws Exception {
    DynamicVO cabVo = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);
    if (cabVo == null) return false;
    DynamicVO topVo = JapeFactory.dao(DynamicEntityNames.TIPO_OPERACAO)
        .findByPK(cabVo.asBigDecimal("CODTIPOPER"));
    return topVo != null && !"S".equals(topVo.asString("NAOINCCONF"));
}
```

---

## JapeSession — execWithTX e execWithFakeTX

### execWithTX — bloco com commit

```java
JapeSession.SessionHandle hnd = JapeSession.open();
try {
    final BigDecimal[] resultHolder = new BigDecimal[1];

    hnd.execWithTX(() -> {
        BigDecimal nuNota = criarNota(...);
        adicionarItens(nuNota, ...);
        resultHolder[0] = nuNota;
    });

    BigDecimal nuNota = resultHolder[0]; // disponível após o commit
} finally {
    JapeSession.close(hnd);
}
```

### execWithFakeTX — bloco sem commit (dry-run)

Útil para calcular impostos sem persistir — cria nota temporária, calcula, descarta:

```java
AtomicReference<ImpostosCalculadosDto> atomicDTO = new AtomicReference<>();

// Executa sem commit — todas as operações de banco são revertidas ao final
hnd.execWithFakeTX(() -> {
    BigDecimal nuNota = criarNota(...);
    adicionarItens(nuNota, ...);
    calcularImpostos(nuNota, atomicDTO); // preenche o DTO
});

// Persiste apenas os valores calculados
hnd.execWithTX(() -> {
    ImpostosCalculadosDto dto = atomicDTO.get();
    if (dto == null) return;
    JapeFactory.dao("AD_MINHAENTIDADE")
        .prepareToUpdateByPK(dto.getCodRegistro())
        .set("VLRISS",   dto.getIss())
        .set("VLRINSS",  dto.getInss())
        .set("VLRPIS",   dto.getPis())
        .set("VLRCOFINS", dto.getCofins())
        .update();
});
```

> Use `AtomicReference` ou `new BigDecimal[1]` para passar dados calculados para fora do
> bloco lambda — variáveis locais usadas em lambdas precisam ser efetivamente finais.

---

## JapeSessionContext — Flag de Contexto Comercial

```java
import br.com.sankhya.jape.util.JapeSessionContext;

// Necessário antes de ImpostosHelpper e CentralFinanceiro
JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);

// Sempre remover no finally — não contaminar outras operações da sessão
JapeSessionContext.removeProperty("br.com.sankhya.com.CentralCompraVenda");
```
