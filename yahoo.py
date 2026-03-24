import requests
from bs4 import BeautifulSoup

url = "https://tw.news.yahoo.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("h3")

for i, title in enumerate(titles[:10], 1):
    print(i, title.text.strip())