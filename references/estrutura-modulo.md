# Estrutura do Projeto — Módulo Java DSTech

## Visão Geral

Um módulo Java Sankhya é um projeto Gradle que gera um JAR implantado via Construtor de Telas.
O projeto modelo de referência é `modelo-dstech-customizacoes` em `/mnt/c/Projetos/modelo-dstech-customizacoes`.

**Pacote raiz:** `br.com.sankhya.dstech`

---

## Estrutura de Diretórios (Modelo DSTech)

```
projeto-dstech/
├── Java/
│   └── src/
│       └── br/com/sankhya/dstech/
│           ├── nomedemanda/               ← substituir pelo nome real do módulo
│           │   ├── actionbutton/
│           │   │   └── NomeAction.java          ← AcaoRotinaJava
│           │   ├── event/
│           │   │   └── NomeEvento.java          ← EventoProgramavelJava
│           │   ├── job/
│           │   │   └── NomeJob.java             ← ScheduledAction
│           │   ├── regra/
│           │   │   ├── NomeRegra.java           ← RegraNegocioJava
│           │   │   └── NomeRegraPreferencia.java ← Regra (via preferência)
│           │   ├── service/
│           │   │   └── NomeService.java         ← Regras de negócio
│           │   ├── repository/
│           │   │   └── NomeRepository.java      ← Acesso a dados (entidades AD_*)
│           │   ├── exception/
│           │   │   └── NomeModuloException.java ← Exceções de domínio com código rastreável
│           │   ├── dto/
│           │   │   └── NomeDto.java             ← Transferência de dados entre camadas
│           │   ├── enums/
│           │   │   └── AdicionalEntityNames.java ← Entidades customizadas AD_*
│           │   └── helper/
│           │       └── NomePopUpHelper.java     ← Helper de apresentação (PopUpBuilder)
│           ├── helper/                    ← Helpers transversais (todo o projeto)
│           │   └── JapeHelper.java
│           └── utils/
│               ├── DwfUtils.java
│               ├── MessageUtils.java
│               └── PopUpBuilder.java      ← Não nativo — copiar de examples/PopUpBuilder.java
├── Kotlin/                               ← utilitários Kotlin (MathUtils, ErrorHandle)
│   └── src/br/com/sankhya/dstech/utils/
├── build.gradle
└── Telas Adicionais/                     ← XMLs de metadados para importação
    └── nomedemanda/
        └── Metadados_AD_NOMETABELA.zip
```

---

## Convenções de Nomenclatura

### Pacotes

| Camada | Pacote | Substituir |
|---|---|---|
| Botões de ação | `br.com.sankhya.dstech.nomedemanda.actionbutton` | `nomedemanda` → nome real |
| Eventos | `br.com.sankhya.dstech.nomedemanda.event` | idem |
| Jobs agendados | `br.com.sankhya.dstech.nomedemanda.job` | idem |
| Regras de negócio | `br.com.sankhya.dstech.nomedemanda.regra` | idem |
| Service | `br.com.sankhya.dstech.nomedemanda.service` | idem |
| Repository | `br.com.sankhya.dstech.nomedemanda.repository` | idem |
| Exception | `br.com.sankhya.dstech.nomedemanda.exception` | idem |
| DTO | `br.com.sankhya.dstech.nomedemanda.dto` | idem |
| Enums do módulo | `br.com.sankhya.dstech.nomedemanda.enums` | idem |
| Helper do módulo | `br.com.sankhya.dstech.nomedemanda.helper` | idem |
| Utilitários | `br.com.sankhya.dstech.utils` | fixo |

### Classes

| Tipo | Sufixo | Exemplo |
|---|---|---|
| Evento | `Evento` | `PesoEstimadoEvento` |
| Botão de ação | `Action` | `CriarOrdemCargaAction` |
| Job agendado | `Job` | `ProcessarFinanceiroJob` |
| Regra de negócio | `Regra` | `ValidarNotaVendaRegra` |
| Regra via preferência | `RegraPreferencia` | `ValidarNotaVendaRegraPreferencia` |
| Service | `Service` | `OrdemCargaService` |
| Repository | `Repository` | `OrdemCargaRepository` |
| Exception | `Exception` | `OrdemCargaException` |
| DTO | `Dto` | `OrdemCargaDto` |
| Helper de apresentação | `PopUpHelper` | `OrdemCargaPopUpHelper` |
| Enum de entidade | `EntityNames` | `AdicionalEntityNames` |
| Enum de status | `Status` + domínio | `StatusOrdemCarga` |
| Enum de tipo | `Tipo` + domínio | `TipoMovimento` |

---

## AdicionalEntityNames — Enum de Entidades Customizadas

```java
package br.com.sankhya.dstech.nomedemanda.enums;

public enum AdicionalEntityNames {
    MINHA_ENTIDADE("AD_MINHAENTIDADE"),
    MINHA_ENTIDADE_ITENS("AD_MINHAENTIDADE_ITE");

    private final String entityName;

    AdicionalEntityNames(String entityName) {
        this.entityName = entityName;
    }

    public String getEntityName() {
        return entityName;
    }

    public static AdicionalEntityNames getByEntityName(String entityname) {
        for (AdicionalEntityNames adicional : values()) {
            if (adicional.getEntityName().equals(entityname)) {
                return adicional;
            }
        }
        throw new IllegalArgumentException("Instância inválida: " + entityname);
    }
}
```

> Sempre usar o enum no lugar de strings literais:
> ```java
> // BOM
> JapeFactory.dao(AdicionalEntityNames.ORDEM_COLETA.getEntityName()).findByPK(id);
> // RUIM
> JapeFactory.dao("AD_ORDEMCOLETA").findByPK(id);
> ```

---

## Build e Deploy

### build.gradle típico

```groovy
plugins {
    id 'java'
}

group = 'br.com.sankhya'
version = '1.0.0'
sourceCompatibility = '1.8'
targetCompatibility = '1.8'

sourceSets {
    main {
        java { srcDirs = ['Java/src'] }
        resources { srcDirs = ['Java/resources'] }
    }
}

repositories {
    flatDir { dirs 'libs' }
}

dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
}

jar {
    archiveFileName = 'dstech-nomemodulo.jar'
    from('Java/resources') {
        include "${moduleName}/**"   // inclui HTML/JS de popup e arquivos .sql
    }
}
```

### Processo de Deploy

1. **Build:** `gradle jar` → gera `build/libs/dstech-nomemodulo.jar`
2. **Empacotar ZIP** (quando houver XML de metadados):
   ```
   Metadados_NOMETABELA.zip
   ├── metadata.xml
   └── dstech-nomemodulo.jar
   ```
3. **Importar:** Sankhya → Construtor de Telas → Importar Metadados → selecionar ZIP
4. **Registrar manualmente** (se não constar no XML):
   - Eventos: Gerenciamento → Eventos Programáveis
   - Botões: Gerenciamento → Botões de Ação
   - Regras: Gerenciamento → Regras de Negócio
   - Jobs: Gerenciamento → Ações Agendadas

---

## Javadoc de Configuração (Padrão)

Toda classe que precisa de registro manual no Sankhya deve ter o bloco padronizado.
Facilita re-registro após atualizações de servidor.

```java
/**
 * Breve descrição do que a classe faz.
 *
 * Regras aplicadas: descrever validações e transformações.
 *
 * Configuração no Sankhya:
 *   Entidade    : AD_NOMETABELA                                       (evento)
 *   Tipo        : Before Insert, Before Update                        (evento)
 *   Classe Java : br.com.sankhya.dstech.nomedemanda.event.NomeEvento
 *
 *   — ou —
 *
 *   Entidade : AD_NOMETABELA                                          (botão)
 *   Classe   : br.com.sankhya.dstech.nomedemanda.actionbutton.NomeAction
 *
 *   — ou —
 *
 *   Classe   : br.com.sankhya.dstech.nomedemanda.job.NomeJob          (job)
 *
 *   — ou —
 *
 *   Classe   : br.com.sankhya.dstech.nomedemanda.regra.NomeRegra      (regra)
 */
```
