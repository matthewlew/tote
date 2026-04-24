1. **Add explicit `Escape` key handling to global keydown listener:**
   - Update `document.addEventListener('keydown', ...)` in `index.html`.
   - Add a check for `e.key === 'Escape'`.
   - Close the highest level foreground overlay or open state:
     - Check if neighborhood selection is open (`st.screen === 's-nbhd'`). If so, call `showScreen('s-location')` (the previous screen, or use history if it exists, but for now `s-location` is what the back button does).
     - Check if explore detail is open (`!document.getElementById('exploreDetail').hidden`). If so, call `closeCollection()`.
     - Check if a place detail is open (`st.openId !== null`). If so, call `toggleItem(st.openId)`.
     - Prevent default behavior for `Escape`.

2. **Add keyboard shortcut visual indicators for Escape:**
   - On the `btnNbhdBack` button, add `<span class="shortcut" aria-hidden="true">esc</span>`.
   - On the `btnCollBack` button, add `<span class="shortcut" aria-hidden="true">esc</span>`.

3. **Verify DOM structure and styles for `.shortcut`:**
   - Ensure `aria-hidden="true"` is applied to these indicators so they are not read by screen readers.
   - Wait, `btnNbhdBack` already has `← Back` text. We can append `<span><span class="shortcut" aria-hidden="true">esc</span></span>`.
   - Make sure `.shortcut` and `var(--accent)` or current styling works correctly for these.
   - Let's make sure history stack behavior is proper if possible, but the prompt says: "always implement explicit 'Escape' key handling in global keydown listeners to consistently dismiss overlays. Prioritize closing full-screen overlays (like the neighborhood picker `s-nbhd`) first, then collection details (`exploreDetail`), and finally individual expanded items/rows (`st.openId`), to ensure hidden background elements aren't closed before visible foreground overlays. Provide visual shortcut hints (`<span class="shortcut">esc</span>`) on the corresponding 'Back' or 'Close' buttons." And "The application uses an array-based stack (`st.screenHistory` on the global `st` object) to track navigation state. When implementing back navigation, pop the previous view from this stack (falling back to 's-location' if empty) rather than hardcoding targets. Ensure initial loading states ('loading', 's-loading') are explicitly excluded from being pushed to this history stack."

4. **Implement Navigation Stack (`st.screenHistory`):**
   - In `st` object definition, add `screenHistory: []`.
   - In `showScreen(id)`, implement the push logic (excluding loading states):
     ```javascript
     if (st.screen && !st.screen.includes('loading') && st.screen !== id) {
       st.screenHistory.push(st.screen);
     }
     st.screen = id;
     ```
   - Actually, a back function like `goBack()` would be better:
     ```javascript
     function goBack() {
       if (st.screenHistory.length > 0) {
         const prev = st.screenHistory.pop();
         ['s-loading','s-location','s-nbhd','s-app'].forEach(s => {
           const el = document.getElementById(s);
           if (el) el.hidden = (s !== prev);
         });
         st.screen = prev;
       } else {
         showScreen('s-location'); // fallback
       }
     }
     ```
   - Update `btnNbhdBack` event listener to use `goBack()` instead of hardcoding `showScreen('s-location')`.
   - Update `showScreen` function to modify `.hidden` of screens and set `st.screen = id;`, but wait, we need to push to history if we want to come back. "When implementing back navigation, pop the previous view from this stack (falling back to 's-location' if empty) rather than hardcoding targets. Ensure initial loading states ('loading', 's-loading') are explicitly excluded from being pushed to this history stack."

5. **Modify `showScreen(id)`:**
   ```javascript
   function showScreen(id) {
     if (st.screen && !st.screen.includes('loading') && st.screen !== id) {
       st.screenHistory.push(st.screen);
     }
     ['s-loading','s-location','s-nbhd','s-app'].forEach(s => {
       const el = document.getElementById(s);
       if (el) el.hidden = (s !== id);
     });
     st.screen = id;
   }

   function goBack() {
     const prev = st.screenHistory.length ? st.screenHistory.pop() : 's-location';
     ['s-loading','s-location','s-nbhd','s-app'].forEach(s => {
       const el = document.getElementById(s);
       if (el) el.hidden = (s !== prev);
     });
     st.screen = prev;
   }
   ```
   Wait, if `goBack()` is called, we don't want to call `showScreen` again because that would push the current screen onto the history stack. So we manipulate DOM directly or pass a flag.

6. **Escape Handler logic:**
   ```javascript
    /* Escape handling */
    if (e.key === 'Escape') {
      e.preventDefault();
      if (st.screen === 's-nbhd') {
        goBack();
      } else if (st.screen === 's-app' && st.tab === 'explore' && !document.getElementById('exploreDetail').hidden) {
        closeCollection();
      } else if (st.openId !== null) {
        toggleItem(st.openId);
      }
      return;
    }
   ```

7. **Execute plan verification (Visual check via Playwright):**
   - Write a Playwright script `verify_escape.py` that clicks around to open `s-nbhd`, explore detail, and an item, and presses Escape, taking screenshots and asserting states.
   - Run verification.

8. **Pre-commit and submit.**
