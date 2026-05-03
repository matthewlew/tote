1. **Add explicit `Escape` key handling to global keydown listener:**
   - Modify the global `keydown` event listener in `index.html` to handle the `Escape` key.
   - Evaluation order (top-most layers first):
     1. Individual expanded items (`st.openId`): Close the expanded item using `toggleItem(st.openId)`. Return focus to the corresponding `.p-row` that was just closed.
     2. Collection details (`exploreDetail`): If `st.screen === 's-app'` and `st.tab === 'explore'` and `exploreDetail` is not hidden, call `closeCollection()`. Return focus to the last active `.coll-card` if there was one, or the `.tab-btn[data-tab="explore"]`.
     3. Neighborhood picker (`s-nbhd`): If `st.screen === 's-nbhd'`, show the location screen `showScreen('s-location')`.
   - Prevent default behavior and return early after handling to prevent multiple things closing at once.

2. **Manage Focus when closing items:**
   - To properly manage focus, add logic to remember the trigger element before opening `exploreDetail` or `s-nbhd`. Use `st.lastFocus = document.activeElement`.
   - When closing `exploreDetail`, return focus to `st.lastFocus` and clear it.
   - When closing `s-nbhd`, return focus to `st.lastFocus` and clear it.
   - When toggling an item in `toggleItem(id)`, set focus to the `.p-row` of the toggled item when it is being *closed*. (Although it might just be the active element anyway, it's good to ensure it).

3. **Add visual shortcut hints (`esc`) to 'Back' / 'Close' buttons:**
   - On `#btnNbhdBack`, append `<span class="shortcut" aria-hidden="true">esc</span>`.
   - On `#btnCollBack`, append `<span class="shortcut" aria-hidden="true">esc</span>`.

4. **Verify the changes using Playwright:**
   - Write a python script using Playwright to test opening an item and pressing Escape, opening a collection and pressing Escape, and opening the neighborhood picker and pressing Escape.
   - Take screenshots or videos.
   - Run the script and verify everything works smoothly.

5. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
   - Run the pre commit instructions hook.

6. **Submit changes**
   - Create a PR using `submit`.
