# Converte raw/*.html (article renderizado) em site/*.md com tabelas e código preservados
import sys, os, glob
sys.path.insert(0, 'lib')
from bs4 import BeautifulSoup
import html2text

PIPE_ESCAPADO = chr(92) + '|'

def cell(td):
    return td.get_text(' ', strip=True).replace('|', PIPE_ESCAPADO).replace(chr(10), ' ')

def table_md(t):
    rows = [[cell(c) for c in tr.find_all(['th', 'td'])] for tr in t.find_all('tr')]
    rows = [r for r in rows if r]
    if not rows: return ''
    w = max(len(r) for r in rows)
    rows = [r + [''] * (w - len(r)) for r in rows]
    lines = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * w]
    lines += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
    return '\n'.join(lines)

def convert(src):
    raw = open(src, encoding='utf-8').read()
    soup = BeautifulSoup(raw, 'html.parser')
    blocks = {}
    for i, el in enumerate(soup.find_all(['table', 'pre'])):
        key = f'@@BLOCO{i}@@'
        blocks[key] = table_md(el) if el.name == 'table' else f"```{el.get('data-lang', '')}\n{el.get_text().rstrip()}\n```"
        el.replace_with(soup.new_string(key))
    h = html2text.HTML2Text(); h.body_width = 0; h.ignore_images = True
    md = h.handle(str(soup)).replace('​', '')
    for k, v in blocks.items(): md = md.replace(k, '\n' + v + '\n')
    return raw.split('\n', 1)[0] + '\n' + md

for src in glob.glob('raw/**/*.html', recursive=True):
    out = 'site' + src[3:-5] + '.md'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(convert(src))
