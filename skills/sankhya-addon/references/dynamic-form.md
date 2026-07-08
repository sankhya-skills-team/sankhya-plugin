# Formulários Dinâmicos (Dynamic Forms)

Os **Formulários Dinâmicos** são uma das funcionalidades mais poderosas do Add-on Studio. Eles permitem criar telas de cadastro completas, com campos, abas e relacionamentos, **sem escrever uma única linha de código de interface** (como JavaScript ou HTML).

A tela é gerada automaticamente com base na definição da sua tabela no dicionário de dados.

## Como Funciona?

A criação de um formulário dinâmico envolve três passos principais, todos no dicionário de dados XML:

1. **Definir a Tabela (`<table />`)**: Criar a estrutura da tabela que armazenará os dados.
2. **Declarar a Instância (`<instance />`)**: Dar um "nome lógico" à sua tabela para que o sistema a reconheça.
3. **Criar o Formulário no Menu (`<dynamicForm />`)**: Adicionar um item de menu que aponta para a sua instância, criando a tela.

## Passo a Passo: Criando um Formulário

Vamos criar um formulário de "Atendimento" como exemplo para um add-on fictício chamado "Super Gestão" (prefixo `SGT_`).

### Passo 1: Defina a Tabela e a Instância

Crie um arquivo XML (ex: `SGT_TBTESTE.xml`) para definir a tabela `SGT_TBTESTE` e sua instância `SGT_Teste`.

```xml
<!-- arquivo: src/main/resources/datadictionary/SGT_TBTESTE.xml -->
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
           
    <table name="SGT_TBTESTE">
        <description>Tabela de Atendimentos do Add-on</description>
        <primaryKey>
            <field name="CODIGO"/>
        </primaryKey>
        
        <!-- A instância é o "apelido" da sua tabela no sistema -->
        <instances>
            <instance name="SGT_Teste">
                <description>Atendimento</description>
            </instance>
        </instances>
        
        <fields>
            <field name="CODIGO" dataType="INTEIRO" required="true" />
            <field name="DESCRICAO" dataType="TEXTO" size="100" required="true" />
            
            <!-- Campo de pesquisa que busca na tabela de Usuários -->
            <field name="CODUSU" dataType="PESQUISA" targetInstance="Usuario" targetField="CODUSU" targetType="INTEIRO">
                <description>Usuário Responsável</description>
                <!-- Expressão para preencher com o usuário logado por padrão -->
                <expression><![CDATA[return $ctx_usuario_logado;]]></expression>
            </field>
            
            <field name="DATA_CRIACAO" dataType="DATA_HORA" readOnly="true">
                <description>Data de Criação</description>
                <expression><![CDATA[return $ctx_dh_atual;]]></expression>
            </field>
        </fields>
    </table>
</metadados>
```

> **Nota**: Este exemplo assume que o [Auto DDL](./auto-ddl.md) está habilitado. Se não estiver, você precisará criar a tabela manualmente via `dbscript`.

### Passo 2: Adicione o Formulário ao Menu

Crie outro arquivo XML (ex: `SGT_MENU.xml`) para adicionar o formulário ao menu do sistema.

```xml
<!-- arquivo: src/main/resources/datadictionary/SGT_MENU.xml -->
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <menu id="SGT_MEUMENU" description="Super Gestão">
        <!-- O 'instance' aqui deve ser o mesmo nome da instância definida na tabela -->
        <dynamicForm id="SGT_FORM_TESTE" instance="SGT_Teste" description="Cadastro de Atendimentos"/>
    </menu>
</metadados>
```

**Atributos da tag `<dynamicForm>`:**

| Atributo      | Descrição                                                                 | Exemplo                   |
|---------------|---------------------------------------------------------------------------|---------------------------|
| `id`          | Identificador único para o item de menu. Use um prefixo.                  | `SGT_FORM_TESTE`          |
| `instance`    | **O mais importante**: o nome da instância que este formulário irá gerenciar. | `SGT_Teste`           |
| `description` | O texto que aparecerá no menu para o usuário.                             | `Cadastro de Atendimentos` |

Após o deploy (`./gradlew deployAddon`), um novo menu "Super Gestão" aparecerá no sistema com o item "Cadastro de Atendimentos".

## Boas Práticas

- **Separe os Arquivos**: Mantenha a definição da tabela em um arquivo e a do menu em outro. Isso organiza o projeto.
- **Use um Prefixo Único**: Sempre use um prefixo exclusivo (ex: `SGT_`) nos nomes de tabelas, instâncias e IDs de menu para evitar conflitos.
- **Aproveite as Expressões**: Use expressões (`<expression>`) para preencher campos com valores padrão, como o usuário logado (`$ctx_usuario_logado`) ou a data atual (`$ctx_dh_atual`).

## Anti-Patterns (O que evitar)

- **Uso do Prefixo `AD_`**: Não use o prefixo `AD_`. Ele é genérico e pode levar a conflitos. Crie um prefixo único para seu projeto.
- **Instância sem Tabela**: Declarar um `<dynamicForm>` para uma `instance` que não foi definida em nenhuma `<table>`.
- **Tudo em um Arquivo**: Colocar a definição da tabela e do menu no mesmo arquivo XML. Embora funcione, é uma má prática de organização.
- **Nomes Conflitantes**: Usar nomes de instâncias ou tabelas que já existem no Sankhya (ex: `Produto`, `Parceiro`). Isso causará erros graves.

## Fonte

https://developer.sankhya.com.br/docs/03_dynamicform
