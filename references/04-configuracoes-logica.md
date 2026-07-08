# Parâmetros, Configurações, Variáveis, Argumentos e Expressão

No Design, o painel direito traz as abas **Parâmetros**, **Configurações**, **Variáveis** e **Argumentos**.

---

## Parâmetros

Filtros do gadget na tela de visualização do Dashboard. Ao clicar **OK**, o sistema valida a estrutura da query e reporta erros.

Campos do parâmetro:

| Campo | Descrição |
|---|---|
| Id | identificador único |
| Descrição | label |
| Requerido | obrigatório ou não |
| Salvar último valor | salva o último valor informado |
| Mostrar inativas | permite pesquisar registros inativos nos filtros |
| Tipo | ver abaixo |

**Tipos:** Entidade/Tabela, Período, Data, Texto, Data/Hora, Número Inteiro, Número Decimal, Verdadeiro/Falso, Single List, Multi List.

Campos que aparecem conforme o Tipo:
- **Texto / Número Inteiro / Número Decimal** → **Limite de caracteres**.
- **Data / Data/Hora / Período** → **Considerar data atual?** (na abertura do Dashboard, preenche com a data atual).
- **Número Inteiro / Número Decimal** → **Range** (intervalo permitido).
- **Single List / Multi List** → **Tipo de dado**: **Texto** (lista manual), **SQL** (lista por query) ou **Entidade/Campo**.

**Regras de data:**
- Tipo **Data** → "Salvar último valor" e "Considerar data atual?" não podem ser marcados juntos.
- Tipo **Período** → ambos podem ser marcados juntos, mas a data atual aparece só no período final.

> **Entidade/Tabela** gera campo de pesquisa nos filtros do Dashboard.

### Utilização de Parâmetros

Referência: `:ID_do_parâmetro`. O `:` avisa para buscar o conteúdo do parâmetro:

```sql
SELECT *
FROM TCSOSE
WHERE CODPARC IN :P_PARCEIRO
  AND DHCHAMADA >= '01/01/2021'
ORDER BY NUMOS
```

O `:` é traduzido para `(` + conteúdo + `)`. Com `P_PARCEIRO = 2135`:

```sql
WHERE CODPARC IN (2135)
```

Se o parâmetro for texto, o tradutor adiciona apóstrofos: `SANKHYA` → `('SANKHYA')`.

### Parâmetros Internos

Disponíveis sem declaração, todos **Número Inteiro**:

| Parâmetro | Significado |
|---|---|
| `CODUSU_LOG` | cód. usuário logado |
| `CODGRU_LOG` | cód. grupo do usuário logado |
| `CODPARC_B2B` | cód. parceiro B2B |
| `CODVEN_LOG` | cód. vendedor logado |

### Multi List com mais de mil valores

Parâmetro **Multi List** com expressão **SQL** retornando >1000 valores → obrigatório o delimitador `/*inCollection*/` em torno da condição no Editar Consulta/Expressão:

```sql
-- Antes:
SELECT CODPARC, NOMEPARC, TIPPESSOA, CODCID FROM TGFPAR WHERE CODCID in :P_CODCID

-- Depois:
SELECT CODPARC, NOMEPARC, TIPPESSOA, CODCID FROM TGFPAR WHERE /*inCollection*/
CODCID in :P_CODCID/*inCollection*/
```

> É possível definir tempo de atualização automática do gadget.

---

## Configurações

Configurações rígidas do componente: uma vez salvas, aparecem a cada execução sem precisar reinformar. Campos iguais aos de Parâmetros, com o adicional **Valor Padrão**.

---

## Variáveis

Variáveis locais do gadget, de dois tipos: **SQL** ou **Java BeanShell**.

### SQL — Assistente

Compõe a query por pesquisa e seleção:
1. Selecionar a **Tabela** → o painel mostra as tabelas ligadas a ela.
2. Selecionar os **Campos** (todos ou os desejados).
3. Criar **Filtros** por campo.

O **Parâmetro** da aba Filtros pode ser associado pelo nome a outro parâmetro já criado — basta usar o mesmo nome. Vários gadgets no mesmo Dashboard que compartilham um parâmetro (ex.: `CODUSU`) com o mesmo nome renderizam um único parâmetro para todos.

**Formas de referência na query:**

| Forma | Comportamento |
|---|---|
| `:#PARAMETRO` | recomendada — autopreenche as aspas conforme o tipo do valor |
| `:@PARAMETRO` | autopreenche SQL para valores NULOS e aspas para DATA; para string usar `':@PARAMETRO'` (aspas manuais) |
| `:PARAMETRO` | forma básica |

`:@` e `:#` melhoram a performance (substituição direta dos valores na query).

```sql
-- :#
SELECT * FROM TSICID WHERE DTALTER > :#DTALTER

-- : e :@
SELECT * FROM TSICID WHERE DTALTER > :DTALTER
SELECT * FROM TSICID WHERE NOMECID = ':@DTALTER'
```

### SQL — Avançado

Query digitada diretamente, com ou sem o assistente. Informada aqui, o **assistente é desativado** e todas as manipulações passam a ser responsabilidade do usuário (o funcionamento permanece o mesmo). Variáveis podem ser usadas como parâmetros:

```sql
SELECT CODUSU, NOMEUSU, CODEMP FROM TSIUSU WHERE CODEMP = :COD OR CODEMP = :CODEMP
```

### SQL — Resultado

Testa a query antes de usá-la. Resultado limitado a **20 linhas** (evita sobrecarga no banco).

### Java BeanShell

Trecho de código Java simplificado, digitado direto, sem assistente. Exemplos:

```java
void addColumn(String name, String type, String description){
  ui = uiElement();
  meta = ui.getChild("metadata");
  if( meta == null){
    meta = new org.jdom.Element("metadata");
    ui.addContent( meta );
  }
  f = new org.jdom.Element("field");
  f.setAttribute("name",name);
  f.setAttribute("label",description);
  f.setAttribute("type",type);
  f.setAttribute("visible","true");
  f.setAttribute("useFooter","false");
  meta.addContent(f);
}
void initMetadata(){
  addColumn("CODPROJ","I","Cód.Projeto");
  addColumn("NOMEPROJ","S","Nome Prj");
  addColumn("TAMANHO","I","Tam");
  addColumn("KANBAN","S","Kanban");
  addColumn("DHENTRADA","T","Dh.Entrada");
  addColumn("DHENTREGA","T","Dh.Entrega");
  addColumn("DIAS","I","Dias");
  addColumn("ANALISTA","S","Analista");
  addColumn("DHINIANALISE","T","Ini.Análise");
  addColumn("DHFIMANALISE","T","Fim.Análise");
  addColumn("DEV","S","Dev");
  addColumn("DHINIDEV","T","Ini.Dev");
  addColumn("DHFIMDEV","T","Fim.Dev");
  addColumn("QA","S","QA");
  addColumn("DHINIQA","T","Ini.QA");
  addColumn("DHFIMQA","T","Fim.QA");
  addColumn("VALIDADOR","S","Validação");
  addColumn("DHINIVAL","T","Ini.Val");
  addColumn("DHFIMVAL","T","Fim.Val");
}
initMetadata();
return var("_vprojects");
```

```java
import java.math.BigDecimal;
int qtdSaidas = ((BigDecimal) var("QTD_SAIDAS")).intValue();
Collection linhas = new ArrayList();
linhas.add(new Object[]{ "Qtde. Saídas", qtdSaidas, qtdSaidas });
return linhas;
```

---

## Argumentos

Compostos por **Id** e **Tipo**; são parâmetros de passagem de um nível para outro. Ex.: nível 1 exibe "Vendas por Vendedor"; duplo clique num vendedor passa o código dele (Argumento) para o nível 2, que exibe as vendas desse vendedor.

- Definidos **por nível** (não por gadget) — válidos só no nível onde foram criados.
- Botão **Nível** — edita o nome do nível e navega entre níveis.
- Botões de inserção/exclusão de níveis.
- Argumento `NUARQUIVO` pode direcionar o Dashboard ao registro selecionado no **Portal de Importação de XML**: selecionar o argumento no Construtor e clicar na linha desejada.

---

## Quadrante Expressão

Definições essenciais para gerar os dados. Determina-se o **Tipo**; o assistente de montagem de query abre pelo botão **Editar** (ver Variáveis). Ao salvar, o sistema reconhece os campos retornados e os lista na grade, permitindo redefinir **Tipos** e editar **Descrição**.

> Controle tipo **Valor** suporta HTML simplificado (tamanho, cor, fonte e imagem).

Botões do quadrante:

- **Assistente de edição de campos calculados** — pop-up "Editar Campos Calculados": cálculos personalizados com outros campos e concatenação (ex.: cidade + estado).
- **Assistente de edição de máscara** — para Linhas, Barras e Colunas; só eixos tipo **Valor**. Máscara digitada ou via pop-up "Editar Máscara".
- **Formatação condicional** — regras que, verdadeiras, aplicam-se à célula (cor de fundo, negrito/itálico). Só para **Tabela**, campos **Inteiro, Moeda, Decimal, Data e Data e Hora**. Pop-up "Editar Formatação Condicional".
- **Assistente de Formatação e Agregação** — em campos Inteiro/Decimal/Moeda, coluna **Agregador** (substitui a coluna Totalizar) que exibe o resultado no rodapé da grade. Funções: **Maior, Menor, Média, Somar, Personalizada**.

**Agregador Personalizado** — habilita o ícone `?` → pop-up "Editar Agregadores Personalizados": informar expressão com funções de agregação sobre os campos. Só aceita variáveis da Seleção de Variáveis; sem cálculos além dos permitidos pela Fórmula Personalizada. Campo **Título** nomeia o resultado. O resultado sai sempre no **Rodapé da Grade**:

```sql
SUM(VALOR_VENDA) / SUM(VALOR_CUSTO)
```

> Em campos tipo **Hora** na Tabela também cabem funções de agregação (somar, média, mínimo, máximo, personalizado) — útil para tempo gasto, horas produtivas, orçamento de horas.
