# Design System — Guia prático (regras e armadilhas)

Escrito à mão a partir do snapshot da doc oficial (2026-09-28). Os detalhes de cada componente/classe estão nos arquivos gerados (ver `INDICE.md`). Aqui ficam as regras que atravessam todos os componentes e os pontos em que a doc oficial engana.

> **Lembrete:** o padrão de telas personalizadas é **sankhya-js**. Design System só quando o projeto já tem pipeline Node **e** o usuário pediu explicitamente.

---

## 1. Setup

Duas páginas oficiais se contradizem:

| Página | Diz |
|---|---|
| `setup/configure.md` | React 18 + **Node 14** + webpack (react-scripts); "componentes ainda não preparados para Vite" |
| `setup/onboarding-bff.md` | Fluxo atual: clonar `react-app-starter`, `.env` com `VITE_APP_*`, `npm run dev` (Vite) |

Use **Vite + React 18 + TS + Node 20/22** (validado em campo; Node 14 é EOL). Se o projeto já usa react-scripts, mantenha.

Pacotes: `@sankhyalabs/core`, `@sankhyalabs/ez-design`, `@sankhyalabs/ezui` e, para `snk-*`, `@sankhyalabs/sankhyablocks`.

Entrypoint (`main.tsx`/`index.tsx`) — **sem isso os componentes renderizam em branco**:

```tsx
import { applyPolyfills, defineCustomElements } from "@sankhyalabs/ezui/loader";
import { applyPolyfills as applyBlocks, defineCustomElements as defineBlocks } from "@sankhyalabs/sankhyablocks/loader";
import "@sankhyalabs/ez-design/dist/default/ez-themed.min.css";

applyPolyfills().then(() => defineCustomElements());
applyBlocks().then(() => defineBlocks()); // só se usar snk-*
```

Fonte Roboto (`<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet" />`) vai no `index.html`: em `public/` no CRA, na **raiz** no Vite.

Variáveis do `.env` do starter (onboarding): `SKW_URL` (servidor SankhyaW), `VITE_APP_APP_DESCRIPTION`, `VITE_APP_MODULE_NAME`, `VITE_APP_RESOURCE_ID` (é o resourceID usado por `hasAccess`, ver `references/controle-acesso.md`); `.env.production`: `BASE_PATH`. Login local em `public/workspacemock/workspace.js` (SUP sem senha por padrão) — **nunca** commitar credencial real ali.

> O onboarding cobre telas dentro de módulos Sankhya (desacoplado ou BFF, pipeline GitLab, deploy via gulp). **A doc não explica como empacotar uma tela DS num addon de parceiro** — ver o agente `sankhya-frontend-design-system` (seção "Como o resultado é empacotado no addon" e "ALERTA #2").

---

## 2. HTML × React

A doc oficial é 100% React. Regras para traduzir:

| Aspecto | React | HTML/JS puro |
|---|---|---|
| Import | `import { EzButton } from "@sankhyalabs/ezui/react/components"`; `snk-*` de `@sankhyalabs/sankhyablocks/react/components` | tag `<ez-button>` após `defineCustomElements()` |
| Prop simples | `iconName="bell"` | atributo kebab-case `icon-name="bell"` (HTML ignora maiúsculas: `iconName` como atributo **não chega** à prop) |
| Prop complexa (array, objeto, função: `config`, `dataUnit`, `optionLoader`, `columns`…) | `config={obj}` | **só por propriedade JS**: `el.config = obj` |
| Evento | `onEzChange={e => e.detail}` | `el.addEventListener("ezChange", e => e.detail)` |
| Método | `await ref.current.setFocus()` | `await el.setFocus()` |

- **Todo método de componente é `async`** (retorna `Promise`). `if (el.isInvalid())` sem `await` é sempre verdadeiro.
- A coluna "Attribute" das tabelas de props mostra o nome kebab-case; `--` significa "só por propriedade JS". Algumas tabelas da doc omitem essa coluna — aplique a regra camelCase → kebab-case.
- `enabled` → `isDisabled` foi depreciado **só no `ez-button`**; não generalize para outros componentes.

---

## 3. Receita de tela com `snk-*`

```tsx
import { useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataUnit } from "@sankhyalabs/core";

export default function MinhaTela() {
    const [dataUnit, setDataUnit] = useState<DataUnit>();

    // onDataUnitReady recebe CustomEvent<DataUnit>: a instância está em event.detail
    const aoPrepararDataUnit = (event: CustomEvent<DataUnit>) => setDataUnit(event.detail);

    return (
        <SnkApplication>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={aoPrepararDataUnit}>
                {dataUnit && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
}
```

- `snk-application` é raiz obrigatória e singleton de contexto — um por tela.
- Renderize `SnkCrud`/`SnkGrid`/`SnkForm` **só depois** do DataUnit pronto (gate com `useState`).
- Com `SnkGrid`/`SnkForm`/`SnkTaskbar` isolados (sem `SnkCrud`), chame `du.loadData()` no `onDataUnitReady` ou use `autoLoad`. Omitido, `autoLoad` segue o parâmetro `global.carregar.registros.iniciar.tela`.
- resourceID: `await snkApplicationRef.current.getResourceID()`.
- Parâmetros do sistema: `getStringParam`/`getIntParam`/`getFloatParam`/`getBooleanParam`/`getDateParam(nome)`.
- `snk-taskbar` só aparece se a prop `buttons` for informada. Ids usados em slot customizado precisam constar em `buttons`.
- `presentationMode`: `primary` está em descontinuação; prefira `singleTaskbar` (`PresentationMode.SINGLE_TASKBAR`).
- Mensagens (`snk-message-builder`): arquivo `public/messages/appmessages.js`, `export default appMessages`, chaves camelCase aninhadas: `snkTaskbar: { titleUpdate: "..." }`, `snkForm: { title: { insert: "..." } }`, `crudUtils: {...}`. **Nunca** `SnkTaskbar` nem `"title.insert"`.

## 4. DataUnit sem `snk-*` (`@sankhyalabs/core`)

Ordem obrigatória nos exemplos oficiais: configurar loaders → `loadMetadata()` → `loadData()`.

```ts
const du = new DataUnit("meuDataUnit");
du.metadataLoader = () => Promise.resolve(metadata);
du.dataLoader = (dataUnit, request) => buscarRegistros(request); // paginação/ordenação: ver core/guias/dataUnitLoaderUtils.md
du.saveLoader = (dataUnit, changes) => salvar(changes);          // changes: Array<Change>, ver core/classes/Change.md
du.loadMetadata().then(() => du.loadData());
```

Todos os loaders são opcionais no TypeDoc. Para dados em memória: `core/guias/dataUnitInMemoryLoader.md`. Cache de serviço: `ServiceUtils` com `storageType: StorageType` (enum; padrão `IN_MEMORY_CACHE`), não string.

---

## 5. Armadilhas da doc oficial (não copie)

| Onde | Problema na doc | Faça |
|---|---|---|
| Vários snk (crud/data-unit "padrão recomendado") | `(duInstance) => setDataUnit(duInstance)` | `event.detail` (o evento é `CustomEvent<DataUnit>`) |
| Metade dos exemplos do snk-crud | Não aplicam o gate `onDataUnitReady` que a própria página exige | Sempre aplicar |
| snk-application / snk-crud | Caminho de mensagens `/messages/appmessages.msg.js` | `public/messages/appmessages.js` (página do message-builder) |
| snk-application `loadByPK` | `ref?.loadData(...)` sem `.current`, chamando método do core no componente | `ref.current` + método correto |
| snk-crud statusResolver | Exemplo passa `getStatusResolver` (inexistente) | `statusResolver` |
| snk-form `validate()` | Tipado `Promise<void>`, exemplo lê `result?.isValid` | Validar no pacote antes de depender do retorno |
| snk-taskbar | Nomes de botão inconsistentes (`ACTION_BUTTONS`/`ACTIONS_BUTTON`, `GRID`/`GRID_MODE`) | Conferir enum no pacote |
| ez-list-item | Prosa diz `title`/`textTitle`; exemplos usam `titleText`/`text` | Seguir os exemplos; validar no pacote |
| ez-pagination | Texto diz `type="numeric"`; exemplos usam `number` | Validar no pacote |
| ez-sidebar-navigator | Texto diz small/medium/large; exemplos usam `md`/`lg` | Validar no pacote |
| core, exemplos de campo | `userInterface: "TEXT"` não existe | `UserInterface.SHORTTEXT` |
| core `DependencyType` | `VISIBILITY` tem valor `"REQUIREMENT"` | Usar o membro do enum, nunca o literal |
| core `DateUtils.validateDate` | Tipado `Date`, exemplo passa string | Passar `Date` |
| core `DataBinder` | Documentado junto do core | Vem de `@sankhyalabs/ezui` |
| layout `--font-pattern` | Página de tokens **depreciada** | Acorde: `--font--pattern` (dois hífens) |
| layout Text × Title | Tamanhos: Text `xsmall…xlarge`; Title `extra-small…extra-large` | Não unificar os nomes |
| API Java `ITotalsResolver` | Exemplos anotam com `@CustomFilterBarResolver` | Provável copy-paste; confirmar a anotação no jar |
| API Java `ICustomFilterBarResolver` | `if(!filterBarConfig)` não compila em Java | `if (filterBarConfig == null)` |
| API Java (geral) | Sem pacotes, imports, coordenadas Maven nem registro do `BootModuleListener` | Não inventar: dizer que não está documentado |
| Links internos da doc | ~40 links para subpáginas dão 404 (ex.: `ez-grid/subcomponents`, `snk-grid-config`) | O conteúdo não existe; não citar |
