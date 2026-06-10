/* Variáveis disponíveis (passadas via addVariable no Java):
   nuNota  — PK do registro principal
   filtro  — parâmetro de filtro opcional*/

scope.selecionar = selecionar;
scope.onDatasetCreated = onDatasetCreated;
scope.dataset;

function onDatasetCreated(dataset) {
    scope.dataset = dataset;
    // Adicionar critério de filtro conforme necessidade:
    // dataset.addCriteriaProvider(new CriteriaProvider(Criteria("this.CAMPO = ?", filtro)));
    dataset.initAndRefresh();
}

function selecionar() {
    if (!scope.dataset || scope.dataset.isEmpty()) {
        MessageUtils.showAlert(MessageUtils.TITLE_WARNING, "Selecione um registro!");
        return;
    }

    var registro = scope.dataset.getCurrentRowAsObject();
    var valorSelecionado = registro.CAMPO1; // ajustar para o campo PK da entidade

    ServiceProxy.callService('meumodulo@MeuServicoSP.processar', {
        params: {
            P_NUNOTA: nuNota,
            P_VALOR: valorSelecionado
        }
    }, {}).then(function(response) {
        if (response.responseBody.success) {
            MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION, "Processado com sucesso!");
        } else {
            MessageUtils.showAlert(MessageUtils.TITLE_ERROR, response.responseBody.message);
        }
        scope.$dismiss();
    }).catch(function(error) {
        MessageUtils.showAlert(MessageUtils.TITLE_ERROR, "Erro inesperado: " + error);
    });
}
