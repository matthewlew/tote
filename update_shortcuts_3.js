const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const UI_shortcut_base = `<span class="res-sort" id="resSort">`;

const UI_shortcut_impl = `<span class="res-sort" id="resSort" aria-live="polite">↑ nearest first</span>
      <span class="res-sort shortcut" style="margin-left:8px" aria-hidden="true">d</span>
      <span class="res-sort shortcut" aria-hidden="true">t</span>
      <span class="res-sort shortcut" aria-hidden="true">n</span>`;

html = html.replace(`<span class="res-sort" id="resSort">↑ nearest first</span>`, UI_shortcut_impl);

const UI_r_shortcut = `<span class="res-n" id="resN">— places</span>
      <span class="res-n shortcut" style="margin-left:8px" aria-hidden="true">r</span>
      <span class="res-n shortcut" aria-hidden="true">c</span>`;

html = html.replace(`<span class="res-n" id="resN">— places</span>`, UI_r_shortcut);


const updateLocUI_find = `function updateLocUI() {
  document.getElementById('locName').textContent = st.locLabel;
  document.getElementById('locSub').textContent  = st.locSub;
  document.getElementById('resSort').textContent =
    st.locMode === 'neighborhood' ? '↑ nearest to ' + st.locLabel : (st.sortBy === 'n' ? 'a-z name' : (st.sortBy === 't' ? 'a-z type' : '↑ nearest first'));
}`;

const updateLocUI_replace = `function updateLocUI() {
  document.getElementById('locName').textContent = st.locLabel;
  document.getElementById('locSub').textContent  = st.locSub;
  const resSortEl = document.getElementById('resSort');
  if (resSortEl) {
    if (st.locMode === 'neighborhood') {
      resSortEl.textContent = '↑ nearest to ' + st.locLabel;
    } else {
      if (st.sortBy === 'n') resSortEl.textContent = 'a-z name';
      else if (st.sortBy === 't') resSortEl.textContent = 'a-z type';
      else resSortEl.textContent = '↑ nearest first';
    }

    // update sort button accessibility
    resSortEl.setAttribute('aria-label', \`Sort by \${st.sortBy === 'n' ? 'name' : (st.sortBy === 't' ? 'type' : 'distance')}, currently ascending\`);
  }
}`;

html = html.replace(updateLocUI_find, updateLocUI_replace);

fs.writeFileSync('index.html', html);
