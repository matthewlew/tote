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

## 2024-05-15 - [Optimize nested array search O(N^2) bottlenecks]
**Learning:** `PLACES.some(...)` checks with string manipulations inside a render loop over `M` items (e.g., in `renderCollectionDetail`) causes `O(M*N)` time complexity, resulting in severe render lag on large datasets. Additionally, caching this state in an event listener closure (`btnBookmarkAll`) causes desync bugs if the global state changes before the listener fires.
**Action:** Precompute an O(1) hash map `Set` of normalized strings *before* iterating to reduce complexity to O(M+N). Ensure event listeners that fire asynchronously after rendering continue checking live state (or recompute the cache) rather than relying on stale closures.
