---
name: sankhya-doc-entrega
description: >
  Esta skill deve ser utilizada quando o usuário quiser "gerar documento de entrega",
  "criar documento de entrega de desenvolvimento", "documentar módulo do addon",
  "gerar .html de entrega", "gerar .docx de entrega", "documentar o que foi entregue",
  "gerar documentação Sankhya", ou qualquer variação de geração automática de documento
  de entrega para projetos Java Sankhya OM. Gera em dois formatos, à escolha do usuário:
  HTML interativo (colapsáveis, homologação com evidências, checklist de deploy) ou
  DOCX Word (editável, com tabela de identificação e bloco de assinaturas).
---

# Gerador de Documento de Entrega de Desenvolvimento

Gera `{PASTA_DEMANDA}/Documentacao/Entrega - {NOME_CUSTOMIZACAO}.{html|docx}` a partir
da análise dos fontes Java de um módulo Sankhya OM, no design system Sankhya. Cobre as
duas famílias: **Addon Studio** (`@Service`, `@ActionButton`, `@Listener`, `@Job`,
`@BusinessRule`) e **Módulo Java** (`AcaoRotinaJava`, `EventoProgramavelJava`,
`ScheduledAction`, `Regra`).

| Formato | Conteúdo |
|---|---|
| **HTML** (default) | Capa (só na impressão/PDF), funcionalidades colapsáveis, checklist de deploy com persistência, homologação com marcação de status e evidências por imagem com legenda, botão "Exportar com evidências" e botão "🖨️ Gerar PDF" |
| **DOCX** | Word editável, formatado na ABNT NBR 14724 — identificação, manual de uso, checklist de deploy, homologação em tabela, anexo com as evidências e bloco de assinaturas |

Ambos compartilham análise, escopo e histórico de versões. A diferença está apenas na
renderização final.

## Como funciona

O trabalho de análise é seu; a renderização é dos scripts. Você coleta os inputs, lê os
fontes, monta um **`dados.json`** e chama:

```bash
python {SKILL_DIR}/scripts/gerar_html.py <dados.json>   # ou gerar_docx.py
```

O script cuida de versionamento, backup, histórico, paleta e logo. Ele imprime
`{"arquivo": ..., "versao": ..., "backup": ..., "evidencias_faltando": [...]}`.
**Nunca** monte HTML ou DOCX à mão.

---

## Etapa 0 — Pasta raiz e formato

Exiba o diretório atual e confirme:

> "A pasta raiz do projeto é `{cwd}`? Confirme ou informe o caminho correto."

Use a resposta como `PASTA_RAIZ`. Em seguida, use **uma única chamada `AskUserQuestion`**
com as perguntas de múltipla escolha:

| Pergunta | Opções | Variável |
|---|---|---|
| Formato do documento | `HTML interativo` (recomendado) / `DOCX Word` | `FORMATO` |
| Incluir bloco de homologação? | `Sim` (recomendado) / `Não` | `INCLUIR_HOMOLOGACAO` |
| Incluir bloco de assinaturas? | `Sim` / `Não` | `INCLUIR_ASSINATURAS` |
| Coletar as evidências de homologação agora? | `Sim, você coleta pelo navegador` / `Não, eu anexo depois` | `COLETAR_EVIDENCIAS` |

A última pergunta só aparece se `INCLUIR_HOMOLOGACAO` — sem cenários não há o que
evidenciar. `Sim` dispara a Etapa 6.6.

No DOCX o bloco de homologação vira tabela de cenários com coluna "Resultado" para
preenchimento manual — mantenha a pergunta nos dois formatos.

---

## Etapa 1 — Coleta de inputs

Faça as perguntas abertas em **uma única mensagem numerada** — não uma por vez.

> 1. Nome do cliente / parceiro?
> 2. ID da demanda (DEM-1234, chamado, ticket)? Responda `não` se não houver.
> 3. Nome da pasta da demanda no projeto? (ex.: `DEM-1234`)
> 4. Nome da customização entregue? (ex.: `Pesagem de Entrada`)
> 5. Caminho de acesso no sistema? (ex.: `Menu › Beneficiamento › BEN — Pesagem de Entrada`)
> 6. Pasta com os `.java` deste módulo — pode ser relativa à raiz.
> 7. Documento de escopo funcional (`.docx`, `.pdf`, `.md`)? Responda `não` se não houver.
> 8. Quem desenvolveu? Se houve passagem de responsabilidade: `Dev A → Dev B (a partir da v1.1)`.

Antes de prosseguir, **valide que `PASTA_FONTES` existe** (`PASTA_RAIZ + '/' + resposta 6`).
Se não existir, pergunte de novo em vez de seguir e falhar depois.

Se `INCLUIR_ASSINATURAS`, pergunte também as personas (uma por linha, `Nome — Função`),
separando Sankhya e Cliente. Aceite lista vazia — o DOCX cai nos papéis padrão.

Se o documento já existe (regeração), pergunte:

> "O que mudou nesta versão? Liste as alterações, uma por linha."

Guarde como `CHANGELOG` (lista de strings). Na primeira geração deixe vazio.

---

## Etapa 2 — Análise dos fontes Java

Leia **todos os `.java`** sob `PASTA_FONTES` recursivamente (Glob + Read). O módulo pode
ser **Addon Studio** (classes anotadas) ou **Módulo Java** (classes que implementam as
interfaces do MGE) — documente as duas famílias, que convivem no mesmo repositório.
Classifique conforme `references/analise-fontes.md`:

| Addon Studio | Módulo Java | `tipo` |
|---|---|---|
| `@ActionButton` | `AcaoRotinaJava` | `acao` |
| `@Service` | — | `servico` |
| `@Listener` | `EventoProgramavelJava` | `evento` |
| `@Job` | `ScheduledAction` | `job` |
| `@BusinessRule` | `Regra` / `RegraNegocioJava` | `regra` |
| — | Classes com `CustomModuleLoader` | External — **não geram entrada**, viram observação de arquitetura |

**Granularidade do `@Service`:** a classe anotada costuma ser uma borda fina que só
roteia (dezenas de métodos de uma linha). A entrada em `funcionalidades` é o **serviço de
aplicação** que carrega a lógica — um por domínio de negócio —, e os métodos que ele
expõe viram `passos`. Sem essa camada, agrupe as operações da borda por domínio. As
demais anotações seguem a regra normal: uma classe, uma entrada.

Para cada classe não-External, monte uma entrada em `funcionalidades`:

- `titulo` — nome funcional descritivo (sem SQL, sem nome de tabela)
- `tipo` — conforme a tabela acima
- `icone` — emoji representativo do comportamento
- `passos` — lista de strings, fluxo em linguagem funcional
- `obs` — pré-condições, perfis, alçadas (vazio se não houver)
- `limitacoes` — bloqueios `MGEModelException`, restrições (vazio se não houver)
- `tipo_acesso` — `relatorio` | `tela` | `dashboard` | `""` (dispara aviso de perfis)

**Ordenação:** ações → serviços → eventos → jobs → regras.

**`tipo_acesso`:** título contém "relatório"/"report" ou há `.jrxml` associado →
`relatorio`; tela adicional → `tela`; dashboard → `dashboard`; senão `""`. Pode ser
complementado no drill-down da Etapa 3.

Monte também `objetivo` (2–3 frases sobre o que o módulo entrega ao negócio) e
`limitacoes_gerais` (lista de limitações globais).

**Escreva já no registro certo:** `references/linguagem.md`. Vale tanto para traduzir
o código em linguagem de negócio quanto para não deixar marca de texto gerado por IA.
Corrigir na Etapa 6.5 custa mais caro do que escrever certo aqui.

### Slots de teste

Se `INCLUIR_HOMOLOGACAO`, extraia por classe:

| Slot | Origem no fonte |
|---|---|
| `mensagem_bloqueio` | string literal do `throw new MGEModelException("...")`. Havendo vários, use o principal |
| `condicao_invalida` | condição que dispara o bloqueio (status ≠ "A", campo nulo, …) |
| `condicao_valida` | inverso lógico da anterior |
| `resultado_principal` | o que o código persiste ou retorna com sucesso |
| `perfil` | perfil/permissão exigido; `"não identificado"` se ausente |

Slot não identificável → `"não identificado"`. **Nunca inventar.**

---

## Etapa 3 — Scan de artefatos de deploy

### 3.1 Metadados do Javadoc

Extraia de cada `.java` o bloco `Configuracao no Sankhya:`:

```java
/**
 * Acao "Nome Exibido no Sankhya" da tela ENTIDADE.
 *
 * Configuracao no Sankhya:
 *   Entidade: ENTIDADE
 *   Tipo: AcaoRotinaJava
 *   Classe: br.com.sankhya...
 */
```

Capture o **nome exibido** (string entre aspas na primeira linha) e os pares
chave-valor. Bloco ausente → campos vazios, complementados no drill-down (3.4).

**No Addon Studio o registro está no código, não na tela do Sankhya.** Em vez do bloco de
Javadoc, leia as próprias anotações: `@Service(serviceName)` dá o nome do bean,
`@ActionButton("...")` o rótulo do botão, `@Listener(instanceNames)` a entidade
observada. Não pergunte ao usuário o que a anotação já responde.

E leia `datadictionary/menu.xml` (**ISO-8859-1**): `<nativeFolder resourceId>` mais
`<ui description>` formam o `caminho_sistema`, e cada `<acesso description="...">` é uma
permissão do módulo — a resposta de "quais perfis têm acesso".

### 3.2 Arquivos de deploy

O layout depende da família. Rode os dois conjuntos de glob e use o que existir:

| Módulo Java | Addon Studio |
|---|---|
| `{PASTA_DEMANDA}/Telas Adicionais/**/*.zip` | `datadictionary/**/*.xml` (tabelas e menu) |
| `{PASTA_DEMANDA}/Objetos de Banco/**/*.sql` | `dbscripts/**/*.{xml,sql}` |
| `dist/**/*.jar` | `build/dist/**/*.jar` · `vc/**/*.war` |
| `dist/Dashboards/**/*.zip` | `dashboards/**/*.zip` |

No addon, cada `<table name="...">` do `datadictionary/` é uma tabela que o módulo cria:
entra no checklist como pré-requisito. Ignore os JARs de terceiros que vêm junto no
`build/dist/lib/` (`sdk-sankhya.jar`, `studio-annotations.jar`, `addon-module.jar`) —
o artefato entregue é o JAR do módulo e o `.war` da tela.

### 3.3 Parâmetros TSIPAR

Grep por `TSIPAR` nos `.sql` e `.java`. Extraia os nomes únicos entre aspas
(ex.: `'PROTEGE_ALIQ'`).

### 3.4 Checklist interativo

Apresente a lista detectada numerada, separando **Pré-requisitos** (antes do deploy) de
**Pós-deploy** (após o JAR no servidor), e pergunte:

> "Deseja detalhar ou ajustar algum item? (`1,3` / `todos` / `ok`)"

Para cada item selecionado:

| Tipo | Perguntas |
|---|---|
| `tela_adicional` | Campos adicionais a documentar? Dependência de outra tela? Qual entrada em `funcionalidades` esta tela representa? |
| `parametro` | Descrição, tipo (texto/número/data), valor padrão? |
| `script_sql` | Executar em qual ambiente? (teste / produção / ambos) |
| `acao` `servico` `evento` `job` `regra` | Nome exibido correto? Entidade correta? Quais perfis têm acesso? (no addon, confirme o que o `menu.xml` já respondeu) |
| `jar` | Caminho de destino no servidor? (Enter = padrão Sankhya) |
| `dashboard` / `relatorio` | Nome exibido no Sankhya? Qual entrada em `funcionalidades` representa? |

Ao indicar a funcionalidade correspondente para `tela_adicional`, `dashboard` ou
`relatorio`, defina o `tipo_acesso` da entrada em `funcionalidades`.

Ao final: *"Há itens não detectados automaticamente? (parâmetros, scripts, telas)"*

---

## Etapa 4 — Leitura do escopo

Se o usuário informou documento de escopo:

```bash
python {SKILL_DIR}/scripts/ler_escopo.py "<caminho>" 6000
```

Suporta `.md`, `.txt`, `.docx` e `.pdf` (instala `python-docx`/`pdfplumber` se faltarem).
Use o texto para enriquecer `objetivo` e os `passos` — não para inventar funcionalidade
que não existe no código.

---

## Etapa 5 — Confirmação do objetivo

> "O objetivo abaixo foi gerado a partir da análise dos fontes. Edite se necessário e confirme:
>
> ---
> {objetivo}
> ---"

---

## Etapa 6 — Testes de homologação

Só se `INCLUIR_HOMOLOGACAO`. Preencha `testes` de cada funcionalidade com os templates
abaixo, substituindo apenas os placeholders pelos slots da Etapa 2. Não altere a
estrutura nem a ordem.

**`acao`** — 2 testes fixos + 1 condicional:

```
1. nome:     Executar '{titulo}' com {condicao_valida}
   esperado: Operação concluída. {resultado_principal}
2. nome:     Tentar executar '{titulo}' em condição inválida: {condicao_invalida}
   esperado: Sistema bloqueia com a mensagem: "{mensagem_bloqueio}"
3. nome:     Usuário sem perfil '{perfil}' tenta executar '{titulo}'
   esperado: Acesso negado ou botão indisponível para o perfil
```

**O teste 3 só existe quando `perfil` foi identificado no fonte.** Se `perfil` for
`"não identificado"`, omita-o. Um teste com perfil vazio não é verificável.

**`servico`** — 2 testes fixos + 1 condicional. A operação chega pela tela, então o
cenário se escreve do ponto de vista de quem opera:

```
1. nome:     Executar '{titulo}' pela tela com {condicao_valida}
   esperado: Operação concluída. {resultado_principal}
2. nome:     Executar '{titulo}' em condição inválida: {condicao_invalida}
   esperado: Sistema bloqueia com a mensagem: "{mensagem_bloqueio}"
3. nome:     Usuário sem a permissão '{perfil}' aciona '{titulo}'
   esperado: Acesso negado ou ação indisponível na tela
```

**O teste 3 só existe quando a permissão foi identificada** — nos addons ela costuma vir
do `<acesso>` no `menu.xml`, não do fonte Java. Não identificada, omita.

**`evento`** — 2 testes:

```
1. nome:     Realizar operação que dispara '{titulo}' com {condicao_valida}
   esperado: Evento processa sem erros. {resultado_principal}
2. nome:     Realizar operação bloqueada por '{titulo}': {condicao_invalida}
   esperado: Operação impedida com a mensagem: "{mensagem_bloqueio}"
```

**O teste 2 pressupõe que o evento bloqueia.** Se não houver `mensagem_bloqueio`
no fonte (listener que só propaga efeito, sem lançar exceção), troque-o pelo
caminho negativo real:

```
2. nome:     Realizar operação que NÃO deve disparar '{titulo}': {condicao_invalida}
   esperado: Nenhum efeito aplicado. {consequencia_da_nao_execucao}
```

**`job`** — 2 testes:

```
1. nome:     Acionar '{titulo}' com registros pendentes ({condicao_valida})
   esperado: Processamento correto. {resultado_principal}
2. nome:     Acionar '{titulo}' sem dados novos ou já processados
   esperado: Execução finaliza sem erros, sem duplicidade de processamento
```

**`regra`** — 2 testes:

```
1. nome:     Executar ciclo atendendo '{titulo}': {condicao_valida}
   esperado: Ciclo permitido sem bloqueio. {resultado_principal}
2. nome:     Executar ciclo violando '{titulo}': {condicao_invalida}
   esperado: Ciclo bloqueado com a mensagem: "{mensagem_bloqueio}"
```

`{resultado_principal}` e `{condicao_*}` entram como frase própria, começando com
maiúscula. Não emende com travessão — ver Etapa 6.5.

---

## Etapa 6.5 — Revisão de linguagem (obrigatória)

Todo o texto do documento vem da sua análise, não dos scripts. Sem esta etapa a
entrega sai com cara de texto gerado por IA e o cliente percebe.

Grave o `dados.json` e rode o lint **antes** de gerar:

```bash
python {SKILL_DIR}/scripts/revisar_texto.py <dados.json>
```

Ele varre `objetivo`, `limitacoes_gerais`, `titulo`, `passos`, `obs`,
`limitacoes`, os `testes`, as legendas das evidências e as descrições do checklist —
e trava (código 1) em:

| Regra | O que acusa |
|---|---|
| `travessao` | `—`, `–` ou ` -- ` na prosa |
| `gerundio` | oração de gerúndio pendurada no fim da frase ("…, garantindo a integridade.") |
| `inflado` | vocabulário de propaganda (robusto, eficiente, crucial, vale ressaltar…) |
| `copula` | fuga do verbo "ser" ("serve como", "atua como") |
| `negativa` | paralelismo negativo ("não apenas… mas…") |
| `negrito` | `**markdown**` dentro de campo de texto |

Campos de identificação (`caminho_sistema`, `classe`, `arquivo`, `entidade`) e
mensagens do sistema entre aspas ficam fora do lint — o travessão ali é legítimo.

**Corrija o `dados.json` e rode de novo até sair limpo.** Só então prossiga.

Lint limpo não encerra a revisão. Confira à mão o que regex não vê: regra de três
inventada (conferir a contagem contra o fonte), sinônimos alternados para o mesmo
conceito, passo sem sujeito e frase final que só repete a anterior.

Regras completas com exemplos: `references/linguagem.md`.

---

## Etapa 6.6 — Coleta de evidências

Só se `COLETAR_EVIDENCIAS`. As capturas entram no documento pelo `dados.json`, nos
dois formatos: no HTML como galeria dentro do caso de teste, no DOCX como seção
**Anexos – Evidências de Entrega** no fim.

### Onde capturar

Pergunte **antes** de abrir qualquer navegador, em uma única mensagem:

> 1. Qual a URL da base onde vou capturar?
> 2. É base de teste ou homologação? Confirme que **não** é produção.

**Não existe URL padrão e você não deduz nenhuma.** Cada colega roda contra o ambiente do
cliente dele. Se o projeto declarar a URL (`docker-compose.yml`, `.env`, `README.md`,
`docs/`), ofereça o que achou como sugestão a confirmar; não achou, pergunte e espere.
Base de produção: não capture, peça a de teste.

### Qual ferramenta

**Detecte antes de propor qualquer coisa** — a skill roda na máquina de outros colegas,
não nesta:

1. Você tem as tools `mcp__claude-in-chrome__*`? Use a aba já autenticada do usuário.
   Captura com `computer` / `action: "screenshot"` / `save_to_disk: true`.
2. Senão, `npx playwright --version` responde? Gere o harness com a engine do navegador
   dele (`chromium` · `firefox` · `webkit`). Se o projeto já tem harness em `tools/`,
   reuse-o.
3. Senão, mostre o comando de instalação e **pergunte** antes de instalar.
4. Recusou, ou nada disponível → modo manual: o usuário tira os prints, você monta o
   JSON e escreve as legendas.

A coleta é conveniência. O documento nunca depende dela — sem evidência o bloco de
homologação sai em branco, do jeito que sempre saiu.

Grave em `{PASTA_DEMANDA}/Documentacao/evidencias/`, um arquivo por caso, nomeado
`hom-fc{N}-{M}.png` (`N` = posição da funcionalidade, `M` = posição do teste).
Preencha `evidencias` e `status` de cada teste no `dados.json`.

**Cenário negativo grava dado na base.** Confirme com o usuário antes de disparar
qualquer ação de escrita, e trabalhe em base de teste.

**Nunca escreva usuário e senha em script, em `dados.json` ou no repositório.** Com a
extensão, a sessão do navegador já está logada. Com o Playwright, abra em
`headless: false`, deixe o usuário logar na janela e salve a sessão com `storageState`
para as capturas seguintes.

Protocolo de captura, matriz de navegadores e detalhes de instalação:
`references/coleta-evidencias.md`.

Ao final, rode o lint da Etapa 6.5 de novo — as legendas também são texto de entrega.

---

## Etapa 7 — Geração

Grave o `dados.json` (contrato abaixo) e execute o script do formato escolhido:

```bash
python {SKILL_DIR}/scripts/gerar_html.py /caminho/dados.json
python {SKILL_DIR}/scripts/gerar_docx.py /caminho/dados.json
```

Grave o JSON fora da pasta de entrega (use o diretório de scratchpad da sessão) — ele é
insumo, não artefato de entrega.

O HTML sai com um botão **🖨️ Gerar PDF** na sidebar (chama a impressão nativa do
navegador, `window.print()`, reaproveitando o mesmo CSS que monta a capa e oculta a
sidebar). É o próprio usuário quem clica — normalmente depois de completar a
homologação (evidências e legendas) e exportar. Não gere o PDF por fora nem antecipe
esse clique; é o usuário quem decide o momento.

### Contrato `dados.json`

```jsonc
{
  "arquivo_saida": "<PASTA_RAIZ>/<PASTA_DEMANDA>/Documentacao/Entrega - <NOME>.html",
  "parceiro": "Cliente X",
  "id_demanda": "DEM-1234",            // "" se não houver
  "nome_customizacao": "Pesagem de Entrada",
  "caminho_sistema": "Menu › Beneficiamento › BEN — Pesagem de Entrada",
  "responsavel_tecnico": "Dev A → Dev B (a partir da v1.1)",
  "objetivo": "...",
  "changelog": ["Ajuste na tolerância de peso."],   // [] na primeira geração
  "limitacoes_gerais": ["..."],
  "incluir_homologacao": true,
  "incluir_assinaturas": true,
  "personas_sankhya": ["Ana Paula Souza — Gerente de Projetos"],
  "personas_cliente": ["Roberto Mendes — Diretor Comercial"],
  "funcionalidades": [
    {
      "titulo": "Calcular Pesagem",
      "tipo": "acao",                  // acao | servico | evento | job | regra
      "icone": "⚖️",
      "passos": ["O usuário seleciona o ticket.", "O sistema calcula o peso líquido."],
      "obs": "Requer perfil Balança.",
      "limitacoes": "Irreversível após o encerramento.",
      "tipo_acesso": "tela",           // relatorio | tela | dashboard | ""
      "testes": [{
        "nome": "...",
        "esperado": "...",
        "status": "aprovado",          // pendente | aprovado | reprovado; default pendente
        "evidencias": [{ "arquivo": "hom-fc1-1.png", "legenda": "..." }]
      }]
    }
  ],
  "pasta_evidencias": "",              // default: <pasta do documento>/evidencias
  "checklist_deploy": {
    "pre_requisitos": [
      { "tipo": "tela_adicional", "nome": "AD_X", "arquivo": "Metadados_AD_X.zip", "observacao": "" },
      { "tipo": "parametro", "nome": "X_ALIQ", "descricao": "", "tipo_valor": "", "valor_padrao": "" },
      { "tipo": "script_sql", "nome": "create_ad_x.sql", "observacao": "" }
    ],
    "pos_deploy": [
      { "tipo": "acao", "nome_exibicao": "Calcular X", "entidade": "AD_X",
        "tipo_sankhya": "AcaoRotinaJava", "classe": "br.com...", "perfis": "" },
      { "tipo": "jar", "arquivo": "id2009x-1.0.0.jar", "caminho_servidor": "" },
      { "tipo": "dashboard", "arquivo": "id2009x.zip", "observacao": "" }
    ]
  }
}
```

Todos os campos são opcionais exceto `arquivo_saida`. `versao` **não** entra no JSON —
quem decide é o script.

`evidencias[].arquivo` é relativo a `pasta_evidencias`, ou absoluto. Sem `status`, um
teste com evidência sai como aprovado; sem evidência, pendente.

Arquivo declarado e ausente **não interrompe a geração**: o script avisa no stderr, lista
o caso em `evidencias_faltando` no JSON de saída e segue com as evidências que existem.
Falha de captura não é motivo para ficar sem documento — mas **repasse a lista ao usuário
na Etapa 8**, senão a entrega sai furada sem ninguém perceber.

### Versionamento

Automático. O script mantém `.historico-entregas.json` na pasta `Documentacao`:
primeira geração é `1.0`; se o arquivo já existe, sobe o minor, renomeia o anterior para
`Entrega - {NOME} v{anterior}.{ext}` e acrescenta o `changelog` ao histórico, que é
renderizado como tabela no documento. HTML e DOCX do mesmo módulo têm versões
independentes.

---

## Etapa 8 — Retorno ao usuário

Informe: arquivo gerado · versão · backup da versão anterior (se houve) · lista numerada
das funcionalidades documentadas · total de testes por funcionalidade (se houve
homologação) · total de evidências embutidas (se houve coleta).

Se o script devolveu `evidencias_faltando`, liste caso a caso o que não entrou no
documento e pergunte se o usuário quer capturar de novo ou seguir assim.

Se `FORMATO = html` **e** `INCLUIR_HOMOLOGACAO`, exiba também — pulando os passos que a
coleta da Etapa 6.6 já cobriu:

> **Como usar o bloco de Homologação:**
>
> 1. Abra o `.html` no navegador e vá até **Homologação**.
> 2. Clique no status de cada teste (⏳ → ✅ → ❌) e use **📎 Adicionar evidência** para anexar a imagem de tela — pode anexar várias em sequência.
> 3. Preencha a legenda abaixo de cada imagem anexada, descrevendo o que ela mostra.
> 4. Clique em **↓ Exportar com evidências** — gera um novo HTML com as imagens e legendas embutidas em base64 e o checklist de deploy preservado.
> 5. **Substitua** o arquivo original pelo exportado para tornar as evidências permanentes.
> 6. Para corrigir: abra o exportado, remova/substitua a imagem ou legenda e exporte de novo.
> 7. Quando o documento estiver pronto pra assinatura, clique em **🖨️ Gerar PDF** — abre o diálogo de impressão do navegador; escolha "Salvar como PDF" como destino.

---

## Manutenção

Após mexer nos scripts, rode o auto-teste:

```bash
python {SKILL_DIR}/scripts/test_geracao.py
```

Ele gera HTML e DOCX de exemplo em diretório temporário e valida escape, paleta,
versionamento, backup, histórico, presença do logo e as evidências embutidas nos dois
formatos.

## Referências

| Tópico | Arquivo |
|---|---|
| Categorias de artefatos, extração por tipo de classe, indicadores de permissão | `references/analise-fontes.md` |
| Linguagem funcional e marcas de texto gerado por IA | `references/linguagem.md` |
| Paleta, tipografia, regra HTML × DOCX, logo | `references/design-system.md` |
| Coleta de evidências: ferramentas, navegadores e protocolo | `references/coleta-evidencias.md` |
| Cores, logo e metadados de tipo (implementação) | `scripts/_brand.py` |
