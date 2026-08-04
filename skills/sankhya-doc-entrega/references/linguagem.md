# Linguagem do documento de entrega

Duas camadas de regra. A primeira traduz o código para linguagem de negócio.
A segunda tira as marcas de texto gerado por IA.

O lint `scripts/revisar_texto.py` pega o que é detectável por regex e trava a
geração. O resto depende de leitura. **Nada aqui é opcional.**

---

## Antes de tudo: qual é a voz certa

Documento de entrega é texto técnico de referência, lido por consultor,
key user e quem faz o deploy. A voz correta é neutra e seca.

Não injete primeira pessoa, opinião, humor nem "personalidade" para fugir do
tom de IA. O problema não é falta de tempero, é excesso de enfeite. A correção
é sempre **tirar**, nunca acrescentar.

---

## Camada 1 — Do código para o negócio

| Padrão | Correto | Errado |
|---|---|---|
| Nomes de tabelas | "aba Financeiro", "tela Central de Notas" | "tabela TGFFIN", "TGFCAB" |
| Nomes de campos técnicos | Só quando o usuário precisa localizar na tela: "campo AD_SITUACAO" | Qualquer campo que uma descrição funcional já resolve |
| Bloqueios | "O sistema impede...", "Não é permitido..." | "lança MGEModelException" |
| Job agendado | "processo automático, sem interação do usuário" | "o método execute() processa" |
| Regra de negócio | "disparado ao confirmar a nota", "ao incluir item" | "afterUpdate()", "beforeInsert()" |
| Grupo de usuário | "restrito ao perfil Gerencial" | "CODGRUPO = 14" |
| Padrão External | "requer dois módulos registrados no Sankhya" | "CustomModuleLoader" |

---

## Camada 2 — Marcas de texto gerado por IA

### 1. Travessão — corte todos

O tell mais confiável de todos. Restrição rígida, não preferência.

Substitua, em ordem de preferência: ponto (frase nova), vírgula (aposto curto),
dois-pontos (introduz explicação), parênteses (aparte de verdade).

> ❌ A rotina, central no processo de compras — antes uma tela Flex — foi reescrita.
> ✅ A rotina é central no processo de compras. Antes era uma tela Flex.

> ❌ Operação concluída — peso líquido gravado.
> ✅ Operação concluída. O peso líquido é gravado.

Vale para `—`, `–` e ` -- `. O travessão é legítimo em `caminho_sistema`
(`Menu › Beneficiamento › BEN — Pesagem`) e dentro de mensagem do sistema
citada entre aspas. Nesses dois casos o lint não acusa.

### 2. Gerúndio de encerramento

Oração de gerúndio pendurada no fim da frase para simular profundidade. É o
equivalente em português do "-ing ending" do inglês.

Palavras que denunciam: *garantindo, permitindo, possibilitando, assegurando,
mantendo, refletindo, contribuindo, proporcionando, otimizando, facilitando,
destacando, reforçando, ampliando, viabilizando*.

> ❌ A opção Normal grava o campo em branco, mantendo a compatibilidade com o dado histórico.
> ✅ A opção Normal grava o campo em branco. O dado histórico continua compatível.

> ❌ O sistema valida a alçada antes de gravar, garantindo a integridade do fluxo.
> ✅ O sistema valida a alçada antes de gravar.

Na segunda, a oração cortada não dizia nada: a integridade já estava implícita
na validação. Boa parte dos gerúndios some sem substituição.

### 3. Vocabulário de propaganda

*robusto, eficiente, otimizado, poderoso, inovador, abrangente, vasto, crucial,
primordial, de forma transparente, de maneira eficaz, solução completa, papel
fundamental, ponto crucial, vale ressaltar, é importante destacar, de ponta.*

> ❌ A rotina oferece um fluxo de aprovação robusto e eficiente.
> ✅ A aprovação passa por três níveis: comprador, gerência e diretoria.

Adjetivo de valor não informa nada a quem vai homologar. Troque por o que o
código faz.

### 4. Regra de três

Listar três itens porque três soa completo, não porque existem três.

> ❌ O sistema valida o status, a alçada e o limite de crédito.
> ✅ O sistema valida o status e a alçada.

Se o código valida dois, escreva dois. Se valida cinco, escreva cinco. Conferir
contra o fonte, sempre. O lint não pega isso.

### 5. Fuga do verbo "ser"

> ❌ A tela serve como ponto central do processo de compras.
> ✅ A tela é o ponto central do processo de compras.

Também: *atua como, configura-se como, apresenta-se como, constitui-se*.

### 6. Paralelismo negativo

> ❌ Não apenas valida o status, mas também bloqueia a gravação.
> ✅ Valida o status e bloqueia a gravação quando ele está incorreto.

Vale para a negação truncada no fim: "sem adivinhação", "sem retrabalho",
pendurada como fragmento em vez de oração de verdade.

### 7. Voz passiva sem ator

> ❌ O registro é gravado automaticamente e o histórico é preservado.
> ✅ O sistema grava o registro e preserva o histórico.

Em `passos`, o sujeito é sempre **o usuário** ou **o sistema**. Passo sem
sujeito não é passo.

### 8. Sinônimos alternados

Trocar o termo a cada frase para não repetir. Em documento técnico a repetição
é correta: o leitor precisa saber que é a mesma coisa.

> ❌ A cotação é validada. O orçamento segue para aprovação. A proposta é liberada.
> ✅ A cotação é validada, segue para aprovação e é liberada.

Escolha um termo para cada conceito e mantenha no documento inteiro.

### 9. Negrito e emoji no meio da prosa

O renderizador já define a hierarquia visual: título, badge de tipo, caixa de
observação, caixa de limitação. `**negrito**` dentro de um campo aparece como
asterisco literal. O emoji vai no campo `icone`, não no meio da frase.

### 10. Repetir o óbvio no fim

> ❌ Após a validação, o registro é gravado. Dessa forma, o processo é concluído com o registro gravado.
> ✅ Após a validação, o sistema grava o registro.

---

## Checklist antes de gerar

```bash
python scripts/revisar_texto.py <dados.json>
```

O lint cobre travessão, gerúndio, vocabulário inflado, fuga do "ser",
paralelismo negativo e negrito. Saída limpa não encerra a revisão. Confira à
mão o que regex não vê:

- Regra de três contra o fonte: são três mesmo?
- Sinônimos alternados para o mesmo conceito.
- Passo sem sujeito explícito.
- Frase final que só repete a anterior.
