package br.com.sankhya.customizacao.nomedemanda.exception;

/**
 * Exceção de domínio da demanda NomeDemanda.
 *
 * Usada para erros de negócio — regras violadas, estados inválidos, registros não encontrados.
 * Não usada para erros técnicos inesperados (esses sobem como Exception genérica).
 *
 * Convenção de códigos:
 *   [NOM_XXXX] — prefixo da demanda (3 letras) + sequencial de 4 dígitos
 *   Exemplo: [VGM_0001] para demanda de Viagem, [ENT_0001] para Entregas
 *
 * Regra de borda:
 *   Esta exceção NUNCA sobe para a plataforma Sankhya.
 *   Em actionbutton/ e event/, capturar e converter para MGEModelException:
 *
 *   } catch (NomeModuloException e) {
 *       throw MGEModelException.prettyMsg(e.getMessage(), e);
 *   }
 *
 * O getMessage() retorna a mensagem com código, pronta para exibição ao usuário.
 * O código no prefixo permite localizar o ponto exato no fonte sem precisar de stack trace.
 */
public class NomeModuloException extends Exception {

    public NomeModuloException(String message) {
        super(message);
    }

    public NomeModuloException(String message, Throwable cause) {
        super(message, cause);
    }

    // -------------------------------------------------------------------------
    // Fábrica de mensagens — centraliza os textos e códigos rastreáveis
    // Adicionar um método estático por tipo de erro de negócio da demanda.
    // -------------------------------------------------------------------------

    /** Registro não encontrado pela chave informada. */
    public static NomeModuloException naoEncontrado(String entidade, BigDecimal id) {
        return new NomeModuloException(
                "[NOM_0001] " + entidade + " com ID " + id + " não encontrado.");
    }

    /** Operação inválida para o estado atual do registro. */
    public static NomeModuloException statusInvalido(String statusAtual, String operacao) {
        return new NomeModuloException(
                "[NOM_0002] Status '" + statusAtual + "' não permite a operação '" + operacao + "'.");
    }

    /** Transição de status não permitida pelas regras da demanda. */
    public static NomeModuloException transicaoInvalida(String statusAtual, String statusDestino) {
        return new NomeModuloException(
                "[NOM_0003] Transição de '" + statusAtual + "' para '" + statusDestino + "' não permitida.");
    }

    /** Registro pai/vinculado não encontrado ou em estado incompatível. */
    public static NomeModuloException vinculoInvalido(String descricao) {
        return new NomeModuloException("[NOM_0004] " + descricao);
    }

    /** Validação de campo obrigatório ou valor inválido. */
    public static NomeModuloException dadoInvalido(String descricao) {
        return new NomeModuloException("[NOM_0005] " + descricao);
    }
}
