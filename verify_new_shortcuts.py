from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(500)

        # Press 't' to sort by title
        page.keyboard.press('t')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_sort_t.png')

        # Press 'p' to sort by price
        page.keyboard.press('p')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_sort_p.png')

        # Press 'b' to sort by brand
        page.keyboard.press('b')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_sort_b.png')

        browser.close()

run()
