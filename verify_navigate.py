from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(500)

        # Press 'ArrowDown' three times
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(100)
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(100)
        page.keyboard.press('ArrowDown')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_navigate.png')

        browser.close()

run()
