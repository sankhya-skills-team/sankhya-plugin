> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-form/ (snapshot 2026-09-28)

# Form

O componente **SnkForm** é uma ferramenta robusta projetada para a criação de formulários dentro do ecossistema de aplicações Sankhya. Ele se destaca por carregar automaticamente os campos de uma entidade, respeitando as configurações definidas no **Dicionário de Dados** e no **Configurador de Formulário** da plataforma Sankhya. Isso simplifica o desenvolvimento, garantindo consistência e aderência às regras de negócio.

## Quando utilizar o SnkForm

O **SnkForm** é a escolha ideal quando:

  * Você está desenvolvendo interfaces de formulário que interagem diretamente com entidades e dados do **Sankhya Om**.
  * A necessidade é de uma integração automática e transparente com o **Dicionário de Dados** e o **Configurador de Formulário** do Sankhya, aproveitando as definições e personalizações já existentes.
  * É preciso incorporar rapidamente funcionalidades de criar e atualizar dados para uma entidade específica e comportamentos padronizados pela plataforma Sankhya.
  * O objetivo é agilizar o desenvolvimento de telas de cadastro e manutenção, focando nas regras de negócio específicas da aplicação, enquanto o componente cuida da estrutura e interações básicas do formulário.
  * Se busca consistência visual e funcional com outras telas do sistema Sankhya.

## Quando não utilizar o SnkForm

Considere alternativas ao **SnkForm** se:

  * O formulário destina-se a uma aplicação web genérica, sem qualquer vínculo com o backend ou o ecossistema Sankhya.
  * Você precisa de um componente de formulário mais leve, genérico ou totalmente independente de qualquer plataforma específica. Nestes casos, o componente **EzForm** pode ser uma alternativa mais adequada.
  * É necessário um controle granular e absoluto sobre cada aspecto do comportamento e da apresentação do formulário, sem as convenções ou integrações automáticas do Sankhya.
  * Não há um **SnkDataUnit** para fornecer os metadados e dados da entidade, pois o **SnkForm** depende intrinsecamente dele para operar.
  * A aplicação não utiliza ou não tem acesso ao ambiente e às configurações do **Sankhya Om**.

## SnkForm x EzForm

A principal diferença entre SnkForm e EzForm reside na sua especialização e independência:

SnkForm: Este componente é intrinsecamente vinculado às entidades e regras de negócio específicas da plataforma Sankhya Om. Isso significa que ele já vem com funcionalidades e validações pré-configuradas para interagir de forma otimizada com a lógica e os dados do **[Sankhya Om](https://skw.sankhya.com.br)**.

EzForm: Em contraste, o **EzForm** é um componente totalmente independente. Ele não possui qualquer vínculo preexistente com entidades ou regras de negócio do Sankhya Om, oferecendo maior flexibilidade e autonomia para ser utilizado em contextos variados, sem dependências específicas da plataforma.

## Atenção ao uso com SnkDataUnit

Importante

Ao utilizar o **SnkForm** (assim como **SnkCrud** ou **SnkGrid**) como filho direto de um **SnkDataUnit** , é fundamental garantir que o **SnkDataUnit** esteja completamente inicializado e seus metadados carregados **antes** de renderizar o SnkForm. Caso contrário, o SnkForm pode não funcionar corretamente ou apresentar erros, pois depende do contexto e dos dados fornecidos pelo SnkDataUnit pai.

A abordagem recomendada é utilizar o evento `onDataUnitReady` do SnkDataUnit em conjunto com um estado (por exemplo, via `useState`) para controlar a renderização dos componentes filhos. Assim, o SnkForm só será renderizado após o DataUnit estar pronto.

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
    {dataUnit && <SnkForm />}
</SnkDataUnit>
```

Dessa forma, o `<SnkForm />` só será montado no DOM quando o DataUnit estiver pronto, evitando problemas de inicialização.

Para mais detalhes, consulte a seção correspondente na documentação do SnkDataUnit.

## Propriedades

### Configurações do formulário

> Propriedade utilizada: **configName**

É um identificador único para as configurações do formulário, utilizado para carregar e salvar as configurações.

Para informar ao formulário qual será o identificador utilizado nas configurações, basta passar uma _string_ com o identificador desejado, conforme o exemplo a seguir:

```jsx
import { useState } from "react";
import { SnkApplication, SnkDataUnit, SnkForm } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkForm
                        configName="MovimentoBancario">
                    </SnkForm>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Validador de registros

> Propriedade utilizada: **recordsValidator**

Define um validador responsável pela integridade dos registros.

Observação

No exemplo a seguir, está sendo validado o valor do campo **Vlr. Moeda** , que não pode ser zero (R$ 0,00).

```jsx
import { useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkForm } from "@sankhyalabs/sankhyablocks/react/components";
import { EzButton } from "@sankhyalabs/ezui/react/components";

/**
 * Exemplo de uso da propriedade recordsValidator do SnkForm.
 * O validador impede que o campo VLRMOEDA seja zero.
 */
const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const snkFormRef = useRef(null);

    // Validador de registros: impede valor zero ou indefinido para o campo VLRMOEDA
    const recordsValidator = {
        validateRecord: (record) => {
            const currencyValue = record["VLRMOEDA"];
            if (currencyValue !== undefined || Number(currencyValue) === 0) {
                return {
                    isValid: false,
                    errorTitle: "Valor inválido",
                    errorMessage: "O valor da moeda deve ser maior que zero."
                };
            }
            // Retorne undefined ou um objeto com isValid: true para registros válidos
            return { isValid: true };
        }
    };

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    // Função para validar o formulário ao clicar em "Salvar"
    const handleSalvar = async () => {
        if (snkFormRef.current) {
            const result = await snkFormRef.current.validate();
            if (result?.isValid) {
                alert("Formulário válido! Pronto para salvar.");
            } else {
                alert(result?.errorMessage || "Formulário inválido.");
            }
        }
    };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <>
                        <SnkForm
                            ref={snkFormRef}
                            configName="MovimentoBancario"
                            recordsValidator={recordsValidator}
                        />
                        <EzButton
                            label="Salvar"
                            className="ez-margin-top--medium"
                            onClick={handleSalvar}
                        />
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Principais métodos

### showConfig() e hideConfig()

Estes métodos realizam o controle para exibir ou ocultar o configurador do formulário.

Observação

No exemplo abaixo, ao clicar no botão **Configurações** , o método **showConfig()** será acionado, e o **Configurador do formulário** será exibido. Após 2 segundos, será chamado o método **hideConfig()** , e, então, a tela será ocultada automaticamente.

```jsx
import { useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkForm } from "@sankhyalabs/sankhyablocks/react/components";
import { ApplicationUtils } from "@sankhyalabs/ezui/dist/collection/utils";
import { EzButton } from '@sankhyalabs/ezui/react/components';

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const snkForm = useRef(null);
    const SnkApplicationRef = useRef(null);

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    const handleShowConfig = async () => {
        if (snkForm.current) {
            // Método de abertura da configuração do formulário.
            await snkForm.current.showConfig();

            // O timeout abaixo serve para demonstrar a chamada
            // do médodo hideConfig() apos o tempo de 2 segundos.
            setTimeout(async () => {
                 await snkForm.current.hideConfig()
                    .then(() => {
                        ApplicationUtils.message(
                            "Título da Mensagem",
                            "A configuração do formulário foi fechada!"
                        );
                    });
            }, 2000);
        }
    };

    return (
        <SnkApplication configName="MovimentoBancario" ref={SnkApplicationRef}>
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <>
                        <SnkForm
                            ref={snkForm}
                            configName="MovimentoBancario"
                            messagesBuilder={SnkApplicationRef.current.messagesBuilder}>
                        </SnkForm>
                        <EzButton onClick={handleShowConfig} label="Configurações"></EzButton>
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Alteração dinâmica de props

É possível alterar dinamicamente as propriedades dos campos através do método **setFieldProp** do componente. Este método recebe três argumentos: o nome do campo (`fieldName`), a propriedade a ser alterada (`propName`) e o novo valor para a propriedade (`propValue`).

No exemplo abaixo, ao clicar no botão "Alterar Propriedade do Campo":

  * O campo "VLRMOEDA" que inicialmente possui 2 casas decimais após a virgula por padrão. Agora terá 5 casas decimais.

Isso demonstra como interagir com o formulário em tempo de execução para ajustar a apresentação e o comportamento dos campos dinamicamente.

```jsx
import React, { useRef, useState } from 'react';
import { SnkDataUnit, SnkForm, SnkApplication } from '@sankhyalabs/sankhyablocks/react/components';
import { EzButton } from '@sankhyalabs/ezui/react/components';

const SetFieldPropExample = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const snkFormRef = useRef(null);

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    const alterarPropriedade = async () => {
    if (snkFormRef.current && dataUnitInstance) {
      // Verifica se os campo existe nos metadados antes de tentar alterá-los
      const hasVlrMoeda = dataUnitInstance.metadata.fields.some(f => f.name === 'VLRMOEDA');

      if (hasVlrMoeda) {
        // Altera a quantidade de casas decimais do campo VLRMOEDA
        await snkFormRef.current.setFieldProp('VLRMOEDA', 'precision', 5);
      } else {
        console.warn("Campo 'VLRMOEDA' não encontrado nos metadados.");
      }
    }
  };

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <>
                        <SnkForm
                            ref={snkFormRef}
                            configName="MovimentoBancario">
                        </SnkForm>
                        <EzButton label="Alterar Propriedade do Campo" onClick={alterarPropriedade} className="ez-margin-top--medium" />
                    </>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default SetFieldPropExample;
```

### Editores customizados

Através do método **addCustomEditor** , é possível adicionar editores customizados (**ICustomEditor**) no lugar dos campos do formulário. Quando nenhum editor customizado é adicionado ao campo, seu editor padrão é renderizado.

Existem quatro retornos possíveis para o método **getEditorElement** do **ICustomEditor** , sendo eles:

  * **Nulo/indefinido** : renderiza o editor padrão para aquele campo;
  * **O editor padrão** : renderiza o editor padrão para aquele campo;
  * **Uma string** : faz o parse da string e renderiza o elemento HTML resultante;
  * **Um elemento HTML** : renderiza o elemento diretamente.

Importante

O método **renderToString** não executa nenhum código JavaScript. Para um botão, por exemplo, um manipulador de evento onClick não funcionará. O ideal para estes casos é utilizar **document.createElement** e retornar diretamente o elemento HTML.

```jsx
import { useCallback, useEffect, useRef, useState } from "react";
import { SnkApplication, SnkDataUnit, SnkForm } from "@sankhyalabs/sankhyablocks/react/components";
import { renderToString } from "react-dom/server";
import { EzButton } from "@sankhyalabs/ezui/react/components";

const Demo = () => {
    const [dataUnitInstance, setDataUnitInstance] = useState(null);
    const snkFormRef = useRef(null);

    const handleDataUnitReady = (event) => {
        const du = event.detail;
        setDataUnitInstance(du);
        du.loadData();
    };

    const addCustomEditor = useCallback(async () => {
        if (!snkFormRef.current) return;

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
            getEditorElement: () => {
                return renderToString(<EzButton label='Teste'/>);
            }
        }

        const customEditorUsuario = {
            getEditorElement: () => {
                const launchButton = document.createElement('ez-button');
                launchButton.mode = 'icon';
                launchButton.iconName = 'warning-outline';
                launchButton.onclick = () => {console.log('CLICK DO BOTÃO')};

                return launchButton;
            }
        }

        await snkFormRef.current.addCustomEditor('VLRMOEDA', customEditorVlrMoeda);
        await snkFormRef.current.addCustomEditor('VLRLANC_DESTINO', customEditorVlrLancDestino);
        await snkFormRef.current.addCustomEditor('NUBCO', customEditorNuBancario);
        await snkFormRef.current.addCustomEditor('CODUSU', customEditorUsuario);
    }, [snkFormRef]);

    useEffect(() => {
        if (dataUnitInstance && snkFormRef.current) {
            addCustomEditor();
        }
    }, [dataUnitInstance, snkFormRef, addCustomEditor]);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit
                entityName="MovimentoBancario"
                onDataUnitReady={handleDataUnitReady}
            >
                {dataUnitInstance && (
                    <SnkForm
                        ref={snkFormRef}
                        configName="MovimentoBancario">
                    </SnkForm>
                )}
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

## Row Metadata

Quando existir um Row Metadata Provider no (**SnkDataUnit**) associado ao **SnkForm** , o formulário levará em conta este provedor para mostrar os dados na tela.

No exemplo abaixo, o produto 6 possui uma configuração específica de casas decimais (rm_precision) para os campos Quantidade e Vlr. Unitário. O campo Quantidade possui precisão 3 e o campo Vlr. Unitário possui precisão 5.

Importante

O fluxo completo de Row Metadata encontra-se detalhado no (**SnkDataUnit**).

## Eventos

## Elementos nas extremidades dos campos

> Propriedade utilizada: **onFormItemsReady**

Permite a adição de elementos nas extremidades do formulário, incluindo botões, ícones, badges ou qualquer outro elemento desejado.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

```jsx
import { useState } from "react";
import {
  SnkApplication,
  SnkDataUnit,
  SnkForm,
} from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
  const [dataUnitInstance, setDataUnitInstance] = useState(null);

  const handleDataUnitReady = (event) => {
    const du = event.detail;
    setDataUnitInstance(du);
    du.loadData();
  };

  function addIconsInForm(items) {

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
        onDataUnitReady={handleDataUnitReady}
      >
        {dataUnitInstance && (
          <SnkForm
            configName="MovimentoBancario"
            onFormItemsReady={(evt) => addIconsInForm(evt.detail.items)}
          ></SnkForm>
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
| configName | config-name | Nome usado para guardar/recuperar as configurações do formulário. | string | undefined |
| formLegacyConfigName | form-legacy-config-name | Chave da configuração legada do formulário. | string | undefined |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |
| recordsValidator | -- | Validador responsável por checar a integridade das informações do registro. | IRecordValidator | undefined |
| resourceID | resource-i-d | Identificador de recursos como configurações e acesso. | string | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| actionClick | ⚠️ [DEPRECATED] Esta propriedade foi descontinuada. Ela não tem mais efeito sobre o componente. | CustomEvent<string> |
| exit | ⚠️ [DEPRECATED] Esta propriedade foi descontinuada. Ela não tem mais efeito sobre o componente. | CustomEvent<void> |
| formItemsReady | Responsável por notificar quando ocorrer a renderização de itens do formulário. OBS: Emitido no subcomponente snk-form-view | CustomEvent<HTMLElement[]> |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor) => Promise<void>`

Registra um editor customizado para campos do formulário.

##### Returns

Type: `Promise<void>`

#### `hideConfig() => Promise<void>`

Fecha a janela de configurações do formulário.

##### Returns

Type: `Promise<void>`

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

Altera/adiciona uma propriedade nos metadados do campo.

##### Returns

Type: `Promise<void>`

#### `showConfig() => Promise<void>`

Exibe a janela de configurações do formulário.

##### Returns

Type: `Promise<void>`

#### `validate() => Promise<void>`

Valida o formulário.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

  * snk-form-config
