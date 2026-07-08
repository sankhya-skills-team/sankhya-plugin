# CONTEXT — Estado da Skill sankhya-dicionario

## Estado Atual (2026-04-14)

**Cobertura:**
- ~730+ tabelas mapeadas
- 10 arquivos de referência (~885KB total)
- Fontes: TDDTAB, TDDCAM, TDDOPC, ALL_CONSTRAINTS, TDDINS, TDDLIG, TDDLGC

**Arquivos gerados:**

| Arquivo | Conteúdo | Tamanho |
|---|---|---|
| `tabelas-tdd.md` | 14 TDD (metamodelo) + mapa de instâncias | 22KB |
| `tabelas-tsi.md` | 50 TSI (usuários, empresas, cidades...) | 47KB |
| `tabelas-tgf-core.md` | 22 TGF core (CAB, ITE, FIN, PAR, PRO...) | 71KB |
| `tabelas-tgf-outros.md` | 113 TGF complementares | 95KB |
| `tabelas-relacionadas.md` | Filhas/lookups de TGFCAB, TGFITE, TGFPAR | 39KB |
| `tabelas-tcs-tcb.md` | TCS (CRM/OS/Contratos) + TCB (Contabilidade) | 42KB |
| `tabelas-tgw-tim.md` | TGW (WMS) + TIM (Imobiliário) | 59KB |
| `tabelas-tpr-tri-tga.md` | TPR (Produção) + TRI (REINF) + TGA (Agro) + TSE (Serasa) | 54KB |
| `tabelas-ligacoes.md` | TDDLIG + TDDINS + TDDLGC (entityNames) | 100KB |
| `tabelas-tfp.md` | TFP (Folha de Pagamento / RH) — 265 tabelas | 252KB |

**Prefixos cobertos:** TDD, TSI, TGF, TCS, TCB, TGW, TGC, TIM, TPR, TRI, TGA, TSE, **TFP**

---

## Pendentes / Próximas Adições

### Prefixos sem cobertura (confirmados com baixa/nula presença no TDDCAM)

| Prefixo | Qtd TDDTAB | Status |
|---|---|---|
| `TRD*` | 2 | Apenas TRDEAC e TRDBLC no dicionário — geradas dinamicamente |
| `CMD*` | 0 | Nenhuma tabela no TDDTAB neste banco |

### Tabelas relacionadas ainda não mapeadas com ligações completas

- `TGFFIN` (Financeiro) → TSICTA, TGFTIT, TGFNAT como lookups — ligações em `tabelas-ligacoes.md` mas sem seções detalhadas
- `TGFPRO` (Produto) → grupos, famílias, séries, unidades
- `TGFTOP` (Tipo de Operação) → tributação, CFOP, alíquotas

---

## Processo de Atualização

```bash
# Para re-extrair tudo (TGF/TSI/TDD):
bash ~/.claude/skills/sankhya-dicionario/scripts/extract_and_generate.sh

# Para regenerar TFP:
# 1. Rodar as queries de extração TFP no docker:
docker exec wildfly-docker-sankhya-skdev-oracle-addon-1 bash -c "..." > /tmp/sk_tables_tfp.txt
# (ver queries em /tmp/gen_tfp.py — seção de extração)

# 2. Gerar o arquivo:
python3 /tmp/gen_tfp.py
```

---

## Notas Técnicas

- **Encoding Oracle:** sqlplus retorna `?` para acentos. A função `fix()` em `gen_skill.py` faz substituição parcial — não é perfeito mas é legível.
- **Tabelas `_RP_`:** backups de migration — excluir sempre nas queries.
- **Python oracledb:** thin mode não suporta esta versão Oracle. Usar sqlplus via `docker exec`.
- **TDDCAM.SISTEMA:** não usar como filtro — retorna 0 neste banco.
- **TRD*:** apenas 2 tabelas no dicionário (TRDEAC, TRDBLC) — provavelmente geradas dinamicamente.
- **CMD*:** nenhuma tabela no TDDTAB neste banco — módulo provavelmente não instalado.
- **TFP — `tabelas-tfp.md`:** 252KB com 265 tabelas. 21 prioritárias com até 80 campos, 244 complementares com até 40 campos.
