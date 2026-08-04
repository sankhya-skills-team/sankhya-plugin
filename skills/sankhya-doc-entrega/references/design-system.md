# Design System Sankhya — aplicação nos documentos de entrega

Tokens extraídos de `sankhya.com.br`. A implementação vive em
`scripts/_brand.py` — **é a fonte única**. Este arquivo explica as decisões;
não duplique valores em outros lugares.

---

## Paleta

| Token | Hex | Uso |
|---|---|---|
| `primary` | `#4ADE80` | Destaque, bordas de seção, badges de versão, botão de exportar, numeração de passos |
| `secondary` | `#0EA5E9` | Badge do tipo `acao` (botão de ação) |
| `tertiary` | `#243143` | Sidebar, títulos, cabeçalhos de tabela, texto de destaque |
| `surface` | `#F0FAF0` | Fundo de página — **somente HTML** |
| `on-surface` | `#4B5563` | Texto corrido |

Duas cores semânticas **não** vêm do design system do site e existem só para
status de homologação e blocos de alerta:

| Token | Hex | Uso |
|---|---|---|
| `danger` | `#DC2626` | Teste reprovado, bloco de limitação, grupo de pré-requisitos |
| `warning` | `#D97706` | Bloco de observação, grupo de pós-deploy |

## Cores por tipo de funcionalidade

Restritas à paleta — nada de cor inventada por tipo.

| Tipo | Cor | Badge |
|---|---|---|
| `acao` | `secondary` | Ação Manual |
| `evento` | `primary` | Listener / Evento |
| `job` | `tertiary` | Job Agendado |
| `regra` | `on-surface` | Regra de Negócio |

## Tipografia

`Work Sans` com fallback `Segoe UI, Arial, sans-serif`. O HTML importa a fonte
do Google Fonts; sem internet o fallback assume sem quebrar o layout. O DOCX
declara `Work Sans` e o Word resolve o fallback sozinho.

Escala: 16px corpo (1.5) · 14px secundário (1.43) · 12px micro (1.33) ·
20px título de seção · 18px título do documento.

## Raios e sombras

Raios do design system: `sm 2px · md 3px · lg 4px · xl 5px · full 9999px`.
Cartões usam `xl`; badges e pílulas usam `full`.
Sombras: `0 1px 2px rgba(10,12,18,.05)` e `0 2px 6px rgba(0,0,0,.05)`.

---

## Regra HTML × DOCX

| | HTML | DOCX |
|---|---|---|
| Design system | Completo — fundo `surface`, sidebar `tertiary`, sombras, raios | Apenas as **cores** |
| Fundo de página | `#F0FAF0` | **Branco. Nunca colorir a página.** |
| Preenchimento | Livre | Restrito a cabeçalhos de tabela (`tertiary`, texto branco) |
| Bordas | CSS | Borda inferior `primary` sob títulos de seção nível 2 |

## Logo

Um único ativo, duas formas de consumo — ambas em `scripts/_brand.py`:

- **HTML** — `B.LOGO_SVG`, SVG inline. A wordmark usa `currentColor`, então
  herda a cor do container: branca na sidebar escura, `tertiary` sobre fundo
  claro. Sem arquivo externo, sem caminho para quebrar.
- **DOCX** — `B.LOGO_PNG`, aponta para `assets/sankhya-logo.png` resolvido a
  partir de `__file__`. Inserido com 4 cm de largura no topo do documento.

O PNG foi rasterizado do mesmo SVG (744×168, wordmark `#243143`, símbolo
`#66CB66`). Para regerar após mudança de marca: renderize o SVG com
`svglib` + `reportlab` e substitua o arquivo em `assets/`.
