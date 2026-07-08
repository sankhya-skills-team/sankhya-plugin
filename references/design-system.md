# Sankhya Design System — Índice

O Sankhya Design System é a biblioteca de componentes web para construção de telas personalizadas no portal Sankhya W. Utiliza web components com dois prefixos:

- **`ez-`** — componentes genéricos de UI (design system base)
- **`snk-`** — componentes específicos do ERP Sankhya, integrados com entidades e serviços

**Fonte online:** https://gilded-nasturtium-6b64dd.netlify.app/docs/components

---

## Sub-arquivos por categoria

| Arquivo | O que contém |
|---|---|
| `references/design-system-ez-components.md` | Componentes `ez-` de A a L: actions-button, alert, avatar, badge, breadcrumb, button, calendar, card-item, chart, check, chip, combo-box, date-input, dialog, double-list, dropdown, filter-input, form, grid, icon, list, list-item |
| `references/design-system-ez-components-b.md` | Componentes `ez-` de M a Z: modal, multi-selection-list, number-input, pagination, popover, popup, radio-button, rich-text, search, skeleton, spinner, split-panel, tabselector, tag, text-input, tile, time-input, toast, tooltip, tree, upload |
| `references/design-system-layout.md` | Layout e fundação: Acorde tokens (cores, bordas, espaçamentos, tipografia), Box, Content, Flexbox System, Grid System, Icons, Labels, Margin, Padding, Text, Title |
| `references/design-system-snk-components.md` | Componentes `snk-`: application, attach, crud, data-unit, entity-list, filter-bar, form, grid, pesquisa, simple-crud, simple-form-config, taskbar e outros |
| `references/design-system-utilities.md` | Utilitários TypeScript: DataUnit, DataUnitAction, ServiceUtils, HttpProvider, DateUtils, StringUtils, NumberUtils, ArrayUtils, enums (Action, DataType, SelectionMode), interfaces (FieldDescriptor, Filter, Record) |
| `references/design-system-api-java.md` | API Java BFF: IDataUnitInterceptor, IDataUnitCrudListener, ICustomFilterBarResolver, IDataExporterInterceptor, ITotalsResolver, BootModuleListener |

---

## Como usar

1. Identifique o componente ou API necessária
2. Leia o sub-arquivo correspondente para detalhes de propriedades, eventos, métodos e exemplos
3. Para confirmar informações ou verificar atualizações, consulte a URL do componente via WebFetch (ver protocolo no SKILL.md)

---

## Protocolo de atualização (Design System)

O Design System é hospedado no Netlify e acessível externamente. Ao consultar um componente:

1. Tente buscar a URL correspondente via WebFetch
2. Se bem-sucedido: use o conteúdo ao vivo; se diferente do arquivo local, atualize
3. Se falhar: use o sub-arquivo local como fallback
