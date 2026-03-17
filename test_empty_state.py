from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(2000)

        # Bypass location screen
        page.click('button:has-text("Browse by neighborhood")')
        page.wait_for_timeout(500)

        # Click "Williamsburg"
        page.click('button:has-text("Williamsburg")')
        page.wait_for_timeout(500)

        # Click a category filter that might be empty, or just clear data to force empty state
        page.evaluate("localStorage.clear(); PLACES = []; renderList();")
        page.wait_for_timeout(500)

        page.screenshot(path='screenshot_empty_state.png')

        # Click the Import Places CTA
        page.click('#btnEmptyImport')
        page.wait_for_timeout(500)

        page.screenshot(path='screenshot_after_empty_cta.png')

        browser.close()

run()
