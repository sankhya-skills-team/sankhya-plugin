> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-list-item/ (snapshot 2026-09-28)

# List Item

O **List Item** é um componente versátil utilizado para exibir informações de forma estruturada em listas.

Ele pode conter título, descrição e um ícone à direita, todos opcionais. O componente pode ser empilhado vertical ou horizontalmente e usado tanto para exibição de informações quanto como item interativo.

Título

Texto do item

```jsx
import { EzListItem } from '@sankhyalabs/ezui/react/components';
import './demo.css';

const Demo = () => {

  return (
    <div className={'item-list-demo__container'}>
      <div className={'item-list__width-300'}>
        <EzListItem titleText={'Título'} text={'Texto do item'} iconName={'arrow-forward'} />
      </div>
    </div>
  );

};

export default Demo;
```

## Tamanho

O componente está configurado como `display: flex`, `width: 100%` e `min-width: 150px`, fazendo com que sua **largura** acompanhe a **largura** do elemento **pai** , mantendo o tamanho mínimo de 150px.

Largura

250px

Largura

400px

Largura mínima

150px

demo.js

```jsx
import { EzListItem } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (

    <div className={"item-list-demo__container"}>
      <div className={'item-list__width-250'}>
        <EzListItem titleText={'Largura'} text={'250px'} iconName={'arrow-forward'} />
      </div>

      <div className={'item-list__width-400'}>
        <EzListItem titleText={'Largura'} text={'400px'} iconName={'arrow-forward'} />
      </div>

      <div className={'item-list__width-150'}>
        <EzListItem titleText={'Largura mínima'} text={'150px'} iconName={'arrow-forward'} />
      </div>
    </div>
  );

};

export default Demo;
```

## Propriedades

dica

Todas as propriedades do **Item List** são **opcionais**.

### title

Define o título do item da lista. É um texto curto que descreve o conteúdo principal do item.

Título do item

### textTitle

Define o texto descritivo do item da lista. É um texto mais longo que complementa o título, fornecendo informações adicionais.

Texto complementar do ítem, se comportando como uma breve descrição

demo.js

```jsx
import { EzListItem } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  return (

    <div className={"item-list-demo__container"}>
      <div className={'item-list__width-300'}>
        <EzListItem text={'Texto complementar do ítem, se comportando como uma breve descrição'} />
      </div>
    </div>
  );

};

export default Demo;
```

### iconName

Define o nome do ícone a ser exibido no item da lista. O ícone é exibido à direita do título e do texto, se fornecidos.

Ítem da lista

Ítem da lista

Ítem da lista
