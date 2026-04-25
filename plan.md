1. Add an "Escape" key handler in the global `keydown` event listener in `index.html` to allow keyboard users to dismiss overlays and active items, prioritizing full-screen overlays first:
   - Dismiss the `#s-nbhd` screen by showing `#s-location` and focusing on `#btnBrowseNbhd`.
   - If not in `#s-nbhd`, check if an `exploreDetail` collection is open (not hidden), and if so, close it via `closeCollection()`. Re-focus the `.coll-card` by finding the element whose `.coll-title` matches the title inside `.coll-detail-title`.
   - If no full-screen overlays are active, check `st.openId` to see if a list item is expanded. If so, close it via `toggleItem(st.openId)`, returning focus to its `.p-row` header.
2. Add a visual `<span class="shortcut" aria-hidden="true">esc</span>` to the "#btnNbhdBack" button.
3. Add a visual `<span class="shortcut" aria-hidden="true">esc</span>` to the "#btnCollBack" button inside `renderCollectionDetail`.
4. Verify file changes in `index.html` using `git diff index.html`.
5. Write a temporary Playwright script to verify the Escape key behavior visually and save screenshots and a video to `/home/jules/verification/`.
6. Execute all existing automated test scripts: `python3 verify.py`, `python3 verify_keypress.py`, `python3 verify_mobile.py`, `python3 verify_expand.py`, `python3 test_empty_state.py`, and `python3 test_bg.py`.
7. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
