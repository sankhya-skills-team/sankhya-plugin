> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dropdown/ (snapshot 2026-09-28)

# Dropdown

Documentação do componente EzDropdown.

Importante

O componente **EzDropdown** não possui a capacidade de gerenciar a visibilidade do nível principal. Sua função é controlar somente os subníveis, portanto, é o componente pai ou o programador que é responsável por determinar se o _dropdown_ será exibido na tela ou não. Para realizar esse controle de visibilidade, nos exemplos a seguir será utilizado o componente **EzButton**.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzButton, EzDropdown } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-demo")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    return (
        <div className="ez-flex">
            <div id="dropdown-parent-demo">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}>
                    </EzDropdown>
                }
            </div>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item"
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item"
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ]
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

## Variações e estados

### Manipulação dos itens

> Propriedade utilizada: **items**

Os itens do componente são renderizados por um objeto _JSON_ , nele possui as definições necessárias para configurar cada um destes itens.

Observação

Para adicionar uma sublista com itens filhos a um determinado item, é necessário inserir o atributo **children** com uma lista de itens, utilizando as mesmas configurações do atributo da lista principal.

As configurações de itens disponíveis são:

#### Tipo de item

> Atributo utilizado: **type**

O valor padrão do atributo _type_ é **item**. No entanto, é possível modificar para **divider** e **loading** para que um divisor seja apresentado entre os itens do menu na posição correspondente do _JSON_. O exemplo a seguir ilustra essa possibilidade:

#### Ícones nos itens

> Atributo utilizado: **iconName**

Com o atributo _iconName_ é possível atribuir um ícone no item desejado. Conforme o exemplo a seguir:

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzButton, EzDropdown } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-icon-name")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    return (
        <div className="ez-flex">
            <div id="dropdown-parent-icon-name">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}>
                    </EzDropdown>
                }
            </div>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item"
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item",
        iconName: "close"
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        iconName: "arrow_downward",
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ]
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

#### Ação secundária

> Atributo utilizado: **subAction**

Com o atributo _subAction_ é possível definir uma ação secundária no item desejado.

Informação

O texto de ação secundária terá duas variações de cores:

  * **primary** : utilizada como padrão para ações secundárias.
  * **critical** : utilizada para ações destrutivas como um excluir.

Importante

Caso o item da lista possua uma sublista com itens filhos, a ação secundária não será exibida. Isso significa que o atributo _**subAction**_ será ignorado quando o item tiver o atributo _**children**_ preenchido.

Em **exemplos de eventos** , será demonstrado como utilizar o evento **ezSubActionClick** para explorar a ação secundária e obter mais informações sobre ela.

A seguir será apresentado um exemplo com as duas variações de cores e um item com os atributos _subAction_ e _children_ preenchidos.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzButton, EzDropdown } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-sub-action")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    return (
        <div className="ez-flex">
            <div id="dropdown-parent-sub-action">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}>
                    </EzDropdown>
                }
            </div>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item",
        subAction: {
            id: "sub1",
            label: "Agendar",
            type: 'primary'
        }
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item",
        subAction: {
            id: "sub2",
            label: "Termos da legislação",
            type: 'critical'
        }
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ],
                subAction: {
                    id: "sub3",
                    label: "Selecionar impressora",
                    type: 'primary'
                }
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

#### Nome do grupo

> Atributo utilizado: **group**

O atributo _group_ permite especificar o nome do grupo ao qual um determinado item pertencerá. É necessário informar o nome desejado no formato de _string_ , como ilustrado no exemplo a seguir:

#### Ordenação do grupo

> Atributo utilizado: **group**

Além de permitir definir o nome do grupo ao qual um item pertencerá, o atributo _group_ também possibilita determinar a ordem em que o grupo será apresentado na lista. Para isso, é necessário fornecer um objeto contendo os atributos _**order**_ e _**label**_ , conforme exemplificado abaixo:

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzButton, EzDropdown } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-group-object")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    return (
        <div className="ez-flex">
            <div id="dropdown-parent-group-object">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}>
                    </EzDropdown>
                }
            </div>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item",
        group: {
            order: 1,
            label: "Movimentação"
        }
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item",
        group: {
            order: 1,
            label: "Movimentação"
        }
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        group: {
            order: 0,
            label: "Exportação"
        },
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ]
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

### Capturar o valor do item

> Propriedade utilizada: **value**

A propriedade _value_ armazena o item clicado, com ela é possível capturar os dados deste item. Conforme o exemplo a seguir:

Item selecionado: ****

### Alterar aparência do item

> Propriedade utilizada: **itemBuilder**

A propriedade _itemBuilder_ é uma função que possibilita alterar como o item da lista será apresentado. Conforme o exemplo a seguir:

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { renderToString } from 'react-dom/server';
import { EzButton, EzDropdown, EzIcon } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-item-builder")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    /**
     * Método de exemplo do itemBuilder para alterar a aparência dos itens da lista
     */
    const getItemBuilder = (item, level) => {
        /**
         * O uso da tag style não é recomendado, utilizamos para esse caso de uso apenas para facilitar a exemplificação do itemBuilder.
         */
        const style = {"display": "flex", "alignItems": "center", "padding": "5px 10px", "cursor": "pointer"};
        const arrow = item?.children?.length > 0 && level < 3 ?
            <EzIcon
                slot="leftIcon"
                icon-name="chevron-right"
                title={item.label}
            /> : "";

        return renderToString(
            <div style={style}>
                Teste de itemBuilder
                {arrow}
            </div>
        );
    };

    return (
        <div className="ez-flex">
            <div id="dropdown-parent-item-builder">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}
                        itemBuilder={getItemBuilder}>
                    </EzDropdown>
                }
            </div>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item"
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item"
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ]
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

### Altura máxima

> Variável CSS utilizada: **\--ez-dropdown--max-height**

A variável _\--ez-dropdown--max-height_ define a altura máxima que a lista de itens pode atingir:

## Exemplos de eventos

#### ezClick()

Esse evento é emitido quando ocorre um clique em um item da lista. A seguir será apresentado um exemplo de uso deste evento.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzButton, EzDropdown } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-ez-click")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    const onEzClick = (evt) => {
        const item = evt?.detail;
        if (item == undefined) {
            return;
        }
        ApplicationUtils.message(
            "Título da Mensagem",
            `Item clicado: <strong>${item.label}</strong>.`
        );
    };

    return (
        <div className="ez-flex">
            <div id="dropdown-parent-ez-click">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}
                        onEzClick={onEzClick}>
                    </EzDropdown>
                }
            </div>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item"
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item"
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ]
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

#### ezSubActionClick()

Esse evento é emitido quando ocorrer um clique em uma ação secundária do item. A seguir será apresentado um exemplo de uso deste evento.

#### ezHover()

Esse evento é emitido quando o ponteiro do mouse é colocado sobre um item. A seguir será apresentado um exemplo de uso deste evento.

demo.js

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { EzButton, EzDropdown } from '@sankhyalabs/ezui/react/components';
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const ezButton = useRef();
    const ezDropdown = useRef();
    const [label, setLabel] = useState("Mostrar Dropdown");
    const [show, setShow] = useState(false);
    const [lastHoveredItem, setLastHoveredItem] = useState("");

    useEffect(() => {
        show && positionDropdown();
        setLabel(show ? "Ocultar Dropdown" : "Mostrar dropdown");
    }, [show]);

    useEffect(() => {
        document.removeEventListener("click", closeDropdown.bind(this));
        document.addEventListener("click", closeDropdown.bind(this));
        document.removeEventListener("scroll", positionDropdown.bind(this));
        document.addEventListener("scroll", positionDropdown.bind(this));
    }, []);

    const closeDropdown = (evt) => {
        const target = evt?.target;
        if (target == undefined) {
            return;
        }

        if (!target.closest("#dropdown-parent-ez-click")) {
            setShow(false);
        }
    }

    /**
     * Método responsável em posicionar o dropdown na tela.
     */
    const positionDropdown = () => {
        const bounding = ezButton?.current?.getBoundingClientRect();
        if (bounding == undefined || ezDropdown?.current == undefined) {
            return;
        }
        ezDropdown.current.style.top = (bounding.y + bounding.height + 5) + "px";
        ezDropdown.current.style.left = bounding.x + "px";
    };

    const onEzHover = (evt) => {
        const item = evt?.detail;
        if (item == undefined) {
            return;
        }
        setLastHoveredItem(item.label);
    };

    return (
        <div className="ez-flex ez-flex--justify-between ez-flex--align-items-center">
            <div id="dropdown-parent-ez-click">
                <EzButton
                    ref={ezButton}
                    label={label}
                    onClick={() => setShow(!show)}>
                </EzButton>

                {
                    show &&
                    <EzDropdown
                        ref={ezDropdown}
                        items={items}
                        onEzHover={onEzHover}>
                    </EzDropdown>
                }
            </div>
            <span>
                {lastHoveredItem}
            </span>
        </div>
    )
};

export default Demo;

/**
 * Exemplo de JSON com a lista de itens que serão apresentados no dropdown.
 */
const items = [
    {
        id: "1",
        label: "Emitir NFe",
        type: "item"
    },
    {
        id: "2",
        label: "Cancelar NFe",
        type: "item"
    },
    {
        id: "3",
        label: "Exportar NFe",
        type: "item",
        children: [
            {
                id: "4",
                label: "Danfe PDF",
                type: "item",
                children: [
                    {
                        id: "6",
                        label: "Modo retrato",
                        type: "item"
                    },
                    {
                        id: "7",
                        label: "Modo paisagem",
                        type: "item"
                    }
                ]
            },
            {
                id: "5",
                label: "XML",
                type: "item"
            }
        ]
    }
];
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| itemBuilder | -- | Função builder que possibilita alterar como o item da lista vai ser apresentado. Observação: No react ele se transforma em VNode e não como HTMLElement. | (item: IDropdownItem, level: number) => string \| HTMLElement | undefined |
| items | -- | Lista de itens que vão ser apresentados no dropdown. | IDropdownItem[] | [] |
| value | -- | Último item que recebeu o click. | IDropdownItem | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| ezClick | Emitido quando ocorrer um click em um item da lista, o IDropdownItem que recebeu o click deve ser enviado como data do evento. | CustomEvent<IDropdownItem> |
| ezHover | Emitido quando ocorrer o ponteiro do mouse é colocado sobre um item. | CustomEvent<IDropdownItem> |
| ezOutsideClick | Emitido quando ocorrer um click fora do componente. | CustomEvent<void> |
| ezSubActionClick | Emitido quando ocorrer um click em uma ação secundaria do item,  o IDropdownSubAction deve ser enviado como data do evento. | CustomEvent<IDropdownSubAction> |

### Dependencies

#### Used by

  * ez-breadcrumb
  * ez-split-button

#### Depends on

  * ez-skeleton
  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-dropdown--z-index | Define a posição do componente. |
| --ez-dropdown--padding | Define o espaçamento interno do componente. |
| --ez-dropdown--box-shadow | Define a sombra externa do componente. |
| --ez-dropdown--border-radius | Define o raio da borda do componente. |
| --ez-dropdown--background-color | Define cor de fundo do componente. |
| --ez-dropdown--font-family | Define a fonte do componente. |
| --ez-dropdown--max-height | Define a altura máxima do componente. |
| --ez-dropdown__item--padding | Define o espaçamento interno de cada item do componente. |
| --ez-dropdown__item--gap | Define o espaçamento entre os elementos internos do item do componente. |
| --ez-dropdown__item--border-radius | Define o raio da borda de cada item do componente. |
| --ez-dropdown__item--color | Define a cor do texto de cada item do componente. |
| --ez-dropdown__item--font-weight | Define o peso do texto de cada item do componente. |
| --ez-dropdown__item--font-size | Define o tamanho da fonte de cada item do componente. |
| --ez-dropdown__item--line-height | Define a altura do texto de cada item do componente. |
| --ez-dropdown__item--background-color | Define a cor de fundo no hover de cada item do componente. |
| --ez-dropdown__item--transition | Define o efeito de transição do hover de cada item do componente. |
| --ez-dropdown__item-label--margin-right | Define o espaçamento direito externo de cada label do componente. |
| --ez-dropdown__icon--size | Define o tamanho da área de cada ícone do componente. |
| --ez-dropdown__divider--background-color | Define a cor de fundo do divider do componente. |
| --ez-dropdown__divider--margin | Define o espaçamento externo do divider do componente. |
| --ez-dropdown__group-label--color | Define a cor do título de cada grupo do componente. |
| --ez-dropdown__group-label--font-weight | Define o peso do texto do título de cada grupo do componente. |
| --ez-dropdown__group-label--font-size | Define o tamanho da fonte do título de cada grupo do componente. |
| --ez-dropdown__group-label--line-height | Define a altura do texto do título de cada grupo do componente. |
| --ez-dropdown__group-label--padding | Define o espaçamento interno do título de cada grupo do componente. |
| --ez-dropdown__submenu--z-index | Define a posição do submenu do componente. |
| --ez-dropdown__link--font-weight | Define o peso do texto de cada link do componente. |
| --ez-dropdown__link--primary--color | Define a cor utilizada como padrão para ações secundárias. |
| --ez-dropdown__link--critical--color | Define a cor utilizada para ações destrutivas como um excluir. |
| --ez-dropdown__scrollbar--color-default | Define a cor da barra de rolagem do componente. |
| --ez-dropdown__scrollbar--color-background | Define a cor de fundo da barra de rolagem do componente. |
| --ez-dropdown__scrollbar--color-hover | Define a cor do hover na barra de rolagem do componente. |
| --ez-dropdown__scrollbar--color-clicked | Define a cor do active na barra de rolagem do componente. |
| --ez-dropdown__scrollbar--border-radius | Define o raio da borda da barra de rolagem do componente. |
| --ez-dropdown__scrollbar--width | Define a largura da barra de rolagem do componente. |
| --ez-dropdown__scrollbar--padding-right | Define o espaçamento interno direito quando houver barra de rolagem. |
