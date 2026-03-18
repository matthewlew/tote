const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Update state to include sortBy
html = html.replace(
  "st = {\n  screen:   'loading',",
  "st = {\n  screen:   'loading',\n  sortBy:   'd',"
);

// Update sortedPlaces
html = html.replace(
  "function sortedPlaces() {\n  return PLACES\n    .map(p => ({ ...p, dist: haversine(st.refLat, st.refLng, p.lat, p.lng) }))\n    .sort((a, b) => a.dist - b.dist);\n}",
  `function sortedPlaces() {
  const mapped = PLACES.map(p => ({ ...p, dist: haversine(st.refLat, st.refLng, p.lat, p.lng) }));
  if (st.sortBy === 'n') {
    return mapped.sort((a, b) => a.name.localeCompare(b.name));
  } else if (st.sortBy === 't') {
    return mapped.sort((a, b) => a.cat.localeCompare(b.cat) || a.dist - b.dist);
  }
  return mapped.sort((a, b) => a.dist - b.dist);
}`
);

// Update sorting label
html = html.replace(
  "st.locMode === 'neighborhood' ? '↑ nearest to ' + st.locLabel : '↑ nearest first';",
  `st.locMode === 'neighborhood' ? '↑ nearest to ' + st.locLabel : (st.sortBy === 'n' ? 'a-z name' : (st.sortBy === 't' ? 'a-z type' : '↑ nearest first'));`
);


fs.writeFileSync('index.html', html);
