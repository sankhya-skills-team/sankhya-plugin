# skill-sankhya-doc-entrega

Skill para Claude Code que gera automaticamente o **documento de entrega de desenvolvimento** (`.docx`) para projetos Java Sankhya OM — Addon Studio ou Módulo Java complementar.

---

## O que esta skill faz

Analisa os fontes Java de um módulo entregue, extrai funcionalidades e regras de negócio, e produz o arquivo `Documentacao/Entrega - {NOME_MODULO}.docx` formatado com logo Sankhya, tabelas de identificação, manual de uso, seção de homologação e bloco de assinaturas.

Nenhum arquivo de template externo é necessário — o script Python completo está embutido na skill.

---

## Estrutura da Skill

```
sankhya-doc-entrega/
├── SKILL.md                        Instruções principais e scripts Python
└── references/
    └── analise-fontes.md           Categorias de artefatos, regras de extração e linguagem funcional
```

---

## Artefatos Java Reconhecidos

| Interface / Classe | Tipo no ERP | Acionamento |
|---|---|---|
| `AcaoRotinaJava` | Botão de Ação | Manual — clique do usuário |
| `EventoProgramavelJava` | Listener / Evento | Automático — INSERT/UPDATE/DELETE |
| `ScheduledAction` | Ação Agendada | Automático — cron/horário |
| `Regra` | Regra de Negócio | Automático — ciclo de confirmação de NF |
| `RegraNegocioJava` | Regra de Negócio Avançada | Automático — with ciclo de vida (before/after) |
| Classes com `CustomModuleLoader` | Padrão External (proxy) | Indicam dois JARs registrados |

Classes com padrão External não geram entrada separada no documento — são mencionadas como observação de arquitetura.

---

## Fluxo de Execução

```
Etapa 0 — Confirmar pasta raiz do projeto
Etapa 1 — Coletar inputs (nome, pasta de fontes, escopo, caminho no sistema, cliente)
Etapa 2 — Analisar todos os .java recursivamente e classificar por tipo
Etapa 3 — Ler documento de escopo (se fornecido: .docx, .pdf ou .md)
Etapa 4 — Montar conteúdo em linguagem funcional (sem SQL, sem nomes de tabela)
Etapa 5 — Executar script Python para gerar o .docx
Etapa 6 — Retornar ao usuário com lista de funcionalidades documentadas
```

---

## Documento Gerado

O `.docx` contém:

1. Tabela de Identificação (cliente, FAP, responsável técnico, versão)
2. Objetivos
3. Descrição das Personalizações Realizadas
4. Manual de Uso das Customizações (acesso, funcionalidades passo a passo, limitações)
5. Homologação e Testes
6. Treinamento e Suporte
7. Anexos
8. Observações finais
9. Local, data e assinaturas (Líder, Gerente, Consultor, Solicitante)

---

## Ativação

A skill é ativada automaticamente quando o usuário menciona:

- "gerar documento de entrega"
- "criar documento de entrega de desenvolvimento"
- "documentar módulo do addon"
- "gerar .docx de entrega"
- "documentar o que foi entregue"
- "gerar documentação Sankhya"

Ou via comando:

```
/sankhya-doc-entrega
```

---

## Instalação

### Como skill standalone

```bash
git clone https://github.com/ratk/skill-sankhya-doc-entrega \
    ~/.claude/skills/sankhya-doc-entrega
```

### Como parte de um plugin

```
meu-plugin/
└── skills/
    └── sankhya-doc-entrega/
        ├── SKILL.md
        └── references/
```

---

## Dependências Python

O script instala automaticamente se necessário:

```
python-docx   — geração do .docx
pdfplumber    — leitura de PDF (opcional, para escopo em PDF)
```

---

## Licença

Uso interno — DSTech Soluções.
