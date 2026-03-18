from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--allow-running-insecure-content", "--unsafely-treat-insecure-origin-as-secure=http://localhost:3000"])
        context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'])
        page = context.new_page()
        page.goto('http://localhost:3000')
        page.wait_for_timeout(2000)

        # Press 'l' for location
        page.keyboard.press('l')
        page.wait_for_timeout(500)

        page.screenshot(path='screenshot_shortcuts_initial.png')

        # Press 'n' to sort by name
        page.keyboard.press('n')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_shortcuts_sort_name.png')

        # Press 't' to sort by type
        page.keyboard.press('t')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_shortcuts_sort_type.png')

        # Press 'r' for random pick
        page.keyboard.press('r')
        page.wait_for_timeout(500)
        page.screenshot(path='screenshot_shortcuts_random_pick.png')

        # Press 'c' to copy
        page.keyboard.press('c')
        page.wait_for_timeout(500)

        # We can't easily verify clipboard content visually, but we can check if it didn't crash

        browser.close()

run()
