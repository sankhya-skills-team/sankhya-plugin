> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-form-config/ (snapshot 2026-09-28)

# Simple Form Config

O **SnkSimpleFormConfig** é um componente que realiz a configuração de um formulário simplificado, geralmente utilizado no SnkSimpleCrud

```jsx
import React from 'react';
import { SnkApplication, SnkSimpleFormConfig } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const paymentMethodsRef = useRef(null);
    const [paymentMethodsDataUnit, setPaymentMethodsDataUnit] = useState(null);

    useEffect(() => {
        setPaymentMethodsDataUnit(new DataUnit("paymentMethods"));
    }, []);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleFormConfig ref={paymentMethodsRef} dataUnit={paymentMethodsDataUnit} configName={'PaymentsFormConfig'} />
        </SnkApplication>
    );
}

export default Demo;
```

## Chave da configuração do formulário

> Propriedade utilizada: **configName**

É preciso informar a chave das configurações do formulário, salva no banco de dados.
Exemplo: `FormCfg:GradeItensFormConfig-PA:br.com.sankhya.com.mov.CentralNotas:TIPMOV-P-8`

## Unidade de dados responsável

> Propriedade utilizada: **dataUnit**

O **SnkSimpleFormConfig** precisa receber o dataUnit relativo ao formulário que receberá as alterações.

## Métodos

### show

Responsável por exibir o componente na tela.
