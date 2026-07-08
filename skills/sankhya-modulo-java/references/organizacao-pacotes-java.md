# Organização de Pacotes Java

## O Problema: Conflitos de ClassLoader

Quando múltiplos JARs são implantados no mesmo servidor Sankhya OM, o ClassLoader registra
as classes pelo **nome completo qualificado (FQN)**. Se dois JARs de demandas diferentes
declararem a mesma classe no mesmo pacote, o comportamento é imprevisível — a classe carregada
pode ser a errada, sem erro visível.

### Exemplo do problema

Duas demandas implantadas no mesmo servidor, ambas com um `OrdemService`:

```java
// ❌ ERRADO — demanda "ordemcoleta"
package br.com.sankhya.dstech.service;

public class OrdemService { ... }
```

```java
// ❌ ERRADO — demanda "ordemvenda"
package br.com.sankhya.dstech.service;

public class OrdemService { ... }  // mesmo FQN!
```

FQN gerado em ambos: `br.com.sankhya.dstech.service.OrdemService`

Quando o servidor carrega o segundo JAR, a classe já está registrada. A demanda `ordemvenda`
pode executar silenciosamente a lógica de `ordemcoleta`.

---

## A Solução: Segmento de Demanda no Pacote

O pacote raiz do DSTech é `br.com.sankhya.dstech`. Cada demanda **deve** ter seu próprio
segmento como parte do pacote:

```
br.com.sankhya.dstech.{nomedemanda}.{camada}
```

```java
// ✅ CORRETO — demanda "ordemcoleta"
package br.com.sankhya.dstech.ordemcoleta.service;

public class OrdemService { ... }
// FQN: br.com.sankhya.dstech.ordemcoleta.service.OrdemService
```

```java
// ✅ CORRETO — demanda "ordemvenda"
package br.com.sankhya.dstech.ordemvenda.service;

public class OrdemService { ... }
// FQN: br.com.sankhya.dstech.ordemvenda.service.OrdemService
```

Zero conflito — FQNs únicos.

---

## Estrutura Padrão do Projeto

```
br.com.sankhya.dstech.
  {nomedemanda}/          ← substituir pelo nome real (ex: ordemcoleta, registroamostra)
    actionbutton/
    component/
    controller/
    enums/
    event/
    exception/
    dto/
    job/
    regra/
    repository/
    service/
    helper/
    utils/                ← DwfUtils, MessageUtils — dentro da demanda
```

O segmento `nomedemanda` é o que garante o isolamento entre demandas.

---

## Antipadrão: Classes "Comuns" sem Segmento de Demanda

Um erro frequente é criar classes compartilhadas diretamente sob `br.com.sankhya.dstech`:

```java
// ❌ ERRADO — direto sob dstech, sem demanda
package br.com.sankhya.dstech.service;
public class NotaService { ... }

// ❌ ERRADO
package br.com.sankhya.dstech.repository;
public class ParceirRepository { ... }
```

Se outro JAR tiver uma classe com o mesmo nome nesse pacote, conflito garantido.

**Exceção legítima:** `br.com.sankhya.dstech.utils` — utilitários genuinamente transversais
a todas as demandas (`DwfUtils`, `MessageUtils`, `PopUpBuilder`). Mas mesmo esses devem ter
nomes suficientemente específicos para evitar colisão.

---

## Convenção de Nomeação

| Segmento | Regra | Exemplo |
|---|---|---|
| `{nomedemanda}` | lowercase, sem separador, nome do módulo | `ordemcoleta`, `registroamostra`, `contratos` |
| `{camada}` | lowercase, nome da camada | `service`, `repository`, `event`, `actionbutton` |
| Classes | PascalCase com sufixo da camada | `OrdemColetaService`, `OrdemColetaRepository` |

---

## Por que o Sufixo da Camada Importa

Mesmo com pacotes corretos, classes com nomes genéricos dentro de uma demanda podem
gerar confusão em logs e stack traces:

```java
// RUIM — o que é "Service" no stack trace?
package br.com.sankhya.dstech.ordemcoleta.service;
public class Service { ... }

// BOM — contexto imediato no stack trace
package br.com.sankhya.dstech.ordemcoleta.service;
public class OrdemColetaService { ... }
// Stack trace: "...ordemcoleta.service.OrdemColetaService.validar(..."
```

---

## Regra de Ouro

> Nunca declare classes diretamente em `br.com.sankhya.dstech.{camada}`.
> Sempre use `br.com.sankhya.dstech.{nomedemanda}.{camada}`.

Isso garante zero conflito de ClassLoader entre demandas implantadas no mesmo servidor.
