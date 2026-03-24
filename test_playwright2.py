from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Starting browser...")

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()

    page.goto("https://playwright.dev/")
    
    page.get_by_role("link", name="Get started").click()
    
    # expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    # print("Title:", page.title())
