/* Variáveis disponíveis (passadas via addVariable no Java):
   codRegistro — PK do registro principal (para filtro e exibição no título)
   codemp      — código da empresa (se necessário para filtro)*/

scope.onDatasetCreated = onDatasetCreated;

function onDatasetCreated(dataset) {
    if (dataset.getEntityName() === "SUBSTITUIR_COM_ENTIDADE") {
        dataset.addCriteriaProvider(new CriteriaProvider(
            Criteria("this.CAMPO_PK = ?", codRegistro)
            /* Adicionar mais critérios conforme necessidade:
             Criteria("this.CODEMP = ? AND this.CAMPO_PK = ?", codemp, codRegistro)*/
        ));
        dataset.initAndRefresh();
    }
}
