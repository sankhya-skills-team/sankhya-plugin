# Design System em addon — o que o plugin Gradle do Addon Studio faz

Levantado por inspeção do bytecode do `br.com.sankhya.studio:gradle-plugin:2.20.0` (classes `GerarTela`, `CompileDS`, `CommonWebPlugin`, `FeatureFlag`) em 2026-10-01. Não há doc oficial disso: confira a versão do plugin do projeto antes de confiar (`~/.gradle/caches/modules-2/files-2.1/br.com.sankhya.studio/gradle-plugin/`).

> Este é o caminho **nativo** de empacotar tela DS em addon. Prefira-o a copiar bundle à mão para `vc/src/main/webapp`.

## 1. Feature flag (beta)

Tudo de DS no plugin depende de `FeaturesBeta.ENABLE_DS`. A flag é lida com prefixo `STUDIO_FEATURE_`:

```sh
STUDIO_FEATURE_ENABLE_DS=true   # variável de ambiente
```

Sem a flag: `gerarTela` gera tela html5 legada e a task `compileDS` fica desabilitada (o build não compila o frontend).

## 2. Gerar a tela — `gerarTela`

```sh
./gradlew gerarTela -Ptela=NomeTela
```

Com a flag ligada:

- extrai `models/react-app-starter.zip` (embutido no jar do plugin) em `frontend/NomeTela/`;
- substitui `:name` (contexto do addon) no `vite.config.ts`, `ReactStarter` no `package.json` e `:name`/`:tela` no `.env.production`.

O starter extraído ainda traz resíduos que o plugin **não** troca: `name: "@sankhyalabs/react-starter"` no `package.json`, `APPNAME = "ReactStarter"` e `../../local.properties` no `gulpfile.ts` (gulp é do fluxo de módulo nativo, não do addon), telas `DemoSnk*` e store `useCartStore` de exemplo. Limpe ao começar.

Sem a flag, gera `vc/src/main/webapp/html5/NomeTela/` (`.html/.js/.css` + `launcher/.include/.body`).

## 3. Registro no menu — `uiDesignSystem`

O `metadados.xsd` tem a tag `uiDesignSystem` (mesmo tipo `ui`: `id`, `url`, `description`, `resourceId`, `license`, `publicAccess`, `<acesso>`). A mensagem que o `gerarTela` imprime monta:

```xml
<uiDesignSystem id="NomeTela" url="/$ctx/NomeTela.xhtml5" description="Descrição"/>
```

O nome da tag na mensagem vem de variável (`uiDesignSystem` com a flag, `ui` sem) — confirmado no XSD, a montagem exata da string foi lida do bytecode.

## 4. Build — task `compileDS`

Registrada pelo `CommonWebPlugin` no módulo `vc`, encadeada ao `buildWar`. Para cada pasta em `frontend/` (ou só a de `-Ptela`, se informada):

1. verifica versões de `node` e `npm`;
2. `npm install --force` e `npm run build` dentro de `frontend/<Tela>`;
3. copia `frontend/<Tela>/build` para `studioGenerated/resources/labsApps/<Tela>/build` (apaga `buildDS` antes).

Os comandos rodam via `sh -c` — **no Windows é preciso `sh` (Git Bash) no PATH** do processo Gradle.

`compileDS` é nativa: **não redefina**. Se precisar de passo extra, crie task própria e pendure nela.

## 5. Caminho publicado e `.env`

`.env.production` do starter:

```properties
BASE_PATH="/<contexto-addon>/labsApps/<Tela>/build/"
VITE_OUTPUT_DIR=buildDS
```

O `vite.config.ts` do starter, no `closeBundle`, grava `VITE_BUILD_DATE` no `.env.production`, copia `ez-design/dist/default` para `build/static/ez-design/default/`, gera `build/module_structure.json` (`npm ls --depth=0 --json`), remove `build/workspacemock` e copia `build/` para `VITE_OUTPUT_DIR`.

Proxy do dev server (`npm run dev`): `^/mge*/*` e `^/<contexto-addon>/*` para `SKW_URL`.

## 6. O que continua valendo

Os problemas de runtime do ALERTA #2 do agente `sankhya-frontend-design-system` (`APPLICATION_NAME`, bridge `utxt`, warm-up do BFF) não são resolvidos pelo plugin — aplique-os do mesmo jeito.

`.env` e `.env.*` do frontend podem ter `SKW_URL`/credenciais: garanta que estão no `.gitignore` do addon (o starter não protege o `.env` da raiz do projeto).
