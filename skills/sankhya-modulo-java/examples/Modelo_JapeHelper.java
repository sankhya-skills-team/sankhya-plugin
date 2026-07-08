package br.com.sankhya.dstech.nomedemanda.helper;

import br.com.sankhya.jape.core.JapeSession;

public class Modelo_JapeHelper {

    private Modelo_JapeHelper() {
        throw new UnsupportedOperationException("Não é permitido instanciar esta classe");
    }

    public static void executeWithTx(JapeRunnable runnable) throws Exception {
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            hnd.execWithTX(runnable::run);
        } finally {
            if (hnd != null) JapeSession.close(hnd);
        }
    }

    public static void executeWithoutTx(JapeRunnable runnable) throws Exception {
        JapeSession.SessionHandle hnd = null;
        try {
            hnd = JapeSession.open();
            runnable.run();
        } finally {
            if (hnd != null) JapeSession.close(hnd);
        }
    }

    @FunctionalInterface
    public interface JapeRunnable {
        void run() throws Exception;
    }
}