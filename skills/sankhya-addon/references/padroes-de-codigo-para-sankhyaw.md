# Padrões de Código para SankhyaW

Documentação dos padrões, convenções e boas práticas de desenvolvimento do projeto SankhyaW

---

## 📑 Índice

1. [Arquitetura](#-arquitetura)
2. [Organização de Pacotes](#-organiza%C3%A7%C3%A3o-de-pacotes)
3. [Nomenclatura de Classes](#-nomenclatura-de-classes)
4. [Padrões de Código Java](#-padr%C3%B5es-de-c%C3%B3digo-java)
5. [Padrões Técnicos Específicos](#-padr%C3%B5es-t%C3%A9cnicos-espec%C3%ADficos)
6. [Camada Web](#-camada-web)
7. [Configuração e Build](#-configura%C3%A7%C3%A3o-e-build)
8. [Design Patterns](#-design-patterns)
9. [Boas Práticas](#-boas-pr%C3%A1ticas)

---

## 🏗️ Arquitetura

### Estrutura Monolítica Modular

O SankhyaW utiliza uma arquitetura **monolítica modular**, onde o sistema é dividido em módulos independentes que se integram de forma coesa.

#### Separação de Camadas

- **Model**: Camada de lógica de negócio e modelo de domínio
- **VC** (View Controller): Camada de apresentação e controle

#### Principais Módulos

| Módulo | Descrição |
| --- | --- |
| `MGE-Core-VC` | Núcleo visual e de controle |
| `MGE-Modelcore` | Núcleo do modelo de negócio |
| `MGE-Base-Model` | Modelo base do sistema |
| `JAPE` | Framework de persistência e acesso a dados |
| `DWF` | Framework web |
| `DAO` | Data Access Objects |
| `Cuckoo` | Módulo Cuckoo |

#### Estrutura de Diretórios

```
sankhyaw/
├── MGE-*-Model/          # Módulos de modelo
├── MGE-*-VC/             # Módulos de view/controller
├── JAPE/                 # Framework de persistência
├── DWF/                  # Framework web
├── buildSrc/             # Scripts de build
├── docs/                 # Documentação
└── projects              # Lista de projetos incluídos
```

---

## 📦 Organização de Pacotes

### Convenção de Nomenclatura

```
br.com.sankhya.<módulo>.<camada>.<funcionalidade>
```

### Exemplos Práticos

```
// Fachadas do modelo
br.com.sankhya.modelcore.facades

// Data Access Objects
br.com.sankhya.jape.dao

// Servlets
br.com.sankhya.mge.servlet

// Utilitários do modelo
br.com.sankhya.modelcore.util

// Helpers de negócio
br.com.sankhya.armazem.model.helper

// Gateway/integração
br.com.sankhya.modelcore.gateway.persistencelogs.repository

// Serviços web
br.com.sankhya.mge.core.services
```

### Separação por Responsabilidade

| Pacote | Propósito |
| --- | --- |
| `facades` | Padrão Facade - interfaces simplificadas |
| `dao` | Data Access Objects - acesso a dados |
| `util` | Classes utilitárias gerais |
| `helper` | Classes auxiliares de negócio específicas |
| `servlet` | Camada de controle web (Servlets) |
| `model` | Modelos de domínio |
| `gateway` | Pontos de entrada/saída do sistema |
| `core` | Funcionalidades centrais |
| `services` | Serviços de negócio |

---

## 🎯 Nomenclatura de Classes

### Sufixos Padrão e Suas Aplicações

#### `Helper`

Classes auxiliares com lógica de negócio específica de um domínio.

```
public class ArmazensGeraisHelper {
    // Lógica específica de armazéns
}

public class FotosImovelHelper {
    // Lógica específica de fotos de imóveis
}
```

**Quando usar:**

- Lógica de negócio específica de um contexto
- Operações que não cabem no modelo mas são relacionadas
- Processamento complexo de dados de domínio

---

#### `Utils`

Métodos utilitários estáticos e reutilizáveis.

```
public class StringUtils {
    public static String replaceString(String source, String oldStr, String newStr) {
        // ...
    }
}

public class TimeUtils {
    public static Date parseDate(String dateStr) {
        // ...
    }
}
```

**Quando usar:**

- Funções puramente utilitárias
- Operações genéricas e reutilizáveis
- Métodos sem estado (stateless)

---

#### `Manager`

Gerenciamento de recursos, processos ou coordenação de operações.

```
public class DigitalSignatureManager {
    // Gerencia assinaturas digitais
}
```

**Quando usar:**

- Coordenação de múltiplos componentes
- Gerenciamento de ciclo de vida de recursos
- Orquestração de processos complexos

---

#### `Factory`

Padrão Factory para criação de objetos.

```
public class EntityFacadeFactory {
    public static EntityFacade createEntityFacade() {
        // Lógica de criação
    }
}
```

**Quando usar:**

- Criação de objetos complexos
- Decisão de qual implementação instanciar
- Encapsulamento da lógica de construção

---

#### `Builder`

Padrão Builder para construção fluente de objetos complexos.

```
public class MGEReportBuilder {
    private String title;
    private String format;

    public MGEReportBuilder withTitle(String title) {
        this.title = title;
        return this;
    }

    public Report build() {
        // Constrói o relatório
    }
}
```

**Quando usar:**

- Objetos com muitos parâmetros opcionais
- Construção passo a passo
- Melhorar legibilidade na criação

---

#### `Resolver`

Resolução/processamento de dados ou decisões.

```
public class GadgetResolver {
    // Resolve dados de gadgets
}

public class DigitalSignStatusResolver {
    // Resolve status de assinatura digital
}
```

**Quando usar:**

- Resolução de referências ou dados
- Processamento e transformação
- Lógica de decisão/roteamento

---

#### `Bean`

Enterprise JavaBeans (EJBs) - componentes de negócio.

```
public class SystemUtilsSPBean implements SessionBean {
    // Utilitários de sistema como EJB
}

public class DatasetSPBean implements SessionBean {
    // Manipulação de datasets
}
```

**Quando usar:**

- Componentes gerenciados pelo container
- Serviços de negócio transacionais
- Componentes com estado gerenciado

---

#### `Servlet`

Servlets HTTP - camada de controle web.

```
public class MgeServletContextListener implements ServletContextListener {
    // Listener do contexto servlet
}

public class ImobSessionUploadServlet extends SnkDefaultServlet {
    // Servlet para upload
}
```

**Quando usar:**

- Endpoints HTTP
- Controle de requisições web
- Integração com camada de apresentação

---

#### `Proxy`

Padrão Proxy - controle de acesso a objetos.

```
public class ConnectionProxy implements InvocationHandler {
    // Proxy para conexões
}

public class CrudServiceProviderProxy {
    // Proxy para serviços CRUD
}
```

**Quando usar:**

- Controle de acesso
- Lazy loading
- Logging/monitoramento transparente

---

#### `Wrapper`

Encapsulamento/adaptação de funcionalidades.

```
public class DataSourceWrapper implements DataSource {
    // Encapsula DataSource
}

public class JapeWrapper {
    // Encapsula funcionalidades JAPE
}
```

**Quando usar:**

- Adaptação de interfaces
- Adicionar funcionalidades a objetos existentes
- Compatibilidade entre versões

---

## 💻 Padrões de Código Java

### Organização de Imports

Siga sempre esta ordem:

```
// 1. Imports do Java (java.* e javax.*)
import java.io.File;
import java.io.InputStream;
import java.math.BigDecimal;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.ejb.SessionBean;
import javax.servlet.http.HttpSession;

// 2. Imports de bibliotecas externas
import org.apache.commons.io.IOUtils;
import org.jdom.Document;
import org.jdom.Element;

import com.google.gson.JsonObject;
import com.sankhya.util.StringUtils;
import com.sankhya.util.TimeUtils;

// 3. Imports do projeto Sankhya (br.com.sankhya.*)
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.dao.EntityDAO;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
import br.com.sankhya.util.troubleshooting.SKError;
import br.com.sankhya.util.troubleshooting.TSLevel;
```

---

### Tratamento de Erros

#### Sistema de Troubleshooting Customizado

```
import br.com.sankhya.util.troubleshooting.TSLevel;
import br.com.sankhya.util.troubleshooting.SKError;

public class ExemploTratamentoErro {
    public void processar() {
        try {
            // Operação que pode falhar
        } catch (Exception e) {
            SKError.registrarErro(TSLevel.ERROR, "Erro ao processar", e);
            throw new RuntimeException("Falha no processamento", e);
        }
    }
}
```

---

### Uso de Collections e Tipos

#### Preferências de Tipos

```
// Valores monetários/precisão - SEMPRE BigDecimal
BigDecimal valor = new BigDecimal("100.50");
BigDecimal total = valor.multiply(new BigDecimal("2"));

// Datas/Timestamps
Timestamp dataHora = new Timestamp(System.currentTimeMillis());
SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

// Collections - use interfaces nas declarações
Map<String, Object> mapa = new HashMap<>();
List<String> lista = new ArrayList<>();
Set<Integer> conjunto = new HashSet<>();
Collection<DynamicVO> vos = new ArrayList<>();
```

#### Evite

```
// ❌ NÃO use float ou double para valores monetários
float preco = 100.50f; // Impreciso!

// ❌ NÃO use implementações concretas em declarações
HashMap<String, Object> mapa = new HashMap<>(); // Menos flexível

// ✅ USE
Map<String, Object> mapa = new HashMap<>();
```

---

### Logging com Lombok

```
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class CustomModuleLoader {

    public void carregarModulo() {
        log.info("Iniciando carregamento do módulo");

        try {
            // Lógica
            log.debug("Módulo carregado com sucesso");
        } catch (Exception e) {
            log.error("Erro ao carregar módulo", e);
        }
    }
}
```

**Níveis de Log:**

- `log.trace()` - Informações muito detalhadas
- `log.debug()` - Informações de debug
- `log.info()` - Informações gerais
- `log.warn()` - Avisos
- `log.error()` - Erros

---

### Padrão Value Object (VO)

```
import br.com.sankhya.jape.vo.DynamicVO;

public class ExemploVO {
    public void exemplo() {
        DynamicVO vo = // obtém do EntityFacade

        // Acesso a propriedades
        BigDecimal valor = vo.asBigDecimal("VALOR");
        String nome = vo.asString("NOME");
        Timestamp data = vo.asTimestamp("DATA");
    }
}
```

---

## 🔧 Padrões Técnicos Específicos

### JAPE - Framework de Persistência

O JAPE é o framework próprio de persistência do SankhyaW.

#### EntityFacade - Operações de Entidade

```
import br.com.sankhya.jape.EntityFacade;
import br.com.sankhya.jape.vo.DynamicVO;
import br.com.sankhya.jape.wrapper.JapeWrapper;

public class ExemploEntityFacade {

    public void consultarEntidade() throws Exception {
        EntityFacade facade = EntityFacade.getWrapper("NomeEntidade");

        // Criar novo registro
        DynamicVO novoVO = facade.getDefaultValueObjectInstance();
        novoVO.setProperty("CAMPO", "valor");
        facade.createEntity(novoVO);

        // Buscar registro
        DynamicVO vo = facade.findEntityByPrimaryKey(1);

        // Atualizar
        vo.setProperty("CAMPO", "novo valor");
        facade.updateEntity(vo);

        // Remover
        facade.removeEntity(vo);
    }
}
```

---

#### JapeSession - Gerenciamento de Sessão

```
import br.com.sankhya.jape.core.JapeSession;
import br.com.sankhya.jape.core.JapeSession.SessionHandle;

public class ExemploJapeSession {

    public void executarComSessao() throws Exception {
        SessionHandle handle = null;
        try {
            handle = JapeSession.open();

            // Operações dentro da sessão
            EntityFacade facade = EntityFacade.getWrapper("Entidade");
            // ... operações

        } finally {
            if (handle != null) {
                JapeSession.close(handle);
            }
        }
    }
}
```

---

#### EntityDAO - Data Access Object

```
import br.com.sankhya.jape.dao.EntityDAO;
import br.com.sankhya.jape.dao.JdbcWrapper;
import br.com.sankhya.jape.sql.NativeSql;

public class ExemploDAO {

    public void executarSQL() throws Exception {
        JdbcWrapper jdbc = null;
        try {
            jdbc = // obtém wrapper

            NativeSql sql = new NativeSql(jdbc);
            sql.appendSql("SELECT * FROM TABELA WHERE CAMPO = ?");
            sql.setParameter("valor");

            ResultSet rs = sql.executeQuery();
            while (rs.next()) {
                // Processar resultado
            }
        } finally {
            JdbcWrapper.closeSession(jdbc);
        }
    }
}
```

---

### Gerenciamento de Transações

```
import br.com.sankhya.jape.util.TXManagerUtil;

public class ExemploTransacao {

    public void executarTransacional() throws Exception {
        try {
            TXManagerUtil.begin();

            // Operações transacionais
            EntityFacade facade = EntityFacade.getWrapper("Entidade");
            // ... operações

            TXManagerUtil.commit();
        } catch (Exception e) {
            TXManagerUtil.rollback();
            throw e;
        }
    }
}
```

---

### Tratamento de SQL e JDBC

```
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.sankhya.util.JdbcUtils;

public class ExemploJDBC {

    public void consultarBanco(Connection conn) {
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
            stmt = conn.prepareStatement("SELECT * FROM TABELA WHERE ID = ?");
            stmt.setInt(1, 123);

            rs = stmt.executeQuery();
            while (rs.next()) {
                String nome = rs.getString("NOME");
                BigDecimal valor = rs.getBigDecimal("VALOR");
                // Processar...
            }
        } catch (Exception e) {
            log.error("Erro ao consultar banco", e);
        } finally {
            JdbcUtils.closeResultSet(rs);
            JdbcUtils.closeStatement(stmt);
        }
    }
}
```

---

## 🌐 Camada Web

### Servlets

#### Herança do Servlet Base

```
import br.com.sankhya.dwf.servlet.SnkDefaultServlet;

public class MeuServlet extends SnkDefaultServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        // Lógica do GET
        String parametro = req.getParameter("param");

        // Processar...

        resp.setContentType("application/json");
        resp.getWriter().write(resultado);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        // Lógica do POST
    }
}
```

---

#### Upload de Arquivos

```
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

import br.com.sankhya.dwf.controller.fileupload.MonitoredDiskFileItemFactory;

public class UploadServlet extends SnkDefaultServlet {

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        ServletFileUpload upload = new ServletFileUpload(
            new MonitoredDiskFileItemFactory(new UploadListener(req), req.getSession())
        );

        try {
            List<FileItem> items = upload.parseRequest(req);

            for (FileItem item : items) {
                if (!item.isFormField()) {
                    String fileName = item.getName();
                    InputStream fileContent = item.getInputStream();
                    // Processar arquivo...
                }
            }
        } catch (Exception e) {
            log.error("Erro no upload", e);
        }
    }
}
```

---

### GWT (Google Web Toolkit)

#### EntryPoint

```
import com.google.gwt.core.client.EntryPoint;

public class MeuEntryPoint implements EntryPoint {

    @Override
    public void onModuleLoad() {
        // Inicialização da aplicação GWT
    }
}
```

#### Interfaces para Callbacks

```
public interface MeuCallback {
    void onSuccess(String resultado);
    void onError(String mensagem);
}

// Uso
public void executarAcao(MeuCallback callback) {
    try {
        String resultado = // processar
        callback.onSuccess(resultado);
    } catch (Exception e) {
        callback.onError(e.getMessage());
    }
}
```

---

## 📋 Configuração e Build

### Gradle Multi-Projeto

#### settings.gradle

```
apply from: "buildSrc/apply.gradle"

// Lê arquivo 'projects' linha por linha
file("projects").eachLine {
    if(!it.startsWith("//") && !it.startsWith("#") && !it.isEmpty())
        include(it)
}
```

#### Arquivo projects

```
MGE-Core-VC
MGE-Modelcore
JAPE
DWF
// MGE-Desabilitado  # Comentários são ignorados
```

---

#### build.gradle (raiz)

```
// Mapeamento Projeto -> Artefato Nexus
def maps = [
    "MGE-Modelcore" : "mge-modelcore",
    "JAPE"          : "jape",
    "DWF"           : "dwf",
    // ...
]

// Configurações comuns
allprojects {
    group = 'br.com.sankhya'
    version = '4.35.0'
}

// Dependências substituídas por projetos locais quando disponíveis
```

---

### Dependências Gradle de Módulos

```
dependencies {
    // Dependências internas
    implementation project(':JAPE')
    implementation project(':SankhyaUtil')

    // Dependências externas
    implementation 'org.apache.commons:commons-lang3:3.12.0'
    implementation 'com.google.code.gson:gson:2.8.9'

    // Dependências provided (fornecidas pelo container)
    providedCompile 'javax.servlet:javax.servlet-api:4.0.1'
}
```

---

## 🎨 Design Patterns

### Padrões Identificados no Codebase

#### 1. Facade Pattern

**Propósito:** Simplificar interfaces complexas

```
package br.com.sankhya.modelcore.facades;

public class SystemUtilsSPBean {

    // Fachada que simplifica acesso a múltiplos subsistemas
    public String executarOperacaoComplexa(String parametro) {
        // Coordena múltiplos componentes internamente
        SubsistemaA.processar(parametro);
        SubsistemaB.validar(parametro);
        return SubsistemaC.finalizar(parametro);
    }
}
```

---

#### 2. DAO (Data Access Object) Pattern

**Propósito:** Abstração da persistência

```
package br.com.sankhya.jape.dao;

public class EntityDAO {

    public DynamicVO findById(Object primaryKey) {
        // Abstrai detalhes de acesso ao banco
    }

    public void save(DynamicVO entity) {
        // Abstrai lógica de persistência
    }
}
```

---

#### 3. Factory Pattern

**Propósito:** Criação de objetos

```
public class EntityFacadeFactory {

    public static EntityFacade createEntityFacade(String entityName) {
        // Decide qual implementação retornar
        // Encapsula lógica de criação
        return new EntityFacadeImpl(entityName);
    }
}
```

---

#### 4. Builder Pattern

**Propósito:** Construção fluente

```
public class MGEReportBuilder {

    private String title;
    private String format;
    private Map<String, Object> parameters = new HashMap<>();

    public MGEReportBuilder withTitle(String title) {
        this.title = title;
        return this;
    }

    public MGEReportBuilder withFormat(String format) {
        this.format = format;
        return this;
    }

    public MGEReportBuilder addParameter(String key, Object value) {
        this.parameters.put(key, value);
        return this;
    }

    public Report build() {
        return new Report(title, format, parameters);
    }
}

// Uso
Report report = new MGEReportBuilder()
    .withTitle("Relatório de Vendas")
    .withFormat("PDF")
    .addParameter("mes", "Janeiro")
    .build();
```

---

#### 5. Proxy Pattern

**Propósito:** Controle de acesso

```
public class ConnectionProxy implements InvocationHandler {

    private Connection realConnection;

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) {
        // Log antes
        log.debug("Executando: " + method.getName());

        Object result = method.invoke(realConnection, args);

        // Log depois
        log.debug("Executado: " + method.getName());

        return result;
    }
}
```

---

#### 6. Session Pattern

**Propósito:** Gerenciamento de estado

```
public class JapeSession {

    private static ThreadLocal<SessionHandle> currentSession = new ThreadLocal<>();

    public static SessionHandle open() {
        SessionHandle handle = new SessionHandle();
        currentSession.set(handle);
        return handle;
    }

    public static void close(SessionHandle handle) {
        currentSession.remove();
    }

    public static SessionHandle getCurrentSession() {
        return currentSession.get();
    }
}
```

---

#### 7. Helper/Utility Pattern

**Propósito:** Funções auxiliares

```
// Utility - métodos estáticos genéricos
public class StringUtils {

    public static boolean isEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }

    public static String replaceString(String source, String oldStr, String newStr) {
        // Implementação
    }
}

// Helper - lógica específica de domínio
public class ArmazensGeraisHelper {

    public BigDecimal calcularSaldoEstoque(Integer codProduto) {
        // Lógica específica de armazém
    }
}
```

---

## 📚 Boas Práticas

### 1. Nomenclatura Clara e Consistente

```
// ✅ BOM - Nome indica responsabilidade
public class UsuarioRepository {
    public Usuario buscarPorId(Integer id) { }
}

// ❌ RUIM - Nome genérico
public class DAO {
    public Object get(Object id) { }
}
```

---

### 2. Separação de Camadas

```
// ✅ BOM - Camadas separadas
// Model
package br.com.sankhya.vendas.model;
public class Pedido { }

// VC (Controller/View)
package br.com.sankhya.vendas.vc.servlet;
public class PedidoServlet extends SnkDefaultServlet { }
```

---

### 3. Reutilização via Utils e Helpers

```
// ✅ BOM - Reutilizar código comum
public class ValidationUtils {
    public static void validarCPF(String cpf) {
        // Validação reutilizável
    }
}

// ❌ RUIM - Duplicar código
public class ClasseA {
    private void validarCPF(String cpf) { /* duplicado */ }
}

public class ClasseB {
    private void validarCPF(String cpf) { /* duplicado */ }
}
```

---

### 4. Use Facades para Simplificar

```
// ✅ BOM - Facade simplifica acesso
public class VendasFacade {

    public void processarVenda(DadosVenda dados) {
        // Coordena múltiplos serviços
        estoqueService.reservar(dados.getProdutos());
        financeiroService.gerarCobranca(dados.getValor());
        notaFiscalService.emitir(dados);
    }
}

// Cliente usa interface simples
facade.processarVenda(dados);
```

---

### 5. Gerenciamento Adequado de Recursos

```
// ✅ BOM - Try-with-resources (Java 7+)
public void lerArquivo(String path) {
    try (InputStream is = new FileInputStream(path);
         BufferedReader reader = new BufferedReader(new InputStreamReader(is))) {

        String linha;
        while ((linha = reader.readLine()) != null) {
            processar(linha);
        }
    } catch (IOException e) {
        log.error("Erro ao ler arquivo", e);
    }
}

// ✅ BOM - Finally quando try-with-resources não é possível
public void executarQuery() {
    Connection conn = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;

    try {
        conn = getConnection();
        stmt = conn.prepareStatement("SELECT ...");
        rs = stmt.executeQuery();
        // Processar
    } catch (SQLException e) {
        log.error("Erro SQL", e);
    } finally {
        JdbcUtils.closeResultSet(rs);
        JdbcUtils.closeStatement(stmt);
        JdbcUtils.closeConnection(conn);
    }
}
```

---

### 6. Logging Consistente

```
// ✅ BOM - Use @Slf4j do Lombok
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class MinhaClasse {

    public void metodo() {
        log.debug("Iniciando processamento");

        try {
            // Lógica
            log.info("Processamento concluído com sucesso");
        } catch (Exception e) {
            log.error("Erro no processamento", e);
            throw e;
        }
    }
}

// ❌ RUIM - System.out.println
public class MinhaClasse {
    public void metodo() {
        System.out.println("Iniciando..."); // Não usar!
    }
}
```

---

### 7. Use BigDecimal para Valores Monetários

```
// ✅ BOM - BigDecimal para precisão
BigDecimal preco = new BigDecimal("100.50");
BigDecimal quantidade = new BigDecimal("3");
BigDecimal total = preco.multiply(quantidade);

// Configure escala e arredondamento
BigDecimal resultado = total.setScale(2, RoundingMode.HALF_UP);

// ❌ RUIM - float/double perdem precisão
float preco = 100.50f;
float quantidade = 3f;
float total = preco * quantidade; // Pode ter erro de arredondamento!
```

---

### 8. Tratamento de Exceções

```
// ✅ BOM - Tratar apropriadamente
public void processarPedido(Integer pedidoId) {
    try {
        Pedido pedido = pedidoRepository.buscar(pedidoId);
        validarPedido(pedido);
        processar(pedido);

    } catch (PedidoInvalidoException e) {
        log.warn("Pedido inválido: {}", pedidoId, e);
        throw new BusinessException("Pedido não pode ser processado", e);

    } catch (Exception e) {
        log.error("Erro inesperado ao processar pedido: {}", pedidoId, e);
        throw new SystemException("Erro no processamento", e);
    }
}

// ❌ RUIM - Engolir exceção
public void processar() {
    try {
        // código
    } catch (Exception e) {
        // Não fazer nada - NUNCA!
    }
}

// ❌ RUIM - Catch genérico sem log
public void processar() {
    try {
        // código
    } catch (Exception e) {
        throw new RuntimeException("Erro"); // Perde stack trace original!
    }
}
```

---

### 9. Validações

```
// ✅ BOM - Validar entrada
public void criarUsuario(String nome, String email) {
    if (StringUtils.isEmpty(nome)) {
        throw new IllegalArgumentException("Nome é obrigatório");
    }

    if (StringUtils.isEmpty(email)) {
        throw new IllegalArgumentException("Email é obrigatório");
    }

    if (!EmailValidator.isValid(email)) {
        throw new IllegalArgumentException("Email inválido");
    }

    // Processar...
}
```

---

### 10. Documentação JavaDoc

```
/**
 * Processa um pedido de venda, validando estoque e emitindo nota fiscal.
 *
 * @param pedidoId ID do pedido a ser processado
 * @return Nota fiscal gerada
 * @throws PedidoNotFoundException se o pedido não for encontrado
 * @throws EstoqueInsuficienteException se não houver estoque disponível
 * @throws BusinessException para erros de negócio
 */
public NotaFiscal processarPedido(Integer pedidoId)
        throws PedidoNotFoundException, EstoqueInsuficienteException, BusinessException {
    // Implementação
}
```

---

## 📊 Checklist de Qualidade

Antes de fazer commit/merge, verifique:

### Código

- Código segue padrões de nomenclatura
- Imports organizados corretamente
- Sem warnings do compilador
- Sem código comentado desnecessário
- Logging apropriado implementado
- Tratamento de exceções adequado

### Testes

- Código testado manualmente
- Testes unitários criados (quando aplicável)
- Testes não quebram build existente

### Documentação

- JavaDoc atualizado para métodos públicos
- README atualizado (se necessário)
- Comentários explicativos em lógica complexa

### Git

- Mensagem de commit segue Conventional Commits
- Branch correta para tipo de mudança
- Merge para branches superiores quando necessário

### Performance

- Sem queries N+1
- Recursos fechados adequadamente
- Sem memory leaks evidentes

---

## 🔗 Referências

### Documentação Interna

- [README do Projeto](../README.md)
- [Diagramas de Arquitetura](./arquitetura-sankhya.excalidraw)

### Padrões Externos

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Java Code Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html)
- [Effective Java (Joshua Bloch)](https://www.oreilly.com/library/view/effective-java/9780134686097/)

### Ferramentas

- [Gradle](https://gradle.org/)
- [Lombok](https://projectlombok.org/)
- [SLF4J](http://www.slf4j.org/)

## 🔗 Recursos Adicionais

### Leitura Complementar

- [Clean Code: Boas práticas para criar métodos](como-cria-um-metodo)
- [Clean Code: Boas práticas para criar variáveis](como-criar-um-a-variavel)
- [Avaliação Preguiçosa](avaliacao-preguicosa)

---

## 📝 Notas Finais

Este documento é vivo e deve ser atualizado conforme o projeto evolui. Sugestões de melhorias são bem-vindas!

**Última atualização:** Fevereiro de 2026
**Mantenedores:** Time de Arquitetura SankhyaW

---

**Dúvidas ou sugestões?** Entre em contato com o time de arquitetura.
