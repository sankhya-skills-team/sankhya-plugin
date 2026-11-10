# sankhya-gera-escopo

Skill para Claude Code que gera o **documento de escopo** de uma demanda Sankhya em Word (`.docx`), no modelo padrão, com formatação, fonte e estilos já definidos.

## O que esta skill faz

- Recebe o contexto geral da demanda e estrutura o conteúdo nas seções do modelo de escopo
- Preenche o template Word mantendo estilos, fontes e formatação
- Gera o `.docx` final por script, a partir de um JSON de conteúdo
- Converte `.docx` em Markdown quando é preciso ler um documento existente

## Quando acionar

> criar documento de escopo · gerar documento de escopo · proposta técnica de escopo · escopo Sankhya no modelo padrão · gerar DOCX de escopo · modelo v2 de escopo

## Estrutura da skill

```
sankhya-gera-escopo/
├── SKILL.md                            Instruções da skill (carregadas pelo Claude Code)
├── README.md                           Este arquivo
├── assets/
│   └── escopo-template.docx            Modelo Word do documento de escopo
├── examples/
│   └── conteudo-exemplo.json           Exemplo do JSON de conteúdo
├── references/
│   ├── estrutura-documento.md          Seções e estrutura do documento
│   └── metodo-escopo.md                Método para levantar e escrever o escopo
└── scripts/
    ├── create_scope_docx.py            Gera o .docx a partir do JSON
    └── docx_to_markdown_fallback.py    Converte .docx em Markdown
```

## Skills relacionadas

- `sankhya-estimativa-planejador`: transforma o escopo em backlog e estimativa de horas
- `sankhya-doc-entrega`: documento de entrega, depois do desenvolvimento
