# Checklist antes de entregar

## No .jrxml

- [ ] Margens 28 e `columnWidth` 539 (retrato) / 786 (paisagem).
- [ ] Todo `<style>` com `fontName="Calibri"`; nenhum `SansSerif`, Arial, `pdfFontName`, `pdfEncoding`.
- [ ] Todo campo de texto com altura ≥ fonte × 1,25 + padding (tabela em `tipografia.md`).
- [ ] Todo `<line>` com `lineColor` no `<pen>` igual ao `forecolor`.
- [ ] Toda cor está em `marca-dstech.md`.
- [ ] Logo do cliente trocada (placeholder "LOGO DO CLIENTE" só em prévia; se faltou a logo, avisar) e selo DSTech
      no rodapé.
- [ ] Campo de altura fixa (título, tarja, cartão, rótulo-valor, grupo, rodapé) com
      `net.sf.jasperreports.text.truncate.suffix` "…" como 1º filho do `reportElement`; campo de tabela com
      `isStretchWithOverflow`.
- [ ] Nulo tratado antes de todo `format(...)`, `.trim()`, `.replaceAll(...)` e do código de barras.
- [ ] `markup="styled"` com todo campo do banco escapado (`&` e `<`).
- [ ] Números à direita com `V_QTD`/`V_MOEDA`; datas `dd/MM/yyyy`; identificador com `toPlainString()`.
- [ ] Destaque com legenda e com texto/negrito (não só cor); legenda some quando não houve destaque.
- [ ] `pageHeader` de continuação com `PAGE_NUMBER > 1`; cabeçalho de grupo reimprime na quebra.
- [ ] "Página X de Y" rente à margem direita; "Emitido em" presente.
- [ ] Sem comentário XML, sem linha em branco, sem `uuid`, sem `<paragraph>`, sem `y` negativo.
- [ ] `<property name="dstech.padrao.visual" value="sankhya-relatorio-visual 1.0.0"/>`.
- [ ] Redesenho: consulta, parâmetros, campos e atributos do `<jasperReport>` idênticos ao original; código de barras
      com mesmo `barWidth`, `barHeight`, largura e altura.
- [ ] XLS: grade única, nada sobreposto, `conditionalStyle`, valores tipados (`xls.md`).

## No PDF impresso pelo ERP

- [ ] Fontes do PDF: `Calibri` e `Calibri-Bold`; nada de `Helvetica-Bold`.
- [ ] Negrito aparece no título, cartões e cabeçalho da tabela.
- [ ] Teste com dado no limite: nome longo, observação longa, campo nulo, `&` e `<` no texto, muitas linhas
      (quebra de página, cabeçalho de coluna e de grupo repetindo).
- [ ] Impressão (ou conversão) em P&B: tabela legível pelo fio, destaque visível com o texto.
- [ ] Código de barras lido pelo leitor de verdade.
- [ ] Números no formato `1.234,56` (se não, servidor sem pt-BR: ver `xls.md` §5).
- [ ] XLS (se aplicável): exportar pela tela, abrir no Excel, conferir colunas, somar uma coluna de valor.
