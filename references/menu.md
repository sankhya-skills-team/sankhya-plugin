# Menus Personalizados

## Visão Geral

Menus são o ponto de entrada para as funcionalidades do add-on no Sankhya Om. Eles organizam o acesso a formulários, telas e outras ações de forma hierárquica na barra de navegação principal.

A definição dos menus é feita no dicionário de dados usando as tags `<menu>`, `<nativeFolder>` e `<folder>`.

---

## Abordagens

### Opção 1: Novo Menu Principal (`<menu>`)

Cria um item de nível superior na barra de navegação.

**Arquivo:** `datadictionary/SGT_MENU.xml`

```xml
<metadados>
    <!-- A tag <menu> define o menu principal (nível 1) -->
    <menu id="SGT_MEUMENU" description="Meu Add-on" icon="/$ctx/assets/meu_icone.png">
        <!-- Conteúdo do menu: folders e dynamicForms -->
    </menu>
</metadados>
```

| Atributo | Descrição | Exemplo |
|---|---|---|
| `id` | **Obrigatório.** Identificador único. Use prefixo do add-on. | `SGT_MEUMENU` |
| `description` | Texto exibido ao usuário | `Meu Add-on` |
| `icon` | (Opcional) URL do ícone | `/$ctx/assets/icon.png` |

### Opção 2: Adicionar a Menu Nativo (`<nativeFolder>`)

"Anexa" itens a um menu já existente no Sankhya Om.

**Arquivo:** `datadictionary/SGT_NATIVE_MENU.xml`

```xml
<metadados>
    <!-- Adiciona itens ao menu nativo de Configurações -->
    <nativeFolder resourceId="sankhya.core.configuracoes">
        <!-- Conteúdo a ser adicionado -->
    </nativeFolder>
</metadados>
```

| Atributo | Descrição | Exemplo |
|---|---|---|
| `resourceId` | ID da pasta nativa a estender | `sankhya.core.configuracoes` |

> Para descobrir o `resourceId` de um menu nativo, inspecione a interface do Sankhya Om com as ferramentas de desenvolvedor do navegador.

### Submenus com `<folder>`

Independente da abordagem, use `<folder>` para criar submenus e organizar itens.

```xml
<menu id="SGT_MEUMENU" description="Meu Add-on">

    <!-- <folder> cria um sub-menu (nível 2) -->
    <folder id="SGT_SUBMENU_CADASTROS" description="Cadastros">
        <dynamicForm id="SGT_FORM_TESTE" instance="SGT_Teste" description="Cadastro de Atendimentos"/>
    </folder>

</menu>
```

| Atributo | Descrição | Exemplo |
|---|---|---|
| `id` | **Obrigatório.** Identificador único. Use prefixo. | `SGT_SUBMENU_CADASTROS` |
| `description` | Texto exibido no submenu | `Cadastros` |

---

## Ícones

### Ícone Local

1. Crie a pasta `src/main/webapp/assets`
2. Coloque o arquivo de imagem (ex: `meu_icone.png`) dentro dela
3. No atributo `icon`, use `/$ctx/assets/seu_icone.png` — `$ctx` representa a raiz do add-on

### Ícone Externo

```xml
<menu id="SGT_OUTRO_MENU" description="Externo" icon="https://exemplo.com/icone.svg" />
```

---

## Deploy e Verificação

```shell
./gradlew clean deployAddon
```

Após o deploy, acesse o Sankhya Om e verifique se o menu aparece na barra de navegação.

---

## Boas Práticas

- **Hierarquia lógica:** agrupe funcionalidades relacionadas em `<folder>` dentro do menu
- **Prefixos únicos:** use sempre um prefixo que identifique o add-on (ex: `SGT_`, `MEUADDON_`) nos IDs de menus e folders
- **Ícones leves:** prefira SVG ou PNG otimizado para não impactar o carregamento

## Antipadrões

- **Aninhar `<menu>` dentro de `<menu>`:** não é suportado e causa erros — use `<folder>` para submenus
- **Usar o prefixo `AD_`:** reservado para uso interno do Sankhya Om; causa conflitos inesperados
- **IDs duplicados:** dois menus ou pastas com o mesmo `id` causam erro de renderização
- **Caminhos de ícone quebrados:** o menu aparece sem ícone se o caminho não existir
- **Menu sem conteúdo:** criar menu ou pasta que não leva a nenhuma funcionalidade confunde o usuário

## Fonte

https://developer.sankhya.com.br/docs/06_menu