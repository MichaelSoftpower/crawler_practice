
from playwright.sync_api import sync_playwright

p = None
browser = None
page = None

def start_browser(base_url):
    
    global p, browser, page
    
    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()
    page.goto(
        base_url,
        wait_until="domcontentloaded"
    )
    return page


def close_browser():

    global browser, p

    if browser:
        browser.close()

    if p:
        p.stop()
