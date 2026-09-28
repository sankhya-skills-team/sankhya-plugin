> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataBinder/ (snapshot 2026-09-28)

# DataBinder

Documentação do componente DataBinder.

## Métodos

### validateByDataunit

O método estático `validateByDataunit` tem como objetivo fazer a validação de dados a partir de um `DataUnit` de forma isolada, sem a dependência de componentes adicionais.

demo.js

```jsx
import React, { useEffect, useState } from 'react';
import { DataUnit } from '@sankhyalabs/core';
import { EzButton, EzForm } from '@sankhyalabs/ezui/react/components';
import DataBinder from '@sankhyalabs/ezui/dist/collection/utils/form/DataBinder';

/**
 * Exemplo de JSON com o metadata do formulário.
 * Os exemplos e a explicação sobre metadata está na documentação do dataUnit.
 */
const metadata = {
    "name": "baixa",
    "label": "baixa",
    "fields": [
        {
            "name": "_dadosBancarios_nomeCliente",
            "label": "Nome do cliente",
            "dataType": "TEXT",
            "userInterface": "SHORTTEXT",
            "readOnly": false,
            "required": true
        },
        {
            "name": "_dadosBancarios_dataCadastro",
            "label": "Data do cadastro",
            "dataType": "DATE",
            "userInterface": "DATE",
            "readOnly": false,
            "required": true
        },
        {
            "name": "_valores_valorDesconto",
            "label": "Desconto",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_valores_valorMulta",
            "label": "Multas",
            "dataType": "NUMBER",
            "userInterface": "DECIMALNUMBER",
            "readOnly": false,
            "required": false
        },
        {
            "name": "_dadosBancarios_historico",
            "label": "Observações",
            "dataType": "TEXT",
            "userInterface": "LONGTEXT",
            "readOnly": true,
            "required": false
        }
    ]
};

const Demo = () => {
    const [dataUnit, setDataUnit] = useState();

    useEffect(() => {
        const dataUnit = new DataUnit();
        dataUnit.addRecord();
        setDataUnit(dataUnit);
    }, []);

    useEffect(() => {
        if (!dataUnit) return;
        dataUnit.metadataLoader = metadataLoader;
        dataUnit.loadMetadata();
    }, [dataUnit]);

    async function metadataLoader() {
        return metadata;
    }

    async function validate() {
        const isValid = await DataBinder.validateByDataunit(dataUnit);
        if (isValid) {
            alert('Campos são válidos!');
            return;
        }
        alert('Ops, campos inválidos!');
    }

    return (
        <div className="ez-flex ez-flex--column">
            <EzButton
                onClick={() => validate()}
                label='Validar'
                className="ez-button--primary ez-margin-bottom--medium"
            />
            {dataUnit &&
                <EzForm
                    dataUnit={dataUnit}
                />
            }
        </div>
    )
};

export default Demo;
```
