> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-navigator/ (snapshot 2026-09-28)

# Sidebar Navigator

O **Sidebar Navigator** é um componente de navegação lateral que pode funcionar de três maneiras: flutuante, fixo ou dinâmico.

O comportamento do menu pode ser configurado para abrir ao passar o mouse sobre o **SidebarButton** (modo flutuante) ou ao clicar nele (modo fixo). No modo dinâmico (padrão), o menu começa como flutuante, mas pode ser fixado conforme o desejo do usuário.

```jsx
import './demo.css';

import React from 'react';
import { EzSidebarNavigator, EzTree } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    return (
        <div className="ez-flex sidebarNavigator__container">
            <EzSidebarNavigator className="ezSidebarNavigator">
                <EzTree items={items} />
            </EzSidebarNavigator>
        </div>
    )
};

export default Demo;

const items = [
	{
		id: "4654321",
		label: "Geral",
		expanded: true,
		children: [
			{
				id: "4654322",
				label: "Endereço",
				children: [
					{ id: "4654331", label: "Pendencias", disabled: true }
				]
			}
		]
	}
];
```

## Propriedades (Props)

### `type`

  * Tipo: `TypeMenuEnum`

  * Padrão: `'dynamic'` Define o comportamento do menu:

  * **`float`** : O menu é aberto ao passar o mouse sobre o **SidebarButton**.

  * **`fixed`** : O menu é fixo e precisa ser aberto/fechado manualmente ao clicar no **SidebarButton**.

  * **`dynamic`** (padrão): Inicia no modo flutuante, mas pode ser fixado pelo usuário.

### `mode`

  * Tipo: `ModeMenuEnum`
  * Padrão: `'float'`

Define o modo inicial do menu: `'float'` ou `'fixed'`.

### `size`

  * Tipo: `SizeMenuEnum`
  * Padrão: `'small'`

Controla a largura do menu, com três opções:

  * **`small`** : 240px de largura.
  * **`medium`** : 280px de largura.
  * **`large`** : 320px de largura.

Por padrão o componente utiliza a altura total da tela, mas é possível definir uma altura fixa utilizando a variavel de estilo `--ez-sidebar-navigator--height`

### `isResponsive`

  * Tipo: `boolean`
  * Padrão: `false`

Define se a largura do menu é ajustada automaticamente com base no tamanho da tela:

  * **Até 768px** : utiliza o tamanho `small`.
  * **Até 992px** : utiliza o tamanho `medium`.
  * **Acima de 1200px** : utiliza o tamanho `large`.

### `titleMenu`

  * Tipo: `string`

Define o título do **Sidebar Navigator**. Se não for especificado, o conteúdo ocupará o espaço do título.

### `showCollapseMenu`

  * Tipo: `boolean`
  * Padrão: `true`

Permite ocultar o botão de recolher o menu.

### `showFixedButton`

  * Tipo: `boolean`
  * Padrão: `true`

Permite ocultar o botão que fixa o menu no modo dinâmico.

demo.js

```jsx
import './demo.css';

import React, { useState } from 'react';
import { EzButton, EzSidebarNavigator, EzTree } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
	const [collapseMenu, setCollapseMenu] = useState(true);
	const [responsive, setResponsive] = useState(false);
	const [mode, setMode] = useState('float');

	const changeMode = () => {
		if (mode === 'float') {
			setMode('fixed')
		} else {
			setMode('float')
		}
	}
    return (
        <div className="ez-flex sidebarNavigator__container">
            <EzSidebarNavigator
				className="ezSidebarNavigator"
				titleMenu="Defina um titulo"
				size="md"
				mode={mode}
				isResponsive={responsive}
				showCollapseMenu={collapseMenu}
				showFixedButton={false}
			>
                <EzTree items={items} />
            </EzSidebarNavigator>
			<div className="ez-flex ez-flex--justify-evenly ez-flex--column ez-flex--align-items-center">
				<EzButton
					className="ez-margin-horizontal--auto ez-margin-top--medium"
					onClick={() => setCollapseMenu(!collapseMenu)}
					label="Exibe Collapsar"
					enabled={mode === 'fixed'}
				/>
				<EzButton
					className="ez-margin-horizontal--auto ez-margin-top--medium"
					onClick={() => setResponsive(!responsive)}
					label="Responsivo"
				/>
				<EzButton
					className="ez-margin-horizontal--auto ez-margin-top--medium"
					onClick={changeMode}
					label={`Alterar para o modo ${mode === 'fixed' ? 'flutuante' : 'fixo'}`}
				/>
			</div>
        </div>
    )
};

export default Demo;

const items = [
	{
		id: "4654321",
		label: "Geral",
		expanded: true,
		children: [
			{
				id: "4654322",
				label: "Endereço",
				children: [
					{ id: "4654331", label: "Pendencias", disabled: true }
				]
			}
		]
	}
];
```

## Slots

O **Sidebar Navigator** disponibiliza os seguintes slots para personalização:

  * **start** : Conteúdo no início do cabeçalho.
  * **content** : Espaço principal no cabeçalho. Se o `titleMenu` for definido, o conteúdo desse slot será posicionado abaixo do título.
  * **end** : Conteúdo no final do cabeçalho.
  * **footer** : Conteúdo do rodapé do menu.

## Eventos

Quando há uma mudança de modo entre `fixed` e `float`, é emitido um evento contendo o novo modo selecionado.

float

demo.js

```jsx
import './demo.css';

import React, { useState } from 'react';
import { EzSidebarNavigator, EzTree } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

	const [mode, setMode] = useState('float');

    return (
        <div className="ez-flex ez-flex--between sidebarNavigator__container">
            <EzSidebarNavigator
				className="ezSidebarNavigator"
				titleMenu="Defina um titulo"
				onEzChangeMode={(event) => setMode(event.detail)}
			>
                <EzTree items={items} />
            </EzSidebarNavigator>
			<div>
				{mode}
			</div>
        </div>
    )
};

export default Demo;

const items = [
	{
		id: "4654321",
		label: "Geral",
		expanded: true,
		children: [
			{
				id: "4654322",
				label: "Endereço",
				children: [
					{ id: "4654331", label: "Pendencias", disabled: true }
				]
			}
		]
	}
];
```

## Métodos

### `openSidebar()`

Abre o menu programaticamente.

### `closeSidebar()`

Fecha o menu programaticamente.

### `changeModeMenu()`

Alterna entre os modos fixo e flutuante. Este método só funciona quando o `type` do componente for `dynamic`.

## Tipos de Comportamento

### Fixo

O menu já começa aberto e ocupa um espaço fixo na tela. Ao ser fechado, é necessário clicar no **SidebarButton** para reabri-lo.

Para usar esse comportamento, defina a propriedade `type` como `'fixed'`.

demo.js

```jsx

import React, { useRef, useState } from 'react';
import { EzButton, EzCheck, EzFilterInput, EzSidebarNavigator, EzTree } from '@sankhyalabs/ezui/react/components';
import './demo.css';

let lastId = 4654331;

const Demo = () => {
	const tree = useRef();

    const applyFilter = filter => {
        tree.current.applyFilter(filter);
    };

	const openHandler = () => {
        tree.current.openItem("4654321");
        tree.current.openItem("4654321 >> 4654322");
        tree.current.openItem("4654323");
        tree.current.openItem("4654326");
    };

	const addChildHandler = () => {
        tree.current.addChild({
            id: ++lastId,
            label: "Item adicionado"
        });
    };

	const disableHandler = () => {
        tree.current.disableItem("4654323");
    };

    const enableHandler = () => {
        tree.current.enableItem("4654323");
    };

    return (
        <div className="ez-flex sidebarNavigator__container">
            <EzSidebarNavigator className="ezSidebarNavigator" type="fixed" size="lg">
				<EzFilterInput slot="content" mode="slim" label="Digite um filtro" onEzChange={evt => applyFilter(evt.detail)}/>
                <EzCheck label="Exemplo 1"></EzCheck>
                <EzCheck label="Exemplo 2" value="true"></EzCheck>
                <EzTree ref={tree} items={items} />
				<EzButton
					slot="start"
					onClick={openHandler}
					mode="icon"
					size="small"
					iconName="dual-chevron-right"
					title="Expardir itens"
					aria-label="Expardir itens"
					/>
				<div slot="end">
					<EzButton
						slot="start"
						onClick={addChildHandler}
						mode="icon"
						size="small"
						iconName="plus"
						title="Adicionar item"
						aria-label="Adicionar iten"
					/>
				</div>
				<div slot="footer" className="ez-flex ez-flex--justify-between ez-size-width--full">
					<EzButton
						onClick={disableHandler}
						mode="icon"
						size="small"
						iconName="account-outline"
						title="Desabilitar Contatos"
					/>
					<EzButton
						onClick={enableHandler}
						mode="icon"
						size="small"
						iconName="account"
						title="Habilitar Contatos"
					/>

				</div>
            </EzSidebarNavigator>
        </div>
    )
};

export default Demo;
const items = [
    {
        id: "4654321",
        label: "Geral",
        children: [
            {
                id: "4654322",
                label: "Endereço",
                children: [
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    },
    {
        id: "4654326", label: "Fiscal",
        children: [
            { id: "4654327", label: "NF-e/NFS-e/CT-e" }
        ]
    },
    { id: "4654328", label: "Lotação" },
    { id: "4654329", label: "Observação" },
    { id: "4654330", label: "Juros/Multa", disabled: true}
];
```

### Flutuante

O menu inicia fechado e é exibido ao passar o mouse sobre o **SidebarButton**. Quando o mouse sai do componente, o menu é ocultado novamente. O menu não ocupa espaço na tela enquanto está oculto.

Para usar esse comportamento, defina a propriedade `type` como `'float'`.

### Dinâmico

Esse é o comportamento padrão, onde o menu começa no modo flutuante, mas pode ser fixado pelo usuário clicando em um botão no cabeçalho.

Para usar o modo dinâmico explicitamente, defina a propriedade `type` como `'dynamic'`.

demo.js

```jsx

import React, { useRef } from 'react';
import { EzButton, EzFilterInput, EzSidebarNavigator, EzTree } from '@sankhyalabs/ezui/react/components';
import './demo.css';

let lastId = 4654331;

const Demo = () => {
	const tree = useRef();

    const applyFilter = filter => {
        tree.current.applyFilter(filter);
    };

	const openHandler = () => {
        tree.current.openItem("4654321");
        tree.current.openItem("4654321 >> 4654322");
        tree.current.openItem("4654323");
        tree.current.openItem("4654326");
    };

	const addChildHandler = () => {
        tree.current.addChild({
            id: ++lastId,
            label: "Item adicionado"
        });
    };

	const disableHandler = () => {
        tree.current.disableItem("4654323");
    };

    const enableHandler = () => {
        tree.current.enableItem("4654323");
    };

    return (
        <div className="ez-flex sidebarNavigator__container">
            <EzSidebarNavigator className="ezSidebarNavigator" type="dynamic" titleMenu="Titulo">
				<EzFilterInput slot="content" mode="slim" label="Digite um filtro" onEzChange={evt => applyFilter(evt.detail)}/>
				<EzTree ref={tree} items={items} />
				<EzButton
					slot="start"
					onClick={openHandler}
					mode="icon"
					size="small"
					iconName="dual-chevron-right"
					title="Expardir itens"
					aria-label="Expardir itens"
					/>
				<div slot="end">
					<EzButton
						slot="start"
						onClick={addChildHandler}
						mode="icon"
						size="small"
						iconName="plus"
						title="Adicionar item"
						aria-label="Adicionar iten"
					/>
				</div>
				<div slot="footer" className="ez-flex ez-flex--justify-between ez-size-width--full">
					<EzButton
						onClick={disableHandler}
						mode="icon"
						size="small"
						iconName="account-outline"
						title="Desabilitar Contatos"
					/>
					<EzButton
						onClick={enableHandler}
						mode="icon"
						size="small"
						iconName="account"
						title="Habilitar Contatos"
					/>

				</div>
            </EzSidebarNavigator>
        </div>
    )
};

export default Demo;
const items = [
    {
        id: "4654321",
        label: "Geral",
        children: [
            {
                id: "4654322",
                label: "Endereço",
                children: [
                    {id: "4654331", label: "Pendencias", disabled: true}
                ]
            }
        ]
    },
    {
        id: "4654323",
        label: "Contatos",
        children: [
            { id: "4654324", label: "Perfil" },
            { id: "4654325", label: "Endereço" }
        ]
    },
    {
        id: "4654326", label: "Fiscal",
        children: [
            { id: "4654327", label: "NF-e/NFS-e/CT-e" }
        ]
    },
    { id: "4654328", label: "Lotação" },
    { id: "4654329", label: "Observação" },
    { id: "4654330", label: "Juros/Multa", disabled: true}
];
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| isResponsive | is-responsive | Define se terá responsividade, Controle deverá ser pelo CSS. | boolean | false |
| mode | mode | Define se o menu será do tipo FIXED ou FLOAT. | ModeMenuEnum.FIXED \| ModeMenuEnum.FLOAT | ModeMenuEnum.FLOAT |
| showCollapseMenu | show-collapse-menu | Define se o botão de "Recolher Menu" será exibido | boolean | true |
| showFixedButton | show-fixed-button | Define se o botão de "Fixar Menu" será exibido | boolean | true |
| size | size | Define o tamanho do menu (small, medium, large). | SizeMenuEnum.LARGE \| SizeMenuEnum.MEDIUM \| SizeMenuEnum.SMALL | SizeMenuEnum.SMALL |
| titleMenu | title-menu | Define o título do Sidebar Navigator | string | "" |
| type | type | Define o tipo do menu (float, fixed ou dynamic (livre)). | TypeMenuEnum.DYNAMIC \| TypeMenuEnum.FIXED \| TypeMenuEnum.FLOAT | TypeMenuEnum.DYNAMIC |

### Events

| Event | Description | Type |
|---|---|---|
| ezChangeMode | Evento emitido sempre que o modo (FLOAT ou FIXED) do menu for alterado.. | CustomEvent<ModeMenuEnum.FIXED \| ModeMenuEnum.FLOAT> |

### Methods

#### `changeModeMenu() => Promise<void>`

Método para fixar/desafixar o menu, emitindo o evento ezChangeMode.

##### Returns

Type: `Promise<void>`

#### `closeSidebar() => Promise<void>`

Método para fechar o menu automaticamente após uma ação, fluxo, etc.

##### Returns

Type: `Promise<void>`

#### `openSidebar() => Promise<void>`

Método para abrir o menu automaticamente após uma ação, fluxo, etc.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * ez-sidebar-button
  * ez-button
  * ez-scroller

### CSS Variables

| Variable | Description |
|---|---|
| --ez-sidebar-navigator--padding-left | Define o espaçamento da esquerda do container |
| --ez-sidebar-navigator--padding-right | Define o espaçamento da direita do container |
| --ez-sidebar-navigator--gap | Define o espaçamento entre o cabeçalho conteúdo e rodapé |
| --ez-sidebar-navigator--box-shadow | Define a cor de shadow box do container de label |
| --ez-sidebar-navigator--background-color | Define a cor de fundo do container de label |
| --ez-sidebar-navigator--border-radius | Define o border radius do container de label |
| --ez-sidebar-navigator--height | Força uma altura especifica para o sidebar, o padrão é 100% da tela |
| --ez-sidebar-navigator--z-index | Define a camada em que o componente será exibido. |
| --ez-sidebar-navigator--header-gap | Define o espaçamento entre os componente do cabeçalho |
| --ez-sidebar-navigator--footer-gap | Define o espaçamento entre os componente do rodadé |
| --ez-ez-sidebar-navigator__title--font-family | Define a fonte do título do componente |
| --ez-ez-sidebar-navigator__title--font-size | Define o tamanho da fonte do título do componente. |
| --ez-ez-sidebar-navigator__title--color | Define a cor da fonte do título do componente. |
| --ez-ez-sidebar-navigator__title--font-weight | Define o peso da fonte do título do componente. |
