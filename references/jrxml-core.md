# JRXML Core — JasperReports/iReport 4.0.1

Use para criar, revisar ou corrigir a estrutura principal de um `.jrxml`.

## Ciclo de vida

- `.jrxml` → fonte XML editável no iReport
- `.jasper` → compilado (Build > Compile Report)
- `.jrprint` → relatório preenchido em runtime
- Exportações: PDF, XLS, HTML, CSV, XML

## Compatibilidade 4.0.1

- Remover `uuid="..."` de elementos importados de versões novas
- Evitar `java.time`, lambdas e APIs modernas — usar JDK 1.6/1.7
- Não usar tags/atributos de versões recentes do schema
- Compilar no mesmo runtime do servidor quando possível

### Ordem obrigatória dos filhos de `<jasperReport>` (validação XSD rígida)

Qualquer elemento fora desta sequência causa `SAXParseException` ao abrir no iReport:

```
style*
parameter*
queryString?
field*
sortField*
variable*
filterExpression?
group*
background
title
pageHeader
columnHeader
detail
columnFooter
pageFooter
lastPageFooter
summary
noData
```

**Erros comuns de ordem:**
- `<style>` depois de `<variable>` → erro: "conteúdo inválido começando com o elemento 'style'"
- `<title>` depois de `<pageFooter>` → erro: "conteúdo inválido começando com o elemento 'title'"

### Atributo `fontSize` vs `size`

`fontSize=` é válido **apenas em `<style>`**. Dentro de `<font>` filho de `<textElement>`, o atributo correto é `size=`:

```xml
<!-- CORRETO em <style> -->
<style name="Cabecalho" fontName="Arial" fontSize="12" isBold="true"/>

<!-- CORRETO dentro de <textElement> -->
<textElement>
    <font fontName="Arial" size="9" isBold="false"/>
</textElement>

<!-- ERRADO — causa: "atributo 'fontSize' não pode aparecer no elemento 'font'" -->
<textElement>
    <font fontName="Arial" fontSize="9"/>
</textElement>
```

### Atributo `markup`

`markup=` pertence a `<textElement>`, **não a `<textField>`**:

```xml
<!-- CORRETO -->
<textField isStretchWithOverflow="true" evaluationTime="Report">
    <reportElement x="0" y="0" width="495" height="80"/>
    <textElement textAlignment="Justified" markup="html">
        <font fontName="Arial" size="9"/>
    </textElement>
    <textFieldExpression class="java.lang.String"><![CDATA["texto <b>negrito</b>"]]></textFieldExpression>
</textField>

<!-- ERRADO — causa: "atributo 'markup' não pode aparecer no elemento 'textField'" -->
<textField markup="html">
```

### Comentários XML e ISO-8859-1

- **Proibido `--` dentro de `<!-- -->`** — XML não permite; causa `SAXParseException` fatal
- **Solução recomendada: não usar comentários XML no `.jrxml`** — o iReport não exige e evita toda essa classe de erro
- **Em-dash `—` (U+2014) e en-dash `–` (U+2013) não existem em ISO-8859-1** — substituir por `-` antes de salvar; `iconv` falha silenciosamente ou aborta na posição do caractere

## Cabeçalho seguro

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports
                http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="NOME_DO_RELATORIO"
              language="java"
              pageWidth="842" pageHeight="595"
              orientation="Landscape"
              columnWidth="802"
              leftMargin="20" rightMargin="20"
              topMargin="20" bottomMargin="20"
              whenNoDataType="AllSectionsNoDetail">
```

**Atributos importantes de `jasperReport`:**
- `whenNoDataType` — comportamento quando query não retorna dados (`AllSectionsNoDetail`, `NoPages`, `BlankPage`)
- `isIgnorePagination` — útil quando alvo principal for XLS
- `orientation` — `Portrait` ou `Landscape`

## Bandas

| Banda | Quando renderiza |
|---|---|
| `background` | Fundo ou marca d'água |
| `title` | Uma vez, início do relatório |
| `pageHeader` | Topo de cada página |
| `columnHeader` | Antes do detalhe (cabeçalho de colunas) |
| `detail` | Uma vez por linha da query |
| `groupHeader` | Abertura de agrupamento |
| `groupFooter` | Fechamento / subtotal de agrupamento |
| `columnFooter` | Após o detalhe |
| `pageFooter` | Rodapé de cada página |
| `lastPageFooter` | Rodapé última página (substitui `pageFooter`) |
| `summary` | Uma vez, ao final do relatório |

**Cuidados:**
- Bandas altas geram quebras inesperadas
- `splitType="Prevent"` pode criar grandes espaços em branco
- Elementos com stretch podem invadir elementos abaixo se a banda não estiver planejada

## Campos

```xml
<field name="VALOR_TOTAL" class="java.math.BigDecimal"/>
```

Tipos comuns:
- texto: `java.lang.String`
- inteiros: `java.lang.Integer`, `java.lang.Long`
- financeiro: `java.math.BigDecimal`
- data: `java.sql.Date`
- data/hora: `java.sql.Timestamp`

Boas práticas: alias SQL = nome do campo; remover campos não usados; não converter tudo para `String`.

## Parâmetros

Prefixar com `P_` os parâmetros de filtro (usuário). Parâmetros internos relevantes:

| Parâmetro interno | Uso |
|---|---|
| `REPORT_CONNECTION` | Conexão JDBC — repassar a subreports |
| `REPORT_DATA_SOURCE` | Datasource alternativo |
| `REPORT_PARAMETERS_MAP` | Mapa de todos os parâmetros — usar em `parametersMapExpression` |
| `REPORT_LOCALE` | Localização para formatação |
| `REPORT_TIME_ZONE` | Fuso horário |

```xml
<!-- Parâmetro de filtro Sankhya com lookup de tabela -->
<parameter name="P_CODVEND" class="java.math.BigDecimal" isForPrompting="true">
    <property name="nomeTabela" value="TGFVEN"/>
    <parameterDescription><![CDATA[Vendedor]]></parameterDescription>
    <defaultValueExpression><![CDATA[null]]></defaultValueExpression>
</parameter>

<!-- Parâmetro de data — SEMPRE Timestamp no Sankhya -->
<parameter name="P_DTINI" class="java.sql.Timestamp" isForPrompting="true">
    <parameterDescription><![CDATA[Data Início]]></parameterDescription>
    <defaultValueExpression><![CDATA[null]]></defaultValueExpression>
</parameter>
```

## Variáveis

Prefixar com `V_`. Configurações essenciais:

- `calculation`: `Sum`, `Count`, `Average`, `First`, `Highest`, `Lowest`, `Nothing`
- `resetType`: `Report`, `Page`, `Column`, `Group`, `None`
- `resetGroup`: obrigatório quando `resetType="Group"`

```xml
<!-- Soma total geral -->
<variable name="V_TOTAL" class="java.math.BigDecimal" calculation="Sum">
    <variableExpression><![CDATA[$F{VLRTOT}]]></variableExpression>
</variable>

<!-- Soma que reseta por grupo -->
<variable name="V_TOTAL_OS" class="java.math.BigDecimal"
          resetType="Group" resetGroup="GRP_OS" calculation="Sum">
    <variableExpression><![CDATA[$F{VLRTOT}]]></variableExpression>
</variable>

<!-- Primeiro valor do grupo (para exibir cabeçalho) -->
<variable name="V_RAZAOSOCIAL" class="java.lang.String" calculation="First">
    <variableExpression><![CDATA[$F{RAZAOSOCIAL}]]></variableExpression>
    <initialValueExpression><![CDATA[""]]></initialValueExpression>
</variable>
```

Variáveis built-in: `$V{PAGE_NUMBER}`, `$V{REPORT_COUNT}`.

## Expressões

```java
// Acesso básico
$F{CAMPO}       // campo da query
$P{PARAM}       // parâmetro
$V{VARIAVEL}    // variável calculada

// Null-safe — opção 1: ternário
$F{NOME} == null ? "" : $F{NOME}

// Null-safe — opção 2: isBlankWhenNull="true" no textField (mais limpo)

// Comparar String — sempre .equals(), nunca ==
"bloco1".equals($F{BLOCO})

// Formatar data
new java.text.SimpleDateFormat("dd/MM/yyyy").format($F{DTNEG})

// Formatar Timestamp de parâmetro
new java.text.SimpleDateFormat("dd/MM/yyyy").format($P{P_DTINI})

// Divisão segura
($F{VLRTOT} != null && $F{QTD} != null && $F{QTD}.doubleValue() != 0)
  ? $F{VLRTOT}.divide($F{QTD}, 2, java.math.RoundingMode.HALF_UP)
  : java.math.BigDecimal.ZERO

// Condicional
($F{STATUS}.intValue() <= 5) ? "SIMULAÇÃO" : "DOCUMENTO VÁLIDO"

// Paginação — campo normal
"Página " + $V{PAGE_NUMBER} + " de"
// Paginação — total (evaluationTime="Report")
" " + $V{PAGE_NUMBER}

// Número com padding
String.format("%04d", $V{PAGE_NUMBER})
```

Boas práticas: manter expressões curtas; mover cálculos repetidos para variáveis; evitar lógica de negócio pesada no `.jrxml`.
