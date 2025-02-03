# зробити словник, де ключом буде автор, а значенням вислів, якщо у автора не один вислів,
# то переробити значення на список, та додати у цей список ще один вислів

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
for index, i in enumerate(lst2):
    lst2[i] = lst1[index]
print(lst1, lst2)
