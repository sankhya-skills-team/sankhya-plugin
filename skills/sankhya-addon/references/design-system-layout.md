# Design System — Layout e Fundação

Sistema de layout, tokens de design e fundação visual do Sankhya Design System.

---

## Getting Started — Overview

O Sankhya Design System é um ecossistema de componentes para garantir consistência e padronização na plataforma EIP. Facilita o trabalho de designers e desenvolvedores, entregando uma experiência mais simples, consistente e intuitiva.

**Seções principais:**
- **Componentes**: UI de uso geral sem acoplamento ao EIP.
- **Layout**: Classes CSS para layout responsivo.
- **EIP Componentes**: Blocos dependentes de estruturas do Sankhya (dicionário de dados, provedores).
- **Utilitários**: Funções comuns de formatação de datas e números.

**Pacotes:**
- `@sankhyalabs/core` — lógica e utilitários
- `@sankhyalabs/ez-design` — estilos/tokens
- `@sankhyalabs/ezui` — componentes UI
- `@sankhyalabs/sankhyablocks` — EIP components

---

## Getting Started — Configuração

**Pré-requisitos:** ReactJS 18, Node 14 (recomendado NVM).

### Método 1: Starter Application (recomendado)
```bash
git clone https://gitlab.sankhya.com.br/dti/design-system/react-app-starter
cd react-app-starter
npm install && npm start
```

### Método 2: Projeto React existente
```bash
npm install @sankhyalabs/core@latest
npm install @sankhyalabs/ez-design@latest
npm install @sankhyalabs/ezui@latest
```

**index.tsx:**
```javascript
import { applyPolyfills, defineCustomElements } from "@sankhyalabs/ezui/loader";
import '@sankhyalabs/ez-design/dist/default/ez-themed.min.css';
applyPolyfills().then(() => { defineCustomElements(); });
```

**public/index.html:**
```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

**Exemplo de uso:**
```javascript
import { EzButton } from "@sankhyalabs/ezui/react/components";
<EzButton class="ez-button--primary" label="Clique-me" onClick={() => alert('Olá!')} />
```

### Método 3: EIP Components (Building Blocks)
```bash
npm install @sankhyalabs/sankhyablocks@latest
```
```javascript
import { applyPolyfills as applyBlocks, defineCustomElements as defineBlocks }
  from "@sankhyalabs/sankhyablocks/loader";
applyBlocks().then(() => { defineBlocks(); });
```

> **Nota:** Vite não é suportado. Use ReactJS 18 com webpack (react-scripts).

---

## Acorde — Fundação (Design Tokens)

**Instalação:**
```bash
npm install @sankhya-acorde/design
```
```css
@import "@sankhya-acorde/design/dist/default/acorde/acorde.css";
```

O pacote inclui tokens para: Border Radius, Colors, Spacing, Typography.

---

## Acorde — Bordas (Border Radius)

Tokens para padronizar o arredondamento de bordas dos elementos.

| Token | Valor |
|-------|-------|
| `--border--radius-0` | 0px |
| `--border--radius-2` a `--border--radius-64` | 2px – 64px (incrementos de 2px) |
| `--border--radius-100` | 100px |
| `--border--radius-200` | 200px |

**Boas práticas:**
- Padrão moderno: `24px` (`--border--radius-24`)
- Elementos circulares: `200px`
- Máximo de duas variações por layout

```css
.elemento { border-radius: var(--border--radius-24); }
.circular  { border-radius: var(--border--radius-200); }
```

---

## Acorde — Cores

Tokens de cor que definem a paleta cromática. Proporção: **20% cores de ação / 80% neutros**.

### Ocean Green (cor primária)
| Token | Hex |
|-------|-----|
| `--color--ocean-green-600` | #008561 (principal) |
| `--color--ocean-green-500` | #1A9171 |
| `--color--ocean-green-400` | #42A58A |
| `--color--ocean-green-100` | #BDDFD6 |
| `--color--ocean-green-90` | #E6F3EF |

### Gray (neutro)
| Token | Hex |
|-------|-----|
| `--color--gray-900` | #0B0C0E |
| `--color--gray-400` | #77777A |
| `--color--gray-200` | #D2D2D3 |
| `--color--gray-90` | #EAEAEA |
| `--color--gray-70` | #FFFFFF |

### Feedback
| Paleta | Uso | Token principal |
|--------|-----|----------------|
| Green | Sucesso | `--color--green-600` (#157A00) |
| Yellow | Alerta | `--color--yellow-600` (#EFB103) |
| Red | Erro | `--color--red-600` (#BD0025) |
| Petroleum | Texto/fundo escuro | `--color--petroleum-600` (#2B3A54) |

```css
.elemento {
  background-color: var(--color--ocean-green-500);
  color: var(--color--petroleum-900);
}
```

---

## Acorde — Espaçamentos

Tokens para padronizar distâncias entre elementos.

| Tokens disponíveis | Valores |
|-------------------|---------|
| `--space--0` a `--space--52` | 0px – 52px (incrementos de 2px) |

**Distâncias recomendadas:** 16px, 20px, 24px, 28px, 32px
- Entre conteúdos/ícones: `16px`
- Entre componentes: `16px – 24px`
- Margens laterais: `24px`
- Navegação: `8px`

```css
.elemento {
  margin: var(--space--16);
  padding: var(--space--8) var(--space--16);
  gap: var(--space--8);
}
```

---

## Acorde — Tipografia

| Propriedade | Token / Valor |
|-------------|---------------|
| Font family | `--font--pattern` → Roboto |
| Font sizes | `--font-size--default` (14px) até `120px` |
| Peso regular | `--font-weight--regular` → 400 |
| Peso medium | `--font-weight--medium` → 500 |
| Peso semi-bold | `--font-weight--semi-bold` → 600 |
| Peso bold | `--font-weight--bold` → 700 |
| Letter spacing | `--letter-spacing--0/1/2` → 0/1/2px |

**Diretrizes:**
- Parágrafos: 14px, regular, line-height 30–40px
- Títulos: 24px padrão, range 22–44px, máximo 3 linhas
- Line heights: `--line-height--24` a `--line-height--78`

```css
.texto-padrao {
  font-family: var(--font--pattern);
  font-size: var(--font-size--default);
  font-weight: var(--font-weight--regular);
  line-height: var(--line-height--24);
}
.titulo {
  font-size: var(--font-size--xxlarge);
  font-weight: var(--font-weight--bold);
}
```

---

## Box

Componente para separar a página em seções, mantendo organização dos dados.

**Estrutura:** elemento interno com classe `ez-box__container`.

| Tamanho | Classe |
|---------|--------|
| Small | `ez-box__container--small` |
| Medium | `ez-box__container--medium` |
| Large | `ez-box__container--large` |
| Extra Large | `ez-box__container--extra-large` |
| Auto | `ez-box__container--size-auto` |

| Status | Classe |
|--------|--------|
| Sucesso | `ez-box--info--success` |
| Aviso | `ez-box--info--warning` |

---

## Content

Componente de layout para controlar tamanhos e estilos de containers de conteúdo. Suporta posicionamento sticky via `ez-content-sticky`.

---

## Flexbox System

Classe base: `ez-flex` (aplicada ao elemento pai).

### Direção
| Classe | Comportamento |
|--------|--------------|
| `ez-flex--row-reverse` | Linha invertida |
| `ez-flex--column` | Coluna |
| `ez-flex--column-reverse` | Coluna invertida |
| `ez-flex--wrap` | Quebra de linha |

### justify-content
| Classe | Comportamento |
|--------|--------------|
| `ez-flex--justify-start/end/center/between/around/evenly` | Alinhamento eixo principal |

### align-items
| Classe | Comportamento |
|--------|--------------|
| `ez-flex--align-items-stretch/start/end/center/baseline` | Alinhamento eixo cruzado |

### Itens individuais
| Classe | Comportamento |
|--------|--------------|
| `ez-flex-item--first/last` | Posicionamento |
| `ez-flex-item--align-stretch/start/end/center/baseline` | align-self |
| `ez-flex-item--auto` | Ocupa espaço disponível |

---

## Grid System

Sistema de 12 colunas com breakpoints responsivos.

| Device | Prefixo | Min-width |
|--------|---------|-----------|
| Small | `--sd-` | 320px |
| Phone | `--pn-` | 480px |
| Tablet | `--tb-` | 768px |
| Medium | `--md-` | 992px |
| Large | `--ld-` | 1200px |

```html
<div class="ez-row">
  <div class="ez-col --md-6 --sd-12">Conteúdo</div>
  <div class="ez-col --md-6 --sd-12">Conteúdo</div>
</div>
```

---

## Icons

Ícones simples, modernos e reduzidos à forma mínima. Utilizar o componente **EzIcon** para implementação.

---

## Labels

Elemento `<label>` com estilização padronizada.

| Variação | Classes |
|----------|---------|
| Base | `ez-label` |
| Título | `ez-label ez-label--title` |
| Descrição | `ez-label ez-label--description` |
| Opcional | `ez-label ez-label--optional` |
| Textarea | `ez-label ez-label--textarea` |

---

## Margin

Controla o espaçamento externo dos elementos.

**Classes disponíveis:** `ez-margin--{size}` onde size = `extra-small | small | medium | large | none | auto`

**Direcionais:** `ez-margin-{horizontal|vertical|left|right|top|bottom}--{size}`

---

## Padding

Controla o espaçamento interno dos elementos.

**Classes disponíveis:** `ez-padding--{size}` onde size = `extra-small | small | medium | large | none`

**Direcionais:** `ez-padding-{horizontal|vertical|left|right|top|bottom}--{size}`

---

## Text

Utilitários de tipografia para tamanho, alinhamento, cor, peso e quebra de linha.

**Classe base:** `ez-text`

| Propriedade | Classes |
|-------------|---------|
| Tamanho | `ez-text--xsmall/small/medium/large/xlarge` |
| Largura | `ez-text--full` |
| Alinhamento | `ez-text--left/right/center` |
| Cor | `ez-text--primary/secondary/tertiary/inverted/error` |
| Peso | `ez-text--bold` |
| Estilo | `ez-text--uppercase` |
| Overflow | `ez-text--ellipsis` (reticências) |
| Quebras | `ez-text--break-line` |

```html
<div class="ez-text ez-text--large ez-text--bold ez-text--primary">Texto</div>
```

---

## Title

Utilitário para estilização de títulos.

**Classe base:** `ez-title`

| Propriedade | Classes |
|-------------|---------|
| Tamanho | `ez-title--extra-small/small/medium/large/extra-large` |
| Alinhamento | `ez-title--center/left/right` + `ez-size-width--full` |
| Cor | `ez-title--primary/secondary/tertiary/inverted` |
