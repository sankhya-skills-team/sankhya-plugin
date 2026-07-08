# Skill: sankhya-dicionario

Conhecimento avançado sobre o **dicionário de dados do Sankhya OM** extraído diretamente do banco Oracle de produção.

## O que cobre

- **~730 tabelas** mapeadas com campos, descrições, PKs, FKs e opções de campos
- Tabelas **TDD\*** — metamodelo interno (14 tabelas)
- Tabelas **TSI\*** — sistema/configuração (50 tabelas)
- Tabelas **TGF\*** — backoffice comercial/fiscal/financeiro (135 tabelas core + outros)
- Tabelas **TFP\*** — Folha de Pagamento / RH (265 tabelas)
- Tabelas **TCS\*** — CRM, OS, Contratos, Projetos
- Tabelas **TCB\*** — Contabilidade / Plano de Contas
- Tabelas **TGW\*** — WMS / Gestão de Armazém
- Tabelas **TIM\*** — Imobiliário
- Tabelas **TPR\*** — Produção / Manufatura
- Tabelas **TRI\*** — EFD-REINF
- Tabelas **TGA\*** — Agronegócio
- Tabelas **TSE\*** — Serasa / Bureau de Crédito
- Relacionamentos completos entre tabelas (chaves estrangeiras reais do banco)
- Enums/opções de campos (valores válidos para campos como `TIPMOV`, `RECDESP`, `CONFIRMADA`, etc.)
- Ligações lógicas (`TDDLIG`) e `entityName` para uso em `JapeFactory.dao()`

## Como foi gerada

A skill foi criada via extração direta do banco Oracle Sankhya OM (`SKCONTAINER` / `XE`):

| Fonte | Conteúdo |
|---|---|
| `TDDTAB` | Descrições de 3.119 tabelas do sistema |
| `TDDCAM` | Descrições de 42.076+ campos (tipo, tamanho, ordem) |
| `TDDOPC` + `TDDCAM` | Opções de campos (enums do sistema) |
| `TDDINS` | 1.636 instâncias com entityNames para JapeFactory |
| `TDDLIG` | 3.352 ligações lógicas entre instâncias |
| `TDDLGC` | 4.407 pares de campos de join |
| `ALL_CONS_COLUMNS` | Colunas de chaves primárias |
| `ALL_CONSTRAINTS` | Relacionamentos FK entre tabelas |

**Data da extração:** 2026-04-14  
**Banco:** Oracle XE — `localhost:1521` / schema `SKCONTAINER`  
**Container Docker:** `wildfly-docker-sankhya-skdev-oracle-addon-1`

## Estrutura dos Arquivos

```
sankhya-dicionario/
├── SKILL.md                           ← Skill principal (carregada automaticamente)
├── README.md                          ← Esta documentação
├── CONTEXT.md                         ← Estado atual e próximos passos
├── scripts/
│   ├── extract_and_generate.sh        ← Script de re-extração completa
│   └── gen_skill.py                   ← Gerador dos arquivos de referência
└── references/
    ├── tabelas-tdd.md                 ← 14 tabelas TDD (metamodelo interno) — 23KB
    ├── tabelas-tsi.md                 ← 50 tabelas TSI (sistema/configuração) — 48KB
    ├── tabelas-tgf-core.md            ← 22 tabelas TGF core — 72KB
    ├── tabelas-tgf-outros.md          ← 113 tabelas TGF complementares — 96KB
    ├── tabelas-relacionadas.md        ← Filhas/lookups de TGFCAB, TGFITE, TGFPAR — 40KB
    ├── tabelas-tcs-tcb.md             ← TCS (CRM/OS) + TCB (Contabilidade) — 43KB
    ├── tabelas-tgw-tim.md             ← TGW (WMS) + TIM (Imobiliário) — 60KB
    ├── tabelas-tpr-tri-tga.md         ← TPR (Produção) + TRI (REINF) + TGA (Agro) + TSE — 55KB
    ├── tabelas-ligacoes.md            ← TDDLIG + TDDINS + TDDLGC (entityNames) — 100KB
    └── tabelas-tfp.md                 ← 265 tabelas TFP (Folha de Pagamento / RH) — 252KB
```

**Total references:** ~800KB

## Tabelas Mais Importantes por Categoria

### Documentos Comerciais
| Tabela | Descrição | PK |
|---|---|---|
| `TGFCAB` | Cabeçalho de notas e pedidos | `NUNOTA` |
| `TGFITE` | Itens de nota | `NUNOTA`, `SEQUENCIA` |
| `TGFFIN` | Títulos financeiros | `NUFIN` |
| `TGFORD` | Ordens de carga | `ORDEMCARGA` |

### Cadastros Base
| Tabela | Descrição | PK | Refs |
|---|---|---|---|
| `TGFPAR` | Parceiros (clientes/fornecedores/motoristas) | `CODPARC` | 152 |
| `TGFPRO` | Produtos | `CODPROD` | 123 |
| `TGFEMP` | Empresa Financeiro | `CODEMP` | 102 |
| `TGFVEN` | Vendedores Representantes | `CODVEND` | 22 |
| `TGFCTT` | Contatos dos Parceiros | `CODCTTO` | 16 |
| `TGFVEI` | Veículos | `CODVEI` | 16 |

### Configuração Operacional
| Tabela | Descrição | PK | Refs |
|---|---|---|---|
| `TGFTOP` | Tipos de Operação | `CODTIPOPER` | 16 |
| `TGFNAT` | Natureza de Receitas e Despesas | `CODNAT` | 26 |
| `TGFLOC` | Locais de estoque | `CODLOCAL` | 39 |
| `TGFVOL` | Volumes/Unidades de medida | `CODVOL` | 29 |
| `TGFEST` | Estoque (posição) | composta | — |
| `TGFTIT` | Tipos de Título | `CODTIPTIT` | 16 |
| `TGFTAB` | Tabelas de Preço | `CODTAB` | — |
| `TGFNTA` | Nome das Tabelas de Preço | `CODTAB` | 30 |
| `TGFSER` | Série Produto | `CODSER` | — |
| `TGFCFO` | Código Fiscal de Operações (CFOP) | `CODCFO` | 13 |
| `TGFGRU` | Grupos de Produtos | `CODGRUPOPROD` | 12 |
| `TGFFAM` | Família de Produtos | `CODFAM` | — |

### Sistema (TSI)
| Tabela | Descrição | PK | Refs |
|---|---|---|---|
| `TSIUSU` | Usuários do sistema | `CODUSU` | 272 |
| `TSIEMP` | Empresas | `CODEMP` | 38 |
| `TSICTA` | Contas Bancárias | `CODCTABCOINT` | 32 |
| `TSICUS` | Centros de Resultado | `CODCENCUS` | 30 |
| `TSICID` | Cidades | `CODCID` | 29 |
| `TSIUFS` | Unidades Federativas | `UF` | 23 |
| `TSIBCO` | Bancos | `CODBCO` | 12 |
| `TSIBAI` | Bairros | `CODBAI` | — |
| `TSIEND` | Endereços | `CODEND` | — |
| `TSIGRU` | Grupos de usuários | `CODGRUPO` | — |
| `TSIPAR` | Parâmetros do sistema | — | — |

### Folha de Pagamento (TFP)
| Tabela | Descrição | PK |
|---|---|---|
| `TFPFUN` | Funcionários | `CODFUNC` |
| `TFPFOL` | Eventos da Folha | — |
| `TFPDEP` | Departamentos | `CODDEP` |
| `TFPCAR` | Cargos | `CODCAR` |
| `TFPLOT` | Lotações | `CODLOT` |
| `TFPHOR` | Carga Horária / Horários | `CODHOR` |
| `TFPFER` | Férias | — |
| `TFPPON` | Ponto | — |
| `TFPEVE` | Eventos | `CODEVE` |
| `TFPSIN` | Sindicatos | `CODSIN` |
| `TFPAFA` | Afastamentos | — |
| `TFPASO` | Atestado de Saúde Ocupacional | — |
| `TFPCAT` | CAT | — |
| `TFPAUD` | Auditoria E-Social | — |

### Metamodelo (TDD)
| Tabela | Descrição |
|---|---|
| `TDDTAB` | Descrições de todas as tabelas Sankhya |
| `TDDCAM` | Descrições de todos os campos |
| `TDDINS` | Instâncias (telas e formulários) |
| `TDDOPC` | Opções de campos (enums) |
| `TDDLIG` | Ligações entre tabelas (relacionamentos lógicos) |
| `TDDLGC` | Campos de ligação |
| `TDDREL` | Relacionamentos |
| `TDDPTH` | Paths de navegação |
| `TDDIAC` | Ações disponíveis |
| `TDDCRE` | Credenciais/permissões |
| `TDDPER` | Perfis de permissão |
| `TDDPCO` | Atributos de campo |
| `TDDPRE` | Preferências |
| `TDDEXP` | Exportações |

## Prefixos NÃO cobertos

| Prefixo | Motivo |
|---|---|
| `TRD*` | Apenas 2 tabelas no TDDCAM (TRDEAC, TRDBLC) — geradas dinamicamente |
| `CMD*` | Nenhuma tabela no TDDTAB neste banco — módulo não instalado |

## Como Atualizar

```bash
# Re-extração completa (TGF, TSI, TDD):
bash ~/.claude/skills/sankhya-dicionario/scripts/extract_and_generate.sh

# Re-extração TFP:
# Os scripts de extração estão documentados em /tmp/gen_tfp.py
# Conexão: SKCONTAINER/tecsis@localhost:1521/XE
# Container: wildfly-docker-sankhya-skdev-oracle-addon-1
```
