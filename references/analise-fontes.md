# Análise de Fontes Java — Referência Completa

## Categorias de Artefatos Reconhecidos

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

Cada classe não-External identificada se torna **uma entrada na lista FUNCIONALIDADES** com:

```python
{
  "titulo": "Botão Gerar Desconto",           # nome funcional descritivo
  "passos": "1. O usuário seleciona...\n2. O sistema verifica...\n3. ...",
  "obs": "• Requer status X\n• Bloqueado para grupo Y\n• Irreversível após..."
}
```

**Ordenação recomendada:**
1. Botões de Ação (`AcaoRotinaJava`)
2. Listeners/Eventos (`EventoProgramavelJava`)
3. Jobs agendados (`ScheduledAction`)
4. Regras de negócio (`Regra`, `RegraNegocioJava`)

---

## Regras de Linguagem Funcional

Aplicar ao montar FUNCIONALIDADES e demais seções de conteúdo:

| Padrão | Correto | Errado |
|---|---|---|
| Nomes de tabelas | "aba Financeiro", "tela Central de Notas" | "tabela TGFFIN", "TGFCAB" |
| Nomes de campos técnicos | Apenas quando necessário para localizar na tela (ex: "campo AD_SITUACAO") | Evitar substituíveis por descrição funcional |
| Bloqueios | "O sistema impede...", "Não é permitido..." | "lança MGEModelException" |
| ScheduledAction | "processo automático, sem interação do usuário" | "método execute() processa" |
| Regra / RegraNegocioJava | "disparado automaticamente ao confirmar NF", "ao alterar dados", "ao incluir item" | "afterUpdate()", "beforeInsert()" |
| Grupo de usuário | "restrito ao perfil Gerencial" | "CODGRUPO = 14" |
| External | "utiliza o padrão External — requer dois módulos registrados" | "CustomModuleLoader" |

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
