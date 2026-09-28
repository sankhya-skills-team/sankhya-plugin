> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/acorde/tipografia/ (snapshot 2026-09-28)

# Tipografia

Os tokens de tipografia são utilizados para padronizar os textos e garantir consistência visual por meio de valores predefinidos para tamanho de fonte, peso, altura de linha e espaçamento entre letras.

## Fonte do Texto

O Design System utiliza a fonte `Roboto` como padrão

| Token | Valor |
|---|---|
| --font--pattern | 'Roboto' |

## Tamanho do Texto

Todos os tamanhos podem ser reutilizados para diversos objetivos. Os tamanhos de fonte variam de `8px` até `120px`.

| Token | Valor |
|---|---|
| --font-size--xxsmall | 8px |
| --font-size--xsmall | 10px |
| --font-size--small | 12px |
| --font-size--default | 14px |
| --font-size--medium | 16px |
| --font-size--large | 18px |
| --font-size--xlarge | 20px |
| --font-size--xxlarge | 22px |
| --font-size--xxxlarge | 24px |
| --font-size--4xlarge | 26px |
| --font-size--5xlarge | 28px |
| --font-size--6xlarge | 30px |
| --font-size--7xlarge | 32px |
| --font-size--8xlarge | 34px |
| --font-size--9xlarge | 36px |
| --font-size--10xlarge | 38px |
| --font-size--11xlarge | 40px |
| --font-size--12xlarge | 42px |
| --font-size--13xlarge | 44px |
| --font-size--14xlarge | 46px |
| --font-size--15xlarge | 48px |
| --font-size--16xlarge | 50px |
| --font-size--17xlarge | 60px |
| --font-size--18xlarge | 70px |
| --font-size--19xlarge | 80px |
| --font-size--20xlarge | 90px |
| --font-size--21xlarge | 100px |
| --font-size--22xlarge | 110px |
| --font-size--23xlarge | 120px |

## Parágrafos

Podemos utilizar uma escada de `8px` até `20px`, todos os tamanhos podem ser utilizados como for necessário, porém o tamanho principal para leitura é de `14px`.

### Boas Práticas de Utilização

  * Mantenha o tamanho `14px` para textos de leitura.
  * Evite excessivas variações de tamanhos de fonte na mesma interface. Quando tudo tem a mesma importância, nada se destaca. A hierarquia visual é essencial para orientar o usuário e transmitir claramente as prioridades.
  * Utilize tamanhos de fonte entre `8px` e `20px` para parágrafos. Em situações específicas, esses tamanhos também podem ser aplicados em títulos, mas prefira escolher um tamanho que realmente se destaque, assegurando clareza e hierarquia visual.

### O que não fazer

  * Evite utilizar tamanhos de fonte diferentes de `14px` para textos de leitura.
  * Um tamanho maior não garante melhor legibilidade; o padrão de `14px` já proporciona o equilíbrio ideal para uma leitura confortável.

## Títulos

Para os títulos podemos utilizar uma escada de `22px` até `44px`, todos os tamanhos podem ser utilizados como for necessário, porém o tamanho principal é `24px`.

### Boas Práticas de Utilização

  * Mantenha o tamanho `24px` para títulos.
  * Evite excessivas variações de tamanhos de fonte na mesma interface. Quando tudo tem a mesma importância, nada se destaca. A hierarquia visual é essencial para orientar o usuário e transmitir claramente as prioridades.
  * Em casos específicos, como landing pages ou situações que exigem maior destaque, podem ser utilizados tamanhos de fonte acima de `24px` para títulos

### O que não fazer

  * Evite utilizar títulos excessivamente grandes para conteúdos muito extensos. O ideal é que os títulos ocupem de `1` a `3` linhas, dependendo da largura da tela, garantindo boa legibilidade e hierarquia visual.
  * Evite usar títulos coloridos, ou seja, vários títulos de cores diferentes.

## Peso do Texto

Todos os pesos podem ser reutilizados para diversos objetivos, por padrão, o peso `regular` é o mais indicado para garantir uma leitura confortável. Ele é utilizado na maioria dos componentes e parágrafos.

| Token | Valor |
|---|---|
| --font-weight--regular | 400 |
| --font-weight--medium | 500 |
| --font-weight--semi-bold | 600 |
| --font-weight--bold | 700 |

### Boas Práticas de Utilização

  * Para garantir uma leitura mais fluida, mantenha o peso `regular` em todos os textos de leitura comum.
  * Partes dos textos podem ser marcados com `semi bold`, porém, essa aplicação não pode ser maior que o texto comum.

### O que não fazer

  * Mantenha o uso do semi-bold moderado, priorizando o peso `regular` para preservar a hierarquia e a legibilidade.
  * O uso do negrito acima de `semi bold` deve ser reservado para destacar informações essenciais, evitando sobrecarregar a interface.

## Altura da Linha

Todas as alturas podem ser reutilizados para diversos objetivos, porém existem alturas mais recomendadas, embora elas variem conforme o tamanho da tipografia, as alturas mais comuns são de `30px` e `40px` para parágrafos, e `42px` ou menor para títulos.

| Token | Valor |
|---|---|
| --line-height--16 | 16px |
| --line-height--18 | 18px |
| --line-height--20 | 20px |
| --line-height--22 | 22px |
| --line-height--24 | 24px |
| --line-height--26 | 26px |
| --line-height--28 | 28px |
| --line-height--30 | 30px |
| --line-height--32 | 32px |
| --line-height--34 | 34px |
| --line-height--36 | 36px |
| --line-height--38 | 38px |
| --line-height--40 | 40px |
| --line-height--42 | 42px |
| --line-height--44 | 44px |
| --line-height--46 | 46px |
| --line-height--48 | 48px |
| --line-height--50 | 50px |
| --line-height--52 | 52px |
| --line-height--54 | 54px |
| --line-height--56 | 56px |
| --line-height--58 | 58px |
| --line-height--60 | 60px |
| --line-height--64 | 64px |
| --line-height--68 | 68px |
| --line-height--74 | 74px |
| --line-height--78 | 78px |

### Boas Práticas de Utilização

  * Mantenha a altura da linha consistente para todos os parágrafos e títulos dentro da mesma interface.
  * Ajuste a altura da linha apenas se o espaçamento entre as linhas estiver excessivamente apertado.

### O que não fazer

  * Evite misturar várias alturas de linha na mesma interface.
  * Não deixe os textos de leitura excessivamente apertados.

## Espaçamento entre Letras

Controle do espaçamento horizontal entre caracteres:

| Token | Valor |
|---|---|
| --letter-spacing--0 | 0px |
| --letter-spacing--1 | 1px |
| --letter-spacing--2 | 2px |

## Exemplos de Utilização

Os tokens de tipografia podem ser utilizados através das variáveis CSS:

```css
.texto-padrao {
  font-family: var(--font--pattern);
  font-size: var(--font-size--default);
  font-weight: var(--font-weight--regular);
  line-height: var(--line-height--24);
  letter-spacing: var(--letter-spacing--0);
}

.titulo {
  font-size: var(--font-size--xxlarge);
  font-weight: var(--font-weight--bold);
  line-height: var(--line-height--32);
}
```
