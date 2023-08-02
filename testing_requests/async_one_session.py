import asyncio
import aiohttp
from testing_requests import time_decoratos as td


async def get_async_diff(session, url):
    async with session.get(url) as request:
        return request


@td.time_check_async
async def one_session_check(urls: list[str]):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*map(lambda x: get_async_diff(session, x), urls))
