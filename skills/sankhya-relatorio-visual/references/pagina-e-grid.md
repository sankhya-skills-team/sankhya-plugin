# Página, grid e medidas

Unidade: ponto (pt). 1 cm ≈ 28,35 pt. Coordenadas relativas à área útil (depois da margem).

## Decisões antes de desenhar

| pergunta | resposta → escolha |
|---|---|
| Documento de **um registro** (nota, pedido, ordem, romaneio, comprovante)? | **retrato** com cabeçalho + cartões + tabela de itens |
| **Listagem** por período/filtro com muitas colunas (≥ 8) ou que vai para Excel? | **paisagem**, variante XLS (`xls.md`) |
| Itens se dividem por uma chave (grupo de produto, natureza, rota, parceiro)? | `<group>` com faixa de grupo e total do grupo |
| Alguém vai **escrever à mão** na folha (conferência, inventário)? | linha da tabela h 28 e caixas de escrita |
| Precisa ser lido por **leitor de código**? | código de barras com fundo branco e zona de silêncio |
| Sai em impressora **P&B**? | sempre presuma que sim: destaque com texto/negrito + legenda |

## Página

| | retrato | paisagem | etiqueta (3 por A4) |
|---|---|---|---|
| `pageWidth` × `pageHeight` | 595 × 842 | 842 × 595 (`orientation="Landscape"`) | 595 × 842 |
| margens (4 lados) | 28 | 28 | 28 |
| `columnWidth` (área útil) | **539** | **786** | 539 |

Margem é **sempre 28**. Não use margem diferente por relatório.

## Espaçamento

- Use as medidas deste arquivo; não invente espaçamento novo. Deslocamentos internos (texto 5 pt abaixo do topo do
  cartão, tarja 3 pt abaixo do topo) são parte da peça.
- **8 pt** entre cartões lado a lado e entre colunas de rótulo-valor.
- **8 pt** entre blocos do cabeçalho (fio verde → cartões → rótulo-valor → observação).
- **6 pt** antes do total geral no `summary`.

## Cabeçalho da página 1 (`title`)

| elemento | retrato (x, y, w, h) | paisagem |
|---|---|---|
| logo do cliente | 0, 4, 140, 22 | 0, 4, 106, 22 |
| fio vertical verde 1,5 | 150, 2, 1, 28 | borda esquerda do bloco de título (`frame`) em x 106 |
| título 16 bold petróleo | 160, 0, 280, 22 | 106, 0, 426, 22 (padding esquerdo 10) |
| subtítulo 8 `#6B7785` | 160, 22, 379, 12 | 106, 22, 426, 12 |
| tarja petróleo 9 bold branca | 449, 3, 90, 16 | 652, 3, 134, 16 |
| fio verde 2 pt | 0, 38, 539, 1 | borda inferior do `frame` 0, 0, 786, 40 |
| cartões | y 46, h 44 | y 48, h 44 |
| rótulo-valor | rótulo y 98 h 10, valor y 108 h 14 | (opcional) |
| rótulo-valor, linhas seguintes | + 26 por linha (rótulo y 124, valor y 134; …) | |
| observação | 8 abaixo do último valor (y 130 com uma linha de rótulo-valor), h 22, estica | (opcional) |

Título nunca em `y` negativo.

**Cartões no retrato (4 por linha, gap 8):** x 0 / 136 / 272 / 408, larguras 128 / 128 / 128 / 131.
Rótulo em (x+10, y+5, w−15, 10); valor em (x+10, y+15, w−15, 26).
Valor 18 bold, ou 15 quando o texto é longo (data, moeda).

**Rótulo-valor (3 colunas, gap 8):** larguras 260 / 130 / 133. Coloque o campo mais longo (nome) na 1ª coluna.

## Cabeçalho da página 2+ (`pageHeader`)

`<printWhenExpression>` na band: `Boolean.valueOf($V{PAGE_NUMBER}.intValue() > 1)`. Altura 32 (retrato) / 28 (paisagem).
Retrato: logo (0, 3, 100, 16) · fio vertical · título 11 bold "Nome · identificador (continuação)" · linha 7 com o
parceiro · fio verde 1 pt. Paisagem/XLS: logo (0, 2, 106, 16) e título no `frame` com borda verde. Título com "…".
Nunca repita os cartões.

## Tabela

| peça | medida |
|---|---|
| cabeçalho de coluna (`columnHeader`) | h 20, fonte 7 bold branca, padding 1/3 |
| linha de 1 nível | h 16, fonte 8, padding 2/3 |
| linha com 2ª linha de texto (`styled`) | h 24 |
| linha para escrita à mão | h 28 |
| zebra | linhas pares; com grupo use `$V{<GRUPO>_COUNT}` (reinicia por grupo) |
| fio inferior | 0,5 `#D5DBE1`, `positionType="FixRelativeToBottom"` |
| band do detail | `splitType="Prevent"` (linha não quebra entre páginas) |

**Larguras:** a soma das colunas é exatamente a área útil (539 / 786). Ordem: identificação (seq., código) → descrição
→ atributos curtos (un., tipo) → números → situação. Comece pelas larguras fixas abaixo e dê **o que sobrar** à
descrição (ou ao nome do parceiro, na listagem):

| coluna | largura |
|---|---|
| seq. | 28 |
| código / nº | 46–56 |
| referência / código de barras | 60–70 |
| un. | 30 |
| tipo / situação curta | 50 |
| situação com palavra ("VENCIDO") | 70–80 |
| data | 56 |
| quantidade | 50 |
| valor unitário | 54–60 |
| valor total | 58–70 |
| escrita à mão (qtd., lote) | 80–110 |

Exemplo do retrato-agrupado: 28 · 46 · 213 · 60 · 30 · 50 · 54 · 58 = 539.

**Alinhamento:** texto, código e identificador à esquerda; quantidade e valor à direita; data, unidade, seq. e
situação ao centro. O cabeçalho da coluna segue o alinhamento do dado.

**Total geral:** o rótulo ocupa da esquerda até o início das colunas numéricas que ele soma; cada valor fica na
coluna que soma (mesmo x e largura). Total de uma coluna só: o valor pode ocupar as duas últimas colunas.

## Grupo

- `groupHeader` h 24: faixa (0, 4, 539, 18) `#EEF2F5` + fio verde (0, 4, 3, 18). Texto 9 bold petróleo com padding
  esquerdo 10, "código · descrição", com reticências. Contagem à direita (`evaluationTime="Group"`).
- `groupFooter` h 20: `frame` `#EEF2F5` com fio superior 1,5 petróleo; dentro, "Total do grupo" e o valor na coluna do
  valor (estilo `Total`, sem fundo próprio).
- No `<group>`: `isReprintHeaderOnEachPage="true"` e `minHeightToStartNewPage="60"`, para não deixar cabeçalho de grupo
  órfão no pé da página.

## Resumo (`summary`)

Total geral (`frame` h 24 como o total do grupo, rótulo 11 e valor 13) · legenda dos destaques, 8 abaixo · assinaturas
(linhas em y 80). Paisagem/XLS: uma linha de total por soma (h 18, células alinhadas às colunas) e legenda como
célula colorida de 50 + texto.

## Rodapé (`pageFooter`, h 24)

| elemento | retrato (x, w) | paisagem |
|---|---|---|
| fio 0,5 `#D5DBE1` | y 4, largura total | borda superior do `frame` |
| selo DSTech h 12 | 0, 50 | 0, 50 |
| identificação (8, `#6B7785`) | 58, 132 | 50, 532 (junto com "Emitido em") |
| "Emitido em dd/MM/yyyy HH:mm" | 195, 150, centralizado | (junto da identificação) |
| "Página X de Y" (8 bold petróleo) | 389, 150, alinhado à direita | 582, 204 |

"Página X de Y" num campo só com `evaluationTime="Auto"` (ver `pecas.md`): termina rente à margem.
Caixas do rodapé **não se sobrepõem**.

## Etiqueta (band de 262 = 3 por A4)

Moldura (0, 0, 539, 196) `radius="8"`, petróleo 1,25 · título 11 bold (16, 8) · logo pequena à direita (h 14) ·
fio verde 1 · código de barras (16, 34, 507, 72) · código legível 28 bold (16, 108, 507, 38) com padding esquerdo
= 10 × `barWidth` (alinha com a 1ª barra) · faixa `#EEF2F5` (10, 150, 519, 38) com a descrição 12 bold centralizada,
2 linhas, "…" · fora da moldura: selo (h 9) e "Emitido em … · página N" 7 pt.
