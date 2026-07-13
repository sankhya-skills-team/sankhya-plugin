package br.com.sankhya.customizacao.utils;

import br.com.sankhya.modelcore.MGEModelException;

/**
 * Utilitário para leitura de arquivos armazenados em colunas BLOB do Sankhya.
 *
 * O Sankhya prefixa o conteúdo binário com um cabeçalho no formato:
 *   __start_fileinformation__{"name":"...","size":...,"type":"...","lastModifiedDate":"..."}__end_fileinformation__
 * seguido dos bytes reais do arquivo.
 *
 * Uso:
 *   byte[] conteudoBlob = (byte[]) vo.getProperty("CAMPO_BLOB");
 *   BlobUtil blob = new BlobUtil(conteudoBlob);
 *   byte[] bytes = blob.getFileData();
 *
 * Referência completa → references/importacao-xls.md
 */
public class Modelo_BlobUtil {

    private static final String MARKER_FIM = "__end_fileinformation__";

    private final String nomeArquivo;
    private final long tamanhoArquivo;
    private final String tipoArquivo;
    private final String dataModificacao;
    private final byte[] dadosArquivo;

    public Modelo_BlobUtil(byte[] conteudoBlob) throws MGEModelException {
        if (conteudoBlob == null || conteudoBlob.length == 0) {
            throw new MGEModelException("Conteúdo BLOB vazio.");
        }

        byte[] markerFimBytes;
        try {
            markerFimBytes = MARKER_FIM.getBytes("UTF-8");
        } catch (Exception e) {
            throw new MGEModelException("Erro interno ao processar BLOB.");
        }

        int posMarkerFim = indexOfBytes(conteudoBlob, markerFimBytes);

        if (posMarkerFim < 0) {
            // Sem cabeçalho Sankhya — trata como arquivo bruto sem metadados
            this.nomeArquivo = "arquivo";
            this.tamanhoArquivo = conteudoBlob.length;
            this.tipoArquivo = "";
            this.dataModificacao = "";
            this.dadosArquivo = conteudoBlob;
        } else {
            int inicioDados = posMarkerFim + markerFimBytes.length;
            this.dadosArquivo = new byte[conteudoBlob.length - inicioDados];
            System.arraycopy(conteudoBlob, inicioDados, this.dadosArquivo, 0, this.dadosArquivo.length);

            String cabecalhoTexto;
            try {
                cabecalhoTexto = new String(conteudoBlob, 0, posMarkerFim, "UTF-8");
            } catch (Exception e) {
                cabecalhoTexto = "";
            }

            int inicioJson = cabecalhoTexto.indexOf("{");
            String json = (inicioJson >= 0) ? cabecalhoTexto.substring(inicioJson) : "{}";

            this.nomeArquivo = extrairCampoJsonString(json, "name", "arquivo");
            this.tipoArquivo = extrairCampoJsonString(json, "type", "");
            this.dataModificacao = extrairCampoJsonString(json, "lastModifiedDate", "");

            long size = 0;
            try {
                size = Long.parseLong(extrairCampoJsonNumerico(json, "size", "0"));
            } catch (Exception ignored) {
            }
            this.tamanhoArquivo = size;
        }
    }

    /** Nome completo do arquivo declarado no cabeçalho (ex: "planilha.xls"). */
    public String getFileName() {
        return nomeArquivo;
    }

    /** Tamanho em bytes declarado no cabeçalho. */
    public long getFileSize() {
        return tamanhoArquivo;
    }

    /** MIME type declarado no cabeçalho (ex: "application/vnd.ms-excel"). */
    public String getFileType() {
        return tipoArquivo;
    }

    /** Data de modificação declarada no cabeçalho (ex: "May 26, 2026 18:39:23"). */
    public String getFileLastModifiedDate() {
        return dataModificacao;
    }

    /** Bytes reais do arquivo — tudo que vem após o marcador __end_fileinformation__. */
    public byte[] getFileData() {
        return dadosArquivo;
    }

    /** Bytes em representação hexadecimal maiúscula (ex: "504B0304..."). */
    public String getFileDataHEX() {
        StringBuilder sb = new StringBuilder(dadosArquivo.length * 2);
        for (byte b : dadosArquivo) {
            sb.append(String.format("%02X", b & 0xFF));
        }
        return sb.toString();
    }

    /** Extensão com ponto (ex: ".xls", ".xlsx"). Vazio se não houver extensão. */
    public String getFileExtension() {
        int pos = nomeArquivo.lastIndexOf('.');
        return (pos < 0) ? "" : nomeArquivo.substring(pos);
    }

    /** Nome sem extensão (ex: "planilha" para "planilha.xls"). */
    public String getFileNamePure() {
        int pos = nomeArquivo.lastIndexOf('.');
        return (pos < 0) ? nomeArquivo : nomeArquivo.substring(0, pos);
    }

    // --- helpers de extração de JSON simples (sem dependência externa) ----------

    private String extrairCampoJsonString(String json, String campo, String valorPadrao) {
        String chave = "\"" + campo + "\":\"";
        int inicio = json.indexOf(chave);
        if (inicio < 0) return valorPadrao;
        inicio += chave.length();
        int fim = json.indexOf("\"", inicio);
        return (fim < 0) ? valorPadrao : json.substring(inicio, fim);
    }

    private String extrairCampoJsonNumerico(String json, String campo, String valorPadrao) {
        String chave = "\"" + campo + "\":";
        int inicio = json.indexOf(chave);
        if (inicio < 0) return valorPadrao;
        inicio += chave.length();
        int fimVirgula = json.indexOf(",", inicio);
        int fimChave = json.indexOf("}", inicio);
        int fim;
        if (fimVirgula >= 0 && fimChave >= 0) fim = Math.min(fimVirgula, fimChave);
        else if (fimVirgula >= 0) fim = fimVirgula;
        else if (fimChave >= 0) fim = fimChave;
        else return valorPadrao;
        return json.substring(inicio, fim).trim();
    }

    private int indexOfBytes(byte[] haystack, byte[] needle) {
        outer:
        for (int i = 0; i <= haystack.length - needle.length; i++) {
            for (int j = 0; j < needle.length; j++) {
                if (haystack[i + j] != needle[j]) continue outer;
            }
            return i;
        }
        return -1;
    }
}
