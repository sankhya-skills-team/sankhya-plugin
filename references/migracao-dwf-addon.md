# Migração DWF → Add-on Studio

> Fonte oficial: https://developer.sankhya.com.br/docs/migrando-extensoes-que-usam-o-dwf-para-o-add-on-studio
> Usar quando a estimativa indicar **conversão de extensão legada/terceiro** (ver
> `sankhya-estimativa-planejador/references/addon-vs-modulo-java.md`).

## Motivação

Migrar extensões DWF (legado) para Add-on Studio elimina dependência de
ferramental obsoleto e moderniza a manutenção.

## Pré-requisitos

- Backup completo do dicionário de dados legado (`metadata.xml`).
- Acesso total ao código-fonte da extensão.

## Fase 1 — Setup do projeto

- Criar solução no Portal do Desenvolvedor (ou reaproveitar existente).
- Baixar e configurar o template do Add-on Studio.
- Estrutura esperada: `datadictionary/`, `dbscripts/`, `model/` (backend),
  `vc/` (frontend).

## Fase 2 — Importar Dicionário de Dados

1. Localizar arquivos legados: normalmente
   `meu-projeto.war/WEB-INF/dictionary/metadata.xml` e os scripts SQL.
2. Rodar a task de conversão:

```bash
./gradlew importAndConvertDD \
  -PlocationMetadata=/caminho/metadata.xml \
  -PlocationScripts=/caminho/scripts/
```

3. A ferramenta converte e organiza os metadados em XMLs contextuais (menus,
   tabelas customizadas, extensões de nativas).

## Fase 3 — Migrar código

- Transportar a estrutura de pacotes Java mantendo a hierarquia.
- Copiar os resources do projeto legado.
- Adaptar ao novo padrão arquitetural (anotações Addon Studio).

### Equivalências de API (legado → Addon Studio)

| DWF / Módulo legado | Add-on Studio |
|---|---|
| `EventoProgramavelJava` (event-listener no XML) | `@Listener` |
| `AcaoRotinaJava` (botão de ação) | `@ActionButton` |
| `RegraNegocioJava` | `@BusinessRule` |
| `ScheduledAction` | `@Job` |
| Serviço SP registrado manualmente | `@Service` + `service-providers.xml` |
| Acesso a dados ad-hoc | JAPE (`EntityFacade`/`JapeFactory`) — ver `jape.md` |

## Problemas comuns

| Problema | Causa | Solução |
|---|---|---|
| Erro de chave primária ausente | Tabela convertida sem PK | Adicionar `<primaryKey><field name="X"/></primaryKey>` ao XML |
| Metadata inválido | Caminho errado ou XML corrompido | Conferir local e validade do XML |
| Pasta de scripts ausente | Diretório inexistente/vazio | Garantir `mssqlserver.sql` e `oracle.sql` no diretório |

## Boas práticas

- Backup antes de começar; migrar **incrementalmente por feature**.
- Usar **DTOs** na I/O dos serviços, não expor entidades.
- Aproveitar a migração para modernizar a arquitetura.
- Versionar com Git desde o início.
- Evitar prefixo `AD_` em tabelas novas do addon (reservado internamente ao ERP) —
  usar a nomenclatura própria do addon.
- Testar funcionalidade crítica antes de produção.
