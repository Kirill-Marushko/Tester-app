import requests
from bs4 import BeautifulSoup

r = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(r.content, "html.parser")

lst1 = []
for data in soup.select(".text"):
    y = data.text
    lst1.append(y)

lst2 = []
for data in soup.select(".author"):
    s = data.text
    lst2.append(s)

x = {}
for index, i in enumerate(lst1):
    x[i] = lst2[index]
print(lst1, lst2)
