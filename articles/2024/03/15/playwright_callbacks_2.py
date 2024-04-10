import asyncio
import hashlib
from playwright.async_api import async_playwright, Playwright


def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    print(f"Hello from sha256 -- {text}")
    return m.hexdigest()


async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    page = await browser.new_page()
    await page.expose_function("sha256", sha256)
    await page.set_content(
        """
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
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
