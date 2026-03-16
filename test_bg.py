from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={'width': 1200, 'height': 800})
        page = context.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(2000)
        page.screenshot(path='screenshot_bg_2.png', full_page=True)
        browser.close()

run()
