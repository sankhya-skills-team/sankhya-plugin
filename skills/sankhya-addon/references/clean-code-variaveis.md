# Clean Code: Boas Praticas para Criar Variaveis

## Regra de Ouro

Se voce precisa de um comentario para explicar a variavel, o nome nao esta bom.

---

## 1. Nomes Reveladores de Intencao

O nome deve responder: por que existe, o que faz e como e usada.

```java
// RUIM
int d;
String s;
List<User> list1;

// BOM
int daysSinceCreation;
String userName;
List<User> activeUsers;
```

---

## 2. Evite Desinformacao

Nao use palavras que ja tenham significado especifico ou que possam confundir.

```java
// RUIM
Set<String> accountList;    // e um Set, nao uma List
int hp;                     // hit points? horsepower? home page?
String theUser;             // artigo "the" nao agrega valor
List<Account> accountGroup; // e uma lista, nao um grupo

// BOM
Set<String> accounts;
int healthPoints;
String userName;
List<Account> activeAccounts;
```

---

## 3. Faca Distincoes Significativas

Nao adicione numeros ou palavras vazias so para diferenciar nomes.

```java
// RUIM
String userName1;
String userName2;
String userNameString;
Product productData;
Product productInfo;
Customer customerObject;

// BOM
String currentUserName;
String previousUserName;
Product product;
ProductDetails productDetails;
Customer customer;
```

---

## 4. Use Nomes Pronunciaveis

Se nao consegue pronunciar, e dificil discutir o codigo com a equipe.

```java
// RUIM
Date genymdhms;
String pszqint;
int DtaRcrd102;

// BOM
Date generationTimestamp;
String queryString;
int customerRecord;
```

---

## 5. Use Nomes Buscaveis

Variaveis com nomes de uma letra ou numeros magicos sao dificeis de localizar.

```java
// RUIM
for (int i = 0; i < 7; i++) { }

// BOM
final int DAYS_IN_WEEK = 7;
for (int dayOfWeek = 0; dayOfWeek < DAYS_IN_WEEK; dayOfWeek++) { }

int totalScore = 0;
final int NUMBER_OF_TASKS = 34;
final int MULTIPLIER = 4;
final int DIVISOR = 5;
for (int taskIndex = 0; taskIndex < NUMBER_OF_TASKS; taskIndex++) {
    totalScore += (taskScores[taskIndex] * MULTIPLIER) / DIVISOR;
}
```

Excecao: Variaveis de loop muito simples podem usar i, j, k.

---

## 6. Evite Prefixos e Notacoes Hungaras

Desnecessarios em IDEs modernas.

```java
// RUIM
String strUserName;
int iCount;
boolean bIsActive;
String m_description;
IShapeFactory factory;

// BOM
String userName;
int count;
boolean isActive;
String description;
ShapeFactory factory;
```

---

## 7. Evite Codificacao Mental

Nao force o leitor a traduzir mentalmente o que a variavel significa.

```java
// RUIM
String r;
int a;
for (String s : list) { }

// BOM
String requestUrl;
int area;
for (String userName : userNames) { }
```

---

## 8. Nomes de Variaveis Booleanas

Booleanos devem parecer perguntas de sim/nao.

```java
// RUIM
boolean flag;
boolean check;
boolean status;

// BOM
boolean isActive;
boolean hasPermission;
boolean canEdit;
boolean shouldUpdate;
boolean wasSuccessful;
```

Padroes comuns:
- is...    -> isValid, isEmpty, isEnabled
- has...   -> hasChildren, hasPermission, hasErrors
- can...   -> canExecute, canEdit, canDelete
- should.. -> shouldUpdate, shouldNotify

---

## 9. Constantes com Nomes Significativos

Evite numeros magicos. Use constantes com nomes descritivos.

```java
// RUIM
if (age > 18) { }
if (status == 1) { }
double price = quantity * 29.99;
Thread.sleep(86400000);

// BOM
private static final int MINIMUM_LEGAL_AGE = 18;
private static final int STATUS_ACTIVE = 1;
private static final double UNIT_PRICE = 29.99;
private static final long MILLISECONDS_PER_DAY = 86_400_000; // use _ para separar milhares (Java 7+)

if (age > MINIMUM_LEGAL_AGE) { }
if (status == STATUS_ACTIVE) { }
double price = quantity * UNIT_PRICE;
Thread.sleep(MILLISECONDS_PER_DAY);
```

---

## 10. Escopo da Variavel

Mantenha o escopo das variaveis o mais restrito possivel.

```java
// RUIM - variaveis de instancia usadas apenas em um metodo
public class UserService {
    private String tempName;
    private int counter;

    public void processUsers(List<User> users) {
        for (User user : users) {
            tempName = user.getName();
            counter++;
        }
    }
}

// BOM - variaveis locais ao metodo
public class UserService {
    public void processUsers(List<User> users) {
        int processedCount = 0;
        for (User user : users) {
            String userName = user.getName();
            processedCount++;
        }
    }
}
```

---

## 11. Variaveis com Um Proposito

Nao reutilize variaveis para propositos diferentes.

```java
// RUIM
int result = calculateAge(birthDate);
result = calculateSalary(hoursWorked);

// BOM
int age = calculateAge(birthDate);
double salary = calculateSalary(hoursWorked);
```

---

## 12. Colecoes: Use Plural

```java
// RUIM
List<User> userList;
Set<String> nameSet;
String[] orderArray;

// BOM
List<User> users;
Set<String> userNames;
String[] orders;

// Excecao - quando o tipo de colecao e relevante para o contexto
Map<String, User> usersByEmail;
Queue<Order> pendingOrders;
```

---

## 13. Contexto Adequado

Adicione contexto quando necessario, mas nao exagere.

```java
// Sem contexto suficiente (fora de uma classe Address)
String street;
String city;

// Contexto excessivo
String addressStreet;
String addressCity;

// BOM - use uma classe para dar contexto
public class Address {
    private String street;
    private String city;
    private String state;
    private String zipCode;
}
```

---

## 14. Evite Abreviacoes

Clareza e mais importante que brevidade.

```java
// RUIM
String usrNm;
int qty;
double amt;
String msg;
int cnt;

// BOM
String userName;
int quantity;
double amount;
String message;
int count;
```

Excecoes aceitaveis: id, url, html, acronimos conhecidos do dominio.

---

## 15. Variaveis Temporarias

Minimize o uso e use nomes descritivos. Evite temp, tmp, s.

```java
// RUIM
String temp = user.getFirstName() + " " + user.getLastName();
int tmp = calculateTotal(items);

// BOM
String fullName = user.getFirstName() + " " + user.getLastName();
int totalPrice = calculateTotal(items);

// MELHOR - evite a temporaria quando possivel
sendEmail(user.getFullName());
```

---

## 16. Convencoes de Nomenclatura Java

| Tipo                   | Convencao        | Exemplo                       |
|------------------------|------------------|-------------------------------|
| Variaveis e parametros | camelCase        | firstName, totalCount         |
| Constantes             | UPPER_SNAKE_CASE | MAX_RETRIES, DEFAULT_ENCODING |
| Classes                | PascalCase       | UserAccount, OrderProcessor   |
| Packages               | lowercase        | com.example.project.service   |

---

## Checklist

Ao criar uma variavel, verifique:

- [ ] O nome revela a intencao?
- [ ] O nome e pronunciavel?
- [ ] O nome e buscavel (nao e uma letra so)?
- [ ] Evitei desinformacao (ex: chamar Set de List)?
- [ ] Evitei prefixos desnecessarios (str, int, m_)?
- [ ] Para booleanos, usei is/has/can/should?
- [ ] Substitui numeros magicos por constantes?
- [ ] O escopo esta o mais restrito possivel?
- [ ] Usei plural para colecoes?
- [ ] Evitei abreviacoes confusas?
- [ ] Segui as convencoes de nomenclatura do Java?

---

## Exemplo Completo: Antes e Depois

```java
// RUIM
public class Proc {
    int d;
    String s;
    List<String> l1;

    public void proc(int x) {
        if (x > 18) {
            for (int i = 0; i < l1.size(); i++) {
                String temp = l1.get(i);
                if (temp.length() > 5) {
                    s += temp + " ";
                    d++;
                }
            }
        }
    }
}

// BOM
public class UserProcessor {
    private static final int MINIMUM_LEGAL_AGE = 18;
    private static final int MINIMUM_NAME_LENGTH = 5;

    private int processedUserCount;
    private String validUserNames;
    private List<String> userNames;

    public void processEligibleUsers(int userAge) {
        if (userAge < MINIMUM_LEGAL_AGE) {
            return;
        }

        for (String userName : userNames) {
            if (isValidUserName(userName)) {
                validUserNames += userName + " ";
                processedUserCount++;
            }
        }
    }

    private boolean isValidUserName(String userName) {
        return userName.length() > MINIMUM_NAME_LENGTH;
    }
}
```
