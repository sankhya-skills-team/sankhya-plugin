# Clean Code: Boas Práticas para Criar Variáveis

## Regra de Ouro

Se você precisa de um comentário para explicar a variável, o nome não está bom.

---

## Nota sobre o Contexto Sankhya

Campos de `DynamicVO` são sempre strings em UPPER_CASE — isso é uma convenção da plataforma,
não violação de clean code:

```java
vo.asString("STATUS")      // campo JAPE — UPPER_CASE é correto
vo.asBigDecimal("NUNOTA")  // campo JAPE — UPPER_CASE é correto
```

O que **você** nomeia (variáveis Java, métodos, classes) deve seguir as regras abaixo.
Além disso, use `BigDecimal` para todos os valores numéricos do Sankhya — nunca `int`
ou `double` para IDs e valores monetários.

---

## 1. Nomes Reveladores de Intenção

O nome deve responder: por que existe, o que faz e como é usada.

```java
// RUIM
BigDecimal d;
String s;
DynamicVO vo2;

// BOM
BigDecimal nuNota;
String statusOrdem;
DynamicVO itemVO;
```

---

## 2. Evite Desinformação

Não use palavras que já tenham significado específico em Java ou no domínio Sankhya.

```java
// RUIM
List<DynamicVO> voList;      // redundante — List já diz que é lista
String notaString;           // String já é String
DynamicVO cabecalhoObject;   // Object não agrega nada

// BOM
List<DynamicVO> itensNota;
String statusNota;
DynamicVO cabecalhoVO;
```

---

## 3. Faça Distinções Significativas

Não adicione números ou palavras vazias para diferenciar.

```java
// RUIM
DynamicVO vo1;
DynamicVO vo2;
BigDecimal valor1;
BigDecimal valor2;

// BOM
DynamicVO cabecalhoVO;
DynamicVO itemVO;
BigDecimal pesoLiquido;
BigDecimal pesoBruto;
```

---

## 4. Use Nomes Pronunciáveis

Se não consegue pronunciar, é difícil discutir o código com a equipe.

```java
// RUIM
BigDecimal vlrTotCab;
String stsCdPar;
BigDecimal dtRg;

// BOM
BigDecimal valorTotalCabecalho;
String statusCodParceiro;
BigDecimal dataCadastro;
```

---

## 5. Use Nomes Buscáveis

Variáveis com nomes de uma letra ou números mágicos são difíceis de localizar.

```java
// RUIM
for (int i = 0; i < 30; i++) { }

// BOM
final int DIAS_VALIDADE_ORDEM = 30;
for (int diaProcessado = 0; diaProcessado < DIAS_VALIDADE_ORDEM; diaProcessado++) { }
```

Exceção: variáveis de loop muito simples podem usar `i`, `j`, `k`.

---

## 6. Evite Prefixos e Notações Húngaras

Desnecessários — o tipo já está declarado.

```java
// RUIM
String strStatus;
BigDecimal bdValor;
boolean bAtivo;
DynamicVO voNota;

// BOM
String status;
BigDecimal valor;
boolean ativo;
DynamicVO nota;
```

---

## 7. Evite Codificação Mental

Não force o leitor a traduzir o que a variável significa.

```java
// RUIM
String r;
BigDecimal a;
for (DynamicVO v : lista) { }

// BOM
String statusRetorno;
BigDecimal aliquotaIss;
for (DynamicVO itemVO : itensNota) { }
```

---

## 8. Nomes de Variáveis Booleanas

Booleanos devem parecer perguntas de sim/não.

```java
// RUIM
boolean flag;
boolean check;
boolean status;

// BOM
boolean notaConfirmada;
boolean temItensValidos;
boolean podeProcessar;
boolean deveRecalcularImpostos;
```

Padrões comuns:
- `is...` → `isAtivo`, `isEmpty`, `isNullOrZero`
- `has...` → `hasItens`, `hasErros`
- `can...` → `canProcessar`, `canAprovar`
- `deve...` → `deveNotificar`, `deveRecalcular`
- `foi...` → `foiConfirmada`, `foiProcessado`

---

## 9. Constantes com Nomes Significativos

Nunca use strings ou números mágicos. Use enums ou constantes.

```java
// RUIM
if ("A".equals(vo.asString("STATUS"))) { }
if ("V".equals(vo.asString("TIPMOV"))) { }
BigDecimal limite = new BigDecimal("1000.00");

// BOM — enum de status
if (StatusAmostra.APROVADO.getCodigo().equals(vo.asString("STATUS"))) { }

// BOM — constante nomeada
private static final String TIPO_MOV_VENDA = "V";
private static final BigDecimal LIMITE_APROVACAO_AUTOMATICA = new BigDecimal("1000.00");

if (TIPO_MOV_VENDA.equals(vo.asString("TIPMOV"))) { }
```

---

## 10. Escopo da Variável

Mantenha o escopo das variáveis o mais restrito possível.

```java
// RUIM — variável de instância usada só em um método
public class OrdemColetaService {
    private DynamicVO tempVO;      // variável de instância desnecessária
    private BigDecimal tempPeso;

    public BigDecimal calcularPeso(List<DynamicVO> itens) {
        tempPeso = BigDecimal.ZERO;
        for (DynamicVO item : itens) {
            tempVO = item;
            tempPeso = tempPeso.add(tempVO.asBigDecimal("PESOBRUTO"));
        }
        return tempPeso;
    }
}

// BOM — variáveis locais ao método
public class OrdemColetaService {
    public BigDecimal calcularPeso(List<DynamicVO> itens) {
        BigDecimal pesoTotal = BigDecimal.ZERO;
        for (DynamicVO item : itens) {
            BigDecimal pesoBruto = item.asBigDecimal("PESOBRUTO");
            if (!BigDecimalUtil.isNullOrZero(pesoBruto)) {
                pesoTotal = pesoTotal.add(pesoBruto);
            }
        }
        return pesoTotal;
    }
}
```

---

## 11. Variáveis com Um Propósito

Não reutilize variáveis para propósitos diferentes.

```java
// RUIM
DynamicVO vo = JapeFactory.dao(ENTIDADE_CABECALHO).findByPK(nuNota);
vo = JapeFactory.dao(ENTIDADE_ITEM).findByPK(nuNota, sequencia); // reutilizou!

// BOM
DynamicVO cabecalhoVO = JapeFactory.dao(ENTIDADE_CABECALHO).findByPK(nuNota);
DynamicVO itemVO = JapeFactory.dao(ENTIDADE_ITEM).findByPK(nuNota, sequencia);
```

---

## 12. Coleções: Use Plural

```java
// RUIM
List<DynamicVO> voList;
Collection<DynamicVO> itemCollection;

// BOM
List<DynamicVO> itensNota;
Collection<DynamicVO> ordens;
List<BigDecimal> nuNotas;
```

---

## 13. Evite Abreviações

Clareza é mais importante que brevidade.

```java
// RUIM
BigDecimal vlr;
String obs;
BigDecimal qtd;
DynamicVO cab;

// BOM
BigDecimal valor;
String observacao;
BigDecimal quantidade;
DynamicVO cabecalhoVO;
```

Exceções aceitáveis no contexto Sankhya: `nuNota`, `codEmp`, `codParc` — esses são
nomes de campos nativos do Sankhya amplamente conhecidos, não abreviações arbitrárias.

---

## 14. Convenções de Nomenclatura Java

| Tipo | Convenção | Exemplo Sankhya |
|---|---|---|
| Variáveis e parâmetros | camelCase | `nuNota`, `statusOrdem`, `pesoTotal` |
| Constantes | UPPER_SNAKE_CASE | `STATUS_PENDENTE`, `LIMITE_APROVACAO` |
| Classes | PascalCase | `OrdemColetaService`, `AmostraRepository` |
| Pacotes | lowercase sem separador | `ordemcoleta`, `registroamostra` |
| Campos JAPE (DynamicVO) | UPPER_CASE — convenção da plataforma | `"STATUS"`, `"NUNOTA"` |

---

## Checklist

Ao criar uma variável:

- [ ] O nome revela a intenção?
- [ ] O nome é pronunciável?
- [ ] Evitei desinformação (ex: chamar `Collection` de `List`)?
- [ ] Evitei prefixos desnecessários (`str`, `bd`, `vo`)?
- [ ] Para booleanos, usei `is`/`has`/`can`/`deve`/`foi`?
- [ ] Substituí strings e números mágicos por enums ou constantes?
- [ ] O escopo está o mais restrito possível?
- [ ] Usei plural para coleções?
- [ ] Evitei abreviações arbitrárias?
- [ ] Segui as convenções Java (camelCase para variáveis, UPPER_SNAKE_CASE para constantes)?
