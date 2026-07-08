// Template: directive AngularJS 1.x no padrao sankhya-js.
// Uso: widget reutilizavel em src/components/<nome>/.
// Referencia: .claude/skills/sankhya-js/reference/patterns.md secao 3
//
// ATENCAO: apenas <nome>.module.js declara com [] de deps.
// Outros arquivos do mesmo modulo reutilizam SEM array — passar []
// de novo sobrescreve o modulo e perde services ja declarados (gotcha 11).

// ====================================================================
// <nome>.module.js
// ====================================================================
angular.module('snk.components.meucomp', []);

// ====================================================================
// <nome>.directive.js
// ====================================================================
angular
    .module('snk.components.meucomp')
    .directive('skMeucomp', [function () {
        return {
            restrict: 'E',
            scope: {
                // = : two-way. Use quando o componente altera o valor do pai.
                // @ : string literal. Use para labels/titulos fixos.
                // & : expressao. Use para callbacks invocados pelo componente.
                value: '=',
                label: '@',
                onChange: '&'
            },
            templateUrl: 'components/meucomp/meucomp.html',
            controller: ['$scope', function ($scope) {
                var self = this;

                self.click = function () {
                    // Nomes do objeto viram variaveis locais na expressao do pai.
                    // Aqui o pai pode usar `value` em on-change="ctrl.aoMudar(value)".
                    $scope.onChange({ value: $scope.value });
                };
            }],
            controllerAs: 'ctrl'
        };
    }]);

// ====================================================================
// USO em HTML (tela que ja importou snk.components.meucomp)
// ====================================================================
//
// <sk-meucomp
//     value="ctrl.valorAtual"
//     label="{{ 'MinhaTela.campo' | translate }}"
//     on-change="ctrl.aoMudar(value)">
// </sk-meucomp>
//
// No controller da tela:
//
//   angular.module('minhaTela').controller('MinhaCtrl', function () {
//       var ctrl = this;
//       ctrl.valorAtual = 'inicial';
//       ctrl.aoMudar = function (valor) {
//           // `valor` vem do $scope.onChange({ value: ... }) do componente.
//       };
//   });
