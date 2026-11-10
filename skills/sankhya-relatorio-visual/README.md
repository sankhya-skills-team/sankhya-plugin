# sankhya-relatorio-visual

Skill para Claude Code com o **padrão visual da DSTech** para relatório, etiqueta e comprovante JasperReports (`.jrxml`, iReport) no Sankhya.

## O que esta skill faz

- Define página e grid, tipografia Calibri e paleta petróleo/verde
- Monta o cabeçalho com logo do cliente e o rodapé com selo DSTech e "Página X de Y"
- Traz as peças prontas: cartões, rótulo e valor, tabela com zebra, grupo com total, destaque com legenda e assinaturas
- Garante leitura em P&B: destaque nunca só por cor
- Tem variante segura para exportar para Excel e etiqueta com código de barras
- Evita os erros silenciosos do Jasper: texto que some por altura baixa, negrito perdido no PDF, nulo e escape em `markup="styled"`

## Quando acionar

> criar relatório · montar impressão · layout do relatório · relatório feio · logo no relatório · negrito não aparece no PDF · cabeçalho · rodapé · zebra · agrupamento · exportar para Excel · etiqueta com código de barras

Entra sempre que for criar, redesenhar, revisar ou ajustar o layout de um `.jrxml`.

## Estrutura da skill

```
sankhya-relatorio-visual/
├── SKILL.md                         Instruções da skill (carregadas pelo Claude Code)
├── README.md                        Este arquivo
├── assets/
│   ├── dstech-selo.b64              Selo DSTech (PNG em base64)
│   └── logo-placeholder.b64         Logo provisória "LOGO DO CLIENTE" (PNG em base64)
├── references/
│   ├── pagina-e-grid.md             Medidas de página, cabeçalho, cartões, tabela, grupo, rodapé e etiqueta
│   ├── pecas.md                     Trecho XML pronto de cada peça
│   ├── marca-dstech.md              Paleta, cores semânticas, P&B e uso do selo
│   ├── tipografia.md                Fonte, escala de tamanhos e altura mínima
│   ├── texto-e-dados.md             Corte com reticências, nulo, número, data, CNPJ/CPF e escape
│   ├── logo-e-selo.md               Como trocar a logo do cliente e embutir o selo
│   ├── xls.md                       Variante segura para Excel
│   └── checklist.md                 Conferência antes de entregar
└── templates/
    ├── retrato-agrupado.jrxml       Documento com itens agrupados (nota, pedido, ordem)
    ├── paisagem-listagem-xls.jrxml  Listagem por período que exporta para Excel
    └── etiqueta-codigo.jrxml        Etiqueta com Code128, até 3 por folha A4
```

## Skills relacionadas

- `sankhya-relatorio`: parâmetros, SQL, subreport, compilação, deploy e cadastro. Esta skill prevalece em tudo que é aparência
- `sankhya-bi`: dashboard e gadget, não documento imprimível
