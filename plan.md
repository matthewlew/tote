1. **Initialize focusHistory state variable**
   - In `index.html`, add `focusHistory: []` to the `const st = { ... }` object to track the active element before opening full-screen overlays like `s-nbhd` and `exploreDetail`.

2. **Implement Escape key handling**
   - In `index.html`, add an `Escape` key condition within the main `keydown` event listener.
   - The handler should check states in reverse visual order:
     - If `st.screen === 's-nbhd'`, set `st.screen = 's-location'`, pop the focus stack, and refocus the originating element.
     - If `st.tab === 'explore'` and `exploreDetail` is open (`!document.getElementById('exploreDetail').hidden`), call `closeCollection()`, pop the focus stack, and refocus.
     - If an item is expanded (`st.openId !== null`), close it by calling `toggleItem(st.openId)`.

3. **Update trigger buttons to push to focusHistory**
   - Update `document.getElementById('btnChangeLoc').addEventListener` and `document.getElementById('btnBrowseNbhd').addEventListener` to push `document.activeElement` to `st.focusHistory` before showing `s-nbhd`.
   - Update `card.addEventListener('click', ...)` and `card.addEventListener('keydown', ...)` in `renderExploreIndex` to push `document.activeElement` to `st.focusHistory` before showing `exploreDetail`.
   - Ensure `closeCollection()` logic is robust and correctly handles focus restoration for standard mouse clicks too.

4. **Verify changes by running the test suite**
   - `node test.js`
   - `python3 test_bg.py`
   - `python3 test_empty_state.py`
   - `python3 verify.py`
   - `python3 verify_expand.py`
   - `python3 verify_keypress.py`
   - `python3 verify_mobile.py`

5. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
