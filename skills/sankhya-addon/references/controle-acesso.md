# Controle de Acesso — Permissões Especiais Sankhya

Implementação de permissões especiais (acessos customizados) em todas as camadas: dicionário de dados, backend Java e frontend React/TypeScript.

---

## Conceitos fundamentais

### Permissões padrão vs especiais

O core do Sankhya fornece automaticamente permissões **padrão** para qualquer `<ui>` registrada no `menu.xml`:

- **CONSULTAR (C)** — acesso à tela. Sem ela, o **menu não aparece** na hierarquia/busca. Porém o core **não bloqueia** acesso direto por URL nem queries de DataUnit — por isso a checagem explícita de CONSULTAR no backend e no frontend ainda é necessária (defesa em profundidade).
- **INSERIR (I)**, **ALTERAR (A)**, **EXCLUIR (E)** — operações CRUD.
- **CONFIGURAR**, **CLONAR**, etc. — operações adicionais.

**Permissões especiais** são acessos customizados definidos via `<acesso>` no `menu.xml`. Exemplos: `EXECUTAR`, `APROVAR`, `PUBLICAR`. Controlam ações específicas da tela além do CRUD padrão.

### Princípios de implementação

1. **Defesa em profundidade** — verifique no frontend (UX) e no backend (segurança). Inclui o CONSULTAR padrão para evitar acesso direto por URL.
2. **Fail-closed** — em caso de erro na verificação, **negue** o acesso.
3. **Bypass do SUP é resolvido dentro do manager** — o superusuário (`CODUSU = 0`) tem acesso total sem registro explícito, e o próprio `MGEAuthorizationManager` trata isso. Não é preciso guard externo. Ver "Armadilhas documentadas".
4. **Consistência do RESOURCE_ID** — o mesmo ID de recurso em todas as camadas.
5. **Prefixo de módulo no RESOURCE_ID** — ao verificar via `MGEAuthorizationManager` (backend) ou `SnkApplication.hasAccess` (frontend), o RESOURCE_ID deve ser qualificado com o prefixo do módulo: `{context-root}.{id}`.

---

## Camada 1: Dicionário de dados (`menu.xml`)

Adicione o elemento `<acesso>` dentro da `<ui>` correspondente:

```xml
<ui id="NomeTela" url="/$ctx/Modulo.xhtml5?nativeV3=true" description="Descrição da Tela">
    <!-- Acesso especial — controla uma ação específica -->
    <acesso description="Executar" acronym="EXECUTAR" sequence="1"/>
</ui>
```

**Atributos obrigatórios:**

- `description`: nome legível exibido no painel de permissões.
- `acronym`: sigla usada no código (backend e frontend, em SCREAMING_SNAKE_CASE).
- `sequence`: ordem de exibição no painel (começa em 1).

---

## Camada 2: Backend Java — serviço de permissão

### Interface funcional

```java
package br.com.sankhya.{modulo}.service;

@FunctionalInterface
public interface PermissaoReader {
    boolean temPermissao(String resourceId, String acronym) throws Exception;
}
```

### Serviço de permissão

```java
package br.com.sankhya.{modulo}.service;

import br.com.sankhya.modelcore.MGEModelException;
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
import br.com.sankhya.modelcore.auth.MGEAuthorizationManager;

import java.math.BigDecimal;

public class Permissao{Dominio}Service {
    static final String RESOURCE_ID = "{modulo}.{ResourceId}";
    static final String ACRONYM_CONSULTAR = "C";
    static final String ACRONYM_EXECUTAR = "EXECUTAR";

    private final PermissaoReader reader;

    public Permissao{Dominio}Service() {
        this.reader = (resourceId, acronym) -> {
            BigDecimal codUsu = AuthenticationInfo.getCurrent().getUserID();
            MGEAuthorizationManager.MGEResourceAuthorization auth =
                MGEAuthorizationManager.getMGEResourceAuthorization(resourceId, codUsu);
            return auth.hasAuthorization(acronym); // SUP já retorna true aqui dentro
        };
    }

    public boolean temExecutar() throws Exception {
        return reader.temPermissao(RESOURCE_ID, ACRONYM_EXECUTAR);
    }

    public void assertTemExecutar() throws Exception {
        if (!temExecutar()) {
            throw new MGEModelException("Acesso negado: permissão ausente.");
        }
    }
}
```

### Armadilhas documentadas

> Comportamento abaixo verificado no bytecode de `mge-modelcore` 4.35 (`MGEAuthorizationManager` e `MGEAuthorizationManager$MGEResourceAuthorization`).

- **SUP não precisa de guard externo.** `getMGEResourceAuthorization` **sempre** instancia um `MGEResourceAuthorization`; quando `CODUSU` vale `0`, marca `isSup = true` e retorna imediatamente. `hasAuthorization` começa com `if (isSup) return true;`. Ou seja: o método **não retorna `null` para o SUP** e checar `AuthenticationInfo.isSUP()` antes é redundante — serve no máximo para evitar a consulta, nunca para evitar NPE.
- **Nulo é erro de programação, não "sem acesso".** `resourceId` vazio/nulo e `codUsu` nulo **lançam exceção** (registrada via `SKError.registry(TSLevel.ERROR, ...)`) em vez de retornar `null` ou `false`. Trate como bug de chamada, não como acesso negado.
- **Sigla inexistente retorna `false`.** `hasAuthorization` busca a sigla no mapa de domínios; sigla não encontrada nega o acesso. Concede quando a permissão direta está ligada **ou** quando o domínio de grupo do usuário a concede.
- **Tela em modo flow não usa a máscara do usuário.** Antes de ler as permissões, o manager consulta `TelaNativaFlowUtil.ehModoFlow(resourceId)`; sendo modo flow, os acessos são preenchidos por `TelaNativaFlowUtil.fillAuthorization(...)`. Divergência de permissão nessas telas se investiga no modelador, não na permissão do usuário.
- **Classe interna:** `MGEResourceAuthorization` é classe interna estática de `MGEAuthorizationManager`. `hasAnyAuthorization()` responde se o usuário tem qualquer acesso no recurso.

### Siglas padrão do core

Constantes públicas `SIGLA_*` de `MGEAuthorizationManager` (valores lidos da 4.35):

| Sigla | Constante | Índice do domínio |
|---|---|---|
| `I` | `SIGLA_INCLUIR` | 1 |
| `A` | `SIGLA_ALTERAR` | 2 |
| `E` | `SIGLA_EXCLUIR` | 3 |
| `C` | `SIGLA_CONSULTAR` | 4 |
| `F` | `SIGLA_CONFIGURAR` | 5 |
| `N` | `SIGLA_CONFIGURAR_NUMERACAO` | 6 |
| `D` | `SIGLA_DUPLICAR` | 7 |
| `U` | `SIGLA_FILTRO_AVANCADO` | 8 |
| `G` | `SIGLA_CONFIGURAR_GRID` | — (fora dos domínios numerados) |

Use as constantes em vez da string literal. Para a permissão especial, a sigla é a que você declarou no `acronym` do `<acesso>`.

**Layout da máscara de acesso:** `QTD_DOMINIOS_PADRAO = 10` domínios de `TAMANHO_DOMINIO = 3` posições cada. Dentro de cada domínio, os offsets são `OFFSET_PERMISSAO = 0`, `OFFSET_REPASSAR = 1`, `OFFSET_GRUPO = 2` — "repassar" é o direito de conceder aquela permissão a outro usuário. Não leia a máscara na mão: use `hasAuthorization`.

---

## Camada 3: Frontend React/TypeScript

Aplica quando a tela é nativa V3 (React + Design System Sankhya). Ver também `references/design-system/componentes/snk-application.md` (`hasAccess`, `getAllAccess`, `getResourceID`) e `references/design-system/guia.md`.

### Armadilhas críticas da API de permissão

- **❌ `getAllAccess()` NÃO funciona para permissões customizadas.** Retorna só o CRUD padrão.
- **✅ `hasAccess()` funciona para QUALQUER permissão.** Aceita qualquer string e faz bypass automático do SUP.

### Override de tipagem

`src/utils/getSnkApp.ts` — sobrescreva a tipagem de `hasAccess` para aceitar qualquer string:

```typescript
import { ApplicationContext } from "@sankhyalabs/core";
import type { SnkApplication } from "@sankhyalabs/sankhyablocks/dist/types/components/snk-application/snk-application";

type SnkApp = Omit<SnkApplication, "hasAccess"> & {
  hasAccess(access: string, resourceID?: string): Promise<boolean>;
};

const getSnkApp = (): SnkApp =>
  ApplicationContext.getContextValue("__SNK__APPLICATION__");

export default getSnkApp;
```

### Exemplo de uso

```tsx
import React, { useEffect, useState } from "react";
import getSnkApp from "@/utils/getSnkApp";

const RESOURCE_ID = "{modulo}.{ResourceId}";

export function MeuComponente() {
  const [temPermissao, setTemPermissao] = useState<boolean | null>(null);

  useEffect(() => {
    async function checarPermissao() {
      const snkApp = getSnkApp();
      const result = await snkApp.hasAccess("EXECUTAR", RESOURCE_ID);
      setTemPermissao(!!result);
    }
    checarPermissao();
  }, []);

  return (
    <button disabled={!temPermissao}>
      Executar Ação
    </button>
  );
}
```

> **Componentes do Design System:** em componentes como `EzButton`, a prop de desabilitar costuma se chamar `isDisabled`, não `disabled`. Cheque a API do componente.
