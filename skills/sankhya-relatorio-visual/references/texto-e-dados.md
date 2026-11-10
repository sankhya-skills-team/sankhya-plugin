# Texto e dados: corte, nulo, número, data, escape

## Texto que não cabe

| onde | comportamento | como |
|---|---|---|
| célula de tabela | **estica** (a linha cresce, a zebra acompanha) | `isStretchWithOverflow="true"` em todos os campos da linha; zebra e destaque com `stretchType="RelativeToBandHeight"`; fio com `positionType="FixRelativeToBottom"` |
| observação longa | **estica** dentro de um `frame` | `frame` com `isRemoveLineWhenBlank="true"` e `printWhenExpression` de não vazio; textField interno com `isStretchWithOverflow="true"` |
| título, subtítulo, tarja, cartão, rótulo-valor, faixa de grupo, rodapé, etiqueta | **altura fixa, corta com "…"** | `<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>` como **primeiro filho** do `<reportElement>` |

A propriedade de reticências existe no JR 4.0.0. Ela corta na última palavra
inteira que cabe e acrescenta "…". Um campo de altura fixa sem ela corta o texto em silêncio.

Ordem dentro do `<reportElement>` (o XSD exige): `<property>` → `<printWhenExpression>`.

```xml
<reportElement style="Tarja" x="449" y="3" width="90" height="16">
	<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>
	<printWhenExpression><![CDATA[Boolean.valueOf($F{TIPMOV} != null)]]></printWhenExpression>
</reportElement>
```

Nunca use `isStretchWithOverflow` em campo de altura fixa dentro de moldura ou faixa: o texto vaza por cima da
borda.

## Nulo

| onde | mostra | expressão |
|---|---|---|
| cartão, rótulo-valor | `-` | `$F{X} == null ? "-" : …` |
| célula de tabela | vazio | `isBlankWhenNull="true"` ou `$F{X} == null ? "" : …` |
| total | `0` / `0,00` | `$V{T} == null ? "0,00" : $V{V_MOEDA}.format($V{T})` |
| frase composta | só as partes que existem | separador dentro do ternário da parte: `$F{CODPARC}.toPlainString() + ($F{NOMEPARC} == null ? "" : " · " + $F{NOMEPARC})` |
| nulo que é o próprio problema | texto do destaque | `$F{VLRTOT} == null \|\| $F{VLRTOT}.signum() == 0 ? "sem valor" : …` + fundo de destaque |
| mensagem com parâmetro (sem dados) | sem "null" | `"Nota " + ($P{PK_NUNOTA} == null ? "" : $P{PK_NUNOTA}.toPlainString())` |
| número zero que significa "não tem" (NUMNOTA 0) | `-` | `$F{NUMNOTA} == null \|\| $F{NUMNOTA}.signum() == 0 ? "-" : …` |

`DecimalFormat.format(null)` e `SimpleDateFormat.format(null)` lançam exceção e derrubam a impressão: **sempre** teste
nulo antes de formatar. Campo de código de barras vazio também derruba ("Data to encode cannot be empty"): ponha
`printWhenExpression` de não vazio no `componentElement`.

## Número e data

Formatadores como variáveis `calculation="System"` (criadas uma vez, sem parâmetro novo):

```xml
<variable name="V_QTD" class="java.text.DecimalFormat" calculation="System">
	<initialValueExpression><![CDATA[new java.text.DecimalFormat("#,##0.###", new java.text.DecimalFormatSymbols(new java.util.Locale("pt", "BR")))]]></initialValueExpression>
</variable>
<variable name="V_MOEDA" class="java.text.DecimalFormat" calculation="System">
	<initialValueExpression><![CDATA[new java.text.DecimalFormat("#,##0.00", new java.text.DecimalFormatSymbols(new java.util.Locale("pt", "BR")))]]></initialValueExpression>
</variable>
<variable name="V_DATA" class="java.text.SimpleDateFormat" calculation="System">
	<initialValueExpression><![CDATA[new java.text.SimpleDateFormat("dd/MM/yyyy")]]></initialValueExpression>
</variable>
```

| tipo | formato | alinhamento |
|---|---|---|
| quantidade | `#,##0.###` (sem zeros à toa: 12,5 e não 12,500) | direita |
| moeda | `#,##0.00`, sem "R$" na célula; "(R$)" no cabeçalho da coluna | direita |
| data | `dd/MM/yyyy` | centro |
| data e hora | `dd/MM/yyyy HH:mm` | centro |
| percentual | `#,##0.00'%'` | direita |

O locale pt-BR fica **explícito** porque o idioma do servidor do cliente não é garantido. Na variante XLS, os valores
são tipados com `pattern` (ver `xls.md`).

## Documento

```java
// CNPJ (14) / CPF (11), senão o texto como veio
$F{CGC_CPF} == null || $F{CGC_CPF}.trim().length() == 0 ? "-" :
($F{CGC_CPF}.trim().length() == 14 ? $F{CGC_CPF}.trim().replaceAll("(\\d{2})(\\d{3})(\\d{3})(\\d{4})(\\d{2})", "$1.$2.$3/$4-$5") :
($F{CGC_CPF}.trim().length() == 11 ? $F{CGC_CPF}.trim().replaceAll("(\\d{3})(\\d{3})(\\d{3})(\\d{2})", "$1.$2.$3-$4") : $F{CGC_CPF}.trim()))
```

Identificador numérico (NUNOTA, CODPROD) com `.toPlainString()`: nunca sai em notação científica nem com ",00".

## Texto estilizado (`markup="styled"`)

Use para duas informações na mesma célula (nome em bold + razão social menor embaixo). **Todo** campo do banco dentro
do texto estilizado é escapado, testando nulo antes:

```java
"<style isBold=\"true\" forecolor=\"#2E3C50\">" + ($F{NOMEPARC} == null ? "" : $F{NOMEPARC}.replaceAll("&", "&amp;").replaceAll("<", "&lt;")) + "</style>"
+ ($F{RAZAOSOCIAL} == null ? "" : "\n<style size=\"7\" forecolor=\"#6B7785\">" + $F{RAZAOSOCIAL}.replaceAll("&", "&amp;").replaceAll("<", "&lt;") + "</style>")
```

Sem escape, um `<` no dado gera "Error parsing styled text" e o campo inteiro some da impressão. Campo que nunca terá
`<` ou `&` (código, número) não precisa de escape, mas campo de texto livre (placa, nome, observação, unidade) precisa.

## Separadores

- `·` (ponto médio) entre partes da mesma linha: "2201 · CLIENTE EXEMPLO".
- `/` em cidade/UF e nota/série.
- Travessão e `·` funcionam porque a Calibri é embutida; o `.jrxml` é UTF-8.
