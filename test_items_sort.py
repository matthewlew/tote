from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:3000')
        page.click("text=Jason's Coffee")
        page.wait_for_selector('.row')

        # Click sort by type
        page.keyboard.press('t')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_type.png')

        # Click sort by title
        page.keyboard.press('n')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_title.png')

        # Click locate me then sort by distance
        page.keyboard.press('d')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_distance.png')

        browser.close()

run()
