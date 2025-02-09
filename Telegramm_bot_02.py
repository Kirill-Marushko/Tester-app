# 3 функції, 1 буде робити запит на тренувальний сервер,
# друга функція буде робити запит на auto ria і знаходити всі назви та формує їх у якості списку,
# і третя яка буде писати вітання,
# та після буде спати 2 секунди, та після цього напише допобачення

import asyncio
import requests
from bs4 import BeautifulSoup


async def a():
    h = requests.get("https://quotes.toscrape.com/")
    print(h)


async def b():
    r = requests.get("https://auto.ria.com/search/?categories.main.id=1&price.currency=1&indexName=auto,order_auto,newauto_search&brand.id[0]=118&model.id[0]=3108&year[0].gte=2019&year[0].lte=2024&size=20")
    soup = BeautifulSoup(r.content, "html.parser")
    lst1 = []
    for data in soup.select(".head-ticket"):
        y = data.text
        lst1.append(y)
    print(lst1)


async def c():
    print("Добрий день!!!")
    await asyncio.sleep(2)
    print("Допобачення!!!")


async def main(loop):
    f1 = loop.create_task(a())
    f2 = loop.create_task(b())
    f3 = loop.create_task(c())
    await asyncio.wait([f1, f2, f3])

loop = asyncio.new_event_loop()
loop.run_until_complete(main(loop))
loop.close()
