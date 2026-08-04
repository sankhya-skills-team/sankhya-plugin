# skill-sankhya-doc-entrega

Skill para Claude Code que gera o **documento de entrega de desenvolvimento** de projetos
Java Sankhya OM — Addon Studio ou Módulo Java complementar. Dois formatos, à escolha do
usuário: **HTML interativo** ou **DOCX Word**, ambos no design system Sankhya.

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
| **HTML interativo** (default) | Funcionalidades colapsáveis, checklist de deploy com persistência, homologação com marcação de status e evidências por imagem, histórico de versões, botão "Exportar com evidências" |
| **DOCX Word** | Documento editável: identificação, histórico de versões, manual de uso passo a passo, checklist de deploy em tabela, homologação com coluna de resultado e bloco de assinaturas |

---

## Estrutura

```
sankhya-doc-entrega/
├── SKILL.md                    Fluxo, perguntas e contrato do dados.json
├── assets/
│   └── sankhya-logo.png        Logo usado no DOCX
├── references/
│   ├── analise-fontes.md       Categorias de artefatos e linguagem funcional
│   └── design-system.md        Paleta, tipografia, regra HTML × DOCX, logo
└── scripts/
    ├── _brand.py               Cores, logo (SVG + PNG) e metadados de tipo
    ├── _comum.py               Entrada, versionamento, histórico, personas
    ├── gerar_html.py           dados.json → .html
    ├── gerar_docx.py           dados.json → .docx
    ├── ler_escopo.py           Extrai texto de .md/.txt/.docx/.pdf
    └── test_geracao.py         Auto-teste dos geradores
```

---

## Artefatos Java reconhecidos

| Interface / Classe | Tipo no ERP | Acionamento |
|---|---|---|
| `AcaoRotinaJava` | Botão de Ação | Manual — clique do usuário |
| `EventoProgramavelJava` | Listener / Evento | Automático — INSERT/UPDATE/DELETE |
| `ScheduledAction` | Ação Agendada | Automático — cron/horário |
| `Regra` / `RegraNegocioJava` | Regra de Negócio | Automático — ciclo de confirmação de NF |
| Classes com `CustomModuleLoader` | Padrão External (proxy) | Não geram entrada — viram observação de arquitetura |

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
python scripts/test_geracao.py
```

Gera HTML e DOCX de exemplo em diretório temporário e valida escape, paleta do design
system, versionamento, backup, histórico e presença do logo.
