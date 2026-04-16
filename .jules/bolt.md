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

## 2026-03-16 - O(N^2) bottlenecks in Vanilla JS
**Learning:** Calling an `O(N)` search function like `isSavedPlace` inside a loop (like `sorted.filter` or `sorted.forEach`) creates an `O(N^2)` bottleneck. When rendering large collections of items (like in `renderCollectionDetail`), this causes significant synchronous blocking on the main thread.
**Action:** Precompute an `O(1)` hash map (e.g., `Set`) of the normalized values outside the loop before iterating. However, avoid capturing this cached state inside asynchronous event listeners (like click handlers) defined in the same scope, as it creates stale closures. Always use live global state or functions (like `isSavedPlace`) for async event handlers to prevent desync bugs.
