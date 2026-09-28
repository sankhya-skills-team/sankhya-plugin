> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/ (snapshot 2026-09-28)

# Sankhya-bff

Essa documentação se destina a exemplificar cenários de implementação e uso das APIs JAVA, disponibilizadas pela biblioteca `sankhya-bff`.

## IDataUnitInterceptor

Define interceptadores para ações relacionadas a um `DataUnit`. É implementado quando existe a necessidade de manipulação dos metadados nativos de uma entidade.

Como exemplos de casos de uso, podemos citar:

  * A necessidade de mapear campos de entidades filhas.
  * A possibilidade de remover dependências de campos FKs.
  * Alteração de propriedades de campos diretamente no `interceptFieldMetadata` como: `label`, `defaultvalue`, `required`, `visible`, entre outras.

## IDataUnitCrudListener

Define interceptadores para operações _CRUD_ em um `DataUnit`.

É implementado quando se precisa adicionar comportamentos adicionais diretamente nos dados na entrada ou saída do banco de dados. Também pode ser usado como validador ou para preenchimento de comportamentos automáticos.

Dica

Um exemplo de uso seria a implementação de critério de busca de central de certificação, onde um WHERE é adicionado como filtro automático e não pode ser visto via tela.

## ICustomFilterBarResolver

Interface para resolver e manipular configurações da `FilterBar`.

Usado quando é necessário adicionar alguma configuração adicional para resolver os filtros ou para busca de configurações por usuários.

## IDataExporterInterceptor

Interface para interceptar e customizar o comportamento do exportador de dados.

Implementado no caso de necessidade de adicionar colunas requeridas no exportador, bem como expressões de agrupamento de soma.

## ITotalsResolver

Interface que permite a implementação de resolvers específicos para o componente de Totalizador.
