from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        # Select superlative
        page.select_option('#superlative-select', value='dive_bars') # Or whatever superlative exists
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshot_empty.png')
        browser.close()

run()
