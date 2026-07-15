# Segurança — Padrões Específicos do Sankhya

Padrões de vulnerabilidade próprios do ecossistema Sankhya (OM, módulos, add-ons, PDV Varejo). Complementa OWASP genérico com conhecimento que nenhum scanner identifica sozinho. Aplique ao escrever, revisar ou triar código Java que toca persistência, web services, dados fiscais/financeiros ou cartão.

---

## 1. Validação de permissão ao chamar módulo restrito

**Padrão vulnerável:** uma rotina de uso geral (ex: nota fiscal) aciona operação de módulo restrito (ex: financeiro) e o serviço chamado não revalida se o usuário em contexto tem permissão naquele recurso. Usuário com acesso só à rotina geral acaba operando no módulo restrito.

**Detecção:** procure por `DynamicProxy.getFor(...)` (chamada inter-módulo via Dynamic Proxy) e verifique se o método invocado valida autorização logo no início.

**Correção:** toda operação sensível começa validando autorização do usuário corrente (`MGEAuthorizationManager` / `UserContextManager` + checagem de módulo/recurso). Não confie em quem chamou; valide no início do método.

**Severidade típica:** ALTA (escalonamento de privilégio dentro da aplicação).

---

## 2. SQL injection em NativeSql

`JapeSession` permite `NativeSql` para queries complexas. Montar o SQL por concatenação com input do usuário é injeção direta no banco do ERP.

**Vulnerável:**
```java
NativeSql sql = new NativeSql(jape);
sql.appendSql("SELECT * FROM TGFCAB WHERE NUNOTA = " + entradaUsuario);
```

**Seguro:**
```java
NativeSql sql = new NativeSql(jape);
sql.appendSql("SELECT * FROM TGFCAB WHERE NUNOTA = :NUNOTA");
sql.setNamedParameter("NUNOTA", entradaUsuario);   // ou setLong/setString conforme o tipo
```

**Detecção:** procure `appendSql` seguido de concatenação com variável e ausência de `setNamedParameter`/`setLong`/`setString` por perto. Mesmo cuidado vale para `EntityFacade.executeQuery(String)` e qualquer execução de SQL montado como String.

**Severidade típica:** ALTA a CRÍTICA.

---

## 3. Desserialização insegura

Endpoints legados e alguns mecanismos de WebService aceitam payload serializado. `ObjectInputStream` sem filtro de classes permite RCE se houver classe gadget no classpath.

**Correção:** prefira JSON (Jackson configurado) ou whitelist explícita de classes via `ObjectInputFilter`. Nunca desserialize objeto Java arbitrário vindo de fora.

**Severidade típica:** CRÍTICA (RCE).

---

## 4. Audit trail ausente em operação crítica

Operações que alteram dados fiscais, financeiros ou de estoque exigem trilha de auditoria:

- Cancelamento de nota fiscal
- Estorno de pagamento
- Ajuste de estoque
- Alteração de preço por usuário final (não por job automático)
- Alteração de permissão de usuário

**Padrão:** registrar usuário, timestamp, registro afetado, valor antes, valor depois e justificativa (quando aplicável).

**Detecção:** métodos que fazem `update` em tabelas críticas (`TGFCAB`, `TCSFAT`, `TGFFIN`, `TSIUSU`, `TSIACU`) sem registro de auditoria.

**Severidade típica:** MÉDIA (ausência impede forense e viola compliance fiscal/SOX quando aplicável).

---

## 5. WebService com acesso público

Endpoints `.rm` / `.mge` publicados sem autenticação (ou com autenticação fraca) permitem chamada direta.

**Padrão:** todo WS valida sessão ativa via `ServiceProxy`. Método `public` em controller sem gate de sessão é risco. Centralize o gate e negue por padrão (fail-closed).

**Severidade típica:** CRÍTICA quando expõe escrita; ALTA quando expõe leitura de dado sensível.

---

## 6. Hash de senha fraco

Verifique o hash do campo de senha em `TSIUSU` (ou equivalente). Sistemas legados às vezes usam MD5 ou SHA-1.

**Aceitável atual:** bcrypt (cost ≥ 12), Argon2 ou PBKDF2 (≥ 600k iterações).

**Migração:** ao detectar hash fraco em produção, faça rehash transparente no próximo login bem-sucedido.

---

## 7. PDV (Varejo) — PCI-DSS no checkout

- **CVV nunca persistido** — não pode estar em tabela de histórico, log de transação nem backup.
- **PAN mascarado** em qualquer exibição (ticket, tela, relatório): `************1234`.
- **Tokenização** — prefira integração com TEF/maquininha que devolve token; não manipule o PAN no app.
- **Tracks magnéticos** (Track 1/Track 2) nunca armazenados após autorização.

**Detecção:**
- grep por nomes de campo: `cvv`, `cvc`, `cav`, `cvv2`, `trackdata`.
- objetos de pagamento inteiros em `log.info(...)`.
- relatórios de transação exibindo PAN completo.

**Severidade típica:** CRÍTICA (violação PCI-DSS com multa; vazamento de cartão = fraude imediata).

---

## 8. SEFAZ — certificado e assinatura

- Certificado A1 (`.pfx`): acesso restrito, **nunca commitar**.
- Certificado A3 (token/smartcard): acesso físico ao host.
- Chave privada **nunca** cacheada em memória global de longa duração — recarregue por operação ou sessão curta.
- Valide a cadeia do certificado SEFAZ antes de aceitar resposta.
- Assinatura XMLDSig conforme padrão SEFAZ/ICP-Brasil.

**Severidade típica:** CRÍTICA se a chave privada vazar (atacante emite nota em nome do emitente).

---

## 9. Upload de anexos

A plataforma permite anexar arquivos a registros (ordem de serviço, chamado, etc.).

**Vulnerabilidades típicas:**
- Sem validação de tipo MIME → upload de `.html` com XSS ou `.jsp` com RCE no container servlet.
- Armazenamento com o nome original do usuário → path traversal.
- Servir o arquivo com `Content-Type` inferido pelo browser → `.html` executa.

**Correção:**
- Whitelist de extensões e MIME.
- Renomear para UUID no servidor; preservar o nome original só em metadado.
- Servir sempre com `Content-Disposition: attachment` (ou via domínio/bucket separado).
- Antivírus opcional (ClamAV).

---

## 10. Checklist de review para PR Sankhya

- [ ] `NativeSql` sem bind parameters?
- [ ] Operação em módulo restrito sem revalidar permissão?
- [ ] WebService novo com gate de sessão?
- [ ] Audit trail em operação crítica mantido/adicionado?
- [ ] PDV: CVV/PAN tratados conforme PCI?
- [ ] SEFAZ: chave privada em memória por tempo limitado?
- [ ] Upload: whitelist + renomeação + content-disposition?
- [ ] Hash de senha em bcrypt/Argon2?
- [ ] Dado pessoal (CPF, e-mail) mascarado em log?

---

## Fonte

Adaptado de `snk-ai-registry` (Sankhya AI Prompt Registry) — skill `sankhyaeip-security-patterns`.
