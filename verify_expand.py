import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000')

        await page.wait_for_selector('#btnBrowseNbhd', state='visible', timeout=10000)
        await page.click('#btnBrowseNbhd')

        # Click "Williamsburg" (visible button [4])
        await page.locator('button:has-text("Williamsburg")').click()

        await page.wait_for_selector('.p-row')

        # click the first row
        first_row = page.locator('.p-row').first
        await first_row.click()
        await page.wait_for_timeout(500)

        await page.screenshot(path='screenshot_expanded.png', full_page=False)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
