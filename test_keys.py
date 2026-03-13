from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(500)

        # Press ArrowDown
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_arrow_down.png')

        # Press ArrowRight
        page.keyboard.press('ArrowRight')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_arrow_right.png')

        browser.close()

run()
