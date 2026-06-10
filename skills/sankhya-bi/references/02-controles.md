## Controles > Valor

Acionando-se o botão de "Edição" será feito o direcionamento para a seguinte tela: 


A imagem acima mostra a edição de um componente de "Valor" que retornará um "valor pontual" ou "texto" após a renderização. 

#### Aba Geral 

Na utilização do componente "Controle/Valor" pode-se trabalhar com uma barra de ferramentas para formatação de textos, transcrevendo estes em formato HTML. Para utilização desta funcionalidade, efetua-se a "seleção do texto" desejado, e aciona-se o botão referente a formatação que será empregada no texto em questão. 

Os botões apresentados para utilização, possuem as seguintes funcionalidades: 

O texto será adaptado para a exibição em "Negrito" ; 

O texto selecionado, será apresentado no modo "Sublinhado" ; 

O texto será apresentado no modo "Itálico" ; 

Através desta opção, será adicionada uma "Quebra de linha" ao texto selecionado; 

O texto selecionado, será alinhado à "Esquerda" ; 

Este botão irá alinhar o texto selecionado ao "Centro" ; 

O texto selecionado, será alinhado à "Direita" ; 

Através deste botão, pode-se definir os "Tipos de Fonte" que serão utilizados no texto selecionado; 

Por este botão, pode-se determinar o "Tamanho da Fonte" do texto; 

As cores definidas nestas duas caixas, irão determinar a "Cor da Fonte" e a "Cor do Realce" , respectivamente. 

Nota: vale ressaltar que para empregar ao texto alguma das formatações mencionadas acima é necessário que primeiramente este texto seja selecionado (através do mouse), e em seguida aciona-se o botão desejado. 

Caso um "Título" seja informado, este será renderizado como um label. No painel à direita, o sistema disponibilizará todos o "Parâmetros/Variáveis disponíveis" para que estes possam ser utilizados no componente. 

Estes parâmetros e variáveis poderão ser utilizados tanto no "Texto" quanto no "Título" do componente. Basta arrastar o parâmetro ou variável para o campo do Título ou do Texto. 

Contudo, pode-se digitar diretamente no texto os parâmetros, desde que estes estejam disponíveis para o componente caso contrário o sistema acusará erro. 

Além disso, este componente permite por meio de expressões a criação de links que se direcionam para os sites desejados. Para tanto, é necessário atentar-se para alguns detalhes na referida expressão, como por exemplo na criação de um link direcionado para o site www.google.com a expressão ficará da seguinte forma: 

```
<a href="http://www.google.com"  target="_blank"> Nome do link</a> 
```

Importante: na constituição da expressão deve-se sempre utilizar o target = " _ blank" no final do link para que o mesmo funcione de forma correta. 

#### Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo]

---

## Controles > Tabela

Quando o componente for do tipo "Tabela" o painel de "Edição" não apresentará o campo "Texto" , apenas o "Título" . Contudo, a edição da "Descrição" será muito importante neste tipo de componente, pois ela aparecerá no header (cabeçalho) da Tabela, após a renderização. 

#### Aba Geral 


No campo "Entidade" poderemos definir uma Entidade/Tabela de modo que será possível executar ações vinculadas à estas entidades. Teremos o exemplo, onde informou-se neste campo a entidade "Parceiro" , e na tela Dicionário de Dados definiu-se duas ações para ela, denominadas neste exemplo, "Script" e "Lançador" , como pode-se notar na imagem abaixo: 


No componente gerado tem-se um botão de ações que traz para utilização as duas ações configuradas para a entidade Parceiro: 


Na edição do componente Tabela temos a marcação "Permite seleção de múltiplas linhas?" que quando selecionada, faz com que no componente gerado, possa ser selecionado várias linhas da tabela, e ao pressionar a tecla "Ctrl" no teclado, você poderá selecionar as linhas de sua preferência pelo clique do mouse. 

Ao acionar a marcação "Utilizar a nova versão da grade" são disponibilizados novos recursos na grade do componente. Inicialmente, o botão "Configuração da Grade" e o seu pop-up são exibidos em um novo formato : 


Além disso, é disponibilizado o acesso ao "Menu da Grade" que propicia uma maior agilidade e conforto na visualização e pesquisa das informações contidas na grade. 


Todas as informações a respeito das funcionalidades contidas no Menu da Grade podem ser acessadas através da opção "Iniciar Tour" . 

Na utilização do componente Tabela , ao definir um campo como "Farol" na criação de sua expressão, configura-se para que seu retorno seja uma cor, isso fará com que as análises realizadas no dashboard sejam efetuadas com rapidez e proporcionem melhor entendimento dos resultados. Por meio da aba Expressão na configuração deste recurso, pode-se optar por um farol grande "Farol(G)" ou farol "Farol(P)" : 


Observe um exemplo de configuração de retorno para o campo: 

```
SELECT 

CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#86C154' ELSE '#C3C3C3' END AS FAROL, 
CASE WHEN Financeiro.VLRDESDOB < 100 THEN 'RED' ELSE 'GREEN' END AS FAROL2, 
Financeiro.NUFIN, 
Financeiro.VLRDESDOB, 
CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FF0000' ELSE '' END AS FGCOLOR, 
CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FFFF00' ELSE '' END AS BKCOLOR 

FROM 

TGFFIN Financeiro 
```

Observe o exemplo de um Componente que contêm um campo onde utilizou-se o tipo "Farol" : 


Na utilização dos componentes "Tabela" e "Tabela Dinâmica" (apresentada no tópico abaixo), quando há geração de dados, o título de cada coluna terá a possibilidade de filtragem e/ou ordenação das informações da tabela, e para sua configuração você deve apenas posicionar o mouse sobre a coluna que é desejável empregar para filtro/ordenação; será apresentado o botão , que ao ser acionado, exibirá a seguintes opções: 

- Ordenar crescente; 

- Ordenar decrescente; 

- Remover ordenação; 

- Filtrar; 

- Remover filtro. 

Observe a referida opção em uma tabela construída para exemplificação: 


Na utilização deste componente, tendo-se a tabela gerada, pode-se caso necessário, "Copiar" as informações de uma célula ou de uma linha para algum outro documento desejado; pode-se fazê-lo selecionado o trecho a ser copiado com o mouse, e pressionando as teclas "Ctrl + C" no teclado, ou mesmo pela opção do botão direito do mouse. 

Relacionada à apresentação dos dados na grade tem-se a configuração decorrente do parâmetro "Limite de linhas nas grades do dashboard - LIMITLINHASDASH" ; informa-se nesta parametrização, a quantidade máxima de linhas a serem apresentadas quando na geração do gadget. 

Ao realizar a geração do gadget através do ícone localizado no canto superior direito da tela, pode-se realizar a exportação de todos os dados gerados pelo componente em questão, independente do limite de linhas definido no parâmetro de chave LIMITLINHASDASH ; a quantidade de linhas estabelecidas neste parâmetro, serão exibidas no ícone. Este é um comportamento disponível apenas para gadget's do tipo Tabela . É importante mencionar que este ícone será apresentado, apenas se o parâmetro citado for configurado com algum valor diferente e maior que "0" (zero). 

Aba BIA 

As informações pertinentes a esta aba podem ser acessadas no link B.I.A - Business Intelligence Analyst . 


[voltar ao topo] 

Alterando seletivamente as cores das linhas em componentes do tipo Tabela 

É possível que o usuário customize sua tabela com cores, podendo assim criar uma interface mais gerencial. Para isso, a expressão SQL (query) do componente tipo Tabela deve retornar duas novas colunas: BKCOLOR, e FGCOLOR. O conteúdo destas colunas são valores hexadecimais, os quais correspondem ao código da cor desejada. A coluna BKCOLOR corresponde a cor do fundo da linha na tabela. Já a coluna FGCOLOR faz referência à cor das letras do texto. 

Exemplo: 

```
SELECT 

Financeiro.NUFIN, 
Financeiro.VLRDESDOB, 
Financeiro.DHBAIXA, 
Financeiro.CODPARC, 
CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FF0000' ELSE '' END AS FGCOLOR, 
CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FFFF00' ELSE '' END AS BKCOLOR 

FROM 

TGFFIN Financeiro 
```

Na edição do componente aciona-se o botão "Editar" presente na grade "Expressão" : 


Será aberta a tela para edição da consulta/expressão: 


Criando uma Formatação Condicional por célula em componentes do tipo Tabela 

O recurso de "Formatação Condicional" está localizado na extremidade direita da grade "Expressão" , este método possibilita que o usuário crie a definição de uma ou mais Regras de formatação, sendo que quando a regra for verdadeira será aplicada na célula respectiva ao campo selecionado. Pode-se personalizar a cor de fundo, o estilo da fonte entre negrito e/ou itálico de células especificas. A referida formatação só está disponível para o componente "Tabela" , nos campos do tipo "Inteiro" , "Moeda" , "Decimal" , "Data" e "Data e Hora" . Ao clicar no recurso será aberto um pop-up para edição da formatação condicional: 


Primeiramente, neste pop-up deve-se selecionar no campo Tipo , o tipo de layout a ser utilizado no assistente; tem-se as opções Formatação ou Escala de Cores ; a primeira delas permite a adição e edição de todas as demais regras; já a segunda, é exclusiva para uso de escala de cores. 

Tratando sobre o tipo "Escala de Cores" , estas podem ser do estilo Bicolor ou Tricolor , ou seja: 

- Bicolor : Determina-se duas colorações, bem como, duas parametrizações possíveis e correspondentes às cores; trabalha-se com pontos Mínimos e Máximos de modo que estes podem ser do tipo Menor valor , Valor e Percentil , e Maior valor , Valor e Percentil , respectivamente. 

Na escala de cores Bicolor, o ponto mínimo não pode ter valor maior do que o máximo se os dois forem do mesmo tipo (percentual ou valor). 

- Tricolor : Neste estilo de escala, determina-se três parametrizações e suas respectivas colorações; além dos pontos Mínimos e Máximos (que podem ser do tipo Menor valor , Valor e Percentil , e Maior valor , Valor e Percentil , respectivamente), define-se também o ponto Médio e sua correspondente coloração; um ponto Médio pode ser apenas do tipo Valor ou Percentil . 

Na escala de cores Tricolor, o ponto mínimo não pode ter valor maior que o médio se os dois forem do mesmo tipo, além disso, o ponto médio não pode ser maior que o máximo seguindo a mesma regra. 

Importante: não são permitidos valores menores que "0" (zero) e maiores que "100" (cem) no campo Valor se o tipo do ponto for Percentil . 


Definindo-se o Tipo como "Formatação" , tem-se as seguintes possibilidades de Regra : 

- Maior (>): O valor informado for maior que o resultado obtido na consulta; 

- Maior igual (>=): O valor informado for maior ou igual ao resultado obtido na consulta; 

- Menor (<): O valor informado for menor que o resultado obtido na consulta; 

- Menor igual (<=): O valor informado for menor ou igual ao resultado obtido na consulta; 

- Igual (=): O valor informado for igual ao resultado obtido na consulta; 

- Diferente (<>): O valor informado for diferente do resultado obtido na consulta; 

- Entre (Between): Os valores informados estiverem entre o resultado obtido na consulta; 

- Não entre (not Between): Os valores informados não estiverem entre o resultado obtido na consulta; 

- Vazia (NULL): Quando não houver valor no resultado obtido na consulta; 

- Não vazia (NOT NULL): Quando houver valor no resultado obtido na consulta. 

- Fórmula Personalizada: Esse tipo de formatação permite a criação e aplicação de uma fórmula personalizada em uma célula especifica, com base no valor de outros campos. A referida fórmula só pode utilizar os campos do mesmo componente de tabela em questão, sendo possível a utilização de todos os outros tipos de regras na mesma fórmula, como por exemplo 'CODCR>=100'. 

Ícone: Esta opção é composta por uma listagem de ícones a serem apresentados juntamente com a regra de formatação condicional; estes ícones tem como objetivo salientar as divergências que podem ocorrer nos resultados, bem como aprimorar a apuração dos mesmos, em casos de grandes volumes de informação. 

Mostrar somente ícone: Esta marcação se realizada, o texto correspondente ao campo será ocultado e apenas o ícone será exibido. Por padrão, esta marcação não é apresentada assinalada. 


Observação: caso já exista uma regra do tipo Escala de Cores não será permitido incluir outras regras de qualquer tipo. Além disso, várias regras do tipo Formatação podem ser adicionadas em um mesmo campo, porém, se ao menos uma for adicionada, a opção de Escala de Cores ficará indisponível. 

Os botões apresentados para utilização, possuem as seguintes funcionalidades: 

Este botão exibe alguns exemplos de expressão. 

Através deste botão, será adicionada a variável que foi selecionada. 

Por este botão, pode-se selecionar a variável desejada. 

A célula específica será exibida no modo Negrito . 

A célula específica será exibida no modo Itálico . 

Este botão permite a alteração da cor da fonte. 

Através deste botão, pode-se alterar a cor de fundo do texto. 

O campo "Valor" deverá ser usado como referência para que o sistema verifique se a regra configurada é verdadeira ou falsa. Apresentando-se de acordo com seu tipo, ou seja: 

Inteiro: Não deve possuir casas decimais. 

Moeda: Deve apresentar casas decimais. 

Data: Deve apresentar a máscara de data. 

Nota: nas regras "Célula vazia" e "Célula não vazia" , o campo Valor estará inativo. 

Observação: na criação de várias regras de formatação condicional para o mesmo campo, o sistema irá verificar a ordem de acordo com a grade, caso o sistema verifique que a primeira é verdadeira irá desconsiderar as demais. 

[voltar ao topo]

---

## Controles > Tabela Dinâmica

Este componente é uma poderosa ferramenta para análise das mais variadas informações. Este pode ser configurado e utilizado da mesma forma que a tabela acima mencionada. Para configurá-la, deve-se editar e inserir uma expressão contendo a query desejada. 

Pode-se arrastar os campos da consulta a fim de se criar a visualização padrão. Esta configuração é válida para a primeira vez que o componente for executado. Se for feita alguma alteração, o sistema irá manter o último estado da tabela dinâmica. 

Acionando a edição da Tabela Dinâmica, determina-se seu "Título" , o "Tamanho do texto" , além da forma de "Visualização padrão" dos campos que irão compor a tabela. Dentre as configurações pertinentes a forma de visualização padrão, tem-se a marcação "Sempre usar visualização padrão" que quando acionada estabelecerá que as últimas alterações (linhas e colunas) efetuadas pelo usuário não serão salvas e assim o gadget será iniciado com a visualização padrão que foi configurada. 

Simultaneamente a estas configurações, define-se os "Parâmetros/variáveis disponíveis" , bem como, a "Expressão" do componente (grades no lado direito da tela) 


Caso seja necessário, na utilização deste componente e a tabela dinâmica gerada, você poderá "Copiar" as informações de uma célula ou de uma linha para algum outro documento desejado, para executar essa ação pode-se selecionar o trecho a ser copiado com o mouse, e pressionar as teclas "Ctrl + C" no teclado, ou pela opção do botão direito do mouse. 

Nota: ao configurar-se um filtro utilizando-se de um dos campos, este ficará na cor "vermelha" para que identificar que ele está em uso como filtro. 

Importante: relacionada à apresentação dos dados na grade tem-se a configuração decorrente do parâmetro "Limite de linhas nas grades do dashboard - LIMITLINHASDASH" ; informa-se nesta parametrização, a quantidade máxima de linhas a serem apresentadas quando na geração do gadget. Vale salientar que esta configuração influencia apenas os componentes que geram grade (Tabela e Tabela Dinâmica); os demais não são afetados por este parâmetro. 

Observação: quando um parâmetro vazio for utilizado, os valores na tabela dinâmica serão exibidos em branco ou zerados, dependendo do formato do campo. Desta forma, a configuração realizada no layout não será perdida. 

Nota: ao realizar uma consulta a descrição desta não poderá conter caracteres, como ' . ', por exemplo. 

[voltar ao topo]

---

## Controles > Geomapa

Assim como os demais componentes, para início da utilização do Geomapa, basta arrastá-lo para o centro da tela, onde através do ícone dá-se início a sua configuração. 


Os dados inseridos na seção "Configurações do mapa" serão utilizados para centralizar o mapa quando carregado; não sendo informado nenhum pondo de referência, o mapa será centralizado no Brasil. Além disso, por meio do campo "Raio" é possível inserir um raio em KM ao redor do ponto central (inserido no campo "Endereço" ) . Deste modo, viabilizando a verificação da volumetria e o grau de proximidade, como por exemplo, de clientes que se encontrem próximos a um endereço informado. 

Na seção "Marcadores" tem-se a configuração das informações que irão representar os dados retornados pela expressão SQL. Assinalando-se a opção "Apenas marcar" , um pino vermelho será a representação de cada aspecto do analisado no mapa. Já a opção "Marcar com uma bolha" se refere à representatividade da marcação, ou seja, serão apresentadas bolhas no mapa com diferentes tamanhos e cores, onde quanto maior a bolha, maior a representatividade da marcação. 

Vale ressaltar que ao definir um evento de clique através do botão "Evento" , e juntamente definir detalhes para o marcador, o evento de clique é redirecionado para um link chamado "Mais detalhes" , dentro do balão de informações. 

Na última seção "Detalhe do marcador (opcional)" pode-se adicionar detalhes ao marcador. Realizando esta configuração, ao clicar- em um marcador será apresentada uma pequena janela contendo as informações definidas em cada campo de detalhe. No campo de Título, define-se um resumo da informação. Pode-se adicionar nesse campo, textos fixos em conjunto com variáveis de níveis, parâmetros de usuário e campos da expressão SQL. Já no campo de Texto, determina-se o restante da informação. A forma de utilizar é a mesma do campo de título, com a diferença que pode-se adicionar tag's HTML. 

Observação: no gadget Geomapa, visando a manutenção de sua performance são apresentados pelo sistema os primeiros 400 (quatrocentos) marcadores retornados na consulta por visualização. 


Observação: quando a query que realiza as buscas dos parâmetros que foram enviados posteriormente ao GEOMAPA possuir campos vazios ou valores nulos, a API do Maps não irá considerar o registro, mesmo que o campo com os valores nulos não estejam sendo utilizados, ou seja, para que a localização seja precisa, é necessário que os campos "Latitude" e "Longitude" dos Parceiros na aba Endereço do Cadastro de Parceiros , estejam preenchidos com seus respectivos valores. 

[voltar ao topo]

---

## Controles > HTML5

Para utilização deste componente, pode-se inicialmente seguir os seguintes passos: 

- Através das opções "Download Modelo Simples HTML5" ou "Download Modelo Completo HTML5" (botão Outras Opções...) realiza-se a baixa do modelo desejado; 

- Realiza-se a abertura do arquivo baixado, onde tem-se dois modelos no formato XML , correspondentes ao banco de dados da empresa, SqlServer ou Oracle ; deve-se abrir o arquivo XML correspondente ao seu banco de dados e copiar o seu conteúdo; 

- O conteúdo copiado deve ser colado no espaço apresentado com o acionamento do botão "XML" referente ao componente que está sendo criado; informa-se o Título adequado ao gadget, e a partir disso, o componente começa a possuir um formato definido; 

- Feito isso, por meio do botão "Upload do Pacote HTML" realiza-se o total carregamento do pacote inicialmente baixado. Finalizado o upload, será exibida a seguinte mensagem: 

"Pacote HTML5 atualizado com sucesso." 

Vale mencionar que os modelos disponibilizados pelas opções "Download Modelo Simples HTML5" e "Download Modelo Completo HTML5" são apenas embasamentos para utilização do componente HTML5. 


Da mesma forma que os demais componentes, para início da utilização do HTML5, basta arrastá-lo para o centro da tela, onde através do ícone dá-se início a sua configuração. 


Na seção "Configurar Componente HTML5" tem-se as seguintes informações: 

Ponto de Entrada: Neste campo especifica-se o nome completo (com extensão) do arquivo JSP a ser compilado. 

Logo à frente do campo Ponto de Entrada tem-se o botão , que ao ser acionado será exibido um pop-up contendo os arquivos .JSP e .HTML do pacote zip anexado ao gadget. 

No alto da aba, tem-se o link " Editando {Nome_Componente } [{Nome_Nível}] " , que ao ter o cursor sobre este label posicionado, será exibido um tooltip com o Id do componente em questão; clicando-se sobre o mesmo, este será copiado para a área de transferência. 

Importante: o Componente HTML5 pode receber query's nos formatos de parâmetros padrão, além de manter também o formato antigo. Nele pode-se inserir as consultas da query no formato padrão, como descrito nos exemplos abaixo: 

Exemplo 1: 

```
SELECT * FROM TGFPAR WHERE CODPARC = :CODPARC_PARAM ORDER BY CODPARC ASC 
```

Exemplo 2: 

```
SELECT CAB.CODPARC, CAB.NOMEPARC 

FROM TGFCAB CAB WHERE CODPARC IN 

(SELECT PAR.CORPARC 

FROM TGFPAR PAR INNER JOIN TGFCTT CTT ON (PAR.CODPARC = CTT.CODPARC) 

WHERE PAR.ATIVO IN (:P_ATIVOLIST) 

AND PAR.CODPARC IN (:P_CODPARCLIST) 

AND CTT.ATIVO IN (:P_ATIVOLIST)) 

AND (:P_DTNEG.INI IS NULL OR CAB.DTNEG >= :P_DTNEG.INI) 

AND (:P_DTNEG.FIN IS NULL OR CAB.DTNEG <= :P_DTNEG.FIN) 

AND (:P_SERIENOTA IS NULL OR CAB.SERIENOTA LIKE '%' || :P_SERIENOTA || '%') 
```

Observação: no caso do banco de dados em SQL Server deve-se alterar a última linha para: 

```
AND (:P_SERIENOTA IS NULL OR CAB.SERIENOTA LIKE '%' + :P_SERIENOTA + '%') 
```

[voltar ao topo]

---

## Controles > IReport

Este componente permite a exibição de relatórios formatados nos dashboards. 


Para utilização deste componente é necessário realizar a criação de um relatório na tela de Relatórios Formatados , adicionar no mesmo os arquivos do Jasper Reports (extensão JRXML) e apontar o seu código no componente que está sendo criado. 


Deste modo, será possível "Importar Parâmetros do Relatório" e abrir a tela de Relatórios Formatados já posicionada no relatório configurado. Ao importar os parâmetros do relatório, caso existam parâmetros com o mesmo nome estes não serão importados. 

Ao acionar a marcação "Ignorar paginação" os relatórios que possuem quebra de página serão apresentados em paginação contínua. 

Observação: alguns cuidados devem ser tomados ao configurar os parâmetros do componente, são eles: 

- Para utilizar os parâmetros do tipo Multi List no dashboard, deve-se configurar o relatório para receber o parâmetro como String . 

- Para usar os parâmetros do tipo Período , é necessário configurar dois parâmetros do tipo Data (Date ou Timestamp) no relatório com o mesmo nome, porém um com sufixo .ini e o outro com sufixo .fin . Vejamos um exemplo: 

No dashboard o parâmetro do tipo Período é nomeado como ENTRADA e no relatório são configurados dois parâmetros do tipo Timestamp nomeados como "ENTRADA.INI" e "ENTRADA.FIN". 

É possível também utilizar eventos de click no componente iReport, mas é necessário criá-los no editor do Jasper Report (iReport Design ou outro). As informações a cerca da criação destes eventos, podem ser acessadas por meio do tutorial Como criar eventos de click no IReport . 


[voltar ao topo]