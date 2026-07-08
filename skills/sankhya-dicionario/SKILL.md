---
name: sankhya-dicionario
description: >
  Esta skill deve ser utilizada quando o usuário perguntar sobre estrutura de tabelas Sankhya,
  campos de TGFCAB, TGFPAR, TGFPRO, TGFFIN, TGFITE, TGFEST, TGFTOP, TGFNAT, TGFVEN, TSIUSU,
  TSIEMP, TSICID, TSIBCO, relacionamentos entre tabelas, chaves primárias e estrangeiras,
  significado de campos, opções de campos (enums), metamodelo TDDTAB/TDDCAM, dicionário de dados
  Sankhya, "qual tabela armazena X", "quais campos tem Y", "como relacionar A com B",
  "tabelas mais utilizadas", "estrutura do banco Sankhya", "campos adicionais AD_",
  "entityName para JapeFactory", "qual entityName usar", "ligações TDDLIG".
version: 1.1.0
---

# Dicionário de Dados Sankhya OM

Especialidade: estrutura interna do banco de dados Sankhya OM — tabelas, campos,
relacionamentos, PKs, FKs, enums e metamodelo.

**Base de conhecimento:** extraída diretamente do banco Oracle via `TDDTAB`, `TDDCAM`,
`TDDOPC`, `TDDINS`, `TDDLIG`, `TDDLGC` e `ALL_CONSTRAINTS` — ~730 tabelas, ~42.000 campos mapeados.

---

## Organização do Banco Sankhya OM

### Prefixos das Tabelas

| Prefixo | Domínio | Qtd aprox. |
|---|---|---|
| `TGF*` | Gestão Fiscal / Backoffice (comercial, financeiro, fiscal) | ~135+ |
| `TFP*` | Folha de Pagamento / Pessoal e RH | ~265 |
| `TSI*` | Sistema / Configuração (usuários, empresas, cidades, bancos) | ~50 |
| `TDD*` | Dicionário de Dados (metamodelo interno Sankhya) | ~14 |
| `TCS*` | CRM / Ordens de Serviço / Contratos / Projetos | — |
| `TCB*` | Contabilidade / Plano de Contas | — |
| `TGW*` | WMS — Gestão de Armazém | — |
| `TIM*` | Imobiliário | — |
| `TPR*` | Produção / Manufatura | — |
| `TRI*` | EFD-REINF | — |
| `TGA*` | Agronegócio | — |
| `TSE*` | Serasa / Bureau de Crédito | — |
| `AD_*` | Campos/tabelas adicionais (customizações) | — |

### Camadas de Importância

```
Críticas (núcleo):    TGFPAR, TGFPRO, TGFCAB, TGFITE, TGFFIN, TGFEMP
Operacionais:         TGFTOP, TGFNAT, TGFVEN, TGFEST, TGFLOC, TGFVOL, TGFORD
Configuração:         TSIUSU, TSIEMP, TSICID, TSIUFS, TSIBCO, TSIBAI, TSIEND
Tributário/Fiscal:    TGFCFO, TGFISS, TGFALI, TGFTCFOP, TGFPAEM
Preços:               TGFTAB, TGFNTA, TGFITE (VLRUNIT, VLRTOT)
Metamodelo:           TDDTAB, TDDCAM, TDDINS, TDDOPC, TDDLIG, TDDLGC
```

---

## Relacionamentos Centrais

```
TGFPAR (parceiro) ──────────────────────────────────┐
TSIEMP (empresa) ──────────────────────────────┐    │
TGFTOP (tipo operação) ─────────────────────┐  │    │
                                            │  │    │
TGFCAB (cabeçalho nota)  ←── CODEMP ────────┘  │    │
                          ←── CODPARC ─────────┘────┘
                          ←── CODTIPOPER ─────────────→ TGFTOP
                          ←── CODVEND ────────────────→ TGFVEN
                          │
                          └──→ TGFITE (itens)
                                ←── CODPROD ────────→ TGFPRO
                                ←── CODLOCAL ───────→ TGFLOC
                                ←── CODVOL ─────────→ TGFVOL
                          │
                          └──→ TGFFIN (financeiro/títulos)
                                ←── CODPARC ────────→ TGFPAR
                                ←── CODEMP ─────────→ TSIEMP

TGFEST (estoque):  CODPROD + CODLOCAL + CODEMP → posição de estoque
TSIUSU (usuário):  CODUSU → referenciado em TGFCAB.CODUSU, TGFITE, TGFFIN etc.
```

---

## Convenções do Banco Sankhya

### Tipos de Campos (TDDCAM.TIPCAMPO)

| Código | Tipo Oracle | Uso |
|---|---|---|
| `I` | NUMBER | Inteiro / FK / PK |
| `F` | NUMBER(p,s) | Decimal / monetário |
| `S` | VARCHAR2 | Texto / flag S/N / código |
| `D` | DATE | Data |
| `T` / `H` | DATE | Data+Hora (timestamp) |
| `L` | VARCHAR2(1) | Lógico: `S`=sim, `N`=não |
| `M` | CLOB | Memo / texto longo |
| `B` | BLOB | Binário / arquivo |

### Campos Padrão Presentes na Maioria das Tabelas

| Campo | Tipo | Significado |
|---|---|---|
| `CODEMP` | I | Código da empresa (FK → TSIEMP) |
| `CODUSU` | I | Usuário da última alteração (FK → TSIUSU) |
| `DTALTER` | H | Data/hora da última alteração |
| `DTINCLUSAO` | D | Data de inclusão do registro |
| `ADICIONAL` | S(1) | `S`=campo adicional customizado, `N`=nativo |

### Padrão de Flags S/N

A maioria dos campos booleanos usa `VARCHAR2(1)` com valores `'S'` (sim) e `'N'` (não).
Em `DynamicVO`, ler com `vo.asBoolean("CAMPO")` ou como String direta.

### Campos Adicionais (AD_)

Campos `AD_*` são customizações sobre tabelas nativas. Criados via:
- **Addon Studio:** `<nativeTable>` no `datadictionary/`
- **Módulo Java:** XML do Construtor de Telas

Prefixo `AD_` é **reservado pelo Sankhya** — addons devem usar prefixo próprio (ex: `SGT_`).

---

## Metamodelo TDD — Como Consultar

O próprio Sankhya armazena seu dicionário nas tabelas TDD. Consultas úteis:

```sql
-- Listar campos de uma tabela
SELECT NOMECAMPO, TIPCAMPO, TAMANHO, DESCRCAMPO
FROM TDDCAM WHERE NOMETAB = 'TGFCAB' ORDER BY ORDEM;

-- Descrição de uma tabela
SELECT DESCRTAB FROM TDDTAB WHERE NOMETAB = 'TGFCAB';

-- Opções de um campo (enum)
SELECT o.VALOR, o.OPCAO
FROM TDDOPC o JOIN TDDCAM c ON c.NUCAMPO = o.NUCAMPO
WHERE c.NOMETAB = 'TGFCAB' AND c.NOMECAMPO = 'TIPMOV';

-- Relacionamentos de uma tabela
SELECT * FROM TDDLIG WHERE NOMETAB = 'TGFCAB';
```

Para consultas em tempo real no banco Oracle local, usar o script `scripts/consultar-oracle.sh`.

---

## Guia de Navegação — Qual Arquivo Abrir

| Pergunta do usuário | Arquivo a consultar |
|---|---|
| "Qual tabela armazena X?" (backoffice) | `references/tabelas-tgf-core.md` + `references/tabelas-tgf-outros.md` |
| "Quais campos tem TGFCAB/TGFPAR/TGFPRO?" | `references/tabelas-tgf-core.md` |
| "Como relacionar parceiro com nota?" | TGFCAB.CODPARC → TGFPAR.CODPARC (diagrama acima) |
| "O que é TDDCAM / TDDTAB?" | `references/tabelas-tdd.md` |
| "Quais opções o campo TIPMOV aceita?" | `references/tabelas-tgf-core.md` seção TGFCAB |
| "Quais tabelas TGF existem além das core?" | `references/tabelas-tgf-outros.md` |
| "Qual entityName usar no JapeFactory?" | `references/tabelas-ligacoes.md` |
| "Tabelas de usuário, empresa, cidade, banco" | `references/tabelas-tsi.md` |
| "Tabelas de folha de pagamento / RH" | `references/tabelas-tfp.md` |
| "CRM, OS, contratos, projetos" | `references/tabelas-tcs-tcb.md` |
| "Contabilidade, plano de contas" | `references/tabelas-tcs-tcb.md` |
| "WMS, armazém, endereçamento" | `references/tabelas-tgw-tim.md` |
| "Produção, manufatura, ordens de produção" | `references/tabelas-tpr-tri-tga.md` |
| "Filhas/lookups de TGFCAB, TGFITE, TGFPAR" | `references/tabelas-relacionadas.md` |

### Padrões de Grep para Arquivos Grandes

Os arquivos abaixo excedem 10k palavras. Para localizar uma tabela específica sem carregar
o arquivo inteiro, usar o Grep antes de ler:

```
# Em tabelas-tfp.md (45k palavras — 265 tabelas TFP):
grep -n "^## TFPFUN\|^## TFPFOL\|^## TFPCAR" references/tabelas-tfp.md

# Em tabelas-tgf-outros.md (16k palavras — 113 tabelas TGF):
grep -n "^## TGFICM\|^## TGFISS\|^## NOME_TABELA" references/tabelas-tgf-outros.md

# Em tabelas-ligacoes.md (15k palavras — entityNames):
grep -n "entityName\|^## TGFCAB\|JapeFactory" references/tabelas-ligacoes.md

# Em tabelas-tgf-core.md (12k palavras — tabelas core):
grep -n "^## TGF\|^### TGF\|CODPARC\|NUNOTA" references/tabelas-tgf-core.md
```

---

## Consulta ao Banco Oracle em Tempo Real

Para tabelas não cobertas pelos arquivos de referência ou para dados frescos:

```bash
# Buscar campos de qualquer tabela diretamente no Oracle
bash ~/.claude/skills/sankhya-dicionario/scripts/consultar-oracle.sh TGFCAB

# Buscar opções de um campo
bash ~/.claude/skills/sankhya-dicionario/scripts/consultar-oracle.sh TGFCAB TIPMOV
```

O script conecta via `docker exec` no container `wildfly-docker-sankhya-skdev-oracle-addon-1`.

---

## Manutenção — Como Regenerar o Dicionário

```bash
# Re-extração completa (TGF, TSI, TDD, TCS, TCB, TGW, TIM, TPR, TRI, TGA, TSE):
bash ~/.claude/skills/sankhya-dicionario/scripts/extract_and_generate.sh

# Conexão Oracle: SKCONTAINER/tecsis@localhost:1521/XE
# Container: wildfly-docker-sankhya-skdev-oracle-addon-1
```

Ver `README.md` para detalhes completos de cobertura e fontes de extração.

---

## Uso por Outras Skills Sankhya

Esta skill é o repositório central de estrutura do banco Sankhya OM. As demais skills do
ecossistema devem consultá-la sempre que precisarem de:

- Campos de uma tabela (nomes, tipos, tamanhos, ordem)
- PKs, FKs e relacionamentos entre tabelas
- Opções de campos (enums via TDDOPC)
- `entityName` para uso em `JapeFactory.dao()`
- Validação de existência de tabelas ou campos antes de gerar código ou queries

**Skills que devem usar sankhya-dicionario como fonte primária:**
- **`sankhya-addon`** — campos de `<nativeTable>`, entityNames, validação de tabelas nativas
- **`sankhya-modulo-java`** — estrutura de entidades, campos TGFCAB/TGFITE/TGFFIN/TGFPAR
- **`sankhya-bi`** — validação de campos nas queries SQL dos gadgets antes de gerar XML
- **`sankhya-estimativa-planejador`** — validação de entidades e campos Sankhya citados no escopo
- **`sankhya-doc-entrega`** — nomes corretos de campos persistidos ao documentar entregas

---

## Armadilhas Comuns

### Coluna física ≠ campo do dicionário da instância (EntityName)

Uma coluna existir na tabela (visível em `describe_table` / `TDDCAM` da tabela) **não** garante que
ela esteja exposta como campo do **dicionário de uma instância** (EntityName). Cargas via
`CRUDServiceProvider.loadRecords`, `MetadataProvider` e metadados só enxergam os campos do
dicionário da instância, não as colunas físicas cruas.

Pedir um campo que é coluna física mas **não** é campo do DD da instância (ex.: `TGFITE.PESO`
na entidade `ItemNota`) falha com `CORE_E04064 "Descritor do campo inválido"`.

> Para esses casos, use **SQL nativo num Service backend** em vez de carga por entidade.

### Validar o EntityName antes de usar

Antes de `JapeFactory.dao("<EntityName>")` ou `instanceName="<EntityName>"`, confirme que a
instância existe no dicionário (via `search_entities` ou `TDDINS`). EntityName inexistente/placeholder
passa pelo deploy e estoura **em runtime**:

```
Não foi encontrado objeto de acesso a dados para este BMP: mge-dwf:<EntityName>
```

Exemplo real: usaram `ContratoComercializacao` (inexistente) quando a tabela `TCSCON` expõe
`Contrato`, `ContratoArmazenagemGeral` e `ContradosOrigem`. **A mesma tabela pode ter várias
instâncias com filtros diferentes** — escolha a correta para o caso de negócio.

---

## Referências

| Conteúdo | Arquivo |
|---|---|
| Metamodelo interno (TDDTAB, TDDCAM, TDDINS, TDDOPC, TDDLIG...) + instâncias | `references/tabelas-tdd.md` |
| Sistema/configuração (TSIUSU, TSIEMP, TSICID, TSIBCO, TSIBAI...) | `references/tabelas-tsi.md` |
| TGF core (TGFPAR, TGFPRO, TGFCAB, TGFITE, TGFFIN, TGFEMP...) | `references/tabelas-tgf-core.md` |
| TGF complementares (fiscal, MDF-e, NF-e, comissões, tarefas...) | `references/tabelas-tgf-outros.md` |
| Filhas/lookup de TGFCAB, TGFITE e TGFPAR (TGFICM, TGFTPP, TSIMOE...) | `references/tabelas-relacionadas.md` |
| TCS (CRM/OS/Contratos/Projetos) e TCB (Contabilidade/Plano de Contas) | `references/tabelas-tcs-tcb.md` |
| TGW (WMS/Armazém) e TIM (Imobiliário) | `references/tabelas-tgw-tim.md` |
| TPR (Produção/Manufatura), TRI (EFD-REINF), TGA (Agronegócio) e TSE (Serasa) | `references/tabelas-tpr-tri-tga.md` |
| Ligações lógicas TDDLIG + instâncias TDDINS + TDDLGC (entityNames para JapeFactory) | `references/tabelas-ligacoes.md` |
| Folha de Pagamento e RH (TFPFUN, TFPFOL, TFPCAR, TFPDEP, TFPFER, TFPPON...) | `references/tabelas-tfp.md` |
