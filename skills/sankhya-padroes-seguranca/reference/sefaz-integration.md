# SEFAZ — Padrões de Segurança na Integração

A integração com a SEFAZ estadual (NFe, NFSe, NFCe, CT-e, MDFe) tem requisitos de segurança específicos pela natureza fiscal. Vazar a chave privada do certificado permite emitir documentos em nome do emitente — fraude fiscal direta.

## Certificado digital

### Tipos
- **A1** — arquivo `.pfx` ou `.p12` com chave privada protegida por senha. Validade de 1 ano.
- **A3** — em hardware (smart card, token USB). Validade de 1 a 3 anos. Não extraível por design.

### Armazenamento seguro

**A1:**
- Arquivo em filesystem com permissão 0600 (só o usuário do processo lê)
- Senha em Secrets Manager, NUNCA em arquivo de config commitado
- Backup encriptado em storage seguro (S3 com SSE-KMS)
- Certificado isolado por cliente/tenant — não compartilhar arquivo entre clientes

**A3:**
- Driver PKCS#11 configurado no host
- Acesso físico ao host controlado (datacenter)
- Uso via biblioteca que não extrai a chave (ex: SunPKCS11 no Java)

### Validade e rotação
- Monitorar a expiração com alerta 30 dias antes
- Renovação automatizada onde possível; caso contrário, runbook documentado
- Ao renovar, revogar o antigo se houve suspeita de comprometimento

## Assinatura XML

### Padrão
XMLDSig (XML Digital Signature, W3C) conforme o layout da SEFAZ. Campos assinados:
- `<NFe>` ou o elemento raiz do documento
- Canonicalization C14N
- Signature method: `rsa-sha1` (legado ainda aceito pela SEFAZ em alguns estados; rsa-sha256 preferido quando suportado)
- Transforms: `enveloped-signature` + `c14n`

### Validação

Antes de aceitar a resposta da SEFAZ:
1. Validar o schema XSD oficial
2. Validar a assinatura da SEFAZ (certificado SEFAZ conhecido, chain válida até a ICP-Brasil)
3. Validar que o protocolo de autorização bate com a NF enviada

### Vulnerabilidade comum: XXE no parse

A SEFAZ responde XML. Parser sem proteção permite XXE:
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
```

Parser SEGURO (Java):
```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
factory.setFeature("http://xml.org/sax/features/external-general-entities", false);
factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
factory.setXIncludeAware(false);
factory.setExpandEntityReferences(false);
```

## Chave privada em memória

### Problema

Chave em memória por muito tempo aumenta a janela de vazamento via heap dump, core dump ou exploit de RCE.

### Padrões seguros

- Carregar a chave por operação (emitir nota → carrega → emite → descarta)
- Se precisar manter (alto volume), usar provedor PKCS#11 que mantém a chave fora do heap da JVM
- Nunca logar objeto `PrivateKey` ou `KeyStore`
- `KeyStore` nunca exposto por endpoint (inclui JMX, actuator, admin UI)

## Ambientes SEFAZ

- **Produção (1)** — emissão real, eventos fiscais
- **Homologação (2)** — sandbox para teste, documentos sem validade fiscal

Uma variável de ambiente explícita controla o ambiente; erro de configuração que manda documento de homologação para a SEFAZ de produção causa rejeição (ou pior, emite documento de teste como fiscal). Testes automatizados devem forçar `tpAmb=2`.

## Comunicação

- HTTPS com TLS 1.2+ obrigatório (a SEFAZ não aceita menos)
- O certificado da SEFAZ muda entre estados — cadeia confiável ICP-Brasil
- Timeout generoso (a SEFAZ às vezes demora) — mínimo 30s; máximo 120s
- Retry com backoff em erros 500 ou timeout; não fazer retry em rejeição lógica (CStat != 100)

## Audit trail

Cada operação fiscal (emitir, cancelar, inutilizar) exige log auditável:
- Usuário operador
- Timestamp UTC
- Chave de acesso do documento
- CStat e xMotivo da SEFAZ
- Arquivo assinado (XML) armazenado imutavelmente (S3 Object Lock)

Guarda mínima: 5 anos após a emissão (art. 195, CTN — prazo decadencial).

## Checklist para review

- [ ] Certificado A1 em filesystem 0600, senha em secrets manager
- [ ] Parser XML com XXE desabilitado
- [ ] Chain da SEFAZ validada antes de aceitar a resposta
- [ ] Ambiente (produção/homologação) configurado por env var
- [ ] Chave privada não cacheada com duração longa
- [ ] Log de operação fiscal com retenção >= 5 anos
- [ ] XML assinado armazenado imutavelmente
- [ ] Teste automatizado roda em tpAmb=2 sempre
