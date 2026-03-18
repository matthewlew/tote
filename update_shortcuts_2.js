const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const shortcutSection = `
    /* Location shortcut */
    if (e.key === 'l' || e.key === 'L') {
`;

const shortcutsImpl = `
    /* Shortcuts */
    if (st.screen === 's-app') {
      if (e.key === 'd' || e.key === 'D') {
        e.preventDefault();
        st.sortBy = 'd';
        renderList(true);
        updateLocUI();
        return;
      }
      if (e.key === 't' || e.key === 'T') {
        e.preventDefault();
        st.sortBy = 't';
        renderList(true);
        updateLocUI();
        return;
      }
      if (e.key === 'n' || e.key === 'N') {
        e.preventDefault();
        st.sortBy = 'n';
        renderList(true);
        updateLocUI();
        return;
      }
      if (e.key === 'r' || e.key === 'R') {
        e.preventDefault();
        const items = filteredPlaces();
        if (items.length) {
          const rand = items[Math.floor(Math.random() * items.length)];
          toggleItem(rand.id);
          const el = document.querySelector(\`.place[data-pid="\${rand.id}"] .p-row\`);
          if (el) {
            el.focus();
            el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
        return;
      }
      if (e.key === 'c' || e.key === 'C') {
        e.preventDefault();
        if (st.openId !== null) {
          const p = PLACES.find(x => x.id === st.openId);
          if (p) {
            const text = \`\${p.name}\\n\${p.cat} · \${p.tag}\\n\${mapsUrl(p.q)}\`;
            navigator.clipboard.writeText(text);
          }
        }
        return;
      }
    }

    /* Location shortcut */
    if (e.key === 'l' || e.key === 'L') {
`;

html = html.replace(shortcutSection, shortcutsImpl);

fs.writeFileSync('index.html', html);
