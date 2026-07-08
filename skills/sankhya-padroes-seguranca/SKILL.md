---
name: sankhya-padroes-seguranca
description: Use ao revisar, escrever ou triar código Java do Sankhya EIP quando o foco envolver vulnerabilidades específicas da plataforma — bypass de contexto de tenant/usuário em chamadas inter-módulo via Dynamic Proxy, SQL injection em NativeSql sem bind parameters, desserialização insegura em EntityFacade, validação de cadeia de certificados SEFAZ (A1/A3), mascaramento de PAN e não-persistência de CVV em PDV/PCI, e audit trail obrigatório em operações críticas. Invocar sempre que o código em foco usar `DynamicProxy.getFor`, `NativeSql` com concatenação de strings, `EntityFacade` com input externo, integrações SEFAZ/NF-e, fluxos de cartão no PDV ou pontos de auditoria de operações financeiras. Cobre o que scanner genérico OWASP não pega: conhecimento proprietário da plataforma.
paths: "**/src/**/*.java, **/*Service*.java, **/*Facade*.java, **/*Controller*.java, **/webservices/**"
---

# Sankhya EIP — Padrões de Segurança

Padrões de vulnerabilidade **específicos** da plataforma Sankhya EIP (SankhyaOM ERP, módulos, add-ons, PDV Varejo). Complementa a análise genérica OWASP Top 10 com conhecimento proprietário que nenhum scanner ou agent nativo conhece.

Para o contexto de persistência, usar em conjunto com a skill [sankhya-jape](../sankhya-jape/SKILL.md). Duas dependências ficam fora deste plugin e são descritas inline onde aparecem: o mecanismo de chamada inter-módulo via Dynamic Proxy (uma camada de proxy que resolve e invoca a service de outro módulo em runtime) e o stack SankhyaOM (o conjunto EJB/JAPE/EntityFacade sobre o qual os módulos rodam).

Integração SEFAZ detalhada em [reference/sefaz-integration.md](reference/sefaz-integration.md).

---

## 1. Bypass de contexto de tenant/usuário em chamadas inter-módulo

**Padrão vulnerável:** o módulo A chama o módulo B via Dynamic Proxy inter-módulo, mas B não valida que o usuário em contexto tem permissão em B.

Se A é de uso geral (ex: nota fiscal) e B é restrito (ex: financeiro), o usuário com acesso a A opera em B pela chamada inter-módulo sem ser barrado.

**Detecção:** procurar por `DynamicProxy.getFor(...)` ou equivalentes e verificar se o método chamado valida autorização logo no início.

**Correção:** toda service exposta via proxy inter-módulo começa com verificação de autorização (`UserContextManager` + checagem de módulo/recurso).

**Severidade típica:** HIGH (privilege escalation intra-aplicação).

---

## 2. SQL injection em NativeSql

`JapeSession` permite `NativeSql` para queries complexas. SQL montado por concatenação com input do usuário é vulnerável.

**Vulnerável:**
```java
NativeSql sql = new NativeSql(jape);
sql.appendSql("SELECT * FROM TGFCAB WHERE NUNOTA = " + userInput);
```

**Seguro:**
```java
NativeSql sql = new NativeSql(jape);
sql.appendSql("SELECT * FROM TGFCAB WHERE NUNOTA = ?");
sql.setNamedParameter("nunota", userInput);   // ou setLong(1, ...) conforme API
```

**Detecção:** grep por `appendSql` seguido de concatenação com variável. Verificar ausência de `setNamedParameter` / `setLong` / `setString` por perto.

O mesmo padrão vale para `EntityFacade.executeQuery(String)` e `Sql.execute(String)`.

**Severidade típica:** HIGH a CRITICAL (SQL injection com acesso direto ao banco do ERP).

---

## 3. Desserialização insegura em EntityFacade / WebService legado

`ServiceProxy` e alguns endpoints legados aceitam payload serializado. Desserializar sem validar a classe permite RCE quando o codebase tem classes gadget.

**Vulnerável:** `ObjectInputStream` sem filtro de classes permitidas.

**Correção:** usar JSON (Jackson com `StdTypeResolverBuilder` configurado) ou whitelist explícita via `ObjectInputFilter`.

**Severidade típica:** CRITICAL (RCE).

---

## 4. Audit trail ausente em operações críticas

Operações que alteram dados fiscais, financeiros ou de estoque exigem trilha:
- Cancelamento de nota fiscal
- Estorno de pagamento
- Ajuste de estoque
- Alteração de preço por usuário final (não por job automático)
- Alteração de permissão de usuário

**Padrão Sankhya:** usar `AuditLogService` (ou equivalente no módulo) com os campos: usuário, timestamp, registro afetado, campo antes, campo depois, justificativa (quando aplicável).

**Detecção:** métodos em services que fazem `update` em tabelas críticas (TGFCAB, TCSFAT, TGFFIN, TSIUSU, TSIACU) sem chamada a audit.

**Severidade típica:** MEDIUM (a ausência impede forensics e viola compliance fiscal/SOX quando aplicável).

---

## 5. WebService com acesso público

Endpoints `.rm` / `.mge` publicados sem autenticação ou com autenticação fraca permitem chamada direta.

**Padrão Sankhya:** todo WS valida autenticação via `ServiceProxy` com sessão válida. Método `public` no controller sem `@RequireSession` ou equivalente é risco.

**Correção:** centralizar o gate de autenticação no `WebServicesFacade` / `ServicePoolResolver`; negar por default.

**Severidade típica:** CRITICAL quando expõe operações de escrita; HIGH quando expõe leitura de dados sensíveis.

---

## 6. Armazenamento de senhas em TSIUSU (ou equivalente)

Verificar se o campo de senha usa hash forte. Sistemas legados às vezes ainda têm MD5 ou SHA-1.

**Padrão aceitável atual:** bcrypt (cost >= 12) ou PBKDF2 (>= 600k iterações).

**Migração:** ao detectar hash fraco em produção, planejar migração transparente — rehash no próximo login bem-sucedido.

---

## 7. PDV (Varejo) — PCI-DSS no checkout

**Padrões críticos:**

- **CVV nunca persistido** — validar que não está em tabela de histórico, log de transação ou backup
- **PAN mascarado** em displays (ticket impresso, tela, relatório): `************1234`
- **Tokenização** — preferir integração com TEF/maquininha que retorna token, não manipular PAN no app
- **Tracks magnéticos** — dados de Track 1/Track 2 nunca armazenados pós-autorização

**Detecção:**
- grep por nome de campo: `cvv`, `cvc`, `cav`, `cvv2`, `trackdata`
- Verificar se aparece em log: `log.info(...)` com objetos de pagamento inteiros
- Relatórios de transação: verificar se o PAN completo aparece

**Severidade típica:** CRITICAL (violação de PCI-DSS com multa; vazar cartão = fraude imediata).

O checklist PCI-DSS de referência exige: PAN mascarado em toda exibição, CVV/CVC nunca persistido e tracks magnéticos descartados após a autorização.

---

## 8. SEFAZ — certificado e assinatura

Resumo (detalhes na referência):

- Certificado A1 em arquivo `.pfx` — acesso restrito, não commitar
- Certificado A3 em token/smartcard — acesso físico ao host
- Chave privada NUNCA cacheada em memória global com duração longa — recarregar por operação ou por sessão curta
- Validar a chain do certificado SEFAZ antes de aceitar a resposta
- Assinatura XMLDSig conforme padrão SEFAZ/ICP-Brasil

**Severidade típica:** CRITICAL se a chave privada vaza (o atacante emite nota em nome do emitente).

---

## 9. Upload de anexos e arquivos

O padrão Sankhya permite anexar arquivos a registros (ordem de serviço, chamado, etc.).

**Vulnerabilidades típicas:**
- Ausência de validação de tipo MIME (permite upload de `.html` com XSS ou `.jsp` com RCE no container servlet)
- Armazenamento no filesystem com o nome original do usuário (path traversal)
- Servir o arquivo com `Content-Type` inferido pelo browser — `.html` executa

**Correção:**
- Whitelist de extensões e MIME
- Renomear para UUID no servidor; preservar o nome original só em metadata
- Servir sempre com `Content-Disposition: attachment` ou via bucket separado do domínio principal
- Antivírus scan opcional (ClamAV)

---

## 10. Checklist de review para PR em SankhyaEIP

O agent `security-auditor` aplica em cada PR que toca `sankhyaeip`:

- [ ] NativeSql sem bind parameters?
- [ ] Service pública via proxy inter-módulo sem verificação de permissão?
- [ ] WebService novo tem gate de sessão?
- [ ] Audit trail em operação crítica adicionada/mantida?
- [ ] PDV: CVV/PAN manipulado conforme PCI?
- [ ] SEFAZ: chave privada em memória por tempo limitado?
- [ ] Upload de arquivo: whitelist + renomeação + content-disposition?
- [ ] Hash de senha em bcrypt/argon2?
- [ ] Dados pessoais (CPF, email) com máscara em log?
