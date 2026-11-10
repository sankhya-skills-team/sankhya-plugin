# sankhya-bi

Skill para Claude Code especializada em **dashboards e componentes de BI (gadgets)** do Sankhya OM, feitos no Construtor de Componentes de BI.

## O que esta skill faz

- Gera o XML do gadget (`TSIGDG.CONFIG`) pronto para importar
- Monta gráficos (pizza, barras, colunas, linha), tabelas e parâmetros de filtro
- Configura níveis de drill-down, eventos e ações entre componentes
- Cria dashboards customizados com o componente HTML5
- Aplica as regras obrigatórias de geração de XML e indica onde salvar os arquivos

## Quando acionar

> criar dashboard · componente de BI · gadget · gráfico de pizza/barras/colunas/linha · tabela no dashboard · parâmetro de filtro · gerar XML do dashboard · dashboard de estoque/financeiro/vendas

## Estrutura da skill

```
sankhya-bi/
├── SKILL.md                              Instruções da skill (carregadas pelo Claude Code)
├── README.md                             Este arquivo
├── examples/
│   └── template-tabela-operacional.html  Modelo de tabela operacional em componente HTML5
└── references/
    ├── 01-introducao-design.md           Introdução e desenho do dashboard
    ├── 02-controles.md                   Controles e parâmetros
    ├── 03-graficos.md                    Gráficos
    ├── 04-configuracoes-logica.md        Configurações e lógica
    ├── 05-eventos-acoes.md               Eventos e ações
    ├── 06-html5-component.md             Componente HTML5
    └── 07-padroes-xml-avancados.md       Padrões avançados de XML
```

## Skills relacionadas

- `sankhya-relatorio` e `sankhya-relatorio-visual`: documento imprimível (JasperReports), não dashboard
- `sankhya-dicionario`: tabelas e campos usados nas consultas
