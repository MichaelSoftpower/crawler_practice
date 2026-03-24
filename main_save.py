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

with open("news.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title.text + "\n")