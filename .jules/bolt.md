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
## 2024-06-25 - DocumentFragment for Batch Appends & State Access in Handlers
**Learning:** Attaching nodes one by one to the live DOM inside large render loops causes expensive layout thrashing (O(N) layout recalculations). Additionally, when optimizing render loops involving lookups with precomputed state (like a `Set`), capturing this localized cache within asynchronous event listeners (e.g., click handlers for toggling bookmarks) leads to stale closures, as the cached state doesn't update on subsequent state changes without a full re-render.
**Action:** Always batch DOM append operations using `document.createDocumentFragment()` to reduce reflows to O(1) when generating lists. When event listeners need to check or modify global state asynchronously, they must rely on live state lookup functions (like `isSavedPlace()`) instead of captured cached variables, ensuring state updates remain synced without requiring complete component redraws.
