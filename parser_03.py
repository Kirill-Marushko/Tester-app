import requests
from bs4 import BeautifulSoup

r = requests.get("https://auto.ria.com/search/?categories.main.id=1&price.currency=1&indexName=auto,order_auto,newauto_search&brand.id[0]=118&model.id[0]=3108&year[0].gte=2019&year[0].lte=2024&size=20")
soup = BeautifulSoup(r.content, "html.parser")

lst1 = []
for data in soup.select(".price-ticket"):
    y = data.text
    lst1.append(y)

for i in lst1:
    print(i[3:9])

price1 = []
int_price = []
for price in price1:
    int_price.append(int(price))
x = sum(int_price) // len(int_price)
price1.append(x)
print(price1)
