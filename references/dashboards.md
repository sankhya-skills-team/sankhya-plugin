# Dashboards Embarcados

> Disponível a partir da versão 2.0 do Add-on Studio.  
> Versão mínima do Sankhya Om: **4.35b44**.

## Visão Geral

É possível inserir arquivos de dashboards exportados do Sankhya Om diretamente no Add-on Studio. O dashboard fica incorporado à estrutura do add-on, facilitando manutenção e instalação no ambiente do cliente.

---

## Passo 1 — Exportar o Dashboard do Sankhya Om

1. Crie o dashboard no Sankhya Om.
2. Exporte-o — o resultado é um arquivo `.zip`.
3. Descompacte o `.zip`. Dentro você encontrará o arquivo `dashboardMetadata.xml`.
4. Mova esse arquivo para a pasta `dashboards` dentro do projeto Add-on Studio.

> Se quiser adicionar mais de um dashboard ao add-on, **renomeie** cada arquivo antes de mover para a pasta `dashboards` (ex: `dashboard1.xml`, `dashboard2.xml`). Todos os arquivos dentro dessa pasta devem ter nomes únicos.

---

## Passo 2 — Referenciar no `datadictionary`

Para que o dashboard apareça como uma tela no Sankhya, crie um `<menu>` ou uma `<nativeFolder>` dentro do diretório `datadictionary`, referenciando o arquivo do dashboard.

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

   <!-- Dashboard diretamente em um menu customizado -->
   <menu id="dash" description="Dashboard" icon="/$ctx/assets/icon_2.png">
       <dashboard id="1" file="dashboardMetadata.xml" description="Dashboard Teste 1"/>
       <folder id="folder" description="Dashboards">
           <dashboard id="2" file="dashboard2.xml" description="Dashboard Teste 2"/>
       </folder>
   </menu>

   <!-- Dashboard em uma pasta nativa do Sankhya -->
   <nativeFolder name="CONFIGURACOES_CADASTROS">
       <dashboard id="3" file="dashboardMetadata2.xml" description="Dashboard Teste 3"/>
   </nativeFolder>

</metadados>
```

### Atributos da tag `<dashboard>`

| Atributo | Descrição |
|---|---|
| `id` | Identificador único do dashboard dentro do add-on. Deve ser único para cada dashboard. |
| `file` | Caminho relativo ao arquivo XML dentro da pasta `dashboards`. Ex: `minhapasta/dash1.xml` |
| `description` | Descrição exibida na tela do Sankhya. |

### Observações importantes sobre o `id`

- **Não altere o `id` após o dashboard ter sido instalado no cliente.** Ao mudar o ID, o Sankhya Om trata o item como algo novo, exigindo novas liberações de acesso.
- Use números como IDs e apenas incremente ao adicionar novos dashboards — nunca edite os IDs existentes.
- O ID final do dashboard é um **hash computado em tempo de compilação**. Nos metadados gerados você verá um ID diferente do que informou — isso é esperado e não é um problema.
- O dashboard criado via add-on **não aparece** na tela Construtor de Dashboards do Sankhya.

---

## Passo 3 — Deploy

```shell
./gradlew clean deployAddon
```

Após o deploy, acesse o menu no Sankhya Om para verificar se o dashboard foi processado e está disponível.

---

## Fonte

https://developer.sankhya.com.br/docs/04_dashboard