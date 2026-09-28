> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/acorde/cores/ (snapshot 2026-09-28)

# Cores

Os tokens de cor são variáveis que definem a paleta cromática do Design System Sankhya.

Essas cores são fundamentais para garantir a consistência visual em toda a interface, assegurando uma experiência coesa e alinhada aos padrões do sistema.

## Paleta Ocean Green

O Ocean green 600 é a cor que dará vida às principais ações do sistema. Ela servirá como base para destacar botões e outros elementos importantes da interface.

| Token | Valor |
|---|---|
| --color--ocean-green-1000 | #00281D |
| --color--ocean-green-900 | #003D2D |
| --color--ocean-green-800 | #00523C |
| --color--ocean-green-700 | #00684C |
| --color--ocean-green-600 | #008561 |
| --color--ocean-green-500 | #1A9171 |
| --color--ocean-green-400 | #42A58A |
| --color--ocean-green-300 | #6BB8A3 |
| --color--ocean-green-200 | #94CCBD |
| --color--ocean-green-100 | #BDDFD6 |
| --color--ocean-green-90 | #E6F3EF |

### Boas Práticas de Utilização

  * Sempre utilize a cor base como principal referência.
  * Utilize as demais cores para composição visual, evitando aplicá-las como cores de ação.
  * Mantenha a interface limpa e equilibrada, seguindo a proporção de `20%` de cores de ação e `80%` de cores neutras.
  * Priorize as cores secundárias para fundos e underfaces, garantindo harmonia e contraste adequado.

### O que não fazer

  * Não utilize outras cores além do Ocean green 600 como cor primária.
  * Não sobrecarregue a interface com underfaces que ultrapassem `20%` da composição da tela, mantendo o equilíbrio visual.

### Percentual de aplicação de cores

Como padrão, busque manter a aplicação de cores na proporção de `20%` para a cor de ação e `80%` para cores neutras. O objetivo é garantir uma interface limpa e equilibrada. Essa proporção representa o ideal de uso, sendo o limite máximo recomendado para a aplicação da cor principal.

## Paleta Gray

Os tons de cinza podem ser usados em textos, fundos, linhas, ícones e outros elementos, desde que respeitem o contraste adequado para garantir boa visibilidade aos usuários.

| Token | Valor |
|---|---|
| --color--gray-1000 | #060607 |
| --color--gray-900 | #0B0C0E |
| --color--gray-800 | #111114 |
| --color--gray-700 | #16171B |
| --color--gray-600 | #1C1D22 |
| --color--gray-500 | #494A4E |
| --color--gray-400 | #77777A |
| --color--gray-300 | #A4A5A7 |
| --color--gray-200 | #D2D2D3 |
| --color--gray-100 | #DEDEDE |
| --color--gray-90 | #EAEAEA |
| --color--gray-80 | #F9F9F9 |
| --color--gray-70 | #FFFFFF |

### Boas Práticas de Utilização

  * Para textos sempre priorizar a utilização de cores mais escuras.
  * Evite aplicar muitas cores escuras em underfaces ou componentes. Para fundos, o ideal é manter a aplicação entre `10%` a `20%`.
  * Mantenha a interface visualmente limpa, utilizando cores neutras como base predominante.

### O que não fazer

  * Evite usar cores mais escuras para fundos de botões e componentes de ação, exceto em casos de temas ou dark mode.
  * Não aplique cores claras em elementos de leitura, onde isso possa comprometer a legibilidade para os usuários.
  * Para elementos com underface, é essencial garantir que o contraste entre o fundo e o elemento seja suficientemente perceptível.

### Percentual de aplicação de cores

Recomenda-se aplicar de 10% a 20% de tons mais escuros na interface, mantendo o restante (80%) reservado para cores neutras.

## Paleta Green

A escala de verde pretende não só sinalizar cores de sistema como também servir para compor a interface para chamadas, banners, avisos, estados, mensagens de retorno e outros.

Aqui também podemos compor underface e surface dependendo da experiência aplicada, em caso de dúvidas consulte alguém do time de Design System.

| Token | Valor |
|---|---|
| --color--green-1000 | #041800 |
| --color--green-900 | #083100 |
| --color--green-800 | #0D4900 |
| --color--green-700 | #116200 |
| --color--green-600 | #157A00 |
| --color--green-500 | #449533 |
| --color--green-400 | #73AF66 |
| --color--green-300 | #A1CA99 |
| --color--green-200 | #D0E4CC |
| --color--green-100 | #EEF9EC |

### Boas Práticas de Utilização

  * Utilize as tonalidades de verde 500 ou 600 para indicar estados de sucesso, como confirmações ou ações concluídas com êxito.
  * As tonalidades de verde mais escuras devem ser aplicadas apenas quando houver uma necessidade específica, como destacar informações ou situações que exijam maior ênfase.
  * As versões mais suaves de verde podem ser utilizadas para compor o visual geral da interface, criando áreas de destaque, componentes de interação, ou como fundo em elementos como underface e surface, mantendo a harmonia e a legibilidade.

### O que não fazer

  * Evite o uso excessivo das tonalidades de verde reservadas para feedbacks de sistema, garantindo que a cor seja aplicada apenas nas situações específicas para as quais foi designada.
  * Não utilize as tonalidades de verde do feedback de sistema como cor principal da marca. O verde de feedback não deve competir com o verde da identidade da marca, garantindo que a cor de marca seja sempre a protagonista na interface.
  * Não aplique as tonalidades de verde de feedback em botões ou interações onde a cor da marca deve ser destacada. As cores do feedback de sistema devem ser reservadas para estados informativos e não para ações de interação com o usuário.

### Percentual de aplicação de cores

Como padrão, busque manter a aplicação de cores em no máximo 20%, priorizando uma interface limpa. O restante da composição deve ser reservado para cores neutras, variando entre `80%` e `90%`.

## Paleta Yellow

A escala de amarelo procura não só sinalizar cores de sistema como também servir para compor a interface para chamadas, banners, avisos, estados, mensagens de retorno e outros.

Aqui também podemos compor underface e surface dependendo da experiência aplicada, em caso de dúvidas consulte alguém do time de Design System.

| Token | Valor |
|---|---|
| --color--yellow-1000 | #302301 |
| --color--yellow-900 | #604701 |
| --color--yellow-800 | #8F6A02 |
| --color--yellow-700 | #BF8E02 |
| --color--yellow-600 | #EFB103 |
| --color--yellow-500 | #F2C135 |
| --color--yellow-400 | #F5D068 |
| --color--yellow-300 | #F9E09A |
| --color--yellow-200 | #FCEFCD |
| --color--yellow-100 | #FAF7EE |

### Boas Práticas de Utilização

  * Utilize as tonalidades de amarelo 500 ou 600 para indicar estados de alerta, como avisos ou mensagens que chame a atenção do usuário.
  * As tonalidades de amarelo mais escuras devem ser aplicadas apenas quando houver uma necessidade específica, como destacar informações ou situações que exijam maior ênfase.
  * As versões mais suaves do amarelo podem ser utilizadas para compor o visual geral da interface, criando áreas de destaque, componentes de interação, ou como fundo em elementos como underface e surface, mantendo a harmonia e a legibilidade.

### O que não fazer

  * Evite o uso excessivo das tonalidades de amarelo reservadas para alerta de sistema, garantindo que a cor seja aplicada apenas nas situações específicas para as quais foi designada.
  * Não aplique as tonalidades de amarelo em botões ou interações onde a cor da marca deve ser destacada. As cores do feedback de sistema devem ser reservadas para estados informativos e não para ações de interação com o usuário.
  * Não é recomendado a utilização de amarelo em fundo claro como branco, o amarelo é uma cor bem próxima do branco e dependendo da tonalidade isso pode causar perda de contraste.

### Percentual de aplicação de cores

Como padrão, busque manter a aplicação de cores em no máximo 20%, priorizando uma interface limpa. O restante da composição deve ser reservado para cores neutras, variando entre 80% e 90%.

## Paleta Red

A escala de vermelho procura não só sinalizar cores de sistema como também servir para compor a interface para chamadas, banners, avisos, estados, mensagens de retorno e outros.

Aqui também podemos compor underface e surface dependendo da experiência aplicada, em caso de dúvidas consulte alguém do time de Design System.

| Token | Valor |
|---|---|
| --color--red-1000 | #260007 |
| --color--red-900 | #4C000F |
| --color--red-800 | #710016 |
| --color--red-700 | #97001E |
| --color--red-600 | #BD0025 |
| --color--red-500 | #CA3351 |
| --color--red-400 | #D7667C |
| --color--red-300 | #E599A8 |
| --color--red-200 | #F2CCD3 |
| --color--red-100 | #F9EBEE |

### Boas Práticas de Utilização

  * Utilize as tonalidades de vermelho 500 ou 600 para indicar estados de erro, como avisos ou mensagens críticas.
  * As tonalidades de vermelho mais escuras devem ser aplicadas apenas quando houver uma necessidade específica, como destacar informações ou situações que exijam maior ênfase.
  * As versões mais suaves de vermelho podem ser utilizadas para compor o visual geral da interface, criando áreas de destaque, componentes de interação, ou como fundo em elementos como underface e surface, mantendo a harmonia e a legibilidade.

### O que não fazer

  * Evite o uso excessivo das tonalidades de vermelho reservadas para feedbacks de sistema, garantindo que a cor seja aplicada apenas nas situações específicas para as quais foi designada.
  * Não aplique as tonalidades de vermelho de feedback em botões ou interações onde a cor da marca deve ser destacada. As cores do feedback de sistema devem ser reservadas para estados informativos e não para ações de interação com o usuário.

### Percentual de aplicação de cores

Como padrão, busque manter a aplicação de cores em no máximo 20%, priorizando uma interface limpa. O restante da composição deve ser reservado para cores neutras, variando entre 80% e 90%.

## Paleta Petroleum

Os tons de petróleo podem ser usados em textos, fundos, linhas, ícones e outros elementos, desde que respeitem o contraste adequado para garantir boa visibilidade aos usuários.

| Token | Valor |
|---|---|
| --color--petroleum-1000 | #0D1119 |
| --color--petroleum-900 | #141B27 |
| --color--petroleum-800 | #1B2434 |
| --color--petroleum-700 | #222D42 |
| --color--petroleum-600 | #2B3A54 |
| --color--petroleum-500 | #404E65 |
| --color--petroleum-400 | #626D80 |
| --color--petroleum-300 | #848D9C |
| --color--petroleum-200 | #A6ACB7 |
| --color--petroleum-100 | #C8CCD3 |
| --color--petroleum-90 | #EAEBEE |
| --color--petroleum-80 | #F4F6F9 |
| --color--petroleum-70 | #F4F6F9 |

### Boas Práticas de Utilização

  * Priorize sempre o uso de cores mais escuras para textos, garantindo legibilidade e contraste adequados.
  * Evite o excesso de cores escuras em underfaces ou componentes. Para fundos, o ideal é manter a aplicação entre 10% a 20%.é que seja na medida de 10% a 20%.
  * Mantenha a interface visualmente harmoniosa, utilizando cores neutras como base predominante.

### O que não fazer

  * Evite o uso de cores mais escuras para fundos de botões e componentes de ação, exceto em casos específicos, como temas ou Dark Mode.
  * Não utilize cores claras em elementos de leitura, pois isso pode comprometer a legibilidade para os usuários.
  * Garanta que o contraste entre o fundo e o elemento com underface seja suficientemente perceptível, assegurando clareza visual.

### Percentual de aplicação de cores

Como padrão, busque manter a aplicação de cores em no máximo 20%, priorizando uma interface limpa. O restante da composição deve ser reservado para cores neutras, variando entre 80% e 90%.

## Exemplos de Utilização

Os tokens de cores podem ser utilizados através das variáveis CSS, por exemplo:

```css
.elemento {
  background-color: var(--color--ocean-green-500);
  color: var(--color--petroleum-900);
}
```
