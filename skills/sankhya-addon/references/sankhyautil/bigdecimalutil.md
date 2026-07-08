# BigDecimalUtil

**Pacote:** `com.sankhya.util.BigDecimalUtil`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.BigDecimalUtil;
import java.math.BigDecimal;
```

---

## Constantes

```java
BigDecimalUtil.ZERO_VALUE  // BigDecimal.ZERO (reutilizar sem criar nova instância)
BigDecimalUtil.CEM_VALUE   // BigDecimal(100)
```

---

## Null-safe: obter valor

```java
// retorna zero se null
BigDecimal val  = BigDecimalUtil.getValueOrZero(vo.asBigDecimal("VLRTOTAL"));

// retorna default se string inválida/nula
BigDecimal val2 = BigDecimalUtil.strToBigDecimalDef(texto, BigDecimal.ZERO);
```

---

## Verificações

```java
boolean vazio    = BigDecimalUtil.isEmpty(bd);      // null ou zero
boolean nulZero  = BigDecimalUtil.isNullOrZero(bd); // mesma semântica que isEmpty
boolean iguais   = BigDecimalUtil.safelyEquals(a, b); // null-safe comparison
```

---

## Construção a partir de tipos primitivos

```java
// double/Number — usa BigDecimal.valueOf internamente (evita imprecisão de float)
BigDecimal bd1 = BigDecimalUtil.buildFromDouble(3.14);
BigDecimal bd2 = BigDecimalUtil.buildFromDouble((Number) minhaVariavel);

// valueOf — sobrecargas
BigDecimal bd3 = BigDecimalUtil.valueOf(3.14);        // double
BigDecimal bd4 = BigDecimalUtil.valueOf(100L);        // long
BigDecimal bd5 = BigDecimalUtil.valueOf("1234.56");   // String

// a partir de Object genérico (DynamicVO, ResultSet, etc.)
BigDecimal bd6 = BigDecimalUtil.getBigDecimal(objeto);
```

---

## Arredondamento

```java
// HALF_UP (padrão fiscal/contábil)
BigDecimal arr1 = BigDecimalUtil.getRounded(valor, 2);           // BigDecimal
BigDecimal arr2 = BigDecimalUtil.getRounded(3.145, 2);           // double

// HALF_DOWN
BigDecimal arr3 = BigDecimalUtil.getRoundedHalfDown(valor, 4);

// Arredondamento para baixo (truncar)
BigDecimal trunc1 = BigDecimalUtil.truncate(valor, 2);           // BigDecimal
BigDecimal trunc2 = BigDecimalUtil.truncate(3.999, 2);           // → 3.99

// truncar usando regra MGE (específica Sankhya)
BigDecimal truncMGE = BigDecimalUtil.truncateMGE(valor, 4);
```

---

## Divisão segura

```java
import java.math.MathContext;

// divide sem ArithmeticException se divisor = zero
BigDecimal res = BigDecimalUtil.safetyDivision(numerador, denominador, MathContext.DECIMAL128);

// divide com scale padrão (throws ArithmeticException se zero — use com validação)
BigDecimal res2 = BigDecimalUtil.divide(numerador, denominador);
BigDecimal res3 = BigDecimalUtil.divide(numerador, denominador, 4); // 4 casas decimais
```

---

## Porcentagem

```java
// calcula percentual: (valor * percentual) / 100
BigDecimal resultado = BigDecimalUtil.porcentagem(valor, BigDecimal.valueOf(10)); // 10%
BigDecimal res2      = BigDecimalUtil.porcentagem(valor, pct, MathContext.DECIMAL128);
```

---

## Min/Max null-safe

```java
BigDecimal maior = BigDecimalUtil.max(a, b); // null-safe
BigDecimal menor = BigDecimalUtil.min(a, b); // null-safe
int menorInt     = BigDecimalUtil.min(x, y); // int overload
```

---

## Formatação

```java
// formata como moeda (2 casas, separador padrão Locale)
String moeda1 = BigDecimalUtil.toCurrency(valor);         // "1.234,56"
String moeda2 = BigDecimalUtil.formatCurrency(valor, 4);  // 4 casas decimais
```

---

## Antipadrões

```java
// ERRADO — double direto no construtor
new BigDecimal(3.14)  // imprecisão de ponto flutuante
// CORRETO
BigDecimalUtil.buildFromDouble(3.14)  // usa BigDecimal.valueOf internamente

// ERRADO — divisão sem proteção
valor.divide(divisor)  // ArithmeticException se divisor = 0
// CORRETO
if (BigDecimalUtil.isEmpty(divisor)) {
    throw new MGEModelException("Divisor não pode ser zero.");
}
BigDecimal res = BigDecimalUtil.divide(valor, divisor);
// OU usar safetyDivision que retorna zero automaticamente
BigDecimal res = BigDecimalUtil.safetyDivision(valor, divisor, MathContext.DECIMAL128);

// ERRADO — comparação com ==
if (valor == BigDecimal.ZERO) { ... }
// CORRETO
if (BigDecimalUtil.isEmpty(valor)) { ... }
// ou
if (BigDecimalUtil.safelyEquals(valor, BigDecimal.ZERO)) { ... }
```
