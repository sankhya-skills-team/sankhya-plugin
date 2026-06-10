## Gráficos > Linha

Ao acionar o modo de edição do gráfico, define-se seu "Título" , o "Tamanho do texto" a ser utilizado para apresentação do gráfico e se sua "Legenda" será ou não apresentada; caso afirmativo, deve-se estabelecer também sua "Posição" e "Direção" no gráfico. 

#### Aba Eixos 

No componente gráfico do tipo "Linha" deve-se definir uma "Descrição" pro eixo, tanto "Horizontal" quanto "Vertical" e definir se este será do tipo "Valor" ou do tipo "Categoria" . 

- Categoria : Este tipo será por grupo; exemplo: Receitas e Despesas. 

- Valor : Este tipo será contínuo, quantitativo; exemplo: Volume de Receitas e Volume de Despesas. 

Através do campo "Visão Parcial" pode-se definir dentre as opções Primeiros Registros e Últimos Registros , quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise. 

Observação: as configurações feitas no eixo horizontal influenciam nas configurações do eixo vertical. Por exemplo: Quando o campo Visão Parcial está desativado, ele ignora as configurações do mínimo e máximo do quadrante vertical. 

Na edição dos gráficos cartesianos (Linhas, Barras e Colunas) o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; pode-se posicioná-los de "-90º" a "90º" ; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico. 

A opção "Redimensionamento Vertical" quando acionada, efetivará a configuração realizada para os valores mínimo e máximo do redimensionamento vertical condizentes ao gráfico. Além disso, o redimensionamento poderá ser apontado de forma automática ou fixa. Sendo que, optando pela forma Fixa o mesmo permitirá a fixação do seu posicionamento em um valor decimal de 4 casas. 

A marcação "Omitir valores nulos" quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget. 

#### Aba Séries 

Série é um conjunto de dados que irão compor o gráfico. Nesta aba poderão ser definidas várias "Séries" sendo que cada uma representará uma linha no gráfico. 


No gráfico de Linha a "Série" poderá ser apenas do tipo "Linha" . Informa-se também a "Descrição" da Série. O "Campo na Horizontal" e o "Campo na Vertical" virão das variáveis disponíveis, e apresentarão os valores para a Série na vertical e na horizontal. 

Quando a opção "Destacar pontos" é assinalada, irá fazer com que os pontos onde ocorreram mudança nos valores do gráfico, sejam enfatizados; esta opção marca automaticamente o campo "Mostrar placa de valor" (localizado logo abaixo), que no gráfico irá apresentar a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo. Vejamos um exemplo de um gráfico gerado: 


Na aba "Série" , tanto em modo grade, como em formulário, para os gráficos cartesianos (Linha, Barras e Colunas), o sistema disponibiliza o campo "Cor" para que seja informada a cor de apresentação da Série , possibilitando a personalização desta. Da mesma forma, os demais campos também são apresentados nas duas formas de visualização (grade e formulário) para serem analisados e editados se necessário. 

Se o campo de marcação "Usar cor padrão" não estiver assinalado, a paleta de cores será habilitada e a Série receberá cores definidas na paleta; caso contrário, serão utilizadas cores padrão do sistema. 

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

Observação: este tipo de gadget ao ser visualizado conta com o recurso de "Zoom" que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão "Resetar Zoom" , que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela. 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Barras

#### Aba Eixos 


Na edição dos gráficos cartesianos ( Linhas , Barras e Colunas ) o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que eles serão apresentados nos gráficos; você poderá posicioná-los de "-90º" a "90º" ; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico. 

Ainda na aba "Eixos" , a única diferença entre a configuração do gráfico de Barras para o gráfico de Linhas será no campo "Tipo" , que apresentará um valor fixo , tanto para o eixo horizontal quanto para o eixo vertical. Como no gráfico de Barras somente o eixo horizontal poderá apresentar valores quantitativos, o Tipo virá fixado como "Valor" , já para o eixo vertical que apresentará os agrupamentos, o Tipo virá fixado como "Categoria" . 

Por meio do campo "Visão Parcial" pode-se definir dentre as opções Primeiros Registros e Últimos Registros , quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise. 

A marcação "Omitir valores nulos" quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget. 

#### Aba Séries 


O gráfico de Barras permite a associação de Série de "Barras" com "Linhas" . Pode-se definir "n" séries para um gráfico. Exemplo: 

Pode-se criar uma Série com vendas por parceiro e outra por compras, sendo as duas por "Barras" e criar sobre estas, uma "Linha" trazendo o somatório mostrando o volume de negociações. 

O campo "Mostrar placa de valor" no gráfico irá apresentar a informação de cada barra quando o mouse for posicionado sobre a mesma. 

Observação: para que seja exibida uma placa de valor que está sobrepondo outra placa, é necessário que o parâmetro "Permite sobreposição de placas de valor em gráfico - SOBREVALORGRAF" esteja ligado. Do contrário, o sistema irá ocultar as placas de valor quando identificar que a mesma irá sobrepor outra. 


Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

Observação: este tipo de gadget ao ser visualizado, conta com o recurso de "Zoom" que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão "Resetar Zoom" , que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela. 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Colunas

Na utilização do Gráfico de Colunas, ao realizar sua edição, nota-se o campo "Colunas" que é utilizado para determinar-se a quantidade de colunas que se deseja visualizar no momento em que o Dashboard em construção será aberto. Este campo possui "6" (seis) como valor padrão, não podendo este valor ser diminuído, apenas acrescido. 

#### Aba Eixos 


Na edição dos gráficos cartesianos (Linhas, Barras e Colunas) o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; você poderá posicioná-los de "-90º" a "90º" ; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico. 

A única discrepância em relação à configuração do gráfico de barras para este, será a inversão dos valores do campo "Tipo" nesta aba. Pois, num gráfico de "Colunas" o eixo horizontal apresentará os agrupamentos e o Tipo virá fixado como "Categoria" , já o eixo vertical apresentará valores quantitativos e o Tipo virá fixado como "Valor" . 

Por meio do campo "Visão Parcial" pode-se definir dentre as opções Primeiros Registros e Últimos Registros , quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise. 

Observação: as configurações feitas no eixo horizontal influenciam nas configurações do eixo vertical. Por exemplo: Quando o campo Visão Parcial está desativado, ele ignora as configurações do mínimo e máximo do quadrante vertical. 

A opção "Redimensionamento Vertical" quando acionada, irá efetivar a configuração realizada para os valores mínimo e máximo do redimensionamento vertical condizentes ao gráfico. Além disso, o redimensionamento poderá ser apontado de forma automática ou fixa. Sendo que, optando pela forma Fixa o mesmo permitirá a fixação do seu posicionamento em um valor decimal de 4 casas. 

Nota: o Redimensionamento Vertical não será aplicado, caso exista dois ou mais cadastros de série e um deles estiver com a marcação "Escala Secundária" acionada. 

A marcação "Omitir valores nulos" quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget. 

Ao ativar a opção "Rotacionar Resultados" , pode-se redefinir novos intervalos no gráfico, referentes ao seu eixo "Y" , ou seja, dependendo do dimensionamento do gráfico, pode-se visualizar valores de 0 a 10, ou de 2 a 8, por exemplo, bastando para isso, movimentar a barra vertical que será apresentada no lado superior direito da tela. 

#### Aba Série 

Assim com o gráfico de Barras, o de Colunas também permite a associação de Série de "Linhas" com "Colunas" . Pode-se definir "n" séries para um gráfico. 


Importante: a ordenação das séries (controlada pelos botões ) influencia na apresentação do gráfico, pois se for criado um dashboard que contenha uma linha de totalização, esta é exibida por detrás das barras. 

O campo "Mostrar placa de valor" no gráfico irá apresentar a informação pertinente a cada coluna, quando posicionar-se o mouse sobre a mesma. 

Observação: pode-se através da expressão SQL buscar a informação desejada para ser colocada no balão de informações do gráfico e adicioná-la ao campo Descrição, sempre prefixado pelo símbolo $ . 

O botão localizado no lado superior direito da tela, quando acionado, apresenta as opções "Mostrar Título" (quando marcada, exibe o título do gráfico), "Mostrar Legenda" (apresenta a legenda do gráfico, quando assinalada; quando marcada, esta opção assume a nomenclatura "Ocultar Legenda" para a necessidade de se esconder a legenda novamente) e "Imprimir Gráfico" (da início ao processo de impressão do gráfico em questão). 

Ainda sobre a aba Série na configuração do gráfico de colunas, definindo-se o campo Série com a opção "Linha" , tem-se a aba com as seguintes informações: 


Deve-se preencher os campos "Descrição" , "Campo na Horizontal" e "Campo na Vertical" ; o link Acumular valores , irá apresentar os detalhes a respeito da referida marcação. 

A marcação "Escala Secundária" ao ser assinalada, será possível no gráfico gerado, realizar a criação de uma escala vertical secundária para que seja feito o destaque dos valores da respectiva série de dados. Efetuando-se esta marcação, será apresentado logo abaixo da mesma, o campo "Sufixo da Escala" , para inclusão de uma breve denominação para a escala secundária. Caso a série possua escala secundária (marcação realizada), o recurso de Visão Parcial Vertical do Gráfico não será apresentado. A Escala Secundária poderá ser utilizada se o campo Série for definido com ambas as opções disponíveis, Linha e Colunas . 

A opção "Destacar pontos" quando assinalada, irá fazer com que os pontos onde ocorreram mudança nos valores do gráfico, sejam enfatizados; esta opção exibe e assinala automaticamente a marcação "Mostrar placa de valor" (localizado logo abaixo), que no gráfico irá apresentar a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo. 

A marcação "Cor" é utilizada para informar-se a cor de apresentação da Série , possibilitando a personalização desta, de modo que pode-se utilizar a cor desejada ou ainda, a cor padrão . 

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

Observação: este tipo de gadget ao ser visualizado, conta com o recurso de "Zoom" que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão "Resetar Zoom" , que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela. 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Pizza

Em relação à configuração dos gráficos apresentados anteriormente, este tipo de gráfico apresenta uma maior variação, uma vez que para ele não configura-se as abas "Eixos" e "Série" . 


#### Aba Geral 

Como teoricamente em um gráfico de Pizza será apresenta uma única "Série" , além do "Título" , configura-se aqui os campos "Valor" e "Agrupamento" . 

As funcionalidades do botão "Evento" podem ser visualizadas clicando-se no link Eventos - Gráficos . 

O "Campo Valor" trará o percentual de determinado setor circular. O "Campo Agrupamento" definirá o campo que fará o agrupamento no gráfico. 

Por meio do campo "Tamanho dos Títulos" , você definirá a quantidade de caracteres que serão utilizados na legenda de cada região do gráfico de pizza. Por exemplo, em um gráfico onde uma das legendas é "Nota de Compra" , ao definir o campo "Tamanho dos Títulos" com "3" caracteres, será apresentada no gráfico a descrição "Not..." ; em outras palavras, o sistema irá limitar a descrição à quantidade de caracteres definidos no campo. Vejamos um exemplo de um gráfico de pizza: 


#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Análise de Rentabilidade

Neste gráfico além do seu "Título" , define-se o "Tamanho do texto" a ser nele utilizado. 

Apresentação: Determina-se como será a apresentação (label) do gráfico; se por "Produto" ou "Serviço" . 

Na "Apresentação" será determinado como se a apresentação (label) do gráfico será por "Produto" ou por "Serviço" . 

A "Posição da legenda" será definido a posição que a legenda se encontrará. 

No campo "Apresentações dos Valores" deve-se indicar se os valores a serem exibidos será por "Percentual" ou "Valores" . 

Em "Colunas na legenda" determina-se a quantidade de divisões de colunas das legendas de cada região do gráfico. 

Por meio da marcação "Abreviar legenda" você poderá abreviar a legenda gerada para cada região do gráfico. Como por exemplo, se tivermos a "Faturamento" será apresentada no gráfico como "FAT" . 

O botão "Evento" possui algumas opções que irão possibilitar a exploração das informações pertinentes à Análise de Rentabilidade em diferentes níveis de detalhamento, exibindo-as de maneira hierárquica. Tem-se as seguintes alternativas: 

- Faturamento; 

- CMV/PV: 

- Gasto Variável; 

- Gasto Fixo; 

- M. Contribuição; 

- Resultado. 

Depois de definido o ponto a ser considerado para configuração do Evento, o pop-up Editar Evento será exibido, os detalhes deste poderão consultados por meio do link Eventos - Gráficos . 

Observação: a Margem de Contribuição não pode ser configurada por meio de evento, pois é um resultado obtido através do seguinte cálculo: 

```
MC = Faturamento - Custo Mercadoria Vendida - Gasto Variável 
```


Além da expressão principal , definida na aba "Expressão" , este tipo de gráfico permitirá que sejam criadas expressões independentes para cada uma de suas partes. Para isto, basta apenas dar um duplo clique sobre qualquer uma das partes para que o construtor de expressões seja aberto. Na expressão independente que esta sendo definida para uma determinada parte, pode-se utilizar variáveis ou campos que vieram da expressão principal. 

Nota: a expressão principal é a que foi definida na aba Expressão , trata-se da query básica que trará informações para o componente. Cada componente possui uma expressão principal. 

Importante: se não for informada uma expressão para a Margem de Contribuição, seu valor será calculado com base nos outros dados informados. 

Observe o exemplo de um gráfico de Análise de Rentabilidade: 


[voltar ao topo]

---

## Gráficos > Velocímetro

O funcionamento do gráfico de Gauge (Velocímetro) segue o mesmo princípio dos demais componentes. 


#### Aba Geral 

Aqui, teremos os seguintes dados: 

Será determinado no "Campo de Valor" , a qual campo será atribuído o valor do gráfico (lembrando-se que se trata de um gráfico de valor pontual). 

Definiremos nos campos "Valor Mínimo" e "Valor Máximo" , os valores mínimo e máximo a serem considerados no gráfico. 

Serão estabelecidas em "Faixa de alerta" , as cores dos intervalos de valores a serem empregados no gráfico. 

Nota: na grade dos intervalos são feitas algumas validações para auxiliar o usuário. Caso seja encontrado algum problema será exibida uma mensagem em vermelho acima da grade com a listagem de problemas encontrados. 

As funcionalidades do botão "Evento" podem ser visualizadas clicando-se no link Eventos - Gráficos . 


O botão localizado no lado superior direito da tela, quando acionado, apresenta as opções "Mostrar Título" (quando marcada, exibe o título do gráfico), "Mostrar Legenda" (apresenta a legenda do gráfico, quando assinalada; quando marcada, esta opção assume a nomenclatura "Ocultar Legenda" para a necessidade de se esconder a legenda novamente) e "Imprimir Gráfico" (da início ao processo de impressão do gráfico em questão). 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Geográfico

Uma vez adicionado o gráfico no nível, configura-se as informações que serão representadas. 


Define-se o "Modo de apresentação do mapa" ; se as informações serão geradas por "Países" ou "Estados" . 

Tem-se também a configuração da "Legenda" , onde determina-se qual e a quantidade das faixas de cores a serem utilizadas no mapa. 

Além disso, faz-se a definição dos "Marcadores" e "Nomenclaturas" a serem empregadas no mapa quando este for visualizado. 

[voltar ao topo]

---

## Gráficos > Área

Ao acionar-se a edição deste gadget, as configurações a serem realizadas, são semelhantes às efetuadas no uso do gadget de Colunas. Na aba "Eixos" , tem-se: 

Na edição do gráfico, o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; pode-se posicioná-los de "-90º" a "90º" ; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico. 

A marcação "Redimensionamento Vertical" quando acionada, efetivará a configuração realizada para os valores mínimo e máximo do redimensionamento vertical condizentes ao gráfico. Além disso, o redimensionamento poderá ser apontado de forma automática ou fixa. Sendo que, optando pela forma Fixa o mesmo permitirá a fixação do seu posicionamento em um valor decimal de 4 casas. 

A única diferença entre a configuração do gráfico de barras para este, será a inversão dos valores do campo "Tipo" nesta aba. Pois, num gráfico de "Colunas" o eixo horizontal apresentará os agrupamentos e o Tipo virá fixado como "Categoria" , já o eixo vertical apresentará valores quantitativos e o Tipo virá fixado como "Valor" . 

Através do campo "Visão Parcial" pode-se definir dentre as opções Primeiros Registros e Últimos Registros , quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise. 

A marcação "Omitir valores nulos" quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget. 

Na construção deste gadget, também é essencial a configuração da aba "Série" . 


Observação: este tipo de gadget ao ser visualizado, conta com o recurso de "Zoom" que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão "Resetar Zoom" , que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela. 

As informações pertinentes a aba "BIA" podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Donut

Primeiramente na configuração do gráfico de Donut, define-se seu "Título" , o "Tamanho do texto" a ser utilizado para apresentação do gráfico e se sua "Legenda" será ou não apresentada; caso afirmativo, deve-se estabelecer também sua "Posição" e "Direção" no gráfico. 

As funcionalidades do botão "Evento" podem ser visualizadas clicando-se no link Eventos - Gráficos . 

Esta configuração é semelhante a que é realizada no uso do gráfico de Pizza, se diferenciando pela definição do "Tipo de Donut" , que traz as opções "Completo - 360º" e "Semicírculo - 180º" ; a escolha feita neste campo, irá determinar o formato em que o gráfico Donut será apresentado, ou seja, se irá formar um círculo completo ou um semicírculo. 


As informações pertinentes a aba "BIA" podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


Observe abaixo o exemplo de um gráfico Donut gerado no formato completo: 


[voltar ao topo]

---

## Gráficos > Bolha

Aqui, teremos mais  uma alternativa para geração de gráficos nos Componentes de BI. Suas configurações básicas e funcionalidades, seguem o padrão dos demais componentes. 

A diferença principal para os outros componentes é a necessidade de definição de um diâmetro para as bolhas, a saber; para construção de um gráfico de bolha, são necessários três valores, "X" , "Y" e "Z" , que se referem aos campos do eixo X, eixo Y e diâmetro da bolha, respectivamente. 

Observação: vale ressaltar que o dashboard de Bolha não utiliza campo de "Categoria", somente campo de "Valor" . 

Primeiramente na configuração do gráfico de Bolhas, define-se seu "Título" , o "Tamanho do texto" a ser utilizado para apresentação do gráfico e se sua "Legenda" será ou não apresentada; caso afirmativo, deve-se estabelecer também sua "Posição" e "Direção" no gráfico. 

Na aba "Eixos" configura-se a nomenclatura a ser atribuída aos eixos "Horizontal" e "Vertical" do gráfico que será construído. 

Na aba "Séries" configura-se os dados para cada agrupamento de bolhas. Cada série configurada será referente a uma coloração de bolhas, portanto, pode-se ter mais de uma série em cada gráfico gerado. 


Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

Observação: este tipo de gadget ao ser visualizado, conta com o recurso de "Zoom" que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão "Resetar Zoom" , que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela. 

As informações pertinentes a aba "BIA" podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > TreeMap

Ao acionar a tela para configuração deste componente, tem-se as abas "Geral" , "Categorias" e "BIA" . 


Depois de informado o Título e definido o Tamanho do texto, na aba Geral tem-se a marcação "Exibir valor no item" , que quando efetuada, no gráfico gerado, será apresentado juntamente a cada item, o valor que este representa. 

As funcionalidades do botão "Evento" podem ser visualizadas clicando-se no link Eventos - Gráficos . 

Na seção "Layout de Apresentação" tem-se a possibilidade de personalização da apresentação do gráfico; faz-se esta personalização por meio de duas opções, "Categoria" e "Item" . A opção de layout para Categoria determina como as categorias serão exibidas; a opção Item, como os itens dentro de um categoria serão apresentados. 

Tem-se quatro layout's disponibilizados para Categoria e Item . A saber: 

- Simples e rápido: Layout simples e rápido para apresentar, porém, pode dificultar a comparação das informações. 

- Listra: Layout simples que apresenta as informações na mesma direção. 

- Proporcional alternado: Layout que tenta apresentar as informações para facilitar a comparação, porém, pode alterar a direção das mesmas. 

- Proporcional: Comportamento semelhante ao "Proporcional alternado", porém, não altera a direção das informações. 

Na aba "Categorias" , configura-se exatamente as categorias que serão utilizadas na apresentação do gráfico. 


No "Id" , ou Identificador de categoria, Todos os itens (resultados retornados na expressão) que pertencem a ela, deverão ter obrigatoriamente o valor idêntico ao identificador na coluna configurada no "Campo de Categoria" . 

Na "Descrição" , informaremos a descrição da categoria que será exibida no Treemap. 

Você definirá no campo "Cor" , a cor de fundo para os itens desta categoria. 

Na seção "Configurações das colunas" configura-se os campos de acordo com a query utilizada para gerar os dados do gráfico. 

No "Campo de Nome" será inserido o nome da coluna com o valor da descrição do item que será exibido no Gráfico Treemap. 

Informaremos em "Campo de Categoria" o nome da coluna  com o valor que representa a categoria "pai" do item; essa opção é quem define em qual quadrante o resultado será encaixado no momento de renderização do Gadget. 

Teremos no "Campo de Valor" , uma coluna com o valor que o item possui. Deverá ser uma coluna que retorna um valor numérico . 

As informações pertinentes a aba "BIA" podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Dispersão

O gráfico de Dispersão permite a verificação da existência ou não de relação entre duas variáveis de natureza quantitativa, ou seja, analisando dois aspectos, será possível com este tipo de gráfico, identificar se um elemento melhora, piora ou se mantém, quando relacionado com o segundo fator. 

Depois de determinar-se o "Título" do Componente, bem como o Tamanho do texto e suas respectivas Posições e Direções , tem-se para sua configuração, as abas "Eixos" , "Série" e "BIA" : 


Na aba Eixos , determinam-se as descrições dos eixos Horizontal e Vertical . Além disso, o campo "Tipo de apresentação" define se o gráfico gerado será composto por Pontos e linhas , ou Somente pontos . 

Já na aba Série , determinam-se as particularidades de cada conjunto de pontos e/ou linhas a serem apresentados no gráfico, tais como sua Descrição , as variáveis na Horizontal e na Vertical , as Cores de cada um e se serão exibidas Placas de valor (ao passar o mouse sobre os pontos, tem-se o valor correspondente à cada um deles). 


Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

As informações pertinentes a aba BIA podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


Vejamos abaixo o exemplo de um gráfico gerado por este componente: 


Observação: este tipo de gadget ao ser visualizado, conta com o recurso de "Zoom" que funciona clicando-se sobre a área desejada no gráfico e arrastando com o mouse até o ponto de deseja-se ampliar; automaticamente será apresentado na tela o botão "Resetar Zoom" , que ao ser acionado, tem-se a restauração da visão inicial do gráfico; ele será novamente exibido em sua totalidade na tela. 

[voltar ao topo]

---

## Gráficos > Radar

Ao acionar o modo de edição do gráfico, define-se seu "Título" , o "Tamanho do texto" a ser utilizado para apresentação do gráfico e se sua "Legenda" será ou não apresentada; caso afirmativo, deve-se estabelecer também sua "Posição" e "Direção" no gráfico. 

#### Aba Eixos 


No componente gráfico do tipo Radar , deve-se definir uma "Descrição" pro eixo, tanto Horizontal quanto Vertical e definir se este será do tipo "Valor" ou do tipo "Categoria" . 

- Categoria: Este tipo será por grupo; exemplo: Receitas e Despesas. 

- Valor: Este tipo será contínuo, quantitativo; exemplo: Volume de Receitas e Volume de Despesas. 

É possível também informar uma "Máscara" para formatar os valores dos eixos. O campo para informar a máscara só estará disponível para eixos do tipo "Valor" . É possível digitar a máscara diretamente no campo ou editá-la através do "Assistente de edição de máscara" (ícone localizado ao lado do campo). 

A marcação "Omitir valores nulos" quando realizada, caso o componente ao ser gerado, possua campos com nenhum valor (nulo), estes campos terão tais dados ocultados na visualização do gadget. 

De forma similar à marcação anterior, assinalando a opção "Omitir títulos" , alguns títulos serão automaticamente ocultados, para que se tenha uma visualização mais clara. 

Na edição do gráfico, na seção Vertical , o sistema possibilita a rotação do Título, ou seja, o ângulo em que este será apresentado nos gráficos; pode-se posicioná-lo de "-90º" a "90º" ; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título será exibido no gráfico. 

#### Aba Série 


Série é um conjunto de dados que irão compor o gráfico. Nesta aba poderão ser definidas várias "Séries" sendo que cada uma representará uma linha ou área no gráfico. 

No gráfico de Radar a "Série" poderá ser do tipo Linha ou Área , ou seja, o gráfico gerado terá seu resultado delimitado por linhas que se ligam ponto a ponto, ou toda a área que abrange o resultado será preenchida com a coloração desejada. Informa-se também a "Descrição" da Série. As informações referentes ao "Campo na Horizontal" e o "Campo na Vertical" virão das variáveis disponíveis, e apresentarão os valores para a "Série" na vertical e na horizontal. 

O campo "Mostrar placa de valor" quando assinalado, no gráfico tendo-se a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo. 

Ainda na aba "Série" , tanto em modo grade como em formulário, o sistema disponibiliza o campo "Cor" para que seja informada a cor de apresentação da "Série", possibilitando a personalização desta. Da mesma forma, os demais campos também são apresentados nas duas formas de visualização (grade e formulário) para serem analisados e editados se necessário. 

Se o campo de marcação "Usar cor padrão" não estiver assinalado, a paleta de cores será habilitada e a Série receberá cores definidas na paleta; caso contrário, serão utilizadas cores padrão do sistema. Vejamos o exemplo de um gráfico gerado: 


Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Funil

Os gráficos de Funil permitem a visualização de valores em vários estágios de um processo. Pode-se por exemplo, exibir o número de clientes em potencial em cada etapa de um cronograma de vendas. 


Primeiramente na configuração do gráfico de Funil , define-se seu "Título" , o "Tamanho do texto" a ser utilizado para apresentação do gráfico e se sua "Legenda" será ou não apresentada; caso afirmativo, deve-se estabelecer também sua "Posição" e "Direção" no gráfico. 

#### Aba Geral 

As funcionalidades do botão "Evento" podem ser visualizadas clicando-se no link Eventos - Gráficos . 

Por meio do "Campo Valor" você determinará o campo que irá representar os valores em cada setor no funil. O "Campo Etapa" define qual informação será tomada como base para apresentação das etapas no gráfico. 

Através do campo "Exibição dos Títulos" , define-se como se dará a apresentação dos resultados no gráfico, dentre as opções Valor e % da etapa anterior ; a primeira exibe os valores exatos correspondentes a cada "fatia" do gráfico; já o % da etapa anterior, apresenta o quanto em percentual uma etapa representa em relação ao seu estágio precedente. Vejamos um exemplo de um gráfico de funil: 


#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Gráficos > Intervalo de Área

Os gráficos de Intervalo de Área permitem a criação de ranges de valores, possibilitando assim destacar comparações de valores em um determinado período. Como por exemplo, uma empresa pode visualizar o dia que o preço praticado ficou acima, na média ou abaixo do preço adotado pelo mercado. 


Ao acionar-se a edição deste gadget, as configurações a serem realizadas, são semelhantes às efetuadas no uso do gadget de Colunas. Na aba "Eixos" , tem-se: 

Na edição do gráfico, o sistema possibilita a rotação dos Títulos e Resultados, ou seja, o ângulo em que estes serão apresentados nos gráficos; pode-se posicioná-los de "-90º" a "90º" ; a palavra "Exemplo" posicionada à frente desta definição, serve como teste para verificação de como o título e resultado serão exibidos no gráfico. 

Através do campo "Visão Parcial" pode-se definir dentre as opções Primeiros Registros e Últimos Registros , quando na visualização do componente, se serão apresentados os dados iniciais ou finais resultantes da geração do gadget. Por padrão, este campo é definido para exibir os Primeiros Registros da análise. 

Em um gráfico de "Intervalo de Área" o eixo horizontal apresentará os agrupamentos e o "Tipo" virá fixado como "Categoria" , já o eixo vertical apresentará valores quantitativos e o "Tipo" virá fixado como "Valor" . 

A opção "Omitir títulos" quando acionada, alguns títulos serão automaticamente ocultados, para que se tenha uma visualização mais clara. 

#### Aba Série 


A Série poderá ser do tipo "Intervalo de Área" ou "Linha" . Informa-se também a "Descrição" da Série. O "Campo na Horizontal" virá das variáveis disponíveis, e apresentará os valores para a Série na horizontal. 

Os valores informados nos campos "Campo Mín." e "Campo Máx." serviram como pontos limitadores onde o gráfico irá oscilar mostrando as elevações e quedas atingidas durante um certo período. Como por exemplo, em uma analise semanal dos valores máximo e mínimo praticados no mercado; o gráfico apresentará o valor que foi praticado pela empresa em relação à estes valores. 

O campo "Mostrar placa de valor" quando acionado, irá apresentar no gráfico a informação pertinente a cada ponto, quando posicionar-se o mouse sobre o mesmo. 

Ainda na aba Série , o sistema disponibiliza o campo "Cor" para que seja informada a cor de apresentação da Série, possibilitando a personalização desta. Se o campo de marcação "Usar cor padrão" não estiver assinalado, a paleta de cores será habilitada e a Série receberá cores definidas na paleta; caso contrário, serão utilizadas cores padrão do sistema. 

Além disso, com essa aba em modo grade, você pode agrupar as séries cadastradas. Para isso, aperte e segure o botão "Ctrl" do seu teclado, marque as séries e clique no botão "Agrupar séries" . 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Acumular Valores

A opção "Acumular valores" , está disponível para os gráficos dos tipos "Linha" , "Barras" e "Colunas" , está localizada na aba "Série" , logo abaixo dos campos "Campo na Horizontal" e "Campo na Vertical" . 

Porém esta opção estará disponível de forma diferente de acordo com o tipo do gráfico. 

- Para os gráficos do tipo "Linha" , a opção estará ligada aos dois campos "Campo na Horizontal" , e "Campo na Vertical" ; 

- Já para os gráficos do tipo "Barras" , a opção se relaciona ao campo "Campo na Horizontal" ; 

- Nos de tipo "Colunas" , ela é relacionada ao campo "Campo na Vertical" . 

Esta opção permite a configuração de indicadores (barras, colunas, linhas) nos gráficos de modo a somar seus próprios valores conforme o progresso. Para exemplificar o seu uso, considere um gráfico válido (em barras, colunas, ou em linhas) que mostre o andamento das vendas conforme determinado período (o período pode ser configurado em forma de parâmetro). 

Para isso, o gadget deve ser configurado para realizar uma busca no banco de dados que possibilite o gráfico ser alimentado com os valores necessários. Dessa forma, uma expressão SQL deve ser especificada para isso. Para os gráficos do tipo "Barras" , configurar uma "Série" onde o eixo vertical corresponda ao período e o eixo horizontal, aos valores das vendas. 

Marcando-se a opção "Acumular valores" , as barras que partem do eixo referente ao período, somarão seus valores conforme a evolução do período. Ou seja, a primeira barra, correspondente ao primeiro dia/mês do período, possuirá o valor total das vendas realizadas até então. A segunda barra, que corresponderá ao segundo dia/mês do período, somará/acumulará o seu próprio valor, ao valor da barra anterior, e assim por diante. 

O mesmo ocorre nos demais tipos de gráfico, porém, com seus comportamentos particulares. É importante observar que a opção Acumular valores é utilizada apenas para campos numéricos. 


Na edição desses tipos de gráficos (linhas, barras e colunas) é possível informar uma máscara para formatar os valores dos eixos. O campo para informar a máscara só estará disponível para eixos do tipo "Valor" . É possível digitar a máscara diretamente no campo ou editá-la através do "Assistente de edição de máscara" (ícone localizado ao lado do campo): 


[voltar ao topo]