> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-data-unit/ (snapshot 2026-09-28)

# Data Unit

Utilizamos o **SnkDataUnit** para exibição e manipulação de dados. Ele atua na aplicação Sankhya como uma camada de abstração entre o back-end e a interface do usuário, proporcionando uma solução eficaz para o gerenciamento de dados.

## O que é o SnkDataUnit?

O `SnkDataUnit` é um componente fundamental no ecossistema de desenvolvimento Sankhya. Ele atua como uma camada de abstração robusta entre a interface do usuário (frontend) e as fontes de dados (backend). Sua principal responsabilidade é gerenciar o ciclo de vida dos dados de uma entidade específica, incluindo busca, apresentação, manipulação (inserção, alteração, exclusão) e persistência, além de lidar com metadados, validações e interações com componentes visuais como grades e formulários.

Ele encapsula a lógica de comunicação com o Data Unit do backend, facilitando o desenvolvimento de telas que interagem com as entidades do ERP Sankhya de forma padronizada e eficiente.

### Diferença entre `DataUnit` (core) e `SnkDataUnit` (componente)

É crucial entender a distinção:

  * **`DataUnit`** : É uma classe TypeScript parte do pacote `@sankhyalabs/core`. Ela é o cérebro por trás da manipulação de dados, contendo a lógica de estado, comunicação com o backend, gerenciamento de metadados, e as operações de CRUD. Ela é agnóstica em relação à interface do usuário.
  * **`SnkDataUnit`** : É um Web Component (criado com StencilJS) que você utiliza em suas telas (arquivos `.jsx` ou `.tsx`). Ele _instancia e gerencia_ um objeto `DataUnit` internamente. O `SnkDataUnit` expõe as funcionalidades do `DataUnit` através de propriedades, métodos e eventos, permitindo que você interaja com os dados de forma declarativa em sua UI e conecte-o a outros componentes visuais da Sankhya. Essencialmente, o `SnkDataUnit` é a ponte entre a lógica de dados do `DataUnit` e a sua aplicação frontend.

## Quando usar o SnkDataUnit?

  * **Gerenciamento de Dados de Entidades:** Sempre que precisar interagir com os dados de uma entidade do ERP Sankhya (ex: Produtos, Parceiros, Notas Fiscais) em uma tela customizada.
  * **Operações CRUD:** Para implementar funcionalidades de criação, leitura, atualização e exclusão de registros de forma integrada.
  * **Integração com Componentes Visuais:** Quando for utilizar componentes como `snk-grid`, `snk-form`, `snk-crud`, pois o `SnkDataUnit` fornece os dados e a lógica de manipulação para eles.
  * **Abstração da Lógica de Backend:** Para evitar chamadas diretas a serviços e padronizar a forma como os dados são tratados no frontend, promovendo um código mais limpo e de fácil manutenção.
  * **Reutilização de Lógica:** Para centralizar a lógica de negócios relacionada a uma entidade, facilitando a manutenção e garantindo consistência através de diferentes partes da aplicação.
  * **Tratamento de Metadados Dinâmicos:** Quando a apresentação e o comportamento dos campos precisam se adaptar dinamicamente com base em metadados (como `rmp` e `rm_precision`) fornecidos pelo backend.
  * **Controle de Estado dos Dados:** Para ter um controle claro sobre o estado dos dados (sujo, novo, copiado, etc.) e reagir a essas mudanças na interface do usuário.

## Quando NÃO usar o SnkDataUnit?

  * **Dados Estáticos ou Puramente Locais:** Se os dados a serem exibidos são puramente estáticos, não vêm do backend Sankhya, ou são gerenciados inteiramente no lado do cliente sem necessidade de persistência no ERP.
  * **Chamadas de Serviço Específicas sem Ciclo de Vida CRUD:** Para chamadas de serviço pontuais que não se encaixam no ciclo de vida de uma entidade (ex: executar uma ação específica que não é um CRUD, buscar uma configuração simples). Nesses casos, o método `SnkApplication.callServiceBroker` pode ser mais direto e apropriado.
  * **Visualização Simples sem Interação Complexa:** Se você precisa apenas exibir uma informação específica de uma entidade sem nenhuma interação de edição, cópia, ou exclusão, e a estrutura do `SnkDataUnit` parecer excessiva para a simplicidade da tarefa.
  * **Lógica de UI Muito Específica e Desacoplada de Entidades do ERP:** Para componentes de UI que têm sua própria lógica de estado e não se relacionam diretamente com uma entidade gerenciada pelo Data Unit do Sankhya.
  * **Performance Crítica com Grandes Volumes de Dados Não Paginados de Forma Não Padrão:** Embora o `SnkDataUnit` lide com paginação e otimizações, se houver um requisito muito específico para carregar volumes massivos de dados de uma forma altamente customizada e a abstração do Data Unit se tornar um gargalo, pode ser necessário considerar estratégias mais diretas (com devida cautela e análise).

## Hierarquia

O **SnkDataUnit** deve ser implementado dentro de um **SnkApplication**. O `SnkApplication` fornece o contexto necessário, como configurações, permissões de acesso e o sistema de mensagens padrão da aplicação, que são utilizados pelo **SnkDataUnit**.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication>
        <SnkDataUnit />
    </SnkApplication>
);

export default Demo;
```

## Renderizando Componentes Filhos (SnkCrud, SnkForm, SnkGrid)

Ao utilizar componentes como `SnkCrud`, `SnkForm` ou `SnkGrid` como filhos diretos de um `SnkDataUnit`, é crucial garantir que o `SnkDataUnit` esteja completamente inicializado e seus metadados carregados antes que esses componentes filhos tentem ser renderizados. Caso contrário, eles podem não funcionar corretamente ou gerar erros, pois dependem do contexto e dos dados fornecidos pelo `SnkDataUnit` pai.

A abordagem recomendada é utilizar o evento `onDataUnitReady` em conjunto com `useState` para gerenciar o estado de prontidão e condicionar a renderização dos componentes filhos. O evento `onDataUnitReady` é disparado quando a instância interna do `DataUnit` (core) está inicializada, seus metadados foram carregados e o `SnkDataUnit` está pronto para uso. Ele também emite a instância do `DataUnit` (core).

Veja o padrão recomendado:

  1. **Crie um estado** para armazenar a instância do `DataUnit` (ou `null` inicialmente):

```jsx
const [dataUnit, setDataUnit] = useState(null);
```

  2. **Defina uma função manipuladora** para o evento `onDataUnitReady` que recebe a instância do `DataUnit`:

```jsx
const handleDataUnitReady = (duInstance) => {
    // duInstance é a instância do DataUnit (core)
    console.log("DataUnit está pronto!", duInstance);
    setDataUnit(duInstance); // Armazena a instância no estado
};
```

  3. **Passe o manipulador** para a propriedade `onDataUnitReady` do `SnkDataUnit` e **renderize condicionalmente** os filhos verificando se o estado `dataUnit` é truthy:

```jsx
<SnkDataUnit
    entityName="SuaEntidade"
    onDataUnitReady={handleDataUnitReady}
>
    {dataUnit && <SnkCrud />}
    {/* Outros componentes filhos que dependem do DataUnit também aqui */}
</SnkDataUnit>
```

Este padrão assegura que o `<SnkCrud />` (ou outros componentes dependentes) só será montado no DOM quando o estado `dataUnit` contiver a instância do `DataUnit` (core), ou seja, após o evento `onDataUnitReady` ter sido disparado e o estado atualizado.

Se você precisar da referência ao componente `SnkDataUnit` para chamar seus métodos (ex: `snkDataUnitRef.current.navigateToKey()`), você ainda pode usar `useRef`. No entanto, para apenas garantir a instanciação do DataUnit (core) antes de renderizar filhos, `onDataUnitReady` e o armazenamento da instância do `DataUnit` no estado é a forma mais direta e recomendada.

## Variações e estados

### Após salvar

> Propriedade utilizada: **afterSave**

Define o método a ser executado após a conclusão da operação de salvar.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud} from "@sankhyalabs/sankhyablocks/react/components";

/** Para simular tente inserir um item
 * e clique sobre o botão "Salvar" do CRUD.
 * Uma mensagem de alerta deve aparecer depois de salvar.
 */
const afterSave = () => {
    alert("Depois de salvar");
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnit(duInstance);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                afterSave={afterSave}
                className="ez-size-height--full"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnit && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Antes de salvar

> Propriedade utilizada: **beforeSave**

Define o método a ser executado antes da tentativa de salvar os dados. Pode ser usado para validações.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

/** Para simular tente inserir um item
 * e clique sobre o botão "Salvar" do CRUD.
 * Uma mensagem de alerta deve aparecer antes de salvar.
 */
const beforeSave = () => {
    alert("Antes de salvar");
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnit(duInstance);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                beforeSave={beforeSave}
                onDataUnitReady={handleDataUnitReady}>
                {dataUnit && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Estado dos dados

> Propriedade utilizada: **dataState**

Representa o estado atual dos dados gerenciados pelo **SnkDataUnit** (ex: se há dados sujos, modo de inserção, etc.).

```jsx
import React, {useState, useRef} from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkDataUnitRef = useRef(null);
    const [dataUnitForCrud, setDataUnitForCrud] = useState(null);
    const [copyMode, setCopyMode] = useState(null);
    const [insertionMode, setInsertionMode] = useState(null);
    const [isDirty, setIsDirty] = useState(null);
    const [hasDirtyRecords, setHasDirtyRecords] = useState(null);
    const [hasNext, setHasNext] = useState(null);
    const [hasPrevious, setHasPrevious] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnitForCrud(duInstance);
    };

    const updateDataStateList = () => {
        let dataState = snkDataUnitRef.current.dataState;
        setCopyMode(dataState.copyMode);
        setInsertionMode(dataState.insertionMode);
        setIsDirty(dataState.isDirty);
        setHasDirtyRecords(dataState.hasDirtyRecords);
        setHasNext(dataState.hasNext);
        setHasPrevious(dataState.hasPrevious);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <div className="ez-flex ez-flex--column ez-margin--medium">
                <label className="ez-label">{"copyMode: " + copyMode}</label>
                <label className="ez-label">{"insertionMode: " + insertionMode}</label>
                <label className="ez-label">{"isDirty: " + isDirty}</label>
                <label className="ez-label">{"hasDirtyRecords: " + hasDirtyRecords}</label>
                <label className="ez-label">{"hasNext: " + hasNext}</label>
                <label className="ez-label">{"hasPrevious: " + hasPrevious}</label>
            </div>
            <EzButton onClick={updateDataStateList} label="Clique para atualizar o status exibido na lista" />
            <SnkDataUnit
                ref={snkDataUnitRef}
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnitForCrud && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
}

export default Demo;
```

### Nome do SnkDataUnit

> Propriedade utilizada: **dataUnitName**

Nome utilizado para identificar e armazenar em cache a instância do `DataUnit` (core) gerenciada por este `SnkDataUnit`. Se diferentes componentes `SnkDataUnit` na mesma tela usarem o mesmo `dataUnitName` para a mesma `entityName`, eles compartilharão a mesma instância do `DataUnit` (core). Se omitido, um nome será gerado internamente, geralmente baseado no `entityName`.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit dataUnitName="principal">
            <SnkCrud />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Identificador da configuração de metadados

> Propriedade utilizada: **configName**

Identificador da configuração de metadados específica a ser carregada para o `DataUnit`. Permite carregar diferentes conjuntos de metadados (campos, visibilidade, etc.) para a mesma entidade.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataUnit } from '@sankhyalabs/core';

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit configName='__CONFIG_TEST_NAME' dataUnit={new DataUnit()}>
            <SnkCrud />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Definindo DataUnit

> Propriedade utilizada: **dataUnit**

Propriedade que expõe a instância do `DataUnit` (core) gerenciada por este componente, após sua inicialização. Permite interações programáticas diretas com o `DataUnit` (core).

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataUnit } from '@sankhyalabs/core';

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit dataUnit={new DataUnit()}>
            <SnkCrud />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Nome da entidade

> Propriedade utilizada: **entityName**

Nome da entidade do ERP Sankhya cujos dados serão gerenciados por este `SnkDataUnit` (ex: 'Produto', 'Parceiro').

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit entityName="MovimentoBancario">
            <SnkCrud />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Linhas por página

> Propriedade utilizada: **pageSize**

Define o número de registros a serem carregados por página quando a paginação está habilitada.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnitInstance(duInstance);
    };
    <SnkApplication  configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            pageSize={10}
            onDataUnitReady={handleDataUnitReady}
            className="ez-size-height--full">
            {dataUnitInstance && <SnkCrud />}
        </SnkDataUnit>
    </SnkApplication>
}

export default Demo;
```

## Principais métodos

#### getDataUnit()

Retorna a instância do `DataUnit` (core) gerenciada por este componente. Útil para interações programáticas avançadas.

```jsx
import React, {useRef, useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkDataUnitRef = useRef(null);
    const [dataUnitForCrud, setDataUnitForCrud] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnitForCrud(duInstance);
    };

    const showDataUnitName = () => {
        if (snkDataUnitRef.current) {
            snkDataUnitRef.current.getDataUnit().then(dataUnit => {
                alert("Nome do dataUnit: " + dataUnit.name);
            }).catch(error => {
                console.error("Erro ao obter o DataUnit para mostrar o nome:", error);
                alert("Erro ao obter o DataUnit.");
            });
        } else {
            alert("SnkDataUnit ref não está pronta.");
        }
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <EzButton onClick={showDataUnitName} label="Mostrar nome do dataUnit" />
            <SnkDataUnit
                ref={snkDataUnitRef}
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
                className="ez-size-height--full"
            >
                {dataUnitForCrud && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Exemplos de eventos

### Ao cancelar edição

> Evento: **cancelEdition**

Evento disparado quando a edição de um registro é cancelada.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

/** Para simular tente editar um item
 * e clique sobre o botão "Cancelar" do CRUD.
 * Uma mensagem de alerta deve aparecer depois de cancelar.
 */
const cancelEdition = () => {
    alert("Edição cancelada");
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnit(duInstance);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onCancelEdition={cancelEdition}
                onDataUnitReady={handleDataUnitReady}
                className="ez-size-height--full"
            >
                {dataUnit && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Ao alterar dados

> Evento: **dataStateChange**

Evento disparado sempre que o estado dos dados gerenciados pelo `SnkDataUnit` é alterado (ex: após carregar dados, salvar, alterar um campo, selecionar um registro).

Atenção

**Antes de invocar métodos que modificam o estado do`DataUnit` dentro deste evento, reavalie se é realmente necessário fazer isso aqui.** Na maioria dos casos, os **observers nativos do DataUnit** (como `beforeDataChanged`, `afterDataChanged`, etc.) são mais apropriados e seguros para essa finalidade.

Métodos como `setFieldValue`, `addRecord`, `removeRecords`, entre outros, disparam novamente o evento `dataStateChange`, o que pode causar **loops infinitos** se não houver uma condição de parada apropriada.

**Recomendações:**

  1. **Priorize o uso dos observers do DataUnit** ao invés de modificar dados dentro deste evento.
  2. Se for absolutamente necessário modificar dados aqui, sempre adicione validações condicionais rigorosas para evitar chamadas recursivas (ex: verifique se o valor realmente mudou antes de chamar `setFieldValue` novamente).

```jsx
import React, {useState, useRef} from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);
    const [dataUnitForCrud, setDataUnitForCrud] = useState(null);
    const [copyMode, setCopyMode] = useState(null);
    const [insertionMode, setInsertionMode] = useState(null);
    const [isDirty, setIsDirty] = useState(null);
    const [hasDirtyRecords, setHasDirtyRecords] = useState(null);
    const [hasNext, setHasNext] = useState(null);
    const [hasPrevious, setHasPrevious] = useState(null);

    const dataStateChange = (ev) => {
        let dataState = ev.target.dataState;
        setCopyMode(dataState.copyMode);
        setInsertionMode(dataState.insertionMode);
        setIsDirty(dataState.isDirty);
        setHasDirtyRecords(dataState.hasDirtyRecords);
        setHasNext(dataState.hasNext);
        setHasPrevious(dataState.hasPrevious);
    };

    const handleDataUnitReady = (duInstance) => {
        setDataUnitForCrud(duInstance);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <div className="ez-flex ez-flex--column ez-margin--medium">
                <label className="ez-label">{"copyMode: " + copyMode}</label>
                <label className="ez-label">{"insertionMode: " + insertionMode}</label>
                <label className="ez-label">{"isDirty: " + isDirty}</label>
                <label className="ez-label">{"hasDirtyRecords: " + hasDirtyRecords}</label>
                <label className="ez-label">{"hasNext: " + hasNext}</label>
                <label className="ez-label">{"hasPrevious: " + hasPrevious}</label>
            </div>
            <SnkDataUnit
                ref={snkDataUnit}
                entityName="MovimentoBancario"
                onDataStateChange={dataStateChange}
                onDataUnitReady={handleDataUnitReady}
                className="ez-size-height--full"
            >
                {dataUnitForCrud && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Quando o DataUnit está pronto

> Evento: **dataUnitReady**

Evento disparado quando a instância interna do `DataUnit` (core) está inicializada, seus metadados foram carregados e o `SnkDataUnit` está pronto para uso.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnit, setDataUnit] = useState(false);

    const handleDataUnitReady = (dataUnit) => {
        alert("O DataUnit está pronto");
        setDataUnit(dataUnit);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}>
                {dataUnit && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Ao iniciar cadastro de um novo registro

> Evento: **insertionMode**

Evento disparado quando o `SnkDataUnit` entra no modo de inserção, seja ao adicionar um novo registro ou ao copiar um existente.

```jsx
import React, { useState } from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

/** Para simular tente cadastrar um novo registro
 * Uma mensagem de alerta deve aparecer.
 */
const insertionMode = () => {
    alert("Entrou em modo de inserção");
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState(null);

    const handleDataUnitReady = (duInstance) => {
        setDataUnit(duInstance);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onInsertionMode={insertionMode}
                onDataUnitReady={handleDataUnitReady}
                className="ez-size-height--full"
            >
                {dataUnit && <SnkCrud />}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Row Metadata

### Propriedade rmp (Row Metadata Provider)

O Row Metadata Provider (`rmp`) é uma propriedade configurada no dicionário de dados para um campo de uma entidade. Ela especifica o nome do _provider_ (uma classe Java no backend) responsável por fornecer metadados dinâmicos para aquele campo, baseados no valor de outros campos do mesmo registro.

### Propriedade rm_precision (Row Metadata Precision)

A propriedade Row Metadata Precision (`rm_precision`) também é configurada no dicionário de dados para um campo. Seu valor indica o caminho (ex: `NOME_DO_CAMPO_RMP.decVlr`) dentro dos dados retornados pelo `rmp` que contém a precisão numérica a ser aplicada ao campo atual. Isso permite, por exemplo, que a precisão de um campo de valor monetário seja definida dinamicamente com base na moeda selecionada em outro campo.

### Apresentação dos dados com rm_precision

Quando existem campos com a propriedade **rm_precision** , os componentes de grade e formulário mostram corretamente a precisão definida pelo provider.

#### Grade

Cada linha será apresentada com as precisões corretas de cada coluna, a depender do valor do provider definido.

No exemplo abaixo, cada produto possui uma configuração diferente de casas decimais (rm_precision) para as colunas de Quantidade e Vlr. Unitário.

#### Formulário

Cada registro será apresentado com as precisões corretas de cada campo, a depender do valor do provider definido.

No exemplo abaixo, o produto do registro selecionado possui uma configuração de 5 casas decimais para o campo Vlr. Unitário e 3 casas decimais para o campo Quantidade.

### Row Metadata no DataState

O DataState disparado pelo evento **dataStateChange** contém algumas informações de row metadata. A propriedade **metadataByRow** é um map com rmp por ID de registro. E a propriedade **rowMetadata** é o rmp do registro selecionado.

```jsx
import React, {useState, useRef} from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const snkDataUnit = useRef(null);
    const [dataUnitForCrud, setDataUnitForCrud] = useState(null);
    const [rowMetadata, setRowMetadata] = useState(null);
    const [metadataByRow, setMetadataByRow] = useState(null);
    const [controleRmp, setControleRmp] = useState(null);

    const dataStateChange = (ev) => {
        let dataState = ev.target.dataState;
        setRowMetadata(dataState.rowMetadata);
        setMetadataByRow(dataState.metadataByRow);

        const controleRmps = dataState.rowMetadata?.getProp('CODPROD.PRODUTORMP.controle');
        setControleRmp(controleRmps);
    };

    const handleDataUnitReady = (duInstance) => {
        setDataUnitForCrud(duInstance);
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <div className="ez-flex ez-flex--column ez-margin--medium">
                <label className="ez-label">{"rowMetadata: " + rowMetadata}</label>
                <label className="ez-label">{"metadataByRow: " + metadataByRow}</label>
                <label className="ez-label">{"controleRmp: " + controleRmp}</label>
            </div>
            <SnkDataUnit
                ref={snkDataUnit}
                entityName="ItemNota"
                onDataStateChange={dataStateChange}
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitForCrud && <SnkCrud />}
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
| afterSave | -- | Executado após a ação de salvar. | (dataUnit: DataUnit) => void | undefined |
| beforeSave | -- | Executado imediatamente antes da ação de salvar as alterações. Útil no caso de validações por exemplo. Caso retorne "false" (ou a promessa se resolva como false), cancela a ação. | (dataUnit: DataUnit) => boolean \| Promise<boolean> | undefined |
| configName | config-name | Usado para obter configuração de metadados. | string | undefined |
| dataState | -- | Controla o estado atual dos dados. | DataState | undefined |
| dataUnit | -- | Uma vez instanciado, pode-se obter o dataUnit por esta propriedade. | DataUnit | undefined |
| dataUnitName | data-unit-name | Usado para criar o dataUnit uma única vez. Se omitido, será usado o próprio nome da entidade. | string | undefined |
| domainMessagesBuilder | domain-messages-builder | Define a chave customizada para sobrescrever as mensagens (Não pegando pela entidade) | string | undefined |
| entityName | entity-name | Determina qual a entidade que representa os dados em questão. | string | undefined |
| ignoreSaveMessage | ignore-save-message | Responsável por evitar a mensagem de sucesso ao salvar. | boolean | undefined |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| pageSize | page-size | Determina quantas linhas são retornadas por página. | number | 150 |
| resourceID | resource-i-d | Identificador de recursos como configurações e acesso. | string | undefined |
| useCancelConfirm | use-cancel-confirm | Determina se será usado mensagem de confirmação padrão na tentativa de cancelar a edição. | boolean | true |

### Events

| Event | Description | Type |
|---|---|---|
| cancelEdition | Emitido quando se cancela uma inserção ou cópia. | CustomEvent<void> |
| dataStateChange | Emitido quando há qualquer mudança de estado no DataUnit. | CustomEvent<DataState> |
| dataUnitFieldsHidded | Emitido quando há campos no DataUnit que devem ser ocultados. | CustomEvent<void> |
| dataUnitReady | Emitido quando o DataUnit está pronto. | CustomEvent<DataUnit> |
| insertionMode | Emitido quando um registro é adicionado ou copiado. | CustomEvent<void> |
| messagesBuilderUpdated | Emitido quando o messagesBuilder é atualizado. | CustomEvent<SnkMessageBuilder> |

### Methods

#### `getDataUnit() => Promise<DataUnit>`

Obtém o dataUnit.

##### Returns

Type: `Promise<DataUnit>`

Uma promessa que resolve com a instância do DataUnit.

#### `getFieldsWithRmPrecision() => Promise<string[]>`

Retorna os campos que possuem a propriedade "rm_precision" (Row Metadata Precision).

##### Returns

Type: `Promise<string[]>`

Uma promessa que resolve com um array de nomes de campos.

#### `getFieldsWithRmp() => Promise<string[]>`

Retorna os campos que possuem a propriedade "rmp" (Row Metadata Provider).

##### Returns

Type: `Promise<string[]>`

Uma promessa que resolve com um array de nomes de campos.

#### `getRowMetadata(record?: Record | string) => Promise<RowMetadata>`

Busca os metadados da linha selecionada.

##### Returns

Type: `Promise<RowMetadata>`

Uma promessa que resolve com os metadados da linha.

#### `getSelectedRecordsIDsInfo() => Promise<Array<IRecordID>>`

Método que retorna a lista de IDs dos registros selecionados.

##### Returns

Type: `Promise<IRecordID[]>`

Retorna uma promessa que resolve com a lista de IDs dos registros selecionados.

### Dependencies

#### Used by

  * snk-detail-view
  * snk-guides-viewer
  * snk-simple-crud
