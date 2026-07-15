package br.com.sankhya.customizacao.utils;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

/**
 * Builder para popups personalizados em Módulos Java Sankhya OM.
 *
 * IMPORTANTE: Esta classe NÃO é nativa do Sankhya SDK. Deve ser incluída
 * manualmente no pacote br.com.sankhya.customizacao.utils do projeto.
 *
 * Referência original: addon interno de controle de projeto (utils.PopUpBuilder)
 * Adaptação: pacote ajustado para br.com.sankhya.customizacao.utils
 *
 * Como funciona:
 * 1. Gera um HTML completo com CSS/JS embutidos
 * 2. O HTML usa Angular do Sankhya OM e jQuery (disponíveis no contexto do popup)
 * 3. Serviços Angular (MessageUtils, ServiceProxy, etc.) são injetados automaticamente
 * 4. O HTML gerado é passado para MessageUtils.showInfo() que usa ServiceContext.setStatus(2)
 * 5. O frontend Sankhya reconhece status=2 e renderiza como modal popup
 *
 * Uso:
 * <pre>
 *   String popup = new PopUpBuilder.Builder()
 *       .setTitle("Título do Popup")
 *       .setHtmlFile(getClass().getResourceAsStream("/popup/MeuPopUp.html"))
 *       .setJsFile(getClass().getResourceAsStream("/popup/MeuPopUp.js"))
 *       .setWidth(700)
 *       .setHeight(400)
 *       .addVariable("codRegistro", codRegistro)    // Number: var codRegistro = 42;
 *       .addVariable("nomeEntidade", "TGFCAB")      // String: var nomeEntidade = 'TGFCAB';
 *       .addVariable("ativo", true)                 // Boolean: var ativo = true;
 *       .build();
 *
 *   MessageUtils.showInfo(popup);
 * </pre>
 *
 * No JavaScript do popup, após o build(), os seguintes estão disponíveis:
 *   - scope         (AngularJS scope do popup)
 *   - ObjectUtils, MessageUtils, AngularUtil, DateUtils, NumberUtils,
 *     ServiceProxy, StringUtils, SkApplicationInstance
 *   - Todas as variáveis adicionadas via addVariable()
 *   - scope.$dismiss() para fechar o popup
 *
 * Convenção de nomes de arquivo:
 *   Java:  br.com.sankhya.customizacao.{modulo}.helper.PopUp{Nome}Helper.java
 *   HTML:  Java/resources/{pacote}/popup/PopUp{Nome}.html
 *   JS:    Java/resources/{pacote}/popup/PopUp{Nome}.js
 *
 * Para que os recursos sejam incluídos no JAR, coloque-os em:
 *   Java/resources/br/com/sankhya/customizacao/{modulo}/popup/
 * Isso garante que o include "br/com/sankhya/customizacao/${moduleName}/**"
 * do build.gradle capture os arquivos.
 */
public class PopUpBuilder {

    public static class Builder {

        private String title;
        private InputStream jsFile;
        private InputStream htmlFile;
        private InputStream cssFile;
        private int width;
        private int height;
        private Map<String, Object> variables;

        // CSS padrão injetado em todo popup -- ajusta o modal para o tamanho configurado
        private final String defaultCss =
            "<style>" +
            ".modal-backdrop.in{background-color:#fff}" +
            ".modal-content{width:${width}px}" +
            "h4{font-size:16px;font-weight:700}" +
            ".celula-grid{padding:5px!important;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}" +
            ".gridpopup>tbody>tr:hover{background-color:#b6e7b6}" +
            ".sk-popup.modal-type-warning .modal-header{background-color:#f3f3f3!important}" +
            ".sk-popup.modal.fade .modal-dialog,.sk-popup.modal.in .modal-dialog{margin-left:-190px!important}" +
            ".modal-body{min-height:${height}px !important;width:${width}px}";

        // JavaScript padrão: esconde botões nativos, injeta scope e serviços Angular
        private final String defaultJs =
            "</style>" +
            "<div id=\"myPopUp\">" +
            "<script type=\"text/javascript\">" +
            "${init}" +
            "$(\".modal-footer-right\").css(\"display\", \"none\");" +
            "$(\".modal-body\").css(\"height\", \"${height}px !important;\");" +
            "var scope=angular.element($(\"#myPopUp\")).scope();" +
            "var scopeInjector=angular.element($(\"#myPopUp\")).injector();" +
            "var ObjectUtils=null,MessageUtils=null,AngularUtil=null,DateUtils=null," +
            "    NumberUtils=null,ServiceProxy=null,StringUtils=null,SkApplicationInstance=null;" +
            "scopeInjector.invoke([\"ObjectUtils\",\"MessageUtils\",\"AngularUtil\",\"DateUtils\"," +
            "\"NumberUtils\",\"ServiceProxy\",\"StringUtils\",\"SkApplicationInstance\"," +
            "function(l,t,e,i,n,s,r,U){" +
            "ObjectUtils=l,MessageUtils=t,AngularUtil=e,DateUtils=i," +
            "NumberUtils=n,ServiceProxy=s,StringUtils=r,SkApplicationInstance=U" +
            "}]);" +
            "scope.$popupTitle=\"${title}\";";

        public Builder() {
            this.width = 800;
            this.height = 400;
            this.variables = new HashMap<>();
        }

        public Builder setTitle(String title) {
            this.title = title;
            return this;
        }

        public Builder setJsFile(InputStream jsFile) {
            this.jsFile = jsFile;
            return this;
        }

        public Builder setHtmlFile(InputStream htmlFile) {
            this.htmlFile = htmlFile;
            return this;
        }

        public Builder setCssFile(InputStream cssFile) {
            this.cssFile = cssFile;
            return this;
        }

        public Builder setWidth(int width) {
            this.width = width;
            return this;
        }

        public Builder setHeight(int height) {
            this.height = height;
            return this;
        }

        /**
         * Adiciona uma variável Java ao escopo JavaScript do popup.
         *
         * String  -> var key = 'value';   (aspas simples)
         * Outros  -> var key = value;     (sem aspas -- número, boolean, JSON)
         *
         * Para passar JSON como String sem que as aspas duplas causem problema,
         * o JSON é envolvido em aspas simples, o que é seguro pois nomes de
         * tabelas/colunas não contêm aspas simples.
         */
        public Builder addVariable(String key, Object value) {
            this.variables.put(key, value);
            return this;
        }

        private void readFile(StringBuilder strBuilder, InputStream file) {
            try (BufferedReader reader = new BufferedReader(
                    new InputStreamReader(file, StandardCharsets.UTF_8))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    strBuilder.append(new String(line.getBytes(), StandardCharsets.UTF_8));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        public String build() {
            StringBuilder strBuilder = new StringBuilder();
            strBuilder.append(this.defaultCss);

            if (this.cssFile != null) {
                readFile(strBuilder, this.cssFile);
            }

            strBuilder.append(defaultJs);

            if (this.jsFile != null) {
                readFile(strBuilder, this.jsFile);
            }

            strBuilder.append("</script>");

            if (this.htmlFile != null) {
                readFile(strBuilder, this.htmlFile);
            }

            strBuilder.append("</div>");

            StringBuilder strVariables = new StringBuilder();
            for (Map.Entry<String, Object> variable : this.variables.entrySet()) {
                String value;
                if (variable.getValue() instanceof String) {
                    value = "'" + variable.getValue() + "'";
                } else {
                    value = variable.getValue().toString();
                }
                strVariables.append("var ")
                            .append(variable.getKey())
                            .append(" = ")
                            .append(value)
                            .append(";");
            }

            String strPopUp = strBuilder.toString();
            strPopUp = strPopUp.replace("${title}", this.title != null ? this.title : "");
            strPopUp = strPopUp.replace("${width}", String.valueOf(this.width));
            strPopUp = strPopUp.replace("${height}", String.valueOf(this.height));
            strPopUp = strPopUp.replace("${init}", strVariables.toString());

            return strPopUp.trim();
        }
    }
}
