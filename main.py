import requests
from bs4 import BeautifulSoup

# 目標網站
url = "https://news.ycombinator.com/"

# 發送請求
response = requests.get(url)

# 解析 HTML
soup = BeautifulSoup(response.text, "html.parser")

# 找標題
titles = soup.select(".titleline > a")

# 印出結果
for i, title in enumerate(titles[:10], 1):
    print(f"{i}. {title.text}")