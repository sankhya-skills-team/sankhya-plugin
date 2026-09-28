> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-empty-card/ (snapshot 2026-09-28)

# Empty Card

O Empty Card é um componente base utilizado com um container para outros conteúdos, podendo ser utilizado de base para criação de novos componentes ou como uma forma padronizada de acomodar outros componentes.

Nome.UsuárioProgramador senior

Conteúdo 1Conteúdo 2Conteúdo 3

demo.js

```jsx
import React from 'react';
import { EzEmptyCard, EzAvatar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    return (
        <div class="ez-flex ez-flex--justify-evenly" style={{ padding: '1rem', backgroundColor: '#DEDEDE'}}>
            <EzEmptyCard
                width={425}
                height={258}
            >
                <div class="ez-flex ez-flex--column ez-flex--justify-between" style={{height: "100%"}}>
                    <div className="ez-flex" style={{gap: "16px", alignItems: "center"}}>
                        <EzAvatar shape="square" size="60" />
                        <div className="ez-flex ez-flex--column">
                            <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--xxlarge)", lineHeight:"var(--line-height--32)", fontWeight: "var(--font-weight--regular)", color: "var(--color--petroleum-500)"}}>Nome.Usuário</span>
                            <span style={{fontFamily: "var(--font-family)", fontSize: "var(--font-size--default)", lineHeight:"var(--line-height--24)", fontWeight: "var(--font-weight--regular)", color: "var(--color--petroleum-300)"}}>Programador senior</span>
                        </div>
                    </div>
                    <div className="ez-flex" style={{gap: "9px", alignItems: "center"}}>
                        <EzEmptyCard
                            color="green"
                            width={120}
                            height={134}
                        >
                            <span>Conteúdo 1</span>
                        </EzEmptyCard>
                        <EzEmptyCard
                            color="green"
                            width={120}
                            height={134}
                        >
                            <span>Conteúdo 2</span>
                        </EzEmptyCard>
                        <EzEmptyCard
                            color="green"
                            width={120}
                            height={134}
                        >
                            <span>Conteúdo 3</span>
                        </EzEmptyCard>
                    </div>
                </div>
            </EzEmptyCard>
        </div>
    )
};

export default Demo;
```

## Variações

### Tamanhos

O Empty Card tem por padrão as dimensões de 335px x 155px, que podem ser modificadas através das propriedades `width` e `height`.

Empty card: default
width: (default) 335px
height: (default) 155px  Empty card: default
width: 200px
height: (default) 155px

Empty card: default
width: (default) 335px
height: 200px  Empty card: default
width: 200px
height: 200px

demo.js

```jsx
import React from 'react';
import { EzButton, EzEmptyCard } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
  <>
    <div class="ez-flex ez-flex--justify-evenly" style={{ padding: '1rem', backgroundColor: '#DEDEDE'}}>
      <EzEmptyCard>
        <span> Empty card: default </span>
        <br/>
        <span> width: (default) 335px </span>
        <br/>
        <span> height: (default) 155px </span>
      </EzEmptyCard>
      <EzEmptyCard
        width={200}
      >
        <span> Empty card: default </span>
        <br/>
        <span> width: 200px </span>
        <br/>
        <span> height: (default) 155px </span>
      </EzEmptyCard>
    </div>
    <div class="ez-flex ez-flex--justify-evenly" style={{ padding: '1rem', backgroundColor: '#DEDEDE'}}>
    <EzEmptyCard
      height={200}
    >
      <span> Empty card: default </span>
      <br/>
      <span> width: (default) 335px </span>
      <br/>
      <span> height: 200px </span>
    </EzEmptyCard>
    <EzEmptyCard
      width={200}
      height={200}
    >
      <span> Empty card: default </span>
      <br/>
      <span> width: 200px </span>
      <br/>
      <span> height: 200px </span>
    </EzEmptyCard>
  </div>
</>
);

export default Demo;
```

### Cores

O Empty Card possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio da propriedade `color`.

Empty card: default

Empty card: gray

Empty card: green

Empty card: yellow

Empty card: red

Empty card: petroleum

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| color | color | Define a cor tema do componente. | "default" \| "gray" \| "green" \| "petroleum" \| "red" \| "yellow" | "default" |
| height | height | Define o tamanho do componente, sobrescrevendo o padrão da propriedade size. | number \| string | undefined |
| width | width | Define a largura do componente, sobrescrevendo o padrão da propriedade size. | number \| string | undefined |

### CSS Variables

| Variable | Description |
|---|---|
| --ez-empty-card--width | Define a largura do componente. |
| --ez-empty-card--height | Define a altura do componente. |
| --ez-empty-card--padding | Define a margem do componente. |
| --ez-empty-card--border-radius | Define o raio da borda do componente. |
| --ez-empty-card--background-color | Define a cor de fundo do componente. |
