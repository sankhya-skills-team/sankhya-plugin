> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/onboarding/onboarding/bff/ (snapshot 2026-09-28)

# Onboarding

## Criando novas telas utilizando o Design System

A primeira decisão que devemos tomar ao criar uma nova tela utilizando o Design System é onde criá-la.

Para podermos fazer entregas rápidas e independentes devemos partir da premissa que deve ser possível realizar atualizações a quente, ou seja, devemos ter módulos desacoplados do monólito. Para isso temos duas opções:

  * Se o módulo que contém a tela já tiver um projeto desacoplado podemos criar a tela diretamente neste projeto;
  * Se o módulo que contém a tela ainda estiver dentro do monólito, devemos solicitar a criação de um novo módulo BFF.

informação

Procure o Arquiteto da Squad para obter estas informações.

### O que é um BFF e quando usar?

Os BFFs são módulos de apoio ao Design System baseados na arquitetura [BFF](https://medium.com/jeitosanar/backend-for-frontend-uma-estrat%C3%A9gia-sob-demanda-para-a-entrega-de-microsservi%C3%A7os-2f12d4cb9e3f) (Backend for Frontend) que visam permitir atualizações a quente do front-end de módulos do sistema que ainda não foram desacoplados do monólito.

Sempre que formos criar uma tela que seu projeto base ainda se encontra dentro do monólito (Projeto SankhyaW), devemos solicitar que a equipe da Quebra do Monólito realize e criação de um novo módulo BFF que será utilizado até que o módulo no monólito seja desacoplado.

## Como adicionar uma tela a um módulo separado do monólito?

Este processo se aplica tanto a módulos desacoplados quanto BFFs.

### 1 - Clonar projeto react-app-starter

Solicitar acesso ao projeto:

  * [Projeto react-app-starter](https://gitlab.sankhya.com.br/dti/design-system/react-app-starter)

Clonar o repositório:

```text
git clone https://gitlab.sankhya.com.br/dti/design-system/react-app-starter.git
```

### 2 - Copiar conteúdo do projeto react-app-starter para o diretório que irá conter a nova tela

Copiar o conteúdo da raiz do projeto

dica

Garanta que o arquivo .env suba para o repositório remoto, pois normalmente ele esta na lista de ignorados do .gitignore

Podemos forçar o commit do .env com o comando

```text
git add .env -f
```

### 3 - Setup inicial da tela

#### Ajustar .env

  * SKW_URL: URL do servidor de aplicação com o sankhyaW rodando;
  * VITE_APP_APP_DESCRIPTION: Nome da tela;
  * VITE_APP_MODULE_NAME: Nome do módulo;
  * VITE_APP_RESOURCE_ID: Resource ID da tela;

#### Ajustar .env.production

  * BASE_PATH: path dentro do SankhyaOm para acessar a tela (substituir o nome do módulo e da tela)

#### Ajustar package.json da tela:

Trocar referências do projeto:

#### Realizar o install e rodar o projeto:

```text
npm install

npm run dev
```

### 4 - Ajustar configurações de pipeline

As configurações da pipeline podem ter muitas particularidades dependendo do projeto em que se encontram. Os responsáveis por essas devem fazer os ajustes necessários.

As pipelines dos módulos BFF atualmente possuem uma configuração padrão de herança dos arquivos de build na raiz do frontend do módulo:

Exemplo:

```text
./financeiro-frontend/.gitlab-ci.yml

include:
  - local: '*/**/scripts/gitlab/.*Build.yml'
  ...
```

Isso faz com que qualquer arquivo que siga o padrão descrito seja executado no build da pipeline.

Portando devemos criar a pasta gitlab dentro do diretório scripts contendo os arquivos de configuração do build a tela:

Exemplos dos arquivos:

./financeiro-frontend/MinhaTelaBonitona/scripts/gitlab/.minhaTelaBonitonaBuild.yml

```text
workflow:
 rules:
   - when: always

minha-tela-bonitona-build:
 variables:
   PROJECT_PATH: "MinhaTelaBonitona"
 only:
   changes:
     - "financeiro-frontend/MinhaTelaBonitona/**/*"
 extends:
   - .build

minha-tela-bonitona-test:
 variables:
   PROJECT_PATH: "MinhaTelaBonitona"
 needs: ["minha-tela-bonitona-build"]
 only:
   changes:
     - "financeiro-frontend/MinhaTelaBonitona/**/*"
 extends:
   - .test

minha-tela-bonitona-deploy:
 variables:
   PROJECT_PATH: "MinhaTelaBonitona"
 needs: ["minha-tela-bonitona-test"]
 only:
   changes:
     - "financeiro-frontend/MinhaTelaBonitona/**/*"
 extends:
   - .deploy
```

./financeiro-frontend/MinhaTelaBonitona/scripts/gitlab/.minhaTelaBonitonaBuildInstall.yml

```text
minha-tela-bonitona-install:
  variables:
    PROJECT_PATH: "MinhaTelaBonitona"
    PACKAGE_NAME: "minha-tela-bonitona"
    JOB_DEPENDENCY: "minha-tela-bonitona-install"
  extends:
    - .build_screen
```

### Hands-on

[Criando uma tela no DS](https://drive.google.com/file/d/1arNhZs5dgVps6_xjNCiA1tlq_rnZ-GqW/view?usp=drive_link)

## Fluxo de desenvolvimento da tela

### Ajustar endereço do servidor e credenciais

Para rodar a tela fora do SankhyaOm, devemos ter um servidor de aplicação contendo o SankhyaW com a versão necessário do backend da tela (SankhyaW, módulo e/ou BFF) rodando.

Após ter o servidor de aplicação rodando, devemos mapear nos arquivos .env a variável SKW_URL:

Exemplo:

```text
SKW_URL=http://127.0.0.1:8180
...
```

dica

O projeto está inicialmente configurado para acessar com usuário SUP sem senha, caso seja necessário mudar as credenciais acessar o arquivo:

```text
./MinhaTelaBonitona/public/workspacemock/workspace.js
```

Na seção Auth, editar o NOMUSU e INTERNO para o nome e senha do usuário respectivamente. Exemplo:

```text
"requestBody": {
    "NOMUSU": {
        "$": "NOVOUSUARIO"
    },
    "INTERNO": {
        "$": "SENHADONOVOUSUARIO"
    }
}
```

### Ajustar o gulpfile

O gulp é responsável por automatizar a tarefa de deploy da tela para dentro do SankhyaOm

Ajustar as variáveis MODULE e APPNAME no arquivo gulpfile.test

### Fazer link entre projetos

informação

Estes passos só devem ser executados em casos de desenvolvimento de componentes ou em projetos dependência.

Muitas vezes precisamos fazer alterações ou consumir alterações ainda não disponíveis em produção em projetos dependência. Para isso utilizamos o `npm link`:

Quando rodamos o comando `npm link` em um projeto (dep-proj) criamos um symlink (symbolic link) no node_modules para que outros projetos tenham facil acesso aos arquivos.

Quando rodamos o comando `npm link dep-proj` estamos dizendo para a aplicação que estamos utilizar o symlink global da dependência que criamos anteriormente.

Dessa forma podemos fazer alterações no `dep-proj` e isso será refletido automaticamente (após o build do projeto em alguns casos) no projeto que está consumindo o link.

Com isso temos um processo padrão para o link dos projetos:

  * Acessar dependência;
  * `npm install`; (Caso ainda não tenha feito o install)
  * `npm link`;
  * `npm run build`;
  * Acessar projeto consumidor;
  * `npm link dep-proj`; (conferir arquivo runlink.sh na pasta scripts)

Após isso, realizar alguma alteração no projeto dependência e verificar que a alteração refletiu na tela.

dica

O VS-Code muitas vezes não atualiza o ícone do Symlink automaticamente. Pata atualizar, abrir a paleta de comandos

  * Show and Run commands (Ctrl+Shift+P)
  * Developer: Reload Window

Para verificar o Symlink: Acesse a paste node_modules, encontre o caminho da dependência linkada e veja se existe a setinha com o symbolic link

O diagrama a seguir representa a base dos links dos projetos BFF:
