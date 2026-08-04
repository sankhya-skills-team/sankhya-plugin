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
da análise dos fontes Java de um módulo Sankhya OM (Addon Studio ou Módulo Java
complementar), no design system Sankhya.

| Formato | Conteúdo |
|---|---|
| **HTML** (default) | Funcionalidades colapsáveis, checklist de deploy com persistência, homologação com marcação de status e evidências por imagem, botão "Exportar com evidências" |
| **DOCX** | Word editável, formatado na ABNT NBR 14724 — identificação, manual de uso, checklist de deploy, homologação em tabela e bloco de assinaturas |

Ambos compartilham análise, escopo e histórico de versões. A diferença está apenas na
renderização final.

## Como funciona

O trabalho de análise é seu; a renderização é dos scripts. Você coleta os inputs, lê os
fontes, monta um **`dados.json`** e chama:

```bash
python {SKILL_DIR}/scripts/gerar_html.py <dados.json>   # ou gerar_docx.py
```

O script cuida de versionamento, backup, histórico, paleta e logo. Ele imprime
`{"arquivo": ..., "versao": ..., "backup": ...}`. **Nunca** monte HTML ou DOCX à mão.

---

## Etapa 0 — Pasta raiz e formato

Exiba o diretório atual e confirme:

> "A pasta raiz do projeto é `{cwd}`? Confirme ou informe o caminho correto."

Use a resposta como `PASTA_RAIZ`. Em seguida, use **uma única chamada `AskUserQuestion`**
com as três perguntas de múltipla escolha:

| Pergunta | Opções | Variável |
|---|---|---|
| Formato do documento | `HTML interativo` (recomendado) / `DOCX Word` | `FORMATO` |
| Incluir bloco de homologação? | `Sim` (recomendado) / `Não` | `INCLUIR_HOMOLOGACAO` |
| Incluir bloco de assinaturas? | `Sim` / `Não` | `INCLUIR_ASSINATURAS` |

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

Leia **todos os `.java`** sob `PASTA_FONTES` recursivamente (Glob + Read). Categorize
cada classe pela interface implementada, conforme `references/analise-fontes.md`:

| Interface / classe | `tipo` |
|---|---|
| `AcaoRotinaJava` | `acao` |
| `EventoProgramavelJava` | `evento` |
| `ScheduledAction` | `job` |
| `Regra` / `RegraNegocioJava` | `regra` |
| Classes com `CustomModuleLoader` | External — **não geram entrada**, viram observação de arquitetura |

Para cada classe não-External, monte uma entrada em `funcionalidades`:

- `titulo` — nome funcional descritivo (sem SQL, sem nome de tabela)
- `tipo` — conforme a tabela acima
- `icone` — emoji representativo do comportamento
- `passos` — lista de strings, fluxo em linguagem funcional
- `obs` — pré-condições, perfis, alçadas (vazio se não houver)
- `limitacoes` — bloqueios `MGEModelException`, restrições (vazio se não houver)
- `tipo_acesso` — `relatorio` | `tela` | `dashboard` | `""` (dispara aviso de perfis)

**Ordenação:** ações → eventos → jobs → regras.

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

### 3.2 Arquivos de deploy

Glob em: `{PASTA_DEMANDA}/Telas Adicionais/**/*.zip` · `{PASTA_DEMANDA}/Objetos de
Banco/**/*.sql` · `dist/**/*.jar` · `dist/Dashboards/**/*.zip`.

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
| `acao` `evento` `job` `regra` | Nome exibido correto? Entidade correta? Quais perfis têm acesso? |
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
`limitacoes`, os `testes` e as descrições do checklist — e trava (código 1) em:

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

## Etapa 7 — Geração

Grave o `dados.json` (contrato abaixo) e execute o script do formato escolhido:

```bash
python {SKILL_DIR}/scripts/gerar_html.py /caminho/dados.json
python {SKILL_DIR}/scripts/gerar_docx.py /caminho/dados.json
```

Grave o JSON fora da pasta de entrega (use o diretório de scratchpad da sessão) — ele é
insumo, não artefato de entrega.

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
      "tipo": "acao",                  // acao | evento | job | regra
      "icone": "⚖️",
      "passos": ["O usuário seleciona o ticket.", "O sistema calcula o peso líquido."],
      "obs": "Requer perfil Balança.",
      "limitacoes": "Irreversível após o encerramento.",
      "tipo_acesso": "tela",           // relatorio | tela | dashboard | ""
      "testes": [{ "nome": "...", "esperado": "..." }]
    }
  ],
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
homologação).

Se `FORMATO = html` **e** `INCLUIR_HOMOLOGACAO`, exiba também:

> **Como usar o bloco de Homologação:**
>
> 1. Abra o `.html` no navegador e vá até **Homologação**.
> 2. Clique no status de cada teste (⏳ → ✅ → ❌) e use **📎 Adicionar evidência** para anexar a imagem de tela.
> 3. Clique em **↓ Exportar com evidências** — gera um novo HTML com as imagens embutidas em base64 e o checklist de deploy preservado.
> 4. **Substitua** o arquivo original pelo exportado para tornar as evidências permanentes.
> 5. Para corrigir: abra o exportado, remova/substitua a imagem e exporte de novo.

---

## Manutenção

Após mexer nos scripts, rode o auto-teste:

```bash
python {SKILL_DIR}/scripts/test_geracao.py
```

Ele gera HTML e DOCX de exemplo em diretório temporário e valida escape, paleta,
versionamento, backup, histórico e presença do logo.

## Referências

| Tópico | Arquivo |
|---|---|
| Categorias de artefatos, extração por tipo de classe, indicadores de permissão | `references/analise-fontes.md` |
| Linguagem funcional e marcas de texto gerado por IA | `references/linguagem.md` |
| Paleta, tipografia, regra HTML × DOCX, logo | `references/design-system.md` |
| Cores, logo e metadados de tipo (implementação) | `scripts/_brand.py` |
