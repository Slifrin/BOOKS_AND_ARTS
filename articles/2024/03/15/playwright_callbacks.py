import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.expose_binding("pageURL", lambda source: source["page"].url)
    await page.set_content(
        """
    <script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    </script>
    <button onclick="onClick()">Click me</button>
    <div></div>
    """
    )
    await page.click("button")


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
