# sankhya-js

Skill para Claude Code especializada no **framework frontend `sankhya-js`** (AngularJS 1.x) do Sankhya OM, usado nas telas HTML5.

## O que esta skill faz

- Chama serviços backend por `/mge/service.sbr` com `ServiceProxy` e `FluidBuilder`
- Declara componentes: botão, popup, grid, dataset, datagrid, wizard, pesquisa e outros
- Obtém metadados de entidade com `MetadataProvider` e textos com `SkI18nService`
- Registra módulos dinamicamente (`$SkInjectorProvider`, `SkComponentRegistry`, `SkWorkspace`)
- Compartilha telas entre módulos em `src/commons`
- Avisa das armadilhas: tela custom roda em iframe e colide com Bootstrap

## Quando acionar

Ao escrever, alterar ou revisar código AngularJS do `sankhya-js`: telas HTML5, consumo de serviço, componentes, metadados, i18n, e o uso do framework pelos módulos VC (`MGE-Base-VC`, `MGE-Fin-VC`, `MGE-Checkout-VC`) em JSPs.

## Estrutura da skill

```
sankhya-js/
├── SKILL.md       Instruções da skill (carregadas pelo Claude Code)
├── README.md      Este arquivo
├── reference/     19 guias: aplicação, datagrid, dataset, formulário, filtros, inputs, mensagens e popup,
│                  navegação, pesquisa, abas, wizard, build com Grunt, padrões, anti-padrões e armadilhas
└── templates/     7 modelos: diretiva de componente, dataset isolado, interceptor de filtro, popup custom,
                   chamada de serviço (simples e com builder) e passo de wizard
```

## Skills relacionadas

- `sankhya-addon`: tela personalizada dentro de um addon
- `sankhya-jape`: o serviço backend que a tela consome
