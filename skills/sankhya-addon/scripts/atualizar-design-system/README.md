# Atualizar o snapshot do Design System

Regenera `references/design-system/` (exceto `guia.md`) a partir do site oficial.

O HTML estático do site não contém os exemplos de código: eles ficam atrás do botão "Apresentar código" e só existem após o JS rodar. Por isso a coleta usa um navegador headless.

## Pré-requisitos

- Node 18+ e Python 3.10+
- Pasta de trabalho temporária (fora do repositório)

```sh
cd <pasta-temporaria>
npm init -y && npm i playwright && npx playwright install chromium
pip install --target lib beautifulsoup4 html2text
```

## Execução

```sh
node <skill>/scripts/atualizar-design-system/render.mjs        # ~10 min; gera raw/*.html
python <skill>/scripts/atualizar-design-system/tomd.py         # gera site/*.md (tabelas e código preservados)
python <skill>/scripts/atualizar-design-system/organizar.py site novo AAAA-MM-DD
```

Depois:

1. Compare `novo/` com `references/design-system/` (ex.: `git diff --no-index`).
2. Substitua o conteúdo gerado, **preservando `guia.md`**.
3. Revise o `guia.md` contra o diff, principalmente a seção 5 (armadilhas da doc oficial).

`tomd.py` espera as bibliotecas Python em `./lib` (instaladas com `--target lib`).
