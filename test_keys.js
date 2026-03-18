const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
const expectedKeys = ['d', 't', 'n', 'r', 'c'];
expectedKeys.forEach(k => {
    if (!html.includes(`e.key === '${k}'`)) {
        console.error(`Missing e.key === '${k}'`);
    } else {
        console.log(`Found ${k}`);
    }
});
