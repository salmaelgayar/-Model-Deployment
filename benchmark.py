import asyncio
import aiohttp
import time

URL = "http://localhost:8000/generate"


async def worker(session, i):

    payload = {
        "prompt": f"Explain machine learning {i}"
    }

    start = time.time()

    async with session.post(URL, json=payload) as response:

        await response.text()

    end = time.time()

    return end - start


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = [
            worker(session, i)
            for i in range(10)
        ]

        results = await asyncio.gather(*tasks)

    print(results)

    print("Average:", sum(results)/len(results))


asyncio.run(main())
