# Variante segura para XLS

Use quando o relatório pode ser exportado para Excel (listagens, conferências que viram planilha). Template:
`templates/paisagem-listagem-xls.jrxml`. O PDF continua com o mesmo visual do padrão; só a construção muda.

## Por que

O exportador XLS transforma cada `x` distinto de elemento numa coluna da planilha e cada elemento numa célula.
Elemento sobreposto (retângulo de zebra atrás do texto, fio por cima) vira célula quebrada, coluna vazia ou cor perdida.

## Regras

1. **Grade única.** Os `x` e larguras de todo elemento (título, cartões, rodapé) caem nas fronteiras das colunas da
   tabela. Exemplo do template (786): fronteiras 0, 50, 106, 162, 212, 402, 532, 582, 652, 708, 786.
2. **Nada sobreposto.** Sem `rectangle` atrás de texto e sem `line` no detail.
   - zebra: `conditionalStyle` no estilo da célula (`mode="Opaque"`, `backcolor="#F1F4F7"`);
   - fio entre linhas: `bottomPen` 0,5 `#D5DBE1` no `box` do estilo;
   - destaque: `conditionalStyle` só na célula que importa (`backcolor="#F5B85C"`, bold);
   - cartão: `frame` opaco com rótulo e valor dentro; o "gap" entre cartões é uma borda branca de 4 pt (`rightPen`);
   - fio verde do cabeçalho: borda inferior (`bottomPen`) de um `frame` da largura total; fio vertical: `leftPen` do
     `frame` do título.
3. **Condições mutuamente exclusivas.** Quando zebra e destaque podem valer na mesma célula, a zebra perde para o
   destaque **só se a condição dela excluir o destaque**:
   `$V{REPORT_COUNT}.intValue() % 2 == 0 && !(<condição do destaque>)`. Sem isso, a zebra apaga o destaque nas linhas
   pares.
4. **Mesma altura** para todos os campos da linha, com `stretchType="RelativeToTallestObject"`, para a linha que estica
   não deixar buraco na planilha.
5. **Valor tipado, data como texto.** No Excel, campo `String` vira texto e o usuário não consegue somar. Na coluna
   de **valor** use a classe real e `pattern`:
   ```xml
   <textField isStretchWithOverflow="true" pattern="#,##0.00" isBlankWhenNull="true">
   	<reportElement style="Linha" stretchType="RelativeToTallestObject" x="582" y="0" width="70" height="16"/>
   	<textElement textAlignment="Right"/>
   	<textFieldExpression class="java.math.BigDecimal"><![CDATA[$F{VLRDESDOB}]]></textFieldExpression>
   </textField>
   ```
   **Data NUNCA tipada** (`java.util.Date`/`Timestamp` no textField): o exportador **XLSX** do JR 4.0.0 grava a célula
   como `t="d"` com número de série, o que é inválido, e o Excel abre com "Encontramos um problema em um conteúdo…"
   e repara a planilha. Data vai como texto: `$F{DTVENC} == null ? "" : $V{V_DATA}.format($F{DTVENC})`.
   O mesmo exportador numera os formatos próprios a partir de 1 (devia ser 164); o Excel tolera, sem reparo.
   No PDF, o `pattern` do valor usa o locale do servidor. Confira no cliente; se sair `1,234.56`, volte o valor para texto com `V_MOEDA` (perde a soma no Excel).
6. Propriedades no `<jasperReport>`:
   ```xml
   <property name="net.sf.jasperreports.export.xls.detect.cell.type" value="true"/>
   <property name="net.sf.jasperreports.export.xls.remove.empty.space.between.rows" value="true"/>
   <property name="net.sf.jasperreports.export.xls.white.page.background" value="false"/>
   ```
7. Totais e cartões com `evaluationTime="Report"` funcionam no XLS.
8. **Sem repetição de página na planilha.** No PDF cada página tem rodapé e cabeçalho de continuação; no Excel isso
   vira linhas no meio dos dados. Exclua só na exportação Excel (o PDF não muda):
   ```xml
   <property name="net.sf.jasperreports.export.xls.exclude.origin.band.1" value="pageFooter"/>
   <property name="net.sf.jasperreports.export.xls.exclude.origin.band.2" value="pageHeader"/>
   <property name="net.sf.jasperreports.export.xls.exclude.origin.keep.first.band.3" value="columnHeader"/>
   ```
   Resultado: título, cartões, **um** cabeçalho de coluna, todas as linhas seguidas e o resumo.
9. **Identificador numérico como número** (Nº fin., nota): `java.math.BigDecimal` com `pattern="0"` e alinhado à
   esquerda. Como texto, o Excel marca cada célula com o triângulo verde "número armazenado como texto". Zero que
   significa "não tem" vira `null` na expressão (`isBlankWhenNull`).

## O que fica diferente do PDF de documento

- Cartões sem canto arredondado (`frame` não tem `radius`).
- Cores no Excel são aproximadas para a paleta de 56 cores do formato XLS (o âmbar `#F5B85C` vira um laranja claro).
- As margens de 28 pt viram uma coluna estreita vazia em cada lado da planilha. É esperado.

