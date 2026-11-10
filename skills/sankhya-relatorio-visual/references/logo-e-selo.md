# Logo do cliente e selo DSTech

## Padrão: base64 embutido

A logo do cliente vai **dentro do `.jrxml`**, em base64, numa variável. Não depende de arquivo no servidor nem de
parâmetro novo, e funciona igual em qualquer ambiente (teste, produção, Cloud).

```xml
<variable name="V_LOGO" class="java.awt.Image" calculation="System">
	<initialValueExpression><![CDATA[javax.imageio.ImageIO.read(new java.io.ByteArrayInputStream(java.util.Base64.getDecoder().decode("iVBORw0KGgo...")))]]></initialValueExpression>
</variable>
<variable name="V_SELO" class="java.awt.Image" calculation="System">
	<initialValueExpression><![CDATA[javax.imageio.ImageIO.read(new java.io.ByteArrayInputStream(java.util.Base64.getDecoder().decode("...conteúdo de assets/dstech-selo.b64...")))]]></initialValueExpression>
</variable>
```

```xml
<image scaleImage="RetainShape" hAlign="Left" vAlign="Middle" onErrorType="Blank">
	<reportElement x="0" y="4" width="140" height="22"/>
	<imageExpression class="java.awt.Image"><![CDATA[$V{V_LOGO}]]></imageExpression>
</image>
```

Os templates já vêm com a logo placeholder ("LOGO DO CLIENTE", `assets/logo-placeholder.b64`) e o selo
(`assets/dstech-selo.b64`). Para entregar, **troque só a string dentro de `decode("…")` da `V_LOGO`**.

**Sem a logo do cliente:** peça antes de entregar. O placeholder serve para prévia e homologação; em produção nunca
vai com ele nem com a logo de outro cliente. Se o pedido não trouxe logo, gere com o placeholder e diga na
resposta que falta a logo.

### Preparar a logo do cliente

1. Pegue a logo em PNG (ou SVG convertido para PNG), **horizontal**, fundo branco ou transparente.
2. **Recorte** as bordas vazias e reduza para ~600 px de largura. Com 16 a 32 cores o arquivo fica em 2–8 KB.
3. Gere o base64 numa linha só:
   - macOS/Linux: `base64 -i logo.png | tr -d '\n' > logo.b64`
   - Windows (PowerShell): `[Convert]::ToBase64String([IO.File]::ReadAllBytes("logo.png")) | Set-Content -NoNewline logo.b64`
4. Cole o conteúdo de `logo.b64` no lugar do base64 da `V_LOGO`.

Limite: o literal Java aguenta **64 KB**. Logo acima de ~40 KB em base64 é sinal de imagem grande demais: reduza.
JPG funciona (o `ImageIO` lê), mas PNG recortado fica menor e sem borda cinza.

### Tamanho e posição

| lugar | caixa (w × h) | alinhamento |
|---|---|---|
| cabeçalho página 1, retrato | 140 × 22 | esquerda, centro vertical |
| cabeçalho página 1, paisagem | 106 × 22 | esquerda |
| cabeçalho página 2+ | 100 × 16 (paisagem: 106 × 16) | esquerda |
| etiqueta | 90 × 14 | direita |

`scaleImage="RetainShape"`: a logo nunca distorce; logo quadrada fica pequena na caixa, o que é aceitável. Se o cliente
só tem logo quadrada, use caixa 40 × 26 e encoste o fio vertical nela.

## Variante: logo por empresa (`PDIR_MODELO`)

Para cliente com **várias empresas e uma logo por empresa**, leia a logo da pasta do modelo e caia no base64 se o
arquivo não existir:

```xml
<parameter name="PDIR_MODELO" class="java.lang.String" isForPrompting="false"/>
```

```xml
<imageExpression class="java.awt.Image"><![CDATA[$P{PDIR_MODELO} != null && new java.io.File($P{PDIR_MODELO}, "logo.png").isFile() ? javax.imageio.ImageIO.read(new java.io.File($P{PDIR_MODELO}, "logo.png")) : $V{V_LOGO}]]></imageExpression>
```

Com a pasta, usa o arquivo; com pasta inexistente, usa o base64 sem erro.
Antes de adotar, confirme no servidor do cliente qual pasta o `PDIR_MODELO` aponta e o nome do arquivo de logo
de cada empresa antes de adotar. Em relatório existente, `PDIR_MODELO` é parâmetro novo: só acrescente se o relatório
já não o tiver e o cliente realmente for multiempresa.

## Selo DSTech

- Regra do time: **em todo relatório**, no rodapé, à esquerda, caixa 50 × 12 (etiqueta: 38 × 9, fora da moldura).
- Sempre em base64 (`V_SELO`), nunca por arquivo.
- Não recolorir, não esticar, não pôr ao lado da logo do cliente no cabeçalho.
