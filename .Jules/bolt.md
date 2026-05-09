## 2026-05-09 - DocumentFragment for Batched Appends
**Learning:** Inside vanilla JS architecture, rendering list items inside a loop by appending directly to the DOM causes O(N) layout thrashing and expensive reflows.
**Action:** Always use `DocumentFragment` to batch DOM appends when generating multiple elements in a loop (e.g., list rendering).
