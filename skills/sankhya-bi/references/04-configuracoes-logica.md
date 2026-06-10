## Parâmetros

No construtor de componentes pelo "Design" , o painel a direita da tela apresenta abas para que sejam informados os "Parâmetros" , "Configurações" , "Variáveis" e "Argumentos" ; estes dados serão manipulados no novo "gadget". Vejamos cada uma delas a seguir: 

Inicialmente, na aba "Parâmetros" informam-se os parâmetros que serão utilizados como filtros para o "gadget" na tela de visualização de Dashboard. 


Observação: na criação de uma consulta, o sistema realiza sua validação verificando se existem erros em sua estrutura ao clicar-se no botão "OK" . Caso exista algum erro, este será apresentado na tela, de modo a orientar o usuário para sua correção. 

Deve-se informar um "Id" único e uma "Descrição" para ele. Discriminar pelo campo "Requerido" se este será um parâmetro obrigatório ou não. E pelo campo "Salvar último valor" definir se o último parâmetro informado será ou não salvo. 

Já quando a marcação "Mostrar inativas" for habilitada será possível pesquisar registros inativos nos filtros de pesquisa dos dashboards. 

No campo "Tipo" , seleciona-se como será o "gadget". Tem-se as seguintes opções: 

- Entidade/Tabela; 

- Período; 

- Data; 

- Texto; 

- Data/Hora; 

- Número Inteiro; 

- Número Decimal; 

- Verdadeiro/Falso; 

- Single List; 

- Multi List. 


De acordo com o "Tipo" definido, abaixo dele serão apresentados campos que irão consumar o tipo determinado. Vejamos abaixo alguns exemplos: 

- Utilizando-se os tipos "Texto" , "Número Inteiro" e "Número Decimal" pode-se configurar o campo "Limite de caracteres" e estabelecer-se um limite para os caracteres a serem utilizados. 

- Na escolha dos tipos "Data" , "Data/Hora" ou "Período" , será habilitado para possível marcação, o campo "Considerar data atual?" ; ao realizá-la e construindo posteriormente um Dashboard, em sua abertura, o parâmetro será apresentado preenchido automaticamente com a data atual. 

Observações: se o tipo utilizado for Data o campo "Salvar último valor" não poderá ser marcado simultaneamente ao campo "Considerar data atual?" . Caso seja feita a utilização do tipo Período , os campos "Salvar último valor" e "Considerar data atual?" podem ser marcados em paralelo, porém a "data atual" será apresentada apenas para o período final. 

- O campo "Range" é empregado para os tipos "Número Inteiro" e "Número Decimal" , onde pode-se estabelecer que sejam informados os valores dentro do intervalo determinado. 

- Os tipos "Single List" e "Multi List" , devem ser combinados com o campo "Tipo de dado" , que apresenta as opções "Texto" , "SQL" ou "Entidade/Campo" . Utilizando-se o tipo de dado "SQL" por exemplo, pode-se realizar a criação de uma lista por meio de uma query personalizada; no tipo de dado "Texto" , a criação de uma lista por meio do fornecimento manual de valores, e assim sucessivamente. 

#### Utilização de Parâmetros 

Para utilizar um parâmetro criado, você deve se referir a ele com :ID_do_parâmetro . Sendo que, ":" é o aviso para buscar o conteúdo do parâmetro identificado pelo ID. Vejamos o exemplo a seguir: 

Suponha que criamos um parâmetro (P_PARCEIRO) para escolher de qual parceiro queremos ver as OS de 01/01/2021 em diante. Para se referir a esse parâmetro numa consulta SQL, utilizamos: 

```
SELECT * 
FROM TCSOSE 
WHERE CODPARC IN :P_PARCEIRO 
AND DHCHAMADA >= '01/01/2021' 
ORDER BY NUMOS 
```

Quando utilizamos o " : " , o Construtor de Componentes de BI, traduz isso da seguinte forma "(“, conteúdo do parâmetro, ")" . Suponha que o valor 2135 esteja no P_PARCEIRO . Logo, a tradução da query SQL ficaria: 

```
SELECT * 
FROM TCSOSE 
WHERE CODPARC IN IN (2135) 
AND DHCHAMADA >= '01/01/2021' 
ORDER BY NUMOS 
```

Se o tipo do parâmetro for texto, o tradutor acrescentará um apóstrofo (‘) antes e depois do conteúdo. Se o parâmetro contiver a palavra SANKHYA, a tradução seria (‘SANKHYA’) . 

Existem algumas variantes do ":" , que são: 


#### Parâmetros Internos 

Existem parâmetros internos do sistema que podem ser utilizados nas consultas e expressões. São eles: 

CODUSU_LOG = cód. usuário logado 

CODGRU_LOG = cód. grupo usuário logado 

CODPARC_B2B = cód. parceiro B2B 

CODVEN_LOG = cód. vendedor logado 

Todos estes parâmetros são do tipo Número Inteiro . 

Nota: o tipo "Entidade/Tabela" irá gerar nos filtros do Dashboard campos com opção de pesquisa, como mostra a imagem a seguir: 

É possível definir um tempo de atualização automática do gadget. 

Nota: ao utilizar o parâmetro Multi list , o tipo de expressão for SQL , e este retornar um resultado com mais de mil valores, deve-se editar o Tipo no Editar Consulta/Expressão e adicionar o delimitador "/*Incolletion*/" . Desta forma, observa-se o exemplo em que antes da inclusão do delimitador tem-se a expressão: 

```
SELECT CODPARC, NOMEPARC, TIPPESSOA, CODCID FROM TGFPAR WHERE CODCID 
in :P_CODCID 
```

Depois da edição deste, nota-se: 

```
SELECT CODPARC, NOMEPARC, TIPPESSOA, CODCID FROM TGFPAR WHERE /*inCollection*/ 
CODCID in :P_CODCID/*inCollection*/ 

```

Importante: quando o parâmetro retornar um resultado com mais de mil valores, a inserção do delimitador será obrigatória. 

[voltar ao topo]

---

## Configurações

Nesta aba serão informadas as configurações mais rígidas do componente; uma vez que estas sejam salvas gadget, sempre que este for executado estas configurações serão apresentadas, não sendo necessário informá-las novamente. 


Os campos desta aba são similares aos apresentados na aba "Parâmetros" , diferenciando-se pela possibilidade de informar um "Valor Padrão" . 

[voltar ao topo]

---

## Variáveis

Aqui são informadas as Variáveis locais que serão utilizadas no gadget. As variáveis poderão ser de dois tipos, "SQL" ou "Java BeanShell" . 

#### SQL 

Esta opção conta com o "Assistente" de query do sistema, que visa auxiliar aos usuários na construção da query. 


#### Assistente 

Através da uma pesquisa e seleção, o usuário compõe a query nesta aba, como pode-se visualizar no exemplo abaixo. Inicialmente, seleciona-se a "Tabela" : 


Ao selecionar uma Tabela, todas as outras tabelas ligadas a esta tabela principal serão apresentadas no painel. Observe a imagem a seguir: 


Depois de selecionada a Tabela, os "Campos" pertencentes à esta tabela serão apresentados no painel ao lado. Podem-se selecionar todos os campos da tabela para compor a query ou apenas os desejados; além disso, pode-se depois de selecionar os campos, criar "Filtros" específicos para alguns deles. 


O "Parâmetro" utilizado na aba Filtros pode ser associado, pelo nome, a outro parâmetro já criado pelo usuário, ou seja, bastará informar o nome de um parâmetro criado anteriormente para que o sistema faça a ligação entre eles. Se o usuário desejar colocar vários gadgets em um mesmo Dashboard e todos eles precisarem de um mesmo "Parâmetro" , por exemplo, "CODUSU" , é interessante colocar todos com o mesmo nome, pois quando o Dashboard for renderizado, será renderizado apenas um parâmetro que será utilizado em todas os gadgets. 

Na criação de uma query (consulta SQL) cujo objetivo final é a geração de dados para montagem do Gadget, pode-se informar o parâmetro variável da seguinte maneira: 

```
:#PARAMETRO 
```

Esta maneira é a mais recomendada, por ela realizar o auto preenchimento das ' ' (aspas) corretas de acordo com o tipo do valor do parâmetro. 

Pode-se também utilizar ':@' para representar um parâmetro, onde este possui também as seguintes funcionalidades: 

- Autopreenchimento correto do SQL quando os valores forem NULOS; 

- Autopreenchimento das aspas corretas quando os valores forem DATA; 

Vale salientar que na utilização desta forma quando se trata de string, deve-se informar ' ' (aspas) antes e depois do parametro - ':@PARAMETRO' . 

A utilização do :@ ou :# visa melhorar a performance da query, pois elas realizam a substituição direta dos valores na query. Para utilizar a nova forma de parâmetro :# , vejamos o seguinte exemplo: 

```
SELECT * FROM TSICID WHERE DTALTER > :#DTALTER 
```

As outras formas de criação da query, com ":" ou ":@" , funcionam da seguinte maneira: 

```
SELECT * FROM TSICID WHERE DTALTER > :DTALTER 

SELECT * FROM TSICID WHERE NOMECID = ':@DTALTER ' 
```

#### Avançado 


Pode-se construir a query diretamente nesta aba sem nenhuma assistência ou mesmo visualizá-la já montada com a ajuda do assistente. 

Importante: caso o usuário informe uma query diretamente nesta aba, o assistente para criação de query será desativado e o usuário ficará por sua conta. Neste caso, o sistema irá reconhecer a query informada nesta aba e todas as manipulações necessárias nesta query serão feitas sob responsabilidade exclusiva do usuário, que fará os ajustes diretamente na query. Ou seja, o sistema não mais auxiliará o usuário na edição da query, contudo o funcionamento permanecerá o mesmo. 

Na configuração de expressão dos componentes do dashboard, pode-se utilizar variáveis como parâmetros da query configurada. Vejamos abaixo um exemplo da utilização da variável CODEMP: 

```
SELECT CODUSU, NOMEUSU, CODEMP FROM TSIUSU WHERE CODEMP = :COD OR CODEMP = 
:CODEMP 
```

#### Resultado 

Esta aba possibilita ao usuário testar a query criada antes de utilizá-la no novo gadget. Como se trata apenas de um teste, o resultado é limitado a 20 linhas para que não haja sobrecarga no banco de dados. 


#### Java BeanShell 


O "Java BenShell" representa outra forma de criação de uma expressão variável, que constitui um trecho de código Java mais simplificado , digitado diretamente nesta área. Esta forma de criação de variáveis dispensa o auxílio do assistente. 

Trouxemos dois exemplos: 

1. 

```
void addColumn(String name, String type, String description){ 
ui = uiElement(); 
meta = ui.getChild("metadata"); 
if( meta == null){ 
meta = new org.jdom.Element("metadata"); 
ui.addContent( meta ); 
} 

f = new org.jdom.Element("field"); 
f.setAttribute("name",name); 
f.setAttribute("label",description); 
f.setAttribute("type",type); 
f.setAttribute("visible","true"); 
f.setAttribute("useFooter","false"); 

meta.addContent(f); 
} 

void initMetadata(){ 
addColumn("CODPROJ","I","Cód.Projeto"); 
addColumn("NOMEPROJ","S","Nome Prj"); 
addColumn("TAMANHO","I","Tam"); 
addColumn("KANBAN","S","Kanban"); 
addColumn("DHENTRADA","T","Dh.Entrada"); 
addColumn("DHENTREGA","T","Dh.Entrega"); 
addColumn("DIAS","I","Dias"); 
addColumn("ANALISTA","S","Analista"); 
addColumn("DHINIANALISE","T","Ini.Análise"); 
addColumn("DHFIMANALISE","T","Fim.Análise"); 
addColumn("DEV","S","Dev"); 
addColumn("DHINIDEV","T","Ini.Dev"); 
addColumn("DHFIMDEV","T","Fim.Dev"); 
addColumn("QA","S","QA"); 
addColumn("DHINIQA","T","Ini.QA"); 
addColumn("DHFIMQA","T","Fim.QA"); 
addColumn("VALIDADOR","S","Validação"); 
addColumn("DHINIVAL","T","Ini.Val"); 
addColumn("DHFIMVAL","T","Fim.Val"); 
} 

initMetadata(); 

return var("_vprojects"); 
```

2. 

```
import java.math.BigDecimal; 

int qtdSaidas = ((BigDecimal) var("QTD_SAIDAS")).intValue(); 

Collection linhas = new ArrayList(); 
linhas.add(new Object[]{ "Qtde. Saídas", qtdSaidas, qtdSaidas }); 
return linhas; 
```

[voltar ao topo]

---

## Argumentos

Os Argumentos são compostos por um "Id" e um "Tipo" ; estes são parâmetros de entrada de um nível para outro, ou seja, parâmetros de passagem. Deste modo, pode-se criar um gadget que no primeiro nível exiba, por exemplo, "Vendas por Vendedor", sendo que ao dar um duplo clique sobre algum vendedor apresentado no gráfico, sejam apresentadas as vendas deste vendedor em outra grade, logo, o código deste vendedor que permitiu passar do primeiro pro segundo nível seria um exemplo de "Argumento" . 

Ao contrário das demais abas da opção "Design" que são definidas por "gadgets", os Argumentos são definidos por "nível" , ou seja, o Argumento será válido apenas para o nível que foi definido. 

O botão "Nível" permite ao usuário tanto editar o nome do nível , quanto navegar pelos diversos níveis de um gadget. 


Os botões permitem a inserção e exclusão dos níveis, respectivamente. 

Podemos ainda, lançar o Argumento na tela Portal de Importação de XML no registro que você desejar. Para tal ação, selecione o argumento NUARQUIVO na tela Construtor de Componentes de BI e, ao clicar na linha desejada o Dahsboard será direcionado especificamente ao registro desejado. 

[voltar ao topo]

---

## Quadrante Expressão

No quadrante Expressão , são realizadas definições essenciais para a geração dos dados no Dashboard. Inicialmente determina-se o Tipo a ser trabalhado; as explicações a respeito deste aspecto, bem como dados a respeito do assistente de montagem de query aberto com o acionamento do botão "Editar" , podem ser visualizadas por meio do link Variáveis . 

Ao salvar a expressão o sistema irá reconhecer os campos da query ou código que aquela expressão retorna e informar todos eles na grade, permitindo a redefinição dos "Tipos" ou edição da "Descrição" . 


Nota: o Controle do tipo "Valor" suporta HTML do tipo simplificado (tamanho, cor, fonte e imagem). 

Em seguida tem-se os seguintes botões: 

Assistente de edição de campos calculados - Será aberto o pop-up denominado "Editar Campos Calculados" , onde tem-se a possibilidade de configurar-se cálculos personalizados com valores de outros campos, além de concatenar informações como o nome de uma cidade e seu respectivo estado; 

Assistente de edição de máscara - Ao utilizar análises do tipo Linhas , Barras e Colunas , poderemos utilizar máscaras para formatação dos valores do eixos. O campo para informar a máscara estará disponível para eixos do tipo Valor . A máscara pode ser digitada diretamente no campo, ou pode ser editada clicando-se neste botão, onde será aberto o pop-up "Editar Máscara" ; 

Formatação condicional - O recurso de Formatação Condicional possibilita a definição de uma ou mais Regras de formatação, sendo que quando a regra for verdadeira será aplicada na célula respectiva ao campo selecionado. Pode-se personalizar a cor de fundo, o estilo da fonte entre negrito e/ou itálico de células específicas. A referida formatação só está disponível para o componente "Tabela" , nos campos do tipo "Inteiro" , "Moeda" , "Decimal" , "Data" e "Data e Hora" . Ao clicar no recurso será aberto o pop-up "Editar Formatação Condicional" para ajustes na formatação condicional. 

Assistente de Formatação e Agregação - Ao editar e/ou inserir uma Expressão SQL, nos campos do tipo Inteiro , Decimal ou Moeda , pode-se efetuar a configuração de agregação de valores através da coluna "Agregador" , que irá apresentar tais informações no rodapé da grade do componente gerado. A coluna Agregador , é utilizada em substituição a coluna Totalizar . Pode-se escolher as seguintes funções de agregação: 

- Maior; 

- Menor; 

- Média; 

- Somar; 

- Personalizada. 

Optando-se pela opção Personalizada , pode-se criar várias particularidades de agregadores para a coluna selecionada. Por meio desta opção, será habilitado o ícone ? , que ao ser acionado, será aberto o pop-up "Editar Agregadores Personalizados" , onde será possível informar uma expressão e utilizar valores dos outros campos com funções de agregação dos cálculos retornados. 

Observação: em componentes de Tabela , na utilização de campos do tipo "Hora" também pode-se empregar o uso de funções de agregação para os mesmos (somar, média, mínimo, máximo, personalizado). Esta configuração visa auxiliar nas análises em que tem-se tempo gasto, horas produtivas, orçamento de horas, entre outras possibilidades. 

Importante: a Formatação de Agregação Personalizada não permite a realização de cálculos matemáticos que fujam das possibilidades disponibilizadas pela Fórmula Personalizada ; pode-se trabalhar apenas com a utilização de cálculos com base nos campos pertencentes à consulta. No pop-up Editar Agregadores Personalizados , nas fórmulas utilizadas na expressão, somente são aceitas as variáveis existentes na Seleção de Variáveis ; pode-se configurar quantos agregadores forem necessários. O campo Título é utilizado para informar-se uma descrição para o resultado da fórmula do agregador personalizado. O resultado da agregação configurada, é sempre apresentado no Rodapé da Grade . Vejamos um exemplo: 

```
SUM(VALOR_VENDA) / SUM(VALOR_CUSTO) 
```

[voltar ao topo]