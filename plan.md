1. **Optimize `isSavedPlace` in `index.html`**
   - Precompute an O(1) cache (`Set`) of normalized saved place names before looping through `coll.places` in `renderCollectionDetail` to prevent O(N*M) nested array searches.
   - Refactor `renderCollectionDetail` to create a `savedPlaceNames` Set.
   - Modify the inline calls to `isSavedPlace(p.name)` inside `renderCollectionDetail` to use the precomputed `savedPlaceNames.has(norm(p.name))`.
2. **Verify Changes**
   - Run a `git diff` to verify the edit exactly matches the intention.
3. **Run Linting & Tests**
   - Ensure the tests still pass successfully using Playwright tests `python3 verify.py`, etc.
4. **Complete pre commit steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
