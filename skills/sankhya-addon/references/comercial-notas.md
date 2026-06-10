# Integração com o Núcleo Comercial do Sankhya

Padrões reais para criar notas fiscais, calcular impostos, confirmar notas e refazer financeiro programaticamente a partir de um add-on.

> Estes padrões são do Add-on Studio 1.0 (SPBean). As classes do núcleo comercial (`BarramentoRegra`, `CACHelper`, `ImpostosHelpper`, `CentralFinanceiro`) são as mesmas em ambas as versões.

---

## Criar Nota Fiscal via BarramentoRegra + CACHelper

O caminho correto para criar uma nota fiscal programaticamente é via `CACHelper` — não via `JapeWrapper.create()` diretamente na entidade `CabecalhoNota`. O `CACHelper` aciona o barramento de regras e garante que todos os defaults e validações do Sankhya sejam aplicados.

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

> `getDefaultValueObjectInstance` cria um VO com todos os defaults da entidade ja preenchidos — equivalente a abrir um novo registro na tela. Sempre use isso em vez de `new DynamicVO()` para entidades nativas.

---

## Calcular Impostos e Totalizar Nota

Apos criar a nota e adicionar os itens, calcule os impostos e totalize:

```java
import br.com.sankhya.jape.util.JapeSessionContext;
import br.com.sankhya.modelcore.comercial.impostos.ImpostosHelpper;

public void totalizarSalvarImpostos(BigDecimal nuNota) throws Exception {
    // Flag necessaria para o contexto de compra/venda
    JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);

    ImpostosHelpper helper = new ImpostosHelpper();
    helper.carregarNota(nuNota);
    helper.calcularImpostos(nuNota);
    helper.calcularPIS();
    helper.calcularCOFINS();
    helper.calcularCSSL();
    helper.totalizarNota(nuNota);
    helper.salvarNota();
}
```

### Forçar recálculo de impostos após adicionar itens

Quando os itens são adicionados programaticamente e os impostos precisam ser recalculados do zero:

```java
ImpostosHelpper helper = new ImpostosHelpper();
helper.setForcarRecalculo(true); // força recálculo mesmo que já existam impostos calculados
helper.carregarNota(nuNota);
helper.calcularImpostos(nuNota);
helper.calcularPIS();
helper.calcularCOFINS();
helper.calcularCSSL();
helper.totalizarNota(nuNota);
helper.salvarNota();
```

> Use `setForcarRecalculo(true)` sempre que adicionar itens programaticamente — sem isso, o helper pode ignorar os novos itens se já houver impostos calculados na nota.

---

## Refazer Financeiro

Apos totalizar, refaca o financeiro para gerar os titulos:

```java
import br.com.sankhya.modelcore.comercial.CentralFinanceiro;

public void refazerFinanceiro(BigDecimal nuNota) throws Exception {
    JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);

    CentralFinanceiro cf = new CentralFinanceiro();
    cf.inicializaNota(nuNota);
    cf.refazerFinanceiro();
}
```

---

## Confirmar Nota

### Confirmacao via BarramentoRegra (silenciosa)

Para confirmar sem exibir popups de liberacao:

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

### Confirmacao via PlatformService (thread separada)

Quando a confirmacao precisa ocorrer apos o commit da transacao atual (ex: a nota foi criada na mesma transacao e o commit ainda nao ocorreu):

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

            // Aguarda o commit da nota antes de confirmar
            Thread.sleep(1000);

            PlatformService svc = PlatformServiceFactory.getInstance()
                .lookupService("@core:confirmacao.nota.service");
            svc.set("NUNOTA", nunota);
            svc.execute();

        } catch (Exception e) {
            System.out.println("Falha ao confirmar NUNOTA " + nunota + ": " + e.getMessage());
        } finally {
            if (sctx != null) sctx.unregistry();
            JapeSession.close(hnd);
        }
    }, "ConfirmaNota-" + nunota.toPlainString());
    t.setDaemon(true);
    t.start();
}
```

> Use a confirmacao assincrona com cautela — o `Thread.sleep` e um workaround para garantir que o commit da nota ocorra antes da confirmacao. Em cenarios de alta concorrencia, prefira a confirmacao sincrona via `BarramentoRegra`.

---

## Fluxo Completo de Faturamento

Sequência típica para faturar um registro via nota fiscal. Cada etapa usa diretamente as APIs do Sankhya — não há interfaces intermediárias obrigatórias:

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

    // 1. Criar cabeçalho da nota via CACHelper (nunca via JapeWrapper direto)
    // Ver seção "Criar Nota Fiscal via BarramentoRegra + CACHelper" neste arquivo
    BigDecimal nuNota = criarNota(codEmp, codParc, codTipVenda, codNat, codTipOper, "V");

    // 2. Adicionar itens via JapeWrapper na entidade ItemNota
    JapeFactory.dao(DynamicEntityNames.ITEM_NOTA).create()
        .set("NUNOTA",  nuNota)
        .set("CODPROD", codProd)
        .set("QTDNEG",  quantidade)
        .set("VLRUNIT", vlrUnitario)
        .save();

    // 3. Calcular impostos e totalizar
    JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);
    try {
        ImpostosHelpper helper = new ImpostosHelpper();
        helper.setForcarRecalculo(true); // obrigatório quando itens foram adicionados programaticamente
        helper.carregarNota(nuNota);
        helper.calcularImpostos(nuNota);
        helper.calcularPIS();
        helper.calcularCOFINS();
        helper.calcularCSSL();
        helper.calcularISS(nuNota);
        helper.totalizarNota(nuNota);
        helper.salvarNota();

        // 4. Refazer financeiro
        CentralFinanceiro cf = new CentralFinanceiro();
        cf.inicializaNota(nuNota);
        cf.refazerFinanceiro();
    } finally {
        JapeSessionContext.removeProperty("br.com.sankhya.com.CentralCompraVenda");
    }

    // 5. Confirmar nota (se a TOP permitir)
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

    // 6. Marcar o registro de origem como faturado
    JapeFactory.dao("MinhaEntidade")
        .prepareToUpdateByPK(codRegistro)
        .set("STATUS", "F")
        .set("NUNOTA",  nuNota)
        .set("DHALTER", TimeUtils.getNow())
        .update();

    return nuNota;
}
```

### Verificar se a TOP permite confirmação automática

```java
private boolean deveConfirmar(BigDecimal nuNota) throws Exception {
    DynamicVO cabVo = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);
    if (cabVo == null) return false;
    DynamicVO topVo = JapeFactory.dao(DynamicEntityNames.TIPO_OPERACAO)
        .findByPK(cabVo.asBigDecimal("CODTIPOPER"));
    return topVo != null && !"S".equals(topVo.asString("NAOINCCONF"));
}
```

---

## DynamicEntityNames — Constantes de Entidades Nativas

Use sempre as constantes em vez de strings literais:

```java
import br.com.sankhya.modelcore.util.DynamicEntityNames;

JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA)  // "CabecalhoNota"
JapeFactory.dao(DynamicEntityNames.EMPRESA)          // "Empresa"
JapeFactory.dao(DynamicEntityNames.PARCEIRO)         // "Parceiro"
JapeFactory.dao(DynamicEntityNames.CONTRATO)         // "Contrato"
JapeFactory.dao(DynamicEntityNames.FUNCIONARIO)      // "Funcionario"
```

---

## JapeSessionContext — Flags de Contexto

Algumas operacoes do nucleo comercial exigem flags no contexto da sessao JAPE:

```java
import br.com.sankhya.jape.util.JapeSessionContext;

// Necessario antes de calcular impostos e refazer financeiro
JapeSessionContext.putProperty("br.com.sankhya.com.CentralCompraVenda", true);

// Sempre limpar a flag apos o uso (no bloco finally)
JapeSessionContext.removeProperty("br.com.sankhya.com.CentralCompraVenda");
```

> Sem essa flag, `ImpostosHelpper` e `CentralFinanceiro` podem nao funcionar corretamente em contextos de add-on. Sempre remova a flag no `finally` para nao contaminar outras operacoes na mesma sessao.

---

## JapeSession.SessionHandle — Controle Explícito de Transação

Quando você tem acesso ao `SessionHandle`, pode controlar transações explicitamente:

### execWithTX — Executar bloco com commit

```java
JapeSession.SessionHandle hnd = JapeSession.open();
try {
    final BigDecimal[] resultHolder = new BigDecimal[1];

    hnd.execWithTX(() -> {
        BigDecimal codRegistro = registroService.incluir(cab, referencia, null, null);
        dadosService.carregar(codRegistro, referencia, contrato, func, dep);
        resultHolder[0] = codRegistro;
    });

    // resultHolder[0] disponível após o commit
    BigDecimal codRegistro = resultHolder[0];
} finally {
    JapeSession.close(hnd);
}
```

### execWithFakeTX — Executar bloco sem commit (dry-run)

Útil para calcular valores sem persistir — por exemplo, criar uma nota temporária para calcular impostos e depois descartar:

```java
AtomicReference<ImpostosCalculadosDto> atomicDTO = new AtomicReference<>();

// Executa sem commit — todas as operações de banco são revertidas ao final
hnd.execWithFakeTX(() -> {
    BigDecimal nuNota = cabecalhoSvc.gerarCabecalho(codRegistro, false);
    itensSvc.adicionarItens(nuNota, codRegistro);
    impostosSvc.calcularImpostos(codRegistro, nuNota, atomicDTO);
});

// Agora persiste apenas os valores calculados
hnd.execWithTX(() -> {
    ImpostosCalculadosDto dto = atomicDTO.get();
    if (dto == null) return;
    JapeFactory.dao("MinhaEntidade")
        .prepareToUpdateByPK(dto.getCodRegistro())
        .set("ISS",    dto.getIss())
        .set("INSS",   dto.getInss())
        .set("PIS",    dto.getPis())
        .set("COFINS", dto.getCofins())
        .update();
});
```

> `execWithFakeTX` é equivalente a um rollback automático — todas as operações dentro do bloco são desfeitas ao final. Use `AtomicReference` ou array de um elemento (`new BigDecimal[1]`) para passar dados calculados para fora do bloco lambda.

### Obter o SessionHandle atual

```java
// Abrir nova sessão
JapeSession.SessionHandle hnd = JapeSession.open();

// Reutilizar sessão já existente (quando há uma sessão ativa na thread)
JapeSession.SessionHandle hnd = JapeSession.getCurrentSession().getTopMostHandle();
```

---

## TimeUtils — Data/Hora Atual

```java
import com.sankhya.util.TimeUtils;

Timestamp agora = TimeUtils.getNow(); // equivalente a new Timestamp(System.currentTimeMillis())
```

