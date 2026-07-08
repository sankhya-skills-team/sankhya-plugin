# SDK Sankhya — Introdução

> **Acesso Antecipado (Beta):** Esta documentação refere-se a uma versão em acesso antecipado do SDK Sankhya. As funcionalidades e APIs estão sujeitas a modificações.

## O que é o SDK Sankhya

O SDK Sankhya é um conjunto de ferramentas para modernizar e simplificar o desenvolvimento na plataforma Sankhya. Tem forte inspiração em frameworks como **Spring** e **JPA/Hibernate**, com foco em código mais limpo, manutenível e testável.

---

## Os Quatro Pilares

### 1. Injeção de Dependências

Dependências são injetadas diretamente no **construtor** das classes. Desacopla componentes, simplifica o ciclo de vida dos objetos e facilita testes unitários com mocks.

### 2. Camada de Acesso a Dados (Data Layer)

Inspirada no Spring Data JPA. O padrão **Repository** abstrai a complexidade da persistência:
- Você define uma interface
- O SDK gera a implementação em tempo de execução
- Consultas via anotações `@Criteria` e `@Query`

### 3. Controle Transacional Declarativo

A anotação `@Transactional` gerencia o escopo de transações de banco de dados — sem controle manual. Garante atomicidade e integridade das operações.

### 4. Validação de Dados (Bean Validation)

Integra o Bean Validation (JSR 303/380). Use anotações como `@NotNull`, `@Size` e `@Email` diretamente nos DTOs ou entidades. A validação é executada automaticamente.

---

## Benefícios

| Benefício | Descrição |
|---|---|
| Curva de aprendizado reduzida | Familiaridade com Spring e JPA acelera a integração |
| Código consistente | Forma uniforme de interagir com o JAPE |
| Foco na lógica de negócio | Abstrai o boilerplate de acesso a dados |
| Alta testabilidade | Injeção de dependências permite mocks e testes isolados |
| Validação automática | Integridade dos dados de forma declarativa e reutilizável |

---

## Fonte

https://developer.sankhya.com.br/docs/introducao-sdk-sankhya
