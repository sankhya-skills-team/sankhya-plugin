// Renderiza cada página, expande "Apresentar código" e salva o HTML limpo do <article>
import { chromium } from 'playwright';
import fs from 'fs'; import path from 'path';
const HOST = 'https://gilded-nasturtium-6b64dd.netlify.app';
// o sitemap publica o domínio placeholder do Docusaurus; troca pelo host real
const sitemap = await (await fetch(`${HOST}/sitemap.xml`)).text();
const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1].replace(/https:\/\/[^/]+/, HOST)).filter(u => u.includes('/docs/'));
const b = await chromium.launch();
async function worker(queue) {
  const p = await b.newPage();
  while (queue.length) {
    const u = queue.shift(); const rel = u.replace(HOST+'/docs/','').replace(/\/$/,'') || 'index';
    try {
      await p.goto(u, {waitUntil:'networkidle', timeout:60000});
      for (const t of await p.locator('article ez-collapsible-box[label="Apresentar código"] button.collapsible-box__title').all()) await t.click().catch(()=>{});
      await p.waitForTimeout(500);
      const html = await p.evaluate(() => {
        const a = document.querySelector('article').cloneNode(true);
        a.querySelectorAll('pre').forEach(pre => {
          const cls = (pre.className.match(/language-(\w+)/)||[])[1] || '';
          const lines = [...pre.querySelectorAll('.token-line')];
          const txt = lines.length ? lines.map(l=>l.textContent).join('\n') : pre.textContent;
          const n = document.createElement('pre'); n.setAttribute('data-lang', cls); n.textContent = txt; pre.replaceWith(n);
        });
        a.querySelectorAll('[class*="taskBar"], nav, .theme-doc-footer, .pagination-nav, svg, style, button, ez-tabselector').forEach(e=>e.remove());
        return a.innerHTML;
      });
      const out = path.join('raw', rel + '.html'); fs.mkdirSync(path.dirname(out), {recursive:true});
      fs.writeFileSync(out, `<!-- ${u} -->\n` + html);
    } catch (e) { console.log('ERRO', u, e.message.split('\n')[0]); }
  }
  await p.close();
}
const q = [...urls]; await Promise.all(Array.from({length:6}, ()=>worker(q)));
await b.close(); console.log('ok', urls.length);
