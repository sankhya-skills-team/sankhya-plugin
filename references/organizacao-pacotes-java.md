# Organização de Pacotes Java

**Subtítulo:** A Importância do Contexto de Projeto na Organização de Pacotes Java

---

## O Problema: Conflitos de ClassLoader

Ao desenvolver algum módulo, micromódulo, ou addons para integrar o SankhyaOm, é necessário atenção para um problema comum e muitas vezes subestimado que é o **conflito de classes** causado pela organização inadequada de pacotes.

### Exemplo do Problema

Considere a seguinte estrutura de pacotes:

```java
// ❌ Organização INCORRETA
package br.com.sankhya.services;

public class NotificationService {
    // implementação do módulo financeiro
}
```

```java
// ❌ Organização INCORRETA (outro módulo)
package br.com.sankhya.services;

public class NotificationService {
    // implementação do módulo comercial
}
```

### Por Que Isso é um Problema?

Quando utilizamos **ClassLoaders** para carregar dinamicamente classes de diferentes módulos, o sistema registra as classes por seu **nome completo qualificado** (Fully Qualified Name - FQN):

```
br.com.sankhya.services.NotificationService
```

Se dois ou mais módulos registrarem classes com o **mesmo pacote** e o **mesmo nome**, temos um **conflito de ClassLoader**:

- ⚠️ Comportamento imprevisível
- ⚠️ A classe carregada pode não ser a real
- ⚠️ Dificuldade em debugar qual implementação está sendo executada
- ⚠️ Problemas de versionamento e compatibilidade

---

## A Solução: Contexto de Projeto no Pacote

A solução é simples e eficaz: **incluir o contexto/nome do projeto na estrutura de pacotes**.

### Exemplo Correto

```java
// ✅ Organização CORRETA
package br.com.sankhya.mgefin.services;

public class NotificationService {
    // implementação do módulo de financeiro
}
```

```java
// ✅ Organização CORRETA (outro módulo)
package br.com.sankhya.mgecom.services;

public class NotificationService {
    // implementação do módulo comercial
}
```

Agora temos nomes completos únicos:

- `br.com.sankhya.mgefin.services.NotificationService`
- `br.com.sankhya.mgecom.services.NotificationService`

---

## Benefícios desta Abordagem

### 1. Isolamento de Módulos
Cada módulo possui seu próprio namespace, evitando colisões.

### 2. Clareza e Manutenibilidade
Fica evidente a qual contexto/módulo cada classe pertence.

```java
// Ao ler o import, já sabemos o contexto
import br.com.sankhya.mgefin.services.ProductService;
import br.com.sankhya.mgecom.services.ProductService;
```

### 3. Facilita o Debug
Logs e stack traces mostram claramente qual módulo está executando:

```
[ERROR] br.com.sankhya.mgefin.services.PaymentService - Erro ao processar pagamento
```

### 4. Permite Coexistência de Versões
Diferentes versões ou implementações podem coexistir sem conflitos.

### 5. Melhora a Arquitetura
Força uma organização mais clara e modular do código.

---

## Padrão Recomendado de Mercado

### Estrutura Padrão

```
br.com.{empresa}.{contexto_projeto}.{camada}.{funcionalidade}
```

**Onde:**

- `{empresa}`: Domínio reverso da organização (ex: `sankhya`)
- `{contexto_projeto}`: Identificador único do módulo/projeto (ex: `mgefin`, `mgecom`, `mgepes`)
- `{camada}`: Camada arquitetural (ex: `services`, `controllers`, `repositories`, `models`, `util`)
- `{funcionalidade}`: Nome descritivo da funcionalidade/domínio (ex: `faturamento`, `estoque`, `rh`)

### Exemplos Práticos

```
✅ br.com.sankhya.mgefin.services.CustomerService
✅ br.com.sankhya.mgefin.faturamento.controllers.InvoiceController
✅ br.com.sankhya.mgecom.estoque.repositories.ProductRepository
✅ br.com.sankhya.mgepes.rh.models.Employee
```

> **📚 Referência**: Esta convenção segue as recomendações do Oracle Java Package Naming Conventions e padrões de modularização como Java Platform Module System (JPMS), garantindo unicidade e evitando conflitos de namespace em sistemas modulares.

---

## Impacto no Registro de ClassLoader

Quando registramos ClassLoader com suas classes no ClasspathUtils, a estrutura de pacotes influencia diretamente na forma como as classes são identificadas e carregadas.

### ❌ Erro que acontece — pacotes iguais para classes diferentes

```java
ClassLoader clMgefin
//[br.com.sankhya.services.NotificationService,...]
ClassLoader clMgecom
//[br.com.sankhya.services.NotificationService,...]
```

No warmup de cada módulo é registrado o classloader:

```java
ClasspathUtils.registryLoockupClassloader("mgefin", clMgefin);
ClasspathUtils.registryLoockupClassloader("mgecom", clMgecom);
```

Qual classe será retornada, mgefin ou mgecom? 🤔

```java
ClasspathUtils.getClassFromContextClassLoader('br.com.sankhya.services.NotificationService');
```

### ✅ SEM CONFLITO — chaves únicas

```java
ClassLoader clMgefin
//[br.com.sankhya.mgefin.services.NotificationService,...]
ClassLoader clMgecom
//[br.com.sankhya.mgecom.services.NotificationService,...]
```

No warmup de cada módulo é registrado o classloader:

```java
ClasspathUtils.registryLoockupClassloader("mgefin", clMgefin);
ClasspathUtils.registryLoockupClassloader("mgecom", clMgecom);
```

A classe que será retornada é a correta do mgefin sem conflitos: 😀

```java
ClasspathUtils.getClassFromContextClassLoader('br.com.sankhya.mgefin.services.NotificationService');
```

---

## Conclusão

A inclusão do **contexto de projeto na estrutura de pacotes** não é apenas uma boa prática de organização – é uma **necessidade técnica** em sistemas que utilizam:

- ✓ Múltiplos módulos integrados que utilizam classes de outros classpath

**Regra de ouro**: Sempre use `br.com.sankhya.{contexto}.{camada}` ao invés de `br.com.sankhya.{camada}`

Isso garantirá:

- 🎯 Zero conflitos de ClassLoader
- 🎯 Código mais organizado e manutenível
- 🎯 Facilidade para debugar e rastrear problemas
- 🎯 Escalabilidade do sistema

---

*Fonte: Sankhya Learn — Padrões de Código para SankhyaW*