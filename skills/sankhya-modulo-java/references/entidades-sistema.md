# Entidades do Sistema — DynamicEntityNames e Tabelas Nativas

## DynamicEntityNames — Constantes das Entidades Nativas

Classe `br.com.sankhya.modelcore.util.DynamicEntityNames` contém constantes para as
principais entidades nativas do Sankhya. Sempre preferir estas constantes a strings literais.

```java
import br.com.sankhya.modelcore.util.DynamicEntityNames;

// Exemplos de uso
JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA).findByPK(nuNota);
JapeFactory.dao(DynamicEntityNames.ITEM_NOTA).findByPK(nuNota, sequencia);
JapeFactory.dao(DynamicEntityNames.FINANCEIRO).findByPK(nuFin);
```

## Entidades Mais Utilizadas

### Documentos Comerciais

| Constante | Entidade JAPE | Tabela | Descrição |
|---|---|---|---|
| `CABECALHO_NOTA` | `CabecalhoNota` | `TGFCAB` | Cabeçalho de notas e pedidos |
| `ITEM_NOTA` | `ItemNota` | `TGFITE` | Itens de nota |
| `FINANCEIRO` | `Financeiro` | `TGFFIN` | Títulos financeiros |
| `ORDEM_CARGA` | `OrdemCarga` | `TGFORD` | Ordens de carga |

### Cadastros

| Constante | Entidade JAPE | Tabela | Descrição |
|---|---|---|---|
| `PARCEIRO` | `Parceiro` | `TGFPAR` | Parceiros (clientes/fornecedores/motoristas) |
| `PRODUTO` | `Produto` | `TGFPRO` | Produtos |
| `EMPRESA` | `Empresa` | `TSIEMP` | Empresas |
| `USUARIO` | `Usuarios` | `TSIUSU` | Usuários do sistema |
| `CONTRATO_ARMAZENAGEM` | `ContratoArmazenagemGeral` | `TCSCON` | Contratos de armazenagem de grãos |
| `LIBERACAO_LIMITE` | `LiberacaoLimite` | `TSILIB` | Liberações por alçada |
| `LIMITE_LIBERACAO` | `LimiteLiberacao` | `TSLIM` | Limites por usuário/evento |

> **TSIUSU vs TGFUSU:** Em versões modernas do Sankhya OM a tabela de usuários é `TSIUSU`, onde `TGFUSU` não existe.
> O entityName XML é `"Usuario"` (singular). Em `JapeFactory.dao()` usa-se a string `"Usuario"` (singular).
> O `DynamicEntityNames.USUARIO` aponta para a entidade/instância `Usuario`.

### Estoque e Logística

| Constante | Entidade JAPE | Tabela | Descrição |
|---|---|---|---|
| — | `Estoque` | `TGFEST` | Posição de estoque |
| — | `LocalFinanceiro` | `TGFLOC` | Locais de estoque/depósitos |
| — | `Volume` | `TGFVOL` | Unidades de medida/volumes |
| — | `Veiculo` | `TGFVEI` | Veículos |

### Endereços

| Constante | Entidade JAPE | Tabela | Descrição |
|---|---|---|---|
| — | `Endereco` | `TSIEND` | Logradouros |
| — | `Cidade` | `TSICID` | Cidades |
| — | `Bairro` | `TSIBAI` | Bairros |
| — | `Contato` | `TGFCTT` | Contatos de parceiro |

---

## Filtros Comuns por Entidade

### Parceiro — filtros de tipo

```java
// Apenas clientes
"CLIENTE = 'S'"

// Apenas fornecedores
"FORNECEDOR = 'S'"

// Apenas motoristas
"MOTORISTA = 'S'"
```

### CabecalhoNota — filtros de tipo de movimento

```java
// Notas confirmadas
"this.CONFIRMADA = 'S'"

// Por tipo de movimento
"this.TIPMOV = 'O'"  // pedido de compra
"this.TIPMOV = 'V'"  // pedido de venda
"this.TIPMOV = 'C'"  // nota de compra

// Por contrato
"this.NUMCONTRATO = ?"  // com parâmetro BigDecimal
```

### Financeiro — filtros

```java
// Títulos a receber em aberto (não baixados)
"this.RECDESP = 1 AND this.STATUSNFE = 'P'"

// Títulos a pagar em aberto
"this.RECDESP = -1 AND this.STATUSNFE = 'P'"

// Por parceiro
"this.CODPARC = ?"
```

---

## Campos Comuns por Entidade

### CabecalhoNota (TGFCAB)

| Campo | Tipo | Descrição |
|---|---|---|
| `NUNOTA` | BigDecimal | Número da nota (PK) |
| `CODEMP` | BigDecimal | Código da empresa |
| `CODPARC` | BigDecimal | Código do parceiro |
| `DTNEG` | Timestamp | Data de negociação |
| `CONFIRMADA` | String | `S`=confirmada, `N`=pendente |
| `TIPMOV` | String | Tipo de movimento |
| `VLRNOTA` | BigDecimal | Valor total da nota |
| `ORDEMCARGA` | BigDecimal | Número da ordem de carga |
| `NUMCONTRATO` | BigDecimal | Número do contrato |
| `CODVEND` | BigDecimal | Código do vendedor |
| `CODTIPVENDA` | BigDecimal | Tipo de operação |

### ItemNota (TGFITE)

| Campo | Tipo | Descrição |
|---|---|---|
| `NUNOTA` | BigDecimal | Número da nota (PK1) |
| `SEQUENCIA` | BigDecimal | Sequência do item (PK2) |
| `CODPROD` | BigDecimal | Código do produto |
| `QTDNEG` | BigDecimal | Quantidade negociada |
| `VLRUNIT` | BigDecimal | Valor unitário |
| `VLRTOT` | BigDecimal | Valor total do item |
| `PESOBRUTO` | BigDecimal | Peso bruto |
| `PESOLIQ` | BigDecimal | Peso líquido |
| `CODVOL` | String | Código da unidade de volume |
| `CONTROLE` | String | Lote |

### Financeiro (TGFFIN)

| Campo | Tipo | Descrição |
|---|---|---|
| `NUFIN` | BigDecimal | Número do título (PK) |
| `NUNOTA` | BigDecimal | Nota de origem |
| `CODPARC` | BigDecimal | Parceiro |
| `VLRDESDOB` | BigDecimal | Valor do desdobramento |
| `VLRBAIXA` | BigDecimal | Valor baixado |
| `DTVENC` | Timestamp | Data de vencimento |
| `DTBAIXA` | Timestamp | Data de baixa |
| `STATUSNFE` | String | Status: `P`=pendente, `B`=baixado, `C`=cancelado |
| `RECDESP` | BigDecimal | `1`=receita (contas a receber), `-1`=despesa (contas a pagar) |

### Usuários (TGFUSU)

| Campo | Tipo | Descrição |
|---|---|---|
| `CODUSU` | BigDecimal | Código do usuário (PK) |
| `NOMEUSU` | String | Nome do usuário |
| `CODGRUPO` | BigDecimal | Grupo do usuário |
| `ATIVO` | String | `S`=ativo, `N`=inativo |

---

## AdicionalEntityNames — Padrão do Projeto

Entidades customizadas (`AD_`) devem ser catalogadas no enum `AdicionalEntityNames`
do projeto, evitando strings espalhadas pelo código.

```java
// BOM — usar o enum
JapeFactory.dao(AdicionalEntityNames.ORDEM_COLETA.getEntityName()).findByPK(id);

// RUIM — string literal espalhada
JapeFactory.dao("AD_ORDEMCOLETA").findByPK(id);
```

Ao criar nova entidade, sempre adicionar no enum:

```java
public enum AdicionalEntityNames {
    // ... existentes ...
    NOVA_ENTIDADE("AD_NOVAENTIDADE");

    // ...
}
```
