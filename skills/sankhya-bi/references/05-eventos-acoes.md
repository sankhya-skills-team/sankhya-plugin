## Eventos - Gráficos

Nos gráficos, os eventos são definidos por "Séries" , cada uma das séries apresentará o botão "Evento" , que acionará a tela de edição de eventos, através da qual o usuário definirá o comportamento de cada componente quando este for acionado no Dashboard, como por exemplo, quando sob a ação de um duplo clique. 


Ao acionar o botão "Evento" é aberta a tela de edição de eventos que conta com duas possibilidades, "Abrir um novo nível" ou "Lançar uma tela do sistema" . 

Optando por "Abrir um novo nível" , serão apresentados os níveis já criados para o componente. Selecionando-se um destes níveis, se houver um "Argumento" vinculado a ele, este também será apresentado e o usuário associará a variável ou campo ao argumento, pela coluna "Valor" . 

Sendo que, se tratando de um gadget com por exemplo 3 (três) níveis, o terceiro nível já herda todas as variáveis que foram passadas como argumento do primeiro para o segundo nível. Deste modo, torna-se mais adequado a utilização das variáveis herdadas evitando assim a criação de novas variáveis com os mesmos valores. 

Por meio da opção "Lançar uma tela do sistema" , configura-se o componente para que este abra a partir do Dashboard, qualquer tela ou Dashboard do Sankhya Om através de um duplo clique. Isto poderá ser feito tanto em valores, quanto em uma linha na grade, uma coluna ou barra ou ainda um campo, a configuração é livre. 


No editor de eventos seleciona-se a tela ou Dashboard que se deseja vincular ao componente. A "PK" da tabela principal da tela selecionada será apresentada no "Argumento" , permitindo ao usuário associar a esta através do "Valor" , uma variável local do "gadget"; deste modo, a tela será aberta posicionada no registro que está sendo analisado. 

Observações: 

- "PK" é o mesmo que chave primária. Resumidamente chave primária é o conjunto de campos da tabela que identificam unicamente uma linha, ou seja, nenhuma outra linha da tabela terá valores repetidos para esta coluna. Um exemplo, é o cadastro de parceiros que terá como chave primária o campo Código do Parceiro, pois não existirão outros iguais. 

- No momento da visualização do Dashboard, uma tela só será efetivamente aberta, se o usuário logado possuir pelo menos permissão de visualização para a tela. 

Na Aba "Atualizar detalhes" é possível configurar para que o controle corrente force a atualização de um outro controle vinculado a ele. 


Nesta aba serão listados os controles que estão no mesmo nível do controle selecionado. Para fazer o vínculo, basta marcar um ou mais componentes que serão atualizados. Existe a possibilidade de passar grandezas do componente mestre como argumentos para a atualização. Os argumentos são informados na grade localizada logo abaixo da lista de componentes. Nesse caso, esses argumentos serão inseridos diretamente no ambiente dos componentes selecionados, podendo esses argumentos serem utilizados na query/expressão do componente detalhe. Vejamos um exemplo: 

Suponhamos um componente com dois elementos em um nível, uma tabela de parceiros e um gráfico em pizza agrupado por segmento de atuação. Ao clicar em uma das "fatias da pizza", a tabela é atualizada, buscando os parceiros correspondentes àquele segmento em que o clique aconteceu. Neste exemplo, o componente mestre é o Gráfico de Pizza, e é nele que o Evento deve ser configurado, marcando-se na aba "Atualizar detalhes" a opção correspondente a tabela e passando os argumentos necessários para atualização do componente detalhe; neste caso esse argumento seria o "Segmento de atuação". 

[voltar ao topo]

---

## Eventos - Controles/Tabela

Nos componentes do tipo "Tabela" o evento é único e será acionado também pelo botão "Evento" . Neste caso, o evento será definido de acordo com a linha da tabela que será acionada. 


[voltar ao topo]

---

## Eventos - Controles/Valor

No caso dos componentes do tipo "Valor" pontual, o evento será reenderizado como um "link" . 


[voltar ao topo]

---

## Pré-Visualização

Outro recurso que favorece a criação do gadget é o botão "Pré-visualizar" localizado no canto direito da barra de ferramentas e ao lado do botão "Outras Opções" no topo da tela, tanto para a opção "Design" quanto para opção "XML" . 


Este recurso abrirá o gadget assim como em um Dashboard, possibilitando a visualização do resultado final, permitindo uma noção de como funcionará o Dashboard. Através do botão "Editar" localizado no canto superior direito da tela, o usuário que tiver acesso para alterações nesta tela, poderá retornar para edição do Dashboard. Caso o usuário não tenha acesso para alteração nesta tela, este botão não estará disponível. 


Deste modo, o gadget irá rodar sozinho em um Dashboard de visualização, onde pode-se analisar se ele realmente está retornando o resultado esperado. 

No ambiente móbile os gráficos são apresentados maximizados automaticamente permitindo a navegação entre gráficos, assim como na versão desktop. 

[voltar ao topo]

---

## Impressão/Exportação

Componentes do tipo "Gráfico" permitem sua impressão através do ícone em forma de engrenagem, onde tem-se a opção "Imprimir Gráfico" : 


Componentes do tipo "Tabela" possibilitam tanto a exportação como "PDF" quanto em "Planilha Excel" ou "Visualizar em Cubo" . 


Nas tabelas dos Componentes de BI que forem criados, é disponibilizado um botão para apresentação dos dados estatísticos referentes aos campos numéricos exibidos na grade. Para maiores detalhes sobre esta funcionalidade, clique no link Estatísticas . 

Observações: 

1. No editor de dashboard, para que expressões sejam interpretadas como HTML, é necessário que as infomações estejam em um blocoo CDATA no XML, como pode-se notar no exemplo abaixo: 

```
<title><![CDATA[Mês negociado<br><br>Junho</br></br>]]></title> 
```

2. Nos editores de fonte do Dashboard agora é possível utilizar o CTRL+Z para desfazer uma edição no texto. 

3. Ao visualizar o dashboard, no menu lateral de filtros agora é possível aplicar um filtro pressionando a tecla "Enter" no teclado. 

4. Na edição do XML principal e na configuração das query's dos componentes, pode-se utilizar o botão scroll do mouse (botão de rolagem localizado entre os botões direito e esquerdo), de modo a facilitar a navegação. 

[voltar ao topo]

---

## Ações nos Componentes de BI

Ao realizar a construção de um componente de BI, é possível utilizar as ações vinculadas a uma entidade nos componentes de grid's do construtor e lançar ações através da visualização do dashboard; em poucas palavras, pode-se executar uma ação partindo de um Componente de BI. Para isso realiza-se as seguintes configurações: 

- Ao cadastrar um novo componente de BI, preenche-se os campos "Título" , "Categoria" , "Ativo" e "Descrição" . Neste caso, o componente deve ser do tipo "Tabela" . 

- Depois de selecionado o tipo Tabela, clica-se no botão "Editar" , onde define-se um "Título" e uma entidade a ser trabalhada. 

- Clicando-se na aba "Expressão" presente no lado direito da tela, e em seguida no botão "Editar" , tem-se a tela "Editar Consulta/Expressão" , onde na aba "Avançado" informa-se uma query que irá proporcionar um resultado para alimentar a tabela. Além disso nesta aba, pode-se pesquisar dentro do editor de consulta/expressão, por trechos do texto existentes na consulta/expressão criada; para isso, informa-se a palavra desejada no campo de busca localizado na parte superior da tela. Sendo feita alguma modificação, o sistema irá apresentar um pequeno lembrete para possível salvamento das alterações realizadas. 

- Na tela "Configurações > Avançado > Dicionário de Dados" , pesquisando pelo "Nome da Instância" , identifica-se a entidade a ser trabalhada e na aba "Ações" , efetua-se a inclusão de uma ação que pode ser do tipo "Rotina no Banco de Dados" , "Script (JavaScript)" , "Lançador" ou "Rotina Java" . 

Ao visualizar o Componente de BI criado através do botão , pode-se visualizar a ação criada. 

Observação: na configuração de ações pelo usuário, tem-se a opção de utilizar o parâmetro "Ordenar ações por ordem alfabética? - ORDENARACOES" que quando ativado, ordena a visualização das ações por ele criadas em seu correspondente botão de ações de forma alfabética. 

Importante: ao utilizar a ação de uma entidade vinculada a tabela, os dados que podem ser utilizados são os que estão presentes na entidade relacionada. Não é possível utilizar em um botão de ação, um campo que não esteja nessa entidade relacionada. 

[voltar ao topo]

---

## Central de Certificações para Dashboards

Para acessar as informações sobre o processo de inserção das regras pertinentes à Central de Certificações na construção do Dasboard, acesse Restrição por Dashboard . 

[voltar ao topo]

---

## Botão Outras Opções

A opção "Dashboards que usam esse componente" quando acionada, permite visualizar a listagem de todos os dashboards que utilizam determinado componente de BI. 


Ao efetuar um duplo clique em algum item da lista, será aberta a tela de "Construtor de Dashboard" posicionando a navegação de registro, no dashboard correspondente ao item clicado. 

Nota: caso seja necessário, é possível realizar a construção de um componente de BI para ser executado a partir da tela "Configurações > Consulta > Ficha de Parceiros" considerando a marcação "Exibir por Matriz ou Convênio" . Na criação do Componente de BI, pode ser utilizado o parâmetro EXIBIRMATRIZ correspondente a marcação mencionada na tela Ficha de Parceiros. 

Através da opção "Download Modelo JavaScript Simples HTML5" , pode-se baixar o modelo de documento html que possui a estrutura de referência que permite a execução de queries em tempo de execução via JavaScript. Os seguintes pontos devem ser observados: 

- Este modelo está configurado para receber parâmetros do tipo Data/Hora , Data , MultiList:Text , Periodo , Entidade/Tabela , Texto e SingleList:Text . 

- Para o parâmetro do tipo MultiList:Text , se nenhum item é selecionado são retornados todos os registros, então para utilização fixa na query este parâmetro deve ser configurado como obrigatório. 

- A consulta pode usar tanto um parâmetro quanto uma combinação de vários parâmetros. 

[voltar ao topo] 
Esse artigo foi útil? Sim Não Usuários que acharam isso útil: 21 de 32 
## 


Escreva seu comentário aqui 

Por favor, entre para comentar. 

Confira os outros artigos 
MGEScript Configurando Ações Personalizadas Módulo Java O modelo não pertence ao MGE O usuário ZERO não pode liberar ou negar limites