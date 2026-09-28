> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-application/ (snapshot 2026-09-28)

# SnkApplication

O componente `snk-application` é fundamental no ecossistema sankhya-blocks. Ele atua como um contêiner principal e provedor de contexto para diversos outros componentes e serviços dentro de uma aplicação construída com sankhya-blocks. Ele é o coração de uma aplicação construída com sankhya-blocks, fornecendo a infraestrutura e os serviços necessários para que os demais componentes funcionem de maneira coesa.

## Quando utilizar o snk-application

  * Você deve utilizar o `snk-application` como o componente raiz ou um dos componentes de mais alto nível em qualquer aplicação que utilize os sankhya-blocks. Ele é essencial para o funcionamento correto de muitos outros componentes que dependem do contexto e dos serviços que ele provê.
  * Sempre que precisar de um ponto central para gerenciar mensagens, configurações globais da aplicação, ou interações com serviços de backend de forma padronizada.

## Quando NÃO utilizar o snk-application (ou ter cautela)

  * Não faria sentido utilizar múltiplos `snk-application` aninhados ou em paralelo de forma descoordenada na mesma visualização, pois ele é projetado para ser um singleton de contexto para uma "aplicação" ou uma seção principal dela.
  * Se você estiver construindo um componente Web Component completamente isolado que não depende de nenhum serviço ou contexto global dos sankhya-blocks, tecnicamente você poderia não precisar dele. No entanto, a maioria dos componentes `snk-*` parece depender dele.

## Principais Funcionalidades e Responsabilidades

  * **Provedor de Contexto** : Ele registra a si mesmo no `ApplicationContext` (`ApplicationContext.setContextValue("__SNK__APPLICATION__", this)`), permitindo que outros componentes acessem sua instância e, por conseguinte, seus métodos e propriedades. Muitos componentes, como `SnkDataExporter`, `SnkFormConfig`, `SnkAttach`, e `SnkFilterFieldSearch`, obtêm a instância do `snk-application` através do `ApplicationContext.getContextValue("__SNK__APPLICATION__")`.
  * **Gerenciamento de Mensagens** : O `snk-application` é responsável por instanciar e disponibilizar o `SnkMessageBuilder`. Este utilitário é usado para carregar e fornecer mensagens de texto para a interface do usuário, permitindo a internacionalização e customização de textos. As mensagens podem ser customizadas criando um arquivo `/messages/appmessages.msg.js` na aplicação.
  * **Interação com Serviços** : Ele interage com o `DataFetcher` para realizar requisições de dados (conforme o método `getDataFetcher` e o registro de `requestListener` em `connectedCallback`).
  * **Ciclo de Vida e Inicialização** : Possui métodos de ciclo de vida como `connectedCallback`, `disconnectedCallback`, `componentWillLoad`, e `componentDidLoad`. O método `whenApplicationReady` permite que outras partes da aplicação aguardem a completa inicialização do `snk-application`.
  * **Gerenciamento de Configurações** : Está envolvido no carregamento de configurações, como as de layout de formulário (método `setLayoutFormConfig`) e configurações de componentes (`ConfigStorage.preload`).
  * **Funcionalidades UI** : Oferece funcionalidades como `showPopUp` e `showScrimApp` para interações com o usuário, além de gerenciar o estado de carregamento da aplicação com `enableLockManagerLoadingApp`.

## Métodos Públicos Detalhados

O `snk-application` expõe diversos métodos via `@Method()` para serem consumidos por outros componentes ou pela própria aplicação.

### `whenApplicationReady(): Promise<SnkApplication>`

Retorna uma promessa que será resolvida quando o `snk-application` estiver carregado e registrado no `ApplicationContext`. É útil para garantir que a aplicação esteja pronta antes de executar certas lógicas.

```jsx
import React, { useRef, useEffect } from 'react';

const WhenApplicationReadyExample = () => {
  const snkApplicationRef = useRef(null);

  useEffect(() => {
    const init = async () => {
      if (snkApplicationRef.current) {
        try {
          const app = await snkApplicationRef.current.whenApplicationReady();
          console.log('SnkApplication está pronto:', app);
          // Agora você pode chamar outros métodos em 'app' com segurança
        } catch (error) {
          console.error('Erro ao aguardar SnkApplication:', error);
        }
      }
    };
    init();
  }, []);

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <p>Verifique o console para ver quando a aplicação está pronta.</p>
      </div>
    </SnkApplication>
  );
};

export default WhenApplicationReadyExample;
```

### `showPopUp(content: HTMLElement, size?: "auto" | "full", useHeader?: boolean, onCloseCallback?: Function): Promise<void>`

Exibe um conteúdo HTML dentro de um componente de popup.

  * `content`: O elemento HTML a ser exibido no popup.
  * `size`: (Opcional) Define o tamanho do popup. Padrão: `"full"`.
  * `useHeader`: (Opcional) Define se o cabeçalho do popup deve ser exibido. Padrão: `true`.
  * `onCloseCallback`: (Opcional) Função a ser chamada quando o popup for fechado.

```jsx
import React, { useRef } from 'react';
import { EzButton } from "@sankhyalabs/ezui/react/components";

const ContasReceber = () => {
  const snkApplicationRef = useRef(null);

  const handleShowPopUp = async () => {
    if (snkApplicationRef.current) {
      const content = document.createElement('div');
      content.innerHTML = `
        <h2>Olá do PopUp!</h2>
        <p>Este é um conteúdo personalizado exibido em um popup.</p>
        <ez-button id="closePopupBtn" label="Fechar"></ez-button>
      `;
      const closePopupBtn = content.querySelector('#closePopupBtn');

      const popupInstance = await snkApplicationRef.current.showPopUp(content, "auto", true, () => {
        console.log('Popup fechado!');
      });

      // Exemplo de como interagir com o conteúdo do popup, se necessário,
      // embora a interação direta com o próprio popupInstance seja limitada.
      // A principal forma de fechar é através do botão de fechar interno do popup ou clicando fora (se configurado).
      if (closePopupBtn) {
        closePopupBtn.onclick = () => {
          // Para fechar programaticamente, você pode precisar encontrar o componente ez-popup e chamar seu método close.
          // Este é um exemplo simplificado; o fechamento direto de fora pode ser complexo.
          // Por enquanto, o próprio botão de fechar do cabeçalho do popup ou onCloseCallback lida com o fechamento.
          console.log('Botão de fechar personalizado clicado dentro do conteúdo do popup.');
          // Normalmente, o próprio componente de popup lida com seu fechamento.
          // Se você precisar fechá-lo programaticamente daqui, precisaria de uma referência ao ez-popup.
        };
      }
    }
  };

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <EzButton onClick={handleShowPopUp} label="Mostrar PopUp"></EzButton>
      </div>
    </SnkApplication>
  );
};

export default ContasReceber;
```

### `createDataunit(entityName: string, dataUnitName?: string, parentDataUnit?: DataUnit, configName?: string, resourceID?: string): Promise<DataUnit>`

Cria uma instância de `DataUnit` a partir do nome da entidade. Se `dataUnitName` for fornecido, o `DataUnit` pode ser cacheado e reutilizado.

```jsx
import React, { useRef, useEffect } from 'react';

const CreateDataUnitExample = () => {
  const snkApplicationRef = useRef(null);

  useEffect(() => {
    const createAndUseDataUnit = async () => {
      if (snkApplicationRef.current) {
        try {
          const app = await snkApplicationRef.current.whenApplicationReady();

          // Exemplo 1: Criar um DataUnit sem cacheá-lo explicitamente pelo nome (ainda será gerenciado internamente)
          const duProdutos = await app.createDataunit('Produto');
          console.log('DataUnit "Produto" criado (sem nome de cache explícito):', duProdutos);
          await duProdutos.loadMetadata();
          console.log('Metadados para "Produto" carregados.');

          // Exemplo 2: Criar um DataUnit e cacheá-lo com um nome específico
          // Se getDataUnit for chamado posteriormente com 'MeuDataUnitParceiro', esta instância será retornada.
          const duParceiroCached = await app.createDataunit('Parceiro', 'MeuDataUnitParceiro');
          console.log('DataUnit "Parceiro" criado e cacheado como "MeuDataUnitParceiro":', duParceiroCached);
          await duParceiroCached.loadMetadata();
          console.log('Metadados para "MeuDataUnitParceiro" carregados.');

          // Exemplo 3: Tentando obter o DataUnit cacheado
          const retrievedDuParceiro = await app.getDataUnit('Parceiro', 'MeuDataUnitParceiro');
          console.log('DataUnit "MeuDataUnitParceiro" recuperado do cache:', retrievedDuParceiro);
          console.log('As instâncias são as mesmas?', duParceiroCached === retrievedDuParceiro); // Deve ser true

        } catch (error) {
          console.error('Erro ao criar ou usar DataUnit:', error);
        }
      }
    };
    createAndUseDataUnit();
  }, []);

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <p>Verifique o console para os resultados da criação e uso de DataUnits.</p>
      </div>
    </SnkApplication>
  );
};

export default CreateDataUnitExample;
```

### `getDataUnit(entityName: string, dataUnitName: string, parentDataUnit?: DataUnit, configName?: string, resourceID?: string): Promise<DataUnit>`

Obtém um `DataUnit` do cache da aplicação. Se não existir no cache, cria um novo (utilizando `createDataunit` internamente) e o armazena no cache.

```jsx
import React, { useRef, useEffect } from 'react';

const GetDataUnitExample = () => {
  const snkApplicationRef = useRef(null);

  useEffect(() => {
    const fetchDataUnit = async () => {
      if (snkApplicationRef.current) {
        try {
          // Certifique-se de que a aplicação está pronta antes de tentar obter uma data unit
          await snkApplicationRef.current.whenApplicationReady();
          const dataUnit = await snkApplicationRef.current.getDataUnit('Produto', 'ProdutoDataUnitGlobal');
          console.log('DataUnit "ProdutoDataUnitGlobal" para a entidade "Produto" obtida:', dataUnit);
          // Agora você pode usar esta instância de dataUnit para buscar dados, etc.
          // Por exemplo, para carregar metadados:
          // await dataUnit.loadMetadata();
          // console.log('Metadados carregados para ProdutoDataUnitGlobal');
        } catch (error) {
          console.error('Erro ao obter DataUnit:', error);
        }
      }
    };
    fetchDataUnit();
  }, []);

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <p>Verifique o console para a tentativa de obtenção do DataUnit.</p>
        {/*
          Para tornar este exemplo totalmente executável, você normalmente teria um snk-data-unit
          ou outros componentes que interagem com o DataUnit.
          Este exemplo foca na obtenção programática via snk-application.
        */}
      </div>
    </SnkApplication>
  );
};

export default GetDataUnitExample;
```

### `callServiceBroker(serviceName: string, payload: string | Object, options?: Options): Promise<any>`

Realiza uma chamada a um Service Broker específico.

  * `serviceName`: Nome do serviço a ser chamado.
  * `payload`: Dados a serem enviados para o serviço.
  * `options`: (Opcional) Parâmetros de URL.

```jsx
import React, { useRef, useState } from 'react';
import { EzButton, EzTextInput } from "@sankhyalabs/ezui/react/components";

const CallServiceBrokerExample = () => {
  const snkApplicationRef = useRef(null);
  const [configKey, setConfigKey] = useState('USALOCAL'); // Chave de configuração padrão
  const [serviceResponse, setServiceResponse] = useState('');

  const handleCallGetConfig = async () => {
    if (snkApplicationRef.current && configKey) {
      try {
        const serviceName = 'SystemUtilsSP.getConf'; // Serviço para buscar configuração

        const payload = {
          requestBody: { // Adicionando requestBody conforme o padrão de chamadas de serviço
            config: {
              chave: configKey,
              tipo: "T" // Tipo Texto, ajuste conforme a configuração real
            }
          }
        };

        console.log(`Chamando serviço: ${serviceName} para a chave: ${configKey} com payload:`, payload);
        setServiceResponse(`Chamando serviço: ${serviceName} para a chave: ${configKey}...`);

        const response = await snkApplicationRef.current.callServiceBroker(serviceName, payload);
        console.log('Resposta do Service Broker (getConfig):', response);

        if (response && response.responseBody && response.responseBody.config && response.responseBody.config.data !== undefined) {
          const successMessage = `Configuração '${configKey}' obtida com sucesso! Valor: ${response.responseBody.config.data}.`;
          alert(successMessage + " Verifique o console para a resposta completa.");
          setServiceResponse(successMessage + ` Resposta completa: ${JSON.stringify(response)}`);
        } else {
          const partialResponseMessage = `Serviço '${serviceName}' chamado para a chave '${configKey}'. Resposta não contém 'responseBody.config.data' esperado ou o valor é undefined.`;
          alert(partialResponseMessage + " Verifique o console.");
          setServiceResponse(partialResponseMessage + ` Resposta completa: ${JSON.stringify(response)}`);
        }

      } catch (error) {
        console.error(`Erro ao chamar o Service Broker (${serviceName}) para a chave '${configKey}':`, error);
        const errorMessage = `Erro ao chamar o serviço '${serviceName}' para a chave '${configKey}'. Detalhes: ${error.message || error}`;
        alert(errorMessage + " Verifique o console.");
        setServiceResponse(errorMessage);
      }
    } else if (!configKey) {
        const noKeyMessage = "Por favor, informe uma chave de configuração.";
        alert(noKeyMessage);
        setServiceResponse(noKeyMessage);
    }
  };

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfigForGetConfig">
      <div>
        <EzTextInput
          label="Chave de Configuração"
          value={configKey}
          onEzChange={(e) => setConfigKey(e.detail)}
          placeholder="Ex: USALOCAL, EMAILSMTP"
          style={{ marginBottom: '10px' }}
        />
        <EzButton onClick={handleCallGetConfig} label="Chamar SystemUtilsSP.getConf"></EzButton>
        <p style={{ marginTop: '10px' }}>
          Este exemplo tenta chamar o serviço 'SystemUtilsSP.getConf' para buscar a configuração com a chave informada.
          Certifique-se de que este serviço está disponível e a chave de configuração existe.
          A resposta esperada contém o valor da configuração em <code>response.responseBody.config.data</code>.
        </p>
        {serviceResponse && (
          <div style={{ marginTop: '15px', padding: '10px', border: '1px solid #ccc', backgroundColor: '#f9f9f9' }}>
            <strong>Log da Chamada:</strong>
            <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-all', maxHeight: '200px', overflowY: 'auto' }}>
              {serviceResponse}
            </pre>
          </div>
        )}
      </div>
    </SnkApplication>
  );
};

export default CallServiceBrokerExample;
```

### Métodos para Obtenção de Parâmetros do Sistema (`get[Type]Param`)

O `snk-application` fornece um conjunto de métodos para buscar parâmetros configurados no sistema Sankhya. Estes parâmetros são frequentemente definidos na tela "preferências" dentro do ERP e controlam diversos comportamentos da aplicação. Cada método é especializado em retornar o valor do parâmetro no tipo JavaScript correspondente.

  * **`getBooleanParam(name: string): Promise<boolean>`**: Busca um parâmetro do sistema e o retorna como um valor booleano (`true` ou `false`).
  * **`getStringParam(name: string): Promise<string>`**: Busca um parâmetro do sistema e o retorna como uma string.
  * **`getIntParam(name: string): Promise<number>`**: Busca um parâmetro do sistema e o retorna como um número inteiro.
  * **`getFloatParam(name: string): Promise<number>`**: Busca um parâmetro do sistema e o retorna como um número de ponto flutuante (decimal).
  * **`getDateParam(name: string): Promise<Date>`**: Busca um parâmetro do sistema, que geralmente está armazenado como uma string de data, e o converte para um objeto `Date` do JavaScript.

**Parâmetros:**

  * `name`: (string) A chave (nome) do parâmetro do sistema que se deseja obter. Esta chave corresponde ao identificador do parâmetro no Sankhya ERP.

**Retorno:**

  * Uma `Promise` que resolve com o valor do parâmetro no tipo especificado pelo método, ou pode ser rejeitada se o parâmetro não for encontrado ou ocorrer um erro na busca.

**Exemplo de Uso Consolidado:**

O exemplo abaixo demonstra como buscar diferentes tipos de parâmetros do sistema Sankhya dentro de um componente React. Ele utiliza a referência ao `snk-application` para acessar os métodos `get[Type]Param`.

```jsx
import React, { useEffect, useRef } from 'react';

const ParamFetcherComponent = () => {
  const snkApplicationRef = useRef(null);

  async function fetchSankhyaParameters(snkApplicationInstance) {
    if (!snkApplicationInstance) return;

    try {
      // Boolean parameters
      const utilizaNroSerieGlobal = await snkApplicationInstance.getBooleanParam('mge.utiliza.numero.serie.global');
      const controlaFatLocacaoBem = await snkApplicationInstance.getBooleanParam("controla.fat.loc.bem");
      console.log('Parâmetro (Boolean) mge.utiliza.numero.serie.global:', utilizaNroSerieGlobal);
      console.log('Parâmetro (Boolean) controla.fat.loc.bem:', controlaFatLocacaoBem);

      // Float parameters
      const topConsignacaoVenda = await snkApplicationInstance.getFloatParam('tops.consignacao.venda'); // Ex: 'tops.consignacao.venda' ou 'tops.consignacao.compra'
      const dataBaseFaturamento = await snkApplicationInstance.getFloatParam('com.data.base.faturamento');
      console.log('Parâmetro (Float) tops.consignacao.venda:', topConsignacaoVenda);
      console.log('Parâmetro (Float) com.data.base.faturamento:', dataBaseFaturamento);

      // Integer parameters
      const veiculoNoHelp = await snkApplicationInstance.getIntParam("com.apresenta.veiculo.help");
      const diasExibirPedParceiro = await snkApplicationInstance.getIntParam("com.nro.dias.exibe.tela.pedidos.parceiro");
      console.log('Parâmetro (Integer) com.apresenta.veiculo.help:', veiculoNoHelp);
      console.log('Parâmetro (Integer) com.nro.dias.exibe.tela.pedidos.parceiro:', diasExibirPedParceiro);

      // String parameters
      const precisaoMoeda = await snkApplicationInstance.getStringParam('mgefin.decimais.calc.moeda');
      const seriePadraoVenda = await snkApplicationInstance.getStringParam('com.serie.padrao.para.faturamento.venda');
      console.log('Parâmetro (String) mgefin.decimais.calc.moeda:', precisaoMoeda);
      console.log('Parâmetro (String) com.serie.padrao.para.faturamento.venda:', seriePadraoVenda);

      // Date parameters
      // Supondo que exista um parâmetro 'mgecom.data.inicio.ult.nota.tecnica.mdfe' configurado no sistema
      const dataLimitePromocao = await snkApplicationInstance.getDateParam('mgecom.data.inicio.ult.nota.tecnica.mdfe');
      if (dataLimitePromocao instanceof Date) {
        console.log('Parâmetro (Date) mgecom.data.inicio.ult.nota.tecnica.mdfe:', dataLimitePromocao.toLocaleDateString());
      } else {
        console.log('Parâmetro (Date) mgecom.data.inicio.ult.nota.tecnica.mdfe não encontrado ou inválido.');
      }

    } catch (error) {
      console.error('Erro ao buscar parâmetros Sankhya:', error);
      // Tratar o erro apropriadamente em uma aplicação real
      if (snkApplicationInstance && snkApplicationInstance.error) {
        snkApplicationInstance.error('Erro de Parâmetros', `Falha ao buscar parâmetros: ${error.message || error}`);
      }
    }
  }

  useEffect(() => {
    if (snkApplicationRef.current) {
      snkApplicationRef.current.whenApplicationReady().then(appInstance => {
        fetchSankhyaParameters(appInstance);
      });
    }
  }, []);

  return (
    <SnkApplication ref={snkApplicationRef} config-name="ParamFetcherApp">
      <div>
        Verifique o console para os valores dos parâmetros buscados.
      </div>
    </SnkApplication>
  );
};

export default ParamFetcherComponent;
```

Este exemplo consolida a busca de diversos tipos de parâmetros, ilustrando como cada método `get[Type]Param` é utilizado. As chaves dos parâmetros (`'mge.utiliza.numero.serie.global'`, `'tops.consignacao.venda'`, etc.) são exemplos reais encontrados no contexto do `SelecaoDocumento`, demonstrando a aplicação prática destes métodos.

### `hasAccess(access: AutorizationType, resourceID?: string): Promise<boolean>`

Verifica se o usuário logado possui uma permissão específica para um determinado `resourceID`.

### `getAllAccess(resourceID?: string): Promise<any>`

Obtém todas as permissões do usuário logado para um `resourceID`.

```jsx
import React, { useRef, useEffect, useState } from 'react';

const HasAccessExample = () => {
  const snkApplicationRef = useRef(null);
  const [accessResult, setAccessResult] = useState('Verificando...');
  const [allAccessResult, setAllAccessResult] = useState('Verificando...');
  const resourceID = 'TGFPRO'; // ID de Recurso de Exemplo

  useEffect(() => {
    const checkUserAccess = async () => {
      if (snkApplicationRef.current) {
        try {
          // Aguarda a aplicação estar pronta
          const app = await snkApplicationRef.current.whenApplicationReady();

          // Verifica um acesso específico (ex: 'SELECT')
          // AutorizationType pode ser: 'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'EXECUTE', 'EXPORT', 'IMPORT', 'ADMIN'
          const hasSelectAccess = await app.hasAccess('SELECT', resourceID);
          setAccessResult(`Usuário possui acesso 'SELECT' para o recurso '${resourceID}': ${hasSelectAccess}`);
          console.log(`Usuário possui acesso 'SELECT' para o recurso '${resourceID}':`, hasSelectAccess);

          // Obtém todos os acessos para o recurso
          const allAccess = await app.getAllAccess(resourceID);
          setAllAccessResult(`Todos os acessos para o recurso '${resourceID}': ${JSON.stringify(allAccess)}`);
          console.log(`Todos os acessos para o recurso '${resourceID}':`, allAccess);

        } catch (error) {
          console.error('Erro ao verificar acesso:', error);
          setAccessResult('Erro ao verificar acesso. Veja o console.');
          setAllAccessResult('Erro ao verificar todos os acessos. Veja o console.');
        }
      }
    };
    checkUserAccess();
  }, []);

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <p><strong>Verificação de Acesso Específico:</strong> {accessResult}</p>
        <p><strong>Verificação de Todos os Acessos:</strong> {allAccessResult}</p>
        <p>Este exemplo verifica permissões para o ID de recurso '{resourceID}'. Os resultados dependem das permissões do usuário logado.</p>
      </div>
    </SnkApplication>
  );
};

export default HasAccessExample;
```

### `importScript(relativePath: string | Array<string>): Promise<void>`

Realiza a importação de um ou mais scripts JavaScript localizados na pasta `/public` da aplicação.

```jsx
import React, { useRef } from 'react';
import { EzButton } from "@sankhyalabs/ezui/react/components";

// Crie um arquivo de script de exemplo na sua pasta /public para este exemplo funcionar.
// ex: /public/custom-scripts/my-utility.js
// Conteúdo de /public/custom-scripts/my-utility.js:
//
// window.myUtilityFunction = () => {
//   console.log('myUtilityFunction chamada do script importado!');
//   alert('myUtilityFunction do script importado foi chamada!');
// };
// console.log('my-utility.js carregado');
//

const ImportScriptExample = () => {
  const snkApplicationRef = useRef(null);

  const handleImportAndRun = async () => {
    if (snkApplicationRef.current) {
      try {
        // O caminho é relativo ao diretório /public da sua aplicação
        const scriptPath = 'custom-scripts/my-utility.js';

        console.log(`Tentando importar script: ${scriptPath}`);
        await snkApplicationRef.current.importScript(scriptPath);
        console.log(`Script ${scriptPath} importado com sucesso.`);

        // Tenta usar uma função definida no script importado
        if (window.myUtilityFunction) {
          window.myUtilityFunction();
        } else {
          console.warn('myUtilityFunction não está definida em window. Verifique o conteúdo e o caminho do script.');
          alert('Script importado, mas myUtilityFunction não encontrada. Verifique o console.');
        }
      } catch (error) {
        console.error('Erro ao importar script:', error);
        alert('Erro ao importar script. Verifique o console e certifique-se de que o script existe em /public/custom-scripts/my-utility.js');
      }
    }
  };

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <EzButton onClick={handleImportAndRun}>Importar e Executar Script Utilitário</EzButton>
        <p>
          Este exemplo tenta importar <code>/public/custom-scripts/my-utility.js</code> e executar <code>window.myUtilityFunction()</code>.
        </p>
        <p>
          Por favor, crie <code>my-utility.js</code> na pasta <code>public/custom-scripts/</code> da sua aplicação com o seguinte conteúdo:
        </p>
        <pre>
{`window.myUtilityFunction = () => {
  console.log('myUtilityFunction chamada do script importado!');
  alert('myUtilityFunction do script importado foi chamada!');
};
console.log('my-utility.js carregado');`}
        </pre>
      </div>
    </SnkApplication>
  );
};

export default ImportScriptExample;
```

### `executeSearch(searchArgument: ISearchArgument, fieldName: string, dataUnit: DataUnit, ctxOptions?: any): Promise<Array<IOption> | IOption>`

Executa uma pesquisa com base nos argumentos fornecidos, nome do campo e `DataUnit`. Utilizado internamente por componentes de pesquisa.

### `executePreparedSearch(mode: string, argument: string, options: any): Promise<Array<IOption> | IOption>`

Executa uma pesquisa já preparada, podendo ser em modo "ADVANCED" (que abre um popup de pesquisa) ou direto (retornando uma lista de opções).

```jsx
import React, { useRef, useState, useEffect } from 'react';
import { EzButton } from "@sankhyalabs/ezui/react/components";

const ExecuteSearchExample = () => {
  const snkApplicationRef = useRef(null);
  const [searchResults, setSearchResults] = useState([]);
  const [preparedSearchResults, setPreparedSearchResults] = useState([]);
  const [dataUnitInstance, setDataUnitInstance] = useState(null);

  useEffect(() => {
    const setup = async () => {
      if (snkApplicationRef.current) {
        try {
          // Para executeSearch, precisamos de um DataUnit com o campo que será pesquisado.
          // O nome 'ProdutoSearchDU' é um nome de cache para este exemplo.
          const du = await snkApplicationRef.current.createDataunit('Produto', 'ProdutoSearchDU');
          await du.loadMetadata(); // Metadados são importantes para a pesquisa
          setDataUnitInstance(du);
          console.log('DataUnit para Produto (ProdutoSearchDU) obtido e metadados carregados.');
        } catch (error) {
          console.error('Falha ao obter ou preparar DataUnit para pesquisa:', error);
          alert('Falha ao preparar DataUnit. Verifique o console.');
        }
      }
    };
    setup();
  }, []);

  const handleExecuteSearch = async () => {
    if (snkApplicationRef.current && dataUnitInstance) {
      try {
        // Argumento para executeSearch:
        // - argument: o texto/valor a ser pesquisado
        // - mode: geralmente 'SIMPLE' para pesquisa direta ou 'ADVANCED' para abrir popup (mas executeSearch é mais para programático)
        const searchArgument = {
          argument: 'SANKHYA', // O que estamos procurando
          mode: 'SIMPLE' // Modo de pesquisa
        };
        // fieldName: O nome do campo no DataUnit que está originando a pesquisa.
        // Os metadados deste campo (ex: entidade de busca associada) serão usados.
        const fieldName = 'DESCRPROD';

        console.log('Executando executeSearch com argumento:', searchArgument, 'no campo:', fieldName, 'usando DataUnit:', dataUnitInstance);
        const results = await snkApplicationRef.current.executeSearch(searchArgument, fieldName, dataUnitInstance);
        console.log('Resultados de executeSearch:', results);
        setSearchResults(Array.isArray(results) ? results : (results ? [results] : []));
        alert('executeSearch concluído. Verifique o console e os resultados abaixo.');
      } catch (error) {
        console.error('Erro em executeSearch:', error);
        alert('Erro durante executeSearch. Verifique o console.');
        setSearchResults([]);
      }
    } else {
      alert('SnkApplication ou DataUnit não está pronto para executeSearch.');
    }
  };

  const handleExecutePreparedSearchAdvanced = async () => {
    if (snkApplicationRef.current) {
      try {
        // Para executePreparedSearch, passamos os detalhes da pesquisa diretamente.
        const argument = ''; // Pode ser um valor inicial para o popup de pesquisa
        const options = {
          entity: 'Produto', // Entidade a ser pesquisada
          entityDescription: 'Pesquisa de Produtos', // Título do popup
          criteria: { expression: "CODPROD > 0", params: [] }, // Critérios adicionais, se necessário
          searchOptions: { // Opções específicas da pesquisa
            // rootEntity: 'Produto', // Se for hierárquico
            descriptionFieldName: 'DESCRPROD',
            codeFieldName: 'CODPROD'
          },
          // isHierarchyEntity: false,
          // allowsNonAnalytic: false
        };

        console.log('Executando executePreparedSearch (ADVANCED) com argumento:', argument, 'e opções:', options);
        // O modo "ADVANCED" geralmente abre um popup (snk-pesquisa).
        // A promessa é resolvida quando o popup é fechado.
        const results = await snkApplicationRef.current.executePreparedSearch('ADVANCED', argument, options);
        console.log('Resultados de executePreparedSearch (ADVANCED):', results);
        setPreparedSearchResults(Array.isArray(results) ? results : (results ? [results] : []));
        alert('executePreparedSearch (ADVANCED) concluído. Verifique o console e os resultados abaixo se algum foi retornado diretamente (após fechar o popup).');
      } catch (error) {
        console.error('Erro em executePreparedSearch (ADVANCED):', error);
        alert('Erro durante executePreparedSearch (ADVANCED). Verifique o console.');
        setPreparedSearchResults([]);
      }
    } else {
      alert('SnkApplication não está pronto para executePreparedSearch.');
    }
  };

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <p>Este exemplo demonstra `executeSearch` (pesquisa programática baseada em um campo de DataUnit) e `executePreparedSearch` (pesquisa com parâmetros explícitos, frequentemente abrindo um popup).</p>

        <h4>Demonstração de <code>executeSearch</code></h4>
        <p>Requer que o DataUnit 'Produto' (nomeado 'ProdutoSearchDU') esteja configurado e o campo 'DESCRPROD' exista.</p>
        <EzButton onClick={handleExecuteSearch} disabled={!dataUnitInstance} label="Executar Pesquisa Programática (executeSearch)"></EzButton>
        <p>Resultados de executeSearch (buscando por "SANKHYA" em DESCRPROD):</p>
        <ul>
          {searchResults.map((item, index) => (
            <li key={index}>{item.label || JSON.stringify(item)} (Valor: {item.value})</li>
          ))}
        </ul>
        {searchResults.length === 0 && <p>Sem resultados ou pesquisa ainda não executada.</p>}

        <hr style={{margin: '20px 0'}} />

        <h4>Demonstração de <code>executePreparedSearch</code></h4>
        <EzButton onClick={handleExecutePreparedSearchAdvanced} label="Executar Pesquisa Preparada (executePreparedSearch - Modo ADVANCED)"></EzButton>
        <p>Resultados de executePreparedSearch (ADVANCED) - após fechar o popup:</p>
        <ul>
          {preparedSearchResults.map((item, index) => (
            <li key={index}>{item.label || JSON.stringify(item)} (Valor: {item.value})</li>
          ))}
        </ul>
        {preparedSearchResults.length === 0 && <p>Sem resultados ou pesquisa ainda não executada/popup fechado sem seleção.</p>}
      </div>
    </SnkApplication>
  );
};

export default ExecuteSearchExample;
```

### `addClientEvent(eventID: string, handler: (clientEvent: IClientEventResponse, dataFetcherRecaller: IDataFetcherRecaller) => void): Promise<void>`

Registra um manipulador para um evento de cliente no `DataFetcher` da aplicação.

### `removeClientEvent(eventID: string): Promise<void>`

Remove um manipulador de evento de cliente previamente registrado.

```jsx
import React, { useRef, useEffect } from 'react';
import { ApplicationContext } from "@sankhyalabs/core"; // Importar para acesso no cleanup
import { EzButton } from "@sankhyalabs/ezui/react/components";

const AddRemoveClientEventExample = () => {
  const snkApplicationRef = useRef(null);
  const eventId = 'meu.evento.customizado.exemplo';

  // É importante que a função handler seja estável ou memorizada se usada em dependências de useEffect.
  const meuManipuladorDeEvento = (clientEvent, dataFetcherRecaller) => {
    console.log(`Manipulador para "${eventId}" chamado! Evento:`, clientEvent);
    alert(`Evento "${eventId}" recebido! Dados: ${JSON.stringify(clientEvent.response)}`);
    // dataFetcherRecaller pode ser usado para re-executar a chamada de serviço original, se necessário
    // Exemplo: dataFetcherRecaller.recall();
  };

  useEffect(() => {
    let appInstanceForCleanup; // Para armazenar a instância do app para o cleanup

    const setupEvents = async () => {
      if (snkApplicationRef.current) {
        try {
          appInstanceForCleanup = snkApplicationRef.current; // Armazena para o cleanup

          // Adicionar o client event
          await snkApplicationRef.current.addClientEvent(eventId, meuManipuladorDeEvento);
          console.log(`Client event "${eventId}" adicionado.`);
          alert(`Manipulador para "${eventId}" foi registrado. Para testar, um evento com este ID precisaria ser disparado pelo backend (ex: via Service Broker).`);

          // Verificar se o evento foi adicionado (opcional)
          const hasEvent = await snkApplicationRef.current.hasClientEvent(eventId);
          console.log(`O evento "${eventId}" está registrado? ${hasEvent}`); // Deve ser true

        } catch (error) {
          console.error('Erro ao configurar client events:', error);
          alert('Erro ao registrar client event. Veja o console.');
        }
      }
    };

    setupEvents();

    // Função de limpeza para remover o client event quando o componente for desmontado
    return () => {
      const removeEvent = async () => {
        // Tenta usar a instância armazenada ou obter do ApplicationContext como fallback
        const appToUse = appInstanceForCleanup || ApplicationContext.getContextValue("__SNK__APPLICATION__");
        if (appToUse) {
          try {
            await appToUse.removeClientEvent(eventId);
            console.log(`Client event "${eventId}" removido no cleanup do componente.`);
          } catch (error) {
            // Não lançar alerta aqui, pois pode ocorrer durante a desmontagem e ser indesejado.
            console.error(`Erro ao remover client event "${eventId}" no cleanup:`, error);
          }
        } else {
            console.warn(`Não foi possível obter a instância do SnkApplication para remover o evento "${eventId}" no cleanup.`);
        }
      };
      removeEvent();
    };
  }, []); // Array de dependências vazio para rodar apenas na montagem e desmontagem

  const handleRemoveEventManually = async () => {
    if (snkApplicationRef.current) {
        try {
            await snkApplicationRef.current.removeClientEvent(eventId);
            console.log(`Client event "${eventId}" removido manualmente pelo botão.`);
            alert(`Manipulador para "${eventId}" foi removido manualmente.`);
            const hasEvent = await snkApplicationRef.current.hasClientEvent(eventId);
            console.log(`O evento "${eventId}" está registrado após remoção manual? ${hasEvent}`); // Deve ser false
        } catch (error) {
            console.error('Erro ao remover client event manualmente:', error);
            alert('Erro ao remover client event manualmente. Veja o console.');
        }
    }
  }

  const handleSimulateBackendEvent = async () => {
    // ATENÇÃO: Esta é uma SIMULAÇÃO LOCAL e NÃO REPRESENTA como o backend dispara eventos.
    // O backend dispararia o evento através de sua própria lógica e infraestrutura.
    // Esta função apenas invoca o handler diretamente para fins de demonstração da UI.
    console.warn(`Simulando recebimento do evento "${eventId}" LOCALMENTE. O backend deve disparar o evento real.`);
    const mockClientEvent = {
        eventID: eventId,
        response: {
            message: "Este é um evento simulado localmente!",
            timestamp: new Date().toISOString(),
            data: { info: "Dados de exemplo" }
        }
    };
    const mockDataFetcherRecaller = {
        recall: () => console.log("Simulação: dataFetcherRecaller.recall() chamado.")
    };
    meuManipuladorDeEvento(mockClientEvent, mockDataFetcherRecaller);
  }

  return (
    <SnkApplication ref={snkApplicationRef} config-name="myAppConfig">
      <div>
        <p>Este exemplo demonstra o registro e remoção de um manipulador para um Client Event com ID: "<strong>{eventId}</strong>".</p>
        <p>Verifique o console para o status do registro e remoção.</p>
        <p>Para testar o recebimento real do evento, o backend precisaria disparar um client event com o ID acima (ex: após uma chamada de Service Broker).</p>
        <EzButton onClick={handleRemoveEventManually} style={{marginRight: '10px'}} label="Remover Evento Manualmente"></EzButton>
        <EzButton onClick={handleSimulateBackendEvent} label="Simular Recebimento de Evento (Local)"></EzButton>
        <p style={{marginTop: '10px', fontSize: '0.9em', color: 'gray'}}>
            <em>A simulação local invoca o manipulador diretamente e não reflete o fluxo real de um evento vindo do backend.</em>
        </p>
      </div>
    </SnkApplication>
  );
};

export default AddRemoveClientEventExample;
```

## Propriedades Importantes

### `loadByPK: (objPK: { pk: Record<string, any> }, redirectFrom?: string) => void`

A propriedade `loadByPK` é um recurso poderoso que permite à sua aplicação carregar e exibir informações específicas de forma inteligente quando ela é acessada através de um link ou navegação que contém identificadores únicos (conhecidos como chave primária ou PK) na URL.

Imagine que um usuário clica em um link (em outra tela, um e-mail ou um relatório) que o direciona para a sua aplicação com o intuito de visualizar ou editar um item específico – como um produto, um cliente ou um pedido. A `loadByPK` é o mecanismo que permite à sua aplicação "entender" exatamente qual item o usuário deseja ver e, então, carregar e apresentar os dados corretos assim que a tela é aberta.

Para os desenvolvedores, isso significa definir uma função que recebe esses identificadores (ex: `{ pk: { CODPROD: 10, CODLOCAL: 2 } }`) e, com base neles, busca e exibe os dados relevantes, seja preenchendo um formulário ou filtrando uma grade.

Se essa lógica personalizada não for fornecida através da `loadByPK`, a aplicação tentará um comportamento padrão: ela procurará o primeiro componente de dados (`snk-data-unit`) na tela e aplicará um filtro usando os identificadores recebidos. Isso funciona bem para cenários mais simples. No entanto, para fluxos de trabalho mais complexos ou quando uma lógica de carregamento específica é necessária (por exemplo, carregar dados de múltiplas fontes ou realizar validações antes de exibir), a implementação personalizada da `loadByPK` é essencial.

Este recurso é fundamental para criar experiências de usuário fluidas e contextuais, garantindo que os usuários cheguem diretamente à informação que precisam, sem etapas manuais de busca ou filtro.

Existem três abordagens principais para utilizar o `loadByPK`:

  1. **Implementação Personalizada da Função`loadByPK`**: Você fornece uma função diretamente para a propriedade `loadByPK` do `snk-application`. Isso oferece controle total sobre como os dados da PK são usados para carregar ou filtrar os `DataUnits` ou realizar qualquer outra ação necessária. É a abordagem mais flexível.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit } from "@sankhyalabs/sankhyablocks/react/components";

const snkDataUnitFinanceiro = useRef(null);

const loadByPK = (pkObject) => {
    snkDataUnitFinanceiro?.loadData({
        filter: {
            name: 'LOAD_BY_PK_FILTER',
            expression: "this.NUFIN = :NUFIN",
            params: [{ name: "NUFIN", dataType: "NUMBER", value: pkObject.pk.NUFIN }]
        }
    })
}

const Demo = () => {
    return (
        <SnkApplication loadByPK={loadByPK}>
            <SnkDataUnit entityName="Financeiro"
                key="duFinanceiro"
                ref={snkDataUnitFinanceiro}>
                    <SnkCrud></SnkCrud>
                </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

  2. **Comportamento Padrão com Atributo`data-load-by-pk` no `snk-data-unit`**: Se você não fornecer uma função `loadByPK` personalizada, mas adicionar o atributo `data-load-by-pk` a um `snk-data-unit` específico, o `snk-application` automaticamente aplicará um filtro a esse `DataUnit` usando os campos e valores da PK recebidos na URL. Isso é útil quando você tem múltiplos `DataUnits` na tela e quer direcionar o carregamento por PK para um deles especificamente, sem escrever código customizado.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit } from "@sankhyalabs/sankhyablocks/react/components";

const snkDataUnitFinanceiro = useRef(null);

const Demo = () => {
    return (
        <SnkApplication>
            <SnkDataUnit entityName="Financeiro"
                key="duFinanceiro"
                ref={snkDataUnitFinanceiro}
                data-load-by-pk>
                    <SnkCrud></SnkCrud>
                </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

  3. **Comportamento Padrão (Implícito)** : Se nenhuma função `loadByPK` for fornecida e nenhum `snk-data-unit` tiver o atributo `data-load-by-pk`, o `snk-application` tentará aplicar o filtro de PK ao _primeiro_ `snk-data-unit` que encontrar na árvore DOM dentro dele. Esta é a abordagem mais simples, mas menos explícita, e funciona bem para telas com um único `DataUnit` principal.

```jsx
import React from 'react';
import { SnkApplication, SnkDataUnit } from "@sankhyalabs/sankhyablocks/react/components";

const snkDataUnitFinanceiro = useRef(null);

const Demo = () => {
    return (
        <SnkApplication>
            <SnkDataUnit entityName="Financeiro"
                key="duFinanceiro"
                ref={snkDataUnitFinanceiro}>
                    <SnkCrud></SnkCrud>
                </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

#### Resumo das Diferenças:

  * **Personalizado (`loadByPK` prop)**: Máxima flexibilidade. Você define a lógica exata de como usar a PK. Ideal para cenários complexos, múltiplos `DataUnits` com lógicas distintas, ou quando ações adicionais são necessárias além de um simples filtro.
  * **Padrão com Atributo (`data-load-by-pk`)**: Conveniência com especificidade. O `snk-application` aplica um filtro padrão, mas você direciona para qual `DataUnit` ele deve ser aplicado. Bom para telas com múltiplos `DataUnits` onde um deles é o alvo principal do `loadByPK`.
  * **Padrão Implícito** : Simplicidade máxima. O `snk-application` filtra o primeiro `DataUnit` encontrado. Adequado para telas simples com um único `DataUnit` principal.

A escolha da abordagem depende da complexidade da sua tela e do nível de controle que você precisa sobre o processo de carregamento por PK.

### `enableLockManagerLoadingApp: boolean`

Quando a propriedade `enableLockManagerLoadingApp` está ativa (`true`), ela habilita um sistema inteligente de gerenciamento de carregamento para a aplicação, conhecido como LockManager. Este sistema controla como o conteúdo é exibido durante o carregamento inicial da tela ou quando ocorrem recarregamentos de dados.

Em vez de mostrar uma tela em branco ou conteúdo aparecendo de forma fragmentada enquanto os dados e componentes são carregados, o `snk-application` pode exibir automaticamente um "esqueleto de carregamento" (placeholders visuais que imitam a estrutura da interface final) ou um indicador de progresso (spinner). Isso previne que o usuário tenha uma experiência visual desconfortável e dá um feedback claro de que a aplicação está trabalhando.

O LockManager ajuda a coordenar operações assíncronas. Métodos como `addLoadingLock()` e `markToReload()` permitem sinalizar ao `snk-application` quando partes da aplicação estão em processo de carregamento ou precisam ser atualizadas, garantindo que os indicadores visuais sejam exibidos corretamente.

Este recurso melhora significativamente a percepção de performance e a qualidade da experiência do usuário. Uma indicação visual clara durante os momentos de espera torna a aplicação mais profissional, reduz a frustração do usuário e transmite uma sensação de responsividade e estabilidade.

```jsx
import React, { useRef, useEffect, useState } from 'react';

const EnableLockManagerLoadingAppExample = () => {
  const snkApplicationRef = useRef(null);
  const [log, setLog] = useState([]);
  const [showContent, setShowContent] = useState(false);

  const addLog = (message) => {
    setLog(prevLog => [...prevLog, `${new Date().toLocaleTimeString()}: ${message}`]);
  };

  useEffect(() => {
    addLog('Componente montado.');

    const simulateAsyncLoad = async () => {
      if (snkApplicationRef.current) {
        const app = await snkApplicationRef.current.whenApplicationReady();
        addLog('SnkApplication está pronto.');

        // Simula uma tarefa de carregamento que usa o LockManager
        addLog('Iniciando simulação de tarefa de carregamento (3 segundos)...');
        const lockId = await app.addLoadingLock(); // Adiciona uma trava
        addLog(`Trava de carregamento adicionada (ID: ${lockId || 'N/A - pode não retornar ID se já travado'}). App deve mostrar skeleton/spinner.`);

        setTimeout(async () => {
          if (lockId) { // Se uma trava foi realmente adquirida
             await app.markToReload(); // Isso irá destravar e resolver o LockManager
          }
          // Se addLoadingLock não retornou um lockId (ex: já estava travado e resolvendo),
          // o markToReload pode não ser necessário ou pode ser chamado de outra forma.
          // Para este exemplo simples, assumimos que a trava foi pega.
          // Em cenários mais complexos, o gerenciamento de locks pode ser mais granular.

          addLog('Tarefa de carregamento simulada concluída. Conteúdo deveria ser visível.');
          setShowContent(true); // Mostra o conteúdo real
        }, 3000);
      }
    };

    simulateAsyncLoad();

  }, []);

  return (
    // Defina enable-lock-manager-loading-app como true para ver o efeito.
    // O skeleton padrão (grid) será exibido durante o "carregamento".
    <SnkApplication ref={snkApplicationRef} config-name="lockManagerApp" enable-lock-manager-loading-app="true">
      <div>
        <p>
          Este exemplo demonstra o uso de <code>enable-lock-manager-loading-app="true"</code>.
        </p>
        <p>
          Durante o carregamento inicial e operações que utilizam <code>addLoadingLock()</code> / <code>markToReload()</code>,
          um esqueleto de carregamento (ou spinner, dependendo da configuração e contexto) será exibido.
        </p>
        <p>
          Observe o console e os logs abaixo. Um carregamento simulado de 3 segundos ocorrerá após a aplicação estar pronta.
          Durante esses 3 segundos, o esqueleto de carregamento deve estar visível se <code>enable-lock-manager-loading-app</code> estiver ativo.
        </p>

        {showContent ? (
          <div style={{ padding: '20px', backgroundColor: '#e6ffe6', border: '1px solid green' }}>
            <h3>Conteúdo Carregado!</h3>
            <p>Este conteúdo apareceu após a simulação de carregamento.</p>
          </div>
        ) : (
          <div style={{ padding: '20px', backgroundColor: '#ffeee6', border: '1px solid orange' }}>
            <p>Aguardando o fim da simulação de carregamento para exibir o conteúdo principal...</p>
            <p>Se <code>enable-lock-manager-loading-app</code> estiver <code>true</code>, você deverá ver um skeleton/spinner em vez desta mensagem e do conteúdo principal.</p>
          </div>
        )}

        <h4>Logs do Exemplo:</h4>
        <ul style={{ maxHeight: '200px', overflowY: 'auto', border: '1px solid #ccc', padding: '10px' }}>
          {log.map((entry, index) => (
            <li key={index}>{entry}</li>
          ))}
        </ul>
         <p><em>Se <code>enable-lock-manager-loading-app</code> for <code>false</code>, o skeleton não será exibido automaticamente pelo <code>snk-application</code> durante o carregamento inicial gerenciado pelo LockManager.</em></p>
      </div>
    </SnkApplication>
  );
};

export default EnableLockManagerLoadingAppExample;
```

## Eventos Emitidos

### `applicationLoading: EventEmitter<boolean>`

O evento `applicationLoading` é disparado pelo `snk-application` no exato momento em que ele inicia seu processo de carregamento e inicialização. Ele sinaliza o "ponto de partida" do carregamento da tela.

Este evento é útil para desenvolvedores que precisam executar alguma lógica preparatória muito cedo no ciclo de vida da aplicação, como exibir um indicador de carregamento global customizado ou iniciar tarefas em segundo plano, antes mesmo que qualquer conteúdo principal seja renderizado ou que a aplicação esteja totalmente pronta para interação (o que é sinalizado pelo evento `applicationLoaded`).

É importante entender que este evento ajuda a mapear o ciclo de vida completo do carregamento da aplicação. Embora o feedback visual durante o carregamento seja frequentemente gerenciado pela propriedade `enableLockManagerLoadingApp`, saber que este evento marca o início do processo pode ser útil para discussões sobre a experiência de carregamento.

```jsx
import React, { useRef, useEffect, useState } from 'react';

const ApplicationLoadingEventExample = () => {
  const snkApplicationRef = useRef(null);
  const [status, setStatus] = useState('Aguardando snk-application iniciar o carregamento...');
  const [eventReceived, setEventReceived] = useState(false);

  useEffect(() => {
    const appElement = snkApplicationRef.current;

    const handleApplicationLoading = (event) => {
      console.log('Evento "applicationLoading" recebido!', event);
      // event.detail deve ser true
      setStatus(`Evento "applicationLoading" recebido! A aplicação iniciou o processo de carregamento. (event.detail: ${event.detail})`);
      setEventReceived(true);

      // Neste ponto, a aplicação apenas começou a carregar.
      // Útil para, por exemplo, mostrar um indicador de carregamento global muito cedo.
    };

    const handleApplicationLoaded = () => {
        setStatus(prev => prev + ' | Evento "applicationLoaded" também recebido (aplicação pronta).');
    }

    if (appElement) {
      // Adiciona o event listener para applicationLoading
      appElement.addEventListener('applicationLoading', handleApplicationLoading);
      // Adiciona listener para loaded para ver a sequência
      appElement.addEventListener('applicationLoaded', handleApplicationLoaded);
      setStatus('Listeners para "applicationLoading" e "applicationLoaded" adicionados. Aguardando os eventos...');
    }

    // Cleanup: remove os event listeners quando o componente for desmontado
    return () => {
      if (appElement) {
        appElement.removeEventListener('applicationLoading', handleApplicationLoading);
        appElement.removeEventListener('applicationLoaded', handleApplicationLoaded);
        console.log('Listeners para "applicationLoading" e "applicationLoaded" removidos.');
      }
    };
  }, []); // Array de dependências vazio para executar apenas na montagem e desmontagem

  return (
    <SnkApplication ref={snkApplicationRef} config-name="appLoadingEventDemo">
      <div>
        <h3>Exemplo do Evento <code>applicationLoading</code></h3>
        <p>
          Este exemplo demonstra como escutar o evento <code>applicationLoading</code> disparado pelo <code>snk-application</code>.
          Este evento é emitido assim que o componente inicia seu ciclo de carga.
        </p>
        <p>
          <strong>Status Atual:</strong> {status}
        </p>
        {eventReceived && (
          <div style={{ padding: '10px', backgroundColor: '#e6f7ff', border: '1px solid blue' }}>
            <p>O evento <code>applicationLoading</code> foi recebido!</p>
          </div>
        )}
        <p>Verifique o console para mais detalhes sobre o evento e a sequência em relação ao <code>applicationLoaded</code>.</p>
      </div>
    </SnkApplication>
  );
};

export default ApplicationLoadingEventExample;
```

### `applicationLoaded: EventEmitter<boolean>`

O evento `applicationLoaded` é disparado quando o `snk-application` e todos os seus componentes principais foram completamente carregados, inicializados e a aplicação está totalmente pronta para a interação do usuário. Ele sinaliza que "as cortinas subiram" e a interface está operacional.

Para os desenvolvedores, este é um momento crucial para executar lógicas que dependem da aplicação estar em pleno funcionamento, como buscar dados iniciais que não bloquearam a renderização inicial, ativar funcionalidades interativas ou integrar-se com outros sistemas. É uma alternativa à espera programática (como `await snkApplicationRef.current.whenApplicationReady()`), especialmente útil em arquiteturas orientadas a eventos.

É importante entender que este evento marca o ponto em que qualquer indicador de carregamento inicial deve desaparecer, e o usuário pode começar a interagir com todas as funcionalidades da tela. É o sinal de que a aplicação está pronta para entregar valor ao usuário.

```jsx
import React, { useRef, useEffect, useState } from 'react';

const ApplicationLoadedEventExample = () => {
  const snkApplicationRef = useRef(null);
  const [status, setStatus] = useState('Aguardando snk-application carregar...');
  const [eventReceived, setEventReceived] = useState(false);

  useEffect(() => {
    const appElement = snkApplicationRef.current;

    const handleApplicationLoaded = (event) => {
      console.log('Evento "applicationLoaded" recebido!', event);
      // event.detail deve ser true
      setStatus(`Evento "applicationLoaded" recebido! A aplicação está totalmente carregada e pronta. (event.detail: ${event.detail})`);
      setEventReceived(true);

      // Agora você pode executar lógicas que dependem da aplicação estar pronta.
      // Ex: interagir com outros componentes, buscar dados iniciais, etc.
      // Exemplo: appElement.callServiceBroker(...);
    };

    if (appElement) {
      // Adiciona o event listener
      appElement.addEventListener('applicationLoaded', handleApplicationLoaded);
      setStatus('Listener para "applicationLoaded" adicionado. Aguardando o evento...');
    }

    // Cleanup: remove o event listener quando o componente for desmontado
    return () => {
      if (appElement) {
        appElement.removeEventListener('applicationLoaded', handleApplicationLoaded);
        console.log('Listener para "applicationLoaded" removido.');
      }
    };
  }, []); // Array de dependências vazio para executar apenas na montagem e desmontagem

  return (
    <SnkApplication ref={snkApplicationRef} config-name="appLoadedEventDemo">
      <div>
        <h3>Exemplo do Evento <code>applicationLoaded</code></h3>
        <p>
          Este exemplo demonstra como escutar o evento <code>applicationLoaded</code> disparado pelo <code>snk-application</code>.
        </p>
        <p>
          <strong>Status Atual:</strong> {status}
        </p>
        {eventReceived && (
          <div style={{ padding: '10px', backgroundColor: '#e6ffe6', border: '1px solid green' }}>
            <p>O evento foi recebido! A aplicação está pronta.</p>
          </div>
        )}
        <p>Verifique o console para mais detalhes sobre o evento.</p>
      </div>
    </SnkApplication>
  );
};

export default ApplicationLoadedEventExample;
```

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| configName | config-name | Nome da configuração utilizada para salvar as preferências dos blocos de construção. | string | undefined |
| enableLockManagerLoadingApp | enable-lock-manager-loading-app | Define se o componente deve usar o LockManager para controle de carregamento da aplicação. | boolean | undefined |
| formLegacyConfigName | form-legacy-config-name | Chave da configuração legada do formulário, utilizada para migração de configurações antigas. | string | undefined |
| gridLegacyConfigName | grid-legacy-config-name | Chave da configuração legada da grade, utilizada para migração de configurações antigas. | string | undefined |
| loadByPK | -- | Usado para receber um parâmetro na inicialização da tela, e utilizá-lo conforme necessário caso a tela receba um parâmetro, e, esta propriedade não seja informada é criado um filtro de forma automática através do método defaultLoadByPk | (objPK: { pk: any; }, redirectFrom?: string) => void | undefined |
| messagesBuilder | -- | Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. | SnkMessageBuilder | undefined |

### Events

| Event | Description | Type |
|---|---|---|
| applicationLoaded | Emitido quando a aplicação for carregada. | CustomEvent<boolean> |
| applicationLoading | Emitido ao iniciar a carga do componente. | CustomEvent<boolean> |

### Methods

#### `addClientEvent(eventID: String, handler: (clientEvent: IClientEventResponse, dataFetcherReacaller: IDataFetcherRecaller) => void) => Promise<void>`

Registra um client event para o DataFetcher da aplicação.

##### Returns

Type: `Promise<void>`

#### `addLoadingLock(forceReady?: boolean, templateSkeletonType?: TEMPLATES_SKELETON) => Promise<() => void>`

Adiciona um bloqueio de carregamento à aplicação.

##### Returns

Type: `Promise<() => void>`

O ID do bloqueio adicionado.

#### `addPendingAction(actionsLocker: string, action: Function) => Promise<void>`

Adiciona uma ação pendente que deve ser executada por um determinado locker.

##### Returns

Type: `Promise<void>`

#### `addSearchListener(entityName: string, dataUnit: DataUnit, listener: ISearchListener) => Promise<IRemoveSearchListener>`

Adiciona um listener no fetcher de Pesquisa.

##### Returns

Type: `Promise<IRemoveSearchListener>`

Uma função para remover o listener.

#### `alert(title: string, message: string, icon?: string, options?: MessageOptions) => Promise<boolean>`

Exibe o diálogo de alerta de acordo com os parâmetros passados.

##### Returns

Type: `Promise<boolean>`

#### `callServiceBroker(serviceName: string, payload: string | Object, options?: Options) => Promise<any>`

Realiza a chamada ao Service Broker conforme o nome do serviço.

##### Returns

Type: `Promise<any>`

A resposta do Service Broker.

#### `clearPopUpTitle() => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `closeModal() => Promise<void>`

Fecha o Modal e limpa o conteúdo.

##### Returns

Type: `Promise<void>`

#### `closePopUp() => Promise<void>`

Fecha o Popup e limpa o conteúdo.

##### Returns

Type: `Promise<void>`

#### `confirm(title: string, message: string, icon?: string, dialogType?: DialogType, options?: MessageOptions) => Promise<boolean>`

Exibe um diálogo de confirmação.

##### Returns

Type: `Promise<boolean>`

`true` se confirmado, `false` caso contrário.

#### `createDataunit(entityName: string, dataUnitName?: string, parentDataUnit?: DataUnit, configName?: string, resourceID?: string) => Promise<DataUnit>`

Cria o DataUnit a partir do nome da entidade. É possível armazená-lo no cache passando o dataUnitName, assim, se mais de uma chamada for feita, o mesmo DataUnit será usado.

##### Returns

Type: `Promise<DataUnit>`

O DataUnit criado ou obtido do cache.

#### `error(title: string, message: string, icon?: string, options?: MessageOptions) => Promise<boolean>`

Exibe o diálogo de erro de acordo com os parâmetros passados.

##### Returns

Type: `Promise<boolean>`

#### `executePreparedSearch(mode: string, argument: string, options: any) => Promise<Array<IOption> | IOption>`

Obtém as opções em componentes de pesquisa com base em opções preparadas. Ex.: snk-config-options

##### Returns

Type: `Promise<IOption | IOption[]>`

Uma lista de opções ou uma única opção.

#### `executePreparedSearchPlus(mode: string, argument: string, options: any) => Promise<Array<IOption> | IOption>`

Realiza a pesquisa de registros Ex.: snk-config-options

##### Returns

Type: `Promise<IOption | IOption[]>`

Uma lista de opções ou uma única opção.

#### `executeSearch(searchArgument: ISearchArgument, fieldName: string, dataUnit: DataUnit, ctxOptions?: ISearchCtxOptions) => Promise<Array<IOption> | IOption>`

Obtém as opções em componentes de pesquisa. Ex.: snk-config-options

##### Returns

Type: `Promise<IOption | IOption[]>`

Uma lista de opções ou uma única opção.

#### `executeSelectDistinct(dataUnit: DataUnit, fieldName: string, argument: string) => Promise<Array<any>>`

Com base em um campo realiza um "select distinct" respeitando os filtros atuais do dataUnit e um critério de filtro para a própria coluna.

##### Returns

Type: `Promise<any[]>`

Uma lista de valores distintos.

#### `getAllAccess(resourceID?: string) => Promise<any>`

Obtém todos os acessos do usuário logado para um recurso específico ou para a aplicação.

##### Returns

Type: `Promise<any>`

Um objeto contendo todos os tipos de acesso e se o usuário os possui.

#### `getAppLabel() => Promise<string>`

Obtém o nome (label) da aplicação.

##### Returns

Type: `Promise<string>`

O nome da aplicação.

#### `getApplicationPath() => Promise<string>`

Retorna o path relativo da aplicação.

##### Returns

Type: `Promise<string>`

O caminho relativo da aplicação.

#### `getAttributeFromHTMLWrapper(attribName: string) => Promise<string>`

Acessa informações de contexto "empurrados" na abertura da tela.

##### Returns

Type: `Promise<string>`

O valor do atributo.

#### `getBooleanParam(name: string) => Promise<boolean>`

Obtém o valor de um parâmetro do tipo booleano.

##### Returns

Type: `Promise<boolean>`

O valor do parâmetro como booleano.

#### `getConfig(key: string) => Promise<any>`

Obtém a configuração de um recurso por service broker.

##### Returns

Type: `Promise<any>`

Os dados da configuração.

#### `getDataFetcher() => Promise<DataFetcher>`

Retorna a instância do DataFetcher utilizado pelo application.

##### Returns

Type: `Promise<DataFetcher>`

O DataFetcher da aplicação.

#### `getDataUnit(entityName: string, dataUnitName: string, parentDataUnit?: DataUnit, configName?: string, resourceID?: string) => Promise<DataUnit>`

Obtém um DataUnit do cache ou cria um caso ainda não tenha sido criado.

##### Returns

Type: `Promise<DataUnit>`

O DataUnit obtido do cache ou recém-criado.

#### `getDateParam(name: string) => Promise<Date>`

Obtém o valor de um parâmetro do tipo data.

##### Returns

Type: `Promise<Date>`

O valor do parâmetro como objeto Date.

#### `getFloatParam(name: string) => Promise<number>`

Obtém o valor de um parâmetro do tipo Decimal.

##### Returns

Type: `Promise<number>`

O valor do parâmetro como número decimal.

#### `getIntParam(name: string) => Promise<number>`

Obtém o valor de um parâmetro do tipo Inteiro.

##### Returns

Type: `Promise<number>`

O valor do parâmetro como número inteiro.

#### `getKeyboardManager() => Promise<KeyboardManager>`

Obtém o controlador de teclado.

##### Returns

Type: `Promise<KeyboardManager>`

O gerenciador de teclado.

#### `getLayoutFormConfig() => Promise<LayoutFormConfig>`

Obtém o notificador de Layout de formulário.

##### Returns

Type: `Promise<LayoutFormConfig>`

O configurador de Layout do Formulário.

#### `getResourceID() => Promise<string>`

Obtém o resourceID da tela em questão.

##### Returns

Type: `Promise<string>`

O ID do recurso da aplicação.

#### `getStringParam(name: string) => Promise<string>`

Obtém o valor de um parâmetro do tipo string.

##### Returns

Type: `Promise<string>`

O valor do parâmetro como string.

#### `getUserID() => Promise<string>`

Obtém o UserId do usuário logado.

##### Returns

Type: `Promise<string>`

O ID do usuário.

#### `hasAccess(access: AutorizationType, resourceID?: string) => Promise<boolean>`

Obtém `true` caso o usuário logado tenha permissão para determinada ação.

##### Returns

Type: `Promise<boolean>`

`true` se o usuário tiver acesso, `false` caso contrário.

#### `hasClientEvent(eventID: String) => Promise<boolean>`

Verifica se um client event está registrado no DataFetcher da aplicação.

##### Returns

Type: `Promise<boolean>`

`true` se o evento estiver registrado, `false` caso contrário.

#### `importScript(relativePath: string | Array<string>) => Promise<void>`

Realiza o import de um JavaScript que está disponível dentro da pasta /public da aplicação.

##### Returns

Type: `Promise<void>`

#### `info(message: string, options?: MessageOptions) => Promise<void>`

Exibe uma informação efêmera (de segundo plano).

##### Returns

Type: `Promise<void>`

#### `initOnboarding(onboardingKey: string) => Promise<void>`

Inicializa o onboarding para uma chave específica.

##### Returns

Type: `Promise<void>`

#### `isDebugMode() => Promise<boolean>`

Obtém `true` caso a tela esteja em modo de debug.

##### Returns

Type: `Promise<boolean>`

#### `isFeatureActive(featureName: string) => Promise<boolean>`

Retorna se uma feature flag global está ativa ou não.

##### Returns

Type: `Promise<boolean>`

#### `isLoadedByPk() => Promise<boolean>`

Obtém a informação se o último carregamento do dataunit foi feito através de um loadByPk.

##### Returns

Type: `Promise<boolean>`

`true` se foi carregado por PK, `false` caso contrário.

#### `isUserSup() => Promise<boolean>`

Obtém `true` caso o usuário logado seja o SUP.

##### Returns

Type: `Promise<boolean>`

`true` se o usuário for SUP, `false` caso contrário.

#### `loadTotals(name: string, resourceID: string, filters: Array<Filter>) => Promise<Map<string, number>>`

Obtém os totalizadores da grade.

##### Returns

Type: `Promise<Map<string, number>>`

Um mapa com os nomes dos totalizadores e seus valores.

#### `markToReload(templateSkeletonType?: TEMPLATES_SKELETON) => Promise<void>`

Marca a aplicação para recarregar, opcionalmente especificando um tipo de esqueleto de carregamento.

##### Returns

Type: `Promise<void>`

#### `message(title: string, message: string, icon?: string, options?: MessageOptions) => Promise<boolean>`

Exibe um diálogo de mensagem comum.

##### Returns

Type: `Promise<boolean>`

#### `openApp(resourceId: string, pkObject: Object) => Promise<void>`

Abre determinada tela, repassando pkObject.

##### Returns

Type: `Promise<void>`

#### `preloadMangerRemoveRecord(dataUnit: DataUnit, recordsIDs: Array<string>) => Promise<void>`

Remove registro do cache do PreLoader do dataunit. Deve ser usado quando existe um dataunit usando loader do application, mas o removeLoader está sendo sobrescrito.

##### Returns

Type: `Promise<void>`

#### `removeClientEvent(eventID: String) => Promise<void>`

Remove um client event do DataFetcher da aplicação.

##### Returns

Type: `Promise<void>`

#### `saveConfig(key: string, data: Object) => Promise<any>`

Salva a configuração de determinado recurso.

##### Returns

Type: `Promise<any>`

O resultado da operação de salvamento.

#### `setPopUpTitle(title: string) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `setSearchFilterContext(name: string, value: string) => Promise<void>`

Atribui valor para parâmetros de contexto no componente de pesquisa.

##### Returns

Type: `Promise<void>`

#### `showAlerts(alerts: Array<AlertItem>) => Promise<void>`

Apresenta uma lista de alertas. Geralmente é utilizado para apresentar resultados de processamentos em lote.

##### Returns

Type: `Promise<void>`

#### `showModal(content: HTMLElement) => Promise<void>`

Exibe o conteúdo passado em um Modal.

##### Returns

Type: `Promise<void>`

#### `showPopUp(content: HTMLElement, size?: "auto" | "full", useHeader?: boolean, onCloseCallback?: Function) => Promise<void>`

Exibe o conteúdo passado em um Popup.

##### Returns

Type: `Promise<void>`

#### `showScrimApp(active: boolean) => Promise<void>`

##### Returns

Type: `Promise<void>`

#### `success(title: string, message: string, icon?: string, options?: MessageOptions) => Promise<boolean>`

Exibe o diálogo de sucesso de acordo com os parâmetros passados.

##### Returns

Type: `Promise<boolean>`

#### `temOpcional(opcional: string) => Promise<boolean>`

Verifica se a licença do cliente tem determinado opcional (produto).

##### Returns

Type: `Promise<boolean>`

`true` se o cliente tiver o opcional, `false` caso contrário.

#### `updateDataunitCache(oldName: string, dataUnitName: string, dataUnit: DataUnit) => Promise<void>`

Atualiza o cache de dataunits da aplicação.

##### Returns

Type: `Promise<void>`

#### `webConnection(keyPort: string, methodName: string, params: IAppletCallerParams) => Promise<void>`

Realiza a chamada do WebConnection para realizar a exportação de arquivo.

##### Returns

Type: `Promise<void>`

#### `whenApplicationReady() => Promise<SnkApplication>`

Retorna uma promise que será resolvida quando o snk-application estiver carregado e registrado no ApplicationContext.

##### Returns

Type: `Promise<SnkApplication>`

O componente SnkApplication carregado.

### Dependencies

#### Used by

  * teste-pesquisa

#### Depends on

  * snk-pesquisa
