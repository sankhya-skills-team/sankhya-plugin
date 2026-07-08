/* Variáveis disponíveis (passadas via addVariable no Java):
   codRegistro — PK do registro a ser atualizado*/

scope.modelo = { prioridade: 'M' };
scope.salvar = salvar;

function salvar() {
    if (!scope.modelo.observacao || scope.modelo.observacao.trim() === '') {
        MessageUtils.showAlert(MessageUtils.TITLE_WARNING, "Preencha a observação!");
        return;
    }

    ServiceProxy.callService('meumodulo@MeuServicoSP.atualizar', {
        params: {
            P_ID:         codRegistro,
            P_OBS:        scope.modelo.observacao,
            P_PRIORIDADE: scope.modelo.prioridade,
            P_DATA_PREV:  scope.modelo.dataPrevista
        }
    }, {}).then(function(response) {
        if (response.responseBody.success) {
            MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION, "Dados salvos com sucesso!");
            scope.$dismiss();
        } else {
            MessageUtils.showAlert(MessageUtils.TITLE_ERROR, response.responseBody.message);
        }
    }).catch(function(error) {
        MessageUtils.showAlert(MessageUtils.TITLE_ERROR, "Erro inesperado: " + error);
    });
}
