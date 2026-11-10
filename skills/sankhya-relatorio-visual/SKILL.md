---
name: sankhya-relatorio-visual
description: |
  Padrão VISUAL obrigatório da DSTech para relatório, etiqueta e comprovante JasperReports (.jrxml/iReport) no
  Sankhya (JR 4.0, Java 8): página e grid, Calibri, paleta petróleo/verde, logo do cliente no cabeçalho, cartões,
  tabela com zebra, grupo, destaque com legenda, assinaturas, rodapé com selo DSTech e "Página X de Y", P&B,
  variante XLS e etiqueta com código de barras. Use SEMPRE que for criar, redesenhar, revisar ou ajustar layout
  de .jrxml no Sankhya, mesmo sem a palavra "visual": "criar relatório", "montar impressão", "layout do relatório",
  "relatório feio", "logo no relatório", "negrito não aparece no PDF", "cabeçalho", "rodapé", "zebra",
  "agrupamento", "exportar para Excel", "etiqueta com código de barras". PREVALECE sobre fonte, cor, cabeçalho e
  estilo sugeridos pela sankhya-relatorio; dela valem só as regras não visuais (parâmetros, SQL, deploy).
---

# Padrão visual de relatório Sankhya (DSTech)

Todo relatório que sai da DSTech tem a mesma cara: logo do cliente no cabeçalho, selo DSTech no rodapé,
Calibri, petróleo e verde. Este arquivo traz as regras; as medidas e os trechos prontos estão em `references/`.

## Precedência (leia antes de tudo)

| assunto | quem manda |
|---|---|
| fonte, tamanho, cor, paleta, cabeçalho, rodapé, cartão, tabela, zebra, grupo, destaque, logo, selo, P&B, XLS | **esta skill** |
| parâmetros (`PK_<campo>`, `isForPrompting`, `nomeTabela`), datas `java.sql.Timestamp`, subreport, SQL, compilação, deploy, cadastro | `sankhya-relatorio` |

Se outra skill ou exemplo mandar usar Arial, `SansSerif`, `pdfFontName="Helvetica-Bold"`, `pdfEncoding="Cp1252"`,
cabeçalho de tabela cinza `#CCCCCC` ou "evitar retângulo" fora do contexto XLS: **ignore e siga este padrão**.

## Ambiente do servidor Sankhya

- **JasperReports 4.0.0** (o jar do EAR se chama `jasperreports-1.1.0.jar`; o MANIFEST diz 4.0.0) e **Java 8**.
  Sem `uuid`, sem `<paragraph>`, sem generics, lambda, diamond nem API de Java 9+.
- **Fontes:** módulo `custom.net.sf.jasperreports.fonts` (`skw-ireport-pdf-fonts.jar`), com Calibri regular e bold
  embutidas no PDF. `SansSerif` vira Helvetica no PDF e **perde o negrito**.
- **Código de barras:** `barbecue-1.1` (`jr:barbecue`). QR Code via `zxing` 2.3.0 (`MatrixToImageWriter`).
- **Em cliente novo:** confirme que o módulo de fontes existe no WildFly do cliente
  (`modules/custom/net/sf/jasperreports/fonts/main/`). Sem ele, a Calibri não embute; veja `references/tipografia.md`.

## Regras (as que dão errado se esquecer)

1. **Todo `<style>` declara `fontName="Calibri"`.** Elemento com `style="X"` não herda o estilo `isDefault`.
   Estilo sem `fontName` cai em SansSerif → Helvetica sem negrito.
2. **Altura do texto ≥ tamanho da fonte × 1,25 + padding vertical.** Calibri 16 pede ≥ 20 pt. Abaixo disso o Jasper
   **não imprime nada** (o campo some sem erro).
3. **Fio (`<line>`) com `lineColor` no `<pen>`** igual ao `forecolor`. Sem os dois, o fio sai na cor errada.
4. **Logo do cliente e selo DSTech embutidos em base64** numa variável `java.awt.Image`, `calculation="System"`.
   `<image onErrorType="Blank">`. Logo por empresa: variante `PDIR_MODELO` com fallback. Sem a logo do cliente em
   mãos: peça; nunca entregue em produção com o placeholder nem com logo de outro cliente. Detalhe em
   `references/logo-e-selo.md`.
5. **Texto que não cabe:**
   - célula de tabela e observação **esticam** (`isStretchWithOverflow="true"`);
   - cabeçalho, cartão, rótulo-valor e etiqueta têm altura fixa e **cortam com reticências**:
     `<property name="net.sf.jasperreports.text.truncate.suffix" value="…"/>` como **primeiro filho** do
     `<reportElement>` (antes do `printWhenExpression`; na ordem errada o XML não valida e não compila).
   Vale para título, subtítulo, tarja, valor de cartão, rótulo-valor, faixa de grupo, rodapé e etiqueta.
   Nunca deixe texto cortado sem "…" nem vazando por cima de outro elemento.
6. **Nulo:** cartão e rótulo-valor mostram `-`; célula de tabela fica vazia (ou o texto do destaque, se nulo for o
   próprio problema, como "sem valor"); total mostra `0` / `0,00`; frase composta só põe o separador (`·`, `/`, `|`)
   quando os dois lados existem; mensagem com parâmetro testa nulo. `format(null)` e `.trim()` em nulo quebram o
   relatório.
7. **`markup="styled"` escapa todo campo do banco:** `.replaceAll("&", "&amp;").replaceAll("<", "&lt;")`, testando nulo
   antes. Sem escape, um `<` no dado apaga o texto inteiro do campo.
8. **Números e datas** com `DecimalFormat`/`SimpleDateFormat` em pt-BR explícito (variáveis formatadoras `V_QTD`,
   `V_MOEDA`, `V_DATA`). Quantidade e valor à **direita**; data ao **centro**; código e identificador (NUNOTA, CODPROD)
   à esquerda, sempre com `.toPlainString()`. Exceção: variante XLS (regra 13).
9. **Comentário XML e linha em branco: proibidos** no `.jrxml` (quebram o cadastro no Sankhya). Versione com
   `<property name="dstech.padrao.visual" value="sankhya-relatorio-visual 1.0.0"/>` (a variante XLS acrescenta " xls").
10. **Redesenho de relatório existente: só o visual muda.** Consulta, parâmetros, campos e atributos do
    `<jasperReport>` ficam idênticos. Variável nova pode (logo, selo, formatadores, paginação).
11. **Código de barras e QR existentes: intocados** (mesmo `barWidth`, `barHeight`, largura e altura). Pode mudar de
    posição. Fundo branco atrás, nada de zebra, faixa ou moldura colada nas barras.
12. **P&B:** destaque nunca só por cor. Toda célula destacada leva também texto ou negrito, e há **legenda** no resumo.
13. **XLS:** se o relatório pode ser exportado para Excel, use a variante de grade (`references/xls.md`): nada sobreposto,
    colunas alinhadas, zebra e destaque por `conditionalStyle`, sem `rectangle`/`line` no detail, valores tipados.

## Peças (medidas em `references/pagina-e-grid.md`, trechos em `references/pecas.md`)

| peça | resumo |
|---|---|
| Página | A4, margem 28 pt nos 4 lados. Retrato: área útil 539. Paisagem: 786 |
| Cabeçalho (página 1) | logo do cliente (h 22) · fio vertical verde · título 16 bold petróleo + subtítulo 8 · tarja petróleo à direita com o estado/tipo · fio verde 2 pt |
| Cabeçalho (página 2+) | `pageHeader` compacto com `PAGE_NUMBER > 1`: logo h 16, título 11 bold "… (continuação)", fio verde 1 pt |
| Cartões | `rectangle radius="4"` sem borda, 4 por linha, gap 8. O número que identifica o documento vai no cartão **petróleo** com texto branco |
| Rótulo + valor | rótulo 7 bold MAIÚSCULO cinza acima, valor 9 abaixo, 3 colunas |
| Observação | `frame` `#EEF2F5` com fio verde 3 pt à esquerda, estica e some quando vazia |
| Tabela | cabeçalho petróleo 7 bold branco (h 20) · linha h 16 · zebra `#F1F4F7` · fio inferior 0,5 `#D5DBE1` |
| Total | `frame` `#EEF2F5` com fio superior 1,5 petróleo e os textos dentro (sem emenda entre rótulo e valor) |
| Grupo | faixa `#EEF2F5` com fio verde 3 pt · contagem à direita · zebra reinicia no grupo · "Total do grupo" no rodapé do grupo |
| Destaque | fundo `#F5B85C` só na célula que importa, com texto ("sem valor", "VENCIDO") + legenda no resumo. Sem destaque, sem legenda |
| Escrita à mão | caixa `radius="3"` branca, borda `#9AA5B1`, guia `/ /` cinza, checkbox desenhado 14×14 |
| Assinaturas | linha 0,75 petróleo + rótulo 7 bold embaixo. Só quando o papel precisa de aceite (conferência, entrega, recebimento) |
| Rodapé | fio 0,5 · selo DSTech h 12 · identificação · "Emitido em dd/MM/yyyy HH:mm" ao centro · "Página X de Y" rente à margem direita |
| Etiqueta | moldura `radius="8"` petróleo 1,25 · título + logo pequena · barras e código legível alinhados à esquerda · faixa clara com descrição (2 linhas, "…") · emissão 7 pt fora da moldura |

## Templates (`templates/`): copie o mais próximo e adapte

| template | quando usar | o que demonstra |
|---|---|---|
| `retrato-agrupado.jrxml` | documento de 1 registro com itens (nota, pedido, ordem, romaneio). **Sem grupo:** apague o `<group>` e troque `$V{GRUPO_COUNT}` por `$V{REPORT_COUNT}` na zebra | cabeçalho, cartões, rótulo-valor, observação, `pageHeader` de continuação, grupo com total, zebra por grupo, destaque + legenda, assinaturas |
| `paisagem-listagem-xls.jrxml` | listagem por período/filtro, que o usuário exporta para Excel | variante XLS: grade alinhada, cartões em `frame`, `conditionalStyle`, valores tipados |
| `etiqueta-codigo.jrxml` | etiqueta / identificação com código de barras; uma etiqueta por linha da consulta, até 3 por folha A4 | moldura, Code128 sem `drawText`, código legível alinhado às barras, descrição com corte |

Os 3 já trazem a logo placeholder ("LOGO DO CLIENTE") e o selo DSTech embutidos e compilam no JR 4.0.0 como estão.
As consultas usam só tabelas nativas.

## Fluxo

1. Decidir orientação, se terá grupo e se vai para XLS (`references/pagina-e-grid.md` §Decisões).
2. Copiar o template mais próximo. Trocar a consulta, campos, título, tarja e colunas, mantendo estilos e medidas.
   **Parâmetro da chave:** relatório impresso a partir de uma tela recebe automaticamente a chave do registro em
   `PK_` + nome do campo da **chave primária da tabela da tela** (`PK_NUNOTA` em TGFCAB, `PK_CODPROD` em TGFPRO,
   `PK_NUFIN` em TGFFIN). Confira a PK da tabela no banco (constraint `PK_<TABELA>`) antes de nomear; chave composta
   = um parâmetro por campo (`PK_NUNOTA` + `PK_SEQUENCIA` em TGFITE). Com outro nome o parâmetro chega nulo e o
   Sankhya responde "Nenhuma página a apresentar. Verifique o filtro e tente novamente."
3. Trocar a logo placeholder pela do cliente (`references/logo-e-selo.md`).
4. Conferir a checklist (`references/checklist.md`): fontes, alturas, nulos, escape, P&B, XLS.
5. Compilar no iReport e **imprimir uma vez no ERP do cliente**, em PDF (e em XLS se for o caso).

## Referências

| arquivo | quando ler |
|---|---|
| `references/pagina-e-grid.md` | medidas da página, colunas, alturas, espaçamentos, decisões de layout |
| `references/pecas.md` | trecho XML pronto de cada peça |
| `references/marca-dstech.md` | paleta completa, cores semânticas, P&B medido, uso do verde e do selo |
| `references/tipografia.md` | escala de tamanhos, pesos, fonte no servidor |
| `references/texto-e-dados.md` | corte, nulo, número, data, CNPJ/CPF, escape no styled |
| `references/logo-e-selo.md` | como trocar a logo, variante `PDIR_MODELO`, selo DSTech |
| `references/xls.md` | variante segura para Excel |
| `references/checklist.md` | conferência antes de entregar |
