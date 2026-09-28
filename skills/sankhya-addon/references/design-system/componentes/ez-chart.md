> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chart/ (snapshot 2026-09-28)

# Chart

O componente `ez-chart` é utilizado para renderizar gráficos com base em séries de dados fornecidas. Ele permite a personalização dos gráficos através de várias propriedades, proporcionando flexibilidade para atender diferentes necessidades.

```jsx
import React, { useState } from "react";
import { EzButton, EzChart } from "@sankhyalabs/ezui/react/components";
import "./demo.css"

const Demo = () => {
    const [showLegend, setShowLegend] = useState(false);
    return (
        <div className="height-400">
            <EzChart
                chartTitle="Titulo do gráfico"
                chartSubTitle="Sub-titulo do gráfico"
                legendEnabled={showLegend}
                width={600}
                height={400}
                series={[
                    {
                        name: 'Qtd. Vendas',
                        data: [
                            { name: 'primeiro', y: 13, color: '#FF5733' },
                            { name: 'segundo', y: 7, color: '#33FF57' },
                            { name: 'terceiro', y: 18, color: '#000000' },
                            { name: 'quarto', y: 16, color: '#FF33A8' },
                            { name: 'quinto', y: 12, color: '#FFD133' },
                            { name: 'sexto', y: 10, color: '#33FFF5' },
                        ],
                        yAxis: 1,
                        type: 'column',
                        showDataLabel: true,
                    },
                    {
                        name: 'Vlr. Vendas',
                        color: '#66cc66',
                        data: [25600, 21600, 24500, 26890, 20560, 22508],
                        yAxis: 0,
                        toolTipFormatter: (serieName, xAxis, yAxis) => `<b>${serieName}</b><br/>Posição eixo X: ${xAxis}<br/>Valor no eixo Y: ${yAxis}`,
                    },
                ]}
                yAxis={[
                    {
                        text: 'Valor das vendas no semestre',
                        formatter: value => `<b>R$ ${value / 1000} mil</b>`
                    },
                    {
                        text: 'Quantidade de itens vendidos',
                        invertedPosition: true,
                    }
                ]}
                xAxis={{
                    text: 'Defina uma descrição para o eixo',
                    color: '#008561',
                    categories: ['Jan', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun']
                }}
            />
            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
                <EzButton label="Ativar Legenda" onClick={() => setShowLegend(true)} />
                <EzButton label="Desativar Legenda" onClick={() => setShowLegend(false)} />
            </div>
        </div>
    );
};

export default Demo;
```

## Alteração de largura e altura

Utilize as propriedade `width` e `height` sempre passando os valores em pixel somente números

## Como adicionar Título e Subtítulo

Utilize a propriedade `chartTitle` para definir o título que aparecerá no gráfico.

Utilize a propriedade `chartSubTitle` para definir o subtítulo que aparecerá no gráfico.

## Como Desativar as Legendas

A propriedade `legendEnabled` permite ocultar ou exibir a legenda do gráfico, que por padrão é exibida.

Importante

Gráficos ou series do `type` definido como `'pie'` ou `'donut'` não possui legenda

## Como Definir as Séries

É possível definir as `series` como um `ChartSerie` ou um `Array<ChartSerie>`.

  * Utilize a propriedade `name` para definir o nome da sua série.
  * Utilize a propriedade `color` para definir a cor da sua série.
  * Por padrão, os rótulos dos valores não são exibidos no gráfico. Use a propriedade `showDataLabel` com valor `true` para exibi-los.
  * Utilize a propriedade `type` para definir o tipo individual da série.

Importante

A propriedade **type** definida na série sobrepõe a propriedade `type` do gráfico de forma individual para cada série. Pode ser definida como `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

## Personalizar `data` de uma Série

Os dados (`data`) de uma série podem ser definidos como um array de números ou um array de objetos `ChartSerieData`.

Para detalhes específicos em cada valor da série, utilize `ChartSerieData`, definindo as propriedades `y`, `name`, e `color` (opcional).

  * A propriedade `y` é do tipo `number` e define o valor no eixo y.
  * A propriedade `name` é do tipo `string` e define um nome para o valor da série.
  * A propriedade `color` (opcional) é do tipo `string` e define uma cor para o ponto da série.

Ao visualizar o tooltip padrão, verá que ele exibe a propriedade `name` definida em cada ponto da série, com cores distintas.

## Formatar Tooltip da Série

É possível definir um tooltip personalizado para cada série através de uma função de formatação.

Na série, defina a propriedade `toolTipFormatter`, que deve ser uma função que recebe os seguintes parâmetros: `(serieName: string, xAxis: string | number, yAxis: number, dataName: string, percentage: number)` e retorna uma string HTML com a formatação desejada.

Importante

  * É necessário definir um **name** para a série, pois ele é usado para identificar o tooltip.
  * O tooltip deve ser definido individualmente para cada série que deseja personalizar.

Importante

Gráficos ou series do `type` definido como `'pie'` ou `'donut'` possui outros parametros para formatar o tooltip, vejo com detalhe na sua propria sessão

## Personalização dos Eixos

Importante

Gráficos ou series do `type` definido como `'pie'` ou `'donut'` não tuiliza a propriedade `xAxis` e `yAxis` e não possuí personalização dos eixos

É possível personalizar os eixos dos gráficos, alterando a descrição, a cor, e definindo categorias que podem ser personalizadas usando um formatter.

### Personalização da Descrição

  * Utilize a propriedade `text` para adicionar uma descrição no eixo do gráfico.
  * Utilize a propriedade `color` para alterar a cor da descrição adicionada no eixo.

### Personalização das Categorias

  * Utilize a propriedade `categories` para inserir um `Array<string>` que substitui os números por texto no eixo.
  * Utilize a propriedade `formatter` para personalizar o estilo dos valores no eixo.

### Múltiplos Eixos

Você pode criar um eixo secundário ou múltiplos eixos.

  * Passe um `Array<ChartAxis>` e defina quais séries devem usar diferentes eixos.
  * Na série, defina a propriedade `yAxis` com o índice do eixo definido.
  * Também é possível usar a propriedade `invertedPosition` para inverter a posição do eixo.

## Interação com gráfico

  * Utilize a propriedade `onEzSerieClick` chamar uma função de callback com informações da serie clicada

demo.js

```jsx
import React, { useState } from "react";
import { EzButton, EzChart } from "@sankhyalabs/ezui/react/components";
import "./demo.css"

const Demo = () => {

    const [state, setState] = useState(-1);

    const categoriesStates = ['MG', 'SP', 'RJ'];
    const categoriesCitys = [['Uberlandia', 'Belo Horizonte', 'Juiz de Fora', 'Contagem'], ['São Paulo', 'Barretos', 'Barueri', 'Riberão Preto', 'Campinas',], ['Rio de Janeiro', 'Cabo Frio', 'Duque de Caxias',]];

    const states = {
        name: 'Vendas nos Estados',
        data: [20, 32, 32]
    }
    const citys = [
        {
            name: 'Minas Gerais',
            data: [
                { name: 'Uberlandia', y: 20 },
                { name: 'Belo Horizonte', y: 32 },
                { name: 'Juiz de Fora', y: 32 },
                { name: 'Contagem', y: 32 }
            ]
        },
        {
            name: 'São Paulo',
            data: [
                { name: 'São Paulo', y: 20 },
                { name: 'Barretos', y: 32 },
                { name: 'Barueri', y: 32 },
                { name: 'Riberão Preto', y: 32 },
                { name: 'Campinas', y: 32 },
            ]
        },
        {
            name: 'Rio de Janeiro',
            data: [
                { name: 'Rio de Janeiro', y: 20 },
                { name: 'Cabo Frio', y: 32 },
                { name: 'Duque de Caxias', y: 32 },
            ]
        }
    ];

    const series = () => {
        if (state >= 0) {
            return citys[state];
        }
        return states;
    }

    return (
        <div className="height-400">
            <EzChart
                chartTitle="Interação"
                chartSubTitle="Simução de drill down"
                type="column"
                onEzSerieClick={(event) => {
                    if (state === -1) setState(event.detail.yAxis)
                }}
                series={series()}
                xAxis={{ categories: state >= 0 ? categoriesCitys[state] : categoriesStates }}
                yAxis={{ text: 'Vendas' }}
            />
            <div className="ez-flex ez-flex--justify-evenly ez-flex--align-items-center">
                {state >= 0 && <EzButton label="Voltar para estados" onClick={() => setState(-1)} />}
            </div>
        </div>
    );
};

export default Demo;
```

## Gráfico de Linha

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

## Gráfico de Coluna

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de coluna utilize o `type`: `'column'`

demo.js

```jsx
import React from "react";
import { EzChart } from "@sankhyalabs/ezui/react/components";
import "./demo.css"

const Demo = () => {

    return (
        <div className="height-400">
            <EzChart
                type="column"
                chartTitle="Titulo do gráfico coluna"
                chartSubTitle="Sub-titulo do gráfico coluna"
                series={[
                    {
                        name: 'Qtd. Vendas',
                        data: [23, 20, 22, 26, 24, 28],
                        yAxis: 1,
                        showDataLabel: true,
                    },
                    {
                        name: 'Vlr. Vendas',
                        data: [25600, 21600, 24500, 26890, 20560, 22508],
                        yAxis: 0,
                        toolTipFormatter: (serieName, xAxis, yAxis) => `<b>${serieName}</b><br/>Posição eixo X: ${xAxis}<br/>Valor no eixo Y: ${yAxis}`,
                    },
                ]}
                yAxis={[
                    {
                        text: 'Valor das vendas no semestre',
                        formatter: value => `<b>R$ ${value / 1000} mil</b>`
                    },
                    {
                        text: 'Quantidade de itens vendidos',
                        invertedPosition: true,
                    }
                ]}
                xAxis={{
                    text: 'Defina uma descrição para o eixo',
                    color: '#008561',
                    categories: ['Jan', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun']
                }}
            />
        </div>
    );
};

export default Demo;
```

## Gráfico de Linha e Coluna

Utilizando um Array de `series`, você pode criar um gráfico combinando linha e coluna, onde o `type` de uma serie deve ser `'column'` e o `type` da outra serie deve ser `'line'`

## Gráfico de Barra

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de barra utilize o `type`: `'bar'`

Importante

  * Quando definimos o tipo do gráfico como barra (`'bar'` ) os eixos são invertidos, sendo que o eixo Y fica na horizontal e o eixo X na vertical, mesmo uma serie do tipo coluna, ficaria na horizontal

demo.js

```jsx
import React from "react";
import { EzChart } from "@sankhyalabs/ezui/react/components";
import "./demo.css"

const Demo = () => {

    return (
        <div className="height-400">
            <EzChart
                type="bar"
                chartTitle="Titulo do gráfico barra"
                chartSubTitle="Sub-titulo do gráfico barra"
                series={[
                    {
                        name: 'Qtd. Vendas',
                        data: [23, 20, 22, 26, 24, 28],
                        yAxis: 1,
                        showDataLabel: true,
                    },
                    {
                        name: 'Vlr. Vendas',
                        data: [25600, 21600, 24500, 26890, 20560, 22508],
                        yAxis: 0,
                        toolTipFormatter: (serieName, xAxis, yAxis) => `<b>${serieName}</b><br/>Posição eixo X: ${xAxis}<br/>Valor no eixo Y: ${yAxis}`,
                    },
                ]}
                yAxis={[
                    {
                        text: 'Valor das vendas no semestre',
                        formatter: value => `<b>R$ ${value / 1000} mil</b>`
                    },
                    {
                        text: 'Quantidade de itens vendidos',
                        invertedPosition: true,
                    }
                ]}
                xAxis={{
                    text: 'Defina uma descrição para o eixo',
                    color: '#008561',
                    categories: ['Jan', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun']
                }}
            />
        </div>
    );
};

export default Demo;
```

## Gráfico de Pizza

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de pizza utilize o `type`: `'pie'`

Importante

  * Quando definimos o tipo do gráfico como (`'pie'` ou `'donut'` ) não é utilizado as propriedades `'xAxis'` e `'yAxis'`

Importante

Não é recomendado utilizar varias series com o `type` definido como `'pie'` pois pode haver sobreposição

A propriedade `legendEnabled` permite ocultar ou exibir a legenda do gráfico, que por padrão é exibida.

Importante

Gráficos ou series do `type` definido como `'pie'` não possui legenda

Importante

  * É interessante definir a propriedade `name` para o `data` as `series` para que seja exibido um nome para as fatias

Na série, defina a propriedade `toolTipFormatter`, que deve ser uma função que recebe os seguintes parâmetros: `(serieName: string, xAxis: string | number, yAxis: number, dataName: string, percentage: number)` e retorna uma string HTML com a formatação desejada.

## Gráfico de Donut

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de Donut utilize o `type`: `'donut'`

Importante

  * Quando definimos o tipo do gráfico como (`'pie'` ou `'donut'` ) não é utilizado as propriedades `'xAxis'` e `'yAxis'`

Importante

Não é recomendado utilizar varias series com o `type` definido como `'pie'` pois pode haver sobreposição

A propriedade `legendEnabled` permite ocultar ou exibir a legenda do gráfico, que por padrão é exibida.

Importante

Gráficos ou series do `type` definido como `'pie'` não possui legenda

Importante

  * É interessante definir a propriedade `name` para o `data` as `series` para que seja exibido um nome para as fatias

Na série, defina a propriedade `toolTipFormatter`, que deve ser uma função que recebe os seguintes parâmetros: `(serieName: string, xAxis: string | number, yAxis: number, dataName: string, percentage: number)` e retorna uma string HTML com a formatação desejada.

demo.js

```jsx
import React from "react";
import { EzChart } from "@sankhyalabs/ezui/react/components";
import "./demo.css"

const Demo = () => {

    return (
        <div className="height-400">
            <EzChart
                chartTitle="Titulo do gráfico donut"
                chartSubTitle="Sub-titulo do gráfico donut"
                type="donut"
                series={[
                    {
                        name: "Melhor grafico",
                        data: [{ name: 'Coluna', y: 13, color: '#FF5733' }, { name: 'Barra', y: 7, color: '#33FF57' }, { name: 'Pizza', y: 18, color: '#000000' }, { name: 'Donut', y: 16, color: '#FF33A8' }, { name: 'Linha', y: 12, color: '#FFD133' }],
                    },
                ]}
            />
        </div>
    );
};

export default Demo;
```
