import re

with open('index.html', 'r') as f:
    content = f.read()

# Add aria-hidden="true" to visually structural elements and shortcut spans
# Add aria-keyshortcuts where shortcuts are present

# Fix: btnEnableLoc shortcut span and structural arrow
content = re.sub(
    r'<button class="loc-btn" id="btnEnableLoc">Enable location <span><span class="shortcut">l</span> <span class="arr">→</span></span></button>',
    r'<button class="loc-btn" id="btnEnableLoc" aria-keyshortcuts="l">Enable location <span aria-hidden="true"><span class="shortcut">l</span> <span class="arr">→</span></span></button>',
    content
)

# Fix: btnBrowseNbhd structural arrow
content = re.sub(
    r'<button class="loc-btn ghost" id="btnBrowseNbhd">Browse by neighborhood <span class="arr">→</span></button>',
    r'<button class="loc-btn ghost" id="btnBrowseNbhd">Browse by neighborhood <span class="arr" aria-hidden="true">→</span></button>',
    content
)

# Fix: separator dot in hd-loc-sep
content = re.sub(
    r'<span class="hd-loc-sep">·</span>',
    r'<span class="hd-loc-sep" aria-hidden="true">·</span>',
    content
)

# Fix: fpill shortcuts and add aria-keyshortcuts
for i, cat in enumerate(["All", "Coffee", "Food", "Bars", "Shops", "Culture"], 1):
    old_str = f'<button class="fpill{" active" if i==1 else ""}" data-cat="{cat}">{cat} <span class="shortcut">{i}</span><span class="fpill-n" id="n-{cat}"></span></button>'
    new_str = f'<button class="fpill{" active" if i==1 else ""}" data-cat="{cat}" aria-keyshortcuts="{i}">{cat} <span class="shortcut" aria-hidden="true">{i}</span><span class="fpill-n" id="n-{cat}"></span></button>'
    content = content.replace(old_str, new_str)

# Fix: importBtn and importPasteBtn structural arrows
content = re.sub(
    r'<button class="import-btn" id="importBtn" disabled>\s*<span id="importBtnLabel">Fetch List</span>\s*<span>→</span>\s*</button>',
    r'<button class="import-btn" id="importBtn" disabled>\n          <span id="importBtnLabel">Fetch List</span>\n          <span aria-hidden="true">→</span>\n        </button>',
    content
)
content = re.sub(
    r'<button class="import-btn" id="importPasteBtn" disabled>\s*<span id="importPasteBtnLabel">Parse &amp; Import</span>\s*<span>→</span>\s*</button>',
    r'<button class="import-btn" id="importPasteBtn" disabled>\n          <span id="importPasteBtnLabel">Parse &amp; Import</span>\n          <span aria-hidden="true">→</span>\n        </button>',
    content
)

# Fix: disambigConfirm arrow
content = re.sub(
    r'<button class="import-btn" id="disambigConfirm">\s*<span id="disambigConfirmLabel">Add Selected</span>\s*<span>→</span>\s*</button>',
    r'<button class="import-btn" id="disambigConfirm">\n            <span id="disambigConfirmLabel">Add Selected</span>\n            <span aria-hidden="true">→</span>\n          </button>',
    content
)

# Write back
with open('index.html', 'w') as f:
    f.write(content)

# Fix nbhd-arr
content = re.sub(
    r'<span class="nbhd-arr">→</span>',
    r'<span class="nbhd-arr" aria-hidden="true">→</span>',
    content
)

# Write back
with open('index.html', 'w') as f:
    f.write(content)

# Fix coll-count arrow (in exploreDetail)
content = re.sub(
    r'<span class="coll-count">\$\{coll\.places\.length\} places →</span>',
    r'<span class="coll-count">${coll.places.length} places <span aria-hidden="true">→</span></span>',
    content
)

# Fix back buttons arrows
content = re.sub(
    r'<button class="back-btn" id="btnNbhdBack">← Back</button>',
    r'<button class="back-btn" id="btnNbhdBack"><span aria-hidden="true">←</span> Back</button>',
    content
)
content = re.sub(
    r'<button class="coll-detail-back" id="btnCollBack">← Back</button>',
    r'<button class="coll-detail-back" id="btnCollBack"><span aria-hidden="true">←</span> Back</button>',
    content
)

# Fix sync dot
content = re.sub(
    r'<span class="sync-text">synced · 2m ago</span>',
    r'<span class="sync-text">synced <span aria-hidden="true">·</span> 2m ago</span>',
    content
)


# Write back
with open('index.html', 'w') as f:
    f.write(content)

# Fix import inputs aria-labels
content = re.sub(
    r'<input class="import-input" id="importInput" type="url" inputmode="url"\s*autocomplete="off" autocorrect="off" spellcheck="false"\s*placeholder="https://maps.app.goo.gl/… or maps.google.com/…" />',
    r'<input class="import-input" id="importInput" type="url" inputmode="url"\n            autocomplete="off" autocorrect="off" spellcheck="false"\n            aria-label="Google Maps list URL"\n            placeholder="https://maps.app.goo.gl/… or maps.google.com/…" />',
    content
)
content = re.sub(
    r'<textarea class="import-textarea" id="importPasteArea"\s*placeholder="Paste your list here — one place per line, or copied directly from Google Maps…"></textarea>',
    r'<textarea class="import-textarea" id="importPasteArea"\n            aria-label="Paste list text"\n            placeholder="Paste your list here — one place per line, or copied directly from Google Maps…"></textarea>',
    content
)

# Write back
with open('index.html', 'w') as f:
    f.write(content)

# Fix checkbox input without aria-label inside disambigList
content = re.sub(
    r'<input type="checkbox" data-group="\$\{group\.name\}" data-ci="\$\{ci\}" />',
    r'<input type="checkbox" data-group="${group.name}" data-ci="${ci}" aria-label="Select ${cand.name}" />',
    content
)

# Write back
with open('index.html', 'w') as f:
    f.write(content)
