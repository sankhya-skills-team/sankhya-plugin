# SDK Sankhya — Foreign Keys Compostas

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## O que são

Foreign Keys Compostas são chaves estrangeiras formadas por **múltiplas colunas** que referenciam uma chave primária composta de outra tabela.

---

## Sintaxe

### FK Simples (`@JoinColumn`)

```java
@ManyToOne
@JoinColumn(
    name = "CODPARC",
    referencedColumnName = "CODPARC",
    description = "Código do Parceiro"
)
private Parceiro parceiro;
```

### FK Composta (`@JoinColumns`)

```java
@ManyToOne
@JoinColumns({
    @JoinColumn(name = "NUNOTA", referencedColumnName = "NUNOTA", description = "Num. Nota"),
    @JoinColumn(name = "SEQUENCIA", referencedColumnName = "SEQUENCIA", description = "Sequência Item")
})
private ItemNota itemNota;
```

---

## Exemplos

### PK Simples referenciando PK Composta

```java
@JapeEntity(entity = "ChaveSimples", table = "TB_CHAVE_SIMPLES")
public class ChaveSimples {

    @Id
    @Column(name = "ID")
    private Long id;

    @ManyToOne
    @JoinColumns({
        @JoinColumn(name = "FK_COL1", referencedColumnName = "COL1", description = "Coluna 1"),
        @JoinColumn(name = "FK_COL2", referencedColumnName = "COL2", description = "Coluna 2")
    })
    private ChaveComposta chaveComposta;
}
```

### PK Composta referenciando PK Composta

```java
@JapeEntity(entity = "ChaveComposta2", table = "TB_CHAVE_COMPOSTA_2")
public class ChaveComposta2 {

    @Id
    private ChaveComposta2Id id;

    @ManyToOne
    @JoinColumns({
        @JoinColumn(name = "FK_TB1_COL1", referencedColumnName = "COL1", description = "FK Col1"),
        @JoinColumn(name = "FK_TB1_COL2", referencedColumnName = "COL2", description = "FK Col2")
    })
    private ChaveComposta1 chaveComposta1;
}
```

---

## Boas Práticas

- Use nomes descritivos nas colunas FK (ex: `CODEMP_CONTRATO` em vez de `EMP`)
- Mantenha a mesma ordem de colunas em `@JoinColumns` e `@Embeddable`
- Prefira `Cascade.CREATE` e `Cascade.MERGE` em vez de `Cascade.ALL`

---

## Fonte

https://developer.sankhya.com.br/docs/foreign-keys-compostas
