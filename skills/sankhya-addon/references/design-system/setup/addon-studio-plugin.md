# Design System em addon — plugin Gradle do Addon Studio (2.x)

Caminho nativo de empacotar tela DS em addon. Não copie bundle à mão para `vc/src/main/webapp`.

Levantado por inspeção do `br.com.sankhya.studio:gradle-plugin:2.20.0` e validado em campo (2026-10). Não é doc oficial: confira a versão do plugin do projeto (`~/.gradle/caches/modules-2/files-2.1/br.com.sankhya.studio/gradle-plugin/`) antes de confiar.

> **Decida o contexto antes de criar o addon:** `rootProject.name` sem hífen (ex.: `addonexemplo`, não `addon-exemplo`). Os blocos `snk-*` exigem um pacote Java com o nome do contexto (ver Pré-requisitos), e trocar depois exige o roteiro de renomeação no fim deste arquivo.

## Feature flag

Tudo de DS depende de `STUDIO_FEATURE_ENABLE_DS=true` (variável de ambiente). Sem ela, `gerarTela` gera tela html5 legada e `compileDS` não roda.

## Gerar a tela

```sh
./gradlew gerarTela -Ptela=NomeTela
```

Extrai o `react-app-starter` embutido no plugin em `frontend/NomeTela/`. Resíduos do starter a limpar: `name` do `package.json`, `gulpfile.ts` (fluxo de módulo nativo, não serve no addon), telas `DemoSnk*`, store `useCartStore`, `StrictMode` no `index.tsx`.

## Menu

```xml
<uiDesignSystem id="NomeTela" url="/$ctx/NomeTela.xhtml5" description="Descrição"
                resourceId="br.com.<empresa>.<contexto>.NomeTela"/>
```

## Build e deploy

`compileDS` **não** é dependência do `deployAddon`. Sem chamá-la, o WAR sai sem `labsApps/` e a tela não abre:

```sh
./gradlew :vc:compileDS deployAddon     # Windows: .\gradlew.bat (precisa de sh/Git Bash no PATH)
```

`compileDS` roda `npm install --force` + `npm run build` em cada `frontend/<Tela>` e copia o `build/` para `vc/buildGradle/studioGenerated/resources/labsApps/<Tela>/build`.

**WAR crescendo a cada deploy:** tanto o `closeBundle` do `vite.config.ts` (cópia para `buildDS`) quanto o `compileDS` copiam por cima da saída anterior, acumulando chunks com hash. Corrija nos dois pontos:

```ts
// vite.config.ts, antes de copiar build/ para VITE_OUTPUT_DIR
fs.rmSync(env.VITE_OUTPUT_DIR, { recursive: true, force: true });
```

```groovy
// vc/build.gradle — compileDS é registrada depois da avaliação do vc: use matching, não named
tasks.matching { it.name == 'compileDS' }.configureEach {
    doFirst {
        def labsApps = layout.projectDirectory.dir('buildGradle/studioGenerated/resources/labsApps')
        def tela = providers.gradleProperty('tela').orNull
        // com -Ptela só essa tela é recompilada: apagar labsApps inteiro tiraria as outras do WAR
        delete(tela ? labsApps.dir(tela) : labsApps)
    }
}
```

Coloque `buildDS` no `.gitignore` do frontend.

## Pré-requisitos do addon para `snk-*`

- **`web.xml` com `SankhyaGraphQLServlet` (`/graphql`)** e o `SankhyaGraphQLServletContextListener`. Template antigo vem sem: faça backup de `vc/src/main/webapp/WEB-INF/web.xml`, apague-o, deixe o plugin recriar do template atual e reaplique as customizações que o backup tinha (filtros, servlets, `context-param`). Sem o servlet, o `snk-application` cai no BFF do core e o GraphQL responde 500 `Sessão MGE não iniciada`.
- **Contexto (`rootProject.name`) sem hífen.** Os blocos `snk-*` pedem ao servidor `br.com.sankhya.bff.<contexto>.BFFDataUnitDatasetAdapter`. Sem ela (ou com hífen no contexto, que não forma pacote válido) o erro é `ClassNotFoundException ... BFFDataUnitDatasetAdapter`. Crie no `model` essa classe vazia:

  ```java
  package br.com.sankhya.bff.<contexto>;
  public class BFFDataUnitDatasetAdapter extends br.com.sankhya.modelcore.dataset.DataUnitDatasetAdapter {
      public BFFDataUnitDatasetAdapter() throws Exception { super(); }
  }
  ```
- Chamada de serviço do próprio addon pelo front: `callServiceBroker("<contexto>@<Servico>SP.metodo", { request: {...} })`. Sem o prefixo vai para `/mge`. Resposta de `@Controller` do SDK chega em `responseBody.body`.

## Renomear o contexto depois do primeiro deploy

1. Trocar `rootProject.name`, `BASE_PATH` do `.env.production`, proxy do `vite.config.ts`, prefixo `<contexto>@` das chamadas e o pacote do `BFFDataUnitDatasetAdapter`.
2. `UPDATE <tabela> SET DOMAIN = '<novo>' WHERE DOMAIN = '<antigo>'` nas tabelas do dicionário com coluna `DOMAIN`. Sem isso: "A tabela X já existe no Addon <antigo>".
   - **Só em base de desenvolvimento**, com backup dessas tabelas antes e tudo numa transação única. Em base de cliente, não renomeie: crie addon novo.
   - Tabelas (levantadas no schema 4.31; as `*_RP_*`, `*_MP` e `BKP_*` são cópias, ignore): `TDDADB`, `TDDTAB`, `TDDTABI18N`, `TDDCAM`, `TDDCAMI18N`, `TDDINS`, `TDDINSI18N`, `TDDOPC`, `TDDOPCI18N`, `TDDPCO`, `TDDLIG`, `TDDLGC`, `TDDIAC`, `TDDI18N`, `TRDCON`, `TRDCONI18N`, `TRDEVE`, `TRDFCO`, `TRDPCO`, `TRDSCP`. Confira na sua versão quais tabelas têm coluna `DOMAIN` (MCP `search_columns("DOMAIN")`).
3. Remover o EAR antigo de `standalone/deployments`, rodar `clean` e **reiniciar o Wildfly**: o core guarda referência ao classloader do EAR removido (`ClassNotFoundException ... from [Module "deployment.<antigo>.ear"]`).
