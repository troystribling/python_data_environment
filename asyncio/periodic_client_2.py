import asyncio
import aiohttp
from time import time

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)

poll_interval = 30.0
currency_pair = 'BTC_ETH'

async def fetch_page(url):
    with aiohttp.Timeout(10):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.read()

async def poll():
    end_time = time()
    while True:
        url = f'https://poloniex.com/public?command=returnTradeHistory&currencyPair={currency_pair}&start={end_time - poll_interval}&end={end_time}'
        print(url)
        end_time += poll_interval
        content = await fetch_page(url)
        print(content)
        await asyncio.sleep(poll_interval)

loop.run_until_complete(poll())
