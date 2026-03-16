from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(2000)
        page.click('#btnBrowseNbhd')
        page.wait_for_timeout(500)
        page.click('.nbhd-item') # click first neighborhood
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshot.png')
        browser.close()

run()
