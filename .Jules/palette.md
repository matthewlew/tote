## 2026-03-12 - Accessibility Audit of Tote Navigation & Lists
**Learning:** The brutalist text-only aesthetic of Tote hid interactive states (`aria-hidden` on sort headers) and lacked focus outlines (`focus-visible` missing), making keyboard navigation impossible to track. Dynamic content loading via category switching was invisible to screen readers without `aria-live`.
**Action:** Always ensure visually raw designs maintain standard keyboard focus rings (using the existing `var(--accent)`) and check that interactive headers are properly exposed to the accessibility tree. Apply `aria-live` to dynamic data lists.

## 2025-03-13 - Keyboard Navigation in Custom List Items
**Learning:** When building custom list components (like `.row` elements) without semantic `<ul>` and `<li>` structure, it is crucial to explicitly manage focus. Setting `tabindex="0"` programmatically allows them to receive keyboard focus, but users are left lost if the `focus-visible` states do not match or align closely with the mouse `:hover` states, ensuring parity of experience. Arrow key support dramatically speeds up navigation vs. repeatedly pressing `Tab`.
**Action:** Always replicate or mirror `hover` styles onto `focus-visible` for list items, explicitly set `tabindex` on interactable custom rows, and bind arrow key navigation alongside visual keyboard shortcut hints in the UI.

## 2026-03-14 - Interactive Expand/Collapse in Custom Lists
**Learning:** When converting simple `div` elements into interactive list items that expand or collapse on click, setting `tabindex="0"` is not enough for screen reader accessibility. Users with assistive technologies have no indication that the element is interactable or what its current state is. Furthermore, relying only on mouse click events completely breaks the experience for keyboard-only users who expect `Space` or `Enter` to trigger the interaction.
**Action:** Always add `role="button"` and `aria-expanded="false"` attributes to custom interactive rows when created. Ensure event listeners that toggle the visual state (like a CSS `expanded` class) also toggle the `aria-expanded` boolean. Explicitly bind `Space` (and optionally `Enter` if it doesn't conflict with link navigation) to trigger this toggle programmatically for keyboard users while preventing default page scrolling.

## 2026-03-15 - Screen Reader Verbosity on Dynamic Lists
**Learning:** Applying `aria-live="polite"` directly to a large list container (`#list`) causes screen readers to read out the entire contents of the new list every time it changes (e.g. during sorting, changing categories). This results in overwhelming verbosity and makes navigation difficult.
**Action:** Remove `aria-live` from the list container itself and instead apply `aria-live="polite" aria-atomic="true"` to a concise summary element (like the total item count `span#hd-n`). This provides the user with an immediate, succinct status update while letting them explore the list content at their own pace.

## 2026-03-17 - Actionable Empty States
**Learning:** Empty list states (like the "Nothing in this category" view) without direct call-to-actions create dead-ends for the user. When users are told what they *could* do (e.g., "Add places from your Google Maps list"), forcing them to manually discover how to do so (by hunting for the Import tab) adds friction to the onboarding flow.
**Action:** Always provide an explicit, actionable Call-To-Action (CTA) button directly within empty state containers to route users smoothly to the solution, using existing UI components like `.bt-add`.

## 2025-03-24 - Global Escape Key Navigation
**Learning:** When adding keyboard navigation, providing an "Escape" hatch to dismiss the current view or return to the previous screen is a crucial accessibility expectation. However, hardcoding the "Back" button's destination (e.g., returning from a global modal like the Neighborhood Picker always to the Location screen) creates frustrating dead-ends.
**Action:** Implement an explicit history stack (e.g., `st.screenHistory`) to track the user's previous view state and pop the stack to dynamically navigate back. Bind the 'Escape' key globally to dismiss the most specific open state first (expanded row > sub-view > main view), matching natural user expectations.
