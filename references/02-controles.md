# Controles

## Controles > Valor

Retorna um valor pontual ou texto após a renderização.

### Aba Geral

Barra de ferramentas de formatação de texto (gera HTML): selecionar o texto e acionar o botão. Botões disponíveis:

- Negrito, Sublinhado, Itálico
- Quebra de linha
- Alinhamento: Esquerda, Centro, Direita
- Tipo de Fonte, Tamanho da Fonte
- Cor da Fonte e Cor do Realce (duas caixas de cor)

> Formatação só se aplica ao texto previamente selecionado.

O **Título** informado é renderizado como label. O painel à direita lista os **Parâmetros/Variáveis disponíveis** — arrastar para o campo Título ou Texto, ou digitar diretamente (o parâmetro precisa estar disponível ao componente, senão dá erro). Parâmetros e variáveis valem tanto no Texto quanto no Título.

**Links via expressão** — sempre terminar com `target="_blank"`:

```html
<a href="http://www.google.com" target="_blank">Nome do link</a>
```

### Aba BIA
Ver B.I.A - Business Intelligence Analyst.

---

## Controles > Tabela

No tipo Tabela o painel de edição não tem campo Texto, só Título. A **Descrição** aparece no header (cabeçalho) da tabela após a renderização.

### Aba Geral

- **Entidade** — vincula uma Entidade/Tabela ao componente. As ações cadastradas para essa entidade no Dicionário de Dados (ex.: "Script", "Lançador") ficam disponíveis num botão de ações na tabela gerada.
- **Permite seleção de múltiplas linhas?** — marcada, permite selecionar várias linhas (segurar `Ctrl` + clique).
- **Utilizar a nova versão da grade** — habilita novos recursos: botão "Configuração da Grade" em novo formato e acesso ao **Menu da Grade** (visualização/pesquisa; ver "Iniciar Tour").

**Campo Farol** — na expressão, o campo retorna uma cor para colorir a análise. Dois tamanhos: `Farol(G)` (grande) e `Farol(P)` (pequeno). Exemplo:

```sql
SELECT
  CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#86C154' ELSE '#C3C3C3' END AS FAROL,
  CASE WHEN Financeiro.VLRDESDOB < 100 THEN 'RED' ELSE 'GREEN' END AS FAROL2,
  Financeiro.NUFIN,
  Financeiro.VLRDESDOB,
  CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FF0000' ELSE '' END AS FGCOLOR,
  CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FFFF00' ELSE '' END AS BKCOLOR
FROM TGFFIN Financeiro
```

**Filtro/ordenação por coluna** (vale para Tabela e Tabela Dinâmica) — posicionar o mouse sobre a coluna → botão com as opções: Ordenar crescente, Ordenar decrescente, Remover ordenação, Filtrar, Remover filtro.

**Copiar dados** — selecionar célula/linha e `Ctrl + C` (ou botão direito).

**Limite de linhas** — parâmetro `LIMITLINHASDASH` define o máximo de linhas exibidas na geração do gadget. Na Tabela, o ícone de geração (canto superior direito) permite exportar todos os dados independente do limite; o ícone só aparece se `LIMITLINHASDASH > 0`. Comportamento exclusivo de gadget Tabela.

### Cores de linha por SQL (BKCOLOR / FGCOLOR)

A query da Tabela pode retornar duas colunas com valores hexadecimais:
- **BKCOLOR** → cor de fundo da linha
- **FGCOLOR** → cor do texto

```sql
SELECT
  Financeiro.NUFIN,
  Financeiro.VLRDESDOB,
  Financeiro.DHBAIXA,
  Financeiro.CODPARC,
  CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FF0000' ELSE '' END AS FGCOLOR,
  CASE WHEN Financeiro.VLRDESDOB < 100 THEN '#FFFF00' ELSE '' END AS BKCOLOR
FROM TGFFIN Financeiro
```

### Formatação Condicional por célula

Recurso na extremidade direita da grade Expressão. Só para **Tabela**, nos campos tipo **Inteiro, Moeda, Decimal, Data e Data e Hora**. Define regras: quando verdadeira, aplica-se à célula do campo (cor de fundo, negrito e/ou itálico).

No pop-up, o campo **Tipo** define o layout do assistente:

**Formatação** — permite todas as regras:

| Regra | Condição |
|---|---|
| Maior (>) | valor > resultado da consulta |
| Maior igual (>=) | valor >= resultado |
| Menor (<) | valor < resultado |
| Menor igual (<=) | valor <= resultado |
| Igual (=) | valor = resultado |
| Diferente (<>) | valor <> resultado |
| Entre (Between) | resultado entre os valores informados |
| Não entre (not Between) | resultado fora do intervalo |
| Vazia (NULL) | sem valor no resultado |
| Não vazia (NOT NULL) | há valor no resultado |
| Fórmula Personalizada | fórmula sobre campos do próprio componente (ex.: `CODCR>=100`); aceita as demais regras dentro dela |

Opções da regra:
- **Ícone** — lista de ícones exibidos junto à regra.
- **Mostrar somente ícone** — oculta o texto do campo, exibe só o ícone (desmarcado por padrão).

Botões do editor: exemplos de expressão, adicionar/selecionar variável, negrito, itálico, cor da fonte, cor de fundo.

O campo **Valor** é a referência da regra, conforme o tipo: Inteiro (sem decimais), Moeda (com decimais), Data (com máscara). Nas regras "Célula vazia" e "Célula não vazia" o Valor fica inativo.

**Escala de Cores** — layout exclusivo (não combina com regras de Formatação):

- **Bicolor** — duas cores e dois pontos (Mínimo/Máximo), cada um do tipo Menor valor/Valor/Percentil e Maior valor/Valor/Percentil. Se do mesmo tipo, o mínimo não pode ser maior que o máximo.
- **Tricolor** — três cores; além de Mínimo e Máximo, um ponto Médio (só Valor ou Percentil). Mesma-tipagem: mínimo ≤ médio ≤ máximo.
- Tipo Percentil: valor entre 0 e 100.

**Precedência:** existindo uma regra Escala de Cores, nenhuma outra é permitida. Existindo ≥1 regra Formatação, a Escala de Cores fica indisponível. Com várias regras Formatação no mesmo campo, o sistema aplica a primeira verdadeira (ordem da grade) e ignora as demais.

### Aba BIA
Ver B.I.A - Business Intelligence Analyst.

---

## Controles > Tabela Dinâmica

Configura-se como a Tabela: editar e inserir a query na expressão. Arrastar campos da consulta define a **visualização padrão** (válida na primeira execução; alterações posteriores do usuário são mantidas).

Na edição define-se Título, Tamanho do texto e a Visualização padrão. Marcação **Sempre usar visualização padrão** → descarta alterações do usuário (linhas/colunas) e inicia sempre no padrão configurado. Define-se também Parâmetros/variáveis e Expressão.

- Copiar dados: `Ctrl + C` ou botão direito.
- Campo usado como filtro fica **vermelho**.
- Limite de linhas por `LIMITLINHASDASH` (afeta só Tabela e Tabela Dinâmica).
- Parâmetro vazio → valores em branco/zerados conforme o formato, sem perder o layout.
- A descrição da consulta não pode conter caracteres como `.`.

---

## Controles > Geomapa

Arrastar para o centro e configurar pelo ícone.

- **Configurações do mapa** — centraliza o mapa ao carregar (sem ponto informado, centraliza no Brasil). Campo **Raio** (KM) ao redor do ponto central (campo **Endereço**) — útil para volumetria/proximidade.
- **Marcadores** — representam os dados da expressão SQL:
  - **Apenas marcar** → pino vermelho por registro.
  - **Marcar com uma bolha** → bolhas de tamanho/cor variável (maior bolha = maior representatividade).
- **Evento** (botão) — ao definir clique junto com detalhes do marcador, o clique vira o link "Mais detalhes" no balão.
- **Detalhe do marcador (opcional)** — janela ao clicar no marcador. **Título**: resumo (texto fixo + variáveis de nível, parâmetros e campos da SQL). **Texto**: restante da informação (mesmo uso do Título, aceitando tags HTML).

**Observações:**
- Máximo de **400 marcadores** por visualização (performance).
- Registros com **Latitude/Longitude** nulos são ignorados pela API do Maps, mesmo que o campo nulo não esteja em uso — os campos de Latitude/Longitude do Parceiro (aba Endereço) precisam estar preenchidos.

---

## Controles > HTML5

Passos iniciais (botão **Outras Opções...**):

1. **Download Modelo Simples HTML5** ou **Download Modelo Completo HTML5** — baixa o modelo.
2. O arquivo traz dois modelos XML (SqlServer e Oracle) — abrir o correspondente ao banco e copiar o conteúdo.
3. Colar no botão **XML** do componente e informar o Título.
4. **Upload do Pacote HTML** — carrega o pacote baixado. Mensagem: "Pacote HTML5 atualizado com sucesso."

> Os modelos são apenas base de referência para o componente HTML5.

Arrastar para o centro e configurar pelo ícone. Seção **Configurar Componente HTML5**:

- **Ponto de Entrada** — nome completo (com extensão) do arquivo JSP a compilar. Botão ao lado abre pop-up com os `.JSP` e `.HTML` do zip anexado.
- Link "Editando {Componente} [{Nível}]" no topo — tooltip mostra o Id do componente; clicar copia o Id para a área de transferência.

O componente aceita queries em parâmetros no formato padrão (além do formato antigo):

```sql
SELECT * FROM TGFPAR WHERE CODPARC = :CODPARC_PARAM ORDER BY CODPARC ASC
```

```sql
SELECT CAB.CODPARC, CAB.NOMEPARC
FROM TGFCAB CAB WHERE CODPARC IN
  (SELECT PAR.CORPARC
   FROM TGFPAR PAR INNER JOIN TGFCTT CTT ON (PAR.CODPARC = CTT.CODPARC)
   WHERE PAR.ATIVO IN (:P_ATIVOLIST)
     AND PAR.CODPARC IN (:P_CODPARCLIST)
     AND CTT.ATIVO IN (:P_ATIVOLIST))
  AND (:P_DTNEG.INI IS NULL OR CAB.DTNEG >= :P_DTNEG.INI)
  AND (:P_DTNEG.FIN IS NULL OR CAB.DTNEG <= :P_DTNEG.FIN)
  AND (:P_SERIENOTA IS NULL OR CAB.SERIENOTA LIKE '%' || :P_SERIENOTA || '%')
```

> SQL Server → concatenação com `+`:
> ```sql
> AND (:P_SERIENOTA IS NULL OR CAB.SERIENOTA LIKE '%' + :P_SERIENOTA + '%')
> ```

---

## Controles > IReport

Exibe relatórios formatados nos dashboards.

Pré-requisito: criar o relatório na tela **Relatórios Formatados**, anexar o JRXML (Jasper Reports) e apontar o código do relatório no componente.

- **Importar Parâmetros do Relatório** — importa os parâmetros e abre Relatórios Formatados no relatório configurado. Parâmetros com nome duplicado não são importados.
- **Ignorar paginação** — relatórios com quebra de página passam a paginação contínua.

Cuidados com parâmetros:
- **Multi List** → configurar o relatório para receber o parâmetro como **String**.
- **Período** → dois parâmetros Data (Date/Timestamp) no relatório, mesmo nome, sufixos `.ini` e `.fin`. Ex.: dashboard `ENTRADA` → relatório `ENTRADA.INI` e `ENTRADA.FIN`.

Eventos de clique no IReport existem, mas devem ser criados no editor Jasper (iReport Design ou outro).
