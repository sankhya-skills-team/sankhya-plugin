from collections import defaultdict, Counter
import os

SEP = '|||'
SKILL_DIR = '/home/daniel/.claude/skills/sankhya-dicionario'
REF_DIR = f'{SKILL_DIR}/references'
os.makedirs(REF_DIR, exist_ok=True)

def parse_file(path):
    rows = []
    with open(path, 'r', encoding='utf-8', errors='replace') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('ORA-') or line.startswith('SP2-') or 'ERROR at' in line:
                continue
            parts = [p.strip() for p in line.split(SEP)]
            if len(parts) >= 2 and parts[0]:
                rows.append(parts)
    return rows

def fix(s):
    s = s.replace('c?o', 'ção').replace('c?es', 'ções').replace('c?a', 'ça').replace('c?', 'ç')
    s = s.replace('?o', 'ão').replace('?a', 'ã').replace('?es', 'ões').replace('?e', 'õe')
    s = s.replace('?', '')
    return s.strip()

def tipo_campo(t):
    tipos = {'I':'Inteiro','F':'Decimal','S':'Texto','D':'Data','T':'Data/Hora','L':'Lógico','M':'Memo','B':'Blob'}
    return tipos.get(t, t or '?')

tables = {}
for r in parse_file('/tmp/sk_tables.txt'):
    tables[r[0]] = fix(r[1]) if len(r) > 1 else ''

fields = defaultdict(list)
for r in parse_file('/tmp/sk_campos_tgf.txt'):
    if len(r) >= 4:
        tab, col, desc, typ = r[0], r[1], fix(r[2]), r[3]
        sz = int(r[4]) if len(r) > 4 and r[4].strip().lstrip('-').isdigit() else 0
        fields[tab].append({'col': col, 'desc': desc, 'typ': typ, 'size': sz})
for r in parse_file('/tmp/sk_campos_tsi.txt'):
    if len(r) >= 4:
        tab, col, desc, typ = r[0], r[1], fix(r[2]), r[3]
        sz = int(r[4]) if len(r) > 4 and r[4].strip().lstrip('-').isdigit() else 0
        fields[tab].append({'col': col, 'desc': desc, 'typ': typ, 'size': sz})

pk_map = defaultdict(list)
for r in parse_file('/tmp/sk_pks.txt'):
    if len(r) >= 3 and r[2].strip().isdigit():
        pk_map[r[0]].append((int(r[2]), r[1]))
for tab in pk_map:
    pk_map[tab] = [col for _, col in sorted(pk_map[tab])]

fk_by_table = defaultdict(list)
ref_count = Counter()
for r in parse_file('/tmp/sk_fks.txt'):
    if len(r) >= 4:
        fk_by_table[r[0]].append((r[1], r[2], r[3]))
        ref_count[r[2]] += 1

options = defaultdict(lambda: defaultdict(list))
for r in parse_file('/tmp/sk_opcoes.txt'):
    if len(r) >= 4:
        options[r[0]][r[1]].append((r[2], fix(r[3])))

with open('/tmp/selected_tables.txt') as fh:
    selected = [l.strip() for l in fh if l.strip()]

def gen_table_doc(tab_name, max_fields=60):
    desc = tables.get(tab_name, '(sem descrição)')
    tab_fields = fields.get(tab_name, [])
    pks = pk_map.get(tab_name, [])
    fks = fk_by_table.get(tab_name, [])
    fk_map = {}
    for item in fks:
        col, ref_tab, ref_col = item[0], item[1], item[2]
        fk_map[col] = (ref_tab, ref_col)

    lines = [f'### {tab_name}', f'**{desc}**', '']
    if pks:
        lines.append(f'**PK:** `{"`, `".join(pks)}`  ')
    refs = ref_count.get(tab_name, 0)
    if refs > 0:
        lines.append(f'**Referenciada por:** {refs} tabelas  ')
    lines.append('')

    if tab_fields:
        lines.append('| Campo | Tipo | Descrição | FK |')
        lines.append('|---|---|---|---|')
        pk_set = set(pks)
        shown = 0
        for fd in tab_fields:
            if shown >= max_fields:
                remaining = len(tab_fields) - shown
                lines.append(f'| *... +{remaining} campos adicionais* | | | |')
                break
            col = fd['col']
            desc_col = fd['desc']
            tipo = tipo_campo(fd['typ'])
            if fd['size'] > 0 and fd['typ'] in ('S','I','F'):
                tipo = f"{tipo}({fd['size']})"
            pk_marker = ' 🔑' if col in pk_set else ''
            fk_info = ''
            if col in fk_map:
                rt, rc = fk_map[col]
                fk_info = f'→ `{rt}`.`{rc}`'
            lines.append(f'| `{col}`{pk_marker} | {tipo} | {desc_col} | {fk_info} |')
            shown += 1
    else:
        lines.append('*(Campos não mapeados no dicionário TDDCAM)*')

    tab_opts = options.get(tab_name, {})
    if tab_opts:
        shown_opts = 0
        for col, opts in tab_opts.items():
            if 2 <= len(opts) <= 15 and shown_opts < 6:
                lines.append('')
                vals = ', '.join([f'`{v}`={d}' for v, d in opts[:12]])
                lines.append(f'**Opções `{col}`:** {vals}')
                shown_opts += 1
    lines.append('')
    return '\n'.join(lines)

# ===== TDD =====
print("Gerando tabelas-tdd.md...")
tdd_list = sorted([t for t in selected if t.startswith('TDD')])
content = ['# Metamodelo Sankhya — Tabelas TDD', '',
    'As tabelas `TDD*` formam o **metamodelo interno do Sankhya OM** — definem tabelas,',
    'campos, instâncias, menus, relacionamentos e permissões. São lidas pela plataforma',
    'em tempo de execução para montar telas, validar permissões e resolver navegação.',
    '',
    '> **Regra:** Nunca escrever diretamente nessas tabelas em código customizado.',
    '> Usar Construtor de Telas ou `datadictionary/` do Addon Studio.',
    '']
for t in tdd_list:
    content.append(gen_table_doc(t, 30))
with open(f'{REF_DIR}/tabelas-tdd.md', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(content))
print(f"  {len(tdd_list)} tabelas, {os.path.getsize(REF_DIR+'/tabelas-tdd.md')//1024}KB")

# ===== TSI =====
print("Gerando tabelas-tsi.md...")
tsi_list = sorted([t for t in selected if t.startswith('TSI')])
content = ['# Tabelas TSI — Configuração do Sistema', '',
    'Tabelas `TSI*` — base de configuração do Sankhya OM: usuários, empresas, grupos,',
    'cidades, estados, bancos, endereços, parâmetros e controle de acesso.',
    '']
for t in tsi_list:
    content.append(gen_table_doc(t, 50))
with open(f'{REF_DIR}/tabelas-tsi.md', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(content))
print(f"  {len(tsi_list)} tabelas, {os.path.getsize(REF_DIR+'/tabelas-tsi.md')//1024}KB")

# ===== TGF CORE =====
print("Gerando tabelas-tgf-core.md...")
tgf_core_order = ['TGFPAR','TGFPRO','TGFCAB','TGFITE','TGFFIN','TGFEMP','TGFTOP','TGFNAT',
                   'TGFVEN','TGFCTT','TGFLOC','TGFVOL','TGFEST','TGFORD','TGFTIT',
                   'TGFGRU','TGFFAM','TGFTAB','TGFNTA','TGFVEI','TGFCFO','TGFSER']
tgf_core_list = [t for t in tgf_core_order if t in tables]
content = ['# Tabelas TGF — Core Comercial e Operacional', '',
    'Tabelas centrais do backoffice Sankhya: parceiros, produtos, notas fiscais,',
    'financeiro, estoque, ordens de carga, tabelas de preço e configuração operacional.',
    '',
    '## Relacionamento Central',
    '```',
    'TGFPAR ←── TGFCAB ──→ TGFTOP (tipo operação)',
    '             │',
    '             ├──→ TGFITE ──→ TGFPRO',
    '             │      └──→ TGFLOC / TGFVOL',
    '             └──→ TGFFIN (títulos financeiros)',
    '',
    'TSIEMP (empresa) ←── TGFCAB, TGFITE, TGFFIN',
    'TGFVEN (vendedor) ←── TGFCAB',
    'TGFEST (estoque) = posição por TGFPRO + TGFLOC',
    '```',
    '']
for t in tgf_core_list:
    content.append(gen_table_doc(t, 100))
with open(f'{REF_DIR}/tabelas-tgf-core.md', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(content))
print(f"  {len(tgf_core_list)} tabelas, {os.path.getsize(REF_DIR+'/tabelas-tgf-core.md')//1024}KB")

# ===== TGF OUTROS =====
print("Gerando tabelas-tgf-outros.md...")
tgf_done = set(tgf_core_list)
tgf_outros = sorted([t for t in selected if t.startswith('TGF') and t not in tgf_done])
content = ['# Tabelas TGF — Complementares', '',
    'Tabelas TGF complementares: fiscal, tributação, comissões, MDF-e, NF-e,',
    'cobrança, tarefas agendadas, alíquotas e configurações adicionais.',
    '']
for t in tgf_outros:
    content.append(gen_table_doc(t, 40))
with open(f'{REF_DIR}/tabelas-tgf-outros.md', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(content))
print(f"  {len(tgf_outros)} tabelas, {os.path.getsize(REF_DIR+'/tabelas-tgf-outros.md')//1024}KB")

print("\nArquivos de referência gerados:")
for fn in sorted(os.listdir(REF_DIR)):
    sz = os.path.getsize(f'{REF_DIR}/{fn}')
    print(f"  {fn}: {sz//1024}KB")
