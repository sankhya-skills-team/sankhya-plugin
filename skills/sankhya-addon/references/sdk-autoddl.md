# SDK Sankhya — AutoDD e AutoDDL

> **Acesso Antecipado (Beta):** APIs sujeitas a modificações.

## O que são

- **AutoDD**: Gera o dicionário de dados XML automaticamente a partir das entidades Java anotadas com `@JapeEntity`
- **AutoDDL**: Converte o XML do dicionário de dados em scripts DDL (`CREATE`/`ALTER`) para Oracle e MSSQL

São complementares: AutoDD elimina a criação manual do XML; AutoDDL elimina a conversão manual do XML em DDL.

> O AutoDD é focado exclusivamente em `Table` e `NativeTable`. Views, menus, dashboards, filtros etc. ainda precisam ser mapeados manualmente.

---

## Habilitando

```groovy
// build.gradle (raiz do projeto)
addon {
    autoDD = true
    autoDDL = true
}
```

---

## Como Funciona

1. Defina a entidade com `@JapeEntity` e anotações de campo
2. Execute o build (`./gradlew clean deployAddon`)
3. O AutoDD processa as entidades e gera o XML do dicionário de dados
4. (Se AutoDDL habilitado) O XML é convertido em scripts SQL para Oracle/MSSQL

---

## Exemplos

### Entidade Simples

```java
@Data
@NoArgsConstructor
@JapeEntity(entity = "TST_MinhaClasse", table = "TST_MINHA_CLASSE", description = "Minha Classe Exemplo")
public class MinhaClasse {

    @Id
    @GeneratedValue(strategy = GeneratedValue.GenerationType.AUTO)
    @Column(name = "ID", dataType = DataType.INTEGER, description = "Id")
    private Long id;

    @Column(name = "MSG", dataType = DataType.TEXT, description = "Mensagem")
    private String mensagem;
}
```

### Entidades com Relacionamentos

```java
@JapeEntity(entity = "TST_MinhaClasse", table = "TST_MINHA_CLASSE", description = "Minha Classe")
public class MinhaClasse {

    @Id
    @GeneratedValue(strategy = GeneratedValue.GenerationType.AUTO)
    @Column(name = "ID", dataType = DataType.INTEGER, description = "Id")
    private Long id;

    @OneToMany(cascade = Cascade.ALL, orphanRemovalStrategy = OrphanRemovalStrategy.DETACH)
    private List<MinhaOutraClasse> itens;
}

@JapeEntity(entity = "TST_MinhaOutraClasse", table = "TST_MINHA_OUTRA_CLASSE", description = "Outra Classe")
public class MinhaOutraClasse {

    @Id
    @GeneratedValue(strategy = GeneratedValue.GenerationType.AUTO)
    @Column(name = "ID", dataType = DataType.INTEGER, description = "Id")
    private Long id;

    @Column(
        name = "STATUS",
        dataType = DataType.LIST,
        description = "Status",
        options = {
            @Option(label = "Ativo", value = "ATIVO"),
            @Option(label = "Inativo", value = "INATIVO")
        }
    )
    private Status status;

    @ManyToOne(cascade = Cascade.MERGE)
    @JoinColumn(name = "MINHA_ENTIDADE_ID", referencedColumnName = "ID",
                dataType = DataType.INTEGER, description = "Referência para MinhaClasse")
    private MinhaClasse minhaClasse;
}
```

### Tabela/Instância Nativa

```java
@JapeEntity(
    entity = "TST_InstanciaCustomizadaUsuarios",
    table = "TSIUSU",
    description = "Instância Customizada de Usuários",
    isNativeTable = true,
    isNativeInstance = false
)
public class InstanciaCustomizadaUsuarios {

    @Id
    @Column(name = "CODUSU", description = "Código do Usuário", dataType = DataType.INTEGER)
    private Long codUsuario;

    @Column(name = "NOMUSU", description = "Nome do Usuário", dataType = DataType.TEXT)
    private String nomeUsuario;
}
```

---

## Boas Práticas

- Use prefixos exclusivos para tabelas e entidades (ex: `SGT_`, `LOG_`)
- Nunca use o prefixo `AD_` — reservado pelo sistema
- Sempre revise os scripts DDL gerados antes de aplicar em produção

---

## Fonte

https://developer.sankhya.com.br/docs/autodd-gera%C3%A7%C3%A3o-autom%C3%A1tica-do-dicion%C3%A1rio-de-dados-data-dictionary
