from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={'width': 414, 'height': 896}) # Mobile sizing
        page = context.new_page()
        page.goto('http://localhost:3000')
        page.screenshot(path='screenshot_mobile.png')
        browser.close()

run()
