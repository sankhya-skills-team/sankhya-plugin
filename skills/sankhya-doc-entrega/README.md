# skill-sankhya-doc-entrega

Skill para Claude Code que gera o **documento de entrega de desenvolvimento** de projetos
Java Sankhya OM — Addon Studio ou Módulo Java complementar. Dois formatos, à escolha do
usuário: **HTML interativo** ou **DOCX Word**, ambos no modelo DS "Evidências de Entrega
de Customização v.4", com cores e tipografia do guia Padrão Sankhya 2026.

---

## O que esta skill faz

Analisa os fontes Java de um módulo entregue, extrai funcionalidades e regras de negócio
em linguagem funcional (sem SQL, sem nomes de tabela) e produz
`{PASTA_DEMANDA}/Documentacao/Entrega - {NOME}.{html|docx}`.

O agente faz a análise e monta um `dados.json`; a renderização fica nos scripts Python —
o SKILL.md não carrega código de template para o contexto.

---

## Formatos

| Formato | Conteúdo |
|---|---|
| **HTML interativo** (default) | Estrutura do modelo v.4 com capa e contracapa. Funcionalidades colapsáveis, homologação com marcação de status e evidências por imagem, checklist de deploy com persistência, botões "Exportar com evidências" e "Gerar PDF" |
| **DOCX Word** | Preenchido sobre o template v.4 (`assets/modelo-entrega-v4.docx`): capa, controle do documento, sumário, seções 01 a 08, assinaturas e contracapa. Evidências e checklist de deploy em 07 Anexos |

Seções dos dois formatos: Controle do documento · 01 Identificação · 02 Objetivo · 03
Descrição das Personalizações · 04 Manual de Uso · 05 Homologação e Testes · 06
Treinamento e Suporte · 07 Anexos · 08 Prazo de Garantia · Assinaturas.

---

## Evidências de homologação

As capturas entram pelo `dados.json`, em `funcionalidades[].testes[].evidencias`, e
aparecem nos dois formatos: no HTML como galeria dentro do caso de teste, no DOCX em
"07 Anexos › Capturas de tela". O `status` do teste marca o resultado.

Evidência declarada e ausente não interrompe nada: o gerador avisa no stderr, devolve a
lista em `evidencias_faltando` no JSON de saída e emite o documento com o que existe.

Quando o usuário aceita, o agente coleta as capturas ele mesmo. A ferramenta é detectada
em tempo de execução, nunca presumida: extensão do navegador (`mcp__claude-in-chrome__*`)
primeiro, por usar a aba já autenticada; Playwright depois, único caminho para Firefox e
Safari; e o modo manual, em que o usuário tira os prints e o agente só monta o JSON.
Detalhes em `references/coleta-evidencias.md`.

O DOCX não carrega formatação no código: margens, fontes, estilos, cabeçalho e rodapé
vêm do template. Campo não informado mantém o placeholder `< ... >` do modelo, para
preenchimento manual no Word.

---

## Estrutura

```
sankhya-doc-entrega/
├── SKILL.md                    Fluxo, perguntas e contrato do dados.json
├── assets/
│   ├── modelo-entrega-v4.docx  Template DS v.4 preenchido pelo gerar_docx.py
│   ├── capa-fundo.jpg          Fundo da capa (HTML), extraído do template
│   └── contracapa-fundo.jpg    Fundo da contracapa (HTML), extraído do template
├── references/
│   ├── analise-fontes.md       Categorias de artefatos e extração por tipo de classe
│   ├── coleta-evidencias.md    Ferramentas, navegadores e protocolo de captura
│   ├── linguagem.md            Linguagem funcional e marcas de texto gerado por IA
│   └── design-system.md        Paleta, tipografia, regra HTML × DOCX, template
└── scripts/
    ├── _brand.py               Cores, tipografia, logo SVG e metadados de tipo
    ├── _comum.py               Entrada, versionamento, histórico, assinaturas
    ├── gerar_html.py           dados.json → .html
    ├── gerar_docx.py           dados.json → .docx
    ├── ler_escopo.py           Extrai texto de .md/.txt/.docx/.pdf
    ├── revisar_texto.py        Lint de linguagem — trava a geração
    └── test_geracao.py         Auto-teste dos geradores
```

---

## Revisão de linguagem

Todo o texto do documento vem da análise do agente, não dos scripts. Sem gate, a
entrega sai com cara de texto gerado por IA.

`revisar_texto.py` roda antes da geração e **sai com código 1** enquanto houver
ocorrência de travessão, gerúndio de encerramento, vocabulário de propaganda,
fuga do verbo "ser", paralelismo negativo ou negrito em campo de texto. Campos de
identificação (`caminho_sistema`, `classe`, `arquivo`) e mensagens do sistema
entre aspas ficam fora — o travessão ali é legítimo.

O que regex não pega (regra de três inventada, sinônimos alternados, passo sem
sujeito) está em `references/linguagem.md` e depende de leitura.

Regras destiladas da skill [humanizer](https://github.com/Dicklesworthstone/humanizer)
e adaptadas para português e para o gênero "documento de entrega".

---

## Artefatos Java reconhecidos

Duas famílias, que convivem no mesmo repositório:

| Addon Studio | Módulo Java | Tipo no ERP | Acionamento |
|---|---|---|---|
| `@ActionButton` | `AcaoRotinaJava` | Botão de Ação | Manual — clique do usuário |
| `@Service` | — | Serviço chamado pela tela HTML5 | Manual — ação do usuário na tela |
| `@Listener` | `EventoProgramavelJava` | Listener / Evento | Automático — INSERT/UPDATE/DELETE |
| `@Job` | `ScheduledAction` | Ação Agendada | Automático — cron/horário |
| `@BusinessRule` | `Regra` / `RegraNegocioJava` | Regra de Negócio | Automático — ciclo de confirmação de NF |
| — | Classes com `CustomModuleLoader` | Padrão External (proxy) | Não geram entrada — viram observação de arquitetura |

No addon, a unidade documentada do `@Service` é o **serviço de aplicação**, não o arquivo:
a classe anotada costuma ser uma borda fina que só roteia dezenas de métodos. O
`datadictionary/` responde o que antes vinha de pergunta ao usuário — `menu.xml` dá o
caminho de acesso e as permissões por botão, e os XMLs de tabela entram no checklist.

---

## Versionamento

Automático, mantido em `.historico-entregas.json` dentro da pasta `Documentacao`.
Primeira geração é `v1.0`; regerar sobe o minor, faz backup do anterior como
`Entrega - {NOME} v{anterior}.{ext}` e acrescenta as alterações informadas ao histórico,
que aparece como tabela no documento. HTML e DOCX do mesmo módulo versionam de forma
independente.

---

## Ativação

Dispara quando o usuário menciona "gerar documento de entrega", "documentar módulo do
addon", "gerar .html/.docx de entrega", "documentar o que foi entregue" ou "gerar
documentação Sankhya".

---

## Dependências Python

Instaladas sob demanda pelos próprios scripts, via `sys.executable -m pip`:

```
python-docx   — geração do .docx e leitura de escopo .docx
pdfplumber    — leitura de escopo em .pdf
```

O HTML não depende de nada além da stdlib.

---

## Manutenção

```bash
python scripts/test_geracao.py          # geradores HTML e DOCX
python scripts/revisar_texto.py --autoteste   # regras do lint de linguagem
```

O primeiro gera HTML e DOCX de exemplo em diretório temporário e valida escape, paleta
do Padrão 2026, versionamento, backup, histórico, o preenchimento do modelo v.4 e as
evidências embutidas nos dois formatos. O segundo confere
que as seis regras acusam e que campos de identificação e mensagens citadas continuam
fora do lint.
