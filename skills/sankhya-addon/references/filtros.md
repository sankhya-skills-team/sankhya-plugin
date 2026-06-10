# Filtros para Formulários Dinâmicos

## Visão Geral

Os filtros permitem que usuários pesquisem dados de forma eficiente em formulários dinâmicos. Adicione a seção `<filters>` na definição da tabela no dicionário de dados — o Add-on Studio renderiza automaticamente na tela.

## Como Adicionar Filtros

Use a tag `<filters>` dentro da definição de `<table>`:

**Arquivo:** `datadictionary/SGT_TBTESTE.xml`

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <table name="SGT_TBTESTE">
        <description>Tabela de Atendimentos do Add-on</description>
        <primaryKey>
            <field name="CODIGO"/>
        </primaryKey>

        <instances>
            <instance name="SGT_Teste">
                <description>Atendimento</description>
            </instance>
        </instances>

        <fields>
            <field name="CODIGO" dataType="INTEIRO" required="true" />
            <field name="DESCRICAO" dataType="TEXTO" size="100" required="true" />
            <field name="CODUSU" dataType="PESQUISA" targetInstance="Usuario"
                   targetField="CODUSU" targetType="INTEIRO" />
            <field name="DATA_CRIACAO" dataType="DATA_HORA" readOnly="true" />
        </fields>

        <filters>
            <filter field="CODIGO" />
            <filter field="DESCRICAO" useLikeExpression="true" />
            <filter field="CODUSU" label="Usuário Responsável" />
            <filter field="DATA_CRIACAO" type="PERIODO" label="Período de Criação" />
        </filters>
    </table>
</metadados>
```

## Atributos da Tag `<filter>`

| Atributo | Descrição | Padrão | Exemplo |
|---|---|---|---|
| `field` | **Obrigatório.** Nome do campo da tabela | — | `CODUSU` |
| `label` | Texto exibido ao usuário; usa descrição do campo se omitido | — | `Usuário Responsável` |
| `type` | Tipo de componente de filtro | `PADRAO` | `PERIODO` |
| `useLikeExpression` | Se `true`, busca usa `LIKE '%valor%'` | `false` | `true` |
| `required` | Se `true`, filtro deve ser preenchido para executar busca | `false` | `true` |
| `keepLast` | Se `true`, sistema memoriza o último valor do filtro | `true` | `false` |

## Tipos de Filtro (`type`)

| Tipo | Descrição |
|---|---|
| `PADRAO` | Campo de texto simples ou pesquisa, conforme o `dataType` |
| `PERIODO` | Dois campos de data ("De" e "Até") — ideal para `DATA` ou `DATA_HORA` |
| `MULTI_SELECAO` | Permite selecionar múltiplos valores |

## Boas Práticas

- Adicione filtros apenas para campos mais usados na busca (códigos, descrições, datas)
- Use `useLikeExpression="true"` para campos de texto livre como nome ou descrição
- Para campos de data, prefira `type="PERIODO"` — mais intuitivo que campo único
- Crie índices via `dbscripts` para campos frequentemente filtrados em tabelas grandes

## Antipadrões

- **Filtros em excesso:** polui a interface e confunde o usuário
- **Índices em excesso:** cada índice consome espaço e degrada performance de escrita (INSERT, UPDATE, DELETE)
- **Filtro em campo errado:** não crie filtros para campos de controle interno ou booleanos raramente usados
- **Omitir `label`:** deixar o nome da coluna do banco (ex: `CODUSU`) sem label amigável prejudica a experiência

## Fonte

https://developer.sankhya.com.br/docs/05_filtros
