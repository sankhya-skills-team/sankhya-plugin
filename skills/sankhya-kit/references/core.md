# Kit no core 4.35b844: pedido, nota, estoque e impostos

## O que é kit para o core

- Produto com `TGFPRO.TIPOKIT` preenchido: `D` (Composição Padrão) ou `P` (Composição
  Personalizada). A composição de kit fica na `TGFICP` com `VARIACAO=30000`, `CODLOCAL=0` e
  `CONTROLE=' '`, filtro que a separa das fórmulas de produção (mesmo critério de
  `SuporteKitHelper_queTemComponente.sql`). A cadeia `TGFFCP → TGFEPR → TGFICP` precisa existir (FK);
  a explosão usa a fórmula principal (`TGFFCP.FORMPRINCIPAL='S'`). O core de kit não consulta a TPRLPA.
- Kit independente: `TSIPAR.CONFKITIND=S` (`com.configuracao.kit.independente`) e
  `TGFPRO.CODCONFKIT` → `TSIKIT` (tela **Configuração de Kit**, `br.com.sankhya.mge.configuracao.kit`).
- A abertura do kit em itens `USOPROD='D'` só acontece na **inclusão ou alteração do item pela
  Central/CAC** (`SuporteKit.afterInsert/afterUpdate` → `KitIndependenteHelper.explodirComponentes`,
  com `TSIKIT.EXPLODCOMP='S'`). O faturamento e a confirmação **não** abrem o kit.
- Os `D` ficam ligados ao kit pela `TGFVAR` da própria nota (`NUNOTAORIG=NUNOTA`,
  `SEQUENCIAORIG` = item do kit). Quantidade do `D` = `QTDMISTURA × QTDNEG` do kit, **sem
  arredondar** pelo `DECQTD` do componente.
- Componente de kit vendido como item avulso: **CORE_E01199** "O produto X faz parte de um kit e não
  pode ser vendido separadamente" (`SuporteKit`, venda e `USOPROD` fora de `M`/`D`), a não ser que
  `TGFPRO.VENCOMPINDIV='S'` ("Aceitar venda fora do KIT") ou a TOP esteja em
  `com.lista.tops.para.venda.individual.componentes`.

## Quem decide a baixa de estoque

| Linha | Campo da TOP | Observação |
|---|---|---|
| Kit (USOPROD do produto, ex.: `R`/`V`) | `ATUALEST` (`B` = -1, `E`/`R` = 1, `N` = 0) | Sem exceção para kit no `CentralFaturamento` nem flag no produto |
| Componente `D` | `ATUALESTMP` (-1 baixa, 0 nada, 1 entra, 2 reserva) | Com `ATUALEMPRODKIT=N` o `D` usa o `ATUALEST` (`ComercialUtils.usaAutalestMP`) |

- `TRG_INC_TGFITE` (~linhas 305-315) recusa item não `D` com `ATUALESTOQUE` diferente da TOP. Addon
  **não** consegue zerar a baixa do kit numa TOP que baixa. `D` com `ATUALESTOQUE=0` é aceito.
- TOP de faturamento com `ATUALEST=N` e `ATUALESTMP=-1`: kit não baixa e os `D` baixam, mas as peças
  avulsas da mesma nota também deixam de baixar. Só serve com TOP própria para kit.
- TOP de pedido que reserva (`ATUALEST='R'`) reserva o kit **e** os `D`; sem saldo do próprio kit
  cria TSILIB evento 10 do kit.

## Nota de entrada (compra, ajuste) com kit

A abertura dos `D` com kit independente vale para **qualquer** `TIPMOV`, compra inclusive
(`SuporteKit.validarSuporteKit`; a exceção `ehMPKitCompra` só vale fora do kit independente).
Quem decide o saldo é a TOP de entrada:

| TOP de entrada | Kit | Componentes `D` |
|---|---|---|
| `ATUALEST=E`, `ATUALESTMP=1` | entra | **entram também** (confirmado em runtime: nota de ajuste com kit +1 e cada componente + composição) |
| `ATUALEST=E`, `ATUALESTMP=0` | entra | não mexem (pelo core; não testado) |
| `ATUALEST=E`, `ATUALESTMP=-1` | entra | **baixam** (montagem: entra o kit, saem os componentes; pelo core e pelo `ehMPKitCompra`) |

- Com `ADIARATUALEST=S` todos os itens ficam `ATUALESTOQUE=0` até a confirmação; na confirmação o
  `D` recebe o `ATUALESTMP` quando `ATUALEMPRODKIT=S`, ou o `ATUALEST` da TOP (`E` → 1) quando
  `ATUALEMPRODKIT=N` (`ComercialUtils.usaAutalestMP`). Ou seja, com `ATUALEMPRODKIT=N` os componentes
  podem entrar mesmo numa TOP com `ATUALESTMP=0`.
- Para só o kit ganhar saldo: TOP de entrada com `ATUALESTMP=0` e `ATUALEMPRODKIT=S`, ou kit sem
  `EXPLODCOMP` (só aceito em kit `TIPOKIT='P'`).

## Pedido → nota: os componentes vão ou não?

`TSIPAR.INIBESELECUSOPD` (`inibe.exibicao.materia.prima.vendas`, "Inibir exibição de MP nos
movimentos de vendas?"), lido no `CentralFaturamento`: com pedido de origem a seleção ganha
`AND TGFITE.USOPROD <> 'D'`.

| `INIBESELECUSOPD` | Nota (TOP `ATUALEST=B`, `ATUALESTMP=-1`) | Estoque e reserva |
|---|---|---|
| `S` | Só o kit | Kit baixa o próprio estoque; os `D` do pedido ficam **pendentes e reservando para sempre** |
| `N` | Kit + `D` com as quantidades do pedido | `D` baixam e liberam a reserva; pedido todo atendido; **o kit também baixa** |

Vale para todas as vendas da base. O valor da nota não muda (os `D` não somam no total).

## Flags da Configuração de Kit (`TSIKIT`)

Testadas uma a uma: **nenhuma muda a baixa de estoque**.

| Flag (tela) | Coluna | Efeito |
|---|---|---|
| Calcula imposto do componente | `CALCIMPKIT` | Nada visível no pedido (ICMS dos `D` continuou 0) |
| Soma custo do componente ao kit | `SOMACUSTOCOMPKIT` | `CUSTO` do kit = Σ custo × quantidade dos `D` |
| Soma preço do componente ao kit | `SOMAPRECOCOMPKIT` | Preço do kit = Σ preço dos `D` |
| Distribuir preço do kit nos componentes | `DISTRIBUIKITCOMP` | Rateia o total do kit nos `D` (proporção do core, não da tabela; o último absorve a diferença) |
| Distribuir desconto do kit nos componentes | `DISTDESCKITCOMP` | Rateia o desconto do kit nos `D` |
| Explodir componentes na grade de MP da central | `EXPLODCOMP` | Sem explosão não há `D`. Não grava se a configuração estiver ligada a kit `TIPOKIT='D'` (CORE_E04505) |
| Faturar apenas KIT com estoque de todos os componentes | `FAKITESTCOMP` | Só atua com componente sem saldo, no faturamento (`validaKitCompleto`) |
| (sem campo na tela) | `UTILPRECOABACOMP` | Usa `TGFICP.PRECO` com `com.informar.preco.componente.kit` |

A tela recusa "Distribuir preço" junto com "Soma custo" ou "Soma preço".

## Impressão e imposto do kit (`TGFTOP.TIPOIMPKIT`)

Aba **Impressão** da TOP, "Kit/Componentes - Impressão e Livro Fiscal": `K` Kit, `C` Componentes,
`T` Kit e Componentes. Não mexe em estoque.

- `K`: ICMS no kit; os `D` são ignorados (`ImpostosHelpper.ignorarPelaTOP`).
- `C`: o cálculo pula o **kit** que tem `D` ligados pela TGFVAR. No faturamento pelo Portal o ICMS do
  kit vem copiado do pedido e a nota ainda não confirmada fica com **ICMS em dobro** (kit +
  componentes). Na nota confirmada de um cliente com `C` o kit está com `BASEICMS=0` (o recálculo da
  confirmação zera o kit; não verificado em base clone por causa da SEFAZ).
- Faturar pedido de TOP com `TIPOIMPKIT` diferente da TOP destino: CORE_E04697.

## Validação de saldo dos componentes

- Na abertura do kit (`KitIndependenteHelper.validaEstoqueComp`), para cada `D` com baixa
  (`ATUALESTOQUE=-1`) ou reserva em TOP que valida estoque (`VALEST`): saldo `ComercialUtils.validaEstoque`
  menor que a quantidade →
  - grupo com validação `A` (avisar): o core lê a chave de sessão
    `central.notas.pode.efetivar_<CODPROD>`; ausente → lança o ClientEvent
    `br.com.sankhya.mgecomercial.event.estoque.insuficiente.produto` (sem tela registrada: "Erro
    interno ... há ClientEvents não registrados"); `"true"` aceita; `"false"` recusa (CORE_E03881);
  - produto inativo ou sem TGFEST: CORE_E03880.
- Item avulso vai por outro caminho (`EstoqueHelpper.validarEstoqueV2`).

## Outros parâmetros de kit da TSIPAR

| Chave | Parâmetro | Efeito |
|---|---|---|
| `ATUALEMPRODKIT` | `com.considerar.atualestmp.produto.kit` | `S`: `D` usa o `ATUALESTMP`; `N`: usa o `ATUALEST`. Com `B`/`-1` dá na mesma |
| `COMCONSKITIMPIT` | `mgecom.considera.kit.no.calcular.impostos.item` | Considera o kit no cálculo de impostos do item |
| `HABSUPORTEKITSW` | `com.habilitar.suporte.kit.sw` | Suporte a kit do SankhyaW (fluxo antigo `SuporteKitHelper`/`ItemNotaCrudListener`); sem efeito no estoque |
| `HABSUBSKITIND` | `com.hab.subst.kit.independente` | Substituição de kit independente |

Sem linha na TSIPAR vale o `default` do XML do core (`mgecomercial/parameters/mge-com.xml`,
`modelcore/parameters/mge-core.xml`). Chave ↔ nome: `unzip -p <jar> <xml> | grep -a -A8 '"CHAVE"'`.

## Configuração de um cliente em que "funciona"

`INIBESELECUSOPD=N`, `CONFKITIND=S`, `ATUALEMPRODKIT=N`, `COMCONSKITIMPIT=N`, `HABSUPORTEKITSW=S`,
`HABSUBSKITIND=N`; TOP do pedido `ATUALEST=N` (não reserva); TOP de faturamento `B` / `-1` /
`TIPOIMPKIT=C`; kit `TIPOKIT='D'`, `VENCOMPINDIV='S'`. Lá o kit **também baixa** na nota; funciona
porque o kit é estocado (saldo positivo). Não serve para kit sem saldo próprio.
