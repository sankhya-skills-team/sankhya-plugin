# Dicionário de Dados (Data Dictionary)

## Visão Geral

O **Dicionário de Dados** é o componente central de um add-on no Sankhya. Define declarativamente a estrutura de dados da aplicação usando arquivos XML, garantindo armazenamento estruturado e padronizado dentro do ecossistema Sankhya.

## Estrutura de Arquivos

Todos os arquivos devem estar em `datadictionary/`, localizado em `model/src/main/resources/`.

**Boa prática:** Crie um arquivo XML separado para cada entidade principal (uma tabela, um menu, etc.).
Exemplos: `SGT_MINHATABELA.xml`, `SGT_MEUMENU.xml`

## Arquivo XML Base

Todo arquivo deve seguir a estrutura padrão referenciando `metadados.xsd`:

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <!-- Definições de tabelas, menus, etc. -->

</metadados>
```

O XSD permite validação em tempo de desenvolvimento e autocompletar na IDE (IntelliJ, etc.).

## Estruturas Suportadas

| Estrutura | Tag XML | Descrição |
|---|---|---|
| **Tabelas Novas** | `<table />` | Define novas tabelas criadas no banco de dados |
| **Tabelas Hierárquicas** | `<treeTable />` | Define tabelas com estrutura pai/filho |
| **Extensão de Tabelas Nativas** | `<nativeTable />` | Estende tabelas existentes com novos campos |
| **Views** | `<view />` | Cria views de banco de dados |
| **Formulários Dinâmicos** | `<dynamicForm />` | Cria telas de cadastro baseadas em tabelas |
| **Menus** | `<menu />` | Adiciona entradas de menu no sistema |
| **Telas Personalizadas** | `<ui />` | Registra telas customizadas (XHTML/JSF) |
| **Filtros** | `<filters />` | Adiciona seção de filtros a formulários |

## Boas Práticas

- **Prefixo único:** Use um prefixo exclusivo (ex: `SGT_`) para evitar conflitos com tabelas nativas e de outros add-ons
- **Organização por entidade:** Separe definições em arquivos lógicos, um por entidade
- **Validação contínua:** Corrija erros apontados pelo XSD antes do deploy

## Antipadrões

- **Prefixo `AD_`:** Nunca use — é reservado internamente pelo SankhyaOm
- **XML monolítico:** Evite colocar todas as definições em um único arquivo gigante
- **Tabelas para campos adicionais:** Criar nova tabela apenas para dados extras é má prática — use `<nativeTable />` para estender tabelas existentes
- **Ignorar XSD:** Escrever XML sem validação causa erros descobertos apenas em deploy

## Relacionamentos Mestre-Detalhe (relationShip)

Para que abas filhas apareçam em qualquer tela Sankhya — seja HTML5 customizada ou dynaform padrão gerado automaticamente — o relacionamento mestre-detalhe **deve ser declarado no datadictionary**. Sem isso, as abas simplesmente não aparecem, independente do tipo de tela.

No caso de telas HTML5, além do datadictionary, também é necessário adicionar as tags `<dynaform-*>` no HTML. Mas o datadictionary é o pré-requisito fundamental em ambos os casos.

### Regras

- A entidade **mestre** declara `<relation>` para cada filha, com `removeCascade="S"` se a exclusão deve ser em cascata.
- A entidade **filha** declara `<relation>` de volta para a mestre com `relation="OneToMany"`.
- O campo de join deve ser declarado em `<fields>` com `localName` (campo local) e `targetName` (campo na outra entidade).

### Entidade mestre (ex: TGFCOT.xml)

```xml
<instance name="TzaCotZan">
    <description>Cotacao ZCT</description>
    <relationShip>
        <relation entityName="TzaCotZanPro" removeCascade="S">
            <fields>
                <field localName="NUMCOTACAO" targetName="NUMCOTACAO"/>
            </fields>
        </relation>
        <relation entityName="TzaCotZanFor" removeCascade="S">
            <fields>
                <field localName="NUMCOTACAO" targetName="NUMCOTACAO"/>
            </fields>
        </relation>
    </relationShip>
</instance>
```

### Entidade filha (ex: TZACOTPRO.xml)

```xml
<instance name="TzaCotZanPro">
    <description>Cotacao ZCT - Produto</description>
    <relationShip>
        <relation entityName="TzaCotZan" relation="OneToMany">
            <fields>
                <field localName="NUMCOTACAO" targetName="NUMCOTACAO"/>
            </fields>
        </relation>
    </relationShip>
</instance>
```

### No HTML da tela

Após declarar os relacionamentos no datadictionary, adicione as tags das abas filhas dentro do `<sk-dynaform>`:

```html
<sk-dynaform sk-entity-name="TzaCotZan" ...>
    <dynaform-tza-cot-zan>
        <sk-navigator></sk-navigator>
    </dynaform-tza-cot-zan>
    <dynaform-tza-cot-zan-pro>
        <sk-navigator></sk-navigator>
    </dynaform-tza-cot-zan-pro>
    <dynaform-tza-cot-zan-for>
        <sk-navigator></sk-navigator>
    </dynaform-tza-cot-zan-for>
</sk-dynaform>
```

> O nome da tag HTML é derivado do `entityName` em kebab-case com prefixo `dynaform-`. Ex: `TzaCotZanPro` → `<dynaform-tza-cot-zan-pro>`.

### Antipadrão

```xml
<!-- ERRADO: sem relationShip, as abas não aparecem na tela mesmo com as tags HTML corretas -->
<instance name="TzaCotZan">
    <description>Cotacao ZCT</description>
</instance>
```

## Campos Calculados (Virtual Fields)

Campos calculados são campos que não existem fisicamente no banco — seu valor é computado via expressão SQL em tempo de consulta.

**Regras obrigatórias:**
- O atributo `calculated="S"` é **obrigatório** no `<field>`. Sem ele, o Sankhya não inicializa o campo e lança erro `Metadados do campo 'X' não inicializados` ao carregar a entidade.
- A expressão deve retornar exatamente uma linha e uma coluna.
- O prefixo `#type.sql#` indica que a expressão é SQL nativo Oracle.
- Referencie colunas da tabela principal pelo nome completo: `NOMETABELA.COLUNA`.

**Exemplo:**

```xml
<field name="INTEGRACAP" dataType="CHECKBOX" allowSearch="S" visibleOnSearch="S" calculated="S">
    <description>Integrado com o Pagar</description>
    <expression><![CDATA[#type.sql# SELECT CASE WHEN BAS.NUFIN IS NULL THEN 'N' ELSE 'S' END FROM TFPBAS BAS WHERE BAS.CODEMP = NTCTRRES.CODEMP AND BAS.CODFUNC = NTCTRRES.CODFUNC AND BAS.TIPFOLHA = 'R']]></expression>
</field>
```

**Antipadrão — campo calculado sem `calculated="S"`:**

```xml
<!-- ERRADO: causa "Metadados do campo não inicializados" -->
<field name="MEUCAMPO" dataType="INTEIRO" allowSearch="N" visibleOnSearch="N">
    <expression><![CDATA[#type.sql# SELECT COUNT(1) FROM ...]]></expression>
</field>

<!-- CORRETO -->
<field name="MEUCAMPO" dataType="INTEIRO" allowSearch="N" visibleOnSearch="N" calculated="S">
    <expression><![CDATA[#type.sql# SELECT COUNT(1) FROM ...]]></expression>
</field>
```

## Fonte

https://developer.sankhya.com.br/docs/01_dicionario-de-dados


## Build-blockers reais (gerarAddon — projeto real, 2026)

- **PESQUISA exige `<instance>` na MESMA tabela.** `dataType="PESQUISA"` só é válido em `<table>` que declara `<instances><instance>`. Em **`<nativeTable>` NÃO existe bloco instance** → `convertMetadata` falha com *"Para configurar campo tipo pesquisa, deve ser criado a tag instance"*. Para FK em nativeTable, usar `dataType="INTEIRO"` (guarda o código) e configurar o lookup no Construtor pós-deploy, OU mapear via relacionamento próprio. **Não** colocar PESQUISA em nativeTable.
- `<relation>` em `<relationShip>` é para **mestre-detalhe**, NÃO é requisito do PESQUISA. PESQUISA funciona só com `targetInstance/targetField/targetType` desde que a tabela tenha `<instance>`.


## Limite de nome de instância (deploy — projeto real, 2026)

⚠️ **EntityName/`<instance name>` ≤ 30 caracteres.** A coluna `TDDINS.NOMEINSTANCIA` tem máximo 30. No deploy (`deployAddon`), nome maior aborta com `ORA-12899: valor muito grande para a coluna "...".TDDINS.NOMEINSTANCIA (real: N, máximo: 30)` e o módulo não sobe. Compila e empacota normalmente — só falha ao registrar no banco. Ex.: `TesteMovimentacaoCertificadoSaida` (33) → `TesteMovimentacaoCertSaida` (26). Conferir TODOS os instance names antes do deploy.
