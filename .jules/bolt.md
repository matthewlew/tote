## Bolt's Journal

## 2026-03-14 - Batching DOM updates in Vanilla JS
**Learning:** In a vanilla JS architecture, appending hundreds of elements directly to the active DOM in a loop (like lists of rows) causes expensive O(N) layout thrashing and reflows. Since this project explicitly avoids frameworks like React/Vue, this performance bottleneck is particularly critical.
**Action:** Always use `DocumentFragment` to batch DOM appends when rendering lists or generating multiple elements. Append the fragment once to the active DOM to ensure a single reflow instead of N reflows.

## 2026-03-15 - Event Delegation in Vanilla JS
**Learning:** Attaching event listeners inside a loop (like `items.forEach`) for a list of hundreds of elements consumes significant memory and slows down the render loop (`O(N)` listener attachments).
**Action:** Always use event delegation for large lists. Attach a single event listener to the parent container (`listEl`) and use `e.target.closest('.row')` to determine the target element, turning `O(N)` memory into `O(1)`.

## 2026-03-15 - RegExp Precompilation
**Learning:** Re-instantiating the same regular expression literal inside a `.forEach` render loop adds a measurable overhead to execution time because the regex engine compiles it repeatedly.
**Action:** When working with vanilla JS, extract constant regex patterns and assign them to a variable outside the render loop or function to avoid redundant compilations.
## 2026-03-16 - O(N^2) bottlenecks in string matching render loops
**Learning:** Checking elements against a global array inside a `.forEach()` and `.filter()` loop, particularly when string normalization (e.g. `.toLowerCase().replace(/[^a-z0-9]/g, '')`) is involved on both ends for every iteration, scales terribly and causes noticeable UI freezing when lists are large.
**Action:** When a render loop needs to check inclusion against a dynamic or global array with string normalization, precompute a `Set` of the normalized strings once *outside* the render loop, reducing $O(N \times M)$ overhead to $O(N)$ with $O(1)$ lookups.
