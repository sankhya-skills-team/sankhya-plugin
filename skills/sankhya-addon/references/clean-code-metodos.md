# Clean Code: Boas Práticas para Criar Métodos

## 1. Nomes Significativos e Descritivos

O nome do método deve expressar claramente o que ele faz. Use verbos no infinitivo para ações.

```java
// RUIM
public void proc(User u) { }
public int calc(int a, int b) { return a + b; }

// BOM
public void processUserRegistration(User user) { }
public int calculateTotalPrice(int quantity, int unitPrice) {
    return quantity * unitPrice;
}
```

---

## 2. Faça Uma Coisa Apenas (Single Responsibility)

Cada método deve ter apenas uma responsabilidade. Se você precisa usar "e" para descrever o que o método faz, ele está fazendo demais.

```java
// RUIM
public void validateAndSaveAndSendEmail(User user) {
    if (user.getEmail() == null || user.getEmail().isEmpty()) {
        throw new IllegalArgumentException("Email inválido");
    }
    userRepository.save(user);
    emailService.send(user.getEmail(), "Bem-vindo!");
}

// BOM
public void registerUser(User user) {
    validateUser(user);
    saveUser(user);
    sendWelcomeEmail(user);
}

private void validateUser(User user) {
    if (user.getEmail() == null || user.getEmail().isEmpty()) {
        throw new IllegalArgumentException("Email inválido");
    }
}

private void saveUser(User user) {
    userRepository.save(user);
}

private void sendWelcomeEmail(User user) {
    emailService.send(user.getEmail(), "Bem-vindo!");
}
```

---

## 3. Métodos Pequenos

Métodos devem ser curtos — idealmente menos de 20 linhas. Extraia responsabilidades para métodos auxiliares.

```java
// RUIM
public void processOrder(Order order) {
    // 50+ linhas: validações, cálculos, persistência, notificações, logging...
}

// BOM
public void processOrder(Order order) {
    validateOrder(order);
    calculateTotal(order);
    saveOrder(order);
    notifyCustomer(order);
    logOrderProcessed(order);
}
```

---

## 4. Poucos Parâmetros

Limite a 0–2 parâmetros. Se precisar de mais, encapsule em um objeto.

```java
// RUIM
public void createUser(String name, String email, String phone,
                       String address, String city, String state,
                       String zipCode, Date birthDate) { }

// BOM
public void createUser(UserRegistrationData registrationData) { }

public class UserRegistrationData {
    private String name;
    private String email;
    private String phone;
    private Address address;
    private Date birthDate;
    // getters e setters
}
```

---

## 5. Return Early (Retorno Antecipado)

Ao invés de ter um único ponto de retorno com condicionais aninhadas, divida o código em várias condições e **retorne imediatamente** quando uma condição é satisfeita. Isso evita estruturas de controle complexas e torna o fluxo mais fácil de seguir.

**Benefícios:**
- Melhor legibilidade — condições de saída ficam explícitas logo no início
- Redução da complexidade ciclomática
- Melhor eficiência — evita execução desnecessária de instruções
- Facilita a depuração — pontos de saída são claros e isolados

**Exemplo simples (JavaScript):**

```javascript
// RUIM
function verificarIdade(idade) {
    if (idade < 0) {
        console.log("Idade inválida");
    } else {
        if (idade < 18) {
            console.log("Acesso negado");
        } else {
            console.log("Acesso permitido");
        }
    }
}

// BOM
function verificarIdade(idade) {
    if (idade < 0) {
        console.log("Idade inválida");
        return;
    }

    if (idade < 18) {
        console.log("Acesso negado");
        return;
    }

    console.log("Acesso permitido");
}
```

**Exemplo em Java:**

```java
// RUIM
public BigDecimal calculateDiscount(Customer customer, BigDecimal amount) {
    if (customer != null) {
        if (customer.isVip()) {
            if (amount.compareTo(new BigDecimal("100")) > 0) {
                return amount.multiply(new BigDecimal("0.20"));
            } else {
                return amount.multiply(new BigDecimal("0.10"));
            }
        } else {
            return amount.multiply(new BigDecimal("0.05"));
        }
    }
    return BigDecimal.ZERO;
}

// BOM
public BigDecimal calculateDiscount(Customer customer, BigDecimal amount) {
    if (customer == null) {
        return BigDecimal.ZERO;
    }

    if (!customer.isVip()) {
        return amount.multiply(new BigDecimal("0.05"));
    }

    if (amount.compareTo(new BigDecimal("100")) > 0) {
        return amount.multiply(new BigDecimal("0.20"));
    }

    return amount.multiply(new BigDecimal("0.10"));
}
```

> **Regra de revisão de código:** O padrão Return Early deve ser exigido em revisões. Condicionais aninhadas são um sinal de que o método precisa ser refatorado.

---

## 6. Evite Efeitos Colaterais

Métodos não devem alterar estados inesperados ou ter efeitos colaterais ocultos.

```java
// RUIM
public boolean checkPassword(String password) {
    if (passwordValidator.isValid(password)) {
        session.initialize(); // efeito colateral inesperado!
        return true;
    }
    return false;
}

// BOM
public boolean checkPassword(String password) {
    return passwordValidator.isValid(password);
}

public void authenticateUser(String password) {
    if (checkPassword(password)) {
        session.initialize();
    }
}
```

---

## 7. Use Exceções ao Invés de Códigos de Erro

Retornar códigos de erro torna o código confuso. Use exceções para situações excepcionais.

```java
// RUIM
public int deleteUser(Long userId) {
    User user = userRepository.findById(userId);
    if (user == null) return -1;
    if (!user.canBeDeleted()) return -2;
    userRepository.delete(user);
    return 0;
}

// BOM
public void deleteUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));

    if (!user.canBeDeleted()) {
        throw new UserCannotBeDeletedException(userId);
    }

    userRepository.delete(user);
}
```

---

## 8. Não Repita Código (DRY)

Extraia lógica repetida para métodos reutilizáveis.

```java
// RUIM
public void processStandardOrder(Order order) {
    order.setStatus(OrderStatus.PROCESSING);
    order.setProcessedDate(LocalDateTime.now());
    orderRepository.save(order);
    logger.info("Order processed: " + order.getId());
}

public void processExpressOrder(Order order) {
    order.setStatus(OrderStatus.PROCESSING);
    order.setProcessedDate(LocalDateTime.now());
    orderRepository.save(order);
    logger.info("Order processed: " + order.getId()); // duplicado!
}

// BOM
public void processStandardOrder(Order order) {
    markOrderAsProcessed(order);
}

public void processExpressOrder(Order order) {
    markOrderAsProcessed(order);
    assignExpressShipping(order);
}

private void markOrderAsProcessed(Order order) {
    order.setStatus(OrderStatus.PROCESSING);
    order.setProcessedDate(LocalDateTime.now());
    orderRepository.save(order);
    logger.info("Order processed: " + order.getId());
}
```

---

## 9. Comentários Não Substituem Código Ruim

Se você precisa comentar o que o código faz, o código não está claro o suficiente.

```java
// RUIM
// verifica se o usuário tem mais de 18 anos
public boolean check(User u) {
    return u.getAge() >= 18;
}

// BOM
public boolean isAdult(User user) {
    final int LEGAL_AGE = 18;
    return user.getAge() >= LEGAL_AGE;
}
```

---

## 10. Mantenha o Mesmo Nível de Abstração

Não misture operações de alto nível (chamar services) com operações de baixo nível (manipular strings/HTML) no mesmo método.

```java
// RUIM
public void generateReport(List<Order> orders) {
    StringBuilder report = new StringBuilder();
    report.append("<html><body>"); // baixo nível
    BigDecimal total = calculateTotal(orders); // alto nível
    report.append("<h1>Total: ").append(total).append("</h1>"); // baixo nível
    report.append("</body></html>");
    saveReport(report.toString()); // alto nível
}

// BOM
public void generateReport(List<Order> orders) {
    BigDecimal total = calculateTotal(orders);
    String htmlContent = buildHtmlReport(total);
    saveReport(htmlContent);
}

private String buildHtmlReport(BigDecimal total) {
    return new HtmlReportBuilder()
        .addHeader("Relatório de Pedidos")
        .addTotal(total)
        .build();
}
```

---

## Checklist

Ao criar um método, pergunte-se:

- [ ] O nome deixa claro o que ele faz?
- [ ] O método faz apenas uma coisa?
- [ ] Tem menos de 20 linhas?
- [ ] Tem no máximo 2–3 parâmetros?
- [ ] Não há aninhamento excessivo de condicionais?
- [ ] Não tem efeitos colaterais inesperados?
- [ ] Usa exceções ao invés de códigos de erro?
- [ ] Não há código duplicado?
- [ ] Os comentários são realmente necessários?
- [ ] Todos os elementos estão no mesmo nível de abstração?

---

## Fonte

https://sankhya-learn.sankhya.com.br/docs/como-cria-um-metodo
