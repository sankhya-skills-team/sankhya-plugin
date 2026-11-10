# Tabela Hierárquica (treeTable)

## Visão Geral

A tag `<treeTable>` permite criar tabelas com estrutura hierárquica pai/filho, ideal para cadastros como centros de custo, categorias de produtos ou organogramas.

## Exemplo Prático: Centro de Custo

**Arquivo:** `datadictionary/SGT_CENTROCUSTO.xml`

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <treeTable name="SGT_CENTROCUSTO" defaultMask="##.##.##">
        <description>Centro de Custo</description>
        <primaryKey>
            <field name="CODCENCUS"/>
        </primaryKey>

        <instances>
            <instance name="SGT_CentroCusto">
                <description>Centro de Custo</description>
            </instance>
        </instances>

        <fields>
            <field name="CODCENCUS" dataType="INTEIRO" allowSearch="S" visibleOnSearch="S" nullable="N" required="S" />
            <field name="DESCRCENCUS" dataType="TEXTO" size="100" allowSearch="S" visibleOnSearch="S" nullable="N" required="S" />
            <field name="ATIVO" dataType="TEXTO" size="1" allowSearch="S" visibleOnSearch="S" nullable="N" required="S" />
        </fields>
    </treeTable>
</metadados>
```

Para exibir no menu, crie um `<dynamicTreeView>` apontando para a instância `SGT_CentroCusto`.

## Atributos da Tag `<treeTable>`

| Atributo | Descrição | Exemplo |
|---|---|---|
| `name` | **Obrigatório.** Nome da tabela no banco de dados | `SGT_CENTROCUSTO` |
| `defaultMask` | Máscara de formatação para código hierárquico (opcional) | `##.##.##` |
| `maskName` | Nome de máscara já definida no sistema (opcional) | `CENTROCUSTO_MASK` |

## Campos de Controle Hierárquico

### Com Auto DDL habilitado

O Add-on Studio cria automaticamente os campos de controle — não é necessário declará-los no XML:

| Campo | Função |
|---|---|
| `CODIGOPAI` | Armazena a chave do registro pai |
| `ANALITICO` | Indica se recebe lançamentos (`S`) ou é agrupador (`N`) |
| `GRAU` | Define o nível hierárquico (0 para raiz, 1+ para filhos) |

### Com Auto DDL desabilitado (dbscript manual)

O script `CREATE TABLE` **deve obrigatoriamente** incluir os campos de controle:

```sql
CREATE TABLE SGT_CENTROCUSTO (
    -- Campos declarados no XML
    CODCENCUS    NUMBER(10)    NOT NULL,
    DESCRCENCUS  VARCHAR2(100) NOT NULL,
    ATIVO        CHAR(1)       NOT NULL,

    -- Campos de controle hierárquico (obrigatórios)
    CODIGOPAI    NUMBER(10),
    ANALITICO    CHAR(1) DEFAULT 'S' NOT NULL,

    CONSTRAINT PK_SGT_CENTROCUSTO PRIMARY KEY (CODCENCUS)
);
```

> Omitir esses campos em dbscript manual causa erros em execução — a interface depende deles.

## Boas Práticas

- Use `defaultMask` para manter consistência visual dos códigos hierárquicos
- Prefira Auto DDL — gerencia os campos de controle automaticamente

## Antipadrões

- **Esquecer campos de controle no dbscript:** erro mais comum ao não usar Auto DDL; impede o funcionamento
- **Usar `treeTable` para dados não hierárquicos:** se não há relação pai/filho, use `<table>` normal

## Fonte

https://developer.sankhya.com.br/docs/04_tabela_hierarquica
