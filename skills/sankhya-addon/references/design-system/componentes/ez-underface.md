> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-underface/ (snapshot 2026-09-28)

# Underface

O Underface é um componente base utilizado como um fundo para outros conteúdos, podendo ser utilizado de base para criação de novos componentes ou como uma forma padronizada de acomodar outros conteúdos.

Seja um parceirocomercial

Seja um parceiro comercial Sankhya, acesse o PortalDeveloper e tenha outros benefícios

demo.js

```jsx
import React from 'react';
import { EzUnderface, EzButton, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    return (
        <div class="ez-flex ez-flex--justify-evenly">
        <EzUnderface
                height={430}
                color="ocean-green"
            >
            <div class="ez-flex ez-flex--column ez-flex--align-items-center ez-flex--justify-center" style={{height: "100%", gap: "16px"}}>
                <div className="ez-flex ez-flex--column ez-flex--align-items-center ez-flex--justify-center">
                        <span style={{fontFamily: "Roboto", fontSize: "70px", lineHeight:"78px", fontWeight: "600", color: "#F9F9F9"}}>Seja um parceiro</span>
                        <span style={{fontFamily: "Roboto", fontSize: "70px", lineHeight:"78px", fontWeight: "600", color: "#F9F9F9"}}>comercial</span>
                </div>
                <div className="ez-flex ez-flex--column ez-flex--align-items-center">
                    <span style={{fontFamily: "Roboto", fontSize: "16px", lineHeight:"28px", fontWeight: "400", color: "#FFFFFF"}}>Seja um parceiro comercial Sankhya, acesse o Portal</span>
                    <span style={{fontFamily: "Roboto", fontSize: "16px", lineHeight:"28px", fontWeight: "400", color: "#FFFFFF"}}>Developer e tenha outros benefícios</span>
                </div>
                <div className="ez-flex">
                    <EzButton label="Quero me cadastrar" size="large">
                        <EzIcon className="ez-margin-left--small" slot="rightIcon" iconName="arrow-forward"></EzIcon>
                    </EzButton>
                </div>
            </div>
        </EzUnderface>
        </div>
    )
};

export default Demo;
```

## Variações

### Tamanhos

O Underface tem por padrão as dimensões de 693px x 247px, que podem ser modificadas através das propriedades `width` e `height`.

Default size
width: (default) 693px
height: (default) 247px  Custom size
width: 200px
height: 150px

### Cores

O Underface possui 6 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio da propriedade `color`.

Underface: default

Underface: light-green

Underface: green

Underface: light-gray

Underface: dark-petroleum

Underface: ocean-green

demo.js

```jsx
import { EzUnderface } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <>
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center ez-flex--justify-center" style={{ gap: '8px', padding: '1rem', backgroundColor: '#DEDEDE'}}>
            <EzUnderface>
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "white"}}> Underface: default</span>
                </div>
            </EzUnderface>
            <EzUnderface
                color="light-green"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "var(--color--petroleum-500)"}}> Underface: light-green</span>
                </div>
            </EzUnderface>
            <EzUnderface
                color="green"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "white)"}}> Underface: green</span>
                </div>
            </EzUnderface>
            <EzUnderface
                color="light-gray"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "var(--color--petroleum-500)"}}> Underface: light-gray</span>
                </div>
            </EzUnderface>
            <EzUnderface
                color="dark-petroleum"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "white"}}> Underface: dark-petroleum</span>
                </div>
            </EzUnderface>
            <EzUnderface
                color="ocean-green"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "white"}}> Underface: ocean-green</span>
                </div>
            </EzUnderface>
        </div>
    </>
  );
};

export default Demo;
```

Além disso qualquer token de cor disponível na paleta de cores do Design System está disponível para ser utilizada através da propriedade `customColor`

customColor="--color--yellow-600"

customColor="--color--red-800"

demo.js

```jsx
import { EzUnderface } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <>
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center ez-flex--justify-center" style={{ gap: '8px', padding: '1rem', backgroundColor: '#DEDEDE'}}>
            <EzUnderface
                customColor="--color--yellow-600"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)"}}> customColor="--color--yellow-600"</span>
                </div>
            </EzUnderface>
            <EzUnderface
                customColor="--color--red-800"
            >
                <div className="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center">
                    <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "white"}}> customColor="--color--red-800"</span>
                </div>
            </EzUnderface>
        </div>
    </>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| color | color | Define a cor de fundo do componente. | "dark-petroleum" \| "default" \| "green" \| "light-gray" \| "light-green" \| "ocean-green" | "default" |
| customColor | custom-color | Define uma cor de fundo customizada, dentro da paleta de cores do Design System, sobrescrevendo a propriedade color. Exemplo: "--color--yellow-600" | string | undefined |
| height | height | Define a altura do componente. | number | undefined |
| width | width | Define a largura do componente. | number | undefined |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-underface--width | Define a largura do componente. |
| --ez-underface--height | Define a altura do componente. |
| --ez-underface--padding | Define o padding do componente. |
| --ez-underface--border-radius | Define o raio da borda do componente. |
