> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile-medium/ (snapshot 2026-09-28)

# Tile Medium

O **Tile Medium** é um componente que pode ser utilizado para somente leitura ou acompanhado de um botão que pode enviar para uma página específica, contém tags para mostrar status, título e parágrafo configuráveis para atender a necessidade do time que for usar.

demo.js

```jsx
import { EzTileMedium } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const title = "Alerta de Performance do Time";
    const description = "Detectamos uma queda na performance de alguns membros da equipe — confira sugestões para manter a produtividade em alta.";

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
            <EzTileMedium
                titleText={title}
                iconName="warning-outline"
                iconColor="--color--petroleum-600"
                descriptionText={description}
                buttonProps={{
                    label: "Visualizar",
                    colors:{
                        background: '--color--petroleum-600',
                        backgroundHover: '--color--petroleum-700',
                        backgroundActive: '--color--petroleum-500',
                    },
                    onClick: () => {alert('Visualizar alerta de Performance')}
                }}
                tags={[
                    {
                        label: "Gestão de pessoas",
                        color: '--color--petroleum-600'
                    },
                    {
                        label: "Alerta",
                        color: '--color--red-600'
                    },
                    {
                        label: "BI"
                    }
                ]}
            ></EzTileMedium>
        </div>
    </div>
  );
};

export default Demo;
```

## Variações

### Tamanhos

O Tile Medium tem por padrão as dimensões fixas de `446px * 257px` O Tile Medium suporta altura e largura customizadas por padrão, que podem ser definidas por meio das propriedades `height` e `width`.

demo.js

```jsx
import { EzTileMedium } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ padding: '1rem', gap: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
      <EzTileMedium
        iconName="expand"
        smallTitleText="Variações"
        titleText="Tamanhos"
        descriptionText="Tamanho default"
      ></EzTileMedium>
      <EzTileMedium
        iconName="expand"
        smallTitleText="Variações"
        titleText="Tamanhos"
        descriptionText="Tile Medium com widtch 100% e height 170px"
        width='100%'
        height='170px'
        tags={[
            {
                label: "width: 100%"
            },
            {
                label: "height: 170px"
            }
        ]}
      ></EzTileMedium>
    </div>
  );
};

export default Demo;
```

### Cores

O Tile Medium possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio da propriedade `color`.

## Variações - Header

O header do Tile Medium pode ser construído de forma dinâmica. Do lado esquerdo podendo ser apresentado um ícone ou avatar. Do lado esquerdo podendo apresentar até 3 tags de cores diferentes.

### Ícone

O ícone, quando presente, fica do canto superior esquerdo do componente.

  * O ícone é definido pela propriedade `iconName`;
  * Uma cor customizada pode ser passada para o ícone pela propriedade `iconColor`, dentre as cores da paleta do Design System. Veja a paleta de cores...

demo.js

```jsx
import { EzTileMedium } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
            <EzTileMedium
                titleText="Icon Ausente"
                descriptionText="Icon Ausente"
            ></EzTileMedium>
            <EzTileMedium
                titleText="Icon Default"
                descriptionText="Icon Default"
                iconName="home"
            ></EzTileMedium>
            <EzTileMedium
                titleText="Icon Color"
                descriptionText="Icon Color"
                iconName="home"
                iconColor="--color--yellow-600"
            ></EzTileMedium>
        </div>
    </div>
  );
};

export default Demo;
```

### Avatar

O avatar, quando presente, fica do canto superior esquerdo do componente, substituindo o ícone quando este também for definido

  * O avatar é definido pela propriedade `avatarProps`, que é um objeto que define as propriedades do avatar, sendo elas:
    * `name?: string;` (Define a letra que será apresentada no avatar)
    * `shape?: 'circle' | 'square';` (Define o formato do avatar)
    * `imageSrc?: string;` (Define uma imagem a ser apresentada no avatar)

### Tags

As tag, quando presentes, ficam do canto superior direito do componente. O componente suporte de até 3 tags simultâneas.

  * A tags são definidos pela propriedade `tags`, que é array de objetos que define as propriedades do grupo de tags, sendo elas:
    * `label: string;` (Define a letra que será apresentada no avatar)
    * `color?: string;` (Define o formato do avatar)

demo.js

```jsx
import { EzTileMedium } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
            <EzTileMedium
                titleText="Tag padrão"
                iconName="warning-outline"
                tags={[{label: "tag default"}]}
            ></EzTileMedium>
            <EzTileMedium
                titleText="Limite de 3 tags"
                iconName="warning-outline"
                tags={[
                    {label: "tag 1"},
                    {label: "tag 2"},
                    {label: "tag 3"},
                    {label: "tag 4"},
                    {label: "tag 5"},
                ]}
            ></EzTileMedium>
            <EzTileMedium
                titleText="Tags coloridas"
                iconName="warning-outline"
                tags={[
                    {
                        label: "deafult",
                    },
                    {
                        label: "red",
                        color: "--color--red-600"
                    },
                    {
                        label: "yellow",
                        color: "--color--yellow-600"
                    },
                ]}
            ></EzTileMedium>
        </div>
    </div>
  );
};

export default Demo;
```

## Variações - Content

A seção de conteúdo do Tile Medium pode apresentar dinamicamente 3 níveis de texto (Título pequeno, Título principal e descrição) e um botão.

Caso algumas das propriedades que definem cada sub-seção não tenha valor, a mesma não será apresentada

### Textos

  * O Título Pequeno, pode ser passado por meio da variável `smallTitleText`
  * O Título Principal, pode ser passado por meio da variável `titleText`
  * A descrição, pode ser passado por meio da variável `descriptionText`

### Quantidade máxima de linhas

A quantidade máxima de linhas de texto apresentadas em cada seção pode ser definida através das propriedades:

  * Quantidade máxima de linhas do Título Pequeno, pode ser definida por meio da variável `smallTitleMaximumLines` (Padrão 1)
  * Quantidade máxima de linhas do Título Principal, pode ser definida por meio da variável `titleMaximumLines` (Padrão 1)
  * Quantidade máxima de linhas da descrição, pode ser definida por meio da variável `descriptionMaximumLines` (Padrão 3)

demo.js

```jsx
import { EzTileMedium } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";
  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
            <EzTileMedium
                smallTitleText={text}
                titleText={text}
                descriptionText={text}
                tags={[
                  {
                    label: "SmallTitle: Default"
                  },
                  {
                    label: "Title: Default"
                  },
                  {
                    label: "Description: Default"
                  }
                ]}
            ></EzTileMedium>
            <EzTileMedium
                smallTitleText={text}
                smallTitleMaximumLines={2}
                titleText={text}
                titleMaximumLines={2}
                descriptionText={text}
                descriptionMaximumLines={1}
                tags={[
                  {
                    label: "smallTitleMaximumLines: 2"
                  },
                  {
                    label: "titleMaximumLines: 2"
                  },
                  {
                    label: "descriptionMaximumLines: 1"
                  }
                ]}
            ></EzTileMedium>
        </div>
    </div>
  );
};

export default Demo;
```

### Botão

O botão, quando presente, fica do canto inferior esquerdo do componente.

  * O botão é definido pela propriedade `buttonProps`, que é um objeto que define as propriedades do ez-button, sendo elas:

```text
label: string;
enabled?: boolean;
mode?: 'regular' | 'icon' | 'link' | 'label-icon';
iconName?: string;
size?: 'x-small' | 'small' | 'medium' | 'large';
onClick: () => void;
colors?:{
  background?: string;
  backgroundHover?: string;
  backgroundActive?: string;
  text?: string;
  textHover?: string;
  textActive?: string;
}
```

## Métodos

### setFocus e setBlur

O Tile Medium pode receber ou remover foco de forma imperativa através dos métodos `setFocus` e `setBlur`.

Focado: **Não** O foco será removido automaticamente após 1 segundos

demo.js

```jsx
import { useRef, useState } from 'react';
import { EzTileMedium, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const title = "Alerta de Performance do Time";
    const description = "Detectamos uma queda na performance de alguns membros da equipe — confira sugestões para manter a produtividade em alta.";

    const element = useRef(null);
    const [isFocus, setIsFocus] = useState(false);

    const focusButton = () => {
        element.current.setButtonFocus();
    };

    const handleFocus = () => {
        setIsFocus(true);
        setTimeout(() => {
            element.current.setButtonBlur();
            setIsFocus(false);
        }, 1000);
    };

  return (
    <div class="ez-flex ez-flex--row ez-flex--justify-evenly ez-flex--align-items-center">
        <div class="ez-flex ez-flex--column ez-flex--justify-evenly ez-flex--align-items-center" style={{ gap: '1rem', padding: '1rem', backgroundColor: '#DEDEDE', width: '100%'}}>
            <EzTileMedium
                ref={element}
                onFocus={() => handleFocus()}
                titleText={title}
                iconName="warning-outline"
                iconColor="--color--petroleum-600"
                descriptionText={description}
                buttonProps={{
                    label: "Visualizar",
                    colors:{
                        background: '--color--petroleum-600',
                        backgroundHover: '--color--petroleum-700',
                        backgroundActive: '--color--petroleum-500',
                    },
                    onClick: () => {alert('Visualizar alerta de Performance')}
                }}
                tags={[
                    {
                        label: "Gestão de pessoas",
                        color: '--color--petroleum-600'
                    },
                    {
                        label: "Alerta",
                        color: '--color--red-600'
                    },
                    {
                        label: "BI"
                    }
                ]}
            ></EzTileMedium>

            <label className="ez-margin--medium">
                Focado: <strong>{isFocus ? "Sim" : "Não"}</strong>
            </label>
            <label className="ez-margin-top--small">O foco será removido automaticamente após 1 segundos</label>

            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center ez-gap--medium">
                <EzButton
                    label="Focar Botão"
                    className="ez-padding--medium"
                    onClick={focusButton}
                />
            </div>
        </div>
    </div>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| avatarProps | -- | Propriedade utilizada para configurar o avatar, se definida substitui o ícone por um ez-avatar | { name?: string; imageSrc?: string; shape?: "circle" \| "square"; } | undefined |
| buttonProps | -- | Define as props que serão passadas para o botão, caso o objeto seja passado, o botão será renderizado. | { label: string; enabled?: boolean; mode?: "link" \| "regular" \| "icon" \| "label-icon"; iconName?: string; size?: "small" \| "medium" \| "large" \| "x-small"; onClick: () => void; colors?: { background?: string; backgroundHover?: string; backgroundActive?: string; text?: string; textHover?: string; textActive?: string; }; } | undefined |
| color | color | Define a cor tema do componente. | "default" \| "gray" \| "green" \| "red" \| "yellow" | "default" |
| descriptionMaximumLines | description-maximum-lines | Define a quantidade máxima de linhas de texto a serem apresentadas na descrição. Quando a propriedade não é passada, limita a 3 linhas. | number | undefined |
| descriptionText | description-text | Texto a ser apresentado como descrição do componente | string | undefined |
| height | height | Define a altura do componente, sobrescrevendo o padrão de 257px. | string | undefined |
| iconColor | icon-color | Define uma cor customizada para o ícone, dentro da paleta de cores do Design System. Exemplo: "--color--yellow-600" | string | undefined |
| iconName | icon-name | Define o ícone a ser usado da biblioteca de ícones: ez-icons | string | undefined |
| smallTitleMaximumLines | small-title-maximum-lines | Define a quantidade máxima de linhas de texto a serem apresentadas no título pequeno. Quando a propriedade não é passada, limita a 1 linha. | number | undefined |
| smallTitleText | small-title-text | Texto a ser apresentado como um título pequeno do componente. | string | undefined |
| tags | -- | Define as props que serão passadas para as tags, caso um objeto seja passado, a(s) tag(s) será renderizada(s), se limitando a 3 tags. | { label: string; color?: string; }[] | undefined |
| titleMaximumLines | title-maximum-lines | Define a quantidade máxima de linhas de texto a serem apresentadas no título. Quando a propriedade não é passada, limita a 1 linha. | number | undefined |
| titleText | title-text | Texto a ser apresentado como título do componente. | string | undefined |
| width | width | Define a largura do componente, sobrescrevendo o padrão de 446px. | string | undefined |

### Methods

#### `setButtonBlur() => Promise<void>`

Remove o foco do botão.

##### Returns

Type: `Promise<void>`

#### `setButtonFocus() => Promise<void>`

Aplica o foco no botão.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-badge
  * ez-avatar
  * ez-icon
  * ez-button

### CSS Variables

| Variable | Description |
|---|---|
| --ez-tile-medium--width | Define a largura do componente. |
| --ez-tile-medium--height | Define a altura do componente. |
| --ez-tile-medium--padding | Define a margem do componente. |
| --ez-tile-medium--border-radius | Define o raio da borda do componente. |
| --ez-tile-medium--background-color | Define a cor do fundo. |
| --ez-tile-medium--color | Define a cor do title. |
| --ez-tile-medium--icon-color | Define a cor do ícone. |
| --ez-tile-medium--font-family | Define a família da fonte do title. |
| --ez-tile-medium--header-gap | Define o gap entre a seção de imagem e tags. |
| --ez-tile-medium--icon-line-height | Define a altura da linha do ícone. |
| --ez-tile-medium--tag-group-gap | Define o gap entre uma tag e outra. |
| --ez-tile-medium_button--background-color | Define a cor de fundo do botão. |
| --ez-tile-medium_button--color | Define a cor do label do botão. |
| --ez-tile-medium_button--hover--background-color | Define a cor de fundo quando o cursor está sobre o botão. |
| --ez-tile-medium_button--hover-color | Define a cor do texto e do ícone quando o cursor está sobre o botão. |
| --ez-tile-medium_button--active--background-color | Define a cor do fundo ao ativar o botão. |
| --ez-tile-medium_button--active-color | Define a cor do texto e do ícone ao ativar o botão. |
