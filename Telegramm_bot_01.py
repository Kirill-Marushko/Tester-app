import asyncio


async def a():
    print(1)
    await asyncio.sleep(4)
    print(2)


async def b():
    print(3)
    await asyncio.sleep(5)
    print(4)


async def c():
    print(5)
    await asyncio.sleep(3)
    print(6)


async def main(loop):
    f1 = loop.create_task(a())
    f2 = loop.create_task(b())
    f3 = loop.create_task(c())
    await asyncio.wait([f1, f2, f3])


loop = asyncio.new_event_loop()
loop.run_until_complete(main(loop))
loop.close()