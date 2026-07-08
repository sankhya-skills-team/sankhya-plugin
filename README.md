# sankhya-relatorio

Skill para Claude Code especializada em criação de **relatórios imprimíveis para o ERP Sankhya OM** usando **JasperReports 4.0 via iReport**.

---

## O que esta skill faz

Transforma o Claude em especialista em relatórios Sankhya, capaz de:

- Gerar arquivos `.jrxml` completos e prontos para compilar no iReport
- Estruturar **relatório principal + sub-relatórios** com passagem de parâmetros e retorno de variáveis
- Configurar **parâmetros padrão Sankhya** (`PK_ID`, `SUBREPORT_DIR`, `PDIR_MODELO`, `REPORT_CONNECTION`)
- Criar **parâmetros de filtro** com `isForPrompting="true"`, `<parameterDescription>` e `nomeTabela` para lookup automático
- Declarar parâmetros de data como `java.sql.Timestamp` (requisito Sankhya)
- Escrever **expressões Java** null-safe: formatação de data, divisão segura, condicionais, paginação
- Aplicar **estilos condicionais** por status ou valor
- Orientar o **deploy** dos `.jasper` no servidor e cadastro no Sankhya

---

## Quando acionar

Acionar esta skill quando o usuário mencionar:

> relatório · impressão · JasperReports · iReport · jrxml · jasper · sub-relatório · subreport · layout de impressão · compilar jrxml · parâmetro relatório · deploy jasper · relatório sankhya · impressão sankhya

---

## Estrutura da Skill

```
sankhya-relatorio/
├── SKILL.md                          Instruções principais da skill (carregadas pelo Claude Code)
├── README.md                         Este arquivo
│
├── assets/
│   └── relatorio/                    Exemplos reais de relatório Sankhya
│       ├── orcamento_capa.jrxml      Relatório principal: capa empresa/cliente, agrupamento por OS,
│       │                             2 sub-relatórios, totalizadores, logo dinâmica, paginação
│       ├── Itens.jrxml               Sub-relatório de serviços: query CTE, retorna variáveis ao pai
│       └── Itens_mat.jrxml           Sub-relatório de materiais: UNION ALL, mesmos retornos
│
└── references/
    └── relatorio-jasper.md           Documentação técnica completa: estrutura, bandas, parâmetros,
                                      sub-relatórios, variáveis, expressões, estilos, deploy
```

---

## Conceitos Fundamentais

| Conceito | Descrição |
|---|---|
| `.jrxml` | Arquivo fonte XML — editado no iReport |
| `.jasper` | Arquivo compilado usado em runtime (Build > Compile Report) |
| `language="java"` | Obrigatório declarar no `<jasperReport>`; permite expressões Java completas |
| Sub-relatório | Relatório filho embutido na banda `detail` do pai — recebe parâmetros, devolve variáveis |

---

## Parâmetros Padrão Sankhya

| Parâmetro | Tipo | Preenchido por |
|---|---|---|
| `PK_ID` | `java.math.BigDecimal` | Sankhya — chave do registro selecionado |
| `SUBREPORT_DIR` | `java.lang.String` | Configuração do relatório — pasta dos `.jasper` |
| `PDIR_MODELO` | `java.lang.String` | Configuração do relatório — pasta do cliente (logo) |
| `REPORT_CONNECTION` | (built-in) | Sankhya — conexão JDBC; repassar a todos os sub-relatórios |

Parâmetros preenchidos pelo sistema: `isForPrompting="false"`.  
Parâmetros de data/período: sempre `java.sql.Timestamp` (nunca `java.util.Date`).

---

## Regras Críticas

1. **`language="java"`** — declarar no `<jasperReport>` sem exceção; habilita expressões Java completas.
2. **Sub-relatórios** — margens `0,0,0,0`; `$P{REPORT_CONNECTION}` como `connectionExpression`.
3. **`<returnValue>`** — declarar para cada variável que o pai precisa agregar.
4. **Parâmetros de filtro** — `isForPrompting="true"` + `<parameterDescription>` + `nomeTabela` quando referenciam tabela Sankhya.
5. **Datas** — `java.sql.Timestamp`; nunca `java.util.Date`.
6. **`SUBREPORT_DIR`** — caminho deve terminar com separador de diretório (`\\`).
7. **Expressões** — sempre null-safe para campos opcionais (`$F{X} == null ? "" : $F{X}`).
8. **Compilar** — entregar `.jasper` compilado e testado no iReport, não apenas o `.jrxml`.

### Regras específicas 4.0.1 (aprendidas em campo)

9. **Ordem dos elementos no `<jasperReport>`** — o XSD é rígido: `style → parameter → queryString → field → variable → background → title → pageHeader → columnHeader → detail → columnFooter → pageFooter → lastPageFooter → summary`. Qualquer inversão causa `SAXParseException`.
10. **`fontSize` só em `<style>`** — dentro de `<font>` filho de `<textElement>`, usar `size=` (não `fontSize=`). Erro: "atributo 'fontSize' não pode aparecer no elemento 'font'".
11. **`markup=` em `<textElement>`** — nunca em `<textField>`. Erro: "atributo 'markup' não pode aparecer no elemento 'textField'".
12. **Sem comentários XML** — o iReport rejeita `--` dentro de `<!-- -->` (XML inválido). Solução mais segura: não usar comentários no `.jrxml`.
13. **ISO-8859-1: sem em-dash/en-dash** — `—` (U+2014) e `–` (U+2013) não existem em ISO-8859-1; substituir por `-` antes de salvar ou o `iconv` aborta.

---

## Fluxo de Raciocínio

Antes de gerar qualquer `.jrxml`, o Claude levanta:

```
Necessidade de impressão
→ Tabelas, campos e joins Oracle
→ Parâmetro de entrada (chave primária — PK_ID)
→ Precisa de sub-relatório? (seções distintas com queries separadas)
→ Variáveis totalizadoras e agrupamentos
→ Orientação e dimensões da página
→ Logo/imagem dinâmica? (PDIR_MODELO)
→ Campos com formatação condicional por valor? (style + conditionalStyle)
→ Estrutura de bandas (title, columnHeader, detail, groupHeader/Footer, pageFooter, summary)
→ Montar .jrxml principal + sub-relatórios se necessário
→ Checklist de entrega
```

---

## Checklist de Entrega

- [ ] `language="java"` no `<jasperReport>`
- [ ] Ordem dos elementos: `style → parameter → queryString → field → variable → bands`
- [ ] Ordem das bandas: `background → title → pageHeader → columnHeader → detail → columnFooter → pageFooter → summary`
- [ ] `<font>` dentro de `<textElement>` usa `size=` (não `fontSize=`)
- [ ] `markup=` declarado em `<textElement>`, não em `<textField>`
- [ ] Sem comentários XML no `.jrxml` (evita erro de `--` e problemas de encoding)
- [ ] Sem em-dash `—` ou en-dash `–` no conteúdo (não existem em ISO-8859-1)
- [ ] Parâmetros do sistema com `isForPrompting="false"`
- [ ] Parâmetros de filtro com `isForPrompting="true"` + `<parameterDescription>`
- [ ] Parâmetros que referenciam tabela Sankhya com `<property name="nomeTabela" value="NOME_TABELA"/>`
- [ ] Parâmetros de data/período como `java.sql.Timestamp`
- [ ] Sub-relatórios com margens `0,0,0,0`
- [ ] `$P{REPORT_CONNECTION}` em todos os sub-relatórios
- [ ] `<returnValue>` para cada variável que o pai agrega
- [ ] Expressões null-safe para campos opcionais
- [ ] `.jasper` compilado e testado no iReport antes de entregar
- [ ] `SUBREPORT_DIR` com separador de diretório ao final (`\\`)

---

## Licença

Uso interno — DSTech Soluções.
