> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/getting-started/configure (snapshot 2026-09-28)

# Configurando

## Pré requisitos

  * ReactJS 18
  * Node 14

Dica

Recomendamos a utilização do [NVM](https://github.com/coreybutler/nvm-windows) para gerenciar versões do node

Existem duas formas de iniciar uma aplicação utilizando o biblioteca do design system:

### Utilizar a aplicação starter

> Essa é a forma mais simples e recomendada para iniciar uma aplicação.

Basta executar os comandos a seguir e a aplicação estará funcionando na porta 3000:

```sh
git clone https://gitlab.sankhya.com.br/dti/design-system/react-app-starter
cd react-app-starter
npm install
npm start
```

### Fazer a configuração manualmente em um projeto React

> Recomendamos esse caminho apenas quando já existir uma aplicação React em andamento, e você deseja adicionar o design system a essa aplicação.

O primeiro passo é executar a instalação das seguintes dependências no projeto React:

```sh
npm install @sankhyalabs/core@latest
npm install @sankhyalabs/ez-design@latest
npm install @sankhyalabs/ezui@latest
```

Agora que instalamos, precisamos configurar essas dependências no arquivo `index.tsx` da aplicação da seguinte forma:

```jsx
import { applyPolyfills, defineCustomElements } from "@sankhyalabs/ezui/loader";

applyPolyfills().then(() => {
  defineCustomElements();
});
```

Também é necessário realizar a importação dos estilos do projeto ez-design, é esse arquivo que vai definir o estilo dos componentes. A importação deve ser realizada no arquivo `index.tsx` da seguinte forma:

```jsx
import  '@sankhyalabs/ez-design/dist/default/ez-themed.min.css';
```

E por último é necessário adicionar a fonte Roboto ao projeto alterando o arquivo `public\index.html` da seguinte forma:

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

Agora, basta utilizar os componentes do design system conforme exemplo:

```tsx
import { EzButton } from "@sankhyalabs/ezui/react/components";

export default function App() {
    return (
        <div className="ez-flex
                        ez-flex--justify-around
                        ez-flex--align-items-center
                        ez-size-height--full">
            <EzButton   class="ez-button--primary"
                        label="Clique-me"
                        onClick={() => alert('Olá Sankhya design system!')}>
            </EzButton>
        </div>
    );
}
```

### Utilizando blocos de construção

Caso seja necessário utilizar os componentes do EIP é necessário instalar a dependência a seguir:

```sh
npm install @sankhyalabs/sankhyablocks@latest
```

E configura-la no `index.tsx` da seguinte forma:

```jsx
import { applyPolyfills as applyBlocks,
         defineCustomElements as defineBlocks} from "@sankhyalabs/sankhyablocks/loader";

applyBlocks().then(() => {
  defineBlocks();
});
```

Importante

Existe um grande desejo de nossos times em utilizar ferramentas de build como o [Vitejs](https://vitejs.dev/) para desenvolvimento de suas aplicações, mas, infelizmente, nossos componentes ainda não estão preparados para utilizar essas ferramentas. Estamos trabalhando para que isso seja possível e em breve traremos novidades, mas por enquanto, sugerimos a utilização do ReactJS `18` juntamente com as configurações do webpack disponibilizado pelo react-scripts.
