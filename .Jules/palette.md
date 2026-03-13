## 2026-03-12 - Accessibility Audit of Tote Navigation & Lists
**Learning:** The brutalist text-only aesthetic of Tote hid interactive states (`aria-hidden` on sort headers) and lacked focus outlines (`focus-visible` missing), making keyboard navigation impossible to track. Dynamic content loading via category switching was invisible to screen readers without `aria-live`.
**Action:** Always ensure visually raw designs maintain standard keyboard focus rings (using the existing `var(--accent)`) and check that interactive headers are properly exposed to the accessibility tree. Apply `aria-live` to dynamic data lists.

## 2026-03-12 - Screen Reader Focus Trap in Brutalist UI
**Learning:** Found an accessibility anti-pattern where a container (`.header-row`) used `aria-hidden="true"` while containing interactive `<button>` elements inside it. This hides the buttons from screen readers but leaves them in the keyboard tab order, creating a disorienting "invisible" focus trap for keyboard + screen reader users. The brutalist design choice of "hidden headers" shouldn't come at the cost of screen reader functionality.
**Action:** Always verify that elements containing interactive children (like buttons or links) never use `aria-hidden="true"`. Instead, use semantic structural attributes like `role="group"` and `aria-label` to provide context while keeping the interactive elements accessible to assistive tech.

## 2025-03-13 - Keyboard Navigation in Custom List Items
**Learning:** When building custom list components (like `.row` elements) without semantic `<ul>` and `<li>` structure, it is crucial to explicitly manage focus. Setting `tabindex="0"` programmatically allows them to receive keyboard focus, but users are left lost if the `focus-visible` states do not match or align closely with the mouse `:hover` states, ensuring parity of experience. Arrow key support dramatically speeds up navigation vs. repeatedly pressing `Tab`.
**Action:** Always replicate or mirror `hover` styles onto `focus-visible` for list items, explicitly set `tabindex` on interactable custom rows, and bind arrow key navigation alongside visual keyboard shortcut hints in the UI.
