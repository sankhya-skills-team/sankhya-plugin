# Marca DSTech no relatório

## Regra do time

Todo relatório entregue pela DSTech leva:
- **logo do cliente** no cabeçalho, à esquerda;
- **selo DSTech** (h 12) no rodapé, à esquerda, em todas as páginas;
- a **paleta abaixo**. Nenhuma cor fora dela.

O selo vale para todo cliente; não é opcional.

## Paleta

| nome | hex | uso | cinza no P&B (0–255) |
|---|---|---|---|
| Petróleo | `#2E3C50` | título, cabeçalho de tabela, cartão principal, tarja, total | 58 |
| Texto | `#1F2933` | texto corrido, células | 39 |
| Secundário | `#4A5563` | texto de apoio (unidade, referência, CNPJ) | 83 |
| Rótulo | `#6B7785` | rótulos, subtítulo, rodapé, legenda | 117 |
| Rótulo inverso | `#CFD6DF` | rótulo sobre fundo petróleo | 213 |
| Borda de escrita | `#9AA5B1` | borda da caixa de escrita à mão | 163 |
| Fio | `#D5DBE1` | fio entre linhas e do rodapé | 218 |
| Cartão | `#EEF2F5` | cartão, faixa de grupo, observação, total | 241 |
| Zebra | `#F1F4F7` | linhas pares | 243 |
| Branco | `#FFFFFF` | fundo, texto sobre petróleo | 255 |
| Verde DSTech | `#66CB66` | **só fio e acento**: fio do cabeçalho, fio vertical, fio da faixa de grupo | 161 |
| Verde escuro | `#4A8F55` | cabeçalho de coluna "preencher à mão" | 116 |
| Destaque | `#F5B85C` | fundo da célula que precisa de atenção | 192 |

### Cores semânticas (só quando o significado for estado)

| nome | texto | fundo | uso |
|---|---|---|---|
| Erro / bloqueio | `#C62F2F` | `#FDECEC` | divergência, recusado, bloqueado |
| OK / concluído | `#1E7F4E` | — | conferido, aprovado |
| Alerta | `#B7791F` | `#F5B85C` (destaque) | atenção, vencido, abaixo do esperado |

Sempre acompanhadas de **texto** ("VENCIDO", "DIVERGENTE"). Nunca só a cor.

## Verde

O verde é acento: fio de 1 a 3 pt, nunca fundo de área grande nem cor de texto corrido. No P&B ele vira cinza
médio (161), então o fio continua visível. A exceção é o verde escuro `#4A8F55`, que pode ser fundo do cabeçalho
das colunas que o usuário preenche à mão, para separá-las das colunas de dado.

## P&B (medido por luminância)

- Petróleo, texto e secundário ficam escuros e legíveis.
- **Zebra (243) e cartão (241) quase somem** numa impressora P&B. Por isso a linha da tabela **sempre** tem o fio
  inferior `#D5DBE1` (218): a separação continua mesmo sem a zebra.
- O destaque (192) fica cinza médio. Por isso destaque sempre tem **texto ou negrito** e **legenda**.
- Conferir: imprimir uma página em P&B (ou converter o PNG para tons de cinza) antes de entregar.

## Selo e logo

Selo DSTech: `assets/dstech-selo.b64` (PNG 360×83, colorido, fundo claro). Ainda não existe versão do selo em uma cor
só; em P&B ele sai em tons de cinza legíveis. Como embutir e como trocar a logo do cliente: `logo-e-selo.md`.
