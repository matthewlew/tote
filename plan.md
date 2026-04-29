1. **Add `aria-keyshortcuts` to all buttons with shortcuts**
   - Location button: `<button class="loc-btn" id="btnEnableLoc" aria-keyshortcuts="l">`
   - Filter pills: `<button class="fpill" data-cat="All" aria-keyshortcuts="1">` (and so on for 2,3,4,5,6)

2. **Hide visual shortcut hints and structural symbols from screen readers using `aria-hidden="true"`**
   - Location button shortcut `span` and `span.arr`: `<span aria-hidden="true"><span class="shortcut">l</span> <span class="arr">→</span></span>`
   - Filter pill shortcuts: `<span class="shortcut" aria-hidden="true">1</span>`
   - Browse neighborhood button: `<span class="arr" aria-hidden="true">→</span>`

3. **Add "Esc" visual hints and `aria-keyshortcuts` to Back/Close buttons**
   - Nbhd Back button (`#btnNbhdBack`): `<button class="back-btn" id="btnNbhdBack" aria-keyshortcuts="Escape">← Back <span class="shortcut" aria-hidden="true">esc</span></button>`
   - Collection Back button (`#btnCollBack`): In JS `renderCollectionDetail`, `<button class="coll-detail-back" id="btnCollBack" aria-keyshortcuts="Escape">← Back <span class="shortcut" aria-hidden="true">esc</span></button>`

4. **Implement Global Escape Key Handling**
   - Add a global `keydown` listener for `Escape`.
   - Priority 1: If `st.screen === 's-nbhd'`, show location screen (`showScreen('s-location')` if no history, but actually the memory says "pop the previous view from this stack... falling back to 's-location'"). I'll look into `st.screenHistory`. Wait, `st.screenHistory` doesn't exist, I need to check memory again. "The application uses an array-based stack (`st.screenHistory` on the global `st` object) to track navigation state... Ensure initial loading states ('loading', 's-loading') are explicitly excluded". I need to implement `st.screenHistory`.
   - Priority 2: If in Explore tab and Collection Detail is open (`!document.getElementById('exploreDetail').hidden`), close it (`closeCollection()`), restore focus to triggered card.
   - Priority 3: If `st.openId` is set, close it (`toggleItem(st.openId)`), restore focus to triggered row.

5. **Implement Screen History for Navigation**
   - Modify `showScreen(id)` to push previous screen to `st.screenHistory`.
   - Update `btnNbhdBack` click and Escape logic to use `screenHistory` to pop back to the previous screen.
