import requests
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Starting browser...")

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()
    page.goto("https://stage2.friendlysky.com/")
    # page.pause()

    
login_url = "https://stage2.friendlysky.com/login"
data_url = "https://stage2.friendlysky.com/bos/#/sites"

payload = {
    "username": "michael.lin@friendlysky.com",
    "password": "!Softpower123"
}
session = requests.Session()

res = session.post(login_url, data=payload)


# print(response.url)
print(session.cookies)
# print(response.text)

# login_url = "https://example.com/login"
# data_url = "https://example.com/dashboard"

# session = requests.Session()

# 登入資料
# payload = {
#     "username": "your_account",
#     "password": "your_password"
# }

# 送登入 request
# session.post(login_url, data=payload)

# 再抓資料（帶著登入狀態）
# response = session.get(data_url)

# print(response.text)