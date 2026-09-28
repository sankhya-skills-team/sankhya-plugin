> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-entity-list/ (snapshot 2026-09-28)

# Entity List

O bloco snk-entity-list é responsável por renderizar uma lista de múltiplos checkbox com a opção de adição de itens pelo campo de pesquisa.

## Exemplo

```
import { SnkEntityList } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";

const Demo = () => {
    const config = {
        "id": "CODPARC",
        "label": "Parceiro",
        "detailTitle": "Informe o parceiro",
        "type": "SEARCH",
        "props": {
            "expression": "this.CODPARC = :CODPARC",
            "searchContext": {
                "entity": "Parceiro",
                "entityDescription": "Parceiro",
                "searchOptions": {
                    "rootEntity": "Financeiro",
                    "descriptionFieldName": "NOMEPARC",
                    "codeFieldName": "CODPARC",
                    "showInactives": false
                }
            }
        },
        "visible": true,
        "value": [
            {
                "id": "1",
                "check": true,
                "label": "Parceiro 1"
            },
            {
                "id": "2",
                "check": false,
                "label": "Parceiro 2"
            }
        ]
    };

    const entityListChange = (newValue) => {
        ApplicationUtils.message("Valor alterado", "Modificação realizada na lista de valores!");
    }

    const buildRightSlot = (item) => {
        return (
            <div>
                <ez-icon iconName={"delete"} onClick={() => removeValueFromConfig(item)}></ez-icon>
            </div>
        );
    }

    const removeValueFromConfig = (item) => {
        config.value.splice(config.value.findIndex(i => i.id === item.id), 1);
    }

    return (
        <SnkEntityList
            config={config}
            onValueChanged={value => { entityListChange(value) }}
            rightListSlotBuilder={(item) => buildRightSlot(item)} ></SnkEntityList>
    );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| config | -- | Configurações para carregar os dados do componente | SnkFilterItemConfig | undefined |
| errorMessage | error-message | Usado para exibir mensagens de erro. | string | undefined |
| maxHeightList | max-height-list | Permite definir uma altura máxima para o ez-list, adicionando um scroll ao atingir esta medida | string | "" |
| rightListSlotBuilder | -- | Método que possibilita alterar como o item da lista vai ser apresentado. Observação: No React ele se transforma em VNode e não HTMLElement. | (item: ListItem, group?: ListGroup) => string \| HTMLElement | undefined |
| value | -- | Define o valor do componente | IOption | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| valueChanged | Emite um evento customizado ao realizar alteração nos valores do componente | CustomEvent<CustomEvent<any>> |

### Methods

#### `reloadList() => Promise<void>`

##### Returns

Type: `Promise<void>`
