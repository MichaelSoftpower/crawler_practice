import requests
from bs4 import BeautifulSoup

url = "https://stage2.friendlysky.com/"

session = requests.Session()

headers = {
    "Cookie": "sessionid=59ccfc76-99f7-49f6-bceb-844423261136"
}

requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print(response.text)