# Coleta de evidências de homologação

Como capturar as telas que entram no documento de entrega. Nada aqui é obrigatório:
o documento sai igual com prints tirados à mão. A automação só poupa o trabalho.

Nunca presuma o que está instalado na máquina de quem roda a skill — cada colega tem
um ambiente. **Detecte antes de propor.**

---

## Qual base

A URL vem do usuário, sempre. Pergunte antes de abrir o navegador e confirme que é base
de teste ou homologação — print tirado em produção não volta atrás depois de entregue.

**Não existe URL padrão.** Cada colega roda a skill contra o ambiente do cliente dele:
servidor da unidade, VM, container, porta própria. `localhost:8080` é o ambiente de quem
escreveu esta referência, não um default.

Se o projeto declarar a URL em algum lugar (`docker-compose.yml`, `.env`, `README.md`,
`docs/`), ofereça o que achou como **sugestão a confirmar**, nunca como resposta pronta.
Não achou nada? Pergunte e espere — capturar contra uma URL adivinhada é pior do que não
capturar. `.sankhya-mcp.env`, comum nesses projetos, descreve o **banco**: host de Oracle
não é URL de navegador.

A URL entra como variável de ambiente (`SANKHYA_URL`), nunca escrita no script, e sem
valor de fallback: faltou a variável, o harness para e avisa.

---

## Ordem de preferência

| # | Ferramenta | Quando |
|---|---|---|
| 1 | **Extensão do navegador (`mcp__claude-in-chrome__*`)** | Você tem essas tools na sessão |
| 2 | **Playwright** | A extensão não existe, ou o projeto já tem harness em `tools/` |
| 3 | **Manual** | Nada disponível, ou o usuário prefere assim |

A extensão ganha porque usa a **aba já autenticada** do usuário: sem senha em script,
sem MFA, sem ambiente extra. O Playwright ganha em repetição e é o único que cobre
Firefox e Safari.

### Cobertura por navegador

| Navegador | Extensão Claude | Playwright |
|---|---|---|
| Chrome, Edge, Brave (Chromium) | sim | `chromium` (ou `channel: 'chrome'` / `'msedge'`) |
| Firefox | não existe | `firefox` |
| Safari | não existe | `webkit` (só macOS) |

Não há extensão Claude para Firefox nem Safari. Para esses dois, ou Playwright ou manual.

---

## Opção 1 — Extensão do navegador

Confirme que você tem as tools `mcp__claude-in-chrome__*` nesta sessão. Se não tiver,
não invente: passe para a opção 2 e diga ao usuário que a extensão Claude for Chrome
(Chrome Web Store) é a alternativa mais simples, para Chrome, Edge ou Brave.

Fluxo:

1. `tabs_context_mcp` — veja as abas abertas.
2. `tabs_create_mcp` + `navigate` até a URL do Sankhya. O usuário já está logado na
   sessão do navegador; se cair na tela de login, peça que ele entre e avise.
3. Navegue até a tela do caso de teste.
4. `computer` com `action: "screenshot"` e **`save_to_disk: true`** — o resultado traz
   o caminho do PNG gravado.
5. Mova o arquivo para `{PASTA_DEMANDA}/Documentacao/evidencias/` com o nome do caso
   (ver "Nomenclatura").

Nunca dispare ação destrutiva sem confirmar com o usuário a cada passo: metade dos
cenários de homologação é caminho negativo e grava dado na base.

---

## Opção 2 — Playwright

Detecte:

```bash
npx playwright --version        # ou: node -e "require('playwright')"
```

Não tem? Mostre o comando e **pergunte** antes de instalar:

```bash
npm install -D playwright && npx playwright install chromium   # firefox | webkit
```

Se o projeto já tem harness (`tools/fase5-e2e/*.js` nos módulos convertidos), reuse-o:
ele já sabe abrir as telas daquele módulo. Senão, escreva o mínimo — abrir, esperar,
capturar:

```js
const { chromium } = require('playwright');   // firefox | webkit conforme o navegador

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });

  // Sem default: a base é a do cliente de quem está rodando, não a de quem escreveu isto.
  const BASE = process.env.SANKHYA_URL;
  if (!BASE) throw new Error('defina SANKHYA_URL com a base onde capturar');
  await page.goto(BASE);
  // login, navegação até a tela, e então:
  await page.screenshot({ path: 'Documentacao/evidencias/hom-fc1-1.png' });
  await browser.close();
})();
```

### Login sem senha no código

O Playwright abre um perfil limpo, sem a sessão do usuário. **Não escreva credencial em
script, em `dados.json` ou em qualquer arquivo do repositório.** Abra em
`headless: false`, peça ao usuário para logar na janela e salve a sessão:

```js
await page.context().storageState({ path: '.auth/sankhya.json' });   // fora do git
```

Nas capturas seguintes, `browser.newContext({ storageState: '.auth/sankhya.json' })`
reabre já logado. Se o cliente exigir login automatizado, as credenciais vêm de variável
de ambiente em tempo de execução, nunca de arquivo versionado.

---

## Opção 3 — Manual

Peça ao usuário:

1. Tire os prints das telas de cada cenário.
2. Salve em `{PASTA_DEMANDA}/Documentacao/evidencias/`.
3. Nomeie pelo id do caso.

Você monta o `evidencias` no `dados.json` e escreve as legendas.

---

## Protocolo de captura no Sankhya

O que costuma estragar a captura, visto nos módulos convertidos da Zanchetta:

- **Popup de aviso sobre a tela.** Antes do print, feche os diálogos: procure botão
  `Ok`/`OK` visível na página **e em cada iframe** e clique. As telas `dynamicForm`
  moram dentro do iframe do `DynaformLauncher`.
- **Grade ainda carregando.** Espere as linhas aparecerem, não um tempo fixo.
- **Cursor sobre um botão** deixa tooltip e estado hover no print. Mova o ponteiro para
  uma área vazia e espere ~1s antes de capturar.
- **Tela rolada para colunas vazias.** A evidência útil costuma ser o formulário com a
  aba relevante aberta, não a grade em branco.
- **Resolução.** Viewport de 1600×900 ou maior; abaixo disso a tela do Sankhya corta.
- **Dado real.** Print de tela vazia não prova nada. Use a base com massa de teste e
  escolha um registro que exercite o cenário.

---

## Nomenclatura e legenda

O id do caso é `hom-fc{N}-{M}`: `N` é a posição da funcionalidade em `funcionalidades`,
`M` a posição do teste dentro dela. Nomeie o arquivo pelo caso — `hom-fc1-2.png` — e,
havendo mais de uma captura no mesmo caso, sufixe: `hom-fc1-2b.png`.

A legenda descreve **o que a imagem mostra**, com os dados que aparecem nela:

> "Entrada de Matéria Prima, aba Documentos da visita 9, com o documento 9900001
> importado e as ações Resolver Pedido/Produtos e Recusar Documento na barra da grade."

Não escreva "tela do sistema" nem repita o nome do teste. Vale o registro de
`linguagem.md` — a legenda é texto de entrega como qualquer outro.
