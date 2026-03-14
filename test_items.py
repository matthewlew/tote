from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.click("text=Jason's Coffee")
        page.wait_for_selector('.row')
        page.screenshot(path='screenshot.png')
        browser.close()

run()
