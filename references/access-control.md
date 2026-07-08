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
3. **Bypass do SUP** — o superusuário (SUP) tem acesso total sem registro explícito.
4. **Consistência do RESOURCE_ID** — o mesmo ID de recurso em todas as camadas.
5. **Prefixo de módulo no RESOURCE_ID** — ao verificar via `MGEAuthorizationManager` (backend) ou `SnkApplication.hasAccess` (frontend), o RESOURCE_ID deve ser qualificado com o prefixo do módulo: `{context-root}.{id}`.

---

## Camada 1: Dicionário de dados (`menu.xml`)

**Arquivo:** `datadictionary/menu.xml`

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

**Arquivo:** `service/PermissaoReader.java`

```java
package br.com.sankhya.{modulo}.service;

@FunctionalInterface
public interface PermissaoReader {
    boolean temPermissao(String resourceId, String acronym) throws Exception;
}
```

### Serviço de permissão

**Arquivo:** `service/Permissao{Dominio}Service.java`

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
            AuthenticationInfo authInfo = AuthenticationInfo.getCurrent();
            if (authInfo.isSUP()) return true; // BYPASS DO SUP

            BigDecimal codUsu = authInfo.getUserID();
            MGEAuthorizationManager.MGEResourceAuthorization auth =
                MGEAuthorizationManager.getMGEResourceAuthorization(resourceId, codUsu);
            return auth.hasAuthorization(acronym);
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

- **SUP — bypass obrigatório:** o SUP **não tem** registros explícitos. `getMGEResourceAuthorization` retorna `null` para o SUP. Sempre cheque `isSUP()` **antes** de consultar o manager, senão dá NPE.
- **Classe interna:** `MGEResourceAuthorization` é classe interna de `MGEAuthorizationManager`.

---

## Camada 3: Frontend React/TypeScript

Aplica quando a tela é nativa V3 (React + Design System Sankhya). Ver também os refs `sankhya-js-*`.

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
