# Como testar kit no Sankhya OM

## Trocar parâmetro da TSIPAR sem reiniciar

1. Tela **Preferências** (`br.com.sankhya.core.cfg.Preferencias`): busca pela chave + Enter,
   campo "Ligado/Desligado", salvar no ✓. Conferir no banco: o dropdown às vezes não grava na
   primeira tentativa.
2. Tela **Cache do Servidor** (`br.com.sankhya.core.cfg.InvalidarCache`) → "Descartar Cache Agora".
   Valeu na hora para o `INIBESELECUSOPD`.
3. Só se ainda não valer: reiniciar o WildFly (UPDATE antes de parar; tirar os `.ear` dos addons de
   `deployments` e recolocar depois).

Anotar o valor original antes e restaurar pelo mesmo caminho. Parâmetro sem linha na TSIPAR: a tela
cria a linha; restaurar com o `default` do core.

## Configuração de Kit e TOP

- `TSIKIT`: tela Configuração de Kit (toggles + ✓); lida na hora.
- TOP: tela **Tipos de Operação - TOP** (`br.com.sankhya.com.cad.tipooperacao`). Cada gravação cria
  uma **versão nova** (`DHALTER`); restaurar = gravar de novo o valor antigo (fica mais uma versão).
  `TIPOIMPKIT` fica na aba Impressão.

## Roteiro de uma rodada

1. Gerar o pedido (no addon, ou incluindo o kit pela Central; kit só pela lupa).
2. Central de Vendas → Confirmar.
3. Portal de Vendas: Tipo de Movimento "Pedido de venda", Número único, Aplicar, selecionar a linha →
   Faturar → data (`Ctrl+A` antes de digitar) → Próximo → TOP → Concluir.
4. Conferir no banco (abaixo).
5. Limpar: excluir a nota na Central, depois o pedido. A Central aceita no máximo 5 documentos
   abertos (pede para substituir um).

Nota de base clone de cliente fica **sem confirmar**: a confirmação envia a NF-e à SEFAZ.

## Consultas de conferência

```sql
-- itens do pedido/nota
SELECT I.NUNOTA, I.SEQUENCIA, I.CODPROD, I.USOPROD, I.QTDNEG, I.VLRUNIT, I.VLRTOT, I.CUSTO,
       I.BASEICMS, I.VLRICMS, I.ATUALESTOQUE, I.RESERVA, I.PENDENTE
  FROM TGFITE I WHERE I.NUNOTA IN (:PEDIDO, :NOTA) ORDER BY 1, 2;
-- ligação kit ↔ componentes e pedido ↔ nota
SELECT NUNOTA, SEQUENCIA, NUNOTAORIG, SEQUENCIAORIG, QTDATENDIDA FROM TGFVAR WHERE NUNOTA = :NOTA;
-- estoque e reserva
SELECT CODPROD, ESTOQUE, RESERVADO FROM TGFEST
 WHERE CODEMP = :EMP AND CODLOCAL = :LOCAL AND CONTROLE = ' ' AND CODPARC = 0 AND CODPROD IN (...);
-- parâmetros e configuração
SELECT CHAVE, LOGICO FROM TSIPAR WHERE CHAVE IN ('INIBESELECUSOPD','CONFKITIND','ATUALEMPRODKIT',
       'COMCONSKITIMPIT','HABSUPORTEKITSW','HABSUBSKITIND');
SELECT * FROM TSIKIT;
SELECT CODTIPOPER, DHALTER, ATUALEST, ATUALESTMP, TIPOIMPKIT FROM TGFTOP
 WHERE CODTIPOPER = :TOP ORDER BY DHALTER DESC;
```
