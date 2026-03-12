from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(500)

        # Press '2'
        page.keyboard.press('2')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_after_keypress.png')

        browser.close()

run()
