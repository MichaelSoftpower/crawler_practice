import requests

login_url = "https://example.com/login"
data_url = "https://example.com/dashboard"

session = requests.Session()

# 登入資料
payload = {
    "username": "your_account",
    "password": "your_password"
}

# 送登入 request
session.post(login_url, data=payload)

# 再抓資料（帶著登入狀態）
response = session.get(data_url)

print(response.text)