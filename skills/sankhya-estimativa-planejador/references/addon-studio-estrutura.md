# Estrutura de um projeto Addon Studio válido (template oficial Sankhya)

Formatos canônicos do **template oficial Sankhya** (`br.com.fabricante` como placeholder de pacote). Esta referência é **autossuficiente** — não depende de ler projetos externos. Ao gerar um addon, **partir do template oficial** (copiar e limpar os exemplos) e seguir estes formatos.

## Base: o template oficial

Localização local (quando presente): `/home/daniel/c/Projetos/AddonsStudio/addon-template`.
**Procedimento ao criar um addon novo:**
1. Copiar o template inteiro para a pasta do addon (estrutura, build files, `.ant`/xdoclet, `gradle/wrapper`, `.editorconfig`, `.gitignore`, `model/src/main/resources/META-INF`, `vc/src/main/webapp/{assets,WEB-INF}`).
2. **Esvaziar o código de exemplo** (manter a estrutura de pastas): `model/src/main/java/br/com/fabricante/addon/exemplos/` e a tabela de exemplo `datadictionary/tabela.xml`.
3. Ajustar `group`/`rootProject.name`/`description`/`appKey`/`parceiroNome` para o projeto.
4. Preencher com os artefatos gerados nos pacotes do parceiro.

Se o template local não existir (outra máquina), **reproduzir o skeleton a partir desta referência**.

## Árvore

```
addon/
├── build.gradle              # plugin addonstudio, appKey, group br.com.<parceiro>.addon
├── settings.gradle           # rootProject.name + include 'model' + include 'vc'
├── gradle.properties · gradlew · gradle/wrapper · .editorconfig · .gitignore · .run/
├── datadictionary/           # metadados XML ISO-8859-1
│   ├── <Tabela>.xml          # tabela própria (<table>)
│   ├── NT_<NATIVA>.xml        # campos adicionais em tabela nativa (<nativeTable>)
│   └── menu.xml
├── dbscripts/                # V1.xml, V2.xml... DDL dual-dialect idempotente
├── model/                    # backend
│   ├── .ant/                 # xdoclet (gera tripé EJB) — NÃO remover
│   ├── build.gradle
│   └── src/main/
│       ├── java/br/com/<parceiro>/addon/...
│       └── resources/META-INF/{extension-listeners.xml, parameter.xml}
└── vc/                       # frontend
    ├── build.gradle
    └── src/main/webapp/
        ├── assets/icon.png
        ├── html5/<Tela>/...
        └── WEB-INF/{web.xml, resources/service-providers.xml}
```

> **Encoding:** `.java`/`.kt`/`.xml`(datadictionary,dbscripts)/`.properties`/`.gradle`/`.sql` = **ISO-8859-1**; `.js`/`.html`/`.css`/`.json` = UTF-8. `extension-listeners.xml`/`parameter.xml` do template vêm em UTF-8 (são em inglês/sem acento). Gravar via iconv/Python, nunca Write/Edit nativo. Acento em `<description>` = byte Latin-1 ou `<![CDATA[...]]>`.

## build.gradle (raiz)

> ⚠️ **Use o plugin v2 + KSP + Kotlin (obrigatório).** O skeleton antigo com
> `gradle-plugin:1+` NÃO roda KSP e o pacote `br.com.sankhya.studio.annotations`
> não fica no classpath → `compileJava` falha com *"package ... does not exist"*.
> O plugin 2 processa as anotações via KSP; precisa do KSP e do Kotlin plugin
> declarados no `buildscript`, e do plugin `dotenv` para ler `WILDFLY_HOME`.

```groovy
buildscript {
    repositories { mavenLocal(); mavenCentral()
        maven { url = uri("https://artifacts-partners.sankhya.com.br/repository/maven-releases") } }
    dependencies {
        classpath "br.com.sankhya.studio:gradle-plugin:2+"
        classpath "com.google.devtools.ksp:symbol-processing-gradle-plugin:2.0.0-1.0.24"
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:2.0.0"
    }
}
plugins {
    id 'co.uzzu.dotenv.gradle' version '4.0.0'
}
group = 'br.com.<parceiro>.addon'
version = "1.0.0"
description = "<Nome do Addon>"

apply(plugin: "br.com.sankhya.addonstudio")
snkmodule {
    serverFolder = System.getenv("WILDFLY_HOME") ?: env.fetch('WILDFLY_HOME')
    plataformaMinima = "4.26"
}
addon {
    appKey = "<UUID do Sankhya Place>"   // gerar em areadev.sankhya.com.br, unico por addon
    parceiroNome = "<Parceiro>"
}
```

`settings.gradle`: `rootProject.name = 'nomedoaddon'` + `include 'model'` + `include 'vc'`.
`model/build.gradle`: deps (lombok compileOnly+annotationProcessor) + `test { useJUnitPlatform() }`. Encoding ISO-8859-1 no JavaCompile.

## datadictionary — tabela própria (`<table>`)

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">
    <table name="AD_CTROS" sequenceType="A" sequenceField="CODIGO">
        <description>Tabela exemplo</description>
        <primaryKey><field name="CODIGO"/></primaryKey>
        <instances>
            <instance name="MinhaEntidade">
                <description>Entidade</description>
                <relationShip>
                    <relation entityName="Parceiro" relation="OneToMany">
                        <fields><field localName="CODPARC" targetName="CODPARC"/></fields>
                    </relation>
                </relationShip>
            </instance>
        </instances>
        <fields>
            <field name="CODIGO" dataType="INTEIRO" allowSearch="S" visibleOnSearch="S">
                <description>Código</description>
            </field>
            <field name="DESCRICAO" dataType="TEXTO" allowSearch="S" visibleOnSearch="S">
                <description>Descrição</description>
            </field>
            <field name="CODUSU" dataType="PESQUISA" targetInstance="Usuario" targetField="CODUSU" targetType="INTEIRO" allowSearch="S" visibleOnSearch="S">
                <description>Usuário</description>
                <expression><![CDATA[return $ctx_usuario_logado;]]></expression>
            </field>
            <field name="DATA_CRIACAO" dataType="DATA_HORA" allowSearch="S" visibleOnSearch="S">
                <description>Data de criação</description>
                <expression><![CDATA[return $ctx_dh_atual;]]></expression>
            </field>
        </fields>
    </table>
</metadados>
```

- `sequenceType="A"` + `sequenceField` = PK sequencial automática.
- **dataTypes:** `INTEIRO`, `DECIMAL`, `TEXTO`, `DATA`, `DATA_HORA`, `LISTA` (`<fieldOptions><option value="X">Label</option></fieldOptions>`), `CHECKBOX`, `PESQUISA` (FK com `targetInstance`/`targetField`/`targetType`).
- **Default por expressão:** `<expression><![CDATA[return $ctx_usuario_logado;]]></expression>`, `$ctx_dh_atual`, etc.
- `<instance name>` = EntityName JAPE usado no código; `<relationShip>` define FKs.
- Tamanho físico (VARCHAR2(n), NUMBER(p,s)) vem do **dbscripts**.

## datadictionary — campos adicionais em tabela nativa (`NT_<TABELA>.xml`)

```xml
<metadados ...>
    <nativeTable name="TGFCAB">
        <fields>
            <field name="AD_LIBERADOFIN" dataType="CHECKBOX" allowSearch="S" visibleOnSearch="S">
                <description><![CDATA[Liberado Financeiro?]]></description>
                <properties>
                    <prop name="UITabName"><![CDATA[Customizações]]></prop>
                    <prop name="UIGroupName">Liberações</prop>
                </properties>
            </field>
        </fields>
    </nativeTable>
</metadados>
```

## dbscripts — DDL dual-dialect idempotente (`V1.xml`, `V2.xml`...)

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<scripts xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="../.gradle/scripts.xsd">
    <sql nomeTabela="AD_CTROS" ordem="1" executar="SE_NAO_EXISTIR" tipoObjeto="TABLE" nomeObjeto="AD_CTROS">
        <oracle>CREATE TABLE AD_CTROS ( CODIGO NUMBER(10) PRIMARY KEY, CODPARC NUMBER(10) )</oracle>
        <mssql>CREATE TABLE AD_CTROS ( CODIGO INT PRIMARY KEY, CODPARC INT )</mssql>
    </sql>
    <sql nomeTabela="AD_CTROS" ordem="2" executar="SE_NAO_EXISTIR" tipoObjeto="FOREIGN KEY" nomeObjeto="FK_AD_CTROS_PARC">
        <oracle>ALTER TABLE AD_CTROS ADD CONSTRAINT FK_AD_CTROS_PARC FOREIGN KEY (CODPARC) REFERENCES TGFPAR (CODPARC)</oracle>
        <mssql>ALTER TABLE AD_CTROS ADD CONSTRAINT FK_AD_CTROS_PARC FOREIGN KEY (CODPARC) REFERENCES TGFPAR (CODPARC)</mssql>
    </sql>
    <sql nomeTabela="AD_CTROS" ordem="3" executar="SE_NAO_EXISTIR" tipoObjeto="INDEX" nomeObjeto="IDX_AD_CTROS_PARC">
        <oracle>CREATE INDEX IDX_AD_CTROS_PARC ON AD_CTROS (CODPARC)</oracle>
        <mssql>CREATE INDEX IDX_AD_CTROS_PARC ON AD_CTROS (CODPARC)</mssql>
    </sql>
</scripts>
```

- **`executar`:** `SE_NAO_EXISTIR` (DDL idempotente), `SEMPRE` (DML), `SE_EXISTIR` (drop/ajuste).
- **`tipoObjeto`:** `TABLE`, `COLUMN`, `FOREIGN KEY` (FK), `CONSTRAINT` (CHECK/outras), `INDEX`, `VIEW`.
- **Sempre `<oracle>` e `<mssql>`**: `NUMBER(p,s)`↔`INT`/`DECIMAL`, `VARCHAR2(n)`↔`VARCHAR(n)`, `SYSDATE`↔`GETDATE()`.
- `ordem` crescente: TABLE → COLUMN → FOREIGN KEY → INDEX. Campos AD_ em nativa = `tipoObjeto="COLUMN"` na tabela nativa.

## Backend — EJB Service (`*SPBean`) — padrão obrigatório

Para **tela personalizada (vc/html5)**, o JS chama um **EJB Service bean**. Documentação XDoclet é **obrigatória** (sem ela o xdoclet não gera as interfaces e o serviço não é encontrado).

```java
package br.com.<parceiro>.addon.<dominio>.servico;

import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.util.BaseSPBean;
import br.com.sankhya.ws.ServiceContext;
import com.google.gson.JsonObject;
import javax.ejb.SessionBean;

/**
 * @ejb.bean name="MeuServicoSP"
 *           jndi-name="br/com/<parceiro>/addon/<dominio>/servico/MeuServicoSP"
 *           type="Stateless" transaction-type="Container" view-type="remote"
 * @ejb.transaction type="Supports"
 * @ejb.util generate="false"
 */
public class MeuServicoSPBean extends BaseSPBean implements SessionBean {

    /**
     * @throws MGEModelException
     * @ejb.interface-method tview-type="remote"
     */
    public void calcular(ServiceContext ctx) throws MGEModelException {
        JsonObject resp = new JsonObject();
        resp.addProperty("status", "OK");
        ctx.setJsonResponse(resp);
    }
}
```

- Classe termina em **`*SPBean`**; `@ejb.bean name` termina em **`*SP`**; `jndi-name` = caminho completo separado por `/`.
- Método recebe **`ServiceContext ctx`**; entrada via `ctx.getJsonRequestBody()`, saída via `ctx.setJsonResponse(JsonObject)`.
- **Registrar em `vc/src/main/webapp/WEB-INF/resources/service-providers.xml`** (criar se não existir) — sem isso o serviço não é localizado em runtime.
- **Chamada do JS:** `ServiceProxy.callService('<rootProject.name>@MeuServicoSP.calcular', { ... })` (ou URL `/<nome_projeto>/service.sbr?serviceName=MeuServicoSP.calcular`).
- Lógica de negócio em um **Service POJO** testável; o `*SPBean` é fachada fina (abre `JapeSession`, extrai JSON, delega, trata erro com `throwExceptionRollingBack`).

## Backend — Listener (`extends PersistenceEventAdapter`)

Para **tela nativa ou adicional filha de nativa** (eventos de persistência):

```java
package br.com.<parceiro>.addon.<dominio>.listener;
import br.com.sankhya.jape.event.PersistenceEvent;
import br.com.sankhya.jape.event.PersistenceEventAdapter;

public class MeuListener extends PersistenceEventAdapter {
    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        super.beforeInsert(event);
        // regra aqui
    }
}
```

- **Registrar em `model/src/main/resources/META-INF/extension-listeners.xml`** (obrigatório):
  `<listener entityName="MinhaEntidade">br.com.<parceiro>.addon.<dominio>.listener.MeuListener</listener>`

## Backend — Job (`*Job extends BaseSPBean`)

`getScheduleConfig()` retorna cron (`"* * * * *"`); `onSchedule()` executa. Mesma documentação XDoclet do EJB (`@ejb.bean name="*Job"`, view-type="local").

## EJB × ActionButton (regra)

- **Tela personalizada (vc/html5, não-filha de nativa):** EJB Service bean (`*SPBean`) + chamada por `ServiceProxy.callService`. **Nunca** `@ActionButton`.
- **Tela nativa / adicional filha de nativa (DynamicForm):** `@ActionButton`/Listener/BusinessRule.

## menu.xml

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados ...>
    <menu id="parceiro.dominio" description="Meu Addon" icon="/$ctx/assets/icon.png">
        <folder id="dominio" description="Cadastros">
            <dynamicForm id="dominio.entidade" instance="MinhaEntidade" description="Minha Entidade"/>
            <ui id="dominio.painel" url="/$ctx/MinhaTela.html5" description="Meu Painel"/>
        </folder>
    </menu>
</metadados>
```

`<dynamicForm instance="...">` = CRUD automático da entidade. `<ui url="/$ctx/*.html5">` = tela frontend do `vc/`.

## parameter.xml

`model/src/main/resources/META-INF/parameter.xml` — declara parâmetros personalizados (`<parameters group-name="mge.:name" ...>`).

## Convenções e checklist

- Tabelas próprias: `AD_*` ou prefixo do parceiro. Campos em nativa: `NT_<TABELA>.xml`. Views: `VW_*`. dbscripts `V1.xml`, `V2.xml`... incrementais (nunca editar um já aplicado).
- Pacotes Java: `br.com.<parceiro>.addon.<dominio>` em `model/src/main/java`; frontend em `vc/`.
- [ ] partiu do template oficial (estrutura completa, exemplos esvaziados)
- [ ] `build.gradle` com `addonstudio` + `appKey` + encoding ISO-8859-1
- [ ] datadictionary (`<table>`/`<nativeTable>`) + `menu.xml`; dbscripts dual-dialect idempotente ordenado
- [ ] EJB registrado em `service-providers.xml`; Listener em `extension-listeners.xml`
- [ ] tudo ISO-8859-1 verificado (`file --mime-encoding` + `LC_ALL=C grep` U+FFFD)
