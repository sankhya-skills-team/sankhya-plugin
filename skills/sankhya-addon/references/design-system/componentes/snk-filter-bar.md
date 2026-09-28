> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-filter-bar/ (snapshot 2026-09-28)

# Filter Bar

A **Barra de Filtros (SnkFilterBar)** é um componente essencial para telas que necessitam de filtragem de dados complexa e interativa. Ela oferece uma interface visual onde os filtros aplicados são exibidos como "chips", permitindo que os usuários visualizem e modifiquem rapidamente os critérios de busca. Além disso, um modal completo de gerenciamento de filtros está disponível para configurações mais avançadas, incluindo a criação de filtros personalizados.

**Principais Funcionalidades:**

  * **Barra de Filtros Interativa:** Exibe os filtros ativos como "chips" em uma barra com rolagem horizontal.
  * **Edição Rápida:** Ao clicar em um chip de filtro, um pop-up é aberto, permitindo a alteração rápida do valor do filtro, além de opções para limpar, fixar/desafixar ou remover o filtro da barra.
  * **Modal de Gerenciamento Completo:** Um botão "Filtros" dá acesso a um modal que exibe todos os filtros disponíveis para a tela, agrupados por categorias. Neste modal, o usuário pode ativar ou desativar filtros, configurar seus valores e aplicar todas as mudanças de uma só vez.
  * **Filtros Personalizados:** O componente se integra ao sistema de filtros personalizados, permitindo que os usuários criem, editem e apliquem seus próprios filtros.
  * **Modos de Exibição:** Suporta diferentes modos de apresentação (`regular`, `button`, `hidden`), adaptando-se a diversas necessidades de layout.
  * **Integração com Dados:** Conecta-se a um `DataUnit` para carregar metadados e aplicar os filtros diretamente nas consultas de dados, com a opção de carregamento automático (`autoLoad`).
  * **Persistência:** As configurações da barra de filtros, como a visibilidade e a ordem dos itens, são salvas por usuário, garantindo uma experiência consistente entre as sessões.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication  configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkFilterBar />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

## Quando utilizar

**Importante:** O uso do `snk-filter-bar` é recomendado exclusivamente para a construção de telas no contexto de aplicações Sankhya, pois depende de integrações específicas do ecossistema Sankhya para seu pleno funcionamento.

Utilize a Barra de Filtros em cenários onde os usuários precisam de controle granular sobre os dados exibidos. É ideal para:

  * **Telas de consulta e relatórios:** Onde a capacidade de filtrar por múltiplos campos (como datas, status, categorias, etc.) é fundamental.
  * **Dashboards interativos:** Para permitir que os usuários explorem os dados dinamicamente.
  * **Listas de registros extensas:** Onde a filtragem é necessária para encontrar informações específicas de forma eficiente.

## Quando não utilizar

Evite usar a Barra de Filtros em situações onde a filtragem é simples ou desnecessária. Por exemplo:

  * **Telas de cadastro ou formulários simples:** Onde o foco é a entrada de dados e não a consulta.
  * **Telas com um único ou poucos critérios de filtro:** Nesses casos, um campo de busca simples ou alguns controles de filtro dedicados (como um `ez-combo-box` ou `ez-date-input`) podem ser mais diretos e ocupar menos espaço na interface.
  * **Interfaces com espaço muito limitado:** Embora a barra é rolável, em telas muito pequenas ou com muitos outros elementos, ela pode sobrecarregar a interface. Considere o modo `button` ou `hidden` como alternativa.

## Propriedades

### Definir o **DataUnit**

> Propriedade utilizada: **dataUnit**

Define o DataUnit com os metadados para carregamento dos componentes no filtro.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const handleDataUnitReady = (event) => {
        setDataUnitInstance(event.detail);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkFilterBar dataUnit={dataUnitInstance} />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Definir o nome da configuração

> Propriedade utilizada: **configName**

Define o nome da configuração para ser identificado no código.

Eventualmente poderemos ter mais de uma barra de filtros. Essa propriedade serve para separar a configuração de cada uma.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkFilterBar configName="MovimentoBancario" dataUnit={dataUnitInstance} />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Configuração do filtro

> Propriedade utilizada: **filterConfig**

Define uma configuração customizada para a barra de filtros.

```jsx
import { useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);

    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);

        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }

    };

    const setFilterConfig = () => {
        snkFilterBar.current.filterConfig = [
            {
                "id": "CODLANC",
                "label": "Lançamento origem",
                "detailTitle": "Informe o lançamento de origem",
                "type": "SEARCH",
                "visible": true
            }
        ];
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <EzButton onClick={setFilterConfig} label="Aplicar cofiguração do filtro" />
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Loader customizado das configurações

> Propriedade utilizada: **customFilterBarConfig**

É possível definir um loader customizado para carregar as configurações de filtro dinamicamente, após o carregamento do componente na tela.

```jsx
import {useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    const snkApplicationRef = useRef(null);

    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    /**
     *
     * A função de callback receberá três argumentos
     *
     * @param configName: string
     * @param resourceId: string
     * @param options: any
     * @returns {Promise<Array<SnkFilterItemConfig>>}
     */
    async function customConfigLoader(configName, resourceId, options){
        // ... Lógica interna
        console.log(`configName: ${configName} | resourceId: ${resourceId} | options: ${options}`)

        // retorno: array de SnkFilterItemConfig
        return [
            {
                "id": "CODLANC",
                "label": "Lançamento origem",
                "detailTitle": "Informe o lançamento de origem",
                "type": "SEARCH",
                "visible": true
            }
        ];
    }

    const handleDataUnitReady = async (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();

       if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkFilterBar dataUnit={dataUnitInstance} customFilterBarConfig={customConfigLoader} resourceID={resourceID} />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Definir título da barra de filtros

> Propriedade utilizada **title**

Define um título para a barra de filtros

```jsx
import {useState, useRef} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkApplicationRef = useRef(null);

    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);

        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && (
                    <SnkFilterBar dataUnit={dataUnitInstance} title={"Exemplo Título"} resourceID={resourceID} />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

O tamanho máximo do título é de 250px. Caso o texto informado ultrapasse esse valor, é aplicado o estilo de **text-overflow: ellipsis**

### Modo de exibição

Define o modo de exibição da barra de filtros.

> Propriedade: **mode="regular"**

Modo padrão, apresenta um botão com um ícone "+" e o label "Filtros" que, ao ser clicado, abre o modal de filtros.

```jsx
import { useRef, useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const dataUnitRef = useRef();
    const snkApplicationRef = useRef(null);

    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);

        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef} >
            <SnkDataUnit
                ref={dataUnitRef}
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkFilterBar
                        messagesBuilder={dataUnitRef.current.messagesBuilder}
                        mode="regular"
                        dataUnit={dataUnitInstance}
                        resourceID={resourceID}
                    />
                )}
            </SnkDataUnit>
        </SnkApplication>
    )
};

export default Demo;
```

> Propriedade: **mode="button"**

Será apresentado apenas um botão com o label "Filtros" que, ao ser clicado, abre o modal de filtros.

```jsx
import { useRef, useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

/**
 * Neste exemplo você pode alterar a propriedade `mode` do componente `SnkFilterBar` para "regular", "button" ou "hidden".
 */
const Demo = () => {
    const dataUnitRef = useRef();
    const snkApplicationRef = useRef(null);

    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);

        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef} >
            <SnkDataUnit
                ref={dataUnitRef}
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkFilterBar
                        messagesBuilder={dataUnitRef.current.messagesBuilder}
                        mode="button"
                        dataUnit={dataUnitInstance}
                        resourceID={resourceID}
                    />
                )}
            </SnkDataUnit>
        </SnkApplication>
    )
};

export default Demo;
```

> Propriedade: **mode="hidden"**

Será criada apenas a instância da barra de filtros, mas não será exibida. Utilizada para poder abrir o modal de filtros a partir de ações customizadas utilizando a referência.

```jsx
import { useRef, useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

/**
 * Neste exemplo você pode alterar a propriedade `mode` do componente `SnkFilterBar` para "regular", "button" ou "hidden".
 */
const Demo = () => {
    const dataUnitRef = useRef();
    const snkApplicationRef = useRef(null);

    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);

        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef} >
            <SnkDataUnit
                ref={dataUnitRef}
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkFilterBar
                        messagesBuilder={dataUnitRef.current.messagesBuilder}
                        mode="hidden"
                        dataUnit={dataUnitInstance}
                        resourceID={resourceID}
                    />
                )}
            </SnkDataUnit>
        </SnkApplication>
    )
};

export default Demo;
```

### Carregamento automático de registros

> Propriedade utilizada: **autoLoad**

Define o carregamento automático de dados.

O **autoLoad** controla se os dados serão carregados na inicialização do componente.

Caso a propriedade seja atribuída, o seu valor será respeitado, independente dos parâmetros estabelecidos, caso não, o componente seguirá seu fluxo padrão, onde será respeitado o parâmetro **global.carregar.registros.iniciar.tela**.

```jsx
import { useRef, useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzGrid, EzButton } from '@sankhyalabs/ezui/react/components';

const MovimentacaoBancaria = () => {
    const snkApplicationRef = useRef(null);
    const [dataUnit, setDataUnit] = useState(null);
    const [autoLoad, setAutoLoad] = useState(false);
    const [key, setKey] = useState(0);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnit(event.detail);
        if (snkApplicationRef.current && !resourceID) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const handleSetAutoLoadFalse = () => {
        setAutoLoad(true);
        setKey(prev => prev + 1);
        setDataUnit(null);
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <h2 className="ez-title">{autoLoad ? 'Com' : 'Sem'} autoLoad</h2>
            <p className="ez-text">
                {autoLoad
                    ? 'Os dados são carregados automaticamente ao iniciar a tela.'
                    : 'Os dados não são carregados automaticamente. É necessário aplicar um filtro para que a carga ocorra.'}
            </p>
            {!autoLoad && (
                <EzButton onClick={handleSetAutoLoadFalse} style={{ marginBottom: '1rem' }} label="Testar com autoLoad ligado" />
            )}
            <div key={key}>
                <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                    {dataUnit && resourceID && (
                        <>
                            <SnkFilterBar dataUnit={dataUnit} resourceID={resourceID} autoLoad={autoLoad} />
                            <div style={{ height: '300px', marginTop: '1rem' }}>
                                <EzGrid dataUnit={dataUnit} />
                            </div>
                        </>
                    )}
                </SnkDataUnit>
            </div>
        </SnkApplication>
    );
};

export default MovimentacaoBancaria;
```

### Metódo executado pós aplicação dos filtros

> Propriedade utilizada: **afterApplyConfig**

Função chamada depois de aplicar os filtros.

Neste exemplo, uma notificação de sucesso é exibida sempre que as configurações de filtro são aplicadas através do modal de filtros.

```jsx
import React, {useRef} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);

    const [dataUnit, setDataUnit] = React.useState(null);
    const [resourceID, setResourceID] = React.useState(null);

    const afterApplyConfig = () => {
        alert('A configuração do filtro foi aplicada com sucesso.');
    };

    const handleDataUnitReady = async (event) => {
        setDataUnit(event.detail);
        if (snkApplicationRef.current && !resourceID) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                { dataUnit && resourceID && (
                    <SnkFilterBar ref={snkFilterBar} afterApplyConfig={afterApplyConfig} resourceID={resourceID}/>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Metódos

### reload

Faz o recarregamento da barra de filtros buscando o state no servidor.

O exemplo abaixo demonstra como usar o método `reload` para forçar o recarregamento da configuração da barra de filtros a partir do servidor, útil para quando as configurações são alteradas externamente.

```jsx
import {useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton, EzGrid } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const removeFilterItem = async () => {
        const filterItem = await snkFilterBar.current.removeFilterItem('HISTORICO');
        console.log('Item de filtro removido:', filterItem);
    };

    const reloadFilterBar = () => {
        snkFilterBar.current.reload();
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <p className="ez-text">
                Primeiro, remova o filtro "Historico". Depois, clique em "Recarregar" para restaurar a configuração original da barra de filtros.
            </p>
            <div className="ez-flex" style={{ gap: '1rem', marginBottom: '1rem' }}>
                <EzButton onClick={removeFilterItem} label="Remover item de filtro" />
                <EzButton onClick={reloadFilterBar} label="Recarregar"/>
            </div>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <>
                        <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                        <div style={{ height: '300px', marginTop: '1rem' }}>
                            <EzGrid dataUnit={dataUnitInstance} />
                        </div>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### getFilterItem

Retorna um item de filtro pelo ID.
Neste exemplo, o método `getFilterItem` é usado para obter a configuração do filtro com o ID 'HISTORICO' e exibi-la em uma notificação, permitindo a inspeção de um filtro específico.

```jsx
import {useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton, EzGrid } from '@sankhyalabs/ezui/react/components';

/**
 * Para que o exemplo funcione, é necessario que a configuração do filtro esteja criada no Sankhya.
 * A configuração deve conter o filtro "Tipo de Movimento" (CODCTABCOINT) e o filtro deve estar visível.
 *
 * Se preferir, você pode usar o exemplo para outra entidade, desde que a configuração do filtro exista e contenha o filtro desejado.
 */
const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef();
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const getFilterItem = async () => {
        const filterItem = await snkFilterBar.current.getFilterItem('CODCTABCOINT');
        alert(`Veja a configuração do Filtro "Tipo de Movimento" no console.`);
        console.log(filterItem);
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <p className="ez-text">Clique no botão para obter a configuração do filtro "Tipo de Movimento" e exibi-la em um alerta.</p>
            <EzButton onClick={getFilterItem} label="Obter item de filtro" style={{ marginBottom: '1rem' }} />
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <>
                        <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                        <div style={{ height: '300px', marginTop: '1rem' }}>
                            <EzGrid dataUnit={dataUnitInstance} />
                        </div>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### updateFilterItem

Atualiza um item do filtro. O exemplo a seguir mostra como atualizar o `label` de um item de filtro existente. O filtro com ID 'HISTORICO' terá seu `label` alterado para 'Historico Alterado', refletindo a mudança na interface.

```jsx
import React, {useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton, EzGrid } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const updateFilterItem = async () => {
        const currentFilter = await snkFilterBar.current.getFilterItem('HISTORICO');
        if (currentFilter) {
            snkFilterBar.current.updateFilterItem({
                ...currentFilter,
                label: 'Histórico Alterado',
            });
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <p className="ez-text">Clique no botão para alterar o label do filtro "Histórico" para "Histórico Alterado".</p>
            <EzButton onClick={updateFilterItem} label="Atualizar item de filtro" style={{ marginBottom: '1rem' }} />
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <>
                        <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                        <div style={{ height: '300px', marginTop: '1rem' }}>
                            <EzGrid dataUnit={dataUnitInstance} />
                        </div>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### AddFilterItem

Adiciona um item de filtro. Este exemplo demonstra como adicionar um novo item de filtro de texto à barra de filtros dinamicamente, expandindo as opções de filtragem em tempo de execução.

```jsx
import React, {useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton, EzGrid } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [isFilterAdded, setIsFilterAdded] = useState(false);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const addFilterItem = () => {
        snkFilterBar.current.addFilterItem({
            "id": "NOVO_FILTRO",
            "label": "Novo Filtro",
            "detailTitle": "Informe o novo filtro",
            "type": "TEXT",
            "visible": true
        });
        setIsFilterAdded(true);
    };

    const removeFilterItem = () => {
        snkFilterBar.current.removeFilterItem("NOVO_FILTRO");
        setIsFilterAdded(false);
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <p className="ez-text">Clique no botão para adicionar um novo filtro de texto à barra de filtros.</p>
            <div className="ez-flex" style={{ gap: '1rem', marginBottom: '1rem' }}>
                <EzButton onClick={addFilterItem} label="Adicionar item de filtro" enabled={!isFilterAdded} />
                <EzButton onClick={removeFilterItem} label="Remover item adicionado" enabled={isFilterAdded} color="secondary" />
            </div>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <>
                        <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                        <div style={{ height: '300px', marginTop: '1rem' }}>
                            <EzGrid dataUnit={dataUnitInstance} />
                        </div>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### RemoveFilterItem

Remove um item de filtro. No exemplo abaixo, o filtro com o ID 'HISTORICO' é removido da barra de filtros ao clicar no botão, simplificando a interface para o usuário.

```jsx
import { useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton, EzGrid } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const removeFilterItem = async () => {
        const filterItem = await snkFilterBar.current.removeFilterItem('HISTORICO');
        console.log('Item de filtro removido:', filterItem);
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <p className="ez-text">Clique no botão para remover o filtro "HISTORICO". Ele não estará mais disponível, nem no modal de filtros.</p>
            <EzButton onClick={removeFilterItem} label="Remover item de filtro" style={{ marginBottom: '1rem' }} />
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <>
                        <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                        <div style={{ height: '300px', marginTop: '1rem' }}>
                            <EzGrid dataUnit={dataUnitInstance} />
                        </div>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### showFilterModal

Abre o modal de filtros. Este exemplo mostra como abrir programaticamente o modal de filtros através de uma referência ao componente `SnkFilterBar`, oferecendo um ponto de entrada customizado para o gerenciamento de filtros.

```jsx
import { useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton, EzGrid } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkFilterBar = useRef(null);
    const snkApplicationRef = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const handleDataUnitReady = async (event) => {
        setDataUnitInstance(event.detail);
        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    const showFilterModal = () => {
        snkFilterBar.current.showFilterModal();
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <p className="ez-text">Clique no botão para abrir o modal com todos os filtros disponíveis.</p>
            <EzButton onClick={showFilterModal} label="Abrir modal de filtros" style={{ marginBottom: '1rem' }} />
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <>
                        <SnkFilterBar ref={snkFilterBar} dataUnit={dataUnitInstance} resourceID={resourceID} />
                        <div style={{ height: '300px', marginTop: '1rem' }}>
                            <EzGrid dataUnit={dataUnitInstance} />
                        </div>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Eventos

### ConfigUpdated

Evento emitido quando a configuração dos filtros é atualizada. Neste exemplo, o evento `onConfigUpdated` é usado para ouvir as mudanças na configuração dos filtros (seja por adição, remoção ou atualização de valor) e exibir os dados atualizados em uma notificação.

```jsx
import {useRef, useState} from 'react';
import { SnkApplication, SnkDataUnit, SnkFilterBar } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkApplicationRef = useRef(null);
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const [resourceID, setResourceID] = useState(null);

    const onConfigUpdated = (event) => {

        alert('Veja a configuração atualizada no console.log');
        console.log('Configuração atualizada:', event.detail);
    };

    const handleDataUnitReady = async (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();

        if (snkApplicationRef.current) {
            const appResourceID = await snkApplicationRef.current.getResourceID();
            setResourceID(appResourceID);
        }
    };

    return (
        <SnkApplication ref={snkApplicationRef}>
            <SnkDataUnit entityName="MovimentoBancario" onDataUnitReady={handleDataUnitReady}>
                {dataUnitInstance && resourceID && (
                    <SnkFilterBar onConfigUpdated={onConfigUpdated} dataUnit={dataUnitInstance} resourceID={resourceID} />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| afterApplyConfig | -- |  | () => void | undefined |
| autoLoad | auto-load |  | boolean | undefined |
| configName | config-name |  | string | undefined |
| customFilterBarConfig | -- |  | (configName: string, resourceId: string, options: any) => Promise<SnkFilterItemConfig[]> | undefined |
| dataUnit | -- |  | DataUnit | undefined |
| disablePersonalizedFilter | disable-personalized-filter |  | boolean | undefined |
| enableLockManagerLoadingComp | enable-lock-manager-loading-comp |  | boolean | false |
| filterBarLegacyConfigName | filter-bar-legacy-config-name |  | string | undefined |
| filterConfig | -- |  | SnkFilterItemConfig[] | undefined |
| filterCustomConfig | -- |  | SnkFilterItemConfig[] | undefined |
| filterCustomConfigInterceptor | -- |  | (config: SnkFilterItemConfig[]) => SnkFilterItemConfig[] | undefined |
| messagesBuilder | -- |  | SnkMessageBuilder | undefined |
| mode | mode |  | "button" \| "hidden" \| "regular" | "regular" |
| resourceID | resource-i-d |  | string | undefined |
| title | title |  | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| configUpdated |  | CustomEvent<SnkFilterItemConfig[]> |

### Methods

#### `addFilterItem(filterItem: SnkFilterItemConfig) => Promise<void>`

##### Returns

Type: `Promise<void>`

Retorna uma Promise que resolve quando o item for adicionado.

#### `getFilterItem(id: string) => Promise<SnkFilterItemConfig | undefined>`

##### Returns

Type: `Promise<SnkFilterItemConfig>`

O item de filtro correspondente ou undefined se não for encontrado.

#### `getFilters() => Promise<Filter[]>`

##### Returns

Type: `Promise<Filter[]>`

#### `reload() => Promise<void>`

##### Returns

Type: `Promise<void>`

Retorna uma Promise que resolve quando o recarregamento for concluído.

#### `removeFilterItem(filterID: string) => Promise<SnkFilterItemConfig | undefined>`

##### Returns

Type: `Promise<SnkFilterItemConfig>`

Retorna o item de filtro removido, ou undefined caso não seja encontrado.

#### `showFilterModal() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `updateFilterItem(newFilterItem: SnkFilterItemConfig) => Promise<void>`

##### Returns

Type: `Promise<void>`

Retorna uma Promise que resolve quando a atualização for concluída.

### Dependencies

#### Used by

  * snk-grid

#### Depends on

  * snk-filter-item
  * snk-personalized-filter
  * snk-filter-modal
