> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/content/ (snapshot 2026-09-28)

# Content

A seguir será apresentada a documentação e os exemplos de uso da **Content** , controlando tamanhos e estilos.

## Como funciona

A **Sticky** é utilizada para criar um container cujo seu posicionamento seja fixado no topo da página em caso de scroll.

Lorem ipsum dolor sit amet. Eos galisum excepturi est expedita assumenda et dolor facilis aut dolorem dignissimos nam velit nisi! Aut similique ullam rem dolor iste aut numquam ullam est dolorem facere hic vero consequatur ea nulla nobis. Non quis eligendi ab cupiditate perspiciatis sed praesentium natus qui cumque recusandae et voluptatum quasi ut harum nesciunt.

**Sticky Content**

Lorem ipsum dolor sit amet. Eos galisum excepturi est expedita assumenda et dolor facilis aut dolorem dignissimos nam velit nisi! Aut similique ullam rem dolor iste aut numquam ullam est dolorem facere hic vero consequatur ea nulla nobis. Non quis eligendi ab cupiditate perspiciatis sed praesentium natus qui cumque recusandae et voluptatum quasi ut harum nesciunt. Ea cumque provident eos ipsum obcaecati et dolor quam est alias maiores et repellendus voluptates. Non numquam consequuntur sit labore accusantium sed nobis debitis sit omnis molestiae et delectus totam non voluptatum eligendi et explicabo velit. At obcaecati necessitatibus ut omnis aspernatur non omnis necessitatibus eos pariatur commodi ab dolore provident. Sit possimus quisquam qui veniam voluptatem ab sint fugiat. Et aperiam labore qui impedit dolor id consequatur placeat ea magnam quia.

demo.js

```jsx
import React from 'react';

const Demo = () => {
  return (
    <div style={{ height: 200, overflow: 'auto' }}>
      <div className='ez-content'>
        Lorem ipsum dolor sit amet. Eos galisum excepturi est expedita assumenda et dolor facilis aut dolorem
        dignissimos nam velit nisi! Aut similique ullam rem dolor iste aut numquam ullam est dolorem facere hic vero
        consequatur ea nulla nobis. Non quis eligendi ab cupiditate perspiciatis sed praesentium natus qui cumque
        recusandae et voluptatum quasi ut harum nesciunt.
      </div>

      <div className='ez-content--sticky ez-flex--column'>
        <b className='ez-flex' style={{ background: 'var(--ifm-link-color)', color: 'white', padding: 5}}>
          Sticky Content
        </b>
      </div>

      <div className='ez-content'>
        Lorem ipsum dolor sit amet. Eos galisum excepturi est expedita assumenda et dolor facilis aut dolorem
        dignissimos nam velit nisi! Aut similique ullam rem dolor iste aut numquam ullam est dolorem facere hic vero
        consequatur ea nulla nobis. Non quis eligendi ab cupiditate perspiciatis sed praesentium natus qui cumque
        recusandae et voluptatum quasi ut harum nesciunt.

        Ea cumque provident eos ipsum obcaecati et dolor quam est alias maiores et repellendus voluptates. Non numquam
        consequuntur sit labore accusantium sed nobis debitis sit omnis molestiae et delectus totam non voluptatum
        eligendi et explicabo velit.

        At obcaecati necessitatibus ut omnis aspernatur non omnis necessitatibus eos pariatur commodi ab dolore
        provident. Sit possimus quisquam qui veniam voluptatem ab sint fugiat. Et aperiam labore qui impedit dolor id
        consequatur placeat ea magnam quia.
      </div>
    </div>
  );
};

export default Demo;
```
