import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:3000')

        # Click "Williamsburg" (visible button [4])
        await page.locator('button:has-text("Williamsburg")').click()

        await page.wait_for_selector('.row')

        # click the first row
        first_row = page.locator('.row').first
        await first_row.click()
        await page.wait_for_timeout(500)

        await page.screenshot(path='screenshot_expanded.png', full_page=False)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
