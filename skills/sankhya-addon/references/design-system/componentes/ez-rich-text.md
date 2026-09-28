> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ (snapshot 2026-09-28)

# Rich Text

O `ez-rich-text` possibilita ao usuário, criar um conteúdo HTML permitindo não apenas sua edição, mas também sua pré-visualização.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

demo.js

```jsx
import React from 'react';

const Demo = () => {
  return (
    <ez-rich-text label={"Conteúdo HTML"}/>
  )
};

export default Demo;
```

Dica

Disponibilizamos alguns atalhos de teclado para deixar a navegação e usabilidade do componente mais fluida:

  * **Pré visualizar** : `Ctrl` \+ `P`
  * **Desfazer** : `Ctrl` \+ `Z`
  * **Refazer** : `Ctrl` \+ `X`
  * **Negrito** : `Ctrl` \+ `B`
  * **Itálico** : `Ctrl` \+ `I`
  * **Sublinhado** : `Ctrl` \+ `U`
  * **Lista** : `Ctrl` \+ `L`
  * **Inserir imagem** : `Ctrl` \+ `O`
  * **Inserir link** : `Ctrl` \+ `K`
  * **Quebra de linha** : `Ctrl` \+ `ENTER`

## Desabilitando Funcionalidades

Por padrão, todas as funcionalidades estão disponíveis no componente. Porém, para permitir uma maior customização e flexibilidade de uso, permitimos que grupos de funcionalidades possam ser desabilitadas programaticamente, conforme a necessidade, através de suas propriedades.

### Modo de pré-visualização

> Propriedade utilizada: `showPreview = false`.

Desabilita a funcionalidade de modo de pré-visualização.

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

demo.js

```jsx
import React from 'react';

const Demo = () => {
  return (
    <ez-rich-text label={"Conteúdo HTML sem preview"} show-preview={false}/>
  )
};

export default Demo;
```

### Desfazer e refazer

> Propriedade utilizada: `showUndoRedo = false`.

Desabilita da taskbar, as funcionalidades de _desfazer_ e _refazer_.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

### Formatação de texto

> Propriedade utilizada: `showTextFormat = false`.

Desabilita as funcionalidades de formatação em _negrito_ , _sublinhado_ e _itálico_.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

demo.js

```jsx
import React from 'react';

const Demo = () => {
  return (
    <ez-rich-text label={"Conteúdo HTML sem formatação de texto (negrito, itálico e sublinhado)"} show-text-format={false}/>
  )
};

export default Demo;
```

### Opções diversas

> Propriedade utilizada: `showConfigs = false`.

Desabilita as funcionalidades de _formatar lista_ , _inserir imagem_ e _inserir link_.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

### Desabilitando edição

> Propriedade utilizada: `enabled = false`.

Desabilita a edição do elemento, por padrão, todas as funcionalidades são desabilitadas, exceto o modo de **pré-visualização**.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

demo.js

```jsx
import React from 'react';

const Demo = () => {

  const value = `<strong> Edição de texto inativa</strong>`

  return (
    <ez-rich-text label={"Conteúdo HTML com edição inativa"} value={value} enabled={false}/>
  )
};

export default Demo;
```

## Eventos

### ezChange

Emitido sempre que há uma mudança na propriedade `value` do componente.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

Resultado gerado pelo HTML:

## Métodos

### Aplicar foco e blur

> Métodos usados: `setFocus` e `setBlur`.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

demo.js

```jsx
import React, { useRef, useState } from 'react';
import "./style.css";
import { EzRichText, EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

  const element = useRef(null);

  return (
    <div className="rich-text-container">
      <EzRichText label={'Conteúdo HTML'} ref={element} />
      <br />

      <div className="rich-text-actions">
        <EzButton label={"Aplicar Foco"} class="ez-button--primary" onClick={async () => {
          await element.current?.setFocus();
        }}/>

        <EzButton label={"Aplicar Blur"} onClick={() => {
          element.current?.setBlur();
        }}/>
      </div>
    </div>
  );
};

export default Demo;
```

Dica

O método `setFocus` sempre irá definir o `rich-text` para o modo de **edição** , para que consiga focar no `text-area`.

### Verificar se campo está inválido

> Método usado: `isInvalid`.

Este método retorna `true` caso haja uma mensagem de erro atribuída ao componente.

É bastante útil para validações em formulários, onde são necessários alguns pré-requisitos para validar uma informação.

Pré-visualizar

## Adicionar link

Insira um link no texto para abrir novas páginas.

## Upload de imagens

Envie seus arquivos preenchendo apenas 1 campo por vez.

OU

Arraste e solte ou clique para adicionar arquivos

Valor é inválido? NÃO
