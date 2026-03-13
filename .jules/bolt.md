## Bolt's Journal

## 2025-03-08 - [Batching DOM updates with DocumentFragment]
**Learning:** Because this project explicitly eschews UI frameworks (like React or Vue) to remain a pure, easily clonable vanilla template, it lacks a Virtual DOM to batch updates automatically. When rendering or sorting large category lists (e.g., hundreds of items), inserting rows individually into the DOM causes expensive O(N) reflows and repaints, creating noticeable layout thrashing.
**Action:** When working on vanilla JS projects with large lists, always use `DocumentFragment` to batch DOM node creation and append the fragment entirely to the live DOM in a single operation.
