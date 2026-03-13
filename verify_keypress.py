from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(500)

        # Press 'ArrowRight'
        page.keyboard.press('ArrowRight')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_after_keypress_1.png')

        # Press 'ArrowDown' multiple times to focus a row
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(100)
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_after_keypress_2.png')

        browser.close()

run()
