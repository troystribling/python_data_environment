import signal
import sys
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)

async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit, client):
    url = 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5'
    response = await get_json(client, url)
    results = json.loads(response.decode('utf-8'))
    for result in results['data']['children']:
        score = result['data']['score']
        title = result['data']['title']
        link = result['data']['url']
        print(f"{score}: {title} ({link})")
    print(f"DONE {subreddit}\n")

def signal_handler(signal, frame):
    print("Recieved exit")
    loop.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

loop.run_until_complete(asyncio.gather(get_reddit_top('python', client),
                                       get_reddit_top('programming', client),
                                       get_reddit_top('compsci', client)))
client.close()
loop.close()
