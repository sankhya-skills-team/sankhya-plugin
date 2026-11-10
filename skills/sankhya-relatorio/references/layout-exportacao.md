# Layout e Exportação

Use quando o problema envolver alinhamento, aparência, PDF, XLS, fontes, estilos, imagens ou comportamento visual.

> **Padrão visual:** fonte, cor, paleta, cabeçalho, rodapé, logo, tabela, zebra, grupo e destaque seguem a skill
> `sankhya-relatorio-visual`, que prevalece sobre este arquivo em tudo que é aparência. Carregue-a antes de
> desenhar ou redesenhar um `.jrxml`. Aqui ficam o comportamento de exportação e a mecânica dos elementos.

## Canal principal — decidir antes de desenhar

| Alvo | Estratégia |
|---|---|
| **PDF** | Fidelidade visual, paginação, acentuação, fontes embutidas |
| **XLS** | Grade rígida, sem sobreposição, sem decoração excessiva |
| **Ambos** | Priorizar grade simples; `isIgnorePagination` para XLS |

## XLS — grade rígida

- Não sobrepor elementos
- Alinhar `x`, `y`, `width` e `height` exatos
- Mesma altura para elementos da mesma linha
- Evitar retângulos, frames e decoração excessiva na banda `detail`
- Desalinhamento mínimo cria colunas extras vazias
- Elementos sobrepostos viram células quebradas

## PDF — fontes e acentuação

A fonte é **Calibri**, embutida pelo módulo de fontes do Sankhya (`custom.net.sf.jasperreports.fonts`). Todo
`<style>` declara `fontName="Calibri"`. Não use `Arial`, `SansSerif`, `pdfFontName`, `pdfEncoding` nem
`isPdfEmbedded`: eles fazem o PDF trocar a fonte e perder o negrito. Regras e escala de tamanhos em
`sankhya-relatorio-visual` (`references/tipografia.md`).

Outras propriedades úteis: `REPORT_LOCALE`, `REPORT_TIME_ZONE`

Testar acentuação sempre no servidor, não só no iReport local.

## Estilos

Reduzem repetição visual. Centralizar fonte, tamanho, borda e cores.

Os estilos prontos (cabeçalho de tabela, célula, zebra, total, cartão, rodapé), com cores e medidas, estão nos
templates e em `references/pecas.md` da skill `sankhya-relatorio-visual`. Copie de lá em vez de criar estilos novos.

## Estilos condicionais

```xml
<style name="estilo_status" mode="Transparent" forecolor="#000000" fontSize="10">
    <conditionalStyle>
        <conditionExpression><![CDATA[$F{STATUS}.intValue() <= 5]]></conditionExpression>
        <style forecolor="#FF0000" isBold="true"/>
    </conditionalStyle>
</style>

<!-- Aplicar no campo -->
<textField>
    <reportElement style="estilo_status" x="0" y="0" width="200" height="16"/>
    ...
</textField>
```

## TextField — atributos importantes

```xml
<textField isBlankWhenNull="true"
           isStretchWithOverflow="true"
           pattern="dd/MM/yyyy"
           evaluationTime="Report">
```

- `isBlankWhenNull="true"` — alternativa limpa ao null-safe ternário
- `isStretchWithOverflow="true"` — expande quando conteúdo ultrapassa a altura
- `pattern` — formata data/número direto no elemento (ex: `#,##0.00`, `dd/MM/yyyy`)
- `evaluationTime="Report"` — avalia no fim do relatório (total de páginas)
- `markup="html"` — interpreta HTML básico no conteúdo

## Elementos gráficos

- `line` — separadores
- `rectangle` — blocos e bordas
- `frame` — agrupar elementos relacionados (ver `componentes-avancados.md`)
- `ellipse` — raramente útil em relatório corporativo

Para XLS: evitar excesso de elementos gráficos.

## Imagens

```xml
<!-- Logo dinâmica via PDIR_MODELO -->
<image scaleImage="RetainShape" onErrorType="Blank" hAlign="Center" vAlign="Middle">
    <reportElement x="0" y="0" width="140" height="68"/>
    <imageExpression class="java.lang.String">
        <![CDATA[$P{PDIR_MODELO} + "logo.png"]]>
    </imageExpression>
</image>
```

- `scaleImage="RetainShape"` — preserva proporção
- `onErrorType="Blank"` — não quebra o relatório quando imagem não existe
- Evitar caminhos absolutos locais (`C:\Users\...`)
- Reduzir imagens grandes antes de usar

## Paginação no rodapé

```xml
<pageFooter>
    <band height="16">
        <!-- Data/hora de impressão -->
        <textField pattern="dd/MM/yyyy HH:mm">
            <reportElement x="0" y="0" width="194" height="16"/>
            <textFieldExpression class="java.util.Date">
                <![CDATA[new java.util.Date()]]>
            </textFieldExpression>
        </textField>

        <!-- "Página X de" -->
        <textField>
            <reportElement x="692" y="0" width="80" height="16"/>
            <textFieldExpression class="java.lang.String">
                <![CDATA["Página " + $V{PAGE_NUMBER} + " de"]]>
            </textFieldExpression>
        </textField>

        <!-- Total de páginas (avaliado no fim) -->
        <textField evaluationTime="Report">
            <reportElement x="772" y="0" width="30" height="16"/>
            <textFieldExpression class="java.lang.String">
                <![CDATA[" " + $V{PAGE_NUMBER}]]>
            </textFieldExpression>
        </textField>
    </band>
</pageFooter>
```

## Checklist visual

- Layout respeita área útil da página (`columnWidth` + margens)?
- Há sobreposição indevida de elementos?
- Textos dinâmicos têm espaço ou `isStretchWithOverflow`?
- PDF preserva acentos e fontes?
- XLS sai com colunas limpas (sem células quebradas)?
- Imagens e subreports usam caminhos portáveis?
