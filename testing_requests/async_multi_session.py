import aiohttp
import asyncio
from testing_requests import time_decoratos as td


async def get_async(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


@td.time_check_async
async def multi_session(urls: list[str]):
    await asyncio.gather(*map(get_async, urls))

