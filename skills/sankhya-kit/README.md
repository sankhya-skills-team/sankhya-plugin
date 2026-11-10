# sankhya-kit

Skill para Claude Code com o **comportamento do kit de produtos no core do Sankhya OM** (4.35/4.36), confirmado em runtime e no bytecode.

## O que esta skill faz

- Explica a composição do kit (`TGFPRO.TIPOKIT`, `TGFICP`, `TGFFCP`) e o kit independente (`CONFKITIND`, `TSIKIT`)
- Mostra quando o kit abre em componentes `USOPROD='D'` e quem decide a baixa e a reserva de estoque no pedido e na nota
- Cobre os parâmetros `INIBESELECUSOPD`, `ATUALEMPRODKIT`, `COMCONSKITIMPIT`, `HABSUPORTEKITSW` e `HABSUBSKITIND`
- Trata impressão e imposto do kit (`TGFTOP.TIPOIMPKIT`) e a validação de saldo dos componentes
- Explica os erros `CORE_E01199`, `CORE_E04505`, `CORE_E04697`, `CORE_E03880` e `CORE_E03881`
- Traz um roteiro de teste e as consultas de conferência

## Quando acionar

> kit · kit de peças · kit no pedido · kit no faturamento · kit baixa estoque · baixar só os componentes · componente D · Configuração de Kit · kit independente · reserva presa do componente · kit sem saldo

Vale ao implementar, revisar, estimar, homologar ou dar suporte a qualquer coisa que envolva kit, em addon ou módulo.

## Estrutura da skill

```
sankhya-kit/
├── SKILL.md              Instruções da skill (carregadas pelo Claude Code)
├── README.md             Este arquivo
└── references/
    ├── core.md           Composição, estoque, reserva, flags, impostos e validações
    └── como-testar.md    Troca de parâmetro, roteiro de teste e consultas de conferência
```
