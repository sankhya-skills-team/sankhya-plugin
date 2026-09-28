> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sanmodule/ (snapshot 2026-09-28)

# Sanmodule

Esta documentação destina-se a exemplificar cenários de implementação e uso das APIs JAVA disponibilizadas pela biblioteca `sanmodule`.

# BootModuleListener

Interface que define listeners para serem executados em um momentos específicos do ciclo de vida de um módulo Sankhya.

Como caso de uso, podemos citar os módulos bff Financeiro e Comercial, que realizam o registro de suas telas no Sankhya Om antes do da inicialização do módulo (`beforeStartModule`).
