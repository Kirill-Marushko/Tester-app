import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.redbullracing.com/int-en/races")
soup = BeautifulSoup(r.content, "html.parser")

for data in soup.select(".driver_name__nFGy_"):
    print(data.text)
