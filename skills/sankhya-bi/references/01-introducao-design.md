# Construtor de Componentes de BI — Introdução e Design

O gadget (componente) é a unidade básica de um Dashboard. Cada gadget é criado nesta tela; um Dashboard é a composição de vários gadgets. Ao abrir a tela em modo Grade, lista os gadgets já cadastrados.

---

## Painel de Filtros (lado esquerdo)

Filtra os gadgets já criados:

| Campo | Filtra por |
|---|---|
| Botão de Filtros | cria filtros personalizados |
| Código | código do gadget |
| Título Contendo | trecho do título |
| Descrição Contendo | trecho da descrição |
| Categoria | categoria atribuída ao gadget |

Ícone no canto direito → visualiza e edita a posição dos níveis do dashboard (também disponível durante a edição).

---

## Cadastro de um novo gadget

Botão de inclusão (`+`) → informar os campos do cabeçalho:

| Campo | Descrição |
|---|---|
| Título | nome do gadget |
| Categoria | agrupa gadgets; campo de livre digitação — cria ou pesquisa uma categoria existente. Não há cadastro prévio: a categoria nasce ao ser digitada |
| Ativo | ativa/desativa o gadget conforme a marcação |
| Descrição | comentário livre para identificar o gadget |

**Licenciamento:** se o cliente possui o visualizador de Dashboards (`30647 - DASHVIEWER/W`), a visualização não consome licenças do Construtor de Componentes de BI (`30616 - EDITOR DE DASHBOARD/W`). Esgotadas as licenças de visualização, nenhuma visualização de Dashboard abre.

---

## Design × XML

Duas formas de montar o gadget:

- **Design** — assistente visual. Arrasta-se um Componente para a área de trabalho e configura-se por telas. À medida que se monta, o sistema gera o XML correspondente.
- **XML** — edição direta da sintaxe (para quem já a conhece).

O XML é gravado em `TSIGDG.CONFIG` (a tabela `TSIGDG` guarda o cabeçalho do gadget; `CONFIG` guarda o XML completo). É possível usar banco de dados externo ao Sankhya Om como fonte de dados.

**Componentes disponíveis no Design** — divididos em Controles e Gráficos:

| Controles | Gráficos |
|---|---|
| Valor | Linha, Barras, Colunas |
| Tabela | Pizza, Donut, Área |
| Tabela Dinâmica | Análise de Rentabilidade |
| Geomapa | Velocímetro, Geográfico |
| | Bolha, TreeMap, Dispersão |
| | Intervalo de Área |

> Componente comprado protegido pelo Place → botões **Design** e **XML** ficam desabilitados.

---

## Área de Trabalho

Arrastar o componente desejado para a área principal. Cada componente inserido oferece as ferramentas:

| Ferramenta | Ação |
|---|---|
| Alterar tipo | só para Gráficos — troca por outro tipo de gráfico |
| Mover para cima / baixo | reposiciona o componente na análise |
| Editar | abre a tela de edição/configuração do componente (também via duplo clique) |
| Remover | exclui o componente (também via tecla `Delete`), com confirmação |

### Disposição dos componentes (quadro Ferramentas)

Quadro no canto superior esquerdo, para layouts com múltiplos gadgets:

- **Aba Dividir** → divide a área selecionada (principal ou já preenchida) na quantidade de colunas desejada. Colunas resultantes também podem ser subdivididas.
- **Aba Inserir** → acrescenta colunas ao layout.

Opções no topo do quadro:

| Opção | Ação |
|---|---|
| Desfazer última ação | reverte a última alteração no layout |
| Excluir coluna selecionada | remove a coluna |
| Limpar coluna selecionada | esvazia a coluna sem excluí-la |
| Mesclar coluna selecionada | funde os componentes da tela numa única camada no painel principal |
| Layout | **Top-Down** (só vertical) ou **Personalizado** (vertical e horizontal). Padrão: Personalizado |

Botões de navegação entre níveis (dashboards multi-nível) → voltar ao primeiro nível, voltar ao nível anterior, avançar ao próximo.

> A disposição definida aqui é mantida na geração/visualização do dashboard.

**Observações:**
- Carregamento lento (muitos dados) → interromper pelo `x` na barra de carregamento (canto superior esquerdo).
- Parâmetro `USADASHANT` (Usa dashboard antigo) ativo → o quadro Ferramentas some e esta forma de disposição fica indisponível.
- **Nunca deixar container de segundo nível vazio** — o sistema tenta interpretá-lo como contendo um gadget (inclusive relatórios não-IReport) e gera erro.

---

## Cartões Inteligentes

Opção **Cartão Inteligente** exibe o componente como cartão na área de trabalho. Disponível apenas com a base atualizada no Sankhya Om.

Requisitos do componente:
- Estar ativo;
- Possuir informações;
- Não conter filtros (parâmetros);
- Nenhum nível com mais de um gadget — exceto gadgets do tipo **Valor**, que não têm limite por nível.

Atendidos os requisitos, habilita-se a opção de tamanho de exibição do cartão. O componente passa a aparecer na tela de **Acessos**, onde o administrador define quais usuários o veem na área de trabalho.

> O componente só sai da tela de Acessos quando excluído do Construtor. Habilitar/desabilitar não apaga as configurações de acesso.
