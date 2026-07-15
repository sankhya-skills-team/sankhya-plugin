# Estrutura oficial de estimativa — Template de horas (7 fases)

Toda estimativa Sankhya é itemizada por **rotina** (artefato entregável) e dividida em **7 fases**. Confirmado idêntico em 10 projetos de clientes distintos. A saída de estimativa da skill **deve replicar esta estrutura**, não apenas "horas de dev + buffer".

## Colunas do template

| Item | Rotina | Levantamento | Desenvolvimento | Homologação | Treinamento | Simulação | Documentação | Produção e acompanhamento | TOTAL |
|---|---|---|---|---|---|---|---|---|---|

- **1 linha = 1 artefato entregável**: uma tela, uma aba/guia, um botão de ação, um relatório, um dashboard, uma regra de negócio, um campo+regra. Granularidade fina — o mesmo cadastro vira 5–6 linhas (estrutura + cada aba + cada botão).
- **Desenvolvimento** é a coluna calculada pelas tabelas de base por artefato × multiplicadores (ver `heuristicas-estimativa.md`).
- As demais 6 fases são o overhead de projeto, alocado por rotina.

## Proporção das fases (calibrado em dados reais)

Sobre o total de **Desenvolvimento** do projeto:

| Fase | Proporção típica | Observação |
|---|---|---|
| Levantamento | ~0 (piso 0–2h) | Não cobrado como fase separada na maioria |
| Desenvolvimento | base (100%) | Calculado por artefato × multiplicadores |
| Homologação | 7–12% do dev | Sempre presente |
| Treinamento | ~0 (0–4h) | Só em módulos com usuário final novo |
| Simulação | ~5% do dev | Teste de cenário real |
| Documentação | piso ~2h, escala em projeto grande (~5–6% do dev) | 2h fixo nos pequenos |
| Produção e acompanhamento | 6–30% do dev | **Overhead dominante e mais variável** |

**Overhead total não-dev: ~28–30% sobre o dev** em projetos ≥70h; sobe para **~40–55%** em projetos pequenos (≤40h), porque Documentação/Homologação/Produção têm piso fixo que não escala para baixo.

**Alocação não é proporcional linha a linha.** As fases não-dev concentram-se em poucas **rotinas-âncora** — a rotina que cria a estrutura do módulo carrega a Documentação e o Treinamento de tudo. Ex. real (Projeto A): "Criar estrutura de OS/SubOS" = 8h dev mas 35h não-dev (doc 16, simul 5, homolog 4, treino 4, prod 2); já "Regras gerais de validações" = 40h dev e 1h não-dev. Concentrar doc/treino na rotina estruturante, não diluir.

## Faixas reais observadas por artefato (coluna Desenvolvimento, horas)

Calibração a partir de planilhas preenchidas — usar para sanity-check das tabelas de base:

| Artefato | Dev (h) | Mediana |
|---|---|---|
| Botão de ação | 6–32 | ~16 |
| Aba / cadastro pequeno (Peças, Serviços, Peritagem) | 4 | 4 |
| Tela com regras/validações | 6–16 | ~10 |
| Estrutura de cadastro com hierarquia (rotina-âncora) | 8 dev (+ não-dev pesado) | — |
| Relatório Jasper / iReport | 16–20 | ~18 |
| Relatório com fotos / agregação multi-registro | 20–24 | ~22 |
| Dashboard / gadget BI | 16–24 | ~20 |
| Regra de negócio | 8–24 | — |
| "Regras gerais de validações" (catch-all agregado) | 40 | 40 |

Taxa horária base observada: **~180 R$/h** (varia por cliente/proposta).

> ⚠️ **Estas faixas são de planilhas VENDIDAS e subestimam o real em ~1,6–2,2×** (ex.: Projeto A vendida 282h dev × código real 460–610h). Para realismo, ver pesos medidos por artefato, produtividade (~12 LOC/h), EJB e frontend vc em `references/calibracao-real.md`. Quando a abordagem correta for addon com UI própria, somar as telas vc explicitamente — é o que leva o real a 600h+.

## Confronto com estimativa-âncora do documento

Documentos de pré-vendas frequentemente trazem um número pré-fechado (ex.: "totalizando 60h", "packs de plataforma"). **Detectar e confrontar com a estimativa itemizada**, nunca aceitar cego nem ignorar.

> Caso real: levantamento do Projeto A trazia "60h" (pré-vendas); a estimativa itemizada por rotina deu **360h** — 6× maior. Divergência grande = escopo subdimensionado na pré-venda. Sinalizar explicitamente: "âncora do documento: Xh; estimativa itemizada: Yh; divergência Z× — revisar escopo/proposta".

## Genêro as-built → não estimar

Se o documento for de entrega/as-built (gênero E/F em `generos-documento.md` — traz código-fonte, views/triggers, ou caso de uso passo-a-passo), **não gerar estimativa**: o trabalho já foi feito. Usar como referência técnica/complexidade para projetos similares.

## Formato de saída da estimativa (substitui a tabela só-dev)

```
## 12. Estimativa de horas (template de fases)

| Rotina (artefato) | Abordagem | Lev. | Dev. | Homol. | Trein. | Simul. | Doc. | Prod. | Total |
|---|---|---|---|---|---|---|---|---|---|
| Criar estrutura X | [MÓDULO JAVA] | 1 | 8 | 4 | 4 | 5 | 16 | 2 | 40 |
| Botão Calcular Y | [MÓDULO JAVA] | – | 16 | 2 | – | 1 | 1 | – | 20 |
| Relatório Z (iReport) | [RELATÓRIO] | – | 20 | 3 | – | – | 1 | – | 24 |
| **Total** | | **1** | **44** | **9** | **4** | **6** | **18** | **2** | **84** |

**Âncora do documento:** 60h · **Estimativa itemizada:** 84h · divergência 1,4×
**Confiança geral:** MÉDIO
```
