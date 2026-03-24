import requests
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Starting browser...")

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()
    page.goto(
        "https://stage2.friendlysky.com/",
        wait_until="domcontentloaded"
    )

    page.fill("input[name=username]", "michael.lin@friendlysky.com")    
    page.fill("input[name=password]", "!Softpower123")
    page.click("button[type=submit]")

    page.wait_for_load_state("networkidle")

    print("Current URL:", page.url)

    page.get_by_text("Training").click()

    page.goto(
        "https://stage2.friendlysky.com/bos/#/events",
        wait_until="domcontentloaded"
    )

    input("Press Enter to exit")
