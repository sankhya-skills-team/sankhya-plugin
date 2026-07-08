# Construtor de Telas — XML de Metadados Sankhya

## Visão Geral

O Construtor de Telas é o mecanismo do Sankhya OM para criar e atualizar tabelas/telas customizadas
sem utilizar o Addon Studio. O processo consiste em:

1. Montar um arquivo XML de metadados no formato `<metadata>`
2. Empacotar o JAR do módulo Java dentro de um ZIP junto com o XML (opcional para registrar módulo)
3. Importar via: **Gerenciamento → Construtor de Telas → Importar Metadados**

Após a importação, o Sankhya cria ou atualiza a tabela no banco e registra a instância JAPE.

---

## Estrutura Geral do XML

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadata>
  <exportInfo>
    <!-- gerado automaticamente na exportação, pode omitir na criação manual -->
    <exportTime>DD/MM/YYYY HH:MM:SS</exportTime>
    <systemVersion>4.35b52</systemVersion>
    <systemCharSet>ISO-8859-1</systemCharSet>
  </exportInfo>
  <instances>

    <!-- Uma ou mais instâncias (tabelas/entidades) -->
    <instance name="AD_NOMETABELA" isUpdate="false">
      <!-- ... -->
    </instance>

  </instances>
</metadata>
```

> **`isUpdate="true"`** — atualiza instância existente (adicionar campo, modificar configuração).
> **`isUpdate="false"`** — cria nova instância.

---

## Estrutura de uma Instância

```xml
<instance name="AD_NOMETABELA" isUpdate="false">

  <instanceDescription><![CDATA[Descrição da Tela]]></instanceDescription>

  <tableInfo name="AD_NOMETABELA" sequenceType="A" sequenceField="IDCAMPO">
    <category><![CDATA[Nome da Categoria no Menu]]></category>
    <telaDescription><![CDATA[Observações técnicas ou regras da tela (opcional)]]></telaDescription>
    <tableDescription><![CDATA[Descrição da Tabela]]></tableDescription>
    <primaryKey>
      <IDCAMPO />
      <!-- Para PK composta: -->
      <!-- <CAMPO2 /> -->
    </primaryKey>
  </tableInfo>

  <fields>
    <!-- ver seção de campos abaixo -->
  </fields>

  <relationShip>
    <!-- ver seção de relacionamentos abaixo -->
  </relationShip>

  <events>
    <!-- ver seção de eventos abaixo -->
  </events>

</instance>
```

### Atributo `sequenceType`

| Valor | Comportamento |
|---|---|
| `A` | Sequência automática gerenciada pelo Sankhya (auto-increment) |
| `N` | Sem sequência — valor informado pelo usuário ou evento |

---

## Tipos de Campos (`dataType` e `presentationType`)

### `dataType` — Tipo de dado no banco

| Código | Tipo SQL | Uso |
|---|---|---|
| `I` | INTEGER / NUMBER | Inteiros, códigos, FKs |
| `F` | FLOAT / NUMBER | Decimais, valores monetários, quantidades |
| `S` | VARCHAR2 | Textos curtos |
| `T` | CLOB / VARCHAR2(4000) | Textos longos, observações |
| `D` | DATE | Datas |
| `O` | VARCHAR2 | Campo com opções pré-definidas (combobox) |
| `B` | BLOB | Binários (arquivos) |

### `presentationType` — Tipo de apresentação na tela

| Código | Apresentação |
|---|---|
| `P` | Campo simples (lookup por código, com ícone de pesquisa se tiver relacionamento) |
| `O` | Campo com lista de opções (`<options>`) |
| `T` | Campo de texto longo (textarea) |
| `C` | Checkbox (S/N) |

---

## Exemplos de Campos

### Campo chave primária (PK) auto-sequencial

```xml
<field name="IDREGISTRO" systemField="N" dataType="I" presentationType="P"
       calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="N" size="10">
  <description><![CDATA[ID Registro]]></description>
</field>
```

### Campo inteiro com lookup (FK)

```xml
<field name="CODPARC" systemField="N" dataType="I" presentationType="P"
       calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="S" size="10">
  <description><![CDATA[Cód. Parceiro]]></description>
  <properties>
    <prop name="nullable"><![CDATA[S]]></prop>
    <prop name="visivel"><![CDATA[S]]></prop>
    <prop name="readOnly"><![CDATA[N]]></prop>
    <prop name="requerido"><![CDATA[S]]></prop>
    <prop name="combobox"><![CDATA[N]]></prop>
  </properties>
</field>
```

### Campo decimal com casas decimais

```xml
<field name="QTDE" systemField="N" dataType="F" presentationType="P"
       calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
  <description><![CDATA[Quantidade]]></description>
  <properties>
    <prop name="nullable"><![CDATA[S]]></prop>
    <prop name="visivel"><![CDATA[S]]></prop>
    <prop name="nuCasasDecimais"><![CDATA[2]]></prop>
    <prop name="readOnly"><![CDATA[N]]></prop>
    <prop name="requerido"><![CDATA[S]]></prop>
    <prop name="combobox"><![CDATA[N]]></prop>
  </properties>
</field>
```

### Campo calculado (expression JavaScript)

```xml
<field name="TOTAL" systemField="N" dataType="F" presentationType="P"
       calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
  <description><![CDATA[Total]]></description>
  <expression><![CDATA[
    var qtde   = com.sankhya.util.BigDecimalUtil.getRounded($col_QTDE, 2);
    var vlrunt = com.sankhya.util.BigDecimalUtil.getRounded($col_VLRUNIT, 2);
    return com.sankhya.util.BigDecimalUtil.getRounded(qtde.multiply(vlrunt), 2);
  ]]></expression>
  <properties>
    <prop name="nullable"><![CDATA[S]]></prop>
    <prop name="visivel"><![CDATA[S]]></prop>
    <prop name="nuCasasDecimais"><![CDATA[2]]></prop>
    <prop name="readOnly"><![CDATA[S]]></prop>
    <prop name="requerido"><![CDATA[N]]></prop>
    <prop name="combobox"><![CDATA[N]]></prop>
  </properties>
</field>
```

> Na expression, referenciar campos da linha com `$col_NOMECAMPO`.

### Campo com opções pré-definidas (O)

```xml
<field name="STATUS" systemField="N" dataType="O" presentationType="O"
       calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
  <description><![CDATA[Status]]></description>
  <options>
    <option value="P"><![CDATA[Pendente]]></option>
    <option value="A"><![CDATA[Aprovado]]></option>
    <option value="R" default="S"><![CDATA[Reprovado]]></option>
  </options>
  <properties>
    <prop name="nullable"><![CDATA[S]]></prop>
    <prop name="visivel"><![CDATA[S]]></prop>
    <prop name="readOnly"><![CDATA[N]]></prop>
    <prop name="requerido"><![CDATA[S]]></prop>
    <prop name="combobox"><![CDATA[N]]></prop>
  </properties>
</field>
```

### Campo texto longo

```xml
<field name="OBSERVACOES" systemField="N" dataType="S" presentationType="T"
       calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
  <description><![CDATA[Observações]]></description>
</field>
```

### Campo data

```xml
<field name="DTREGISTRO" systemField="N" dataType="D" presentationType="P"
       calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="S">
  <description><![CDATA[Data do Registro]]></description>
  <properties>
    <prop name="nullable"><![CDATA[S]]></prop>
    <prop name="visivel"><![CDATA[S]]></prop>
    <prop name="readOnly"><![CDATA[N]]></prop>
    <prop name="requerido"><![CDATA[S]]></prop>
    <prop name="combobox"><![CDATA[N]]></prop>
  </properties>
</field>
```

### Campo com apresentação customizada (prop `apresentacao`)

Usado para lookup que exibe um campo descritivo diferente do campo código (ex: exibir nome da OC).

```xml
<field name="ORDEMCARGA" systemField="N" dataType="I" presentationType="P"
       calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="S" size="10">
  <description><![CDATA[Ordem de Carga]]></description>
  <properties>
    <prop name="nullable"><![CDATA[S]]></prop>
    <prop name="visivel"><![CDATA[S]]></prop>
    <prop name="apresentacao"><![CDATA[IDORDEMCARGA]]></prop>
    <prop name="readOnly"><![CDATA[N]]></prop>
    <prop name="requerido"><![CDATA[S]]></prop>
    <prop name="combobox"><![CDATA[N]]></prop>
  </properties>
</field>
```

### Properties — referência completa

| Propriedade | Valores | Descrição |
|---|---|---|
| `nullable` | `S` / `N` | Campo aceita null |
| `visivel` | `S` / `N` | Campo visível na tela |
| `readOnly` | `S` / `N` | Campo somente leitura |
| `requerido` | `S` / `N` | Campo obrigatório |
| `combobox` | `S` / `N` | Exibir como combobox |
| `nuCasasDecimais` | número | Casas decimais para tipo `F` |
| `apresentacao` | nome do campo | Campo exibido no lookup |

---

## Relacionamentos

```xml
<relationShip>

  <!-- Relacionamento com entidade do sistema (systemInstance="S") -->
  <relation entityName="Parceiro" type="I" insert="N" update="N" remove="N">
    <targetInfo systemInstance="S" tableName="TGFPAR" />
    <!-- Filtro opcional na lista de seleção -->
    <expression><![CDATA[CLIENTE = 'S']]></expression>
    <fields>
      <field localName="CODPARC" targetName="CODPARC" />
    </fields>
  </relation>

  <!-- Relacionamento com entidade customizada (systemInstance="N") -->
  <relation entityName="AD_MINHAENTIDADE" type="I" insert="N" update="N" remove="S">
    <targetInfo systemInstance="N" tableName="AD_MINHAENTIDADE" />
    <fields>
      <field localName="IDCAMPO_LOCAL" targetName="IDCAMPO_REMOTO" />
    </fields>
  </relation>

  <!-- Relacionamento com filtro dinâmico baseado em campos do formulário -->
  <relation entityName="Contato" type="I" insert="N" update="N" remove="N">
    <targetInfo systemInstance="S" tableName="TGFCTT" />
    <expression><![CDATA[@form-filter[this.CODPARC = form.CODPARC]@ref-param[force-one-to-one=true]]]></expression>
    <fields>
      <field localName="CODCONTATO" targetName="CODCONTATO" />
    </fields>
  </relation>

  <!-- Relacionamento com filtro de nota (apresentacao CONFIRMADA) -->
  <relation entityName="CabecalhoNota" type="I" insert="N" update="N" remove="N">
    <targetInfo systemInstance="S" tableName="TGFCAB" />
    <expression><![CDATA[@form-filter[this.NUMCONTRATO = form.NUMCONTRATO]this.TIPMOV = 'O']]></expression>
    <fields>
      <field localName="NUNOTA" targetName="NUNOTA" />
    </fields>
  </relation>

</relationShip>
```

### Atributos do `<relation>`

| Atributo | Descrição |
|---|---|
| `entityName` | Nome da instância JAPE alvo |
| `type` | `I` = inner join (normal) |
| `insert` | `S` = permite inserir na entidade relacionada pelo lookup |
| `update` | `S` = permite alterar na entidade relacionada |
| `remove` | `S` = ao excluir o registro pai, exclui os filhos em cascata |

### Expressões especiais em `<expression>`

| Expressão | Descrição |
|---|---|
| `@form-filter[this.CAMPO = form.CAMPO]` | Filtra lookup pelo valor de outro campo no formulário |
| `@ref-param[force-one-to-one=true]` | Garante que o lookup retorne exatamente um resultado |
| `this.CAMPO = 'VALOR'` | Filtro fixo na entidade relacionada |
| `CAMPO = 'S'` | Filtro sem alias |

---

## Eventos no XML

Registra um `EventoProgramavelJava` diretamente no XML de metadados:

```xml
<events>
  <event type="RJ">
    <description><![CDATA[NOME DO EVENTO EM MAIÚSCULO]]></description>
    <eventConfig>
      <javaCall className="br.com.empresa.dctm.modulo.evento.NomeEvento" />
    </eventConfig>
    <moduleName><![CDATA[NOME DO MÓDULO]]></moduleName>
    <moduleResourceID><![CDATA[br.com.empresa.dctm.nomeModulo]]></moduleResourceID>
  </event>
</events>
```

> O tipo `RJ` indica "Rotina Java". Esse é o tipo padrão para `EventoProgramavelJava`.
> `moduleResourceID` é um identificador único do módulo — usar o pacote base.

---

## Estrutura de ZIP para Deploy com JAR

Para registrar um módulo Java junto com as telas, empacote:

```
Metadados_NOME_MODULO.zip
  ├── metadata.xml          ← XML com todas as instâncias
  └── modulo.jar            ← JAR compilado do projeto Java
```

No XML, referenciar o JAR:

```xml
<!-- No nível de <metadata>, antes de <instances> -->
<jars>
  <jar name="modulo.jar" />
</jars>
```

> Quando o ZIP é importado pelo Construtor de Telas, o Sankhya registra o JAR no classpath
> e cria/atualiza as tabelas. Os eventos registrados no XML ficam ativos imediatamente.

---

## Exemplo Completo — Nova Tabela com Aba (relacionamento pai-filho)

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadata>
  <instances>

    <!-- Instância filha (itens / aba) -->
    <instance name="AD_MODITE" isUpdate="false">
      <instanceDescription><![CDATA[Itens do Módulo]]></instanceDescription>
      <tableInfo name="AD_MODITE" sequenceType="A" sequenceField="SEQUENCIA">
        <category><![CDATA[Meu Módulo]]></category>
        <tableDescription><![CDATA[Itens do Módulo]]></tableDescription>
        <primaryKey>
          <IDMODULO />
          <SEQUENCIA />
        </primaryKey>
      </tableInfo>
      <fields>
        <field name="SEQUENCIA" systemField="N" dataType="I" presentationType="P"
               calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="N">
          <description><![CDATA[Sequência]]></description>
        </field>
        <field name="IDMODULO" systemField="N" dataType="I" presentationType="P"
               calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="N">
          <description><![CDATA[ID Módulo]]></description>
        </field>
        <field name="NUNOTA" systemField="N" dataType="I" presentationType="P"
               calculated="N" allowSearch="S" allowDefault="N" visibleOnSearch="S" allowNull="S" size="10">
          <description><![CDATA[Nº Nota]]></description>
          <properties>
            <prop name="nullable"><![CDATA[S]]></prop>
            <prop name="visivel"><![CDATA[S]]></prop>
            <prop name="readOnly"><![CDATA[N]]></prop>
            <prop name="requerido"><![CDATA[S]]></prop>
            <prop name="combobox"><![CDATA[N]]></prop>
          </properties>
        </field>
        <field name="VLRUNIT" systemField="N" dataType="F" presentationType="P"
               calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
          <description><![CDATA[Vlr. Unitário]]></description>
          <properties>
            <prop name="nullable"><![CDATA[S]]></prop>
            <prop name="visivel"><![CDATA[S]]></prop>
            <prop name="nuCasasDecimais"><![CDATA[2]]></prop>
            <prop name="readOnly"><![CDATA[N]]></prop>
            <prop name="requerido"><![CDATA[S]]></prop>
            <prop name="combobox"><![CDATA[N]]></prop>
          </properties>
        </field>
      </fields>
      <relationShip>
        <relation entityName="CabecalhoNota" type="I" insert="N" update="N" remove="N">
          <targetInfo systemInstance="S" tableName="TGFCAB" />
          <fields>
            <field localName="NUNOTA" targetName="NUNOTA" />
          </fields>
        </relation>
        <!-- Vínculo com o pai — remove="S" para cascata -->
        <relation entityName="AD_MODULO" type="I" insert="N" update="N" remove="S">
          <targetInfo systemInstance="N" tableName="AD_MODULO" />
          <fields>
            <field localName="IDMODULO" targetName="IDMODULO" />
          </fields>
        </relation>
      </relationShip>
      <events>
        <event type="RJ">
          <description><![CDATA[PREENCHER VALOR UNITÁRIO]]></description>
          <eventConfig>
            <javaCall className="br.com.empresa.dctm.modulo.event.PreencherVlrUnitEvento" />
          </eventConfig>
          <moduleName><![CDATA[MEU MÓDULO]]></moduleName>
          <moduleResourceID><![CDATA[br.com.empresa.dctm.meuModulo]]></moduleResourceID>
        </event>
      </events>
    </instance>

    <!-- Instância pai (cabeçalho) -->
    <instance name="AD_MODULO" isUpdate="false">
      <instanceDescription><![CDATA[Meu Módulo]]></instanceDescription>
      <tableInfo name="AD_MODULO" sequenceType="A" sequenceField="IDMODULO">
        <category><![CDATA[Meu Módulo]]></category>
        <tableDescription><![CDATA[Meu Módulo]]></tableDescription>
        <primaryKey>
          <IDMODULO />
        </primaryKey>
      </tableInfo>
      <fields>
        <field name="IDMODULO" systemField="N" dataType="I" presentationType="P"
               calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="N" size="10">
          <description><![CDATA[ID]]></description>
        </field>
        <field name="DATA" systemField="N" dataType="D" presentationType="P"
               calculated="N" allowSearch="S" allowDefault="S" visibleOnSearch="S" allowNull="S">
          <description><![CDATA[Data]]></description>
          <properties>
            <prop name="nullable"><![CDATA[S]]></prop>
            <prop name="visivel"><![CDATA[S]]></prop>
            <prop name="readOnly"><![CDATA[N]]></prop>
            <prop name="requerido"><![CDATA[S]]></prop>
            <prop name="combobox"><![CDATA[N]]></prop>
          </properties>
        </field>
        <field name="STATUS" systemField="N" dataType="O" presentationType="O"
               calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
          <description><![CDATA[Status]]></description>
          <options>
            <option value="P" default="S"><![CDATA[Pendente]]></option>
            <option value="A"><![CDATA[Aprovado]]></option>
            <option value="R"><![CDATA[Reprovado]]></option>
          </options>
          <properties>
            <prop name="nullable"><![CDATA[S]]></prop>
            <prop name="visivel"><![CDATA[S]]></prop>
            <prop name="readOnly"><![CDATA[N]]></prop>
            <prop name="requerido"><![CDATA[S]]></prop>
            <prop name="combobox"><![CDATA[N]]></prop>
          </properties>
        </field>
        <field name="OBS" systemField="N" dataType="S" presentationType="T"
               calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S">
          <description><![CDATA[Observações]]></description>
        </field>
      </fields>
      <relationShip>
        <!-- Aba filha -->
        <relation entityName="AD_MODITE" type="I" insert="N" update="N" remove="S">
          <targetInfo systemInstance="N" tableName="AD_MODITE" />
          <fields>
            <field localName="IDMODULO" targetName="IDMODULO" />
          </fields>
        </relation>
      </relationShip>
    </instance>

  </instances>
</metadata>
```

---

## Tabelas do Sistema mais Usadas em Relacionamentos

| Entidade JAPE (`entityName`) | Tabela | Descrição | Confirmado |
|---|---|---|---|
| `CabecalhoNota` | `TGFCAB` | Cabeçalho de notas/pedidos | ✅ |
| `ItemNota` | `TGFITE` | Itens de nota | — |
| `Financeiro` | `TGFFIN` | Títulos financeiros | ✅ |
| `Parceiro` | `TGFPAR` | Parceiros (clientes/fornecedores) | ✅ |
| `Produto` / `Servico` | `TGFPRO` | Produtos e serviços | ✅ |
| `Empresa` | `TSIEMP` | Empresas | — |
| `Volume` | `TGFVOL` | Unidades de medida | — |
| `LocalFinanceiro` | `TGFLOC` | Locais/depósitos | ✅ |
| `Estoque` | `TGFEST` | Posição de estoque | — |
| `Veiculo` | `TGFVEI` | Veículos | — |
| `OrdemCarga` | `TGFORD` | Ordens de carga | ✅ |
| `Contato` | `TGFCTT` | Contatos de parceiro | — |
| `Endereco` | `TSIEND` | Endereços | — |
| `Cidade` | `TSICID` | Cidades | — |
| `Bairro` | `TSIBAI` | Bairros | — |
| `ContratoArmazenagemGeral` | `TCSCON` | Contratos de armazenagem de grãos | ✅ |
| `Usuario` | `TSIUSU` | Usuários do sistema | ✅ |
| `LiberacaoLimite` | `TSILIB` | Liberações por alçada (TSILIB) | ✅ |

> ✅ = confirmado em produção em projeto real.
> Entidades sem confirmação podem variar entre versões/instâncias do Sankhya OM.

---

## Entidades Nativas — Atenção às Diferenças XML vs Java

Alguns entityNames diferem entre o XML do Construtor de Telas e o uso em `JapeFactory.dao()`:

| Tabela | XML (`entityName`) | Java (`JapeFactory.dao()`) | `DynamicEntityNames` |
|---|---|---|---|
| TSIUSU | `Usuario` | `"Usuarios"` | `USUARIO` |
| TCSCON | `ContratoArmazenagemGeral` | `"ContratoArmazenagemGeral"` | `CONTRATO_ARMAZENAGEM` |

> Sempre testar o entityName XML em ambiente de homologação antes de ir para produção.
> Se o import falhar por entityName inválido, o Sankhya exibe erro explícito na tela de importação.



### Adicionando campos a tabela nativa (`isUpdate="true"`)

```xml
<instance name="TCSCON" isUpdate="true">
  <tableInfo name="TCSCON" sequenceType="M">
    <primaryKey>
      <NUMCONTRATO />
    </primaryKey>
  </tableInfo>
  <fields>
    <field name="AD_MEUCAMPO" systemField="N" dataType="I" presentationType="P"
           calculated="N" allowSearch="N" allowDefault="S" visibleOnSearch="N" allowNull="S" size="10">
      <description><![CDATA[Meu Campo Adicional]]></description>
      <properties>
        <prop name="nullable"><![CDATA[S]]></prop>
        <prop name="visivel"><![CDATA[S]]></prop>
        <prop name="UIGroupName"><![CDATA[Nome do Grupo na Tela]]></prop>
        <prop name="readOnly"><![CDATA[N]]></prop>
        <prop name="requerido"><![CDATA[N]]></prop>
        <prop name="combobox"><![CDATA[N]]></prop>
      </properties>
    </field>
  </fields>
</instance>
```

> Se o import com `isUpdate="true"` falhar, os campos podem ser adicionados manualmente
> via **Configurações > Campos Adicionais da Entidade** informando o entityName correto.

### Criando aba adicional em tabela nativa (ex: aba em TCSCON)

Padrão: criar tabela `AD_*` com `<reference>` apontando para a tabela nativa.
O Sankhya detecta o `<reference>` e cria a aba automaticamente na tela pai.

```xml
<references>
  <reference entityName="ContratoArmazenagemGeral" tableName="TCSCON"
             type="I" insert="N" update="N" remove="S">
    <fields>
      <field name="NUMCONTRATO" systemField="S" localName="NUMCONTRATO" />
    </fields>
  </reference>
</references>
```

> `remove="S"` → cascade delete: ao excluir o contrato, exclui os registros filhos.
