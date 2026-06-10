# Auto DDL: Geração Automática de Tabelas

O recurso **Auto DDL** automatiza a criação e atualização de tabelas no banco de dados. Em vez de escrever scripts SQL manuais, você define suas tabelas em XML e o Add-on Studio cuida do resto.

> Disponível a partir da versão 2.0 do Add-on Studio.

## Por que usar

- **Agilidade:** crie e modifique o modelo de dados apenas editando XML
- **Fonte única da verdade:** o XML é a definição canônica do esquema
- **Redução de erros:** evita inconsistências entre dicionário de dados e banco físico
- **Prototipação rápida:** ideal para criar estruturas de banco para novas funcionalidades
- **Consistência garantida:** mantém dicionário e banco físico sincronizados

## Como Habilitar

Adicione `autoDDL = true` no bloco `addon` do `build.gradle`:

```groovy
// build.gradle
addon {
    appKey = "SUA_APP_KEY"
    parceiroNome = "SUA_EMPRESA"
    autoDDL = true
}
```

> **Atenção:** ao habilitar o `autoDDL`, remova dos `dbscripts` todos os `CREATE TABLE` e `ALTER TABLE` já declarados no XML. Manter os dois em paralelo causa inconsistências e erros no deploy.

A cada `./gradlew deployAddon`, o Add-on Studio verifica e aplica as mudanças do XML no banco.

## Estrutura do XML

O Auto DDL lê os arquivos XML do `datadictionary/`. Principais componentes:

- `<metadados>` — elemento raiz
- `<table name="...">` — define nova tabela (ex: `SGT_MINHATABELA`)
- `<nativeTable name="...">` — estende tabela nativa do Sankhya
- `<primaryKey>` — define a chave primária
- `<fields>` — agrupa todas as colunas
- `<field name="..." dataType="...">` — define uma coluna

**Exemplo (`SGT_PROJETOCUSTOM.xml`):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <table name="SGT_PROJETOCUSTOM">
        <primaryKey>
            <field>IDPROJ</field>
        </primaryKey>
        <fields>
            <field name="IDPROJ" dataType="INTEIRO" required="true" />
            <field name="NOMEPROJ" dataType="TEXTO" size="100" required="true" />
            <field name="ATIVO" dataType="CHECKBOX" required="true" default="S" />
            <field name="DATA_INICIO" dataType="DATA" />
        </fields>
    </table>
</metadados>
```

## Tipos de Dados (`dataType`)

| Tipo no XML   | Oracle           | SQL Server       | Uso Comum                    |
|---------------|------------------|------------------|------------------------------|
| `TEXTO`       | `VARCHAR2(size)` | `VARCHAR(size)`  | Nomes, descrições curtas     |
| `INTEIRO`     | `NUMBER`         | `INT`            | Chaves primárias, contadores |
| `DECIMAL`     | `NUMBER`         | `DECIMAL(p,s)`   | Valores monetários, medidas  |
| `DATA`        | `DATE`           | `DATETIME`       | Datas sem hora               |
| `DATA_HORA`   | `TIMESTAMP`      | `DATETIME`       | Datas com hora               |
| `HORA`        | `NUMBER`         | `SMALLINT`       | Somente hora                 |
| `CHECKBOX`    | `CHAR(1)`        | `CHAR(1)`        | Flags (S/N, Ativo/Inativo)   |
| `CAIXA_TEXTO` | `CLOB`           | `TEXT`           | Textos longos, observações   |
| `ARQUIVO`     | `BLOB`           | `VARBINARY(MAX)` | Arquivos binários            |

**Dicas sobre tipos:**
- `TEXTO` com tamanho > 100 é convertido em caixa de texto na interface
- `TEXTO` com tamanho > 4000 deve usar `CAIXA_TEXTO` (mapeado para CLOB)
- `HORA` é armazenado como NUMBER/SMALLINT, mas lido automaticamente como `java.time.LocalTime` — use `LocalTime` nas entidades

## Boas Práticas

- **Ambientes:** ideal para desenvolvimento e testes. Em produção, prefira `autoDDL = false` e scripts controlados por DBA
- **Nomenclatura:** sempre use prefixo único (ex: `SGT_`). Nunca use `AD_`
- **Controle de versão:** o XML deve estar no Git — é a fonte da verdade do esquema

## Limitações (O que o Auto DDL NÃO faz)

- **Sem operações destrutivas:** não executa `DROP TABLE` ou `DROP COLUMN` — remoções devem ser feitas manualmente
- **Sem renomear:** renomear uma coluna no XML cria uma nova coluna; a antiga permanece no banco
- **Sem alterar tipos incompatíveis:** mudar `TEXTO` para `INTEIRO` não é suportado e causa erros
- **Sem índices e constraints:** `foreign keys`, índices e outras constraints (exceto `PRIMARY KEY` e `NOT NULL`) devem ser criados via `dbscript`

## Migrando um Projeto Existente para Auto DDL

1. **Crie o XML:** defina as tabelas existentes no dicionário de dados
2. **Remova o DDL antigo:** exclua `CREATE TABLE` e `ALTER TABLE` dos `dbscripts` (mantenha `CREATE INDEX`, constraints, etc.)
3. **Habilite:** adicione `autoDDL = true` no `build.gradle`
4. **Deploy:** execute `./gradlew clean deployAddon`
5. **Verifique:** confirme que nenhuma mudança inesperada ocorreu e que a aplicação funciona

## Fonte

https://developer.sankhya.com.br/docs/02_autoddl