# Diagnóstico e Performance

Use para corrigir erros, lentidão, incompatibilidade, falhas de exportação e problemas de runtime.

## Verificações iniciais (checar primeiro)

- `.jasper` foi recompilado após alterar `.jrxml`?
- Versão do JasperReports no runtime é compatível com o `.jasper` compilado?
- Subreports estão compilados (todos os `.jasper` filhos)?
- Caminhos de subreport/imagem são portáveis (não contêm `C:\Users\...`)?
- `<field>` existem na query com os aliases corretos?
- Tipos Java dos campos estão corretos?
- Banda tem altura suficiente para o conteúdo?
- Fontes existem no servidor?

## Compatibilidade 4.0.1

Problemas frequentes:
- `.jrxml` salvo em versão nova do iReport não abre no 4.0.1
- `.jasper` compilado em versão diferente falha no runtime
- Atributo `uuid="..."` nos elementos causa erro de parse
- Componentes modernos não existem no schema 4.0.1

Estratégia segura:
1. Versionar `.jrxml` no controle de fonte
2. Fazer backup antes de abrir em ferramenta nova
3. Compilar sempre no ambiente com a versão correta do runtime
4. Recompilar subreports junto com o relatório principal
5. Testar PDF e XLS após qualquer compilação

## Classpath e ambiente

Itens que precisam estar disponíveis no servidor:
- Driver JDBC Oracle
- Subreports compilados (`.jasper`)
- Fontes (se não forem fontes do sistema)
- Classes de scriptlets ou datasources customizados

No iReport local: revisar **Options > Classpath** para adicionar JARs de driver e dependências.

## Problemas de layout

**Detail quebrado / conteúdo cortado:**
- Aumentar altura da banda
- Revisar `isStretchWithOverflow` nos campos dinâmicos
- Remover sobreposição de elementos
- Dividir em grupos ou blocos

**Páginas extras em branco:**
- Revisar quebras de página explícitas (`pageBreak`)
- Revisar bandas com altura excessiva
- `splitType="Prevent"` pode criar grande espaço em branco — usar com cuidado
- Verificar elementos fora da área útil (`x + width > columnWidth`)
- Conferir margens e `columnWidth`

**XLS com células quebradas:**
- Alinhar todos os elementos: `x`, `y`, `width`, `height` exatos
- Remover elementos sobrepostos
- Usar mesma altura para elementos na mesma linha
- Reduzir decoração (retângulos, frames)
- Evitar gaps mínimos entre colunas

**PDF com acento quebrado:**
- Revisar `fontName` — usar fonte disponível no servidor
- Definir `pdfEncoding="Cp1252"` (Latin-1)
- Considerar `isPdfEmbedded="true"`
- Testar no servidor, não só no iReport local

## Performance

**Query:**
- Evitar `SELECT *`
- Filtrar no banco, não no layout
- Ordenar no banco para grupos
- Revisar índices nas colunas de filtro e join
- Reduzir subqueries caras

**Subreports:**
- Subreport executa uma query por linha do pai — principal gargalo em grandes volumes
- Passar filtros seletivos (não buscar tudo e filtrar no layout)
- Reutilizar `$P{REPORT_CONNECTION}`
- Avaliar se `group` ou `table` resolve sem subreport

**Layout:**
- Reduzir imagens grandes antes de usar
- Usar estilos em vez de formatar cada elemento individualmente
- Evitar expressões complexas repetidas no `detail` — mover para variável
- Remover elementos invisíveis ou com `printWhenExpression` sempre falso

**Relatórios grandes:**
- Considerar virtualizer (configuração no runtime)
- Dividir relatório quando necessário
- Reduzir volume de dados com filtros obrigatórios

## Checklist final de diagnóstico

- O erro é de compilação, fill (preenchimento) ou exportação?
- O `.jrxml` está compatível com 4.0.1 (sem `uuid`, sem APIs modernas)?
- O runtime usa as mesmas bibliotecas da compilação?
- Query, `<field>` e tipos Java batem?
- Subreports, imagens e fontes estão acessíveis no servidor?
- O layout respeita as regras de PDF / XLS?
- Há gargalo claro em query, subreport, imagem ou expressão?
