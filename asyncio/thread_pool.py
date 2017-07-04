import asyncio
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue

thread_pool = ThreadPoolExecutor(max_workers=20)
loop = asyncio.get_event_loop()
queue = Queue()

async def feed():
    for i in range(10):
        print(f"Recieved {i} on thread {threading.current_thread()}")
        queue.put(i)
        loop.run_in_executor(thread_pool, upload)
        await asyncio.sleep(1)

def upload():
    value = queue.get()
    print(f"Uploading {value} on thread {threading.current_thread()}")
    time.sleep(10)
    print(f"Upload {value} completed on thread {threading.current_thread()}")

asyncio.ensure_future(feed())
loop.run_forever()
