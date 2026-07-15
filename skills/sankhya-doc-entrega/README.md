# skill-sankhya-doc-entrega

Skill para Claude Code que gera automaticamente o **documento de entrega de desenvolvimento** para projetos Java Sankhya OM — Addon Studio ou Módulo Java complementar. Gera em **dois formatos, à escolha do usuário**: HTML interativo ou DOCX Word.

---

## O que esta skill faz

Analisa os fontes Java de um módulo entregue, extrai funcionalidades e regras de negócio em linguagem funcional (sem SQL, sem nomes de tabela), e produz o arquivo `Documentacao/Entrega - {NOME}.{html|docx}`.

A análise dos fontes e a leitura do escopo são idênticas nos dois formatos; só a coleta de inputs extras e a geração final ramificam por formato. Nenhum arquivo de template externo é necessário — os scripts Python completos estão embutidos na skill.

---

## Formatos

| Formato | Conteúdo |
|---|---|
| **HTML interativo** (default) | Funcionalidades colapsáveis, testes de homologação com marcação de status e evidências por imagem, checklist de deploy, versionamento automático, botão "Exportar com evidências". |
| **DOCX Word** | Documento editável no Word: tabela de identificação, manual de uso passo a passo, homologação em texto e bloco de assinaturas. Fluxo enxuto (sem homologação interativa, deploy-scan nem personas). |

O formato é perguntado logo após confirmar a pasta raiz (Etapa 0.5).

---

## Estrutura da Skill

```
sankhya-doc-entrega/
├── SKILL.md                 Instruções principais e scripts Python (HTML e DOCX)
├── sankhya_logo.png         Logo (asset)
└── references/
    └── analise-fontes.md    Categorias de artefatos, regras de extração e linguagem funcional
```

---

## Artefatos Java Reconhecidos

| Interface / Classe | Tipo no ERP | Acionamento |
|---|---|---|
| `AcaoRotinaJava` | Botão de Ação | Manual — clique do usuário |
| `EventoProgramavelJava` | Listener / Evento | Automático — INSERT/UPDATE/DELETE |
| `ScheduledAction` | Ação Agendada | Automático — cron/horário |
| `Regra` / `RegraNegocioJava` | Regra de Negócio | Automático — ciclo de confirmação de NF |
| Classes com `CustomModuleLoader` | Padrão External (proxy) | Não geram entrada separada — mencionadas como observação de arquitetura |

---

## Ativação

A skill é ativada automaticamente quando o usuário menciona:

- "gerar documento de entrega", "criar documento de entrega de desenvolvimento"
- "documentar módulo do addon", "documentar o que foi entregue"
- "gerar .html de entrega" ou "gerar .docx de entrega"
- "gerar documentação Sankhya"

---

## Dependências Python

Instaladas automaticamente se necessário:

```
python-docx   — geração do .docx
pdfplumber    — leitura de PDF (opcional, para escopo em PDF)
```
