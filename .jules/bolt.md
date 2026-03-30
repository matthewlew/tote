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

## 2024-05-31 - [Optimize Render Loops with DocumentFragment & O(1) Lookups]
**Learning:** Found O(N^2) bottlenecks when rendering collections due to repeatedly normalizing strings and searching arrays via `.some()` inside the `.forEach` render loop, combined with expensive layout thrashing when appending individual child elements to lists.
**Action:** When rendering arrays in vanilla JS, use `DocumentFragment` to batch DOM appends into a single attachment step to prevent layout recalculation thrashing. For nested searches within a render loop, precompute normalized data into an O(1) hash map (like a `Set`) *outside* the loop to reduce O(N^2) logic back to O(N). Avoid capturing this precomputed `Set` state inside async closures (like event listeners) — always fetch live state in async scopes to avoid desyncs.
