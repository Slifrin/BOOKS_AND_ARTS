import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # launch the browser
        browser = await p.chromium.launch()
        # open a new page
        page = await browser.new_page()

        # visit the target page
        await page.goto("https://arh.antoinevastel.com/bots/areyouheadless")

        # extract the answer contained on the page
        answer_element = page.locator("#res")
        answer = await answer_element.text_content()

        # print the resulting answer
        print(f'The result is: "{answer}"')

        # close the browser and release its resources
        await browser.close()

asyncio.run(main())