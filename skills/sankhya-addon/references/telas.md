# Telas Personalizadas (UI)

## Visão Geral

Quando os Formulários Dinâmicos não são suficientes e você precisa de total controle sobre a interface, o Add-on Studio permite criar telas personalizadas usando a tecnologia HTML5 da Sankhya.

Ideal para dashboards, relatórios complexos ou qualquer interface que exija layout e comportamento específicos.

---

## Como Funciona

A criação de uma tela personalizada envolve dois passos:

1. **Criar o arquivo da View**: desenvolver o arquivo `.xhtml5` com a estrutura da tela
2. **Declarar a tela no menu**: usar a tag `<ui>` no dicionário de dados para vincular o arquivo a um item de menu

---

## Passo a Passo

### Passo 1: Crie o Arquivo da View

1. Navegue até `src/main/webapp/`
2. Crie uma subpasta para organizar suas telas (ex: `src/main/webapp/telas/`)
3. Crie o arquivo de view, por exemplo, `minha_tela.xhtml5`

### Passo 2: Adicione a Tela ao Menu

Edite o arquivo de menu no dicionário de dados (ex: `SGT_MENU.xml`) e adicione a tag `<ui>`.

**Arquivo:** `datadictionary/SGT_MENU.xml`

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <menu id="SGT_MEUMENU" description="Super Gestão">
        <!-- A tag <ui> cria um link para a tela personalizada -->
        <ui id="SGT_MINHA_TELA"
            url="/$ctx/telas/minha_tela.xhtml5"
            description="Minha Primeira Tela"/>
    </menu>
</metadados>
```

## Atributos da Tag `<ui>`

| Atributo | Descrição | Exemplo |
|---|---|---|
| `id` | Identificador único para o item de menu da tela | `SGT_MINHA_TELA` |
| `url` | **O mais importante**: caminho para o arquivo `.xhtml5` | `/$ctx/telas/minha_tela.xhtml5` |
| `description` | Texto que aparecerá no menu para o usuário | `Minha Primeira Tela` |
| `resourceId` | (Opcional) Compatibilidade com add-ons legados (DWF) | `54321` |

> **Importante:** A variável `/$ctx/` é substituída em tempo de execução pelo caminho raiz do add-on. **Sempre use-a no início da URL.** Omiti-la resulta em erro 404.

---

## Boas Práticas

- **Organize suas views**: crie subpastas dentro de `src/main/webapp/` para telas, scripts e estilos (ex: `/telas`, `/js`, `/css`)
- **Use prefixo único**: assim como em menus e tabelas, use um prefixo exclusivo nos IDs das tags `<ui>` para evitar conflitos
- **Componentização**: para telas complexas, utilize componentes JSF (JavaServer Faces) para reutilizar partes da interface

## Antipadrões

- **Usar o prefixo `AD_`**: reservado para uso interno do Sankhya Om; causa conflitos inesperados
- **Esquecer o `/$ctx/`**: sem essa variável o sistema não encontra a tela, resultando em erro 404
- **IDs duplicados**: usar o mesmo `id` para diferentes itens de menu (`<ui>`, `<dynamicForm>`, etc.) causa conflitos
- **Expor lógica de negócio na view**: a tela (XHTML) deve cuidar apenas da apresentação; mantenha a lógica em classes Java (Beans)

## Fonte

https://developer.sankhya.com.br/docs/07_telas