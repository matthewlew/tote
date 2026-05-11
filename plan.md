1. **Add explicit `aria-keyshortcuts`** to buttons that have visual keyboard shortcut indicators (`<span class="shortcut">...</span>`) to improve accessibility parity. Specifically, the "Enable location" button (`btnEnableLoc`) and the category filter pills (`.fpill`). We will use a script to append these attributes to the elements in `index.html`.
2. **Implement Escape key handling** in the main global `keydown` event listener in `index.html`. The logic must respect the hierarchical state layers described in the memory:
   - Check if the user is focused inside an `<input>` or `<textarea>` and ignore the event.
   - If a custom list item/row (`st.openId`) is expanded, collapse it and return focus to the row.
   - If the `exploreDetail` view is open (not hidden), close it (`closeCollection()`) and return focus to the card that opened it, or to the `exploreIndex`.
   - If the `s-nbhd` neighborhood overlay is open, dismiss it by returning to `s-location` and returning focus appropriately.
3. **Add visual `<span class="shortcut">esc</span>` hints** to the "← Back" buttons, specifically `btnNbhdBack` and `btnCollBack`, paired with `aria-hidden="true"` and `aria-keyshortcuts="Escape"` to the button elements to prevent screen reader clutter and improve UX.
4. **Fix accessibility verbosity** for arrow shortcuts (`→`) and text-based separators by adding `aria-hidden="true"` to them to avoid confusing combined text output.
5. **Manage Focus History.** Implement a stack array `st.focusHistory` in `index.html`. Update navigation transitions to save `document.activeElement` before entering overlays or modals and retrieve/focus it when dismissing them via the Esc key or back buttons.
6. Verify file edits by reading specific lines or `git diff`.
7. Write and execute a test script (via Playwright in Python) to verify that the shortcuts (like Esc to close overlays) and accessibility attributes function correctly.
8. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
9. Submit the branch.
