> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-crud/ (snapshot 2026-09-28)

# CRUD

Introdução

O **SnkCrud** é um componente completo para operações de cadastro (CRUD: Create, Read, Update, Delete) de entidades de negócio. Ele reúne, de forma padronizada, uma grade de dados (**SnkGrid**), barra de filtros (**SnkFilterBar**) e formulário (**SnkForm**), além de recursos como barra de tarefas, atalhos de teclado, customização de renderização e edição de campos.

Este componente foi projetado para acelerar o desenvolvimento de telas de manutenção de dados, garantindo consistência visual e funcional nas aplicações Sankhya.

## Quando utilizar o SnkCrud

  * Quando for necessário criar telas de manutenção de dados (cadastros) com operações padrão de inclusão, edição, exclusão e navegação.
  * Quando desejar padronizar a experiência do usuário em diferentes cadastros do sistema.
  * Quando precisar de recursos avançados como múltipla seleção, customização de colunas, exportação de dados, entre outros.

## Quando **não** utilizar o SnkCrud

  * Para telas que não seguem o padrão CRUD tradicional, como dashboards, relatórios analíticos ou fluxos de processo customizados.
  * Quando a interface exigir uma experiência de usuário muito específica, que não se encaixa na estrutura de grid e formulário fornecida pelo componente.
  * Para exibição de dados simples, onde um componente de lista ou tabela básica já é suficiente.

O SnkCrud foi desenvolvido para ser utilizado em cenários de cadastro, promovendo agilidade e padronização no desenvolvimento de aplicações.

## Hierarquia

O **SnkCrud** deve ficar dentro de um **SnkDataUnit** , que contém os metadados e os controles de ações e interações com os componentes do **SnkCrud**. O **SnkDataUnit** , por sua vez, deve ser implementado dentro de um **SnkApplication** , que contém os dados de configurações, permissões de acesso e controle de mensagens padrão da aplicação.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
        <SnkCrud />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

## Atenção ao uso com SnkDataUnit

Importante

Ao utilizar o **SnkCrud** (assim como **SnkForm** ou **SnkGrid**) como filho direto de um **SnkDataUnit** , é fundamental garantir que o **SnkDataUnit** esteja completamente inicializado e seus metadados carregados **antes** de renderizar o SnkCrud. Caso contrário, o SnkCrud pode não funcionar corretamente ou apresentar erros, pois depende do contexto e dos dados fornecidos pelo SnkDataUnit pai.

A abordagem recomendada é utilizar o evento `onDataUnitReady` do SnkDataUnit em conjunto com um estado (por exemplo, via `useState`) para controlar a renderização dos componentes filhos. Assim, o SnkCrud só será renderizado após o DataUnit estar pronto.

**Exemplo de padrão recomendado:**

```jsx
const [dataUnit, setDataUnit] = useState(null);

const handleDataUnitReady = (duInstance) => {
    setDataUnit(duInstance);
};

<SnkDataUnit
    entityName="SuaEntidade"
    onDataUnitReady={handleDataUnitReady}
>
    {dataUnit && <SnkCrud />}
</SnkDataUnit>
```

Dessa forma, o `<SnkCrud />` só será montado no DOM quando o DataUnit estiver pronto, evitando problemas de inicialização.

Para mais detalhes, consulte a seção correspondente na documentação do SnkDataUnit.

## Slots

Por meio dos slots usados no exemplo a seguir é possível exibir conteúdo customizado no rodapé da grade (**SnkGrid**), na barra de tarefas (**SnkTaskbar**) do formulário (**SnkForm**) e no container do **SnkConfigurator**.

  * Customizar rodapé da grade (**SnkGrid**).

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud>
                <div slot="SnkGridFooter">
                    <h1 className="ez-label">Rodapé do Grid</h1>
                </div>
            </SnkCrud>
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

  * Customizar barra de tarefas (**SnkTaskbar**) do formulário (**SnkForm**).

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud>
                <div slot="SnkFormTaskBar">
                    <h1 className="ez-label">Barra de Tarefas do Form</h1>
                </div>
            </SnkCrud>
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

  * Customizar container de configurações do **SnkConfigurator**.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud>
                <div slot="SnkConfigContainerSlot">
                    <h1 className="ez-label">Container do SnkConfig</h1>
                </div>
            </SnkCrud>
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

## Propriedades

### Gerenciador da barra de tarefas

> Propriedade utilizada: **taskbarManager**

O **taskbarManager** possibilita a customização dos botões exibidos na barra de tarefas (**SnkTaskbar**) da grade (**SnkGrid**).

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const buildTaskbarManager = () => {
    return {
        getButtons: (taskbarId, dataState, currentButtons) => {
            currentButtons.push(
                {
                    name: "novo-botao",
                    hint: "Novo Botão",
                    iconName: "check"
                }
            );
            return currentButtons;
        },
        isEnabled: (taskbarId, dataState, buttonName) => {
            return true;
        }
    }
}

const Demo = () => {
    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">
                <SnkCrud taskbarManager={buildTaskbarManager()} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Elementos nas extremidades dos campos

> Evento utilizado: **formItemsReady** (manipulador: `onFormItemsReady` em React)
>
> O evento `formItemsReady` é emitido quando os itens do formulário (campos, etc.) são renderizados e estão prontos no DOM. Ele emite um array de `HTMLElement`s que representam os itens renderizados. Este evento é útil para interagir com os elementos do formulário após sua renderização, como adicionar elementos customizados ao lado dos campos (botões, ícones, badges, etc.).
>
> No exemplo abaixo, utilizamos o manipulador `onFormItemsReady` (padrão React para o evento `formItemsReady`) para adicionar um ícone ao lado de um campo específico.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

```jsx
import { useEffect, useRef } from "react";
import {
  SnkApplication,
  SnkDataUnit,
  SnkCrud,
} from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
  function addIconInForm(items) {
    const addAttr = (el, elName) => {
      el.setAttribute("mode", "icon");
      el.setAttribute("icon-name", "chevron-right");
      el.setAttribute("title", elName);
      el.classList.add("ez-button--tertiary");
      el.addEventListener("click", function () {
        alert(`${elName} foi clicado!`);
      });
    };

    let btn = document.createElement("ez-button");
    addAttr(btn, "btn1");

    items.get("_dadosBancarios_nomeCliente")?.addRightElement(btn);
  }

  return (
    <SnkApplication configName="MovimentoBancario">
      <SnkDataUnit
        entityName="MovimentoBancario"
        dataUnitName="principal"
        key="duPrincipal"
      >
        <SnkCrud onFormItemsReady={(evt) => addIconInForm(evt.detail.items)} />
      </SnkDataUnit>
    </SnkApplication>
  );
};

export default Demo;
```

### Exibição do status

> Propriedade utilizada: **statusResolver**

Utilizando o **statusResolver** é possível exibir uma coluna à esquerda da grade (**SnkGrid**), representando o status daquele registro por meio de uma cor, de acordo com o valor dos campos.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const getStatusResolver = () => {
    return {
        "CONCILIADO": {
            "false" : "#BD0025",
            "true" : "#157A00"
        }
    };
}

const Demo = () => {
    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">
                <SnkCrud statusResolver={getStatusResolver()} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

###

O resolvedor de status também pode ser uma função.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    // Exemplo de uma definição para o Status na grade,
    // baseando no valor do campo "Conciliado?".
    const statusResolver = dataRow => {
        if(dataRow.CONCILIADO){
            return "#157A00"; // green = Sim
        }

        return "#BD0025"; // red = Não
    }

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">
                <SnkCrud statusResolver={getStatusResolver} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Múltiplas seleções

> Propriedade utilizada: **multipleSelection**

O **multipleSelection** permite a seleção de múltiplos registros na grade (**SnkGrid**).

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud multipleSelection={true}/>
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Parâmetro ENTER como TAB

> Propriedade utilizada: **useEnterLikeTab**

O **useEnterLikeTab** possibilita assumir que a tecla `ENTER` tenha o comportamento da tecla `TAB`.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud useEnterLikeTab={true} />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Apresentação da barra de tarefas

> Propriedade utilizada: **presentationMode**

O **presentationMode** altera o modo de apresentação dos botões da barra de tarefas (**SnkTaskbar**).

Informação

A definição do modo de apresentação pode ser realizada por meio dos valores:

  * **primary** \- É o modo **padrão** utilizado para apresentar os botões na barra de tarefas (**SnkTaskbar**);
  * **secondary** \- É o modo **secundário** que altera o formato e ordenação dos botões na barra de tarefas (**SnkTaskbar**).

É necessário informar esse valor como uma _string_ , conforme será apresentado no exemplo a seguir.

#### Barra de tarefas na grade

#### Barra de tarefas no formulário

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud presentationMode="secondary" />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Carregamento automático de registros

> Propriedade utilizada: **autoLoad**

O **autoLoad** controla se os dados serão carregados na inicialização do componente.

Caso a propriedade seja atribuída, o seu valor será respeitado, independente dos parâmetros estabelecidos, caso não, o componente seguirá seu fluxo padrão, onde será respeitado o parâmetro **global.carregar.registros.iniciar.tela**.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud autoLoad={false} />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Foco automático

> Propriedade utilizada: **autoFocus**

Por padrão, a grade possui foco automático, sendo importante para casos onde possui implementações de atalhos de teclado. Porém, existe alguns casos onde o desenvolvedor pode desejar que a mesma não ocorra, para isso, existe a propriedade booleana `autoFocus` onde pode ser definido seu comportamento.

```jsx
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
        <SnkDataUnit
            entityName="MovimentoBancario"
            dataUnitName="principal"
            key="duPrincipal">
            <SnkCrud autoFocus={false} />
        </SnkDataUnit>
    </SnkApplication>
);

export default Demo;
```

### Habilitar inserção na grade

> Propriedade utilizada: **enableGridInsert**

Por padrão, a inserção na grade está desabilitada. Quando ativada, ela permite que o usuário adicione novos registros diretamente na grade, respeitando o modo de visualização atual. A inserção segue o contexto da visualização do usuário:

  * Se o usuário estiver no **modo formulário** , a inserção será realizada via formulário.
  * Se o usuário estiver no **modo grade** , a inserção será feita diretamente na grade.

Conforme mostrado abaixo, ao clicar em "Cadastrar", o modo grade é mantido, permitindo que novos itens sejam inseridos diretamente na grade.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    return (
        <SnkApplication configName="Parceiro">
            <SnkDataUnit
                entityName="Parceiro"
                dataUnitName="principal"
                key="duPrincipal">
                <SnkCrud enableGridInsert={true} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Inserção contínua

Quando a propriedade de **Inserção Contínua** estiver habilitada, uma nova opção é adicionada às 'Mais Opções' na barra de tarefas da grade, no topo da lista: **Ativar Inserção Contínua**.

Ao ativar, o item de menu muda para **Desativar Inserção Contínua**. Sempre que uma nova inserção for finalizada, seja ao salvar ou ao trocar de linha, um novo registro é automaticamente criado e posicionado na primeira célula editável, caso o salvamento seja bem-sucedido.

Quando a **Inserção Contínua** está ativada, o rótulo do menu muda, permitindo desativá-la.

### Feedback de erros durante a inserção

Quando uma coluna contém um valor inválido, o sistema oferece feedback visual e textual do erro. Um **Toast** é exibido com a mensagem de erro, e a borda da célula inválida é destacada em vermelho. Além disso, o foco é automaticamente direcionado para a célula com erro.

## Configurações Legadas (Legacy Configurations)

O **SnkCrud** suporta três propriedades para integração com configurações legadas do sistema Sankhya, permitindo manter a compatibilidade com configurações existentes criadas em versões anteriores do Layout(Flex ou HTML5).

### Configuração legada do formulário

> Propriedade utilizada: **formLegacyConfigName**

A propriedade **formLegacyConfigName** especifica a chave da configuração legada do formulário na tabela, permitindo que o componente utilize configurações de layout e campos previamente definidas.

Observação

Embora esse seja um padrão comum entre as telas, tenha cuidado, pois algumas telas podem não utilizar o padrão.

**Padrão comum:**

```text
FormCfg:{CHAVE DA TABELA}
```

**Exemplo de uso:**

```jsx
import React from 'react';
import { SnkCrud, SnkDataUnit, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

/**
* Este exemplo é a utilização da propriedade na Grade de itens da tela Central de Notas.
* Este exemplo pode não ser funcional em um ambiente de desenvolvimento isolado,
* pois depende de configurações e contextos específicos do Sankhya Om.
*/
function ExemploFormLegacy() {
    // Em um cenário real, 'usePortalContext' forneceria o resourceId.
    // const { resourceId } = usePortalContext();
    const formLegacyConfigName = "FormCfg:GradeItens:br.com.sankhya.com.mov.CentralNotas";

    return (
        <SnkApplication configName="CentralNotas">
            <SnkDataUnit entityName="ItemNota">
                <SnkCrud
                    configName="gradeitens"
                    formLegacyConfigName={formLegacyConfigName}
                />
            </SnkDataUnit>
        </SnkApplication>
    );
}

export default ExemploFormLegacy;
```

### Configuração legada da barra de filtros

> Propriedade utilizada: **filterBarLegacyConfigName**

A propriedade **filterBarLegacyConfigName** define a configuração legada da barra de filtros, mantendo a configuração de filtros de layouts anteriores.

Observação

Embora esse seja um padrão comum entre as telas, tenha cuidado, pois algumas telas podem não utilizar o padrão.

**Padrão comum:**

```text
{resourceId}
```

**Exemplo de uso:**

```jsx
import React from 'react';
import { SnkCrud, SnkDataUnit, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

/**
* Exemplo da tela Central de notas.
* Este exemplo pode não ser funcional em um ambiente de desenvolvimento isolado,
* pois depende de configurações e contextos específicos do Sankhya Om, como 'usePortalContext'.
*/
function ExemploFilterBarLegacy() {
    // Em um cenário real, 'usePortalContext' forneceria o resourceId.
    // const { resourceId, currentTipMov } = usePortalContext();
    const resourceId = "br.com.sankhya.com.mov.CentralNotas"; // Valor de exemplo
    const filterBarLegacyConfigName = `${resourceId}`;

    return (
        <SnkApplication configName="CentralNotas">
            <SnkDataUnit entityName="CabecalhoNota">
                <SnkCrud
                    configName="CabecalhoNota"
                    filterBarLegacyConfigName={filterBarLegacyConfigName}
                />
            </SnkDataUnit>
        </SnkApplication>
    );
}

export default ExemploFilterBarLegacy;
```

### Configuração legada da grade

> Propriedade utilizada: **gridLegacyConfigName**

A propriedade **gridLegacyConfigName** especifica a configuração legada da grade, preservando configurações de colunas, ordenação e layout definidas anteriormente.

Observação

Embora esse seja um padrão comum entre as telas, tenha cuidado, pois algumas telas podem não utilizar o padrão.

**Padrão comum:**

```text
GrdCfgHtml5:{resourceId}
```

**Exemplo de uso:**

```jsx
import React from 'react';
import { SnkCrud, SnkDataUnit, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

/**
* Exemplo da tela Consulta de Produtos.
* Este exemplo pode não ser funcional em um ambiente de desenvolvimento isolado,
* pois depende de configurações e contextos específicos do Sankhya Om, como 'usePortalContext'.
*/
function ExemploGridLegacy() {
    // Em um cenário real, 'usePortalContext' forneceria o resourceId.
    // const { resourceId } = usePortalContext();
    const resourceId = "br.com.sankhya.com.cons.ConsultaProdutos"; // Valor de exemplo
    const gridLegacyConfigName = `GrdCfgHtml5:${resourceId}`;

    return (
        <SnkApplication configName="ConsultaProdutos">
            <SnkDataUnit entityName="Produto"> {/* Ajustado para uma entidade mais provável */}
                <SnkCrud
                    configName="dgProdutos" /* Nome de config de exemplo */
                    gridLegacyConfigName={gridLegacyConfigName}
                />
            </SnkDataUnit>
        </SnkApplication>
    );
}

export default ExemploGridLegacy;
```

### Exemplo completo com todas as configurações

```jsx
import React from 'react';
import { SnkCrud, SnkDataUnit, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

/**
* Exemplo da tela Central de notas.
* Este exemplo pode não ser funcional em um ambiente de desenvolvimento isolado,
* pois depende de configurações e contextos específicos do Sankhya Om,
* como 'usePortalContext' e 'useLancamentoContext'.
*/
function ExemploCompletoLegacyConfig() {
    // Em um cenário real, 'usePortalContext' e 'useLancamentoContext' forneceriam os valores.
    // const { resourceId, currentTipMov } = usePortalContext();
    // const { currentLancamento } = useLancamentoContext();
    const resourceId = "br.com.sankhya.com.mov.CentralNotas"; // Valor de exemplo

    // Configuração do formulário
    const formLegacyConfigName = `FormCfg:${resourceId}`;

    // Configuração da barra de filtros
    const filterBarLegacyConfigName = `${resourceId}`;

    // Configuração da grade
    const gridLegacyConfigName = `GrdCfgHtml5:${resourceId}`;

    return (
        <SnkApplication configName="CentralNotas">
            <SnkDataUnit entityName="ItemNota">
                <SnkCrud
                    configName="gradeitens"
                    formLegacyConfigName={formLegacyConfigName}
                    filterBarLegacyConfigName={filterBarLegacyConfigName}
                    gridLegacyConfigName={gridLegacyConfigName}
                />
            </SnkDataUnit>
        </SnkApplication>
    );
}

export default ExemploCompletoLegacyConfig;
```

### Considerações importantes

Configurações Legadas

  * As configurações legadas são específicas para cada tela do sistema Sankhya.
  * Os nomes devem corresponder exatamente às configurações existentes no banco de dados
  * Quando não especificadas, o componente utilizará as configurações padrão baseadas no `configName`
  * É recomendado criar hooks personalizados para centralizar a lógica de geração dos nomes de configuração

Boas Práticas

  * Utilize hooks personalizados para gerar os nomes de configuração de forma consistente
  * Considere parâmetros do sistema para determinar dinamicamente as configurações
  * Documente os padrões de nomenclatura utilizados em sua aplicação
  * Teste as configurações em diferentes layouts(Flex / HTML5) para garantir compatibilidade

## Principais métodos

### Navegação entre modos de visualização

> Metodo utilizado: **goToView()**

Com o método **goToView** é possível alternar entre os modos de visualização disponíveis no **SnkCrud** , sendo eles o formulário, grade e o configurador.

```jsx
import React, {useRef} from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const snkDataUnit = useRef(null);
    const application = useRef(null);
    const snkCrud = useRef(null);

    const viewForm = () => {
        snkCrud.current.goToView('FORM_MODE');
    }

    const viewGrid = () => {
        snkCrud.current.goToView('GRID_MODE');
    }

    const viewConfigurator = () => {
        snkCrud.current.goToView('CONFIGURATOR');
    }

    return (
        <SnkApplication ref={application} configName="MovimentoBancario">
            <EzButton label="Exibir Form" onClick={viewForm} className="ez-margin-top--medium" />
            <EzButton label="Exibir Grid" onClick={viewGrid} className="ez-margin-top--medium" />
            <EzButton label="Exibir Configurador" onClick={viewConfigurator} className="ez-margin-top--medium" />
            <SnkDataUnit
                ref={snkDataUnit}
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">

                <SnkCrud ref={snkCrud} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Renderização de componentes customizados

> Método utilizado: **addGridCustomRender()**

Com o método **addGridCustomRender** é possível alterar o elemento que é mostrado em uma coluna específica da grade principal do **SnkCrud** , podendo criar um elemento customizado dependendo ou não dos valores anteriores.

Importante

Ao retornar o elemento como string ou utilizando o método `renderToString` provido pelo `react-dom/server`, não será aplicado **nenhum** código JavaScript, portanto, caso necessário (para a criação de um botão, por exemplo) é necessário que o elemento seja criado a partir do `document`, utilizando o método `createElement`.

#### Parâmetros

São passados alguns parâmetros para o método `getRenderElement`, sendo eles:

  * **value** \- Retorna o valor da célula.
  * **currentRender** \- Retorna o elemento padrão.
  * **name** \- Retorna o nome do campo.
  * **getValue** \- Método que retorna o valor da célula.
  * **detailContext** \- Retorna o contexto do master/detail.
  * **renderMetadata** \- Retorna o metadata da célula.

```jsx
import { EzButton } from "@sankhyalabs/ezui/react/components";
import { SnkApplication, SnkCrud, SnkDataUnit } from "@sankhyalabs/sankhyablocks/react/components";
import React, { useRef } from 'react';
import { renderToString } from "react-dom/server";

const Demo = () => {
    const snkDataUnit = useRef(null);
    const application = useRef(null);
    const snkCrud = useRef(null);

    const setCustomElement = () => {
        const customRender = {
            getRenderElement: () => {
                const element = document.createElement('div');
                element.textContent = 'Esse é um elemento totalmente customizado!';
                return element;
            }
        };
        snkCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const setCustomElementString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const elemment = `<div class='ez-text--tertiary'>Valor do campo: ${params.value}</div>`;
                return elemment;
            }
        };
        snkCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const setCustomElementReactString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const Element = <div className="ez-text--tertiary">Valor do campo: {params.value}</div>
                const stringElement = renderToString(Element);
                return stringElement;
            }
        };
        snkCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const editElement = () => {
        const customRender = {
            getRenderElement: (params) => {
                const element = params.currentRender;
                element.textContent = `Valor do campo: ${params.value}`;
                element.className = "ez-text--tertiary";
                return element;
            }
        };
        snkCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const cleanElement = () => {
        const customRender = {
            getRenderElement: () => {}
        };
        snkCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    return (
        <SnkApplication ref={application} configName="MovimentoBancario">
            <EzButton label="Exibir elemento nativo customizado" onClick={setCustomElement} className="ez-margin-top--medium" />
            <EzButton label="Exibir elemento em string customizado" onClick={setCustomElementString} className="ez-margin-top--medium" />
            <EzButton label="Exibir elemento utilizando o reactToString" onClick={setCustomElementReactString} className="ez-margin-top--medium" />
            <EzButton label="Exibir elemento editado" onClick={editElement} className="ez-margin-top--medium" />
            <EzButton label="Resetar elemento" onClick={cleanElement} className="ez-margin-top--medium" />
            <SnkDataUnit
                ref={snkDataUnit}
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">

                <SnkCrud ref={snkCrud} />
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Renderização de editores customizados

> Método utilizado: **addCustomEditor()**

Através deste método, é possível adicionar editores customizados (**ICustomEditor**) para campos específicos. Este editor será aplicado tanto na grade principal quanto no formulário.

Quando nenhum editor customizado é adicionado à coluna, seu campo padrão é renderizado.

Existem quatro retornos possíveis para o método **getEditorElement** do **ICustomEditor** , sendo eles:

  * **Nulo/indefinido** : renderiza o elemento padrão para aquele campo;
  * **O elemento padrão** : renderiza o elemento padrão para aquele campo;
  * **Uma string** : faz o parse da string e renderiza o elemento passado;
  * **Um elemento HTML** : renderiza o elemento.

Nos parâmetros da função getEditorElement, existe o atributo **source** , através do qual é possível definir o editor para grade ou formulário.

Importante

O método **renderToString** não aceita **nenhum** código JavaScript. Para um botão, por exemplo, um onClick não irá funcionar. O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTML.

```jsx
import { useCallback, useEffect, useRef, useState } from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { renderToString } from 'react-dom/server';
import { SnkApplication, SnkCrud, SnkDataUnit } from '@sankhyalabs/sankhyablocks/react/components';

const Demo = () => {
    const snkCrudRef = useRef(null);
    const snkDataUnitRef = useRef(null);

    const [dataUnit, setDataUnit] = useState();

    const addCustomEditor = useCallback(async () => {
        const customEditorVlrMoeda = {
            getEditorElement: () => {
                return null;
            }
        }

        const customEditorVlrLancDestino = {
            getEditorElement: (params) => {
                return params.currentEditor;
            }
        }

        const customEditorNuBancario = {
            getEditorElement: ({source}) => {
                if(source === "FORM") {
                    return renderToString(<EzButton label='Teste'/>);
                }
                return renderToString(<button>Teste</button>);
            }
        }

        const customEditorUsuario = {
            getEditorElement: ({source, setValue, value}) => {
                if(source === "FORM") {
                    const launchButton = document.createElement('ez-button');
                    launchButton.mode = 'icon';
                    launchButton.iconName = 'warning-outline';
                    launchButton.onclick = () => {console.log('CLICK DO BOTÃO')};

                    return launchButton;
                }
                const textInput = document.createElement('input');
                textInput.value = value;
                textInput.onkeyup = (event) => {
                    setValue(event.target.value);
                };
                return textInput;
            }
        }

        await snkCrudRef.current.addCustomEditor('VLRMOEDA', customEditorVlrMoeda);
        await snkCrudRef.current.addCustomEditor('VLRLANC_DESTINO', customEditorVlrLancDestino);
        await snkCrudRef.current.addCustomEditor('NUBCO', customEditorNuBancario);
        await snkCrudRef.current.addCustomEditor('CODUSU', customEditorUsuario);
    }, [snkCrudRef]);

    useEffect(() => {
        snkDataUnitRef.current.getDataUnit().then(dataunit => setDataUnit(dataunit));
    }, [snkDataUnitRef]);

    useEffect(() => {
        if(!snkCrudRef?.current) {
            return;
        }

        addCustomEditor();
    }, [snkCrudRef, dataUnit]);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                ref={snkDataUnitRef}
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
            >
                <SnkCrud ref={snkCrudRef}/>
            </SnkDataUnit>
        </SnkApplication>
    )
};

export default Demo;
```

Importante

Ao utilizar um input no elemento customizado, é necessário que se utilize o listener `onkeyup`, com o objetivo de sempre capturar o novo valor a cada tecla pressionada. Desta forma, o ciclo de vida da grade não interfere na mudança de valor.

## Exemplos de eventos

> Evento utilizado: **onActionClick**

Evento ao clicar em um item da barra de tarefas.

Por meio do **onActionClick** é possível atribuir um processo que será executado quando o usuário clicar em algum botão da barra de tarefas (**SnkTaskbar**).

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit, SnkCrud } from "@sankhyalabs/sankhyablocks/react/components";

const actionClick = () => {
    alert("ok");
};

const Demo = () => {
    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal">

                <SnkCrud onActionClick={actionClick} />

            </SnkDataUnit>
        </SnkApplication>
    );

};

export default Demo;
```

## Customização de mensagens

Por meio do **SnkMessageBuilder** é possível a customização de mensagens dos blocos de construção utilizando um pequeno módulo na estrutura da aplicação:

  * Criar um arquivo no seguinte caminho: /messages/appmessages.msg.js.
  * Para conhecer os detalhes do módulo, vide os arquivos neste projeto "/src/lib/message/resources/*.msg.ts"

## Formatador personalizado

Na grade do **SnkCrud** , é possível adicionar formatadores personalizados (CustomValueFormatter) através do método **addCustomValueFormatter** do componente. Este formatador deve seguir a interface ICustomFormatter e, através do método **format** , retornar um valor formatado a ser apresentado na grade.

O método **removeCustomValueFormatter** remove um formatador personalizado previamente adicionado.

## Alteração dinâmica de props

No formulário do **SnkCrud** , é possível alterar dinamicamente propriedades de campos (como `readonly`, `label`, `visible`, etc.) através do método **setFieldProp**. Este método atua sobre os campos gerenciados pelo `snk-guides-viewer`.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| actionsList | -- | Ações a serem colocadas no botão "Mais opções" do componente snk-taskbar. | Action[] | undefined |
| autoFocus | auto-focus | Define se a grid será focada ao ser carregada. | boolean | true |
| autoLoad | auto-load | Define se a carga dos dados será feita assim que o componente for carregado. | boolean | undefined |
| configName | config-name | Usado para salvar as configurações dos blocos de construção. | string | undefined |
| disablePersonalizedFilter | disable-personalized-filter | Desabilita a apresentação da opção de filtros personalizados na filter bar (chip de filtros) e no modal lateral de filtros (container de filtros personalizados). | boolean | undefined |
| domainMessagesBuilder | domain-messages-builder | Define a chave customizada para sobrescrever as mensagens (Não pegando pela entidade) | string | undefined |
| enableGridInsert | enable-grid-insert | Ativa inserção de registros no modo grade. | boolean | false |
| enableLockManagerLoadingComp | enable-lock-manager-loading-comp | Define se o componente deve usar o LockManager para controle de carregamento da aplicação | boolean | false |
| enableLockManagerTaskbarClick | enable-lock-manager-taskbar-click | Ativa o gerenciamento de locks na grade pela Taskbar. | boolean | false |
| filterBarLegacyConfigName | filter-bar-legacy-config-name | Chave da configuração legado da barra de filtros. | string | undefined |
| filterBarTitle | filter-bar-title | Título que será apresentado na barra de filtros | string | undefined |
| formLegacyConfigName | form-legacy-config-name | Chave da configuração legado do formulário. | string | undefined |
| gridLegacyConfigName | grid-legacy-config-name | Chave da configuração legado da grade. | string | undefined |
| ignoreReadOnlyFormFields | ignore-read-only-form-fields | Ignora os campos "somente leitura" no modo de inserção. | boolean | undefined |
| layoutFormConfig | layout-form-config | Define se o LayoutFormConfig será exibido no configurador. | boolean | true |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| multipleEditionEnabled | multiple-edition-enabled | Habilita a edição de múltiplos registros simultâneos. | boolean | true |
| multipleSelection | multiple-selection | Determina se pode haver mais de uma linha selecionada na grade. | boolean | true |
| paginationCounterMode | pagination-counter-mode | Define se a grid será focada ao ser carregada. | "auto" \| "hidden" \| "show" | 'auto' |
| presentationMode | presentation-mode | Altera o modo de apresentação dos botões do snk-taskbar. | PresentationMode.PRIMARY \| PresentationMode.SECONDARY \| PresentationMode.SINGLE_TASKBAR | PresentationMode.PRIMARY |
| recordsValidator | -- | Validador responsável por checar a integridade das informações do registro. | IRecordValidator | undefined |
| selectionToastConfig | -- | Configuração da seleção de grade no toast. | ISelectionToastConfig | undefined |
| setCustomFormTitle | -- | Define uma função para configurar um título cusotmizado no modo formulário. | () => string | undefined |
| showActionButtons | show-action-buttons | Usado para exibir os botões de ação do snk-configurator | boolean | false |
| statusResolver | -- | Configuração do valor da coluna de status. Exemplo: { "RECDESP": { "-1" : "#BD0025", "1" : "#157A00" } } | ((data: object) => string) \| IStatusResolver | undefined |
| strategyExporter | strategy-exporter | Modo de exportação dos dados. | "ClientSideExporterStrategy" \| "ServerSideExporterStrategy" | ExporterStrategy.SERVER_SIDE |
| taskbarManager | -- | Gerenciador das barras de tarefas. É possível determinar botões específicos ou mesmo gerenciar o estado dos botões. | TaskbarManager | undefined |
| useEnterLikeTab | use-enter-like-tab | Quando verdadeiro, o ENTER fará a navegação como se fosse a tecla TAB na grade. | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| actionClick | Emitido pela taskbar sempre que houver click de botão ou ação. | CustomEvent<string> |
| configuratorCancel | Emitido quando cancela o salvamento da configuração no configurator do CRUD. | CustomEvent<any> |
| configuratorSave | Emitido quando salva a configuração no configurator do CRUD. | CustomEvent<any> |
| formItemsReady | Responsável por notificar quando ocorrer a renderização de itens do formulário. | CustomEvent<HTMLElement[]> |
| viewModeChanged |  | CustomEvent<VIEW_MODE.ATTACHMENT \| VIEW_MODE.FORM \| VIEW_MODE.GRID> |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

##### Returns

Type: `Promise<void>`

#### `addCustomValueFormatter(columnName: string, customFormatter: ICustomFormatter) => Promise<void>`

Registra um formatador de valores para uma coluna da grid.

##### Returns

Type: `Promise<void>`

#### `addGridCustomRender(fieldName: string, customRender: ICustomRender) => Promise<void>`

Registra um render customizado para colunas da grid.

##### Returns

Type: `Promise<void>`

#### `closeConfigurator() => Promise<void>`

Usado para fechar o configurator do CRUD

##### Returns

Type: `Promise<void>`

#### `getFilterBar() => Promise<HTMLSnkFilterBarElement>`

Retorna o elemento da filter-bar da grade.

##### Returns

Type: `Promise<HTMLSnkFilterBarElement>`

#### `goToView(mode: string) => Promise<void>`

Usado para alternar a visão entre GRID e FORM externamente.

##### Returns

Type: `Promise<void>`

#### `openConfigurator() => Promise<void>`

Usado para abrir o configurator do CRUD

##### Returns

Type: `Promise<void>`

#### `reloadFilterBar() => Promise<void>`

Faz o recarregamento da filter-bar do crud, buscando o state no servidor.

##### Returns

Type: `Promise<void>`

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

Remove o formatador de valores de uma coluna da grid.

##### Returns

Type: `Promise<void>`

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

Altera/adiciona uma propriedade nos metadados do campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * snk-grid
  * snk-guides-viewer
  * snk-attach
  * snk-configurator
  * snk-data-exporter
  * snk-actions-button
  * taskbar-split-button
  * taskbar-actions-button
