# Componentes Avançados

Use para subreports, table, list, crosstab, charts, frame e decisões arquiteturais de composição.

## Quando usar cada solução

| Necessidade | Solução |
|---|---|
| Linha tabular principal | banda `detail` |
| Subtotal por chave | `group` + variável |
| Tabela secundária encapsulada com subdataset | `table` component |
| Bloco repetido com layout flexível | `list` component |
| Relatório filho reutilizável ou seções independentes | `subreport` |
| Cruzamento linha × coluna × medida | `crosstab` |
| Síntese visual de dados | `chart` |
| Agrupar elementos relacionados visualmente | `frame` |

---

## Subreport

Use quando:
- master-detail com queries separadas
- reaproveitar layout complexo em vários relatórios
- seções independentes dentro do mesmo documento

### Relatório pai chama subreport

```xml
<detail>
    <band height="31">
        <subreport>
            <reportElement x="0" y="8" width="802" height="23"/>

            <!-- Parâmetros enviados ao subreport -->
            <subreportParameter name="ID">
                <subreportParameterExpression><![CDATA[$F{ID}]]></subreportParameterExpression>
            </subreportParameter>

            <!-- Alternativa: repassar todos os parâmetros de uma vez -->
            <!-- <parametersMapExpression><![CDATA[$P{REPORT_PARAMETERS_MAP}]]></parametersMapExpression> -->

            <!-- Conexão — sempre repassar -->
            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>

            <!-- Receber variáveis calculadas de volta -->
            <returnValue subreportVariable="VLRTOT_1"   toVariable="V_TOTAL_BRUTO"   calculation="Sum"/>
            <returnValue subreportVariable="VLRTOTLIQ"  toVariable="V_TOTAL_LIQUIDO" calculation="Sum"/>
            <returnValue subreportVariable="VLRTOTDESC" toVariable="V_TOTAL_DESCONTO" calculation="Sum"/>

            <!-- Caminho do .jasper compilado -->
            <subreportExpression class="java.lang.String">
                <![CDATA[$P{SUBREPORT_DIR} + "NomeSubRelatorio.jasper"]]>
            </subreportExpression>
        </subreport>
    </band>
</detail>
```

### Subreport (arquivo filho)

```xml
<!-- Margens zero — obrigatório -->
<jasperReport ... leftMargin="0" rightMargin="0" topMargin="0" bottomMargin="0">

    <!-- Parâmetro recebido do pai -->
    <parameter name="ID" class="java.math.BigDecimal" isForPrompting="false"/>

    <!-- Query usa o parâmetro -->
    <queryString><![CDATA[SELECT ... FROM TABELA WHERE ID = $P{ID}]]></queryString>

    <!-- Variáveis que serão retornadas ao pai via returnValue -->
    <variable name="VLRTOT_1" class="java.math.BigDecimal" calculation="Sum">
        <variableExpression><![CDATA[$F{VLRTOT}]]></variableExpression>
    </variable>
```

**Regras obrigatórias no subreport:**
- `leftMargin="0" rightMargin="0" topMargin="0" bottomMargin="0"`
- `$P{REPORT_CONNECTION}` como `connectionExpression`
- `<returnValue>` para cada variável que o pai precisa agregar

**Evite subreport** quando um `group`, `table` ou a própria banda `detail` resolverem com menos custo (subreport executa query por linha do pai).

---

## Table Component

Use quando precisar de tabela interna baseada em `subDataset`, especialmente em bloco mestre-detalhe ou tabela secundária.

```xml
<!-- Estilos recomendados para table -->
<style name="table"><box><pen lineWidth="1.0" lineColor="#000000"/></box></style>
<style name="table_TH" mode="Opaque" backcolor="#FFFFFF">
    <box><pen lineWidth="0.5" lineColor="#000000"/></box>
</style>
<style name="table_CH" mode="Opaque" backcolor="#F2F2F2">
    <box><pen lineWidth="0.5" lineColor="#000000"/></box>
</style>
<style name="table_TD" mode="Opaque" backcolor="#FFFFFF">
    <box><pen lineWidth="0.5" lineColor="#000000"/></box>
</style>

<!-- Declarar subDataset antes dos parâmetros -->
<subDataset name="DS_TABLE">
    <parameter name="P_ID" class="java.math.BigDecimal"/>
    <queryString><![CDATA[SELECT ... WHERE ID = $P{P_ID}]]></queryString>
    <field name="CAMPO1" class="java.lang.String"/>
    <field name="CAMPO2" class="java.math.BigDecimal"/>
</subDataset>

<!-- Usar na banda detail -->
<componentElement>
    <reportElement key="table" style="table" x="0" y="0" width="800" height="60"/>
    <jr:table xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components
                http://jasperreports.sourceforge.net/xsd/components.xsd">
        <datasetRun subDataset="DS_TABLE">
            <datasetParameter name="P_ID">
                <datasetParameterExpression><![CDATA[$F{ID}]]></datasetParameterExpression>
            </datasetParameter>
            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
        </datasetRun>
        <jr:column width="200">
            <jr:tableHeader style="table_TH" height="20" rowSpan="1">
                <staticText>
                    <reportElement x="0" y="0" width="200" height="20"/>
                    <textElement textAlignment="Center" verticalAlignment="Middle"/>
                    <text><![CDATA[Campo 1]]></text>
                </staticText>
            </jr:tableHeader>
            <jr:columnHeader style="table_CH" height="14" rowSpan="1"/>
            <jr:detailCell style="table_TD" height="20" rowSpan="1">
                <textField isBlankWhenNull="true">
                    <reportElement x="0" y="0" width="200" height="20"/>
                    <textElement textAlignment="Center" verticalAlignment="Middle"/>
                    <textFieldExpression class="java.lang.String"><![CDATA[$F{CAMPO1}]]></textFieldExpression>
                </textField>
            </jr:detailCell>
        </jr:column>
    </jr:table>
</componentElement>
```

Cuidados: verificar suporte no iReport/JasperReports 4.0.1 usado no runtime; manter larguras coerentes; testar quebra de página.

---

## List Component

Use quando cada item repetido tem layout próprio com múltiplos campos ou bloco visual customizado.

Evite se o objetivo for grade tabular simples — `detail` ou `table` costuma ser melhor.

```xml
<componentElement>
    <reportElement x="0" y="0" width="500" height="200"/>
    <jr:list xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components"
             printOrder="Vertical">
        <datasetRun subDataset="DS_LISTA">
            <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
        </datasetRun>
        <jr:listContents height="40" width="500">
            <!-- elementos do item -->
        </jr:listContents>
    </jr:list>
</componentElement>
```

---

## Crosstab

Use para tabela dinâmica com grupos de linha, grupos de coluna e medida agregada.

Antes de criar, confirmar:
1. Dimensão de linha (ex: mês)
2. Dimensão de coluna (ex: produto)
3. Medida (ex: valor total)
4. Tipo de agregação (Sum, Count, Average)
5. Largura esperada — crosstabs crescem horizontalmente
6. Se precisa exportar para XLS (risco: células quebradas)

Riscos:
- Crescimento horizontal excessivo em PDF
- Medidas com tipo incorreto
- Resultado ilegível quando muitas colunas
- Configuração errada de totalização

---

## Charts

Use para síntese visual. Tipos disponíveis:

| Tipo | Usar para |
|---|---|
| Barra | Comparação entre categorias |
| Linha | Evolução temporal |
| Pizza | Proporção simples |
| Stacked | Composição acumulada |
| Time Series | Séries temporais |

Boas práticas:
- Usar subdataset dedicado para os dados do gráfico
- Usar poucos pontos de dados — gráficos com muitos itens ficam ilegíveis
- Complementar com tabela-resumo quando necessário
- Testar em PDF e HTML

---

## Frame

Use para agrupar elementos relacionados e mover/bloquear o conjunto.

Bom para: dados do cliente, bloco de totais, observações, assinatura, áreas com borda/fundo comum.

```xml
<frame>
    <reportElement x="0" y="0" width="400" height="80">
        <box>
            <pen lineWidth="1.0"/>
        </box>
    </reportElement>
    <!-- elementos internos -->
    <staticText>
        <reportElement x="5" y="5" width="100" height="14"/>
        <text><![CDATA[Cliente:]]></text>
    </staticText>
    <textField isBlankWhenNull="true">
        <reportElement x="110" y="5" width="285" height="14"/>
        <textFieldExpression class="java.lang.String"><![CDATA[$F{NOMEPARC}]]></textFieldExpression>
    </textField>
</frame>
```

Cuidados: evitar aninhamento excessivo de frames; não usar como decoração pesada em relatórios focados em XLS.
