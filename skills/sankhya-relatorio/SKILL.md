---
name: sankhya-relatorio
version: 1.0.0
github-repo: sankhya-relatorio
description: |
  Usar quando o usuário mencionar relatório, impressão, JasperReports, iReport, jrxml, jasper,
  sub-relatório, subreport, layout de impressão, ou qualquer necessidade de gerar documentos
  imprimíveis no contexto Sankhya ERP.
  Também acionar para: "criar relatório", "montar impressão", "layout jasper",
  "compilar jrxml", "sub-relatório jasper", "parâmetro relatório", "deploy jasper",
  "relatório sankhya", "impressão sankhya".
---

# Relatórios Sankhya — JasperReports / iReport 4.0.1

Especialidade: relatórios imprimíveis para Sankhya ERP usando **iReport** com **JasperReports 4.0.1**.

**Idioma:** Português do Brasil.
**Regra:** Levantar todos os dados necessários antes de gerar qualquer `.jrxml`.

---

## Índice de Referências

Carregar apenas o(s) arquivo(s) necessário(s) para o contexto — não carregar todos por padrão.

| Arquivo | Usar quando |
|---|---|
| `references/jrxml-core.md` | Criar/revisar estrutura do `.jrxml`, compatibilidade 4.0.1, bandas, campos, parâmetros, variáveis, expressões |
| `references/layout-exportacao.md` | Layout PDF/XLS, fontes, estilos condicionais, imagens, paginação, elementos gráficos |
| `references/dados-sql-sankhya.md` | Query Oracle, grupos, subdatasets, parâmetros de data, performance de dados |
| `references/componentes-avancados.md` | Subreports, table component, list, crosstab, charts, frame |
| `references/diagnostico-performance.md` | Erros, compatibilidade de versão, troubleshooting, performance |

---

## Fluxo de Raciocínio (Obrigatório)

```
Necessidade de impressão
→ Dados necessários (tabelas, campos, joins Oracle)
→ Parâmetro de entrada (chave primária — PK_ID ou filtros)
→ Precisa de subreport? (seções distintas com queries separadas)
→ Variáveis totalizadoras e agrupamentos (ORDER BY obrigatório por grupo)
→ Orientação e dimensões da página
→ Alvo principal: PDF ou XLS? (define estratégia de layout)
→ Logo/imagem dinâmica? (PDIR_MODELO)
→ Campos com formatação condicional? (style + conditionalStyle)
→ Componente avançado necessário? (table/list/crosstab/chart)
→ Estrutura de bandas (title, columnHeader, detail, groupHeader/Footer, pageFooter, summary)
→ Localização dos arquivos no projeto (pergunta obrigatória — ver seção abaixo)
→ Montar .jrxml principal + subreports se necessário
→ Checklist de entrega
```

---

## Localização dos Arquivos (Pergunta Obrigatória)

Antes de gerar qualquer `.jrxml`, perguntar:

> **Qual é o modelo do projeto Java?**
>
> 1. **Modelo novo** — pasta dentro da demanda: `<nomedemanda>/Relatorios/`
> 2. **Modelo antigo** — pasta na raiz: `Relatorios/<nomedemanda>/`
> 3. **Outro caminho** — informar o caminho completo

---

## Parâmetros Padrão Sankhya

| Parâmetro | Tipo | Preenchido por |
|---|---|---|
| `PK_ID` | `java.math.BigDecimal` | Sankhya — chave do registro selecionado |
| `SUBREPORT_DIR` | `java.lang.String` | Configuração no Sankhya — pasta dos `.jasper` |
| `PDIR_MODELO` | `java.lang.String` | Configuração no Sankhya — pasta do cliente (logo) |
| `REPORT_CONNECTION` | (built-in) | Sankhya — conexão JDBC; repassar a todos os subreports |

Todos com `isForPrompting="false"`.

---

## Regras Críticas Sankhya

### Parâmetros de filtro (preenchidos pelo usuário)

- `isForPrompting="true"` — Sankhya exibe o campo na tela de parâmetros
- `<parameterDescription>` — label exibido ao usuário (obrigatório)
- `<property name="nomeTabela">` — quando o parâmetro é chave de tabela cadastro; Sankhya usa para lookup/autocomplete

```xml
<parameter name="P_CODEMP" class="java.math.BigDecimal" isForPrompting="true">
    <property name="nomeTabela" value="TSIEMP"/>
    <parameterDescription><![CDATA[Empresa]]></parameterDescription>
</parameter>
```

**Tabelas comuns:**

| Entidade | `value` |
|---|---|
| Empresa | `TSIEMP` |
| Parceiro | `TGFPAR` |
| Produto | `TGFPRO` |
| Vendedor | `TGFVEN` |
| Local / Estoque | `TGFLOC` |
| Tipo de Negociação | `TGFTPN` |
| Grupo de Natureza | `TGFGRU` |

### Parâmetros de data

**Sempre `java.sql.Timestamp`** — o Sankhya não preenche `java.util.Date` corretamente.

```xml
<parameter name="P_DTINI" class="java.sql.Timestamp" isForPrompting="true">
    <parameterDescription><![CDATA[Data Início]]></parameterDescription>
</parameter>
```

### Prefixos de nomenclatura

- Parâmetros de filtro: `P_` (ex: `P_CODEMP`, `P_DTINI`)
- Variáveis calculadas: `V_` (ex: `V_TOTAL`, `V_SUBTOTAL`)

---

## Deploy no Sankhya

1. Compilar `.jrxml` → `.jasper` no iReport (**Build > Compile Report**).
2. Copiar os `.jasper` para a pasta configurada em `SUBREPORT_DIR` no servidor.
3. Configurar o relatório no Sankhya (**Configurações > Relatórios**) apontando para o `.jasper` principal.
4. `PK_ID` recebe a chave do registro automaticamente.
5. `PDIR_MODELO` e `SUBREPORT_DIR` são configurados na tela de cadastro do relatório.

---

## Checklist de Entrega

- [ ] `language="java"` no `<jasperReport>`
- [ ] Cabeçalho XML com `xmlns` e `xsi:schemaLocation` (ver `jrxml-core.md`)
- [ ] Nenhum `uuid="..."` nos elementos (incompatível com 4.0.1)
- [ ] Parâmetros do sistema com `isForPrompting="false"`
- [ ] Parâmetros de filtro com `isForPrompting="true"` e `<parameterDescription>`
- [ ] Parâmetros de tabela Sankhya com `<property name="nomeTabela"/>`
- [ ] Parâmetros de data declarados como `java.sql.Timestamp`
- [ ] Grupos com `ORDER BY` correspondente na query
- [ ] Subreports: margens `0,0,0,0`, `$P{REPORT_CONNECTION}`, `<returnValue>` declarados
- [ ] `SUBREPORT_DIR` com separador de diretório ao final (`\\`)
- [ ] Expressões null-safe para campos opcionais (`isBlankWhenNull` ou ternário)
- [ ] `.jasper` compilado e testado no iReport antes de entregar

---

## Exemplos de Referência

Em `assets/relatorio/`:

**Sankhya (orçamento real com subreports):**

| Arquivo | O que demonstra |
|---|---|
| `orcamento_capa.jrxml` | Relatório principal: capa empresa/cliente, agrupamento por OS, 2 subreports, totalizadores, logo dinâmica, rodapé com paginação |
| `Itens.jrxml` | Subreport de serviços: query CTE, devolve `VLRTOT_1`/`VLRTOTLIQ`/`VLRTOTDESC` ao pai |
| `Itens_mat.jrxml` | Subreport de materiais: UNION ALL, mesmos retornos de variáveis |

**Estrutura básica:**

| Arquivo | O que demonstra |
|---|---|
| `Exemplo_simples_com_textos.jrxml` | Estrutura mínima, `staticText`, `textField`, `isStretchWithOverflow`, markup HTML |
| `Exemplo_simples_com_imagem.jrxml` | Logo via `PDIR_MODELO`, parâmetros com `nomeTabela`, `P_` prefixo, `V_` prefixo, `pageFooter` |

**Agrupamentos:**

| Arquivo | O que demonstra |
|---|---|
| `Exemplo_com_agrupamento.jrxml` | `group`, `groupHeader/Footer`, subtotal, `whenNoDataType`, subdataset, `isBlankWhenNull`, `printWhenExpression` |

**Componentes avançados:**

| Arquivo | O que demonstra |
|---|---|
| `Exemplo_somente_tabela.jrxml` | Table component, subdataset, `datasetRun`, estilos `table_TH/CH/TD` |
| `Exemplo_com_list.jrxml` | List component, repetição de blocos, `datasetRun` |
| `Exemplo_somente_crosstab.jrxml` | Crosstab com grupos linha/coluna/medida |
| `Exemplo_simples_com_grafico.jrxml` | Chart com subdataset |
| `Exemplo_com_crosstab_e_subreport.jrxml` | Composição avançada modular |
| `Subreport_do_exemplo.jrxml` | Relatório filho isolado |
| `Exemplo_Imagem_e_codigo_barras.jrxml` | Código de barras — componente especial |
