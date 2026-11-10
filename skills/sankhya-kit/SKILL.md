---
name: sankhya-kit
description: >
  Comportamento do kit de produtos no core do Sankhya OM (4.35/4.36): composição (TGFPRO.TIPOKIT,
  TGFICP, TGFFCP), kit independente (CONFKITIND, TSIKIT / tela Configuração de Kit), abertura dos
  componentes USOPROD='D', reserva e baixa de estoque do kit e dos componentes no pedido e na nota,
  faturamento pelo Portal de Vendas, impostos e impressão do kit (TGFTOP.TIPOIMPKIT), parâmetros
  INIBESELECUSOPD, ATUALEMPRODKIT, COMCONSKITIMPIT, HABSUPORTEKITSW, HABSUBSKITIND e as validações
  de saldo dos componentes. Usar ao implementar, revisar, estimar, homologar ou dar suporte a
  qualquer coisa que envolva kit em addon ou módulo Sankhya. Gatilhos: "kit", "kit de peças",
  "kit no pedido", "kit no faturamento", "kit na nota", "kit baixa estoque", "baixar só os
  componentes", "componente D", "matéria-prima no pedido de venda", "TIPOKIT", "TGFICP",
  "Configuração de Kit", "TSIKIT", "kit independente", "INIBESELECUSOPD", "TIPOIMPKIT",
  "ATUALEMPRODKIT", "reserva presa do componente", "kit sem saldo", "CORE_E01199", "CORE_E04505",
  "CORE_E04697", "CORE_E03881", "estoque.insuficiente.produto".
---

# Kit no core do Sankhya OM

Conhecimento confirmado em runtime (core 4.35b844) e no bytecode descompilado (`mgecom-model`,
`mge-modelcore`). Vale para qualquer addon ou módulo.

## Conclusão que mais importa

**Nenhuma configuração do core faz a nota baixar só os componentes e deixar o kit parado.**
A linha do kit segue o `ATUALEST` da TOP, e o gatilho `TRG_INC_TGFITE` recusa qualquer outra baixa
("Atualização de estoque diferente da definição na TOP."). Para o kit não movimentar estoque, o
documento não pode levar o kit: o pedido tem de ir com os componentes como itens comuns (e aí vale
o CORE_E01199, ver abaixo).

## Decisão rápida

| Quero... | Como fica |
|---|---|
| Nota baixar os componentes | `TSIPAR.INIBESELECUSOPD=N` + TOP de faturamento com `ATUALESTMP=-1`. O kit **também** baixa (`ATUALEST=B`) |
| Nota baixar só o kit | `INIBESELECUSOPD=S` (padrão de muitas bases). Os `D` do pedido ficam pendentes e reservando |
| Kit não baixar | Só sem o kit no documento (componentes como itens comuns), ou TOP própria com `ATUALEST=N` |
| Imposto nos componentes | `TGFTOP.TIPOIMPKIT=C` (aba Impressão da TOP) |
| Custo do kit igual aos componentes | `TSIKIT.SOMACUSTOCOMPKIT=S` |
| Componente vendido avulso | `TGFPRO.VENCOMPINDIV='S'` ou TOP em `com.lista.tops.para.venda.individual.componentes` |

## Referências

- **`references/core.md`**: composição, abertura dos `D`, baixa e reserva por linha, o
  `INIBESELECUSOPD`, flags da `TSIKIT`, `TIPOIMPKIT` e impostos, parâmetros de kit da TSIPAR,
  validação de saldo dos componentes, configuração de um cliente em que funciona.
- **`references/como-testar.md`**: trocar parâmetro sem reiniciar (Preferências + Descartar Cache),
  TOP e suas versões, roteiro pedido → nota → limpeza, consultas de conferência.

