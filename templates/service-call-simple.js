// Template: chamada simples ao backend via ServiceProxy.
// Uso: 80% dos casos — carregar dados ou disparar uma operacao.
// Referencia: .claude/skills/sankhya-js/reference/patterns.md secao 1

angular
    .module('snk.commons')
    .controller('MinhaCtrl', ['$scope', 'ServiceProxy',
        function ($scope, ServiceProxy) {
            var self = this;

            self.carregar = function (codParc) {
                // serviceName DEVE ter prefixo de modulo (mgecom@, mgefin@, ...).
                // Sem prefixo cai em "mge" e o servico de outro modulo falha (gotcha 1).
                // { $: valor } e a notacao herdada do transform XML/JSON do backend.
                ServiceProxy.callService(
                    'mgecom@FichaParceiroSP.getFinanceiros',
                    { codParc: { $: codParc } }
                ).then(function (data) {
                    $scope.financeiros = data.responseBody;
                });

                // Popup de erro ja e exibido por default pelo ServiceProxy.
                // NAO adicionar .catch so para mostrar outro popup — gera dialogos
                // sobrepostos (anti-pattern 11). Se precisar tratar manualmente,
                // use o template service-call-builder.js com errorHandler/ignorePopUpErrorMsgs.
            };
        }
    ]);

// ====================================================================
// USO em HTML
// ====================================================================
//
// <div ng-controller="MinhaCtrl as ctrl">
//     <sk-button label="Carregar" ng-click="ctrl.carregar(123)"></sk-button>
//
//     <ul>
//         <li ng-repeat="f in financeiros track by f.codigo">
//             {{ f.descricao }}
//         </li>
//     </ul>
// </div>
