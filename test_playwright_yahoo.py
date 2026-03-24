from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Starting browser...")

    browser = p.chromium.launch(
        headless=False    )

    # 連往yahoo
    page = browser.new_page()
    page.goto(
        "https://tw.yahoo.com/",
        wait_until="domcontentloaded"
       )
    page.wait_for_timeout(3000)

titles = page.locator("h3").all_text_contents()

for i, title in enumerate(titles[:10], 1):
    print(i, title)

    # print("Title:", page.title())

    browser.close()