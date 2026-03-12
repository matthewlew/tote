from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(500)

        # Press 'ArrowDown' two times to land on Bennett Winch Tote (which has a BUY link)
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(100)
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_navigate_with_link.png')

        browser.close()

run()
