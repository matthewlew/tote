from playwright.sync_api import sync_playwright, expect

def test_escape():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={'width': 800, 'height': 800})
        page = context.new_page()
        page.goto("http://127.0.0.1:3000")

        # Wait for loading screen to disappear
        expect(page.locator("#s-loading")).not_to_be_visible()

        # Location screen -> App
        page.locator("#btnEnableLoc").click()
        expect(page.locator("#s-app")).to_be_visible()

        # 1. Test expanding row and pressing Escape
        row = page.locator(".place").first
        row.click()
        expect(row).to_have_class("place animate-in open")
        page.keyboard.press("Escape")
        expect(row).not_to_have_class("place animate-in open")
        expect(row).to_have_class("place animate-in")

        # 2. Test neighborhood modal and pressing Escape
        page.locator("#btnChangeLoc").click()
        expect(page.locator("#s-nbhd")).to_be_visible()

        # Screenshot the neighborhood modal back button
        page.screenshot(path="/home/jules/verification/nbhd_escape.png")

        page.keyboard.press("Escape")
        expect(page.locator("#s-app")).to_be_visible()

        # 3. Test explore collection detail and pressing Escape
        page.keyboard.press("ArrowRight") # explore
        expect(page.locator("#exploreIndex")).to_be_visible()

        coll = page.locator(".coll-card").first
        coll.click()
        expect(page.locator("#exploreDetail")).to_be_visible()

        # Screenshot the collection back button
        page.screenshot(path="/home/jules/verification/coll_escape.png")

        page.keyboard.press("Escape")
        expect(page.locator("#exploreIndex")).to_be_visible()

        print("All escape dismissals verified!")
        browser.close()

if __name__ == "__main__":
    test_escape()
