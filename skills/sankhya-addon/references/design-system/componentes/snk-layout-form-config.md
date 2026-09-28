> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-layout-form-config/ (snapshot 2026-09-28)

# Configurador de Layout do formulário

# snk-layout-form-config

O `snk-layout-form-config` é um componente responsável por gerenciar a configuração de layout dos formulários dentro de uma tela específica. Ele utiliza o `resourceID` da tela como chave para salvar e aplicar as configurações de layout em todos os formulários da tela.

## Arquitetura

  * O componente deve ser utilizado **dentro de um`snk-application`**, pois é este quem realiza o carregamento inicial das configurações e disponibiliza o singleton de notificação para os formulários.
  * Ele utiliza um **singleton** para notificar todos os formulários sobre alterações no layout.
  * Os componentes `snk-configurtorn`, `snk-simple-crud` e `snk-crud` possuem uma `prop` de ativação do configurador chamada **`layoutFormConfig`**.

> ⚠️ **Atenção:** Caso uma tela possua **mais de um** `snk-layout-form-config`, pode haver conflitos, pois o componente foi projetado para **uso único por tela**.

## Modos de Layout

O `snk-layout-form-config` oferece duas opções de layout para os formulários:

  1. **Layout em cascata (`CASCADE`)**: Os campos de texto são organizados verticalmente, um abaixo do outro.
  2. **Layout lado a lado (`SIDE_BY_SIDE`)**: Os campos são organizados horizontalmente, ajustando-se automaticamente à largura da tela.

O usuário pode alternar entre os modos utilizando `ez-check`, que dispara a atualização do layout por meio do singleton.

## Exemplo de Uso

```tsx
<snk-layout-form-config />
```

## Métodos

### `save()`

Salva a configuração de layout escolhida.

```tsx
await layoutFormConfig.save();
```

## Estados (`@State`)

| Estado | Tipo | Descrição |
|---|---|---|
| isCascade | boolean | Indica se o layout em cascata está ativado. |
| isSideBySide | boolean | Indica se o layout lado a lado está ativado. |

## Conclusão

O `snk-layout-form-config` é um componente essencial para a configuração de layout de formulários dentro de uma tela. Seu uso correto garante que todos os formulários compartilhem a mesma configuração, proporcionando uma experiência visual uniforme.

> ⚠️ **Importante:** Sempre utilize **apenas um** `snk-layout-form-config` por tela para evitar conflitos de configuração.
