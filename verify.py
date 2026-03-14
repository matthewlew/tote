from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.evaluate("() => { const cats = document.querySelectorAll('.category-btn'); if(cats.length > 3) cats[3].click(); }")
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshot.png')
        browser.close()

run()
