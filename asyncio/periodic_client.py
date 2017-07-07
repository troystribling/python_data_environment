import asyncio
import aiohttp

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)

async def fetch_page():
    with aiohttp.Timeout(10):
        async with session.get('https://poloniex.com/public?command=return24hVolume') as response:
            assert response.status == 200
            return await response.read()

async def poll():
    while True:
        content = await fetch_page()
        print(content)
        await asyncio.sleep(10)

loop.run_until_complete(poll())
