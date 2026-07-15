# BeforeLoadListener — Interceptar buscas no JAPE

> Fonte oficial: https://developer.sankhya.com.br/docs/interceptando-buscas-com-beforeloadlistener

## O que é

`@BeforeLoadListener` intercepta a execução do Finder de uma entidade **antes da
query chegar ao banco**, permitindo modificar filtros, adicionar ordenação ou
validar parâmetros de busca. Roda em **todas** as buscas daquela instância.

## Interface

Implementar `br.com.sankhya.jape.core.FinderListener`:

```java
void beforeExecute(EntityMetaData entity, FinderWrapper finder) throws Exception
```

## Exemplo completo (Addon Studio)

```java
import br.com.sankhya.jape.core.FinderListener;
import br.com.sankhya.jape.metadata.EntityMetaData;
import br.com.sankhya.jape.wrapper.FinderWrapper;
import br.com.sankhya.studio.annotations.BeforeLoadListener;

import java.util.logging.Logger;

@BeforeLoadListener(instance = "MinhaInstancia")
public class MinhaInstanciaFiltroSeguranca implements FinderListener {

    private static final Logger logger =
            Logger.getLogger(MinhaInstanciaFiltroSeguranca.class.getName());

    @Override
    public void beforeExecute(EntityMetaData entity, FinderWrapper finder)
            throws Exception {
        finder.where("this.ATIVO = 'S'");
        logger.info("Filtro de seguranca aplicado para a entidade: "
                + entity.getName());
    }
}
```

## Requisitos e regras

- A entidade precisa existir no Dicionário de Dados (via XML ou `@JapeEntity`).
- **Um listener por instância** de entidade.
- Suporta injeção de dependência via `@Inject`.
- Restrito a **entidades adicionais do addon** — não intercepta nativas do sistema.

## Cuidado crítico

`beforeExecute` é chamado em **todas** as buscas da entidade. **Evitar query
pesada ao banco dentro deste método** — vira gargalo em cada listagem/consulta.

## Quando usar

- Filtro de segurança/multiempresa transversal (sempre restringir por `CODEMP`,
  status ativo, etc).
- Forçar ordenação padrão.
- Validar/normalizar parâmetro de busca antes da query.

Para gatilhos de escrita (insert/update/delete) use Entity Listener / evento
(ver `references/acesso-dados.md` e `references/event-java.md`), não o BeforeLoadListener.
