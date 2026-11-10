# Tipografia

## Fonte

**Calibri**, regular e bold, em todo texto. Ela vem do módulo de fontes do Sankhya
(`custom.net.sf.jasperreports.fonts`, `skw-ireport-pdf-fonts.jar`), que a embute no PDF com negrito real.

- Todo `<style>` declara `fontName="Calibri"`. O estilo `isDefault="true"` só vale para elemento **sem** `style`.
- Não use `pdfFontName`, `pdfEncoding` nem `isPdfEmbedded`: o módulo de fontes resolve. Esses atributos (comuns em
  exemplos antigos com Arial/Helvetica) fazem o PDF trocar a fonte.
- Não use `SansSerif`, `Serif`, `Monospaced` nem Arial. `SansSerif` vira Helvetica no PDF, sem negrito.
- Itálico: evite. Calibri itálico existe no módulo, mas o padrão não usa.

### Conferir no PDF gerado

Liste as fontes do PDF (por exemplo, `pymupdf`: `page.get_fonts()`). Tem de aparecer `Calibri` e `Calibri-Bold`.
`Helvetica-Bold` = algum texto escapou do padrão. Pode aparecer uma `Helvetica` sem texto visível: é um texto vazio que
o exportador do JR 4.0 grava junto das imagens, e não é erro.

### Cliente sem o módulo de fontes

Confirme no WildFly do cliente: `modules/custom/net/sf/jasperreports/fonts/main/skw-ireport-pdf-fonts.jar`.
Se não existir, a Calibri não embute e o PDF sai em Helvetica. Não troque o padrão para Arial: peça a instalação do
módulo (é o padrão Sankhya) e registre no chamado.

## Escala

| uso | tamanho | peso | cor |
|---|---|---|---|
| título do relatório | 16 (15 se o título for longo) | bold | petróleo |
| título de continuação (página 2+) | 11 | bold | petróleo |
| subtítulo | 8 | regular | rótulo `#6B7785` |
| tarja | 9 | bold | branco sobre petróleo |
| valor do cartão | 18 (15 para data/moeda no cartão de 128 do retrato); 20 no cartão petróleo da paisagem | bold | petróleo (branco no cartão petróleo) |
| rótulo (cartão, rótulo-valor, assinatura) | 7, MAIÚSCULO | bold | rótulo `#6B7785` |
| valor de rótulo-valor | 9 | regular (nome em bold) | texto |
| cabeçalho de coluna | 7 | bold | branco |
| célula | 8 | regular; código/valor principal em bold | texto / petróleo |
| 2ª linha dentro da célula | 7 | regular | rótulo |
| faixa de grupo | 9 | bold | petróleo |
| total do grupo | 9 | bold | petróleo |
| total geral | 11 (rótulo) / 13 (valor) | bold | petróleo |
| número que o leitor procura primeiro **dentro da tabela** (quantidade a conferir) | 13–14 | bold | petróleo |
| legenda | 7 | regular | rótulo |
| rodapé | 8 ("Página" em bold petróleo) | regular | rótulo |
| etiqueta: código legível | 28 | bold | texto |
| etiqueta: descrição | 12 | bold | petróleo |
| etiqueta: emissão | 7 | regular | secundário |

Mínimo absoluto: **7 pt**. Abaixo disso não imprime legível.

## Altura mínima do campo

`altura ≥ tamanho × 1,25 + padding superior + padding inferior`. Exemplos:

| fonte | sem padding | com padding 2+2 |
|---|---|---|
| 7 | 9 | 13 |
| 8 | 10 | 14 |
| 9 | 12 | 16 |
| 11 | 14 | 18 |
| 13 | 17 | 21 |
| 16 | 20 | 24 |
| 18 | 23 | 27 |
| 28 | 35 | 39 |

Abaixo da altura mínima o Jasper não imprime o texto e não avisa.
