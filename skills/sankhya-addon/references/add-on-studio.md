# Add-on Studio

## Visão Geral

O Add-on Studio é uma estrutura baseada em Gradle criada para simplificar o desenvolvimento de add-ons para o Sankhya Om. Permite criar soluções de forma eficiente, segura e alinhada às melhores práticas da plataforma.

**Capacidades:**
- Seguir boas práticas com código organizado e modular
- Testar localmente antes de publicar
- Integrar com pipelines de CI/CD
- Publicar diretamente da linha de comando ou pipeline

## Pré-requisitos

| Ferramenta / Conhecimento | Detalhes |
|---|---|
| Conta Sankhya ID | Permissão na Área do Desenvolvedor |
| Java (JDK) | Versão recomendada pela Sankhya |
| Gradle | Instalado no PATH ou gerenciado pela IDE (IntelliJ gerencia automaticamente) |
| Conhecimento básico | Desenvolvimento de add-ons para o Sankhya Om |

## Passo a Passo para Começar

1. **Crie o Componente** — na Área do Desenvolvedor, crie um novo Componente para o add-on
2. **Baixe o Template** — após a criação, clique em "Baixar Template"
3. **Extraia o Projeto** — descompacte o arquivo no ambiente de desenvolvimento
4. **Configure o Ambiente** — ajuste dependências e variáveis de ambiente
5. **Desenvolva** — siga a estrutura sugerida pelo template
6. **Teste Localmente** — use as ferramentas do Add-on Studio antes de publicar
7. **Automatize** — integre a um pipeline de CI/CD para builds e testes automáticos

## Boas Práticas

- **Modularize o código:** separe responsabilidades em packages distintos (MVC, Clean Architecture, etc.)
- **Documente:** crie documentação clara para o código e para o usuário final
- **Use testes automatizados:** garanta qualidade com testes unitários e de integração
- **Gerencie dependências** explicitamente no `build.gradle`:

```groovy
dependencies {
    implementation 'br.com.sankhya.commercial:sankhya-models:1.0.0'
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.1'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.1'
}
```

### Libs que o runtime já fornece ao addon

O `jboss-deployment-structure.xml` gerado no EAR do addon exporta como `deployment.<lib>` praticamente todo o `sankhyaw.ear/lib` (verificado na 4.35): `jsch` (0.1.55, pacote `com.jcraft.jsch`), `sancrypt`, `cryptacular`, `commons-*`, `httpclient`, `jackson-*`, `gson`, `poi`, `pdfbox`, `bcprov-jdk14`, `javax.mail` etc. Para essas, declare `compileOnly` com a **mesma versão** do runtime — não empacote outra cópia (conflito de classe no mesmo pacote). Lista exata: `standalone/deployments/<addon>.ear/META-INF/jboss-deployment-structure.xml` de um addon já deployado. Lib que o runtime não tem: `implementation` (vai para `lib/` do EAR).

Fork mantido do JSch (`com.github.mwiede:jsch`) usa o **mesmo pacote** `com.jcraft.jsch` do 0.1.55 exportado: empacotá-lo tende a conflitar. O 0.1.55 não suporta `ed25519` e servidores OpenSSH 8.8+ recusam `ssh-rsa` (SHA-1) por padrão — teste contra o servidor real cedo.

### Criptografia reversível (ex.: senha de SFTP)

Os utilitários nativos não servem: `com.sankhya.util.SymmetricKeyAES` (sanutil) lança `UnsupportedOperationException("Rotina descontinuada por questões de segurança.")`; `com.sankhya.util.Crypter` usa `PBEWithMD5AndDES` com chave fixa no próprio jar. Use `javax.crypto` (JDK) com `AES/GCM/NoPadding`, IV aleatório por valor gravado junto do cifrado.

## Antipadrões

- **Código monolítico:** evite um único módulo com toda a lógica do add-on
- **Hardcoding:** nunca fixe senhas, tokens ou URLs diretamente no código — use variáveis de ambiente ou configurações do add-on
- **Ignorar testes:** a ausência de testes leva a falhas inesperadas em produção
- **Falta de documentação:** add-on sem documentação é difícil de usar e manter

## FAQ

**É possível testar sem publicar no Marketplace?**
Sim — o Add-on Studio permite testes locais completos antes da publicação.

**É possível distribuir sem publicar no Marketplace?**
Sim — consulte o artigo "Como criar uma solução de uso exclusivo do cliente".

**Onde tirar dúvidas?**
Utilize a sala Sankhya Developers na comunidade Sankhya Developer.

## Fonte

https://developer.sankhya.com.br/docs/add-on-studio
