# Botão de Ação (`@ActionButton`)

> Disponível a partir da versão 2.0 do Add-on Studio.

## Visão Geral

A anotação `@ActionButton` é a forma declarativa de criar botões de ação personalizados em telas do Sankhya Om. Ela associa uma classe Java — que executa uma lógica de negócio específica — a um botão visível no menu "Ações" da tela.

Para telas personalizadas, prefira criar os botões diretamente na UI e chamar a camada de `@Service`.

---

## Quando usar

Use um Botão de Ação quando o usuário precisar disparar manualmente uma rotina de back-end a partir de um ou mais registros de uma tela nativa.

Casos de uso comuns:
- **Integrações manuais**: enviar dados do registro para um sistema externo (ex: "Enviar para E-commerce").
- **Geração de relatórios/arquivos**: criar planilhas, PDFs ou outros documentos (ex: "Exportar para Excel").
- **Ações em massa**: executar uma operação complexa para vários registros selecionados (ex: "Aprovar Lotes Selecionados").
- **Interação com formulários**: coletar dados adicionais do usuário antes de executar a lógica principal.

---

## Como funciona

Crie uma classe Java que implemente `br.com.sankhya.extensions.actionbutton.AcaoRotinaJava` e anote-a com `@ActionButton`.

O framework do Add-on Studio se encarrega de:
1. Ler a anotação e registrar o botão na tela especificada.
2. Exibir o formulário (se definido) para o usuário.
3. Instanciar a classe e invocar `doAction()`, passando o contexto da execução.
4. Gerenciar a transação de banco de dados.
5. Exibir mensagens de retorno para o usuário.

### Interface `AcaoRotinaJava`

Define o contrato da ação com um único método:

- `doAction(ContextoAcao contexto)` — onde toda a lógica de negócio é executada.

### `ContextoAcao`

Ponto de acesso a todas as informações da execução:

| Método | Descrição |
|---|---|
| `contexto.getLinhas()` | Registros selecionados na tela — retorna `Registro[]` |
| `contexto.getParam("CAMPO")` | Parâmetros preenchidos no formulário |
| `contexto.setMensagemRetorno("msg")` | Define mensagem de sucesso/erro para o usuário |
| `contexto.setArquivoRetorno(file, "nome.ext")` | Retorna um arquivo para download |

### Iterar sobre registros selecionados

```java
import br.com.sankhya.extensions.actionbutton.Registro;

Registro[] linhas = contexto.getLinhas();
for (Registro registro : linhas) {
    // Ler campo do registro selecionado na tela
    BigDecimal numContrato = (BigDecimal) registro.getCampo("NUMCONTRATO");
    String status = (String) registro.getCampo("STATUS");

    // processar cada registro...
}
```

> `registro.getCampo("CAMPO")` retorna `Object` — faça cast para o tipo esperado (`BigDecimal`, `String`, `Timestamp`).

---

## Atributos da anotação `@ActionButton`

| Atributo | Obrigatório | Padrão | Descrição |
|---|---|---|---|
| `description` | Sim | — | Texto exibido no menu "Ações" da tela. |
| `instanceName` | Sim | — | Nome da entidade (instância) à qual o botão está associado. Ex: `"CabecalhoNota"` |
| `form` | Não | — | Formulário exibido ao usuário antes de executar a ação. Usa `@Form(fields = {...})`. |
| `transactionType` | Não | `AUTOMATIC` | Comportamento transacional. O framework gerencia por padrão. |
| `accessControlled` | Não | `true` | Se `true`, a visibilidade depende das permissões de acesso do usuário à tela. |
| `resourceId` | Não | — | Restringe o botão a uma tela específica pelo ID de recurso. Ex: `"br.com.sankhya.core.ped.pedidos"` |
| `refreshType` | Não | `ITEM` | O que atualizar na tela após execução. `ITEM` = registro atual; `ALL` = toda a tela. |

---

## Exemplo completo com formulário

```java
package br.com.fabricante.addon.exemplos;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.studio.annotations.hooks.*;

@ActionButton(
    description = "Exportar Dados para Planilha",
    instanceName = "CabecalhoNota",
    resourceId = "br.com.sankhya.core.mov.centraldenotas",
    form = @Form(
        fields = {
            @Field(
                name = "TIPO_ARQUIVO",
                label = "Formato",
                type = FieldType.LIST,
                required = true,
                options = {
                    @Option(value = "XLSX", label = "Excel (XLSX)"),
                    @Option(value = "CSV",  label = "CSV")
                }
            ),
            @Field(
                name = "DATA_INICIAL",
                label = "Data Inicial",
                type = FieldType.DATE,
                required = true
            ),
            @Field(
                name = "INCLUIR_ITENS",
                label = "Incluir Itens da Nota?",
                type = FieldType.CHECKBOX
            )
        }
    )
)
public class ExportarDadosAction implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao contexto) throws Exception {
        // 1. Captura dos parâmetros do formulário
        String tipoArquivo  = (String) contexto.getParam("TIPO_ARQUIVO");
        java.sql.Timestamp dataInicial = (java.sql.Timestamp) contexto.getParam("DATA_INICIAL");
        boolean incluirItens = "S".equals(contexto.getParam("INCLUIR_ITENS"));

        // 2. Lógica de negócio — delegar para um @Service
        // exportacaoService.gerarPlanilha(tipoArquivo, dataInicial, incluirItens, contexto.getLinhas());

        // 3. Feedback para o usuário
        contexto.setMensagemRetorno("Exportação iniciada para o formato: " + tipoArquivo);

        // Para retornar um arquivo:
        // contexto.setArquivoRetorno(new File(...), "relatorio.xlsx");
    }
}
```

---

## Boas práticas

- **Lógica em Services**: mantenha o `ActionButton` enxuto. Delegue a lógica de negócio para classes `@Service`.
- **Use `resourceId`**: sempre que possível, restrinja o botão à tela desejada para não poluir o menu "Ações" de outras telas que usam a mesma entidade.
- **Feedback claro**: sempre chame `contexto.setMensagemRetorno()` para informar o resultado ao usuário.
- **Mantenha `accessControlled = true`**: garante que o botão respeite as permissões de acesso configuradas no sistema.

## Anti-patterns

- **Lógica de negócio no `doAction`**: evite consultas ao banco, chamadas a APIs ou regras complexas diretamente no método. Dificulta reuso e testes.
- **Ações sem feedback**: nunca deixe o usuário sem saber o que aconteceu.
- **Usar para validações ou gatilhos automáticos**: `@ActionButton` é para ações manuais. Para lógica que dispara ao salvar/excluir/modificar, use `@BusinessRule` ou Listeners.
- **Nomes genéricos**: evite `description = "Processar"` ou `"Executar"` sem contexto. Seja específico.

---

## Exemplo Real — Carga em Lote com JapeWrapper

Padrão real de `@ActionButton` que busca registros e insere em lote:

```java
@ActionButton(
    description = "Carrega Itens de Configuração",
    instanceName = "MinhaEntidadeConfiguracao",
    accessControlled = false,
    transactionType = TransactionType.AUTOMATIC,
    refreshType = RefreshTypeEnum.PARENT_ITEM
)
public class CarregaItensConfigAction implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao contexto) throws Exception {
        // Busca itens que ainda não estão na tabela de configuração
        JapeWrapper itemDAO = JapeFactory.dao("MinhaEntidadeOrigem");
        Collection<DynamicVO> itensVO = itemDAO.find(
            "NOT EXISTS (SELECT 1 FROM MINHA_TAB_CONFIG WHERE CODITEM = TAB_ORIG.CODITEM)"
        );

        JapeWrapper configDAO = JapeFactory.dao("MinhaEntidadeConfiguracao");

        for (DynamicVO itemVO : itensVO) {
            configDAO.create()
                .set("CODITEM",  itemVO.asBigDecimal("CODITEM"))
                .set("TIPITEM",  itemVO.asBigDecimal("TIPITEM").toPlainString())
                .save();
        }

        contexto.setMensagemRetorno("Eventos carregados com sucesso!");
    }
}
```

> `JapeWrapper.find(where)` aceita uma cláusula WHERE em JAPE QL — pode incluir subqueries SQL nativas.

---

## Fonte

https://developer.sankhya.com.br/docs/05_action_button

## Atualização de versão (KSP — projeto real, 2026)

⚠️ **`transactionType` virou OBRIGATÓRIO** em `@ActionButton` nas versões novas do processador KSP do Addon Studio, apesar de a doc antiga marcá-lo como opcional. Sem ele o build falha em `kspKotlin`: *"O atributo 'transactionType' é obrigatório em anotações @ActionButton"*. Sempre incluir:

```java
import br.com.sankhya.studio.annotations.hooks.ActionButton;
import br.com.sankhya.studio.annotations.hooks.TransactionType;

@ActionButton(
    description = "...",
    instanceName = "CabecalhoNota",
    transactionType = TransactionType.AUTOMATIC   // OBRIGATÓRIO nas versões novas
)
```
