#!/bin/bash
# Script para re-extrair dados do banco Sankhya e regenerar a skill sankhya-dicionario
# Uso: bash extract_and_generate.sh
# Requisito: container wildfly-docker-sankhya-skdev-oracle-addon-1 rodando

set -e
SKILL_DIR="$(dirname "$0")/.."
DOCKER_CONTAINER="wildfly-docker-sankhya-skdev-oracle-addon-1"
DB="SKCONTAINER/tecsis@localhost:1521/XE"

run_query() {
    local sql="$1"
    local outfile="$2"
    docker exec "$DOCKER_CONTAINER" bash -c "
echo \"$sql\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > "$outfile" 2>/dev/null
}

echo "[1/6] Tabelas (TDDTAB)..."
docker exec "$DOCKER_CONTAINER" bash -c "
echo \"SET LINESIZE 500 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT TRIM(t.NOMETAB)||'|||'||TRIM(t.DESCRTAB)
FROM SKCONTAINER.TDDTAB t
WHERE LENGTH(t.NOMETAB)<=12
  AND (t.NOMETAB LIKE 'TGF%' OR t.NOMETAB LIKE 'TSI%' OR t.NOMETAB LIKE 'TDD%' 
       OR t.NOMETAB LIKE 'TCS%' OR t.NOMETAB LIKE 'TFP%' OR t.NOMETAB LIKE 'TRD%')
ORDER BY t.NOMETAB;
EXIT;\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > /tmp/sk_tables.txt

echo "[2/6] Campos TGF (TDDCAM)..."
docker exec "$DOCKER_CONTAINER" bash -c "
echo \"SET LINESIZE 600 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT TRIM(NOMETAB)||'|||'||TRIM(NOMECAMPO)||'|||'||TRIM(DESCRCAMPO)||'|||'||TIPCAMPO||'|||'||NVL(TAMANHO,0)
FROM SKCONTAINER.TDDCAM
WHERE NOMETAB LIKE 'TGF%' AND LENGTH(NOMETAB)<=10
ORDER BY NOMETAB, ORDEM;
EXIT;\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > /tmp/sk_campos_tgf.txt

echo "[3/6] Campos TSI/TDD (TDDCAM)..."
docker exec "$DOCKER_CONTAINER" bash -c "
echo \"SET LINESIZE 600 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT TRIM(NOMETAB)||'|||'||TRIM(NOMECAMPO)||'|||'||TRIM(DESCRCAMPO)||'|||'||TIPCAMPO||'|||'||NVL(TAMANHO,0)
FROM SKCONTAINER.TDDCAM
WHERE (NOMETAB LIKE 'TSI%' OR NOMETAB LIKE 'TDD%') AND LENGTH(NOMETAB)<=10
ORDER BY NOMETAB, ORDEM;
EXIT;\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > /tmp/sk_campos_tsi.txt

echo "[4/6] Chaves primárias..."
docker exec "$DOCKER_CONTAINER" bash -c "
echo \"SET LINESIZE 600 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT c.table_name||'|||'||c.column_name||'|||'||c.position
FROM all_cons_columns c
JOIN all_constraints k ON k.owner=c.owner AND k.constraint_name=c.constraint_name
WHERE c.owner='SKCONTAINER' AND k.constraint_type='P'
  AND (c.table_name LIKE 'TGF%' OR c.table_name LIKE 'TSI%' OR c.table_name LIKE 'TDD%' OR c.table_name LIKE 'TCS%')
  AND c.table_name NOT LIKE '%_RP_%' AND LENGTH(c.table_name)<=12
ORDER BY c.table_name, c.position;
EXIT;\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > /tmp/sk_pks.txt

echo "[5/6] Chaves estrangeiras..."
docker exec "$DOCKER_CONTAINER" bash -c "
echo \"SET LINESIZE 600 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT fc.table_name||'|||'||fc.column_name||'|||'||rc.table_name||'|||'||rc.column_name
FROM all_cons_columns fc
JOIN all_constraints fk ON fk.owner=fc.owner AND fk.constraint_name=fc.constraint_name AND fk.constraint_type='R'
JOIN all_constraints pk ON pk.owner=fk.owner AND pk.constraint_name=fk.r_constraint_name
JOIN all_cons_columns rc ON rc.owner=pk.owner AND rc.constraint_name=pk.constraint_name AND rc.position=fc.position
WHERE fc.owner='SKCONTAINER'
  AND (fc.table_name LIKE 'TGF%' OR fc.table_name LIKE 'TSI%')
  AND fc.table_name NOT LIKE '%_RP_%' AND LENGTH(fc.table_name)<=10
ORDER BY fc.table_name, fc.column_name;
EXIT;\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > /tmp/sk_fks.txt

echo "[6/6] Opções de campos (enums)..."
docker exec "$DOCKER_CONTAINER" bash -c "
echo \"SET LINESIZE 500 PAGESIZE 0 FEEDBACK OFF HEADING OFF TRIMSPOOL ON
SELECT TRIM(c.NOMETAB)||'|||'||TRIM(c.NOMECAMPO)||'|||'||TRIM(o.VALOR)||'|||'||TRIM(o.OPCAO)
FROM SKCONTAINER.TDDOPC o
JOIN SKCONTAINER.TDDCAM c ON c.NUCAMPO = o.NUCAMPO
WHERE LENGTH(c.NOMETAB)<=10
  AND (c.NOMETAB LIKE 'TGF%' OR c.NOMETAB LIKE 'TSI%')
ORDER BY c.NOMETAB, c.NOMECAMPO, o.ORDEM;
EXIT;\" > /tmp/sk_q.sql
sqlplus -S $DB @/tmp/sk_q.sql
" > /tmp/sk_opcoes.txt

echo "Extração concluída. Gerando arquivos da skill..."
python3 "$SKILL_DIR/scripts/gen_skill.py"
echo "Pronto!"
