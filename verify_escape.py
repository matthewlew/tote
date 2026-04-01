from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:3000')

        # Wait for loading to finish
        page.locator("#s-loading").wait_for(state="hidden")

        # Start on location screen -> click 'Browse by neighborhood' -> go to neighborhood screen
        page.click('#btnBrowseNbhd')
        page.locator('#s-nbhd').wait_for(state='visible')
        print("At Nbhd Screen")
        page.screenshot(path='/home/jules/verification/escape_1_nbhd.png')

        # Press Escape -> should go back to location screen
        page.keyboard.press('Escape')
        page.locator('#s-location').wait_for(state='visible')
        print("At Location Screen (via Escape)")
        page.screenshot(path='/home/jules/verification/escape_2_loc.png')

        # Go back to nbhd, click an item to go to app screen
        page.click('#btnBrowseNbhd')
        page.locator('#s-nbhd').wait_for(state='visible')
        page.click('.nbhd-item')
        page.locator('#s-app').wait_for(state='visible')
        print("At App Screen")

        # Open an item row
        page.click('.p-row')
        page.locator('.place.open').wait_for(state='visible')
        print("Item opened")
        page.screenshot(path='/home/jules/verification/escape_3_item_open.png')

        # Press Escape -> should close item row
        page.keyboard.press('Escape')
        page.locator('.place.open').wait_for(state='hidden')
        print("Item closed (via Escape)")
        page.screenshot(path='/home/jules/verification/escape_4_item_closed.png')

        # Go to explore tab
        page.click('button[data-tab="explore"]')
        page.locator('#exploreIndex').wait_for(state='visible')

        # Open a collection
        page.click('.coll-card')
        page.locator('#exploreDetail').wait_for(state='visible')
        print("Collection opened")
        page.screenshot(path='/home/jules/verification/escape_5_coll_open.png')

        # Press Escape -> should close collection
        page.keyboard.press('Escape')
        page.locator('#exploreIndex').wait_for(state='visible')
        print("Collection closed (via Escape)")
        page.screenshot(path='/home/jules/verification/escape_6_coll_closed.png')

        # Go back to list -> change location -> open nbhd screen
        page.click('button[data-tab="list"]')
        page.click('#btnChangeLoc')
        page.locator('#s-nbhd').wait_for(state='visible')
        print("At Nbhd Screen (from App Screen)")

        # Press Escape -> should go back to App Screen
        page.keyboard.press('Escape')
        page.locator('#s-app').wait_for(state='visible')
        print("At App Screen (via Escape)")
        page.screenshot(path='/home/jules/verification/escape_7_app.png')

        browser.close()

run()
