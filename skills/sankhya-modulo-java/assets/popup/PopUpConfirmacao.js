/* Variáveis disponíveis (passadas via addVariable no Java):
   idRegistro — PK do registro a processar
   mensagem   — texto principal exibido no popup
   detalhe    — texto secundário (pode ser vazio)*/

scope.mensagem = mensagem || "Deseja confirmar esta operação?";
scope.detalhe  = detalhe  || "Esta ação não pode ser desfeita.";
scope.confirmar = confirmar;

function confirmar() {
    ServiceProxy.callService('meumodulo@MeuServicoSP.executar', {
        params: { P_ID: idRegistro }
    }, {}).then(function(response) {
        if (response.responseBody.success) {
            MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION, "Operação realizada com sucesso!");
        } else {
            MessageUtils.showAlert(MessageUtils.TITLE_ERROR, response.responseBody.message);
        }
        scope.$dismiss();
    }).catch(function(error) {
        MessageUtils.showAlert(MessageUtils.TITLE_ERROR, "Erro inesperado: " + error);
    });
}
