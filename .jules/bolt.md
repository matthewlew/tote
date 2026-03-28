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

## 2026-03-16 - Precomputing O(N^2) Hash Maps for Render Loops
**Learning:** Calling functions that iterate through large data structures (like checking `isSavedPlace(p.name)` which iterats over `PLACES`) inside a list render loop (e.g. `items.forEach`) creates an expensive O(N^2) bottleneck. However, care must be taken with asynchronous event listeners (like click handlers) inside the same loop to avoid capturing stale closures.
**Action:** Precompute an O(1) hash map (e.g. a `Set` of normalized values) *before* the render loop and use it for synchronous lookups during initialization. Leave the original live-data function calls (like `isSavedPlace()`) inside asynchronous event handlers to ensure they fetch the latest state.
