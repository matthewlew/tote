import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000')

        # wait for initial screen to load
        await page.wait_for_selector('#btnBrowseNbhd', state='visible')

        # Click browse by neighborhood
        await page.locator('#btnBrowseNbhd').click()

        # wait for neighborhood list to load
        await page.wait_for_selector('.nbhd-item:has-text("Williamsburg")')

        # Click "Williamsburg"
        await page.locator('.nbhd-item:has-text("Williamsburg")').click()

        await page.wait_for_selector('.place')

        # click the first row
        first_row = page.locator('.place').first
        await first_row.click()
        await page.wait_for_timeout(500)

        await page.screenshot(path='screenshot_expanded.png', full_page=False)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
