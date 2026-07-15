---
name: sankhya-bi
description: Esta skill deve ser utilizada quando o usuário quiser "criar um dashboard no Sankhya", "criar um componente de BI", "montar um gadget", "criar gráfico de pizza/barras/colunas/linha no Sankhya OM", "criar tabela no dashboard", "adicionar parâmetro de filtro no dashboard", "gerar XML do dashboard", "importar componente de BI", "criar dashboard de estoque", "criar dashboard financeiro", "criar dashboard de vendas" ou qualquer variação de criação/configuração de dashboards e componentes de BI no Sankhya OM via Construtor de Componentes de BI.
---

# Dashboards Sankhya OM — Construtor de Componentes de BI

Especialidade: criação de componentes de BI (gadgets) no Sankhya OM via **Construtor de Componentes de BI**
(`Configurações > Avançado > Construtor de Componentes de BI`).

Os gadgets são os blocos individuais de análise (gráficos, tabelas, valores) que compõem um Dashboard.
Cada gadget é construído visualmente pelo modo **Design** ou diretamente pelo **XML** (gravado em `TSIGDG.CONFIG`).

**Idioma:** Respostas em Português do Brasil.

**Regra de ouro:** Entender o objetivo da análise antes de propor o tipo de visualização.

> **Default do pipeline = dashboard HTML5 moderno.** Quando o trabalho é gerar
> dashboard de addon (não um gadget pontual na home do ERP), a preferência é
> **html5 component** com visual moderno (cards/KPIs, gráficos via lib JS, layout
> responsivo) — feito pelo agent `sankhya-bi-report-dev`/`sankhya-frontend-dev`,
> apoiado pelo agent `sankhya-frontend-design-system`. Esta skill (gadget XML
> via Construtor de BI) aplica-se quando o usuário **pede explicitamente** o gadget
> nativo ou um KPI embutido na home padrão.

---

## Regras Obrigatórias de Geração de XML

As regras abaixo são invioláveis em qualquer XML gerado por esta skill:

**1. Proibido comentários XML**
Nunca incluir comentários `<!-- ... -->` no XML gerado. O Sankhya OM ignora comentários mas eles poluem o XML e podem causar erros em determinadas versões do parser.

**2. Proibido linhas vazias**
O XML deve ser compacto, sem linhas em branco entre elementos. Cada linha deve conter conteúdo.

**3. Nunca inventar campos de tabela**
Antes de referenciar qualquer coluna de tabela adicional (`AD_*`) ou tabela nativa menos conhecida:
- Verificar se o campo aparece no código Java do projeto (arquivos `.java`, helpers, eventos)
- Verificar se o campo aparece em queries SQL já existentes no projeto
- Se não houver fonte confiável, verificar os campos reais da tabela via MCP **sankhya-schema** (`describe_table`/`search_columns`) antes de incluí-los na query
- Campos de tabelas nativas Sankhya conhecidas (TGFCAB, TGFITE, TGFPAR, TGFFIN, TGFTOP, TSIEMP, etc.) podem ser usados com confiança — mas confirmar nomes exatos via MCP **sankhya-schema** quando houver dúvida
- Campos de tabelas adicionais (`AD_*`) do cliente **sempre exigem confirmação ou fonte no código**

**4. CSS dentro de value-expression com espaço após dois-pontos**
Dentro de `<value-expression>`, usar `display: flex` e não `display:flex`. O parser HTML do Sankhya não renderiza CSS compactado corretamente.

---

## Fluxo de Criação de um Gadget

### Etapa 0 — Perguntas obrigatórias antes de gerar qualquer SQL ou XML

Antes de escrever qualquer query, fazer as duas perguntas abaixo se a resposta não for conhecida pelo contexto:

**Pergunta 1 — Banco de dados:**
> "O Sankhya deste cliente usa **Oracle** ou **SQL Server**?"

A sintaxe SQL difere significativamente:

| Recurso | Oracle | SQL Server |
|---|---|---|
| Tabela fictícia | `FROM DUAL` | *(omitir FROM)* |
| Truncar data | `TRUNC(campo)` | `CAST(campo AS DATE)` |
| Nulo ou zero | `NVL(campo, 0)` | `ISNULL(campo, 0)` |
| Concatenar | `\|\|` | `+` ou `CONCAT()` |
| Limite de linhas | `ROWNUM <= N` | `TOP N` |
| Converter tipo | `TO_CHAR / TO_DATE` | `CONVERT / CAST` |
| NULLS LAST | `ORDER BY campo NULLS LAST` | `ORDER BY campo DESC` (workaround) |

**Pergunta 2 — Localização dos arquivos do projeto:**
> "Qual é a pasta raiz do projeto? (para salvar os arquivos nos caminhos corretos)"

---

## Onde salvar os arquivos gerados

Sempre salvar os arquivos nas pastas abaixo — nunca na raiz do projeto:

| Tipo | Caminho |
|---|---|
| Dashboard XML (gadget) | `Dashboards/<NomeModulo>/<nome-dashboard>.xml` |
| Componente HTML5 | `Dashboards/html5/<NomeDashboard>/index.html` (+ assets na mesma pasta) |

Exemplos:
- `Dashboards/Epic-8-StatusGlifosato/dashboard-glifosato.xml`
- `Dashboards/html5/PainelExpedicao/index.html`

Se o módulo ainda não tiver pasta em `Dashboards/`, criá-la antes de salvar.

---

### Etapa 1 — Entender a necessidade

Antes de qualquer coisa, identificar:

1. **O que o usuário quer enxergar?** (volume, valor, proporção, evolução, distribuição geográfica)
2. **Qual o nível de detalhe?** (totais, por período, por parceiro, por produto)
3. **Existem filtros interativos necessários?** (data, parceiro, empresa, produto)
4. **Haverá drill-down?** (clicar no gráfico abre um nível mais detalhado)

### Etapa 2 — Escolher o tipo de visualização

Usar a tabela abaixo como guia. Quando o tipo não estiver explícito no escopo, recomendar o mais adequado:

| Objetivo da análise | Tipo recomendado |
|---|---|
| Proporção entre categorias (% do total) | Pizza ou Donut |
| Comparação entre categorias no mesmo período | Barras ou Colunas |
| Evolução ao longo do tempo | Linha ou Área |
| Valor pontual / KPI / texto dinâmico | Controle > Valor |
| Lista de registros navegável | Controle > Tabela |
| Análise cruzada (linhas × colunas) | Controle > Tabela Dinâmica |
| Distribuição geográfica por estado/município | Gráfico > Geográfico ou Geomapa |
| Faixa de valores aceitáveis (meta vs realizado) | Velocímetro |
| Múltiplas dimensões em radar | Radar |
| Estágios de um funil (ex: pipeline) | Funil |
| Relação entre duas variáveis numéricas | Dispersão ou Bolha |
| Hierarquia proporcional de valores | TreeMap |

### Etapa 3 — Montar a query principal

Regras para a query SQL do gadget:

- A query deve retornar exatamente as colunas que o gadget vai consumir
- Para **gráficos cartesianos** (linha, barras, colunas): mínimo 1 coluna de categoria (eixo X) + 1 coluna de valor (eixo Y)
- Para **Pizza/Donut**: 1 coluna de rótulo + 1 coluna de valor
- Para **Tabela**: todas as colunas que aparecerão como colunas na tabela
- Para **Valor pontual**: query retorna 1 linha × 1 coluna (o valor a exibir)
- Referenciar parâmetros com `:ID_DO_PARAMETRO` (será traduzido para `(valor)` em tempo de execução)
- Parâmetros internos disponíveis sem declaração: `CODUSU_LOG`, `CODGRU_LOG`, `CODPARC_B2B`, `CODVEN_LOG`

**Exemplo de query com parâmetro:**
```sql
SELECT
    P.NOMEPARC,
    SUM(C.VLRNOTA) AS TOTAL
FROM TGFCAB C
JOIN TGFPAR P ON P.CODPARC = C.CODPARC
WHERE C.DTNEG BETWEEN :P_DT_INI AND :P_DT_FIN
  AND C.TIPMOV = 'V'
GROUP BY P.NOMEPARC
ORDER BY TOTAL DESC
```

### Etapa 4 — Definir os parâmetros

Para cada filtro interativo identificado na Etapa 1:

| Campo | O que informar |
|---|---|
| Id | Identificador único (ex: `P_PARCEIRO`, `P_DT_INI`) |
| Descrição | Label visível ao usuário |
| Tipo | Entidade/Tabela, Período, Data, Texto, Número Inteiro, Número Decimal, Single List, Multi List |
| Requerido | Sim/Não |
| Salvar último valor | Sim/Não (útil para datas) |

Tipos mais usados:
- **Período** → gera dois campos (data inicial + data final) com opção de marcar "Considerar data atual"
- **Entidade/Tabela** → gera campo de pesquisa vinculado a uma entidade do sistema (ex: Parceiro, Produto)
- **Single List / Multi List** com tipo de dado **SQL** → lista customizada por query

### Etapa 5 — Configurar o gadget no Design

1. Abrir `Configurações > Avançado > Construtor de Componentes de BI`
2. Incluir novo gadget (botão `+`)
3. Informar Título, Categoria e Descrição
4. Clicar em **Design**
5. Arrastar o tipo de componente para a área de trabalho
6. Clicar em **Editar** (duplo clique no componente)
7. Na aba **Expressão/Consulta**: colar a query SQL
8. Na aba **Parâmetros** (painel direito): criar os parâmetros de filtro
9. Na aba **Configurações**: definir dimensões, séries, rótulos, cores
10. Usar **Pré-visualizar** para validar antes de salvar

### Etapa 6 — Vincular ao Dashboard

Após salvar o gadget no Construtor de Componentes de BI, abrir o **Construtor de Dashboards**
(`Configurações > Avançado > Construtor de Dashboards`) e inserir o gadget no painel desejado.

---

## Estrutura XML do Gadget (`TSIGDG.CONFIG`)

O XML gerado pelo Design pode ser exportado e reimportado. Estrutura básica:

```xml
<gadget>
  <title>Título do Gadget</title>
  <components>
    <component type="bar">          <!-- tipo: bar, line, pie, donut, column, table, value, etc. -->
      <query><![CDATA[
        SELECT ... FROM ... WHERE ...
      ]]></query>
      <parameters>
        <parameter id="P_DT_INI" type="date" required="true" />
      </parameters>
      <settings>
        <dimension field="NOMEPARC" />
        <series field="TOTAL" label="Total Vendas" />
      </settings>
    </component>
  </components>
</gadget>
```

> O XML completo varia por tipo de componente. Consultar `references/03-graficos.md` para estrutura específica por tipo de gráfico.

---

## Níveis de Drill-Down

Gadgets suportam múltiplos níveis: clicar em um elemento abre o próximo nível.

- Cada nível é configurado como um componente independente dentro do mesmo gadget
- O valor clicado pode ser passado via **Argumento** para filtrar o próximo nível
- Não deixar containers de nível intermediário vazios — causa erros no sistema
- Usar os botões "voltar ao nível anterior" / "avançar nível" disponíveis na toolbar

---

## Componente HTML5 — Dashboards Customizados

Para painéis que precisam de mais flexibilidade (kanban, tabelas operacionais com edição inline,
progress bars, etc.), usar o **Controle > HTML5** em vez dos gadgets nativos.

Dois padrões disponíveis:
- **JSP + `<snk:load/>`** → `executeQuery(sql, arr, onSuccess, onError)` — suporta `${BASE_FOLDER}` para assets
- **HTML puro + SankhyaJX** → `JX.consultar(sql).then(result => ...)` — mais simples, sem servidor

Ambos são empacotados em ZIP: `NNN_html5Component.zip` contendo pasta `index/` com o arquivo principal.

**Template pronto:** `examples/template-tabela-operacional.html`

---

## Referências

| Tópico | Arquivo |
|---|---|
| Introdução, Design vs XML, Área de Trabalho, Cartões Inteligentes | `references/01-introducao-design.md` |
| Controles: Valor, Tabela, Tabela Dinâmica, Geomapa, HTML5, IReport | `references/02-controles.md` |
| Todos os tipos de gráfico + Acumular Valores | `references/03-graficos.md` |
| Parâmetros, Configurações, Variáveis, Argumentos, Quadrante Expressão | `references/04-configuracoes-logica.md` |
| Eventos, Ações, Pré-Visualização, Impressão/Exportação | `references/05-eventos-acoes.md` |
| **HTML5 Component**: JSP vs HTML, SankhyaJX, API direta, XML, deploy | `references/06-html5-component.md` |
| **Padrões XML Avançados**: drill-down multi-nível, args tipados, formatadores, geochart, KPI cards, refresh-details, on-click-launcher, SQL reutilizável | `references/07-padroes-xml-avancados.md` |
