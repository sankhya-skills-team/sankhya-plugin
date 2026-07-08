#!/bin/bash
# Consulta campos e opções de tabelas Sankhya diretamente no Oracle via Docker
#
# Uso:
#   bash consultar-oracle.sh TGFCAB            → lista todos os campos da tabela
#   bash consultar-oracle.sh TGFCAB TIPMOV      → lista as opções (enum) do campo
#
# Requisito: container wildfly-docker-sankhya-skdev-oracle-addon-1 rodando

set -e

CONTAINER="wildfly-docker-sankhya-skdev-oracle-addon-1"
DB="SKCONTAINER/tecsis@localhost:1521/XE"
TABELA="${1:-}"
CAMPO="${2:-}"

if [ -z "$TABELA" ]; then
  echo "Uso: $0 NOMETAB [NOMECAMPO]"
  echo "  Exemplos:"
  echo "    $0 TGFCAB            → campos da tabela"
  echo "    $0 TGFCAB TIPMOV     → opções do campo"
  exit 1
fi

TABELA=$(echo "$TABELA" | tr '[:lower:]' '[:upper:]')

if [ -z "$CAMPO" ]; then
  # Lista campos da tabela
  echo "=== Campos de $TABELA ==="
  docker exec "$CONTAINER" bash -c "
echo \"SET LINESIZE 200 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT RPAD(c.NOMECAMPO,30)||' '||RPAD(c.TIPCAMPO,3)||' '||RPAD(NVL(TO_CHAR(c.TAMANHO),' '),8)||TRIM(c.DESCRCAMPO)
FROM SKCONTAINER.TDDCAM c
WHERE c.NOMETAB = '$TABELA'
ORDER BY c.ORDEM;
EXIT;\" | sqlplus -S $DB
"
  echo ""
  echo "=== Chaves de $TABELA ==="
  docker exec "$CONTAINER" bash -c "
echo \"SET LINESIZE 200 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT acc.COLUMN_NAME||' ('||ac.CONSTRAINT_TYPE||')'
FROM ALL_CONSTRAINTS ac
JOIN ALL_CONS_COLUMNS acc ON ac.CONSTRAINT_NAME = acc.CONSTRAINT_NAME
WHERE ac.TABLE_NAME = '$TABELA' AND ac.OWNER = 'SKCONTAINER'
  AND ac.CONSTRAINT_TYPE IN ('P','R')
ORDER BY ac.CONSTRAINT_TYPE, acc.POSITION;
EXIT;\" | sqlplus -S $DB
"
else
  # Lista opções de um campo específico
  CAMPO=$(echo "$CAMPO" | tr '[:lower:]' '[:upper:]')
  echo "=== Opções do campo $TABELA.$CAMPO ==="
  docker exec "$CONTAINER" bash -c "
echo \"SET LINESIZE 200 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT RPAD(o.VALOR,20)||o.OPCAO
FROM SKCONTAINER.TDDOPC o
JOIN SKCONTAINER.TDDCAM c ON c.NUCAMPO = o.NUCAMPO
WHERE c.NOMETAB = '$TABELA' AND c.NOMECAMPO = '$CAMPO'
ORDER BY o.ORDEM;
EXIT;\" | sqlplus -S $DB
"
fi
