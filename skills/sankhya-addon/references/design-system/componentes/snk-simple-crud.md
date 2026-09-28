> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-crud/ (snapshot 2026-09-28)

# Simple CRUD

O **SnkSimpleCrud** é um componente independente que encapsula a lógica e a interface de usuário para operações de Cadastro, Leitura, Atualização e Exclusão (CRUD). Ele é composto por:

  * **EzGrid** : Para visualização e edição de múltiplos registros.
  * **EzForm** : Para visualização e edição detalhada de um único registro.
  * **SnkTaskbar** : Uma barra de ferramentas com ações padrão de CRUD (cadastrar, salvar, cancelar, etc.).
  * **SnkDataUnit** : Para gerenciar o estado dos dados e a comunicação com o servidor.

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const paymentMethodsRef = useRef(null);
    const [paymentMethodsDataUnit, setPaymentMethodsDataUnit] = useState(null);

    useEffect(() => {
        setPaymentMethodsDataUnit(new DataUnit("paymentMethods"));
    }, []);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleCrud ref={paymentMethodsRef} dataUnit={paymentMethodsDataUnit} />
        </SnkApplication>
    );
}

export default Demo;
```

### Principais funcionalidades:

  * **Dois modos de operação** : `SERVER` (conectado a uma entidade do backend) e `IN_MEMORY` (para manipulação de dados temporários em memória).
  * **Visualização alternável** : Permite ao usuário alternar facilmente entre a visualização em grade e em formulário.
  * **Configurabilidade** : Oferece a capacidade de salvar e carregar configurações de layout para a grade e o formulário.
  * **Extensibilidade** : Suporta a adição de editores, renderizadores e formatadores de valor customizados para atender a necessidades específicas.
  * **Edição múltipla** : Permite a edição simultânea de vários registros selecionados na grade.
  * **Exportação de dados** : Funcionalidade de exportação da grade integrada.

## Quando usar

Utilize o **SnkSimpleCrud** em cenários que requerem uma interface de manutenção de dados padrão, tais como:

  * **Cadastros simples** : Ideal para telas de cadastro que não exigem lógicas de negócio complexas, como cadastro de tipos, grupos ou configurações simples.
  * **Tabelas de apoio** : Perfeito para gerenciar dados em tabelas de apoio que são usadas em outras partes do sistema.
  * **Itens de um registro mestre** : Pode ser usado para gerenciar uma lista de itens relacionados a um registro principal em uma tela mais complexa (por exemplo, os itens de um pedido de compra, onde o `SnkSimpleCrud` estaria no modo `IN_MEMORY`).
  * **Prototipagem rápida** : Agiliza o desenvolvimento de funcionalidades de CRUD, fornecendo uma solução pronta e robusta.

## Quando não usar

Evite o uso do **SnkSimpleCrud** em situações que demandam alta customização ou lógicas de negócio complexas que o componente não suporta nativamente. Nesses casos, é mais apropriado construir a tela utilizando componentes de mais baixo nível (`EzGrid`, `EzForm`, `SnkTaskbar`) de forma separada.

  * **Fluxos de trabalho complexos** : Se a tela exige um fluxo de trabalho com múltiplos passos, validações condicionais complexas ou integrações com outros sistemas que vão além das operações de CRUD padrão.
  * **Layouts muito customizados** : Quando o layout da tela foge muito do padrão grade/formulário oferecido pelo componente.
  * **Lógica de negócio na interface** : Se há uma grande quantidade de lógica de negócio que precisa ser executada na interface do usuário e que não pode ser encapsulada em eventos ou customizadores simples.

Nesses cenários, compor a interface manualmente com os blocos de construção básicos oferece maior flexibilidade e controle sobre o resultado final.

## Diferenças entre SnkSimpleCrud e SnkCrud

Embora ambos os componentes sirvam para criar interfaces de manutenção de dados (CRUD), eles são projetados para cenários de uso distintos. A escolha entre o **SnkSimpleCrud** e o **SnkCrud** depende principalmente da complexidade da tela a ser desenvolvida.

#### SnkSimpleCrud

  * **Simplicidade** : É um componente mais leve e direto, ideal para cadastros simples e tabelas de apoio.
  * **Composição** : Utiliza componentes de base como **EzGrid** para a grade e **EzForm** para o formulário.
  * **Uso Ideal** : Perfeito para quando você precisa de uma funcionalidade de CRUD padrão sem muita customização ou lógica de negócio complexa. É ótimo para prototipagem rápida e para gerenciar itens em um contexto de mestre-detalhe (usando o modo `IN_MEMORY`).

#### SnkCrud

  * **Robustez e Complexidade** : É um componente mais completo e robusto, projetado para as telas de cadastro principais do sistema, que geralmente envolvem regras de negócio mais complexas.
  * **Composição** : Utiliza componentes mais avançados como **SnkGrid** e **SnkGuidesViewer** para o formulário, que permite a criação de formulários com abas (guias) e uma estrutura mais elaborada.
  * **Uso Ideal** : Indicado para telas que exigem um layout de formulário mais complexo, com múltiplas seções, validações avançadas e uma maior integração com as regras de negócio do ERP.

Em resumo, use **`SnkSimpleCrud`** para agilidade e simplicidade em cadastros auxiliares. Opte pelo **`SnkCrud`** quando precisar de mais poder e flexibilidade para construir as telas de cadastro centrais do sistema.

## Slots

Por meio dos slots usados no exemplo a seguir é possível inserir conteúdo no header e/ou no footer do componente.

  * Customizar rodapé da grade (**EzGrid**).

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const paymentMethodsRef = useRef(null);
    const [paymentMethodsDataUnit, setPaymentMethodsDataUnit] = useState(null);

    useEffect(() => {
        setPaymentMethodsDataUnit(new DataUnit("paymentMethods"));
    }, []);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleCrud ref={paymentMethodsRef} dataUnit={paymentMethodsDataUnit}>
                <div slot="snkSimpleCrudFooter">
                    <footer>
                        <span className="ez-title--primary ez-text ez-text--medium ez-text--bold ez-padding-bottom--medium">
                            Footer de exemplo
                        </span>
                    </footer>
                </div>
            </SnkSimpleCrud>
        </SnkApplication>
    );
}

export default Demo;
```

  * Customizar cabeçalho do componente.

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const paymentMethodsRef = useRef(null);
    const [paymentMethodsDataUnit, setPaymentMethodsDataUnit] = useState(null);

    useEffect(() => {
        setPaymentMethodsDataUnit(new DataUnit("paymentMethods"));
    }, []);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleCrud ref={paymentMethodsRef} dataUnit={paymentMethodsDataUnit}>
                <div slot="snkSimpleCrudHeader">
                    <div className="ez-flex ez-flex--column">
                        <span className="ez-title--primary ez-text ez-text--large ez-text--bold ez-padding-bottom--medium">
                            Formas de pagamento
                        </span>
                        <span className="ez-text ez-text--medium ez-text--secondary">
                            Insira quais as formas de pagamento serão utilizadas
                        </span>
                    </div>
                </div>
            </SnkSimpleCrud>
        </SnkApplication>
    );
}

export default Demo;
```

## Propriedades

### Gerenciamento de Locks

> Propriedades utilizadas: **enableLockManagerLoadingComp** , **enableLockManagerTaskbarClick**

Ativam o `LockManager` para controle de concorrência.

  * `enableLockManagerLoadingComp`: Exibe um loader e bloqueia a interação enquanto uma operação (como salvar ou carregar dados) está em andamento, prevenindo ações conflitantes.
  * `enableLockManagerTaskbarClick`: Desabilita os botões da barra de tarefas durante uma ação para evitar cliques múltiplos.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const LockManager = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && (
        <SnkSimpleCrud
          dataUnit={dataUnit}
          enableLockManagerLoadingComp={true}
          enableLockManagerTaskbarClick={true}
        />
      )}
    </SnkApplication>
  );
};

export default LockManager;
```

### Configuração Inicial da Grade e Formulário

> Propriedades utilizadas: **gridConfig** , **formConfig**

Permitem definir uma configuração inicial para a grade e o formulário, como colunas visíveis, ordenação, e campos do formulário com suas respectivas abas. Essa configuração será aplicada na primeira renderização do componente.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const gridConfig = {
  columns: [
    { name: 'HISTORICO', label: 'Historico', width: 100 },
    { name: 'NUCAIXA', label: 'Núm. Caixa', width: 300 },
    { name: 'DTLANC', label: 'Data de Lançamento', width: 150 },
  ],
  sort: [{ name: 'NUCAIXA', order: 'asc' }],
};

const formConfig = {
  fields: [
    { name: 'HISTORICO', tab: 'Geral' },
    { name: 'NUCAIXA', tab: 'Geral' },
    { name: 'DTLANC', tab: 'Valores' },
  ],
};

const InitialConfig = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && <SnkSimpleCrud dataUnit={dataUnit} formConfig={formConfig} gridConfig={gridConfig}/>}
    </SnkApplication>
  );
};

export default InitialConfig;
```

### Confirmação de Cancelamento

> Propriedade utilizada: **useCancelConfirm**

Por padrão (`true`), ao tentar cancelar uma edição com alterações pendentes, o sistema exibe uma mensagem de confirmação. Ao definir como `false`, a confirmação é desativada e a ação de cancelar é executada diretamente.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const UseCancelConfirm = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && <SnkSimpleCrud dataUnit={dataUnit} useCancelConfirm={false} />}
    </SnkApplication>
  );
};

export default UseCancelConfirm;
```

### Modo do Contador de Paginação

> Propriedade utilizada: **paginationCounterMode**

Controla a visibilidade do contador de páginas na grade.

  * `auto` (padrão): Exibe o contador apenas se houver mais de uma página.
  * `show`: Sempre exibe o contador.
  * `hidden`: Nunca exibe o contador.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

/**
 * Alterne a propriedade `paginationCounterMode` entre `hidden` e `show`.
 * Use o botão refresh da barra de ferramentas para visualizar a diferença entre o modo de paginação padrão e o modo oculto.
 */
const Demo = () => {
    const [duBancario, setDuBancario] = useState(null);
    const snkApplicationRef = useRef(null);

    useEffect(() => {
        if(snkApplicationRef.current){
            snkApplicationRef.current.createDataunit("MovimentoBancario").then(dataUnit=>{
                setDuBancario(dataUnit);
            });
        }
    }, []);

    return (
        <SnkApplication ref={snkApplicationRef}>
            {duBancario && (
               <SnkSimpleCrud dataUnit={duBancario} paginationCounterMode="hidden"/>
            )}
        </SnkApplication>
    );
};

export default Demo;
```

### Ações Customizadas

> Propriedade utilizada: **actionsList**

Permite adicionar itens personalizados ao menu “Mais opções” da barra de tarefas. Cada ação deve ser um objeto contendo as propriedades `label` e `value`.

informação

O disparo de clique no item customizado deve ser interceptado via evento ActionClick

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

/**
 * OBS: Para ouvir o disparo da ação use o evento `ActionClick`
 */
const myActions = [
  {
    label: 'Ação Customizada 1',
    value: 'CUSTOM_ACTION_1',
  },
  {
    label: 'Ação Customizada 2',
    value: 'CUSTOM_ACTION_2',
  },
];

const ActionsList = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && <SnkSimpleCrud dataUnit={dataUnit} actionsList={myActions} />}
    </SnkApplication>
  );
};

export default ActionsList;
```

### Configurações Legadas

> Propriedades utilizadas: **gridLegacyConfigName** , **formLegacyConfigName**

Permitem carregar configurações de grade e formulário a partir de chaves legadas, garantindo a compatibilidade com layouts anteriores enquanto se utiliza o `configName` para novas configurações.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

/**
 * Você deve visualizar no layout DS a ultima configuração salva no layout HTML
 */
const LegacyConfig = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const [resourceID, serResourceID] = useState(null)
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
      appRef.current.getResourceID().then(serResourceID);;
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && resourceID && (
        <SnkSimpleCrud
          dataUnit={dataUnit}
          configName="MovimentoBancario"
          gridLegacyConfigName={'GrdCfgHtml5:'+resourceID}
          formLegacyConfigName={resourceID}
        />
      )}
    </SnkApplication>
  );
};

export default LegacyConfig;
```

### Habilitar Edição Múltipla

> Propriedade utilizada: **multipleEditionEnabled**

Quando a seleção múltipla (`multipleSelection`) está ativa, esta propriedade (`true` por padrão) habilita o botão "Alterar Selecionados", permitindo a edição de vários registros simultaneamente. Defina como `false` para desabilitar essa funcionalidade.

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const MultipleEditionEnabled = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && (
        <SnkSimpleCrud
          dataUnit={dataUnit}
          multipleSelection={true}
          multipleEditionEnabled={false}
        />
      )}
    </SnkApplication>
  );
};

export default MultipleEditionEnabled;
```

### Modo de Contorno

> Propriedade utilizada: **outlineMode**

Altera o estilo visual do componente. Por padrão (`false`), aplica um efeito de sombra. Quando `true`, substitui a sombra por uma borda (contorno), ideal para quando o componente está dentro de outros contêineres como painéis ou pop-ups.

```jsx
import { useEffect, useRef, useState } from 'react';
import {
  SnkSimpleCrud,
  SnkApplication,
} from '@sankhyalabs/sankhyablocks/react/components';

const OutlineMode = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
        {dataUnit && <SnkSimpleCrud dataUnit={dataUnit} outlineMode={true} />}
    </SnkApplication>
  );
};

export default OutlineMode;
```

### Multiplas seleções

> Propriedade utilizada: **multipleSelection**

O **multipleSelection** permite a seleção de múltiplos registros na grade (**EzGrid**).

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleCrud} from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
          <SnkSimpleCrud dataUnit={movBancarioDataUnit} multipleSelection={true}/>
    </SnkApplication>
);

export default Demo;
```

### Data Unit

> Propriedade utilizada: **dataUnit**

Com esta propriedade é possível passar a instância do **DataUnit** para que o componente controle a manipulação dos dados.

```jsx
import { useEffect, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataUnit, ErrorException, StringUtils } from '@sankhyalabs/core';

const dataLoader = () => {
    return new Promise((resolve) => {
        resolve({records: [
            {
                "__record__id__": "1",
                "NOME": "Brasil",
                "POPULACAO": 214300000
              },
              {
                "__record__id__": "2",
                "NOME": "Estados Unidos",
                "POPULACAO": 332915073
              }
        ]});
    });
}

const saveLoader = (_, changes) => {
    return new Promise((resolve) => {
        let dataUnitRecords = [];

        changes.forEach(change => {
            let {record, updatingFields, operation} = change;

            if(operation === "INSERT") {
                record["__record__id__"] = StringUtils.generateUUID(updatingFields);
            }

            dataUnitRecords.push({...record, ...updatingFields});
        });

        resolve(dataUnitRecords);
    });
}

const metadataLoader = () => {
    return new Promise((resolve) => {
        resolve({
            "name": "paises",
            "label": "paises",
            "fields": [
                {
                    "name": "NOME",
                    "label": "Nome do País",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": true
                },
                {
                    "name": "POPULACAO",
                    "label": "Num. Habitantes",
                    "dataType": "NUMBER",
                    "userInterface": "INTEGERNUMBER",
                    "readOnly": false,
                    "required": false
                }
            ]
        });
    });
}

const removeLoader = (dataUnit, recordIds) => {
    if(dataUnit?.records?.length === 1) {
        throw new ErrorException('Erro ao excluir', 'É necessário pelo menos 1 país, portanto, não é possível excluí-lo.');
    }
    return new Promise((resolve) => {
        resolve(recordIds);
    });
}

const Demo = () => {
    const [contryDataUnit, setContryDataUnit] = useState(null);

    const initDataUnit = () => {
        contryDataUnit.dataLoader = dataLoader;
        contryDataUnit.saveLoader = saveLoader;
        contryDataUnit.removeLoader = removeLoader;
        contryDataUnit.metadataLoader = metadataLoader;
    }

    const loadDataUnit = () => {
        contryDataUnit.loadMetadata().then((metadata) => {
            const fields = metadata.fields.map(field => ({...field, readOnly: false}));
            contryDataUnit.metadata = {...metadata, fields};
            contryDataUnit.loadData();
            contryDataUnit.selectFirst();
        });
    }

    useEffect(() => {
        setContryDataUnit(new DataUnit("CountryDataUnit"));
    }, []);

    useEffect(() => {
        if(!contryDataUnit) {
            return;
        }

        initDataUnit();
        loadDataUnit();

    }, [contryDataUnit]);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleCrud dataUnit={contryDataUnit} />
        </SnkApplication>
    );
}

export default Demo;
```

### Entidade

> Propriedade utilizada: **entityName**

Permite configurar a entidade que o componente utilizará para fazer as operações de CRUD.

Observação:

Ao informar um **entityName** , o _simpleCRUD_ irá criar uma instância do **dataUnit**. Porém, caso já exista um **dataUnit** instanciado, a operação será ignorada e será usada a instância já criada anteriormente para realizar as operações de CRUD.

```jsx
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
  return (
    <SnkApplication configName="MovimentoBancario">
        <SnkSimpleCrud entityName={"MovimentoBancario"} />
    </SnkApplication>
  );
};

export default Demo;
```

### Modo de operação (In memory / Server)

> Propriedade utilizada: **mode**

Quando tratamos de cadastros, existem duas variações importantes. Aqueles cadastros que fazem sentido isoladamente e aqueles que só existem em determinado contexto. Por exemplo, quando estamos baixando um título, as formas de pagamento não existem a menos que a baixa seja concluída. Em outras palavras não existe uma tabela no banco de dados onde essas informações são mantidas. Até a conclusão do usuário essas informações são transitórias.

Para estes casos, onde se precisa manter os registros incluídos ou alterados em memória, existe um modo especial em que o dataunit não estará vinculado a uma entidade específica, mantendo os dados somente em memória: `mode=SIMPLE_CRUD_MODE.IN_MEMORY`.

```jsx
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataType, UserInterface } from '@sankhyalabs/core';
import { SIMPLE_CRUD_MODE } from '@sankhyalabs/sankhyablocks/dist/collection/lib/utils/constants';
import { useEffect, useRef } from "react";

const Demo = () => {
    const simpleCrud = useRef();
    useEffect(()=>{
        if(simpleCrud.current){
            const currentDate = new Date();
            simpleCrud.current.setRecords([
                { __record__id__: "01321321501", "VLRBAIXA": 10.33, "CODTIPTIT": { 'value': 1, 'label': 'À vista' }, "DHBAIXA": currentDate },
                { __record__id__: "01321321502", "VLRBAIXA": 10.33, "CODTIPTIT": { 'value': 2, 'label': '30 dias' }, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 30) },
                { __record__id__: "01321321503", "VLRBAIXA": 10.34, "CODTIPTIT": { 'value': 3, 'label': '60 dias' }, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 60) },
            ]);
        }
    }, [simpleCrud]);
    return (
        <SnkApplication>
            <SnkSimpleCrud ref={simpleCrud} mode={SIMPLE_CRUD_MODE.IN_MEMORY}>
                <snk-field-metadata name="VLRBAIXA" label="Valor" dataType={DataType.NUMBER} userInterface={UserInterface.DECIMALNUMBER} readOnly="false" />
                <snk-field-metadata name="CODTIPTIT" label="Forma de Pagamento" dataType={DataType.OBJECT} userInterface={UserInterface.SEARCH} readOnly="false" />
                <snk-field-metadata name="DHBAIXA" label="Data Baixa" dataType={DataType.DATE} userInterface={UserInterface.DATE} readOnly="false" />
            </SnkSimpleCrud>
        </SnkApplication>
    );
};

export default Demo;
```

IN_MEMORY:

Nesse modo o cadastro passa a se comportar como um simples array de registros, sendo a implementação responsável por utilizar e persistir essas informações.

### Page size

> Propriedade utilizada: **pageSize**

É possível flexibilizar quantas linhas serão exibidas na grade por vez. Por padrão a quantidade de linhas por página é 150.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    const [duMovBancario, setDuMovBancario] = useState(null);
    const application = useRef(null);

    useEffect(() => {
        if(application.current){
            application.current.createDataunit("MovimentoBancario").then(dataUnit=>{
                setDuMovBancario(dataUnit);
            });
        }
    }, []);

    return (
        <SnkApplication ref={application} >
            <SnkSimpleCrud dataUnit={duMovBancario} pageSize="3"/>
        </SnkApplication>
    );
};

export default Demo;
```

In memory

No modo SIMPLE_CRUD_MODE.IN_MEMORY não há paginação então esse atributo não tem efeito.

### Estado dos dados

> Propriedade utilizada: **dataState**

Representa o estado do **DataUnit**.

```jsx
import { useRef, useEffect, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';
import { DataType, UserInterface } from '@sankhyalabs/core';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const metadata = {
  name: 'ProdutosInMemory',
  label: 'Produtos em Memória',
  fields: [
    { name: 'CODPROD', label: 'Código', dataType: DataType.INTEGER, userInterface: UserInterface.INTEGER },
    { name: 'DESCRPROD', label: 'Descrição', dataType: DataType.TEXT, userInterface: UserInterface.SHORTTEXT },
  ],
};

const initialRecords = [
  { CODPROD: 1, DESCRPROD: 'Produto A' },
  { CODPROD: 2, DESCRPROD: 'Produto B' },
];

/**
 * Para simular tente inserir, deletar ou fazer copias de registro, sempre clicando no botão para atualizar o status e exibir os dados atualizados.
 */
const Demo = () => {
    const crudRef = useRef(null);
    const [copyMode, setCopyMode] = useState(null);
    const [insertionMode, setInsertionMode] = useState(null);
    const [isDirty, setIsDirty] = useState(null);
    const [hasDirtyRecords, setHasDirtyRecords] = useState(null);
    const [hasNext, setHasNext] = useState(null);
    const [hasPrevious, setHasPrevious] = useState(null);

    const updateDataStateList = () => {
        const dataState = crudRef.current.dataState;
        setCopyMode(dataState.copyMode);
        setInsertionMode(dataState.insertionMode);
        setIsDirty(dataState.isDirty);
        setHasDirtyRecords(dataState.hasDirtyRecords);
        setHasNext(dataState.hasNext);
        setHasPrevious(dataState.hasPrevious);
    };

    useEffect(() => {
        if (crudRef.current) {
        crudRef.current.setMetadata(metadata);
        crudRef.current.setRecords(initialRecords);
        }
    }, []);

    return (
        <SnkApplication>
             <div className="ez-flex ez-flex--column ez-margin--medium">
                <label className="ez-label">{"copyMode: " + copyMode}</label>
                <label className="ez-label">{"insertionMode: " + insertionMode}</label>
                <label className="ez-label">{"isDirty: " + isDirty}</label>
                <label className="ez-label">{"hasDirtyRecords: " + hasDirtyRecords}</label>
                <label className="ez-label">{"hasNext: " + hasNext}</label>
                <label className="ez-label">{"hasPrevious: " + hasPrevious}</label>
            </div>
            <EzButton onClick={updateDataStateList} label="Clique para atualizar o status exibido na lista" />
            <SnkSimpleCrud ref={crudRef} mode={1} autoLoad={true}/>
        </SnkApplication>
    );
};

export default Demo;
```

### Parâmetro ENTER como TAB

> Propriedade utilizada: **useEnterLikeTab**

O **useEnterLikeTab** possibilita assumir que a tecla `ENTER` tenha o comportamento da tecla `TAB`.

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleCrud} from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => (
    <SnkApplication configName="MovimentoBancario">
          <SnkSimpleCrud useEnterLikeTab={true}/>
    </SnkApplication>
);

export default Demo;
```

### Configurador (grade e formulário)

Mesmo em um CRUD simples, pode ser necessário fornecer capacidade de configuração de grade e formulário ao usuário. Assim o SnkSimpleCrud pode lidar com essa funcionalidade, através do botão de configuração.

Como habilitar:

O Botão de configuração só estará disponível caso o atributo `configName` seja informado.

```jsx
import React, { useEffect, useState } from 'react';
import { SnkApplication, SnkCustomSlotElements, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataType, DataUnit, UserInterface  } from '@sankhyalabs/core';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {

    const [paymentDataUnit, setPaymentDataUnit] = useState(null);

    useEffect(() => {
        const dataUnit = new DataUnit();
        dataUnit.metadata = {
            name: "exemplo.snkSimpleCrud",
            label: "Exemplo SnkSimpleCrud",
            fields: [
                {name: "VLRBAIXA", label: "Valor", dataType: DataType.NUMBER, userInterface: UserInterface.DECIMALNUMBER},
                {name: "CODTIPTIT", label: "Forma de Pagamento", dataType: DataType.OBJECT, userInterface: UserInterface.SEARCH},
                {name: "DHBAIXA", label: "Data Baixa", dataType: DataType.DATE, userInterface: UserInterface.DATE}
            ]
        };

        const currentDate = new Date();
        dataUnit.records = [
            {__record__id__: "01321321501", "VLRBAIXA": 10.33, "CODTIPTIT": {'value': 1, 'label': 'À vista'}, "DHBAIXA": currentDate},
            {__record__id__: "01321321502", "VLRBAIXA": 10.33, "CODTIPTIT": {'value': 2, 'label': '30 dias'}, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 30)},
            {__record__id__: "01321321503", "VLRBAIXA": 10.34, "CODTIPTIT": {'value': 3, 'label': '60 dias'}, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 60)},
        ];
        setPaymentDataUnit(dataUnit);
    }, []);

    return (
        <SnkApplication>
            <SnkSimpleCrud configName="payment" dataUnit={paymentDataUnit}>
                <SnkCustomSlotElements slotName="SnkConfigContainerSlot">
                    <EzButton label="Exemplo de slot"/>
                </SnkCustomSlotElements>
            </SnkSimpleCrud>
        </SnkApplication>
    );
};

export default Demo;
```

Em alguns casos pode ser necessário adicionar conteúdo "customizado" nas configurações. A exemplo do SnkCrud, é possível fazer isso através de um slot (o exemplo de código acima, mostra como fazer isso):

#### Botões de controle

> Propriedade utilizada: **showConfiguratorButtons**

Como o conteúdo "customizado" pode participar das configurações, também é possível cotrolar o fluxo de salvamento/cancelamento usando os botões no rodapé.
Os botões "Cancelar" e "Salvar" do rodapé, emitem respectivamente os eventos `configuratorCancel` e `configuratorSave`.

```jsx
import React, { useEffect, useState } from 'react';
import { SnkApplication, SnkCustomSlotElements, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataType, DataUnit, UserInterface  } from '@sankhyalabs/core';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { useRef } from 'react';
import { ApplicationUtils } from '@sankhyalabs/ezui/dist/collection/utils';

const Demo = () => {

    const simpleCrud = useRef();
    const [paymentDataUnit, setPaymentDataUnit] = useState(null);

    useEffect(() => {
        const dataUnit = new DataUnit();
        dataUnit.metadata = {
            name: "exemplo.snkSimpleCrud",
            label: "Exemplo SnkSimpleCrud",
            fields: [
                {name: "VLRBAIXA", label: "Valor", dataType: DataType.NUMBER, userInterface: UserInterface.DECIMALNUMBER},
                {name: "CODTIPTIT", label: "Forma de Pagamento", dataType: DataType.OBJECT, userInterface: UserInterface.SEARCH},
                {name: "DHBAIXA", label: "Data Baixa", dataType: DataType.DATE, userInterface: UserInterface.DATE}
            ]
        };

        const currentDate = new Date();
        dataUnit.records = [
            {__record__id__: "01321321501", "VLRBAIXA": 10.33, "CODTIPTIT": {'value': 1, 'label': 'À vista'}, "DHBAIXA": currentDate},
            {__record__id__: "01321321502", "VLRBAIXA": 10.33, "CODTIPTIT": {'value': 2, 'label': '30 dias'}, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 30)},
            {__record__id__: "01321321503", "VLRBAIXA": 10.34, "CODTIPTIT": {'value': 3, 'label': '60 dias'}, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 60)},
        ];
        setPaymentDataUnit(dataUnit);
    }, []);

    function savePreferencesHandle() {
        ApplicationUtils.message("Salvar preferências", "A ação de salvar preferências foi acionada")
            .then(()=>{closeConfigurator()});
    }

    function cancelPreferencesHandle() {
        closeConfigurator();
    }

    function closeConfigurator(){
        simpleCrud.current.closeConfigurator();
    }

    return (
        <SnkApplication>
            <SnkSimpleCrud
                ref={simpleCrud}
                configName="payment"
                dataUnit={paymentDataUnit}
                showConfiguratorButtons="true"
                onConfiguratorSave={() => savePreferencesHandle()}
                onConfiguratorCancel={() => cancelPreferencesHandle()}
            >
                <SnkCustomSlotElements slotName="SnkConfigContainerSlot">
                    <EzButton label="Exemplo de slot"/>
                </SnkCustomSlotElements>
            </SnkSimpleCrud>
        </SnkApplication>
    );
};

export default Demo;
```

#### Formulário com campos "somente leitura"

> Propriedade utilizada: **ignoreReadOnlyFormFields**

Durante a utilização do CRUD, alguns campos podem ser apenas de leitura. Em determinados momentos, não desejamos que esses campos sejam exibidos no modo de inserção. Para esses casos, podemos utilizar esta flag, que oculta os campos somente leitura nesse contexto.

Por padrão, ela é definida como false, ou seja, os campos somente leitura serão exibidos no formulário mesmo durante a inserção.

Ao definir seu valor como `true`, os campos somente leitura serão ocultados no modo de inserção.

Alterando o valor dela para "true", os campos que são apenas de leitura serão ocultados.

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataUnit } from '@sankhyalabs/core';

const Demo = () => {
    const paymentMethodsRef = useRef(null);
    const [paymentMethodsDataUnit, setPaymentMethodsDataUnit] = useState(null);

    useEffect(() => {
        setPaymentMethodsDataUnit(new DataUnit("paymentMethods"));
    }, []);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleCrud
                ref={paymentMethodsRef}
                dataUnit={paymentMethodsDataUnit}
                ignoreReadOnlyFormFields={true}
            />
        </SnkApplication>
    );
}

export default Demo;
```

### Carregamento automático de registros

> Propriedade utilizada: **autoLoad**

O **autoLoad** controla se os dados serão carregados na inicialização do componente, tendo como comportamento padrão, carregar os dados na inicialização.

Importante

A propriedade **apenas** é respeitada no modo `IN_MEMORY` do **SnkSimpleCrud**.

```jsx
import { useRef, useEffect } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';
import { DataType, UserInterface } from '@sankhyalabs/core';

const metadata = {
  name: 'ProdutosInMemory',
  label: 'Produtos em Memória',
  fields: [
    { name: 'CODPROD', label: 'Código', dataType: DataType.INTEGER, userInterface: UserInterface.INTEGER },
    { name: 'DESCRPROD', label: 'Descrição', dataType: DataType.TEXT, userInterface: UserInterface.SHORTTEXT },
  ],
};

const initialRecords = [
  { CODPROD: 1, DESCRPROD: 'Produto A' },
  { CODPROD: 2, DESCRPROD: 'Produto B' },
];

const Demo = () => {
  const crudRef = useRef(null);

  useEffect(() => {
    if (crudRef.current) {
      crudRef.current.setMetadata(metadata);
      crudRef.current.setRecords(initialRecords);
    }
  }, []);

  return (
    <SnkApplication>
        <SnkSimpleCrud ref={crudRef} mode={1} autoLoad={true}/>
    </SnkApplication>
  );
};

export default Demo;
```

### Foco automático

> Propriedade utilizada: **autoFocus**

Por padrão, a grade possui foco automático, sendo importante para casos onde possui implementações de atalhos de teclado. Porém, existe alguns casos onde o desenvolvedor pode desejar que a mesma não ocorra, para isso, existe a propriedade booleana `autoFocus` onde pode ser definido seu comportamento.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {

    const [duMovBancario, setDuMovBancario] = useState(null);
    const application = useRef(null);

    useEffect(() => {
        if(application.current){
            application.current.createDataunit("MovimentoBancario").then(dataUnit=>{
                setDuMovBancario(dataUnit);
            });
        }
    }, []);

    return (
        <SnkApplication ref={application} >
            <SnkSimpleCrud dataUnit={duMovBancario} autoFocus={true}/>
        </SnkApplication>
    );
};

export default Demo;
```

### Habilitar inserção na grade

> Propriedade utilizada: **enableGridInsert**

Por padrão, a inserção na grade está desabilitada. Quando ativada, ela permite que o usuário adicione novos registros diretamente na grade, respeitando o modo de visualização atual. A inserção segue o contexto da visualização do usuário:

  * Se o usuário estiver no **modo formulário** , a inserção será realizada via formulário.
  * Se o usuário estiver no **modo grade** , a inserção será feita diretamente na grade.

Conforme mostrado abaixo, ao clicar em "Cadastrar", o modo grade é mantido, permitindo que novos itens sejam inseridos diretamente na grade.

```jsx
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { DataType, UserInterface } from '@sankhyalabs/core';
import { SIMPLE_CRUD_MODE } from '@sankhyalabs/sankhyablocks/dist/collection/lib/utils/constants';
import { useEffect, useRef } from "react";

const Demo = () => {
    const simpleCrud = useRef();
    useEffect(()=>{
        if(simpleCrud.current){
            const currentDate = new Date();
            simpleCrud.current.setRecords([
                { __record__id__: "01321321501", "VLRBAIXA": 10.33, "CODTIPTIT": { 'value': 1, 'label': 'À vista' }, "DHBAIXA": currentDate },
                { __record__id__: "01321321502", "VLRBAIXA": 10.33, "CODTIPTIT": { 'value': 2, 'label': '30 dias' }, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 30) },
                { __record__id__: "01321321503", "VLRBAIXA": 10.34, "CODTIPTIT": { 'value': 3, 'label': '60 dias' }, "DHBAIXA": new Date(currentDate.getTime()).setDate(currentDate.getDate() + 60) },
            ]);
        }
    }, [simpleCrud]);
    return (
        <SnkApplication>
            <SnkSimpleCrud ref={simpleCrud} mode={SIMPLE_CRUD_MODE.IN_MEMORY} enableGridInsert={true}>
                <snk-field-metadata name="VLRBAIXA" label="Valor" dataType={DataType.NUMBER} userInterface={UserInterface.DECIMALNUMBER} readOnly="false" />
                <snk-field-metadata name="CODTIPTIT" label="Forma de Pagamento" dataType={DataType.OBJECT} userInterface={UserInterface.SEARCH} readOnly="false" />
                <snk-field-metadata name="DHBAIXA" label="Data Baixa" dataType={DataType.DATE} userInterface={UserInterface.DATE} readOnly="false" />
            </SnkSimpleCrud>
        </SnkApplication>
    );
};

export default Demo;
```

### Inserção contínua

> Propriedade utilizada: **enableContinuousInsert**

Quando a propriedade de **Inserção Contínua** (`enableContinuousInsert`) está habilitada, uma nova opção é adicionada ao menu 'Mais Opções' na barra de tarefas da grade, no topo da lista: **Ativar Inserção Contínua**.

Ao ativar, o item de menu muda para **Desativar Inserção Contínua**. Sempre que uma nova inserção for finalizada, seja ao salvar ou ao trocar de linha, um novo registro é automaticamente criado e posicionado na primeira célula editável, caso o salvamento seja bem-sucedido.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const EnableContinuousInsert = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && (
        <SnkSimpleCrud dataUnit={dataUnit} enableGridInsert={true} enableContinuousInsert={true} />
      )}
    </SnkApplication>
  );
};

export default EnableContinuousInsert;
```

Quando a **Inserção Contínua** está ativada, o rótulo do menu muda, permitindo desativá-la.

### Feedback de erros durante a inserção

Quando uma coluna contém um valor inválido, o sistema oferece feedback visual e textual do erro. Um **Toast** é exibido com a mensagem de erro, e a borda da célula inválida é destacada em vermelho. Além disso, o foco é automaticamente direcionado para a célula com erro.

## Principais métodos

### Gerenciamento de Dados em Memória

> Métodos utilizados: **setMetadata()** , **setRecords()** , **getRecords()**

Esses métodos são essenciais para operar o `SnkSimpleCrud` no modo `IN_MEMORY`.

  * `setMetadata`: Define a estrutura dos dados (campos, tipos, etc.).
  * `setRecords`: Carrega um conjunto inicial de registros na grade.
  * `getRecords`: Retorna todos os registros atualmente no `DataUnit`, incluindo novos, alterados e excluídos.

```jsx
import { useRef, useEffect } from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';
import { DataType, UserInterface } from '@sankhyalabs/core';

const metadata = {
  name: 'ProdutosInMemory',
  label: 'Produtos em Memória',
  fields: [
    { name: 'CODPROD', label: 'Código', dataType: DataType.INTEGER, userInterface: UserInterface.INTEGER },
    { name: 'DESCRPROD', label: 'Descrição', dataType: DataType.TEXT, userInterface: UserInterface.SHORTTEXT },
  ],
};

const initialRecords = [
  { CODPROD: 1, DESCRPROD: 'Produto A' },
  { CODPROD: 2, DESCRPROD: 'Produto B' },
];

const ManageInMemoryData = () => {
  const crudRef = useRef(null);

  useEffect(() => {
    if (crudRef.current) {
      crudRef.current.setMetadata(metadata);
      crudRef.current.setRecords(initialRecords);
    }
  }, []);

  const showRecords = async () => {
    const records = await crudRef.current.getRecords();
    console.log(records);
    alert('Veja os registros no console');
  };

  return (
    <SnkApplication>
      <>
        <EzButton onClick={showRecords} label='Ver Registros (getRecords)'></EzButton>
        <SnkSimpleCrud ref={crudRef} mode={1}/>
      </>
    </SnkApplication>
  );
};

export default ManageInMemoryData;
```

### Gerenciamento do Configurador

> Métodos utilizados: **openConfigurator()** , **closeConfigurator()**

Permitem controlar a exibição do painel de configuração da grade e do formulário de forma programática.

```jsx
import { useRef, useEffect, useState } from 'react';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const ManageConfigurator = () => {
  const crudRef = useRef(null);
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  const openConfig = () => {
    crudRef.current.openConfigurator();

    setTimeout(() => {
        //Simula o fechamento do configurador após 5 segundos
        crudRef.current.closeConfigurator();
    }, 5000);
  };

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && (
        <>
          <EzButton onClick={openConfig} label='Abrir Configurador'></EzButton>
          <SnkSimpleCrud ref={crudRef} dataUnit={dataUnit}/>
        </>
      )}
    </SnkApplication>
  );
};

export default ManageConfigurator;
```

### Navegação entre modos de visualização

> Método utilizado: **goToView()**

Com o método **goToView** , é possível alternar entre os modos de visualização disponíveis no **SnkSimpleCrud** , sendo eles o formulário, a grade e o configurador.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const simpleCrudRef = useRef(null);
    const appRef = useRef(null);
    const [duMovBancaria, setDuMovBancaria] = useState(null);

    useEffect(() => {
        if (appRef.current) {
        appRef.current.createDataunit('MovimentoBancario').then(setDuMovBancaria);
        }
    }, []);
    const viewGrid = () => {
        simpleCrudRef.current.goToView(0);
    }

    const viewForm = () => {
        simpleCrudRef.current.goToView(1);
    }

    const viewConfigurator = () => {
        simpleCrudRef.current.goToView(2);
    }

    return (
        <SnkApplication ref={appRef}>
            <EzButton label="Exibir Form" onClick={viewForm} className="ez-margin-top--medium" />
            <EzButton label="Exibir Grid" onClick={viewGrid} className="ez-margin-top--medium" />
            <EzButton label="Exibir Configurador" onClick={viewConfigurator} className="ez-margin-top--medium" />
            {duMovBancaria &&
                <SnkSimpleCrud ref={simpleCrudRef} dataUnit={duMovBancaria} />
            }
        </SnkApplication>
    );
};

export default Demo;
```

### Renderização de componentes customizados

> Metodo utilizado: **addGridCustomRender()**

Com o método **addGridCustomRender** é possível alterar o elemento que é mostrado na coluna no **SnkSimpleCrud** , podendo criar um elemento customizado dependendo ou não dos valores anteriores.

Importante

Ao retornar o elemento como string ou utilizando o método `renderToString` provido pelo `react-dom/server`, não será aplicado **nenhum** código JavaScript, portanto, caso necessário (para a criação de um botão por exemplo) é necessário que o elemento seja criado a partir do `document`, utilizando o método `createElement`.

#### Parâmetros

São passados alguns parâmetros para o método `getRenderElement`, sendo eles:

  * **value** \- Retorna o valor da célula.
  * **currentRender** \- Retorna o elemento padrão.
  * **name** \- Retorna o nome do campo.
  * **getValue** \- Método que retorna o valor da célula.
  * **detailContext** \- Retorna o contexto do master/detail.
  * **renderMetadata** \- Retorna o metadata da célula.

```jsx
import { useRef, useState } from 'react';
import { EzButton } from "@sankhyalabs/ezui/react/components";
import { SnkApplication, SnkDataUnit, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";
import { renderToString } from "react-dom/server";

/**
 * Visualize as alterações de customização no campo `HISTORICO` na grade.
 */
const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const snkDataUnit = useRef(null);
    const application = useRef(null);
    const snkSimpleCrud = useRef(null);

    const setCustomElement = () => {
        const customRender = {
            getRenderElement: () => {
                const element = document.createElement('div');
                element.textContent = 'Esse é um elemento totalmente customizado!';
                return element;
            }
        };
        snkSimpleCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const setCustomElementString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const elemment = `<div class='ez-text--tertiary'>Valor do campo: ${params.value}</div>`;
                return elemment;
            }
        };
        snkSimpleCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const setCustomElementReactString = () => {
        const customRender = {
            getRenderElement: (params) => {
                const Element = <div className="ez-text--tertiary">Valor do campo: {params.value}</div>
                const stringElement = renderToString(Element);
                return stringElement;
            }
        };
        snkSimpleCrud.current?.addGridCustomRender("HISTORICO", customRender);
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
        snkSimpleCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const cleanElement = () => {
        const customRender = {
            getRenderElement: () => {}
        };
        snkSimpleCrud.current?.addGridCustomRender("HISTORICO", customRender);
    }

    const handleDataUnitReady =  (event) => {
        const du = event.detail;
        setDataUnitInstance(du);

        du.loadData();
    };

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
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkSimpleCrud
                        ref={snkSimpleCrud}
                        dataUnit={snkDataUnit.current.dataUnit}
                        multipleSelection={true}
                    />
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Renderização de editores customizados

> Método utilizado: **addCustomEditor()**

Através deste método, é possível adicionar editores customizados (**ICustomEditor**) no lugar de campos do formulário e/ou grade. Quando nenhum editor customizado é adicionado à coluna, seu campo padrão é renderizado.

Existem quatro retornos possíveis para o métodoo **getEditorElement** do **ICustomEditor** , sendo eles:

  * **Nulo/indefinido** : renderiza o elemento padrão para aquele campo;
  * **O elemento padrão** : renderiza o elemento padrão para aquele campo;
  * **Uma string** : faz o parse da string e renderiza o elemento passado;
  * **Um elemento HTML** : renderiza o elemento.

Nos parâmetros da função getEditorElement, existe o atributo **source** , através do qual é possível definir o editor para grade ou formulário.

Importante

O método **renderToString** não aceita **nenhum** código javascript. Para um botão, por exemplo, um onClick não irá funcionar. O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTML.

```jsx
import { DataUnit } from '@sankhyalabs/core';
import { EzButton } from '@sankhyalabs/ezui/react/components';
import { SnkApplication, SnkSimpleCrud } from '@sankhyalabs/sankhyablocks/react/components';
import { useCallback, useEffect, useRef, useState } from 'react';
import { renderToString } from 'react-dom/server';

const dataLoader = () => {
    return new Promise((resolve) => {
        resolve({records: [
            {
                "__record__id__": "1",
                "NOME": "Brasil",
                "POPULACAO": 214300000,
                "IDIOMA": "Português",
                "CONTINENTE": "América do Sul",
                "PIB": 1920000000
              },
              {
                "__record__id__": "2",
                "NOME": "Estados Unidos",
                "POPULACAO": 332915073,
                "IDIOMA": "Inglês",
                "CONTINENTE": "América do Norte",
                "PIB": 25440000000
              }
        ]});
    });
}

const metadataLoader = () => {
    return new Promise((resolve) => {
        resolve({
            "name": "paises",
            "label": "paises",
            "fields": [
                {
                    "name": "NOME",
                    "label": "Nome do País",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": true
                },
                {
                    "name": "POPULACAO",
                    "label": "Num. Habitantes",
                    "dataType": "NUMBER",
                    "userInterface": "INTEGERNUMBER",
                    "readOnly": false,
                    "required": false
                },
                {
                    "name": "IDIOMAOFC",
                    "label": "Idioma oficial",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": false
                },
                {
                    "name": "CONTINENTE",
                    "label": "Continente",
                    "dataType": "TEXT",
                    "userInterface": "TEXT",
                    "readOnly": false,
                    "required": false
                },
                {
                    "name": "PIB",
                    "label": "PIB",
                    "dataType": "NUMBER",
                    "userInterface": "INTEGERNUMBER",
                    "readOnly": false,
                    "required": false
                }
            ]
        });
    });
}

const Demo = () => {
    const snkSimpleCrudRef = useRef(null);
    const [dataUnit, setDataUnit] = useState();

    const initDataUnit = () => {
        dataUnit.dataLoader = dataLoader;
        dataUnit.metadataLoader = metadataLoader;
    }

    const loadDataUnit = () => {
        dataUnit.loadMetadata().then((metadata) => {
            const fields = metadata.fields.map(field => ({...field, readOnly: false}));
            dataUnit.metadata = {...metadata, fields};
            dataUnit.loadData();
            dataUnit.selectFirst();
        });
    }

    const addCustomEditor = useCallback(async () => {
        const customEditorPopulacao = {
            getEditorElement: () => {
                return null;
            }
        }

        const customEditorIdioma = {
            getEditorElement: (params) => {
                if(params.source !== "FORM") {
                    return;
                }

                return params.currentEditor;
            }
        }

        const customEditorContinente = {
            getEditorElement: (params) => {
                if(params.source !== "FORM") {
                    return;
                }

                return renderToString(<EzButton label='Teste'/>);
            }
        }

        const customEditorPib = {
            getEditorElement: ({source, setValue, value}) => {
                if(source === "FORM") {
                    const textInput = document.createElement('ez-number-input');
                    textInput.label = 'Editor customizado';
                    textInput.value = value;
                    textInput.onkeyup = (event) => {
                        setValue(event.target.value);
                    };
                    return textInput;
                }
                const textInput = document.createElement('input');
                textInput.value = value;
                textInput.type = 'number';
                textInput.onkeyup = (event) => {
                    setValue(event.target.value);
                };
                return textInput;
            }
        }

        await snkSimpleCrudRef.current.addCustomEditor('POPULACAO', customEditorPopulacao);
        await snkSimpleCrudRef.current.addCustomEditor('IDIOMAOFC', customEditorIdioma);
        await snkSimpleCrudRef.current.addCustomEditor('CONTINENTE', customEditorContinente);
        await snkSimpleCrudRef.current.addCustomEditor('PIB', customEditorPib);
    }, [snkSimpleCrudRef]);

    useEffect(() => {
        setDataUnit(new DataUnit("dataUnitTeste"));
    }, []);

    useEffect(() => {
        if(!dataUnit) {
            return;
        }

        initDataUnit();
        loadDataUnit();

    }, [dataUnit]);

    useEffect(() => {
        if(!snkSimpleCrudRef?.current) {
            return;
        }

        addCustomEditor();
    }, [snkSimpleCrudRef, dataUnit]);

    return (
        <SnkApplication configName="Countries">
            <SnkSimpleCrud className='ez-margin--large' ref={snkSimpleCrudRef} dataUnit={dataUnit} />
        </SnkApplication>
    )
};

export default Demo;
```

Importante

Ao utilizar um input no elemento customizado, é necessário que se utilize o listener `onkeyup`, com o objetivo de sempre capturar o novo valor a toda tecla pressionada. Desta forma, o ciclo de vida da grade não interfere na mudança de valor.

### Alteração dinâmica de props

> Método utilizado: **setFieldProp()**

No formulário do **SnkSimpleCrud** , é possível alterar dinamicamente propriedades de campos através do método **setFieldProp** do componente.

No exemplo abaixo, o `setFieldProp` é utilizado para alterar a quantidade de casas decimais do campo `VLRMOEDA`.

```jsx
import { useRef, useState, useEffect} from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
  const crudRef = useRef(null);

  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  const changeProperty = async () => {
    if (crudRef.current && dataUnit) {
      // Verifica se os campo existe nos metadados antes de tentar alterá-los
      const hasVlrMoeda = dataUnit.metadata.fields.some(f => f.name === 'VLRMOEDA');

      if (hasVlrMoeda) {
        // Altera a quantidade de casas decimais do campo VLRMOEDA
        await crudRef.current.setFieldProp('VLRMOEDA', 'precision', 5);
      } else {
        console.warn("Campo 'VLRMOEDA' não encontrado nos metadados.");
      }
    }
  };

  return (
    <SnkApplication ref={appRef}>
        {dataUnit && (
            <>
            <EzButton label="Alterar casas decimais campo Moeda" onClick={changeProperty}/>
            <SnkSimpleCrud
                ref={crudRef}
                dataUnit={dataUnit}
            />
            </>
        )}
    </SnkApplication>
  );
};

export default Demo;
```

### Formatador personalizado

> Métodos utilizados: **addCustomValueFormatter()** , **removeCustomValueFormatter**

Na grade do **SnkSimpleCrud** , é possível adicionar e remover formatadores personalizados (`ICustomFormatter`) para colunas específicas. Isso permite customizar a exibição de dados sem alterar o valor original.

A implementação do formatador deve seguir a interface `ICustomFormatter`:

```typescript
export interface ICustomFormatter {
  /**
   * Formata o valor da célula.
   * @param value - O valor da célula.
   * @param record - O registro da linha.
   * @returns O valor formatado.
   */
  format(value: any, record: Record): any;
  /**
   * Atualiza as linhas selecionadas.
   */
  refreshSelectedRows?(): void;
}
```

No exemplo abaixo, um formatador de moeda é aplicado à coluna `VLRUNIT`.

  * **`addCustomValueFormatter`** : Adiciona um formatador que converte o valor numérico para o formato de moeda brasileira (R$).
  * **`removeCustomValueFormatter`** : Remove o formatador, fazendo com que a coluna volte a exibir o valor original.

```jsx
import { useRef, useState, useEffect} from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';
import { EzButton } from '@sankhyalabs/ezui/react/components';

// Implementação da interface ICustomFormatter
class CurrencyFormatter {
  format(value) {
    if (value === null || value === undefined) {
      return '';
    }
    const number = Number(value);
    return number.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
  }
}

/**
 * Visualize a alteração no campo moeda da grade
 */
const Demo = () => {
    const crudRef = useRef(null);
    const appRef = useRef(null);
    const formatter = new CurrencyFormatter();
    const [dataUnit, setDataUnit] = useState(null);

    useEffect(() => {
        if (appRef.current) {
        appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
        }
    }, []);

    const addFormatter = () => {
        if (crudRef.current) {
        crudRef.current.addCustomValueFormatter('VLRMOEDA', formatter);
        }
    };

    const removeFormatter = () => {
        if (crudRef.current) {
        crudRef.current.removeCustomValueFormatter('VLRMOEDA');
        }
    };

    return (
        <SnkApplication ref={appRef}>
            {dataUnit && (
                <>
                <EzButton onClick={addFormatter} label="Adicionar Formatador de Moeda"></EzButton>
                <EzButton onClick={removeFormatter} label="Remover Formatador"></EzButton>
                <SnkSimpleCrud
                    ref={crudRef}
                    dataUnit={dataUnit}
                />
                </>
            )}
        </SnkApplication>
    );
};

export default Demo;
```

## Exemplos de eventos

### DataUnit Pronto

> Evento utilizado: **onDataUnitReady**

Este evento é emitido assim que a instância do `DataUnit` interna do componente está inicializada e pronta para uso. É útil para obter a referência do `DataUnit` e interagir com ele programaticamente.

```jsx
import React, { useEffect, useRef, useState } from 'react';
import { SnkSimpleCrud, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';

const DataUnitReady = () => {
  const [dataUnit, setDataUnit] = useState(null);
  const appRef = useRef(null);

  useEffect(() => {
    if (appRef.current) {
      appRef.current.createDataunit('MovimentoBancario').then(setDataUnit);
    }
  }, []);

  const handleDataUnitReady = (event) => {
    const dataUnit = event.detail;
    console.log('DataUnit está pronto!', dataUnit);
    alert(`DataUnit para a entidade "${dataUnit.name}" está pronto!`);
  };

  return (
    <SnkApplication ref={appRef}>
      {dataUnit && <SnkSimpleCrud dataUnit={dataUnit} onDataUnitReady={handleDataUnitReady} />}
    </SnkApplication>
  );
};

export default DataUnitReady;
```

### Ação de Clique

> Evento utilizado: **onActionClick**

Evento ao clicar em um item da barra de tarefas.

Por meio do **onActionClick** , é possível atribuir um processo que será executado quando o usuário clicar em algum botão da barra de tarefas (**SnkTaskbar**).

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const handleAction = (event) => {
        event.stopPropagation();
        alert(`Ação ${event.detail}`);
    }

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleCrud onActionClick={handleAction} />
        </SnkApplication>
    );
}

export default Demo;
```

### Elementos nas extremidades dos campos

> Propriedade utilizada: **onFormItemsReady**

Permite a adição de elementos nas extremidades do formulário, incluindo botões, ícones, badges ou qualquer outro elemento desejado.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

```jsx
import { useState } from "react";
import {
  SnkApplication,
  SnkDataUnit,
  SnkSimpleCrud,
} from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [duMovBancaria, setDuMovBancaria] = useState(null);

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDuMovBancaria(du);
        du.loadData();
    };

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

        items.get("NUCAIXA")?.addRightElement(btn);
    }

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                dataUnitName="principal"
                key="duPrincipal"
                onDataUnitReady={handleDataUnitReady}
            >
                {duMovBancaria &&
                    <SnkSimpleCrud
                    dataUnit={duMovBancaria}
                    onFormItemsReady={(evt) => addIconInForm(evt.detail.items)}
                    />
                }
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Row Metadata

Quando existir um Row Metadata Provider no (**SnkDataUnit**) associado ao **SnkSimpleCrud** , a grade e o formulário levarão em conta este provider para mostrar os dados em tela.

No exemplo abaixo, cada produto possui uma configuração diferente de casas decimais (rm_precision) para as colunas de `quantidade` e `vlr. unitário`. O produto 6 possui uma precisão de 3 para `quantidade` e 5 para `vlr. Unitário` e O produto 10 possui uma precisão de 7 para `quantidade` e 2 para `vlr. Unitário`.

#### Grade

#### Formulário

#### Row Metadata no DataState

O DataState disparado pelo evento **dataStateChange** contém algumas informações de row metadata. A propriedade **metadataByRow** é um map com rmp por ID de registro. E a propriedade **rowMetadata** é o rmp do registro selecionado.

Atenção

**Antes de invocar métodos que modificam o estado do`DataUnit` dentro deste evento, reavalie se é realmente necessário fazer isso aqui.** Na maioria dos casos, os **observers nativos do DataUnit** (como `beforeDataChanged`, `afterDataChanged`, etc.) são mais apropriados e seguros para essa finalidade.

Métodos como `setFieldValue`, `addRecord`, `removeRecords`, entre outros, disparam novamente o evento `dataStateChange`, o que pode causar **loops infinitos** se não houver uma condição de parada apropriada.

**Recomendações:**

  1. **Priorize o uso dos observers do DataUnit** ao invés de modificar dados dentro deste evento.
  2. Se for absolutamente necessário modificar dados aqui, sempre adicione validações condicionais rigorosas para evitar chamadas recursivas (ex: verifique se o valor realmente mudou antes de chamar `setFieldValue` novamente).

```jsx
import React, {useState, useRef} from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const application = useRef(null);
    const snkSimpleCrud = useRef(null);
    const [dataUnit, setDataUnit] = useState(null);
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

    const getDataUnit = async () => {
        const itemNotaDU = await application.createDataunit("ItemNota", "ItemNotaDU");
        setDataUnit(itemNotaDU);
    }

    useEffect(() => {
        getDataUnit();
    }, []);

    return (
        <SnkApplication ref={application} configName="MovimentoBancario">
            <div className="ez-flex ez-flex--column ez-margin--medium">
                <label className="ez-label">{"rowMetadata: " + rowMetadata}</label>
                <label className="ez-label">{"metadataByRow: " + metadataByRow}</label>
                <label className="ez-label">{"controleRmp: " + controleRmp}</label>
            </div>
            <SnkSimpleCrud
                ref={snkSimpleCrud}
                dataUnit={dataUnit}
                onDataStateChange={dataStateChange}
            />
        </SnkApplication>
    );
};

export default Demo;
```

Importante

O fluxo completo de Row Metadata se encontra detalhado no (**SnkDataUnit**).

## Tamanho mínimo da grade

Por padrão a grade do _Simple Crud_ possui a altura mínima de **300px** , porém existem alguns casos onde o desenvolvedor pode desejar que a mesma possua uma altura mínima de **0px** para que o componente acompanhe o tamanho do container que o envolve.

Para isso, basta adicionar a classe css `grid_height-0`.

```jsx
import { useEffect, useRef, useState } from 'react';
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const simpleCrudRef = useRef(null);
    const appRef = useRef(null);
    const [duMovBancaria, setDuMovBancaria] = useState(null);

    useEffect(() => {
        if (appRef.current) {
            appRef.current.createDataunit('MovimentoBancario').then(setDuMovBancaria);
        }
    }, []);

    return (
        <SnkApplication ref={appRef}>
            {duMovBancaria &&
                <SnkSimpleCrud ref={simpleCrudRef} dataUnit={duMovBancaria} className={"grid_height-0"}/>
            }
        </SnkApplication>
    );
};

export default Demo;
```

## Exportação da grade

O **SnkSimpleCrud** possui nativamente a exportação de grade.

Informação

As opções de exportar **"Somente a página atual"** e **"Enviar por email..."** não estão disponíveis.

```jsx
import { SnkApplication, SnkSimpleCrud } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
  return (
    <SnkApplication configName="CotacaoMoeda">
        <SnkSimpleCrud entityName={"CotacaoMoeda"} />
    </SnkApplication>
  );
};

export default Demo;
```

Importante

A busca por relatórios personalizados só funciona caso a propriedade **entityName** seja passada para o **SnkSimpleCrud**.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| actionsList | -- |  | Action[] | undefined |
| autoFocus | auto-focus |  | boolean | true |
| autoLoad | auto-load |  | boolean | undefined |
| configName | config-name |  | string | undefined |
| dataState | -- |  | DataState | undefined |
| dataUnit | -- |  | DataUnit | undefined |
| disableGridEdition | disable-grid-edition | Desabilita a edição na grade. | boolean | false |
| domainMessagesBuilder | domain-messages-builder |  | string | undefined |
| enableContinuousInsert | enable-continuous-insert |  | boolean | false |
| enableGridInsert | enable-grid-insert |  | boolean | false |
| enableLockManagerLoadingComp | enable-lock-manager-loading-comp |  | boolean | false |
| enableLockManagerTaskbarClick | enable-lock-manager-taskbar-click |  | boolean | false |
| entityName | entity-name |  | string | undefined |
| formConfig | -- |  | IFormConfig | undefined |
| formLegacyConfigName | form-legacy-config-name |  | string | undefined |
| gridConfig | -- |  | IGridConfig | undefined |
| gridLegacyConfigName | grid-legacy-config-name |  | string | undefined |
| ignoreReadOnlyFormFields | ignore-read-only-form-fields |  | boolean | false |
| layoutFormConfig | layout-form-config |  | boolean | true |
| messagesBuilder | -- |  | SnkMessageBuilder | undefined |
| mode | mode |  | SIMPLE_CRUD_MODE.IN_MEMORY \| SIMPLE_CRUD_MODE.SERVER | SIMPLE_CRUD_MODE.SERVER |
| multipleEditionEnabled | multiple-edition-enabled |  | boolean | true |
| multipleSelection | multiple-selection |  | boolean | undefined |
| outlineMode | outline-mode |  | boolean | false |
| pageSize | page-size |  | number | 150 |
| paginationCounterMode | pagination-counter-mode |  | "auto" \| "hidden" \| "show" | 'auto' |
| resourceID | resource-i-d |  | string | undefined |
| showConfiguratorButtons | show-configurator-buttons |  | boolean | false |
| taskbarManager | -- |  | TaskbarManager | undefined |
| useCancelConfirm | use-cancel-confirm |  | boolean | true |
| useEnterLikeTab | use-enter-like-tab |  | boolean | false |

### Events

| Event | Description | Type |
|---|---|---|
| actionClick |  | CustomEvent<string> |
| configuratorCancel |  | CustomEvent<any> |
| configuratorSave |  | CustomEvent<any> |
| dataStateChange |  | CustomEvent<DataState> |
| dataUnitReady |  | CustomEvent<DataUnit> |
| formItemsReady |  | CustomEvent<HTMLElement[]> |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `addCustomValueFormatter(columnName: string, customFormatter: ICustomFormatter) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `addGridCustomRender(fieldName: string, customRender: ICustomRender) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `closeConfigurator() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `getRecords() => Promise<Array<Record>>`

##### Returns

Type: `Promise<Record[]>`

Uma promessa que resolve com a lista de registros.

#### `goToView(view: VIEW_MODE) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `openConfigurator() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `setMetadata(metadata: UnitMetadata) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `setRecords(records: Array<Record>) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `updateConfig() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

  * snk-attach

#### Depends on

  * snk-taskbar
  * snk-data-unit
  * snk-simple-form-config
  * snk-configurator
  * snk-grid-config
  * snk-data-exporter
  * snk-actions-button
  * taskbar-split-button
  * taskbar-actions-button
