# Como utilizar o Lombok de forma efetiva em seus projetos em Java

**Fonte:** Sankhya Learn — Desenvolvimento
**URL:** https://sankhya-learn.sankhya.com.br/docs/como-utilizar-o-lombok
**Atualizado:** 6 months ago (referência: novembro 2025)

---

O [Lombok](https://projectlombok.org) é uma biblioteca poderosa que pode ajudar a reduzir a quantidade de código boilerplate em aplicações Java. A seguir, algumas dicas sobre como utilizá-lo de forma eficiente.

---

## 1. Instalação do Lombok

Para começar a usar o Lombok, você deve adicioná-lo ao seu projeto. Se estiver usando Maven, adicione a seguinte dependência ao seu arquivo `build.gradle`:

```groovy
dependencies {
    compileOnly 'org.projectlombok:lombok:1.18.24'
    annotationProcessor 'org.projectlombok:lombok:1.18.24'
}
```

---

## 2. Anotações comuns e mais utilizadas do Lombok

O Lombok oferece várias anotações úteis que ajudam a reduzir o código:

- **`@Getter` e `@Setter`**: Gera métodos getters e setters automaticamente.

```java
@Getter @Setter
private String nome;
```

- **`@AllArgsConstructor` e `@NoArgsConstructor`**: Cria construtores automaticamente.

```java
@AllArgsConstructor
public class Pessoa {
    private String nome;
    private int idade;
}
```

- **`@Builder`**: Permite usar o padrão Builder para criar objetos de forma fluente.

```java
@Builder
public class Produto {
    private String nome;
    private double preco;
}
```

- **`@Data`**: Combina várias anotações comuns (`@Getter`, `@Setter`, `@ToString`, `@EqualsAndHashCode`, e `@RequiredArgsConstructor`) em uma única anotação.

```java
@Data
public class Cliente {
    private final String id;
    private String nome;
}
```

---

## 3. Anotações avançadas utilizadas do Lombok

### `@Cleanup`

É utilizada para gerenciar recursos automaticamente, garantindo que o método `close()` seja chamado quando uma instância da classe sair do escopo. Isso é útil para classes que implementam `AutoCloseable` ou `Closeable`, e ajuda a evitar vazamentos de recursos (como conexões de banco de dados ou arquivos).

#### Exemplo de Uso:

```java
import lombok.Cleanup;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ExemploCleanup {
    public static void main(String[] args) {
        @Cleanup // O BufferedReader será fechado automaticamente
        BufferedReader reader = new BufferedReader(new FileReader("arquivo.txt"));

        String linha;
        while ((linha = reader.readLine()) != null) {
            System.out.println(linha);
        } // Não é necessário chamar reader.close()
    }
}
```

---

### `@Synchronized`

Permite que você crie um bloqueio de sincronização em um método, que é uma alternativa mais segura à palavra-chave `synchronized` do Java. Ela evita a exposição da instância de bloqueio, evitando problemas de deadlocks e garantias de thread safety. O enfoque é que o bloqueio não deve ser exposto ao mundo externo, garantindo assim que o controle de sincronização permaneça seguro.

#### Exemplo de Uso:

```java
import lombok.Synchronized;

public class Contador {
    private int contador = 0;

    @Synchronized // Garante que apenas uma thread consiga acessar este método de cada vez
    public void incrementar() {
        contador++;
    }

    @Synchronized // Garante que apenas uma thread consiga acessar este método de cada vez
    public int getContador() {
        return contador;
    }

    public static void main(String[] args) {
        Contador contador = new Contador();

        // Criando várias threads que incrementam o contador
        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementar();
            }
        });

        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementar();
            }
        });

        // Iniciar as threads
        thread1.start();
        thread2.start();

        try {
            // Espera até que as duas threads terminem
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Obtendo o valor final do contador
        System.out.println("Valor final do contador: " + contador.getContador()); // Saída esperada: 2000
    }
}
```

**Segurança:** O uso de `@Synchronized` evita problemas comuns de concorrência, como race conditions, garantindo que o código que modifica o estado interno da classe (como o contador) seja acessado por apenas uma thread de cada vez.

---

### `@SneakyThrows`

Permite que você lance exceções sem a necessidade de declará-las ou capturá-las em um bloco try-catch. Essa anotação é útil em situações onde você deseja simplificar a assinatura de métodos ou evitar a propagação de checked exceptions, tornando a API mais limpa. No entanto, deve ser usada com **cautela**, pois pode obscurecer o tratamento de exceções.

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import lombok.SneakyThrows;

public class ExemploComSneakThrows {

    @SneakyThrows // Permite lançar IOException e SQLException sem declaração explícita
    public void realizarOperacoes(String caminhoArquivo) {
        // Lendo um arquivo
        BufferedReader reader = new BufferedReader(new FileReader(caminhoArquivo));
        String linha;
        try {
            while ((linha = reader.readLine()) != null) {
                System.out.println(linha);
            }
        } finally {
            reader.close(); // Importante fechar o recurso
        }

        // Conectando ao banco de dados
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/exemplo", "usuario", "senha");
        // Aqui você executaria operações no banco de dados
        conn.close(); // Caso você não esteja usando um pool de conexões, feche a conexão
    }

    public static void main(String[] args) {
        ExemploComSneakThrows exemplo = new ExemploComSneakThrows();
        exemplo.realizarOperacoes("arquivo.txt"); // Chamamos sem necessidade de blocos try-catch para tratamento
    }
}
```

---

### `@Delegate`

Permite que você delegue chamadas de método de uma classe para um objeto interno. Isso pode ajudar a simplificar a implementação de padrões de design que envolvem composição.

#### Exemplo de Uso

Suponha que você tenha uma classe `Endereco` que possui alguns métodos, e uma classe `Cliente` que deve delegar certas funcionalidades para a classe `Endereco`.

```java
import lombok.Data;
import lombok.experimental.Delegate;

@Data
class Endereco {
    private String rua;
    private String cidade;

    public void mostrarEndereco() {
        System.out.println("Endereço: " + rua + ", " + cidade);
    }
}

@Data
class Cliente {
    @Delegate
    private Endereco endereco = new Endereco();

    private String nome;
}

public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setNome("João");
        cliente.setRua("Rua A");
        cliente.setCidade("Cidade B");

        // Chamando método delegado
        cliente.mostrarEndereco(); // Saída: Endereço: Rua A, Cidade B
    }
}
```

---

### `@Builder.Default`

Permite que você declare um valor padrão para um campo de classe. Se o usuário do Builder não fornecer um valor para esse campo, o valor padrão especificado será utilizado.

#### Exemplos de Uso

```java
import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
public class Produto {
    @Builder.Default
    private String nome = "Produto Padrão"; // Valor padrão para o nome

    @Builder.Default
    private double preco = 0.0; // Valor padrão para o preço

    @Builder.Default
    private boolean emEstoque = true; // Valor padrão para disponibilidade
}
```

Quando instâncias da classe `Produto` são criadas usando `Produto.builder()`, se um campo não for especificado no Builder, o valor padrão será utilizado:

```java
Produto produto1 = Produto.builder().build();
System.out.println(produto1.getNome()); // Saída: Produto Padrão
System.out.println(produto1.getPreco()); // Saída: 0.0
System.out.println(produto1.isEmEstoque()); // Saída: true
```

Você pode substituir o valor padrão ao especificar um valor no método Builder:

```java
Produto produto2 = Produto.builder().nome("Produto Especial").preco(15.99).build();
System.out.println(produto2.getNome()); // Saída: Produto Especial
System.out.println(produto2.getPreco()); // Saída: 15.99
System.out.println(produto2.isEmEstoque()); // Saída: true (valor padrão não alterado)
```

---

## 4. Mantenha a clareza no código

Embora Lombok possa reduzir a quantidade de código, é importante não abusar dele. Use anotações de forma judiciosa para garantir que o código permaneça legível e mantenha a clareza, ou seja saiba como utilizar as anotações, pois é código desperdiçado que esta sendo gerado.

---

## 5. Integração com IDE

Certifique-se de que sua IDE está configurada para suportar Lombok. Para o IntelliJ IDEA, você pode instalar o plugin Lombok. No Eclipse, você também pode habilitar o suporte ao Lombok.

---

## 6. Teste com cuidado

Ao usar Lombok, faça testes cuidadosos para garantir que os métodos gerados funcionem como esperado. Em caso de dúvidas, verifique a documentação do Lombok para entender como suas anotações afetam o comportamento do seu código.

---

## Conclusão 🤓 🖖

O Lombok pode ser uma ferramenta extremamente útil para simplificar o desenvolvimento em Java. Ao usar as anotações apropriadas, você pode reduzir a quantidade de código boilerplate e manter seu projeto mais limpo e gerenciável.

---

## Resumo das Anotações

| Anotação | Categoria | Descrição |
|---|---|---|
| `@Getter` / `@Setter` | Comum | Gera getters e setters automaticamente |
| `@AllArgsConstructor` / `@NoArgsConstructor` | Comum | Cria construtores automaticamente |
| `@Builder` | Comum | Padrão Builder para criação fluente de objetos |
| `@Data` | Comum | Combina `@Getter`, `@Setter`, `@ToString`, `@EqualsAndHashCode`, `@RequiredArgsConstructor` |
| `@Cleanup` | Avançada | Fecha recursos automaticamente ao sair do escopo |
| `@Synchronized` | Avançada | Sincronização thread-safe sem expor o lock |
| `@SneakyThrows` | Avançada | Lança checked exceptions sem declaração explícita (usar com cautela) |
| `@Delegate` | Avançada | Delega chamadas de método para objeto interno (composição) |
| `@Builder.Default` | Avançada | Define valor padrão para campos em classes com `@Builder` |
