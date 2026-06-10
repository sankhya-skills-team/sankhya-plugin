## Introdução

O primeiro passo para criação de um "Dashboard " será a construção dos "gadgets" (componentes) que farão parte de sua composição. A criação destes componentes será feita por meio desta tela. 

Quando a tela é aberta em modo "Grade" os componentes que já foram cadastrados serão exibidos. 


#### Painel de Filtros 

Localizado no lado esquerdo da tela, teremos o painel com as seguintes funcionalidades: 

- O "Botão de Filtros" permitirá a criação de filtros personalizados. 

- No campo "Código" pode-se pesquisar o código dos gadgets criados para o filtro. 

- Ao informar um texto no campo "Título Contendo" , o sistema fará a busca baseado no texto que foi inserido. 

- Da mesma forma como o campo Título Contendo , o campo "Descrição Contendo" fará a busca com base na Descrição inserida neste. 

- Em "Categoria" você poderá filtrar os gadgets criados por meio da categoria atribuída a cada um deles. 

Teremos ainda no canto direito da tela, o ícone que quando acionado, permitirá a visualização e edição da posição dos níveis contidos no dashboard. Sendo que, esta funcionalidade também estará disponível no momento da edição do dashboard. 

O primeiro passo para criação de um "Dashboard" será a construção dos "gadgets" que farão parte de sua composição. A criação de "gadgets" é feita através desta tela. 

Nota: pode-se visualizar mais detalhes sobre a criação de Dashboards por meio do link Construtor de Dashboards . 

Importante: se a licença de uso do cliente possuir o visualizador de Dashboards ( 30647 - DASHVIEWER/W ), o sistema não irá consumir licenças do Construtor de Componentes de BI ( 30616 - EDITOR DE DASHBOARD/W ) para visualização de Dashboards. Deste modo, quando as licenças de visualização de Dashboards esgotarem não será possível abrir nenhuma visualização de Dashboards. 

Acionando-se o sinal de inclusão de um novo componente (gadget), informa-se um "Título" para o mesmo. O campo "Categoria" serve para que os gadgets sejam agrupados por categoria; é um campo de livre digitação onde pode-se criar a categoria desejada, ou simplesmente pesquisar uma já existente. 

Nota: não existe um cadastro prévio de Categorias, as mesmas são criadas diretamente neste campo a medida em que são digitadas. 

No campo "Ativo" podemos ativa e desativar o componente conforme sua marcação. 

Em "Descrição" o sistema permite que você faça breves comentários sobre o novo gadget de modo que sua identificação fique mais fácil. 


[voltar ao topo]

---

## Design | XML

Temos duas formas de montar o gadget; uma pelo "Design" , que é um assistente que auxiliará na sua montagem: 


Pelo Design selecionam-se os "Componentes" propriamente ditos, sendo estes divididos em "Controles" e "Gráficos" . 

#### Controles 

- Valor; 

- Tabela; 

- Tabela Dinâmica; 

- Geomapa. 

#### Gráficos 

- Linha; 

- Barras; 

- Colunas; 

- Pizza; 

- Análise de Rentabilidade; 

- Velocímetro; 

- Geográfico; 

- Área; 

- Donut; 

- Bolha; 

- TreeMap; 

- Dispersão 

- Intervalo de Área. 

A segunda maneira de construção de um componente é por meio do "XML" caso você conhecer a sintaxe (por esse motivo, não detalharemos aqui a construção de gadgets por meio de XML). 


Caso o componente seja construído pelo "Design" , à medida que é montado, o sistema irá compor o "XML" ; c ontudo, caso você conheça a sintaxe, poderá montar o gadget diretamente pelo XML. Este será gravado no banco de dados na tabela "TSIGDG" , que possui que possibilitam gravar todas as informações do cabeçalho do Construtor de Componentes de BI, além do campo "CONFIG" que irá arquivar todo o conteúdo do XML. 

Hoje no sistema é possível na criação de dashboards utilizar bancos de dados que não é o banco do Sankhya Om como fonte de dados; consideremos para estas situações, bancos de dados externos ao sistema. Para mais informações sobre este procedimento, acesse o link Banco de Dados - Dashboards no Sankhya-Om . 

Nota: quando você comprar uma solução pelo Place e esta for protegida, os botões "Design" e "XML" ficarão desabilitados. 

[voltar ao topo]

---

## Área de Trabalho

Cada componente que pode ser utilizado é selecionado da mesma maneira; ao selecionar o gadget desejado e arrastá-lo para a "área de trabalho [principal]" . Temos como exemplo, a inserção do componente "Gráfico de Linhas" : 


Quando inserido, cada componente possui as seguintes ferramentas: 

Alterar tipo: Esta opção é apresentada apenas para os componentes do tipo "Gráfico" e ao ser acionada tem-se a apresentação de uma pequena tela para seleção do novo componente a ser empregado. 

Mover para cima e Mover para baixo: Nos casos em que se está realizando uma análise que conte com mais de um componente, através destes botões pode-se posicioná-los para cima ou para baixo, respectivamente, conforme a necessidade da análise. 

Editar: Esta opção quando acionada, abre a tela própria de edição de cada componente; através dela, realiza-se toda a configuração do gadget. Através de um duplo clique do mouse sobre o componente na área de trabalho, também é aberto o seu modo de edição. 

Remover: Por meio desta opção você poderá remover um componente que não será utilizado; que quando acionado, o sistema apresentará um questionamento de confirmação do procedimento de exclusão. Quando um componente da área de trabalho for selecionado, ao pressionar a tecla "Delete" do teclado,a remoção também será efetuada. 

#### Disposição dos componentes 

Em casos que há a necessidade de utilização de mais de um gadgets de uma vez para aprimoramento de análise, o sistema contará com uma estrutura que possibilita a construção do layout mais flexível. 

O quadro "Ferramentas" posicionado no canto superior esquerdo da tela possibilita a divisão (aba "Dividir" ) na quantidade de colunas desejadas, da área selecionada; esta pode ser a área principal ainda sem nenhum componente inserido, ou a área já preenchida com algum gadget. Notemos na imagem abaixo, que optou-se por uma divisão em quatro colunas, onde a primeiro e a terceira coluna também foram divididas. 

Pode-se também por meio da aba "Inserir" , acrescentar a quantidade de colunas desejadas e necessárias para a construção do layout. 


No alto do quadro Ferramentas, tem-se as seguintes opções: 

Desfazer a última ação: Esta opção irá desfazer a última atividade realizada na construção do layout. 

Excluir a coluna selecionada: Por meio desta, será feita a exclusão da coluna que estiver selecionada. 

Limpar a coluna selecionada: Diferentemente da opção anterior, esta realiza apenas a limpeza da coluna selecionada; não é feita sua exclusão. 

Mesclar a coluna selecionada: Este recurso pode ser utilizado nos casos em que incluiu-se alguns componentes no painel principal, e optou-se por manter apenas um componente; ao acionar este botão, os componentes presentes na tela são mesclados ao painel principal, obtendo-se assim somente uma camada de componentes a serem configurados. 

Layout: Este botão apresenta as opções "Top-Down" e "Personalizado" ; a primeira permite a configuração da direção dos componentes, apenas na vertical; a segunda opção, possibilita que os componentes sejam divididos/posicionados vertical e horizontalmente. Por padrão, a opção Personalizado é apresentada assinalada. 

Importante: a disposição aqui definida para os componentes será mantida na geração/visualização dos componentes, depois que estes forem devidamente configurados (sequência desta documentação).Trabalhando-se com Dashboards que possuem mais de um nível de navegação, ou seja, clicando-se em um trecho da análise tem-se a abertura de outros níveis, ao utilizar estes botões, será possível retornar para o primeiro nível, retornar ao nível anterior e avançar para o nível seguinte, respectivamente. 

: Trabalhando-se com Dashboards que possuem mais de um nível de navegação, ou seja, clicando-se em um trecho da análise tem-se a abertura de outros níveis, ao utilizar estes botões, será possível retornar para o primeiro nível , retornar ao nível anterior e avançar para o nível seguinte , respectivamente. 

Observação: durante a apresentação de um dashboard na tela, caso seu carregamento seja demorado em consequência da grande quantidade de dados, pode-se interromper sua construção através do "x" localizado no lado superior esquerdo da tela junto à barra de carregamento. 

Nota: caso o parâmetro "Usa dashboard antigo - USADASHANT" esteja ativado, o quadro "Ferramentas" deixará de ser exibido e consequentemente esta forma de visualização dos gadgets não poderá ser utilizada. 

Não é viável deixar os containers do segundo nível vazios no BI, pois mesmo com relatórios de diferentes tipos além do I-report , o sistema tentará interpretá-los como contendo um gadget, resultando em erros. 

[voltar ao topo]

---

## Cartões Inteligentes

No Construtor de Componentes de BI tem-se a opção "Cartão Inteligente" que irá configurar a exibição dos componentes como Cartões Inteligentes . Tem-se que esta opção estará disponível caso a base do usuário esteja atualizada com o Sankhya Om . 


Para utilizar este recurso, o componente deve atender aos seguintes requisitos: 

- Estar ativo; 

- Possuir informações; 

- Não conter filtros (parâmetros); 

- Nenhum de seus níveis possuir mais de um gadget (com exceção dos gadgets do tipo Valor , pois estes não possuem limite de quantidade por nível). 

Deste modo, outra opção será habilitada para que o usuário possa configurar qual será o tamanho de exibição do cartão. 


Uma vez configurado, o componente passa a ser exibido na tela de Acessos para que o administrador configure quais usuários poderão visualizá-lo na área de trabalho. 


Observação: o componente só deixará de ser exibido na tela de Acessos quando for excluído do Construtor de Componentes de BI . Desta forma, você poderá habilitar ou desabilitar o mesmo sem perder as configurações de acesso salvas. 

Ao acessar o sistema com o usuário configurado, o cartão será exibido na área de trabalho: 


[voltar ao topo]