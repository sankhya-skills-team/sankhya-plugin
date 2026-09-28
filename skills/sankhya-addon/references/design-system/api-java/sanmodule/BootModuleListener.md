> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sanmodule/BootModuleListener/ (snapshot 2026-09-28)

# BootModuleListener

Interface que define listeners para serem executados em um momentos específicos do ciclo de vida de um módulo Sankhya.

## Casos de uso

### Registro de telas no sistema

Podemos utilizar `BootModuleListener` para registrar telas específica no sistema durante sua execução, como no cado do `mgefin-bff` e `mgecom-bff`.

```java
public class BootModuleListenerImpl implements BootModuleListener {

    @Override
    public void beforeStartModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Inicializando módulo...");
        registryScreens();
    }

    @Override
    public void afterStartModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Módulo inicializado com sucesso.");
    }

    @Override
    public void beforeStopModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Interrompendo execução do módulo...");
        removeScreens();
    }

    @Override
    public void afterStopModule(ServletContextEvent context) {
        System.out.println("[BootModuleListenerImpl] Módulo finalizado com sucesso.");
    }

    private void registryScreens(){
      System.out.println("[BootModuleListenerImpl] Registrando telas no SankhyaOm.");
      //Simulação do registro de telas
    }

    private void removeScreens(){
      System.out.println("[BootModuleListenerImpl] Removendo telas registradas do SankhyaOm.");
      //Simulação do registro de telas
    }

}
```
