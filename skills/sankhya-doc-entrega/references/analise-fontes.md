# Análise de Fontes Java — Referência Completa

## Duas famílias de artefato

O mesmo módulo entregue pode vir em **Módulo Java** (classes que implementam as
interfaces do MGE) ou em **Addon Studio** (classes anotadas). A skill documenta as duas,
e há projeto com as duas convivendo — o Cotação Analítica da Zanchetta tem `@Service`,
`@ActionButton` e classes `AcaoRotinaJava` no mesmo repositório.

Descubra qual você tem antes de classificar:

```bash
grep -rl "@Service\|@ActionButton\|@Listener\|@Job\|@BusinessRule" --include="*.java" .
grep -rl "AcaoRotinaJava\|EventoProgramavelJava\|ScheduledAction\|RegraNegocioJava" --include="*.java" .
```

---

## Addon Studio — artefatos anotados

| Anotação | Tipo no ERP | `tipo` | Acionamento |
|---|---|---|---|
| `@ActionButton` | Botão de Ação | `acao` | Manual — botão na tela |
| `@Service` | Serviço chamado pela tela HTML5 | `servico` | Manual — ação do usuário na tela |
| `@Listener` | Listener de persistência | `evento` | Automático — INSERT/UPDATE/DELETE |
| `@Job` | Ação agendada | `job` | Automático — agendamento |
| `@BusinessRule` | Regra de negócio | `regra` | Automático — ciclo da nota |

### Granularidade: por operação de negócio, não por arquivo

`@Service` é a diferença que mais confunde. A classe anotada costuma ser uma **borda
fina** que só roteia — o `PreFechamentoFreteService` do Fechamento de Frete expõe 27
métodos de uma linha, cada um delegando para um serviço de aplicação. Documentar
método a método produz 27 entradas sem sentido funcional; documentar a borda produz uma
entrada vazia.

A unidade é o **serviço de aplicação**: a classe que carrega a lógica
(`FechamentoAplicacaoService`, `LiberacaoAplicacaoService`, `CancelamentoAplicacaoService`).
Cada um vira uma entrada em `funcionalidades`, com `tipo: "servico"`, e os métodos que
ele expõe viram `passos`. Não existindo essa camada, agrupe as operações da borda por
domínio e documente cada grupo.

`@ActionButton`, `@Listener`, `@Job` e `@BusinessRule` seguem a regra normal: uma classe,
uma entrada.

### O que extrair de cada anotação

- **`@Service(serviceName = "...")`** → o nome do bean, que aparece no checklist de
  deploy; e `transactionType`, que indica se a operação é transacional.
- **`@ActionButton("Nome Exibido")`** → o rótulo do botão como o usuário o vê.
- **`@Listener(instanceNames = { "..." })`** → a instância de entidade observada. É o
  equivalente ao registro manual de Evento Programável, e vem no código, não na tela.
- **`@Job`** → a periodicidade, quando declarada.

### Metadados do addon: `datadictionary/`

Os XMLs (em **ISO-8859-1**, leia com o encoding certo) declaram o que o módulo Java
tradicional deixaria para o Construtor de Telas:

- **`menu.xml`** → `<ui description="...">` dá o nome da tela e `<nativeFolder resourceId>`
  a pasta do menu — juntos formam o `caminho_sistema`. Os `<acesso description="...">`
  listam as permissões por botão: é a resposta de "quais perfis têm acesso" sem
  perguntar ao usuário.
- **`<table name="...">`** em cada XML → as tabelas que o addon cria. Entram no checklist
  de deploy como pré-requisito.

---

## Módulo Java — artefatos por interface

| Interface / Classe | Tipo no ERP | Acionamento | Configuração |
|---|---|---|---|
| `AcaoRotinaJava` | Botão de Ação | Manual — botão clicado pelo usuário | Botões de Ação na tela |
| `EventoProgramavelJava` | Listener / Evento Programável | Automático — INSERT/UPDATE/DELETE de entidade | Eventos Programáveis na entidade |
| `ScheduledAction` | Ação Agendada (Job) | Automático — agendamento por horário/cron | Ações Agendadas |
| `Regra` | Regra de Negócio (Portal) | Automático — confirmação de NF, inclusão/alteração de cabeçalho e itens nos portais | Tela Regras de Negócio |
| `RegraNegocioJava` | Regra de Negócio Avançada | Automático — mesmos momentos da `Regra`, com controle de ciclo de vida (before/after por operação) | Tela Regras de Negócio + preferência `MODREGCENTRAL` ativada |
| `AcaoRotinaJava` + `CustomModuleLoader` | Botão de Ação — módulo External | Manual — proxy que delega para JAR de lógica | Botões de Ação + preferência com código do módulo |
| `EventoProgramavelJava` + `CustomModuleLoader` | Listener External | Automático — proxy para JAR de lógica | Eventos Programáveis + preferência com código do módulo |
| `RegraNegocioJava` + `CustomModuleLoader` | Regra External | Automático — proxy para JAR de lógica | Regras de Negócio + preferência com código do módulo |
| `ScheduledAction` + `CustomModuleLoader` | Job External | Automático — proxy para JAR de lógica | Ações Agendadas + preferência com código do módulo |

### Identificando classes External (CustomModuleLoader)

Classes External são proxies — reconhecidas por:
- Nome terminando em `External` (ex: `CriarOrdemCargaActionExternal`)
- Corpo do método principal usa `CustomModuleLoader.getClass(...)` ou `MGECoreParameter.getParameterAsInt(...)`
- Não contém lógica de negócio — apenas delegam para outro JAR

**Na documentação:** classes External não geram entrada separada em FUNCIONALIDADES. Elas indicam que o módulo usa o padrão de dois JARs. Mencionar na seção de Observações que "a funcionalidade utiliza o padrão External — requer dois módulos Java registrados no Sankhya."

---

## O que extrair de cada arquivo Java

### Para todas as classes

1. **Nome da classe** → base para o título funcional
2. **Javadoc da classe** (`/** ... */`) → descrição e regras documentadas
3. **Bloqueios** (`throw new MGEModelException(...)`) → extrair mensagens como limitações/observações
4. **Grupos de usuário** → procurar `GrupoUsuarioHelper`, `CODGRUPO`, `TSILIM` (alçadas) → registrar em `PERMISSOES`

### Para `AcaoRotinaJava`

- **Parâmetros** (`ctx.getParam(...)`) → configurações necessárias para o botão
- **Entidade alvo** → inferir de `ctx.getLinhas()[0].getCampo(...)` ou DAO usado
- **Confirmações** (`ctx.confirmarSimNao(...)`) → indicar etapa de confirmação no fluxo
- **Fluxo principal** → sequência de operações em `doAction()` → transformar em passos numerados
- **Título sugerido:** "Botão {NomeDescritivo}"

### Para `EventoProgramavelJava`

- **Entidade alvo** → nome da entidade registrada (`AD_NOMETABELA` ou `DynamicEntityNames`)
- **Métodos ativos** → `beforeInsert`, `afterInsert`, `beforeUpdate`, `afterUpdate`, `beforeDelete`, `afterDelete`
- **Lógica** → extrair o método `processar()` ou equivalente chamado pelos callbacks
- **Título sugerido:** "Listener de {EntidadeDescritiva}" ou "Automação de {ação}"

### Para `ScheduledAction`

- **Frequência/cron** → se mencionado em Javadoc ou comentários
- **Lógica** → método `execute()` ou `onTime()`
- **Sem interação do usuário** → registrar como processo automático
- **Título sugerido:** "Processamento Automático de {ação}"

### Para `Regra` / `RegraNegocioJava`

- **Momento de acionamento** → `isConfirmando()`, `isFaturando()`, `isDuplicando()`, métodos `beforeUpdate/afterUpdate`
- **Tipo de operação alvo** → `CODTIPOPER`, verificações de `TIPMOV`
- **Título sugerido:** "Regra de {ação} na {operação}"

### Para `RegraNegocioJava` especificamente

- **Métodos de ciclo de vida implementados** → quais dentre `beforeInsert/afterInsert/beforeUpdate/afterUpdate` têm lógica real
- **Verificação de limite** → `existeLibLimite`, `estaLiberado` → mencionar como "sujeito à alçada de aprovação"

---

## Mapeamento classe → Entrada em FUNCIONALIDADES

Cada classe não-External identificada se torna **uma entrada na lista `funcionalidades`**
do `dados.json` (contrato completo no `SKILL.md`):

```jsonc
{
  "titulo": "Gerar Desconto",                  // nome funcional descritivo
  "tipo": "acao",                              // acao | servico | evento | job | regra
  "icone": "💰",
  "passos": ["O usuário seleciona o pedido.", "O sistema verifica o limite de desconto."],
  "obs": "Requer status Aberto. Restrito ao perfil Gerencial.",
  "limitacoes": "Irreversível após o faturamento.",
  "tipo_acesso": ""                            // relatorio | tela | dashboard | ""
}
```

`passos` é **lista de strings** — uma por etapa, sem numeração manual (o renderizador
numera).

**Ordenação recomendada:**
1. Botões de Ação (`AcaoRotinaJava`, `@ActionButton`)
2. Serviços de tela (`@Service`)
3. Listeners/Eventos (`EventoProgramavelJava`, `@Listener`)
4. Jobs agendados (`ScheduledAction`, `@Job`)
5. Regras de negócio (`Regra`, `RegraNegocioJava`, `@BusinessRule`)

---

## Regras de Linguagem

Estão em `references/linguagem.md` — fonte única, cobre tanto a tradução do código
para linguagem de negócio quanto as marcas de texto gerado por IA. O lint
`scripts/revisar_texto.py` trava a geração enquanto houver ocorrência.

---

## Indicadores de Permissões nos Fontes

Procurar ativamente nos fontes:

| Indicador | Interpretação |
|---|---|
| `GrupoUsuarioHelper` | Verificação de grupo — registrar em PERMISSOES |
| `AuthenticationInfo.getCurrent()` | Lógica dependente do usuário logado |
| `TSILIM` / alçadas | Sujeito à alçada — registrar em obs da funcionalidade |
| `CODGRUPO` comparado a valor fixo | Restrição de perfil |
| `ctx.confirmarSimNao(...)` | Ação requer confirmação do usuário |
