from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(2000)

        # Press 'l' for location
        page.keyboard.press('l')
        page.wait_for_timeout(500)

        # Make sure that down arrow actually focuses the element
        # (needs `focus-visible` styles)
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(200)
        page.screenshot(path='screenshot_focus_1.png')

        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(200)
        page.screenshot(path='screenshot_focus_2.png')

        browser.close()

run()
