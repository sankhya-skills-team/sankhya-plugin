# SDK Sankhya — Mapeamento Objeto-Relacional (ORM)

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## Visão Geral

O SDK oferece um ORM inspirado em JPA/Hibernate. Permite trabalhar com o banco usando POJOs e anotações, sem escrever SQL ou manipular `DynamicVO` diretamente.

---

## Mapeando Entidades

### Anotação `@JapeEntity`

```java
@JapeEntity(entity = "NomeDaEntidade", table = "NOME_DA_TABELA")
public class MinhaEntidade { }
```

### Chave Primária (`@Id`)

```java
@JapeEntity(entity = "EntidadeA", table = "TABELA_A")
public class EntidadeA {
    @Id
    @Column(name = "ID_PROJETO")
    private Long id;
}
```

### Chave Primária Composta

```java
// Passo 1: classe da chave
@Embeddable
public class ItemNotaPK implements Serializable {
    @Column(name = "NUNOTA") private Long numeroNota;
    @Column(name = "SEQUENCIA") private Integer sequencia;
    // equals() e hashCode() obrigatórios
}

// Passo 2: usar na entidade
@JapeEntity(entity = "ItemNota", table = "TGFITE")
public class ItemNota {
    @Id private ItemNotaPK id;
    @Column(name = "CODPROD") private Long codigoProduto;
}
```

### Mapeamento de Colunas (`@Column`)

```java
@Column(name = "NOME_PROJETO")
private String nome;
```

---

## Mapeando Relacionamentos

### Um-para-Muitos (`@OneToMany`)

```java
@JapeEntity(entity = "CabecalhoNota", table = "TGFCAB")
public class Pedido {
    @Id @Column(name = "NUNOTA") private Long numeroNota;

    @OneToMany(
        cascade = Cascade.ALL,
        relationship = { @Relationship(fromField = "NUNOTA", toField = "NUNOTA") }
    )
    private List<ItemPedido> itens;
}
```

Regras:
- Tipo deve ser `Collection` (`List` ou `Set`)
- Proibido usar `@Column` junto com `@OneToMany`
- NÃO use `@JoinColumn` em `@OneToMany`

### Muitos-para-Um (`@ManyToOne`)

```java
@ManyToOne
@ToString.Exclude
@JoinColumn(name = "CODGRUPOPROD", referencedColumnName = "CODGRUPOPROD", description = "Código do Grupo")
private CategoriaProduto categoria;
```

Regras:
- Obrigatório usar `@JoinColumn` ou `@JoinColumns`
- NÃO use `@Column` em relacionamentos

### Um-para-Um (`@OneToOne`)

```java
@OneToOne
@JoinColumn(name = "CODIGO_PERFIL", referencedColumnName = "CODIGO_PERFIL", description = "Código Perfil")
private PerfilUsuario perfil;
```

---

## Estratégias de Carregamento

O SDK suporta apenas **Lazy Loading**.

### Lazy em relacionamentos (`FetchType.LAZY`)

```java
@ManyToOne(fetchType = FetchType.LAZY)
@JoinColumn(name = "CODPARC", referencedColumnName = "CODPARC", description = "Código Cliente")
private Cliente cliente;
```

### Lazy em campos simples (`@Lazy`)

```java
@Lazy
@ToString.Exclude
@Column(name = "CONTEUDO")
private Text conteudoGrande;
```

Restrições:
- Não se aplica a campos `@Id` nem a relacionamentos
- Obrigatório excluir do `toString()` com `@ToString.Exclude`
- Em `@Controller`, use MapStruct para serializar campos `@Lazy` (Gson usa fields, não getters)

---

## Tipos para Campos Grandes

| DataType | Tipo Java recomendado |
|---|---|
| `TEXT_BOX` | `br.com.sankhya.sdk.data.structures.Text` |
| `FILE` | `br.com.sankhya.sdk.data.structures.Binary` |

```java
Text texto = Text.of("conteudo");
Binary binario = Binary.of(inputStream);
```

---

## Orphan Removal Strategy

| Estratégia | Descrição |
|---|---|
| `NONE` | Nenhuma ação — relacionamento intacto |
| `DETACH` | Define FK da filha como NULL, sem remover do banco |

---

## Operações em Cascata (`Cascade`)

Configuração feita via dicionário de dados (XML).

| Tipo | Descrição |
|---|---|
| `NONE` | Nenhuma operação propagada (padrão) |
| `CREATE` | Persiste filhas novas ao salvar o pai |
| `UPDATE` | Sincroniza filhas ao atualizar o pai |
| `DELETE` | Remove filhas ao excluir o pai |
| `MERGE` | Sincroniza relacionamento em ambos os sentidos |
| `ALL` | Propaga todas as operações |

---

## Boas Práticas

- Use `@ToString.Exclude` em relacionamentos bidirecionais para evitar `StackOverflowError`
- Prefira `Text` e `Binary` sobre `char[]` e `byte[]`
- Ao usar `@Lazy` em campos, sempre exclua do `toString()` e use MapStruct para serialização

---

## Fonte

https://developer.sankhya.com.br/docs/mapeamento-relacional
