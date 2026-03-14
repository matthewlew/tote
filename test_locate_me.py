from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Mocking location to some coordinate in NYC
        context = browser.new_context(
            permissions=['geolocation'],
            geolocation={'latitude': 40.7128, 'longitude': -74.0060}
        )
        page = context.new_page()
        page.goto('http://localhost:3000')

        page.click("text=Jason's Coffee")
        page.wait_for_selector('.row')

        # Click locate me
        page.click("text=Locate Me")
        page.wait_for_timeout(1000)

        # Take screenshot of distance values
        page.screenshot(path='screenshot_located.png')

        browser.close()

run()
