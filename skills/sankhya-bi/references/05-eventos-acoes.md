# Eventos, Ações, Pré-Visualização e Exportação

## Eventos - Gráficos

Nos gráficos, eventos são definidos **por Série**; cada série tem o botão **Evento**, que abre a tela de edição do comportamento no Dashboard (ex.: duplo clique). Duas opções:

### Abrir um novo nível
Lista os níveis já criados. Ao selecionar um nível, se houver **Argumento** vinculado, associa-se uma variável/campo a ele pela coluna **Valor**.

> Num gadget de 3 níveis, o terceiro herda as variáveis passadas do primeiro para o segundo — preferir as herdadas a recriar variáveis com os mesmos valores.

### Lançar uma tela do sistema
Abre qualquer tela ou Dashboard do Sankhya Om a partir do componente (valor, linha, coluna, barra ou campo). No editor, seleciona-se a tela/Dashboard; a **PK** da tabela principal aparece em **Argumento**, e associa-se a ela uma variável local pela coluna **Valor** — a tela abre posicionada no registro analisado.

> - **PK** = chave primária: conjunto de campos que identifica unicamente uma linha (ex.: Código do Parceiro).
> - A tela só abre se o usuário logado tiver ao menos permissão de visualização para ela.

### Aba Atualizar detalhes
Faz o controle atual forçar a atualização de outro controle **do mesmo nível**. Marca-se os componentes a atualizar; grandezas do componente mestre podem ser passadas como argumentos (grade abaixo da lista), inseridos no ambiente dos componentes detalhe e usáveis na query/expressão deles.

Exemplo: nível com tabela de parceiros + gráfico de pizza por segmento. Clicando numa fatia, a tabela busca os parceiros daquele segmento. O mestre é o gráfico de Pizza (onde o Evento é configurado); na aba Atualizar detalhes marca-se a tabela e passa-se o argumento "Segmento de atuação".

---

## Eventos - Controles/Tabela

Evento único, acionado pelo botão **Evento**, definido pela linha acionada.

## Eventos - Controles/Valor

O evento do componente Valor pontual é renderizado como **link**.

---

## Pré-Visualização

Botão **Pré-visualizar** — no canto direito da barra de ferramentas, ao lado de **Outras Opções** (disponível em Design e XML). Abre o gadget como num Dashboard, mostrando o resultado final. O botão **Editar** (canto superior direito) retorna à edição, se o usuário tiver acesso; sem acesso, o botão não aparece.

> No mobile, os gráficos abrem maximizados, com navegação entre eles como no desktop.

---

## Impressão / Exportação

- **Gráfico** — impressão pelo ícone de engrenagem → **Imprimir Gráfico**.
- **Tabela** — exportação em **PDF**, **Planilha Excel** ou **Visualizar em Cubo**. Botão de dados estatísticos dos campos numéricos da grade (ver Estatísticas).

**Observações:**
1. Para que expressões sejam interpretadas como HTML, envolvê-las em CDATA no XML:
   ```xml
   <title><![CDATA[Mês negociado<br><br>Junho</br></br>]]></title>
   ```
2. Editores de fonte aceitam `Ctrl+Z` para desfazer.
3. Na visualização, o filtro do menu lateral é aplicado com `Enter`.
4. No XML principal e nas queries dos componentes, o scroll do mouse facilita a navegação.

---

## Ações nos Componentes de BI

É possível executar ações vinculadas a uma entidade a partir de um Componente de BI (grids). Configuração:

1. Cadastrar o componente (Título, Categoria, Ativo, Descrição) do tipo **Tabela**.
2. Botão **Editar** → definir Título e a **entidade** a trabalhar.
3. Aba **Expressão** → **Editar** → tela "Editar Consulta/Expressão", aba **Avançado**: informar a query que alimenta a tabela. A aba permite buscar trechos na consulta pelo campo de busca (topo); alterações disparam lembrete de salvamento.
4. Em **Configurações > Avançado > Dicionário de Dados**, localizar a entidade pelo **Nome da Instância** e, na aba **Ações**, incluir uma ação do tipo **Rotina no Banco de Dados**, **Script (JavaScript)**, **Lançador** ou **Rotina Java**.

Na visualização do componente, a ação criada fica disponível.

> - Parâmetro `ORDENARACOES` (Ordenar ações por ordem alfabética) — ordena as ações no botão de ações alfabeticamente.
> - Só podem ser usados os dados presentes na entidade relacionada; um campo fora dela não pode ser usado no botão de ação.

---

## Central de Certificações para Dashboards

Regras de certificação na construção do Dashboard — ver Restrição por Dashboard.

---

## Botão Outras Opções

- **Dashboards que usam esse componente** — lista todos os dashboards que usam o componente. Duplo clique num item abre o Construtor de Dashboard posicionado nele.
- Componente de BI para a tela **Configurações > Consulta > Ficha de Parceiros** — considerando a marcação **Exibir por Matriz ou Convênio**, usar o parâmetro `EXIBIRMATRIZ` (correspondente à marcação).
- **Download Modelo JavaScript Simples HTML5** — baixa o modelo HTML que executa queries em tempo de execução via JavaScript:
  - Recebe parâmetros Data/Hora, Data, MultiList:Text, Período, Entidade/Tabela, Texto e SingleList:Text.
  - **MultiList:Text** sem item selecionado retorna todos os registros — para uso fixo na query, configurar como obrigatório.
  - A consulta pode usar um ou vários parâmetros combinados.
