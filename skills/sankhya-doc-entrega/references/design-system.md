# Design System Sankhya — aplicação nos documentos de entrega

Duas fontes oficiais da DS:

- **Estrutura:** "DSTECH - Modelo de Evidências de Entrega de Customização v.4", guardado
  como `assets/modelo-entrega-v4.docx`.
- **Cores e tipografia:** guia "Modelo de Documento Padrão Sankhya 2026".

A implementação vive em `scripts/_brand.py`, que **é a fonte única** para o HTML. Este
arquivo explica as decisões. Não duplique valores em outros lugares.

---

## Paleta

| Token | Hex | Uso |
|---|---|---|
| Navy 900 | `#0C1927` | Fundo escuro mais profundo (capas) |
| Navy 700 | `#212F41` | Texto principal, títulos, cabeçalho de tabela |
| Slate | `#343C50` | Subtítulos de terceiro nível |
| Verde Sankhya | `#00D666` | Destaques sobre fundo escuro, linhas e números |
| Verde apoio | `#00CD5E` | Títulos finos, marcadores e rótulos sobre fundo claro |
| Cinza | `#888888` | Legendas, cabeçalho, rodapé e placeholders |
| Cinza claro | `#F3F3F3` | Fundos de nota, linhas alternadas, coluna de rótulo |

O guia não tem cor semântica. `danger` (`#DC2626`) e `warning` (`#D97706`) existem só no
HTML, para o status reprovado/pendente dos testes de homologação.

## Tipografia

Work Sans em todos os elementos. O DOCX leva a fonte embutida no template. O HTML importa
do Google Fonts, com fallback `Segoe UI, Arial`.

| Elemento | Fonte | Tamanho | Cor |
|---|---|---|---|
| Título de abertura, linha 1 | Work Sans Light, caixa alta | 24 pt | Verde apoio |
| Título de abertura, linha 2 | Work Sans SemiBold, caixa alta | 24 pt | Navy 700 |
| Título 1 | Work Sans SemiBold, caixa alta | 17 pt | Navy 700 |
| Título 2 | Work Sans SemiBold | 12,5 pt | Navy 700 |
| Título 3 | Work Sans SemiBold | 10,5 pt | Slate |
| Texto | Work Sans | 10,5 pt | Navy 700 |
| Legenda, rodapé | Work Sans | 7–8 pt | Cinza |

No HTML os pontos viram px (× 4/3), calculados em `gerar_html.py` a partir de
`_brand.PT_*`.

---

## Regra HTML × DOCX

| | HTML | DOCX |
|---|---|---|
| Fonte da formatação | CSS gerado de `_brand.py` | Estilos do template (`SkCapaLinha*`, `SkTitulo*`, `Heading1/2`, `SkRotulo`, `SkTabela`, `SkLegenda`, `ListParagraph`) |
| Capa e contracapa | Fundos JPG do modelo (`assets/capa-fundo.jpg`, `contracapa-fundo.jpg`), no topo e no fim da tela e como página inteira no PDF | As do template, sem alteração |
| Cabeçalho e rodapé | Não tem (documento de tela) | Os do template, intactos. O bloco Elaborador/Aprovador é o controle do próprio modelo DS, não da entrega |
| Blocos repetidos | Gerados em HTML | Cópias dos elementos do template (caixa OBSERVAÇÃO, tabela do histórico, listas) |

O DOCX não define cor, fonte nem margem no código. Formatação nova entra no template,
não no script.

## Logo

- **HTML:** `B.LOGO_SVG`, SVG inline. A wordmark usa `currentColor` e herda a cor do
  container: branca na sidebar e na contracapa. O fundo da capa já traz a logo e não
  recebe outra por cima.
- **DOCX:** a do template (capa no fundo, contracapa e cabeçalho como imagem).
