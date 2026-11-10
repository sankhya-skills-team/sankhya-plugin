# Peças prontas (trechos XML)

Recortes do `templates/retrato-agrupado.jrxml` (área útil 539), salvo onde indicado. Na paisagem, escale as larguras
para 786. Estilos, formatadores (`V_MOEDA`, `V_DATA`, `V_QTD`), totais (`V_TOT`, `V_TOT_GRUPO`), `V_LOGO`, `V_SELO`,
`V_PAGINA` e `V_CODIGO` estão declarados nos templates: ao copiar um trecho, copie também as declarações que ele usa.

## Estilos base

```xml
<style name="Base" isDefault="true" fontName="Calibri" fontSize="8" forecolor="#1F2933"/>
<style name="Titulo" fontName="Calibri" fontSize="16" isBold="true" forecolor="#2E3C50"/>
<style name="Subtitulo" fontName="Calibri" fontSize="8" forecolor="#6B7785"/>
<style name="Tarja" mode="Opaque" forecolor="#FFFFFF" backcolor="#2E3C50" fontName="Calibri" fontSize="9" isBold="true" hAlign="Center" vAlign="Middle"/>
<style name="Rotulo" fontName="Calibri" fontSize="7" isBold="true" forecolor="#6B7785"/>
<style name="RotuloInverso" fontName="Calibri" fontSize="7" isBold="true" forecolor="#CFD6DF"/>
<style name="ValorCartao" fontName="Calibri" fontSize="18" isBold="true" forecolor="#2E3C50" vAlign="Middle"/>
<style name="Valor" fontName="Calibri" fontSize="9" forecolor="#1F2933" vAlign="Middle"/>
<style name="CabColuna" mode="Opaque" forecolor="#FFFFFF" backcolor="#2E3C50" fontName="Calibri" fontSize="7" isBold="true" vAlign="Middle">
	<box topPadding="1" leftPadding="3" bottomPadding="1" rightPadding="3"/>
</style>
<style name="Celula" fontName="Calibri" fontSize="8" forecolor="#1F2933" vAlign="Middle">
	<box topPadding="2" leftPadding="3" bottomPadding="2" rightPadding="3"/>
</style>
<style name="Grupo" fontName="Calibri" fontSize="9" isBold="true" forecolor="#2E3C50" vAlign="Middle">
	<box leftPadding="10" rightPadding="3"/>
</style>
<style name="Total" fontName="Calibri" fontSize="9" isBold="true" forecolor="#2E3C50" vAlign="Middle">
	<box topPadding="2" leftPadding="3" bottomPadding="2" rightPadding="3"/>
</style>
<style name="Rodape" fontName="Calibri" fontSize="8" forecolor="#6B7785" vAlign="Middle"/>
<style name="Legenda" fontName="Calibri" fontSize="7" forecolor="#6B7785" vAlign="Middle"/>
```

## Cabeçalho (title, página 1)

```xml
<image scaleImage="RetainShape" hAlign="Left" vAlign="Middle" onErrorType="Blank">
	<reportElement x="0" y="4" width="140" height="22"/>
	<imageExpression class="java.awt.Image"><![CDATA[$V{V_LOGO}]]></imageExpression>
</image>
<line>
	<reportElement x="150" y="2" width="1" height="28" forecolor="#66CB66"/>
	<graphicElement><pen lineWidth="1.5" lineColor="#66CB66"/></graphicElement>
</line>
<staticText>
	<reportElement style="Titulo" x="160" y="0" width="280" height="22"/>
	<textElement verticalAlignment="Middle"/>
	<text><![CDATA[Nome do Relatório]]></text>
</staticText>
<textField isBlankWhenNull="true">
	<reportElement style="Subtitulo" x="160" y="22" width="379" height="12">
		<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
	</reportElement>
	<textElement verticalAlignment="Middle"/>
	<textFieldExpression class="java.lang.String"><![CDATA[$F{NOMEEMP}]]></textFieldExpression>
</textField>
<textField isBlankWhenNull="true">
	<reportElement style="Tarja" x="449" y="3" width="90" height="16">
		<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
		<printWhenExpression><![CDATA[Boolean.valueOf($F{TIPMOV} != null)]]></printWhenExpression>
	</reportElement>
	<textElement/>
	<textFieldExpression class="java.lang.String"><![CDATA["V".equals($F{TIPMOV}) ? "VENDA" : $F{TIPMOV}]]></textFieldExpression>
</textField>
<line>
	<reportElement x="0" y="38" width="539" height="1" forecolor="#66CB66"/>
	<graphicElement><pen lineWidth="2.0" lineColor="#66CB66"/></graphicElement>
</line>
```

A tarja diz em uma palavra o que o leitor precisa saber primeiro: tipo (VENDA, COMPRA), sentido (EXPEDIÇÃO,
RECEBIMENTO) ou estado (ABERTA, FECHADA). Sem informação assim, não use tarja.

## Cartão (petróleo = o número que identifica o documento; os demais em `#EEF2F5`)

```xml
<rectangle radius="4">
	<reportElement x="0" y="46" width="128" height="44" forecolor="#2E3C50" backcolor="#2E3C50"/>
	<graphicElement><pen lineWidth="0.0"/></graphicElement>
</rectangle>
<staticText>
	<reportElement style="RotuloInverso" x="10" y="51" width="113" height="10"/>
	<textElement/>
	<text><![CDATA[Nº ÚNICO]]></text>
</staticText>
<textField isBlankWhenNull="true">
	<reportElement style="ValorCartao" x="10" y="61" width="113" height="26" forecolor="#FFFFFF">
		<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
	</reportElement>
	<textElement/>
	<textFieldExpression class="java.lang.String"><![CDATA[$P{PK_NUNOTA} == null ? "-" : $P{PK_NUNOTA}.toPlainString()]]></textFieldExpression>
</textField>
```

Cartão claro: `forecolor`/`backcolor` `#EEF2F5`, rótulo com `style="Rotulo"`, valor sem `forecolor` (petróleo do estilo).

## Rótulo + valor

```xml
<staticText>
	<reportElement style="Rotulo" x="0" y="98" width="260" height="10"/>
	<textElement/>
	<text><![CDATA[PARCEIRO]]></text>
</staticText>
<textField isBlankWhenNull="true">
	<reportElement style="Valor" x="0" y="108" width="260" height="14">
		<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
	</reportElement>
	<textElement><font isBold="true"/></textElement>
	<textFieldExpression class="java.lang.String"><![CDATA[$F{CODPARC} == null ? "-" : $F{CODPARC}.toPlainString() + ($F{NOMEPARC} == null ? "" : " · " + $F{NOMEPARC})]]></textFieldExpression>
</textField>
```

## Observação (estica; some quando vazia)

```xml
<frame>
	<reportElement isRemoveLineWhenBlank="true" mode="Opaque" x="0" y="130" width="539" height="22" backcolor="#EEF2F5">
		<printWhenExpression><![CDATA[Boolean.valueOf($F{OBSERVACAO} != null && $F{OBSERVACAO}.trim().length() > 0)]]></printWhenExpression>
	</reportElement>
	<box><leftPen lineWidth="3.0" lineColor="#66CB66"/></box>
	<textField isStretchWithOverflow="true" isBlankWhenNull="true">
		<reportElement x="10" y="4" width="523" height="14"/>
		<textElement verticalAlignment="Middle" markup="styled"><font size="9"/></textElement>
		<textFieldExpression class="java.lang.String"><![CDATA["<style isBold=\"true\" forecolor=\"#2E3C50\">Observação</style>   " + ($F{OBSERVACAO} == null ? "" : $F{OBSERVACAO}.trim().replaceAll("&", "&amp;").replaceAll("<", "&lt;"))]]></textFieldExpression>
	</textField>
</frame>
```

## Linha da tabela com zebra, destaque e fio

```xml
<band height="16" splitType="Prevent">
	<rectangle>
		<reportElement stretchType="RelativeToBandHeight" mode="Opaque" x="0" y="0" width="539" height="16" forecolor="#F1F4F7" backcolor="#F1F4F7">
			<printWhenExpression><![CDATA[Boolean.valueOf($V{GRUPO_COUNT}.intValue() % 2 == 0)]]></printWhenExpression>
		</reportElement>
		<graphicElement><pen lineWidth="0.0"/></graphicElement>
	</rectangle>
	<rectangle>
		<reportElement stretchType="RelativeToBandHeight" mode="Opaque" x="481" y="0" width="58" height="15" forecolor="#F5B85C" backcolor="#F5B85C">
			<printWhenExpression><![CDATA[Boolean.valueOf($F{VLRTOT} == null || $F{VLRTOT}.signum() == 0)]]></printWhenExpression>
		</reportElement>
		<graphicElement><pen lineWidth="0.0"/></graphicElement>
	</rectangle>
	<line>
		<reportElement positionType="FixRelativeToBottom" x="0" y="15" width="539" height="1" forecolor="#D5DBE1"/>
		<graphicElement><pen lineWidth="0.5" lineColor="#D5DBE1"/></graphicElement>
	</line>
	<textField isStretchWithOverflow="true" isBlankWhenNull="true">
		<reportElement style="Celula" x="74" y="0" width="213" height="16"/>
		<textElement/>
		<textFieldExpression class="java.lang.String"><![CDATA[$F{DESCRPROD}]]></textFieldExpression>
	</textField>
</band>
```

Ordem dentro da band: zebra → destaque → fio → textos. Sem grupo, a zebra usa `$V{REPORT_COUNT}`.
Para Excel, troque tudo isso pela variante de `xls.md`.

## Faixa de grupo e total do grupo

```xml
<group name="GRUPO" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="60">
	<groupExpression><![CDATA[$F{CODGRUPOPROD}]]></groupExpression>
	<groupHeader>
		<band height="24">
			<rectangle>
				<reportElement x="0" y="4" width="539" height="18" forecolor="#EEF2F5" backcolor="#EEF2F5"/>
				<graphicElement><pen lineWidth="0.0"/></graphicElement>
			</rectangle>
			<rectangle>
				<reportElement x="0" y="4" width="3" height="18" forecolor="#66CB66" backcolor="#66CB66"/>
				<graphicElement><pen lineWidth="0.0"/></graphicElement>
			</rectangle>
			<textField isBlankWhenNull="true">
				<reportElement style="Grupo" x="0" y="4" width="420" height="18">
					<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
				</reportElement>
				<textElement/>
				<textFieldExpression class="java.lang.String"><![CDATA[($F{CODGRUPOPROD} == null ? "" : $F{CODGRUPOPROD}.toPlainString() + " · ") + ($F{DESCRGRUPOPROD} == null ? "Sem grupo" : $F{DESCRGRUPOPROD})]]></textFieldExpression>
			</textField>
			<textField evaluationTime="Group" evaluationGroup="GRUPO">
				<reportElement style="Grupo" x="420" y="4" width="119" height="18" forecolor="#4A5563"/>
				<box rightPadding="3"/>
				<textElement textAlignment="Right"><font isBold="false"/></textElement>
				<textFieldExpression class="java.lang.String"><![CDATA[$V{GRUPO_COUNT} + ($V{GRUPO_COUNT}.intValue() == 1 ? " item" : " itens")]]></textFieldExpression>
			</textField>
		</band>
	</groupHeader>
	<groupFooter>
		<band height="20">
			<frame>
				<reportElement mode="Opaque" x="0" y="0" width="539" height="18" backcolor="#EEF2F5"/>
				<box><topPen lineWidth="1.5" lineColor="#2E3C50"/></box>
				<textField>
					<reportElement style="Total" x="0" y="0" width="481" height="18"/>
					<textElement/>
					<textFieldExpression class="java.lang.String"><![CDATA["Total do grupo"]]></textFieldExpression>
				</textField>
				<textField>
					<reportElement style="Total" x="481" y="0" width="58" height="18"/>
					<textElement textAlignment="Right"/>
					<textFieldExpression class="java.lang.String"><![CDATA[$V{V_TOT_GRUPO} == null ? "0,00" : $V{V_MOEDA}.format($V{V_TOT_GRUPO})]]></textFieldExpression>
				</textField>
			</frame>
		</band>
	</groupFooter>
</group>
```

O fundo e o fio do total ficam no `frame`, e os textos dentro dele (estilo `Total` sem fundo): assim não aparece
emenda entre o rótulo e o valor. O total geral do `summary` é igual, com h 24, rótulo 11 e valor 13.

Aviso dentro do grupo (ignorado, cortado): 2ª linha do **mesmo** textField (`\n` + `<style>`), nunca campo separado,
senão a faixa fica com buraco.

## Escrita à mão

Não está em nenhum template (os 3 não têm campo a preencher). Medidas relativas à coluna onde a caixa fica
(x da coluna = `xc`, largura = `wc`), numa linha de tabela h 28. Exemplo para uma coluna "Validade" em `xc` = 449,
`wc` = 90 e checkbox numa coluna "OK" em x 0, largura 28:

```xml
<rectangle radius="3">
	<reportElement x="453" y="3" width="82" height="22" forecolor="#9AA5B1" backcolor="#FFFFFF"/>
	<graphicElement><pen lineWidth="0.75" lineColor="#9AA5B1"/></graphicElement>
</rectangle>
<staticText>
	<reportElement x="453" y="3" width="82" height="21" forecolor="#9AA5B1"/>
	<textElement textAlignment="Center" verticalAlignment="Bottom"><font size="9"/></textElement>
	<text><![CDATA[     /     /      ]]></text>
</staticText>
<rectangle radius="2">
	<reportElement x="7" y="7" width="14" height="14" forecolor="#2E3C50" backcolor="#FFFFFF"/>
	<graphicElement><pen lineWidth="1.0" lineColor="#2E3C50"/></graphicElement>
</rectangle>
```

Caixa = (`xc` + 4, 3, `wc` − 8, 22). Checkbox centrado na coluna (14 × 14). Cabeçalho das colunas a preencher em
verde escuro `#4A8F55`. A guia `/ /` só vai em campo de data.

## Legenda e assinaturas (summary)

```xml
<rectangle>
	<reportElement x="0" y="38" width="10" height="9" forecolor="#F5B85C" backcolor="#F5B85C">
		<printWhenExpression><![CDATA[Boolean.valueOf($V{V_SEM_VALOR}.intValue() > 0)]]></printWhenExpression>
	</reportElement>
	<graphicElement><pen lineWidth="0.0"/></graphicElement>
</rectangle>
<staticText>
	<reportElement style="Legenda" x="14" y="37" width="300" height="11">
		<printWhenExpression><![CDATA[Boolean.valueOf($V{V_SEM_VALOR}.intValue() > 0)]]></printWhenExpression>
	</reportElement>
	<textElement/>
	<text><![CDATA[Item sem valor]]></text>
</staticText>
<line>
	<reportElement x="0" y="80" width="240" height="1" forecolor="#2E3C50"/>
	<graphicElement><pen lineWidth="0.75" lineColor="#2E3C50"/></graphicElement>
</line>
<staticText>
	<reportElement style="Rotulo" x="0" y="83" width="240" height="10"/>
	<textElement/>
	<text><![CDATA[CONFERENTE]]></text>
</staticText>
```

A legenda só aparece se houve destaque: conte os destaques numa variável (`V_SEM_VALOR`, `calculation="Sum"` de
1/0 com a mesma condição do destaque) e ponha `printWhenExpression` `> 0` no quadrado e no texto.

Duas assinaturas: 240 + gap 59 + 240. Três: 170 / 15 / 170 / 14 / 170.

## Rodapé com "Página X de Y" num campo só

```xml
<variable name="V_PAGINA" class="java.lang.Integer" resetType="Page">
	<variableExpression><![CDATA[$V{PAGE_NUMBER}]]></variableExpression>
</variable>
```

```xml
<pageFooter>
	<band height="24">
		<line>
			<reportElement x="0" y="4" width="539" height="1" forecolor="#D5DBE1"/>
			<graphicElement><pen lineWidth="0.5" lineColor="#D5DBE1"/></graphicElement>
		</line>
		<image scaleImage="RetainShape" hAlign="Left" vAlign="Middle" onErrorType="Blank">
			<reportElement x="0" y="9" width="50" height="12"/>
			<imageExpression class="java.awt.Image"><![CDATA[$V{V_SELO}]]></imageExpression>
		</image>
		<textField>
			<reportElement style="Rodape" x="58" y="9" width="132" height="12">
				<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
			</reportElement>
			<textElement/>
			<textFieldExpression class="java.lang.String"><![CDATA["Nº único " + ($P{PK_NUNOTA} == null ? "" : $P{PK_NUNOTA}.toPlainString())]]></textFieldExpression>
		</textField>
		<textField>
			<reportElement style="Rodape" x="195" y="9" width="150" height="12"/>
			<textElement textAlignment="Center"/>
			<textFieldExpression class="java.lang.String"><![CDATA["Emitido em " + new java.text.SimpleDateFormat("dd/MM/yyyy HH:mm").format(new java.util.Date())]]></textFieldExpression>
		</textField>
		<textField evaluationTime="Auto">
			<reportElement style="Rodape" x="389" y="9" width="150" height="12" forecolor="#2E3C50"/>
			<textElement textAlignment="Right"><font isBold="true"/></textElement>
			<textFieldExpression class="java.lang.String"><![CDATA["Página " + $V{V_PAGINA} + " de " + $V{PAGE_NUMBER}]]></textFieldExpression>
		</textField>
	</band>
</pageFooter>
```

`evaluationTime="Auto"` avalia cada variável no seu momento: `V_PAGINA` (reset por página) dá a página atual e
`PAGE_NUMBER` dá o total. O texto termina rente à margem direita. Não use o par "Página X de" + campo
`evaluationTime="Report"`: deixa espaço sobrando à direita.

## Código de barras (etiqueta)

```xml
<componentElement>
	<reportElement x="16" y="34" width="507" height="72">
		<printWhenExpression><![CDATA[Boolean.valueOf($V{V_CODIGO} != null && $V{V_CODIGO}.length() > 0)]]></printWhenExpression>
	</reportElement>
	<jr:barbecue xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd" type="Code128" drawText="false" checksumRequired="false" barWidth="2" barHeight="70">
		<jr:codeExpression><![CDATA[$V{V_CODIGO}]]></jr:codeExpression>
	</jr:barbecue>
</componentElement>
```

- O barbecue desenha as barras **à esquerda** do elemento, com 10 módulos brancos (zona de silêncio) **dentro** do
  elemento. Por isso o código legível vai alinhado à esquerda com `leftPadding` = 10 × `barWidth` (20 com
  `barWidth="2"`): começa na 1ª barra. Não centralize o texto embaixo de barras alinhadas à esquerda.
- Largura: com `barWidth="2"` em 507 pt cabem ~17 caracteres alfanuméricos. Só dígitos ocupam metade (Code128 C).
  Código maior: `barWidth="1"` (só em etiqueta nova; em etiqueta existente, regra 11 do SKILL.md).
- Fundo branco atrás e nada encostado nas barras. QR Code: zona de silêncio de 4 módulos.
- `drawText="false"`: o texto legível é um textField nosso (Calibri 28 bold), não o do barbecue.
