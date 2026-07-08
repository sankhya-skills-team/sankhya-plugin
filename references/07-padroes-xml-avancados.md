# Padrões XML Avançados — Sankhya BI

Padrões extraídos de um dashboard de certificação real, cobrindo drill-down multi-nível,
argumentos tipados, formatadores condicionais, geochart interativo e KPI cards em HTML.

---

## 1. Estrutura Geral do XML

```xml
<gadget refresh-time="60000">

  <!-- Parâmetros de filtro globais (barra superior) -->
  <prompt-parameters>
    <parameter ... />
  </prompt-parameters>

  <!-- Nível principal (sempre o primeiro) -->
  <level id="NIVEL_PRINCIPAL" description="Principal">
    <container orientacao="H" tamanhoRelativo="100">
      ...
    </container>
  </level>

  <!-- Níveis de drill-down (acessados via on-click) -->
  <level id="LVL_2A" description="n2_detalhe">
    <args>
      <arg id="A_CODPARC" type="integer" label="A_CODPARC : Número Inteiro"/>
    </args>
    <container orientacao="V" tamanhoRelativo="100">
      ...
    </container>
  </level>

</gadget>
```

**Regra crítica:** Nunca deixar container de nível intermediário vazio — causa erro no sistema.

---

## 2. Tipos de Parâmetros (`<prompt-parameters>`)

### Período (datePeriod)
```xml
<parameter id="P_PERIODO" description="Período" metadata="datePeriod"
           required="true" keep-last="true" keep-date="true" order="0"/>
```
- Uso na query: `:P_PERIODO.INI` e `:P_PERIODO.FIN`
- `keep-date="true"` → usa data atual como padrão

### Entidade (entity lookup)
```xml
<parameter id="P_PARCEIRO" description="Parceiro" metadata="entity:Parceiro@CODPARC"
           required="false" keep-last="true" order="1"/>
<parameter id="P_CODNAT"   description="Natureza" metadata="entity:Natureza@CODNAT"
           required="false" keep-last="false" order="2"/>
```
- Gera campo de pesquisa vinculado à entidade nativa do sistema
- Uso na query: `:P_PARCEIRO`, `:P_CODNAT`

### Boolean
```xml
<parameter id="P_CONFIR" description="Apenas Confirmados?" metadata="boolean"
           required="false" keep-last="true" order="3"/>
```
- Valores retornados: `'S'` (marcado) / `'N'` (desmarcado)
- Uso na query: `AND (CAB.STATUSNOTA = 'L' OR :P_CONFIR = 'N')`

### Seleção única via SQL (singleList:Text)
```xml
<parameter id="P_STATUS" description="Status" metadata="singleList:Text"
           listType="sql" required="false" keep-last="false" order="2">
  <expression type="SQL"><![CDATA[
    SELECT '' AS VALUE, 'Ambos / Todos' AS LABEL FROM DUAL
    UNION ALL
    SELECT 'A' AS VALUE, 'Alto' AS LABEL FROM DUAL
    UNION ALL
    SELECT 'B' AS VALUE, 'Baixo' AS LABEL FROM DUAL
  ]]></expression>
</parameter>
```

> **Regra:** Sempre incluir a opção "Ambos / Todos" com `VALUE=''` como **primeira entrada** da lista. Sem ela, o usuário não consegue voltar a ver todos os registros após filtrar por um valor específico.

Filtro SQL correspondente — tratar NULL (nada selecionado) **e** string vazia (selecionou "Ambos"):
```sql
AND (RAM.CAMPO = :P_STATUS OR :P_STATUS IS NULL OR :P_STATUS = '')
```

### Multi-seleção via SQL (multiList:Text)
```xml
<parameter id="P_EMPRESA" description="Empresa" metadata="multiList:Text"
           listType="sql" required="false" keep-last="true" order="4">
  <expression type="SQL"><![CDATA[
    SELECT CODEMP AS VALUE, CODEMP || ' - ' || NOMEFANTASIA AS LABEL
    FROM TSIEMP
    ORDER BY 1
  ]]></expression>
</parameter>
```
- Uso na query com `IN`: `AND (CAB.CODEMP IN :P_EMPRESA)`
- multiList não precisa de opção "Todos" — quando nada está selecionado o parâmetro retorna todos

---

## 3. Tipos de Argumentos (`<args>`)

Argumentos são passados entre níveis via drill-down. Tipos disponíveis:

| Tipo | Declaração no `<arg>` | Uso na query |
|---|---|---|
| Inteiro | `type="integer"` | `:A_CODPARC` |
| Texto | `type="text"` | `:A_UF` |
| Decimal | `type="decimal"` | `:A_TOTAL` |
| Data | `type="date"` | `:A_DTMOV` |
| Data/Hora | `type="dateTime"` | `:A_DTNEG` |

**Declaração no nível filho:**
```xml
<level id="LVL_2" description="nv2_detalhe">
  <args>
    <arg id="A_CODPARC"  type="integer"  label="A_CODPARC : Número Inteiro"/>
    <arg id="A_UF"       type="text"     label="A_UF : Texto"/>
    <arg id="A_TOTAL"    type="decimal"  label="A_TOTAL : Número Decimal"/>
    <arg id="A_DTMOV"    type="date"     label="A_DTMOV : Data"/>
    <arg id="A_DTNEG"    type="dateTime" label="A_DTNEG : Data/Hora"/>
  </args>
  ...
</level>
```

**Args locais em grid** (para refresh-details):
```xml
<grid id="grd_detalhe" useNewGrid="S">
  <args>
    <arg id="A_CODVEND" type="integer"></arg>
    <arg id="A_APELIDO" type="text"></arg>
    <arg id="A_TICKET"  type="decimal"></arg>
  </args>
  ...
</grid>
```

---

## 4. Padrões de on-click

### 4.1 Drill-down (navigate-to) — em `<grid>`
```xml
<grid id="grd_principal" useNewGrid="S">
  ...
  <on-click navigate-to="LVL_2">
    <param id="A_CODEMP">$CODEMP</param>
    <param id="A_DESCROPER">$DESCROPER</param>
  </on-click>
</grid>
```

### 4.2 Drill-down — em `<serie>` de gráfico
```xml
<series>
  <serie type="pizza">
    <field>TOTAL</field>
    <nameField>NATUREZA</nameField>
    <on-click navigate-to="LVL_DETALHE">
      <param id="A_NATUREZA">$CODNAT</param>
    </on-click>
  </serie>
</series>
```

### 4.3 Drill-down — em `<region-marker>` de geochart
```xml
<region-marker>
  <name>$UF</name>
  <value>$TOTAL</value>
  <on-click navigate-to="LVL_2">
    <param id="A_UF">$UF</param>
    <param id="A_DESCRICAO">$DESCRICAO</param>
  </on-click>
</region-marker>
```

> Note: `<region-marker>` aceita **ou** `<on-click>` **ou** `<refresh-details>` — não ambos.

### 4.4 Lançar tela nativa (on-click-launcher)
```xml
<!-- Central de Notas (TGFCAB) -->
<on-click-launcher resource-id="br.com.sankhya.com.mov.CentralNotas">
  <NUNOTA>$NUNOTA</NUNOTA>
</on-click-launcher>

<!-- Movimentação Financeira (TGFFIN) -->
<on-click-launcher resource-id="br.com.sankhya.fin.cad.movimentacaoFinanceira">
  <NUFIN>$NUFIN</NUFIN>
</on-click-launcher>
```
O campo dentro da tag é a chave primária da entidade alvo.

---

## 5. refresh-details — Sincronização entre Componentes

Atualiza outro componente ao clicar/selecionar, sem navegar de nível.

### Em geochart → atualiza grid
```xml
<region-marker>
  <name>$UF</name>
  <value>$TOTAL</value>
  <refresh-details ui-list="grd_detalhe">
    <param id="A_UF">$UF</param>
  </refresh-details>
</region-marker>
```

### Em série de gráfico → atualiza grid (múltiplos params)
```xml
<serie type="column">
  <xField>$APELIDO</xField>
  <yField>$TICKET</yField>
  <display><![CDATA[Ticket Médio]]></display>
  <color>0xCC0099</color>
  <refresh-details ui-list="grd_detalhe">
    <param id="A_CODVEND">$CODVEND</param>
    <param id="A_APELIDO">$APELIDO</param>
    <param id="A_TICKET">$TICKET</param>
  </refresh-details>
</serie>
```

O `ui-list` aponta para o `id` do grid/componente alvo. O grid alvo deve ter `<args>` declarados com os mesmos IDs recebidos.

---

## 6. Formatadores Condicionais em Grid

### 6.1 Cores por faixa (greaterThan / lessThan)
```xml
<field name="CRESCIMENTO" label="Var.%" type="F" visible="true" useFooter="false">
  <formatter greaterThan="0">
    <![CDATA[<span style="background-color:#d9ead3; color:#38761d; font-weight:bold; padding:2px 6px; border-radius:4px"> $VALUE%</span>]]>
  </formatter>
  <formatter lessThan="0">
    <![CDATA[<span style="background-color:#fce5cd; color:#c00; font-weight:bold; padding:2px 6px; border-radius:4px"> $VALUE%</span>]]>
  </formatter>
</field>
```

### 6.2 Ícones por valor exato (equalThan)
```xml
<field name="ICONE" label="vs Ticket Médio" type="F" visible="true" useFooter="false">
  <formatter equalThan="1">
    <![CDATA[<span style="; src:iconFlagGreen; somente-icone:S">$VALUE</span>]]>
  </formatter>
  <formatter equalThan="2">
    <![CDATA[<span style="; src:iconFlagRed;   somente-icone:S">$VALUE</span>]]>
  </formatter>
  <formatter equalThan="3">
    <![CDATA[<span style="; src:iconFlagYellow; somente-icone:S">$VALUE</span>]]>
  </formatter>
</field>
```

**SQL que gera os valores de controle:**
```sql
CASE WHEN :A_TICKET <= CAB.VLRNOTA THEN 1   -- acima do ticket → verde
     WHEN :A_TICKET >  CAB.VLRNOTA THEN 2   -- abaixo → vermelho
     WHEN :A_TICKET IS NULL        THEN 3   -- sem referência → amarelo
END AS ICONE
```

**Ícones disponíveis:** `iconFlagGreen`, `iconFlagRed`, `iconFlagYellow`
`somente-icone:S` oculta o valor numérico e exibe apenas o ícone.

### 6.3 FAROL (traffic light) — campo especial
```xml
<!-- Na query: gera código de cor como string -->
CASE WHEN FIN.RECDESP > 0 THEN 'GOLD' ELSE '#86C154' END AS FAROL,

<!-- No metadata: type="L" ativa o modo semáforo -->
<field name="FAROL" label="FAROL" type="L" visible="true" useFooter="false"/>
```
O campo `type="L"` renderiza a célula como indicador colorido com a cor fornecida pelo SQL.

---

## 7. simple-value como KPI Card / Cabeçalho de Seção

**Sintaxe no value-expression:**
- `$CAMPO` → valor retornado pela query (já formatado com a máscara)
- `:P_PARAM` → valor do parâmetro de filtro (string bruta)
- `:A_ARG` → valor do argumento do nível (string bruta)

### 7.1 KPI Cards horizontais (padrão recomendado)

Cards lado a lado com borda colorida à esquerda — padrão validado em produção. Usar sempre que o objetivo for exibir múltiplos indicadores em linha.

> **IMPORTANTE:** O CSS dentro do `value-expression` deve usar **espaço após os dois-pontos** (`display: flex`, não `display:flex`). O parser HTML do Sankhya não renderiza corretamente propriedades CSS sem espaço, deixando os cards na vertical sem formatação.

```xml
<simple-value id="svl_kpi">
  <expression type="sql"><![CDATA[
    SELECT
      COUNT(*)                                                   AS TOTAL,
      SUM(CASE WHEN CAB.TIPMOV = 'V' THEN CAB.VLRNOTA ELSE 0 END) AS VLR_VENDA,
      COUNT(DISTINCT CAB.CODPARC)                                AS QTD_PARCEIROS
    FROM TGFCAB CAB
    WHERE CAB.DTNEG BETWEEN :P_PERIODO.INI AND :P_PERIODO.FIN
    AND CAB.CODEMP IN :P_EMPRESA
  ]]></expression>
  <metadata>
    <field name="TOTAL"         label="Total Notas"  type="I" visible="true" useFooter="false"/>
    <field name="VLR_VENDA"     label="Valor Vendas" type="F" visible="true" useFooter="false" mask="R$ #.##0,00"/>
    <field name="QTD_PARCEIROS" label="Parceiros"    type="I" visible="true" useFooter="false"/>
  </metadata>
  <value-expression><![CDATA[<div style="display: flex; justify-content: space-between; gap: 16px; padding: 10px; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">

    <div style="flex: 1; background: #ffffff; border-radius: 8px; padding: 15px; text-align: center; border-left: 5px solid #64748b; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #64748b; font-weight: 600;">Total de Notas</div>
        <div style="font-size: 28px; font-weight: 800; color: #1e293b; margin-top: 5px;">$TOTAL</div>
    </div>

    <div style="flex: 1; background: #eff6ff; border-radius: 8px; padding: 15px; text-align: center; border-left: 5px solid #2563eb; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #2563eb; font-weight: 600;">Valor Vendas</div>
        <div style="font-size: 28px; font-weight: 800; color: #2563eb; margin-top: 5px;">$VLR_VENDA</div>
    </div>

    <div style="flex: 1; background: #f0fdf4; border-radius: 8px; padding: 15px; text-align: center; border-left: 5px solid #16a34a; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #16a34a; font-weight: 600;">Parceiros</div>
        <div style="font-size: 28px; font-weight: 800; color: #16a34a; margin-top: 5px;">$QTD_PARCEIROS</div>
    </div>

</div>]]></value-expression>
</simple-value>
```

**Anatomia de cada card:**
```
border-left: 5px solid ACCENT_COLOR   ← faixa colorida à esquerda (identidade visual)
background: COR_FUNDO                 ← fundo levemente colorido (tom claro da cor)
box-shadow: 0 2px 4px rgba(0,0,0,0.05) ← elevação sutil
font-size: 11px + uppercase           ← label pequeno e discreto no topo
font-size: 28px + font-weight: 800    ← valor em destaque abaixo
```

**Paleta de cores sugerida por status:**

| Contexto | background | border-left | color texto |
|---|---|---|---|
| Neutro / Total | `#ffffff` | `#64748b` | `#1e293b` |
| Positivo / OK | `#f0fdf4` | `#16a34a` | `#16a34a` |
| Atenção / Alerta | `#fefce8` | `#ca8a04` | `#ca8a04` |
| Negativo / Erro | `#fff1f2` | `#dc2626` | `#dc2626` |
| Informativo | `#eff6ff` | `#2563eb` | `#2563eb` |
| Cinza / Sem dados | `#fafafa` | `#d4d4d4` | `#737373` |

**Regra de quantidade:** de 2 a 5 cards por linha. Acima de 5, dividir em dois `simple-value` empilhados.

### 7.2 Cabeçalho de contexto (drill-down)

Quando o nível 2 recebe argumentos de drill-down, usar `simple-value` para exibir o contexto da seleção:

```xml
<simple-value id="svl_header">
  <expression type="sql"><![CDATA[
    SELECT PAR.NOMEPARC FROM TGFPAR PAR WHERE PAR.CODPARC = :A_CODPARC
  ]]></expression>
  <metadata>
    <field name="NOMEPARC" label="Parceiro" type="S" visible="true" useFooter="false"/>
  </metadata>
  <value-expression><![CDATA[<div style="padding:10px 0;height:100%;display:flex;align-items:center;"><div style="background:#f8f9fa;border-radius:12px;padding:14px 20px;border:1px solid #e2e8f0;width:100%;font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif;"><h3 style="margin:0 0 6px;font-size:17px;color:#1e293b;">$NOMEPARC</h3><p style="margin:0;color:#64748b;font-size:13px;"><b>Período:</b> :P_PERIODO.INI á :P_PERIODO.FIN</p></div></div>]]></value-expression>
</simple-value>
```

### 7.3 Caracteres especiais em títulos

O Sankhya pode converter caracteres especiais em `?` durante o export/import do XML. Evitar em `<title>`:

| Evitar | Substituir por |
|---|---|
| `—` (em-dash) | `-` ou ` / ` |
| `–` (en-dash) | `-` |
| `"` `"` (aspas curvas) | `"` (aspas retas) |
| `•` `·` (bullets) | `*` ou omitir |

Exemplo correto: `<title><![CDATA[Analise Quimica - Glifosato]]></title>`
Exemplo problemático: `<title><![CDATA[Análise Química — Glifosato]]></title>` → vira `?`

---

## 8. Gráfico de Colunas — Padrões

### Múltiplas séries com refresh-details
```xml
<chart id="cht_colunas" type="column" nroColuna="6">
  <title><![CDATA[Ticket Médio por Vendedor]]></title>
  <expression type="sql" ...><![CDATA[ ... ]]></expression>
  <metadata> ... </metadata>

  <horizontal-axis>
    <category field="APELIDO" rotation="0" dropLabel="false">
      <initView value="first"/>
    </category>
  </horizontal-axis>

  <series>
    <serie type="column">
      <xField>$APELIDO</xField>
      <yField>$TICKET</yField>
      <display><![CDATA[Ticket Médio]]></display>
      <color>0xCC0099</color>
      <refresh-details ui-list="grd_detalhe">
        <param id="A_CODVEND">$CODVEND</param>
        <param id="A_APELIDO">$APELIDO</param>
        <param id="A_TICKET">$TICKET</param>
      </refresh-details>
    </serie>
    <serie type="column">
      <xField>$TICKET</xField>
      <yField>$QTD</yField>
      <display><![CDATA[Qtd. Notas]]></display>
      <color>0xFF6699</color>
      <refresh-details ui-list="grd_detalhe">
        <param id="A_CODVEND">$CODVEND</param>
      </refresh-details>
    </serie>
  </series>

  <legend position="bottom" direction="h"/>
</chart>
```

**Atributos relevantes:**
- `nroColuna="6"` → limita colunas visíveis com scroll horizontal
- `rotation="0"` → ângulo dos rótulos do eixo X (0 = horizontal, -45 = diagonal)
- `dropLabel="false"` → não omite rótulos quando há sobreposição
- `<initView value="first"/>` → exibe do primeiro elemento

---

## 9. Geochart — Padrões Completos

```xml
<geochart id="gch_estados">
  <title><![CDATA[Vendas por Estado]]></title>
  <expression type="sql" data-source="MGEDS"><![CDATA[
    SELECT UFS.UF, SUM(TOTAL) AS TOTAL
    FROM ...
    GROUP BY UFS.UF
  ]]></expression>
  <metadata>
    <field name="UF"    label="UF"    type="S" visible="true" useFooter="false"/>
    <field name="TOTAL" label="Total" type="I" visible="true" useFooter="false" mask="R$ #.##0,00"/>
  </metadata>
  <country>BR</country>
  <legend show="false" colors="#D16E8D"/>
  <region-marker>
    <name>$UF</name>
    <value>$TOTAL</value>
    <!-- OPÇÃO A: refresh-details (atualiza outro componente) -->
    <refresh-details ui-list="grd_por_estado">
      <param id="A_UF">$UF</param>
    </refresh-details>
    <!-- OPÇÃO B: on-click navigate-to (abre nível de drill-down) -->
    <!-- <on-click navigate-to="LVL_2"><param id="A_UF">$UF</param></on-click> -->
  </region-marker>
</geochart>
```

**Regra:** `<region-marker>` aceita `<on-click>` **OU** `<refresh-details>`, nunca ambos.
**`<country>BR</country>`** — obrigatório para mapa do Brasil.
**Query obrigatória:** retornar coluna `UF` (sigla de 2 letras) + coluna de valor.

---

## 10. Padrões SQL Reutilizáveis

### Fórmula padrão de valor de nota/item
```sql
((ITE.VLRTOT - ITE.VLRDESC - ITE.VLRREPRED + ITE.VLRSUBST + ITE.VLRIPI)
    * VCA.INDITENS)
    * CASE WHEN TPO.BONIFICACAO = 'S' THEN 0 ELSE 1 END
    * TPO.GOLDEV AS TOTAL
```
Requer JOINs:
- `TGFTOP TPO ON (CAB.CODTIPOPER = TPO.CODTIPOPER AND CAB.DHTIPOPER = TPO.DHALTER)`
- `TGFITE ITE ON (CAB.NUNOTA = ITE.NUNOTA)`
- `VGFCAB VCA ON (CAB.NUNOTA = VCA.NUNOTA)` ← view, não tabela

### Filtros opcionais por tipo de dado

```sql
-- INTEGER: usar NVL com -1
AND (CAB.CODPARC = :P_PARCEIRO OR NVL(:P_PARCEIRO,-1) = -1)

-- TEXT/DATE: usar IS NULL
AND (UFS.UF = :A_UF OR :A_UF IS NULL)
AND (CAB.DTNEG = :A_DTNEG OR :A_DTNEG IS NULL)

-- DECIMAL comparativo (filtro de valores maiores que o selecionado)
AND TOTAL > :A_TOTAL

-- MULTI-LIST (IN): sem OR — parâmetro nunca é nulo quando multiList
AND (CAB.CODEMP IN :P_EMPRESA)
```

### Agrupamento por Mês/Ano
```sql
TO_CHAR(CAB.DTNEG, 'YYYY/MM') AS ANOMES   -- grupo e exibição
-- Filtro:
AND TO_CHAR(CAB.DTNEG, 'YYYY/MM') = :A_ANOMES
```

### Filtros padrão para notas de venda confirmadas
```sql
WHERE TPO.GOLSINAL  = -1          -- sinal negativo = saída (venda)
AND   CAB.STATUSNOTA = 'L'        -- nota confirmada (liberada)
AND   ITE.USOPROD   <> 'D'        -- exclui itens de devoluções internas
AND   ITE.SEQUENCIA > 0           -- exclui cabeçalho de itens (sequência 0)
```

### Boolean param
```sql
-- Quando P_CONFIR = 'S': só confirmadas
-- Quando P_CONFIR = 'N': todas
AND (CAB.STATUSNOTA = 'L' OR :P_CONFIR = 'N')
```

---

## 11. Grid com Título Dinâmico e HTML

O título de qualquer componente aceita HTML e referências a argumentos:

```xml
<title><![CDATA[Detalhes<br>:A_APELIDO]]></title>
```

Permite exibir o contexto do drill-down diretamente no título do componente filho.

---

## 12. Grid — Campos Ocultos e Visíveis

```xml
<!-- Campo auxiliar (chave para on-click), oculto na tabela -->
<field name="CODNAT" label="Cód. Natureza" type="I" visible="false" useFooter="false"/>

<!-- Campo visível com total somado no rodapé -->
<field name="TOTAL"  label="Total"         type="F" visible="true"  useFooter="SUM" mask="R$ #.##0,00"/>

<!-- Campo de data sem rodapé -->
<field name="DTNEG"  label="Data Neg."     type="D" visible="true"  useFooter="false"/>
```

**Tipos de campo:**
- `I` → Inteiro
- `F` → Float/Decimal
- `S` → String/Texto
- `D` → Data
- `L` → FAROL (traffic light)

**useFooter:** `SUM`, `AVG`, `COUNT`, `false`

---

## 13. Layout e Containers

### Orientações
- `orientacao="H"` → colunas lado a lado
- `orientacao="V"` → linhas empilhadas

### tamanhoRelativo
Soma dos filhos diretos deve ser ~100. Valores decimais são aceitos:

```xml
<container orientacao="V" tamanhoRelativo="100">
  <container orientacao="V" tamanhoRelativo="28.77">  <!-- ~29% -->
    <simple-value .../>
  </container>
  <container orientacao="V" tamanhoRelativo="72.23">  <!-- ~71% -->
    <geochart .../>
  </container>
</container>
```

### Layout misto com navigation buttons
```xml
<container orientacao="H" tamanhoRelativo="100">
  <!-- Coluna esquerda: 50% -->
  <container orientacao="V" tamanhoRelativo="50">
    <grid id="grd_principal" .../>
  </container>
  <!-- Coluna direita: 50% dividida V -->
  <container orientacao="V" tamanhoRelativo="50">
    <container orientacao="V" tamanhoRelativo="50">
      <geochart .../>
    </container>
    <container orientacao="V" tamanhoRelativo="50">
      <chart type="pizza" .../>
    </container>
  </container>
</container>
```

---

## 14. Botões de Navegação via simple-value

Para criar botões de navegação entre níveis no nível principal:

```xml
<simple-value id="svl_btn_nav">
  <expression type="sql" data-source="MGEDS"><![CDATA[
    SELECT 'Ver Mapa Geográfico' AS LABEL FROM DUAL
  ]]></expression>
  <metadata>
    <field name="LABEL" label="LABEL" type="S" visible="true" useFooter="false"/>
  </metadata>
  <value-expression><![CDATA[
    <div style="cursor:pointer; padding:8px 16px; background:#2563eb; color:#fff;
                border-radius:8px; display:inline-block; font-weight:600;">
      $LABEL
    </div>
  ]]></value-expression>
  <on-click navigate-to="LVL_GEOGRAFICO">
    <param id="A_DESCROPER">$DESCROPER</param>
  </on-click>
</simple-value>
```

---

## 15. data-source Externo

Para consultar banco de dados externo (não o banco do Sankhya OM):

```xml
<expression type="sql" data-source="NOME_DO_DATASOURCE"><![CDATA[
  SELECT ... FROM tabela_externa
]]></expression>
```

`data-source="MGEDS"` é o datasource padrão do próprio Sankhya OM quando configurado como externo.
Para o banco próprio do sistema (padrão), omitir o atributo `data-source`.

---

## 16. Checklist de Boas Práticas (extraído do dashboard real)

- Usar `useNewGrid="S"` em todos os grids para layout moderno
- Sempre declarar `<args>` no nível filho quando receber argumentos
- Declarar `<args>` locais no grid quando ele recebe `refresh-details`
- Campos-chave usados em `on-click` devem estar no metadata (podem ser `visible="false"`)
- Formatador com `equalThan` exige que o SQL retorne valor numérico exato (1, 2, 3...)
- `type="L"` (FAROL) exige que o SQL retorne uma string de cor CSS válida (`'#86C154'`, `'GOLD'`, etc.)
- Parâmetros opcionais de entidade → `OR NVL(:P_PARAM,-1)=-1` (integer) ou `OR :P_PARAM IS NULL` (texto/data)
- Para geochart BR, a coluna UF deve retornar sigla de 2 letras maiúsculas
- `refresh-details` no geochart impede uso simultâneo de `on-click` — escolher um dos dois
- Multiple `<serie>` no mesmo gráfico podem ter `refresh-details` diferentes
- `value-expression` aceita args (`:A_UF`) e params (`:P_PERIODO.INI`) além de campos (`$VALOR`)
