# Layout e Exportação

Use quando o problema envolver alinhamento, aparência, PDF, XLS, fontes, estilos, imagens ou comportamento visual.

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

Fontes seguras sem pacote próprio: `Arial`, `Times New Roman`, `Courier New`

Propriedades quando houver problema de acento:
- `pdfFontName` — nome da fonte PDF (ex: `Helvetica-Bold`)
- `pdfEncoding` — ex: `Cp1252` para Latin-1
- `isPdfEmbedded="true"` — embutir fonte no PDF

Outras propriedades úteis: `REPORT_LOCALE`, `REPORT_TIME_ZONE`

Testar acentuação sempre no servidor, não só no iReport local.

## Estilos

Reduzem repetição visual. Centralizar fonte, tamanho, borda e cores.

```xml
<style name="CabecalhoTabela" fontName="Arial" fontSize="9" isBold="true"
       mode="Opaque" backcolor="#CCCCCC">
    <box><pen lineWidth="0.5" lineColor="#999999"/></box>
</style>

<style name="DetalheTabela" fontName="Arial" fontSize="8">
    <box><pen lineWidth="0.5" lineColor="#CCCCCC"/></box>
</style>

<style name="Subtotal" fontName="Arial" fontSize="9" isBold="true"/>
<style name="TotalGeral" fontName="Arial" fontSize="10" isBold="true"/>
```

Nomes recomendados: `BaseTexto`, `Titulo`, `CabecalhoTabela`, `DetalheTabela`, `Subtotal`, `TotalGeral`

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
