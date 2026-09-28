> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/acorde/bordas/ (snapshot 2026-09-28)

# Border Radius

Os tokens de borda são utilizados para padronizar o arredondamento das bordas dos elementos, garantindo consistência visual por meio de valores predefinidos.

Disponibilizamos várias opções de densidade para bordas arredondadas, mas poucas são utilizadas no tema. As demais opções são aplicadas em casos específicos.

| Token | Valor |
|---|---|
| border--radius-0 | 0px |
| border--radius-2 | 2px |
| border--radius-4 | 4px |
| border--radius-6 | 6px |
| border--radius-8 | 8px |
| border--radius-10 | 10px |
| border--radius-12 | 12px |
| border--radius-14 | 14px |
| border--radius-16 | 16px |
| border--radius-18 | 18px |
| border--radius-20 | 20px |
| border--radius-22 | 22px |
| border--radius-24 | 24px |
| border--radius-26 | 26px |
| border--radius-28 | 28px |
| border--radius-30 | 30px |
| border--radius-32 | 32px |
| border--radius-34 | 34px |
| border--radius-36 | 36px |
| border--radius-38 | 38px |
| border--radius-40 | 40px |
| border--radius-42 | 42px |
| border--radius-44 | 44px |
| border--radius-46 | 46px |
| border--radius-48 | 48px |
| border--radius-50 | 50px |
| border--radius-52 | 52px |
| border--radius-54 | 54px |
| border--radius-56 | 56px |
| border--radius-58 | 58px |
| border--radius-60 | 60px |
| border--radius-62 | 62px |
| border--radius-64 | 64px |
| border--radius-100 | 100px |
| border--radius-200 | 200px |

## Boas Práticas de Utilização

  * Utilizar bordas de `24px`, deixa a interface mais moderna e atual, seguindo como referência outras interfaces de mercado.
  * As bordas podem variar conforme a aplicação. Em cenários com cards dentro de cards, pode ser necessário ajustar o arredondamento das bordas para uma melhor adequação visual.

## O que não fazer

  * Não mudar o padrão de `24px`, somente se for muito necessário.
  * Evite misturar muitos estilos de bordas diferentes na mesma interface.
  * Evite utilizar mais de duas variações de bordas em um mesmo layout.

## Exemplos de Utilização

```css
.elemento {
  border-radius: var(--border--radius-24);
}

.elemento-circular {
  border-radius: var(--border--radius-200);
}
```
