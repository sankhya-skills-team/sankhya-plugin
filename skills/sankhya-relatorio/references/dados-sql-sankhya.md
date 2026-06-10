# Dados, SQL e Sankhya

Use para query Oracle, datasource, grupos, subdatasets, parâmetros de data e performance de dados.

## Datasources

Para relatórios Sankhya, o caminho principal é JDBC via `REPORT_CONNECTION`.

Outras origens possíveis:
- `JREmptyDataSource` — relatório baseado apenas em parâmetros, subreports ou layout fixo (ex: `Select 1 from dual`)
- `JavaBeans` — coleção Java já carregada
- XML/CSV — arquivos estruturados

## SQL Oracle — boas práticas

- Evitar `SELECT *`; usar aliases claros e estáveis
- Filtrar e ordenar no banco
- Retornar apenas campos usados no layout
- Testar a query isoladamente antes de ajustar layout

Ao alterar SQL: atualizar `<field>` no `.jrxml`, revisar tipos Java, revisar grupos/variáveis que dependem dos campos.

## Parâmetros em SQL

```sql
-- Filtro direto
WHERE DTNEG BETWEEN $P{P_DTINI} AND $P{P_DTFIM}
AND CAB.CODEMP = $P{P_CODEMP}

-- Parâmetro opcional (null = sem filtro)
AND (CAB.CODVEND = $P{P_CODVEND} OR $P{P_CODVEND} IS NULL)

-- Filtro por data com trunc
AND TRUNC(CAB.DTNEG) >= TRUNC($P{P_DTINI})
AND TRUNC(CAB.DTNEG) <= TRUNC($P{P_DTFIM})
```

**Regra crítica Sankhya:** parâmetros de data **sempre** `java.sql.Timestamp` — o Sankhya não preenche `java.util.Date` corretamente.

## Grupos

**Regra crítica:** `ORDER BY` da query **deve** acompanhar a expressão do grupo. Sem ordenação correta o agrupamento falha silenciosamente.

```xml
<group name="GRP_EMPRESA">
    <groupExpression><![CDATA[$F{CODEMP}]]></groupExpression>
    <groupHeader>
        <band height="20">...</band>
    </groupHeader>
    <groupFooter>
        <band height="30">...</band>
    </groupFooter>
</group>
```

Query correspondente:
```sql
ORDER BY CODEMP, DTNEG
```

Usar `groupHeader` para título do grupo e `groupFooter` para subtotais.

## `printWhenExpression` — controle de visibilidade

Útil quando um único detalhe exibe dados de blocos diferentes (ex: UNION ALL com coluna discriminadora):

```xml
<textField isBlankWhenNull="true">
    <reportElement x="0" y="0" width="200" height="14">
        <printWhenExpression><![CDATA["bloco1".equals($F{BLOCO})]]></printWhenExpression>
    </reportElement>
    ...
</textField>
```

## Subdatasets

Subdatasets são declarados fora da query principal e usados por `table`, `list`, `crosstab` e `chart`.

```xml
<subDataset name="DS_EMPRESA">
    <parameter name="P_CODEMP" class="java.math.BigDecimal"/>
    <queryString>
        <![CDATA[SELECT RAZAOSOCIAL, CGC FROM TSIEMP WHERE CODEMP = $P{P_CODEMP}]]>
    </queryString>
    <field name="RAZAOSOCIAL" class="java.lang.String"/>
    <field name="CGC" class="java.lang.String"/>
</subDataset>
```

Como referenciar no componente (`datasetRun`):
```xml
<datasetRun subDataset="DS_EMPRESA">
    <datasetParameter name="P_CODEMP">
        <datasetParameterExpression><![CDATA[$P{P_CODEMP}]]></datasetParameterExpression>
    </datasetParameter>
    <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
</datasetRun>
```

Boas práticas: nomear claramente; passar apenas parâmetros necessários; testar a query isoladamente.

## Performance de dados

Principais riscos:
- Subreport executando query pesada por linha do pai — principal gargalo
- Query sem filtros retornando volume desnecessário
- Falta de `ORDER BY` para grupos
- Imagens grandes embutidas

Melhorias:
- Agregar no SQL quando possível (evita calcular no layout)
- Trocar subreport simples por `group` ou `table` quando não há reutilização
- Usar índices adequados nas colunas de filtro
- Reduzir campos retornados
- Considerar virtualizer em relatórios grandes (muitas páginas)
- Usar variáveis para cálculos repetidos em vez de recomputar em cada expressão

## Checklist de dados

- A query retorna todos os campos usados?
- Os aliases SQL batem com os `<field>` declarados?
- Os tipos Java estão corretos (`BigDecimal` para valores, `Timestamp` para datas)?
- Parâmetros de filtro têm prefixo `P_`?
- Parâmetros opcionais têm tratamento de null na query?
- Grupos têm `ORDER BY` correspondente no SQL?
- Subdatasets recebem `connectionExpression` e parâmetros corretos?
- A consulta evita volume desnecessário?
