# Estrutura de um Projeto Add-on Studio

## Diretórios Principais

```
meu-addon/
├── datadictionary/
├── dbscripts/
├── model/
│   └── src/main/java/
└── vc/
    └── src/main/webapp/
```

### `datadictionary/`

Raiz da definição de dados. Contém arquivos XML que descrevem:

- **Entidades (Jape):** representação das tabelas no sistema
- **Tabelas e campos:** estrutura física das tabelas no banco
- **Menus e telas:** interface do usuário
- **Parâmetros:** configurações customizadas do add-on

### `dbscripts/`

Scripts de banco de dados executados durante instalação/atualização.

- Nomeação sequencial: `V1.xml`, `V2.xml`, ...
- Execução em ordem garantida
- **Imutabilidade:** scripts já executados não devem ser alterados — mudanças vão em novo arquivo de versão
- Uso: views, triggers, migrações de dados complexas não cobertas pelo dicionário de dados

### `model/`

Módulo Gradle com toda a lógica de back-end em Java.

**Localização:** `model/src/main/java/`

**Componentes do Add-on Studio 2.0 clássico:**
- `@Service` — endpoint externo (equivalente a Controller)
- `@Listener` — listener de eventos de persistência
- `@Callback` — callback de eventos de documentos comerciais
- `@BusinessRule` — regra de negócio vinculada a confirmação/faturamento
- `@ActionButton` — botão de ação em tela
- `@Job` — execução periódica em background

### `vc/`

Módulo Gradle para front-end.

**Localização:** `vc/src/webapp/html5/`

A estrutura dentro de `html5/` é flexível — organize em subpastas como `css/`, `js/`, `components/` conforme necessário.

**Conteúdo:**
- Arquivos `.html` — estrutura das telas
- Arquivos `.js` — lógica de front-end (SankhyaJS ou bibliotecas)
- Arquivos `.css` — estilização
- Imagens, fontes e recursos estáticos

---

## Ciclo de Build e Deploy

O Add-on Studio expõe tarefas Gradle para todo o ciclo de vida do add-on.

### Deploy em ambiente local de desenvolvimento

Para testar em uma instância local (Docker + WildFly):

```bash
./gradlew deployAddon
```

- Compila o projeto, empacota e faz deploy direto no WildFly local
- Não requer reinicialização do servidor — o WildFly faz hot-deploy automaticamente
- Use durante o desenvolvimento para validar rapidamente as alterações

### Gerar arquivo de instalação (`.exts`)

Para gerar o pacote de instalação que será entregue ao cliente:

```bash
./gradlew buildAddon
```

- Gera o arquivo `.exts` na pasta de saída do projeto
- Este arquivo é o instalador do add-on — contém dicionário de dados, dbscripts, Java compilado e front-end
- Use para homologação e entrega ao cliente

### Publicar na AreaDev do cliente

Para publicar diretamente na AreaDev do ambiente do cliente:

```bash
./gradlew publishAddon
```

- Faz upload do add-on para a AreaDev configurada
- Requer configuração das credenciais e URL da AreaDev no `gradle.properties` ou `local.properties`
- Use para deploy em produção ou homologação remota

### Fluxo típico

```
Desenvolvimento local  →  ./gradlew deployAddon   (iteração rápida)
Entrega / homologação  →  ./gradlew buildAddon     (gera .exts)
Deploy remoto          →  ./gradlew publishAddon   (publica na AreaDev)
```

---

## Organização de Pacotes — Add-on Studio 2.0 Clássico

No clássico não existe injeção de dependências — colaboradores são instanciados com `new`. A separação de camadas é feita por convenção:

```
br/com/suaempresa/addon/
├── application/          ← lógica de negócio (AplicacaoService)
├── domain/
│   └── dto/              ← DTOs de entrada/saída
├── infra/
│   ├── repository/       ← acesso a dados (JapeWrapper, NativeSql)
│   ├── listeners/        ← @Listener
│   ├── spbean/           ← @Service (SPBean no 1.0)
│   └── helpers/          ← classes auxiliares de infraestrutura
└── actionbutton/         ← @ActionButton
```

**Responsabilidades:**
- `spbean/` — apenas adapter: abre sessão, lê JSON, delega para `application/`, escreve resposta
- `application/` — lógica de negócio; não conhece `ServiceContext` nem `JapeSession`
- `repository/` — apenas acesso a dados via `JapeWrapper` ou `NativeSql`
- `helpers/` — utilitários de infraestrutura (cálculos, mapeamentos, integrações)

**Diretrizes:**
- Cada classe instancia seus próprios colaboradores diretos com `new`
- Nunca exponha `DynamicVO` fora da camada `repository/` — mapeie para DTOs
- Mantenha coesão: todo código de uma funcionalidade no mesmo pacote de feature

## Fonte

https://developer.sankhya.com.br/docs/03_estrutura-do-projeto
