# Gráficos

Configurações comuns a quase todos os gráficos, definidas na edição: **Título**, **Tamanho do texto** e **Legenda** (se exibida, define-se **Posição** e **Direção**).

**Recursos comuns:**
- **Zoom** (na visualização) — clicar e arrastar sobre a área; botão **Resetar Zoom** restaura a visão inicial.
- **Agrupar séries** (aba Série em modo grade) — `Ctrl` + marcar séries + botão "Agrupar séries".
- **Rotação de Títulos/Resultados** (cartesianos) — ângulo de `-90º` a `90º`; a palavra "Exemplo" ao lado serve de teste.
- **Aba BIA** — ver B.I.A - Business Intelligence Analyst.

---

## Gráficos > Linha

### Aba Eixos

Descrição do eixo **Horizontal** e **Vertical**, cada um do tipo:
- **Categoria** — por grupo (ex.: Receitas e Despesas).
- **Valor** — contínuo/quantitativo (ex.: Volume de Receitas e Volume de Despesas).

- **Visão Parcial** — exibe Primeiros Registros ou Últimos Registros na visualização (padrão: Primeiros).
- **Redimensionamento Vertical** — fixa mínimo/máximo do eixo vertical; automático ou fixo (fixo → valor decimal de 4 casas).
- **Omitir valores nulos** — oculta campos sem valor.

> As configurações do eixo horizontal influenciam o vertical. Ex.: com Visão Parcial desativada, ignora mínimo/máximo do quadrante vertical.

### Aba Séries

Série é o conjunto de dados que compõe o gráfico; cada série é uma linha. No gráfico de Linha a série é só do tipo **Linha**. Define-se Descrição, **Campo na Horizontal** e **Campo na Vertical** (das variáveis disponíveis).

- **Destacar pontos** — enfatiza pontos de mudança; marca automaticamente **Mostrar placa de valor** (informação por ponto ao passar o mouse).
- **Cor** — cor da série (grade ou formulário). Sem **Usar cor padrão** marcada, habilita a paleta; com marcada, usa cores padrão do sistema.

---

## Gráficos > Barras

### Aba Eixos

Igual à Linha, exceto o campo **Tipo**, que é fixo. Como só o eixo horizontal apresenta valores quantitativos: horizontal fixo em **Valor**, vertical (agrupamentos) fixo em **Categoria**.

- **Visão Parcial** — Primeiros/Últimos Registros (padrão: Primeiros).
- **Omitir valores nulos**.

### Aba Séries

Permite associar série de **Barras** com **Linhas**; "n" séries por gráfico. Ex.: vendas por parceiro e compras (Barras) + uma Linha somando o volume de negociações.

- **Mostrar placa de valor** — informação por barra ao passar o mouse.

> Placa sobreposta a outra só aparece com o parâmetro `SOBREVALORGRAF` (Permite sobreposição de placas de valor) ligado; senão o sistema oculta a placa que sobreporia outra.

---

## Gráficos > Colunas

Campo **Colunas** — quantidade de colunas visíveis na abertura do dashboard. Padrão `6`, não pode ser reduzido, só aumentado.

### Aba Eixos

Inverso das Barras: horizontal (agrupamentos) fixo em **Categoria**, vertical (quantitativo) fixo em **Valor**.

- **Visão Parcial** — Primeiros/Últimos (padrão: Primeiros). O horizontal influencia o vertical (com Visão Parcial desativada, ignora mínimo/máximo do vertical).
- **Redimensionamento Vertical** — automático ou fixo (4 casas). Não é aplicado se houver ≥2 séries e uma delas com **Escala Secundária** marcada.
- **Omitir valores nulos**.
- **Rotacionar Resultados** — redefine intervalos do eixo Y via barra vertical no canto superior direito.

### Aba Série

Associa série de **Linhas** com **Colunas**; "n" séries.

> A ordenação das séries afeta a apresentação: numa linha de totalização, esta é exibida atrás das barras.

- **Mostrar placa de valor** — informação por coluna ao passar o mouse.
- Descrição pode buscar informação da SQL para o balão, prefixada por `$`.
- Botão no canto superior direito → **Mostrar Título**, **Mostrar Legenda** (alterna para "Ocultar Legenda"), **Imprimir Gráfico**.

Série do tipo **Linha** (dentro do gráfico de Colunas): Descrição, Campo na Horizontal, Campo na Vertical; ver "Acumular valores".

- **Escala Secundária** — cria escala vertical secundária para destacar a série; habilita **Sufixo da Escala**. Com Escala Secundária, o recurso de Visão Parcial Vertical não aparece. Válida se a Série for definida como Linha e Colunas.
- **Destacar pontos** — enfatiza pontos de mudança; marca **Mostrar placa de valor**.
- **Cor** — cor da série (personalizada ou padrão).

---

## Gráficos > Pizza

Não usa abas Eixos nem Série (uma única série).

### Aba Geral

Além do Título, define-se:
- **Campo Valor** — percentual de cada setor.
- **Campo Agrupamento** — campo que agrupa o gráfico.
- **Tamanho dos Títulos** — nº de caracteres na legenda de cada região. Ex.: "Nota de Compra" com `3` → "Not..." (limita a descrição).

Botão **Evento** — ver Eventos - Gráficos.

---

## Gráficos > Análise de Rentabilidade

Além de Título, define-se Tamanho do texto e:
- **Apresentação** — label por **Produto** ou **Serviço**.
- **Posição da legenda**.
- **Apresentação dos Valores** — **Percentual** ou **Valores**.
- **Colunas na legenda** — nº de divisões de colunas da legenda.
- **Abreviar legenda** — abrevia a legenda de cada região (ex.: "Faturamento" → "FAT").

Botão **Evento** — permite detalhamento hierárquico sobre os pontos: **Faturamento, CMV/PV, Gasto Variável, Gasto Fixo, M. Contribuição, Resultado**. Definido o ponto, abre o pop-up Editar Evento (ver Eventos - Gráficos).

> **Margem de Contribuição** não pode ser configurada por evento — é resultado do cálculo:
> ```
> MC = Faturamento - Custo Mercadoria Vendida - Gasto Variável
> ```

Além da expressão principal (aba Expressão, query básica do componente, uma por componente), cada parte aceita **expressão independente** (duplo clique na parte abre o construtor). A expressão independente pode usar variáveis/campos da principal.

> Sem expressão para a Margem de Contribuição, o valor é calculado a partir dos demais dados.

---

## Gráficos > Velocímetro (Gauge)

### Aba Geral

- **Campo de Valor** — campo que fornece o valor (gráfico de valor pontual).
- **Valor Mínimo** / **Valor Máximo**.
- **Faixa de alerta** — cores dos intervalos de valores.

> A grade de intervalos valida os dados; problemas aparecem em mensagem vermelha acima da grade.

Botão **Evento** (ver Eventos - Gráficos). Botão no canto superior direito → **Mostrar Título**, **Mostrar Legenda** (alterna para "Ocultar Legenda"), **Imprimir Gráfico**.

---

## Gráficos > Geográfico

- **Modo de apresentação do mapa** — por **Países** ou **Estados**.
- **Legenda** — quais e quantas faixas de cor.
- **Marcadores** e **Nomenclaturas** do mapa.

---

## Gráficos > Área

Configuração semelhante ao gráfico de Colunas.

### Aba Eixos
- Rotação de Títulos/Resultados (`-90º` a `90º`).
- **Redimensionamento Vertical** — automático ou fixo (4 casas).
- **Tipo** fixo: horizontal (agrupamentos) em **Categoria**, vertical (quantitativo) em **Valor**.
- **Visão Parcial** — Primeiros/Últimos (padrão: Primeiros).
- **Omitir valores nulos**.

Aba **Série** também é essencial.

---

## Gráficos > Donut

Configuração semelhante ao Pizza, com o adicional:
- **Tipo de Donut** — **Completo - 360º** ou **Semicírculo - 180º** (formato do gráfico).

Botão **Evento** — ver Eventos - Gráficos.

---

## Gráficos > Bolha

Requer três valores por bolha: **X** (eixo X), **Y** (eixo Y) e **Z** (diâmetro).

> Bolha não usa campo de Categoria, só de Valor.

- **Aba Eixos** — nomenclatura dos eixos Horizontal e Vertical.
- **Aba Séries** — dados por agrupamento de bolhas; cada série é uma cor (várias séries por gráfico).

---

## Gráficos > TreeMap

Abas: Geral, Categorias, BIA.

### Aba Geral
- **Exibir valor no item** — mostra o valor junto a cada item.
- Botão **Evento** (ver Eventos - Gráficos).
- **Layout de Apresentação** — personaliza por **Categoria** (como as categorias aparecem) e **Item** (como os itens dentro da categoria aparecem). Quatro layouts para cada:
  - **Simples e rápido** — rápido, mas dificulta comparação.
  - **Listra** — mesma direção.
  - **Proporcional alternado** — facilita comparação, mas pode alterar a direção.
  - **Proporcional** — como o alternado, sem alterar a direção.

### Aba Categorias
- **Id** — identificador da categoria; todo item pertencente deve ter valor idêntico ao Id na coluna do **Campo de Categoria**.
- **Descrição** — descrição exibida no TreeMap.
- **Cor** — cor de fundo dos itens da categoria.

**Configurações das colunas** (conforme a query):
- **Campo de Nome** — coluna com a descrição do item exibida.
- **Campo de Categoria** — coluna com a categoria "pai" (define o quadrante de encaixe).
- **Campo de Valor** — coluna numérica com o valor do item.

---

## Gráficos > Dispersão

Verifica relação entre duas variáveis quantitativas. Abas: Eixos, Série, BIA.

- **Aba Eixos** — descrições dos eixos Horizontal e Vertical; **Tipo de apresentação**: **Pontos e linhas** ou **Somente pontos**.
- **Aba Série** — por conjunto de pontos/linhas: Descrição, variáveis Horizontal e Vertical, Cor e Placas de valor (valor ao passar o mouse).

---

## Gráficos > Radar

### Aba Eixos
Descrição do eixo Horizontal e Vertical, tipo **Valor** ou **Categoria** (mesmas definições da Linha).
- **Máscara** — formata os valores dos eixos; só para eixos tipo **Valor** (digitar ou usar o "Assistente de edição de máscara").
- **Omitir valores nulos**.
- **Omitir títulos** — oculta alguns títulos para clareza.
- Rotação do Título na seção Vertical (`-90º` a `90º`).

### Aba Série
No Radar a série é do tipo **Linha** ou **Área** (resultado delimitado por linhas ponto a ponto, ou área preenchida). Define-se Descrição, Campo na Horizontal, Campo na Vertical.
- **Mostrar placa de valor** — valor por ponto ao passar o mouse.
- **Cor** — personalizada ou padrão (**Usar cor padrão**).

---

## Gráficos > Funil

Visualiza valores em estágios de um processo (ex.: clientes por etapa do funil de vendas).

### Aba Geral
- Botão **Evento** (ver Eventos - Gráficos).
- **Campo Valor** — valores de cada setor do funil.
- **Campo Etapa** — base das etapas do gráfico.
- **Exibição dos Títulos** — **Valor** (valores exatos por fatia) ou **% da etapa anterior** (percentual sobre o estágio precedente).

---

## Gráficos > Intervalo de Área

Cria ranges de valores para destacar comparações num período (ex.: preço praticado acima/na média/abaixo do mercado). Configuração semelhante ao gráfico de Colunas.

### Aba Eixos
- Rotação de Títulos/Resultados (`-90º` a `90º`).
- **Visão Parcial** — Primeiros/Últimos (padrão: Primeiros).
- **Tipo** fixo: horizontal (agrupamentos) em **Categoria**, vertical (quantitativo) em **Valor**.
- **Omitir títulos**.

### Aba Série
Série do tipo **Intervalo de Área** ou **Linha**. Define-se Descrição e **Campo na Horizontal**.
- **Campo Mín.** e **Campo Máx.** — limites onde o gráfico oscila (elevações/quedas do período).
- **Mostrar placa de valor** — valor por ponto ao passar o mouse.
- **Cor** — personalizada ou padrão (**Usar cor padrão**).

---

## Acumular Valores

Disponível para **Linha**, **Barras** e **Colunas**, na aba Série, abaixo de Campo na Horizontal/Vertical. O campo a que se liga varia:

| Tipo | Vinculado a |
|---|---|
| Linha | Campo na Horizontal **e** Campo na Vertical |
| Barras | Campo na Horizontal |
| Colunas | Campo na Vertical |

Faz o indicador somar seus próprios valores conforme o progresso. Ex. (Barras): série com eixo vertical = período e horizontal = valores de venda. Marcando **Acumular valores**, a primeira barra traz o total até então; a segunda soma seu valor ao da anterior, e assim por diante. Vale só para campos numéricos.

**Máscara** dos eixos (Linha/Barras/Colunas) — só para eixos tipo **Valor**; digitar ou usar o "Assistente de edição de máscara".
