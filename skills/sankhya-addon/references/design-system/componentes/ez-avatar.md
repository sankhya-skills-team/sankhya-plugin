> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-avatar/ (snapshot 2026-09-28)

# Avatar

O componente **Avatar** tem a função de representar visualmente um usuário, exibindo uma imagem, letra inicial de seu nome ou um ícone, de acordo com a configuração realizada.

demo.js

```jsx
import { EzAvatar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const imgURL = "https://i.pinimg.com/736x/a0/5a/1d/a05a1d8ce76262357f6ea2a9db72a371.jpg"

  return (
    <div className="ez-flex" style={{gap: "16px", flexWrap: "wrap"}}>
      <EzAvatar imageSrc={imgURL}/>
      <EzAvatar name={"Cristiano"}/>
      <EzAvatar/>
    </div>
  );

};

export default Demo;
```

dica

A exibição do conteúdo respeitará a seguinte ordem de prioridade:

  1. **URL da imagem** (`imageSrc`) - se uma imagem for fornecida, ela será exibida.
  2. **Nome** (`name`) - caso não haja imagem, a letra inicial do nome será exibida.
  3. **Ícone padrão** \- se nenhuma imagem ou nome for fornecido, o ícone padrão será utilizado.

## Variações

### Tamanhos

O componente Avatar suporta diferentes tamanhos, que podem ser definidos por meio da propriedade `size`.

demo.js

```jsx
import { EzAvatar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const name = "Avatar"

  return (
    <div className="ez-flex" style={{gap: "16px", alignItems: "baseline", flexWrap: "wrap"}}>
      <EzAvatar name={name} size="320" />
      <EzAvatar name={name} size="300" />
      <EzAvatar name={name} size="280" />
      <EzAvatar name={name} size="260" />
      <EzAvatar name={name} size="240" />
      <EzAvatar name={name} size="220" />
      <EzAvatar name={name} size="200" />
      <EzAvatar name={name} size="180" />
      <EzAvatar name={name} size="160" />
      <EzAvatar name={name} size="140" />
      <EzAvatar name={name} size="120" />
      <EzAvatar name={name} size="100" />
      <EzAvatar name={name} size="80" />
      <EzAvatar name={name} size="60" />
    </div>
  );

};

export default Demo;
```

### Formatos

O componente Avatar pode ser exibido em dois formatos (quadrado ou redondo), controlados pela propriedade `shape`.

### Interatividade

A propriedade `isInteractive` adiciona interatividade ao componente Avatar, exibindo um feedback visual quando o mouse passa por cima.

demo.js

```jsx
import { EzAvatar } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const name = 'Avatar';

  return (
    <div className="ez-flex" style={{ gap: '16px', alignItems: 'baseline', flexWrap: 'wrap' }}>
      <EzAvatar name={name} isInteractive={true} />
      <EzAvatar name={name} />
    </div>
  );

};

export default Demo;
```

### Ícone a ser exibido

Por padrão, quando é exibido o avatar com ícone, é renderizado o ícone `account-outline`. Podemos personalizar isso através da propriedade `iconName`, informando o valor de um dos ícones disponíveis em nossa biblioteca.

Veja a lista completa de ícones.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| iconName | icon-name | Nome do ícone que deve ser exibido no avatar. | string | undefined |
| imageSrc | image-src | URL da imagem do Avatar. | string | undefined |
| isInteractive | is-interactive | Se true, o Avatar será interativo. Caso contrário, será estático. | boolean | false |
| name | name | Nome do usuário para exibição da inicial. | string | undefined |
| shape | shape | Define o formato do Avatar: 'circle' ou 'square'. | "circle" \| "square" | 'circle' |
| size | size | Tamanho do Avatar (valores permitidos): '320x320', '300x300', '280x280', '260x260', '240x240', '220x220', '200x200', '180x180', '160x160', '140x140', '120x120', '100x100', '80x80', '60x60'. | "100" \| "120" \| "140" \| "160" \| "180" \| "200" \| "220" \| "240" \| "260" \| "280" \| "300" \| "320" \| "60" \| "80" | '100' |

### Dependencies

#### Used by

  * ez-tile-medium

#### Depends on

  * ez-icon
