> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/acorde/espacamentos/ (snapshot 2026-09-28)

# Espaçamentos

Os tokens de espaçamento são utilizados para padronizar as distâncias entre elementos, garantindo consistência no layout por meio de valores predefinidos.

| Token | Valor |
|---|---|
| space--0 | 0px |
| space--2 | 2px |
| space--4 | 4px |
| space--6 | 6px |
| space--8 | 8px |
| space--10 | 10px |
| space--12 | 12px |
| space--14 | 14px |
| space--16 | 16px |
| space--18 | 18px |
| space--20 | 20px |
| space--22 | 22px |
| space--24 | 24px |
| space--26 | 26px |
| space--28 | 28px |
| space--30 | 30px |
| space--32 | 32px |
| space--34 | 34px |
| space--36 | 36px |
| space--38 | 38px |
| space--40 | 40px |
| space--42 | 42px |
| space--44 | 44px |
| space--46 | 46px |
| space--48 | 48px |
| space--50 | 50px |
| space--52 | 52px |

## Boas Práticas de Utilização

Tentar manter uma distância de `16px` na maioria dos casos, títulos e parágrafos, entre ícones, entre botões, entre elementos separados, porém estão dentro do mesmo contexto.

Os espaçamentos mais recomendadas, eles variam entre `16, 20, 24, 28` e `32`, conforme recomendações abaixo:

  * **Conteúdos** : Normalmente, utilizamos um espaçamento de `16` entre os conteúdos, o mesmo aplicado à distância entre ícones e imagens dentro do mesmo contexto informativo.
  * **Espaçamento entre componentes** : Geralmente, utilizamos um espaçamento entre `16` e `24`. Se a interface parecer sobrecarregada ou com muitos itens apertados, o ideal é aumentar o espaçamento para melhorar a percepção visual.
  * **Espaçamento de segurança nas laterais** : Utilizamos um espaçamento de `24` para proporcionar mais respiro ao conteúdo central, mas esse valor pode ser ajustado para maior ou menor, conforme a necessidade.
  * **Entre componentes do mesmo contexto** : Geralmente, em listas de componentes de navegação, seja horizontal ou vertical, o ideal é utilizar um espaçamento de `8` podendo variar se necessário.

## O que não fazer

  * Evite misturar distâncias inconsistentes dentro do mesmo contexto.
  * Não adicione distâncias que afastem elementos ou textos do mesmo contexto de informações.

## Exemplos de Utilização

Os tokens de espaçamentos podem ser utilizados através das variáveis CSS, por exemplo:

```css
.elemento {
  margin: var(--space--16);
  padding: var(--space--8) var(--space--16);
  gap: var(--space--8);
}
```
