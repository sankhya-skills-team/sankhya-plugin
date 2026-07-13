package br.com.sankhya.customizacao.nomedemanda.helper;

import br.com.sankhya.customizacao.utils.MessageUtils;
import br.com.sankhya.customizacao.utils.PopUpBuilder;

import java.math.BigDecimal;

/**
 * Helper para popups personalizados — encapsula PopUpBuilder para casos comuns.
 *
 * EXCEÇÃO DE PACOTE: Este helper fica em nomedemanda.helper (não em actionbutton/)
 * porque pode ser chamado por múltiplos artefatos da mesma demanda:
 * actionbutton/, event/ e regra/ compartilham os mesmos popups.
 * Helpers de apresentação com esse perfil pertencem a helper/, não a um artefato específico.
 *
 * Configuração no Sankhya:
 *   - Nenhum registro necessário, apenas inclusão no JAR
 *   - Arquivos HTML/JS em Java/resources/{modulo}/popup/
 */
public class Modelo_PopUpHelper {

    private Modelo_PopUpHelper() {
        throw new UnsupportedOperationException("Não é permitido instanciar esta classe");
    }

    // -------------------------------------------------------------------------
    // Popup de Confirmação Simples
    // -------------------------------------------------------------------------

    public static void confirmarExclusao(BigDecimal idRegistro) throws Exception {
        String popup = new PopUpBuilder.Builder()
            .setTitle("Confirmação de Exclusão")
            .setHtmlFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpConfirmacao.html"))
            .setJsFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpConfirmacao.js"))
            .setWidth(400)
            .setHeight(200)
            .addVariable("idRegistro", idRegistro)
            .build();

        MessageUtils.showInfo(popup);
    }

    // -------------------------------------------------------------------------
    // Popup de Seleção em Grid
    // -------------------------------------------------------------------------

    public static void selecionarTipoOperacao(BigDecimal nuNota, String tipoMov) throws Exception {
        String popup = new PopUpBuilder.Builder()
            .setTitle("Selecione o Tipo de Operação")
            .setHtmlFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpSelecao.html"))
            .setJsFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpSelecao.js"))
            .setWidth(700)
            .setHeight(400)
            .addVariable("nuNota", nuNota)
            .addVariable("tipoMov", tipoMov)
            .build();

        MessageUtils.showInfo(popup);
    }

    // -------------------------------------------------------------------------
    // Popup de Formulário
    // -------------------------------------------------------------------------

    public static void coletarDadosAdicionais(BigDecimal codProj, BigDecimal codEmp) throws Exception {
        String popup = new PopUpBuilder.Builder()
            .setTitle("Informações Adicionais")
            .setHtmlFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpFormulario.html"))
            .setJsFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpFormulario.js"))
            .setWidth(500)
            .setHeight(350)
            .addVariable("codProj", codProj)
            .addVariable("codEmp", codEmp)
            .build();

        MessageUtils.showInfo(popup);
    }

    // -------------------------------------------------------------------------
    // Popup de Exibição de Dados
    // -------------------------------------------------------------------------

    public static void exibirDetalhes(BigDecimal codProd) throws Exception {
        String popup = new PopUpBuilder.Builder()
            .setTitle("Detalhes do Produto")
            .setHtmlFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpDetalhes.html"))
            .setJsFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpDetalhes.js"))
            .setWidth(800)
            .setHeight(400)
            .addVariable("codProd", codProd)
            .build();

        MessageUtils.showInfo(popup);
    }

    // -------------------------------------------------------------------------
    // Popup com CSS Customizado
    // -------------------------------------------------------------------------

    public static void popupComEstilo(BigDecimal id, String titulo) throws Exception {
        String popup = new PopUpBuilder.Builder()
            .setTitle(titulo)
            .setHtmlFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpCustom.html"))
            .setJsFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpCustom.js"))
            .setCssFile(Modelo_PopUpHelper.class.getResourceAsStream("/nomedemanda/popup/PopUpCustom.css"))
            .setWidth(600)
            .setHeight(300)
            .addVariable("id", id)
            .build();

        MessageUtils.showInfo(popup);
    }
}