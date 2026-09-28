> Fonte oficial: https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-scroller/ (snapshot 2026-09-28)

# Scroller

As barras de rolagem servem para navegar em uma série de elementos ou uma lista dentro de um determinado espaço e podem ser utilizadas na horizontal ou vertical.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.

Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

demo.js

```jsx
import React from 'react';
import { EzScroller } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    /**
     * O uso da tag style não é recomendado, utilizamos para esse caso de uso apenas para facilitar a exemplificação do EzScroller.
     */
    <EzScroller style={{"max-height": "100px"}} direction="both">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.</p>
        <p>Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.</p>
        <p>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
    </EzScroller>
);

export default Demo;
```

## Variações e estados

### Scroll na direção Vertical

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.

Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

demo.js

```jsx
import React from 'react';
import { EzScroller } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    /**
     * O uso da tag style não é recomendado, utilizamos para esse caso de uso apenas para facilitar a exemplificação do EzScroller.
     */
    <EzScroller style={{"max-height": "100px"}} direction="vertical">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.</p>
        <p>Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.</p>
        <p>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
    </EzScroller>
);

export default Demo;
```

### Scroll na direção Horizontal

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.

Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

### Scroll em ambas direções

(Vertical e Horizontal)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.

Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

demo.js

```jsx
import React from 'react';
import { EzScroller } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    /**
     * O uso da tag style não é recomendado, utilizamos para esse caso de uso apenas para facilitar a exemplificação do EzScroller.
     */
    <EzScroller style={{"max-height": "100px"}} direction="both">
        <p style={{"white-space": "nowrap"}}>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.</p>
        <p style={{"white-space": "nowrap"}}>Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.</p>
        <p style={{"white-space": "nowrap"}}>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
        <p style={{"white-space": "nowrap"}}>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
        <p style={{"white-space": "nowrap"}}>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
    </EzScroller>
);

export default Demo;
```

### Scroll com efeito de sombreamento

> Propriedade utilizada: **activeShadow**

#### Scroll na direção Vertical

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.

Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

#### Scroll na direção Horizontal

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.

Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.

demo.js

```jsx
import React from 'react';
import { EzScroller } from '@sankhyalabs/ezui/react/components';

const Demo = () => (
    /**
     * O uso da tag style não é recomendado, utilizamos para esse caso de uso apenas para facilitar a exemplificação do EzScroller.
     */
    <EzScroller style={{"max-height": "100px"}} direction="horizontal" activeShadow="true">
        <p style={{"white-space": "nowrap"}}>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate pretium mauris, id euismod tellus placerat in. Proin nec tempor tellus. Nullam luctus eros sit amet mattis varius. Vestibulum suscipit massa eu libero porta, sed vestibulum tortor euismod. Nulla vel nibh felis. Nunc interdum, ipsum et iaculis faucibus, nisl orci hendrerit lorem, ac facilisis nulla arcu consequat sapien. Ut pulvinar ut diam vitae elementum. Pellentesque consectetur iaculis ultricies.</p>
        <p style={{"white-space": "nowrap"}}>Curabitur sollicitudin nisl lorem, sit amet laoreet nunc tincidunt iaculis. Quisque maximus nunc non ex tristique, in ullamcorper enim dignissim. Quisque elementum ipsum in quam sagittis dictum. Maecenas finibus ex eu bibendum pretium. Vestibulum varius varius orci, nec ornare augue posuere at. Sed sit amet laoreet est. Donec facilisis porttitor dolor, eget vulputate ex feugiat in. Suspendisse quam odio, venenatis a justo eget, blandit euismod leo. Vivamus nisl eros, malesuada at mollis a, accumsan quis dui. Vivamus consectetur ipsum a urna cursus, sit amet varius turpis consequat.</p>
        <p style={{"white-space": "nowrap"}}>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
        <p style={{"white-space": "nowrap"}}>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
        <p style={{"white-space": "nowrap"}}>Etiam pharetra pharetra suscipit. Etiam in purus molestie, varius ligula eu, ornare enim. Cras cursus sit amet massa in rutrum. Curabitur posuere lectus magna, et luctus tellus finibus a. Vivamus dui risus, euismod ut dapibus in, iaculis et eros. Curabitur volutpat fermentum diam, et finibus diam accumsan facilisis. Morbi tincidunt sem turpis, eget bibendum enim eleifend a. In euismod velit at tincidunt sollicitudin. Vestibulum ullamcorper nulla cursus, suscipit velit sit amet, iaculis sapien. In nec tincidunt ligula, vel ornare neque. Vivamus a nisl interdum, interdum augue quis, semper arcu. Duis eget ante id dolor fermentum facilisis a eget augue. Maecenas quis fermentum velit.</p>
    </EzScroller>
);

export default Demo;
```

#### Scroll em ambas direções

(Vertical e Horizontal)

Importante

Somente na vertical e na horizontal conseguimos utilizar o efeito de sombreamento.

## API do componente

### Properties

| Property | Attribute | Description | Type | Default |
|---|---|---|---|---|
| activeShadow | active-shadow | Define se haverá efeito de sombreado. | boolean | false |
| direction | direction | Define a direção em que haverá scroll. | EzScrollDirection.BOTH \| EzScrollDirection.HORIZONTAL \| EzScrollDirection.VERTICAL | undefined |
| locked | locked | Define se o scroll estará bloqueado. | boolean | false |
| navigationMode | navigation-mode | Define o modo de navegação: 'scrollbar' (padrão) ou 'buttons' (botões de carrossel). | EzScrollNavigationMode.BUTTONS \| EzScrollNavigationMode.SCROLLBAR | EzScrollNavigationMode.SCROLLBAR |
| scrollAmount | scroll-amount | Define a quantidade de pixels que será rolado ao clicar nos botões de navegação. | number | 200 |

### Dependencies

#### Used by

  * ez-guide-navigator
  * ez-sidebar-navigator

#### Depends on

  * ez-button
  * ez-icon

### CSS Variables

| Variable | Description |
|---|---|
| --ez-scroller--box-shadow-color | Define a cor de efeito de sombreado com componente. |
| --ez-scroller__nav-button--spacing | Define o espaçamento entre os botões de navegação e o conteúdo. |
| --ez-scroller__scrollbar--color-default | Define a cor da barra de rolagem do componente. |
| --ez-scroller__scrollbar--color-background | Define a cor de fundo da barra de rolagem do componente. |
| --ez-scroller__scrollbar--color-hover | Define a cor do hover na barra de rolagem do componente. |
| --ez-scroller__scrollbar--color-clicked | Define a cor do active na barra de rolagem do componente. |
| --ez-scroller__scrollbar--border-radius | Define o raio da borda da barra de rolagem do componente. |
| --ez-scroller__scrollbar--width | Define a largura da barra de rolagem do componente. |
| --ez-scroller__max-height | Define o a altura máxima do componente. |
| --ez-scroller__scrollbar--padding-right | Define o espaçamento interno direito da barra de rolagem do componente. |
| --ez-scroller__nav-button--size | Define o tamanho do botão de navegação. |
| --ez-scroller__nav-button--border-radius | Define o raio da borda do botão de navegação. |
| --ez-scroller__nav-button--gradient-width | Define a largura do gradiente ao lado do botão. |
